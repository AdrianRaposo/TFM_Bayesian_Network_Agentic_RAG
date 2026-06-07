# The curved exponential family of a staged tree* 

Christiane Görgen<br>Mathematisches Institut, Universität Leipzig, Germany<br>e-mail: goergen@math.uni-leipzig.de

## Manuele Leonelli

School of Human Sciences and Technology, IE University, Madrid, Spain
e-mail: manuele.leonelli@ie.edu

## Orlando Marigliano

KTH Royal Institute of Technology, Stockholm, Sweden
e-mail: orlandom@kth.se


#### Abstract

Staged tree models are a discrete generalization of Bayesian networks. We show that these form curved exponential families and derive their natural parameters, sufficient statistic, and cumulant-generating function as functions of their graphical representation. We give necessary and sufficient graphical criteria for classifying regular subfamilies and discuss implications for model selection.


MSC2020 subject classifications: Primary 62H99; secondary 68T99.
Keywords and phrases: Bayesian information criterion, chain event graph, curved exponential family, graphical model, staged tree.

Received December 2020.

## 1. Introduction

Staged trees define statistical models which can account for a variety of partial and asymmetric conditional independence statements between discrete events (Collazo, Görgen and Smith, 2018). The use of these graphical models in applications is constantly increasing (Barclay, Hutton and Smith, 2013; Collazo and Smith, 2015; Keeble et al., 2017) and free software for practitioners is newly available (Carli et al., 2020). However, their formal properties have only recently been studied for the first time (Görgen and Smith, 2018). We now extend this formal study by 1. proving that in general staged tree models form curved exponential families and by 2 . expressing their natural parameters, sufficient statistic,

[^0]
[^0]:    * Christiane Görgen and Manuele Leonelli were supported by the programme "Oberwolfach Leibniz Fellows" of the Mathematisches Forschungsinstitut Oberwolfach in 2017. Orlando Marigliano was supported by International Max Planck Research School and Brummer \& Partners MathDataLab.

and cumulant-generating function as a function of the underlying graphical representation. We also give a graphical criterion under which they form regular exponential families.

Because exponential families exhibit a multitude of desirable inferential properties (Kass and Vos, 1997), similar characterisations for other graphical models have been studied. For instance, undirected graphical models with no hidden variables are regular exponential families (Lauritzen, 1996), Bayesian networks (e.g. Koller and Friedman, 2009) are curved exponential families, and directed graphical models with hidden variables are stratified exponential families (Geiger et al., 2001). These results are critical for model selection techniques. In particular, Haughton (1988) proved that for curved exponential families the Bayesian information criterion (Schwarz, 1978) is an asymptotically valid rule. To this date model selection for staged trees has usually been carried out in a Bayesian fashion by selecting the maximum a posteriori model (Freeman and Smith, 2011; Barclay, Hutton and Smith, 2013; Cowell and Smith, 2014). Now, our results make it theoretically sound to use the Bayesian information criterion as well, and its implementation in the R package stagedtrees (Carli et al., 2020) is thus justified. This criterion has already been employed by Silander and Leong (2013) although its asymptotic geometric validity was not assured at the time.

By expressing every staged tree model explicitly as a curved exponential family, we in particular achieve such an explicit description for every discrete Bayesian network. To the best of our knowledge, this is still missing in the literature. We demonstrate on small-scale examples how a given Bayesian network's exponential form can be stated in staged-tree language. We can then also specify new graphical criteria under which the model is a regular exponential family.

# 2. Staged trees 

### 2.1. Probability trees as graphical statistical models

Probability trees are highly intuitive depictions of unfoldings of discrete events (Shafer, 1996) and have been used in a variety of real-world applications (Smith, 2010; Collazo, Görgen and Smith, 2018).

Let $\mathcal{T}$ be a directed, rooted tree graph where every vertex has either no or at least two emanating edges. For simplicity, we number the inner (non-leaf) vertices $v_{1}, \ldots, v_{k}$, with $v_{1}$ denoting the root, and count the edges emanating from each vertex with indices $j=1, \ldots, \kappa_{i}$ for all $i=1, \ldots, k$. To every edge we assign a positive probability label $\theta_{i j} \in(0,1)$ such that the total sum of all labels belonging to the same vertex is always equal to one, $\sum_{j=1}^{\kappa_{i}} \theta_{i j}=1$. Such a labelled tree graph is called a probability tree.

For all root-to-leaf paths $x$ of $\mathcal{T}$ we define $p_{\theta}(x)=\prod_{i=1}^{k} \prod_{j=1}^{v_{i}} \theta_{i j}^{\alpha_{i j}(x)}$ where $\alpha_{i j}(x)$ is one if $x$ passes through the $j$ th edge emanating from $v_{i}$ and zero otherwise. By the constraints on the $\theta_{i j}$, the function $p_{\theta}$ is a probability distribution on the set of all root-to-leaf paths. We denote the size of this set by $n$. A probability tree model is then the set of all such probability distributions $p_{\theta}$ on $n$

![img-0.jpeg](img-0.jpeg)
(a) A staged tree for three binary random variables representing the collider Bayesian network $X \rightarrow Z \leftarrow Y$.
![img-1.jpeg](img-1.jpeg)
(b) A staged tree representing the conditional independence relation $X \Perp Y$ and $Z \Perp X \mid Y$, and the implied relation $X \Perp Z$.

Fig 1. Two discrete graphical models. Vertices which are in the same stage have been assigned the same colour. In this picture, white-coloured vertices are not in the same stage with any other vertex.
atoms, for varying labels $\theta$. The set of parameters $\theta$ satisfying the constraints above is the parameter space $\Theta_{T}$ of the model. It equals the product $\times_{i=1}^{k} \Delta_{\kappa_{i}-1}^{\circ}$ of the $k$ open probability simplices $\Delta_{\kappa_{i}-1}^{\circ}=\left\{\left(t_{1}, \ldots, t_{\kappa_{i}}\right) \in \mathbb{R}^{\kappa_{i}} \mid \sum_{r=1}^{\kappa_{i}} t_{r}=\right.$ 1 and $0<t_{r}<1$ for all $\left.r=1, \ldots, \kappa_{i}\right\}$. Thus, the parameter space $\Theta_{T}$ has dimension $d=\sum_{i=1}^{k}\left(\kappa_{i}-1\right)$.

# 2.2. Probability trees and conditional independence 

An event in a probability tree is a set of root-to-leaf paths, often specified by shared vertices or edges. Conditional independence relationships between events can be visualized using a simple type of colouring of these vertices in the following way.

A staged tree is a probability tree together with an equivalence relation on the vertex set such that two vertices are in the same stage if and only if their outgoing edges have the same attached probabilities. Figure 1 decpits a first example. A staged tree model is a submodel of a probability tree model where probability simplices in the parameter space have been identified with each other according to the equivalence relation.

For example, if a tree depicts the product state space of a vector of discrete random variables $Y_{i}$, then every inner vertex represents a random variable $Y_{i} \mid Y_{[i-1]}=y_{[i-1]}$ conditional on specific values taken by its ancestors, every edge corresponds to a state $y_{i}$ of that variable, and every edge can be labelled by the conditional probability $P\left(Y_{i}=y_{i} \mid Y_{[i-1]}=y_{[i-1]}\right)$ of the random variable being in that state given the particular ancestor configuration. Here, $[i-1]$ is the set of indices $\{1, \ldots, i-1\}$. The stage relations on the tree can then be used to model conditional independence relations such as

$P\left(Y_{i}=y_{i} \mid y_{[i-1]}\right)=P\left(Y_{i}=y_{i} \mid y_{[i-1]}^{\prime}\right)$.
To illustrate this, in Fig. 1(a) the upward edge emanating from $v_{2}$ can be labeled $P(Y=0 \mid X=0)$ and the upward edge from $v_{4}$ as $P(Z=0 \mid X=0, Y=0)$. Here, the vertices $v_{2}$ and $v_{3}$ are in the same stage. This models the independence $X \Perp Y$ via the equalities $P(Y=y \mid X=0)=P(Y=y \mid X=1)$ for $y=0,1$. Similarly in Fig. 1(b), the additional stages together entail $Z \Perp X \mid Y$.

Thus, staged tree models include as a special case both discrete Bayesian networks and context-specific discrete Bayesian networks, modelling conditional independence relations that hold only for a subset of the states of a discrete random variable (Boutilier et al., 1996). In particular, all conditional independence relations given by the Bayesian network can be reflected in the staging as described above. Varando, Carli and Leonelli (2021) give an algorithm that for any Bayesian network $G$ outputs a staged tree $\mathcal{T}_{G}$ representing the same model.

Because probability trees and staged trees may have root-to-leaf paths of different lengths and because there are no constraints on where stages can be imposed, the class of staged tree models is much wider than the one of discrete Bayesian networks. Working within this class unlocks an immediate graphical representation of modeling assumptions such as the space of events, the intricate conditional independence relationships within this space, and the local sum-to-one conditions. Because staged trees grow quickly even for small problems, whenever they exhibit many symmetries in their subtrees they are sometimes represented more compactly by alternative graphical depictions called chain event graphs: see the textbook by Collazo, Görgen and Smith (2018) for an in-depth discussion of these points.

# 3. Staged trees are curved exponential families 

### 3.1. Exponential families

Following Kass and Vos (1997), a parametric statistical model $\left\{p_{\theta} \mid \theta \in \Theta\right\}$ on a space $\mathcal{X}$ is called an exponential family if every distribution in the model can be written in the form

$$
p_{\theta}(x)=h(x) \exp \left(\eta(\theta)^{\top} T(x)-\psi(\theta)\right) \quad \text { for all } x \in \mathcal{X}
$$

where $\eta: \Theta \rightarrow \mathbb{R}^{d}$ is the canonical parameter, $T: \mathcal{X} \rightarrow \mathbb{R}^{d}$ is a minimally sufficient statistic, ${ }^{\top}$ denotes the transpose operation, and $\psi: \Theta \rightarrow \mathbb{R}$ is the cumulant-generating function. The space $\mathcal{N}=\left\{\eta(\theta) \in \mathbb{R}^{d} \mid(1)\right.$ is integrable $\}$ is called the natural parameter space. If $\mathcal{N}$ is an open and non-empty subset of $\mathbb{R}^{d}$ then the model is called a regular exponential family of dimension $d$.

For exponential families, moments of all orders exist and the maximum likelihood estimator exists and is unique. Regular exponential families are closed under linear contraints on the natural parameter space and the log-likelihood function on that space is concave. Under more general constraints on the parameters, these families are more technical to study but can often retain many

useful asymptotic properties. The two best-studied generalizations of regular exponential families are so-called curved and, more generally, stratified exponential families. The development of this paper requires only the former type of models which we formally introduce in the third subsection below.

# 3.2. Regular exponential families 

In a first step, we focus on probability trees without imposing a stage structure. In this context, the probability tree whose graph is a root vertex connected to its leaves exclusively via single edges is a star as in the graph-theoretic sense.

Lemma 1. Every probability tree model on $n$ atoms is equal to the full probability simplex $\Delta_{n-1}^{s}$.

In particular, the star with $n$ leaves and with probability $\theta_{1 r}$ attached to edge $r$, for $r=1, \ldots, n$, represents the Multinomial distribution $\operatorname{Multi}(1, \theta)$ with one trial and parameters $\theta=\left(\theta_{11}, \ldots, \theta_{1 n}\right)$.

Proof. Every probability tree with $n$ root-to-leaf paths specifies a set of distributions inside the open $n-1$-dimensional probability simplex as outlined in Section 2.1. Conversely, given a fixed tree graph with $n$ leaves, every point $\left(p_{1}, \ldots, p_{n}\right)$ inside the simplex can be interpreted as a vector whose $r$ th component $p_{r}$ is the probability of going down the $r$ th root-to-leaf path in the tree, $r=1, \ldots, n$. We can pick the label of the $j$ th edge out of vertex $v_{i}$ to be the fraction $\sum_{b \in[i j]} p_{b} / \sum_{a \in[i]} p_{a}$ where $[i],[i j] \subseteq\{1, \ldots, n\}$ denote the indices of all root-to-leaf paths passing through vertex $v_{i}$ or through the tail of its $j$ th outgoing edge, respectively. These labels are conditional probabilities and their product along a root-to-leaf path is equal precisely to the atomic probability of that path. This proves the first claim.

As for the second claim, $p_{\theta}(x)=\prod_{r=1}^{n} \theta_{1 r}^{\alpha_{1 r}(x)}$ where $\sum_{r=1}^{n} \theta_{1 r}=1$ is the probability distribution induced by the star with edges numbered $r=1, \ldots, n$. This is the stated Multinomial distribution.

Wishart (1949) derives the exponential form (1) for the Multinomial distribution $\operatorname{Multi}(1, \theta)$ as follows: $h \equiv 1$ is constant, the natural parameters are normalized log-probabilities $\eta_{r}(\theta)=\log \left(\theta_{1 r} /\left(1-\sum_{s=1}^{n-1} \theta_{1 s}\right)\right)$ for $r=1, \ldots, n$, the sufficient statistic is the vector of the first $n-1$ edge indicators $T=\left(\alpha_{11}, \ldots, \alpha_{1, n-1}\right)$, and the cumulant-generating function is the logarithm of the normalizing constant $\psi(\theta)=\log \left(1-\sum_{s=1}^{n-1} \theta_{1 s}\right)$.

By Lemma 1, all probability trees on the same number of root-to-leaf paths are statistically equivalent in the sense that they all represent the same model, namely the full probability simplex. Thus, any probability tree is a graphical representation of the Multinomial distribution, and Wishart's result gives a sufficient statistic, cumulant-generating function, and the natural parameters for any probability tree, possibly after reparametrization.

In Proposition 1, we give a parametrization of the exponential family of a probability tree model which is alternative to Wishart's. This new parametrization has the advantage of respecting the structure of trees having root-to-leaf

![img-2.jpeg](img-2.jpeg)

FIG 2. Illustration of the notation used in Proposition 1. The natural parameter $\eta_{i j}$ belonging to the indicator $\alpha_{i j}$ of "passing through the edge $\left(v_{i}, v_{i j}\right)$ " is a function of the label $\theta_{i j}$ of that edge and of the products $N_{i}$ and $N_{i j}$ of the labels of the downwards pointing $v_{i}$ - and $v_{i j}$-to-leaf paths, respectively. The edges involved in the definition of $\eta_{i j}$ are depicted in bold.
paths longer than single edges. Retaining this extra structure allows us to generalize the exponential-family parametrization of probability trees to the case of staged trees in Section 3.3.

We thus derive the following result. Here for any probability tree $\mathcal{T}$ we say that the $\kappa_{i}$ th edge emanating from vertex $v_{i}$ points downwards, $i=1, \ldots, k$. We then recursively define functions $N_{i}: \Theta_{\mathcal{T}} \rightarrow \mathbb{R}$ as $N_{i}(\theta)=1$ for leaf vertices $v_{i}$ and else as a product of labels pointing downwards $N_{i}(\theta)=\left(1-\sum_{s=1}^{\kappa_{i}-1} \theta_{i s}\right) N_{i \kappa_{i}}(\theta)$ for $i=1, \ldots, k$. The shorthand $N_{i j}$ denotes $N_{r}$ for the vertex $v_{r}$ which is the tail of the $j$ th edge coming out of vertex $v_{i}$. Figure 2 illustrates this notation.

Proposition 1. Every probability tree $\mathcal{T}$ with parameters $\theta$ represents a regular exponential family with the following attributes:

- the indicators $T_{i j}=\alpha_{i j}$ of the first $j=1, \ldots, \kappa_{i}-1$ edges of all inner vertices $i=1, \ldots, k$ are a sufficient statistic,
- the natural parameters $\eta_{i j}$ are locally normalized log-probabilities defined by $\eta_{i j}(\theta)=\log \left(\theta_{i j} N_{i j}(\theta) / N_{i}(\theta)\right)$ for all $j=1, \ldots, \kappa_{i}-1$ and $i=1, \ldots, k$, and the natural parameter space is $\mathbb{R}^{d}$ with $d=\sum_{i=1}^{k}\left(\kappa_{i}-1\right)$, and
- the cumulant-generating function is the negative log-sum of normalizing constants along the root-to-leaf path whose edges all point downwards, $\psi(\theta)=-\log \left(N_{1}(\theta)\right)$
Proof. The desired parametrization is equivalent to

$$
p_{\theta}(x)=N_{1}(\theta) \prod_{i=1}^{k} \prod_{j=1}^{\kappa_{i}-1}\left(\theta_{i j} \frac{N_{i j}(\theta)}{N_{i}(\theta)}\right)^{\alpha_{i j}(x)} \quad \text { for all } x
$$

To prove this equality, we first rewrite the probability mass function introduced in Section 2. For any inner vertex $i=1, \ldots, k$ in the probability tree, the label of the $\kappa_{i}$ th outgoing edge is a function of the first $1, \ldots, \kappa_{i}-1$ edges, namely $\theta_{i \kappa_{i}}=1-\sum_{j=1}^{\kappa_{i}-1} \theta_{i j}$. The indicator $\alpha_{i \kappa_{i}}$ of passing along that edge is a function of the indicators of those same edges and equals $\alpha_{i}(x)\left(1-\sum_{j=1}^{\kappa_{i}-1} \alpha_{i j}(x)\right)$ where $\alpha_{i}(x)$ is one if $x$ reaches vertex $v_{i}$ and zero otherwise.

Thus, the probability mass function of a probability tree can be written as

$$
p_{\theta}(x)=\prod_{i=1}^{k} \prod_{j=1}^{\kappa_{i}} \theta_{i j}^{\alpha_{i j}(x)}=\prod_{i=1}^{k} \prod_{j=1}^{\kappa_{i}-1} \theta_{i j}^{\alpha_{i j}(x)}\left(1-\sum_{j=1}^{\kappa_{i}-1} \theta_{i j}\right)^{\alpha_{i}(x)\left(1-\sum_{j=1}^{\kappa_{i}-1} \alpha_{i j}(x)\right)}
$$

And as a consequence, the claim reduces to:

$$
\prod_{i=1}^{k}\left(1-\sum_{j=1}^{\kappa_{i}-1} \theta_{i j}\right)^{\alpha_{i}(x)\left(1-\sum_{j=1}^{\kappa_{i}-1} \alpha_{i j}(x)\right)}=N_{1}(\theta) \prod_{i=1}^{k} \prod_{j=1}^{\kappa_{i}-1}\left(\frac{N_{i j}(\theta)}{N_{i}(\theta)}\right)^{\alpha_{i j}(x)}
$$

for all root-to-leaf paths $x$. We now prove this claim by induction on the number of inner vertices $k$.

Let thus in a first step the graph be a star, $k=1$. If $x$ is the root-to-leaf path which is one of the first $1, \ldots, \kappa_{1}-1$ edges coming out of the root then (3) states that $1=N_{1}(\theta) \cdot 1 / N_{1}(\theta)=1$. If otherwise $x$ equals the $\kappa_{1}$ st edge then $1-\sum_{j=1}^{\kappa_{1}-1} \theta_{1 j}=N_{1}(\theta)$ which is also true.

If $k>1$ then $x$ may have length greater one and we distinguish two analogous cases. Hereby the induction hypotheses holds for trees smaller than the one we consider and so, in particular, the claim is true for its subtrees. Without loss, we number the vertex at the tail of the first edge of $x$ as $v_{2}$. For simplicity, $A$ denotes the left hand side of (3) and $B$ the right hand side of that equation. Then:

Case 1: The edge $\left(v_{1}, v_{2}\right)$ is one of the first $1, \ldots, \kappa_{1}-1$ edges coming out of the root. Then

$$
\begin{aligned}
A & =1 \cdot \prod_{i=2}^{k}\left(1-\sum_{j=1}^{\kappa_{i}-1} \theta_{i j}\right)^{\alpha_{i}(x)\left(1-\sum_{j=1}^{\kappa_{i}-1} \alpha_{i j}(x)\right)} \\
& =N_{2}(\theta) \prod_{i=2}^{k} \prod_{j=1}^{\kappa_{i}-1}\left(\frac{N_{i j}(\theta)}{N_{i}(\theta)}\right)^{\alpha_{i j}(x)} \\
& =N_{1}(\theta) \frac{N_{2}(\theta)}{N_{1}(\theta)} \prod_{i=2}^{k} \prod_{j=1}^{\kappa_{i}-1}\left(\frac{N_{i j}(\theta)}{N_{i}(\theta)}\right)^{\alpha_{i j}(x)}=B
\end{aligned}
$$

where the final step is true because $N_{2}(\theta)=N_{12}(\theta)$.
Case 2: The edge $\left(v_{1}, v_{2}\right)$ is the $\kappa_{1}$ st edge coming out of the root. Then

$$
\begin{aligned}
A & =\left(1-\sum_{j=1}^{\kappa_{1}-1} \theta_{1 j}\right) \prod_{i=2}^{k}\left(1-\sum_{j=1}^{\kappa_{i}-1} \theta_{i j}\right)^{\alpha_{i}(x)\left(1-\sum_{j=1}^{\kappa_{i}-1} \alpha_{i j}(x)\right)} \\
& =\left(1-\sum_{j=1}^{\kappa_{1}-1} \theta_{1 j}\right) N_{2}(\theta) \prod_{i=2}^{k} \prod_{j=1}^{\kappa_{i}-1}\left(\frac{N_{i j}(\theta)}{N_{i}(\theta)}\right)^{\alpha_{i j}(x)} \\
& =N_{1}(\theta) \prod_{i=2}^{k} \prod_{j=1}^{\kappa_{i}-1}\left(\frac{N_{i j}(\theta)}{N_{i}(\theta)}\right)^{\alpha_{i j}(x)}=B
\end{aligned}
$$

where the final step is true because $\prod_{j=1}^{n_{1}-1}\left(N_{1 j}(\theta) / N_{1}(\theta)\right)^{\alpha_{1 j}(x)}=1$.
This proves (2), and every probability tree represents an exponential family in this parametrization.

The regularity claim follows since the map $\eta$ is a diffeomorphism between the space of model parameters $\Theta$ and $\mathbb{R}^{d}$. Indeed, it has a smooth inverse obtained by first computing $p_{\eta}$ for a given $\eta \in \mathbb{R}^{d}$ according to the given parametrization and then computing $\theta \in \Theta$ such that $p_{\eta}=p_{\theta}$ as described in the proof of Lemma 1.

Proposition 1 enables us to simply read the parametrisation of the underlying exponential family directly from a given probability tree.

Example 1. Consider Fig. 1 and the probability tree which has the same graph as the staged trees in Fig. 1(a) and 1(b). For simplicity, in this binary tree we do not use double indices but label the upwards edges going out of vertex $v_{i}$ as $\theta_{i}$ and the downward edges as $1-\theta_{i}$ for $i=1, \ldots, 7$.

The indicator functions $\alpha_{i 1}$ of the upwards edges $i=1, \ldots, 7$ are a sufficient statistic for this tree. The corresponding natural parameters are then log-ratios of the downwards labels derived as

$$
\begin{aligned}
& \eta_{1}(\theta)=\log \left(\theta_{1}\left(1-\theta_{2}\right)\left(1-\theta_{5}\right) /\left(1-\theta_{1}\right)\left(1-\theta_{3}\right)\left(1-\theta_{7}\right)\right) \\
& \eta_{2}(\theta)=\log \left(\theta_{2}\left(1-\theta_{4}\right) /\left(1-\theta_{2}\right)\left(1-\theta_{5}\right)\right) \\
& \eta_{3}(\theta)=\log \left(\theta_{3}\left(1-\theta_{6}\right) /\left(1-\theta_{3}\right)\left(1-\theta_{7}\right)\right)
\end{aligned}
$$

and $\eta_{i}(\theta)=\log \left(\theta_{i} /\left(1-\theta_{i}\right)\right)$ for $i=4, \ldots, 7$. The cumulant-generating function is the logarithm of the product of the labels along the downward root-to-leaf path coming out of the root vertex $\psi(\theta)=-\log \left[\left(1-\theta_{1}\right)\left(1-\theta_{3}\right)\left(1-\theta_{7}\right)\right]$.

# 3.3. Curved exponential families 

As stated in Section 2.2, every discrete Bayesian network has a corresponding staged tree representation. Since for instance the collider graph does not represent a regular exponential family (Koller and Friedman, 2009), staged trees cannot in general be regular exponential families either. They rather form what is called a curved exponential family: a submodel of a regular exponential family whose parameter space is a smooth manifold (Efron, 1978).

Theorem 1. Staged tree models are curved exponential families.
Proof. By Proposition 1, every staged tree model is a submodel of a regular exponential family. We prove that the natural parameter space is always a smooth manifold of the right dimension by showing that it is the image of a certain linear subspace of $\Theta$ under the diffeomorphism $\eta$.

Let $\mathcal{T}_{0}$ denote a probability tree with parameter space $\Theta_{0}=\times_{i=1}^{k} \Delta_{\kappa_{i}-1}^{\circ}$. Let $\mathcal{T}$ denote the same tree graph together with an imposed stage structure and parameter space $\Theta_{\mathcal{T}}=\times_{r \in R} \Delta_{\kappa_{r}-1}^{\circ}$ for some index set $R \subseteq\{1, \ldots, k\}$. The parameter space of the staged tree model is the kernel of the parameter space of

the saturated model under the linear function $h_{\mathcal{T}}: \mathbb{R}^{d_{0}} \rightarrow \mathbb{R}^{d_{0}-d}$ which encodes the $d_{0}-d$ identifications of edge labels as
$h_{\mathcal{T}}(\theta)=\left(\theta_{i j}-\theta_{s t}\right.$ | for all $j=t=1, \ldots, \kappa_{j}$ and all $v_{i}$ and $v_{s}$ in the same stage $)$
where $d=\sum_{r \in R}\left(\kappa_{r}-1\right)$ is the number of free parameters in the staged tree, and $d_{0}=\sum_{i=1}^{k}\left(\kappa_{i}-1\right)$ is the number of free parameters in the probability tree. By construction, $h_{\mathcal{T}}(\theta)=0$ if and only if $\theta$ fulfills the stage constraints in $\mathcal{T}$. That is, the parameter space of the staged tree model equals the kernel of the $\operatorname{map}(4)$, so $h_{\mathcal{T}}^{-1}(0)=\Theta_{\mathcal{T}}$.

Since $h_{\mathcal{T}}$ is surjective, its kernel is $d$-dimensional. Thus, the parameter space of the staged tree model is a $d$-dimensional linear space in $\mathbb{R}^{d_{0}}$. As a consequence, the natural parameter space, obtained as the image of the diffeomorphism $\eta$ given in Proposition 1, is a smooth manifold of the same dimension. The claim follows.

As an alternative proof strategy for Theorem 1 one may use the characterization of staged tree models as the solution set of a collection of polynomial equations and inequalities provided by Duarte and Görgen (2020). Whenever these polynomials do not exhibit any algebraic singularities inside the probability simplex, the model is a curved exponential family: compare the discussion of implicit model representations given in Geiger et al. (2001) and of algebraic exponential families in Drton and Sullivant (2007).

In particular, whilst the equations coding stage constraints in the conditional probabilities as in (4) are always linear, those coding the same constraints formulated in terms of the natural parameters in general are not. In the following proposition we describe these constraints and explain when they are linear.

Proposition 2. Let $\mathcal{T}$ be a staged tree. For every vertex $v_{i}$ and outgoing edge indexed by $j$, let $\eta_{i j}$ denote the natural parameter of the exponential form derived in Proposition 1, where we additionally define $\eta_{i \kappa_{i}}=0$. Let further $\xi_{i j}=\exp \left(\eta_{i j}\right)$ and $P_{i j}=\sum_{r} \prod_{a b} \xi_{a b}^{\alpha_{a b}(r)}$ where $r$ ranges over the $v_{i j}$-to-leaf paths for every fixed double index $i j$.

Then two vertices $v_{i}$ and $v_{s}$ are in the same stage if and only if they have the same number $\kappa$ of emanating edges and for all $j=1, \ldots, \kappa$ the equality

$$
\eta_{i j}+\log \left(P_{i j}\right)+\log \left(P_{s \kappa}\right)=\eta_{s j}+\log \left(P_{s j}\right)+\log \left(P_{i \kappa}\right)
$$

is true.
Furthermore, let $N_{i j}$ denote the product of the labels along the downwardspointing $v_{i j}$-to-leaf path as in Proposition 1. Then (5) is a linear expression in the $\eta$ if and only if $P_{i j} P_{s \kappa}=P_{s j} P_{i \kappa}$, or equivalently

$$
N_{i j} N_{s \kappa}=N_{s j} N_{i \kappa}
$$

Proof. By definition, $\xi_{i j}=\theta_{i j} N_{i j} / N_{i}$. For any $i$ and edge $j$ emanating from $v_{i}$, the equalities

$$
N_{i j} P_{i j}=\sum_{r} N_{i j} \prod_{a b} \xi_{a b}^{\alpha_{a b}(r)}=\sum_{r} \prod_{a b} \theta_{a b}^{\alpha_{a b}(r)}=1
$$

are true, where $r$ ranges over the $v_{i j}$-to-root paths. In particular, the second equality is obtained by applying (2) to the subtree rooted at $v_{i j}$. The third equality holds because its left-hand side is the sum of all atomic probabilities associated to the subtree rooted at $v_{i j}$. Now let $v_{i}$ and $v_{s}$ be in the same stage. Equivalently, $\theta_{i j}=\theta_{s j}$ for all $j=1, \ldots, \kappa$. This is equivalent to $\xi_{i j} N_{i} / N_{i j}=\xi_{s j} N_{s} / N_{s j}$ which in turn is equivalent to $\xi_{i j} N_{i \kappa} / N_{i j}=\xi_{s j} N_{s \kappa} / N_{s j}$ simply because $\theta_{i \kappa}=\theta_{s \kappa}$. Using $N_{i j} P_{i j}=1$, rearranging, and taking logarithms yields the statement in (5).

As for the second claim, if (6) holds then the log terms in (5) vanish, making it a linear expression in the $\eta$. Conversely, let (5) be a linear expression in the $\eta$. Then the expression

$$
\log \left(P_{i j} P_{s \kappa} / P_{s j} P_{i \kappa}\right)
$$

is also linear in the $\eta$. This implies $P_{i j} P_{s \kappa} / P_{s j} P_{i \kappa}=c \prod_{a b} \xi^{\beta_{a b}}$ for some $c, \beta_{a b} \in \mathbb{R}$. Since the left-hand side of this equality is a rational function in the $\xi$, all $\beta_{a b}$ must be integers. Indeed, otherwise there would exist a choice of $\xi$ that would make the right-hand side evaluate to an irrational number whilst the left-hand side can only evaluate to rational numbers. So, we obtain an equation of the form

$$
P_{i j} P_{s \kappa} \prod_{a b \in A} \xi_{a b}^{\beta_{a b}}=P_{s j} P_{i \kappa} \prod_{c d \in B} \xi_{c d}^{\beta_{c d}}
$$

for some sets $A, B$ of indices and $\beta_{a b}, \beta_{c d} \in \mathbb{N}$.
Suppose now that one of $A$ and $B$ is nonempty, without loss of generality assume it to be $B$. Then some $\xi_{c d}$ divides $P_{i j}$. By the definition of $P_{i j}$, the only way this is possible is if $\xi_{c d}$ divides all summands of $P_{i j}$. That is, if all paths of the subtree rooted at $v_{i j}$ (relabeled with $\theta \mapsto \xi$ ) have the label $\xi_{c d}$ in common. But this is impossible because in a staged tree we assume that each node has at least two children, and thus we can always find a path that avoids the label $\xi_{c d}$. Hence we see that both $A$ and $B$ must be empty, so $P_{i j} P_{s \kappa}=P_{s j} P_{i \kappa}$. And hence $N_{i j} N_{s \kappa}=N_{s j} N_{i \kappa}$ using $N_{i j} P_{i j}=1$.

Let $\mathcal{T}$ be a staged tree. Proposition 2 shows that the exponential family of $\mathcal{T}$ proposed in this paper is a regular exponential family if and only if the equality of ratios in (6) is true for every pair of vertices $v_{i}$ and $v_{s}$ in the same stage and every edge $j$ emanating from these vertices. For this reason, staged trees satisfying this property are of particular interest. We henceforth call these regular staged trees.

Equation (6) gives a simple criterion for regularity by comparing certain concatenations of downwards-pointing paths. Algebraically, it can be checked by comparing the monomials $\prod_{a b} \theta_{a b}$ obtained by multiplying all labels in the four downward-pointing paths starting from $v_{i j}, v_{i \kappa}, v_{s j}, v_{s \kappa}$, respectively. Graphically, it can be verified by checking that the concatenation of the first and fourth path on the above list is the same as the concatenation of the second and third, up to a permutation of the edges.

Next, we explore two prominent classes of regular staged trees. The notion of a balanced staged tree, first formalized in Duarte and Ananiadi (2021), is

an important notion for studying the toric geometry of staged trees (Görgen, Maraj and Nicklasson, 2021). It makes use of the interpolating polynomials $t_{i j}$ defined by $t_{i j}=\sum_{r} \prod_{a b} \theta_{a b}^{\alpha_{a b}(r)}$, where $r$ ranges over the $v_{i j}$-to-leaf paths. This sum is to be read as a formal sum of labels, i.e. without using local sum-to-one conditions. (Including these conditions would imply $t_{i j}=1$.) A staged tree is balanced if for all $v_{i}$ and $v_{s}$ in the same stage and all edges $j$ emanating from $v_{i}$ we have $t_{i j} t_{s \kappa}=t_{i \kappa} t_{s j}$, where again $\kappa$ denotes the chosen downwards-pointing edge emanating from $v_{i}$. This definition for balanced staged trees differs slightly from the one found in the literature but is nevertheless equivalent to it. For a graphical interpretation of this condition, note that $t_{i j} t_{s \kappa}$ is the interpolating polynomial of the staged tree obtained by attaching a copy of the subtree rooted at $v_{s \kappa}$ to each of the leaves of the subtree rooted at $v_{i j}$. The condition for a balanced tree now is equivalent to this composite tree being statistically equivalent to the composite tree corresponding to the product $t_{i \kappa} t_{s j}$.

Simple staged trees are defined in Collazo, Görgen and Smith (2018). A staged tree is simple if for all $v_{i}$ and $v_{s}$ in the same stage and all edges $j$ emanating from $v_{i}$ we have $t_{i j}=t_{s j}$.

Proposition 3. All balanced staged trees are regular. In particular, all simple staged trees are regular.

Proof. By definition, all simple trees are balanced. Now let $\mathcal{T}$ be a balanced staged tree and $v_{i}, v_{s}$ vertices in the same stage. Let $j$ be an edge emanating from $v_{i}$. Splitting off the unique downwards-pointing path from $v_{i j}$, write $t_{i j}=$ $t_{i j}^{\prime}+N_{i j}$, and likewise for the other pairs of indices. Then

$$
\begin{aligned}
0 & =t_{i j} t_{s \kappa}-t_{i \kappa} t_{s j} \\
& =\left(t_{i j}^{\prime} t_{s \kappa}^{\prime}-t_{s j}^{\prime} t_{i \kappa}^{\prime}+t_{i j}^{\prime} N_{s \kappa}-t_{s j}^{\prime} N_{i \kappa}+t_{s \kappa}^{\prime} N_{i j}-t_{i \kappa}^{\prime} N_{s j}\right)+\left(N_{i j} N_{s \kappa}-N_{s j} N_{i \kappa}\right) \\
& =: R+Q
\end{aligned}
$$

where we define $R$ resp. $Q$ to be the left resp. right outer summand of the middle expression. Consider this expression as a polynomial $P$ in the $\theta_{a b}$ labels. Split this set of labels into two sets $A$ and $B$ of labels pointing downwards, resp. not pointing downwards. Thus $P$ can be viewed as a polynomial in $\mathbb{R}[A][B]$. Now, all summands of $P$ in $R$ are divisible by some label in the set $B$. This means that $Q \in \mathbb{R}[A]$ is the constant term of the polynomial $P \in \mathbb{R}[A][B]$. Thus $P=0$ implies $Q=0$.

The following converse to Proposition 3 holds for all binary trees with three levels.

Conjecture 1. All regular staged trees are balanced.
As an indication for this conjecture, while (6) seems much weaker than the balanced condition for two nodes $v_{i}$ and $v_{s}$, in a regular tree it can be applied recursively everywhere downstream of $v_{i}$ and $v_{s}$, greatly limiting the possible staging structure.

Example 2. Figure 1(a) shows a staged tree representation of the collider Bayesian network $X \rightarrow Z \leftarrow Y$ which is not a regular exponential family. We can see here that indeed in our parametrization, the linear stage identifications $\theta_{2}=\theta_{3}$ do not give rise to linear constraints on the natural parameters $\eta_{2}$ and $\eta_{3}$. Instead, by Proposition 2,

$$
\eta_{2}+\log \left(\xi_{4}+1\right)+\log \left(\xi_{7}+1\right)=\eta_{3}+\log \left(\xi_{5}+1\right)+\log \left(\xi_{6}+1\right)
$$

where $\xi_{l}=\exp \left(\eta_{l}\right)$ for $l=1, \ldots, 7$. This implies the following equation

$$
\exp \left(\eta_{2}\right)\left(1+\exp \left(\eta_{4}\right)\right)\left(1+\exp \left(\eta_{7}\right)\right)=\exp \left(\eta_{3}\right)\left(1+\exp \left(\eta_{5}\right)\right)\left(1+\exp \left(\eta_{6}\right)\right)
$$

which fully characterises the corresponding curved exponential family in the natural parameters.

The staged tree in Fig. 1(b) however fulfills the linearity criteria in Proposition 2. In particular, the stage constraints $\theta_{2}=\theta_{3}, \theta_{4}=\theta_{6}$, and $\theta_{5}=\theta_{7}$ together imply that $\left(1-\theta_{4}\right)\left(1-\theta_{7}\right)=\left(1-\theta_{6}\right)\left(1-\theta_{5}\right)$ as in (6). They thus give rise to linear (equality) constraints $\eta_{2}=\eta_{3}$ on the natural parameters. The same simplification would occur were $v_{4}$ and $v_{5}$, and $v_{6}$ and $v_{7}$ in the same stage, respectively, rather than $v_{4}$ and $v_{6}$, and $v_{5}$ and $v_{7}$. These stagings all give rise to balanced and regular trees.

Equations on the natural parameters in a curved exponential family can be highly non-trivial. In this paper we found that for a staged tree they are functions of subgraphs, derived from the conditional independence relations coloured in the tree. Thus, the equations on its exponential family parametrization can be directly read from the graph. This formulation has only been possible thanks to the probability tree's expressiveness of the underlying space of events and of its parametrization.

Analogous results have to the best of the authors' knowledge not been derived in the literature of Bayesian networks. While sufficient statistics for these models are known, natural parameters have not been explicitly computed (e.g. Loh and Wainwright, 2013). In order to translate our formulae into the language of Bayesian networks, first a given directed acyclic graph needs to be transformed into the corresponding staged tree using the algorithm provided by Varando, Carli and Leonelli (2021), and then the staged-tree language can be used to infer a natural parametrization as in Proposition 1. Bayesian networks themselves provide a too-compact representation of the underlying modelling assumptions to be able to directly express their exponential form as a function of the graph. However, Proposition 3 yields the following insight.

Corollary 1. Let $G$ be a Bayesian network. The exponential family obtained by applying Proposition 1 to the associated staged tree $\mathcal{T}_{G}$ is regular if $G$ is decomposable or if there exists a topological ordering $\left(1, \ldots, n_{G}\right)$ of the nodes of $G$ such that the parents of the $(i+1)$ th node are a subset of the union of the $i$ th node and its parents for all $i$.
Proof. The first statement is well known but also a direct consequence of the fact that $\mathcal{T}_{G}$ is balanced if and only if $G$ is decomposable (Duarte and Solus,

2021). The second statement corresponds to the definition of $G$ being simple given in Leonelli and Varando (2022). These authors prove that $G$ is simple if and only if $\mathcal{T}_{G}$ is simple. By Proposition 3, simple staged trees form regular exponential families.

# Acknowledgments 

We are grateful to Giovanni Pistone and to Piotr Zwiernik for discussions during the early stages of this project and to Eva Riccomagno for comments on an earlier version of this paper. We also thank the two anonymous referees for their comments which led to a significant improvent of our results.
