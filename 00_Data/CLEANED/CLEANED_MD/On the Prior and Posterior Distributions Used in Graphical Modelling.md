# On the Prior and Posterior Distributions Used in Graphical Modelling 

Marco Scutari *


#### Abstract

Graphical model learning and inference are often performed using Bayesian techniques. In particular, learning is usually performed in two separate steps. First, the graph structure is learned from the data; then the parameters of the model are estimated conditional on that graph structure. While the probability distributions involved in this second step have been studied in depth, the ones used in the first step have not been explored in as much detail.

In this paper, we will study the prior and posterior distributions defined over the space of the graph structures for the purpose of learning the structure of a graphical model. In particular, we will provide a characterisation of the behaviour of those distributions as a function of the possible edges of the graph. We will then use the properties resulting from this characterisation to define measures of structural variability for both Bayesian and Markov networks, and we will point out some of their possible applications.


Keywords: Markov Networks, Bayesian Networks, Random Graphs, Structure Learning, Multivariate Discrete Distributions.

Graphical models (Pearl 1988; Lauritzen 1996) stand out among other classes of statistical models because of their use of graph structures in modelling and performing inference on multivariate, high-dimensional data. The close relationship between their probabilistic properties and the topology of the underlying graphs represents one of their key features, as it allows an intuitive understanding of otherwise complex models.

In a Bayesian setting, this duality leads naturally to splitting model estimation (which is usually called learning) in two separate steps (Cowell et al. 2007). In the first step, called structure learning, the graph structure $\mathcal{G}$ of the model is estimated from the data. The presence (absence) of a particular edge between two nodes in $\mathcal{G}$ implies the conditional (in)dependence of the variables corresponding to such nodes. In the second step, called parameter learning, the parameters $\Theta$ of the distribution assumed for the data are estimated conditional to the graph structure obtained in the first step. If we denote a graphical model with $\mathcal{M}$, so that $\mathcal{M}=(\mathcal{G}, \Theta)$, then we can write graphical model estimation from a data set $\mathcal{D}$ as

$$
\mathrm{P}(\mathcal{M} \mid \mathcal{D})=\mathrm{P}(\mathcal{G} \mid \mathcal{D}) \mathrm{P}(\Theta \mid \mathcal{G}, \mathcal{D})
$$

Furthermore, following Heckerman et al. (1995), we can rewrite structure learning as

$$
\mathrm{P}(\mathcal{G} \mid \mathcal{D}) \propto \mathrm{P}(\mathcal{G}) \mathrm{P}(\mathcal{D} \mid \mathcal{G})
$$

The prior distribution $\mathrm{P}(\mathcal{G})$ and the corresponding posterior distribution $\mathrm{P}(\mathcal{G} \mid \mathcal{D})$ are defined over the space of the possible graph structures, say $\mathbf{G}$. Since the dimension of $\mathbf{G}$

[^0]
[^0]:    *Genetics Institute, University College London, United Kingdom, m.scutari@ucl.ac.uk

grows super-exponentially with the number of nodes in the graph (Harary and Palmer 1973), it is common practice to choose

$$
\mathrm{P}(\mathcal{G})=\frac{1}{|\mathbf{G}|} \quad \text { for every } \mathcal{G} \in \mathbf{G}
$$

as a non-informative prior, and then to search for the graph structure $\mathcal{G}$ that maximises $\mathrm{P}(\mathcal{G} \mid \mathcal{D})$. Unlike such a maximum a posteriori (MAP) approach, a full Bayesian analysis is computationally unfeasible in most real-world settings (Friedman et al. 1999a; Koller and Friedman 2009). Therefore, inference on most aspects of $\mathrm{P}(\mathcal{G})$ and $\mathrm{P}(\mathcal{G} \mid \mathcal{D})$ is severely limited by the nature of the graph space.

In this paper, we approach the analysis of those probability distributions from a different angle. We start from the consideration that, in a graphical model, the presence of particular edges and their layout are the most interesting features of the graph structure. Therefore, investigating $\mathrm{P}(\mathcal{G})$ and $\mathrm{P}(\mathcal{G} \mid \mathcal{D})$ through the probability distribution they induce over the set $\mathcal{E}$ of their possible edges (identified by the set of unordered pairs of nodes in $\mathcal{G}$ ) provides a better basis from which to develop Bayesian inference on $\mathcal{G}$. This can be achieved by modelling $\mathcal{E}$ as a multivariate discrete distribution encoding the joint state of the edges. Then, as far as inference on $\mathcal{G}$ is concerned, we may rewrite Equation 1 as

$$
\mathrm{P}(\mathcal{G}(\mathcal{E}) \mid \mathcal{D}) \propto \mathrm{P}(\mathcal{G}(\mathcal{E})) \mathrm{P}(\mathcal{D} \mid \mathcal{G}(\mathcal{E}))
$$

As a side effect, this shift in focus reduces the effective dimension of the sample space under consideration from super-exponential (the dimension of $\mathbf{G}$ ) to polynomial (the dimension of $\mathcal{E}$ ) in the number of nodes. The dimension of the parameter space for many inferential tasks, such as the variability measures studied in this paper, is likewise reduced.

The content of the paper is organised as follows. Basic definitions and notations are introduced in Section 1. The multivariate distributions used to model $\mathcal{E}$ are described in Section 2. Some properties of the prior and posterior distributions on the graph space, $\mathrm{P}(\mathcal{G}(\mathcal{E}))$ and $\mathrm{P}(\mathcal{G}(\mathcal{E}) \mid \mathcal{D})$, are derived in Section 3. We will focus mainly on those properties related with the first and second order moments of the distribution of $\mathcal{E}$, and we will use them to characterise several measures of structural variability in Section 4. These measures may be useful for several inferential tasks for both Bayesian and Markov networks; some will be sketched in Section 4. Conclusions are summarised in Section 5, and proofs for the theorems in Sections 2 to 4 are reported in Appendix 5. Appendix 5 lists the exact values for some quantities of interest for $\mathrm{P}(\mathcal{G}(\mathcal{E}))$, computed for several graph sizes.

# 1 Definitions and notations 

Graphical models (Lauritzen 1996; Pearl 1988) are a class of statistical models which combine the rigour of a probabilistic approach with the intuitive representation of relationships given by graphs. They are composed by a set $\mathbf{X}=\left\{X_{1}, \ldots, X_{n}\right\}$ of random variables describing the data $\mathcal{D}$ and a graph $\mathcal{G}=(\mathbf{V}, E)$ in which each vertex or node

$v \in \mathbf{V}$ is associated with one of the random variables in $\mathbf{X}$. Nodes and the corresponding variables are usually referred to interchangeably. The edges $e \in E$ are used to express the dependence relationships among the variables in $\mathbf{X}$. Different classes of graphs express these relationships with different semantics, having in common the principle that graphical separation of two vertices implies the conditional independence of the corresponding random variables (Pearl 1988). The two examples most commonly found in literature are Markov networks (Whittaker 1990; Edwards 2000), which use undirected graphs (UGs, see Diestel 2005), and Bayesian networks (Neapolitan 2003; Korb and Nicholson 2010), which use directed acyclic graphs (DAGs, see Bang-Jensen and Gutin 2009). In the context of Bayesian networks, edges are often called arcs and denoted with $a \in A$; we will adopt this notation as well.

The structure of $\mathcal{G}$ (that is, the pattern of the nodes and the edges) determines the probabilistic properties of a graphical model. The most important, and the most used, is the factorisation of the global distribution (the joint distribution of $\mathbf{X}$ ) into a set of lower-dimensional local distributions. In Markov networks, local distributions are associated with cliques (maximal subsets of nodes in which each element is adjacent to all the others); in Bayesian networks, each local distribution is associated with one node conditional on its parents (nodes linked by an incoming arc). In Markov networks the factorisation is unique; different graph structures correspond to different probability distributions. This is not so in Bayesian networks, where DAGs can be grouped into equivalence classes which are statistically indistinguishable. Each such class is uniquely identified by the underlying UG (i.e. in which arc directions are disregarded, also known as the skeleton) and by the set of $v$-structures (i.e. converging connections of the form $v_{i} \rightarrow v_{j} \leftarrow v_{k}, i \neq j \neq k$, in which $v_{i}$ and $v_{k}$ are not connected by an arc) common to all elements of the class. In addition, Bayesian networks can be represented by their moral graphs (Pearl 1988), the UGs obtained by "marrying" the parents in the v-structures and disregarding arc directions, to facilitate comparisons with Markov networks.

As for the global and the local distributions, there are many possible choices depending on the nature of the data and the aims of the analysis. However, the literature has focused mostly on two cases: the discrete case (Whittaker 1990; Heckerman et al. 1995), in which both the global and the local distributions are multinomial random variables, and the continuous case (Whittaker 1990; Geiger and Heckerman 1994), in which the global distribution is multivariate normal and the local distributions are univariate (in Bayesian networks) or multivariate (in Markov networks) normal random variables. In the former, the parameters of interest $\Theta$ are the conditional probabilities associated with each variable, usually represented as conditional probability tables. In the latter, the parameters of interest $\Theta$ are the partial correlation coefficients between each variable and its neighbours in $\mathcal{G}$. Conjugate distributions (Dirichlet and Wishart, respectively) are then used for learning and inference in a Bayesian setting.

# 2 Multivariate discrete distributions 

The choice of an appropriate probability distribution for the set $\mathcal{E}$ of the possible edges is crucial to make the derivation and the interpretation of the properties of $\mathcal{E}$ and $\mathcal{G}(\mathcal{E})$ easier. We will first note that a graph is uniquely identified by its edge set $E$ (or by its arc set $A$ for a DAG), and that each edge $e_{i j}$ or arc $a_{i j}$ is uniquely identified by the nodes $v_{i}$ and $v_{j}, i \neq j$ it is incident on. Therefore, if we model $\mathcal{E}$ with a random variable we have that any edge set $E$ (or arc set $A$ ) is just an element of its sample space; and since there is a one-to-one correspondence between graphs and edge sets, probabilistic properties and inferential results derived for traditional graph-centric approaches can easily be adapted to this new edge-centric approach and vice versa. In addition, if we denote $\mathcal{E}=\left\{\left(v_{i}, v_{j}\right), i \neq j\right\}$, we can clearly see that $|\mathcal{E}|=\mathcal{O}\left(|\mathbf{V}|^{2}\right)$. On the other hand, $|\mathbf{G}|=\mathcal{O}\left(2^{|\mathbf{V}|^{2}}\right)$ for UGs and even larger for DAGs (Robinson 1973; Harary and Palmer 1973) and their equivalence classes (Gillispie and Perlman 2002).

We will also note that an edge or an arc has only few possible states:

- an edge can be either present $\left(e_{i j} \in E\right)$ or missing from an $\mathrm{UG}\left(e_{i j} \notin E\right)$;
- in a DAG, an arc can be present in one of its two possible directions ( $\overline{\Lambda_{i j}} \in A$ or $\overline{a_{i j}} \in A$ ) or missing from the graph ( $\overline{\Lambda_{i j}} \notin A$ and $\overline{a_{i j}} \notin A$ ).

This leads naturally to the choice of a Bernoulli random variable for the former,

$$
e_{i j} \sim E_{i j}= \begin{cases}1 & e_{i j} \in E \text { with probability } p_{i j} \\ 0 & e_{i j} \notin E \text { with probability } 1-p_{i j}\end{cases}
$$

and to the choice of a Trinomial random variable for the latter,

$$
a_{i j} \sim A_{i j}= \begin{cases}-1 & \overline{\Lambda_{i j}} \in A \text { with probability } \overline{p_{i j}} \\ 0 & \overline{\Lambda_{i j}}, \overline{a_{i j}} \notin A \text { with probability } \overline{p_{i j}} \\ 1 & \overline{a_{i j}} \in A \text { with probability } \overline{p_{i j}}\end{cases}
$$

where $\overline{a_{i j}}$ is the arc $v_{i} \rightarrow v_{j}$ and $\overline{\Lambda_{i j}}$ is the arc $v_{j} \rightarrow v_{i}$. Therefore, a graph structure can be modelled through its edge or arc set as follows:

- UGs, such as Markov networks or the skeleton and the moral graph of Bayesian networks, can be modelled by a multivariate Bernoulli random variable;
- directed graphs, such as the DAGs used in Bayesian networks, can be modelled by a multivariate Trinomial random variable.

In addition to being the natural choice for the respective classes of graphs, these distributions integrate smoothly with and extend other approaches present in the literature. For example, the probabilities associated with each edge or arc correspond to the confidence coefficients from Friedman et al. (1999a) and the arc strengths from Imoto et al. (2002). In a frequentist setting, they have been estimated using bootstrap resampling (Efron and Tibshirani 1993); in a Bayesian setting, Markov chain Monte Carlo (MCMC) approaches (Friedman and Koller 2003; Melançon and Fabrice 2004) have been used instead.

# 2.1 Multivariate Bernoulli 

Let $B_{1}, \ldots, B_{k}, k \in \mathbb{N}$ be Bernoulli random variables with marginal probabilities of success $p_{1}, \ldots, p_{k}$, that is $B_{i} \sim \operatorname{Ber}\left(p_{i}\right), i=1, \ldots, k$. Then the distribution of the random vector $\mathbf{B}=\left[B_{1}, \ldots, B_{k}\right]^{T}$ over the joint probability space of $B_{1}, \ldots, B_{k}$ is a multivariate Bernoulli random variable (Krummenauer 1998), denoted as $\operatorname{Ber}_{k}(\mathbf{p})$. Its probability function is uniquely identified by the parameter collection

$$
\mathbf{p}=\left\{p_{I}: I \subseteq\{1, \ldots, k\}, I \neq \varnothing\right\}
$$

which represents the dependence structure among the $B_{i}$ in terms of simultaneous successes for every non-empty subset $I$ of elements of $\mathbf{B}$. Other characterisations and fundamental properties of the multivariate Bernoulli distribution can be found in Johnson et al. (1997). Kocherlakota and Kocherlakota (1992) focus on the bivariate models specific to $\operatorname{Ber}_{2}(\mathbf{p})$. Additional characterisations and results specific to particular applications can be found in George and McCulloch (1997, variable selection), Farrell and Rogers-Stewart (2008, longitudinal studies), Rubinstein (1999, combinatorial optimisation) and Agresti and Klingenberg (2005, clinical trials), among others.

From the literature we know that the expectation and the covariance matrix of $\mathbf{B}$ are immediate extensions of the corresponding univariate Bernoulli ones;

$$
\mathrm{E}(\mathbf{B})=\left[p_{1}, \ldots p_{k}\right]^{T} \quad \text { and } \quad \operatorname{COV}(\mathbf{B})=\left[\sigma_{i j}\right]=p_{i j}-p_{i} p_{j}
$$

In particular, the covariance matrix $\Sigma=\left[\sigma_{i j}\right]$ has some interesting numerical properties. From basic probability theory, we know its diagonal elements $\sigma_{i i}$ are bounded in the interval $\left[0, \frac{1}{4}\right]$; the maximum is attained for $p_{i}=\frac{1}{2}$, and the minimum for both $p_{i}=0$ and $p_{i}=1$. For the Cauchy-Schwarz theorem then $\left|\sigma_{i j}\right| \in\left[0, \frac{1}{4}\right]$. As a result, we can derive similar bounds for the eigenvalues $\lambda_{1}, \ldots, \lambda_{k}$ of $\Sigma$, as shown in the following theorem.
Lemma 2.1. Let $\mathbf{B} \sim \operatorname{Ber}_{k}(\mathbf{p})$, and let $\Sigma$ be its covariance matrix. Let $\lambda_{i}, i=1, \ldots, k$ be the eigenvalues of $\Sigma$. Then

$$
0 \leqslant \sum_{i=1}^{k} \lambda_{i} \leqslant \frac{k}{4} \quad \text { and } \quad 0 \leqslant \lambda_{i} \leqslant \frac{k}{4}
$$

Proof. See Appendix 5.
These bounds define a closed convex set in $\mathbb{R}^{k}$, described by the family

$$
\mathcal{L}=\left\{\Delta^{k-1}(c): c \in\left[0, \frac{k}{4}\right]\right\}
$$

where $\Delta^{k-1}(c)$ is the non-standard $k-1$ simplex

$$
\Delta^{k-1}(c)=\left\{\left(\lambda_{1}, \ldots, \lambda_{k}\right) \in \mathbb{R}^{k}: \sum_{i=1}^{k} \lambda_{i}=c, \lambda_{i} \geqslant 0\right\}
$$

# 2.2 Multivariate Trinomial 

Construction and properties of the multivariate Trinomial random variable are similar to the ones illustrated in the previous section for the multivariate Bernoulli. For this reason, and because it is a particular case of the multivariate multinomial distribution, the multivariate Trinomial distribution is rarely the focus of research efforts in literature. Some of its fundamental properties are covered either in Johnson et al. (1997) or in monographs on contingency tables analysis such as Bishop et al. (2007).
Let $T_{1}, \ldots, T_{k}, k \in \mathbb{N}$ be Trinomial random variables assuming values $\{-1,0,1\}$ and denoted as $T_{i} \sim \operatorname{Tri}\left(p_{i(-1)}, p_{i(0)}, p_{i(1)}\right)$ with $p_{i(-1)}+p_{i(0)}+p_{i(1)}=1$. Then the distribution of the random vector $\mathbf{T}=\left[T_{1}, \ldots, T_{k}\right]^{T}$ over the joint probability space of $T_{1}, \ldots, T_{k}$ is a multivariate Trinomial random variable, denoted as $\operatorname{Tr} i_{k}(\mathbf{p})$. The parameter collection $\mathbf{p}$ which uniquely identifies the distribution is

$$
\mathbf{p}=\left\{p_{I(T)}: I \subseteq\{1, \ldots, k\}, T \in \times_{i=1}^{|I|}\{-1,0,1\}, I \neq \varnothing\right\}
$$

where $\times$ denotes the cartesian product. The reduced parameter collection we will need to study its first and second order moments is

$$
\tilde{\mathbf{p}}=\left\{p_{i j(T)}: i, j=1, \ldots, k, T \in\{-1,0,1\}^{2}\right\}
$$

From the definition, we can easily derive the expected value and the variance of $T_{i}$,

$$
\begin{aligned}
\mathrm{E}\left(T_{i}\right) & =p_{i(1)}-p_{i(-1)} \\
\operatorname{VAR}\left(T_{i}\right) & =p_{i(1)}+p_{i(-1)}-\left[p_{i(1)}-p_{i(-1)}\right]^{2}
\end{aligned}
$$

and the covariance between two variables $T_{i}$ and $T_{j}$,

$$
\begin{aligned}
\operatorname{COV}\left(T_{i}, T_{j}\right)= & {\left[p_{i j(1,1)}-p_{i(1)} p_{j(1)}\right]+\left[p_{i j(-1,-1)}-p_{i(-1)} p_{j(-1)}\right] } \\
& -\left[p_{i j(-1,1)}-p_{i(-1)} p_{j(1)}\right]-\left[p_{i j(1,-1)}-p_{i(1)} p_{j(-1)}\right]
\end{aligned}
$$

Again, the diagonal elements of the covariance matrix $\Sigma$ are bounded. This can be proved either by solving the constrained maximisation problem

$$
\max _{p_{i(1)}, p_{i(-1)}} \operatorname{VAR}\left(T_{i}\right) \quad \text { s.t. } \quad p_{i(1)} \geqslant 0, p_{i(-1)} \geqslant 0, p_{i(1)}+p_{i(-1)} \leqslant 1
$$

or as an application of the following theorem by Moors and Muilwijk (1971).
Theorem 2.1. If a discrete random variable $X$ can take values only in the segment $\left[x_{1}, x_{n}\right]$ of the real axis, the maximum standard deviation of $X$ equals $\frac{1}{2}\left(x_{n}-x_{1}\right)$. The maximum is reached if $X$ takes the values $x_{1}$ and $x_{n}$ with probabilities $\frac{1}{2}$ each.

Proof. See Moors and Muilwijk (1971).

In both cases we obtain that the maximum variance is achieved for $p_{i(1)}=p_{i(-1)}=\frac{1}{2}$ and is equal to 1 , so $\sigma_{i i} \in[0,1]$ and $\left|\sigma_{i j}\right| \in[0,1]$. Furthermore, we can also prove that the eigenvalues of $\Sigma$ are bounded using the same arguments as in Lemma 2.1.
Lemma 2.2. Let $\mathbf{T} \sim \operatorname{Tr} i_{k}(\mathbf{p})$, and let $\Sigma$ be its covariance matrix. Let $\lambda_{i}, i=1, \ldots, k$ be the eigenvalues of $\Sigma$. Then

$$
0 \leqslant \sum_{i=1}^{k} \lambda_{i} \leqslant k \quad \text { and } \quad 0 \leqslant \lambda_{i} \leqslant k
$$

Proof. See the proof of Lemma 2.1 in Appendix 5.

These bounds define again a closed convex set in $\mathbb{R}^{k}$, described by the family

$$
\mathcal{L}=\left\{\Delta^{k-1}(c): c \in[0, k]\right\}
$$

where $\Delta^{k-1}(c)$ is the non-standard $k-1$ simplex from Equation 5.

Another useful result, which we will use in Section 3.2 to link inference on UGs and DAGs, is introduced below.
Theorem 2.2. Let $\mathbf{T} \sim \operatorname{Tr} i_{k}(\mathbf{p})$; then $|\mathbf{T}|=\mathbf{B} \sim \operatorname{Ber}_{k}\left(\mathbf{p}^{*}\right)$ and $\left|T_{i}\right|=B_{i} \sim \operatorname{Ber}\left(p^{*}\right)$

Proof. See Appendix 5.

It follows that the variance of each $T_{i}$ can be decomposed in two parts:

$$
\operatorname{VAR}\left(T_{i}\right)=\operatorname{VAR}\left(B_{i}\right)+4 p_{i(1)} p_{i(-1)}
$$

The first is a function of the corresponding component $\left|T_{i}\right|=B_{i}$ of the transformed random vector, while the second depends only on the probabilities associated with -1 and 1 (which correspond to $\widehat{\delta_{i j}}$ and $\widehat{a_{i j}}$ in Equation 4).

# 3 Properties of $\mathrm{P}(\mathcal{G}(\mathcal{E}))$ and $\mathrm{P}(\mathcal{G}(\mathcal{E}) \mid \mathcal{D})$ 

The results derived in the previous section provide the foundation for characterising $\mathrm{P}(\mathcal{G}(\mathcal{E}))$ and $\mathrm{P}(\mathcal{G}(\mathcal{E}) \mid \mathcal{D})$. To this end, it is useful to distinguish three cases corresponding to different configurations of the probability mass among the graph structures $\mathcal{G}(\mathcal{E}) \in \mathbf{G}$ :

- minimum entropy: the probability mass is concentrated on a single graph structure. This is the best possible configuration for $\mathrm{P}(\mathcal{G}(\mathcal{E}) \mid \mathcal{D})$, because only one edge set $E$ (or one arc set $A$ ) has a non-zero posterior probability. In other words, the data $\mathcal{D}$ provide enough information to identify a single graph $\mathcal{G}$ with posterior probability 1 ;
- intermediate entropy: several graph structures have non-zero probabilities. This is the case for informative priors $\mathrm{P}(\mathcal{G}(\mathcal{E}))$ and for the posteriors $\mathrm{P}(\mathcal{G}(\mathcal{E}) \mid \mathcal{D})$ resulting from real-world data sets;
- maximum entropy: all graph structures in $\mathbf{G}$ have the same probability. This is the worst possible configuration for $\mathrm{P}(\mathcal{G}(\mathcal{E}) \mid \mathcal{D})$, because it corresponds to the non-informative prior from Equation 2. In other words, the data $\mathcal{D}$ do not provide any information useful in identifying a high-posterior graph $\mathcal{G}$.

Clearly, minimum and maximum entropy are limiting cases for $\mathrm{P}(\mathcal{G}(\mathcal{E}) \mid \mathcal{D})$; the latter is non-informative about $\mathcal{G}(\mathcal{E})$, while the former identifies a single graph in $\mathbf{G}$. As we will show in Sections 3.1 (for UGs) and 3.2 (for DAGs), they provide useful reference points in determining which edges (or arcs) have significant posterior probabilities and in analysing the variability of the graph structure.

### 3.1 Undirected graphs

In the minimum entropy case, only one configuration of edges $E$ has non-zero probability, which means that

$$
p_{i j}= \begin{cases}1 & \text { if } e_{i j} \in E \\ 0 & \text { otherwise }\end{cases} \quad \text { and } \quad \Sigma=\mathbf{O}
$$

where $\mathbf{O}$ is the zero matrix.
The uniform distribution over $\mathbf{G}$ arising from the maximum entropy case has been studied extensively in random graph theory (Bollobás 2001); its two most relevant properties are that all edges $e_{i j}$ are independent and have $p_{i j}=\frac{1}{2}$. As a result, $\Sigma=\frac{1}{4} I_{k}$; all edges display their maximum possible variability, which along with the fact that they are independent makes this distribution non-informative for $\mathcal{E}$ as well as $\mathcal{G}(\mathcal{E})$.

The intermediate entropy case displays a middle-ground behaviour between the minimum and maximum entropy cases. The expected value and the covariance matrix of $\mathcal{E}$ do not have a definite form beyond the bounds derived in Section 2.1. When considering posteriors arising from real-world data, we have in practice that most edges in $\mathcal{E}$

represent conditional dependence relationships that are completely unsupported by the data. This behaviour has been explained by Pearl (2009) with the tendency of "good" graphical models to represent the causal relationships underlying the data, which are typically sparse. As a result, we have that $\mathrm{E}\left(e_{i j}\right)=0$ and $\operatorname{VAR}\left(e_{i j}\right)=0$ for many $e_{i j}$, so $\Sigma$ is almost surely singular unless such edges are excluded from the analysis. Edges that appear with $p_{i j} \simeq \frac{1}{2}$ have about the same marginal probability and variance as in the maximum entropy case, so their marginal behaviour is very close to random noise. On the other hand, edges with probabilities near 0 or 1 can be considered to have a good support (against or in favour, respectively). As $p_{i j}$ approaches 0 or $1, e_{i j}$ approaches its minimum entropy.

The closeness of a multivariate Bernoulli distribution to the minimum and maximum entropy cases can be represented in an intuitive way by considering the eigenvalues $\boldsymbol{\lambda}=\left[\lambda_{1}, \ldots, \lambda_{k}\right]^{T}$ of its covariance matrix $\Sigma$. Recall that the $\boldsymbol{\lambda}$ can assume values in the convex set $\mathcal{L}$ defined in Equation 5, which corresponds to the region of the first orthant delimited by the non-standard simplex $\Delta^{k-1}\left(\frac{k}{4}\right)$. In the minimum entropy case we have that $\Sigma=\mathbf{O}$, so $\lambda_{1}=\ldots=\lambda_{k}=0$, and in the maximum entropy case $\Sigma=\frac{1}{4} I_{k}$, so $\lambda_{1}=\ldots=\lambda_{k}=\frac{1}{4}$; both points lie on the boundary of $\mathcal{L}$, the first in the origin and the second in the middle of $\Delta^{k-1}\left(\frac{k}{4}\right)$. The distance between $\boldsymbol{\lambda}$ and these two points provides an intuitive way of measuring the variability of $\mathcal{E}$ and, indirectly, the entropy of the corresponding probability distributions $\mathrm{P}(\mathcal{G}(\mathcal{E}) \mid \mathcal{D})$ and $\mathrm{P}(\mathcal{G}(\mathcal{E}))$. It is important to note, however, that different distributions over $\mathbf{G}$ may have identical first and second order moments when modelled through $\mathcal{E}$. Such distributions will have the same $\boldsymbol{\lambda}$ and will therefore map to the same point in $\mathcal{L}$.

A simple example comprising three different distributions over a set of two edges is illustrated below.
Example 3.1. Consider three multivariate Bernoulli distributions $\mathbf{B}_{1}, \mathbf{B}_{2}, \mathbf{B}_{3}$ over two edges (denoted with $e_{1} \sim E_{1}$ and $e_{2} \sim E_{2}$ for brevity) with covariance matrices

$$
\Sigma_{1}=\left[\begin{array}{ll}
0.24 & 0.04 \\
0.04 & 0.24
\end{array}\right], \quad \Sigma_{2}=\left[\begin{array}{cc}
0.1056 & -0.0336 \\
-0.0336 & 0.2016
\end{array}\right], \quad \Sigma_{3}=\left[\begin{array}{ll}
0.1056 & 0.1456 \\
0.1456 & 0.2016
\end{array}\right]
$$

and eigenvalues

$$
\boldsymbol{\lambda}_{1}=\left[\begin{array}{l}
0.28 \\
0.20
\end{array}\right], \quad \boldsymbol{\lambda}_{2}=\left[\begin{array}{l}
0.2121 \\
0.095
\end{array}\right], \quad \boldsymbol{\lambda}_{3}=\left[\begin{array}{l}
0.3069 \\
0.0003
\end{array}\right]
$$

Their positions in $\mathcal{L}$ are shown in Figure 1. $\mathbf{B}_{1}$ is the closest to $\left(\frac{1}{4}, \frac{1}{4}\right)$, the point corresponding to the maximum entropy case, while $\mathbf{B}_{2}$ and $\mathbf{B}_{3}$ are farther from $\left(\frac{1}{4}, \frac{1}{4}\right)$ than $\mathbf{B}_{1}$ due to the increasing correlation between $e_{1}$ and $e_{2}$ (which are independent in the maximum entropy case). The correlation coefficients for $\mathbf{B}_{1}, \mathbf{B}_{2}$ and $\mathbf{B}_{3}$ are $\operatorname{COR}_{\mathbf{B}_{1}}\left(E_{1}, E_{2}\right)=0.1666, \operatorname{COR}_{\mathbf{B}_{2}}\left(E_{1}, E_{2}\right)=-0.2303, \operatorname{COR}_{\mathbf{B}_{3}}\left(E_{1}, E_{2}\right)=0.9978$, and they account for the increasing difference between the eigenvalues of each covariance matrix. In fact, $\Sigma_{3}$ is nearly singular because of the strong linear relationship between $e_{1}$ and $e_{2}$, and it is therefore very close to one of the axes delimiting the first quadrant.

![img-0.jpeg](img-0.jpeg)

Figure 1: The covariance matrices $\Sigma_{1}, \Sigma_{2}$ and $\Sigma_{3}$ from Example 3.1 represented as functions of their eigenvalues in the convex set $\mathcal{L}$. The points $(0,0)$ and $\left(\frac{1}{4}, \frac{1}{4}\right)$ correspond to the minimum entropy and maximum entropy cases.

If we denote with $E_{00}=\{\varnothing\}, E_{01}=\left\{e_{2}\right\}, E_{10}=\left\{e_{1}\right\}$, and $E_{11}=\left\{e_{1}, e_{2}\right\}$ all possible edge sets and with $p_{00}, p_{01}, p_{10}$ and $p_{11}$ the associated probabilities, for $\mathbf{B}_{1}$ we have

$$
p_{00}=0.2, \quad p_{01}=0.2, \quad p_{10}=0.2 \quad \text { and } \quad p_{11}=0.4
$$

This is indeed close to a uniform distribution. The probability of both $e_{1}$ and $e_{2}$ is 0.6 and the variance is 0.24 , which are again similar to the reference values for the maximum entropy case. On the other hand, for $\mathbf{B}_{2}$ we have

$$
p_{00}=0, \quad p_{01}=0.12, \quad p_{10}=0.28 \quad \text { and } \quad p_{11}=0.6
$$

These probabilities are markedly different from a uniform distribution; the probabilities of $e_{1}$ and $e_{2}$ are respectively 0.88 and 0.72 . Considering also the correlation between $e_{1}$ and $e_{2}$, it is intuitively clear why $\Sigma_{2}$ is not as close as $\Sigma_{1}$ to $\left(\frac{1}{4}, \frac{1}{4}\right)$. This is also true for $\mathbf{B}_{3}$, which has the same marginal distributions as $\mathbf{B}_{2}$ but with a much stronger correlation.

# 3.2 Directed acyclic graphs 

The behaviour of the multivariate Trinomial distribution in the minimum and intermediate entropy cases is similar to the one of the multivariate Bernoulli in many respects, but presents profound differences in the maximum entropy case. The reason for these differences is that the structure of a Bayesian network is assumed to be acyclic. Therefore, the state of each arc (i.e. whether it is present in the DAG and its direction) is influenced by the state of all other possible arcs even in the maximum entropy case, when otherwise they would be independent. Furthermore, the acyclicity constraint cannot be written in closed form, making the derivation of exact results on the moments of the distribution of $\mathcal{E}$ particularly difficult.

To obtain some simple expressions for the expected value and the covariance matrix, we will first prove a simple theorem on DAGs, which essentially states that if we reverse the direction of every arc the resulting graph is still a DAG.
Theorem 3.1. Let $G=(\mathbf{V}, A)$ be a $D A G$, and let $G^{*}=\left(\mathbf{V}, A^{*}\right)$ be another directed graph such that

$$
\overline{a_{i j}} \in A^{*} \Longleftrightarrow \overline{b_{i j}} \in A \quad \text { and } \quad \overline{b_{i j}} \in A^{*} \Longleftrightarrow \overline{a_{i j}} \in A
$$

for every $a_{i j} \in A$. Then $G^{*}$ is also acyclic.
Proof. See Appendix 5.
An immediate consequence of this theorem is that for every DAG including the arc $\overline{a_{i j}}$ there exists another DAG including the arc $\overline{b_{i j}}$. Since all DAGs have the same probability in the maximum entropy case, this implies that both directions of every arc have the same probability,

$$
\overline{p_{i j}}=\overline{p_{i j}} \quad \text { for every possible } a_{i j}, i \neq j
$$

Then the expected value of each marginal Trinomial distribution is equal to

$$
\mathrm{E}\left(A_{i j}\right)=\overline{p_{i j}}-\overline{p_{i j}}=0
$$

and its variance is equal to

$$
\operatorname{VAR}\left(A_{i j}\right)=\overline{p_{i j}}^{*}+\overline{p_{i j}}-\left(\overline{p_{i j}}^{*}-\overline{p_{i j}}\right)^{2}=2 \overline{p_{i j}}
$$

The joint probabilities associated with each pair of arcs are also symmetric in the maximum entropy case, again due to Theorem 3.1. Denote with $\overline{a_{i j}}$ the event that $\operatorname{arc} a_{i j}$ is not present in the DAG. If we consider that both directions of every arc have the same probability and that there is no explicit ordering among the arcs, we have

$$
\begin{gathered}
\mathrm{P}\left(\overline{a_{i j}}, \overline{a_{k l}}\right)=\mathrm{P}\left(\overline{b_{i j}}, \overline{b_{k l}}\right), \quad \mathrm{P}\left(\overline{a_{i j}}, \overline{b_{k l}}\right)=\mathrm{P}\left(\overline{b_{i j}}, \overline{a_{k l}}\right) \\
\mathrm{P}\left(\overline{a_{i j}}, \overline{a_{k l}}\right)=\mathrm{P}\left(\overline{a_{i j}}, \overline{a_{k l}}\right)=\mathrm{P}\left(\overline{a_{i j}}, \overline{b_{k l}}\right)=\mathrm{P}\left(\overline{b_{i j}}, \overline{a_{k l}}\right)
\end{gathered}
$$

Then the expression for the covariance simplifies to

$$
\operatorname{COV}\left(A_{i j}, A_{k l}\right)=2\left[\mathrm{P}\left(\overline{a_{i j}}, \overline{a_{k l}}\right)-\mathrm{P}\left(\overline{a_{i j}}, \overline{b_{k l}}\right)\right]
$$

which can be interpreted as the difference in probability between a serial connection (i.e. $v_{i} \rightarrow v_{j} \rightarrow v_{l}$, if $j=k$ ) and a converging connection (i.e. $v_{i} \rightarrow v_{j} \leftarrow v_{l}$ ) if the arcs are incident on a common node (Jensen and Nielsen 2007). This is interesting because v-structures are invariant within equivalence classes, while other patterns of arcs are not (Chickering 1995); indeed, equivalence classes are usually represented as partially directed acyclic graphs (PDAGs) in which only arcs belonging to v-structures are directed. All other arcs, with the exclusion of those which could introduce additional vstructures (known as compelled arcs), are replaced with the corresponding (undirected)

![img-1.jpeg](img-1.jpeg)

Figure 2: Exact (dashed line) and approximate (solid line) probabilities of an arc being present in a DAG with $3,4,5,6$, and 7 nodes.
edges. Therefore, the combination of high values of $\left|\operatorname{COV}\left(A_{i j}, A_{k l}\right)\right|$ and $p_{i j}^{\prime}$ is indicative of the belief that the corresponding arcs are directed in the PDAG identified by the equivalence class. Along with with $\operatorname{VAR}\left(A_{i j}\right)$ and $\operatorname{VAR}\left(A_{k l}\right)$, it is also indicative of the stability of the graph structure, both in the arcs and their directions. In an uninformative prior, such as the distribution we are now considering in the maximum entropy case, we expect all covariances to be small; we will show this is the case in Theorem 3.4. On the other hand, in an informative distribution such as the ones considered in the intermediate entropy case, we expect covariances to be closer to their upper bounds for arcs that are compelled or part of a converging connection, and closer to zero for arcs whose direction is not determined in the equivalence class. Note that the sign of $\operatorname{COV}\left(A_{i j}, A_{k l}\right)$ depends on the way the two possible directions of each arc are associated with 1 and -1 ; a simple way to obtain a consistent parameterisation is to follow the natural ordering of the variables (i.e. if $i \leqslant j$ then the arc incident on these nodes is taken to be $A_{i j}, \overline{a_{i j}}$ is associated with 1 and $\overline{\Lambda_{i j}}$ with -1 ).

The equalities in Equations 7 and 8 drastically reduce the number of free parameters in the maximum entropy case. The marginal distribution of each arc now depends only on $\bar{p}_{i j}^{\prime \star}$, whose value can be derived from the following numerical approximation by Melançon et al. (2000).
Theorem 3.2. The average number of arcs in a $D A G$ with $n$ nodes is approximately $\frac{1}{4} n^{2}$ in the maximum entropy case.

Proof. See Melançon et al. (2000).

Theorem 3.3. Let $G=(\mathbf{V}, A)$ be a $D A G$ with $n$ nodes. Then for each possible arc

![img-2.jpeg](img-2.jpeg)

Figure 3: Estimated (dashed line) and approximate (solid line) probabilities of an arc being present in a DAG with 8 to 50 nodes. The dotted line represents the limiting value in the number of nodes.
$a_{i j}, i \neq j$ we have that in the maximum entropy case

$$
\overrightarrow{p_{i j}}=\overrightarrow{p_{i j}} \simeq \frac{1}{4}+\frac{1}{4(n-1)} \quad \text { and } \quad \overrightarrow{p_{i j}} \simeq \frac{1}{2}-\frac{1}{2(n-1)}
$$

Proof. See Appendix 5.

The quality of this approximation is examined in Figure 2 and Figure 3. In Figure 2, the values provided by Theorem 3.3 for DAGs with $3,4,5,6$ and 7 nodes are compared to the corresponding true values. The latter have been computed by enumerating all possible DAGs of that size (i.e. the whole population) and computing the relative frequency of each possible arc. In Figure 3, the values provided by Theorem 3.3 for DAGs with 8 to 50 nodes are compared with the corresponding estimated values computed over a set of $10^{9}$ DAGs of the same size. The latter have been generated with uniform probability using the algorithm from Melançon and Fabrice (2004) as implemented in the bnlearn package (Scutari 2010, 2012) for R (R Development Core Team 2012).

We can clearly see that the approximate values are close to the corresponding true (in Figure 2) or estimated (in Figure 3) values for DAGs with at least 6 nodes. This is not a significant limitation; the true values can be easily computed via exhaustive enumeration for DAGs with 3, 4 and 5 nodes (they are reported in Appendix 5, along with other relevant quantities). Furthermore, it is evident both from Theorem 3.3 and from Figures 2 and 3 that, as the number of nodes diverges,

$$
\lim _{n \rightarrow \infty} \overrightarrow{p_{i j}}=\lim _{n \rightarrow \infty} \overrightarrow{p_{i j}}=\frac{1}{4} \quad \text { and } \quad \lim _{n \rightarrow \infty} \overrightarrow{p_{i j}}=\frac{1}{2}
$$

If we take the absolute value of this asymptotic Trinomial distribution, the resulting random variable is $\operatorname{Ber}\left(p_{i j}\right)$ with $p_{i j}=\frac{1}{2}$, which is the marginal distribution of an edge in an UG in the maximum entropy case. The absolute value transformation can be interpreted as ignoring the direction of the arc; the events $\widehat{\alpha}_{i j}^{-} \in A$ and $\widehat{a}_{i j}^{-*} \in A$ collapse into $e_{i j} \in E$, while $\widehat{\alpha}_{i j}^{-}, \widehat{a}_{i j}^{-} \notin A$ maps to $e_{i j} \notin E$. As a result, the marginal distribution of an arc is remarkably similar to the one of the corresponding edge in an undirected graph for sufficiently large DAGs; in both cases, the nodes $v_{i}$ and $v_{j}$ are linked with probability $\frac{1}{2}$.
No result similar to Theorem 3.2 has been proved for arbitrary pairs of arcs in a directed acyclic graph; therefore, the structure of the covariance matrix $\Sigma$ can be derived only in part. Variances can be approximated using the approximate probabilities from Theorem 3.3:

$$
\operatorname{VAR}\left(A_{i j}\right)=2 \widehat{p_{i j}^{-}} \simeq \frac{1}{2}+\frac{1}{2(n-1)} \rightarrow \frac{1}{2} \text { as } n \rightarrow \infty
$$

Therefore, maximum variance (of each arc) and maximum entropy (of the graph structure) are distinct, as opposed to what happens in UGs. However, we can use the decomposition of the variance introduced in Equation 6 to motivate why the maximum entropy case is still a "worst case" outcome for $\mathrm{P}(\mathcal{G}(\mathcal{E}) \mid \mathcal{D})$. As we can see from Figure 4 , the contributions of the presence of an arc (given by the transformation $\left|A_{i j}\right|$ ) and its direction (given by the $4 \widehat{p}_{i j}^{-} \widehat{p}_{i j}^{-}=4 \widehat{p}_{i j}^{2}$ term) to the variance are asymptotically equal. This is a consequence of the limits in Equation 9, which imply that an arc (modulo its direction) has the same probability to be present in or absent from the DAG and that its directions also have the same probability. As a result, we are not able to make any decision about either the presence of the arc or its direction. On the contrary, when $\operatorname{VAR}\left(A_{i j}\right)$ reaches it maximum at 1 we have that $\mathrm{P}\left(\left\{\widehat{a_{i j}^{-}}, \widehat{\alpha_{i j}^{-}}\right\}\right)=1$ and $\mathrm{P}\left(\widehat{a_{i j}}\right)=0$, so we are sure that the arc will be present in the DAG in one of its two possible directions.

As for the covariances, it is possible to obtain tight bounds using Hoeffding's identity (Hoeffding 1940; Fisher and Sen 1994),

$$
\operatorname{COV}(X, Y)=\iint_{\mathbb{R}^{4}} F_{X, Y}(x, y)-F_{X}(x) F_{Y}(y) d x d y
$$

and the decomposition of the joint distribution of dependent random variables provided by the Farlie-Morgenstern-Gumbel (FMG) family of distributions (Mari and Kotz 2001), which has the form

$$
F_{X, Y}(x, y)=F_{X}(x) F_{Y}(y)\left[1+\varepsilon\left(1-F_{X}(x)\right)\left(1-F_{Y}(y)\right)\right], \quad|\varepsilon| \leqslant 1
$$

In Equations 11 and 12, $F_{X, Y}, F_{X}$ and $F_{Y}$ denote the cumulative distribution functions of the joint and marginal distributions of $X$ and $Y$, respectively.
Theorem 3.4. Let $G=(V, A)$ be a $D A G$, and let $a_{i j}, i \neq j$ and $a_{k l}, k \neq l$ be two possible arcs. Then in the maximum entropy case we have that

$$
\left|\operatorname{COV}\left(A_{i j}, A_{k l}\right)\right| \lessgtr 4\left[\frac{3}{4}-\frac{1}{4(n-1)}\right]^{2}\left[\frac{1}{4}+\frac{1}{4(n-1)}\right]^{2}
$$

![img-3.jpeg](img-3.jpeg)

Figure 4: Decomposition of the asymptotic variance of an arc in the part that depends only on its presence (dashed line) and the part that depends only on its direction (solid line). The dots correspond to the respective values in the maximum entropy case.
![img-4.jpeg](img-4.jpeg)

Figure 5: Bounds for the absolute value of the covariance and the correlation coefficient of two arcs in a DAG with 6 to 50 nodes. The dotted lines represent the respective limiting values.

![img-5.jpeg](img-5.jpeg)

Figure 6: Approximate values for $\mathrm{P}\left(\overline{a_{i j}}, \overline{a_{k l}}\right)$ (solid line) and $\mathrm{P}\left(\overline{a_{i j}}, \overline{b_{k l}}\right)$ (dashed line) for DAGs with 8 to 50 nodes. The dotted line represents their asymptotic value.
and

$$
\left|\operatorname{COR}\left(A_{i j}, A_{k l}\right)\right| \lessgtr 2\left[\frac{3}{4}-\frac{1}{4(n-1)}\right]^{2}\left[\frac{1}{4}+\frac{1}{4(n-1)}\right]
$$

Proof. See Appendix 5.

The bounds obtained from this theorem appear to be tight in the light of the true values for the covariance and correlation coefficients (computed again by enumerating all possible DAGs of size 3 to 7). Figure 5 shows that the bounds for DAGs with 6 to 50 nodes; for DAGs with 3,4 and 5 nodes the approximation of $\overline{p_{i j}}$ the bounds are based on is loose, and the true values of covariance and correlation are known. Non-null covariances range from $\pm 0.08$ (for DAGs with 3 nodes) to $\pm 0.08410$ (for DAGs with 7 nodes), while non-null correlation coefficients vary from $\pm 0.125$ (for DAGs with 3 nodes) to $\pm 0.1423$ (for DAGs with 7 nodes). Both covariance and correlation appear to be strictly increasing in modulus as the number of nodes increases, and converge to the limiting values of the bounds ( 0.140625 and 0.28125 , respectively) from below.

Some other interesting properties are apparent from the true values of the covariance coefficients reported in Appendix 5. They are reported below as conjectures because, while they describe a systematic behaviour that emerges from the DAGs whose sizes we have a complete enumeration for, we were not able to substantiate them with formal proofs.
Conjecture 3.1. Arcs that are not incident on a common node are uncorrelated.
This is a consequence of the fact that if we consider $A_{i j}$ and $A_{k l}$ with $i \neq j \neq k \neq l$, we have $\mathrm{P}\left(\overline{a_{i j}}, \overline{a_{k l}}\right)=\mathrm{P}\left(\overline{a_{i j}}, \overline{b_{k l}}\right)$. Therefore $\operatorname{COV}\left(A_{i j}, A_{k l}\right)=0$. This property seems to generalise to DAGs with more than 7 nodes. Figure 6 shows approximate estimates for

$\mathrm{P}\left(\overrightarrow{a_{i j}}, \overrightarrow{a_{k l}}\right)$ and $\mathrm{P}\left(\overrightarrow{a_{i j}}, \overleftarrow{\delta_{k l}}\right)$ for DAGs with 8 to 50 nodes, obtained again from $10^{9}$ DAGs generated with uniform probability. The curves for the two probabilities are overlapping and very close to each other for all the considered DAG sizes, thus supporting Conjecture 3.1.

Conjecture 3.2. The covariance matrix $\Sigma$ is sparse.
The proportion of arcs incident on a common node converges to zero as the number of nodes increases; therefore, if we assume Conjecture 3.1 is true, the proportion of elements of $\Sigma$ that are equal to 0 has limit

$$
1 \geqslant \lim _{n \rightarrow \infty} \frac{\binom{n}{2}\binom{n-2}{2}}{\binom{n}{2}\binom{n}{2}-\binom{n}{2}} \geqslant \lim _{n \rightarrow \infty} \frac{(n-2)(n-3)}{n(n-1)}=1
$$

Furthermore, even arcs that are incident on a common node are not strongly correlated. Conjecture 3.3. Both covariance and correlation between two arcs incident on a common node are monotonically increasing in modulus.
Conjecture 3.4. The covariance between two arcs incident on a common node takes values in the interval $[0.08,0.140625]$ in modulus, while the correlation takes values in $[0.125,0.28125]$ in modulus.

These intervals can be further reduced to $[0.08410,0.140625]$ and $[0.1423,0.28125]$ for DAGs larger than 7 nodes due to Conjecture 3.3.

As far as the other two cases are concerned, in the minimum entropy case we have that

$$
\mathrm{E}\left(A_{i j}\right)=\left\{\begin{array}{lll}
-1 & \text { if } \delta_{i j}^{-} \in A \\
0 & \text { if } \delta_{i j}^{-}, \overrightarrow{a_{i j}} \notin A \\
1 & \text { if } \overrightarrow{a_{i j}} \in A
\end{array} \quad\right. \text { and } \quad \Sigma=\mathbf{O}
$$

as in the minimum entropy case of UGs. The intermediate entropy case again ranges from being very close to the minimum entropy case (when the graph structure displays little variability) to being very close to the maximum entropy case (when the graph structure displays substantial variability). The bounds on the eigenvalues of $\Sigma$ derived in Lemma 2.2 allow a graphical representation of the variability of the network structure, equivalent to the one illustrated in Example 3.1 for UGs.

# 4 Measures of variability 

Several functions have been proposed in literature as univariate measures of spread of a multivariate distribution, usually under the assumption of multivariate normality; for some examples see Mardia et al. (1979) and Bilodeau and Brenner (1999). Three of them in particular can be used as descriptive statistics for the multivariate Bernoulli and Trinomial distributions: the generalised variance,

$$
\operatorname{VAR}_{G}(\Sigma)=\operatorname{det}(\Sigma)
$$

the total variance,

$$
\operatorname{VAR}_{T}(\Sigma)=\operatorname{tr}(\Sigma)
$$

and the squared Frobenius matrix norm of the difference between $\Sigma$ and a target matrix $\Psi$,

$$
\operatorname{VAR}_{F}(\Sigma, \Psi)=\left\||\Sigma-\Psi|\right\|_{F}^{2}
$$

Both generalised variance and total variance associate high values of the statistic to unstable network structures, and are bounded due to the properties of the multivariate Bernoulli and Trinomial distributions. For total variance, it is easy to show that either $\operatorname{VAR}_{T}(\Sigma) \in\left[0, \frac{k}{4}\right]$ (for the multivariate Bernoulli) or $\operatorname{VAR}_{T}(\Sigma) \in[0, k]$ (for the multivariate Trinomial), due to the bounds on the variances $\sigma_{i i}$ and on the eigenvalues $\lambda_{i}$ derived in Sections 2.1 and 2.2. Generalised variance is similarly bounded due to Hadamard's theorem on the determinant of a non-negative definite matrix (Seber 2008): $\operatorname{VAR}_{G}(\Sigma) \in\left[0,\left(\frac{1}{4}\right)^{k}\right]$ for the multivariate Bernoulli distribution and $\operatorname{VAR}_{G}(\Sigma) \in[0,1]$ for the multivariate Trinomial. They reach the respective maxima in the maximum entropy case and are equal to zero only in the minimum entropy case. Generalised variance is also strictly convex, but it is equal to zero when $\Sigma$ is rank deficient. For this reason it may be convenient to reduce $\Sigma$ to a smaller, full rank matrix (say $\Sigma^{*}$ ) and consider $\operatorname{VAR}_{G}\left(\Sigma^{*}\right)$ instead of $\operatorname{VAR}_{G}(\Sigma)$; using a regularised estimator for $\Sigma$ such as the one presented in Ledoit and Wolf (2003) is also a viable option.
The behaviour of the squared Frobenius matrix norm, on the other hand, depends on the choice of the target matrix $\Psi$. For $\Psi=\mathbf{O}$ (the covariance matrix arising from the minimum entropy case for both the multivariate Bernoulli and the multivariate Trinomial), $\operatorname{VAR}_{F}(\Sigma, \Psi)$ associates high values of the statistic to unstable network structures, like $\operatorname{VAR}_{T}(\Sigma)$ and $\operatorname{VAR}_{G}(\Sigma)$; however, $\operatorname{VAR}_{F}(\Sigma, \mathbf{O})$ does not have a unique maximum and none of its maxima correspond to the maximum entropy case, making its interpretation unclear. A better choice seems to be a multiple of the covariance matrix arising from the maximum entropy case, say $\Psi=k \Sigma_{\max }$, associating high values of $\operatorname{VAR}_{F}\left(\Sigma, k \Sigma_{\max }\right)$ to stable network structures. For the multivariate Bernoulli, if we let $\Psi=\frac{k}{4} I_{k}, \operatorname{VAR}_{F}\left(\Sigma, \frac{k}{4} I_{k}\right)$ can be rewritten as

$$
\operatorname{VAR}_{F}\left(\Sigma, \frac{k}{4} I_{k}\right)=\sum_{i=1}^{k}\left(\lambda_{i}-\frac{k}{4}\right)^{2}
$$

It has both a unique global minimum (because it is a convex function),

$$
\min _{\mathcal{L}} \operatorname{VAR}_{F}\left(\Sigma, \frac{k}{4} I_{k}\right)=\operatorname{VAR}_{F}\left(\frac{1}{4} I_{k}\right)=\sum_{i=1}^{k}\left(\frac{1}{4}-\frac{k}{4}\right)^{2}=\frac{k(k-1)^{2}}{16}
$$

and a unique global maximum,

$$
\max _{\mathcal{L}} \operatorname{VAR}_{F}\left(\Sigma, \frac{k}{4} I_{k}\right)=\operatorname{VAR}_{F}(\mathbf{O})=\sum_{i=1}^{k}\left(\frac{k}{4}\right)^{2}=\frac{k^{3}}{16}
$$

which correspond to the maximum and minimum entropy covariance matrices, respectively. Similar results can be derived for the multivariate Trinomial distribution, using an approximate estimate for $\Sigma_{\max }$ based on the results presented in Section 3.2.

All the descriptive statistics introduced in this section can be normalised as follows:

$$
\begin{array}{r}
\widehat{\operatorname{VAR}}_{T}(\Sigma)=\frac{\operatorname{VAR}_{T}(\Sigma)}{\max _{\Sigma} \operatorname{VAR}_{T}(\Sigma)}, \quad \widehat{\operatorname{VAR}}_{G}(\Sigma)=\frac{\operatorname{VAR}_{G}(\Sigma)}{\max _{\Sigma} \operatorname{VAR}_{G}(\Sigma)} \\
\widehat{\operatorname{VAR}}_{F}\left(\Sigma, k \Sigma_{\max }\right)=\frac{\max _{\Sigma} \operatorname{VAR}_{F}\left(\Sigma, k \Sigma_{\max }\right)-\operatorname{VAR}_{F}\left(\Sigma, k \Sigma_{\max }\right)}{\max _{\Sigma} \operatorname{VAR}_{F}\left(\Sigma, k \Sigma_{\max }\right)-\min _{\Sigma} \operatorname{VAR}_{F}\left(\Sigma, k \Sigma_{\max }\right)}
\end{array}
$$

These normalised statistics vary in the $[0,1]$ interval and associate high values to graphs whose structures display a high variability. Since they vary on a known and bounded scale, they are easy to interpret as absolute quantities (i.e. goodness-of-fit statistics) as well as relative ones (i.e. proportions of total possible variability).

They also have a clear geometric interpretation as distances in $\mathcal{L}$, as they can all be rewritten as functions of the eigenvalues $\lambda_{1}, \ldots, \lambda_{k}$. This allows, in turn, to provide an easy interpretation of otherwise complex properties of $\mathrm{P}(\mathcal{G}(\mathcal{E}))$ and $\mathrm{P}(\mathcal{G}(\mathcal{E}) \mid \mathcal{D})$ and to derive new results. First of all, the measures introduced in Equation 16 can be used to select the best learning algorithm $\mathcal{A}$ in terms of structure stability for a given data set $\mathcal{D}$. Different algorithms make use of the information present in the data in different ways, under different sets of assumptions and with varying degrees of robustness. Therefore, in practice different algorithms learn different structures from the same data and, in turn, result in different posterior distributions on G. If we rewrite Equation 1 to make this dependence explicit,

$$
\mathrm{P}(\mathcal{G}(\mathcal{E}) \mid \mathcal{D}, \mathcal{A}) \propto \mathrm{P}(\mathcal{G}(\mathcal{E})) \mathrm{P}(\mathcal{D} \mid \mathcal{G}(\mathcal{E}), \mathcal{A})
$$

and denote with $\Sigma_{\mathcal{A}}$ the covariance matrix of the distribution of the edges (or the arcs) induced by $\mathrm{P}(\mathcal{G}(\mathcal{E}) \mid \mathcal{D}, \mathcal{A})$, then we can choose the optimal structure learning algorithm $\mathcal{A}^{*}$ as

$$
\mathcal{A}^{*}=\underset{\mathcal{A}}{\operatorname{argmin}} \widehat{\operatorname{VAR}}_{T}\left(\Sigma_{\mathcal{A}}\right)
$$

or, equivalently, using $\widehat{\operatorname{VAR}}_{G}\left(\Sigma_{\mathcal{A}}\right)$ or $\widehat{\operatorname{VAR}}_{F}\left(\Sigma_{\mathcal{A}}, k \Sigma_{\max }\right)$ instead of $\widehat{\operatorname{VAR}}_{T}\left(\Sigma_{\mathcal{A}}\right)$. Such an algorithm has the desirable property of maximising the information gain from the data, as measured by the distance from the non-informative prior $\mathrm{P}(\mathcal{G}(\mathcal{E}))$ in $\mathcal{L}$. In other words, $\mathcal{A}^{*}$ is the algorithm that uses the data in the most efficient way. Furthermore, an optimal $\mathcal{A}^{*}$ can be identified even for data sets without a "golden standard" graph structure to use for comparison; this is not possible with the approaches commonly used in the literature, which rely on variations of the Hamming distance (Jungnickel 2008) and knowledge of such a "golden standard" to evaluate learning algorithms (see, for example Tsamardinos et al. 2006).

Similarly, it is possible to study the influence of different values of a tuning parameter for a given structure learning algorithm (and again a given data set). Such parameters include, for example, restrictions on the degrees of the nodes (Friedman et al. 1999b) and regularisation coefficients (Koller and Friedman 2009). If we denote these tuning parameters with $\tau$, we can again choose an optimal $\tau^{*}$ as

$$
\tau^{*}=\underset{\tau}{\operatorname{argmin}} \widehat{\operatorname{VAR}}_{T}\left(\Sigma_{\mathcal{A}(\tau)}\right)
$$

Another natural application of the variability measures presented in Equation 16 is the study of the consistency of structure learning algorithms. It has been proved in the literature that most structure learning algorithms are increasingly able to identify a single, minimal graph structure as the sample size diverges (see, for example Chickering 2002). Therefore, $\mathrm{P}(\mathcal{G}(\mathcal{E}) \mid \mathcal{D})$ converges towards the minimum entropy case and all variability measures converge to zero. However, convergence speed has never been analysed and compared across different learning algorithms; any one of $\overline{\mathrm{VAR}}_{T}\left(\Sigma_{\mathcal{A}}\right)$, $\overline{\mathrm{VAR}}_{G}\left(\Sigma_{\mathcal{A}}\right)$ or $\overline{\mathrm{VAR}}_{F}\left(\Sigma_{\mathcal{A}}, k \Sigma_{\max }\right)$ provides a coherent way to perform such an analysis.

Lastly, we may use the variability measures from Equation 16 as a basis to investigate different prior distributions for real-world data modelling and to define new ones. Relatively little attention has been paid in the literature to the choice of the prior over G, and the uniform maximum entropy distribution is usually chosen for computational reasons. Its only parameter is the imaginary sample size, which expresses the weight assigned to the prior distribution as the size of an imaginary sample size supporting it (Heckerman et al. 1995).

However, choosing a uniform prior also has some drawbacks. Firstly, Steck and Jaakkola (2002) and Steck (2008) have shown that both large and small values of the imaginary sample size have counter-intuitive effects on the sparsity of a Bayesian network even for large sample sizes. For instance, large values of the imaginary sample size may favour the presence of an arc over its absence even when both $\mathrm{P}(\mathcal{G}(\mathcal{E}))$ and $\mathcal{D}$ imply the variables the arc is incident on are conditionally independent. Secondly, a uniform prior assigns a non-null probability to all possible models. Therefore, it often results in a very flat posterior which is not able to discriminate between networks that are well supported by the data and networks that are not (Koller and Friedman 2009).

Following Pearl (1988)'s suggestion that "good" graphical models should be sparse, sparsity-inducing priors such as the ones in Buntine (1991) and Friedman and Koller (2003) should be preferred to the maximum entropy distribution, as should informative priors (Mukherjee and Speed 2008). For example, the prior proposed in Buntine (1991) introduces a prior probability $\beta$ to include (independently) each arc in a Bayesian network with a given topological ordering, which means $\overline{p_{i j}}=\beta$ and $\overline{p_{i j}}=0$ for all $i<j$ in $\mathrm{P}(\mathcal{G}(\mathcal{E}))$. Thus, $\operatorname{VAR}\left(A_{i j}\right)=\beta-\beta^{2}, \operatorname{VAR}_{T}(\Sigma)=k\left(\beta-\beta^{2}\right)$ and $\operatorname{VAR}_{G}(\Sigma)=\left(\beta-\beta^{2}\right)^{k}$. The prior proposed in Friedman et al. (1999a), on the other hand, controls the number of parents of each node for a given topological ordering. Therefore, it favours low values of $\mathrm{P}\left(\bar{a}_{i j}^{*}, \bar{b}_{j k}^{-}\right)$in $\mathrm{P}(\mathcal{G}(\mathcal{E}))$ and again $\overline{p_{i j}}=0$ for all $i<j$. Clearly, the amount of sparsity induced by the hyperparameters of these priors determines the variability of both the prior and the posterior, and can be controlled through the variability measures from Equation 16 .

Furthermore, these measures can provide inspiration in devising new priors with the desired form and amount of sparsity. For instance, first order moments can be used to model prior knowledge on specific arcs or edges, and second order moments can be used to control their interplay. In the case of Bayesian networks, it may also be of interest to define a prior distribution assigning the same probability to equivalent models. Clearly, first and second order moments are insufficient for this task unless

all the higher order moments of $\mathrm{P}(\mathcal{G}(\mathcal{E}))$ are completely determined by $\mathrm{P}\left(A_{i j}\right)$ and $\mathrm{P}\left(A_{i j}, A_{k l}\right)$. If such an assumption holds, at least approximately, then assigning equal probabilities to equivalent models entails $\overline{p_{i j}}^{*}=\overline{p_{i j}}$ for all the arcs that are undirected in the PDAG of the equivalence class. Implementing this condition is problematic for two reasons. First, $\mathrm{P}\left(A_{i j}, A_{k l}\right)$ needs to be specified conditional on the PDAG as well, as it must be consistent with $\mathrm{P}\left(A_{i j}\right)$; and the correct way to do that is not as intuitively clear as in the case of $\mathrm{P}\left(A_{i j}\right)$. Furthermore, identifying which arcs belong to a v-structure has a computational complexity of $\mathcal{O}\left(|A|^{3}\right)$, as it requires checking every triplet of arcs $\left\{a_{i j}, a_{j k}, a_{i k}\right\}$. In the case of dense graphs, $\mathcal{O}\left(|A|^{3}\right) \rightarrow \mathcal{O}\left(|\mathbf{V}|^{6}\right)$, and even for sparse graphs $\mathcal{O}\left(|A|^{3}\right) \simeq \mathcal{O}\left(|\mathbf{V}|^{3}\right)$. While better than the super-exponential complexity of dealing with the full parameterisation of $\mathrm{P}(\mathcal{G}(\mathcal{E}))$, this is a serious limitation in high dimensional settings.

# 5 Conclusions 

Bayesian inference on the structure of graphical models is challenging in most situations due to the difficulties in defining and analysing prior and posterior distributions over the spaces of undirected or directed acyclic graphs. The dimension of these spaces grows super-exponentially in the number of variables considered in the model, making even MAP analyses problematic.

In this paper, we propose an alternative approach to the analysis of graph structures which focuses on the set of possible edges $\mathcal{E}$ of a graphical model $\mathcal{M}=(\mathcal{G}(\mathcal{E}), \Theta)$ instead of the possible graph structures themselves. The latter are uniquely identified by the respective edge sets; therefore, the proposed approach integrates smoothly with and extends both frequentist and Bayesian results present in the literature. Furthermore, this change in focus provides additional insights on the behaviour of individual edges (which are usually the focus of inference) and reduces the dimension of the sample space from super-exponential to quadratic in the number of variables.

For many inference problems the parameter space is reduced as well, and makes complex inferential tasks feasible. As an example, we characterise several measures of structural variability for both Bayesian and Markov networks using the second order moments of $\mathrm{P}(\mathcal{G}(\mathcal{E}))$ and $\mathrm{P}(\mathcal{G}(\mathcal{E}) \mid \mathcal{D})$. These measures have several possible applications and are easy to interpret from both an algebraic and a geometric point of view.

## Acknowledgments

The author would like to thank to Adriana Brogini (University of Padova) and David Balding (University College London) for proofreading this article and providing many useful comments and suggestions. Furthermore, the author would also like to thank Giovanni Andreatta and Luigi Salce (University of Padova) for their assistance in the development of the material.

# Appendix I: Proofs 

Proof of Lemma 2.1. Since $\Sigma$ is a real, symmetric, non-negative definite matrix, its eigenvalues $\lambda_{i}$ are non-negative real numbers; this proves the lower bound in both inequalities.

The upper bound in the first inequality holds because

$$
\sum_{i=1}^{k} \lambda_{i}=\sum_{i=1}^{k} \sigma_{i i} \leqslant \max _{\left\{\sigma_{i i}\right\}} \sum_{i=1}^{k} \sigma_{i i}=\sum_{i=1}^{k} \max \sigma_{i i}=\frac{k}{4}
$$

as the sum of the eigenvalues is equal to the trace of $\Sigma$. This in turn implies

$$
\lambda_{i} \leqslant \sum_{i=1}^{k} \lambda_{i} \leqslant \frac{k}{4}
$$

which completes the proof.

Proof of Theorem 2.2. It is easy to show that each $\left|T_{i}\right|=B_{i}$, with $p_{i(1)}+p_{i(-1)}=p_{i}^{*}$ and $p_{i(0)}=1-p_{i}^{*}$. It follows that the parameter collection $\mathbf{p}$ of $\mathbf{T}$ reduces to

$$
\begin{aligned}
\mathbf{p}^{*} & =\left\{p_{I(T)}: I \subseteq\{1, \ldots, k\}, T \in\{0,1\}^{[I]}, I \neq \varnothing\right\} \\
& =\left\{p_{I}: I \subseteq\{1, \ldots, k\}, I \neq \varnothing\right\}
\end{aligned}
$$

after the transformation. Therefore, $|\mathbf{T}| \sim \operatorname{Ber}_{k}\left(\mathbf{p}^{*}\right)$ is a uniquely identified multivariate Bernoulli random variable according to the definition introduced at the beginning of Section 2.1.

Proof of Theorem 3.1. Let's assume by contradiction that $G^{*}$ is cyclic; this implies that there are one or more nodes $v_{i} \in \mathbf{V}$ such that

$$
v_{i} \xrightarrow{\overrightarrow{a_{i j}}} v_{j} \rightarrow \ldots \rightarrow v_{k} \xrightarrow{\overrightarrow{a_{k i}}} v_{i}
$$

for some $v_{j}, v_{k} \in \mathbf{V}$. However, this would mean that in $G$ we would have

$$
v_{i} \xrightarrow{\overleftarrow{a_{k i}}} v_{k} \rightarrow \ldots \rightarrow v_{j} \xrightarrow{\overleftarrow{h_{i j}}} v_{i}
$$

which is not possible since $G$ is assumed to be acyclic.

Proof of Theorem 3.3. Each possible arc can appear in the graph in only one direction at a time, so a directed acyclic graph with $n$ nodes can have at most $\binom{n}{2}=\frac{1}{2} n(n-1)$ arcs. Therefore

$$
\overrightarrow{p_{i j}} \cdot \overleftarrow{p_{i j}} \simeq \frac{\frac{1}{4} n^{2}}{\frac{1}{2} n(n-1)}=\frac{1}{2}+\frac{1}{2(n-1)}
$$

But in the maximum entropy case we also have that $\overrightarrow{p_{i j}}=\overleftarrow{p_{i j}}$, so

$$
\overrightarrow{p_{i j}} \cdot \overleftarrow{p_{i j}} \simeq \frac{1}{4}+\frac{1}{4(n-1)} \quad \text { and } \quad \begin{aligned}
& \quad \overrightarrow{p_{i j}}=1-2 \overrightarrow{p_{i j}} \simeq \frac{1}{2}-\frac{1}{2(n-1)}
\end{aligned}
$$

which completes the proof.

Proof of Theorem 3.4. In the maximum entropy case, all arcs have the same marginal distribution function,

$$
F_{A}\left(a_{i j}\right) \simeq \begin{cases}0 & \text { in }(-\infty,-1] \\ \frac{1}{4}+\frac{1}{4(n-1)} & \text { in }(-1,0] \\ \frac{3}{4}-\frac{1}{4(n-1)} & \text { in }(0,1] \\ 1 & \text { in }(1,+\infty)\end{cases}
$$

so the joint distribution of any pair of arcs $a_{i j}$ and $a_{k l}$ can be written as a member of the Farlie-Morgenstern-Gumbel family of distributions as

$$
F_{A_{i j}, A_{k l}}\left(a_{i j}, a_{k l}\right)=F_{A}\left(a_{i j}\right) F_{A}\left(a_{k l}\right)\left[1+\varepsilon\left(1-F_{A}\left(a_{i j}\right)\right)\left(1-F_{A}\left(a_{k l}\right)\right)\right]
$$

Then if we apply Hoeffding's identity from Equation 11 and replace the joint distribution

function $F_{A_{i j}, A_{k l}}\left(a_{i j}, a_{k l}\right)$ with the right hand of Equation 18 we have that

$$
\begin{aligned}
& \left|\operatorname{COV}\left(A_{i j}, A_{k l}\right)\right|= \\
& =\left|\sum_{a_{i j} \in\{-1,0,1\}} \sum_{a_{k l} \in\{-1,0,1\}} F_{A_{i j}, A_{k l}}\left(a_{i j}, a_{k l}\right)-F_{A}\left(a_{i j}\right) F_{A}\left(a_{k l}\right)\right| \\
& \leqslant \sum_{a_{i j} \in\{-1,0,1\}} \sum_{a_{k l} \in\{-1,0,1\}}\left|F_{A_{i j}, A_{k l}}\left(a_{i j}, a_{k l}\right)-F_{A}\left(a_{i j}\right) F_{A}\left(a_{k l}\right)\right| \\
& =\sum_{a_{i j} \in\{-1,0,1\}} \sum_{a_{k l} \in\{-1,0,1\}}\left|F_{A}\left(a_{i j}\right) F_{A}\left(a_{k l}\right)\right. \\
& \times\left[1+\varepsilon\left(1-F_{A}\left(a_{i j}\right)\right)\left(1-F_{A}\left(a_{k l}\right)\right)\right]-F_{A}\left(a_{i j}\right) F_{A}\left(a_{k l}\right) \mid \\
& =\sum_{\{-1,0\}} \sum_{\{-1,0\}}\left(1-F_{A}\left(a_{i j}\right)\right)\left(1-F_{A}\left(a_{k l}\right)\right)
\end{aligned}
$$

We can now compute the bounds for $\left|\operatorname{COV}\left(a_{i j}, a_{k l}\right)\right|$ and $\left|\operatorname{COR}\left(a_{i j}, a_{k l}\right)\right|$ using only the marginal distribution function $F_{A}$ from Equation 17 and the variance from Equation 10, thus obtaining the expressions in Equation 13 and Equation 14.

# Appendix II: Moments and parameters of the multivariate Trinomial distribution in the maximum entropy case 

Below are reported the exact values of the parameters of the marginal Trinomial distributions and of the first and second order moments of the multivariate Trinomial distribution in the maximum entropy case. All these quantities have been computed by a complete enumeration of the directed acyclic graphs of a given size $(3,4,5,6$ and 7$)$.

### 5.1 Moments for the 3-dimensional distribution

$$
A_{i j}= \begin{cases}-1 & \text { with probability } 0.32 \\ 0 & \text { with probability } 0.36 \\ 1 & \text { with probability } 0.32\end{cases} \quad \mathrm{E}\left(A_{i j}\right)=0
$$

### 5.2 Moments for the 4-dimensional distribution

$$
\begin{aligned}
& A_{i j}= \begin{cases}-1 & \text { with probability } 0.309392 \\
0 & \text { with probability } 0.381215 \\
1 & \text { with probability } 0.309392\end{cases} \quad \mathrm{E}\left(A_{i j}\right)=0 \\
& \left|\operatorname{COV}\left(A_{i j}, A_{k l}\right)\right|= \begin{cases}0 & \text { if } i \neq j \neq k \neq l \\
0.081031 & \text { otherwise }\end{cases}
\end{aligned}
$$

# 5.3 Moments for the 5-dimensional distribution 

$$
\begin{gathered}
A_{i j}=\left\{\begin{array}{ll}
-1 & \text { with probability } 0.301082 \\
0 & \text { with probability } 0.397834 \\
1 & \text { with probability } 0.301082
\end{array} \quad \mathrm{E}\left(A_{i j}\right)=0\right. \\
\left|\operatorname{COV}\left(A_{i j}, A_{k l}\right)\right|=\left\{\begin{array}{ll}
0 & \text { if } i \neq j \neq k \neq l \\
0.081691 & \text { otherwise }
\end{array}\right.
\end{gathered}
$$

### 5.4 Moments for the 6-dimensional distribution

$$
\begin{gathered}
A_{i j}=\left\{\begin{array}{ll}
-1 & \text { with probability } 0.294562 \\
0 & \text { with probability } 0.410875 \\
1 & \text { with probability } 0.294562
\end{array} \quad \mathrm{E}\left(A_{i j}\right)=0\right. \\
\left|\operatorname{COV}\left(A_{i j}, A_{k l}\right)\right|=\left\{\begin{array}{ll}
0 & \text { if } i \neq j \neq k \neq l \\
0.082121 & \text { otherwise }
\end{array}\right.
\end{gathered}
$$

### 5.5 Moments for the 7-dimensional distribution

$$
\begin{gathered}
A_{i j}=\left\{\begin{array}{ll}
-1 & \text { with probability } 0.289390 \\
0 & \text { with probability } 0.421220 \\
1 & \text { with probability } 0.289390
\end{array} \quad \mathrm{E}\left(A_{i j}\right)=0\right. \\
\left|\operatorname{COV}\left(A_{i j}, A_{k l}\right)\right|=\left\{\begin{array}{ll}
0 & \text { if } i \neq j \neq k \neq l \\
0.82410 & \text { otherwise }
\end{array}\right.
\end{gathered}
$$