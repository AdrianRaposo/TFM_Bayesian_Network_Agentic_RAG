# MARGINS OF DISCRETE BAYESIAN NETWORKS 

By Robin J. Evans<br>University of Oxford


#### Abstract

Bayesian network models with latent variables are widely used in statistics and machine learning. In this paper, we provide a complete algebraic characterization of these models when the observed variables are discrete and no assumption is made about the state-space of the latent variables. We show that it is algebraically equivalent to the so-called nested Markov model, meaning that the two are the same up to inequality constraints on the joint probabilities. In particular, these two models have the same dimension, differing only by inequality constraints for which there is no general description. The nested Markov model is therefore the closest possible description of the latent variable model that avoids consideration of inequalities. A consequence of this is that the constraint finding algorithm of Tian and Pearl [In Proceedings of the 18th Conference on Uncertainty in Artificial Intelligence (2002) $519-527]$ is complete for finding equality constraints.

Latent variable models suffer from difficulties of unidentifiable parameters and nonregular asymptotics; in contrast the nested Markov model is fully identifiable, represents a curved exponential family of known dimension, and can easily be fitted using an explicit parameterization.


1. Introduction. Directed acyclic graph (DAG) models, also known as Bayesian network models, are widely used multivariate models in probabilistic reasoning, machine learning and causal inference [Bishop (2007), Darwiche (2009), Pearl (2009)]. These models are defined by simple factorizations of the joint distribution, and in the case of discrete or jointly Gaussian random variables, are curved exponential families of known dimension. The inclusion of latent variables within Bayesian network models can greatly increase their flexibility, and also account for unobserved confounding. However, this flexibility comes at the cost of creating models that are not easy to explicitly describe when considered as marginal models over the observed variables. Latent variable models generally do not have fully identifiable parameterizations [Allman, Matias and Rhodes (2009)], and contain "singularities" that lead to nonregular asymptotics [Drton (2009)]. In addition, using them may force a modeller to specify a parametric structure over the latent variables, introducing additional assumptions that are generally difficult to test and may be unreasonable.
[^0]
[^0]:    Received January 2017; revised August 2017.
    MSC2010 subject classifications. 62H99, 62F12.
    Key words and phrases. Algebraic statistics, Bayesian network, latent variable model, nested Markov model, Verma constraint.

![img-0.jpeg](img-0.jpeg)

Fig. 1. A directed acyclic graph on five vertices.

In order to avoid potentially erroneous assumptions about the parametric structure of the latent variables or their state-space, we can use an implicitly defined marginal model. However, no explicit characterization of this model is available, nor is there any obvious method for fitting it to data.

Example 1.1. Consider the DAG on five vertices shown in Figure 1. The graph represents a multivariate model over five random variables $X_{0}, X_{1}, X_{2}, X_{3}$ and $X_{4}$, with the restriction that the joint density factorizes as

$$
p\left(x_{0}, x_{1}, x_{2}, x_{3}, x_{4}\right)=p\left(x_{0}\right) \cdot p\left(x_{1}\right) \cdot p\left(x_{2} \mid x_{0}, x_{1}\right) \cdot p\left(x_{3} \mid x_{2}\right) \cdot p\left(x_{4} \mid x_{0}, x_{3}\right)
$$

here, for example, $p\left(x_{3} \mid x_{2}\right)$ represents the conditional density of $X_{3}$ given $X_{2}$. This model arises naturally in the context of dynamic treatment regimes and longitudinal exposures [Robins (1986)]: $X_{1}$ and $X_{3}$ represent treatments and $X_{2}$ and $X_{4}$ some outcome of interest. The treatments are randomized, though the second treatment $X_{3}$ may depend upon the first outcome $X_{2}$, for example, a dose may be dynamically adjusted. Since the outcomes are measured on the same patient, they are assumed to be correlated due to a common cause $X_{0}$, which might represent an underlying health status, as well as genetic and lifestyle factors.

If we treat $X_{0}$ as a latent variable, the marginal model over the remaining observed variables $\left(X_{1}, X_{2}, X_{3}, X_{4}\right)$ is the collection of probability distributions that can be written in the form

$$
\begin{aligned}
& p\left(x_{1}, x_{2}, x_{3}, x_{4}\right) \\
& \quad=\int_{X_{0}} p\left(x_{0}\right) \cdot p\left(x_{1}\right) \cdot p\left(x_{2} \mid x_{0}, x_{1}\right) \cdot p\left(x_{3} \mid x_{2}\right) \cdot p\left(x_{4} \mid x_{0}, x_{3}\right) d x_{0}
\end{aligned}
$$

That is, the model consists of any $\left(X_{1}, X_{2}, X_{3}, X_{4}\right)$-margin of a distribution which factorizes according to the DAG over all five variables, for any state-space or distribution ${ }^{1}$ of $X_{0}$. From (1), we can deduce that the conditional independence $X_{3} \Perp X_{1} \mid X_{2}$ holds in the marginal model; that is,

$$
p\left(x_{3} \mid x_{1}, x_{2}\right)=p\left(x_{3} \mid x_{2}\right)
$$

[^0]
[^0]:    ${ }^{1}$ In general, it is sufficient to assume hidden variables are uniform on $(0,1)$ [see, for example, Evans (2016)]; for this particular graph, it is a consequence of Theorem 4.7 that we can choose $X_{0}$ to be finite and discrete without loss of generality provided it has a sufficiently large number of states.

In addition, this model satisfies the so-called Verma constraint, originally due to Robins (1986) [see also Verma and Pearl (1990)], because the expression

$$
q\left(x_{4} \mid x_{3}\right) \equiv \sum_{x_{2}} p\left(x_{2} \mid x_{1}\right) \cdot p\left(x_{4} \mid x_{1}, x_{2}, x_{3}\right)
$$

does not depend upon $x_{1}$ (see Example 3.2).
The set of distributions satisfying both (2) and (3) is a so-called nested Markov model [Richardson et al. (2017)]. If the four observed variables are binary, these equations represent four independent constraints, and the nested model is an 11dimensional subset of the 15 -dimensional probability simplex.

It is not immediately clear whether or not this nested model is the same as the marginal model defined by (1): in principle the marginal model might impose additional restrictions beyond (2) and (3). This begs the question: Is the set of distributions that satisfy (1) characterized by (2) and (3)?

The answer turns out to be "almost", in the sense that the set of distributions that can be written in the form (1) is a full-dimensional subset of the set that satisfy (2) and (3), though there are additional inequality constraints. This situation is represented by Figure 2, which shows the marginal model ( $\mathcal{M}$, in blue) lying strictly within the nested model ( $\mathcal{N}$, in red), but the two having the same dimension.

This paper shows that this near-equivalence between the marginal and nested models holds generally for all graphs of this kind. Nested models in general are defined by conditional independences such as (2), and Verma-type constraints such as (3). These latter constraints may always be interpreted as a conditional independence that holds under a different experimental regime to the one observed: in the example above, it implies that if we intervene to perform an experiment that sets $\left\{X_{1}=x_{1}, X_{3}=x_{3}\right\}$ then the resulting distribution of the final outcome $X_{4}$ does not causally depend upon the value of the first treatment, $x_{1}$.
1.1. Other approaches. Alternative approaches to the problem of describing Bayesian network models with hidden variables either make use of parametric structure on the latent variables [e.g., Silva and Ghahramani (2009), Anandkumar et al. (2013)], or are restricted to testing conditional independences and do not consider constraints such as (3). This latter category includes the ancestral graph models of Richardson and Spirtes (2002) and the equivalent ${ }^{2}$ models on acyclic directed mixed graphs (ADMGs) of Richardson (2003); these pure conditional independence models, which we refer to as the ordinary Markov models, generally have a larger dimension than the observable part of any latent variable model, so using them as a proxy leads to a loss of power to distinguish between certain kinds of model.

[^0]
[^0]:    ${ }^{2}$ The models are equivalent if selection variables are not present, which is the case throughout this paper.

![img-1.jpeg](img-1.jpeg)

FIG. 2. Diagrammatic representation of the probability simplex (dashed outline) and a marginal model ( $\mathcal{M}$, in blue) sitting strictly within the associated nested model ( $\mathcal{N}$, in red); note the two models have the same dimension. The boundary of $\mathcal{N}$ is in the simplex boundary, while that of $\mathcal{M}$ is given by inequalities which are generally unknown. Any parametric latent variable model will be contained strictly within $\mathcal{M}$, but it may have a smaller dimension (an example is shown as $\mathcal{L}$ ). The "ordinary Markov model" is not shown, but contains $\mathcal{N}$ and would generally have larger dimension.

On the other hand, parametric hidden variable models suffer from various problems caused by the choice of state-space. They may be "too large", in the sense that the dimension of the parameter space is greater than the dimension of the set of probability distributions in the induced model, thereby introducing identifiability problems. They may also be "too small", in that unwanted additional restrictions are implied by the parametric structure and, therefore, the models have a smaller dimension than the marginal model: this is depicted by the curve labelled $\mathcal{L}$ in Figure 2.

Paradoxically, it may even be the case that a hidden variable model is "too large" and "too small" at the same time. For example, take a latent variable model in Example 1.1 with the simplest possible state-space in which everything is binary: the full model over all five variables has dimension 12; however, we have already established that the dimension of the marginal model over the observed variables is at most 11 , so the model is clearly over-parameterized. In fact, it can be shown that the dimension of this latent variable model over the observed variables is only 10 , so an additional-and perhaps unwelcome-restriction is present due to the choice of a binary latent variable model [see Appendix A, Evans (2018)].

If $X_{0}$ is given enough states, the latent variable model and the marginal model coincide for graphs such as the one in Figure 1, a fact we will exploit in our proofs. However, such a latent variable model is less useful for statistical inference because it is generally massively over-parameterized. See Example 6.2 for a demonstration of this.

None of this should be construed as suggesting that the marginal model supersedes all latent variable models, since sometimes the additional parametric assumptions made in a latent variable model are crucial to their utility. For example, hidden Markov models and phylogenetic tree models are important and widely used latent variable models, but their corresponding marginal models are saturated. Using the marginal model would therefore be statistically uninteresting and likely lead only to trivial inferences. However, as noted above for Example 1.1 and as we will see again in Example 6.2, in some examples marginal models are more suitable than any latent variable model. Marginal models are also of interest in the Quantum Information literature, because they enable comparison between "classical" latent variable models and the more general quantum entangled states [Henson, Lal and Pusey (2014)]. We discuss the implications of our results for quantum models in Section 6.2.
1.2. A short algebra tutorial. This paper makes use of some results from real algebraic geometry, which provides powerful tools for analysing these complicated sets of distributions. All our statistical models are collections of distributions within the probability simplex that satisfy certain constraints. The constraints on a Bayesian network model are conditional independences, and can be represented as the requirement that certain polynomials in the probabilities are equal to zero; for example, the conditional independence $X_{1} \Perp X_{3} \mid X_{2}$ is equivalent to

$$
p\left(x_{2}\right) \cdot p\left(x_{1}, x_{2}, x_{3}\right)-p\left(x_{1}, x_{2}\right) \cdot p\left(x_{2}, x_{3}\right)=0 \quad \forall x_{1}, x_{2}, x_{3}
$$

The set of points at which a collection of polynomials are all zero is called an algebraic variety, or sometimes an algebraic set. This perspective is explored in depth for Bayesian network models by Garcia, Stillman and Sturmfels (2005). In addition to equality constraints, these models will satisfy polynomial inequalities; that is, $p\left(x_{V}\right) \geq 0$. A set defined by a combination of polynomial equalities and inequalities is said to be semi-algebraic; this category includes many common finite-dimensional statistical models. Semi-algebraic sets have the nice property that their images are semi-algebraic under any polynomial map, which includes elimination of variables or projection onto a linear subspace. A consequence of this is that the margin of any model defined by a semi-algebraic set is also defined by a semi-algebraic set.

The Zariski closure of a set is the smallest algebraic variety that contains it; the fact that this is well defined is a significant result in algebraic geometry. For a semialgebraic set, one can informally think of its Zariski closure as the set obtained by keeping the equality constraints and "throwing away" the inequality constraints. Semi-algebraic sets have many interesting properties, but they are not necessarily "nice" from a statistical perspective, in the sense of leading to regular asymptotics. For this, we need our set to be a manifold, that is, to be locally Euclidean.

1.3. Contribution. In this paper, we show that marginal models with finite discrete observed variables are algebraically equivalent to the appropriate nested Markov model, in the sense that the Zariski closures of the marginal model and the nested model are the same. A consequence of this is that a margin of a DAG model and its nested counterpart have the same dimension, and differ only by inequality constraints. The marginal model defined by (1) in Example 1.1 is indeed 11-dimensional, and is algebraically defined by (2) and (3); however, the marginal model also satisfies polynomial inequality constraints that the nested model does not. The result can be interpreted as showing that the constraint finding algorithm of Tian and Pearl (2002) is "complete", in the sense that no other equality constraints are necessary to describe the marginal model.

THEOREM 1.2. Let $\mathcal{G}$ be a Bayesian network model with vertices $V \cup H$, where $X_{V}$ are discrete random variables and $X_{H}$ have an arbitrary state-space. The resulting model over the margin of $X_{V}$ has the same Zariski closure as the set of distributions satisfying the constraints listed in Tian and Pearl (2002).

This means that we have, for the first time, a full algebraic characterization of margins of Bayesian network models. It also shows that the nested model represents a sensible and pragmatic approximation to the marginal model: we currently have no way to derive inequality constraints efficiently, so the nested modelwhich has a factorization criterion, separation criteria and a discrete parameterization [Richardson et al. (2017)]—is much easier to work with, and can easily be fitted with existing algorithms [Evans and Richardson (2010)]. In addition, the nested model inside the probability simplex is a manifold and, therefore, regular whenever the joint distribution is positive, whereas the marginal model may have a boundary that lies strictly inside the simplex. The nested model therefore has better statistical properties than the marginal model, in the sense that data generated from any strictly positive distribution will lead to regular asymptotics.

Causal discovery methods such as the FCI algorithm [Spirtes, Glymour and Scheines (2000)] that use conditional independence constraints could, in principle, be extended to use the constraints implied by nested models; our main result shows that is "as good as it gets", in the sense that there are no other equality constraints to test without making further (e.g., parametric) assumptions. Thus, this paper probes the limits of what it is possible to learn about causal models with hidden variables from observational data when we have no further knowledge about the latent statespace.

We work with a class of hyper-graphs called mDAGs, with which we associate marginals of DAG models [Evans (2016)]. That paper also shows that these mDAGs are a sufficiently rich class of graphs as to represent all the marginal models we will consider. Nested models are introduced in detail by Richardson et al. (2017), and a parameterization of them in the discrete case given by Evans and

Richardson (2015). The existence of this parameterization will allow us to prove our main results.

The remainder of the paper is organized as follows: Section 2 reviews DAG models, their margins and mDAGs, and carefully defines the problem of interest. Section 3 defines the nested Markov model, and recalls relevant properties from Richardson et al. (2017) and Evans and Richardson (2015). The remaining sections contain entirely new material: in Section 4, we introduce latent variable models with specific state-spaces, and show that they can be used to represent some marginal models without loss of generality; Section 5 contains the main results of the paper, including the proof of Theorem 1.2. Finally, in Section 6 we show that a large class of marginal models represent smooth manifolds, and provide some discussion.
2. Directed graphical models. We begin with some elementary graphical definitions.

Definition 2.1. A directed graph, $\mathcal{G}(V, \mathcal{E})$, consists of a finite set of vertices, $V$, and a collection of edges, $\mathcal{E}$, which are ordered pairs of distinct elements of $V$. If $(v, w) \in \mathcal{E}$, we denote this by $v \rightarrow w$, and say that $v$ is a parent of $w$; the set of parents of $w$ is denoted by $\mathrm{pa}_{\mathcal{G}}(w)$. Similarly, $w$ is a child of $v$, and the child set is denoted by $\operatorname{ch}_{\mathcal{G}}(v)$.

A directed graph is acyclic if there is no sequence of edges $v_{1} \rightarrow v_{2} \rightarrow \cdots \rightarrow$ $v_{k} \rightarrow v_{1}$ for $k>1$. We call such a graph a directed acyclic graph, or DAG.

Graphs are best understood visually: an example of a DAG with five vertices and five edges is given in Figure 1. We will require the following generalization of a DAG that allows for two separate types of vertex.

Definition 2.2. A conditional $D A G \mathcal{G}(V, W, \mathcal{E})$ is a DAG with vertices ${ }^{3}$ $V \dot{\cup} W$ and edge set $\mathcal{E}$, with the restriction that no vertex in $W$ may have any parents. The elements of $V$ are the random vertices, and $W$ the fixed vertices; these two sets are disjoint.

If $W=\varnothing$, this reduces to the ordinary definition of a DAG. We depict fixed vertices with square nodes, and random ones with round nodes: see the example in Figure 3(a).
2.1. Graphical models. A graphical model arises from the identification of a graph with a collection of multivariate probability distributions; see Lauritzen (1996) for an introduction. Each vertex $v \in V$ represents a random variable $X_{v}$

[^0]
[^0]:    ${ }^{3}$ Here and throughout, $\dot{U}$ denotes a disjoint union of sets.

![img-2.jpeg](img-2.jpeg)

FIG. 3. (a) A conditional directed acyclic graph with three random vertices $(0,2,4)$ and two fixed vertices $(1,3)$. (b) An mDAG representing the DAG in Figure 1, with the vertex 0 treated as unobserved.
taking values in a finite state-space $\mathfrak{X}_{v}$, and a model for their joint distribution is determined by the structure of the graph. With a conditional DAG $\mathcal{G}$, we associate a collection of probability measures $P\left(\cdot \mid x_{W}\right)$ on $\mathfrak{X}_{V} \equiv \times_{v \in V} \mathfrak{X}_{v}$, indexed by $x_{W} \in$ $\mathfrak{X}_{W}$. Mathematically, fixed nodes play a similar role to the "parameter nodes" used by Dawid (2002).

Following Lauritzen (1996), we say a probability kernel over $\mathfrak{X}_{A}$ given $\mathfrak{X}_{B}$ is a nonnegative function $q: \mathfrak{X}_{A} \times \mathfrak{X}_{B} \rightarrow \mathbb{R}$ such that $\sum_{x_{A}} q\left(x_{A} \mid x_{B}\right)=1$ for all $x_{B} \in \mathfrak{X}_{B}$. A kernel behaves much like a conditional probability distribution, but no assumption is made about any distribution over the indexing set $\mathfrak{X}_{B}$. We apply the usual definitions for marginalizing and conditioning in kernels:

$$
q\left(x_{A} \mid x_{B}\right) \equiv \sum_{x_{C}} q\left(x_{A}, x_{C} \mid x_{B}\right), \quad q\left(x_{A} \mid x_{B}, x_{C}\right) \equiv \frac{q\left(x_{A}, x_{C} \mid x_{B}\right)}{q\left(x_{C} \mid x_{B}\right)}
$$

If $q\left(x_{A} \mid x_{B}, x_{C}\right)$ does not depend upon $x_{B}$, then we will denote it $q\left(x_{A} \mid x_{C}\right)$, and say that $X_{A} \Perp X_{B} \mid X_{C}[q]$. Below, and elsewhere, we use the shorthand $V W$ for $V \cup W$ in subscripts.

DEFINITION 2.3. Let $p\left(x_{V} \mid x_{W}\right)$ be a probability kernel over $\mathfrak{X}_{V}$ indexed by $\mathfrak{X}_{W}$. We say that $p$ obeys the factorization criterion with respect to a DAG $\mathcal{G}$ if it factorizes into univariate kernels as

$$
p\left(x_{V} \mid x_{W}\right)=\prod_{v \in V} p\left(x_{v} \mid x_{\mathrm{pa}(v)}\right), \quad x_{V W} \in \mathfrak{X}_{V W}
$$

Note that if $\mathcal{G}(V \cup W, \mathcal{E})$ is a causally interpreted DAG, then (4) gives the usual formula for $p\left(x_{V} \mid \operatorname{do}\left(x_{W}\right)\right)$, the distribution of $X_{V}$ after intervening to set $X_{W}=$ $x_{W}$.

The definition reduces to the familiar factorization criterion for DAGs if $W=\varnothing$. The extra generality will be useful for discussing Markov properties which involve factorization of the distribution into conditional pieces. The fixed vertices are analogous to variables that have been conditioned upon.

A Bayesian network model can also be defined by insisting that each random variable $X_{v}$ can be written as a measurable function of $X_{\mathrm{pa}(v)}$ and an independent

noise variable; we call this the structural equation property; for discrete variables in particular, these two criteria are equivalent. Although the factorization property is often simpler to work with for practical purposes such as modelling and fitting, the structural equation property is useful in proofs.

EXAMPLE 2.4. A distribution $P$ with density $p$ obeys the factorization criterion for the graph in Figure 1 if the density has the form

$$
p\left(x_{0}, x_{1}, x_{2}, x_{3}, x_{4}\right)=p\left(x_{0}\right) \cdot p\left(x_{1}\right) \cdot p\left(x_{2} \mid x_{0}, x_{1}\right) \cdot p\left(x_{3} \mid x_{2}\right) \cdot p\left(x_{4} \mid x_{0}, x_{3}\right)
$$

Such distributions are precisely those which satisfy the conditional independences

$$
X_{1} \Perp X_{0}, \quad X_{3} \Perp X_{0}, X_{1} \mid X_{2}, \quad X_{4} \Perp X_{1}, X_{2} \mid X_{0}, X_{3}
$$

EXAMPLE 2.5. A kernel $p$ obeys the factorization criterion for the conditional DAG in Figure 3(a) if it can be written as

$$
p\left(x_{0}, x_{2}, x_{4} \mid x_{1}, x_{3}\right)=p\left(x_{0}\right) \cdot p\left(x_{2} \mid x_{0}, x_{1}\right) \cdot p\left(x_{4} \mid x_{0}, x_{3}\right)
$$

2.2. Latent variables and $m D A G s$. We now introduce the possibility that some of the random variables are unobserved or latent, leaving the marginal distribution over the remaining observed variables. We represent the collection of margins of DAG models using a larger class of hyper-graphs called mDAGs ("marginal DAGs"). These avoid dealing with latent variables directly, by instead introducing additional edges to represent them. For example, the DAG in Figure 1, with the vertex 0 treated as a latent variable, is represented by the mDAG in Figure 3(b).

Define an abstract simplicial complex $\mathcal{B}$ over $V$ as a collection of nonempty subsets of $V$ such that (i) $\{v\} \in \mathcal{B}$ for every $v \in V$, and (ii) if $A \in \mathcal{B}$ and $B \subseteq A$ with $B \neq \varnothing$, then $B \in \mathcal{B}$.

DEFINITION 2.6. An $m D A G, \mathcal{G}(V, W, \mathcal{E}, \mathcal{B})$, is a hyper-graph consisting of a conditional DAG with random vertices $V$, fixed vertices $W$ and directed edge set $\mathcal{E}$, together with an abstract simplicial complex $\mathcal{B}$ over $V$, called the bidirected faces.

We say that $\mathcal{G}^{\prime}\left(V^{\prime}, W^{\prime}, \mathcal{E}^{\prime}, \mathcal{B}^{\prime}\right)$ is a subgraph of $\mathcal{G}$ if $V^{\prime} \subseteq V, \mathcal{E}^{\prime} \subseteq \mathcal{E}, \mathcal{B}^{\prime} \subseteq \mathcal{B}$, and $W^{\prime} \subseteq V \cup W$ : that is, each component is contained within the previous one, but random vertices may become fixed.

The mDAG was introduced by Evans (2016), without the additional generality of fixed vertices. This aspect changes very little about the theory of these graphs, but is necessary for understanding the nested Markov model; note that bidirected faces only involve the random vertices. As with conditional DAGs, when representing mDAGs graphically the fixed vertices are drawn as square nodes and random vertices as circles.

![img-3.jpeg](img-3.jpeg)

FIG. 4. (a) An mDAG, $\mathcal{G}$, and (b) a DAG with hidden variables, $\tilde{\mathcal{G}}$, representing the same model (the canonical $D A G)$.

The bidirected simplicial complex is represented by its maximal nontrivial elements (i.e., those of size at least 2), called the bidirected hyperedges, or just edges. These are drawn in red, as in Figure 4(a); in this case $W=\{6\}$ and the maximal sets of $\mathcal{B}$ are $\{1,2\},\{2,3,4\}$ and $\{3,4,5\}$.

With each mDAG, $\mathcal{G}$, we can associate a conditional DAG $\tilde{\mathcal{G}}$ by replacing each maximal element $B \in \mathcal{B}$ (of size at least 2 ) with a new random vertex $u$, such that the children of $u$ are precisely the vertices in $B$. The new vertex $u$ becomes the "unobserved" variable represented by the bidirected edge $B$. We call $\tilde{\mathcal{G}}$ the canonical $D A G$ associated with $\mathcal{G}$. The mDAG in Figure 4(a) is thus associated with the canonical DAG in Figure 4(b).

Our interest in mDAGs lies in their representation of the margin of the associated canonical DAG, and so we define our model in this spirit. From the definitions, it may seem as though the set of models is restricted to cases where the latent variables have no parents; in fact this does not cause any loss of generality since-if we make no assumption about state-space of the latents-all marginal DAG models can be represented in this way [see Evans (2016), Theorem 2].

DEFINITION 2.7. Let $\mathcal{G}$ be an mDAG with vertices $V \dot{U} W$, and let $\tilde{\mathcal{G}}$ be the canonical DAG with vertices $V \dot{U} U \dot{U} W$. A kernel $p$ over $\mathfrak{X}_{V}$ indexed by $\mathfrak{X}_{W}$ is said to be in the marginal model for $\mathcal{G}$ if there exists a kernel $q$ that factorizes according to $\tilde{\mathcal{G}}$, and

$$
p\left(x_{V} \mid x_{W}\right)=\int_{\mathfrak{X}_{U}} q\left(x_{V}, x_{U} \mid x_{W}\right) d x_{U}
$$

That is, the margin of $q$ over $X_{V}$ is $p$. Denote the collection of such kernels by $\mathcal{M}(\mathcal{G})$.

In other words, the marginal model is the collection of kernels that could be constructed as the margin of a Bayesian network with latent variables replacing the bidirected edges. If $\mathcal{G}$ is a DAG, then the marginal model is just the usual model defined by the factorization.

A latent variable model corresponding to a canonical DAG $\tilde{\mathcal{G}}$ (i.e., possibly with parametric or distributional assumptions on the latent variables) always lies within the marginal model corresponding to the mDAG $\mathcal{G}$.

# 2.3. Districts and sterile vertices. 

Definition 2.8. A collection of random vertices $C \subseteq V$ in an mDAG $\mathcal{G}$ is bidirected-connected if for any distinct $v, w \in C$, there is a sequence of vertices $v=v_{0}, v_{1}, \ldots, v_{k}=w$ all in $C$ such that, for each $i=1, \ldots, k$, the pair $\left\{v_{i-1}, v_{i}\right\} \in \mathcal{B}$. A district of an mDAG is an inclusion maximal bidirectedconnected set of random vertices.

More informally, a district is a maximal set of random vertices joined by the red edges in an mDAG. It is easy to see from the definition that districts form a partition of the random vertices in an mDAG. The mDAG in Figure 3(b), for example, contains three districts, $\{1\},\{3\}$ and $\{2,4\}$. Districts inspire a useful reduction of mDAGs, via the following special subgraph.

Definition 2.9. Let $\mathcal{G}$ be an mDAG containing random vertices $C \subseteq V$. Then $\mathcal{G}[C]$ is the subgraph of $\mathcal{G}$ with:
(i) random vertices $C$ and fixed vertices $\mathrm{pa}_{\mathcal{G}}(C) \backslash C$;
(ii) those directed edges $w \rightarrow v$ such that $v \in C$ [and $w \in \mathrm{pa}_{\mathcal{G}}(C)$ ];
(iii) the bidirected simplicial complex $\mathcal{B}_{C} \equiv\{B \cap C: B \in \mathcal{B}(\mathcal{G})\}$.
$\mathcal{G}[C]$ is therefore the subgraph induced over $C$, together with parents of $C$ and edges directed towards $C$. Any edges (whether directed or bidirected) between the newly fixed vertices are removed.

For the graph in Figure 3(b) the subgraphs $\mathcal{G}[\{1\}]$, $\mathcal{G}[\{3\}]$ and $\mathcal{G}[\{2,4\}]$ are shown in Figures 5(a), (b) and (c) respectively. Note in particular that the edge $2 \rightarrow 3$ is not in the subgraph $\mathcal{G}[\{2,4\}]$.

DEFINITION 2.10. Let $\mathcal{G}$ be an mDAG with random vertices $V$. For an arbitrary set $C \subseteq V$, define sterile ${ }_{\mathcal{G}}(C) \equiv C \backslash \mathrm{pa}_{\mathcal{G}}(C)$. In words, sterile ${ }_{\mathcal{G}}(C)$ is the subset of $C$ whose elements have no children in $C$. We say a set $C$ is sterile if $C=$ sterile $_{\mathcal{G}}(C)$.
![img-4.jpeg](img-4.jpeg)

FIG. 5. Subgraphs corresponding to factorization of the graph in Figure 3(b) into districts. Parent nodes of the district are drawn as squares.

3. Nested Markov property. The nested Markov property imposes constraints on a joint distribution that mimic those satisfied by the marginal model, including conditional independences and the Verma constraint in Example 1.1 [Richardson et al. (2017)]. It is defined in the following recursive way, which is a modification of the algorithm of Tian and Pearl (2002).

DEFINITION 3.1 (Nested Markov property). A kernel $p$ over $\mathfrak{X}_{V}$ indexed by $\mathfrak{X}_{W}$ obeys the nested Markov property for an $\operatorname{mDAG} \mathcal{G}(V, W)$ if $V=\varnothing$, or both:

1. $p$ factorizes over the districts $D_{1}, \ldots, D_{l}$ of $\mathcal{G}$ :

$$
p\left(x_{V} \mid x_{W}\right)=\prod_{i=1}^{l} g_{i}\left(x_{D_{i}} \mid x_{\mathrm{pa}\left(D_{i}\right) \backslash D_{i}}\right)
$$

where each $g_{i}$ is a kernel which [if $l \geq 2$ or $\left.W \backslash \mathrm{pa}_{\mathcal{G}}(V) \neq \varnothing\right]$ obeys the nested Markov property with respect to $\mathcal{G}\left[D_{i}\right]$; and
2. for each $v \in V$ such that $\operatorname{ch}_{\mathcal{G}}(v)=\varnothing$, the marginal kernel

$$
p\left(x_{V \backslash v} \mid x_{W}\right)=\sum_{x_{v}} p\left(x_{V} \mid x_{W}\right)
$$

obeys the nested Markov property with respect to $\mathcal{G}[V \backslash\{v\}]$.
The set of kernels that obey the nested Markov property for $\mathcal{G}$ is the nested Markov model, denoted by $\mathcal{N}(\mathcal{G})$.

The condition that $l \geq 2$ or $W \backslash \mathrm{pa}_{\mathcal{G}}(V) \neq \varnothing$ in the first criterion of this definition is simply to prevent an infinite recursion of the definition: all the graphs invoked recursively have either fewer random vertices or fewer vertices overall than their predecessor in the recursion. When we reach a graph with a single random vertex $v$ such that all fixed vertices are parents of $v$, then any kernel $p\left(x_{v} \mid x_{\mathrm{pa}(v)}\right)$ satisfies the nested Markov property.

The discrete nested model is equivalently defined by the constraints above and the parameterization in Evans and Richardson (2015) [as well the nested Markov properties described in Richardson et al. (2017)]. We will make use of these equivalent definitions throughout.

EXAMPLE 3.2. Consider again the mDAG in Figure 3(b). Applying criterion 1 to this graph implies that

$$
p\left(x_{1}, x_{2}, x_{3}, x_{4}\right)=g_{1}\left(x_{1}\right) \cdot g_{24}\left(x_{2}, x_{4} \mid x_{1}, x_{3}\right) \cdot g_{3}\left(x_{3} \mid x_{2}\right)
$$

for some $g_{1}, g_{3}$ and $g_{24}$ obeying the nested Markov property with respect to the mDAGs in Figures 5(a), (b) and (c), respectively. Applying the second criterion to

$g_{24}$ and the now childless vertex 2 [see Figure 5(c)] gives

$$
\sum_{x_{2}} g_{24}\left(x_{2}, x_{4} \mid x_{1}, x_{3}\right)=h\left(x_{4} \mid x_{3}\right)
$$

for some function $h$ independent of $x_{1}$ (by a further application of the first criterion); this is precisely the Verma constraint.

The marginal model implies additional conditions on joint distributions because, although it satisfies the properties used to define the nested model, these properties are not sufficient to describe it. In particular, for $p$ to be in the marginal model, the kernel $g_{24}$ must satisfy Bell's inequalities [see, e.g., ver Steeg and Galstyan (2011), Section 4.1].

The nested Markov property is "sound" with respect to marginal models, in the sense that all constraints represented by the former also hold in the latter. The following theorem is a consequence of the results in Tian and Pearl (2002).

THEOREM 3.3. For any $m D A G \mathcal{G}$, we have $\mathcal{M}(\mathcal{G}) \subseteq \mathcal{N}(\mathcal{G})$.

# 3.1. Parameterizing sets. 

DEFINITION 3.4. Let $\mathcal{G}$ be an mDAG. A subset of random vertices $S \subseteq V$ is called intrinsic if $S$ is a district in any graph that can be obtained by iteratively applying graphical operations of the form 1 and 2 in Definition 3.1 (i.e., taking the graph $\mathcal{G}[D]$ for a district $D$, or $\mathcal{G}[V \backslash\{v\}]$ for a sterile vertex $v$ ).

Given an intrinsic set, $S$, define $H=$ sterile $_{\mathcal{G}}(S)$ to be the recursive head, and $T=\mathrm{pa}_{\mathcal{G}}(S)$ the tail, associated with $S$ (note that $H$ and $T$ are disjoint). The collection of all recursive heads in $\mathcal{G}$ is denoted by $\mathcal{H}(\mathcal{G})$. There is a one-to-one correspondence between intrinsic sets and recursive heads [Evans and Richardson (2015)]. Throughout, we will use $H$ and $T$ to indicate recursive heads and tails, respectively, with the context making it clear which intrinsic set is being referred to. We will sometimes write $T(H)$ to make clear that the head determines the tail.

The definitions above also appear in Evans and Richardson (2015). We introduce a new definition: let

$$
\mathcal{A}(\mathcal{G}) \equiv\{H \cup A \mid H \in \mathcal{H}(\mathcal{G}), A \subseteq T(H)\}
$$

be the parameterizing sets of $\mathcal{G}$. This collection of sets is so-called because it (locally) describes the set of distributions (or kernels) contained in the nested and marginal models, as we will prove in Section 5.

Example 3.5. The mDAG in Figure 3(b) has districts $\{1\},\{3\}$ and $\{2,4\}$, so these are all intrinsic sets. Further, in the subgraph $\mathcal{G}[\{2,4\}]$ the vertices 2 and 4 have no children, so we can marginalize either to see that respectively $\{4\}$ and $\{2\}$

are intrinsic sets. The corresponding recursive heads and tails are then:


Note that every nonempty subset of $V$ is represented in $\mathcal{A}$ except for $\{1,3\}$, $\{1,2,3\},\{1,4\}$ and $\{1,3,4\}$. The first two of these correspond to the conditional independence $X_{1} \Perp X_{3} \mid X_{2}$ in (2), and the others to the Verma constraint (3).

We use the $\triangle$ operator to denote the symmetric difference of two sets: $A \triangle B \equiv$ $(A \backslash B) \cup(B \backslash A)$. Given a finite collection $A_{i}, i=1, \ldots, k$, let

$$
\bigwedge_{i=1}^{k} A_{i} \equiv A_{1} \triangle A_{2} \triangle \cdots \triangle A_{k}
$$

denote the symmetric difference of all the $A_{i}$. That is, it is the set containing precisely those elements $a$ which appear in an odd number of the sets $A_{i}$.

The following result gives a characterization of the parameterizing sets in terms of symmetric differences which will be fundamental to our proof of the main results in this paper.

LEMMA 3.6. A set $A \in \mathcal{A}(\mathcal{G})$ if and only if there exists a bidirected-connected set $C=\left\{v_{1}, \ldots, v_{k}\right\}$ in $\mathcal{G}$, and sets $A_{i}, i=1, \ldots, k$, satisfying $\left\{v_{i}\right\} \subseteq A_{i} \subseteq\left\{v_{i}\right\} \cup$ $\mathrm{pa}_{\mathcal{G}}\left(v_{i}\right)$, such that

$$
A=\bigwedge_{i=1}^{k} A_{i}=A_{1} \triangle \cdots \triangle A_{k}
$$

The proof is found in Section B. 1 of the supplement [Evans (2018)].
3.2. Parameterization of the nested model. The nested Markov model can be parameterized with parameters indexed by head-tail sets [Evans and Richardson (2015)], and the parameterization defines a smooth bijection between an open subset of a real vector space (i.e., the parameter space) and the model (the set of probability distributions). This has some nice consequences that we now state [for proofs, see Evans and Richardson (2015)].

In particular, for a fixed state-space $\mathfrak{X}_{V W}$ the set $\mathcal{N}(\mathcal{G})$ is a smooth manifold within the strictly positive probability simplex, and has dimension ${ }^{4}$

$$
d\left(\mathcal{G}, \mathfrak{X}_{V W}\right) \equiv \sum_{H \in \mathcal{H}(\mathcal{G})}\left|\mathfrak{X}_{T(H)}\right| \prod_{h \in H}\left(\left|\mathfrak{X}_{h}\right|-1\right)
$$

In the all-binary case, this reduces to $d\left(\mathcal{G}, \mathfrak{X}_{V W}\right) \equiv \sum_{H \in \mathcal{H}(\mathcal{G})} 2^{|T(H)|}$. Our main result will show that $\mathcal{M}(\mathcal{G})$ always has the same dimension as $\mathcal{N}(\mathcal{G})$. Indeed, the parameterization of $\mathcal{N}(\mathcal{G})$ will in principle also serve as a parameterization of $\mathcal{M}(\mathcal{G})$, except that one would also have to restrict the parameter space in order to enforce the inequality constraints; of course, this is currently impractical since the inequality constraints are not generally known.
3.3. Relationship between mDAGs and ADMGs. Previous papers considering marginal and nested models for DAGs have used acyclic directed mixed graphs, which are the restriction of mDAGs with random vertices so that each bidirected edge has size two [Richardson (2003), Evans and Richardson (2014), Richardson et al. (2017)]. From the perspective of the nested Markov model, this distinction is unimportant: if we replace any bidirected simplicial complex with all its subsets of size 2, we obtain a conditional ADMG that represents the same model under the nested Markov property.

It therefore follows from Theorem 1.2 that there is no difference in equality constraints between graphs that differ only in this manner; algebraically the model defined by having a single latent parent for several variables is the same as having separate parents for each pair of vertices. Note that the marginal models are not always equal, as the restriction to pairwise independent latent parents will sometimes introduce additional inequality constraints. See Evans (2016) for a more detailed discussion.
4. Geared mDAGs. In this section, we introduce a special class of mDAGs which we term "geared". For marginal models relating to such graphs, the statespace of the hidden vertices can be restricted without loss of generality, making proofs considerably easier. In Section 5, we prove our main result first for geared graphs, and then extend the result to the general case.

DEFINITION 4.1. Let $\mathcal{G}$ be an mDAG with bidirected simplicial complex $\mathcal{B}$. We say that $\mathcal{G}$ is geared if the maximal elements of $\mathcal{B}$ satisfy the running intersection property. That is, there is an ordering of the edges $B_{1}, \ldots, B_{k}$ such that for each $j>1$, there exists $s(j)<j$ with

$$
B_{j} \cap \bigcup_{i<j} B_{i}=B_{j} \cap B_{s(j)}
$$

[^0]
[^0]:    ${ }^{4}$ Note that we use the convention that $\left|\mathfrak{X}_{\varnothing}\right|=1$.

In other words, the vertices that are contained in both $B_{j}$ and any previous edge are all contained within one such edge $B_{s(j)}$.

A particular ordering of the elements of $\mathcal{B}$ that satisfies running intersection is called a gearing of $\mathcal{G} .{ }^{5}$

Example 4.2. The simplest nongeared mDAG is the bidirected 3-cycle, which has bidirected edge sets $\{1,2\},\{2,3\},\{1,3\}$. We cannot order these in a way that satisfies the running intersection property, since whichever edge is placed last in the ordering shares a different vertex with each of the two other edges.

The following fact about geared subgraphs of mDAGs will allow us to generalize our later results to graphs which are not geared.

Lemma 4.3. Let $\mathcal{G}$ be an mDAG with parameterizing sets $\mathcal{A}(\mathcal{G})$. For any $A \in \mathcal{A}(\mathcal{G})$, there exists a geared $m D A G \mathcal{G}^{\prime} \subseteq \mathcal{G}$, such that $A \in \mathcal{A}\left(\mathcal{G}^{\prime}\right)$.

Proof. By Lemma 3.6, $A$ is of the form (5) for some bidirected-connected set $C$. Let $\mathcal{G}^{\prime}$ have the same vertices (random and fixed) and directed edges as $\mathcal{G}$, but be such that the set $C$ is singly connected by bidirected edges (i.e., the edges are all of size 2 and removing any of them will cause $C$ to be disconnected) chosen to be a subgraph of $\mathcal{G}$. Then $\mathcal{G}^{\prime}$ is geared by standard properties of trees and running intersection, and using Lemma 3.6 again we have $A \in \mathcal{A}\left(\mathcal{G}^{\prime}\right)$.
4.1. Functional models. The key property of geared graphical models is that we can find a finite discrete latent variable model that is the same (over the observed variables) as the marginal model; that is, if the latent variables have a sufficiently large state-space then they do not impose additional restrictions on the observed distribution. This is achieved by letting each observed variable be a deterministic function of its latent and observed parents. We illustrate this with an example.

Example 4.4. Consider the mDAG in Figure 6(a) representing the instrumental variables model, used to model noncompliance in clinical trials; here, for example, $X_{1}$ represents a randomized treatment, $X_{2}$ the treatment actually taken,

[^0]
[^0]:    ${ }^{5}$ The term "geared" is chosen because a collection of bidirected edges that satisfies running intersection may appear rather like "cogs" in a set of gears; see Figure 4. The definition is equivalent to the requirement that the simplicial complex $\mathcal{B}$ is vertex decomposable [Provan and Billera (1980)], and is also closely related to the notion of decomposability in an undirected or directed graph. Indeed the term "decomposable" is used by Fox, Käufl and Drton (2015) to describe the same idea. We avoid using this terminology because of its existing meaning in connection with undirected and directed graphical models; for example, ordinary DAGs are trivially geared, but they may or may not be decomposable in the original sense [Lauritzen (1996)].

![img-5.jpeg](img-5.jpeg)

FIG. 6. (a) An mDAG representing the instrumental variables model; (b) a DAG with functional latent variables equivalent to the potential outcomes model of instrumental variables.
and $X_{3}$ a patient's outcome or response, such as survival. Suppose that each of these quantities is binary, taking values in $\{0,1\}$. Conceptually, it can be useful to posit the existence of two different potential outcomes $X_{3}(0), X_{3}(1)$ for the survival response, one for each level of the treatment; $X_{3}(1)$ is the patient's outcome given that they choose to take the treatment (i.e., when $X_{2}=1$ ) and $X_{3}(0)$ is their outcome given that they do not $\left(X_{2}=0\right)$. For example, if $X_{3}(0)=0$ and $X_{3}(1)=1$ then the patient survives if they take the treatment but dies if they do not. This pair of values is known as a patient's response type. Of course, we can only ever observe one of these outcomes in a given patient, the one corresponding to the observed value of $X_{2}$.

Similarly, we can conceive of two versions of the treatment $X_{2}(0), X_{2}(1)$ depending upon the assigned value of $X_{1}$, this pair being called the patient's compliance type. For example, $X_{2}(0)=X_{2}(1)=0$ means that the patient will not take the treatment, regardless of whether or not they are assigned to the treatment group. These concepts have proved fruitful in causal inference, as they enable discussion of whether treatments have effects at the level of individual patients, rather than just over the entire population on average [Neyman (1923), Rubin (1974), Richardson, Evans and Robins (2011)].

Now, since the latent variable (say $U$ ) with children $\{2,3\}$ can take any value, we can-without loss of generality-assume that it includes the pair $\left(X_{3}(0), X_{3}(1)\right)$, or equivalently a function $f_{3}: \mathfrak{X}_{2} \rightarrow \mathfrak{X}_{3}$ that determines, given the observed $X_{2}$, which value $X_{3}$ will take. In this case, $X_{3}$ is still a measurable function of its parents $U$ and $X_{2}$. Similarly, we can assume $U$ includes a function $f_{2}: \mathfrak{X}_{1} \rightarrow \mathfrak{X}_{2}$ that determines $X_{2}$ given an observed $X_{1}$.

An observation for a particular patient can be obtained by drawing a random treatment assignment $X_{1}$, a random compliance type for the patient $f_{2}$, and a random response type $f_{3}$, and then evaluating $\left(X_{1}, X_{2}, X_{3}\right)=\left(X_{1}, f_{2}\left(X_{1}\right)\right.$, $\left.f_{3}\left(f_{2}\left(X_{1}\right)\right)\right)$. The key point is that one can place a distribution over $\left(X_{1}, f_{2}, f_{3}\right)$ and obtain a distribution over the observed variables $\left(X_{1}, X_{2}, X_{3}\right)$. The only requirement for the distribution to be Markov with respect to this particular graph is that $X_{1} \Perp\left\{f_{2}, f_{3}\right\}$, as depicted in Figure 6(b).

The functional construction outlined above is mathematically equivalent to potential outcomes, and provides a model that is somewhat simpler to study than the

general latent variable model. In fact, any geared mDAG can be reduced to a latent variable model in the way described above, something we will proceed to show in Theorem 4.7.

The nested model in the case of Figure 6(b) is saturated and, therefore, not particularly interesting. For causal modelling, the potential outcomes framework is likely to be substantially more useful in this example. However, it is important to note that potential outcomes do not always give a practical alternative to the nested model; see Example 6.2.
4.2. Remainder sets. Given a single-district, geared mDAG with at least one bidirected edge and a gearing $B_{1}, \ldots, B_{k}$, define

$$
R_{j} \equiv B_{j} \backslash \bigcup_{i<j} B_{i}
$$

(taking $R_{1} \equiv B_{1}$ ) to be the remainder set associated with $B_{j}$. Remainder sets partition $V$, so for a random vertex $v \in V$, define $r(v)$ to be the unique $j$ such that $v \in R_{j}$.

Now say that an ordering $<$ on the vertices in $V$ respects the gearing if for $v \in R_{i}$ and $w \in R_{j}$, we have $v<w$ whenever $i>j$; in other words, all the vertices in $R_{k}$ precede all those in $R_{k-1}$, etc.; such an ordering always exists. For each $v \in V$ with $r(v)=j$, let

$$
\pi(v)=\bigcup_{\substack{i>j \\ v \in B_{i}}} R_{i}
$$

that is, the remainders associated with all bidirected edges which contain $v$ and are later than $j$ in the ordering. Then define a collection of functions

$$
\mathcal{F}_{v} \equiv\left\{f: \mathfrak{X}_{\mathrm{pa}(v)} \times \mathcal{F}_{\pi(v)} \rightarrow \mathfrak{X}_{v}\right\}
$$

where $\mathcal{F}_{A}=\mathcal{X}_{a \in A} \mathcal{F}_{a}$ and $\mathcal{F}_{\varnothing}=\mathfrak{X}_{\varnothing}=\{1\}$. This is well defined since all the vertices in $\pi(v)$ precede $v$ in an ordering which respects the gearing.

Example 4.5. The mDAG in Figure 6(a) has only one bidirected edge and, therefore, is trivially geared with $R_{1}=B_{1}=\{2,3\}$. This leads to the sets $\mathcal{F}_{2}=$ $\left\{f_{2}: \mathfrak{X}_{1} \rightarrow \mathfrak{X}_{2}\right\}$ and $\mathcal{F}_{3}=\left\{f_{3}: \mathfrak{X}_{2} \rightarrow \mathfrak{X}_{3}\right\}$, which are precisely the sets of functions for compliance type and response type, respectively.

Example 4.6. Consider the mDAG in Figure 4, and order the bidirected edges as $B_{1}=\{1,2\}, B_{2}=\{2,3,4\}$ and $B_{3}=\{3,4,5\}$, giving respective remainder sets $R_{1}=\{1,2\}, R_{2}=\{3,4\}$ and $R_{3}=\{5\}$. The ordering $5<4<3<2<1$ of the random vertices respects the gearing, and we have

$$
\pi(1)=\pi(5)=\varnothing, \quad \pi(3)=\pi(4)=\{5\}, \quad \pi(2)=\{3,4\}
$$

In this case, then

$$
\begin{aligned}
& \mathcal{F}_{5}=\left\{f: \mathfrak{X}_{3} \rightarrow \mathfrak{X}_{5}\right\}, \quad \mathcal{F}_{4}=\left\{f: \mathfrak{X}_{2,3,6} \times \mathcal{F}_{5} \rightarrow \mathfrak{X}_{4}\right\}, \\
& \mathcal{F}_{3}=\left\{f: \mathfrak{X}_{1} \times \mathcal{F}_{5} \rightarrow \mathfrak{X}_{3}\right\}, \quad \mathcal{F}_{2}=\left\{f: \mathcal{F}_{3,4} \rightarrow \mathfrak{X}_{2}\right\}, \\
& \mathcal{F}_{1}=\left\{f:\{1\} \rightarrow \mathfrak{X}_{1}\right\} .
\end{aligned}
$$

Alternatively, if we order the bidirected edges as $\{2,3,4\},\{1,2\},\{3,4,5\}$, then we could take $5<1<2<3<4$, and

$$
\pi(1)=\pi(5)=\varnothing, \quad \pi(3)=\pi(4)=\{5\}, \quad \pi(2)=\{1\}
$$

this yields $\mathcal{F}_{2}=\left\{f: \mathcal{F}_{1} \rightarrow \mathfrak{X}_{2}\right\}$, with other collections $\mathcal{F}_{v}$ unchanged.
4.3. Functional models for geared graphs. If a vertex $v$ is contained within exactly one bidirected edge, $B$, then without loss of generality we can assume that the latent variable corresponding to $B$ contains all the residual information about how $X_{v}$ should behave given the values of its visible parents, $X_{\mathrm{pa}(v)}$. In other words, the latent variable associated with $B$ includes a (random) function $f_{v}: \mathfrak{X}_{\mathrm{pa}(v)} \rightarrow \mathfrak{X}_{v}$ which, once instantiated, "tells" $X_{v}=f_{v}\left(X_{\mathrm{pa}(v)}\right)$ which value it should take for each value of its other parents, exactly as in Example 4.5. ${ }^{6}$ All the randomness of $X_{v}$ is collapsed into $f_{v}$ and $X_{\mathrm{pa}(v)}$.

If $v$ is contained within two or more bidirected edges, say $B_{i}$ and $B_{j}$, we might say that $B_{i}$ tells $X_{v}$ what value to take for every value of its visible parents and the other latent variables. However, it is not clear how to define such a function until the state-space associated with the other latent parents (i.e., $B_{j}$ ) has already been fixed. The decomposable structure of geared graphs makes it possible to iteratively fix state-spaces for latent variables without loss of generality.

To see this, suppose we have a single-district, geared mDAG $\mathcal{G}$ with remainder sets $R_{1}, \ldots, R_{k}$, and form the canonical DAG $\tilde{\mathcal{G}}$ by replacing each bidirected edge $B_{i}$ in $\mathcal{G}$ with a new vertex $u_{i}$, such that $\operatorname{ch}_{\tilde{\mathcal{G}}}\left(u_{i}\right)=B_{i}$. Compare, for example, the structure of the graphs in Figures 4(a) and (b).

Note that each vertex $v \in R_{k}$ has a single latent parent $u_{k}$ in $\tilde{\mathcal{G}}$. Then, without loss of generality, incorporate the function $f_{v}: \mathfrak{X}_{\mathrm{pa}_{\tilde{\mathcal{G}}}(v)} \rightarrow \mathfrak{X}_{v}$ into the latent variable $U_{k}$. We "replace" $U_{k}$ with the collection of such functions $f_{R_{k}} \in \mathcal{F}_{R_{k}}$.

Each vertex $v \in R_{k-1}$ has latent parent $u_{k-1}$ and possibly also $u_{k}$; but since the state-space of $U_{k}$ has been fixed as $\mathcal{F}_{R_{k}}$, we can define $f_{v}: \mathfrak{X}_{\mathrm{pa}(v)} \times \mathcal{F}_{R_{k}} \rightarrow \mathfrak{X}_{v}$ for those $v$ with latent parents $u_{k-1}$ and $u_{k}$, and just $f_{v}: \mathfrak{X}_{\mathrm{pa}(v)} \rightarrow \mathfrak{X}_{v}$ otherwise. These functions $f_{R_{k-1}}$ can be integrated into $U_{k-1}$, and the process repeated for $i=k-2, \ldots, 1$.

We end up with latent variables $U_{i}$ taking values in $\mathcal{F}_{R_{i}}$ for $i=1, \ldots, k$. For example, with the first gearing given in Example 4.6 for the graph in Figure 4(a),

[^0]
[^0]:    ${ }^{6}$ Equivalently, one could take a deterministic function $f_{v}$ and introduce an "error term" $E_{v}$ so that $X_{v}=f_{v}\left(X_{\mathrm{pa}(v)}, E_{v}\right)$, as in the nonparametric structural equation models of Pearl (2009).

![img-6.jpeg](img-6.jpeg)

FIG. 7. (a) A DAG with functional latent variables, associated with a gearing of the mDAG in Figure 4(a). (b) Subgraph of the DAG in (a), containing the vertex 4 and its parents.
we would have $U_{1}=\left(f_{1}, f_{2}\right), U_{2}=\left(f_{3}, f_{4}\right)$ and $U_{3}=\left(f_{5}\right)$. Associating each variable $U_{i}$ with the vertex $u_{i}$ leads to the DAG in Figure 7(a). Notice that, for each $v \in V$, the function $f_{v}$ is contained within a parent variable of $v$. In addition, all the arguments of the function $f_{v}$ are also parents of $v$. For example, take $v=4$, whose parents are drawn separately in Figure 7(b). The function $f_{4} \in \mathcal{F}_{4}$ is generated as part of the latent variable $U_{2}=\left(f_{3}, f_{4}\right)$, and the associated vertex $u_{2}$ is indeed a parent of 4 . In addition, $\mathcal{F}_{4}=\left\{f: \mathfrak{X}_{2,3,6} \times \mathcal{F}_{5} \rightarrow \mathfrak{X}_{4}\right\}$, so the arguments of the function $f_{4}$, namely $X_{2}, X_{3}, X_{6}$ and $f_{5}$, all correspond to vertices which are also parents of 4 . Thus, in setting $X_{4}=f_{4}\left(X_{2}, X_{3}, X_{6}, f_{5}\right)$ we ensure that $X_{4}$ is a welldefined function of its parent variables.

In fact, using this construction we can set $X_{v}:=f_{v}\left(X_{\mathrm{pa}(v)}, f_{\pi(v)}\right)$ for every $v \in V$, which is well defined because the directed part of the original mDAG is acyclic. The following result shows that the resulting conditional distribution over $X_{V}$ given $X_{W}$ is in the marginal model for the original mDAG.

THEOREM 4.7. Let $\mathcal{G}$ be a geared mDAG, and $R_{i}, i=1, \ldots, k$ be the remainder sets corresponding to some gearing of $\mathcal{G}$. Suppose we generate functions $f_{v} \in \mathcal{F}_{v}$ according to a distribution in which

$$
\left(f_{v} \mid v \in R_{i}\right) \mathbb{L}\left(f_{w} \mid w \in V \backslash R_{i}\right), \quad i=1, \ldots, k
$$

and then define $X_{v}=f_{v}\left(X_{\mathrm{pa}(v)}, f_{\pi(v)}\right)$ for each $v \in V$. Then the induced conditional distribution on $X_{V}$ given $X_{W}$ is in the marginal model for $\mathcal{G}$.

Conversely, any distribution in the marginal model for $\mathcal{G}$ can be generated by such a scheme.

Proof. For each bidirected edge $B_{i}$, define the random variable $U_{i}=\left(f_{v} \mid\right.$ $v \in R_{i}$ ). The $U_{i} \mathrm{~s}$ are represented by exogenous variables on the DAG $\widetilde{\mathcal{G}}$, and the conditions given in the statement of the theorem ensures they are all independent. The structural equation property for $\widetilde{\mathcal{G}}$ will therefore be satisfied if each $X_{v}$ is a well-defined function of its parents in the graph.

In other words, the three components $f_{v}, f_{\pi(v)}$ and $X_{\mathrm{pa}(v)}$ must all be determined from random variables which are parents of $v$ in $\mathcal{G}$. This holds for $X_{\mathrm{pa}(v)}$ by definition. Additionally, $v \in R_{i}$ implies that $v \in B_{i}$, and that therefore the variable $U_{i} \equiv\left(f_{v}: v \in R_{i}\right)$ is a parent variable of $X_{v}$.

Lastly, suppose $w \in \pi(v)$; this happens if and only if $w, v \in B_{j}$ for some $j>i$, in which case $w \in R_{j}$ for the minimal such $j$ by the running intersection property of the gearing. Then $f_{w}$ is contained in $U_{j}$, which is also a parent variable of $X_{v}$.

For the converse, suppose that $p \in \mathcal{M}(\mathcal{G})$ satisfies the structural equation property and let $R_{k}$ be the final remainder set with associated random variable $U_{k}$. Each $X_{v}$ for $v \in R_{k}$ is a measurable function of its parents $X_{\mathrm{pa}(v)}$ and $U_{k}$. Define the random function $f_{v}: \mathfrak{X}_{\mathrm{pa}(v)} \rightarrow \mathfrak{X}_{v}$ by $f_{v}(\cdot)=X_{v}\left(\cdot, U_{k}\right)$, and incorporate it into the latent variable $U_{k}$. Repeating this for all $v \in R_{k}$ gives us $U_{k}^{\prime}=\left(U_{k}, f_{R_{k}}\right)$. By Theorem 2.2 of Čencov (1982), we can rewrite $U_{k}^{\prime}=\left(g\left(f_{R_{k}}, E\right), f_{R_{k}}\right)$ for some measurable function $g$ and random variable $E$, independent of $f_{R_{k}}$, whilst keeping the distribution of $U_{k}^{\prime}$ unchanged.

Since $\mathcal{G}$ is geared, all children of $U_{k}$ that are also children of any other latent variable all share a latent parent, say $U_{j}, j<k$. If we then augment $U_{j}$ with $E$, and replace $U_{k}^{\prime}$ with $U_{k}^{\prime \prime} \equiv f_{R_{k}}$, then all variables remain as measurable functions of their parents because $f_{w}\left(X_{\mathrm{pa}(w)}, U_{k}, U_{j}\right)$ can be replaced with $f_{w}\left(X_{\mathrm{pa}(w)}, g\left(U_{k}^{\prime \prime}, E\right), U_{j}\right)$. Now that $U_{k}^{\prime \prime}$ has a fixed, finite state-space, we can apply this process again to $U_{k-1}$. A simple induction gives the result.

Since each of these latent variables takes values in a finite collection of functions, this means that the marginal model of a geared graph is equivalent to a latent variable model in which all the random variables (latent and observed) are finite and discrete. It follows from the Tarski-Seidenberg theorem [Basu, Pollack and Roy (1996), Chapter 2] that marginal models for geared mDAGs are semialgebraic sets.

Example 4.8. Consider the marginal model for the graph in Figure 3(b). In this case, the vertices 2 and 4 are each contained in only one bidirected edge, so without loss of generality this edge could be replaced in the canonical DAG (Figure 1) with a latent variable taking values in $\mathcal{F}_{2} \times \mathcal{F}_{4}$ where

$$
\mathcal{F}_{2} \equiv\left\{f: \mathfrak{X}_{1} \rightarrow \mathfrak{X}_{2}\right\}, \quad \mathcal{F}_{4} \equiv\left\{f: \mathfrak{X}_{3} \rightarrow \mathfrak{X}_{4}\right\}
$$

That is, the latent variable may be assumed to be $U=\left(f_{2}, f_{4}\right)$, where $f_{2}$ and $f_{4}$, respectively, assign values to $X_{2}$ and $X_{4}$ given particular values of $X_{1}$ and $X_{3}$.

For nongeared graphs such as that in Figure 8(a), there is no clear way to write the marginal model as a latent variable model without possible loss of generality. We therefore cannot use this approach to prove that marginal models corresponding to nongeared mDAGs are semi-algebraic. However, it has recently been

proven that any marginal model can be written as a latent variable model with finite discrete latent states, provided the state-space is sufficiently large (Denis Rosset, personal communication). It follows that all marginal models are semi-algebraic.
4.4. Generating distributions for geared mDAGs. Let $\mathcal{G}$ be a single-district, geared mDAG, with gearing given by remainder sets $R_{1}, \ldots, R_{k}$; assign a probability distribution $\rho_{i}$ to each collection of functions $U_{i} \equiv\left(f_{v} \mid v \in R_{i}\right)$. Suppose we draw values for variables $U_{i}=\left(f_{v}\right)_{v \in R_{i}}$ independently according to $\rho_{i}$, and use them to generate values for the observed variables $X_{V}$ for each possible value of the fixed vertices $X_{W}$. The resulting (conditional) distribution over $X_{V}$ given $X_{W}$ is, by Theorem 4.7, in the marginal model for $\mathcal{G}$.

Let $\pi\left(R_{i}\right) \equiv \bigcup_{v \in R_{i}} \pi(v)$ and $f_{A} \equiv\left(f_{v} \mid v \in A\right)$. Define

$$
\begin{aligned}
& p\left[\rho_{k}, \ldots, \rho_{1}\right]\left(x_{V} \mid x_{W}\right) \\
& \quad=\sum_{f_{R_{k}} \in \Phi_{k}\left(x_{V W}\right)} \rho_{k}\left(f_{R_{k}}\right) \cdots \sum_{f_{R_{1}} \in \Phi_{1}\left(f_{\pi\left(R_{1}\right)}, x_{V W}\right)} \rho_{1}\left(f_{R_{1}}\right)
\end{aligned}
$$

where

$$
\Phi_{i}\left(f_{\pi\left(R_{i}\right)}, x_{V W}\right)=\left\{f_{R_{i}} \mid f_{v}\left(x_{\mathrm{pa}(v)}, f_{\pi(v)}\right)=x_{v} \text { for each } v \in R_{i}\right\}
$$

that is, $\Phi_{i}\left(f_{\pi\left(R_{i}\right)}, x_{V W}\right)$ is precisely the set of functions $f_{R_{i}}$ that, given the indicated values of parent variables, jointly evaluate to $x_{R_{i}}$. Hence (6) is a sum over all the combinations of functions $f_{V}$ that, given the input $X_{W}=x_{W}$, recursively evaluate to $x_{V}$.

The function $p[\cdot]$ takes distributions over the functions $f_{V}$ and returns a kernel over $\mathfrak{X}_{V}$ indexed by $\mathfrak{X}_{W}$. For brevity, we will generally denote this by $p\left[\rho_{k}, \ldots, \rho_{1}\right]=\sum_{\Phi_{k}} \rho_{k} \cdots \sum_{\Phi_{1}} \rho_{1}$, with the dependence upon $x_{V W}$ left implicit. It may be helpful to think of this as an over-parameterized family of kernels for $X_{V}$ given $X_{W}$, with parameters $\rho_{1}, \ldots, \rho_{k}$.

The mapping $p[\cdot]$ is clearly smooth (infinitely differentiable), and its image defines the marginal model. Hence we will be able to deduce various aspects of the model's geometry by studying $p[\cdot]$ and its derivatives. Choosing $\rho_{i}\left(f_{R_{i}}\right)=1$ for each $i$ (up to a constant of proportionality which, for simplicity, we do not write explicitly) induces the uniform distribution on $\mathfrak{X}_{V}$ for each $x_{W} \in \mathfrak{X}_{W}$; we denote this kernel by $p_{0} \equiv p[1, \ldots, 1]$. Clearly, $p_{0}$ is contained within $\mathcal{M}(\mathcal{G})$ for any mDAG $\mathcal{G}$-as, in fact, is any distribution corresponding to all variables being independent.

Example 4.9. For the instrumental variables model in Figure 6 (if we consider $X_{1}$ to be fixed), we have

$$
p[\rho]\left(x_{2}, x_{3} \mid x_{1}\right)=\sum_{\Phi\left(x_{123}\right)} \rho\left(f_{2}, f_{3}\right)
$$

where $\Phi\left(x_{123}\right)=\left\{\left(f_{2}, f_{3}\right): f_{2}\left(x_{1}\right)=x_{2}, f_{3}\left(x_{2}\right)=x_{3}\right\}$.

EXAMPLE 4.10. In the case of the mDAG in Figure 4(a), we have three bidirected edges and remainder sets, and the gearing used in Figure 7(a) gives

$$
p\left[\rho_{3}, \rho_{2}, \rho_{1}\right]=\sum_{\Phi_{3}} \rho_{3}\left(f_{5}\right) \sum_{\Phi_{2}} \rho_{2}\left(f_{3}, f_{4}\right) \sum_{\Phi_{1}} \rho_{1}\left(f_{1}, f_{2}\right)
$$

where

$$
\begin{aligned}
& \Phi_{1}=\left\{\left(f_{1}, f_{2}\right) \mid f_{1}=x_{1}, f_{2}\left(f_{3}, f_{4}\right)=x_{2}\right\} \\
& \Phi_{2}=\left\{\left(f_{3}, f_{4}\right) \mid f_{3}\left(x_{1}\right)=x_{3}, f_{4}\left(x_{2}, x_{3}, x_{6}, f_{5}\right)=x_{4}\right\} \\
& \Phi_{3}=\left\{f_{5} \mid f_{5}\left(x_{3}\right)=x_{5}\right\}
\end{aligned}
$$

5. Main results. In this section, we prove our main result, by showing that the marginal model $\mathcal{M}(\mathcal{G})$ has the same dimension as the nested model. This is done first for geared mDAGs, and the result is then extended to general graphs. For geared graphs, the marginal model is just the image of the infinitely differentiable function $p[\cdot]$ described in the previous section. Such functions can be locally approximated at a particular point, say $p_{0}=p[1, \ldots, 1]$, by the linear map given by the derivative of $p[\cdot]$.

This column space of this linear map (also called the pushforward map) gives the linear space that approximates the model at $p_{0}$, also known as the tangent space. ${ }^{7}$ We will show that the tangent space to the marginal model at $p_{0}$ is equal to the tangent space of the nested model $\mathcal{N}(\mathcal{G})$ at $p_{0}$. To do this, we take a basis of the tangent space of $\mathcal{N}(\mathcal{G})$, and for every vector $\lambda$ in the basis we explicitly construct a vector $\delta$ such that the directional derivative of $p[\cdot]$ with respect to $\delta$ is equal to $\lambda$. This shows that each $\lambda$ is also contained in the tangent space of $\mathcal{M}(\mathcal{G})$. Since the marginal model is contained within the nested model, it will then follow from results in algebraic geometry that the two models coincide in a neighbourhood of $p_{0}$.

For nongeared graphs, we have do slightly more work, showing that we can combine maps from different geared subgraphs to obtain the same result.
5.1. Vector spaces and tangent cones. A probability kernel $p\left(x_{V} \mid x_{W}\right)$ can be thought of equally as a vector with entries indexed by $\mathfrak{X}_{V W}$, or a real function with domain $\mathfrak{X}_{V W}$. The following decomposition of the vector space $\mathbb{R}^{\left|\mathfrak{X}_{V}\right|}$ will prove useful.

DEFINITION 5.1. For any $A \subseteq V$, let $\Lambda_{A}$ be the subspace of $\mathbb{R}^{\left|\mathfrak{X}_{V}\right|}$ consisting of vectors $p$ such that:
(i) $\sum_{y_{a} \in \mathfrak{X}_{a}} p\left(y_{a}, x_{V \backslash a}\right)=0$ for each $a \in A$ and $x_{V \backslash\{a\}} \in \mathfrak{X}_{V \backslash\{a\}}$;
(ii) $p\left(x_{V}\right)=p\left(y_{V}\right)$ whenever $x_{A}=y_{A}$.

[^0]
[^0]:    ${ }^{7}$ In general, the column space could be a subspace of the tangent space, but it is a consequence of Theorem 5.3 that they are equal in this case.

In other words, considered as a function $p: \mathfrak{X}_{V} \rightarrow \mathbb{R}$, the value of $p \in \Lambda_{A}$ only depends upon $x_{A}$, and its sum over $x_{a}$ for $a \in A$ (keeping the other arguments fixed) is 0 . In particular, $\Lambda_{\varnothing}$ is the subspace spanned by the vector of 1 s . The dimension of $\Lambda_{A}$ is $\prod_{a \in A}\left(\left|\mathfrak{X}_{a}\right|-1\right)$; in the case where all the variables are binary, each $\Lambda_{A}$ has dimension one and is the same as the space spanned by the corresponding column of a log-linear design matrix.

It is simple to check that the spaces $\Lambda_{A}$ are all orthogonal, and that the real vector space $\mathbb{R}^{\left|\mathfrak{X}_{V}\right|}$ can be decomposed as the direct sum

$$
\mathbb{R}^{\left|\mathfrak{X}_{V}\right|}=\bigoplus_{A \subseteq V} \Lambda_{A}
$$

DEFINITION 5.2. Let $\mathfrak{A}$ be a subset of $\mathbb{R}^{k}$ containing a point $\boldsymbol{x}$. The tangent cone of $\mathfrak{A}$ at $\boldsymbol{x}$ is the set of vectors of the form $\boldsymbol{v}=\lim _{n \rightarrow \infty} \alpha_{n}\left(\boldsymbol{v}_{n}-\boldsymbol{x}\right)$ where $\alpha_{n} \rightarrow \infty$ and each $\boldsymbol{v}_{n} \in \mathfrak{A}$.

A tangent cone is a cone, but may or may not be a vector space, depending upon whether the set $\mathfrak{A}$ is regular at $\boldsymbol{x}$. If $\mathfrak{A}$ is defined by the image of a differentiable bijective map with differentiable inverse then the tangent cone is a vector space, and the same as the image of the pushforward map. This is the case with the nested model $\mathcal{N}(\mathcal{G})$, which has an explicit and smooth parameterization [Evans and Richardson (2015)]. Its tangent cone at the uniform distribution $p_{0}$ is

$$
\mathrm{TS}_{0}^{n} \equiv \bigoplus_{A \in \mathcal{A}(\mathcal{G})} \Lambda_{A}
$$

where $\mathcal{A}(\mathcal{G})$ are the parameterizing sets; this can be deduced by looking directly at the parameterization.

As noted in Section 4, any marginal model $\mathcal{M}(\mathcal{G})$ also contains the uniform distribution $p_{0}\left(x_{V} \mid x_{W}\right) \equiv\left|\mathfrak{X}_{V}\right|^{-1}$, for all $x_{V} \in \mathfrak{X}_{V}, x_{W} \in \mathfrak{X}_{W}$, at which point all variables are jointly independent. The tangent cone of the marginal model $\mathcal{M}(\mathcal{G})$ at $p_{0}$ is also the vector space (8), which forms the main result of this section.

THEOREM 5.3. The tangent cone of $\mathcal{M}(\mathcal{G})$ at $p_{0}$, denoted $\mathrm{TC}_{0}$, is the vector space $\mathrm{TC}_{0}=\mathrm{TS}_{0}^{n} \equiv \bigoplus_{A \in \mathcal{A}} \Lambda_{A}$.

That $\mathrm{TC}_{0} \subseteq \mathrm{TS}_{0}^{n}$ follows from the fact that $\mathcal{M}(\mathcal{G}) \subseteq \mathcal{N}(\mathcal{G})$. The proof of the reverse inclusion is the subject of this section. We first show this for geared graphs in Section 5.2 then extend to general mDAGs in Section 5.3, culminating in the proof of Theorem 1.2.

# 5.2. Results for geared graphs. 

DEFINITION 5.4. Let $\lambda: \mathfrak{X}_{A} \rightarrow \mathbb{R}$; we say that $\lambda$ is $A$-degenerate (or just degenerate) if for each $a \in A$, and $x_{A \backslash a} \in \mathfrak{X}_{A \backslash a}$,

$$
\sum_{y_{a}} \lambda\left(y_{a}, x_{A \backslash a}\right)=0
$$

It is not hard to see that the set of $A$-degenerate functions is isomorphic to the vector space $\Lambda_{A}$; both formulations will be useful.

DEFINITION 5.5. Given a degenerate function $\varepsilon_{i}: \mathcal{F}_{R_{i}} \rightarrow \mathbb{R}$, define

$$
D_{i}\left(\varepsilon_{i}\right)=\lim _{\eta \downarrow 0} \eta^{-1}\left\{p\left[1, \ldots, 1+\eta \varepsilon_{i}, \ldots, 1\right]-p[1, \ldots, 1, \ldots, 1]\right\}
$$

so that $D_{i}\left(\varepsilon_{i}\right)$ is a vector in $\mathbb{R}^{\left|\mathcal{X}_{V W}\right|}$, the directional derivative of the $i$ th component of $p[\cdot]$ with respect to $\varepsilon_{i}$. For sufficiently small $\eta>0$, the vector $1+\eta \varepsilon_{i}$ is nonnegative and, therefore, a valid distribution over $\mathcal{F}_{R_{i}}$ (up to the normalizing constant); it follows that $D_{i}\left(\varepsilon_{i}\right) \in \mathrm{TC}_{0}$, the tangent cone of $\mathcal{M}(\mathcal{G})$ at $p_{0}$.

Let $T_{i}=\left\{D_{i}\left(\varepsilon_{i}\right) \mid \varepsilon_{i}\right.$ degenerate $\}$. Since the function $p[\cdot]$ is differentiable at $[1, \ldots, 1]$, it follows that $T_{i}$ is a vector space, and also that the vector space $T_{1}+$ $\cdots+T_{k}$ is contained within the tangent cone of $\mathcal{M}$ at the uniform distribution. We will show that $T_{1}+\cdots+T_{k}$ is in fact the same as (8).

It will be useful to define the following collection of supersets of $\Phi_{i}$, for $B \subseteq V$ :

$$
\Phi_{i}^{B}\left(f_{\pi\left(R_{i}\right)}, x_{V W}\right) \equiv\left\{f_{R_{i}} \mid f_{v}\left(x_{\mathrm{pa}(v)}, f_{\pi(v)}\right)=x_{v} \text { for each } v \in R_{i} \cap B\right\}
$$

In words, this is the collection of functions $f_{R_{i}}$ such that, given inputs $f_{\pi\left(R_{i}\right)}$ and $x_{\operatorname{pa}\left(R_{i}\right) \backslash R_{i}}$, the values of $f_{B \cap R_{i}}$ jointly evaluate to $x_{B \cap R_{i}}$. Note that $\Phi_{i}^{B}=\Phi_{i}$ for any $B \supseteq R_{i}$.

LEMMA 5.6. Let $C \subseteq R_{i}$, with sterile ${ }_{\mathcal{G}}(C) \subseteq A \subseteq C \cup \mathrm{pa}_{\mathcal{G}}(C)$ and $E \subseteq \pi(C)$. Then for every degenerate function $\lambda: \mathfrak{X}_{A} \times \mathcal{F}_{E} \rightarrow \mathbb{R}$, there exists a degenerate function $\delta: \mathcal{F}_{C} \rightarrow \mathbb{R}$ such that

$$
\sum_{f_{R_{i}} \in \Phi_{i}} \delta\left(f_{C}\right)=\lambda\left(x_{A}, f_{E}\right)
$$

where $\Phi_{i}$ is given by (7). In addition,

$$
\sum_{f_{R_{i}} \in \Phi_{i}^{B}} \delta\left(f_{C}\right)= \begin{cases}\left|\mathfrak{X}_{R_{i} \backslash B}\right| \lambda\left(x_{A}, f_{E}\right) & \text { if } C \subseteq B \\ 0 & \text { otherwise }\end{cases}
$$

The proof is in the Supplementary Material, Section B. 3 [Evans (2018)].
REMARK 5.7. Note that if we set $E=\varnothing$, the above result shows that for any $\lambda \in \Lambda_{A}$ there exists a $\delta$ such that

$$
\begin{aligned}
\eta^{-1} & \{p[1, \ldots, 1+\eta \delta, \ldots, 1]-p[1, \ldots, 1, \ldots, 1]\} \\
& =\eta^{-1}\left\{\sum_{\Phi_{k}} \cdots \sum_{\Phi_{i}} \eta \delta\left(f_{C}\right) \sum_{\Phi_{i-1}} \cdots \sum_{\Phi_{1}} 1\right\} \\
& =\lambda
\end{aligned}
$$

Hence $\Lambda_{A} \leq T_{i}$ (i.e., $\Lambda_{A}$ is a subspace of the vector space $T_{i}$ ) for any $A$ such that sterile ${ }_{\mathcal{G}}(C) \subseteq A \subseteq C \cup \mathrm{pa}_{\mathcal{G}}(C)$ and $C \subseteq R_{i}$.

The next result, also proved in the Supplementary Material [Evans (2018), Section B.3], forms the backbone for proving Theorem 5.3: it extends Lemma 5.6 to sets $C$ that are not contained within a single remainder set.

LEMMA 5.8. Let $C$ be a bidirected-connected set, and for each $i$ define $C_{i} \equiv C \cap R_{i} ;$ let $I \equiv\left\{i \mid C_{i} \neq \varnothing\right\}$. For sterile ${ }_{\mathcal{G}}\left(C_{i}\right) \subseteq A_{i} \subseteq C_{i} \cup \mathrm{pa}_{\mathcal{G}}\left(C_{i}\right)$, let $A=\bigwedge_{i \in I} A_{i}$. Then $\Lambda_{A}$ is a subspace of $T_{l}$, where $l$ is the minimal element of $I$.

COROLLARY 5.9. For a geared $m D A G \mathcal{G}$ with $k \geq 1$ bidirected edges,

$$
\bigoplus_{A \in \mathcal{A}(\mathcal{G})} \Lambda_{A} \leq T_{1}+\cdots+T_{k}
$$

Proof. By Lemma 3.6, there is some bidirected-connected set $C$ such that $A=\bigwedge_{v \in C} A_{v}$ for sets $\{v\} \subseteq A_{v} \subseteq\{v\} \cup \mathrm{pa}_{\mathcal{G}}(v)$. Take $C_{i} \equiv C \cap R_{i}=$ $\left\{v_{i 1}, \ldots, v_{i k_{i}}\right\}$, so $A$ is of the form

$$
A=\bigwedge_{i, j} A_{i}^{j}=\bigwedge_{i}\left(\bigwedge_{j} A_{i}^{j}\right)
$$

where $A_{i}^{j} \equiv A_{v_{i j}}$ (here we have changed nothing other than to label the vertices $v_{i j}$ by which remainder set they are contained in).

Applying Lemma 3.6 in reverse to the bidirected-connected set $C_{i}$ shows that $A_{i} \equiv \bigwedge_{j} A_{i}^{j}$ is in $\mathcal{A}(\mathcal{G})$ and, therefore, satisfies sterile ${ }_{\mathcal{G}}\left(C_{i}\right) \subseteq A_{i} \subseteq C_{i} \cup \mathrm{pa}_{\mathcal{G}}\left(C_{i}\right)$. Then by Lemma 5.8, the space $\Lambda_{A}$ is contained in some $T_{i}, i=1, \ldots, k$.

EXAMPLE 5.10. The instrumental variables model from Figure 6 (see Examples 4.5 and 4.9) has a saturated nested model with the following parameterizing sets:


Indeed, taking the functional parameterization suggested in Example 4.9, one can see that altering the distribution of the compliance functions $f_{2}$ will affect the distribution of $X_{2}$ conditional on $X_{1}$, which is why $\Lambda_{2}$ and $\Lambda_{12}$ are contained in $\mathrm{TC}_{0}$. For example, to introduce a correlation between $X_{1}$ and $X_{2}$ whilst keeping the marginal distributions fixed, we can increase the proportion of "compliers"

[i.e., the people for whom $f_{2}(0)=0, f_{2}(1)=1$ ] and decrease the proportion of "defiers" $\left[f_{2}(0)=1, f_{2}(1)=0\right]$.

Similarly, modifying the distribution of $f_{3}$ gives us $\Lambda_{3}$ and $\Lambda_{23}$. Obtaining the directional derivatives in $\Lambda_{13}$ and $\Lambda_{123}$ requires modifying the distribution of $f_{2}$, $f_{3}$ jointly.

None of the examples given in this paper require the full generality of Lemma 5.8 to prove that Theorem 5.3 applies to them, however, an example in which this is necessary may be found in the Supplementary Material, Section B. 4 [Evans (2018)].
5.3. Extension to nongeared graphs. Corollary 5.9 puts us in a position to prove Theorem 5.3 for geared graphs; however, it does not so far extend to the general case, because we cannot fix the state-spaces of the latent variables without a gearing. In this section, we will show that the tangent cone of a general marginal model at the uniform distribution is the vector space spanned by the tangent cones of its geared subgraphs, and that therefore the problem can be reduced to geared graphs.

Proposition 5.11. Let $\mathcal{G}$ be an arbitrary $m D A G$ containing geared subgraphs $\mathcal{G}_{1}, \ldots, \mathcal{G}_{k}$. Suppose that, for each subgraph and a suitable gearing $\Lambda_{A_{i}} \leq$ $\mathrm{TC}_{0}\left(\mathcal{G}_{i}\right)$. Then $\Lambda_{A_{1}}+\cdots+\Lambda_{A_{k}} \leq \mathrm{TC}_{0}(\mathcal{G})$.

In other words, the tangent cone of $\mathcal{G}$ includes the vector space spanned by all the tangent cones of the subgraphs. The proof is found in the Supplementary Material, Section B. 5 [Evans (2018)].

Example 5.12. The bidirected 4-cycle in Figure 8(a) is not geared and, therefore, we cannot apply our earlier results to it directly. The nested model for this graph is equivalent to the model defined by the constraints $X_{1} \Perp X_{3}$ and $X_{2} \Perp X_{4}$, and has parameterizing sets

$$
\begin{aligned}
\mathcal{A}(\mathcal{G})= & \{\{1\},\{2\},\{1,2\},\{3\},\{2,3\},\{1,2,3\} \\
& \{4\},\{1,4\},\{1,2,4\},\{3,4\},\{1,3,4\},\{2,3,4\},\{1,2,3,4\}\}
\end{aligned}
$$

![img-7.jpeg](img-7.jpeg)

FIG. 8. (a) The bidirected 4-cycle, and (b), (c) two geared subgraphs.

which are also the bidirected-connected sets of vertices. The two subgraphs in Figures 8(b) and (c), say $\mathcal{G}_{1}$ and $\mathcal{G}_{2}$, are geared, however, and their parameterizing sets combined include all sets in $\mathcal{A}(\mathcal{G})$. Hence, by applying Proposition 5.11 with these graphs, we find that

$$
\bigoplus_{A \in \mathcal{A}(\mathcal{G})} \Lambda_{A}=\bigoplus_{A \in \mathcal{A}\left(\mathcal{G}_{1}\right)} \Lambda_{A}+\bigoplus_{A \in \mathcal{A}\left(\mathcal{G}_{2}\right)} \Lambda_{A} \leq \mathrm{TC}_{0}(\mathcal{G})
$$

It follows that the marginal model is also defined by the independences $X_{1} \Perp X_{3}$ and $X_{2} \Perp X_{4}$, possibly with some additional inequality constraints.

We are now in a position to put together these ideas and prove the main results for general mDAGs.

Proof of ThEOREM 5.3. Suppose first that $\mathcal{G}$ is geared.
$p\left[1, \ldots, 1+\eta \varepsilon_{i}, \ldots, 1\right]$ obeys the nested Markov property for any degenerate function $\varepsilon_{i}$ and any $\eta$ sufficiently small that $1+\eta \varepsilon_{i}$ is positive; it follows that $T_{i} \leq \mathrm{TC}_{0}$ for each $i$, and that therefore using Corollary 5.9,

$$
\bigoplus_{A \in \mathcal{A}(\mathcal{G})} \Lambda_{A} \leq T_{1}+\cdots+T_{k}
$$

is also contained in $\mathrm{TC}_{0}$, by the differentiability of $p[\cdot]$ at $(1, \ldots, 1)$.
Now for general $\mathcal{G}$, and each $A \in \mathcal{A}(\mathcal{G})$, there exists a geared subgraph $\mathcal{G}^{\prime}$ of $\mathcal{G}$ such that $\Lambda_{A} \leq \mathrm{TC}_{0}\left(\mathcal{G}^{\prime}\right)$ by Lemma 4.3. Then applying Proposition 5.11, we see that the space spanned by these subspaces is contained within the tangent cone for $\mathcal{G}$ : that is, $\bigoplus_{A \in \mathcal{A}(\mathcal{G})} \Lambda_{A} \leq \mathrm{TC}_{0}(\mathcal{G})$. If a distribution is in the marginal model, then it is also in the nested model and, therefore, $\mathrm{TC}_{0}$ is contained within the tangent space $\mathrm{TS}_{0}^{n}$ of $\mathcal{N}(\mathcal{G})$ at $p_{0}$, which has dimension

$$
\operatorname{dim}\left(\mathrm{TS}_{0}^{n}\right)=\sum_{H \in \mathcal{H}(\mathcal{G})}\left|\mathfrak{X}_{T(H)}\right| \prod_{h \in H}\left(\left|\mathfrak{X}_{h}\right|-1\right)=\sum_{A \in \mathcal{A}(\mathcal{G})} \operatorname{dim}\left(\Lambda_{A}\right)
$$

the second equality here follows from $\operatorname{dim}\left(\Lambda_{A}\right)=\prod_{h \in A}\left(\left|\mathfrak{X}_{h}\right|-1\right)$ and

$$
\sum_{H \subseteq A \subseteq H \cup T} \operatorname{dim}\left(\Lambda_{A}\right)=\sum_{H \subseteq A \subseteq H \cup T} \prod_{h \in A}\left(\left|\mathfrak{X}_{h}\right|-1\right)=\left|\mathfrak{X}_{T(H)}\right| \prod_{h \in H}\left(\left|\mathfrak{X}_{h}\right|-1\right)
$$

Combining $\bigoplus_{A \in \mathcal{A}(\mathcal{G})} \Lambda_{A} \leq \mathrm{TC}_{0} \subseteq \mathrm{TS}_{0}^{n}$ with the dimension of $\mathrm{TS}_{0}^{n}$ gives the result.

Theorem 1.2 is now a corollary of this result.
Proof of ThEOREM 1.2. Since $\mathcal{N}(\mathcal{G})$ is parametrically defined via polynomials, its Zariski closure is an irreducible variety [see, e.g., Cox, Little and O'Shea (2007), Proposition 4.5.5]. The Zariski closure of $\mathcal{M}(\mathcal{G})$ is, by definition, also an algebraic variety. For algebraic varieties $V_{1}, V_{2}$, if $V_{1} \subseteq V_{2}$ and $V_{2}$ is irreducible,

then either $V_{1}$ has a strictly smaller dimension than $V_{2}$, or they are identical. By Theorem 5.3, the Zariski closures of $\mathcal{M}$ and $\mathcal{N}$ have the same dimension and, therefore, they coincide. This means that, in a neighbourhood of $p_{0}$, the models themselves are also the same.
6. Smoothness of the marginal model. The results of Section 5, together with the smoothness of the nested model, allow us to show that for geared graphs, the interior of the marginal model is a smooth manifold.

THEOREM 6.1. For any $m D A G \mathcal{G}$ and state-space $\mathfrak{X}_{V W}$, the relative interior of the marginal model $\mathcal{M}(\mathcal{G})$ is a manifold of dimension $d\left(\mathcal{G}, \mathfrak{X}_{V W}\right)$, and is described by a finite number of semi-algebraic constraints.

Proof. The nested Markov model is parametrically defined (with a polynomial parameterization) and, therefore, its Zariski closure is an irreducible variety [see, e.g., Cox, Little and O'Shea (2007), Proposition 4.5.5]. Furthermore, Evans and Richardson (2015) give a diffeomorphism between the set of strictly positive distributions obeying the nested Markov property, and an open parameter set. It follows that $\mathcal{N}(\mathcal{G})$ is a manifold on the interior of the simplex [see, e.g., Kass and Vos (1997), Appendix A].

As noted in Section 4, the marginal model is a semi-algebraic set. Since $\mathcal{M}(\mathcal{G}) \subseteq \mathcal{N}(\mathcal{G})$ and these two sets have the same Zariski closure, it follows that $\mathcal{M}(\mathcal{G})$ is defined from $\mathcal{N}(\mathcal{G})$ by a finite number of additional polynomial inequalities. It further follows that it is also a manifold at any point these inequality constraints are not active.

It follows from Theorem 6.1 that the interior of the marginal model for an mDAG is a curved exponential family of dimension $d\left(\mathcal{G}, \mathfrak{X}_{V W}\right)$, and that therefore the nice statistical properties of these models can be applied. For example, the maximum likelihood estimator (MLE) of a distribution within the model will be asymptotically normal and unbiased, and the likelihood ratio statistic for testing this model has an asymptotic $\chi^{2}$-distribution.

For a point on the boundary defined by an active inequality constraint, the asymptotic distribution of the likelihood ratio statistic may be much more complicated than for a point on the relative interior [Drton (2009)]; in general it is a mixture of $\chi^{2}$-distributions, and this mixture will vary depending upon the unknown truth. A possible advantage of the nested model is that we can guarantee that the true distribution does not lie on the boundary of $\mathcal{N}$ if the MLE consists of strictly positive probabilities, because the boundary only consists of distributions with at least some zero probabilities; the same cannot be said for $\mathcal{M}$. This is depicted in Figure 9, in which the MLE under the nested model $\left(\hat{p}_{n}\right)$ is in the interior of $\mathcal{N}$, but the MLE for the marginal model $\hat{p}_{m}$ lies on the boundary of $\mathcal{M}$.

![img-8.jpeg](img-8.jpeg)

FIG. 9. Diagramatic representation of estimation with the marginal model. The thicker line represents the marginal model, and its thinner extension the nested model. The unconstrainted MLE is shown as $\hat{p}$, and its projection to MLEs under the marginal and nested models as $\hat{p}_{m}$ and $\hat{p}_{n}$, respectively. Note that $\hat{p}_{m}$ is on the boundary of $\mathcal{M}$; if the true data generating distribution is on the boundary this generally leads to irregular asymptotics.

Inequality constraints are generally much more complicated than equality constraints, and efforts to characterize them fully in DAGs with latent variable models have been limited by computational challenges; see, for example, the discussion in ver Steeg and Galstyan (2011).
6.1. Why marginal models? Theorem 4.7 tells us that we can use an explicit latent variable model with potential outcomes to obtain the marginal model for any geared graph; in this event, one might ask why we need the constraint-based representation afforded by the nested model. Unfortunately, whilst often useful for causal inference, potential outcomes are impractical to use as a full parameterization in all but the smallest models, because their state-space quickly becomes infeasibly large if there are several treatments or several possible outcomes. In the simplest case of two variables $A \rightarrow Y$ with with respectively $m$ and $n$ states, there are $n^{m}$ possible types for $Y$, compared to only $m n$ distinct, observable outcomes. In reality, $m$ is often quite large, because $Y$ may have several parents.

Example 6.2. Consider a longitudinal treatment program where at each stage $t=1, \ldots, N$, patients are given treatment $A_{t}$ and an outcome $Y_{t}$ is measured. Treatments are chosen by clinicians to depend only on the treatment and outcome at the previous time point, but outcomes are correlated due to unobserved confounding. For $N=2$, this is similar to Example 1.1.

Following the same approach as in Example 4.4 leads to a latent variable consisting of random functions $f_{t}$ that map values of treatments $A_{t}$ onto potential outcomes $Y_{t}$; see Figure 10 for a graph of the relevant latent variable model. For the simplest case of binary variables, each of these functions would have four states; the full latent variable would consist of all $N$ such functions, so would have $4^{N}$ possible states. This latent variable identifies the quantity $P\left(Y_{1}, \ldots, Y_{N} \mid \operatorname{do}\left(A_{1}, \ldots, A_{N}\right)\right)$, which is the distribution of $Y_{1}, \ldots, Y_{N}$ after intervening on $A_{1}, \ldots, A_{N}$; this has a dimension of "only" $\frac{2}{3}\left(4^{N}-1\right)$ under this model, and the difference between these two models grows exponentially in $N$.

![img-9.jpeg](img-9.jpeg)

FIG. 10. Bayesian network representing the dynamic treatment model in Example 6.2.

If $Y_{t}$ depends on $k>1$ treatments, then the problem becomes much worse, as $f_{t}$ requires $2^{2^{k}}$ states. This leads to a latent variable of dimension $O\left(2^{2^{k} T}\right)$ on a contingency table of dimension just $2^{2 T}$.

How would alternative approaches deal with this model? An ancestral graph model [Richardson and Spirtes (2002)] would replace the latent variable with directed edges $Y_{i} \rightarrow Y_{j}$ for each $i<j$ and and $A_{i} \rightarrow Y_{j}$ for each $i \leq j$. As such, it would throw away most of the structural information about causal relationships, and give a model of significantly larger dimension.

An ordinary latent variable model (i.e., without explicit potential outcomes) could reduce the dimension by using fewer states, and would eventually lead to an identified model. However, as we have already seen in the Introduction, there is no way to achieve identifiability in this example without imposing additional equality constraints; in many contexts, including epidemiological examples such as the one above, there is typically no domain knowledge about the hidden variables that would justify such assumptions. They are also difficult to test because the additional constraints are not generally explicitly available, and goodness-of-fit statistics such as likelihood ratio tests do not have the same asymptotic distribution at all points in the parameter space [Drton (2009)].

By contrast, the marginal model (and therefore the nested model) has the correct dimension, which is never larger than the relevant contingency table, and does not impose any constraints not explicitly implied by the Bayesian network model. The discrete nested model is identified everywhere and has a smooth parameterization, and can easily be fitted by maximum likelihood using the algorithm in Evans and Richardson (2010). In addition, the parameterization is made up of precisely of the identifiable causal quantities from the model. For large $N$, the marginal model may still result in a model that is too large for a particular dataset; in this case, further parametric constraints or simplifying assumptions such as additivity, sparsity or symmetry can easily be placed on parameters that are identifiable [see Shpitser et al. (2013) for an example of this]. Unlike a latent variable model, these additional assumptions would lead to a transparent reduction in dimension, do not lead to new questions about identifiability and can be tested directly.

6.2. Quantum causal models. In the Quantum Information literature, there is interest in models where the latent variables are replaced with quantum states or other, even more general objects [see Henson, Lal and Pusey (2014) and references therein]. This can result in larger models, most famously as quantum violations of Bell's inequalities [see Gill (2014) for a statistical introduction]. However, as a consequence of results by Henson, Lal and Pusey (2014), nested constraints also apply to quantum models, and hence the quantum model is also of the same dimension as the nested and marginal models.

Acknowledgements. We thank Angelos Armen for a very close reading and substantial comments, as well as the Associate Editor and several anonymous referees for excellent suggestions to improve the clarity of the paper.

# SUPPLEMENTARY MATERIAL 

Supplement to "Margins of discrete Bayesian networks" (DOI: 10.1214/17AOS1631SUPP; .pdf). Technical proofs and some additional examples are contained in the supplement.
