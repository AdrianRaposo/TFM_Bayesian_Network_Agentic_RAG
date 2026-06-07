# A CONSISTENT MODEL SELECTION PROCEDURE FOR MARKOV RANDOM FIELDS BASED ON PENALIZED PSEUDOLIKELIHOOD 

By Chuanshu Ji ${ }^{1}$ and Lynne Seymour<br>University of North Carolina and University of Georgia

Motivated by applications in texture synthesis, we propose a model selection procedure for Markov random fields based on penalized pseudolikelihood. The procedure is shown to be consistent for choosing the true model, even for Gibbs random fields with phase transitions. As a by-product, rates for the restricted mean-square error and moderate deviation probabilities are derived for the maximum pseudolikelihood estimator. Some simulation results are presented for the selection procedure.

1. Introduction. Markov random fields are widely used as models in statistical image analysis [cf. Karr (1991) and Rosenfeld (1993)]. Since Hassner and Sklansky (1980) and Cross and Jain (1983) first used isotropic Markov random fields to generate synthetic textures, others have explored different types of Markov random fields for texture synthesis. How does one choose a model from a collection of Markov random fields such that its typical sample resembles an observed texture? In this paper we present a model selection procedure based on penalized pseudolikelihood for Markov random fields in the form of an exponential family. It is shown that, asymptotically, this procedure chooses the correct model under very general conditions.

Little has been done to address selection of Markov random fields. Kashyap and Chellappa (1983) first proposed a method of selection based on linear combinations of gray levels plus Gaussian noise. Smith and Miller (1990) proposed a selection procedure which is based on the stochastic complexity of Rissanen (1984) and is similar to the one presented here. Seymour and Ji (1996) derived two Bayesian selection criteria [Akaike (1978); Schwarz (1978)]. The first is based on the maximum likelihood estimate; it is of theoretical interest, but is intractable for random fields. The other criterion uses the Markov chain Monte Carlo approximation to the likelihood developed by Geyer and Thompson (1992). Although Markov chain Monte Carlo criterion is viable, it is difficult to implement for images and requires that the random field exhibit weak spatial dependence.

In Section 2, the required random field framework is briefly introduced. Section 3 gives the formulation of the model selection problem and the main

[^0]
[^0]:    Received November 1994; revised February 1996.
    ${ }^{1}$ Research supported in part by ONR Grant N00014-89-J-1760 and NSF Grant DMS-93-10322. AMS 1991 subject classification. Primary 62M40; secondary 62F12, 68U10.
    Key words and phrases. Markov random fields, Gibbs random fields, model selection, pseudolikelihood, texture synthesis, image analysis.

results. The selection procedure presented is based on the maximum pseudolikelihood estimate of Besag (1974). Although the criterion is similar to the Bayes criteria discussed above, it is not a Bayesian criterion. Even so, it has distinct advantages over the Bayes criteria; our criterion is much easier to compute and asymptotically it is shown to give a consistent choice of model, whether the spatial dependence is weak or strong. Since the spatial dependence involved in texture modelling may vary from short range to long range, the pseudolikelihood procedure has more extensive applications.

Because model selection and parameter estimation are closely related, the maximum pseudolikelihood parameter estimate and existing asymptotic results for this estimate are discussed in Section 4. In addition, two new lemmas are proven which provide rates for the restricted mean-square error and moderate deviation probabilities for the maximum pseudolikelihood estimate.

Section 5 presents and discusses some highlights of a simulation study of model selection via pseudolikelihood. Some concluding remarks are made in Section 6. All technical proofs are in the Appendix.
2. Random field framework. We consider Gibbs random fields induced by translation-invariant pair-potentials of finite range. The extensions to other finite-range translation-invariant potentials is straightforward but involves heavy notation. For a more general discussion of Gibbs random fields, see Georgii (1988).

With each site $i \in \mathbb{Z}^{2}$, associate a random variable $X_{i}$ taking values in a finite set $S$. Then $X=\left\{X_{i}, i \in \mathbb{Z}^{2}\right\}$ is a random field with configuration space $\Omega=S^{\mathbb{Z}^{2}}$. Let $x=\left\{x_{i}, i \in \mathbb{Z}^{2}\right\} \in \Omega$ denote a realization of $X$. For a region $\Lambda \subset \mathbb{Z}^{2}$, the subconfiguration space is given by $\Omega_{\Lambda}=S^{\Lambda}$, so write $X_{\Lambda}=\left\{X_{i}\right.$, $i \in \Lambda\}$ for the random field on $\Lambda$ and $x_{\Lambda}=\left\{x_{i}, i \in \Lambda\right\} \in \Omega_{\Lambda}$ for a realization of $X_{\Lambda}$.

Let the potential $U=\left\{h U_{1}\left(x_{o}\right), \beta_{j} U_{2}\left(x_{o}, x_{j}\right): x_{o}, x_{j} \in S ; j \in \mathbb{Z}^{2}\right\}$, with $o$ representing the origin, be a collection of functions such that $U_{1}: S \rightarrow \mathbb{R}$ and $U_{2}: S \times S \rightarrow \mathbb{R}$ are known and $U_{2}(s, t)=U_{2}(t, s)$. The term $h U_{1}(\cdot)$ (though not usually employed) may be used to model large-scale spatial trends, where $h \in \mathbb{R}$ (the external field coefficient) is an unknown parameter. The term $\beta_{j} U_{2}(\cdot, \cdot)$ is a pair-potential of range $R>0$ : the parameters $\beta_{j} \in \mathbb{R}, j \in \mathbb{Z}^{2}$ (the coupling coefficients) are also unknown and are such that $\beta_{j}=\beta_{-j} \forall j$ and $\beta_{j}=0 \forall j$ with $|j|>R$, where $|\cdot|$ is a norm on $\mathbb{Z}^{2}$. In particular, $\beta_{o}=0$. Let $\theta$ denote the vector parameter with components being the external field and coupling coefficients.

The following examples are just two of the potentials that have been used for modelling with Markov random fields.

Example 1. Consider the general Ising models, where $U_{1}\left(x_{i}\right)=x_{i}$, $U_{2}\left(x_{i}, x_{j}\right)=x_{i} x_{j}$ and $S=\{-1,1\}$. If $\beta_{j}=\beta>0$ for $|j|=1$ and $\beta_{j}=0$ otherwise, then we have the well-known two-dimensional Ising model.

Example 2. Let $U_{1}\left(x_{i}\right) \equiv 0$ and $U_{2}\left(x_{i}, x_{j}\right)=1 /\left[1+\sigma\left(x_{i}-x_{j}\right)^{2}\right]$, where $\sigma>0$ is a constant. This potential is used in Geman and Graffigne (1986).

A Gibbs measure (Gibbs random field) induced by a potential $U$ is a probability measure $P$ on $\Omega$ such that for every $x \in \Omega$ and any finite $\Lambda \in \mathbb{Z}^{2}$,

$$
P\left(X_{\Lambda}=x_{\Lambda} \mid X_{\Lambda^{\prime}}=x_{\Lambda^{\prime}}\right)=\frac{\exp \left[-H_{\Lambda}(x)\right]}{\mathscr{L}_{\Lambda}}
$$

where the energy associated with $x$ on $\Lambda$ is given by

$$
H_{\Lambda}(x)=-h \sum_{i \in \Lambda} U_{1}\left(x_{i}\right)-\frac{1}{2} \sum_{\substack{i, j \in \Lambda \\ 0<|j-i| \leq R}} \beta_{j-i} U_{2}\left(x_{i}, x_{j}\right)-\sum_{\substack{j \in \Lambda \\ j \notin \Lambda \\|j-i| \leq R}} \beta_{j-1} U_{2}\left(x_{i}, x_{j}\right)
$$

and the normalizing factor, called the partition function, is given by

$$
\mathscr{L}_{\Lambda}=\mathscr{L}_{\Lambda}\left(x_{\Lambda^{\prime}}\right)=\sum_{x_{\Lambda}} \exp \left[-H_{\Lambda}(x)\right]
$$

The conditional probabilities $\left\{P\left(X_{i}=\left.x_{i}\right|_{i} X={ }_{i} x\right), x \in \Omega\right\}$, are called the local characteristics at site $i \in \mathbb{Z}^{2}$, where ${ }_{i} X=\left\{X_{i}, j \neq i\right\}$ and ${ }_{i} x=\left\{x_{j}, j \neq i\right\}$. Indeed, the left-hand side of (2.1) is determined by the local characteristics at all $i \in \Lambda$ [Geman (1991)].

Under our assumptions on $U$, the set $\mathscr{G}(U)$ of Gibbs random fields induced by $U$ is always non-empty, but need not be a singleton (in which case there are phase transitions of the Gibbs random field and in which case the random field exhibits spatial long-range dependence).

A neighborhood system $\mathscr{N}$ is a collection $\left\{\mathscr{N}(i): i \in \mathbb{Z}^{2}\right\}$, where $\mathscr{N}(i) \subset \mathbb{Z}^{2}$ is the set of neighbors of $i \in \mathbb{Z}^{2}$ satisfying $i \notin \mathscr{N}(i)$ and $i \in \mathscr{N}(j) \Leftrightarrow j \in \mathscr{N}(i)$ $\forall i, j \in \mathbb{Z}^{2}$. Define the boundary of a finite region $\Lambda \subset \mathbb{Z}^{2}$ by $\partial \Lambda=$ $\left(\cup_{i \in \mathscr{Y}} \mathscr{N}(i)\right) \backslash \Lambda$. Then every $P \in \mathscr{G}(U)$ is a Markov random field with respect to a neighborhood system $\mathscr{N}$ in the sense that for every $x \in \Omega$ and any finite $\Lambda \subset \mathbb{Z}^{2}$,

$$
P\left(X_{\Lambda}=x_{\Lambda} \mid X_{\Lambda^{\prime}}=x_{\Lambda^{\prime}}\right)=P\left(X_{\Lambda}=x_{\Lambda} \mid x_{\partial \Lambda}=x_{\partial \Lambda}\right)
$$

with $\mathscr{N}(i)=\left\{j \in \mathbb{Z}^{2}: \beta_{i-i} \neq 0\right\}$ for every $i$. In fact, a Markov random field on a finite lattice has a Gibbs representation [Hammersley-Clifford theorem in Geman (1991)].

We will be referring to the following examples, which illustrate the similarities and differences in specifying both the neighborhood and the parameter dimension. For these examples, let $U_{1}\left(x_{i}\right) \equiv 0, U_{2}\left(x_{i}, x_{j}\right)=x_{i} x_{j}$ and $S=\{-1,1\}$.

Example 3. The neighborhood system depicted in Figure 1, denoted $m 1$, is for the two-dimensional Ising model. Each site $i$ has four nearest neighbors. The same coupling coefficient $\beta$ is imposed for each pair $(i, j), j \in \mathscr{N}(i)$.

![img-0.jpeg](img-0.jpeg)

Fig. 1. Model m1. Fig. 2. Model m2. Fig. 3. Model m3.

Example 4. For the model in Figure 2, denoted $m 2$, every site $i$ again has four nearest neighbors. However, two parameters $\beta_{V}$ and $\beta_{H}$ are used for "vertical pair" and "horizontal pair" interactions, respectively.

Example 5. For the model in Figure 3, denoted $m 3$, each site $i$ has 12 neighbors that can be subdivided into two layers. The parameters $\beta$ and $\gamma$ are associated with the inner layer and the outer layer, respectively.

Write $\left\{p_{i}(x ; \theta), x \in \Omega, i \in \mathbb{Z}^{2}\right\}$ for the local characteristics with parameter $\theta$.

Definition 1. The parameter $\theta$ is said to be identifiable if $p_{o}(x ; \theta) \neq$ $p_{o}\left(x ; \theta^{\prime}\right)$ for some $x \in \Omega$ whenever $\theta \neq \theta^{\prime}$.

Remark. Identifiability may also be imposed via conditions on the potentials [Georgii (1988); Gidas (1993)] or by conditions on $\mathscr{G}(U)$ [Cométs (1992)].

For an $n \times n$ square lattice $\Lambda(n)$, let $x_{\Lambda(n)}=x(n)$ denote a single realization of $X_{\Lambda(n)}=X(n)$, where $X$ has a distribution $P \in \mathscr{G}(U)$. Write $P_{\theta}$ for $P$ to indicate the parameterization and write $E_{\theta}(\cdot)$ for the expectation with respect to $P_{\theta}$. Extend the observation $x(n)$ to a configuration $\tilde{x}$ on $\mathbb{Z}^{2}$ by periodization, or tiling [toroidal edge correction; Ripley (1981)], as illustrated in Figure 4. Correspondingly, let $\tilde{X}$ denote the periodic random field based on $X_{\Lambda(n)}$.

Define the pseudolikelihood function [Besag (1974)], a product of the local characteristics of the sites of $\Lambda(n)$, as

$$
\mathscr{P} \mathscr{L}(x(n), \theta)=\prod_{i \in \Lambda(n)} P_{\theta}\left(X_{i}=\left.\tilde{x}_{i}\right|_{i} X={ }_{i} \tilde{x}\right)
$$

Any measurable function of $x(n)$ which maximizes $\mathscr{P} \mathscr{L}(x(n), \cdot)$ is called a maximum pseudolikelihood estimate of $\theta$ based on $x(n)$. We denote this estimate by $\hat{\theta}$.

There are several motivating factors for using the maximum pseudolikelihood estimate of $\theta$. A practical one is that the local characteristics are quickly

![img-1.jpeg](img-1.jpeg)

Fig. 4. Tiling.
and easily computed. An intuitive one is that the local geometry of an image may be reasonably summarized by the local characteristics. A theoretical one is that its existence, uniqueness and consistency have been proven by Geman and Graffigne (1986); independently, Gidas (1988) and Cométs (1992) have established its consistency.
3. The model selection problem and a consistency result. Specification of a potential (i.e., selecting a Markov random field model) consists of the interconnected parts of specifying both the neighborhood system $\mathfrak{N}$ and the dimension of the parameter $\theta$.

Let $\Theta=\mathbb{R}^{K}$ be the parameter space of interest, decomposed as the disjoint union $\Theta=\bigcup_{m=0}^{M} \Theta_{M}, \Theta_{m} \cap \Theta_{m^{\prime}}=\varnothing \forall m \neq m^{\prime}$, where each $\Theta_{m}$ corresponds to a candidate model (i.e., a potential) parameterized by an element of $\mathbb{R}^{k_{m}}$. We assume that every closure $\overline{\Theta}_{m}$ is a $k_{m}$-dimensional linear subspace of $\mathbb{R}^{K}$, $m=0,1, \ldots, M$ [cf. Schwarz (1978)]. In particular, $\Theta_{0}$ corresponds to the completely specified model with no unknown parameter. Denote the set of all candidate models by $\mathscr{M}=\{0,1, \ldots, M\}$ and let $\mathfrak{N}_{m}$ be the neighborhood system for the model $m \in \mathscr{M}$.

In Examples 3, 4 and 5, one sees that $\mathfrak{N}_{m 1}=\mathfrak{N}_{m 2} \neq \mathfrak{N}_{m 3}$ and that $k_{m 1}=$ 1 , while $k_{m 2}=k_{m 3}=2$. Several synthetic textures generated from $m 1, m 2$ and $m 3$ by the Gibbs sampler [Geman and Geman (1984)] are shown in Figures 5-10. The coupling coefficients are assigned different values to produce different imaginary patterns of both weak and strong spatial dependence: "sands" (Figure 5), "clouds" (Figure 6), "wood grain" (Figure 8) and "wall papers" (Figures 7, 9 and 10). Note that samples from such simple models are far from resembling real textures.

In general, starting from $\theta \in \Theta$, a different model can be obtained either by equating some components in $\theta$ (e.g., letting $\beta_{V}=\beta_{H} \triangleq \beta$ in $m 2$ to obtain $m 1$ ) or by setting some components to zero (e.g., letting $\gamma=0$ in $m 3$ to obtain $m 1$ ). In this way the pseudolikelihood, when written in the form of an exponential family, may be reduced to its minimal form [cf. Barndorff-Nielsen (1978); Brown (1986)].

For each $m \in \mathscr{M}$, let $\tilde{\theta}_{m}$ be the maximum pseudolikelihood estimate restricted to $\overline{\Theta}_{m}$. Let $\mathscr{P L}_{m}(\cdot, \cdot)$ denote the pseudolikelihood for model $m \in \mathscr{M}$ in minimal form: $\mathscr{P L}_{m}(x(n), \theta)=\exp \left\{|\Lambda(n)\left\|\theta^{\top} V_{m}-g_{m}(\theta)\right]\right\}$, where $V_{m}$ and $g_{m}(\cdot)$ denote functions analogous to the sufficient statistic and cumulant

![img-2.jpeg](img-2.jpeg)

Fig. 5. Model $m 1, \beta=0.1$.
generating function, respectively. Define the information criterion as

$$
Q_{m}=\sup _{\vartheta \in \widetilde{\Theta}_{m}} \log \mathscr{P} \mathscr{L}_{m}(x(n), \vartheta)-\frac{k_{m}}{2} \log |\Lambda(n)|
$$

Then the pseudolikelihood selection procedure is to choose the model $\hat{m} \in \mathscr{M}$ which maximizes $Q_{m}$.

Decompose the collection of candidate models as $\mathscr{M}=\mathscr{M}_{1}(\pi) \cup\{\pi\} \cup \mathscr{M}_{2}(\pi)$, where $\pi \in \mathscr{M}$ is the true model, $\theta \in \Theta_{\pi}$ is the true parameter which is assumed to be identifiable (see Definition 1), $\mathscr{M}_{1}(\pi)=\left\{m \in \mathscr{M}: \theta \notin \widetilde{\Theta}_{m}\right\}$ and $\mathscr{M}_{2}(\pi)=\left\{m \in \mathscr{M}: \widetilde{\Theta}_{\pi} \subset \widetilde{\Theta}_{m}\right\}$. Here $\mathscr{M}_{1}(\pi)$ corresponds to an underparameterized choice of model or to an incorrect specification of neighborhood system (different neighborhoods will correspond to different subspaces which may

![img-3.jpeg](img-3.jpeg)

Fig. 6. Model $m 1, \beta=1.0$.
have the same dimension), while $\mathscr{M}_{2}(\pi)$ corresponds to an overparameterized choice. Note particularly that $\widehat{\Theta}_{\sigma}$ is a proper subset of $\widehat{\Theta}_{m}$ if $m \in \mathscr{M}_{2}(\pi)$ and that our decomposition of $\mathscr{M}$ leaves out no choice of model, since we have decomposed the parameter space $\Theta$ into a disjoint union of subspaces $\Theta_{m}$, $m \in \mathscr{M}$, earlier in this section.

Denote the selection procedure which chooses a model $\hat{m}$ based on $x(n)$ by $\hat{m}=d(x(n))$, where $d: \Omega_{\Lambda(n)} \rightarrow \mathscr{M}$ denotes the decision function.

Definition 2. A selection procedure $d(\cdot)$ is said to be consistent if $\lim _{n \rightarrow \infty} P_{\theta}(d(X(n))=\pi)=1$, where $X(n)$ is a sample from $P_{\theta}, \theta \in \Theta_{\sigma}$, $\pi \in \mathscr{M}$.

![img-4.jpeg](img-4.jpeg)

Fig. 7. Model $m 1, \beta=-1.0$.

The following two propositions give decay rates for the probabilities of choosing an incorrect model in $\mathscr{M}_{1}(\pi)$ and in $\mathscr{M}_{2}(\pi)$, respectively.

Proposition 1. There exists $c>0$ such that $P_{g}\left(\hat{m} \in \mathscr{M}_{1}(\pi)\right) \leq \exp \left(-n^{c}\right)$ for sufficiently large $n$.

Proposition 2. There exists $\alpha>0$ such that $P_{g}\left(\hat{m} \in \mathscr{M}_{2}(\pi)\right)=O\left(n^{-\alpha}\right)$ as $n \rightarrow \infty$.

The following theorem is an immediate consequence of Propositions 1 and 2 .

THEOREM 1. The selection procedure based on $Q_{m}$ is consistent.

![img-5.jpeg](img-5.jpeg)

Fig. 8. Model $m 2, \beta_{1}=1.0, \beta_{2}=0.1$.
4. Some properties of the maximum pseudolikelihood estimator. Because parameter estimation is such an important part of model selection, some asymptotic properties of the maximum pseudolikelihood estimator are discussed in this section. In particular, Lemmas 3 and 4 in this section provide some asymptotic orders of consistency for the maximum pseudolikelihood estimator; these are crucial in proving the consistency for the selection procedure.

Fix a model $m \in \mathscr{M}$ and a parameter $\theta \in \Theta_{m}$ and suppress the notation indicating the model in this section and in the corresponding proofs in the Appendix. Recall the pseudolikelihood in exponential family form: the "sufficient statistic" is given by

$$
V=\frac{1}{|\Lambda(n)|} \sum_{i \in \Lambda(n)} Z\left(\tilde{x}_{i}, \tilde{x}_{x_{i i}}\right)
$$

![img-6.jpeg](img-6.jpeg)

Fig. 9. Model $m 2, \beta_{1}=1.0, \beta_{2}=-1.0$.
for some function $Z(\cdot, \cdot)$ of the appropriate potentials, and the "cumulant generating function" is given by

$$
g(\vartheta)=\frac{1}{|\Lambda(n)|} \sum_{i \in \Lambda(n)} \log \sum_{s \in S} \exp \left\{\theta^{T} Z\left(s, \tilde{x}_{\mathscr{F}(i)}\right)\right\}
$$

The gradient of $g(\vartheta)$ with respect to $\vartheta$ is given by

$$
\nabla g(\vartheta)=\frac{1}{|\Lambda(n)|} \sum_{i \in \Lambda(n)} E_{\beta}\left(Z \mid \tilde{x}_{\mathscr{F}(i)}\right)
$$

where $\vartheta$ specifically denotes a variable.
For each $i \in \Lambda(n)$, let $\Lambda(i, R)$ be the $(2 R+1) \times(2 R+1)$ square lattice centered at $i$, where $R$ is the range of the Gibbs distribution. In particular,

![img-7.jpeg](img-7.jpeg)

Fig. 10. Model $m 3, \beta=1.0, \gamma=-1.0$.
denote $\Lambda(o, R)=\Lambda(2 R+1)$. Let $\xi \in S$ and $\eta \in \Omega_{\Lambda(o, R) \backslash\{o\}}$, so that the combined configuration is $\xi \oplus \eta \in \Omega_{\Lambda(2 R+1)}$. Define

$$
\begin{aligned}
\mathbb{I}_{i}(\xi \oplus \eta) & =1_{\left\{\bar{S}_{\Lambda(i, R)} \sim \xi \oplus \eta\right\}} \\
\mathbb{I}_{i}(\eta) & =1_{\left\{\bar{S}_{\Lambda(i, R) \backslash\{i\}} \sim \eta\right\}} \text { for } i \in \Lambda(n)
\end{aligned}
$$

and

$$
\begin{aligned}
N_{a}(\xi \oplus \eta) & =\sum_{i \in \Lambda(n)} \mathbb{I}_{i}(\xi \oplus \eta) \\
N_{a}(\eta) & =\sum_{i \in \Lambda(n)} \mathbb{I}_{i}(\eta)
\end{aligned}
$$

Define the event

$$
\mathscr{A}(n)=\left\{x(n) \in \Omega_{\Lambda(n)} ; \frac{N_{n}(\xi \oplus \eta)}{|\Lambda(n)|} \geq \lambda \quad \forall \xi \oplus \eta \in \Omega_{\Lambda(2 R+1)}\right\}
$$

on which the empirical probabilities for all configurations in $\Omega_{\Lambda(n)}$ are bounded away from 0 . The complement of this set is negligible for large $n$.

Lemma 1. There exist positive constants $\lambda, c$ and $C$ such that

$$
P_{\theta}\left(\frac{N_{n}(\xi \oplus \eta)}{|\Lambda(n)|}<\lambda\right) \leq C \exp (-c n)
$$

for all large $n$ and all $\xi \oplus \eta \in \Omega_{\Lambda(2 R+1)}$.
Hence, the following lemma is restricted to $\mathscr{A}(n)$.
Lemma 2. There exist $c, C>0$ such that $c \leq v^{T} \nabla^{2} g(\vartheta) v \leq C$ for all unit vectors $v \in \mathbb{R}^{k_{m}}$, all $\vartheta \in \Theta_{m}$ in a neighborhood of $\theta$, all $x(n) \in \mathscr{A}(n)$ and all large $n$.

Remark. The following is a simple argument for the existence and uniqueness of the maximum pseudolikelihood estimator. The "pseudolikelihood" equation is given by $V=\nabla g(\vartheta)$. Now, for all $\vartheta \in \mathbb{R}^{k_{m}}$, it can be shown that $E_{\vartheta}[V-\nabla g(\vartheta)]=0$, so that by Theorem 14.A8 of Georgii (1988), we have

$$
\lim _{n \rightarrow \infty}[V-\nabla g(\theta)]=0, \quad P_{\theta} \text {-a.s. }
$$

By Lemma 2, there exists a small neighborhood of $\theta$, say $\mathscr{O}$, on which $\nabla g(\cdot)$ is a homeomorphism. Then, for large $n$, we have $V \in \nabla g(\mathscr{O})$ by (4.1). Thus there exists $\omega \in \mathscr{O}$ satisfying the pseudolikelihood equation, $V=\nabla g(\omega), P_{\theta}$-a.s. Since $g(\cdot)$ is globally convex [see (A.1) in the proof of Lemma 2 in the Appendix] and locally strictly convex by Lemma 2, the solution $\omega$ is the unique maximum pseudolikelihood estimate $\hat{\theta}$.

The next two lemmas provide asymptotic orders for the restricted mean squared error and moderate deviation probabilities for the maximum pseudolikelihood estimate.

Lemma 3. $E_{\theta}\left\{\|\hat{\theta}-\theta\|^{2} 1_{\mathscr{A}(n)}\right\}=O\left(|\Lambda(n)|^{-1}\right)$ as $n \rightarrow \infty$.
Remark. Theorem 1 may also be proven by Proposition 1, Lemma 3 and the Chebyshev inequality. However, the decay rate of the probability of choosing an incorrect model produced by this method can only be of the order $1 / \log n$-a rate inferior to the one inferred by using Propositions 1 and 2.

Lemma 4. For every $\varepsilon>0$ there exists $\alpha>0$ such that

$$
P_{\theta}\left(|\Lambda(n) \| \bar{\theta}-\theta \|^{2}>\varepsilon \log n\right)=O\left(n^{-\alpha}\right)
$$

as $n \rightarrow \infty$.
Remark. It is noteworthy that the constant $\alpha$ in Lemma 4, which is the same $\alpha$ as in Proposition 2, cannot be made greater than 1 in general. This precludes the use of the Borel-Cantelli lemma in an effort to prove the strong consistency of the pseudolikelihood selection procedure. [A procedure $d(\cdot)$ is said to be strongly consistent if $d(X(n)) \rightarrow \pi, P_{\theta}$-a.s. as $n \rightarrow \infty$, where $X(n)$ is a sample from $P_{\theta}, \theta \in \Theta_{\pi}, \pi \in \mathscr{M}$.] This observation is supported by the exact order of moderate deviation probabilities in the i.i.d. case given in Rubin and Sethuraman (1965).
5. Some simulation results. Although there is an extensive literature in various Markov chain simulation algorithms, we use the Gibbs sampler [Geman and Geman (1984)] for simulating textures. In our simulation studies, we have used the three models $m 1, m 2$ and $m 3$ which were introduced in Section 3. For convenience, we have omitted including a "largest" model among the candidates (cf. Proof of Proposition 1 in the Appendix). We study the pseudolikelihood procedure for $500 \times 500$ random fields with the neighborhood interactions varying from weak to strong. In the tables we present, $\beta_{1}$ corresponds to $\beta$ for $m 1$ and $m 3$ and $\beta_{Y}$ for $m 2$, while $\beta_{2}$ corresponds to $\beta_{H}$ for $m 2$ and $\gamma$ for $m 3$. The symbol $* *$ indicates the chosen model.

The pseudolikelihood procedure seems to work well in all cases, given the similarity of the candidate models. When neighborhood interactions are weak, as in Table 1, there are no phase transitions and an identifying structure cannot be discerned in a realization. In such cases, the pseudolikelihood procedure tends to overparametrize-in fact, the values of $Q_{m}$ do not vary much among the models. Also, the sample from the true model was practically indistinguishable from a sample from $m 1$ with no phase transitions (indeed, $m 1$ is a special case of both). On the other hand, when neighborhood interactions are stronger, phase transitions are possible. The procedure still tends to overparametrize when the true model is $m 1$ (seen in Table 2), but the chosen model is close to the true model and $Q_{m}$ again does not vary much. As seen in Table 3, the pseudolikelihood procedure worked extremely well when structures unique to the model are easily discernible, making a clear (i.e., one value of $Q_{m}$ is much larger than the others) and correct choice over all other candidates.

Remark. These same phenomena may be observed for $m 3$ [Seymour (1993)].
6. Concluding remarks. The model selection procedure proposed in this paper has a similar expression to that of the Bayesian information criterion [Schwarz (1978); Akaike (1978)] with the likelihood replaced by the

Table 1
Weak neighborhood interactions


Table 2
Strong neighborhood interactions $m 1$


pseudolikelihood in the first term and the same penalty for overparameterization in the second term. A similar modification of Akaike's information criterion [Akaike (1974)] may be considered. In the i.i.d. case, Woodroofe (1982) pointed out that Akaike's criterion is superior to the Bayesian criterion asymptotically when the dimensionality of the parameter tends to infinity at an appropriate rate as the sample size tends to infinity. We expect that a similar result will hold for Markov random field texture models if we let the range of the potential $R=R_{n} \rightarrow \infty$; however, more delicate asymptotics are needed to accomplish this, and the result in Ji (1990) may be helpful.

Table 3
Strong neighborhood interactions $m 2$


The asymptotic distributions for the indices $Q_{m}, m \in \mathscr{M}$, may also be investigated. The need for such was demonstrated in Woodroofe (1982), in which the distribution of the number of superfluous parameters contained in the selected model was found. Such a result could be used to make numerical comparisons between different models. The derivation may not be too difficult under Dobrushin's uniqueness condition for Gibbs random fields [Georgii (1988)]. However, the derivation is very challenging under the assumptions we have made in this paper due to the lack of a central limit theorem for Gibbs random fields under phase transitions.

Extensive simulation studies are still being done for real texture synthesis, and many issues remain open. A rich class of candidate potentials is required for using Markov random field models for texture synthesis. Our approach in this paper has been to consider a great variety of neighborhood systems. The recent approach of Künsch, Geman and Kehagias (1995) is to code each site variable in a complex manner while restricting to the nearest neighbors. Both of these approaches involve extremely intense computation. Current research still has yet to achieve the ideal of a convenient statistical method for replicating real textures.

# APPENDIX 

Lemma A.1. Let $R$ be the range of the Gibbs random field. Let $\mathscr{B}(1), \ldots$, $\mathscr{B}(T)$ be bounded regions in $\mathbb{Z}^{2}, T \in \mathbb{N}$, with the distances between $\mathscr{B}(t)$ and $\mathscr{B}\left(t^{\prime}\right)$ greater than $R$ for all $t \neq t^{\prime}$. Also, let $\mathscr{C}=\mathbb{Z}^{2} \backslash\left(\bigcup_{t=1}^{T} \mathscr{B}(t)\right)$ be the

corridor between these regions. Then for any collection of bounded measurable functions $f_{t}: \Omega_{\mathscr{B}(t)} \rightarrow \mathbb{R}, t=1, \ldots, T$, we have

$$
E_{\theta}\left\{\left.\prod_{t=1}^{T} f_{t}\left(X_{\mathscr{B}(t)}\right) \right\rvert\, x_{\mathscr{C}}\right\}=\prod_{t=1}^{T} E_{\theta}\left[f_{t}\left(X_{\mathscr{B}(t)}\right) \right\rvert\, x_{\mathscr{C}}\right]
$$

uniformly for all corridor configurations $x_{\mathscr{C}} \in \Omega_{\mathscr{C}}$, where $E_{\theta}\left(\cdot \mid x_{\mathscr{C}}\right)$ is the conditional expectation with respect to $P_{\theta}\left(\cdot \mid x_{\mathscr{C}}\right)$.

Proof. This result follows from the Markov property of $X$.
Proof of Lemma 1. Assume without loss of generality that ( $3 R+1$ ) divides $n$. Partition $\Lambda(n)$ as a union of disjoint tiles $\Lambda(n)=\bigcup_{t=1}^{T} D(t)$, so that each tile $D(t)$ is a $(3 R+1) \times(3 R+1)$ square lattice. Then $T=[n /$ $(3 R+1)]^{2}$.

Also, write the decomposition $\Lambda(n)=\bigcup_{k=1}^{\left(3 R+1\right)^{2}} G(k)$, where every $G(k)$ contains exactly $T$ sites with the same relative positions in the disjoint tiles $D(t), t=1, \ldots, T$. For instance, one $G(k)$ may consist of the centers of the $T$ tiles, while another $G(k)$ may consist of all upper left corners of the $T$ tiles. Therefore, $N_{n}(\xi \oplus \eta)=\sum_{k=1}^{\left(3 R+1\right)^{2}} \sum_{i \in G(k)} \mathbb{1}_{i}(\xi \oplus \eta)$ and for every $\xi \oplus \eta \in \Omega_{\Lambda(2 R)}$ we have

$$
P_{\theta}\left(\frac{N_{n}(\xi \oplus \eta)}{|\Lambda(n)|}<\lambda\right) \leq \exp (-\lambda n) \sum_{k=1}^{\left(3 R+1\right)^{2}} E_{\theta}\left[\exp \left\{-\frac{1}{n} \sum_{i \in G(k)} \mathbb{1}_{i}(\xi \oplus \eta)\right\}\right]
$$

For a fixed index $k$, let $\mathscr{C}(k)=\mathbb{Z}^{2} \backslash\left(\bigcup_{i \in G(k)} \Lambda(i, R)\right)$ be the corridor dividing the regions $\Lambda(i, R), i \in G(k)$. Then

$$
E_{\theta}\left[\exp \left\{-\frac{1}{n} \mathbb{1}_{i}(\xi \oplus \eta)\right\} \mid x_{\mathscr{C}(k)}\right] \leq 1-\frac{c_{1}}{n}
$$

for some $c_{1}>0$ and all large $n$. Therefore, employing Lemma A.1,

$$
P_{\theta}\left(\frac{N_{n}(\xi \oplus \eta)}{|\Lambda(n)|}<\lambda\right) \leq C \exp (-c n)
$$

for some $C>0$ and some $c>0$.

Proof of Lemma 2. Define

$$
K(\vartheta, n)=\vartheta^{T} V-g(\vartheta)=|\Lambda(n)|^{-1} \log \mathscr{P} \mathscr{L}(x(n), \vartheta)
$$

Let $p_{o}(\xi \mid \eta ; \vartheta)$ be the local characteristic at the origin, where $\xi \oplus \eta \in$ $\Omega_{\Lambda(2 R+1)}, \xi \in S$ is the value at the origin $o$ and $\eta \in \Omega_{\Lambda(2 R+1) \backslash\{o\}}$. Then, via translation invariance, we may write

$$
K(\vartheta, n)=\sum_{\eta} \frac{N_{n}(\eta)}{|\Lambda(n)|} \sum_{\xi} \frac{N_{n}(\xi \oplus \eta)}{N_{n}(\eta)} \log p_{o}(\xi \mid \eta ; \vartheta)
$$

Write the local characteristic at the origin in exponential family form

$$
p_{o}(\xi \mid \eta ; \vartheta)=\frac{\exp \left\{\vartheta^{T} \phi(\xi \oplus \eta)\right\}}{\sum_{s} \exp \left\{\vartheta^{T} \phi(s \oplus \eta)\right\}}
$$

where $\vartheta \in \mathbb{R}^{k_{m}}$ and $\phi(\cdot)$ is an appropriate vector-valued function. Because $\sum_{\xi} N_{o}(\xi \oplus \eta)=N_{o}(\eta)$ for fixed $\eta$, we have

$$
\begin{aligned}
-\nabla^{2} K(\vartheta, n)=\sum_{\eta} \frac{N_{o}(\eta)}{|\Lambda(n)|} E_{\vartheta} & \left(\left(\phi\left(X_{o} \oplus \eta\right)-E_{\vartheta}\left[\phi\left(X_{o} \oplus \eta\right) \mid \eta\right]\right)\right. \\
& \left.\times\left(\phi\left(X_{o} \oplus \eta\right)-E_{\vartheta}\left[\phi\left(X_{o} \oplus \eta\right) \mid \eta\right]\right)^{T} \mid \eta\right]
\end{aligned}
$$

where $E \vartheta(\cdot \mid \eta)$ is the conditional expectation with respect to $p_{o}(\cdot \mid \eta ; \vartheta)$. Hence for $v \in \mathbb{R}^{k_{m}}$, we have

$$
\begin{aligned}
v^{T} \nabla^{2} & g(\vartheta) v \\
& =-v^{T} \nabla^{2} K(\vartheta, n) v \\
& =\sum_{\eta} \frac{N_{o}(\eta)}{|\Lambda(n)|} E_{\vartheta}\left\langle\left[v^{T}\left(\phi\left(X_{o} \oplus \eta\right)-E_{\vartheta}\left[\phi\left(X_{o} \oplus \eta\right) \mid \eta\right]\right)\right]^{2} \mid \eta\right\rangle
\end{aligned}
$$

Since this expectation is bounded and there are only finitely many $\eta \in$ $\Omega_{\Lambda(2 R+1) \backslash\{0\}}$, we see that $v^{T} \nabla^{2} g(\vartheta) v \leq C$ for some $C>0$.

On the other hand, the identifiability of $\theta$ guarantees that the "outside" expectation is strictly positive for at least one of the $\eta$-configurations. Also, for fixed $\xi \in S$ and $\eta \in \Omega_{\Lambda(2 R+1) \backslash\{0\}}$, it should be clear that $N_{o}(\eta) \geq N_{o}(\xi \oplus \eta)$. Then on $\mathscr{A}(n)$,

$$
\frac{N_{o}(\eta)}{|\Lambda(n)|} \geq \frac{N_{o}(\xi \oplus \eta)}{|\Lambda(n)|} \geq \lambda>0
$$

for all $\eta$-configurations. Therefore, $v^{T} \nabla^{2} g(\vartheta) v \geq c$ for some $c>0$.
Proof of Lemma 3. The Taylor expansion of $\nabla K(\vartheta, n)$ about $\tilde{\theta}$ gives

$$
\begin{aligned}
\nabla K(\theta, n) & =\nabla K(\tilde{\theta}, n)+\nabla^{2} K\left(\vartheta^{\prime}, n\right)(\theta-\tilde{\theta}) \\
& =-\nabla^{2} g\left(\vartheta^{\prime}\right)(\theta-\tilde{\theta})
\end{aligned}
$$

for some $\vartheta^{\prime}$ satisfying $\left\|\vartheta^{\prime}-\tilde{\theta}\right\| \leq\|\theta-\tilde{\theta}\|$. By Lemma 2,

$$
\|\tilde{\theta}-\theta\|^{2} \leq C\|\nabla K(\theta, n)\|^{2}
$$

on $\mathscr{A}(n)$ for some $C>0$. Thus $E_{\theta}\left(\|\tilde{\theta}-\theta\|^{2} \mathbf{1}_{\mathscr{A}(n)}\right) \leq C E_{\theta}\left(\|\nabla K(\theta, n)\|^{2}\right)$. Rewrite $K(\theta, n)$ as

$$
K(\theta, n)=\frac{1}{|\Lambda(n)|} \sum_{i \in \Lambda(n)}\left(\sum_{\xi \oplus \eta} \mathbb{1}_{i}(\xi \oplus \eta) \log p_{o}(\xi \mid \eta ; \theta)\right)
$$

so that

$$
\nabla K(\theta, n)=\frac{1}{|\Lambda(n)|} \sum_{i \in \Lambda(n)} W_{i}
$$

where $W_{i}$ is the vector

$$
W_{i}=\sum_{\eta} \mathbb{I}_{i}(\eta)\left(\phi\left(X_{i} \oplus \eta\right)-E_{\theta}\left[\phi\left(X_{i} \oplus \eta\right) \mid \eta\right]\right)
$$

For each $i \in \Lambda(n)$, all of the components of $W_{i}$ are bounded. Let $w_{i}$ denote an arbitrary component of $W_{i}$. Then it is sufficient to show

$$
E_{\theta}\left\{\left(\sum_{i \in \Lambda(n)} w_{i}\right)^{2}\right\}=O(|\Lambda(n)|)
$$

Using the decompositions of $\Lambda(n)$ from the proof of Lemma 1, it is enough to show

$$
E_{\theta}\left\{\left(\sum_{i \in G(k)} w_{i}\right)^{2}\right\}=O(|\Lambda(n)|)
$$

for each $G(k)$. Let $\mathscr{C}(k)$ be a corridor as constructed in the proof of Lemma 1. Then $E_{\theta}\left(W_{i} \mid x_{\mathscr{C}(k)}\right)=0$ for $i \in G_{k}$ and every configuration $x_{\mathscr{C}(k)}$. Since the elements $w_{i}$ are bounded, Lemma A. 1 gives

$$
E_{\theta}\left\{\left(\sum_{i \in G(k)} w_{i}\right)^{2}\right\} \leq C\left|G_{k}\right|
$$

for some $C>0$. Because $|G(k)|=|\Lambda(n)})(3 R+1)^{-2}$, the result clearly follows.

Proof of Lemma 4. By (A.2) and Lemma 1, it suffices to show that for every $\varepsilon>0$,

$$
P_{\theta}(|\Lambda(n)| \|\nabla K(\theta, n)\|^{2}>\varepsilon \log n)=O\left(n^{-\alpha}\right)
$$

Using the notation in the proof of Lemma 3, it is enough to show that for every $\varepsilon>0$,

$$
P_{\theta}\left(\left|\sum_{i \in G(k)} w_{i}\right|>\varepsilon \tau_{n}\right)=O\left(n^{-\alpha}\right)
$$

for some $\alpha>0$, where $\tau_{n}=\sqrt{|\Lambda(n)| \log n}$.
Consider the two cases for the absolute value, studying first the positive case. For $\rho>0$ (to be specified),

$$
P_{\theta}\left(\sum_{i \in G(k)} w_{i}>\varepsilon \tau_{n}\right) \leq \exp \left(-\rho \varepsilon \sqrt{\tau_{n}}\right) E_{\theta}\left[\exp \left(\sum_{i \in G(k)} \frac{\rho w_{i}}{\sqrt{\tau_{n}}}\right)\right]
$$

Using Lemma A. 1 and the construction of the corridor $\mathscr{C}(k)$ in the proof of Lemma 1,

$$
E_{\theta}\left[\exp \left(\sum_{i \in G(k)} \frac{\rho w_{i}}{\sqrt{\tau_{n}}}\right)\right]=E_{\theta}\left\{\prod_{i \in G(k)} E_{\theta}\left[\exp \left(\left.\frac{\rho w_{i}}{\sqrt{\tau_{n}}}\right) \right\rvert\, X_{\mathscr{C}(k)}\right]\right\}
$$

From the proof of Lemma $3, E_{\theta}\left(w_{i} \mid x_{\mathscr{C}(k)}\right)=0$ for every corridor configuration $x_{\mathscr{C}(k)}$, so that

$$
P_{\theta}\left(\sum_{i \in G(k)} w_{i}>\varepsilon \tau_{n}\right) \leq \exp \left(-\rho \varepsilon \sqrt{\tau_{n}}\right) \exp \left(\frac{\alpha^{\prime} \rho^{2}|G(k)|}{\tau_{n}}\right)
$$

for some $\alpha^{\prime}>0$. Let $\alpha^{\prime \prime}=\alpha^{\prime} /(3 R+1)^{2}$ and recall that $|G(k)|=|\Lambda(n)| /$ $(3 R+1)^{2}$. Set $\rho=\varepsilon n^{-1 / 2}(\log n)^{3 / 4}\left(2 \alpha^{\prime \prime}\right)^{-1}$ and note that $|\Lambda(n)|=n^{2}$. Then

$$
P_{\theta}\left(\sum_{i \in G(k)} w_{i}>\varepsilon \tau_{n}\right)=O\left(n^{-\alpha}\right)
$$

with $\alpha=\varepsilon^{2} / 4 \alpha^{\prime \prime}$.
For the negative case,

$$
P_{\theta}\left(-\sum_{i \in G(k)} w_{i}>\varepsilon \tau_{n}\right)=O\left(n^{-\alpha}\right)
$$

can be derived in the same way. Hence (A.4) follows.
Proof of Proposition 1. Note that for all $\vartheta \in \bar{\Theta}_{m}$ and all $m \in \mathscr{M}_{1}(\pi)$, there exists $\varepsilon_{1}>0$ such that $\|\theta-\vartheta\| \geq 3 \varepsilon_{1}$. Let $M$ be the "largest" model (i.e., the model which can be reduced to any of the other candidate models), so that $\bar{\Theta}_{m} \subseteq \bar{\Theta}_{M}$ for all $m \in \mathscr{M}$. Note here that $\bar{\Theta}_{M}=\Theta=\mathbb{R}^{K}$ and that we may write $\tilde{\theta}$ for $\tilde{\theta}_{M}$ since $\tilde{\theta}_{M}$ is a "global" maximum pseudolikelihood estimate over the set $\mathscr{M}$.

Let $\mathscr{D}(n)=\left\{x(n) \in \Omega_{\Lambda(n)}:\|\tilde{\theta}-\theta\| \leq \varepsilon_{1}\right\}$. Then, applying Lemma 1 to $P_{\theta}\left(\mathscr{A}(n)^{c}\right)$ and the exponential consistency of $\tilde{\theta}$ [Cométs (1992)] to $P_{\theta}\left(\mathscr{D}(n)^{c}\right)$, we have $P_{\theta}\left(\left\{\mathscr{A}(n) \cap \mathscr{D}(n)\right\}^{c}\right) \leq \exp \left(-n^{a_{1}}\right)$ for some $a_{1}>0$ and for all large $n$. Hence we restrict our attention to $\mathscr{A}(n) \cap \mathscr{D}(n)$.

Let $\tilde{m} \in \mathscr{M}_{1}(\pi)$, where $\tilde{m}$ denotes the chosen model. Recall from the proof of Lemma 2 that $K(\vartheta, n)=\vartheta^{\top} V-g(\vartheta)=\vartheta^{\top} V_{M}-g_{M}(\vartheta)$. Recall also that $K(\vartheta, n)$ is globally concave and locally strictly concave so that $\tilde{\theta}$ is the unique maximum pseudolikelihood estimate. Since the true parameter $\theta$ is some positive distance away from $\bar{\Theta}_{m}$, there exists $\delta>0$ such that $\sup _{\vartheta \in \bar{\Theta}_{m}} K(\vartheta, n) \leq K(\tilde{\theta}, n)-\delta$ for all large $n, P_{\theta}$ a.s. Then $Q_{M}-Q_{m} \geq$ $a_{2}|\Lambda(n)|$ for some $a_{2}>0$ and for all $m \in \mathscr{M}_{1}(\pi)$ so that

$$
P_{\theta}\left(\tilde{m} \in \mathscr{M}_{1}(\pi)\right) \leq P_{\theta}\left(Q_{\tilde{m}}-Q_{M}>0\right) \leq \exp \left(-n^{c}\right)
$$

as $n \rightarrow \infty$ for some $c>0$.

Proof of Proposition 2. Let $\mathscr{F}(n)=\left\{x(n) \in \Omega_{\Lambda(n)}:|\Lambda(n)| \| \tilde{\theta}_{\text {in }}-\theta \|^{2} \leq\right.$ $\left.\varepsilon \log n \text { for all } m \in \mathscr{M}\right\}$, so that by Lemma $4, P_{\theta}\left(\mathscr{F}(n)^{c}\right)=O\left(n^{-\alpha}\right)$ for some $\alpha>0$. Hence we restrict our attention to $\mathscr{A}(n) \cap \mathscr{F}(n)$.

On $\mathscr{A}(n)$, for a chosen model $\tilde{m} \in \mathscr{M}_{2}(\pi)$, we have

$$
Q_{\pi}-Q_{\tilde{m}}=|\Lambda(n)|\left[K_{\pi}\left(\tilde{\theta}_{\pi}, n\right)-K_{\tilde{m}}\left(\tilde{\theta}_{\tilde{m}}, n\right)\right]-\left(k_{\pi}-k_{\tilde{m}}\right) \log n
$$

Hence, we have

$$
K_{\pi}\left(\tilde{\theta}_{\pi}, n\right)-K_{\tilde{m}}\left(\tilde{\theta}_{\tilde{m}}, n\right) \geq-C\left(\left\|\tilde{\theta}_{\pi}-\theta\right\|^{2}+\left\|\tilde{\theta}_{\tilde{m}}-\theta\right\|^{2}\right)
$$

for some $C>0$, so that

$$
Q_{\pi}-Q_{\tilde{m}} \geq|\Lambda(n)|\left[-C\left(\left\|\tilde{\theta}_{\tilde{m}}-\theta\right\|^{2}+\left\|\tilde{\theta}_{\pi}-\theta\right\|^{2}\right)\right]-\left(k_{\pi}-k_{\tilde{m}}\right) \log n
$$

Then on $\mathscr{A}(n) \cap \mathscr{F}(n)$,

$$
Q_{\pi}-Q_{\tilde{m}} \geq a_{1} \log n
$$

where $a_{1}=k_{\tilde{m}}-k_{\pi}-2 C \varepsilon>0$, provided $\varepsilon$ is sufficiently small. Hence,

$$
P_{\theta}\left(\tilde{m} \in \mathscr{M}_{2}(\pi)\right) \leq P_{\theta}\left(Q_{\tilde{m}}-Q_{\pi}>0\right)=O\left(n^{-\alpha}\right)
$$

as $n \rightarrow \infty$ for some $\alpha>0$.
Acknowledgments. We are grateful to Stuart Geman and Basilis Gidas for stimulating discussions and to Richard Smith for helpful references and suggestions.
