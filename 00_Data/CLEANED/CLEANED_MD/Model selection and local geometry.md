# Model selection and local geometry. 

Robin J. Evans<br>University of Oxford<br>evans@stats.ox.ac.uk

December 6, 2019


#### Abstract

We consider problems in model selection caused by the geometry of models close to their points of intersection. In some cases - including common classes of causal or graphical models, as well as time series models - distinct models may nevertheless have identical tangent spaces. This has two immediate consequences: first, in order to obtain constant power to reject one model in favour of another we need local alternative hypotheses that decrease to the null at a slower rate than the usual parametric $n^{-1 / 2}$ (typically we will require $n^{-1 / 4}$ or slower); in other words, to distinguish between the models we need large effect sizes or very large sample sizes. Second, we show that under even weaker conditions on their tangent cones, models in these classes cannot be made simultaneously convex by a reparameterization.

This shows that Bayesian network models, amongst others, cannot be learned directly with a convex method similar to the graphical lasso. However, we are able to use our results to suggest methods for model selection that learn the tangent space directly, rather than the model itself. In particular, we give a generic algorithm for learning Bayesian network models.


## 1 Introduction

Consider a class of probabilistic models $\mathcal{M}_{i}$ indexed by elements of some set $i \in I$, and suppose that we have data from some distribution $P$; model selection is the task of deducing, from the data, which $\mathcal{M}_{i}$ contains $P$. Typically there will be multiple such models, in which case one may appeal to parsimony or - if the model class is closed under intersection-select the smallest such model by inclusion.

There have been dramatic advancements in certain kinds of statistical model selection, including methods for working with large datasets and very high-dimensional problems (see, for example, Bühlmann and van de Geer, 2011). However, model selection in some settings is more difficult; for example, selecting an optimal Bayesian network for discrete data is known to be an NP-complete problem (Chickering, 1996). In this paper we consider why some model classes are so much harder to learn with than others. Taking a geometric approach, we find that some classes contain models which are distinct but - in a sense that will be made precise-are locally very similar to one another. The task of distinguishing between them using data is therefore fundamentally more difficult, both statistically and computationally.

Example 1.1. To illustrate the main idea in simple terms, consider a model space smoothly described by a two dimensional parameter $\boldsymbol{\theta}=\left(\theta_{1}, \theta_{2}\right)^{T} \in \mathbb{R}^{2}$, and with four submodels of interest:

$$
\begin{array}{ll}
\mathcal{M}_{\theta}: \theta_{1}=\theta_{2}=0 & \mathcal{M}_{1}: \theta_{2}=0 \\
\mathcal{M}_{2}: \theta_{1}=0 & \mathcal{M}_{12}: \text { unrestricted. }
\end{array}
$$

In a setting with independent data, we would expect to have statistical power sufficient to distinguish between $\mathcal{M}_{12}$ and $\mathcal{M}_{2}$ (i.e. to determine whether or not $\theta_{1}=0$ ) provided that the

![img-0.jpeg](img-0.jpeg)

Figure 1: Illustration of model selection close to points of intersection. On the left, the models $\mathcal{M}_1$ and $\mathcal{M}_2$ (in blue and red respectively) have different tangent spaces, so the distance between them increases linearly as one moves away from the intersection. On the right, the models $\mathcal{M}_1$ (in blue) and $\mathcal{M}_2$ (in red) have the same tangent space at the intersection, so they diverge only quadratically with distance from the intersection.

magnitude of $\theta_1$ is large compared to $n^{-1/2}$, where $n$ is the number of independent samples available. We might also expect to be able to distinguish between $\mathcal{M}_1$ and $\mathcal{M}_2$ at the same asymptotic rate; this is the picture in Figure 1(a), in which the distance between the two models is proportional to distance from their intersection $\mathcal{M}_\emptyset = \mathcal{M}_1 \cap \mathcal{M}_2$ (the constant of proportionality being determined by the angle between the two models).

Suppose now that we define a model $\mathcal{M}_2^0 : \psi_1 = 0$, where $\psi_1 \equiv \theta_1^2 - \theta_2$, and have to select between $\mathcal{M}_\emptyset$, $\mathcal{M}_1$, $\mathcal{M}_2^0$, $\mathcal{M}_{12}$ (note that we still have $\mathcal{M}_\emptyset = \mathcal{M}_1 \cap \mathcal{M}_2^0$), as illustrated in Figure 1(b). Superficially, the task of choosing between these four models seems no different to our first scenario, but in fact the models $\mathcal{M}_1$ and $\mathcal{M}_2^0$ are locally linearly identical at the point of intersection $\psi_1 = \theta_2 = 0$: that is, the tangent spaces of the two models at this point are the same, so up to a linear approximation they are indistinguishable.

Models that overlap linearly in the manner above lead to two major consequences relating to statistical power and computational efficiency. First, as illustrated in Figure 1(b), if $\mathcal{M}_1$ is correct the distance between the true parameter value ($\theta_1, 0$) and the closest point on $\mathcal{M}_2^0$ grows quadratically rather than linearly in $\theta_1$. Hence, while $|\theta_1| = \Omega(n^{-1/2})$ is sufficient to gain power against $\mathcal{M}_\emptyset$, one needs $|\theta_1| = \Omega(n^{-1/4})$ to ensure power against $\mathcal{M}_2^0$. This is potentially a very stringent condition indeed: if the effect size is halved, then we will need 16 times the sample size to maintain power against the alternative model.

Second, if two models have the same tangent space then we cannot choose a parameterization under which both models are convex sets. Note that in Figure 1(a) all four models are convex, but in Figure 1(b) the model $\mathcal{M}_2^0$ is not. If we reparameterize to make $\mathcal{M}_2^0$ convex, then $\mathcal{M}_1$ will not be. This prevents penalized methods such as the lasso being used in a computationally efficient way.

Example 1.2 (Directed Gaussian Graphical Models). A common class of models in which the phenomenon described above occurs is Gaussian Bayesian networks. Consider the two graphs shown in Figure 2, each representing certain multivariate Gaussian distributions over variables $X, Y, Z$ with joint correlation matrix $\Pi$. The graph in Figure 2(a) corresponds to the marginal independence model $X \pm Y$, so that there is a zero in the corresponding entry in $\Pi$: $\rho_{xy} = 0$. Figure 2(b), on the other hand, corresponds to the conditional independence model $X \pm Y \mid Z$; that is, to a zero in the $X, Y$ entry of $\Pi^{-1}$, or equivalently to $\rho_{xy} - \rho_{xz} \rho_{zy} = 0$.

<sup>1</sup>Typically this would be approximated by the Mahalanobis distance using the Fisher information. For regular statistical models, this is locally equivalent to the Hellinger distance or the square-root of the KL-divergence.

<sup>2</sup>Recall that for positive functions $f, g$ we have $f(x) = \Omega(g(x))$ if and only if $g(x) = O(f(x))$, and $f(x) = \omega(g(x))$ if and only if $g(x) = o(f(x))$.

<sup>3</sup>By 'reparameterize' we mean under a twice differentiable bijection with an invertible Jacobian. So we do not allow the map $(\theta_1, \theta_2) \mapsto (\psi_1, \theta_2)$ used in the earlier example.

![img-1.jpeg](img-1.jpeg)

Figure 2: Two Bayesian networks in which, for Gaussian random variables, the tangent spaces of the models are identical at some points of intersection.

The two models intersect along two further submodels: for example, if $\rho_{xz}=0$ (so that $X \Perp Z$), then $\rho_{xy}=0$ if and only if $\rho_{xy}-\rho_{xz} \rho_{zy}=0$. The same thing happens if $\rho_{yz}=0$ (i.e. $Y \Perp Z$). When we are at the intersection between all these submodels—so $\rho_{xy}=\rho_{x z}=$ $\rho_{yz}=0$ and all variables are jointly independent—we find that the tangent spaces of the two original models are the same, giving rise to the phenomenon described above. Indeed, we will see that this arises whenever two models intersect along two or more such—suitably distinct—further submodels (Theorem 3.1).

### 1.1 Background and Prior Work

Crudely speaking, there are two flavours of statistical model, and consequently two main reasons for wishing to select one. The first, called substantive or explanatory, emphasizes the use of models to explain underlying phenomena, and such models are sometimes viewed as approximations to an unknown scientific 'ground truth' (Cox, 1990; Skrondal and Rabe-Hesketh, 2004). The second kind, referred to as empirical or predictive, is mainly concerned with predicting outcomes from future observations, generally assuming that such observations will arise from the same population as previous data (Breiman, 2001). A discussion of these two camps, together with some finer distinctions can be found in Cox (1990).

Our focus will primarily be on substantive models, in which case different models may lead to rather different practical conclusions, even if the probability distributions associated with them are 'close' in the sense observed above. The case of causal models such as the graphs in Figure 2 is particularly stark: the reversal of an arrow will significantly affect our understanding of how a system will behave under an intervention. For interpolative prediction—that is, with new data from the same population as the data used to learn the model—such concerns are generally lessened: if two probability distributions are similar then they should give similar conclusions. However, the computational concerns we raise will affect model selection performed for whatever reason.

For Bayesian network (BN) models specifically, there has been a great deal of work dealing with the problem of accurate learning from data. Chickering (1996) showed that the problem of finding the BN which maximizes a penalized likelihood criterion is NP-complete in the case of discrete data with several common penalties. Uhler et al. (2013) give geometric proofs that directed Gaussian graphical models are, in a global sense, very hard to learn using sequential independence tests; this is because the volume of 'unfaithful' points that will mislead at least one hypothesis test for a given sample size is very large, and in settings where the number of parameters is larger than the number of observations will overwhelm the model. Our approach is considerably simpler and is applicable to arbitrary model classes and model selection procedures, but cannot make global statements about the model.

Shojaie and Michailidis (2010) provide a penalized method for learning sparse high-dimensional graphs, but they assume a known topological ordering for the variables in the graph: that is, the direction of each possible edge is known. Ni et al. (2015) develop a Bayesian approach that is similar in spirit, and apply it to gene regulatory networks. Fu and Zhou (2013), Gu et al. (2014) and Aragam and Zhou (2015) all use penalization to learn BNs without a pre-specified topological order, in the former paper even allowing for interventional data; however in each case the resulting optimization problem is non-convex. Other

approaches based on assumptions such as non-Gaussianity or non-linearity are also available (Shimizu et al., 2006; Bühlmann et al., 2014).

# 1.2 Contribution 

In this paper we develop the notion of using local geometry as a heuristic for how closely related two models are, and how rich a class of models is. In several classes of models for which model selection is known to be difficult, we find that they contain distinct models that are linearly equivalent at certain points in the parameter space. This makes it statistically difficult to tell which model is correct.

Under even weaker conditions, we find that distinct models may have directions that can be approximately obtained in both models, but not in their intersection. This means the models cannot be simultaneously convex, and prevents efficient algorithms from being used to learn which model is correct; this makes it computationally hard to pick the best model. To our knowledge, these are completely new contributions to the literature.

The remainder of the paper is organized as follows. In Section 2 we formalize the intuition given above by carefully defining local similarity between models, and then proving results relating to local asymptotic power and convex parameterizations. In Section 3 we give sufficient conditions for this situation to occur, including the intersection of two models along multiple distinct submodels. In Section 4 we apply these results to show that the lasso cannot be used directly to learn Bayesian networks. Section 5 provides further examples of how the result can be applied, while Section 6 considers related phenomena such as double robustness. Section 7 suggests methods to exploit model classes in which the tangent spaces are distinct but in which we cannot make the models simultaneously convex, and Section 8 contains a discussion.

## 2 Models

Consider a class of finite-dimensional probability distributions $\left\{P_{\theta}: \theta \in \Theta\right\}$, where $\Theta$ is an open subset of $\mathbb{R}^{k}$; each $P_{\theta}$ has density $p_{\theta}$ with respect to a measure $\mu$. We assume throughout that the parameter $\theta$ describes a smooth (twice differentiable with full rank Jacobian) bijective map between the set of distributions and $\Theta$. Consequently, we will refer interchangeably to a subset of parameters and the corresponding set of probability distributions as a model.

Suppose we have models corresponding to subsets $\mathcal{M}_{i} \subseteq \Theta, i=1,2, \ldots$. We take our models to be either differentiable manifolds or semialgebraic sets ${ }^{4}$; that is, a finite union of sets defined by a finite set of polynomial equalities and inequalities. Semialgebraic sets include a wide range of models of interest, see Drton and Sullivant (2007) for further examples. Our formal discussion of the similarity of these models is based on their tangent cones and tangent spaces at points of intersection.

Definition 2.1. The tangent cone $\mathrm{C}_{\theta}(\mathcal{M})$ of a model $\mathcal{M} \subseteq \Theta$ at $\theta \in \mathcal{M}$ is defined as the set of limits of sequences $\alpha_{n}\left(\theta_{n}-\theta\right)$, such that $\alpha_{n}>0, \theta_{n} \in \mathcal{M}$ and $\theta_{n} \rightarrow \theta$.

The tangent space of $\mathcal{M}$ at $\theta$ is the vector space $\mathrm{T}_{\theta}(\mathcal{M})$ spanned by elements of the tangent cone.

Clearly the tangent space contains the tangent cone; the model is said to be regular at $\theta$ if the two are equal; in particular this means that $\mathcal{M}$ looks like a differentiable manifold (embedded in $\Theta$ ) at $\theta$, and regular parametric asymptotics apply: in other words, the maximum likelihood estimator is asymptotically normal with covariance given by the inverse Fisher information (van der Vaart, 1998). Most of the models we will initially consider are regular everywhere, though their intersections may not be.

[^0]
[^0]:    ${ }^{4}$ Note that these guarantee Chernoff regularity (Drton, 2009a, Lemma 3.3 and Remark 3.4).

# 2.1 c-equivalence 

Our next definition considers the classification of models based on their local similarity. We work with a local version of the Hausdorff distance between sets; this is the furthest distance from any point on one set to the nearest point on the other. Denote this by

$$
D(A, B) \equiv \max \left\{\sup _{a \in A} \inf _{b \in B}\|a-b\|, \sup _{b \in B} \inf _{a \in A}\|a-b\|\right\}
$$

Definition 2.2. We say that $\mathcal{M}_{1}, \mathcal{M}_{2}$ are $c$-equivalent at $\theta \in \mathcal{M}_{1} \cap \mathcal{M}_{2}$ if the Hausdorff distance between the sets in a ball of radius $\varepsilon$ is $o\left(\varepsilon^{c}\right)$. Formally:

$$
\lim _{\varepsilon \downarrow 0} \varepsilon^{-c} D\left(\mathcal{M}_{1} \cap N_{\varepsilon}(\theta), \mathcal{M}_{2} \cap N_{\varepsilon}(\theta)\right)=0
$$

where $N_{\varepsilon}(\theta)$ is an $\varepsilon$-ball around $\theta$. In other words, within an $\varepsilon$-ball of $\theta$, the maximum distance between the two models is $o\left(\varepsilon^{c}\right)$.

If the limit above is bounded but not necessarily zero - i.e. the distance is $O\left(\varepsilon^{c}\right)$-we will say that $\mathcal{M}_{1}$ and $\mathcal{M}_{2}$ are $c$-near-equivalent at $\theta$.

The definition of $c$-equivalence is given by Ferrarotti et al. (2002), who also derive some of its elementary properties. If $\theta \in \mathcal{M}_{1} \cap \mathcal{M}_{2}$ then 1 -near-equivalence is trivial, while 1 equivalence means that to a linear approximation around $\theta$ the models are the same (formally they have the same tangent cone at $\theta$ ); this is illustrated by the two surfaces in Figure 3(a). Similar considerations can be applied to higher orders: 2-equivalence means that the quadratic surface best approximating one model is the same as that approximating the other. For $D^{k_{-}}$ models $^{5}$ with $l \leq k-1$, we have that $(l-1)$-equivalence for $l \in \mathbb{N}$ implies $l$-near-equivalence.

Proposition 2.3 (Ferrarotti et al. (2002), Proposition 1.3). Two semialgebraic models $\mathcal{M}_{1}, \mathcal{M}_{2}$ are 1-equivalent at $\theta \in \mathcal{M}_{1} \cap \mathcal{M}_{2}$ if and only if $\mathrm{C}_{\theta}\left(\mathcal{M}_{1}\right)=\mathrm{C}_{\theta}\left(\mathcal{M}_{2}\right)$.

Example 2.4. Consider the two graphical models in Figure 2, defined respectively by the independence constraints $X \Perp Y$ and $X \Perp Y \mid Z$. If we take the set of trivariate Gaussian distributions satisfying these two restrictions then, as discussed in Section 1, the two models are 2 -near-equivalent at all diagonal covariance matrices.

For finite discrete variables, however, these two models are not 1-equivalent. Suppose $X, Y, Z$ take $n_{X}, n_{Y}, n_{Z}$ levels respectively. The models are defined by the equations

$$
\begin{aligned}
& X \Perp Y \quad: \quad p(x, y)-p(x) \cdot p(y)=0 \quad \forall x, y \\
& X \Perp Y \mid Z \quad: \quad p(x, y, z) \cdot p(z)-p(x, z) \cdot p(y, z)=0 \quad \forall x, y, z,
\end{aligned}
$$

where, for example, $p(x, z)=P(X=x, Z=z)$. In particular, the marginal independence model is subject to $\left(n_{X}-1\right)\left(n_{Y}-1\right)$ restrictions, but the conditional independence model is subject to that many restrictions for each level of $Z$. One can use this to show that the dimension of the conditional independence model is smaller than the marginal independence model, and so they cannot both be approximated by the same linear space.

### 2.2 Overlap

In spite of the differing dimensions in the example above, we will show that the issue - noted in the Introduction - of the models not being simultaneously convex still arises. This motivates a slightly weaker definition for models meeting in an intuitively 'irregular' manner, which we term overlap.

Definition 2.5. Suppose we have two models $\mathcal{M}_{1}, \mathcal{M}_{2}$ with a common point $\theta \in \mathcal{M}_{1} \cap \mathcal{M}_{2}$. We say that $\mathcal{M}_{1}$ and $\mathcal{M}_{2}$ overlap if there exist points $h \in \mathrm{C}_{\theta}\left(\mathcal{M}_{1}\right) \cap \mathrm{C}_{\theta}\left(\mathcal{M}_{2}\right)$ but $h \notin$ $\mathrm{C}_{\theta}\left(\mathcal{M}_{1} \cap \mathcal{M}_{2}\right)$.

[^0]
[^0]:    ${ }^{5}$ That is, $k$-times differentiable.

In other words, there are tangent vectors that can be obtained in either model, but not in their intersection. Note that necessarily we have $\mathrm{C}_{\theta}\left(\mathcal{M}_{1} \cap \mathcal{M}_{2}\right) \subseteq \mathrm{C}_{\theta}\left(\mathcal{M}_{1}\right) \cap \mathrm{C}_{\theta}\left(\mathcal{M}_{2}\right)$, so the definition asks that this is a strict inclusion. For distinct, regular algebraic models, overlap is implied by 1-equivalence.
Lemma 2.6. Let $\mathcal{M}_{1}$ and $\mathcal{M}_{2}$ be algebraic models that are 1-equivalent and regular at $\theta$, but not equal in a neighbourhood of $\theta$. Then $\mathcal{M}_{1}$ and $\mathcal{M}_{2}$ overlap at $\theta$.
Proof. Suppose that, at $\theta$, the models do not overlap and are 1-equivalent. We will show that they are equal in a neighbourhood of $\theta$.

Since $\mathcal{M}_{1}$ is regular at $\theta$ we can assume that it is an irreducible model, else replace it with its unique irreducible component containing $\theta$ (similarly for $\mathcal{M}_{2}$ ). The condition that the models are 1-equivalent implies $\mathrm{C}_{\theta}\left(\mathcal{M}_{1}\right)=\mathrm{C}_{\theta}\left(\mathcal{M}_{2}\right)$, and no overlap means $\mathrm{C}_{\theta}\left(\mathcal{M}_{1} \cap \mathcal{M}_{2}\right)=$ $\mathrm{C}_{\theta}\left(\mathcal{M}_{1}\right) \cap \mathrm{C}_{\theta}\left(\mathcal{M}_{2}\right)=\mathrm{C}_{\theta}\left(\mathcal{M}_{1}\right)$.

On the other hand, $\mathcal{M}_{1} \cap \mathcal{M}_{2}$ is an algebraic submodel of $\mathcal{M}_{1}$, so it is either equal to $\mathcal{M}_{1}$ or has strictly lower dimension. If the latter, then $\mathrm{C}_{\theta}\left(\mathcal{M}_{1} \cap \mathcal{M}_{2}\right)$ would be of this same lower dimension (Cox et al., 2008, Theorem 9.7.8), and hence is a strict subset. Since we have already seen that $\mathcal{M}_{1} \cap \mathcal{M}_{2}$ has the same tangent cone as $\mathcal{M}_{1}$, it must be that the former possibility holds; that is, $\mathcal{M}_{1} \cap \mathcal{M}_{2}=\mathcal{M}_{1}$, in a neighbourhood of $\theta$. Clearly the same is true for $\mathcal{M}_{2}$, which proves the result.

The same result could be applied to analytic models, defined by the zeroes of analytic functions, since these functions are (by definition) arbitrarily well approximated by their Taylor series.
Remark 2.7. Without assuming that models are analytic, one can construct examples that are 'regular' in most of the usual statistical senses, but for which the previous result fails. As an example of how things can go wrong, consider the function $f(x)=e^{-1 / x^{2}} \sin \left(1 / x^{2}\right)$ (taking $f(0)=0$ ); this is a $C^{\infty}$ function, but is not analytic at $x=0$ (all its derivatives being zero at this point).

Now let $\mathcal{M}_{1}=\{(x, 0): x \in \mathbb{R}\}$ and $\mathcal{M}_{2}=\{(x, f(x)): x \in \mathbb{R}\}$. These models are $c$ equivalent for every $c \in \mathbb{N}$, but are not equal. However, in contrast to the result of Lemma 2.6 they do not overlap. Both sets have tangent cone equal to $\mathcal{M}_{1}$, and since $f$ has infinitely many roots in any neighbourhood of 0 , the tangent cone of $\mathcal{M}_{1} \cap \mathcal{M}_{2}$ is also $\mathcal{M}_{1}$.

A canonical example of sets that overlap but are not 1-equivalent is given by the subsets of $\mathbb{R}^{3}$ shown in Figure 3(c); $\mathcal{M}_{1}=\{(x, y, z): y=z=0\}$ (in blue) and $\mathcal{M}_{2}=\{(x, y, z)$ : $z=-x^{2}\}$ (in red) have $\mathcal{M}_{1} \cap \mathcal{M}_{2}=\{0\}$. The tangent cone of $\mathcal{M}_{2}$ is the plane $z=0$, while $\mathcal{M}_{1}$ is its own tangent cone and therefore $\mathrm{C}_{0}\left(\mathcal{M}_{1}\right) \subseteq \mathrm{C}_{0}\left(\mathcal{M}_{2}\right)$ and $\mathrm{C}_{0}\left(\mathcal{M}_{1}\right) \cap \mathrm{C}_{0}\left(\mathcal{M}_{2}\right)=\mathcal{M}_{1}$. However, $\mathrm{C}_{0}\left(\mathcal{M}_{1} \cap \mathcal{M}_{2}\right)=\{0\}$, so the inclusion is strict. In words, we can approach the origin along a line that becomes tangent to the $x$-axis in either model, but not in the intersection. The blue model has smaller dimension than the red so they clearly not 1-equivalent.

Typically it is hard to show that two models are not 1-equivalent (or do not overlap) anywhere in the parameter space: indeed the difficulty of verifying such global conditions is one of our motivations for considering these local criteria instead. However, for algebraic models we can often show that such points are at most a set of zero measure within a large class of 'interesting' submodels. To be more precise, if two models are not 1-equivalent at some model of total independence (say $\theta_{0}$ ), then they are also 1-equivalent almost nowhere within any algebraic model that contains $\theta_{0}$.

# 2.3 Statistical Power 

We will assume that all the models we consider satisfy standard parametric regularity conditions, in particular differentiability in quadratic mean (DQM), which yields the familiar asymptotic expansion of the log-likelihood $\ell(\theta)$ (see, e.g. van der Vaart, 1998):

$$
\ell\left(\theta+h_{n}\right)-\ell(\theta)=\frac{h^{T}}{\sqrt{n}} \dot{\ell}(\theta)-\frac{1}{2} h^{T} I(\theta) h+o_{p}(1)
$$

![img-2.jpeg](img-2.jpeg)

Figure 3: Illustration of two models that (a),(b) are 1-equivalent; (c) overlap. In (a) and (b) the two surfaces have the same tangent space, but meet in this way for different reasons.

where $\hat{\ell}(\theta)$ is the data dependent score, $I(\theta)$ the Fisher information for one observation, and $n^{1/2}h_{n} \rightarrow h$. For the purpose of distinguishing between models from data we need the difference between the log-likelihoods at points close to the MLE not to vanish as sample size $n \rightarrow \infty$. The expansion above shows that this requires $h \neq 0$ for the right hand side to contain a stable term. Hence the distance between the two parameter values needs to shrink no faster than $n^{-1 / 2}$, the standard parametric rate of statistical convergence.

We consider settings in which $h_{n}, \tilde{h}_{n} \rightarrow 0$ with $n^{1 / 2}\left(h_{n}-\tilde{h}_{n}\right) \rightarrow k$, so that we may compare alternatives in two different models. For this reason we impose the stronger condition that the model is *doubly* differentiable in quadratic mean (DDQM) in some neighbourhood of $\theta$. This is closely related to existence and continuity of the Fisher information and will hold, for example, on the interior of the parameter space of any regular exponential family model.

**Definition 2.8.** Say that $p_{\theta}$ is *doubly differentiable in quadratic mean* (DDQM) at $\theta \in \Theta$ if for any sequences $h, \tilde{h} \rightarrow 0$, we have

$$
\int\left(\sqrt{p_{\theta+h}}-\sqrt{p_{\theta+\tilde{h}}}-\frac{1}{2}(h-\tilde{h})^{T} \hat{\ell}(\theta+\tilde{h}) \sqrt{p_{\theta+\tilde{h}}}\right)^{2} \, d\mu = o\left(\|h-\tilde{h}\|^{2}\right). \tag{1}
$$

Note that DDQM reduces to DQM in the special case $\tilde{h} = 0$, and that (by symmetry) we could replace $\hat{\ell}(\theta+\tilde{h}) \sqrt{p_{\theta+\tilde{h}}}$ by $\hat{\ell}(\theta+h) \sqrt{p_{\theta+h}}$. On the other hand it is strictly stronger than DQM at $\theta$ (see Example A.2 in the Appendix). See Appendix A.1 for more details.

**Theorem 2.9.** Let $\Theta$ be a model that is DDQM at some $\theta$, and further let $h_n$, $\tilde{h}_n \rightarrow 0$ be sequences such that $k = \lim_{n} n^{1/2}\left(h_n - \tilde{h}_n\right)$. Then

$$
\begin{aligned}
\ell(\theta + h_n) - \ell(\theta + \tilde{h}_n) &= \frac{k^T}{\sqrt{n}} \hat{\ell}(\theta + \tilde{h}_n) - \frac{1}{2} k^T I(\theta) k + o_p(1) \\
&\longrightarrow^d N \left( -\frac{1}{2} k^T I(\theta) k, k^T I(\theta) k \right).
\end{aligned}
$$

The proof is given in Appendix A.1. The theorem shows that it is not possible to distinguish between the two models as $n$ grows if $k = 0$, that is, if the difference in the alternatives shrinks at a rate faster than $n^{-1/2}$. The geometry of the model determines the relationship between the rate at which $h_n$, $\tilde{h}_n$ shrink and the size of $\tilde{h}_n - h_n$; in general $\|\tilde{h}_n - h_n\|$ may be of smaller order than both $\|h_n\|$ and $\|\tilde{h}_n\|$.

This leads to our first main result about $c$-equivalence, which is a direct application of its definition.

**Theorem 2.10.** Suppose $S_1$, $S_2$ are $c$-equivalent sets at $x$, and consider $h_n = O(n^{-\frac{1}{2c}})$ with $x + h_n \in S_1$. There exists $\tilde{h}_n$ with $x + \tilde{h}_n \in S_2$ such that $\sqrt{n}(h_n - \tilde{h}_n) \rightarrow 0$.

This result is proved in Appendix A.2. Combining the previous two theorems gives the following useful corollary.

Corollary 2.11. Let $\Theta$ be a model that is $D D Q M$ at some $\theta$, and $\mathcal{M}_{1}, \mathcal{M}_{2} \subset \Theta$ be submodels. If $\mathcal{M}_{1}, \mathcal{M}_{2}$ are c-equivalent (respectively c-near-equivalent) at $\theta$ then they cannot be asymptotically distinguished under local alternatives to $\theta$ of order $O\left(n^{-\frac{1}{2 c}}\right)$ (respectively $o\left(n^{-\frac{1}{2 c}}\right)$ ).

All models that intersect are 1-near-equivalent, and therefore we recover the usual parametric rate: we have power only if $h_{n}$ shrinks at $n^{-1 / 2}$ or slower. For 1-equivalent models this is not enough: a rate of $n^{-1 / 2}$ will be too fast for us to tell whether our parameters are in $\mathcal{M}_{1}$ or $\mathcal{M}_{2}$. In practice, regular models that are 1-equivalent are also 2-near-equivalent, so any rate quicker than $n^{-1 / 4}$ is also too fast.

# 2.4 Convexity 

A second consequence of having 1-equivalent regular models is that it is not possible to have a parameterization with respect to which both models are convex; in fact, this is true even under the weaker assumption of overlap. Some automatic model selection methods such as the lasso (Tibshirani, 1996) rely on a convex parameterization, usually constructed by ensuring that interesting submodels correspond to coordinate zeroes (e.g. $\theta_{1}=0$ ). Such selection methods cannot be directly applied to model classes that contain overlapping models.

Theorem 2.12. Suppose $\mathcal{M}_{1}$ and $\mathcal{M}_{2}$ are distinct models that overlap at a point $\theta$ on their relative interiors. Then there is no parameterization with respect to which both these models are convex in a neighbourhood of $\theta$.

Proof. This is just a statement about sets under differentiable maps with differentiable inverses; note that tangent cones and spaces are isomorphically preserved under such transformations. We will prove the contrapositive: if two sets $C, D$ with $x \in C \cap D$ are convex (in a neighbourhood of $x$ ) then they do not overlap at $x$.

The affine hull of any convex set $C$ is the unique minimal affine space $A$ containing $C$. Furthermore, by definition of the relative interior, for every $x \in C^{\text {int }}$ there is a neighbourhood of $x$ in which $C$ and $A$ are identical, i.e. $C$ coincides with the affine space $A$ at $x$.

Now, suppose two sets $C$ and $D$ are both convex and $x \in C^{\text {int }} \cap D^{\text {int }}$. Then they coincide with affine spaces say $A, B$ and hence are their own tangent spaces at $x$. This implies that $C \cap D$ coincides with the affine space $A \cap B$, and hence the tangent cone of $C \cap D$ is just $A \cap B$. Hence $C$ and $D$ do not overlap. Since isomorphic maps cannot alter the tangent cones of these sets, this is true regardless of the parameterization chosen.

Intuitively, one can reparameterize a regular model such that (at least locally to some point $\theta)$ the model is convex. However, this cannot be done simultaneously for two overlapping models. This is illustrated in Figure 4. The result fails if $\theta$ is not required to be a point on the relative interior, a counterexample being models $\mathcal{M}_{1}=\left\{\theta_{2} \geq \theta_{1}^{2}\right\}$ and $\mathcal{M}_{2}=\left\{\theta_{2} \leq-\theta_{1}^{2}\right\}$ with $\theta=(0,0)$.

Remark 2.13. Many convex methods, including the lasso, proceed by optimizing a convex function over a parameter space containing all submodels of interest. In the case of the lasso, this function has 'cusps' on submodels of interest that lead to a non-zero probability that the optimum lies exactly on the model. Theorem 2.12 shows that such a procedure cannot be convex if the class contains overlapping models, since the submodels themselves cannot be made convex. Any submodel that is not convex cannot represent a cusp in a convex function, and therefore we cannot obtain a non-zero probability of selecting such a model.

The nature of this impossibility result should perhaps not be surprising, since all versions of the lasso in the context of ordinary linear models place a restriction on the collinearity of the different parameters in the form of restricted isometry properties or similar (for an overview see, for example, Bühlmann and van de Geer, 2011). In the case of 1-equivalent models, as we move closer to the point of intersection the angle between the two models shrinks to zero, so no such property could possibly hold. For models that overlap the problem is similar, but

![img-3.jpeg](img-3.jpeg)

Figure 4: Cartoon illustrating why overlapping models cannot be made locally convex. In (a) the red and blue models intersect at a non-zero angle and so the parameterization can be smoothly transformed to make the models locally linear. In (b) there is no angle between the models, and this fact is invariant in any smooth reparameterization.

may only apply as we approach from certain directions. The result implies, in particular, that an algorithm such as the lasso cannot be used directly to learn Bayesian networks, whether Gaussian or discrete. We expand upon this in Section 4.

If a class of models is non-convex when parameterized in a canonical way, it may be possible to reparameterize so that they are all convex, but *only if* no two models overlap. For example, suppose we are interested in Gaussian models of marginal independence; that is, models defined by the pattern of zeroes in the off-diagonal elements of the covariance matrix. The log-likelihood of a multivariate Gaussian with zero mean and covariance matrix $\Sigma$ is

$$
\ell(\Sigma;S) = \frac{n}{2} \left\{ \log \det \Sigma^{-1} - \operatorname{tr}(S\Sigma^{-1}) \right\},
$$

where $S$ is the sample covariance matrix and $n$ is the sample size. This is a simple function of the inverse covariance matrix $\Sigma^{-1}$—the canonical parameter for this exponential family—but a complicated function of the mean parameter $\Sigma$. Indeed, while the log-likelihood is a convex function of $\Sigma^{-1}$, it is typically not as a function of $\Sigma$ (see Zwiernik et al., 2017, for an overview of related problems).

However, if we are prepared to accept some loss of efficiency, there is nothing to stop us estimating $\Sigma$ via a moment matching approach, such as by solving the convex program:

$$
\hat{\Sigma} = \arg\min\_{\Sigma > 0} \left\{ \|\Sigma - S\|^2 + \nu \sum\_{i<j} |\sigma\_{ij}| \right\};
$$

here $\Sigma > 0$ denotes that $\Sigma$ belongs to the convex set of positive definite symmetric matrices. If the penalty $\nu$ is chosen to grow at an appropriate rate ($n^{\delta}$ for some $\frac{1}{2} < \delta < 1$) then under some conditions on the Fisher information for $\Sigma$, this will still be consistent for model selection (see, for example, Rocha et al., 2009, Theorem 5).

## 3 Submodels, Equivalence and Overlap

In this section we consider sufficient conditions for models to be $c$-equivalent or to overlap. We will see that it is often a consequence of having models whose intersections are themselves expressible as a union of two or more distinct models. Let $\mathcal{M}$ be an algebraic model that can be written as $\mathcal{M} = V_1 \cup V_2$ for incomparable algebraic submodels $V_1$ and $V_2$; in this case we say $\mathcal{M}$ is *reducible*, and otherwise *irreducible*.

# 3.1 Identifying $c$-equivalence 

For the example in Figure 2, the 1-equivalence of the two models $\mathcal{M}_{1}=\{\Pi: X \Perp Y\}$ and $\mathcal{M}_{2}=\{\Pi: X \Perp Y \mid Z\}$ was closely related to the fact that if either $X \Perp Z$ or $Y \Perp Z$ holds, then $\mathcal{M}_{1}$ and $\mathcal{M}_{2}$ intersect. This means that their intersection is a reducible model, as it can be non-trivially expressed as the union of two or more models. It follows that at any points where both the submodels $\mathcal{M}_{X \Perp Z}$ and $\mathcal{M}_{Y \Perp Z}$ hold, the two original models are 1-equivalent. This is because any direction in $\mathcal{M}_{1}$ (or $\mathcal{M}_{2}$ ) away from the point of intersection $\mathcal{M}_{1} \cap \mathcal{M}_{2}$ can be written as a linear combination of (limits of) vectors that lie in one of $\mathcal{M}_{X \Perp Z}$ or $\mathcal{M}_{Y \Perp Z}$; the partial derivatives of the distance between $\mathcal{M}_{1}$ and $\mathcal{M}_{2}$ in these directions are zero, and so any directional derivative of this quantity is also zero. This is illustrated in Figure 3(a), which shows two surfaces intersecting along two lines: in directions that are diagonal to these lines, the two surfaces separate at a rate that is at most quadratic.

It is not necessary for models to intersect in this manner in order to be 1-equivalent: for example, the surfaces $z=0$ and $z=x^{2}+y^{2}$ intersect only at the point $(0,0,0)$ (see Figure 3(b)). However, many models that are 1-equivalent do intersect along at least two submodels, including most of the substantive examples that we are aware of; the time series models in Section 5.2 are an exception. If $c>2$ submodels are involved in the intersection, then we will see that the original models are $c$-near-equivalent and asymptotic rates for local alternatives will be even slower than $n^{-1 / 4}$.

To formalize this, we use the next result. Define the normal space of a $D^{1}$ surface $\mathcal{M}$ to be the orthogonal complement of its tangent space, $\mathrm{T}_{\theta}(\mathcal{M})^{\perp}$.

Theorem 3.1. Suppose $\mathcal{M}_{1}, \mathcal{M}_{2}$ and $\mathcal{N}_{1}, \ldots, \mathcal{N}_{m}$ are $D^{m}$ manifolds all containing a point $\theta$, and such that $\mathcal{N}_{i} \cap \mathcal{M}_{1}=\mathcal{N}_{i} \cap \mathcal{M}_{2}$ for $i=1, \ldots, m$. Suppose also that $\mathrm{T}_{\theta}\left(\mathcal{N}_{i} \cap \mathcal{M}_{j}\right)=$ $\mathrm{T}_{\theta}\left(\mathcal{N}_{i}\right) \cap \mathrm{T}_{\theta}\left(\mathcal{M}_{j}\right)$ for each $i=1, \ldots, m$ and $j=1,2$, and further that the normal vector spaces $\mathrm{T}_{\theta}\left(\mathcal{N}_{1}\right)^{\perp}, \ldots, \mathrm{T}_{\theta}\left(\mathcal{N}_{m}\right)^{\perp}$ all have linearly independent bases. Then $\mathcal{M}_{1}$ and $\mathcal{M}_{2}$ are $m$-near-equivalent at $\theta$.

Note that an algebraic set is always a $D^{m}$ manifold within a ball around a regular point. In words, there are $m$ distinct submodels on which $\mathcal{M}_{1}$ and $\mathcal{M}_{2}$ intersect; in order to distinguish between $\mathcal{M}_{1}$ and $\mathcal{M}_{2}$, we need to 'move away' from all the submodels $\mathcal{N}_{i}$. Linear independence of the normal spaces ensures that we cannot move directly away from several submodels at once.

Proof. See the Appendix section A.3.
Perhaps an easier way to think about the normal vector spaces is in terms of the submodels being defined by 'independent constraints'; in particular, by constraints defined on different parts of the model. If $\mathcal{N}_{1}$ is defined by the set of points that are zeros of the functions $f_{1}, \ldots, f_{k}$, then $\mathrm{T}_{\theta}\left(\mathcal{N}_{1}\right)^{\perp}$ contains the space spanned by the Jacobian $J\left(f_{1}, \ldots, f_{k}\right)$. If $\mathcal{N}_{2}$ is similarly defined by $g_{1}, \ldots, g_{l}$ then the condition is equivalent to saying that the Jacobian of all $k+l$ functions has full rank $k+l$ at $\theta$.

Example 3.2 (Discriminating Paths). The graphs in Figures 5(a) and (b) are examples of ancestral graphs, which will be introduced more fully in Section 4. Both these graphs are associated with probabilistic models in which $X_{1} \Perp X_{3}$, but in the case of (a) we also have $X_{1} \Perp X_{4} \mid X_{2}, X_{3}$, whereas (b) implies $X_{1} \Perp X_{4} \mid X_{2}$.

In other words, for multivariate Gaussian distributions, both models imply $\rho_{13}=0$, and (b) gives $f_{b}(\Pi)=\rho_{14}-\rho_{12} \rho_{24}=0$, whereas (a) has

$$
\begin{aligned}
f_{a}(\Pi)=\rho_{14}-\rho_{12} \rho_{24}-\rho_{13} \rho_{34}+\rho_{12} \rho_{34} \rho_{23}+\rho_{13} \rho_{24} \rho_{23}-\rho_{14} \rho_{23}^{2} & =0 \\
\rho_{14}-\rho_{12} \rho_{24}+\rho_{12} \rho_{34} \rho_{23}-\rho_{14} \rho_{23}^{2} & =0
\end{aligned}
$$

(Recall that $\Pi$ is the correlation matrix for the model.) Note that $f_{a}(\Pi)=f_{b}(\Pi)+O\left(\|\Pi-I\|^{3}\right)$ when $\rho_{13}=0$, which strongly suggests these models should be 3 -near-equivalent at $\Pi=I$.

![img-4.jpeg](img-4.jpeg)

Figure 5: (a) and (b) are two graphs that differ only by the arrow heads present at 3. (c) A discriminating path of length $k$.

Indeed, if any of the three edges between the pairs $(1,2),(2,3)$ and $(3,4)$ are removed, then the models do become Markov equivalent—that is, they represent the same conditional independences and therefore are identical. In the case of multivariate Gaussian distributions this corresponds to any of the (partial) correlations $\rho_{12}, \rho_{23}$ or $\rho_{34 \cdot 12}$ being zero. Applying Theorem 3.1 shows that these models are 3 -near-equivalent at points where all variables are independent.

This example can be expanded to arbitrarily long discriminating paths of the kind shown in Figure 5(c): these differ only by the edges incident to the vertex $k$, and this makes them distinguishable. However, if any of the edges $(i, i+1)$ for $i=1, \ldots, k$ are missing, the submodels are Markov equivalent, and hence the Gaussian graphical models are $k$-near-equivalent. This means that the 'discrimination' between different models that is theoretically possible may be quite limited in practice, absent extraordinarily large sample sizes. We provide a simulation study to illustrate this in Section 4.3.

This example has serious ramifications for the FCI (fast causal inference) algorithm, which uses discriminating paths to orient edges (Zhang, 2008). It suggests only very strong dependence will allow an unambiguous conclusion to be reached for moderate to long paths.

# 3.2 Identifying Overlap 

Overlap between two regular models occurs when their intersection is not itself a regular model, but rather a union of such models. Unlike with $c$-equivalence, there is no requirement that normal spaces be linearly independent-incomparability is enough.

Theorem 3.3. Let $\mathcal{M}_{1}$ and $\mathcal{M}_{2}$ be algebraic models, regular at some $\theta \in \mathcal{M}_{1} \cap \mathcal{M}_{2}$, and suppose that $\mathcal{M}_{1} \cap \mathcal{M}_{2}$ is reducible into two (or more) further models that have incomparable tangent cones at $\theta$. Then the models $\mathcal{M}_{1}$ and $\mathcal{M}_{2}$ overlap at $\theta$.

This condition is similar in spirit to Theorem 3.1, but note that here we do not require the normal vector spaces of the two submodels to be linearly independent at the point of intersection, only that the tangent spaces of those pieces are incomparable.

Proof. Let $\mathcal{M}_{1} \cap \mathcal{M}_{2}=V_{1} \cup V_{2}$ be the reduction into submodels. Taking $\theta \in V_{1} \cap V_{2}$, note that $\mathrm{C}_{\theta}\left(\mathcal{M}_{1} \cap \mathcal{M}_{2}\right)=\mathrm{C}_{\theta}\left(V_{1} \cup V_{2}\right)=\mathrm{C}_{\theta}\left(V_{1}\right) \cup \mathrm{C}_{\theta}\left(V_{2}\right)$, the second equality following from the definition of a tangent cone. Now, since $V_{1}, V_{2} \subseteq \mathcal{M}_{1}$ and $\mathcal{M}_{1}$ is regular at $\theta$, this implies that any vector in $\mathrm{C}_{\theta}\left(V_{1}\right)+\mathrm{C}_{\theta}\left(V_{2}\right)$ is contained in $\mathrm{C}_{\theta}\left(\mathcal{M}_{1}\right)$; similarly for $\mathcal{M}_{2}$. Therefore the condition for not overlapping,

$$
\mathrm{C}_{\theta}\left(\mathcal{M}_{1} \cap \mathcal{M}_{2}\right)=\mathrm{C}_{\theta}\left(\mathcal{M}_{1}\right) \cap \mathrm{C}_{\theta}\left(\mathcal{M}_{2}\right)
$$

holds only if $\mathrm{C}_{\theta}\left(V_{1}\right)+\mathrm{C}_{\theta}\left(V_{2}\right) \subseteq \mathrm{C}_{\theta}\left(V_{1}\right) \cup \mathrm{C}_{\theta}\left(V_{2}\right)$. This occurs only if one of $\mathrm{C}_{\theta}\left(V_{1}\right)$ or $\mathrm{C}_{\theta}\left(V_{2}\right)$ is a subspace of the other, but this was ruled out by hypothesis.

Example 3.4. As already noted in Examples 1.2 and 2.4, the Gaussian graphical models defined respectively by the independences $\mathcal{M}_{1}: X \perp Y$ and $\mathcal{M}_{2}: X \perp Y \mid Z$ are 1equivalent at diagonal covariance matrices, but the corresponding discrete models are not. This is because-taking $X, Y, Z$ to be binary-the three-way interaction parameter

$$
\lambda_{X Y Z} \equiv \frac{1}{8} \sum_{x, y, z \in\{0,1\}}(-1)^{|x+y+z|} \log P(X=x, Y=y, Z=z)
$$

is zero in the conditional independence model ${ }^{6}$, but essentially unrestricted in the marginal independence model. However, the intersection of $\mathcal{M}_{1}$ and $\mathcal{M}_{2}$ for binary $X, Y, Z$ is the set of distributions such that either $X \perp Y, Z$ or $Y \perp X, Z$, and these correspond respectively to the submodels

$$
\lambda_{X Y}=\lambda_{X Z}=\lambda_{X Y Z}=0 \quad \text { or } \quad \lambda_{X Y}=\lambda_{Y Z}=\lambda_{X Y Z}=0
$$

also defined by zeros of polynomials in $P$ (see Appendix B for full definitions). These models satisfy the conditions of Theorem 3.3 at points of total independence $\perp\{X, Y, Z\}$, and therefore $\mathcal{M}_{1}$ and $\mathcal{M}_{2}$ do overlap.

# 4 Directed and Ancestral Graph Models 

In this section we focus on two classes of graphical models: Bayesian network models, and the more general ancestral graph models. A more detailed explanation of the relevant theory can be found in Spirtes et al. (2000) and Richardson and Spirtes (2002).

### 4.1 Ancestral Graphs

A maximal ancestral graph (MAG) is a simple, mixed graph with three kinds of edge, undirected $(-)$, directed $(\rightarrow)$ and bidirected $(\leftrightarrow)$. Special cases of ancestral graphs include directed acyclic graphs, undirected graphs and bidirected graphs, but not chain graphs. There are some technical restrictions on the structure of the graph which we omit here for brevity: the key detail is that - under the usual Markov property - the model implies a conditional independence constraint between each pair of vertices if (and only if) they are not joined by any sort of edge in the graph (Richardson and Spirtes, 2002). The set that needs to be conditioned upon to obtain the independence depends on the presence of colliders in the graph. A collider is a pair of edges that meet with two arrowheads at a vertex $k$ : for example, $i \rightarrow k \leftarrow j$ or $i \rightarrow k \leftrightarrow j$. Any other configuration is called a noncollider. We say the collider or noncollider is unshielded if $i$ and $j$ are not joined by an edge.

The special case of an ancestral graph model in which all edges are directed yields a Bayesian network (BN) model, widely used in causal inference and in machine learning (Bishop, 2007; Pearl, 2009). The additional undirected and bidirected edges allow MAGs to represent the set of conditional independence models generated by marginalizing and conditioning a BN model. Ancestral graphs are therefore useful in causal modelling, since they represent the conditional independence model implied by a causal structure with hidden and selection variables.

Example 4.1. Consider the maximal ancestral graphs in Figure 5(a) and (b). The graph in (a) is fully directed and represents the model defined by the conditional independences:

$$
X_{1} \perp X_{3}, \quad X_{1} \perp X_{4} \mid X_{2}, X_{3}
$$

[^0]
[^0]:    ${ }^{6}$ This is equivalent to $\prod_{x+y+z \text { even }} p(x, y, z)=\prod_{x+y+z \text { odd }} p(x, y, z)$, and so certainly still a polynomial condition.

The graph in (b), on the other hand, represents

$$
X_{1} \pm X_{3}, \quad X_{1} \pm X_{4} \mid X_{2}
$$

The difference in the conditioning sets above is due to the fact that $2 \leftarrow 3 \rightarrow 4$ is a noncollider in the first graph, but a collider in the second: $2 \leftrightarrow 3 \leftrightarrow 4$.

An independence model, $\mathcal{I}$, is a collection of (conditional) independence statements of the form $X_{i} \pm X_{j} \mid X_{C}$, for $i \neq j$ and possibly empty $C$. We will say $\mathcal{I}$ is simple if it can be written so that it contains at most one independence statement for each unordered pair $\{i, j\}$. If there is no independence statement between $X_{i}, X_{j}$ in a simple independence model, we say $i$ and $j$ are adjacent.

Theorem 4.2. Let $\mathcal{I}_{1}, \mathcal{I}_{2}$ be simple independence models on the space of $p \times p$ Gaussian covariances matrices. Then the two models are 2-near-equivalent if they have the same adjacencies.

Further, if the two models have different adjacencies then they are 1-equivalent on at most a null set within any parametric independence model.

Proof. Let $E$ denote the set of adjacencies in a simple independence model $\mathcal{I}$. Parameterizing using the set of correlation matrices, we will show that the tangent space of $\mathcal{I}$ at the identity matrix $I$ is

$$
T_{I}(\mathcal{I})=\bigoplus_{\substack{i<j \\\{i, j\} \in E}} D^{i j}
$$

where the matrices $D^{i j}$ have zeroes everywhere except in the $(i, j)$ and $(j, i)$ th entries, which are 1 .

If $\{i, j\} \in E$ it is easy to see that $I+\lambda D^{i j}$ is in the model for all $\lambda \in(-1,1)$, since this means that all conditional independences except those between $X_{i}$ and $X_{j}$ hold; hence $D^{i j} \in T_{I}(\mathcal{I})$. Conversely, if $i$ and $j$ are not adjacent, then some independence restriction $X_{i} \pm X_{j} \mid X_{C}$ holds, so

$$
f(\Pi)=\Pi_{i j}-\Pi_{i C}\left(\Pi_{C C}\right)^{-1} \Pi_{C j}=0
$$

The derivative of $f$ at $\Pi=I$ is just $D^{i j}$, so it follows that $D^{i j} \notin T_{I}(\mathcal{I})$. Hence the tangent space at $I$ is in the form (2). By Proposition 2.3, the models are 1-equivalent, and since these constraints are linearly independent at $\Pi=I$, they are regular and therefore also 2 -near-equivalent.

Conversely, suppose that there is some pair $i, j$ subject to the restriction $X_{i} \pm X_{j} \mid X_{C}$ in $\mathcal{I}_{1}$ but not to any such restriction in $\mathcal{I}_{2}$. By the above analysis, these models have distinct tangent spaces at $\Pi=I$. Since these are models defined by polynomials in $\Pi$, the set of points on which the tangent spaces are identical (say $W$ ) is an algebraic model; its intersection with any irreducible model $V$ is therefore either equal to $V$ or of strictly smaller dimension than $V$ (indeed this follows from the usual definition of dimension in such sets; see Bochnak et al. (2013, Section 2.8)). However, if the identity matrix is contained in $V$ then clearly $W \cap V \subset V$, since we have established that the tangent spaces do not intersect at the identity. Hence $W \cap V$ has smaller dimension, and is a null subset of $V$.

Corollary 4.3. Two Gaussian maximal ancestral graph models are 2-near-equivalent if they have the same adjacencies (when viewed either as an independence model or a graph), and are otherwise 1-equivalent almost nowhere on any submodel of independence.

Proof. This follows from the pairwise Markov property of Richardson and Spirtes (2002).
We conjecture that, in fact, two ancestral graph models of the form given in Theorem 4.2 will overlap nowhere in the set of positive definite correlation matrices if they do not share the same adjacencies (rather than almost nowhere). It is not hard to see that this holds for

models of different dimension, since these models are regular and therefore will share this dimension everywhere. To prove it in general seems challenging; the result above is sufficient for most practical purposes.

Corollary 4.4. Let $\mathcal{G}, \mathcal{H}$ be chain graphs with the same adjacencies under any of the interpretations given in Drton (2009b) (not necessarily the same interpretation). Then the corresponding models are 2-near-equivalent.

Note that Remark 5 of Drton (2009b) makes clear that pairwise independences are sufficient to define Gaussian chain graph models.

# 4.2 Discrete Data 

The picture is slightly rosier if we consider discrete data instead. A well known result of Chickering (1996) shows that finding an optimal Bayesian Network for discrete data is an NP-hard problem; in other words, it is computationally difficult. However, we find that from a statistical point of view, it is somewhat easier than in the Gaussian case.

Theorem 4.5. No two distinct, binary, maximal ancestral graph models are 1-equivalent at the model of total independence.

Proof. See the Appendix, Section C.
Although distinct, discrete MAG models (and therefore BN models) are never 1-equivalent, they do still overlap, as our next result demonstrates.

Proposition 4.6. Let $\mathcal{M}\left(\mathcal{G}_{1}\right), \mathcal{M}\left(\mathcal{G}_{2}\right)$ be two discrete Bayesian network models such that $i \rightarrow k \leftarrow j$ is an unshielded collider in $\mathcal{G}_{1}$ but an unshielded noncollider in $\mathcal{G}_{2}$. Then, if $X_{k}$ is binary, the two models overlap.

Proof. See the Appendix, Section C.
Remark 4.7. The condition that some variables are binary is, in fact, unnecessary-see Remark C. 2 for more details on the general finite discrete case.

Bayesian network models that are consistent with a single topological ordering of the vertices do not overlap, because their intersection is always another BN model. We can therefore work with a class defined by the subgraphs of a single complete BN in order to avoid the problems associated with overlap.

This leads to the question of whether any other, perhaps larger, subclasses share this property. The previous result shows that any such subclass would be restricted fairly severely, since any two graphs must never disagree about a specific unshielded collider. Note that the result does not imply that it is necessary for graphs to be consistent with a single topological order in order for the corresponding models not to overlap; the graphs in Figure 6(a) and (b) provide a counterexample to this.

The easiest way to ensure that a class of models does not overlap at the independence model is to associate each potentially missing edge with a single constraint using a pairwise Markov property, as with the set of BN models that are consistent with a given topological order, or the set of undirected graph models.

Note that Proposition 4.6 and Theorem 2.12 combine to show that the impossibility result discussed in Remark 2.13 applies to binary Bayesian networks, and we will never be able to use a lasso-like method to consistently select from this class under standard conditions.

![img-5.jpeg](img-5.jpeg)

Figure 6: (a) and (b) two Bayesian networks which do not overlap but are not consistent with a single topological order. (c) A simple causal model.

### 4.3 Discriminating Paths

Example 3.2 introduced the notion of a discriminating path, which allows the identification of colliders in an ancestral graph. Formally, define the ancestral graphs $\mathcal{G}_k$ and $\mathcal{G}_k^0$ as having vertices 1, ..., k + 1, with a path 1 ↔ 2 ↔ ... ↔ k and directed edges from each of 2, ..., k − 1 to k + 1. In addition, $\mathcal{G}_k$ has the edges k ↔ k + 1, while $\mathcal{G}_k^0$ has k → k + 1; the graphs are shown in Figure 5(c), with only the final edge left ambiguous. The path from 1 to k + 1 is known as a discriminating path, and its structure allows us to determine whether there is a collider at k (as in $\mathcal{G}_k$) or not (as in $\mathcal{G}_k^0$).

As noted already, if any of the edges i ↔ i + 1 for i = 1, ..., k − 1 are missing (i.e., if X<sub>i</sub> ⊥ X<sub>i+1</sub>), then the two models coincide. In addition, if the final edge between k and k + 1 is missing (so X<sub>k+1</sub> ⊥ X<sub>k</sub> | X<sub>1</sub>, ..., X<sub>k−1</sub>), the two models coincide. We consider the Gaussian graphical models associated with these graphs and, by application of Theorem 3.1, the two ancestral graph models for $\mathcal{G}_k$ and $\mathcal{G}_k^0$ are k-near-equivalent at points where these additional independences hold.

We now perform a small simulation to show that, in order to maintain power as the effect sizes shrink, the sample sizes need to grow at the rates claimed in Corollary 2.11. To do this, we take the structural equation model parameterization from Richardson and Spirtes (2002, Section 8); for $\mathcal{G}_k$ we set the weight of each edge on the discriminating path to be ρ<sub>s</sub> = 0.4 × 2<sup>−s</sup>, and of the other edges to be 0.5. We take a sample size of n<sub>init</sub> × 2<sup>2k</sup> for some n<sub>init</sub>, so that this grows at the rate suggested by Corollary 2.11 to keep the power constant in s. The plot in Figure 7 shows that the simulations agree with the predictions of that result, since the power stays roughly constant as s grows.

Table 1 lists some of the colossal sample sizes that are needed to keep power constant in longer discriminating paths as effect sizes shrink. In the k = 3 case, we have approximately 70% accuracy when ρ = 0.2 and n = 16 000, but to maintain this when ρ = 0.1 we need n = 1 024 000. For k = 4 the respective sample sizes are an increase from n = 2 × 10<sup>5</sup> to n = 5 × 10<sup>7</sup> (a 256-fold increase), and for k = 5 from n = 5 × 10<sup>6</sup> to n = 5 × 10<sup>9</sup> (a 1024-fold increase).

# 5 Other Classes of Model

### 5.1 Undirected Graphs

An undirected graphical model associates a simple undirected graph with a collection of probability distributions. Under the pairwise Markov property, the model consists of distributions such that X<sub>i</sub> ⊥ X<sub>j</sub> | X<sub>V \{i,j\}} whenever i and j are not joined by an edge in the graph. For Gaussian graphical models, this is equivalent to enforcing a zero in the (i, j) entry in the inverse covariance matrix. It is a simple matter to see that no two distinct undirected Gaussian graphical models ever overlap.

This helps to explain why undirected models are fundamentally easier to learn than other classes, something which has been much exploited in high-dimensional statistics. For ex-

![img-6.jpeg](img-6.jpeg)

Figure 7: Ability to discriminate between $\mathcal{G}_{k}$ and $\mathcal{G}_{k}^{\prime}$ for various $k$ and $s$. A sample of 2,500 data sets were drawn from the Gaussian graphical model according to the scheme described in the text, with effect sizes $\rho_{s}=0.4 \times 2^{-s}$; the sample size was fixed at $n_{\text {init }} \times 2^{2 k s}$ for some $n_{\text {init }}$. The $y$-axis gives the proportion of times $\mathcal{G}_{k}$ correctly gave a lower deviance than $\mathcal{G}_{k}^{\prime}$. Each solid line corresponds to a value of $k \in\{2,3,4,5\}$ and a corresponding sample size $n_{\text {init }} \in\{32,250,800,5000\}$ (dashed lines correspond to an initial sample size of $4 n_{\text {init }}$ ). The flattening out each line shows agreement with the prediction of Corollary 2.11. Note that the vertical ordering of the different lines is merely a function of the choice of $n_{\text {init }}$. Larger values of $k$ and $s$ were excluded because the relevant sample sizes grew too quickly ( $k=s=5$ corresponds to $n=5.6 \times 10^{18}$ for the solid line).


Table 1: Table giving effect sizes $\rho_{s}$ and sample sizes used in each of the graphs $\mathcal{G}_{k}$ for $k=2,3,4,5$, and corresponding to the solid lines in Figure 7. For $k=4,5$ the sample sizes grow extremely quickly, and some larger entries are excluded because they led to numerical problems. 'acc.' gives the proportion of runs for which the correct graph was selected.
ample, the graphical lasso (Friedman et al., 2008; Witten et al., 2011) and neighbourhood selection (Meinshausen and Bühlmann, 2006) methods allow very fast consistent model selection amongst undirected Gaussian graphical models, including in high-dimensional settings.

# 5.2 Time Series 

The autoregressive moving average process of order $(p, q)$, or $\operatorname{ARMA}(p, q)$ model, is a time series model that assumes

$$
X_{t}=\varepsilon_{t}+\sum_{i=1}^{p} \phi_{i} X_{t-i}+\sum_{i=1}^{q} \theta_{i} \varepsilon_{t-i}, \quad t \in \mathbb{Z}
$$

where $\varepsilon_{t} \stackrel{\text { i.i.d. }}{=} N\left(0, \sigma^{2}\right)$ and the parameters $\boldsymbol{\phi}=\left(\phi_{i}\right)_{i=1}^{p}$ and $\boldsymbol{\theta}=\left(\theta_{i}\right)_{i=1}^{q}$ are unknown. The model is stationary and Gaussian, and therefore parameterized by $\sigma^{2}$ and the autocorrelations: i.e. $\gamma_{i} \equiv \operatorname{Cor}\left(X_{t}, X_{t+i}\right)$ for $i=1,2, \ldots$. Let the space spanned by $\gamma_{i}$ be $L^{i}$.

The special cases where $p=0$ and $q=0$ are respectively the $\operatorname{MA}(q)$ and $\operatorname{AR}(p)$ models. These are identifiable, and the unique parameter values that lead to independence of the $X_{t} \mathrm{~s}$ are $(\boldsymbol{\phi}, \boldsymbol{\theta})=(\mathbf{0}, \mathbf{0})$. It is not hard to see that the derivative of the joint correlation matrix with respect to either $\phi_{i}$ or $\theta_{i}$ is just $L^{i}$. Hence the tangent space of an $\operatorname{AR}(p)$ or $\operatorname{MA}(p)$ model at this point is of the form

$$
\mathrm{C}_{(\mathbf{0}, \mathbf{0})}\left(\mathcal{M}_{p}\right)=\bigoplus_{i=1}^{p} L^{i}
$$

and so the two $\operatorname{AR}(p)$ and $\operatorname{MA}(p)$ models are 1-equivalent at the point of joint independence. This suggests it will be hard to distinguish between these two types of process when correlations are weak - though this may not matter if the aim of an analysis is predictive.

### 5.3 Nested Markov Models

Richardson et al. (2017) introduce nested Markov models, which are defined by a generalized form of conditional independence that may hold under a Bayesian Network model with hidden variables. For example, the two causal Bayesian networks in Figure 8 differ only in the

![img-7.jpeg](img-7.jpeg)

Figure 8: Two causal models on five variables, differing in the direction of the $L-B$ edge. The variable $U$ is assumed to be unobserved.
direction of a single edge (that between $L$ and $B$ ). Assuming that the variable $U$ is unobserved, the model (a) implies a single observable conditional independence constraint: $Y \Perp A \mid B$.

The model in (b) does not imply any conditional independence constraint over the observed variables, but does impose the restriction that

$$
p(y \mid \operatorname{do}(a, b)) \equiv \sum_{l} p(l \mid a) \cdot p(y \mid a, l, b)
$$

does not depend on $a$. This can be interpreted as the statement that $A$ does not causally affect $Y$, except through $B$. Note that, if $L \Perp B \mid A$, then

$$
\begin{aligned}
p(y \mid \operatorname{do}(a, b)) & \equiv \sum_{l} p(l \mid a) \cdot p(y \mid a, l, b) \\
& =\sum_{l} p(l \mid a, b) \cdot p(y \mid a, l, b) \\
& =p(y \mid a, b)
\end{aligned}
$$

so the statement that this quantity does not depend upon $a$ is the same as the ordinary independence statement $Y \Perp A \mid B$; a similar conclusion can be reached if $Y \Perp L \mid A, B$. Thus there are two distinct submodels along which the two models in Figure 8 intersect. These two submodels also have linearly independent normal vector spaces because they correspond to restrictions on $p(a \mid y, b)$ and $p(l \mid a, y, b)$. It follows that the two models are 2 -nearequivalent at points where $Y \Perp A, L \mid B$ (where both submodels hold) by Theorem 3.1; note that unlike for the case of ancestral graph models, this applies even in the case of discrete variables.

So, even though in principle one can distinguish the two models in Figure 8 and determine the orientation of the $L-B$ edge, in practice the distinction may be hard to show with data. This suggests it will be very difficult to learn the correct model without further information, something borne out by the simulations in Shpitser et al. (2013). Interestingly, the approach in that paper of setting higher-order parameters to zero in order to equalize parameter counts between models may actually have made learning significantly harder, since in some cases this means removing the only directions in the tangent space that differ between models.

# 6 Related Phenomena 

### 6.1 Double Robustness

The phenomenon of double robustness of estimators has been exploited to improve estimation in causal models (Scharfstein et al., 1999); see Kang and Schafer (2007) for an overview. The essential element of double robustness is to choose an estimating equation with two components, such that the solution is a $\sqrt{n}$-consistent estimator when one of the two parts is correctly specified, even if the other is misspecified. For simplicity, we will just consider examples where we assume independence rather than fitting a model.

Consider the simple causal model depicted in Figure 6(c), and suppose we are interested in the causal effect of a binary variable $X$ on the expectation of $Y$, but there is a (potentially continuous) measured confounder $Z$. The causal distribution for $X$ on $Y$ is given by $p(y \mid d o(x))=\sum_{z} p(z) \cdot p(y \mid x, z)$; this is generally different from the ordinary conditional $p(y \mid x)=\sum_{z} p(z \mid x) \cdot p(y \mid x, z)$.

What happens if we use the ordinary conditional anyway? One can easily check that $p(y \mid x)=p(y \mid d o(x))$ if either $X \Perp Z$ or $Y \Perp Z \mid X$, and hence the set of distributions where our estimate is correct contains the union of points $\mathcal{M}_{X \Perp Z} \cup \mathcal{M}_{Y \Perp Z \mid X}$. If we apply Theorem 3.1 we find that any error in estimating the causal effect will be quadratic in the distance from the point where $Z \Perp X, Y$.

# 6.2 Triple Robustness 

Another phenomenon known as triple robustness ${ }^{7}$ is observed in some causal models related to mediation (Tchetgen and Shpitser, 2012). In this case, an estimator will be consistent provided at least two out of three other quantities are correctly specified. Here we introduce another result related to Theorem 3.1.

Proposition 6.1. Let $\mathcal{N}_{1}, \ldots, \mathcal{N}_{m}$ be algebraic submodels containing 0 , and let $f$ be a polynomial such that $f(x)=0$ for any $x \in \mathcal{N}_{i} \subset \Theta$ for $i=1, \ldots, m$. Suppose also that the tangent spaces $\mathrm{T}_{0}\left(\mathcal{N}_{i}\right)$ jointly span $\Theta$. Then, $f(x)=O\left(\|x\|^{2}\right)$.

Proof. For any twice differentiable function with $f(0)=0$, whichever direction we move away from 0 in can be written as a linear combination of directions in the tangent spaces of submodels $\mathcal{N}_{i}$. It follows that the directional derivative of any such function is zero, in any direction. Hence $f(x)=O\left(\|x\|^{2}\right)$.

In light of this, suppose we have three submodels $\mathcal{M}_{1}, \mathcal{M}_{2}, \mathcal{M}_{3}$ each defined by constraints on linearly independent parts of the full model $\Theta$, and such that an estimator is consistent on the intersection of any two of them. The condition on the definition of the $\mathcal{M}_{i}$ means that their normal vector spaces are linearly independent, so any vector is in the tangent space of at least two such submodels. Their pairwise intersections thus satisfy the conditions of the theorem, and the error in estimating the relevant parameter is quadratic in the distance to the joint intersection $\mathcal{M}_{1} \cap \mathcal{M}_{2} \cap \mathcal{M}_{3}$.

### 6.3 Post-double-Selection

Belloni et al. (2014) consider the problem of estimating a causal effect $p(y \mid d o(x))$ in the presence of a high-dimensional measured confounder $Z_{I}, I=\{1, \ldots, p\}$ where $p \gg n$. We can try to find a subset $S \subseteq I$ such that $S$ is much smaller than $I$, and $Z_{S}$ is sufficient to control for the confounding, i.e. $p(y \mid d o(x))=\sum_{z_{S}} p\left(z_{S}\right) p\left(y \mid x, z_{S}\right)$. Formally, this will be satisfied if we ignore any $Z_{i}$ such that $Z_{i} \Perp X \mid Z_{-i}$ or $Z_{i} \Perp Y \mid X, Z_{-i}$. However, in finite samples selecting variables creates an omitted-variable bias, in which the decision boundary of whether to drop a particular variable leads to a bias of order $O\left(n^{-1 / 2}\right)$ at some points in the parameter space.

If we only exclude components of $Z_{i}$ for which both $Z_{i} \Perp X \mid Z_{-i}$ and $Z_{i} \Perp Y \mid X, Z_{-i}$, then the order of the bias on our causal estimate is effectively squared and becomes $O\left(n^{-1}\right)$; this is because-for the same reason as in the discussion of double robustness - the bias induced by a component $Z_{i}$ is at most quadratic in the distance of the true distribution from the intersection of these two independences. Since this bias is small compared to the sampling variance, it can effectively be ignored; this idea is referred by Belloni et al. (2014) to as post-double-selection, and can be viewed as another consequence of the local geometry of the model.

[^0]
[^0]:    ${ }^{7}$ Perhaps misleadingly, since it is strictly weaker than double robustness.

# 7 Algorithms for Learning Models with Overlap 

Suppose we have a class of models $\mathcal{M}_{i}$ that overlap but are not 1-equivalent: that is, the models all have different tangent cones. We have seen already that overlapping models place restrictions on one class of computationally efficient methods, because they cannot be made convex. This suggests that a method which attempts to learn the (linear) tangent cone rather than selecting the model directly may be computationally advantageous. This can be achieved by learning from a set of 'surrogate' models that have the same tangent spaces as the original models, but that do not overlap.

To take a simple example, consider again the graphical models in Figure 2 for binary variables. Letting

$$
\lambda_{X Y}=\frac{1}{8} \sum_{x, y, z \in\{0,1\}}(-1)^{|x+y|} \log P(X=x, Y=y, Z=z)
$$

then the model $\mathcal{M}_{2}$ in (b) consists of the zero parameters: $\lambda_{X Y}=\lambda_{X Y Z}=0$, while (a) involves log-linear parameters over the $X, Y$-margin $\mathcal{M}_{1}: \lambda_{X Y}^{\prime}=0$. This apparently makes model selection tricky because some models involve zeroes of ordinary log-linear parameters, and some of marginal log-linear parameters.

However, one could try replacing $\mathcal{M}_{1}$ with a model that corresponds to the zero of the ordinary log-linear parameter, e.g. $\mathcal{M}_{1}^{\prime}: \lambda_{X Y}=0$. This has the same tangent space as $\mathcal{M}_{1}$ at the uniform distribution, and so it is 'close' to $\mathcal{M}_{1}$ in a precise sense. This suggests that if we pursued a model selection strategy for ordinary log-linear parameters and learned $\lambda_{X Y}=0$ but $\lambda_{X Y Z} \neq 0$ (i.e. we chose $\mathcal{M}_{1}^{\prime}$ ), then we could conclude that this is sufficiently similar to $\mathcal{M}_{1}$ to select this model from the graphical class.

### 7.1 Model Selection

Define $\Lambda_{i}=\left\langle e_{i}\right\rangle$ to be the vector space spanned by the $i$ th coordinate axis. Suppose we have a class of regular algebraic models $\mathcal{M}_{i} \subseteq \Theta \subseteq \mathbb{R}^{k}$ such that each model has a tangent space at $\theta=0$ defined by a subset of coordinate axes: that is, for each model there is some set $c\left(\mathcal{M}_{i}\right) \subseteq\{1, \ldots, k\}$ such that

$$
\mathrm{C}_{0}\left(\mathcal{M}_{i}\right)=\bigoplus_{j \in c\left(\mathcal{M}_{i}\right)} \Lambda_{j}
$$

Suppose further that our class of models is such that $c\left(\mathcal{M}_{i}\right) \neq c\left(\mathcal{M}_{j}\right)$ for any $i \neq j$. We have already seen that, if two models overlap, then it may be computationally difficult to learn the correct one due to a lack of convexity. We will show that, under certain assumptions about the true parameter being sufficiently close to $\theta=0$, we can learn the tangent space itself, thereby circumventing the models' lack of convexity.

Denote the sparsity pattern of a parameter by $c(\theta)=\left\{i: \theta_{i} \neq 0\right\}$; then $\theta \in \mathrm{T}_{0}(\mathcal{M})$ implies that $c(\theta) \subseteq c\left(\mathrm{~T}_{0}(\mathcal{M})\right)=c(\mathcal{M})$. However, note that $\theta \in \mathcal{M}$ does not imply this, and in general the sparsity patterns of parameters in $\mathcal{M}$ is arbitrary.

Suppose we have a model selection procedure which returns a set $\hat{S}$ estimating $S \subseteq$ $\{1, \ldots, k\}$ such that $\theta_{S} \neq 0$ and $\theta_{S^{c}}=0$. We will assume that the procedure is consistent, in the sense that if $\theta_{S^{c}}^{n}=o\left(n^{-1 / 2}\right)$ and $\left|\theta_{s}^{n}\right|=\omega\left(n^{-1 / 2}\right)$ for each $s \in S$, we have $P(\hat{S}=S) \rightarrow 1$. These conditions are satisfied by many common model selection methods such as BIC, or an $L_{1}$-penalized selection method with appropriate penalty (and with Fisher information matrix satisfying certain irrepresentability conditions, Nardi and Rinaldo, 2012).

The following result shows that we can adapt a model selection procedure of this kind to learn models that overlap, by replacing each (possibly non-convex) model of interest by a convex surrogate model with the same tangent space.

Theorem 7.1. Consider a sequence of parameters of the form $\theta_{n}=\theta_{0}+n^{-\gamma} h+O\left(n^{-2 \gamma}\right)$ such that each $\theta_{n} \in \mathcal{M}$; here $\frac{1}{4}<\gamma<\frac{1}{2}$ and $h_{i} \neq 0$ for any $i \in c(\mathcal{M})$. Suppose our model selection procedure provides a sequence of parameter estimates $\tilde{\theta}_{n}$.

Then $P\left(c\left(\tilde{\theta}_{n}\right)=c(\mathcal{M})\right) \rightarrow 1$ as $n \rightarrow \infty$.
Proof. If $i \notin c(\mathcal{M})$ then $\theta_{n i}=O\left(n^{-2 \gamma}\right)=o\left(n^{-1 / 2}\right)$ since $\gamma>\frac{1}{4}$, while if $i \in c(\mathcal{M})$ then $\theta_{n i}=\Omega\left(n^{-\gamma}\right)=\omega\left(n^{-1 / 2}\right)$ since $\gamma<\frac{1}{2}$. By the conditions on our model selection procedure then, we have the required consistency.

The condition $\gamma>\frac{1}{4}$ is to ensure that the bias induced by using the surrogate model is too small to detect at the specific sample size, and that our procedure will set the relevant parameters to zero. Slower rates of convergence (i.e. $0<\gamma \leq \frac{1}{4}$ ) could also lead to a satisfactory model selection procedure if we were simply to subsample our data or otherwise 'pretend' that $n$ is smaller than it actually is. If $\gamma>\frac{1}{2}$, on the other hand, we will not have asymptotic power to identify the truly non-zero parameters.

Note that $P\left(c\left(\tilde{\theta}_{n}\right)=c\left(\theta_{n}\right)\right)$ does not tend to 1 , since the sparsity pattern of the true parameter is not the same as that of the tangent space of the model: it is merely 'close' to having the correct sparsity.

The assumption that $\theta_{n}$ tends to 0 at the required rate may seem rather artificial: some assumption of this form is unavoidable, simply because our results only hold in a neighbourhood of points of intersection. The precise rate at which $\theta_{n} \rightarrow 0$ just needs to be such that 'real' effects do not disappear faster than we can statistically detect them (i.e. slower than $n^{-1 / 2} \rightarrow 0$ ), and that any other effects shrink fast enough that they are taken to be zero. Any more realistic framework would require conditions on the global geometry of the models, and would be extremely challenging to verify.

# 7.2 Application to Bayesian Networks 

Suppose that we have a sequence of binary distributions $p_{n}$, with $\left\|p_{n}-p_{0}\right\|=O\left(n^{-\gamma}\right)$ for $\frac{1}{4}<\gamma<\frac{1}{2}$, where $p_{0}$ is the uniform distribution, and such that each $p_{n}$ is Markov with respect to a Bayesian network $\mathcal{G}$; assume also that $\lambda_{i j}=\omega\left(n^{-1 / 2}\right)$ if $i, j$ are adjacent, and $\lambda_{i j k}=\omega\left(n^{-1 / 2}\right)$ if $i \rightarrow k \leftarrow j$ is an unshielded collider. Then a consistent method to determine $\mathcal{G}$ would be as follows:

- select the model for $p_{n}$ using the log-linear lasso with penalty $\nu=n^{\delta}$ for some $\frac{1}{2}<\delta<1$;
- then find the graph. Asymptotically, the sparsity pattern of the log-linear model is the same as that of the original graph, so this can be done by simply finding the graph with skeleton given by $i-j$ when $\lambda_{i j} \neq 0$ and orienting unshielded triples as colliders $i \rightarrow k \leftarrow j$ if and only if $\lambda_{i j k} \neq 0$.

This is far from an optimal approach, but does give an idea of how one might be able to overcome the non-convexity inherent to overlapping models. The algorithm could also be extended to ancestral graphs, via Theorem 4.5.

## 8 Discussion

We have proposed that the geometry of two models at points of intersection is a useful measure of how statistically difficult it will be to distinguish between them, and shown that when models' tangent spaces are not closed under intersection this restricts the possibility of using convex methods to perform model selection in the class. We have also given examples of model classes in which this occurs and noted that in several cases, model selection is indeed known to be difficult.

We suggest that special consideration should be given in model selection problems to whether or not the class contains models that overlap or are 1-equivalent and-if it does-to

whether a smaller and simpler model class can be used instead. Alternatively, additional experiments may need to be performed to help distinguish between models. The results in this paper provide a point of focus for new model selection methods and also for experimental design. If we are able to work with a class of models that is less rich and therefore easier to select from, then perhaps we ought to. If we cannot, it is useful to know in advance at what points in the parameter space it is likely to be difficult to draw clear distinctions between models, so that we can power our experiments correctly or just report that we do not know which of several models is correct.

# Acknowledgments 

We thank Thomas Richardson for suggesting one of the examples, Bernd Sturmfels for pointing out a problem with a version of Theorem 3.1, as well as several other readers for helpful comments. We also acknowledge the very helpful comments of the referees and associate editor.

# A Technical Results 

## A. 1 Asymptotics

We start with the definition of differentiability in quadratic mean.
Definition A.1. Let $\left(p_{\theta}: \theta \in \Theta\right)$ be a class of densities with respect to a measure $\mu$ indexed by some open $\Theta \subseteq \mathbb{R}^{k}$. We say that this class is differentiable in quadratic mean (DQM) at $\theta$ if there exists a vector $\hat{\ell}(\theta) \in \mathbb{R}^{k}$ such that

$$
\int\left[\sqrt{p_{\theta+h}}-\sqrt{p_{\theta}}-\frac{1}{2} h^{T} \hat{\ell}(\theta) \sqrt{p}_{\theta}\right]^{2} d \mu=o\left(\|h\|^{2}\right)
$$

Recall also our definition of a model that is doubly DQM.
Definition 2.8 Say that $p_{\theta}$ is doubly differentiable in quadratic mean (DDQM) at $\theta \in \mathcal{M}$ if for any sequences $h, \tilde{h} \rightarrow 0$, we have

$$
\int\left(\sqrt{p_{\theta+h}}-\sqrt{p_{\theta+\tilde{h}}}-\frac{1}{2}(h-\tilde{h})^{T} \hat{\ell}(\theta+\tilde{h}) \sqrt{p_{\theta+\tilde{h}}}\right)^{2} d \mu=o\left(\|h-\tilde{h}\|^{2}\right)
$$

Recall also that DDQM reduces to DQM in the special case $\tilde{h}=0$, and that (by symmetry) we could replace $\hat{\ell}_{\theta+\tilde{h}} \sqrt{p_{\theta+\tilde{h}}}$ by $\hat{\ell}_{\theta+h} \sqrt{p_{\theta+h}}$. On the other hand it is strictly stronger than DQM at $\theta$.

![img-8.jpeg](img-8.jpeg)

Figure 9: Surface plot of the function $f(x, y)=x y^{1 / 3}$.

Example A.2. Suppose that $(X, Y)^{T} \sim N(\eta, I)$ where $\eta(\theta)=\left(\theta_{1} \theta_{2}^{1 / 3}, \theta_{2}\right)$. We claim that $p_{\theta}$ is DQM at $(0,0)$ but not DDQM.

Obviously $\eta(0,0)=(0,0)$ and $p_{\eta}$ is DQM at $\eta=(0,0)$, so

$$
\int\left(\sqrt{p_{\eta}}-\sqrt{p_{0}}-\eta^{T} \dot{\ell}(0) \sqrt{p_{0}}\right)^{2} d \eta=o\left(\|\eta\|^{2}\right)
$$

But now for any $\theta$, we have

$$
\begin{aligned}
\frac{p_{\theta}}{p_{0}} & =\exp \left\{-\frac{1}{2}\left[\left(x-\eta_{1}\right)^{2}+\left(y-\eta_{2}\right)^{2}-x^{2}-y^{2}\right]\right\} \\
& =1+x \theta_{1} \theta_{2}^{1 / 3}+y \theta_{2}+o(\|\theta\|) \\
& =1+y \theta_{2}+o(\|\theta\|) \\
\sqrt{\frac{p_{\theta}}{p_{0}}} & =1+\frac{1}{2} y \theta_{2}+o(\|\theta\|)
\end{aligned}
$$

Hence

$$
\mathbb{E}_{0}\left(\sqrt{\frac{p_{\theta}}{p_{0}}}-1-\theta_{2} Y\right)^{2}=o\left(\|\theta\|^{2}\right)
$$

and $p_{\theta}$ is also DQM at $(0,0)$.
Now let $\theta^{n}=\left(n^{-1 / 6}, n^{-1 / 2}\right)$ and $\tilde{\theta}^{n}=\left(n^{-1 / 6},-n^{1 / 2}\right)$. Then $\eta^{n}=\left(n^{-1 / 3}, n^{-1 / 2}\right)$ and $\tilde{\eta}^{n}=\left(-n^{-1 / 3},-n^{-1 / 2}\right)$. In particular, the sequence $\left\|\eta^{n}-\tilde{\eta}^{n}\right\|$ is of order $n^{-1 / 3}$, and hence we will have power to choose between the two sequences.

This (somewhat pathological) construction has a 'wrinkle' in the surface that maps $\theta$ to $\eta$-see Figure 9 for an illustration. The wrinkle is too small for DQM to fail at $\theta=0$, but pairs of points close to the wrinkle and to each other in $\theta$ space may be far apart in $\eta$ space. This model therefore fails to satisfy the condition of $\sqrt{p_{\theta}}$ being continuously differentiable at $\theta=(0,0)$.

Lemma A.3. Let $p_{\theta}$ be $D D Q M$ at $\theta \in \Theta$. Then, the Fisher information $I(\theta) \equiv \mathbb{E} \dot{\ell}(\theta) \dot{\ell}(\theta)^{T}$ exists and is continuous in a neighbourhood of $\theta \in \Theta$.

Proof. Since $p_{\theta}$ is DDQM at $\theta$ it is also DQM, and hence $I(\theta)$ exists by van der Vaart (1998, Theorem 7.2). In addition, the symmetry of DDQM shows that $\lim _{t \rightarrow 0} h^{T} I(\theta+t h) h=$ $h^{T} I(\theta) h$ for any $h$, so this matrix must indeed exist in a neighbourhood of $\theta$.

By the symmetry property noted above, $\int\left[(h-t \tilde{h})^{T} \dot{\ell}\left(\theta+t^{2} \tilde{h}\right) \sqrt{p_{\theta+t^{2} \tilde{h}}}\right]^{2} d \mu=(h-$ $\left.t \tilde{h}\right)^{T} I\left(\theta+t^{2} \tilde{h}\right)(h-t \tilde{h})$ and $(h-t \tilde{h})^{T} I(\theta+t h)(h-t \tilde{h})$ have the same limit, and these are in turn the same as the respective limits of $h^{T} I\left(\theta+t^{2} \tilde{h}\right) h$ and $h^{T} I(\theta+t h) h$. Since $h$ and $\tilde{h}$ are arbitrary, this shows that $I(\theta)$ is continuous at $\theta$.

We now prove Theorem 2.9, closely following the proof of Theorem 7.2 of van der Vaart (1998).

Proof of Theorem 2.9. Let $p_{n}$ and $\tilde{p}_{n}$ respectively denote $p_{\theta+h_{n}}$ and $p_{\theta+\tilde{h}_{n}}$. By DDQM we have that $\sqrt{n}\left(\sqrt{p}_{n}-\sqrt{\tilde{p}}_{n}\right)-\frac{1}{2} k^{T} \dot{\ell}\left(\theta+\tilde{h}_{n}\right) \sqrt{\tilde{p}_{n}}$ converges in quadratic mean to 0 ; since the second term is bounded in squared expectation (given by $k^{T} I\left(\theta+\tilde{h}_{n}\right) k / 4$ ) so is the first, and hence $n^{\gamma}\left(\sqrt{p}_{n}-\sqrt{\tilde{p}}_{n}\right) \rightarrow 0$ in quadratic mean for any $\gamma<\frac{1}{2}$.

Let $g_{n}=k^{T} \dot{\ell}\left(\theta+\tilde{h}_{n}\right)$. Note that DDQM implies that $\frac{1}{2} g_{n} \sqrt{\tilde{p}_{n}}$ has the same limit as $\sqrt{n}\left(\sqrt{p}_{n}-\sqrt{\tilde{p}_{n}}\right)$. By continuity of the inner product, we have

$$
\begin{aligned}
\lim _{n} \mathbb{E}_{\theta+\tilde{h}_{n}} g_{n} & =\lim _{n} \int g_{n} \tilde{p}_{n} d \mu \\
& =\lim _{n} \int \frac{1}{2} g_{n} \sqrt{\tilde{p}_{n}} 2 \sqrt{\tilde{p}_{n}} d \mu \\
& =\lim _{n} \sqrt{n} \int\left(\sqrt{p_{n}}-\sqrt{\tilde{p}_{n}}\right)\left(\sqrt{p_{n}}+\sqrt{\tilde{p}_{n}}\right) d \mu \\
& =\lim _{n} \sqrt{n} \int\left(p_{n}-\tilde{p}_{n}\right) d \mu \\
& =0
\end{aligned}
$$

since $\int\left(p_{n}-\tilde{p}_{n}\right) d \mu=1-1=0$ for all densities $p_{n}, \tilde{p}_{n}$.
Let $W_{n i}=2\left(\sqrt{p_{n} / \tilde{p}_{n}}\left(X_{i}\right)-1\right)$ where $X_{i} \sim \tilde{p}_{n}$. Then

$$
n \mathbb{E} W_{n i}=2 n \int \sqrt{p_{n} \tilde{p}_{n}} d \mu-2 n=-n \int\left(\sqrt{p_{n}}-\sqrt{\tilde{p}_{n}}\right)^{2} d \mu
$$

which, by the DDQM condition, has the same limit as

$$
-\frac{1}{4} k^{T}\left(\mathbb{E}_{\theta+\tilde{h}_{n}} \dot{\ell}\left(\theta+\tilde{h}_{n}\right)^{T} \dot{\ell}\left(\theta+\tilde{h}_{n}\right)\right) k=-\frac{1}{4} k^{T} I\left(\theta+\tilde{h}_{n}\right) k
$$

Then

$$
\begin{aligned}
& \operatorname{Var}_{\theta+\tilde{h}_{n}}\left(\sum_{i} W_{n i}-\frac{1}{\sqrt{n}} \sum_{i} g_{n}\left(X_{i}\right)\right) \\
& \leq \mathbb{E}_{\theta+\tilde{h}_{n}}\left(\sqrt{n} W_{n i}-g_{n}\left(X_{i}\right)\right)^{2} \\
&=\int\left(\sqrt{n} W_{n i}-g_{n}\left(X_{i}\right)\right)^{2} \tilde{p}_{n} d \mu \\
&=\int\left(\sqrt{n} 2\left(\sqrt{p_{n} / \tilde{p}_{n}}-1\right)-k^{T} \dot{\ell}\left(\theta+\tilde{h}_{n}\right)\right)^{2} \tilde{p}_{n} d \mu \\
&=\int 4\left(\sqrt{n}\left(\sqrt{p_{n}}-\sqrt{\tilde{p}_{n}}\right)-\frac{1}{2} k^{T} \dot{\ell}\left(\theta+\tilde{h}_{n}\right) \sqrt{\tilde{p}_{n}}\right)^{2} d \mu \\
&=o(1)
\end{aligned}
$$

by DDQM. It follows from all this that the sequence of random variables

$$
\sum_{i} W_{n i}-\frac{1}{\sqrt{n}} \sum_{i} g_{n}\left(X_{i}\right)+\frac{1}{4} k^{T} I\left(\theta+\tilde{h}_{n}\right) k
$$

has mean and variance tending to zero, and hence they converge to zero in probability.
Using a Taylor expansion, we obtain

$$
\begin{aligned}
\log \prod_{i=1}^{n} \frac{p_{\theta+h_{n}}}{p_{\theta+\tilde{h}_{n}}}\left(X_{i}\right) & =2 \sum_{i=1}^{n} \log \left(1+W_{n i} / 2\right) \\
& =\sum_{i=1}^{n} W_{n i}-\frac{1}{4} \sum_{i=1}^{n} W_{n i}^{2}+\frac{1}{2} \sum_{i=1}^{n} W_{n i}^{2} R\left(W_{n i}\right)
\end{aligned}
$$

for some function $R$ such that $\lim _{x \rightarrow 0} R(x)=0$. By the right-hand side of (3), we have $n W_{n i}^{2}=g_{n}\left(X_{i}\right)^{2}+A_{n i}$ for some $A_{n i}$ such that $\mathbb{E}\left|A_{n i}\right| \rightarrow 0$, and hence $\bar{A}_{n}=n^{-1} \sum_{i} A_{n i}$ converges in probability to 0 . Then

$$
\sum_{i} W_{n i}^{2}-n^{-1} \sum_{i} g_{n}\left(X_{i}\right)^{2}=\bar{A}_{n}=o_{p}(1)
$$

We also have

$$
\begin{aligned}
P\left(\max _{i}\left|W_{n i}\right|>\varepsilon \sqrt{2}\right) & \leq n P\left(\left|W_{n i}\right|>\varepsilon \sqrt{2}\right) \\
& \leq n P\left(g_{n}\left(X_{i}\right)^{2}>n \varepsilon^{2}\right)+n P\left(\left|A_{n i}\right|>n \varepsilon^{2}\right) \\
& \leq \varepsilon^{-2} \mathbb{E} g_{n}\left(X_{i}\right)^{2} \mathbb{1}_{\left\{g_{n}\left(X_{i}\right)^{2}>n \varepsilon^{2}\right\}}+\varepsilon^{-2} \mathbb{E}\left|A_{n i}\right|
\end{aligned}
$$

We already have $\mathbb{E}\left|A_{n i}\right| \rightarrow 0$, and since $\mathbb{E} g_{n}\left(X_{i}\right)^{2}=k^{T} I\left(\theta+\tilde{h}_{n}\right) k$ is continuous (and hence bounded) by Lemma A.3, the first term also tends to 0 . It follows that $\max _{i}\left|W_{n i}\right|=$ $o_{p}(1)$ and thus $\max _{i}\left|R\left(W_{n i}\right)\right|=o_{p}(1)$. Note therefore that the final term is bounded by $\max _{1 \leq i \leq n}\left|R\left(W_{n i}\right)\right| \cdot \sum_{i=1}^{n} W_{n i}^{2}=o_{p}(1) O_{p}(1)$ which converges to zero in probability.

Putting this back into (4) gives

$$
\log \prod_{i=1}^{n} \frac{p_{\theta+h_{n}}}{p_{\theta+\tilde{h}_{n}}}\left(X_{i}\right)=\sum_{i=1}^{n} W_{n i}-\frac{1}{4} k^{T} I\left(\theta+\tilde{h}_{n}\right) k+o_{p}(1)
$$

We then directly obtain

$$
\begin{aligned}
\ell\left(\theta+h_{n}\right)-\ell\left(\theta+\tilde{h}_{n}\right) & =\frac{1}{\sqrt{n}} \sum_{i} g_{n}\left(X_{i}\right)-\frac{1}{2} k^{T} I\left(\theta+\tilde{h}_{n}\right) k+o_{p}(1) \\
& =\frac{1}{\sqrt{n}} k^{T} \hat{\ell}\left(\theta+\tilde{h}_{n}\right)-\frac{1}{2} k^{T} I\left(\theta+\tilde{h}_{n}\right) k+o_{p}(1)
\end{aligned}
$$

Using the fact that $I(\cdot)$ is continuous at $\theta$ then gives the required result.
Sufficient conditions for DQM are given in Lemma 7.6 of van der Vaart (1998); in fact, these conditions are also sufficient for DDQM.
Lemma A.4. Assume that $\theta \mapsto s_{\theta}(x):=\sqrt{p_{\theta}(x)}$ is $\mu$-almost everywhere continuously differentiable, and that the matrix $I(\theta):=\int\left(\dot{p}_{\theta} / p_{\theta}\right)\left(\dot{p}_{\theta}^{T} / p_{\theta}\right) p_{\theta} d \mu$ has well-defined continuous entries. Then $p_{\theta}$ is DDQM.

Proof. We follow the same proof method as Lemma 7.6 in van der Vaart (1998). By the chain rule, $p_{\theta}$ is also differentiable with $\dot{p}_{\theta}=2 s_{\theta} \dot{s}_{\theta}$, and hence $\dot{s}_{\theta}=\frac{1}{2}\left(\dot{p}_{\theta} / p_{\theta}\right) \sqrt{p_{\theta}}$.

Since $\theta \mapsto s_{\theta}(x)$ is continuously differentiable (assuming for now that $x$ excludes the set of measure zero on which this fails), we can write

$$
\frac{s_{\theta+t h}-s_{\theta+t g}}{t}=(h-g)^{T} \dot{s}_{\theta+t(g+u(h-g))}
$$

for some $u \in[0,1]$ by the mean value theorem.
By Cauchy-Schwarz and Fubini, we have

$$
\begin{aligned}
\int\left(\frac{s_{\theta+t h}-s_{\theta+t g}}{t}\right)^{2} d \mu & \leq \iint_{0}^{1}\left((h-g)^{T} \dot{s}_{\theta+t(g+u(h-g))}\right)^{2} d u d \mu \\
& =\frac{1}{4} \int_{0}^{1}(h-g)^{T} I(\theta+t(g+u(h-g)))(h-g) d u \\
& \longrightarrow \frac{1}{4}(h-g)^{T} I(\theta)(h-g)
\end{aligned}
$$

here we have used the continuity of $I(\cdot)$. Continuous differentiability of $s(\cdot)$ shows that $t^{-1}\left(s_{\theta+t h}-s_{\theta+t g}\right)-(h-g)^{T} \dot{s}_{\theta+t g} \rightarrow 0$ pointwise, and hence its integral converges to zero by Proposition 2.29 of van der Vaart (1998).

We remark that Lemmas A. 3 and A. 4 show a close correspondence between continuity of the Fisher information and DDQM.

It is a standard result that the conditions of Lemma A. 4 are satisfied by an exponential family provided that $\theta$ is in the interior of the natural parameter space.

# A. 2 Proof of Theorem 2.10 

Proof. Assume $x=0$ without loss of generality. Given $h_{n} \in S_{1}$ with $h_{n} \rightarrow 0$, and the fact that $S_{1}$ and $S_{2}$ are $c$-equivalent at 0 , there exists a sequence $\tilde{h}_{n}=h_{n}+o\left(c_{n}^{c}\right)$ with $\tilde{h}_{n} \in S_{2}$. Now, choosing $\varepsilon_{n}=\left\|h_{n}\right\|$ which also tends to 0 , we obtain $\tilde{h}_{n}=h_{n}+o\left(\left\|h_{n}\right\|^{c}\right)$.

Now, if $h_{n}=O\left(n^{-\frac{1}{2 c}}\right)$, then $\tilde{h}_{n}-h_{n}=o\left(n^{-1 / 2}\right)$, which gives the required result. A similar argument holds for $c$-near-equivalence, giving $\tilde{h}_{n}-h_{n}=O\left(n^{-1 / 2}\right)$.

## A. 3 Proof of Theorem 3.1

Lemma A.5. Let the conditions of Theorem 3.1 be satisfied with $m \geq 2$. Then $\mathcal{M}_{1}$ and $\mathcal{M}_{2}$ have the same dimension and tangent space at $\theta$.

Proof. We have that $\mathrm{T}_{\theta}\left(\mathcal{M}_{1} \cap \mathcal{N}_{i}\right)=\mathrm{T}_{\theta}\left(\mathcal{M}_{1}\right) \cap \mathrm{T}_{\theta}\left(\mathcal{N}_{i}\right)$ for $i=1,2$. Since $\mathcal{N}_{1}$ and $\mathcal{N}_{2}$ have disjoint normal spaces, it follows that

$$
\begin{aligned}
\mathrm{T}_{\theta}\left(\mathcal{M}_{1}\right) & =\mathrm{T}_{\theta}\left(\mathcal{M}_{1}\right) \cap\left(\mathrm{T}_{\theta}\left(\mathcal{N}_{1}\right)+\mathrm{T}_{\theta}\left(\mathcal{N}_{2}\right)\right) \\
& =\mathrm{T}_{\theta}\left(\mathcal{M}_{1} \cap \mathcal{N}_{1}\right)+\mathrm{T}_{\theta}\left(\mathcal{M}_{1} \cap \mathcal{N}_{2}\right) \\
& =\mathrm{T}_{\theta}\left(\mathcal{M}_{2} \cap \mathcal{N}_{1}\right)+\mathrm{T}_{\theta}\left(\mathcal{M}_{2} \cap \mathcal{N}_{2}\right) \\
& =\mathrm{T}_{\theta}\left(\mathcal{M}_{2}\right) \cap\left(\mathrm{T}_{\theta}\left(\mathcal{N}_{1}\right)+\mathrm{T}_{\theta}\left(\mathcal{N}_{2}\right)\right) \\
& =\mathrm{T}_{\theta}\left(\mathcal{M}_{2}\right)
\end{aligned}
$$

Since $\mathcal{M}_{1}, \mathcal{M}_{2}$ are regular at $\theta$, this completes the proof.
The proof below makes modest use of differential geometry; the basics may be found in Conlon (2008).

Proof of Theorem 3.1. We choose $\theta=0$ for convenience. The result is clear for $m=1$, so assume $m \geq 2$. By Lemma A.5, $\mathcal{M}_{1}$ and $\mathcal{M}_{2}$ share a common dimension and tangent space at 0 . Since $\mathcal{M}_{1}, \mathcal{M}_{2}$ are $D^{m}$ surfaces at 0 , they can each be locally represented by a $D^{m}$ parametric function, say $\phi_{1}, \phi_{2}: U \rightarrow \mathbb{R}^{k}$. Assume that $\phi_{1}(0)=\phi_{2}(0)=0$, and that these functions share a derivative at 0 with respect to $u \in U$.

Choose $\phi_{1}$ so that $\phi_{1}(u)=(u, 0) \in \mathbb{R}^{d} \times \mathbb{R}^{k-d}$, by the constant rank theorem (Conlon, 2008, Theorem 2.4.6). Note this means that $\phi_{2}(u)=\left(u, O\left(\|u\|^{2}\right)\right)$ by the definition of the tangent space and the fact that $\phi_{2}$ is at least $D^{2}$. Also set $\phi_{1}^{-1}(A)=\phi_{2}^{-1}(A)$ for all $A \subseteq \mathcal{M}_{j} \cap \mathcal{N}_{i}$; then for each $u: \phi_{1}(u) \in \mathcal{M}_{1} \cap \mathcal{N}_{i}$ we have $\phi_{2}(u)=(u, 0)$.

By the implicit function theorem, each of the remaining $k-d$ coordinates of $\phi_{2}$ can be written as a $D^{m}$ function of the first $d$. By a further invertible $D^{m}$ transformation, we can ensure that $\phi_{1}(u), \phi_{2}(u) \in \mathcal{N}_{i}$ whenever $u_{c_{i-1}+1}=\cdots=u_{c_{i}}=0$ (where $c_{i}-c_{i-1}$ is the codimension of $\mathcal{M}_{j} \cap \mathcal{N}_{i}$ in $\mathcal{M}_{j}$ ).

Note that this means that not only is $\frac{\partial \phi_{1}(0)}{\partial u_{a}}=\frac{\partial \phi_{2}(0)}{\partial u_{a}}$ for all $a$, but indeed $\frac{\partial^{m-1} \phi_{1}(0)}{\partial u_{a_{1}} \cdots \partial u_{a_{m-1}}}=$ $\frac{\partial^{m-1} \phi_{2}(0)}{\partial u_{a_{1}} \cdots \partial u_{a_{m-1}}}$ for all $a_{1}, \ldots, a_{m-1}$, because there could still be some $i \in\{1, \ldots, m\}$ such that $u_{c_{i-1}+1}=\cdots=u_{c_{i}}=0$; therefore we are still (potentially) in at least one of the $m$ submodels, and $\phi_{1}^{-1}(y)=\phi_{2}^{-1}(y)$ holds at this point.

It follows that the Taylor expansions of $\phi_{1}$ and $\phi_{2}$ at 0 to order $m-1$ are identical, and the first term in which there is any difference will be of the form

$$
\frac{1}{m!} u_{a_{1}} \cdots u_{a_{m}} \frac{\partial^{m} \phi_{j}(0)}{\partial u_{a_{1}} \cdots \partial u_{a_{m}}}
$$

where each $a_{i} \in\left\{c_{i-1}+1, \ldots, c_{i}\right\}$. As a consequence of the product $u_{a_{1}} \cdots u_{a_{m}}$, it follows that $\left\|\phi_{1}(u)-\phi_{2}(u)\right\|=O\left(\|u\|^{m}\right)$, and hence $\mathcal{M}_{1}$ and $\mathcal{M}_{2}$ are $m$-near-equivalent.

# B Log-Linear Parameters 

Let $V$ be a finite set, and define the log-linear design matrix as a $2^{|V|} \times 2^{|V|}$ matrix with rows and columns indexed by subsets of $V$, such that

$$
M_{A, B}=(-1)^{|A \cap B|}
$$

We denote the $B$ th column (or equivalently row) of $M$ by $M_{B}$. Note that

$$
M_{B}=\bigodot_{v \in B} M_{\{v\}}
$$

where $\odot$ denotes the Hadamard (or point-wise) product. As an example, here is a log-linear design matrix for three items.

$$
M=\left(\begin{array}{rrrrrrrr}
1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & \\
1 & -1 & 1 & -1 & 1 & -1 & 1 & -1 & \\
1 & 1 & -1 & -1 & 1 & 1 & -1 & -1 & \\
1 & -1 & -1 & 1 & 1 & -1 & -1 & 1 & \\
1 & 1 & 1 & 1 & -1 & -1 & -1 & -1 & \\
1 & -1 & 1 & -1 & -1 & 1 & -1 & 1 & \\
1 & 1 & -1 & -1 & -1 & -1 & 1 & 1 & \\
1 & -1 & -1 & 1 & -1 & 1 & 1 & -1 &
\end{array}\right) \begin{gathered}
\emptyset \\
\{1\} \\
\{2\} \\
\{1,2\} \\
\{3\} \\
\{1,3\} \\
\{2,3\} \\
\{1,2,3\}
$$

For example, the fourth column of $M$ is $M_{\{1,2\}}$ and is given by the pointwise product of the second and third columns $M_{\{1\}}$ and $M_{\{2\}}$. Note also that $M$ is involutory - that is, its own inverse - up to a constant: $M^{-1}=2^{-|V|} M$.

Let $X_{V}=\left(X_{v}\right)_{v \in V}$ be a vector of binary random variables. We abbreviate the event $\left\{X_{v}=0\right.$ for all $\left.v \in C\right\}$ to $0_{C}$, and similarly $\left\{X_{v}=1\right.$ for all $\left.v \in C\right\}$ to $1_{C}$. Let $\eta_{A}=$ $\log p\left(1_{A}, 0_{V \backslash A}\right)$. Then we define the log-linear parameters via the identities

$$
\boldsymbol{\eta}=M \boldsymbol{\lambda}, \quad \boldsymbol{\lambda}=M^{-1} \boldsymbol{\eta}
$$

Letting $\boldsymbol{p}=\left(p\left(x_{V}\right): x_{V} \in \mathfrak{X}_{V}\right)$, assumed to be ordered in the same way as $\boldsymbol{\eta}$ so that $\boldsymbol{\eta}=\log \boldsymbol{p}$, we have

$$
\frac{\partial \boldsymbol{\lambda}}{\partial \boldsymbol{p}}=\frac{\partial \boldsymbol{\lambda}}{\partial \boldsymbol{\eta}} \frac{\partial \boldsymbol{\eta}}{\partial \boldsymbol{p}}=M^{-1}\left(\operatorname{diag} \boldsymbol{p}\left(x_{V}\right)\right)^{-1}
$$

Of interest to us is the connection between log-linear parameters within different marginal distributions, known as marginal log-linear parameters (Bergsma and Rudas, 2002). Denote the log-linear parameters within a marginal distribution $X_{K}$ by $\boldsymbol{\lambda}^{K} \equiv\left(M^{K}\right)^{-1} \log p\left(x_{K}\right)$, where $M^{K}$ is the appropriate restriction of $M$ to rows and columns indexed by subsets of $K$. We continue to denote the ordinary log-linear parameter associated with a particular interaction set $A$ by $\lambda_{A}=\lambda_{A}^{V}$.
Lemma B.1. The derivative of the parameter $\lambda_{A}^{K}$ (with respect to $\boldsymbol{p}$ ) lies in the span of the derivatives of $\lambda_{A}^{V}, \ldots, \lambda_{V}^{V}$ if $X_{K} \perp X_{V \backslash K}$. If $K=A$, then the converse also holds.

Additionally, if $p\left(x_{V}\right)$ is uniform then $\lambda_{A}^{K}$ and $\lambda_{A}^{V}$ have the same derivative $M_{A}$.
Proof. Let $x_{V}=\left(1_{B}, 0_{V \backslash B}\right)$. We have

$$
\begin{aligned}
\frac{\partial \lambda_{A}^{K}}{\partial p\left(x_{V}\right)} & =\frac{M_{A, B}}{2^{|K|} p\left(x_{K}\right)} \\
\text { and } \quad \sum_{C \subseteq V \backslash A} \alpha_{C} \frac{\partial \lambda_{A C}^{V}}{\partial p\left(x_{V}\right)} & =\frac{M_{A, B}}{2^{|V|} p\left(x_{V}\right)} \sum_{C \subseteq V \backslash A} \alpha_{C} M_{C, B}
\end{aligned}
$$

since $M_{A \cup C, B}=M_{A, B} \cdot M_{C, B}$. For the derivatives $\frac{\partial \lambda_{A}^{K}}{\partial \boldsymbol{p}}$ to lie in the span of the derivatives $\frac{\partial \lambda_{A C}^{V}}{\partial \boldsymbol{p}}$ we need to find $\alpha_{C}$ to solve

$$
\frac{M_{A, B}}{2^{|V|} p\left(x_{V}\right)} \sum_{C \subseteq V \backslash A} \alpha_{C} M_{C, B}=\frac{M_{A, B}}{2^{|K|} p\left(x_{K}\right)}
$$

or equivalently

$$
\sum_{C \subseteq V \backslash A} \alpha_{C} M_{C, B}=2^{|V \backslash K|} p\left(x_{V \backslash K} \mid x_{K}\right)
$$

for each $x_{V}$. If $X_{V \backslash K} \stackrel{1}{=} X_{K}$ this becomes $\sum_{C \subseteq V \backslash K} \alpha_{C} M_{C, B}=2^{|V \backslash K|} p\left(x_{V \backslash K}\right)$, which has a solution because it amounts to $2^{|V \backslash K|}$ linearly independent equations in $2^{|V \backslash A|} \geq 2^{|V \backslash K|}$ variables.

In the case that $K=A$, note that there are precisely as many variables as equations, and since the coefficients $M_{C, B}$ expression given on the left of (6) do not vary with $x_{K}$ (since $C \cap K=\emptyset$ ), it is necessary for $X_{V \backslash K} \stackrel{1}{=} X_{K}$ in order for a solution to exist. For $A \subset K$ a similar argument shows that $X_{V \backslash K} \stackrel{1}{=} X_{D} \mid X_{K \backslash D}$ for some $D \subset K$ with $|D| \leq|K \backslash A|$ is sufficient.

If $p\left(x_{V}\right)$ is uniform, then note that the derivative of $\lambda_{A}^{K}$ does not depend upon $K$.
Since the map from $\boldsymbol{\lambda}$ to $\boldsymbol{p}$ is a smooth one, this yields us the following Corollary.
Corollary B.2. If $\varepsilon \equiv\left\|p-p_{0}\right\|$ for $p_{0}$ under which all variables are uniform, then

$$
\lambda_{A}^{K}=\lambda_{A}^{L}+O\left(\varepsilon^{2}\right)
$$

# B. 1 Log-Linear Models are Algebraic 

Note that a log-linear model is algebraic, since $\lambda_{A}=c$ if and only if

$$
\prod_{\left\|x_{A}\right\|_{1} \text { even }} p\left(x_{A}, x_{V \backslash A}\right)-e^{c 2^{|V|}} \prod_{\left\|x_{A}\right\|_{1} \text { odd }} p\left(x_{A}, x_{V \backslash A}\right)=0
$$

Hence they are defined by the zeroes of polynomials in $p$.

## C Ancestral Graphs

Proof of Theorem 4.5. Let $\mathcal{G}$ be a graph with vertices $V$. We can parameterize the binary probability simplex using log-linear parameters $\lambda_{K}$ for $\emptyset \neq K \subseteq V$ (see Appendix B for details). We consider the tangent space of the model at the uniform distribution; that is, at $\lambda_{K}=0$ for every $K$.

The conditional independence $X_{a} \stackrel{1}{=} X_{b} \mid X_{C}$ is equivalent to the $\lambda_{a b D}^{\prime}=0$ for each $D \subseteq C$, where $\lambda_{K}^{\prime}$ are the log-linear parameters for the marginal distribution over $X_{a}, X_{b}, X_{C}$ (Rudas et al., 2010). However, within $\delta$ of the uniform distribution we have $\lambda_{K}^{\prime}=\lambda_{K}+O\left(\delta^{2}\right)$ (see Corollary B.2). Hence the constraint to the tangent cone imposed by $\lambda_{a b D}^{\prime}=0$ is the same as that imposed by $\lambda_{a b D}=0$ for each $D \subseteq C$.

Now, two MAGs are Markov equivalent if and only if they have the same adjacencies, unshielded colliders, and discriminating paths (e.g. Zhang, 2008, Proposition 2). If they differ in adjacencies (say $i, j$ ), then a log-linear parameter $\lambda_{i j}$ will appear in the tangent cone of one model but not the other. If they differ in an unshielded collider $i \leftrightarrow k \leftrightarrow j$ then in one model $\lambda_{i j k}=0$ but in the other this direction is not restricted. The same holds for a discriminating path between $i$ and $j$ for a potential collider $k$.

Remark C.1. Note that this proof also demonstrates that the skeleton of the graph is determined solely by the two-way interaction parameters, and that the remainder of the model can be deduced entirely from the three-way interaction parameters. This suggests that it might be possible to develop a model selection procedure using only this information, something we do in Section 7. It also illustrates that in cases with strong three-way interactions it should be easier to learn the correct model rather than just the correct skeleton. A 'noisy-OR' model would, for example, have the desired property. The well known ALARM dataset (Beinlich et al., 1989) has strong interaction effects and is - at least in part for this reason - considered to be relatively easy to learn.

Proof of Proposition 4.6. We claim that the spaces spanned by $\lambda_{i k}$ and $\lambda_{j k}$ are contained in the tangent cones of both models, but not of their intersection; the first claim follows from Theorem 4.5. For the second, if $X_{k}$ is binary then $\lambda_{i j}^{\prime}=\lambda_{i j}=0$ if and only if either $\lambda_{i k}=0$ or $\lambda_{j k}=0$ (see Drton et al., 2008, Example 3.1.7). Clearly then directions in which they are both non-zero will not appear in the intersection model.

Remark C.2. Note that these results can easily be extended to a general finite discrete case, though the notation becomes rather cumbersome. In particular, suppose that the statespace is $\mathfrak{X}_{V}=\prod_{v \in V} \mathfrak{X}_{v}$ for some finite sets $\mathfrak{X}_{v}$. In this case $\lambda_{A}$ represents a collection of parameters of dimension $\prod_{a \in A}\left(\left|\mathfrak{X}_{a}\right|-1\right)$; these are redundant whenever some $x_{a}$ is equal to a suitable reference value (say $0_{a} \in \mathfrak{X}_{a}$ ), since they can be inferred from the remaining values.

Then we define

$$
\lambda_{A}\left(x_{A}\right)=\left|\mathfrak{X}_{V}\right|^{-1} \sum_{y_{V} \in \mathfrak{X}_{V}} \log p\left(y_{V}\right) \prod_{v \in A}\left(\left|\mathfrak{X}_{v}\right| \mathbb{1}_{\left\{x_{v}=y_{v}\right\}}-1\right)
$$

Hence $\lambda_{\emptyset}=\left|\mathfrak{X}_{V}\right|^{-1} \sum_{y_{V}} \log p\left(y_{V}\right)$ and

$$
\lambda_{1}\left(x_{1}\right)=\left|\mathfrak{X}_{V}\right|^{-1} \sum_{y_{V} \in \mathfrak{X}_{V}}\left(\left|\mathfrak{X}_{1}\right| \mathbb{1}_{\left\{x_{1}=y_{1}\right\}}-1\right) \log p\left(y_{V}\right)
$$

for example. The results in Section 4 still hold with these parameters at analogous locations.
Now, in the case of Proposition 4.6, the same result will hold even if $X_{k}$ is not binary. Evans (2015, Theorem 3.1) shows that $\lambda_{i j}^{A k}=\lambda_{i j}^{A}+g\left(\boldsymbol{\lambda}_{k \mid A}\right)$, where $g=0$ whenever $X_{k} \perp X_{l}\left|X_{A \backslash\{l\}}\right.$ for any $l \in V$. This means that $X_{k} \perp X_{i} \mid X_{A \backslash\{i\}}$ or $X_{k} \perp X_{j} \mid X_{A \backslash\{j\}}$ are included in the intersections of the two models. Further, one can check that the models are not identical, since adding $\varepsilon>0$ to $P\left(X_{A}=x_{A}, X_{k}=x_{k}\right)$ and subtracting it from $P\left(X_{A}=x_{A}, X_{k}=x_{k}^{\prime}\right)$ will not change the fact that $X_{i} \perp X_{j} \mid X_{A \backslash\{i, j\}}$, but we will no longer have $X_{i} \perp X_{j} \mid X_{A \backslash\{i, j\}}, X_{k}$. It follows that the two models overlap by Theorem 3.3.

# D Example: Discrete LWF Chain Graphs 

Example D.1. Consider the graphs shown in Figure 10. Interpreted using the Lauritzen-Frydenberg-Wermuth (LWF) Markov property (Lauritzen and Wermuth, 1989), these three graphs all represent distinct models. The graph in (a) satisfies the usual Markov property for undirected graphs:

$$
X_{1} \perp X_{4} \mid X_{2}, X_{3}, \quad X_{2} \perp X_{3} \mid X_{1}, X_{4}
$$

The graphs in (b) and (c) satisfy these independences, as well as the respective independences $X_{1} \perp X_{2}$ (in the case of (b)), and $X_{1} \perp X_{2} \mid X_{3}, X_{4}$ for (c). These two additional constraints are generally distinct, but they coincide if any of the three remaining edges are not present: i.e. if any of the conditional independences

$$
X_{1} \perp X_{3} \mid X_{2}, X_{4}, \quad X_{3} \perp X_{4} \mid X_{1}, X_{2}, \quad X_{2} \perp X_{4} \mid X_{1}, X_{3}
$$

![img-9.jpeg](img-9.jpeg)

Figure 10: Three chain graphs. When interpreted under the LWF Markov property, all associated models satisfy $X_{1} \Perp X_{4} \mid X_{2}, X_{3}$ and $X_{2} \Perp X_{3} \mid X_{1}, X_{4}$; these constraints define the model in (a). The submodel (b) additionally implies that $X_{1} \Perp X_{2}$, whereas (c) implies $X_{1} \Perp X_{2} \mid X_{3}, X_{4}$.
also hold. Under either model, each of these constraints corresponds to a single zero log-linear parameter:

$$
\lambda_{13}=0, \quad \lambda_{34}=0, \quad \lambda_{24}=0
$$

[recall that $\lambda_{A}:=2^{-|V|} \sum_{x_{V}}(-1)^{\left|x_{A}\right|} \log P\left(X_{V}=x_{V}\right)$ ]. Taking the models defined by these three constraints, we can apply Theorem 3.1 and find that the two models in (b) and (c) are 3 -near-equivalent at all points in the model of complete independence.

One can extend this example arbitrarily by drawing a graph of the form $1 \rightarrow 3-4-\cdots-$ $k \leftarrow 2$ and comparing it to its undirected counterpart. In this case if the effect corresponding to any of the $k-1$ edges is missing, then the two models intersect. Hence, by Theorem 3.1 these two models are $(k-1)$-near-equivalent.