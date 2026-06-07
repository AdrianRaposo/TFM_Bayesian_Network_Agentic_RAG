![img-0.jpeg](img-0.jpeg)

# HAL open science 

## Estimation of Markov Random Field Prior Parameters Using Markov Chain Monte Carlo Maximum Likelihood

Xavier Descombes, Robin Morris, Josiane Zerubia, Marc Berthod

## To cite this version:

Xavier Descombes, Robin Morris, Josiane Zerubia, Marc Berthod. Estimation of Markov Random Field Prior Parameters Using Markov Chain Monte Carlo Maximum Likelihood. RR-3015, INRIA. 1996. inria-00073679

## HAL Id: inria-00073679 <br> https://inria.hal.science/inria-00073679v1

Submitted on 24 May 2006

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L'archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d'enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

# INRIA 

INSTITUT NATIONAL DE RECHERCHE EN INFORMATIQUE ET EN AUTOMATIQUE

## Estimation of Markov Random Field prior parameters using Markov chain Monte Carlo Maximum Likelihood

Xavier Descombes, Robin Morris, Josiane Zerubia, Marc Berthod

$$
\mathbf{N}^{\circ} 3015
$$

October 1996

THÈME 3 $\qquad$
![img-1.jpeg](img-1.jpeg)

.

# JNRIA 

## Estimation of Markov Random Field prior parameters using Markov chain Monte Carlo Maximum Likelihood

Xavier Descombes, Robin Morris, Josiane Zerubia, Marc Berthod<br>Thème 3 - Interaction homme-machine,<br>images, données, connaissances<br>Projet PASTIS<br>Rapport de recherche $\mathrm{n}^{\circ} 3015$ - October 1996 - 28 pages


#### Abstract

Recent developments in statistics now allow maximum likelihood estimators for the parameters of Markov Random Fields to be constructed. We detail the theory required, and present an algorithm which is easily implemented and practical in terms of computation time. We demonstrate this algorithm on three MRF models - the standard Potts model, an inhomogeneous variation of the Potts model, and a long-range interaction model, better adapted to modeling real-world images. We estimate the parameters from a synthetic and a real image, and then resynthesise the models to demonstrate which features of the image have been captured by the model. Segmentations are computed based on the estimated parameters and conclusions drawn.


Key-words: Estimation, Maximum Likelihood, Potts model, Chien-model, image segmentation, image restoration
(Résumé : tsvp)

[^0]
[^0]:    * R.D. Morris was supported by a grant from the Commission of the European Communities under the HCM program.
    ** email: name@sophia.inria.fr

# Estimation au sens du Maximum de Vraisemblance des paramètres d'un modèle markovien par méthode de Monte Carlo 

Résumé : De récents développements en statistiques rendent maintenant possible l'estimation au sens du maximum de vraisemblance des paramètres associés aux champs de Markov. Dans ce rapport, nous détaillons la théorie requise et présentons un algorithme facilement implémentable et abordable du point de vue du temps CPU. Nous appliquons cet algorithme à trois modèles markoviens : le modèle de Potts, une variante inhomogène de ce modèle et au chien-modèle (modèle comprenant des interactions mettant en jeu plus de deux pixels et plus adapté pour modéliser des images réelles). Nous estimons les paramètres à partir d'images de synthèse et d'images réelles, puis re-synthétisons les modèles pour étudier les caractéristiques de l'image captées par le modèle. Nous faisons aussi des segmentations en utilisant les paramèters que nous avons estimés, et nous donnons des conclusions.

Mots-clé : Estimation, Maximum de Vraisemblance, modèle de Potts, chienmodèle, segmentation d'images, restauration d'images

# Contents 

1 Introduction ..... 4
2 Maximum Likelihood estimators ..... 5
2.1 The log-likelihood ..... 5
2.2 Importance sampling ..... 6
3 An MCMCML algorithm ..... 8
3.1 Estimate a robustness criterion ..... 8
3.2 Estimation algorithm ..... 10
4 Validation on Markovian priors ..... 11
4.1 The Potts model ..... 11
4.2 An inhomogeneous variation of the Potts model ..... 11
4.3 The chien-model ..... 14
5 Pros and cons of the priors ..... 18
5.1 Image constraints modeled by priors ..... 18
5.2 Bayesian inference using Markovian priors ..... 18
5.3 Sampling considerations ..... 24
6 Conclusion ..... 26

# 1 Introduction 

Early vision algorithms extract some information from observed data without any specific knowledge about the scene. However, these data (remote sensing data, medical images,...) are usually disturbed by noise. To improve the algorithms, regularization techniques are used, incorporating constraints on the solution. These constraints represent a general knowledge about what a natural scene should be. A popular way to define these constraints is to consider a probabilistic model (the prior) of the expected result. Using the Bayesian approach, we search for a realization which optimizes the probability of the solution, given the data. A key point to obtain unsupervised algorithms in this paradigm is to be able to estimate the different parameters involved in the prior. Accurate estimators of these parameters are necessary to control the impact of the prior on the properties desired for the solution.

Because of their ability to model global properties using local constraints, Markov Random Fields (MRFs) are very popular priors. Several optimization algorithms converging either toward a global minimum of the energy [1] or a local one [2], [3] are now well defined. But accurate estimation of the parameters is still an open issue. Indeed, the partition function (normalization constant) leads to intractable computation. Parameter estimation methods are then either devoted to very specific models [4], [5] or based on approximations such as Maximum Pseudo Likelihood (MPL) [6], [7]. Unfortunately, these approximations lead to inaccurate estimators for the prior parameters. Maximum Likelihood Estimators (MLEs) have more interesting properties. Gidas proves in [8] that MLEs are consistent. Asymptotic normality can be reached in some special case, such as the 2-dimensional Ising model. For high dependency models, the MPL gives poor results as reported in [9]. The aim of MRFs in image processing is to obtained regularized solutions. High dependencies are required to get homogeneous realizations. Thus, MLEs should improve image segmentation and image restoration algorithms based on Markovian priors.

Markov Chain Monte Carlo algorithms (MCMC) [10] are very popular in image processing to derive optimization methods when using a Markovian prior [2], [1]. In fact, MCMC algorithms can be developed for other purposes than Bayesian inference. Indeed, they can be used to derive MLE. The partition function of Gibbs Fields can be estimated using an MCMC procedure.

A Maximum Likelihood estimation using an MCMC algorithm is proposed in [11]. Geyer proves the convergence in probability of the MCMC toward the MLE. This method can be applied to a wide range of models such a Point Processes [12] or Markov Random Fields. In this paper, we propose an estimation algorithm for Markovian prior parameters based on an MCMCML procedure. We validate this algorithm on three different priors.

In section 2, we compute the Maximum Likelihood estimators of a given Gibbs Field whose energy is linear with respect to parameters. Importance sampling is also introduced. This allows us to compute statistics of the model associated with given parameters using samples obtained with other parameter values. These results lead to an MCMCML estimation method described in section 3. Results are detailed in section 4. We consider three different Markovian priors: the Potts model, an inhomogeneous variation of the Potts model and the Chien-model. This Maximum Likelihood estimation allows us to derive some comments about the priors. Section 5 is devoted to a comparison between the priors considered. Finally, we conclude in section 6.

# 2 Maximum Likelihood estimators 

### 2.1 The log-likelihood

Let $P_{\Theta}$ be a random field defined on $S$ and parameterized with vector $\Theta=\left(\theta_{i}\right)$. We consider $P_{\Theta}$ to be a Gibbs Field, whose energy is linear with respect to the parameters $\theta_{i}$. We then have :

$$
P_{\Theta}(Y)=\frac{1}{Z(\Theta)} \exp -\langle\Theta, Y\rangle=\frac{1}{Z(\Theta)} \exp \left[-\sum_{i} \theta_{i} N_{i}(Y)\right]
$$

where $N_{i}(Y)$ are functions of the configuration $Y$. In this paper, we consider a continuous framework for the state space $\Lambda$. Results are still valid in the discrete case by changing integrals into sums. The partition function $Z(\Theta)$ is then written:

$$
Z(\Theta)=\int_{\Lambda^{S}} \exp \left[-\sum_{i} \theta_{i} N_{i}(X)\right] d X
$$

where $S$ is the site set and $\Lambda$ is the state space.

We consider that we have data $Y$. We want to fit the model to the data. The log-likelihood is then defined by :

$$
\begin{gathered}
\log P(Y \mid \Theta)=\log \left[\frac{1}{Z(\Theta)} \exp -\sum_{i} \theta_{i} N_{i}(Y)\right] \\
\log P(Y \mid \Theta)=-\sum_{i} \theta_{i} N_{i}(Y)-\log Z(\Theta)
\end{gathered}
$$

The maximum likelihood estimators are obtained by maximizing the log-likelihood. We then have:

$$
\forall i, \frac{\partial \log P(Y \mid \Theta)}{\partial \theta_{i}}(\hat{\Theta})=0
$$

and then:

$$
\forall i,-N_{i}(Y)+\frac{\int_{\Lambda^{S}} N_{i}(X) \exp \left[-\sum_{i} \hat{\theta}_{i} N_{i}(X)\right] d X}{\int_{\Lambda^{S}} \exp \left[-\sum_{i} \hat{\theta}_{i} N_{i}(X)\right] d X}=0
$$

where $\hat{\theta}_{i}$ is the maximum likelihood estimator of $\theta_{i}$.
Denoting by $\left\langle a(x)\right\rangle_{\Theta}$, the expectation of $a(x)$ with respect to $P_{\Theta}$, we finally get:

$$
\forall i,\left\langle N_{i}(X)\right\rangle_{\hat{\Theta}}=N_{i}(Y)
$$

To evaluate the log-likelihood function, we have to compute the partition function. The partial derivatives of the log-likelihood requires the computation of the different $\left\langle N_{i}(X)\right\rangle_{\Theta}$. Unfortunately, the computation of these quantities is intractable. We can estimate the $\left\langle N_{i}(X)\right\rangle_{\Theta}$ by sampling the distribution. Nevertheless, to sample the distribution for each value of $\Theta$ is inconceivable from CPU time considerations.

# 2.2 Importance sampling 

We introduce importance sampling to avoid having to sample the model for each value of $\Theta$. Indeed, importance sampling allows us to estimate statistical moments corresponding to $P_{\Theta}$ using samples obtained from $P_{\Psi}$.

Consider first the partition function. We have:

$$
Z(\Theta)=\int_{\Omega} \exp \left[-\sum_{i} \theta_{i} N_{i}(X)\right] d X
$$

then:

$$
\begin{aligned}
& Z(\Theta)=\int_{\Omega} \exp \left[-\sum_{i}\left(\theta_{i}-\psi_{i}\right) N_{i}(X)\right] \exp \left[-\sum_{i} \psi_{i} N_{i}(X)\right] d X \\
& Z(\Theta)=\int_{\Omega} \exp \left[-\sum_{i}\left(\theta_{i}-\psi_{i}\right) N_{i}(X)\right] Z(\Psi) d P_{\Psi}(X)
\end{aligned}
$$

For each couple $(\Theta, \Psi)$, the ratio of the partition functions is given by:

$$
\frac{Z(\Theta)}{Z(\Psi)}=E_{\Psi}\left(\exp \left[-\sum_{i}\left(\theta_{i}-\psi_{i}\right) N_{i}(X)\right]\right)
$$

where $E_{\Psi}$ refers to the expectation with respect to the law $P_{\Psi}$.
The partition function corresponding to $P_{\Theta}$ can thus be estimated from the sampling of $P_{\Psi}$. We just have to sample the law with parameter $\Psi$ to get an estimator of the ratio $\frac{Z(\Theta)}{Z(\Psi)}$ for all $\Theta$ by computing from the samples the expectation given by formula (10).

Consider now the log-likelihood. The maximum likelihood estimator is given by the vector $\Theta$ which maximizes formula (3). This is equivalent to minimizing the following expression:

$$
-\log P_{\Theta}(Y)=\sum_{i} \theta_{i} N_{i}(Y)+\log \frac{Z(\Theta)}{Z(\Psi)}
$$

The partial derivative of the partition function can be written:

$$
\begin{aligned}
& \frac{\partial Z(\Theta)}{\partial \theta_{i}}=\int_{\Omega}-N_{i}(X) \exp \left[-\sum_{j}\left(\theta_{j}-\psi_{j}\right) N_{j}(X)\right] Z(\Psi) d P_{\Psi}(X) \\
& \frac{\partial Z(\Theta)}{\partial \theta_{i}}=-Z(\Psi) E_{\Psi}\left(N_{i}(X) \exp \left[-\sum_{j}\left(\theta_{j}-\psi_{j}\right) N_{j}(X)\right]\right)
\end{aligned}
$$

Then, we have:

$$
\frac{\partial-\log P_{\Theta}(Y)}{\partial \theta_{i}}=N_{i}(Y)-\frac{E_{\Psi}\left(N_{i}(X) \exp \left[-\sum_{j}\left(\theta_{j}-\psi_{j}\right) N_{j}(X)\right]\right)}{E_{\Psi}\left(\exp \left[-\sum_{j}\left(\theta_{j}-\psi_{j}\right) N_{j}(X)\right]\right)}
$$

From a sampling of $P_{\Psi}$ we thus can theoretically estimate the log-likelihood of $P_{\Theta}$ and its partial derivatives for all $\Theta$. The same kind of computation allows us to compute the Hessian, and we have:

$$
\frac{\partial^{2}-\log P_{\Theta}(Y)}{\partial \theta_{i} \partial \theta_{j}}=N_{i}(Y) N_{j}(Y)-\frac{E_{\Psi}\left(N_{i}(X) N_{j}(X) \exp -\left[\sum_{k}\left(\theta_{k}-\psi_{k}\right) N_{k}(X)\right]\right)}{E_{\Psi}\left(\exp -\left[\sum_{k}\left(\theta_{k}-\psi_{k}\right) N_{k}(X)\right]\right)}
$$

# 3 An MCMCML algorithm 

### 3.1 Estimate a robustness criterion

Consider an image $Y$ from which we wish to compute the maximum likelihood estimator of $\Theta$ using $P_{\Theta}$ as a model. From the image we can extract the value of the $N_{i}(Y)$. Then, we can sample the law $P_{\Psi}$ for a given $\Psi$. From the samples, the different expectations involved in formulas (10) and (13) can be estimated. Then, for all $\Theta$, we can estimate the log-likelihood and its derivatives. An optimization algorithm (gradient descent, conjugate gradient for example) leads then to the maximum likelihood estimator of $\Theta$, when the log-likelihood is a convex function.

Nevertheless, if the two parameters $\Theta$ and $\Psi$ are too far from each other, the estimation of the expectations will be inaccurate. Indeed, the robustness of the estimation of the expectations requires the overlap between the two distributions $P_{\Theta}$ and $P_{\Psi}$ to be large enough. The proposed method is practically valid only in a neighborhood of parameter $\Psi$. During the optimization, when the current value of $\Theta$ is too far from $\Psi$, we have to re-sample the model using a new value for $\Psi$ (we take the current value of $\Theta$ for $\Psi$ ). Such a sampling requires CPU time. So, we need a criteria to define the neighborhood of $\Psi$ on which the estimation is robust to avoid un-necessary sampling. A first idea is to use a metric between the distributions $P_{\Psi}$ and $P_{\Theta}$ given by:

$$
d\left(P_{\Theta}, P_{\Psi}\right)=\frac{1}{2} \int\left|P_{\Theta}(X)-P_{\Psi}(X)\right| d X
$$

By definition, we have:

$$
P_{\Theta}(X)-P_{\Psi}(X)=\frac{\exp -\langle X, \Theta\rangle}{Z(\Theta)}-\frac{\exp -\langle X, \Psi\rangle}{Z(\Psi)}
$$

$$
P_{\Theta}(X)-P_{\Psi}(X)=\left(\frac{Z(\Psi)}{Z(\Theta)} \exp [-\langle X, \Theta\rangle+\langle X, \Psi\rangle]-1\right) \frac{\exp -\langle X, \Psi\rangle}{Z(\Psi)}
$$

Thus, we define a distance between the distribution by:

$$
\begin{aligned}
\int\left|P_{\Theta}(X)-P_{\Psi}(X)\right| d X & =\int\left|\left(\frac{Z(\Psi)}{Z(\Theta)} \exp [-\langle X, \Theta\rangle+\langle X, \Psi\rangle]-1\right)\right| d P_{\Psi}(X) \\
& =E_{\Psi}\left(\left|\frac{Z(\Psi)}{Z(\Theta)} \exp [-\langle X, \Theta\rangle+\langle X, \Psi\rangle]-1\right|\right)
\end{aligned}
$$

By using formula (10), we then have:

$$
d\left(P_{\Theta}, P_{\Psi}\right)=\frac{1}{2} E_{\Psi}\left(\left|\frac{Z(\Psi)}{Z(\Theta)} \exp [-\langle X, \Theta\rangle+\langle X, \Psi\rangle]-1\right|\right)
$$

We can compute this distance to test the robustness of estimates and decide whether we should sample the model once more or not. However, this distance is also estimated and can be biased. Therefore, we define a heuristic criterion, considering the current samples used for estimating the expectations. For each sample $X_{i}$, we define a weight by:

$$
\begin{gathered}
\omega_{i}=U_{\Theta}\left(X_{i}\right)-U_{\Psi}\left(X_{i}\right) \\
\omega_{i}=\sum_{j}\left(\Theta_{j}-\Psi_{j}\right) N_{j}\left(X_{i}\right)
\end{gathered}
$$

Computing the expectations, we use the following trick to avoid overflow and numerical instabilities:

$$
\sum_{\text {samples } i} \exp \left[-\omega_{i}\right]=\exp \left[-\omega_{\max }\right] \sum_{\text {samples } i} \exp \left[-\left(\omega_{i}-\omega_{\max }\right)\right]
$$

where $\omega_{\max }=\max _{\text {samples }_{i}} \omega_{i}$.
Consider the different samples. If $\omega_{\max }$ is too far from most of the $\omega_{i}$ the quantity $\exp \left[-\left(\omega_{i}-\omega_{\max }\right)\right]$ will be close to 0 and results in a poor estimation. So, we can consider the estimation robust only if $\omega_{\max }-\omega_{\min }$ is lower than a given threshold.

# 3.2 Estimation algorithm 

We can now derive an algorithm based on the conjugate gradient principle. Consider the current parameter estimate $\hat{\Theta}$ and a sampling of $P_{\hat{\Theta}}$. We can estimate the gradient and the Hessian of the log-likelihood function at $\hat{\Theta}$. We then compute the conjugate directions [13]. Along each conjugate direction we define an interval using the distance defined by equation (19), where the log-likelihood estimation is robust. We then maximize the log-likelihood along these intervals.

The algorithm can be written as follows:

1. Compute the $N_{i}(Y)$
2. Initialize $\hat{\Theta}_{0}, n=0$
3. Sample the distribution $P_{\hat{\Theta}_{n}}$
4. Estimate the gradient and the Hessian of the log-likelihood at $\hat{\Theta}_{n}$, using equations (13) and (14)
5. Compute the conjugate directions $\Delta_{i}$
6. For each conjugate direction define a search interval using either the distance defined in equation (19): $I_{i}=\left[\hat{\Theta}_{n}-\alpha_{i} \Delta_{i}, \hat{\Theta}_{n}+\beta_{i} \Delta_{i}\right]$ where $\alpha_{i}=\sup _{\alpha \in \mathbb{R}^{+}}\left\{\alpha: d\left(P_{\hat{\Theta}_{n}}, P_{\hat{\Theta}_{n}-\alpha \Delta_{i}}\right)<T\right\}$,
$\beta_{i}=\sup _{\beta \in \mathbb{R}^{+}}\left\{\beta: d\left(P_{\hat{\Theta}_{n}}, P_{\hat{\Theta}_{n}+\beta \Delta_{i}}\right)<T\right\}$ where $T$ is a threshold, or the proposed heuristic criterion.
7. Compute $\hat{\Theta}_{n+1}$ by maximizing the log-likelihood along each search interval using golden section search [13]
8. if $\left\|\hat{\Theta}_{n+1}-\hat{\Theta}_{n}\right\|>T_{2}$ put $n=n+1$ and go back to 3 , where $T_{2}$ is another threshold.

# 4 Validation on Markovian priors 

In this section, we consider different Markov models used as priors in image processing. We validate the estimation method on these models and demonstrate the generality of its applicability.

### 4.1 The Potts model

The Potts model is commonly used as a prior in image segmentation. It depends on a single parameter $\beta$ and is defined by:

$$
P_{\beta}(X)=\frac{1}{Z(\beta)} \exp \left[-\beta \sum_{c=\left\{s, s^{\prime}\right\} \in \mathcal{C}} \delta_{x_{s} \neq x_{s^{\prime}}}\right]
$$

where $\mathcal{C}$ is the set of cliques. In this case, a clique consists in two neighboring pixels. We consider the case where the lattice $S$ is a subset of $\mathbb{Z}^{2}$. For simulations and estimations we have considered the 4 nearest-neighbors. The Potts model can be embedded in the general form of equation (1):

$$
P_{\beta}(X)=\frac{1}{Z(\beta)} \exp \left[-\beta N_{0}(X)\right]=\frac{1}{Z(\beta)} \exp \left[-\beta \#_{X}\right]
$$

where $N_{0}(X)=\#_{X}$ is the number of inhomogeneous cliques in the configuration $X$. The model depends on one single parameter, so the proposed algorithm is simplified as we do not have to compute the conjugate directions. Table 1 shows estimates obtained using the MCMCML method for different values of $\beta$.

### 4.2 An inhomogeneous variation of the Potts model

We can extend the procedure to the case of a non-stationary Potts model. Consider a Potts mode for which the parameter $\beta$ depends on the localization of the clique. We suppose for simplicity that this dependency is linear and that $\beta$ is written:

$$
\beta_{c=\left\{x_{i, j}, x_{p, q}\right\}}=a\left(\frac{i+p}{2}\right)+b\left(\frac{j+q}{2}\right)+c
$$


Table 1: Estimation of the Potts model parameter

To estimate $\beta$ we have to estimate $a, b$ and $c$. The associated distribution is written:

$$
P_{a, b, c}(X)=\frac{1}{Z(a, b, c)} \exp \left[-\sum_{c=\left\{s, s^{\prime}\right\} \in \mathcal{C}}\left(a\left(\frac{i+p}{2}\right)+b\left(\frac{j+q}{2}\right)+c\right) \delta_{x_{s} \neq x_{s^{\prime}}}\right]
$$

This model can be written in the form of equation (1):

$$
P_{a, b, c}(X)=\frac{1}{Z(a, b, c)} \exp \left[-c N_{0}(X)-b N_{1}(X)-a N_{2}(X)\right]
$$

where:

$$
\begin{aligned}
& N_{0}(X)=\#_{X}, \text { the number of inhomogeneous cliques } \\
& N_{1}(X)=\sum_{\text {inhomogeneous cliques }} \frac{j+q}{2}=N_{0}(X)\left\langle\frac{j+q}{2}\right\rangle_{\text {inh.cl. }} \\
& N_{2}(X)=\sum_{\text {inhomogeneous cliques }} \frac{i+p}{2}=N_{0}(X)\left\langle\frac{i+p}{2}\right\rangle_{\text {inh.cl. }}
\end{aligned}
$$

Table 2 shows samples from this model and the parameters estimated from these samples.








Sample
![img-2.jpeg](img-2.jpeg)
![img-3.jpeg](img-3.jpeg)

Table 2: Estimation of an inhomogeneous variation of the Potts model.

# 4.3 The chien-model 

To improve segmentations some more complex models have been proposed in the last few years. These models consider cliques of more than two pixels to define more accurately local configurations and their contribution to the model. Such a model based on $3 \times 3$ cliques was proposed in [14]. Another model on an hexagonal lattice can be found in [15]. These models consider only the clique configurations. In [16], a binary model (the chien-model) taking into account links between neighboring cliques is proposed. This model has been generalized to the m-ary case in [17]. This model, although regularizing, preserves fine structures and linear shapes in images. In this model, the set of cliques is composed of $3 \times 3$ squares. The chien-model is defined from the discrimination between noise, lines and edges. Three parameters ( $n, l$ and $e$ ) are associated to these patterns.

Before constructing the model the different configurations induced by a $3 \times 3$ square are classified using the symmetries (symmetry black-white, rotations, etc.) This classification and the number of elements in each class are
![img-4.jpeg](img-4.jpeg)

Figure 1: The different classes induced by a binary $3 \times 3$ model and their number of elements
described in Figure 1. A parameter is associated to each class and refers to the value of the potential function for the considered configuration. So, under the

hypothesis of isotropy of the model which induces the symmetries, we have for such a topology (cliques of $3 \times 3$ ) fifty one degrees of freedom. The construction of the model consists in imposing constraints by relations between its parameters. Two energy functions which differ only by a constant are equivalent, so we suppose that the minimum of the energy is equal to 0 . The global realization of 0 energy are called the ground states of the model and represent the realization of maximal probability. We suppose that uniform realizations are ground states, so we have the first equation for the parameters given by $C(1)=0$. We then define the different constraints with respect to those two uniform realizations. The first class of constraints concerns the energy of edges which is noted $e$ per unit of length. Due to symmetries and rotations we just have to define three orientations of edges corresponding to the eight ones induced by the size of cliques. These constraints and the derived equations are represented on figure 2. These constraints are defined for features of width at
![img-5.jpeg](img-5.jpeg)

Figure 2: Equations associated with edges constraints
least equal to 3. For other features, we have to define other constraints. When the width of the considered object is one pixel, it is referred as a line and has energy per unit $l$. For larger features (double and triple lines), we consider that the energy per unit is given by $2 \times e$, which correspond to left and right edge, and get more equations. All these constraints induce eleven equations which depend on fourteen parameters leading to the following solution (see [16] for full details):

$$
\begin{gathered}
C(3)=C(5)=\frac{e}{4} \quad C(26)=l-e \quad C(14)=\frac{\sqrt{2} e}{4} \\
C(16)=C(23)=\frac{\sqrt{5}}{6} l-\frac{e}{4} \quad C(11)=C(28)=\frac{\sqrt{2} l}{3}-\frac{e}{6} \\
C(35)=\frac{\sqrt{2} e}{2} \quad C(29)=\frac{\sqrt{5} e}{6} \quad C(13)=C(9)=C(19)=\frac{e}{2}
\end{gathered}
$$

Noise is defined by assigning to every other configuration a positive value $n$.

To extend the binary chien-model in an m-ary model, we define the energy of a given configuration as the sum of several energies given by the binary model. Consider a configuration and a given label $\sigma_{0}$. We put every pixels of the configuration which are in state $\sigma_{0}$ to 0 and others to 1 . We then have a binary configuration. The energy of the m-ary model is the sum of the energies obtained by these deduced binary configurations for the $m$ labels (see figure 3). The potential associated with each configuration is then a linear combination
![img-6.jpeg](img-6.jpeg)

Figure 3: M-ary extension of the chien-model
of the three parameters $e, l$ and $n$ :

$$
\forall i=0, \ldots, 51 C(i)=\epsilon(i) e+\lambda(i) l+\eta(i) n
$$

The resulting distribution is written:

$$
P_{e, l, n}(X)=\frac{1}{Z(e, l, n)} \exp \left[-e N_{0}(X)-l N_{1}(X)-n N_{2}(X)\right]
$$

where:

$$
\begin{aligned}
& N_{0}(X)=\sum_{i=1, \ldots, 51} \epsilon(i) \#_{i}(X) \\
& N_{1}(X)=\sum_{i=1, \ldots, 51} \lambda(i) \#_{i}(X) \\
& N_{2}(X)=\sum_{i=1, \ldots, 51} \eta(i) \#_{i}(X)
\end{aligned}
$$

$\#_{i}(X)$ being the number of configurations of type $i$ in the realization $X$.
Results are summarized in table 3. The chosen parameter values show the properties of the model. Indeed, we can control the total length of edges as well as the total length of lines. Moreover, parameter $n$ allows us to control the amount of noise. The table also shows that we can accurately estimate the parameters of this model.








Sample
![img-7.jpeg](img-7.jpeg)
![img-8.jpeg](img-8.jpeg)

Table 3: Estimation of chien-model parameters

# 5 Pros and cons of the priors 

### 5.1 Image constraints modeled by priors

In this section, we provide tests to evaluate the properties the different models can incorporate into, for example, a segmentation result. First, we consider a binary synthetic image (see figure 4.a). A segmented SPOT image is the second proposed test (see figure 4.b). We estimate the corresponding parameters for each model and then synthesize the model using estimated parameters. In this way, we can observe the properties of the initial image which are captured by the different models. We first consider the synthetic image shown in figure 4.a. Results obtained for the Potts and chien models using a MCMCML estimation are summarized in table 4. As we consider a general model for segmented images, the realization of the models are visually far from the original image. Nevertheless, we can point out that in the case of the Potts model, the only image characteristic represented in the simulation is the number of inhomogeneous cliques. For a given number of inhomogeneous cliques, there are many more configurations composed of an uniform background with noise than configurations composed of several homogeneous shapes. Therefore, using estimated parameters, the Potts model does not seem to be a regularizing prior. As it considers cliques of $3 \times 3$ pixels, the chien-model allows us to define edge and line lengths. The realization of the chien-model obtained with estimated parameters contains different shapes. The global edge and line lengths are the same as the original image. Therefore, it seems more appropriate to be used as a prior for image modeling.

### 5.2 Bayesian inference using Markovian priors

We consider in this subsection a classical application to validate the previous assertions concerning the priors in this study. We first consider a noisy version of the binary synthetic image shown on figure 4.a. The original image is corrupted by a channel noise of ratio $0.15(15 \%$ of the original pixels are reversed) (see figure 5). We perform a restoration in a Bayesian framework.

Denote the noisy image by $X=\left(x_{s}\right)_{s \in S}$ and the restored image by $Y=$ $\left(y_{s}\right)_{s \in S}$ where $S$ is the lattice and $s=(i, j)$ is a pixel. The data are $X$ and we search for $Y$ which minimizes some cost function under the probability

![img-9.jpeg](img-9.jpeg)
a: Binary synthetic image
b: Segmented SPOT image, 5 classes
Figure 4: Test images: $256 \times 256$
![img-10.jpeg](img-10.jpeg)
a: channel noise corrupted $(\tau=0.15)$
b: SPOT image

Figure 5: Test images: $256 \times 256$


Table 4: Comparison of Potts model and chien-model as prior for the binary synthetic image


Table 5: Comparison of Potts model and chien-model as prior for a segmented SPOT image

$P(Y \mid X)$. Using Bayes law, we have:

$$
P(Y \mid X)=\frac{P(X \mid Y) P(Y)}{P(X)} \propto P(X \mid Y) P(Y)
$$

$P(Y)$ is defined by the prior whereas $P(X \mid Y)$ represents the data attachment term. As we have considered an uncorrelated channel noise of ratio 0.15 , we have:

$$
\forall s \in S,\left\{\begin{array}{l}
p\left(x_{s}=0 \mid y_{s}=0\right)=0.85 \\
p\left(x_{s}=1 \mid y_{s}=0\right)=0.15 \\
p\left(x_{s}=0 \mid y_{s}=1\right)=0.15 \\
p\left(x_{s}=1 \mid y_{s}=1\right)=0.85
\end{array}\right.
$$

The global probability $P(X \mid Y)$ is written as follows:

$$
P(X \mid Y)=\prod_{s \in S} p\left(x_{s} \mid y_{s}\right)=\exp \sum_{s \in S} \ln p\left(x_{s} \mid y_{s}\right)
$$

We consider a prior given by equation (1). We then have:

$$
P(Y \mid X) \propto \frac{1}{Z(\Theta)} \exp \left[-\sum_{i} \theta_{i} N_{i}(Y)+\sum_{s \in S} \ln p\left(x_{s} \mid y_{s}\right)\right]
$$

As $P(Y)$ is a Markov Random Field, $N_{i}(Y)$ is written as a sum of local potentials: $\sum_{c \in \mathcal{C}} V_{c}\left(y_{s}, s \in c\right)$. We use the Maximiser of the Posterior Marginal (MPM) estimate, found using a Gibbs Sampler [18].

The results obtained are shown in table 6. The restored image obtained with the Potts model is still noisy. It is not surprising when we consider the simulation shown in table 4. However, we can find in the literature better restorations using a Potts model as a prior. In that case the parameter $\beta$ is increased in order to over-regularize the solution. By using this trick, the noise is erased but details are lost (see figure 6). In some cases, the parameter $\beta$ is estimated using a Maximum Pseudo-likelihood criteria [19]. Such an estimator tend to over-estimate the parameter [11]. The chien model, however, successfully regularises the segmentation. The noise is removed and for the most part the structures in the image are retained. The model has truly captured the salient characteristics of the original image.


Table 6: Segmentation of a noisy binary image using MCMCML estimators for the prior parameters
![img-13.jpeg](img-13.jpeg)

Figure 6: Restoration of figure 5 with a Potts model over-regularizing $(\beta=1.0)$

We now consider the original SPOT image (see figure 5.b). We compare the behavior of the models being studied when segmenting this image. We suppose that each of the five classes can be represented by a normal law. The means and variances of these classes are estimated using the empirical estimators on the subsets defined on figure 4.b. The conditional probability $P(Y \mid X)$ is then written as follows:
$P(Y \mid X) \propto \frac{1}{Z(\Theta)} \exp \left[-\sum_{i} \theta_{i} N_{i}(Y)+\sum_{s \in S} \sum_{\operatorname{class} c}\left(\frac{\left(x_{s}-\mu_{c}\right)^{2}}{2 \sigma_{c}}-\ln \left(2 \pi \sigma_{s}^{2}\right)\right) \delta_{y_{s}=c}\right]$
This distribution is sampled and an MPM estimation performed. The resulting segmentations using the Potts model and the chien model are given in table 7. Both segmentations are close to that shown in figure 4. This is because the data (figure 5.b) is very clear and noise free - it is in effect easy to segment; little regularisation is required. The errors in the segmentations occur at the edges of the regions. This partially explains the apparent success in the literature of segmentations performed with the Potts model as prior - in many cases the precise form of the regularisaton is unimportant. As we have seen with the binary image corrupted by channel noise, this is not always true and accurate prior modeling is important in these cases.

# 5.3 Sampling considerations 

In the proposed MCMCML algorithm, more than $99 \%$ of the required CPU time consists in sampling the model. Computing the log-likelihood and its derivatives is very fast when we have the samples, indeed, once the samples are in place performing the maximum likelihood estimation takes less than a minute on a Sun-20. This sampling is obtained using a Metropolis-Hasting algorithm. We first have to iterate the algorithm until we reach convergence and then achieve enough iterations to get accurate estimates of the different statistical moments involved in the MCMCML estimation. Among MetropolisHasting algorithms, the Gibbs Sampler is the most used in image processing. However, when considering the Potts model the Swendsen-Wang algorithm [20] is more efficient. The Swendsen-Wang algorithm considers clusters instead of pixels. The convergence rate is then faster than a single site updating algorithm. Moreover, as it moves freely within the distribution, we need fewer


Table 7: Segmentation of a SPOT using MCMCML estimators for the prior parameters

samples to obtain accurate estimates of the statistical moments than when using a Gibbs Sampler. Unfortunately, this algorithm can not be applied to the Chien-model. Finding an auxiliary variable to define clusters in this case is still an open issue. In a CPU time point of view, users may then prefer the Potts model.

Notice that, for given parameters, we only ever have to sample the model once. To compute the estimation, we need for each sample the values of the $N_{i}$. We can store these values in a data base. The parameter space can be discretized. The discretization step depends on the robustness of the importance sampling. Once we have sample the model for each value of the discrete parameter space the proposed algorithm requires a few seconds on a SUN 20. We can initialize the parameters with the values corresponding to the closest $<N_{i}>$ in the data base and derive the estimators without further sampling of the model.

# 6 Conclusion 

In this paper, we have used recent development in statistics to propose an algorithm performing maximum likelihood estimation of Markovian prior parameters. Using importance sampling, the proposed algorithm avoids too much sampling which would require huge CPU time. Moreover, a data base can be computed which suppresses sampling. We are currently working on such a data base.

Using the maximum likelihood criterion leads to accurate estimators of the prior parameters. Therefore, we can compare the different priors and the regularizing properties they handle. In this paper, we have considered three Markovian priors: the Potts model and a nonstationary variation of this model, and the Chien-model. The property handled by the two first models consists essentially of homogeneous cliques. The chien model seems more appropriate to image processing as it controls image features (edge length, line length, noise) independently. On the other hand, this model requires more CPU time as it considers higher order interactions. The quality of the data can also influence on a practical level the choice of a priori model.
