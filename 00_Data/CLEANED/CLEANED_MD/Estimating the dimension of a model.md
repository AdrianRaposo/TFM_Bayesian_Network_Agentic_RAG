# ESTIMATING THE DIMENSION OF A MODEL ${ }^{1}$ 

By Gideon Schwarz

Hebrew University

The problem of selecting one of a number of models of different dimensions is treated by finding its Bayes solution, and evaluating the leading terms of its asymptotic expansion. These terms are a valid large-sample criterion beyond the Bayesian context, since they do not depend on the a priori distribution.

1. Introduction. Statisticians are often faced with the problem of choosing the appropriate dimensionality of a model that will fit a given set of observations. Typical examples of this problem are the choice of degree for a polynomial regression and the choice of order for a multi-step Markov chain.

In such cases the maximum likelihood principle invariably leads to choosing the highest possible dimension. Therefore it cannot be the right formalization of the intuitive notion of choosing the "right" dimension. An extension of the maximum likelihood principle is suggested by Akaike [1] for the slightly more general problem of choosing among different models with different numbers of parameters. His suggestion amounts to maximizing the likelihood function separately for each model $j$, obtaining, say, $M_{j}\left(X_{1}, \cdots, X_{n}\right)$, and then choosing the model for which $\log M_{j}\left(X_{1}, \cdots, X_{n}\right)-k_{j}$ is largest, where $k_{j}$ is the dimension of the model. We present an alternative approach to the problem.

In a model of given dimension maximum likelihood estimators can be obtained as large-sample limits of the Bayes estimators for arbitrary nowhere vanishing a priori distributions.

Therefore we look for the appropriate modification of maximum likelihood for our case, by studying the asymptotic beavior of Bayes estimators under a special class of priors. These priors are not absolutely continuous, since they put positive probability on some lower-dimentional subspaces of the parameter space, namely the subspaces that correspond to the competing models. In the large-sample limit, the leading term of the Bayes estimator turns out to be just the maximum likelihood estimator. Only in the next term something new is obtained. This was to be expected, since (as was shown in [2] and [3], albeit for sequential testing) the leading term depends on the prior only through its support, while the second order term does reflect singularities of the a priori distribution. We shall arrive at the following procedure:

Choose the model for which $\log M_{j}\left(X_{1}, \cdots, X_{n}\right)-\frac{1}{2} k_{j} \log n$ is largest.
The validity of this procedure as a large-sample version of Bayes procedures

[^0]
[^0]:    Received August 1976; revised February 1977.
    ${ }^{1}$ Written while the author was a Fellow of the Institute for Advanced Studies on Mt. Scopus. AMS 1970 subject classifications. Primary 62F99, 62J99.
    Key words and phrases. Dimension, Akaike information criterion, asymptotics.

will be established here for the case of independent, identically distributed observations, and linear models.
2. The exact Bayes procedure. In a general parameter space, there is no intrinsic linear structure. We therefore assume that observations come from a Koopman-Darmois family, i.e., relative to some fixed measure on the sample space they possess a density of the form

$$
f(x, \boldsymbol{\theta})=\exp (\boldsymbol{\theta} \cdot \mathbf{y}(x)-b(\boldsymbol{\theta}))
$$

where $\boldsymbol{\theta}$ ranges over the natural parameter space $\Theta$, a convex subset of the $K$ dimensional Euclidean space, and $\mathbf{y}$ is the sufficient $K$-dimensional statistic. The competing models are given by sets of the form $m_{j} \cap \Theta$, where each $m_{j}$ is a $k_{j^{-}}$ dimensional linear submanifold of $K$-dimensional space.

Fitting the asymptotic nature of the result, the a priori distribution need not be known exactly. It suffices to assume that it is of the form $\sum \alpha_{j} \mu_{j}$, where $\alpha_{j}$ is the a priori probability of the $j$ th model being the true one, and $\mu_{j}$, the conditional a priori distribution of $\theta$ given the $j$ th model, has a $k_{j}$-dimensional density that is bounded and locally bounded away form zero throughout $m_{j} \cap \Theta$. This implies mutual orthogonality of the $\mu_{j}$, since the intersection of two distinct linear manifolds either is one of them, or has lower dimensions than both.

Finally, we assume a fixed penalty for guessing the wrong model. (Actually, a loss that depends on $\boldsymbol{\theta}$ and on the guess would yield the same asymptotic results, provided the loss function stays between two fixed positive bounds for all wrong decisions.) Under this assumption, the Bayes solution consists of selecting the model that is a posteriori most probable. Via Bayes' formula that is equivalent to choosing the $j$ that maximizes

$$
S(\mathbf{Y}, n, j)=\log \int \alpha_{j} \exp ((\mathbf{Y} \circ \boldsymbol{\theta}-b(\boldsymbol{\theta})) n) d \mu_{j}(\boldsymbol{\theta})
$$

where the integral extends over $m_{j} \cap \Theta$, and $\mathbf{Y}$ is the averaged $\mathbf{y}$-statistic $(1 / n) \sum \mathbf{y}\left(X_{i}\right)$.
3. Asymptotics. The asymptotic expansion of $S(\mathbf{y}, n, j)$ could be obtained from results in an earlier paper [3] as a special case. We shall, however, keep this paper self-contained by outlining a proof of the necessary result directly.

Proposition. For fixed $\mathbf{Y}$ and $j$, as $n$ tends to $\infty$,

$$
S(\mathbf{Y}, n, j)=n \sup (\mathbf{Y} \circ \boldsymbol{\theta}-b(\boldsymbol{\theta}))-\frac{1}{2} k_{j} \log n+R
$$

where the remainder $R=R(\mathbf{Y}, n, j)$ is bounded in $n$ for fixed $\mathbf{Y}$ and $j$.
Proof. We shall proceed in steps.
Lemma 1. The proposition holds when $\mathbf{Y} \circ \boldsymbol{\theta}-b(\boldsymbol{\theta})=A-\lambda\left\|\boldsymbol{\theta}-\boldsymbol{\theta}_{0}\right\|^{2}$ where $\lambda>0, \boldsymbol{\theta}_{0}$ is a fixed vector in $m_{j}$, and $\mu_{j}$ is Lebesgue measure on $m_{j}$.

Explicit evaluation of the integral yields $\alpha_{j}(\pi / n \lambda)^{k_{j} / 2} e^{n \lambda}$, and

$$
\sup A-\lambda\left\|\boldsymbol{\theta}-\boldsymbol{\theta}_{0}\right\|^{2}=A
$$

Therefore

$$
S(\mathbf{Y}, n, j)=n A-\frac{1}{2} k_{j} \log (n \lambda / \pi)+\log \alpha_{j}
$$

establishes the proposition for this case, with $R=\frac{1}{2} k_{j} \log (\pi / \lambda)+\log \alpha_{j}$.
Lemma 2. If two bounded positive random variables $U$ and $V$ agree on the set where either exceeds $\rho$ for some $0<\rho<\sup U$, then

$$
\log E\left(U^{n}\right)-\log E\left(V^{n}\right) \rightarrow 0
$$

as $n \rightarrow \infty$.
Clearly it suffices to show that this holds for $V$ that vanishes where $U \leqq \rho$. In this case $0 \leqq U^{n}-V^{n} \leqq \rho^{n}$, and therefore

$$
E\left(V^{n}\right) \leqq E\left(U^{n}\right) \leqq E\left(V^{n}\right)+\rho^{n}=E\left(V^{n}\right)\left(1+\frac{\rho^{n}}{E\left(V^{n}\right)}\right)
$$

and we only have to show $\log \left(1+\left(\rho^{n} / E\left(V^{n}\right)\right)\right) \rightarrow 0$. Now $\left(E\left(V^{n}\right)\right)^{1 / n} \rightarrow \sup V$ (a well-known fact on $L_{n}$ norms) and $\sup V=\sup U>\rho$ yield for $\rho /\left(E\left(V^{n}\right)\right)^{1 / n}$ a limit strictly less than 1 , hence $\rho^{n} / E\left(V^{n}\right)$ tends to zero, and so does $\log (1+$ $\left.\left(\rho^{n} / E\left(V^{n}\right)\right)\right)$.

Lemma 3. For some $0<\rho<e^{A}$, where $A=\sup (\mathbf{Y} \circ \boldsymbol{\theta}-b(\boldsymbol{\theta}))$, a vector $\boldsymbol{\theta}_{0}$, and some positive $\lambda_{1}$ and $\lambda_{2}$, the following holds wherever $\exp (\mathbf{Y} \circ \boldsymbol{\theta}-b(\boldsymbol{\theta}))>\rho$ :

$$
A-\lambda_{1}\left\|\boldsymbol{\theta}-\boldsymbol{\theta}_{0}\right\|^{2}<(\mathbf{Y} \circ \boldsymbol{\theta}-b(\boldsymbol{\theta}))<A-\lambda_{2}\left\|\boldsymbol{\theta}-\boldsymbol{\theta}_{0}\right\|^{2}
$$

As is well known, the matrix of second-order derivatives of $b(\boldsymbol{\theta})$ is the covariance matrix of $y$, and hence positive definite. Therefore $\mathbf{Y} \circ \boldsymbol{\theta}-b(\boldsymbol{\theta})$ is strictly convex, and is easily seen to attain its maximum. Let $\boldsymbol{\theta}_{0}$ be the point where the maximum $A$ is attained. The Taylor expansion of $\mathbf{Y} \circ \boldsymbol{\theta}-b(\boldsymbol{\theta})$ around $\boldsymbol{\theta}_{0}$ now yields the stated inequalities for some neighborhood of $\boldsymbol{\theta}_{0}$, if $2 \lambda_{1}$ and $2 \lambda_{2}$ are larger and smaller than all the eigenvalues of the matrix of second order derivatives of $b(\boldsymbol{\theta})$ at $\boldsymbol{\theta}_{0}$. By strict convexity it is now easy to determine $\rho<e^{A}$ so that it will bound $\exp (\mathbf{Y} \circ \boldsymbol{\theta}-b(\boldsymbol{\theta}))$ outside that neighborhood.

The proposition is now proved by combining the lemmas, and the assumption of local boundedness of the density function of $\mu_{j}$ on $m_{j} \cap \Theta$.

Qualitatively both our procedure and Akaike's give "a mathematical formulation of the principle of parsimony in model building." Quantitatively, since our procedure differs from Akaike's only in that the dimension is multiplied by $\frac{1}{2} \log n$, our procedure leans more than Akaike's towards lower-dimensional models (when there are 8 or more observations). For large numbers of observations the procedures differ markedly from each other. If the assumptions we made in Section 2 are accepted, Akaike's criterion cannot be asymptotically optimal. This would contradict any proof of its optimality, but no such proof seems to have been published, and the heuristics of Akaike [1] and of Tong [4] do not seem to lead to any such proof.
