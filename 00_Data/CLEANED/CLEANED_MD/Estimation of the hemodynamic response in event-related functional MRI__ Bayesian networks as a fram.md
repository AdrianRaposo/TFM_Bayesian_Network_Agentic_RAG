![img-0.jpeg](img-0.jpeg)

# Estimation of the hemodynamic response in event-related functional MRI: Bayesian networks as a framework for efficient Bayesian modeling and inference. 

Guillaume Marrelec, Philippe Ciuciu, Mélanie Pélégrini-Issac, Habib Benali

## To cite this version:

Guillaume Marrelec, Philippe Ciuciu, Mélanie Pélégrini-Issac, Habib Benali. Estimation of the hemodynamic response in event-related functional MRI: Bayesian networks as a framework for efficient Bayesian modeling and inference.. IEEE Transactions on Medical Imaging, 2004, 23 (8), pp.959-67. 10.1109/TMI.2004.831221 . cea-00333687

## HAL Id: cea-00333687 <br> https://cea.hal.science/cea-00333687v1

Submitted on 23 Oct 2008

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L'archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d'enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

# Estimation of the Hemodynamic Response in Event-Related Functional MRI: Bayesian Networks as a Framework for Efficient Bayesian Modeling and Inference 

Guillaume Marrelec*, Philippe Ciuciu, Member, IEEE, Mélanie Pélégrini-Issac, and<br>Habib Benali, Senior Member, IEEE


#### Abstract

A convenient way to analyze blood-oxygen-level-dependent functional magnetic resonance imaging data consists of modeling the whole brain as a stationary, linear system characterized by its transfer function: the hemodynamic response function (HRF). HRF estimation, though of the greatest interest, is still under investigation, for the problem is ill-conditioned. In this paper, we recall the most general Bayesian model for HRF estimation and show how it can beneficially be translated in terms of Bayesian graphical models, leading to 1) a clear and efficient representation of all structural and functional relationships entailed by the model, and 2) a straightforward numerical scheme to approximate the joint posterior distribution, allowing for estimation of the HRF, as well as all other model parameters. We finally apply this novel technique on both simulations and real data.


Index Terms-Bayesian inference, Bayesian networks, functional MRI, hemodynamic response function.

## I. INTRODUCTION

FUNCTIONAL magnetic resonance imaging (fMRI) is a noninvasive technique allowing for the evolution of brain processes to be dynamically followed in various cognitive and behavioral tasks [1]. In the most common fMRI technique, based on the so-called blood-oxygen-level-dependent (BOLD) contrast, the measure is only indirectly related to neuronal activity through a process that is still under investigation [2]-[4]. For this reason, a convenient way to analyze BOLD fMRI data consists of modeling the whole brain as a stationary, linear "black box" system characterized by its transfer response function, also called hemodynamic response function (HRF)

[^0][5]. This model, called general linear model (GLM), fairly well accounts for the properties of the real system as long as the inter-stimulus interval does not decrease beyond about two seconds [6], [7]. When this constraint is not respected, other models have to be developed [8], [9].

Estimation of the HRF is of the greatest interest when analyzing fMRI data, since it can give a deep insight into the underlying dynamics of brain activation and the relationships between activated areas. HRFs are increasingly suspected to vary from region to region, from task to task, and from subject to subject [10]-[12]. Age and disease are also more and more believed to have a significant influence on the BOLD response [13], [14]. Nevertheless, accurate estimation of the response function still belongs to ongoing research, since the problem is badly conditioned. Various nonparametric methods have been developed so far in an attempt to infer the HRF at each time sample, such as selective averaging [6], averaging over regions [15], introduction of nondiagonal models for the temporal covariance of the noise [16], or temporal regularization [17].

In [18] and [19], we proposed a Bayesian nonparametric estimation of the HRF for event-related designs. Basic yet relevant physiological information was introduced to temporally constrain the problem and calculate robust estimators of the parameters of interest. In [20]-[22], the model was extended to account for asynchronous event-related designs, different trial types, and several fMRI sessions, further improving the estimation. For calculation reasons, all variants proposed so far have, however, the drawback of not integrating the hyperparameter uncertainty. Furthermore, probabilistic treatment of the drift parameters in the extended model was possible [23], [24], but at a significantly higher computational cost.

In this paper, we propose to cast a new light on the GLM. We still place ourselves in a Bayesian framework, permitting integration of information originating from various sources and efficient inference on the parameters of interest. A general model is set to account for most event-related fMRI data. In a conventional Bayesian approach, we would then calculate the joint posterior distribution of all parameters, which would be the pivotal quantity for all further inference. Since direct sampling from this probability density function (pdf) would prove impossible, Monte Carlo Markov chain (MCMC) sampling would be required, such as Gibbs sampling [25], [26]. In this case, posterior conditional pdfs should be derived. In this perspective,


[^0]:    Manuscript received January 5, 2004; revised May 3, 2004. The work of G. Marrelec was supported by the Fondation pour la Recherche Médicale. This paper is an extension of [33] that appeared in the IPMI'03 Proceedings. The Guest Editors responsible for coordinating the review of this paper and recommending its publication were C. J. Taylor and J. A. Noble. Asterisk indicates corresponding author.Asterisk indicates corresponding author.
    ${ }^{*} \mathrm{G}$. Marrelec is with INSERM U494, CHU Pitié-Salpêtrière, 91 boulevard de l'Hôpital, 75634 Paris Cedex 13, France and also with the IFR 49, Orsay, France.
    H. Benali are with INSERM U494, CHU Pitié-Salpêtrière, 91 boulevard de l'Hôpital, 75634 Paris Cedex 13, France, and also with the IFR 49, Orsay, France.
    P. Ciuciu is with SHFJ/CEA/INSERM U562, 91401 Orsay, France, and also with the IFR 49, Orsay, France.
    M. Pélégrini-Issac is with INSERM U483, 9 quai Saint Bernard, 75005 Paris, and also with the IFR 49, Orsay, France.
    Digital Object Identifier 10.1109/TMI.2004.831221

we advocate that calculation of the posterior pdf is unncessary. Instead, we resort to a novel approach that focuses on graphical modeling and that, once the model has been properly set, makes it possible to directly lead probabilistic inference about all parameters. More precisely, we utilize graph theory [27] to conveniently deal with the model. Indeed, graphs give a very simple and efficient representation of the model, however complex it may be. In this framework, we translate the model into a Bayesian network. Using Markov properties of such networks, drawing inference becomes straightforward, and Gibbs sampling finally provides us with a numerical approximation of the joint posterior pdf.

In the next part of this paper, we develop the general Bayesian framework for HRF estimation, presenting an extended version of the GLM. In Section III, the GLM is translated in terms of graphical model, and it is shown how inference can readily be performed from there. We briefly present simulations and finally apply our model to real data.

## II. HRF Estimation in fMRI Data Analysis

## A. Notations

In the following, $x$ denotes a real number, $\boldsymbol{x}$ a vector, and $\boldsymbol{X}$ a matrix. For the sake of simplicity, $\left(x_{i}\right)$-between parentheses-is a shortcut for $\left(x_{i}\right)_{1 \leq i \leq I}$. " " is the regular matrix transposition. $\boldsymbol{I}_{N}$ stands for the $N \times N$ identity matrix. " $\propto$ " relates two expressions that are proportional. For two variables $x$ and $y$, " $x \mid y$ " stands for " $x$ given $y$," and $\mathrm{p}(x)$ for the probability of $x . \mathcal{N}(\boldsymbol{m}, \boldsymbol{V} ; \boldsymbol{x})$ is the Gaussian density function with mean $\boldsymbol{m}$ and covariance matrix $\boldsymbol{V}$ calculated at sample $\boldsymbol{x}$. Inv- $\chi^{2}\left(d, r^{2} ; u\right)$ is the scaled inverse-chi-square density function ${ }^{1}$ with $d$ degrees of freedom and scale parameter $r^{2}$ evaluated at sample $u$.

## B. General Linear Model

Let an fMRI experiment be composed of $S$ sessions, each session involving $I$ different stimulus types. Define $\boldsymbol{y}_{s}=\left(y_{s, t_{s, n}}\right)_{1 \leq n \leq N_{s}}$ as the BOLD fMRI time course of a voxel (i.e., volume element) at (not-necessarily uniformly sampled) times $\left(t_{s, n}\right)$ for session $s$, and $\boldsymbol{x}_{s, i}=\left(x_{s, i, t}\right)_{t_{s, 0} \leq t \leq t_{s, N_{s}}}$ the corresponding binary time series, composed of the $i$ th stimulus onsets. The following discrete linear convolution model $(H)$ is assumed to hold between the stimuli and the data
$y_{s, t_{s, n}}=\sum_{i=1}^{I} \sum_{k=0}^{K_{i}} x_{s, i, t_{s, n}-k \Delta t} h_{i, k \Delta t}+\sum_{m=1}^{M_{s}} d_{m, t_{s, n}} \lambda_{s, m}+e_{t_{n}}$ $n=n_{s}+1, \ldots, N_{s}$, where $n_{s}$ is the largest integer so, that $t_{s, n}-K_{i} \Delta t<t_{s, 1}$ for all $i$. The $\left(K_{i}+1\right)$-dimensional vector $\boldsymbol{h}_{i}=\left(h_{i, k \Delta t}\right)^{t}$ represents the $i$ th unknown HRF to be estimated, sampled every $\Delta t$. All HRFs are assumed to be constant across sessions. $L_{s}=N_{s}-n_{s}$ is the actual amount of data used in the calculation for each session. $\boldsymbol{X}_{s, i}=\left(x_{s, i, t_{s, n}-k \Delta t}\right)$ is the regular $L_{s}$-by- $\left(K_{i}+1\right)$ design matrix, consisting of the lagged stimulus covariates. In the $L_{s}$-by- $M_{s}$ matrix $\boldsymbol{D}_{s}=\left(d_{m, t_{s, n}}\right)$

[^0]are the values at times $\left(t_{s, n}\right)$ of a basis of $M_{s}$ functions that takes a potential drift and any other nuisance effect into account, and $\boldsymbol{\lambda}_{s}=\left(\lambda_{s, m}\right)^{t}$ contains the corresponding coefficients. For the sake of simplicity, the basis is assumed to be orthonormal, so that $\left(1 / L_{s}\right) \boldsymbol{D}_{s} \boldsymbol{D}_{s}^{t}=\boldsymbol{I}_{L_{s}}$. Vector $\boldsymbol{e}_{s}=\left(e_{s, t_{s, n}}\right)^{t}$ accounts for noise and is supposed to consist of independent and identically distributed Gaussian variables of unknown variance $\sigma_{s}^{2}$, assumed to be independent from the HRFs. In matrix form, $(H)$ boils down to

$$
\boldsymbol{y}_{s}=\sum_{i=1}^{I} \boldsymbol{X}_{s, i} \boldsymbol{h}_{i}+\boldsymbol{D}_{s} \boldsymbol{\lambda}_{s}+\boldsymbol{e}_{s}, \quad s=1, \ldots, S
$$

also called general linear model (GLM). In this model, the likelihood of the data yields

$$
\begin{aligned}
& \mathrm{p}\left(\left(\boldsymbol{y}_{s}\right) \mid H,\left(\boldsymbol{h}_{i}\right),\left(\sigma_{s}^{2}\right),\left(\boldsymbol{\lambda}_{s}\right)\right) \\
& \quad=\prod_{s=1}^{S} \mathrm{p}\left(\boldsymbol{y}_{s} \mid H,\left(\boldsymbol{h}_{i}\right), \sigma_{s}^{2}, \boldsymbol{\lambda}_{s}\right)
\end{aligned}
$$

with each term in the product reading

$$
\begin{aligned}
& \mathrm{p}\left(\boldsymbol{y}_{s} \mid H,\left(\boldsymbol{h}_{i}\right), \sigma_{s}^{2}, \boldsymbol{\lambda}_{s}\right) \\
& \quad=\mathcal{N}\left(\sum_{i=1}^{I} \boldsymbol{X}_{s, i} \boldsymbol{h}_{i}+\boldsymbol{D}_{s} \boldsymbol{\lambda}_{s}, \sigma_{s}^{2} \boldsymbol{I}_{L_{s}} ; \boldsymbol{y}_{s}\right)
\end{aligned}
$$

## C. HRFs and Hyperparameters

In its general form, the GLM is usually ill-conditioned, for there are too many parameters to estimate compared to the information brought by the data. Prior information must, hence, be incorporated in order to constrain the problem. Since the underlying physiological process of BOLD fMRI is as of yet only partially understood, we set the following soft constaints [18], [21].
P1) The HRFs start and end at 0 . This amounts to setting the first and last samples of each HRF to 0 , so that only $K_{i}-1$ parameters (instead of $K_{i}+1$ ) are now unknown.
P2) The HRFs are smooth. Quantification is achieved by setting Gaussian priors for the norm of the second derivative of the HRFs, whose variances are adjusted by hyperparameters $\epsilon_{i}$ 's. More precisely, we assume that

$$
\begin{array}{r}
\mathrm{p}\left(\boldsymbol{h}_{i} \mid H, \epsilon_{i}^{2}\right) \propto \exp \left[\frac{1}{2 \epsilon_{i}^{2}}\left\|\partial^{2} \boldsymbol{h}_{i}\right\|^{2}\right] \\
i=1, \ldots, I
\end{array}
$$

Following usual practice, $\partial^{2} \boldsymbol{h}_{i}$ can be discretized as
$\left(\partial^{2} \boldsymbol{h}\right)_{i, k \Delta t} \approx \frac{h_{i,(k+1) \Delta t}-2 h_{i, k \Delta t}+h_{i,(k-1 \Delta t)}}{(\Delta t)^{2}}$
for $k=1, \ldots, K_{i}-1$. Taking into account that $h_{i, 0}=$ $h_{i, K}=0$, we obtain in matrix form

$$
\partial^{2} \boldsymbol{h}_{i}=\boldsymbol{D}_{2, i} \boldsymbol{h}_{i}
$$

where $\boldsymbol{D}_{2, i}$ is the following $\left(K_{i}-1\right) \times\left(K_{i}-1\right)$ matrix:

$$
\boldsymbol{D}_{2, i}=\frac{1}{(\Delta t)^{2}}\left(\begin{array}{cccccc}
-2 & 1 & 0 & & & \\
1 & -2 & 1 & 0 & & \\
0 & 1 & -2 & 1 & 0 & & \\
& \ddots & \ddots & \ddots & \ddots & \ddots & \\
& & 0 & 1 & -2 & 1 & 0 \\
& & & 0 & 1 & -2 & 1 \\
& & & & 0 & 1 & -2
\end{array}\right)
$$


[^0]:    ${ }^{1}$ If $n$ is chi-square distributed with $d$ degrees of freedom, then $d r^{2} / n$ is scaled inverse-chi-square distributed with $d$ degrees of freedom and scale parameter $r^{2}$. Equivalently, a scaled inverse-chi-square distribution Inv- $\chi^{2}\left(d, r^{2}\right)$ is a special case of the inverse Gamma distribution Inv- $\Gamma(\alpha, \beta)$, with $\alpha=d / 2$ and $\beta=$ $d r^{2} / 2$. See the Appendix for the exact expression of the corresponding pdf.

Hence

$$
\begin{aligned}
\left\|\partial^{2} \boldsymbol{h}_{i}\right\|^{2} & =\left(\boldsymbol{D}_{2, i} \boldsymbol{h}_{i}\right)^{t}\left(\boldsymbol{D}_{2, i} \boldsymbol{h}_{i}\right) \\
& =\boldsymbol{h}_{i}^{t}\left(\boldsymbol{D}_{2, i}^{t} \boldsymbol{D}_{2, i}\right) \boldsymbol{h}_{i}
\end{aligned}
$$

Finally, we obtain for $\boldsymbol{h}_{i}$ :

$$
\mathrm{p}\left(\boldsymbol{h}_{i} \mid H, \epsilon_{i}^{2}\right)=\mathcal{N}\left(\mathbf{0}, \epsilon_{i}^{2} \boldsymbol{R}_{i}^{-1} ; \boldsymbol{h}_{i}\right) \quad i=1, \ldots, I
$$

where $\boldsymbol{R}_{i}=\boldsymbol{D}_{2, i}^{t} \boldsymbol{D}_{2, i}$ is the following ( $K_{i}-$ 1)-by- $\left(K_{i}-1\right)$ symmetrical positive definite matrix

$$
\begin{aligned}
& \boldsymbol{R}_{i}=\frac{1}{(\Delta t)^{4}} \\
& \times\left(\begin{array}{cccccccc}
5 & -4 & 1 & 0 & & \cdots & & & 0 \\
-4 & 6 & -4 & 1 & 0 & & & \\
1 & -4 & 6 & -4 & 1 & 0 & & \\
0 & 1 & -4 & 6 & -4 & 1 & 0 & & \\
& \ddots & \ddots & \ddots & \ddots & \ddots & \ddots & \ddots & \\
\vdots & & 0 & 1 & -4 & 6 & -4 & 1 & 0 \\
& & & 0 & 1 & -4 & 6 & -4 & 1 \\
& & & & & 0 & 1 & -4 & 6 & -4 \\
0 & & & & \cdots & 0 & 1 & -4 & 5
\end{array}\right) .
\end{aligned}
$$

P3) No prior dependence is assumed between HRFs, so that

$$
\mathrm{p}\left(\left(\boldsymbol{h}_{i}\right),\left(\epsilon_{i}^{2}\right) \mid H\right)=\prod_{i=1}^{I} \mathrm{p}\left(\boldsymbol{h}_{i} \mid H, \epsilon_{i}^{2}\right) \cdot \mathrm{p}\left(\epsilon_{i}^{2} \mid H\right)
$$

For convenience reasons, the priors for $\epsilon_{i}^{2}$ 's are set as conjugate priors, i.e., these parameters are assumed to be a priori independent identically distributed with common pdf a scaled inverse- $\chi^{2}$ with $n_{\epsilon}$ degrees of freedom and scale parameter $r_{\epsilon}^{2}$ given in the model ( $n_{\epsilon}$ set to a small value to obtain a "hardly" informative prior). This setting is further precised later and also analyzed in the discussion.

## D. Drifts and Noise Variances

Unlike the HRFs, noise variances and drift parameters may vary across sessions. Each $\sigma_{\delta}^{2}$ is assumed to follow a scaled in-verse- $\chi^{2}$ distribution with $n_{\sigma, \delta}$ degrees of freedom and scale parameter $r_{\sigma, \delta}^{2}$. Each $\boldsymbol{\lambda}_{\boldsymbol{s}}$ is assumed to be Gaussian distributed with mean $\boldsymbol{m}_{\lambda, \delta}$ and covariance matrix $\boldsymbol{V}_{\lambda, \delta}$.

## E. Joint Posterior Distribution

Considering the model so constructed and assuming no further prior dependence between parameters, formal application of the chain rule yields

$$
\begin{aligned}
& \mathrm{p}\left(\left(\boldsymbol{y}_{\mathrm{s}}\right),\left(\epsilon_{i}^{2}\right),\left(\boldsymbol{h}_{i}\right),\left(\sigma_{\delta}^{2}\right),\left(\boldsymbol{\lambda}_{\mathrm{s}}\right) \mid H\right) \\
& =\prod_{\delta=1}^{S} \mathrm{p}\left(\boldsymbol{y}_{\mathrm{s}} \mid H,\left(\boldsymbol{h}_{i}\right), \sigma_{\delta}^{2}, \boldsymbol{\lambda}_{\mathrm{s}}\right) \\
& \times \mathrm{p}\left(\boldsymbol{\lambda}_{\mathrm{s}} \mid H\right) \cdot \mathrm{p}\left(\sigma_{\delta}^{2} \mid H\right) \\
& \cdot \prod_{i=1}^{I} \mathrm{p}\left(\boldsymbol{h}_{i} \mid H, \epsilon_{i}^{2}\right) \cdot \mathrm{p}\left(\epsilon_{i}^{2} \mid H\right)
\end{aligned}
$$

Given data $\left(\boldsymbol{y}_{\mathrm{s}}\right)$, our knowledge relative to the model parameters can easily be updated using the conditioning formula

$$
\begin{aligned}
& \mathrm{p}\left(\left(\epsilon_{i}^{2}\right),\left(\boldsymbol{h}_{i}\right),\left(\sigma_{\delta}^{2}\right),\left(\boldsymbol{\lambda}_{\mathrm{s}}\right) \mid H,\left(\boldsymbol{y}_{\mathrm{s}}\right)\right)= \\
& \frac{\mathrm{p}\left(\left(\boldsymbol{y}_{\mathrm{s}}\right),\left(\epsilon_{i}^{2}\right),\left(\boldsymbol{h}_{i}\right),\left(\sigma_{\delta}^{2}\right),\left(\boldsymbol{\lambda}_{\mathrm{s}}\right) \mid H\right)}{\mathrm{p}\left(\left(\boldsymbol{y}_{\mathrm{s}}\right) \mid H\right)}
\end{aligned}
$$

In words, the joint posterior probability distribution is proportional to the joint probability of (4). Replacing all distributions by their functional forms, this joint posterior pdf could be calculated in closed form, as is indeed done in most works applying Bayesian analysis. Since direct sampling from the joint posterior pdf is impossible, we must resort to MCMC, e.g., Gibbs sampling where the conditional pdfs should be derived. In this perspective, we propose to avoid calculating the joint posterior pdf to directly proceed to inference. In order to do so, we beforehand embed our model in a framework that allows for convenient representation, handling, and numerical inference: Bayesian graphical models.

## III. GRAPHICAL MODELING

## A. Directed Acyclic Graphs and Bayesian Networks

A graph $G$ is a mathematical object that relates a set of vertices, or nodes, $V$, to a set of edges, $E$, consisting of pairs of elements taken from $V$. There is a directed edge or arrow between vertices $\boldsymbol{z}_{n}$ and $\boldsymbol{z}_{m}$ in $V$ if the set $E$ contains the ordered pair $\left(\boldsymbol{z}_{n}, \boldsymbol{z}_{m}\right)$; vertex $\boldsymbol{z}_{n}$ is a parent of vertex $\boldsymbol{z}_{m}$, and vertex $\boldsymbol{z}_{m}$ is a child of vertex $\boldsymbol{z}_{n}$. A directed graph is a graph whose edges are all directed. A path is a sequence of distinct vertices $\boldsymbol{z}_{n_{1}}, \ldots, \boldsymbol{z}_{n_{m}}$ for which $\left(\boldsymbol{z}_{n_{l}}, \boldsymbol{z}_{n_{l+1}}\right)$ is in $E$ for each $l=1, \ldots, m-1$. The path is a cycle if the end points are allowed to be the same, $\boldsymbol{z}_{n_{1}}=\boldsymbol{z}_{n_{m}}$. An oriented graph with no cycle is called a directed acyclic graph (DAG).

A distribution p over $\boldsymbol{z}$ is compatible with a DAG $G$ if it satisfies all independence relationships entailed by $G .(G, \mathrm{p})$ is then called a Bayesian network. For more details, the reader is referred to [27]. The major feature of Bayesian networks is that $\mathrm{p}(\boldsymbol{z})$ must factorize according to the so-called factorization property

$$
\mathrm{p}(\boldsymbol{z})=\prod_{n=1}^{N} \mathrm{p}\left(\boldsymbol{z}_{n} \mid \mathrm{pa}\left(\boldsymbol{z}_{n}\right)\right)
$$

where $\mathrm{pa}(n)$ is the set of parents of vertex $\boldsymbol{z}_{n}$. This is nothing but a multidimensional generalization of the Markov chain rule. Defining a Bayesian network, hence, amounts to 1) defining relevant variables (i.e., nodes) $\boldsymbol{z}_{n}$, 2) defining structural relationships (i.e., edges) $\boldsymbol{z}_{n} \rightarrow \boldsymbol{z}_{m}$, and 3) defining functional relationships $\mathrm{p}\left(\boldsymbol{z}_{n} \mid \mathrm{pa}(n)\right)$. Pearl [28] showed a property that proves to be very efficient for numerical sampling, namely that nothing more is required to calculate the conditional probability of any node: the probability distribution of any variable $\boldsymbol{z}_{n}$ in the network, conditioned on the state of all other variables, is given by the product

$$
\mathrm{p}\left(\boldsymbol{z}_{n} \mid \mathrm{r} . \mathrm{v}\right) \propto \mathrm{p}\left(\boldsymbol{z}_{n} \mid \mathrm{pa}\left(\boldsymbol{z}_{n}\right)\right) \cdot \prod_{\boldsymbol{z}_{m} \in \operatorname{ch}\left(\boldsymbol{z}_{n}\right)} \mathrm{p}\left(\boldsymbol{z}_{m} \mid \mathrm{pa}\left(\boldsymbol{z}_{m}\right)\right)
$$

![img-1.jpeg](img-1.jpeg)

Fig. 1. Structural dependence of $\boldsymbol{y}_{s}$.
![img-2.jpeg](img-2.jpeg)

Fig. 2. Structural dependence of $\boldsymbol{h}_{i}$.
where r.v. stands for "remaining variables" and $\operatorname{ch}\left(\boldsymbol{z}_{n}\right)$ for the children nodes of $\boldsymbol{z}_{n}$. Note that $\boldsymbol{z}_{m}$ can have several parents and, hence, $\mathrm{pa}\left(\boldsymbol{z}_{m}\right)$ may not be restricted to $\boldsymbol{z}_{n}$. This formula states that the conditional probabilities can be derived from local quantities that are part of the model specification.

## B. Constructing the GLM Graphical Model

The GLM can easily be expressed in terms of a Bayesian network. This translation requires two major steps: representing the structural relationships, and then the functional relationships.

Equation (1) states that each $\boldsymbol{y}_{s}$ depends on the corresponding $\boldsymbol{\lambda}_{s}$ and $\sigma_{s}^{2}$, as well as all $\boldsymbol{h}_{i}$ 's. This equation can, hence, be represented by the graph depicted in Fig. 1.

As to the model relative to the prior information on the HRFs, it expresses that each $\boldsymbol{h}_{i}$ depends exclusively on $\epsilon_{i}^{2}$. Fig. 2 is, hence, a good model for it.

Gathering all parts leads to the graph proposed in Fig. 3. Irrespective of the functional relationships between nodes, application of (5) to the graphical model states that the joint pdf for all variables decomposes as

$$
\begin{aligned}
& \mathrm{p}\left(\left(\boldsymbol{y}_{s}\right),\left(\epsilon_{i}^{2}\right),\left(\boldsymbol{h}_{i}\right),\left(\sigma_{s}^{2}\right),\left(\boldsymbol{\lambda}_{s}\right) \mid H\right) \\
& \quad=\prod_{s=1}^{S} \mathrm{p}\left(\boldsymbol{y}_{s} \mid H, \mathrm{pa}\left(\boldsymbol{y}_{s}\right)\right) \\
& \quad \times \mathrm{p}\left(\boldsymbol{\lambda}_{s} \mid H, \mathrm{pa}\left(\boldsymbol{\lambda}_{s}\right)\right) \cdot \mathrm{p}\left(\sigma_{s}^{2} \mid H, \mathrm{pa}\left(\sigma_{s}^{2}\right)\right) \\
& \quad \times \prod_{i=1}^{I} \mathrm{p}\left(\boldsymbol{h}_{i} \mid H, \mathrm{pa}\left(\boldsymbol{h}_{i}\right)\right) \cdot \mathrm{p}\left(\epsilon_{i}^{2} \mid H, \mathrm{pa}\left(\epsilon_{i}^{2}\right)\right)
\end{aligned}
$$

which, once developed, is exactly (4). Our graphical model, thus, unambiguously embeds all structural relationships of the GLM. However, complicated $(H)$ may be, it is still much simpler to conceptualize it in graph form than as it was presented before. Whereas determination of structural relationships between two given variables in model $(H)$ remains a tough problem to tackle, the corresponding DAG clearly and unambiguously represents all possible independence relationships, that can be read off the graph using its Markov properties.

Among others, a direct consequence of this modeling is that it is now possible to apply (6) to the GLM graph model, expressing the conditional pdfs of all vari-
![img-3.jpeg](img-3.jpeg)

Fig. 3. DAG corresponding to the GLM.
ables, $\quad \mathrm{p}\left(\epsilon_{i}^{2} \mid H\right.$, r.v. $\left.), \mathrm{p}\left(\boldsymbol{h}_{i} \mid H\right.$, r.v. $\left.), \mathrm{p}\left(\sigma_{s}^{2} \mid H\right.$, r.v. $\left.), \quad\right.$ and $\mathrm{p}\left(\boldsymbol{\lambda}_{s} \mid H\right.$, r.v.) as a function of the distributions already defined

$$
\begin{aligned}
\mathrm{p}\left(\epsilon_{i}^{2} \mid H, \text { r.v. }\right) & \propto \mathrm{p}\left(\epsilon_{i}^{2} \mid H\right) \cdot \mathrm{p}\left(\boldsymbol{h}_{i} \mid H, \epsilon_{i}^{2}\right) \\
\mathrm{p}\left(\boldsymbol{h}_{i} \mid H, \text { r.v. }\right) & \propto \mathrm{p}\left(\boldsymbol{h}_{i} \mid H, \epsilon_{i}^{2}\right) \\
& \times \prod_{s=1}^{S} \mathrm{p}\left(\boldsymbol{y}_{s} \mid H,\left(\boldsymbol{h}_{i}\right), \sigma_{s}^{2}, \boldsymbol{\lambda}_{s}\right) \\
\mathrm{p}\left(\sigma_{s}^{2} \mid H, \text { r.v. }\right) & \propto \mathrm{p}\left(\sigma_{s}^{2} \mid H\right) \cdot \mathrm{p}\left(\boldsymbol{y}_{s} \mid H,\left(\boldsymbol{h}_{i}\right), \sigma_{s}^{2}, \boldsymbol{\lambda}_{s}\right) \\
\mathrm{p}\left(\boldsymbol{\lambda}_{s} \mid H, \text { r.v. }\right) & \propto \mathrm{p}\left(\boldsymbol{\lambda}_{s} \mid H\right) \cdot \mathrm{p}\left(\boldsymbol{y}_{s} \mid H,\left(\boldsymbol{h}_{i}\right), \sigma_{s}^{2}, \boldsymbol{\lambda}_{s}\right)
\end{aligned}
$$

Note that the functional relationships have not been defined yet-all the properties abovementioned are entailed by the sole structural relationships. As a matter of fact, the graphical representation is much more general than the GLM. The only constraints set by the graph is that the functional relationships be of the form $\mathrm{p}\left(\epsilon_{i}^{2}\right), \mathrm{p}\left(\boldsymbol{h}_{i} \mid \epsilon_{i}^{2}\right), \mathrm{p}\left(\sigma_{s}^{2}\right), \mathrm{p}\left(\boldsymbol{\lambda}_{s}\right)$, and $\mathrm{p}\left(\boldsymbol{y}_{s} \mid H,\left(\boldsymbol{h}_{i}\right), \sigma_{s}^{2}, \boldsymbol{\lambda}_{s}\right)$. But these conditional distributions can, in turn, be chosen at will. On the other hand, the graphical model can be made more specific for our purpose, so that it exactly fits the GLM. Identifying all functional relationships of the network to their counterparts for model $(H)$ then makes the DAG a perfect representation of the GLM. $\mathrm{p}\left(\epsilon_{i}^{2}\right)$ and $\mathrm{p}\left(\boldsymbol{h}_{i} \mid \epsilon_{i}^{2}\right)$ can be chosen to a scaled inverse- $\chi^{2}$ and a Gaussian distribution, respectively, as detailed in Section II-C. $\mathrm{p}\left(\sigma_{s}^{2}\right)$ and $\mathrm{p}\left(\boldsymbol{\lambda}_{s}\right)$ can be set as in Section II-D. Finally, $\mathrm{p}\left(\boldsymbol{y}_{s} \mid H,\left(\boldsymbol{h}_{i}\right), \sigma_{s}^{2}, \boldsymbol{\lambda}_{s}\right)$ can be set as in (2).

## C. Numerical Inference

To obtain a numerical approximation of the joint posterior pdf, we apply Gibbs sampling. This consists of starting with a seed vector and sequentially modifying one vector component at a time by sampling according to the conditional pdf of that component given the remaining variables. Samples are composed of the set of all vectors whose components have been updated an equal amount of times.

A key issue with Gibbs sampling is to partition the vector of all parameters into components whose conditional sampling can easily be performed. Another one is derivation of the conditional pdfs corresponding to the chosen clustering. In our case, both questions are answered at once, thanks to the previous step of graph modeling. As a matter of fact, it first allows us to decompose the parameter vector onto its $2 I+2 S$ canonical components: $I \epsilon_{i}^{2}$ 's and $\boldsymbol{h}_{i}$ 's, $S \sigma_{s}^{2}$ 's, and $\boldsymbol{\lambda}_{s}$ 's. All $\boldsymbol{y}_{s}$ 's being given, no sampling needs to be done on these variables. The updating steps are performed on these

variables; we, therefore, need access to the following conditional pdfs: $\mathrm{p}\left(\epsilon_{i}^{2} \mid H, \mathrm{r} . \mathrm{v}\right.$.$) , \mathrm{p}\left(\boldsymbol{h}_{i} \mid H, \mathrm{r} . \mathrm{v}\right.$.$) , \mathrm{p}\left(\sigma_{s}^{2} \mid H, \mathrm{r} . \mathrm{v}\right.$.$) ,$ and $\mathrm{p}\left(\boldsymbol{\lambda}_{s} \mid H, \mathrm{r} . \mathrm{v}\right.$.$) . But these are just the conditional distributions$ given by Pearl's theorem and structurally developed in (7). Integration of the exact functional relationships into (7) leads to (see the Appendix for a summary of the properties used)

- According to (7a), $\left(\epsilon_{i}^{2} \mid H, \mathrm{r} . \mathrm{v}\right.$.$) is proportional to the$ product of two inverse-chi-square distributions in $\epsilon_{i}^{2}$; it is, hence, also inverse-chi-square distributed

$$
\mathrm{p}\left(\epsilon_{i}^{2} \mid H, \text { r.v. }\right)=\operatorname{Inv}-\chi^{2}\left(\mu_{i}, \tau_{i}^{2} ; \epsilon_{i}\right)
$$

with

$$
\begin{aligned}
\mu_{i} & =n_{\epsilon}+\left(K_{i}-1\right) \\
\tau_{i}^{2} & =\frac{n_{\epsilon} \tau_{s}^{2}+\boldsymbol{h}_{i}^{t} \boldsymbol{R} \boldsymbol{h}_{i}}{n_{\epsilon}+\left(K_{i}-1\right)}
\end{aligned}
$$

- According to (7b), $\left(\boldsymbol{h}_{i} \mid H, \mathrm{r} . \mathrm{v}\right.$.$) is proportional to the$ product of two multivariate Normal distributions in $\boldsymbol{h}_{i}$; it is, hence, also multivariate Normal distributed

$$
\mathrm{p}\left(\boldsymbol{h}_{i} \mid H, \mathrm{r} . \mathrm{v}\right)=\mathcal{N}\left(\boldsymbol{\delta}_{i}, \boldsymbol{\Delta}_{i} ; \boldsymbol{h}_{i}\right)
$$

with

$$
\begin{aligned}
\boldsymbol{\Delta}_{i}= & \left(\frac{1}{\epsilon_{s}^{2}} \boldsymbol{R}+\sum_{s} \frac{1}{\sigma_{s}^{2}} \boldsymbol{X}_{s, i}^{t} \boldsymbol{X}_{s, i}\right)^{-1} \\
\boldsymbol{\delta}_{i}= & \boldsymbol{\Delta}_{i}\left(\sum_{s} \frac{1}{\sigma_{s}^{2}} \boldsymbol{X}_{s, i}^{t}\right. \\
& \left.\cdot\left(\boldsymbol{y}_{s}-\sum_{j \neq i} \boldsymbol{X}_{s, j} \boldsymbol{h}_{j}-\boldsymbol{D}_{s} \boldsymbol{\lambda}_{s}\right)\right)
\end{aligned}
$$

- According to (7c), $\left(\sigma_{s}^{2} \mid H\right.$, r.v.) is proportional to the product of two inverse-chi-square distributions in $\sigma_{s}^{2}$; it is, hence, also inverse-chi-square distributed

$$
\mathrm{p}\left(\sigma_{s}^{2} \mid H, \mathrm{r} . \mathrm{v}\right)=\operatorname{Inv}-\chi^{2}\left(\nu_{s}, \omega_{s}^{2} ; \sigma_{s}^{2}\right)
$$

with

$$
\begin{aligned}
\nu_{s} & =n_{\sigma, i}+L_{s} \\
\omega_{s}^{2} & =\frac{n_{\sigma, s} r_{\sigma, i}^{2}+\left\|\boldsymbol{y}_{s}-\sum_{i} \boldsymbol{X}_{s, i} \boldsymbol{h}_{i}-\boldsymbol{D}_{s} \boldsymbol{\lambda}_{s}\right\|^{2}}{n_{\sigma, i}+L_{s}}
\end{aligned}
$$

- According to (7d), $\left(\boldsymbol{\lambda}_{s} \mid H, \mathrm{r} . \mathrm{v}\right.$.$) is proportional to the$ product of two multivariate Normal distributions in $\boldsymbol{\lambda}_{s}$; it is, hence, also multivariate Normal distributed

$$
\mathrm{p}\left(\boldsymbol{\lambda}_{s} \mid H, \mathrm{r} . \mathrm{v}\right)=\mathcal{N}\left(\boldsymbol{\gamma}_{s}, \boldsymbol{\Gamma}_{s} ; \boldsymbol{\lambda}_{s}\right)
$$

with

$$
\begin{aligned}
\boldsymbol{\Gamma}_{s} & =\left(\boldsymbol{V}_{\lambda, s}^{-1}+\frac{1}{\sigma_{s}^{2}} \boldsymbol{D}_{s}^{t} \boldsymbol{D}_{s}\right)^{-1} \\
\boldsymbol{\gamma}_{s} & =\boldsymbol{\Gamma}_{s}\left(\boldsymbol{V}_{\lambda, s}^{-1} \boldsymbol{m}_{\lambda, s}+\frac{1}{\sigma_{s}^{2}} \boldsymbol{D}_{s}^{t}\left(\boldsymbol{y}_{s}-\sum_{i} \boldsymbol{X}_{s, i} \boldsymbol{h}_{i}\right)\right)
\end{aligned}
$$

The sampling can then be performed by sequentially updating the $\epsilon_{i}^{2}$ 's, the $\boldsymbol{h}_{i}$ 's, then the $\sigma_{s}^{2}$ 's, and finally the $\boldsymbol{\lambda}_{s}$ 's. Convergence monitoring is performed component-wise using parallel sampling as detailed in [29]. More precisely, we first take the logarithm of $\epsilon_{i}^{2}$ and $\sigma_{s}^{2}$, so that all variables are spanned from $-\infty$ to $+\infty$. For each estimand $\phi, \phi=\log \epsilon_{i}^{2}, \log \sigma_{s}^{2}, h_{i, k}$, and $\lambda_{s, m}$, we draw $B$ parallel sequences of length $C$ (we typically
took $B=10$ and $C=50$ ), each sample being denoted $\phi^{[b c]}$, with $b=1, \ldots, B$ and $c=1, \ldots, C$. We then compute the be-tween-sequence variance BV, and the within-variance sequence WV as follows:

$$
\mathrm{BV}=\frac{C}{B-1} \sum_{b=1}^{B}\left(\tilde{\phi}^{[b c]}-\tilde{\phi}^{[c c]}\right)^{2}
$$

with

$$
\tilde{\phi}^{[b c]}=\frac{1}{C} \sum_{c=1}^{C} \phi^{[b c]} \quad \text { and } \quad \tilde{\phi}^{[c c]}=\frac{1}{B} \sum_{b=1}^{B} \phi^{[b c]}
$$

and

$$
W V=\frac{1}{B} \sum_{b=1}^{B}\left(s^{2}\right)^{[b]}
$$

where

$$
\left(s^{2}\right)^{[b]}=\frac{1}{C-1} \sum_{c=1}^{C}\left(\phi^{[b c]}-\tilde{\phi}^{[b c]}\right)^{2}
$$

We then calculate

$$
\sqrt{\bar{R}}=\sqrt{1+\frac{1}{C}\left(\frac{\mathrm{BV}}{W V}-1\right)}
$$

for each scalar estimand. These quantities are supposed to decline to 1 as the sampling converges. We stop the algorithm when all $\sqrt{\bar{R}}$ are close enough to 1 , e.g., smaller than 1.1 , and remove $\alpha$ percent of each chain to account for a burn-in period.

We are admittedly mostly interested in the HRFs, but knowledge of the values taken by the other parameters are relevant as well for our analysis and a better understanding of brain processing. Gibbs sampling gives us access to estimates for all parameters or any quantity of interest related to them. For instance, in this paper, parameter estimators are given as
posterior mean $\pm$ posterior standard deviation.
Once Gibbs sampling has converged, these quantities are approximated by their sample counterparts.

## IV. Simulations

We simulated data with two HRFs $(I=2)$, as depicted in Fig. 4. To obtain the $\epsilon_{i}$ 's corresponding to these HRFs, we calculated them as follows. If we knew that $\boldsymbol{h}_{i}=\boldsymbol{h}_{i}^{0}$, then we could infer $\epsilon_{i}^{2}$ using Bayes' theorem

$$
\mathrm{p}\left(\epsilon_{i}^{2} \mid H^{\prime}, \boldsymbol{h}_{i}=\boldsymbol{h}_{i}^{0}\right) \propto \mathrm{p}\left(\epsilon_{i}^{2} \mid H^{\prime}\right) \cdot \mathrm{p}\left(\boldsymbol{h}_{i}=\boldsymbol{h}_{i}^{0} \mid H^{\prime}, \epsilon_{i}^{2}\right)
$$

where $\mathrm{p}\left(\boldsymbol{h}_{i}=\boldsymbol{h}_{i}^{0} \mid H^{\prime}, \epsilon_{i}^{2}\right)$ would be given by (3), and $\mathrm{p}\left(\epsilon_{i}^{2} \mid H^{\prime}\right)$ could be taken as a uniform prior, asuming no particular prior knowledge. $\left(\epsilon_{i}^{2} \mid H^{\prime}, \boldsymbol{h}_{i}=\boldsymbol{h}_{i}^{0}\right)$ would then be Inv- $\chi^{2}$ distributed and

$$
\mathrm{E}\left[\epsilon_{i}^{2}\right]=\frac{1}{K-1} \cdot \boldsymbol{h}_{i}^{0} \boldsymbol{R} \boldsymbol{h}_{i}^{0}
$$

This last relation can, in turn, be taken as estimate for $\epsilon_{i}^{2}$, leading to

$$
\begin{aligned}
& \epsilon_{1}^{2}=1.21 \\
& \epsilon_{2}^{2}=0.30
\end{aligned}
$$

For the simulation, we also took two sessions of $N=100$ time samples. $\Delta t$ and the sampling interval were both set to

![img-4.jpeg](img-4.jpeg)

Fig. 4. Simulations. Estimated (dashed line) and simulated (solid line) HRF (Available: www.fil.ion.ucl.ac.uk/spm/spm99.html).
1.5 s. Quadratic drifts $\left(p_{1}(t)=846+0.2 \cdot t+0,001 \cdot t^{2}\right.$ and $p_{2}(t)=950+0.15 \cdot t+0.0011 \cdot t^{2}$ ) and Gaussian white noises $\left(\sigma_{1}^{2}=50, \sigma_{2}^{2}=100\right)$ were also added. Note that the noise standard deviations are about of the same amplitude as the HRF. For the analysis, we set both orders to $K=20$, and took a quadratic drift in consideration $(M=3)$ with each $\boldsymbol{m}_{\lambda, s}$ set to $\left(\mathrm{E}\left[\boldsymbol{y}_{s}\right], 0,0\right)^{\mathrm{t}}$, and $\boldsymbol{V}_{\lambda, s}$ to a diagonal matrix such, that $\operatorname{diag}\left(\boldsymbol{V}_{\lambda, s}\right)=\left(10000^{2} 1000^{2} 1000^{2}\right)$. All $n_{\sigma, s}$ and $n_{\epsilon}$ were set to 1 to implement vague priors for $\sigma_{s}^{2}$ 's and $\epsilon_{i}^{2}$ 's. As to the remaining hyperparameters, the goal was to set them, so that they provide a magnitude order for the corresponding variables as follows:

- each $r_{\sigma, s}^{2}$ was set to $\operatorname{Var}\left[\boldsymbol{y}_{s}\right]$;
- $r_{\epsilon}^{2}$ was set to

$$
\frac{\mathrm{E}_{s}\left[\operatorname{Var}\left[\boldsymbol{y}_{s}\right]\right]}{\max \left[\boldsymbol{h}_{\mathrm{SPM}}\right]},\left[\frac{1}{K-1} \cdot \boldsymbol{h}_{\mathrm{SPM}}^{\mathrm{t}} \boldsymbol{R} \boldsymbol{h}_{\mathrm{SPM}}\right]
$$

where $\boldsymbol{h}_{\mathrm{SPM}}$ is SPM canonical HRF and $\mathrm{E}_{s}\left[\operatorname{Var}\left[\boldsymbol{y}_{s}\right]\right]$ is a scaling factor.
Gibbs sampling took about 2250 updates for each of the 10 parallel chains to converge, and we kept the last $10 \%$ of each chain. We obtained the following estimates:

$$
\begin{aligned}
\epsilon_{1}^{2} & \approx 1.29 \pm 0.80 \\
\epsilon_{2}^{2} & \approx 0.936 \pm 0.524 \\
\sigma_{1}^{2} & \approx 38.6 \pm 7.8 \\
\sigma_{2}^{2} & \approx 109 \pm 20 \\
\lambda_{1,0} & \approx 858 \pm 4 \\
\lambda_{2,0} & \approx 956 \pm 4
\end{aligned}
$$

Estimates for $\epsilon_{i}^{2}, \sigma_{s}^{2}$, and $\boldsymbol{\lambda}_{\epsilon}$ were accurate. As shown in Fig. 4, HRF estimates were also very accurate for the noise level considered.
![img-5.jpeg](img-5.jpeg)

Fig. 5. Convergence monitoring. Every 50 steps is represented $\max [\sqrt{R}]$ taken among all $\epsilon_{i}^{2}$ (diamonds), $\sigma_{s}^{2}$ (circles), $h_{i, k}$ (squares), and $\lambda_{e, n_{i}}$ (stars).

## V. REAL DATA

Eleven healthy subjects (age 18-40) were scanned while performing a motor sequence learning task. Using a joystick, they were asked to reach a target projected on a screen for 3 s , following an elliptic curve as precisely and rapidly as possible. They had to complete 64 trials of sequence (SEQ) mode (the targets appeared in a predefined order, unknown to the subject, to form a 8 -item-long sequence) and 16 trials of random (RAN) mode (the targets appeared pseudorandomly). The time interval beween two consecutive trials, or inter-stimulus interval, was randomly selected to uniformly lie between 3 and 4 s . Functional $\mathrm{T}_{2}^{*}$-weighted acquisitions were performed on a 3 T Bruker MEDSPEC 30/80 MR system (TR: 3486 ms , TE: 35 ms , flip angle: $90^{\circ}$, matrix $64 \times 64 \times 42$, voxel size $3 \times 3 \times 3 \mathrm{~mm}$ ).

The data imply to work with $I=2$ HRFs ( $i=1$ and $i=$ 2 corresponding to SEQ and RAN, respectively) and $S=5$ sessions. For the analysis, we first adjusted the stimulus on a grid of interval $\Delta t=\mathrm{TR} / 5$. Both HRFs were assumed to have a common order $K=5 \times 5$, for a total duration of 5 TRs. The prior hyperparameters were set as in Section IV. To illustrate the method, we selected two voxels, $v_{1}$ and $v_{2} . v_{1}$ was located in the right cerebellum and $v_{2}$ in the right inferotemporal lobe. Our goal was to estimate both HRFs corresponding to conditions SEQ and RAN, respectively.

Based on our monitoring system, convergence took around 1300 iterations to occur. Fig. 5 shows a typical convergence curve. As showed in Fig. 6, the method was able to extract different HRF behaviors for different conditions, despite a very low signal-to-noise ratio. The high noise level was reflected in the large estimate error bars but did not prevent discrimination between conditions. The estimated values for the other parameters are given in Table I.

## VI. DISCUSSION

Our approach made it possible to associate the well-known GLM for HRF estimation in fMRI data analysis to a directed acyclic graph. This had the first advantage of making clear all modeling hypotheses. Moreover, in a Bayesian framework, the complex, yet central, step of calculating the joint posterior pdf was avoided. Instead, the graph provided us with a very convenient tool to first break down the set of all variables into coherent subsets, namely its nodes. Using the Markov properties, it was direct to derive all conditional pdfs that were required for Gibbs sampling as products of conditional pdfs that have been

![img-6.jpeg](img-6.jpeg)

Fig. 6. Real data. HRFs corresponding to the SEQ (solid line) and RAN (dashed line) stimuli. Each sample has been slightly shifted to the left (SEQ) or to the right (RAN) for a better graphical rendering.

TABLE I
Estimates of the Smoothing Parameters $\epsilon_{i}$, the Noise Variances $\sigma_{i}^{2}$, and the Baselines $\lambda_{s, 1}$


specified with the modeling. Fully probabilistic numerical inference was then straightforward at a reasonable time cost. Furthermore, solving the same problem with several variables set to certain values was an easy matter, since all that must be done is removing these variables from the sampling scheme.

Because variable partitioning is implied by the graph structure, our application of Gibbs sampling differs from classical applications. For instance, we sequentially sampled each HRF, resp. drift vector, resp. noise variance, whereas a conventional procedure would simultaneously sample all HRFs, then all drift parameters, and so on. What influence this difference makes on the convergence speed of the Markov chain is a matter that needs
to be further investigated. Another point would be to compare our method to a more conventional procedure where part, or all, of the nuisance parameters (e.g., drift parameters) are integrated out of the joint posterior pdf, and inference is done on the posterior marginal pdf of the HRFs. In the "marginal" scheme, each sample is performed on a lower dimension, and the Markov Chain is also of lower dimension. For these reasons, it is expected that convergence will be faster. This scheme is, however, very sensitive to model changes and makes inference on other parameters tedious.

Influence of the prior parameters is of importance to check sensitivity of the estimates. $\boldsymbol{m}_{\lambda}$ and $\boldsymbol{V}_{\lambda}$ were found to have very little weight on the inference, $n_{\sigma}$ and $r_{\sigma}$ some more. Selection of $n_{\epsilon}$ and $r_{\epsilon}$ did not much matter for drift and noise parameters, but had a dramatic influence on HRF estimation. The ad hockery proposed to manually set these hyperparameters seems to be useful, but its influence on the sampling scheme is still unclear. Indeed, except for this, we did not even have a prior idea of the magnitude order of $\epsilon_{i}^{2}$, whereas scaled inverse-chi-square pdfs are relatively localized around their mode. To remedy this flaw, we suggest that setting priors for $\log \left(\epsilon_{i}^{2}\right)$ would prove more adapted to the state of ignorance that we are in relative to these parameters than conjugate priors. A general procedure is proposed in [30] to sample from pdfs that have the structure implied by (6) using rejectionsampling. Another improvement would be to modify the model, so that $\epsilon_{i}$ becomes independent of the HRF intensity. This could be achieved by consideration of a normalized HRF and a scaling factor. Choice of noninformative, i.e., improper, ${ }^{2}$ priors might also help to circumvent that problem. The reason why we did not consider this option here is that it is safe to use improper priors as long as the posterior pdf can be proved to be proper. Since one advantage of our method is to avoid calculation of the posterior pdf, this step cannot be performed in our setting without making it lose some of its appeal. Nonetheless, we are optimistic and believe that further investigation could justify use of improper priors in a restricted fashion.

In the framework of DAG modeling, the local properties of relationships renders the model very simple to structurally or functionally modify at a local level, either because it does not correctly explain the phenomenon under interest, or because a more complex model is sought. As a matter of fact, the proposed model for HRF estimation can already be seen as an improvement of the graphical model associated to the basic one-HRF, one-session linear model. Fig. 7 illustrates how this model can successively be expanded by introduction of smoothing priors, several sessions, and several stimulus types. These models can be dealt with as efficiently as the one detailled in this paper. Their joint posterior distribution would be given by application of (5), whereas all conditional distributions required by Gibbs sampling could easily be obtained through (6).

Besides, consideration of local spatial information, as in [23], [24], [31] could be achieved by gathering all voxel graphical models that were here assumed to be independent from each other and adding relationships between neighboring $\boldsymbol{h}_{v, i}$ 's. Another point would be to relax the assumption that all HRFs are
${ }^{2} \mathrm{~A}$ prior pdf $\rho$ is improper if its integral is not finite, i.e.,

$$
\int p(x) \mathrm{d} x=\infty
$$

![img-7.jpeg](img-7.jpeg)

Fig. 7. Successives complexification of the HRF model. (a) basic model; (b) model with hyperparameter for smoothness regularization; $\left(c_{1}\right)$ model accounting for one stimulus type and several sessions; $\left(c_{2}\right)$ model accounting for several stimulus types and one sessions; (d) GLM considered in this paper.
constant across sessions and rather assume that they share the same shape accross sessions, with an amplitude that can vary, as discussed in [22]. As more and more information is incorporated into the model, the corresponding graph will become more and more complex. However, tools have been developed to deal with such graphs. Parallel processing of Gibbs sampling can be implemented. To avoid the problem of simultaneous updating of neighboring variables, one has to apply the so-called "edge reversal" control policy, as detailed in [28]. For huge graphs, [32] proposed an efficient variant of Gibbs sampling.

We finally believe that this novel approach has a much broader application range than just fMRI data analysis. Indeed, we are confident in the fact that any Bayesian model can be embedded in a graphical framework. This would allow to concentrate on the modeling, since efficient and automated inference would directly derive from the model.

## VII. CONCLUSION

In this paper, we proposed a novel Bayesian inference framework for HRF estimation in fMRI data analysis, based on trans-
lating the existing Bayesian model into a Bayesian network to combine the features of graphical modeling and Bayesian analysis. This approach makes extensive use of Bayesian networks to 1) represent the model in a compact, yet efficient way, and 2) lead probabilistic inference through Gibbs sampling. This technique takes advantage of Markov properties of DAGs. Models can easily be designed, and both structural (i.e., of independence) and functional relationships are clearly presented. Moreover, using Gibbs sampling on the DAG, fully probabilistic numerical inference is straightforward. Ongoing research includes integration of more diffuse prior pdfs when necessary, as well as spatial constraints for the HRFs.

## APPENDIX

The results detailed here originate from [29].

## A. Multivariate Normal Distribution

If $\boldsymbol{x}$ is a $d$-dimensional multivariate Normal distributed variable with mean $\boldsymbol{m}$ and covariance matrix $\boldsymbol{V}$, then

$$
\mathrm{p}(\boldsymbol{x})=(2 \pi)^{d / 2}|\boldsymbol{V}|^{-1 / 2} \exp \left[-\frac{1}{2}(\boldsymbol{x}-\boldsymbol{m})^{\mathrm{t}} \boldsymbol{V}^{-1}(\boldsymbol{x}-\boldsymbol{m})\right]
$$

If $\boldsymbol{x}$ has a probability distribution defined by

$$
\mathrm{p}(\boldsymbol{x}) \propto f_{1}(\boldsymbol{x}) \cdot f_{2}(\boldsymbol{x})
$$

where $f_{i}$ is multivariate Gaussian with mean $\boldsymbol{m}_{i}$ and covariance matrix $\boldsymbol{V}_{i}$, then $\boldsymbol{x}$ is multivarite Gaussian with mean

$$
\boldsymbol{m}=\left(\boldsymbol{V}_{1}^{-1}+\boldsymbol{V}_{2}^{-1}\right)^{-1}\left(\boldsymbol{V}_{1}^{-1} \boldsymbol{m}_{1}+\boldsymbol{V}_{2}^{-1} \boldsymbol{m}_{2}\right)
$$

and covariance matrix

$$
\boldsymbol{V}=\left(\boldsymbol{V}_{1}^{-1}+\boldsymbol{V}_{2}^{-1}\right)^{-1}
$$

## B. Inverse-Chi-Square Distribution

If $y$ is inverse-chi-square distributed with $n$ degrees of freedom and scale $s$, then

$$
\mathrm{p}(y)=\frac{(n / 2)^{n / 2}}{\Gamma(n / 2)} s^{n} y^{-(n / 2+1)} e^{-n s^{2} /(2 y)}
$$

If $y$ has a probability distribution defined by

$$
\mathrm{p}(y) \propto f_{1}(y) \cdot f_{2}(y)
$$

where $f_{i}$ is inverse-chi-square distributed with $n_{i}$ degrees of freedom scale $s_{i}$, then $y$ is inverse-chi-square with

$$
n=n_{1}+n_{2}
$$

degrees of freedom and scale $s$ so, that

$$
s^{2}=\frac{n_{1} s_{1}^{2}+n_{2} s_{2}^{2}}{n_{1}+n_{2}}
$$

## ACKNOWLEDGMENT

The authors are grateful to Pr. J. Doyon (Institut de Gériatrie, Université de Montréal, Canada) for providing them with the data and to C. Posé for her technical support.
