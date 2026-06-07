# Implicit inequality constraints in a binary tree model 

Piotr Zwiernik<br>Institute for Pure and Applied Mathematics, 460 Portola Plaza, Box 957121,<br>Los Angeles, CA 90095-7121<br>e-mail: piotr.zwiernik@gmail.com

and

Jim Q. Smith<br>University of Warwick<br>Department of Statistics<br>CV7AL, Coventry, UK<br>e-mail: j.q.smith@warwick.ac.uk


#### Abstract

In this paper we investigate the geometry of a discrete Bayesian network whose graph is a tree all of whose variables are binary and the only observed variables are those labeling its leaves. We provide the full geometric description of these models which is given by a set of polynomial equations together with a set of complementary implied inequalities induced by the positivity of probabilities on hidden variables. The phylogenetic invariants given by the equations can be useful in the construction of simple diagnostic tests. However, in this paper we point out the importance of also incorporating the associated inequalities into any statistical analysis. The full characterization of these inequality constraints derived in this paper helps us determine how and why routine statistical methods can break down for this model class.


AMS 2000 subject classifications: Primary 62H05, 62E15; secondary 60K99, 62F99.
Keywords and phrases: Graphical models on trees, binary data, tree cumulants, semialgebraic statistical models, phylogenetic invariants, inequality constraints.

Received October 2010.

## Contents

1 Introduction ..... 1277
2 Tree models and tree cumulants ..... 1280
3 Inferential issues related to the semialgebraic description ..... 1285
4 Explicit expression of implied inequality constraints ..... 1289
5 Example: The quartet tree model ..... 1294
6 Discussion ..... 1295
Acknowledgments ..... 1296

A Change of coordinates ..... 1296
B Proofs ..... 1298
C The proof of the main theorem ..... 1300
D Phylogenetic invariants ..... 1308
References ..... 1310

# 1. Introduction 

A Bayesian network whose graph is a tree all of whose inner nodes represent variables which are not directly observed defines an important class of models containing both phylogenetic tree models and hidden Markov models. Inference for this model class tends to be challenging and often needs to employ fragile numerical algorithms. In [40] we established a useful new coordinate system to analyze such models when all of the variables are binary. This reparametrization enabled us not only to address various identifiability issues but also helped us to derive exact formulae for the maximum likelihood estimators given that the sample proportions were in this model class.

However, as well as making identifiability issues more transparent and open to systematic analysis, this new coordinate system can be also used to analyze the global structure of tree models. In particular, it enables us to obtain the full description of these models in terms of implicit polynomial equations and inequalities. Knowing this full semi-algebraic description is extremely useful when used in conjunction with the identifiability structure as discussed in [40]. We explain in Section 3 how this study impacts the stability of the maximum likelihood and Bayesian estimation procedures within the class of phylogenetic tree models. It is also helpful in the construction of tree diagnostics and model selection procedures within this class.

This paper builds on the results in [12] where some partial understanding of the analytic approach to the maximum likelihood estimation was presented. The problem here is that routinely fitted phylogenetic models often violate the inequality constraints defining the model. One effect of this phenomenon is then that the maximum likelihood estimators (MLEs) usually lie on to the boundaries of the parameter space (see Section 3 for an example). In a full Bayesian analysis it will make the ensuing inference about probabilities highly sensitive to the settings of prior distributions on the parameters (see [32, 33]). This, in turn, automatically interferes with the appropriate functioning of model selection algorithms. For example Bayes Factor scores will be highly influenced again by priors. On the other hand more classical methods like for example AIC or BIC algorithms, when used routinely, misbehave because many of the MLEs will lie on the boundary of the feasible region since usual dimension counting penalties are implicitly too large (see [38]). For these and other reasons explained in more detail in Section 3, the inequality conditions are of considerable practical importance.

This paper is part of an explosion of work which apply techniques in algebraic geometry to study and develop statistical methodologies. The particular geometric study of tree models was first introduced by Lake [21], and Cavender

![img-0.jpeg](img-0.jpeg)

Fig 1. The graphical representation of the tripod tree model.
and Felsenstein [9]. This research was initially focused on so called phylogenetic invariants. These are algebraic relationships expressed as a set of polynomial equations over the observed probability tables which must hold for a given phylogenetic model to be valid. We note that these algebraic techniques have also been embraced by computational algebraic geometers $[2,17,37]$ enhancing statistical and computational analysis of such models [7] (see also [1] and references therein).

The main technical deficiency of using phylogenetic invariants alone in this way is that they do not give a full geometric description of the statistical model. However, the additional inequalities obtained as the main result of this paper complete this description. Where and how these inequality constraints can helpfully supplement an analysis based on phylogenetic invariants is illustrated by the simple example given below.

Example 1.1. Let $T$ be the tripod tree in Figure 1 where we use the convention that observed nodes are depicted by black nodes. The inner node represents a binary hidden variable $H$ and the leaves represent binary observable variables $X_{1}, X_{2}, X_{3}$. The model is given by all probability distributions $p_{\alpha}$ for $\alpha \in\{0,1\}^{3}$ such that

$$
p_{\alpha}=\theta_{0}^{(H)} \prod_{i=1}^{3} \theta_{\alpha_{i} \mid 0}^{(i)}+\theta_{1}^{(H)} \prod_{i=1}^{3} \theta_{\alpha_{i} \mid 1}^{(i)}
$$

where $\theta_{i}^{(H)}=\mathbb{P}(H=i)$ for $i=0,1$ and $\theta_{j \mid k}^{(i)}=\mathbb{P}\left(X_{i}=j \mid H=k\right)$ for $i=1,2,3$ and $j, k=0,1$. The model has full dimension over the space of observed marginal distributions $\left(X_{1}, X_{2}, X_{3}\right)$ and consequently there are no non-trivial equalities defining it. However, it is not a saturated model since not all the marginal probability distributions over the observed vector $\left(X_{1}, X_{2}, X_{3}\right)$ lie in the model class. For example Lazarsfeld and Henry [23, Section 3.1] showed that the second order moments of the observed distribution must satisfy

$$
\operatorname{Cov}\left(X_{1}, X_{2}\right) \operatorname{Cov}\left(X_{1}, X_{3}\right) \operatorname{Cov}\left(X_{2}, X_{3}\right) \geq 0
$$

Together with many other constraints we derive later, this constraint, which clearly impacts the inferences we might want to make (see Section 3), is not acknowledged through the study of phylogenetic invariants. Therefore inference based solely on these invariants is incomplete. For example naive estimates de-

rived through these methods can be infeasible within the model class in a sense illustrated later in this paper.

This example and the discussion of some inferential issues discussed above motivated the closer investigation of the semi-algebraic features associated with the geometry of binary tree models with hidden inner nodes. The main problem with the geometric analysis of these models is that, in general, it is hard to obtain all the inequality constraints defining a model explicitly even for very simple examples (see [15, Section 4.3], [18, Section 7]). Despite this, some results can be found in the literature. A binary naive Bayes model was studied by Auvray et al. [3]. There are also some partial results for general tree structures on binary variables given by Pearl and Tarsi [27] and Steel and Faller [36]. The most important applications in biology involve variables that can take four values. Recently Matsen [24] gave a set of inequalities in this case for group-based phylogenetic models (additional symmetries are assumed) using the Fourier transformation of the raw probabilities. Here we provide a simpler and more statistically transparent way to express the constrained space.

The semialgebraic description we obtain here also has an elegant mathematical structure. For example [8] gave an intriguing correspondence between, on the one hand, a correlation system on tree models and on the other distances induced by trees where the length between two nodes in a tree is given as a sum of the length of edges in the path joining them. The new coordinate system for tree models that we introduced in [40] enables us to explore in detail this relationship between probabilistic tree models (also called the tree decomposable distributions in [27]) and tree metrics and extend these results.

It has been known for some time that the constraints on possible distances between any two leaves in the tree imply some additional inequality constraints on the possible covariances between the binary variables represented by the leaves. These inequalities, given in (16), follow from the four-point condition ([29], Definition 7.1.5) together with some other simple non-negativity constraints. By using our new parametrization we are able to show in this paper that these two types of inequality constraints cannot be sufficient to describe the model class. Thus any probability distribution in the model class must satisfy many other additional constraints involving higher order moments. Using our methods we are able to provide the full set of the defining constraints in Theorem 4.7. This is given by a list of polynomial equations and inequalities which describe the set of all probability distributions in the model.

The paper is organized as follows. In Section 2 we briefly introduce general Markov models. We then proceed to describe a convenient new change of coordinates for these models given in [40]. In the new coordinate system the parametrization of the model has an elegant product form. We use this to obtain the full semi-algebraic description of a simple naive Bayes model. In Section 3 we discuss various ways in which an awareness of these implicit inequalities can enrich a statistical analysis of this model class. In Section 4 we state our main theorem and illustrate how it can be used. In Section 5 we discuss these results for a simple quartet tree model.

# 2. Tree models and tree cumulants 

We begin by defining and reviewing a new coordinate system for tree models and demonstrate how it can be used to provide a better understanding of this model class. We list the main results from our previous paper [40] and link it to the results presented in the next sections.

Parametrizations based on moments are one way of providing a structured model a structure more amenable to an algebraic analysis (see [4, 14]). This approach has proved particularly effective in the presence of hidden data (see [31]) since then the analysis of a particular marginal distributions over a subset of the observed variables can be specified as a function of the joint moments containing that subset only. On the other hand when a model class is defined by a set of conditional independences further insight may be provided by reparametrizing to other functions of these moments to elegantly represent this additional underlying structure. These functions typically resemble cumulants.

One useful property of standard cumulants is that joint cumulants always vanish whenever the random vector under analysis can be split into two independent subvectors. Here we exploit analogous property using a reparametrization customized to the topology of a particular tree. These tree cumulants are introduced in [40]. They vanish only if some of the edges in the defining tree model are missing. This corresponds to the marginal independence of the leaves of two connected components of the induced forest. The property follows from a more general result in [39, Proposition 4.3] and partly explains the elegant product-like structure of the resulting parametrization in Proposition 2.3.

In this paper we assume that random variables are binary taking values either 0 or 1 . We consider models with hidden variables, i.e. variables whose values are never directly observed. The vector $Y$ has as its components all variables in the graphical model, both those that are observed and those that are hidden. The subvector of $Y$ of observed variables is denoted by $X$ and the subvector of hidden variables by $H$. A (directed) tree $T=(V, E)$, where $V$ is the set of vertices (or nodes) and $E \subseteq V \times V$ is the set of edges of $T$, is a connected (directed) graph with no cycles. A rooted tree is a directed tree that has one distinguished vertex called the root, denoted by the letter $r$, and all the edges are directed away from $r$. A rooted tree is usually denoted by $T^{r}$. For each $v \in V$ by $\mathrm{pa}(v)$ we denote the node preceding $v$ in $T^{r}$. In particular $\mathrm{pa}(r)=\emptyset$. A vertex of $T$ of degree one is called a leaf. A vertex of $T$ that is not a leaf is called an inner node.

Let $T$ denote an undirected tree with $n$ leaves and let $T^{r}=(V, E)$ denote $T$ rooted in $r \in V$. A Markov process on a rooted tree $T^{r}$ is a sequence $\left\{Y_{v}\right.$ : $v \in V\}$ of random variables such that for each $\alpha=\left(\alpha_{v}\right)_{v \in V} \in\{0,1\}^{V}$ its joint distribution satisfies

$$
p_{\alpha}(\theta)=\theta_{\alpha_{r}}^{(r)} \prod_{v \in V \backslash r} \theta_{\alpha_{v} \mid \alpha_{\mathrm{pa}(v)}}^{(v)}
$$

where $\theta_{\alpha_{r}}^{(r)}=\mathbb{P}\left(Y_{r}=\alpha_{r}\right)$ and $\theta_{\alpha_{v} \mid \alpha_{\mathrm{pa}(v)}}^{(v)}=\mathbb{P}\left(Y_{v}=\alpha_{v} \mid Y_{\mathrm{pa}(v)}=\alpha_{\mathrm{pa}(v)}\right)$. Since $\theta_{0}^{(r)}+\theta_{1}^{(r)}=1$ and $\theta_{0 \mid i}^{(v)}+\theta_{1 \mid i}^{(v)}=1$ for all $v \in V \backslash\{r\}$ and $i=0,1$ then the set of parameters consists of exactly $2|E|+1$ free parameters: we have two parameters:

$\theta_{1 \mid 0}^{(v)}, \theta_{1 \mid 1}^{(v)}$ for each edge $(u, v) \in E$ and one parameter $\theta_{1}^{(r)}$ for the root. We denote the parameter space by $\Theta_{T}=[0,1]^{2|E|+1}$ and the Markov process on $T^{r}$ by $\widetilde{\mathcal{M}}_{T}$. Remark 2.1. The reason to omit the root $r$ in the notation is that this model does not depend on the rooting and is equivalent to the undirected graphical model given by global Markov properties on $T$. To prove this note that $T^{r}$ is a perfect directed graph and hence by [22, Proposition 3.28] parametrization in (1) is equivalent to factorization with respect to $T$. Since $T$ is decomposable, by [22, Proposition 3.19], this factorization is equivalent to the global Markov properties.

Let $\Delta_{2^{n}-1}=\left\{p \in \mathbb{R}^{2^{n}}: \sum_{\beta} p_{\beta}=1, p_{\beta} \geq 0\right\}$ with indices $\beta$ ranging over $\{0,1\}^{n}$ be the probability simplex of all possible distributions of $X=$ $\left(X_{1}, \ldots, X_{n}\right)$ represented by the leaves of $T$. We assume now that all the inner nodes represent hidden variables. Equation (1) induces a polynomial map $f_{T}: \Theta_{T} \rightarrow \Delta_{2^{n}-1}$ obtained by marginalization over all the inner nodes of $T$

$$
p_{\beta}(\theta)=\sum_{\mathcal{H}} \theta_{\alpha_{r}}^{(r)} \prod_{v \in V \backslash r} \theta_{\alpha_{v} \mid \alpha_{\mathrm{pa}(v)}}^{(v)}
$$

where $\mathcal{H}$ is the set of all $\alpha \in\{0,1\}^{V}$ such that the restriction to the leaves of $T$ is equal to $\beta$. We let $\mathcal{M}_{T}=f_{T}\left(\Theta_{T}\right)$ denote the general Markov model over the set of observable random variables (c.f. [29, Section 8.3]).

A semialgebraic set in $\mathbb{R}^{d}$ is a finite union of sets given by a finite number of polynomial equations and inequalities. Since $\Theta_{T}$ is a semialgebraic set and $f_{T}$ is a polynomial map then by [5, Proposition 2.2.7] $\mathcal{M}_{T}$ is a semialgebraic set as well. Moreover, if $f$ is a polynomial isomorphism from $\Delta_{2^{n}-1}$ to another space then $f\left(\mathcal{M}_{T}\right)$ is also a semialgebraic set. The semialgebraic description of $f\left(\mathcal{M}_{T}\right)$ in $f\left(\Delta_{2^{n}-1}\right)$ gives the semialgebraic description of $\mathcal{M}_{T}$.

The idea behind tree cumulants was to define a polynomial isomorphism from $\Delta_{2^{n}-1}$ to the space of new coordinates $\mathcal{K}_{T}$. We defined a partially ordered set (poset) of all the partitions of the set of leaves induced by removing edges of the given tree $T$. Then tree cumulants are given as a function of probabilities induced by a Möbius function on the poset. The details of this change of coordinates are given in Appendix A and are illustrated below.

The tree cumulants are given by $2^{n}-1$ coordinates: $n$ means $\lambda_{i}=\mathbb{E} X_{i}$ for all $i=1, \ldots, n$ and a set of real-valued parameters $\left\{\kappa_{I}: I \subseteq[n]\right.$ where $\left.|I| \geq 2\right\}$. Each formula for $\kappa_{I}$ is expressed as a function of the higher order central moments of the observed variables. These formulae are given explicitly in equation (19) of Appendix A. Since the change of coordinates is a polynomial isomorphism then, by [5, Proposition 2.2.7], the image of $\mathcal{M}_{T}$ in the space of tree cumulants, denoted by $\mathcal{M}_{T}^{\kappa}$, is a semialgebraic set. In this paper we provide the full semialgebraic description of $\mathcal{M}_{T}^{\kappa}$, that is the complete set of polynomial equations and inequalities involving the tree cumulants which describes $\mathcal{M}_{T}^{\kappa}$ as the subset of $\mathcal{K}_{T}$, for subsequent use in a statistical analysis of the model class.
Example 2.2. Consider the quartet tree model, i.e. the general Markov model given by the graph in Figure 2. The tree cumulants are given by 15 coordinates:

![img-1.jpeg](img-1.jpeg)

Fig 2. A quartet tree
$\lambda_{i}$ for $i=1,2,3,4$ and $\kappa_{I}$ for $I \subseteq[4]$ such that $|I| \geq 2$. Denoting $U_{i}=X_{i}-\mathbb{E} X_{i}$ we have $\kappa_{i j}=\mathbb{E} U_{i} U_{j}=\operatorname{Cov}\left(X_{i}, X_{j}\right)$ for $1 \leq i<j \leq 4$ and

$$
\kappa_{i j k}=\mathbb{E}\left(U_{i} U_{j} U_{k}\right)
$$

for all $1 \leq i<j<k \leq 4$ which we note is a third order central moment. However, in general tree cumulants of higher order cannot be equated with their corresponding central moments but only expressed as functions of them. These functions are obtained by performing an appropriate Möbius inversion. Thus for example from equation (19) in Appendix A we have that

$$
\kappa_{1234}=\mathbb{E}\left(U_{1} U_{2} U_{3} U_{4}\right)-\mathbb{E}\left(U_{1} U_{2}\right) \mathbb{E}\left(U_{3} U_{4}\right)
$$

Note that since the observed higher order central moments can be expressed as functions of probabilities, tree cumulants can also be expressed as functions of these probabilities.

Let $X_{\bar{i}}=\left(X_{1}, X_{2}, X_{3}, X_{4}\right) \backslash\left\{X_{i}\right\}$ for $i=1,2,3,4$. From [39, Proposition 4.3] it follows in particular that, like for the joint cumulant, $\kappa_{1234}=0$ whenever $X_{i} \Perp X_{\bar{i}}$ for any $i=1,2,3,4$ or $\left(X_{1}, X_{2}\right) \Perp\left(X_{3}, X_{4}\right)$. However, in general, $\kappa_{1234} \neq 0$ for example if $\left(X_{1}, X_{3}\right) \Perp\left(X_{2}, X_{4}\right)$ and hence tree cumulants differ from classical cumulants. Vanishing of the tree cumulants corresponds to an edge being missing in the particular defining tree. This generalizes for other trees and gives a heuristic explanation for the nice product-like parametrization presented in Proposition 2.3 below. We explain this now formally.

Let $T^{r}=(V, E)$ and let $\Omega_{T}$ denote the set of parameters with coordinates given by $\bar{\mu}_{v}$ for $v \in V$ and $\eta_{u, v}$ for $(u, v) \in E$. Define a reparametrization map $f_{\theta \omega}: \Theta_{T} \rightarrow \Omega_{T}$ as follows:

$$
\begin{array}{ll}
\eta_{u, v}=\theta_{1 \mid 1}^{(v)}-\theta_{1 \mid 0}^{(v)} & \text { for every }(u, v) \in E \text { and } \\
\bar{\mu}_{v}=1-2 \lambda_{v} & \text { for each } v \in V
\end{array}
$$

where $\lambda_{v}=\mathbb{E} Y_{v}$ is a polynomial in the original parameters $\theta$. To see this let $r, v_{1}, \ldots, v_{k}, v$ be a directed path in $T$. Then

$$
\lambda_{v}=\mathbb{P}\left(Y_{v}=1\right)=\sum_{\alpha \in\{0,1\}^{k+1}} \theta_{1 \mid \alpha_{k}}^{(v)} \theta_{\alpha_{k} \mid \alpha_{k-1}}^{(v_{k})} \cdots \theta_{\alpha_{r}}^{(r)}
$$

It can be easily checked that if $\operatorname{Var}\left(Y_{u}\right)>0$ then $\eta_{u, v}=\operatorname{Cov}\left(Y_{u}, Y_{v}\right) / \operatorname{Var}\left(Y_{u}\right)$. Hence $\eta_{u, v}$ is just the regression coefficient of $Y_{v}$ with respect to $Y_{u}$.

The parameter space $\Omega_{T}$ is given by the following constraints:

$$
\begin{aligned}
& -1 \leq \bar{\mu}_{r} \leq 1, \quad \text { and for each }(u, v) \in E \\
& -\left(1+\bar{\mu}_{v}\right) \leq\left(1-\bar{\mu}_{u}\right) \eta_{u, v} \leq\left(1-\bar{\mu}_{v}\right) \\
& -\left(1-\bar{\mu}_{v}\right) \leq\left(1+\bar{\mu}_{u}\right) \eta_{u, v} \leq\left(1+\bar{\mu}_{v}\right)
\end{aligned}
$$

In Appendix A we show that there is a polynomial isomorphism between $\Delta_{2^{n}-1}$ and the space of tree cumulants $\mathcal{K}_{T}$ giving the following diagram, where the dashed arrow denotes the induced parametrization.
![img-2.jpeg](img-2.jpeg)

One motivation behind this change of coordinates is that the induced parametrization $\psi_{T}: \Omega_{T} \rightarrow \mathcal{K}_{T}$ has a particularly elegant form.
Proposition 2.3 ([40], Proposition 4.1). Let $T$ be an undirected tree with $n$ leaves. Assume that $T$ is trivalent which here means that all of its inner nodes have degree at most three. Let $T^{r}=(V, E)$ be $T$ rooted in $r \in V$. Then $\mathcal{M}_{T}^{n}$ is parametrized by the map $\psi_{T}: \Omega_{T} \rightarrow \mathcal{K}_{T}$ given as $\lambda_{i}=\frac{1}{2}\left(1-\bar{\mu}_{i}\right)$ for $i=1, \ldots, n$ and

$$
\kappa_{I}=\frac{1}{4}\left(1-\bar{\mu}_{r(I)}^{2}\right) \prod_{v \in \operatorname{int}(V(I))} \bar{\mu}_{v}^{\operatorname{deg}(v)-2} \prod_{(u, v) \in E(I)} \eta_{u, v} \quad \text { for } I \subseteq[n],|I| \geq 2
$$

where the degree is taken in $T(I)=(V(I), E(I))$; int $(V(I))$ denotes the set of inner nodes of $T(I)$ and $r(I)$ denotes the root of $T^{r}(I)$.

Proposition 2.3 has been formulated for trivalent trees. However, it can be easily extended to the general case as explained in [40, Section 4].

This result enabled us to completely understand identifiability of tree models extending results in [10]. In particular [40, Theorem 5.4] identifies the cases when the model is identified up to label switching. This condition is rather technical and here we usually would recommend the use of the sufficient condition that all the covariances between the leaves are nonzero. Further results focus on the geometry of the unidentified space in the case when the identifiability fails. More importantly, [40, Corollary 5.5] gives us formulae for parameters given a probability distribution in the case when identifiability holds. This result gives us a closed-form formulae for MLEs in certain special cases (see Corollary 3.1).

To illustrate our technique we next obtain the full semialgebraic description of the tripod tree model. This result is not new (see e.g. $[3,30]$ and a special case given by [26, Theorem 3.1]). However, this allows us not only to unify notation but also to introduce the strategy we use to prove the general case. We begin with a definition.

Definition 2.4. Let $A$ be a $2 \times 2 \times 2$ table. The hyperdeterminant of $A$ as defined by Gelfand, Kapranov, Zelevinsky [19, Chapter 14] is given by

$$
\begin{aligned}
\operatorname{Det} A & =\left(a_{000}^{2} a_{111}^{2}+a_{001}^{2} a_{110}^{2}+a_{010}^{2} a_{101}^{2}+a_{011}^{2} a_{100}^{2}\right) \\
& -2\left(a_{000} a_{001} a_{110} a_{111}+a_{000} a_{010} a_{101} a_{111}+a_{000} a_{011} a_{100} a_{111}\right. \\
& +a_{001} a_{010} a_{101} a_{110}+a_{001} a_{011} a_{110} a_{100}+a_{010} a_{011} a_{101} a_{100} \\
& +4\left(a_{000} a_{011} a_{101} a_{110}+a_{001} a_{010} a_{100} a_{111}\right)
\end{aligned}
$$

If $\sum a_{i j k}=1$ then treating all entries formally as joint cell probabilities (without positivity constraints) we can simplify this formula using the change of coordinates to central moments. The reparametrizations in Appendix A are well defined for this extended space of probabilities and we have that

$$
\operatorname{Det} A=\mu_{123}^{2}+4 \mu_{12} \mu_{13} \mu_{23}
$$

which can be verified by direct computations.
From the construction of tree cumulants (c.f. Appendix A) it follows that $\kappa_{I}=\mu_{I}$ for all $I \subseteq[n]$ such that $2 \leq|I| \leq 3$. Henceforth, for clarity, these lower order tree cumulants will be written as their more familiar corresponding central moments.

Proposition 2.5 (The semialgebraic description of the tripod model). Let $\mathcal{M}_{3}$ be the general Markov model on a tripod tree $T$ rooted in any node of $T$. Let $P$ be a $2 \times 2 \times 2$ probability table for three binary random variables $\left(X_{1}, X_{2}, X_{3}\right)$ with central moments $\mu_{12}, \mu_{13}, \mu_{23}, \mu_{123}$ (equivalent to the corresponding tree cumulants) and means $\lambda_{i}$, for $i=1,2,3$. Then $P \in \mathcal{M}_{3}$ if and only if one of the following two cases occurs:
(i) $\mu_{123}=0$ and at least two of the three covariances $\mu_{12}, \mu_{13}, \mu_{23}$ vanish.
(ii) $\mu_{12} \mu_{13} \mu_{23}>0$ and

$$
\begin{aligned}
& \left|\mu_{j k}\right| \sqrt{\overline{\operatorname{Det} P}}-\mu_{123} \mu_{j k} \leq\left(1-\bar{\mu}_{i}\right) \mu_{j k}^{2} \\
& \left|\mu_{j k}\right| \sqrt{\overline{\operatorname{Det} P}}+\mu_{123} \mu_{j k} \leq\left(1+\bar{\mu}_{i}\right) \mu_{j k}^{2}
\end{aligned}
$$

for all $i=1,2,3$ where by $j, k$ we denote elements of $\{1,2,3\} \backslash i$.
Sketch of the proof. The proof is given in Appendix B. Here, for convenience, we give its outline. Denote by $\mathcal{M} \subseteq \Delta_{7}$ the family of distributions described by (i) and (ii). We need to show that $\mathcal{M}_{3}=\mathcal{M}$. To show that $\mathcal{M}_{3} \subseteq \mathcal{M}$ we use the parametrization in Proposition 2.3 to prove that either (i) holds or it does not, and then, inequalities in (ii) are equivalent to (5). To show the opposite inclusion we propose formulae for the parameters in terms of the observed distribution given by [40, Corollary 5.5], and show that this formulae agree with the parametrization in Proposition 2.3 up to the sign. The inequality $\mu_{12} \mu_{13} \mu_{23}>0$ assures that there is a choice of signs for the parameters such that the parametrization holds exactly.

All the points satisfying (i) correspond to submodels of $\mathcal{M}$ where some of the observed variables are independent of each other.

# 3. Inferential issues related to the semialgebraic description 

There are at least three reasons why the implicit inequality constraints of this model class can have a critical impact on a statistical analysis of this model class. First, used in conjunction with other geometric techniques these inequalities help us determine, whether or not the likelihood associated with a given tree model has multiple local maxima. Second, it gives us the basis for developing simple model diagnostics which complement those associated with implicit algebraic constraints. Finally, awareness of whether these constraints are active for given data set enables us to identify when standard numerical methods might fail both for estimation and model selection across different candidate trees. We consider and illustrate all these issues below.

Proposition 2.5 and Theorem 4.7 give explicit descriptions of tree models as subsets of the probability simplex and hence also as submodels of the multinomial model. The literature on constrained multinomial models (see [13] for a review) gives many examples of what may go wrong in this case. If the multiway marginal table of observed random variables is sampled at random then its likelihood will be given as the multinomial likelihood constrained to the model. The unconstrained multinomial likelihood is of course a very well-behaved function. In particular it is log-concave and its unique maximum is given by the sample proportions $\hat{p}$ as long as all the entries of $\hat{p}$ are nonzero. However, after constraining to the model this function may become much more complicated.

We know that unidentifiability of parameters causes estimation problems associated for example with multiple local maxima of the likelihood and the posterior density. However, because the constraints on the model do not define a convex region, the constrained likelihood will not necessarily have a unique maximum (see Figure 4). So even if we use ways of cleverly accounting for the aliasing caused by unidentifiability we can still be left with other multiple local solutions induced by the violations of the constraints. This, in turn, can make estimation schemes unstable. The discussion below complements results presented in [12].

If the unconstrained multinomial maximum likelihood estimator given by the sample proportions satisfies the equation but does not satisfy some of the inequalities then the MLE of the given tree model will always lie on the boundary of the parameter space $\Theta_{T}$. Of course, if all the inequalities hold but some of the equalities do not then, in principle, it is not such a serious problem as the estimates will typically lie in the interior of the parameter space. However, if there are even the smallest perturbations of the model class we are likely to be drawn outside the feasible region. This is a phenomenon observed in many applied analyzes of these models (see, e.g. [12]). This occurs even in the simple tripod tree above where the feasible region accounts for only $8 \%$ of $\Delta_{7}$. Of course simply sampling from the tree model itself will not identify this potential difficulty since such samples will automatically not violate the constraints in any significant way. But if the tree only approximately holds then we begin to encounter certain difficulties.

![img-3.jpeg](img-3.jpeg)

FIG 3. The space of all possible covariances $\mu_{12}, \mu_{13}, \mu_{23}$ for the tripod tree model in the case when $\lambda_{1}=\lambda_{2}=\lambda_{3}=\frac{1}{2}$ and $\mu_{123}$ is equal to 0,0 .005 and 0.02 (from left to right).
![img-4.jpeg](img-4.jpeg)

FIG 4. The multinomial likelihood and a submodel of the saturated model given by four disjoint regions. The four local maxima are obtained on boundaries of these regions.

Since the tripod tree model $\mathcal{M}_{3}$ is of full dimension there are no non-trivial phylogenetic invariants and so the feasible regions of the model class are purely associated with inequality constraints and so particularly straightforward. In Figure 3 we depict these constraints as they apply to the second order moments of the three observed variables given some typical values of the other coordinates. For example there are four components corresponding to four possible choices of signs for covariances satisfying $\mu_{12} \mu_{13} \mu_{23} \geq 0$.

We can now give an explicit illustration of the type of multimodality that can be induced in this context. The likelihood function $\ell: \Theta_{T} \rightarrow \mathbb{R}$ for the tripod tree model can be also treated as a function on $\Delta_{7}$ by $\ell(\theta)=\ell(p(\theta))$ in

which case it will be denoted by $\ell(p)$. Since we understand the parametrization $p: \Theta_{T} \rightarrow \Delta_{7}$ of $\mathcal{M}_{3}$ then understanding $\ell(p)$ gives us automatically understanding of $\ell(\theta)$. The advantage is that in this setting $\ell(p)$ is just obtained as the multinomial likelihood function $\ell(p)=\ell(p ; x)=\prod_{i j k} p_{i j k}^{x_{i j k}}$ constrained to the model as explained above. If $\hat{p}$ lies in the model class $\mathcal{M}_{3}$ then $\ell(p)$ has a unique maximum and the maxima of $\ell(\theta)$ can be obtained by mapping back $\hat{p}$ to the parameter space $\Theta_{T}$ by using [40, Equation (3)]. This result generalizes.

Corollary 3.1. Let $T=(V, E)$ be a phylogenetic tree with $n$ leaves and let $\mathcal{M}_{T}$ be the corresponding tree model. If $\hat{p} \in \mathcal{M}_{T}$ then [40, Corollary 5.5] gives the formulae for the maximum likelihood estimators. In the case when the number of MLEs is finite, there are always exactly $2^{|V|-n}$ MLEs which are equivalent up to switching labels of the hidden variables.

We have however argued that usually $\hat{p} \notin \mathcal{M}_{T}$. In this case there is potentially more than one local maximum of the constrained multinomial likelihood function. Let $\hat{p}$ the sample proportions for some observed data on three binary random variables. We have three possible scenarios:
(i) $\hat{p} \in \mathcal{M}_{3}$ and then $\ell(p)$ is unimodal.
(ii) $\hat{p} \notin \mathcal{M}_{3}$ and $\ell(p)$ is multimodal but there exists only one global maximum.
(iii) $\hat{p} \notin \mathcal{M}_{3}$ and $\ell(p)$ has multiple global maxima.

The situation in (iii) raises an interesting question related to the model identifiability. For every data point satisfying (iii) we are not able to identify the parameters using the maximum likelihood estimation even if we take into account the label switching problem.

Of course from the numerical point of view the situation in (ii) and (iii) may describe equally bad scenarios since in both cases the algorithms become unstable even for arbitrary large sample sizes. Thus suppose that a sample of size 10000 has been observed

By direct computations we check that all the constraint in Proposition 2.5 hold apart from $\mu_{12} \mu_{13} \mu_{23} \geq 0$ and hence $\hat{p}$ does not lie in $\mathcal{M}_{3}$. The corresponding parameters will lie on the boundary of the parameter space. We performed the following simulation. We sampled uniformly from $\Theta_{T}=[0,1]^{7}$ the starting parameters for the EM algorithm and noted the results of the EM approximation. For 100 iterations the procedure found four different isolated maxima given in Table 1 .

Up to label switching on the inner node these are two distinct maximizers of the log-likelihood function $\ell(\theta)$ corresponding to rows 1,3 . The value of the log-likelihood function, computed as $\sum_{i j k} x_{i j k} \log p_{i j k}$, is equal to -18387 and -18917 respectively. Both points correspond to somewhat degenerate tripod tree models where one of the observed variables is functionally related to the hidden variable. For example the first point lies on the submodel given by $X_{1} \Perp X_{3} \mid X_{2}$. We performed a similar analysis for other data points for which

TABLE 1
Results of the EM algorithm


only $\mu_{12} \mu_{13} \mu_{23} \geq 0$ fails and three different EM maximizers were often found. In every case the maximizers corresponded to degenerate submodels. In conjunction with [40, Theorem 5.4] we also have data for which the likelihood function $\ell(\theta)$ is maximized over an infinite number of points. This for example holds for any data such that the constrained multinomial likelihood is maximized over a point such that $p_{0 i j}=\lambda p_{1 i j}$ for some $\lambda$ and each $i, j=0,1$. In this case $\mu_{12}=\mu_{13}=0$ and the MLEs form a set of a positive dimension by [40, Theorem 5.4].

We note that the whole discussion above remains valid for more general tree models. The conditional independence properties of tree models imply that, since any three leaves are separated by an inner node, the corresponding marginal distributions form a tripod tree model. Demanding that tripod tree constraints must be satisfied by all triples of observed random variables cuts out all but a small proportion of the probability simplex. Furthermore by Theorem 4.7 we know that, in addition, many other constraints involving higher order moments will also apply. Therefore, the types of issues we illustrated above become increasingly critical for inference on trees, which in practical applications are of a much higher dimension. Thus real-world data will typically satisfy all the constraints defining the model very rarely. This, in turn, tends to result in multimodality of the likelihood function and MLEs lying on the boundary of the parameter space.

By acknowledging the existence of the inequality constraints we have already demonstrated how graphical methods can be used to identify why and where the fitted tree model might be flawed. Most naively, when samples are very large we could calculate the sample moments and notice which inequality constraints are active on the data set presented. When these lie outside these regions then we have strong information that the fitted tree model is inappropriate and we can expect there to be problems with both estimation - as illustrated above and model selection. Slightly more sophisticatedly we could also compare the model MLE: constrained as it is by these inequalities, with the MLE in the saturated model. Likelihood ratio statistics can then be used to measure the extent of the model inaccuracy. Of course this comparison can be performed directly. However, then we lose the geometrical insight as to exactly why and how the model is failing. This insight will be helpful in guiding us in identifying alternative models that might better explain the data. We note that the likelihood ratio statistics for a constrained multinomial model against the saturated model in general will not asymptotically have the $\chi^{2}$ distribution (see e.g. [11]). If the constrains are linear then the underlying distribution is called the chi-bar

squared distribution (see [13]). The situation is however much more complicated for tree models since here the constraints define a union of non-convex bodies. In the end of Section 4 we provide a short discussion on a description of $\mathcal{M}_{T}$ in terms of convex sets.

Inequalities are also relevant for the model choice. Suppose that the sufficient statistic does not satisfy some inequalities for each of the models under analysis. Then asymptotic model selection techniques like BIC can mislead. The effective parameter size will be miscounted because at least some of the MLEs will lie of the boundary of the space (see e.g. [28, 38]). Model selection based on Bayes factors will also tend to be unrobust. Since the estimates lie on the boundary the marginal likelihood for each of the models depends heavily on the tail behavior of the prior distribution on that boundary. See [32] and [33] for explanations of why this is so. For example a standard choice of a prior distribution for conditional distributions in tree models is the Dirichlet distribution. However, for different choices of its prior parameters the Bayes factors generated by the prior tails can be very different. Note that within the Bayesian paradigm the sampling of the tripod tree is straightforward once we recognize the constraint structure using a simple importance sampler generating samples from $\Delta_{7}$ and rejecting if they do not satisfy the defining inequalities. Of course this is not the only way of specifying a prior density for selecting between the saturated model and the tree model. However, our suggestion is very simple to implement and its inferential consequences are more transparent than more conventional methods using default priors within the conventional probabilitistic parametrization, where the selection can be highly dependent on the tails of priors.

# 4. Explicit expression of implied inequality constraints 

In this section we discuss the geometry of general tree models. First, we use some links to tree metrics to provide a simple set of algebraic constraints on the model space. Then, in Theorem 4.7, we provide the complete semialgebraic description for this model class.

Let $T=(V, E)$ be a general undirected tree with $n$ leaves and $T^{r}$ the tree $T$ rooted in $r \in V$. Before stating the main theorem of the paper we first show how to obtain an elegant set of necessary constraints on $\mathcal{M}_{T}$. In this section we assume that $\bar{\mu}_{v}^{2} \neq 1$ and $\eta_{u, v} \neq 0$ for all $(u, v) \in E$. By [40, Remark 4.3], this implies that $\bar{\mu}_{v}^{2} \neq 1$ for all $v \in V$. Since $\operatorname{Var}\left(Y_{u}\right)=\frac{1}{2}\left(1-\bar{\mu}_{u}^{2}\right)$ the correlation between $Y_{u}$ and $Y_{v}$ is defined as $\rho_{u v}=\frac{4 \mu_{u v}}{\sqrt{\left(1-\bar{\mu}_{u}^{2}\right)\left(1-\bar{\mu}_{v}^{2}\right)}}$. This gives

$$
\rho_{u v}=\eta_{u, v} \sqrt{\frac{1-\bar{\mu}_{u}^{2}}{1-\bar{\mu}_{v}^{2}}}=\eta_{v, u} \sqrt{\frac{1-\bar{\mu}_{v}^{2}}{1-\bar{\mu}_{u}^{2}}}
$$

Lemma 4.1. For any $i, j \in[n]$ let $E(i j)$ be the set of edges on the unique path joining $i$ and $j$ in $T$. Then

$$
\rho_{i j}=\prod_{(u, v) \in E(i j)} \rho_{u v}
$$

for each probability distribution in $\mathcal{M}_{T}^{n}$ such that all the correlations are well defined.
Proof. By (7) applied to $T(i j)$ we have $\mu_{i j}=\frac{1}{4}\left(1-\bar{\mu}_{r}^{2}\right) \prod_{(u, v) \in E(i j)} \eta_{u, v}$, where $r$ is the root of the path between $i$ and $j$ and hence

$$
\rho_{i j}=\sqrt{\frac{1-\bar{\mu}_{r}^{2}}{1-\bar{\mu}_{i}^{2}}} \sqrt{\frac{1-\bar{\mu}_{r}^{2}}{1-\bar{\mu}_{j}^{2}}} \prod_{(u, v) \in E(i j)} \eta_{u, v}
$$

Now apply (11) to each $\eta_{u, v}$ in the product above to show (12).
The above equation allows us to demonstrate an interesting reformulation of our problem in term of tree metrics (c.f. [29, Section 7]) which we explain below (see also Cavender [8]).
Definition 4.2. A function $\delta:[n] \times[n] \rightarrow \mathbb{R}$ is called a tree metric if there exists a tree $T=(V, E)$ with the set of leaves given by $[n]$ and with a positive real-valued weighting $w: E \rightarrow \mathbb{R}_{>0}$ such that for all $i, j \in[n]$

$$
\delta(i, j)= \begin{cases}\sum_{e \in E(i j)} w(e), & \text { if } i \neq j \\ 0, & \text { otherwise }\end{cases}
$$

Let now $d: V \times V \rightarrow \mathbb{R}$ be a map defined as

$$
d(k, l)= \begin{cases}-\log \left(\rho_{k l}^{2}\right), & \text { for all } k, l \in V \text { such that } \rho_{k l} \neq 0 \\ +\infty, & \text { otherwise }\end{cases}
$$

then $d(k, l) \geq 0$ because $\rho_{k l}^{2} \leq 1$ and $d(k, k)=0$ for all $k \in V$ since $\rho_{k k}=1$. If $K \in \mathcal{M}_{T}^{n}$ then by (12) $\rho_{i j}^{2}=\prod_{e \in E(i j)} \rho_{e}^{2}$ and we can define map $d_{(T ; K)}$ : $[n] \times[n] \rightarrow \mathbb{R}$

$$
-\log \left(\rho_{i j}^{2}\right)=d_{(T ; K)}(i, j)= \begin{cases}\sum_{(u, v) \in E(i j)} d(u, v), & \text { if } i \neq j \\ 0, & \text { otherwise }\end{cases}
$$

This map is a tree metric by Definition 4.2. In our case we have a point in the model space defining all the second order correlations and $d_{(T ; K)}(i, j)$ for $i, j \in[n]$. The question is: What are the conditions for the "distances" between leaves so that there exists a tree $T$ and edge lengths $d(u, v)$ for all $(u, v) \in E$ such that (13) is satisfied? Or equivalently: What are the conditions on the absolute values of the second order correlations in order that $\rho_{i j}^{2}=\prod_{e \in E_{i j}} \rho_{e}^{2}$ (for some edge correlations) is satisfied? We have the following theorem.
Theorem 4.3 (Tree-Metric Theorem, Buneman [6]). A function $\delta:[n] \times[n] \rightarrow$ $\mathbb{R}$ is a tree metric on $[n]$ if and only if for every four (not necessarily distinct) elements $i, j, k, l \in[n]$,

$$
\delta(i, j)+\delta(k, l) \leq \max \{\delta(i, k)+\delta(j, l), \delta(i, l)+\delta(j, k)\}
$$

Moreover, a tree metric defines the tree uniquely.

This theorem gives us a set of explicit constraints on the distributions in a tree model. Since $\delta(i, j)=\log \left(-\rho_{i j}\right)$ the constraints in Theorem 4.3 translate in terms of correlations to

$$
-\log \left(\rho_{i j}^{2} \rho_{k l}^{2}\right) \leq-\min \left\{\log \left(\rho_{i k}^{2} \rho_{j l}^{2}\right), \log \left(\rho_{i l}^{2} \rho_{j k}^{2}\right)\right\}
$$

Since $\log$ is a monotone function we obtain

$$
\min \left\{\frac{\rho_{i k}^{2} \rho_{j l}^{2}}{\rho_{i j}^{2} \rho_{k l}^{2}}, \frac{\rho_{i l}^{2} \rho_{j k}^{2}}{\rho_{i j}^{2} \rho_{k l}^{2}}\right\}=\min \left\{\frac{\mu_{i k}^{2} \mu_{j l}^{2}}{\mu_{i j}^{2} \mu_{k l}^{2}}, \frac{\mu_{i l}^{2} \mu_{j k}^{2}}{\mu_{i j}^{2} \mu_{k l}^{2}}\right\} \leq 1
$$

for all not necessarily distinct leaves $i, j, k, l \in[n]$. Hence, using the relation between correlations and tree metrics given in [8] we managed to provide a set of simple semialgebraic constraints on the model. Furthermore, later in Theorem 4.7 we show that these constraints are not the only active constraints on the model $\mathcal{M}_{T}$. Before we present this theorem it is helpful to make some simple observations about the relationship between correlations and probabilistic tree models.

Since $\rho_{u v}$ can have different signs we define a signed tree metric as a tree metric with an additional sign assignment for each edge of $T$.

Lemma 4.4. Let $T$ be a tree with set of leaves $[n]$. Suppose that we have a map $\sigma:[n] \times[n] \rightarrow\{-1,1\}$. Then there exists a map $s_{0}: E \rightarrow\{-1,1\}$ such that for all $i, j \in[n]$

$$
\sigma(i, j)=\prod_{(u, v) \in E(i j)} s_{0}(u, v)
$$

if and only if for all triples $i, j, k \in[n] \sigma(i, j) \sigma(i, k) \sigma(j, k)=1$.
The proof is given in Appendix B.
The following proposition gives a set of simple constraints on probability distribution in tree models. This may be particularly useful in practice since it involves only computing pairwise margins of the data and it enables us to check if a data point may come from a phylogenetic tree model.
Proposition 4.5. Let $P \in \Delta_{2^{n}-1}$ be a probability distribution. If $P \in \mathcal{M}_{T}$ for some tree $T$ with $n$ leaves then

$$
0 \leq \min \left\{\frac{\mu_{i k} \mu_{j l}}{\mu_{i j} \mu_{k l}}, \frac{\mu_{i l} \mu_{j k}}{\mu_{i j} \mu_{k l}}\right\} \leq 1
$$

for all (not necessarily distinct) $i, j, k, l \in[n]$ whenever $\mu_{i j}, \mu_{k l} \neq 0$.
Proof. Lemma 4.4 implies that for all $i, j, k \in[n]$ necessarily $\mu_{i j} \mu_{i k} \mu_{j k} \geq 0$. This in particular implies that $\frac{\mu_{i k} \mu_{j l}}{\mu_{i j} \mu_{k l}} \geq 0$ for all $i, j, k, l \in[n]$. By taking the square root in (14) these constraints can be combined to give the inequalities in (16).

In Theorem 4.7 we show that (16) provides the complete set of inequality constraints on $\mathcal{M}_{T}$ that involve only second order moments in their expression.

The fact that additional constraints involving higher order moments exist is illustrated in the following simple example.

Example 4.6. Consider the tripod tree model in Proposition 2.5. Let $K$ be a point in $\mathcal{K}_{T}$ given by $\lambda_{i}=0.15$ for $i=1,2,3, \mu_{i j}=0.0625$ (or equivalently $\left.\rho_{i j}=0.49\right)$ for each $i<j$ and $\mu_{123}=0.0526$. This point lies in the space of tree cumulants $\mathcal{K}_{T}$ which can be checked by mapping back the central moments to probabilities, since the resulting vector $\left[p_{\alpha}\right]$ lies in $\Delta_{7}$.

Clearly $K$ satisfies all the tree metric constraints in (16). The equation (12) is satisfied with $\rho_{h i}=0.7$ for each $i=1,2,3$. We now show that despite this $K \notin \mathcal{M}_{T}^{n}$. For if $K \in \mathcal{M}_{T}^{n}$ then we could find $\bar{\mu}_{h}$ and $\eta_{h, i}$ satisfying constraints in (5) so that (21) held. Using the formulae in [40, Corollary 5.5] it is easy to compute that $\bar{\mu}_{h}=0.86$ and $\eta_{h, i} \approx 0.98$. However, $K$ is not in the model since these parameters do not lie in $\Omega_{T}$. Indeed,

$$
\left(1+\bar{\mu}_{h}\right) \eta_{h, i} \approx 1.8228>\left(1+\bar{\mu}_{i}\right)=1.7
$$

and hence (5) is not satisfied.
The consequence of the fact that the parameters do not lie in $\Omega_{T}$ is that this parametrization does not lead to a valid assignment of conditional probabilities to the edges of the tree. For example with the values given above we can calculate that the induced marginal distribution for $\left(X_{i}, H\right)$ would have to satisfy $\mathbb{P}\left(X_{i}=0, H=1\right)=-0.0043$ which is obviously not a consistent assignment for a probability model. Thus, there must exist other constraints involving observed higher order moments that need to hold for a probability model to be valid. We note that for the tripod tree these were given by Proposition 2.5.

The following theorem gives the complete set of constraints which have to be satisfied by tree cumulants to lie in $\mathcal{M}_{T}$ in the case when $T$ is a trivalent tree. Let $P \in \Delta_{2^{n}-1}$ be the probability distribution of the vector $\left(X_{1}, \ldots, X_{n}\right)$ then for any $i, j, k \in[n]$ let $P^{i j k}$ denote the $2 \times 2 \times 2$ table of the marginal distribution of $\left(X_{i}, X_{j}, X_{k}\right)$.

Theorem 4.7. Let $T=(V, E)$ be a trivalent tree with $n$ leaves and $\mathcal{M}_{T} \subseteq$ $\Delta_{2^{n}-1}$ be the model defined as an image of the parametrization in (2). Suppose $P$ is a joint probability distribution on $n$ binary variables. Then $P \in \mathcal{M}_{T}$ if and only if the following conditions hold:
(C1) For each edge split $A \mid B$ (c.f. Definition A.1) of the set of leaves of $T$ whenever we have four nonempty subsets (not necessarily disjoint) $I_{1}, I_{2} \subseteq$ $A, J_{1}, J_{2} \subseteq B$ then

$$
\kappa_{I_{1} J_{1}} \kappa_{I_{2} J_{2}}-\kappa_{I_{1} J_{2}} \kappa_{I_{2} J_{1}}=0
$$

(C2) For all $1 \leq i<j<k \leq n$ the corresponding marginal distribution $P^{i j k}$ lies in the tripod model.
(C3) for all $I \subseteq[n]$ if there exist $i, j \in I$ such that $\mu_{i j}=0$ then $\kappa_{I}=0$

(C4) for any $i, j, k, l \in[n]$ such that there exists $e \in E$ inducing a split $A \mid B$ such that $i, j \in A$ and $k, l \in B$ we have

$$
\left(2 \mu_{i k} \mu_{j l}\right)^{2} \leq\left(\sqrt{\mu_{j l}^{2} \operatorname{Det} P^{i j k}} \pm \mu_{j l} \mu_{i j k}\right)\left(\sqrt{\operatorname{Det} P^{i k l}} \mp \mu_{i k l}\right)
$$

Moreover, if $\mu_{i j} \neq 0$ for all $i, j \in[n]$ then the constraints in Proposition 4.5 are the only constraints involving only second order moments.

Sketch of the proof. The proof is given in Appendix C. Here, for convenience, we give its outline. Denote by $\mathcal{M} \subseteq \Delta_{2^{n}-1}$ the family of distributions described by (C1)-(C4). We need to show that $\mathcal{M}_{T}=\mathcal{M}$. To show that $\mathcal{M}_{T} \subseteq \mathcal{M}$ we use the parametrization in Proposition 2.3 to show that (C1) and (C3) always hold, and that (C2) and (C4) are equivalent to (5). To show the opposite inclusion we propose formulae for the parameters in terms of the observed distribution given by [40, Corollary 5.5], and show that this formulae agree with the parametrization in Proposition 2.3 up to the sign. The last part is technical since we need to show that (C1)-(C4) also imply that there is a choice of signs for the parameters such that the parametrization in Proposition 2.3 holds exactly.

Theorem 4.7 has been formulated for trivalent trees. However, any tree with degrees of some nodes higher than three can be realized as a submodel of a trivalent tree model as explained in [40, Section 4]. Also, including degree two nodes does not change anything in the induced marginal distribution. This result is well known (see e.g. [40, Lemma 2.1]).

A natural question arises for how large trees it is feasible to verify the constraints defining the model. The equality constraints in (C1) can be expressed directly in the raw probabilities and they are easy to check even for relatively large trees. This, by [2, Theorem 4], can be done using so called edge flattenings, which is explained in more details in Appendix D. Checking the other constraints requires only computing $\binom{n}{2}$ covariances between the observed variables and $\binom{n}{2}$ third order central moments. In particular, in practice there is no need of changing the coordinates from the raw probabilities to tree cumulants which can be quite complicated even for relatively small trees.

Another important practical aspect is whether there exist some efficient convex bounds for the model in the space of the raw probabilities. The answer to this question is negative, which follows from the fact that $\operatorname{conv}\left(\mathcal{M}_{T}\right)=\Delta_{2^{n}-1}$. This is easily seen from the fact that $\mathcal{M}_{\text {ind }} \subseteq \mathcal{M}_{T}$, where $\mathcal{M}_{\text {ind }}$ denotes the model of full independence $X_{1} \Perp \ldots \Perp X_{n}$, and that $\operatorname{conv}\left(\mathcal{M}_{\text {ind }}\right)=\Delta_{2^{n}-1}$. To get some informative convex bounds one possibility is to generalize the tripod tree case. Here the model consists of four components depicted in Figure 4 corresponding to different sign patterns of the observed covariances. These components are equivalent up to rotation and symmetry. Instead of taking the convex hull of the whole model we suggest the analysis of the convex hull of each of the components separately. This is also well motivated by the fact that in phylogenetics it is usually assumed that $\eta_{u, v}>0$ for all $(u, v) \in E$ which means restriction to one of the components with all the observed covariances positive. We will not discuss this issue here in more detail.

Table 2
Moments and tree cumulants for a probability assignment which lies in $\mathcal{M}_{T}$, where $T$ is the quartet tree


# 5. Example: The quartet tree model 

We can check that the point $K \in \mathcal{K}_{T}$ provided in Table 2 satisfies all the constraints in Theorem 4.7. It is convenient to provide the numbers as rationals so that the equalities can be checked exactly. To check (C1), note for example that

$$
\begin{gathered}
\kappa_{13} \kappa_{24}-\kappa_{14} \kappa_{23}=\frac{5}{324} \cdot \frac{2}{243}-\frac{5}{486} \cdot \frac{1}{81}=0 \\
\kappa_{123} \kappa_{134}-\kappa_{1234} \kappa_{13}=\frac{10}{2187} \cdot \frac{5}{2187}-\frac{40}{59049} \cdot \frac{5}{324}=0
\end{gathered}
$$

To check (C2) verify for example that $\operatorname{Det} P^{123}=\frac{25}{531441}$ and

$$
\begin{aligned}
& \left(\left(1 \pm \bar{\mu}_{1}\right) \mu_{23} \mp \mu_{123}\right)^{2}=\left\{\frac{1369}{4782969}, \frac{289}{4782969}\right\} \\
& \left(\left(1 \pm \bar{\mu}_{2}\right) \mu_{13} \mp \mu_{123}\right)^{2}=\left\{\frac{30625}{76527504}, \frac{9025}{76527504}\right\} \\
& \left(\left(1 \pm \bar{\mu}_{3}\right) \mu_{12} \mp \mu_{123}\right)^{2}=\left\{\frac{7225}{4782969}, \frac{4225}{4782969}\right\}
\end{aligned}
$$

and hence

$$
\operatorname{Det} P^{123} \leq \min \left\{\left(\left(1 \pm \bar{\mu}_{\sigma(i)}\right) \mu_{\sigma(j) \sigma(k)} \mp \mu_{i j k}\right)^{2}\right\}=\frac{289}{4782969}
$$

is satisfied.

Table 3
Moments and tree cumulants of the given probability assignment which does not lie in $\mathcal{M}_{T}$


From the point of view of the original motivation a different scenario is of interest. Imagine that we have $K \in \mathcal{K}_{T}$ such that all the equalities in (C1) are satisfied, i.e. all the phylogenetic invariants hold. If one of the constraints in (C2)-(C5) does not hold then $K \notin \mathcal{M}_{T}^{n}$. This shows that the method of phylogenetic invariants as commonly used can lead to spurious results. For example consider sample proportions and the corresponding tree cumulants as in Table 3. It can be checked that for this point all the equations in (C1) are satisfied. However, this point does not lie in the model space. Using the formulae in [40, Corollary 5.5], which gives the inverse map for the parametrization, it is simple to confirm that the point mapping to $K$ satisfies $\theta_{1 \mid 1}^{(4)}=\frac{67}{54}>1$. This cannot therefore be a probability and so $\theta \notin \Theta_{T}$.

# 6. Discussion 

The new coordinate system proposed in [40] provides a better insight into the geometry of phylogenetic tree models with binary observations. The product form of the parametrization is useful and has already enabled us to obtain the full geometric description of the model class.

Of course it is one thing formally being able to identify the constraints in the model and quite another to use this understanding for model selection and estimation in realistically large scale problems. The results in this paper only formally allow us to determine explicitly the extremely complex nature of the feasible solution space of a given tree model and determine whether a proposed

estimate is feasible. So they simply represent the first stage in constructing methodology which supports these insights with an inferential technology that can address statistical issues in large tree. In particular, there remains the much more challenging issue of designing samplers that use our results explicitly to efficiently estimate and explore the tree model space. We are currently investigating this issue and hope to report such algorithms in a later paper.

One of the interesting implications of our results for phylogenetic analysis is that it enables us to consider different, simpler model classes containing the original one in such a way that the whole evolutionary interpretation in terms of the tree topologies remains valid. If we were interested only in the tree we could consider the model defined only by a subsets of constraints in Theorem 4.7 involving only covariances. The cost of this reduction is that the conditional independencies induced by the original model no longer hold, which, in turn, affects the interpretation of the model. We note that this approach is in a similar spirit to that employed to motivate the MAG model class introduced in [34].

# Acknowledgments 

Diane Maclagan and John Rhodes contributed substantially to this paper. We would also like to thank Bernd Sturmfels for a stimulating discussion at the early stage of our work and Lior Pachter for pointing out reference [8].

## Appendix A: Change of coordinates

In this section we index raw probabilities with subsets of $[n]$ instead of $\{0,1\}^{n}$. We identify $I \subseteq[n]$ with $\alpha \in\{0,1\}^{n}$ such that $\alpha_{i}=1$ only if $i \in I$. We first change our coordinates from the raw probabilities $p=\left[p_{I}\right]_{I \subseteq[n]}$ to the noncentral moments $\lambda=\left[\lambda_{I}\right]_{I \subseteq[n]}$, where $\lambda_{I}=\mathbb{E}\left(\prod_{i \in I} X_{i}\right)$. This is a linear map $f_{p \lambda}: \mathbb{R}^{2^{n}} \rightarrow \mathbb{R}^{2^{n}}$ with determinant equal to one, where the components $\lambda_{I}$ of the vector $\lambda=f_{p \lambda}(p)$ are defined by

$$
\lambda_{I}=\sum_{J \supseteq I} p_{J} \quad \text { for any } I \subseteq[n]
$$

In particular $\lambda_{\emptyset}=1$ for all probability distributions and the image $f_{p \lambda}\left(\Delta_{2^{n}-1}\right)$ is contained in the hyperplane defined by $\lambda_{\emptyset}=1$. Moreover, from (17), it follows that the $\lambda$ 's are just marginal probabilities. The linearity of the expectation implies that the central moments can be expressed in terms of non-central moments. Define $\mu_{I}=\mathbb{E}\left(\prod_{i \in I} U_{i}\right)$, where $U_{i}=X_{i}-\mathbb{E} X_{i}$. Then

$$
\mu_{I}=\sum_{J \subseteq[n]}(-1)^{|J|} \lambda_{I \backslash J} \prod_{i \in J} \lambda_{i} \quad \text { for } I \subseteq[n]
$$

Using these equations we can transform coordinates from the non-central moments $\lambda=\left[\lambda_{I}\right]$ to another set of variables given by all the means $\lambda_{1}, \ldots, \lambda_{n}$ and

central moments $\left[\mu_{I}\right]$ for $I \subseteq[n]$. The polynomial map $f_{\lambda \mu}: \mathbb{R}^{2^{n}} \rightarrow \mathbb{R}^{n} \times \mathbb{R}^{2^{n}}$ is an identity on the first $n$ coordinates corresponding to the means $\lambda_{1}, \ldots, \lambda_{n}$ and is defined on the remaining coordinates using the equations (18). Let $\mathcal{C}_{n}=$ $\left(f_{\lambda \mu} \circ f_{p \lambda}\right)\left(\Delta_{2^{n}-1}\right)$. This is contained in a subspace of $\mathbb{R}^{n} \times \mathbb{R}^{2^{n}}$ given by

$$
\mu_{\emptyset}=1 \quad \text { and } \quad \mu_{1}=\cdots=\mu_{n}=0
$$

Since $f_{\lambda \mu}$ is invertible (see [40, Appendix A.1]) it provides a change of coordinates from the non-central moments to a coordinate system on $\mathcal{C}_{n}$ given by $\lambda_{1}, \ldots, \lambda_{n}$ together with $\mu_{I}$ for all $I \subseteq[n]$ such that $|I| \geq 2$. Note that the Jacobian of $f_{\lambda \mu} \circ f_{p \lambda}: \Delta_{2^{n}-1} \rightarrow \mathcal{C}_{n}$ is constant and equal to one.

The final change of coordinates requires some combinatorics.
Definition A.1. Let $T=(V, E)$ be a tree with $n$ leaves. An edge split is a partition of $[n]$ into two non-empty sets induced by removing an edge $e \in E$ and restricting $[n]$ to the connected components of the resulting graph. By an edge partition we mean any partition $B_{1}|\cdots| B_{k}$ of the set of leaves of $T$ induced by removing a subset of $E$. Each $B_{i}$ is called a block of the partition.

Let $\Pi_{T}$ denote the partially ordered set (poset) of all tree partitions of the set of leaves. The ordering in this poset is induced from the ordering in the lattice $\Pi_{n}$ of all partitions of $[n]$ (see [35, Example 3.1.1.d]). Thus for $\pi=B_{1}|\cdots| B_{r}$ and $\nu=B_{1}^{\prime}|\cdots| B_{s}^{\prime}$ we have $\pi \leq \nu$ if every block of $\pi$ is contained in one of the blocks of $\nu$. The poset $\Pi_{T}$ has a unique minimal element $1|2| \cdots \mid n$ induced by removing all edges in $E$ and the maximal one with no edges removed which is equal to a single block $[n]$. The maximal element is denoted by $\overline{1}$ and the minimal one is denoted by $\overline{0}$.

For any poset $\Pi$ a Möbius function $\mathfrak{m}_{\Pi}: \Pi \times \Pi \rightarrow \mathbb{R}$ can be defined in such a way that $\mathfrak{m}_{\Pi}(\pi, \pi)=1$ for every $\pi \in \Pi, \mathfrak{m}_{\Pi}(\nu, \pi)=-\sum_{\nu<\delta<\pi} \mathfrak{m}_{\Pi}(\nu, \delta)$ for $\nu<\delta$ in $\Pi$ and is zero otherwise (c.f. [35, Section 3.7]). Let $T(W)$, for $W \subset V$, denote the minimal subtree of $T$ containing $W$ in its set of vertices. Then $\Pi_{T(W)}$ is the poset of all multisplits of the set of leaves of $T(W)$ induced by edges of $T(W)$. The Möbius function on $\Pi_{T(W)}$ will be denoted by $\mathfrak{m}_{W}$ and the Möbius function on $\Pi_{T}$ will be denoted by $\mathfrak{m}$. Let $\overline{0}_{W}$ and $\overline{1}_{W}$ denote the minimal and the maximal element of $\Pi_{T(W)}$ respectively.

Consider a map $f_{\mu \kappa}: \mathbb{R}^{n} \times \mathbb{R}^{2^{n}} \rightarrow \mathbb{R}^{n} \times \mathbb{R}^{2^{n}}$ where the coordinates in the domain are denoted by $\lambda_{1}, \ldots, \lambda_{n}$ and $\mu_{I}$ for $I \subseteq[n]$ and let the coordinates of the image space be denoted by $\lambda_{1}, \ldots, \lambda_{n}$ and $\kappa_{I}$ for $I \subseteq[n]$. The map is defined as the identity on the first $n$ coordinates corresponding to $\lambda_{1}, \ldots, \lambda_{n}$ and

$$
\kappa_{I}=\sum_{\pi \in \Pi_{T(I)}} \mathfrak{m}_{I}\left(\pi, \overline{1}_{I}\right) \prod_{B \in \pi} \mu_{B} \quad \text { for all } I \subseteq[n]
$$

where by convention $\kappa_{\emptyset}=\mu_{\emptyset}$. Let $\mathcal{K}_{T}=f_{\mu \kappa}\left(\mathcal{C}_{n}\right)$. Note that for any $I \subseteq[n]$ such that $|I| \leq 3, \kappa_{I}=\mu_{I}$. In particular $\mathcal{K}_{T}$ is contained in the subspace of $\mathbb{R}^{n} \times \mathbb{R}^{2^{n}}$ given by

$$
\kappa_{\emptyset}=1, \quad \kappa_{1}=\cdots=\kappa_{n}=0
$$

The map $f_{\mu \kappa}: \mathcal{C}_{n} \rightarrow \mathcal{K}_{T}$ is a polynomial isomorphism with a polynomial inverse $f_{\kappa \mu}$. It therefore gives a change of coordinates to a coordinate system on $\mathcal{K}_{T}$ given by $\lambda_{1}, \ldots, \lambda_{n}$ and $\kappa_{I}$ for $|I| \geq 2$. The exact form of the inverse map is given by the Möbius inversion formula (c.f. [40, Section 3.2])

$$
\mu_{I}=\sum_{\pi \in \Pi_{T(I)}} \prod_{B \in \pi} \kappa_{B} \quad \text { for all } I \subseteq[n],|I| \geq 2
$$

Note that after restriction to $\Delta_{2^{n}-1}, f_{p \lambda}\left(\Delta_{2^{n}-1}\right)$ and $\mathcal{C}_{n}$ respectively all $f_{p \lambda}, f_{\lambda \mu}$ and $f_{\mu \kappa}$ are polynomial maps with polynomial inverses (c.f. [40, Appendix A]). This therefore implies that there is a polynomial isomorphism between $\Delta_{2^{n}-1}$ and $\mathcal{K}_{T}$.

# Appendix B: Proofs 

Proof of Proposition 2.5. By Remark $2.1 \mathcal{M}_{3}$ does not depend on the rooting. Therefore, we can assume that $T$ is rooted in $h$. In this case Proposition 2.3 implies that $\mathcal{M}_{3}^{\kappa}$ is given by $\lambda_{i}=\frac{1}{2}\left(1-\bar{\mu}_{i}\right)$ for $i=1,2,3$ and

$$
\begin{aligned}
& \mu_{i j}=\frac{1}{4}\left(1-\bar{\mu}_{h}^{2}\right) \eta_{h, i} \eta_{h, j} \text { for all } i \neq j \in\{1,2,3\} \text { and } \\
& \mu_{123}=\frac{1}{4}\left(1-\bar{\mu}_{h}^{2}\right) \bar{\mu}_{h} \eta_{h, 1} \eta_{h, 2} \eta_{h, 3}
\end{aligned}
$$

subject to constraints in (5).
Denote the subset of $\mathcal{K}_{T}$ given by constraints (i),(ii) by $\mathcal{M}$. We need to show that $\mathcal{M}=\mathcal{M}_{3}^{\kappa}$. First, we prove that $\mathcal{M}_{3}^{\kappa} \subseteq \mathcal{M}$. Let $K=\psi_{T}(\omega)$ for some $\omega \in \Omega_{T}$ with coordinates given by $\bar{\mu}_{h}$ and $\bar{\mu}_{i}, \eta_{h, i}$ for $i=1,2,3$. We consider two cases. Either $\left(1-\bar{\mu}_{h}^{2}\right) \eta_{h, 1} \eta_{h, 2} \eta_{h, 3}$ is zero or not. In the first case $\mu_{123}=0$ and at least two covariances vanish and hence (i) holds.

Now we show that if $\left(1-\bar{\mu}_{h}^{2}\right) \eta_{h, 1} \eta_{h, 2} \eta_{h, 3} \neq 0$ then (ii) holds. From (21)

$$
\mu_{12} \mu_{13} \mu_{23}=\left(\frac{1}{4}\left(1-\bar{\mu}_{h}^{2}\right)\right)^{3}\left(\eta_{h, 1} \eta_{h, 2} \eta_{h, 3}\right)^{2}>0
$$

To show that $K$ satisfies (9) we can simply substitute for the corresponding moments using (21). After trivial reductions we then obtain that

$$
\left|\eta_{h, i}\right| \pm \bar{\mu}_{h} \eta_{h, i} \leq\left(1 \pm \bar{\mu}_{i}\right)
$$

which is equivalent to (5). Therefore, since by hypothesis (5) holds, we also have that $\mathcal{M}_{3}^{\kappa} \subseteq \mathcal{M}$.

To show $\mathcal{M} \subseteq \mathcal{M}_{3}^{\kappa}$ we prove that for $K \in \mathcal{M}$ a parameter $\omega$ in (21) exists which satisfies the constraints defining $\Omega_{T}$ and $K=\psi_{T}(\omega)$. Let $P$ be the probability distribution corresponding to $K$. First, consider the points satisfying (i). If all three covariances vanish for this point then taking $\eta_{h, 1}=\eta_{h, 2}=\eta_{h, 3}=0$ and $\bar{\mu}_{h}^{2}=1$ we obtain a valid choice of parameters in (21) and their values

satisfy (5). When one covariance is non-zero, say $\mu_{12} \neq 0$, then, if a choice of parameters exists it must satisfy $\bar{\mu}_{h}^{2} \neq 1, \eta_{h, 1}, \eta_{h, 2} \neq 0$ and $\eta_{h, 3}=0$. Such a choice of parameters will exist if we can ensure that $\mu_{12}=\left(1-\bar{\mu}_{h}^{2}\right) \eta_{h, 1} \eta_{h, 2}$. This follows from [20, Corollary 2] which states that if only $\mu_{12} \neq 0$ then there always exists a choice of parameters for model $X_{1} \Perp X_{2} \mid H$, where $H$ is hidden.

Consider now case (ii). Since $\mu_{12} \mu_{13} \mu_{23}>0$ then in particular Det $P>0$. Set $\bar{\mu}_{h}^{2}=\frac{\mu_{123}^{2}}{\operatorname{Det} P}$ and $\eta_{h, i}^{2}=\frac{\operatorname{Det} P}{\mu_{j k}^{2}}$ for $i=1,2,3$. It follows that $\left(\frac{1}{4}\left(1-\bar{\mu}_{h}^{2}\right)\right)^{2} \eta_{h, i}^{2} \eta_{h, j}^{2}=$ $\mu_{i j}^{2}$ for $i, j=1,2,3$ and $\left(\frac{1}{4}\left(1-\bar{\mu}_{h}^{2}\right)\right)^{2} \bar{\mu}_{h}^{2} \eta_{h, 1}^{2} \eta_{h, 2}^{2} \eta_{h, 3}^{2}=\mu_{123}^{2}$. This coincides with (21) modulo the sign. It can be easily shown that $\mu_{12} \mu_{13} \mu_{23}>0$ implies that there exist a choice of signs for $\eta_{h, i}$ for $i=1,2,3$ such that

$$
\frac{1}{4}\left(1-\bar{\mu}_{h}^{2}\right) \eta_{h, i} \eta_{h, j}=\mu_{i j}
$$

for all $1 \leq i<j \leq 3$ as in (21). For example set $\operatorname{sgn}\left(\eta_{h, i}\right)=\operatorname{sgn}\left(\mu_{j k}\right)$ and use the fact that, by our assumption, $\operatorname{sgn}\left(\mu_{i j}\right)=\operatorname{sgn}\left(\mu_{i k}\right) \operatorname{sgn}\left(\mu_{j k}\right)$. This choice of signs already determines the sign of $\bar{\mu}_{h}$ so that

$$
\frac{1}{4}\left(1-\bar{\mu}_{h}^{2}\right) \bar{\mu}_{h} \eta_{h, 1} \eta_{h, 2} \eta_{h, 3}=\mu_{123}
$$

holds.
It remains to show that parameters set in this way satisfy the constraints defining $\Omega_{T}$. First note that since $0<4 \mu_{12} \mu_{13} \mu_{23} \leq \operatorname{Det} P$ then $\bar{\mu}_{h}^{2} \in(0,1)$ as required. From [40, Appendix D] we know that if $\left(\eta_{h, 1}, \eta_{h, 2}, \eta_{h, 3}, \bar{\mu}_{h}\right)$ is one choice of parameters then there exists only one alternative choice and it is $\left(-\eta_{h, 1},-\eta_{h, 2},-\eta_{h, 3},-\bar{\mu}_{h}\right)$. For a fixed $i=1,2,3$ it is easily checked that $\left(\eta_{h, i}, \bar{\mu}_{h}\right)$ satisfies (5) if and only if $\left(-\eta_{h, i},-\bar{\mu}_{h}\right)$ does. Therefore, we can assume that $\eta_{h, i}=\frac{\sqrt{\operatorname{Det} P}}{\left|\mu_{j k}\right|}>0$. In this case $\bar{\mu}_{h}=\operatorname{sgn}\left(\mu_{j k}\right) \frac{\mu_{123}}{\sqrt{\operatorname{Det} P}}$. It follows that (5) is satisfied if and only if (9) holds.

Proof of Lemma 4.4. First assume that the map $s_{0}: E \rightarrow\{-1,1\}$, given in the statement of the lemma, exists. This induces a map $s: V \times V \rightarrow\{-1,1\}$ such that $s(k, l)=\prod_{(u, v) \in E(k l)} s_{0}(u, v)$. For any triple $i, j, k$ there exists a unique inner node $h$ which is the intersection of all three paths between $i, j, k$. By the above equation the choice of signs for all $(u, v) \in E$ gives $s(i, h), s(j, h)$ and $s(k, h)$. Since $s(i, j)=s(i, h) s(j, h)$ and the same for the two other pairs, we get that $s(i, j) s(i, k) s(j, k)=s^{2}(i, h) s^{2}(j, h) s^{2}(k, h)=1$ and the result follows since by construction $\sigma(i, j)=s(i, j)$ for all $i, j \in[n]$.

Now we prove the converse implication. Whenever there is a path $E(u v)$ in $T$ such that all its inner nodes have degree two then a sign assignment satisfying (15) exists if and only if there exists a sign assignment for the same tree but with $E(u v)$ contracted to a single edge $(u, v)$. Hence we can assume that the degree of each inner node is at least three.

We use an inductive argument with respect to number of hidden nodes. First we will show that the theorem is true for trees with one inner node (star trees) denoted by $h$. In this case we will use induction with respect to number of leaves.

It can easily be checked directly that the theorem is true for the tripod tree. Assume it works for all star trees with $k \leq m-1$ leaves and let $T$ be a star tree with $m$ leaves. By assumption for any three leaves $i, j, k: \sigma(i, j) \sigma(i, k) \sigma(j, k)=1$. If we consider a subtree with $(1, h)$ deleted then by induction assumption we can find a consistent choice of signs for all remaining edges. A choice of a sign for $(1, h)$ consistent with (15) exists if for all $i \geq 2 \sigma(1, i)=s_{0}(1, h) s_{0}(i, h)$. This is true if either $\sigma(1, i) s_{0}(i, h)=1$ for all $i$ or $\sigma(1, i) s_{0}(i, h)=-1$ for all $i$. Assume it is not true, i.e. there exist two leaves $i, j$ such that $\sigma(1, i) s_{0}(i, h)=1$ and $\sigma(1, j) s_{0}(j, h)=-1$. Then in particular since $\sigma(i, j)=s_{0}(i, h) s_{0}(j, h)$ we would have that $\sigma(1, i) \sigma(1, j) \sigma(i, j)=-1$ which contradicts our assumption.

If the number of the inner nodes is greater than one then pick an inner node $h$ adjacent to exactly one inner node. Let $h^{\prime}$ be the inner node adjacent to $h$ and let $I$ be a subset of leaves which are adjacent to $h$. Choose one $i \in I$ and consider a subtree $T^{\prime}$ obtained by removing all leaves in $I$ and the incident edges apart from the node $i$ and the edge $(h, i)$. By the induction, since $h$ has degree two in the resulting subtree, we can find signs for all edges of $T^{\prime}$. Set $s_{0}\left(h, h^{\prime}\right)=1$ then $s_{0}(h, i)=s\left(h^{\prime}, i\right)$ which identifies $s_{0}(h, i)$. Similarly it can be showed that there exists a choice of signs for all remaining edges $\left(i^{\prime}, h\right)$. The result follows since the choice of $i \in I$ was arbitrary.

# Appendix C: The proof of the main theorem 

Let $K \in \mathcal{K}_{T}$ have coordinates given by $\lambda_{i}$ for $i=1, \ldots, n$ and $\kappa_{I}$ for $I \subseteq[n]$ such that $|I| \geq 2$. Let $K^{J}, J \subseteq[n]$, denote the projection onto the coordinates given by $\lambda_{i}$ for $i \in J$ and $\kappa_{I}, I \subseteq J,|I| \geq 2$. Directly from the definition of $\mathcal{M}_{T}$ it follows that $K \in \mathcal{M}_{T}^{v}$ if and only if $K^{I} \in \mathcal{M}_{T(I)}^{v}$ for all $I \subseteq[n]$.

Let $\mathcal{M}$ denote the subset of $\mathcal{K}_{T}$ defined by constraints in (C1)-(C4). We need to show that $\mathcal{M}=\mathcal{M}_{T}^{v}$. We divide the proof into series of lemmas.

Lemma C.1. The inclusion $\mathcal{M}_{T}^{v} \subseteq \mathcal{M}$ holds.
Proof. Since the rooting is not relevant by Remark 2.1, we choose an arbitrary inner node as the root node. Let $K \in \mathcal{M}_{T}^{v}$ and hence $K=\psi_{T}(\omega)$ for some $\omega \in \Omega_{T}$.

To show that the equations in (C1) hold let $A \mid B$ be an edge split and let $e=\left(w, w^{\prime}\right)$ be the edge inducing this split. By $T \backslash e$ we denote the graph obtained from $T$ by removing the edge $e$. We assume that $w$ lies in the same connected component of $T \backslash e$ as $A$ and $w^{\prime}$ lies in the second component of $T \backslash e$. For every non-empty $I \subseteq A$ and $J \subseteq B$ from Proposition 2.3

$$
\begin{aligned}
\kappa_{I J}= & \frac{1}{4}\left(1-\bar{\mu}_{v(I J)}^{2}\right) \prod_{v \in \operatorname{int}\left(V\left(I w^{\prime}\right)\right)} \bar{\mu}_{v}^{\operatorname{deg}(v)-2} \prod_{v \in \operatorname{int}(V(J w))} \bar{\mu}_{v}^{\operatorname{deg}(v)-2} \\
& \cdot \eta_{w, w^{\prime}} \prod_{(u, v) \in E(I w)} \eta_{u, v} \prod_{(u, v) \in E\left(J w^{\prime}\right)} \eta_{u, v}
\end{aligned}
$$

From this it easily follows that for any non-empty $I_{1}, I_{2} \subseteq A$ and $J_{1}, J_{2} \subseteq B$,

$\kappa_{I_{1} J_{1}} \kappa_{I_{2} J_{2}}-\kappa_{I_{1} J_{2}} \kappa_{I_{2} J_{1}}=0$ if and only if

$$
\left(1-\mu_{r\left(I_{1} J_{1}\right)}^{2}\right)\left(1-\mu_{r\left(I_{2} J_{2}\right)}^{2}\right)=\left(1-\mu_{r\left(I_{1} J_{2}\right)}^{2}\right)\left(1-\mu_{r\left(I_{2} J_{1}\right)}^{2}\right)
$$

To show that (23) is always true, we consider two cases: either $r(A B) \in V(A w)$ or $r(A B) \in V\left(B w^{\prime}\right)$. If $r(A B) \in V(A w)$ then $r\left(I_{1} J_{1}\right)=r\left(I_{1} w\right), r\left(I_{1} J_{2}\right)=$ $r\left(I_{1} w\right), r\left(I_{2} J_{1}\right)=r\left(I_{2} w\right)$ and $r\left(I_{2} J_{2}\right)=r\left(I_{2} w\right)$. Hence in this case (23) holds. The case $r(A B) \in V\left(B w^{\prime}\right)$ follows by symmetry. Therefore the equations in (C1) always hold.

To show that $K$ satisfies (C2) consider the projection $K^{i j k}$ for each $i, j, k \in$ $[n]$. By [40, Corollary 2.2] $\mathcal{M}_{T(i j k)}^{n}$ is equal to the tripod tree model. Since $K^{i j k} \in \mathcal{M}_{T(i j k)}^{n}$ then, by Proposition 2.5, (C2) must hold. To show that $K$ satisfies (C3) let $i, j \in[n]$ be such that $\mu_{i j}=0$. Let $I \subseteq[n]$ be such that $i, j \in I$ and assume that $\kappa_{I}(\omega) \neq 0$. Then by (7) in particular $\mu_{r(I)}^{2} \neq 1$ and $\eta_{u, v} \neq 0$ for all $(u, v) \in E(I)$. By [40, Remark 4.3] this implies in particular that $\bar{\mu}_{r(i j)}^{2} \neq 1$. From this, again by (7), it follows that $\mu_{i j} \neq 0$ and we get a contradiction. Hence if $\mu_{i j}=0$ then $\kappa_{I}=0$ for all $I$ such that $i, j \in I$.

To show that $K$ satisfies (C4) let $i, j, k, l \in[n]$ be the four leaves mentioned in the condition. Let $u$ and $v$ be two inner nodes such that $u$ separates $i$ from $j$, $v$ separates $k$ from $l$ and $\{u, v\}$ separates $\{i, j\}$ from $\{k, l\}$. In other words $u, v$ are the only inner nodes of degree three in $T(i j k l)$. By [40, Lemma 2.1], $T(i j k l)$ gives the same model as the quartet tree with four leaves $i, j, k, l$ and two inner nodes $u, v$. Moreover, by Remark 2.1, $\mathcal{M}_{T(i j k l)}$ does not depend on the rooting so we can assume that the tree is rooted in $u$. Since $K^{i j k l} \in \mathcal{M}_{T(i j k l)}$ then for some parameter choices

$$
\begin{aligned}
\mu_{i k}=\frac{1}{4}\left(1-\bar{\mu}_{u}^{2}\right) \eta_{u, i} \eta_{u, v} \eta_{v, k}, & \mu_{j l}=\frac{1}{4}\left(1-\bar{\mu}_{u}^{2}\right) \eta_{u, j} \eta_{u, v} \eta_{v, l} \\
\mu_{i j k}=\frac{1}{4}\left(1-\bar{\mu}_{u}^{2}\right) \bar{\mu}_{u} \eta_{u, i} \eta_{u, j} \eta_{u, v} \eta_{v, k}, & \mu_{i k l}=\frac{1}{4}\left(1-\bar{\mu}_{u}^{2}\right) \bar{\mu}_{v} \eta_{u, i} \eta_{u, v} \eta_{v, k} \eta_{v, l}
\end{aligned}
$$

Substitute these equations into (C4). There are then two cases to consider: $\mu_{u v} \geq 0, \mu_{u v}<0$. Laborious but elementary algebra shows that the condition in (C4) is equivalent to (5) applied to $\left(1-\bar{\mu}_{u}^{2}\right) \eta_{u, v}$ and hence (C4) holds by definition. Consequently $\mathcal{M}_{T}^{n} \subseteq \mathcal{M}$.

To show the opposite inclusion is a bit more complicated. We consider two separate cases. Let $K \in \mathcal{M}$. We construct a point $\omega_{0} \in \mathbb{R}^{|V|+|E|}$ such that $\omega_{0} \in \Omega_{T}$ and $\psi_{T}\left(\omega_{0}\right)=K$, i.e. $\omega_{0}$ is such that, for all $I \subseteq[n]$ such that $|I| \geq 2$, $\kappa_{I}$ can be written in terms of the parameters in $\omega_{0}$ as in (7).
Lemma C.2. Let $K$ be such that $\mu_{i j} \neq 0$ for all $i, j \in[n]$. If $K \in \mathcal{M}$ then $K \in \mathcal{M}_{T}^{n}$.
Proof. We set squares of values of all the parameters in terms of the observed moments using [40, Corollary 5.5]. We will show that the equations in (7) must hold for their absolute values. We will then need to ensure there is at least one assignment of signs for a set of parameters such that all equations in (7) hold

exactly. Finally, we will show that the parameter vector $\omega_{0}$ defined in this way lies in $\Omega_{T}$.

For each inner node $h$ of $T$ let $i, j, k \in[n]$ be any three leaves separated by $h$ in $T$. By (C2) we have that $\mu_{i j} \mu_{i k} \mu_{j k}>0$ and hence also that $\operatorname{Det} P^{i j k}>0$. Now set

$$
\left(\bar{\mu}_{h}^{0}\right)^{2}=\frac{\mu_{i j k}^{2}}{\operatorname{Det} P^{i j k}}
$$

We show that (C1), which $K$ satisfies by assumption, implies that the value of $\left(\bar{\mu}_{h}^{0}\right)^{2}$ does not depend on the choice of $i, j, k$. It suffices to show that if $k$ is replaced by another leaf $k^{\prime}$ such that $i, j, k^{\prime}$ are separated by $h$ in $T$ then $\frac{\mu_{i j k}^{2}}{\operatorname{Det} P^{i j k}}=\frac{\mu_{i j k^{\prime}}^{2}}{\operatorname{Det} P^{i j k^{\prime}}}$. Since $h$ has degree three in $T$ then there exists an edge $e \in E$ inducing a split $A \mid B$ such that $i, j \in A$ and $k, k^{\prime} \in B$. From (C1) it follows that

$$
\mu_{i k} \mu_{j k^{\prime}}=\mu_{i k^{\prime}} \mu_{j k}, \quad \mu_{i j k} \mu_{i k^{\prime}}=\mu_{i j k^{\prime}} \mu_{i k}, \quad \mu_{i j k} \mu_{j k^{\prime}}=\mu_{i j k^{\prime}} \mu_{j k}
$$

and consequently

$$
\operatorname{Det} P^{i j k} \mu_{i j} \mu_{i k^{\prime}} \mu_{j k^{\prime}}=\operatorname{Det} P^{i j k^{\prime}} \mu_{i j} \mu_{i k} \mu_{j k}
$$

which implies that

$$
\frac{\mu_{i j k}^{2}}{\operatorname{Det} P^{i j k}}=\frac{\mu_{i j k}^{2} \mu_{i j} \mu_{i k^{\prime}} \mu_{j k^{\prime}}}{\operatorname{Det} P^{i j k} \mu_{i j} \mu_{i k^{\prime}} \mu_{j k^{\prime}}}=\frac{\mu_{i j k^{\prime}}^{2} \mu_{i j} \mu_{i k} \mu_{j k}}{\operatorname{Det} P^{i j k^{\prime}} \mu_{i j} \mu_{i k} \mu_{j k}}=\frac{\mu_{i j k^{\prime}}^{2}}{\operatorname{Det} P^{i j k^{\prime}}}
$$

as required.
For terminal edges $(v, i)$ of $T$ such that $i \in[n]$, let $j, k \in[n]$ be any two leaves of $T$ such that $v$ separates $i, j, k$. Set

$$
\left(\eta_{v, i}^{0}\right)^{2}=\frac{\operatorname{Det} P^{i j k}}{\mu_{j k}^{2}}
$$

As in the previous case it is straightforward to check that, given (C1), this value does not depend on the choice of $j, k$. For example, if instead of $k$ we have $k^{\prime}$ and $v$ separates $i, j, k^{\prime}$ in $T$ then there exists an edge split such that $\{i, j\}$ and $\left\{k, k^{\prime}\right\}$ are in different blocks. By (25), we can show that

$$
\frac{\operatorname{Det} P^{i j k}}{\mu_{j k}^{2}}=\frac{\mu_{i k} \operatorname{Det} P^{i j k}}{\mu_{i k^{\prime}} \mu_{j k^{\prime}} \mu_{j k}}=\frac{\operatorname{Det} P^{i j k^{\prime}}}{\mu_{j k^{\prime}}^{2}}
$$

For inner edges $(u, v) \in E$ let $i, j, k, l \in[n]$ be any four leaves such that $u$ separates $i$ from $j, v$ separates $k$ from $l$ and $\{u, v\}$ separates $\{i, j\}$ from $\{k, l\}$. Set

$$
\left(\eta_{u, v}^{0}\right)^{2}=\frac{\mu_{i j}^{2}}{\mu_{i j}^{2}} \frac{\operatorname{Det} P^{i j k}}{\operatorname{Det} P^{i k l}}
$$

which is well-defined since $\mu_{i j}^{2}$ and $\operatorname{Det} P^{i k l}$ are strictly positive. We now show that this value does not depend on the choice of $i, j, k, l$. By symmetry it suffices

to show that we obtain the same value if instead of $l$ we took another leaf $l^{\prime}$ such that $u, v$ are the only degree three nodes in $T\left(i j k l^{\prime}\right)$. Since $v$ has degree three then there must exist an inner edge separating $i, j, k$ from $l, l^{\prime}$. From (C1) it follows that

$$
\mu_{i l^{\prime}} \mu_{k l^{\prime}} \operatorname{Det} P^{i k l}=\mu_{i l} \mu_{k l} \operatorname{Det} P^{i k l^{\prime}}, \quad \mu_{i l} \mu_{k l^{\prime}}=\mu_{i l^{\prime}} \mu_{k l}
$$

and hence

$$
\frac{\mu_{i l}^{2}}{\mu_{i j}^{2}} \frac{\operatorname{Det} P^{i j k}}{\operatorname{Det} P^{i k l}}=\frac{\mu_{i l^{\prime}} \mu_{k l^{\prime}}}{\mu_{i l^{\prime}} \mu_{k l^{\prime}}} \frac{\mu_{i l}^{2}}{\mu_{i j}^{2}} \frac{\operatorname{Det} P^{i j k}}{\operatorname{Det} P^{i k l}}=\frac{\mu_{i l^{\prime}}^{2}}{\mu_{i j}^{2}} \frac{\operatorname{Det} P^{i j k}}{\operatorname{Det} P^{i k l^{\prime}}}
$$

as required.
We now show that with the choice of parameters satisfying (24), (27) and (28) the modulus of equations in (7) hold. First consider the case $I=\{i, j\}$. Label the inner nodes of $E(i j)$ by $v_{1}, \ldots, v_{k}$ beginning from the node adjacent to $i$. For each $s=1, \ldots, k$ let $i_{s}$ denote a leaf such that $v_{s}$ separates $i, j, i_{s}$ in $T$. By Remark 2.1, we can choose any rooting. We assume that the root $r(i j)$ of this path is in $v_{1}$. We now proceed to check that

$$
\begin{aligned}
\mu_{i j}^{2} & =\left(\frac{1}{4}\left(1-\left(\bar{\mu}_{r(i j)}^{0}\right)^{2}\right)\right)^{2} \prod_{(u, v) \in E(i j)}\left(\eta_{u, v}^{0}\right)^{2} \\
& =\left(\frac{1}{4}\left(1-\left(\bar{\mu}_{r(i j)}^{0}\right)^{2}\right)\right)^{2}\left(\eta_{v_{1}, u}^{0}\right)^{2}\left(\prod_{s=2}^{k}\left(\eta_{v_{s-1}, v_{s}}^{0}\right)^{2}\right)\left(\eta_{v_{k}, v}^{0}\right)^{2}
\end{aligned}
$$

Since $v_{1}$ separates $i, j, i_{1}$ by construction, from (24) we therefore have

$$
\frac{1}{4}\left(1-\left(\bar{\mu}_{v_{1}}^{0}\right)^{2}\right)=\frac{\mu_{i j} \mu_{i i_{1}} \mu_{j i_{1}}}{\operatorname{Det}\left(P^{i j i_{1}}\right)}
$$

Now substitute this equation and all the set values in (27), (28) into the right hand side of (29). Use the fact that $v_{k}$ separates $i, j, i_{k}$ in $T$ and $i_{s-1}, i_{s}$ are the only degree three nodes in $T\left(i i_{s-1} j i_{s}\right)$. Since $\left(v_{1}, i\right)$ and $\left(v_{k}, j\right)$ are the only terminal edges we obtain

$$
\left(\frac{\mu_{i j} \mu_{i i_{1}} \mu_{j i_{1}}}{\operatorname{Det}\left(P^{i j i_{1}}\right)}\right)^{2} \cdot \frac{\operatorname{Det} P^{i j i_{1}}}{\mu_{j i_{1}}^{2}} \cdot\left(\prod_{s=2}^{k} \frac{\mu_{i i_{s}}^{2}}{\mu_{i i_{s-1}}^{2}} \frac{\operatorname{Det} P^{i j i_{s-1}}}{\operatorname{Det} P^{i j i_{s}}}\right) \cdot \frac{\operatorname{Det} P^{i j i_{k}}}{\mu_{j i_{k}}^{2}}
$$

It can now be checked that all the expressions with hyperdeterminants cancel out and the formula reduces to $\mu_{i j}^{2}$ as required.

Now we need to show that for every $I=\{i, j, k\}$

$$
\mu_{i j k}^{2}=\left(\frac{1}{4}\left(1-\bar{\mu}_{r(i j k)}^{0}\right)^{2}\right)^{2}\left(\bar{\mu}_{w}^{0}\right)^{2} \prod_{(u, v) \in E(i j k)}\left(\eta_{u, v}^{0}\right)^{2}
$$

where by $w$ we denote the node separating $i, j$ and $k$. Assume that $T(i j k)$ is rooted somewhere on the path between $i$ and $j$. Using (29) the right hand side of (31) can be rewritten as

$$
\mu_{i j}^{2}\left(\bar{\mu}_{w}^{0}\right)^{2} \prod_{(u, v) \in E(w k)}\left(\eta_{u, v}^{0}\right)^{2}
$$

Number the degree three nodes in $E(w k)$ by $v_{1}, \ldots, v_{l}$ and let $i_{s}$ denote a leaf such that the inner nodes of $T\left(i j k i_{s}\right)$ of degree three are exactly $v_{s-1}$ and $v_{s}$, where $v_{0}=w$. By an exactly analogous argument as in the case above we obtain

$$
\begin{aligned}
& \prod_{(u, v) \in E(w k)}\left(\eta_{u, v}^{0}\right)^{2} \\
& \quad=\frac{\mu_{i i_{1}}^{2}}{\mu_{i j}^{4}} \frac{\operatorname{Det} P^{i j k}}{\operatorname{Det} P^{i k i_{1}}} \cdot\left(\prod_{s=2}^{l} \frac{\mu_{i_{s-1} i_{s}}^{2}}{\mu_{i_{s-2} i_{s-1}}^{2}} \frac{\operatorname{Det} P^{i_{s-2} i_{s-1} k}}{\operatorname{Det} P^{i_{s-1} i_{s} k}}\right) \frac{\operatorname{Det} P^{i_{l-1} i_{l} k}}{\mu_{i_{l-1} i_{l}}^{2}}
\end{aligned}
$$

where $i_{0}=i$. It can be easily checked that all the hyperdeterminants apart from the term $\operatorname{Det} P^{i j k}$ cancel out. Moreover, all the covariances apart from the term $\mu_{i j}^{-2}$ cancel out as well. Hence (33) is equal to $\frac{\operatorname{Det} P^{i j k}}{\mu_{i j}^{2}}$. Now, by using the definition of $\left(\bar{\mu}_{w}^{0}\right)^{2}$ in (24), it can be easily checked that (32) is equal to $\mu_{i j k}^{2}$ as required.

So far we have confirmed only that the squares of parameters in $\omega_{0}$ satisfy required equations at least for the tree cumulants up to the third order. Next, we show that there exists a consistent choice of signs for these parameters such that the equations are satisfied exactly. Let $\sigma(i, j)=\operatorname{sgn}\left(\mu_{i j}\right)$. Since by assumption $\mu_{i j} \neq 0$ for all $i, j \in[n]$ then the conditions in (C2) imply that $\sigma(i, j) \sigma(i, k) \sigma(j, k)=1$ for all triples $i, j, k \in[n]$. Hence by Lemma 4.4 there exists a choice $s_{0}(u, v) \in\{-1,+1\}$ for all $(u, v) \in E$ such that $\sigma(i, j)=\prod_{(u, v) \in E(i j)} s_{0}(u, v)$ for all $i, j \in[n]$. For any two nodes $k, l \in V$ we define $s(k, l)=\prod_{(u, v) \in E(k l)} s_{0}(u, v)$. A choice of signs for the parameters can be obtained as follows: For each edge $(u, v) \in E$ we set $\operatorname{sgn}\left(\eta_{u, v}^{0}\right)=s_{0}(u, v)$ and, for each inner node $v$, set $\operatorname{sgn}\left(\bar{\mu}_{v}^{0}\right)=\operatorname{sgn}\left(\mu_{i j k}\right) s(v, i) s(v, j) s(v, k)$ where $i, j, k$ are any three leaves of $T$ separated by $v$.

Assume now that the choice of the signs of the parameters, induced by $s_{0}(u, v)$ for $(u, v) \in E$, has been made. This choice of signs gives

$$
\begin{gathered}
\bar{\mu}_{v}^{0}=s(v, i) s(v, j) s(v, k) \frac{\mu_{i j k}}{\sqrt{\operatorname{Det} P^{i j k}}} \\
\eta_{v, i}^{0}=s(v, i) \frac{\sqrt{\operatorname{Det} P^{i j k}}}{\left|\mu_{j k}\right|} \\
\eta_{u, v}^{0}=s_{0}(u, v)\left|\frac{\mu_{i l}}{\mu_{i j}}\right| \sqrt{\frac{\operatorname{Det} P^{i j k}}{\operatorname{Det} P^{i k l}}}
\end{gathered}
$$

Note that, in particular, with this choice of signs $\operatorname{sgn}\left(\eta_{u, v}^{0}\right)=s_{0}(u, v)$ for all $(u, v) \in E$ and $\operatorname{sgn}\left(\bar{\mu}_{v}^{0}\right)=\operatorname{sgn}\left(\mu_{i j k}\right) \prod_{(u, v) \in E(i j k)} s_{0}(u, v)$. Since (29) holds, it follows that

$$
\left|\mu_{i j}\right|=\frac{1}{4}\left(1-\left(\bar{\mu}_{r(i j)}^{0}\right)^{2}\right) \prod_{(u, v) \in E(i j)}\left|\eta_{u, v}^{0}\right|
$$

Now multiply both sides by $s(i, j)=\prod_{(u, v) \in E(i j)} s_{0}(u, v)$ to get

$$
\begin{aligned}
\mu_{i j}=s(i, j)\left|\mu_{i j}\right| & =\frac{1}{4}\left(1-\left(\bar{\mu}_{r(i j)}^{0}\right)^{2}\right) \prod_{(u, v) \in E(i j)} s_{0}(u, v)\left|\eta_{u, v}^{0}\right| \\
& =\frac{1}{4}\left(1-\left(\bar{\mu}_{r(i j)}^{0}\right)^{2}\right) \prod_{(u, v) \in E(i j)} \eta_{u, v}^{0}
\end{aligned}
$$

Similarly, from (31), we have that

$$
\left|\mu_{i j k}\right|=\frac{1}{4}\left(1-\left(\bar{\mu}_{r(i j k)}^{0}\right)^{2}\right)\left|\bar{\mu}_{w}^{0}\right| \prod_{(u, v) \in E(i j k)}\left|\eta_{u, v}^{0}\right|
$$

Multiply both sides by $\operatorname{sgn}\left(\mu_{i j k}\right)$ and use the fact that $\left(\prod_{(u, v) \in E(i j k)} s_{0}(u, v)\right)^{2}=$ 1 to get

$$
\begin{aligned}
\mu_{i j k}= & \frac{1}{4}\left(1-\left(\bar{\mu}_{r(i j k)}^{0}\right)^{2}\right)\left(\left|\bar{\mu}_{w}^{0}\right| \operatorname{sgn}\left(\mu_{i j k}\right) \prod_{(u, v) \in E(i j k)} s_{0}(u, v)\right) \\
& \cdot \prod_{(u, v) \in E(i j k)} s_{0}(u, v)\left|\eta_{u, v}^{0}\right| \\
= & \frac{1}{4}\left(1-\left(\bar{\mu}_{r(i j k)}^{0}\right)^{2}\right) \bar{\mu}_{w}^{0} \prod_{(u, v) \in E(i j k)} \eta_{u, v}^{0}
\end{aligned}
$$

as desired.
We now show (7) for $|I| \geq 4$ by induction. Let $(u, v) \in E$ be any edge splitting $I$ into two subsets $I_{1}$ and $I_{2}$ such that $\left|I_{1}\right|,\left|I_{2}\right| \geq 2$ and $u$ is the node closer to $I_{1}$. Let $i \in I_{1}$ and $j \in I_{2}$ then, by (C1),

$$
\kappa_{I_{1} I_{2}}=\frac{\kappa_{I_{1} j} \kappa_{i I_{2}}}{\kappa_{i j}}
$$

By induction we can assume that $\kappa_{I_{1} j}, \kappa_{i I_{2}}$ and $\kappa_{i j}$ have form as in (7). Moreover,

$$
\begin{gathered}
\frac{\prod_{(u, v) \in E\left(i I_{2}\right)} \eta_{u, v} \prod_{(u, v) \in E\left(I_{1} j\right)} \eta_{u, v}}{\prod_{(u, v) \in E(i j)} \eta_{u, v}}=\prod_{(u, v) \in E(I)} \eta_{u, v} \\
\prod_{h \in N\left(i I_{2}\right)} \bar{\mu}_{h}^{\operatorname{deg} h-2}=\prod_{h \in N\left(v I_{2}\right)} \bar{\mu}_{h}^{\operatorname{deg} h-2}
\end{gathered}
$$

$$
\prod_{h \in N\left(I_{1} j\right)} \bar{\mu}_{h}^{\operatorname{deg} h-2}=\prod_{h \in N\left(I_{1} u\right)} \bar{\mu}_{h}^{\operatorname{deg} h-2}
$$

Using this we can write

$$
\kappa_{I_{1} I_{2}}=\frac{1}{4} \frac{\left(1-\bar{\mu}_{r\left(i I_{2}\right)}^{2}\right)\left(1-\bar{\mu}_{r\left(I_{1} j\right)}^{2}\right)}{\left(1-\bar{\mu}_{r(i j)}^{2}\right)} \prod_{h \in N(I)} \bar{\mu}_{h}^{\operatorname{deg} h-2} \prod_{(u, v) \in E(I)} \eta_{u, v}
$$

The root of $T(I)$ is either in $T\left(I_{1} u\right)$ or in $T\left(v I_{2}\right)$. In the first case $r\left(I_{1} j\right)=r(I)$ and $r\left(i I_{2}\right)=r(i j)$. In the second case $r\left(I_{1} j\right)=r(i j)$ and $r\left(i I_{2}\right)=r(I)$. Hence in both cases

$$
\frac{\left(1-\bar{\mu}_{r\left(i I_{2}\right)}^{2}\right)\left(1-\bar{\mu}_{r\left(I_{1} j\right)}^{2}\right)}{\left(1-\bar{\mu}_{r(i j)}^{2}\right)}=\left(1-\bar{\mu}_{r(I)}^{2}\right)
$$

and (38) has the required form given by (20). It follows that $K=\psi_{T}\left(\omega_{0}\right)$.
It now remains to show that the parameters defined in (34), (35) and (36) define a parameter vector $\omega_{0}$ which lies in $\Omega_{T}$. Since, by (C2), $\mu_{i j k}^{2} \leq \operatorname{Det} P^{i j k}$ for all $i, j, k \in[n]$ for all inner nodes $h$ we have $\bar{\mu}_{h}^{0} \in[-1,1]$ as required. For a terminal edge $(v, i)$ consider the marginal model induced by $T(i j k)$, where $j, k$ are any two leaves such that $v$ separates $i, j, k$ in $T$. From Proposition 2.5 constraints (C2) and (C3) imply that $\eta_{v, i}$ is a valid parameter. To show that (36) satisfies (5) write

$$
\left(1 \pm \bar{\mu}_{u}^{0}\right) \eta_{u, v}^{0}=\left(1 \pm s(u, i) s(u, j) s(u, k) \frac{\mu_{i j k}}{\sqrt{\operatorname{Det} P^{i j k}}}\right) s(u, v)\left|\frac{\mu_{i l}}{\mu_{i j}}\right| \sqrt{\frac{\operatorname{Det} P^{i j k}}{\operatorname{Det} P^{i k l}}}
$$

Now substitute this together with the expressions for $\bar{\mu}_{u}^{0}$ and $\bar{\mu}_{v}^{0}$, given by (34), into (5). First assume $s(u, v)=1$. Then $s(u, k)=s(v, k), s(v, i)=s(u, i)$ and (5) becomes

$$
\left(\sqrt{\operatorname{Det} P^{i j k}} \pm s(u, i) \mu_{i j k}\right)\left|\frac{\mu_{i l}}{\mu_{i j}}\right| \leq\left(\sqrt{\operatorname{Det} P^{i k l}} \pm s(v, l) \mu_{i k l}\right)
$$

By multiplying both sides by a positive expression $\left|\mu_{j l}\right|\left(\sqrt{\operatorname{Det} P^{i j k}} \mp s(u, i) \mu_{i j k}\right)$ we obtain

$$
4 \mu_{i k}^{2} \mu_{j l}^{2} \leq\left(\sqrt{\operatorname{Det} P^{i j k}} \pm s(u, l) \mu_{j l} \mu_{i j k}\right)\left(\sqrt{\operatorname{Det} P^{i k l}} \mp s(v, l) \mu_{i k l}\right)
$$

However, $s(u, l)=s(v, l)$ hence this is satisfied by (C5). It is easily calculated that the case $s(u, v)=-1$ leads to the same constraint. This finishes the proof of Lemma C.2.

Lemma C.3. The inclusion $\mathcal{M} \subseteq \mathcal{M}_{T}^{n}$ holds.
Proof. Let $K \in \mathcal{M}$ be a tree cumulant and let $\Sigma=\left[\mu_{i j}\right] \in \mathbb{R}^{n \times n}$ be the matrix of all covariances between the leaves. We say that an edge $e \in E$ is isolated relative to $K$ if $\mu_{i j}=0$ for all $i, j \in[n]$ such that $e \in E(i j)$. By $\widetilde{E} \subseteq E$ we denote the set of all edges of $T$ which are isolated relative to $K$. By $\widetilde{T}=(V, E \backslash \widetilde{E})$ we

denote the forest obtained from $T$ by removing edges in $\widetilde{E}$ and we call it the $K$-forest. We define relations on $\widetilde{E}$ and $E \backslash \widetilde{E}$. For two edges $e, e^{\prime}$ with either $\left\{e, e^{\prime}\right\} \subset \widetilde{E}$ or $\left\{e, e^{\prime}\right\} \subset E \backslash \widetilde{E}$ write $e \sim e^{\prime}$ if either $e=e^{\prime}$ or $e$ and $e^{\prime}$ are adjacent and all the edges that are incident with both $e$ and $e^{\prime}$ are isolated relative to $K$. Let us now take the transitive closure of $\sim$ restricted to pairs of edges in $\widetilde{E}$ to form an equivalence relation on $\widetilde{E}$. This transitive closure is constructed as follows. Consider a graph with nodes representing elements of $\widetilde{E}$ and put an edge between $e, e^{\prime}$ whenever $e \sim e^{\prime}$. Then the equivalence classes correspond to connected components of this graph. Similarly, take the transitive closure of $\sim$ restricted to the pairs of edges in $E \backslash \widetilde{E}$ to form an equivalence relation in $E \backslash \widetilde{E}$. We will let $[\widetilde{E}]$ and $[E \backslash \widetilde{E}]$ denote the set of equivalence classes of $\widetilde{E}$ and $E \backslash \widetilde{E}$ respectively (for details see [40, Section 5]).

Again we show that there exists $\omega_{0} \in \Omega_{T}$ such that $\psi_{T}\left(\omega_{0}\right)=K$. Set $\eta_{u, v}^{0}=0$ for all $(u, v) \in \widetilde{E}$ and $\bar{\mu}_{v}^{0}=0$ for all inner nodes of $T$ with degree zero in $\widetilde{T}$. It then follows that $\left(1 \pm \bar{\mu}_{u}\right) \eta_{u, v}=0$ satisfies (5) for all $(u, v) \in \widetilde{E}$ and $\bar{\mu}_{v}^{0} \in[-1,1]$ for all $v \in \widetilde{V}$ and hence these parameters satisfy constraints defining $\Omega_{T}$. If $I \subseteq[n]$ is such that $E(I) \cap \widetilde{E} \neq \emptyset$ then $\kappa_{I}=0$ by (C3). Hence in this case we can assert that

$$
\kappa_{I}=\frac{1}{4}\left(1-\left(\bar{\mu}_{v(I)}^{0}\right)^{2}\right) \prod_{v \in N(I)}\left(\bar{\mu}_{v}^{0}\right)^{\operatorname{deg}(v)-2} \prod_{(u, v) \in E(I)} \eta_{u, v}^{0}
$$

simply because both sides of this equation are zero. By [40, Remark 5.2 (iv)] every connected component of $\widetilde{T}$ is a subtree which is either an inner node or a tree with the set of leaves contained in $[n]$. Denote the connected subtrees which are not inner nodes by $T_{1}, \ldots, T_{k}$ and their sets of leaves by $\left[n_{l}\right]$ for $l=1, \ldots, k$. For every $l=1, \ldots, k$ and all $i, j \in\left[n_{l}\right]$ we have that $\mu_{i j} \neq 0$. Hence for each $T_{l}$ applying Lemma C. 2 we have $K^{\left[n_{l}\right]} \in \mathcal{M}_{T_{l}}$. If $I \subseteq[n]$ is such that $E(I) \cap \widetilde{E}=\emptyset$ then $I \subseteq\left[n_{l}\right]$ for some $l=1, \ldots, k$. Since $K^{\left[n_{l}\right]} \in \mathcal{M}_{T_{l}}$ then there exists a choice of parameters such that $\kappa_{I}$ can be written as (7). Therefore $K \in \mathcal{M}_{T}$ and we are done.

The proof that $\mathcal{M}=\mathcal{M}_{T}^{a}$ follows from Lemma C. 1 and Lemma C.3. It suffices to show that, given that all covariances are non-zero, the only constraints of $\mathcal{M}$ involving only second order moments are (16). In the formulation of the main result the only such constraints are all the equations in (C1) involving only covariances and the positivity constraints in (C2). By the four-point condition (c.f. (14)) the inequalities

$$
\min \left\{\left(\frac{\mu_{i k} \mu_{j l}}{\mu_{i j} \mu_{k l}}\right)^{2},\left(\frac{\mu_{i l} \mu_{j k}}{\mu_{i j} \mu_{k l}}\right)^{2}\right\} \leq 1
$$

for all not necessarily distinct $i, j, k, l \in[n]$ uniquely define the underlying tree metric and hence they are equivalent to all the equations in (C1) involving only second order moments. The inequalities

$$
\min \left\{\frac{\mu_{i k} \mu_{j l}}{\mu_{i j} \mu_{k l}}, \frac{\mu_{i l} \mu_{j k}}{\mu_{i j} \mu_{k l}}\right\} \geq 0
$$

are equivalent to $\mu_{i j} \mu_{i k} \mu_{j k} \geq 0$ for all $i, j, k \in[n]$. However, the two above sets of inequalities are exactly equivalent to (16).

# Appendix D: Phylogenetic invariants 

In a seminal paper Allman and Rhodes [2] identified equations defining the general Markov $\mathcal{M}_{T}$ in the case when $T$ is a trivalent tree. In this section we relate their results to ours. To introduce their main theorem we need the following definition.

Definition D.1. Let $X=\left(X_{1}, \ldots, X_{n}\right)$ be a vector of binary random variables and let $P=\left(p_{\gamma}\right)_{\gamma \in\{0,1\}^{n}}$ be a $2 \times \ldots \times 2$ table of the joint distribution of $X$. Let $A \mid B$ form a split of $[n]$. Then the flattening of $P$ induced by the split is a matrix

$$
P_{A \mid B}=\left[p_{\alpha \beta}\right], \quad \alpha \in\{0,1\}^{|A|}, \beta=\{0,1\}^{|B|}
$$

where $p_{\alpha \beta}=\mathbb{P}\left(X_{A}=\alpha, X_{B}=\beta\right)$. Let $T=(V, E)$ be a tree. In particular, for edge partitions the induced flattening is called an edge flattening and we denote it by $P_{e}$, where $e \in E$ is the edge inducing the split.

Note that whenever we implicitly use some order on coordinates indexed by $\{0,1\}$-sequences we always mean the order induced by the lexicographic order on $\{0,1\}$-sequences such that $0 \cdots 00>0 \cdots 01>\ldots>1 \cdots 11$. This gives in particular the ordering of rows and columns of flattenings.

Theorem D. 2 (Allman, Rhodes [2]). Let $T^{r}$ be a trivalent tree rooted in $r$ and $\mathcal{M}_{T}$ be the general Markov model on $T^{r}$ as defined by (2). Then the smallest algebraic variety, i.e. a subset of a real space defined by a finite set of polynomial equations, containing the general Markov model, is defined by vanishing of all $3 \times 3$-minors of all the edge flattenings of $T^{r}$ together with the trivial polynomial equation $\sum_{\alpha} p_{\alpha}=1$.

Note that the result includes the case of the tripod tree model since in this case each edge flattening of the joint probability table is a $2 \times 4$ table so there are no $3 \times 3$ minors and hence there are no non-trivial polynomials vanishing on the model.

Just as we defined edge flattenings of probability tables we can also define edge flattenings of $\left(\kappa_{I}\right)_{I \subseteq[n]}$ where $\kappa_{\emptyset}=1$ and $\kappa_{i}=0$ for all $i \in[n]$ (c.f. Appendix A). Let $e$ be an edge of $T$ inducing a split $A \mid B \in \Pi_{T}$ such that $|A|=r,|B|=n-r$. Then $\widetilde{N}_{e}$ is a $2^{r} \times 2^{n-r}$ matrix such that for any two subsets $I \subseteq A, J \subseteq B$ the element of $\widetilde{N}_{e}$ corresponding to the $I$-th row and the $J$-th column is $\kappa_{I J}$. Let $N_{e}$ denote its submatrix given by removing the column and the row corresponding to empty subsets of $A$ and $B$. Here the labeling for the rows and columns is induced by the ordering of the rows and columns for $P_{e}$ (c.f. Definition D.1), i.e. all the subsets of $A$ and $B$ are coded as $\{0,1\}$-vectors and we introduce the lexicographic order on the vectors with the vector of ones being the last one.

The following result allows us to rephrase the equations in Theorem D. 2 in terms of our new coordinates.

Proposition D.3. Let $T=(V, E)$ be a tree and let $P$ be a probability distribution of a vector $X=\left(X_{1}, \ldots, X_{n}\right)$ of binary variables represented by the leaves of $T$. If $e \in E$ is an edge of $T$ inducing a split $A_{1} \mid A_{2}$ then $\operatorname{rank}\left(P_{e}\right)=2$ if and only if $\operatorname{rank}\left(N_{e}\right)=1$.
Proof. Let $P_{e}=\left[p_{\alpha \beta}\right]$ be the matrix induced by a split $A_{1} \mid A_{2}$. We will show that $\operatorname{rank}\left(P_{e}\right)=\operatorname{rank}\left(D_{e}\right)$ where $D_{e}=\left[d_{I J}\right]$ is a block diagonal matrix with 1 as the first $1 \times 1$ block (i.e. $d_{\emptyset \emptyset}=1, d_{\emptyset J}=0, d_{I \emptyset}=0$ for all $I \subseteq A_{1}, J \subseteq A_{2}$ ) and the matrix $N_{e}$ as the second block. It will then follow that $\operatorname{rank}\left(P_{e}\right)=2$ if and only if $\operatorname{rank}\left(N_{e}\right)=1$.

First note that the flattening matrix $P_{e}$ can be transformed to the flattening of the non-central moments just by adding rows and columns according to (17) and then to the flattening of the central moments $M_{e}=\left[\mu_{I J}\right]$ such that $I \subseteq A_{1}$, $J \subseteq A_{2}$ using (18). It therefore suffices to show that $\operatorname{rank}\left(M_{e}\right)=\operatorname{rank}\left(D_{e}\right)$.

Let $I \subseteq A_{1}, J \subseteq A_{2}$. Then for each $\pi \in \Pi_{T(I J)}$ there is at most one block containing elements from both $I$ and $J$. For if this were not so then removing $e$ would increase the number of blocks in $\pi$ by more than one which is not possible. Denote this block by $\left(I^{\prime} J^{\prime}\right)$ where $I^{\prime} \subseteq I, J^{\prime} \subseteq J$. Note that by construction we have either both $I^{\prime}, J^{\prime}$ are empty sets if $\pi \geq A_{1} \mid A_{2}$ in $\Pi_{T(I J)}$ or both $I^{\prime}, J^{\prime} \neq \emptyset$ otherwise. We can rewrite (20) as

$$
\mu_{I J}=\sum_{\pi \in \Pi_{T(I J)}}\left(\kappa_{I^{\prime} J^{\prime}} \prod_{I \supseteq B \in \pi} \kappa_{B} \prod_{J \supseteq B \in \pi} \kappa_{B}\right)
$$

We have $d_{I^{\prime} J^{\prime}}=\kappa_{I^{\prime} J^{\prime}}$ and it can be further rewritten as

$$
\mu_{I J}=\sum_{I^{\prime} \subseteq I} \sum_{J^{\prime} \subseteq J} u_{I I^{\prime}} d_{I^{\prime} J^{\prime}} v_{J^{\prime} J}
$$

where $u_{I I^{\prime}}=\sum_{\pi \in \Pi_{T}\left(I \backslash I^{\prime}\right)} \prod_{B \in \pi} \kappa_{B}$ and $v_{J^{\prime} J}=\sum_{\pi \in \Pi_{T}\left(J \backslash J^{\prime}\right)} \prod_{B \in \pi} \kappa_{B}$. Setting $u_{I I^{\prime}}=0$ for $I^{\prime} \nsubseteq I, v_{J^{\prime} J}=0$ for $J^{\prime} \nsubseteq J$ we can write these coefficients in terms of a lower triangular matrix $U$ and an upper triangular matrix $V$. Since by construction $u_{I I}=1$ for all $I \subseteq A_{1}$ and $v_{J J}=1$ for all $J \subseteq A_{2}$ we have $\operatorname{det} U=\operatorname{det} V=1$. Therefore, $M_{e}$ has the same rank as $D_{e}$.

The proposition shows that the vanishing of all $3 \times 3$ minors of all the edge flattenings of $P$ and the trivial invariant $\sum p_{\alpha}=1$ are together equivalent to the vanishing all $2 \times 2$ minors of all edge flattenings of $\kappa=\left(\kappa_{I}\right)_{I \in[n]_{>3}}$. An immediate corollary follows which gives the equations in (C1) in Theorem (4.7).

Corollary D.4. Let $T=(V, E)$ be a trivalent tree. Then the smallest algebraic variety containing $\mathcal{M}_{T}^{n}$ is defined by the following set of equations. For each split $A \mid B$ induced by an edge consider any four (not necessarily disjoint) nonempty sets $I_{1}, I_{2} \subseteq A, J_{1}, J_{2} \subseteq B$ and the induced equation $\kappa_{I_{1} J_{1}} \kappa_{I_{2} J_{2}}-\kappa_{I_{1} J_{2}} \kappa_{I_{2} J_{1}}=0$.

In [16] Eriksson noted that some of the invariants usually prove to be better in discriminating between different tree topologies than the others. His simulations showed that the invariants related to the four-point condition were especially powerful. The binary case we consider in this paper can give some partial understanding of why this might be so. Here, the invariants related to the four-point condition are the only ones which involve second order moments (c.f. Section 4). Moreover, the estimates of the higher-order moments (or cumulants) are sensitive to outliers and their variance generally grows with the order of the moment. Let $\hat{\mu}$ be a sample estimator of the central moments $\mu$ and let $f$ be one of the polynomials in Theorem D. 4 but expressed in terms of the central moments. Then using the delta method we have

$$
\operatorname{Var}(f(\hat{\mu})) \simeq \nabla f(\mu)^{t} \operatorname{Var}(\hat{\mu}) \nabla f(\mu)
$$

Consequently, in this loose sense at least, the higher the order of the central moments (or equivalently the higher the order of the tree cumulants) the higher the variability of we might expect the invariant to exhibit (see [25, Section 4.5]).
