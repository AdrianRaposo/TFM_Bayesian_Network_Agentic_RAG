# A Bayesian approach to sparse dynamic network identification 

Alessandro Chiuso ${ }^{\text {a }}$, Gianluigi Pillonetto ${ }^{\text {b }}$<br>${ }^{a}$ Dipartimento di Tecnica e Gestione dei Sistemi Industriali<br>University of Padova, Vicenza, (Italy)<br>${ }^{\text {b }}$ Department of Information Engineering<br>University of Padova, Padova (Italy)


#### Abstract

Modeling and identification for high dimensional (i.e. signals with many components) data sets poses severe challenges to off-the-shelf techniques for system identification. This is particularly so when relatively small data sets, as compared to the number signal components, have to be used. It is often the case that each component of the measured signal can be described in terms of few other measured variables and these dependence can be encoded in a graphical way via so called "Dynamic Bayesian Networks". Finding the interconnection structure as well as the dynamic models can be posed as a system identification problem which involves variables selection. While this variable selection could be performed via standard selection techniques, computational complexity may however be a critical issue, being combinatorial in the number of inputs and outputs. Parametric estimation techniques which result in sparse models have nowadays become very popular and include, among others, the well known Lasso, LAR and their "grouped" versions Group Lasso and Group LAR. In this paper we introduce two new nonparametric techniques which borrow ideas from a recently introduced Kernel estimator called "stable-spline" as well as from sparsity inducing priors which use $\ell_{1}$-type penalties. Numerical experiments regarding estimation of large scale sparse (ARMAX) models show that this technique provides a definite advantage over a group LAR algorithm and state-of-the-art parametric identification techniques based on prediction error minimization.


Key words: linear system identification; sparsity inducing priors; kernel-based methods; Bayesian estimation; regularization; Gaussian processes

## 1 Introduction

Black-box identification approaches are widely used to learn dynamic models from a finite set of input/output data $[32,49]$. In particular, in this paper we focus on the identification of large scale linear systems that involve a wide amount of variables and find important applications in many different domains such as chemical engineering, econometrics/finance, computer vision, systems biology, social networks and so on $[7,39,30]$.

In engineering applications, when data are collected from a physical plant, it is often the case that there is an underlying interconnection structure; for instance the overall plant could be the interconnection via cascade, parallel, feedback and combinations thereof, of many dynamical systems. In this

[^0]scenario any given variable may be directly related to only a few other variables.

In the static Gaussian case, the "relation" is expressed in terms of conditional independence conditions between subsets of variables, see e.g. [14]. Estimation of sparse graphical models have been the subject of intense research which is impossible to survey in this paper; we only point the reader to the early paper [37] which propose using the Lasso to this purpose, and to the more recent technical report [21] which suggests new directions introducing symmetric procedures as well as grouping strategies to reduce the number of nodes, providing also comparisons between different methods.

In the dynamic case, i.e. when observed data are trajectories of (possibly stationary) stochastic processes, one may consider several notions of conditional independence which can be encoded via the so-called time series correlation (TSC) graphs, Granger causality graphs and "partial correlation" graphs, see [13] for details.

When the number of measured variables is very large and possibly larger than the number of data available (i.e. the


[^0]:    ${ }^{1}$ This paper was not presented at any IFAC meeting. Corresponding author Alessandro Chiuso Ph. +390498277709

    Email addresses: alessandro.chiuso@unipd.it (Alessandro Chiuso), giapi@dei.unipd.it (Gianluigi Pillonetto).

number of "samples" available for statistical inference), even though there is no "physical" underlying network, constructing meaningful models which are useful for prediction/monitoring/intepretation requires trading off model complexity vs. fit. In a parametric setup this complexity depends on the number of parameters which is related to both the complexity of each "subsystem" (e.g. measured via its order) as well as to their number (i.e. the number of dynamical systems which are "non zero").

Problems of this sort have been recently studied in the literature, see for instance [52,40,35,36] and references therein. In the paper [52] coupled nonlinear oscillators (Kuramoto type) are considered where the coupling strengths are to be estimated; in [40] nonlinear dynamics are allowed and the attention is restricted to the linear term ${ }^{1}$ in the state update equation, equivalent to a vector autoregressive (VAR) model of order one. In both cases it is assumed that the entire state space is measurable and an $\ell_{1}$-penalized regression problem is solved for estimating the coupling strenghts/linear approximations. Sparse models under "smoothing" conditional independence relations, encoded by "partial correlation" graphs or equivalently via zeros in the inverse spectrum [8], have been recently studied in the literature. For instance, in [50] considers VAR models and $\ell_{1}$-type penalized regression while in $[35,36]$ a methodology based on smoothing $a$ la Wiener is proposed, where interconnections are found by putting a threshold on the estimated transfer functions.

In this work we shall focus on stationary stochastic processes described via Granger causality graphs, where conditional independence conditions encode the fact that the prediction of (the future of) one variable (which we shall call "output variable") may require only the past history of few other variables (which we shall call "inputs") plus possibly its own past. This can be represented with a graph where nodes are variables and (directed) edges are (non zero) transfer functions, self-loops encoding dependence on the "output" own past ${ }^{2}$. In general both the dynamical systems and the interconnection structure is unknown and have to be inferred from data. Without loss of generality we shall address the problem of modeling the relation between one node in this graph (the "output" variable) and all the other measured variables (the "inputs" ) in a "prediction error" framework. Beyond linearity, we shall not make any assumption on each subsystem (e.g. no knowledge of system orders). Our focus is both on finding the underlying connection structure (if any) as well as obtaining reliable and easily interpretable models which can be used, e.g. for prediction/monitoring etc. Of course, the problem of modeling an "output" $y$ as a function of certain inputs $u$ is meaningful per se, and one may not be interested at all in building a complete "network of dependences" for the joint process $(u, y)$ but just to per-

[^0]form variable selection in linear system identification when many "exogenous" variables are present.

In this scenario a key point is that the identification procedure should be sparsity-favoring, i.e. able to extract from the large number of subsystems entering the system description just that subset which influences significantly the system output. Such sparsity principle permeates many well known techniques in machine learning and signal processing such as feature selection, selective shrinkage and compressed sensing $[27,16]$.
In the classical identification scenario, Prediction Error Methods (PEM) represent the most used approaches to optimal prediction of discrete-time systems [32]. The statistical properties of PEM (and Maximum Likelihood) methods are well understood when the model structure is assumed to be known. However, in real applications, first a set of competitive parametric models has to be postulated. Then, a key point is the selection of the most adequate model structure, usually performed by AIC and BIC criteria [1,47]. Not surprisingly, the resulting prediction performance, when tested on experimental data, may be distant from that predicted by "standard" (i.e. without model selection) statistical theory, which suggests that PEM should be asymptotically efficient for Gaussian innovations. If this drawback may affect standard identification problems, a fortiori it renders difficult the study of large scale systems where the elevated number of parameters, as compared to the number of data available, may undermine the applicability of the theory underlying e.g. AIC and BIC.

Some novel estimation techniques inducing sparse models have been recently proposed. They include the well known Lasso [51] and Least Angle Regression (LAR) [17] where variable selection is performed exploiting the $\ell_{1}$ norm. This type of penalty term encodes the so called bi-separation feature, i.e. it favors solutions with many zero entries at the expense of few large components. Consistency properties of this method are discussed e.g. in [63,64]. Extensions of this procedure for group selection include Group Lasso and Group LAR (GLAR) [61] where the sum of the Euclidean norms of each group (in place of the absolute value of the single components) is used. Theoretical analysis of these approaches such and connections with the multiple kernel learning problem can be found in [5,38] while a discussion on the advantages of Group Lasso over Lasso is discussed in [29]. We warn the reader that one should not take "sparse" estimators as panacea; it is for instance shown in [31] that sparse estimators which possess some sort of "Oracle property" [19] have unbounded (normalized) maximal risk as the sample size increases.

Most of the work available in the literature addresses the "static" scenario while very little, with some exception [57,28], can be found regarding the identification of dynamic systems.
In this paper we adopt a Bayesian point of view to prediction and identification of sparse linear systems. Our starting point is the new identification paradigm developed in [45] that relies on nonparametric estimation of impulse


[^0]:    1 Thinking of a first order Taylor expansion around the trajectory
    2 In the language of classical System Identification, dependence of the predictor on the past outputs will result in ARMAX models, lack of dependence in Output Error (OE) models.

responses (see also [44] for extensions to predictor estimation). Rather than postulating finite-dimensional structures for the system transfer function, e.g. ARX, ARMAX or Laguerre [32], the system impulse response is searched for within an infinite-dimensional space. The intrinsical illposed nature of the problem is circumvented using Bayesian regularization methods. In particular, working under the framework of Gaussian regression [46], in [45] the system impulse response is modeled as a Gaussian process whose autocovariance is the so called stable spline kernel that includes the BIBO stability constraint.
In this paper, expanding on our recent works [12,11], we extend this nonparametric paradigm to the design of optimal linear predictors for sparse systems. Without loss of generality, analysis is restricted to MISO systems, where the variable to be predicted is called "output variable" and all the other (say $m-1$ ) available variables are called "inputs". In this way we interpret the predictor as a system with $m$ inputs (given by the past outputs and inputs) and one output (output predictions). Thus, predictor design amounts to estimating $m$ impulse responses modeled as realizations of Gaussian processes. We set their autocovariances to stable spline kernels with unknown scale factors.

We consider two approaches: the first, which we shall call Stable-Spline GLAR (SSGLAR), is based in the GLAR algorithm in [61] and can be seen as a variation of the socalled "elastic net" [65]; the second, which we shall call Stable-Spline Exponential Hyperprior (SSEH) uses a hierarchical prior which assigns exponential hyperpriors having a common hypervariance to the scale factors. This second approach has connections with the so-called Relevance Vector Machine in [53]; see also the discussion on scale-mixture distributions in [24]. In this way, while SSGLAR uses the sum of the $\ell_{1}$ norms of the single impulse responses, the hyerarchical hyperprior favors sparsity through an $\ell_{1}$ penalty on kernel hyperparameters. Inducing sparsity by hyperpriors is an important feature of our second approach. In fact, this permits to obtain the marginal posterior of the hyperparameters in closed form and hence also their estimates in a robust way. Once the kernels are selected, the impulse responses are obtained by a convex Tikhonov-type variational problem.

As we shall see, however, SSEH requires solving a nonlinear optimization problem which may benefit from a "good" initialization. We shall argue that a forward-selection type of procedure which is in some sense related to SSGLAR provides a robust and computationally attractive way of initializing SSEH.

Numerical experiments involving sparse ARMAX systems show that this approach provides a definite advantage over both the standard GLAR (applied to ARX models) and PEM (equipped with AIC or BIC) in terms of predictive capability on new output data while also effectively capturing the "structural" properties of the dynamic network, i.e. being able to identify correctly, with high probability, the absence of dynamic links between certain variables.

The paper is organized as follows: Section 2 contains the problem formulation while Section 3 contains some background material including the nonparametric approach to system identification introduced in [45] as well as standard approaches to sparsification. Section 4 formulates the input selection as a "group-sparsity" problem also formulating the predictor estimation problem in our Bayesian framework. Sections 5 and 6 describe the two algorithms we introduce while Section 7 reports some simulation results. Conclusions end the paper.

## Notation

The symbols $\mathbb{E}[\cdot]$ denotes expectation while $\hat{\mathbb{E}}[\cdot \mid \cdot]$ denotes the best linear estimator (conditional expectation in the Gaussian case). In addition for $A \in \mathbb{R}^{n \times m}, A^{[i j]}$ will denote the element of $A$ in position $(i, j)$. If $A$ is a vector the notation $A^{[i]}$ will be used in place of $A^{[i 1]}$ or $A^{[1 i]}$; in addition $A^{[-i]}$ denotes the vector $A$ with the $i-t h$ component suppressed. The symbol $I$ denotes the identity matrix of suitable dimensions, $A^{\top}$ is the transpose of the matrix $A$ and $\|x\|_{p}$ is the $p$-norm of the vector $x$. The symbol $\ell_{1}\left(\mathbb{Z}^{+}\right)$ will denote the space of real infinite sequences (indexed by $\mathbb{Z}^{+}$) having finite $\ell_{1}$ norm, i.e. the infinite column vector $g:=\left[g_{1}, g_{2}, \ldots, g_{k}, \ldots\right]^{\top} \in \ell_{1}\left(\mathbb{Z}^{+}\right)$iff $\sum_{i=1}^{\infty}\left|g_{i}\right|<\infty$.

## 2 Statement of the problem and notation

Let $\left\{z_{t}\right\}_{t \in \mathbb{Z}}, z_{t} \in \mathbb{R}^{m}$ be a stationary stochastic processes which models the joint time evolution of some variables of interests. With some abuse of notation the symbol $z_{t}$ will both denote a random variable (from the random process $\left\{z_{t}\right\}_{t \in \mathbb{Z}}$ ) and its sample value. We can think of each component of the vector process $\left\{z_{t}\right\}$ as being attached to the node of a network. Our purpose is to build linear dynamical models which describe dynamically each of the components of $\left\{z_{t}\right\}$ as a function of the others. To this purpose we define $y_{t}:=z_{t}^{[i]}$ (the $i-t h$ component of $z_{t}$ ) as "output" and all the others $u_{t}:=z_{t}^{[-i]} \in \mathbb{R}^{m-1}$ as "inputs". Of course the argument can be repeated for $i=1, \ldots, m$ thus obtaining a description of all the variables in $z_{t}$ as a function of the others. Throughout the paper we shall make a specific choice of $i$ which, w.l.o.g., can be taken equal to 1 so that

$$
z_{t}:=\left[\begin{array}{l}
y_{t} \\
u_{t}
\end{array}\right]
$$

This sort of notation is standard in modeling feedback interconnections (see e.g. $[22,20,10]$ ) where one concentrates on one variable viewing the others as "inputs", with the assumption that the overall interconnection is such that the joint process is stationary. Also the absence of direct feedthrough terms (i.e. $f_{0}=0$ in (2)) makes life a bit easier (see e.g.

[54]) in that under mild excitation conditions it guarantees identifiability.

From stationarity of $\left\{z_{t}\right\}_{t \in \mathbb{Z}}$ it follows that $\left\{y_{t}\right\}_{t \in \mathbb{Z}}$ and $\left\{u_{t}\right\}_{t \in \mathbb{Z}}$ are jointly stationary stochastic processes which can be thought of, respectively, as the output and input of an unknown time-invariant dynamical system ${ }^{3}$ :

$$
y_{t}=\sum_{k=1}^{\infty} f_{k} u_{t-k}+\sum_{k=0}^{\infty} g_{k} e_{t-k}
$$

were $f_{k} \in \mathbb{R}^{1 \times m}$ and $g_{k} \in \mathbb{R}$ are (matrix) coefficients of the unknown impulse responses and $e_{t}$ is the innovation sequence, i.e. the one step ahead linear prediction error

$$
\begin{aligned}
e_{t} & :=y_{t}-\hat{y}_{t \mid t-1} \\
& :=y_{t}-\hat{\mathbb{E}}\left[y_{t} \mid y_{t-1}, y_{t-2}, \ldots, u_{t-1}, u_{t-2}, \ldots\right]
\end{aligned}
$$

where

$$
\begin{aligned}
& \hat{\mathbb{E}}\left[y_{t} \mid y_{t-1}, y_{t-2}, \ldots, u_{t-1}, u_{t-2}, \ldots\right] \\
& :=\sum_{j=1}^{m-1}\left[\sum_{k=1}^{\infty} h_{k}^{[j]} u_{t-k}^{[j]}\right]+\sum_{k=1}^{\infty} h_{k}^{[m]} y_{t-k}
\end{aligned}
$$

The sequences $h_{k}:=\left[h_{k}^{[1]}, . ., h_{k}^{[m-1]}, h_{k}^{[m]}\right] \in \mathbb{R}^{1 \times m}, k \in \mathbb{Z}^{+}$are the predictor impulse response coefficients and are required to describe (BIBO) stable systems, i.e. $h^{[m]} \in \ell_{1}\left(\mathbb{Z}^{+}\right)$.

In the prediction error minimization (PEM) framework identification of the dynamical system in (2) can be framed as estimation of the predictor impulse responses $h_{k}$ in (3) from a finite set of input-output data. We specifically address situations in which $m$ is large as compared to the number of available data and only few variables are in fact needed to predict $y_{t}$. Mathematically this means that $h_{k}^{[i]}=0, \forall k \in \mathbb{Z}^{+}$. In a graphical representation there will be a directed link from the node representing $u_{k}^{[i]}$ to that representing $y_{k}$ if and only if $\exists k \in \mathbb{Z}^{+}: h_{k}^{[i]} \neq 0, i=1, . ., m-1$; in addition there is a self loop if and only if $\exists k \in \mathbb{Z}^{+}: h_{k}^{[m]} \neq 0$. For instance for the network represented in Figure 1, $h_{k}^{[5]}=h_{k}^{[1]}=0, \forall k \in \mathbb{Z}^{+}$ while $h_{k}^{[2]}, h_{k}^{[3]}, h_{k}^{[4]}$ and $h_{k}^{[6]}$ are not identically zero, meaning that for prediction of $y_{t}$ one needs (only) the past of $u^{[2]}, u^{[3]}, u^{[4]}$ and of $y$ itself.

In practice one does not know whether a measured signal is significant for prediction of $y_{t}$. Standard PEM methods [32,49] do not attempt to perform input selection and estimate a "full" model which uses all inputs. As we shall see
${ }^{3}$ In order to streamline notation we shall assume one delay from $u_{t}$ to $y_{t}$. If this is true for all possible decompositions $y_{t}=z_{t}^{[i]}$, $u_{t}=z_{t}^{[-i]}, i=1, \ldots m$, it can be shown that the interconnection is well posed. Of course to achieve stationarity further restrictions have to be imposed.
![img-0.jpeg](img-0.jpeg)

Fig. 1. A dynamical network representing the interaction between $m=6$ variables. The solid edges represent the links related to the dynamical model for node $y_{t}:=z_{t}^{[1]}$ given all the others. With reference to equation (3), absence of links from $u_{t}^{[i]}=z_{t}^{[i+1]}, i=1,5$ to $y_{t}:=z_{t}^{[1]}$ means that $h_{k}^{[1]}=h_{k}^{[5]}=0, \forall k \in \mathbb{Z}^{+}$. The node containing $y_{t}$ has an "entering" arrow which represents the influence of $e_{t}$ (the one step ahead prediction error of $y_{t}$ ). The dotted edges refer to other decompositions of the form (1) where $y_{t}=z_{t}^{[j]}, u_{t}=z_{t}^{[-j]}$ for $j \neq 1$.
this may yield poor results when the number of inputs becomes large as compared to the data available. Variable selection methods has been subject of intense research; classical methods can be found in the books [58,26] while we refer to the survey [25] for a more recent overview.

In this paper we shall be specifically concerned with methodologies which, favoring sparsity, will be able to capture the structure of a dynamical network, like the one Figure 1, and at the same time estimate all the (non-zero) impulse responses $h_{k}^{[i]}$ in (3).

## 3 Preliminaries: kernels for system identification and sparsity inducing priors

### 3.1 Bayesian estimation and Kernel-based regularization

Consider the problem of reconstructing a single unknown function $h$ from indirect noisy measurements. In the framework of Gaussian regression, the key point is to interpret $h$ as (a realization of) a zero-mean Gaussian process whose covariance (also called kernel) encodes the available prior knowledge.

Just for a while, it is now useful to think of $h$ as a continuoustime signal. Often, the only available prior knowledge is the fact that $h$, and possibly some of its derivatives, are continuous with bounded energy. Hence, one often models $h$ as the $p$-fold integral of white noise. If the white noise has unit intensity, the autocorrelation of the process $h$, with

domain restricted to the unit interval, is $W_{p}$ where

$$
\begin{aligned}
& W_{p}(s, t)=\int_{0}^{1} G_{p}(s, u) G_{p}(t, u) d u, \quad s, t \in[0,1] \\
& G_{p}(r, u)=\frac{(r-u)_{+}^{p-1}}{(p-1)!}, \quad(u)_{+}= \begin{cases}u & \text { if } u \geq 0 \\
0 & \text { if } u<0\end{cases}
\end{aligned}
$$

The autocovariance $W_{p}$ is associated with the Bayesian interpretation of the $p$-th order smoothing splines [55]. In particular, when $p=2$, one obtains the cubic spline kernel.

Now, it is useful to recall that, when data become available, the Bayes estimate of $h$ belongs to a reproducing kernel Hilbert space (RKHS) $\mathscr{H}$ defined by the covariance of $h$ [4], Such space is equipped with a norm that, as also illustrated in the sequel, controls the complexity of the function to reconstruct, regularizing the estimation process. For instance, as described in [55], the cubic spline kernel is associated with a particular Sobolev space equipped with the norm

$$
\|h\|_{\mathscr{H}}^{2}=\int_{0}^{1}\left(h^{(2)}(s)\right)^{2} d s
$$

Thus, the Gaussian prior associated with $W_{2}$ introduces information on the smoothness of $h$ via a regularization term given by the energy of the second-order derivative of $h$.

### 3.2 Stable spline kernels

In the system identification scenario, the main drawback of the covariances (4) is that they do not account for impulse response stability, as illustrated in Fig. 2 (left) which displays 100 realizations using an autocovariance proportional to $W_{2}$. In fact, if the autocovariance of $h$ is $W_{p}$, the variance of $h(t)$ is zero at $t=0$ and tends to $\infty$ as $t$ increases. However, if $f$ represents a stable impulse response, one should let it have a finite variance at $t=0$ which goes exponentially to zero as $t$ tends to $\infty$. Following [45], this property can be ensured by modeling $h$ via stable spline kernels defined by

$$
K_{p}(s, t)=W_{p}\left(e^{-\beta s}, e^{-\beta t}\right), \quad s, t \in \mathbb{R}^{+}
$$

where $\beta$ is a positive scalar governing the decay rate of the variance [45,43]. In real applications, $\beta$ will be unknown so that, in what follows, it is treated as a hyperparameter to be estimated from data.
When $p=2$ the autocovariance becomes the Stable Spline kernel introduced in [45]:

$$
K_{2}(t, \tau)=\frac{e^{-\beta(t+\tau)} e^{-\beta \max (t, \tau)}}{2}-\frac{e^{-3 \beta \max (t, \tau)}}{6}
$$

and the following result holds.
Proposition 1 [45] Let $h$ be zero-mean Gaussian with autocovariance $K_{2}$. Then, with probability one, the realizations
![img-1.jpeg](img-1.jpeg)

Fig. 2. Realizations of a stochastic process $h$ with autocovariance proportional to the standard Cubic Spline kernel (left), the new Stable Spline kernel (middle) and its sampled version enriched by a parametric component defined by the poles $-0.5 \pm 0.6 \sqrt{-1}$ (right).
of $h$ are continuous impulse responses of BIBO stable dynamic systems.

The effect of the stability constraint is now illustrated in Fig. 2 (middle) which displays 100 realizations drawn from a zero-mean Gaussian process whose autocovariance is proportional to $K_{2}$ with $\beta=0.4$.

A full characterization of the RKHS induced by the stable spline kernels can be found in [43]. Here, we just recall that the kernel $K_{2}$ induces the following norm

$$
\|h\|_{\mathscr{H}}^{2}=\int_{0}^{\infty}\left(h^{(2)}(s)+\beta h^{(1)}(s)\right)^{2} \frac{e^{3 \beta s}}{\beta^{3}} d s
$$

In this way, the Gaussian prior defined by $K_{2}$ defines a penalty term on $h$ that not only forces the energy of the derivatives to be bounded, but also requires them to decay to zero at least exponentially. Hence, information on both smoothness and exponential stability of $h$ are introduced in the stochastic model.

### 3.3 Prior for predictor impulse responses

Coming back to our original problem, instead of one unknown function, our aim is to estimate the set $\left\{h^{[i]}\right\}$ of discrete-time impulse responses. Then, we model them as sampled versions of continuous-time and independent zeromean Gaussian processes. As in [44], their autocovariances are defined by an "enriched" version of $K_{2}$ and share the same hyperparameters, apart from the scale factors $\left\{\lambda_{i}^{2}\right\}$. More specifically, each discrete-time impulse response $h^{[i]}$ is the convolution of a zero-mean Gaussian process, with autocovariance given by the sampled version of $\lambda_{i}^{2} K_{2}$, with a parametric impulse response $r$ used to capture dynamics hardly represented by a smooth process such as

high-frequency oscillations. The zeta-transform $R(z)$ of $r$ is parametrized as follows

$$
R(z)=\frac{z^{2}}{P_{\theta}(z)}, \quad P_{\theta}(z)=z^{2}+\theta_{1} z+\theta_{2}, \quad \theta \in \Theta \subset \mathbb{R}^{2}
$$

where the feasible region $\Theta$ constraints the two roots of $P_{\theta}(z)$ to belong to the open left unit semicircle in the complex plane. The role of the finite-dimensional component of the model is illustrated in Fig. 2 (right panel). Here, we display some realizations (with samples linearly interpolated) drawn from a discrete-time zero-mean normal process with autocovariance given by $K_{2}$ and enriched using $P_{\theta}(z)=z^{2}+z+0.61$ in (10). This corresponds to introducing high-frequency dynamics in the realizations by enriching the Stable Spline kernel with the poles $-0.5 \pm 0.6 \sqrt{-1}$. The autocovariance of each predictor impulse response $h^{[i]}$, defined by (8) and (10), is denoted by $K: \mathbb{N} \times \mathbb{N} \mapsto \mathbb{R}$ so that one has

$$
\mathbb{E}\left[h_{i}^{[i]} h_{k}^{[i]}\right]=\lambda_{i}^{2} K(\ell, k ; \theta, \beta), \quad i=1, \ldots, m, \quad \ell, k \in \mathbb{N}
$$

### 3.4 Sparsity inducing priors

Differently from the previous subsections, we now discuss a finite-dimensional estimation problem where the goal is to reconstruct the parameter $\phi \in \mathbb{R}^{m}$ in the linear model

$$
y_{i}=X_{i}^{\top} \phi+e_{i}, \quad i=1, \ldots, T
$$

In (12), $\left\{X_{i} \in \mathbb{R}^{m}\right\}$ are the $T$ "regression vectors" while $\left\{e_{i}\right\}$ is zero-mean Gaussian noise of variance $\sigma^{2}$.
When the number $m$ of regressors is very large, e.g. as compared to the number $T$ of data available, obtaining accurate and stable predictors and easily interpretable models becomes a challenging issue which has been quite extensively addressed in the statistical literature in the last decade, see e.g. $[51,6,53,26,17,19,9]$ and references therein.
A pioneering work in this direction has been the so called Lasso (Least Absolute Shrinkage and Selection Operator) [51] that performs regressor selection solving a problem of the form

$$
\hat{\phi}:=\underset{\phi}{\arg \min } \sum_{i=1}^{T}\left(y_{i}-X_{i}^{\top} \phi\right)^{2}+\gamma\|\phi\|_{1}
$$

where the positive scalar $\gamma$ is the so called regularization parameter. Notice that the problem is finite-dimensional and the penalty term involves the $\ell_{1}$ norm in place of the squared norm in a RKHS. In a Bayesian framework, this difference stems from the fact that $\phi$ is no longer modeled as a Gaussian process as in the previous section. In particular, $\hat{\phi}$ can be seen as the Maximum a Posteriori (MAP) estimator once the random vector $\phi$ is independent of the measurement noise and is assigned a double exponential-type prior

$$
\mathbf{p}(\phi) \propto e^{-\xi\|\phi\|_{1}}
$$

yielding

$$
\begin{aligned}
\hat{\phi} & :=\underset{\phi}{\arg \max } \mathbf{p}\left(\left\{y_{i}\right\} \mid \phi\right) \mathbf{p}(\phi) \\
& =\underset{\phi}{\arg \max } e^{-\frac{1}{2 \pi^{2}} \sum_{i=1}^{T}\left(y_{i}-X_{i}^{\top} \phi\right)^{2}} e^{-\xi\|\phi\|_{1}}
\end{aligned}
$$

that is equivalent to problem (13) once $\gamma$ is set to $2 \xi \sigma^{2}$. Despite its nice properties, it has been argued that Lasso had not had a significant impact in statistical practice due to its relative computational inefficiency, see [34]. The Least Angle Regression (LAR) algorithm [17] has provided a new approach to regressor selection and, with minor modifications (the "Lasso modification", [17]), also an efficient implementation of the Lasso.
Recently the Lasso has been proposed for estimation of regression models with autoregressive noise [57] and for Vector Autoregressive with eXogenous inputs (VARX) models [28]. This is a rather straightforward application once the regressor vectors $\left\{X_{i}\right\}$ in (13) are formed with past inputs and outputs and $\phi$ contains the parameters of the finite memory predictors (ARX models).
Another avenue which has been put forward in the statistics literature adopts a Bayesian point of view by modeling the components of $\phi$ as independent Gaussian random variables $\mathbf{p}\left(\phi^{[i]} \mid \lambda_{i}\right)=\mathcal{N}\left(\phi^{[i]} ; 0, \lambda_{i}^{2}\right)$ where

$$
\mathcal{N}\left(\phi ; m, \lambda^{2}\right)=\frac{1}{\sqrt{2 \pi \lambda^{2}}} e^{-\frac{1}{2} \frac{\left(\phi-m\right)^{2}}{\lambda^{2}}}
$$

A second layer is then added to the model by assuming that also the $\lambda_{i}$ 's are random variables with a certain density $\mathbf{p}\left(\lambda_{i}\right)$. It follows that

$$
\mathbf{p}(\phi)=\prod_{i} \int \mathbf{p}\left(\phi^{[i]} \mid \lambda_{i}\right) \mathbf{p}\left(\lambda_{i}\right) d \lambda_{i}
$$

which is a so-called "scale-mixture" distribution [3,59,41,24]. It is well known $[3,59,41]$ that, if $\lambda_{i}^{2}$ has an exponential distribution itself, then $\mathbf{p}(\phi)$ in (16) has the "double exponential" form (14). This is also related to the so called "Relevance Vector Machine" introduced in [53] which, however, uses a Gamma-type of prior on $\lambda_{i}^{-2}$.

### 3.5 Concluding remarks of the section

We have introduced two different signal priors that lead to two different regularization terms. The first one derives from Gaussian assumptions and corresponds to a penalty on the signal given by the squared norm associated with the kernel $K$ in (11), hereby denoted by $\|\cdot\|_{A_{i}}^{2}$. This penalty term is suited for identification of infinite-dimensional discretetime impulse responses. The other one has been introduced in a finite-dimensional context and derives from a double exponential-type prior which leads to the $\ell_{1}$ norm underlying the LASSO.

In the rest of the paper we shall be concerned with a version of the problem (12) where these two types of norms may interact. In particular, each of the components $\phi^{[i]}$ of $\phi$ will become an unknown impulse response $h^{[i]}$ modeled as a zero-mean Gaussian Process with covariance $K$. Hence, the Bayes estimate of each $h^{[i]}$ will belong to an infinitedimensional RKHS denoted by $\mathscr{H}_{K}$. The regressor vectors $\left\{X_{i}\right\}$ will become linear operators whose representation has infinitely many columns and will contain the past histories of $u$ and $y$. Details are found in the next section.

## 4 Variable selection as group sparsity and the sparse identification problem

### 4.1 The sparse identification problem

In this section we shall see how variable selection can be posed as the problem of obtaining sparse solutions of a linear problem similar to (12) discussed in Section 3.4. There are, however, a few notable differences which makes this, in our opinion, a non-trivial extension of previous results. In particular:
(a) Since we are interested in performing variable selection, we would like that certain impulse responses to be identically zero. This is a sort of "group" problem, similar to those discussed in [61]; however our "groups" are the impulse responses $h^{[i]}$. In a parametric scenario (i.e. when the impulse response are modeled in finite dimensional model classes, see e.g. [32,49]) each group of parameters would describe one impulse response. If we restrict our interest to ARX/FIR models this naturally yields to an algorithm for variable selection which we shall call "ARX-GLAR" since we shall exploit the "group LAR" algorithm (as an alternative, one could also use the "group Lasso" [61]). In general however, the parametrization is non-linear and, in addition, a further model selection problem would have to be faced related to the complexity (order) of the parametric class describing each impulse response. We prefer to work in the nonparametric scenario described in Section 3 so that the "groups" live in an infinite dimensional space.
(b) The unknown "parameters" are the (infinite dimensional) impulse responses modeled as Gaussian Processes. This follows the framework developed in the first subsections of Section 3 and yields to a problem formulation similar to multiple kernel learning [5].

For our purposes, it is useful to set up some notation. Let us define

$$
\begin{aligned}
& y_{t}^{-}:=\left[y_{t-1}, y_{t-2}, y_{t-3}, \ldots\right], \quad u_{t}^{-}:=\left[u_{t-1}, u_{t-2}, u_{t-3}, \ldots\right] \\
& y_{t}^{+}:=\left[\begin{array}{c}
y_{t} \\
\vdots \\
y_{t+T-1}
\end{array}\right], \quad e_{t}^{+}:=\left[\begin{array}{c}
e_{t} \\
\vdots \\
e_{t+T-1}
\end{array}\right], \quad h:=\left[\begin{array}{c}
h^{[1]} \\
\vdots \\
h^{[m]}
\end{array}\right] ;
\end{aligned}
$$

where $h^{[i]}, i=1, . ., m$, are impulse responses of stable systems. We also define $A_{t i} \in \mathbb{R}^{T \times m}, i=1, . ., m$, where

$$
\begin{aligned}
& A_{t i}^{[j k]}:=u_{t-j-k}^{[i]}, \quad i=1, . ., m-1 \\
& A_{t m}^{[j k]}:=y_{t-j-k}, \quad j, k \in \mathbb{Z}^{+}
\end{aligned}
$$

In practice, the operators $\left\{A_{t i}\right\}$ above are never completely known since we assume that the measurements $y_{t}, u_{t}$ are only taken in an interval of the form $t \in[1, N]$. However, we will think of each $A_{t i}$ as known setting to zero the unobserved entries. We also let the positive integer $t_{0}$ denote a positive instant sufficiently large to capture the dynamics of the predictor and define

$$
y^{+}:=y_{t_{0}}^{+}, \quad e_{t_{0}}^{+}:=e^{+}, \quad A_{i}:=A_{t_{0} i}
$$

In this way, the predictor in (3) can be rewritten ${ }^{4}$ as:

$$
y^{+}=\underbrace{\left[A_{1} \ldots A_{m}\right]}_{:=A} h+e^{+}
$$

Now, our identification problem corresponds to estimating $h$ in (20), subject to the stability constraints $h^{[i]} \in \ell_{1}\left(\mathbb{Z}^{+}\right)$, $i=1, . ., m$. Recall that we are interested in estimators which automatically select, among $u^{[1]}, . ., u^{[m-1]}, y$, the variables which are useful for predicting $y$ and which are not. In other words, certain impulse responses $\hat{h}^{[i]}$ are expected to be exactly zero. As said, solving this problem entails estimation in "grouped" variables $[61,60]$ but a peculiarity here is that each "group" lives in an infinite dimensional space.

### 4.2 A (non sparse) predictor estimator using Gaussian Regression

Under the framework developed in Section 3.3, we assume that the impulse responses $h^{[i]}$ are zero-mean Gaussian processes with covariance function $K$ in (11) ${ }^{5}$. Hence, the prob-

[^0]
[^0]:    ${ }^{4}$ The product of semi-infinite matrices should be intended as the limit of finite sequences. However, given the assumption $h^{[i]} \in$ $\ell_{1}\left(\mathbb{Z}^{+}\right)$the limit operation is well posed and, as such, we can formally work with the limiting expressions (see [44]).
    5 When not needed, in order to simplify notations we shall omit the explicit dependence on $\theta$ and $\beta$.

lem of estimating the impulse responses $h^{|i|}$ from measured data $\left\{y_{t}, u_{t}\right\}$ can be formulated as the minimum variance estimator

$$
\tilde{h}^{|i|}=\mathbb{E}\left[h^{|i|} \mid\left\{y_{t}, u_{t}\right\}\right], \quad i=1, . ., m
$$

Equivalently, one can assume that $h^{|i|}$ are functions in $\mathscr{H}_{K}$, the reproducing Kernel Hilbert space associated to the sampled Kernel $K$. Under suitable hypotheses discussed in [44] and also later on in Section 6, one has
$\left\{\tilde{h}^{|i|}\right\}_{i=1}^{m}=\underset{\left\{h^{|i|} \in \mathscr{H}_{K}\right\}_{i=1}^{m}}{\arg \min } \quad\left\|y^{+}-\sum_{i=1}^{m} A_{i} h^{|i|}\right\|^{2}+\sigma^{2} \sum_{i=1}^{m} \frac{\left\|h^{|i|}\right\|_{\mathscr{H}_{K}}^{2}}{\lambda_{i}^{2}}$
where $\|\cdot\|$ is the Euclidean norm. Notice that in (21), each $\sigma^{2} / \lambda_{i}^{2}$ represents a regularization parameter that trades fit $y_{t}-\hat{y}_{t \mid t-1}$ vs. regularity of $h^{|i|}$.
In [44], the estimator (21) has been shown to be very competitive with respect to established identification methods such as PEM and subspace methods. However, in the context of the present paper, a limitation of this estimator is that it does not induce sparse solutions since it exploits quadratic criteria to define both the loss and the penalty terms.

### 4.3 Sparsifying the predictor estimator

Motivated from the above discussion, the aim now is to introduce two different approaches to sparsify the estimator (21). They are:
(i) SS-GLAR: a "group version" [61] of (13) extended to a non-parametric setup where the "groups" $h^{|i|}$ are modeled as Gaussian Processes with autocovariance equal to the stable spline kernel (8); including a "Laplace-type" prior which enforces sparsity (see Section 3.4) leads us to a mixed $\ell_{1}-\ell_{2}$ regularization problem which can be seen as a "group" version of the so-called "elastic-net" [65]. It is well known that the $\ell_{2}$ penalty in the elastic net helps in selecting groups of correlated variables [65]. Details will be given in Section 5.
(ii) SSEH: a hierarchical model where $h^{|i|}$ is a Gaussian Process with covariance $\lambda_{i}^{2} K(s, t)$ and the hyperparameters $\left\{\lambda_{i}\right\}$ have an exponential distribution. Differently from the previous approach, notice that this will favor sparsity on the space of scale factors. As mentioned in [11], this is also related to multiple kernel learning, see also [15]. This second technique will actually allow us to introduce more flexibility in the Kernels. In fact, we will model each $h^{|i|}$ using $K$ in (11) that corresponds to the stable spline kernel (8) enriched with the parametric component (10); as argued in [44] this may be advantageous in situations where the impulse responses contain "fast" dynamics penalized by the regularization term, see also [43]. Details will be given in Section 6.

## 5 Stable Splines Group LAR (SSGLAR) algorithm

### 5.1 Enforcing sparsity using the GLAR algorithm

In this section we shall discuss how to modify (21) to enforce sparsity on the groups $h^{|i|}$ using the GLAR algorithm [61]. In order to do so we shall have to assume the parameter $\theta$ in (10) has been fixed (without any prior information it will be fixed equal to zero) and that all the kernel scale factors are equal each other, i.e. $\lambda=\lambda_{i}$ for $i=1, \ldots, m$. In addition, it is worth recalling that the norm $\left\|h^{|i|}\right\|_{\mathscr{H}_{K}}^{2}$ admits a "matrix" representation of the form

$$
\left\|h^{|i|}\right\|_{\mathscr{H}_{K}}^{2}=\left[h^{|i|}\right]^{\top} \Lambda h^{|i|}
$$

where $\Lambda \in \mathbb{R}^{m \times m}$ can be thought of as the "inverse" of the matrix representation of the Kernel $K \in \mathbb{R}^{m \times m}$. The matrix $\Lambda$ is symmetric an positive definite, thus admitting a square root $\Lambda^{1 / 2}$ such that $\Lambda=\Lambda^{1 / 2} \Lambda^{1 / 2} .{ }^{6}$
Now, in place of (20), our measurements model is modified as follows

$$
\tilde{y}^{+}=\sum_{i=1}^{m} \tilde{A}_{i} h^{|i|}+e^{+}
$$

where

$$
\begin{gathered}
\tilde{y}^{+}:=\left[\begin{array}{c}
y^{+} \\
0_{1 \times(i-m)}
\end{array}\right] \\
\tilde{A}_{i}:=\left[\begin{array}{ll}
A_{i} & \chi_{i} \otimes \sqrt{\gamma} \Lambda^{1 / 2}
\end{array}\right], \quad \gamma=\frac{\sigma^{2}}{\lambda^{2}} \\
\chi_{i}:=\left[\underbrace{0 \ldots 0}_{i-1} 1 \underbrace{0 \ldots 0}_{m-i}\right]^{\top}
\end{gathered}
$$

Note that the measurement model (23) is designed so as to include the $\ell_{2}$-type regularization term in (21), which can be written as in equation (22).

Performing input selection can be tackled, as discussed in Section 3.4, via the Group Least Angle Regression algorithm in [17] applied to the regression problem (23). We shall call SS-GLAR (Stable Spline Group Least Angle Regression) the resulting algorithm which we now summarize:

## Algorithm: Stable Spline Group Least Angle Regression (SS-GLAR)

(1) fix the parameter $\beta$ in (11);
(2) fix the parameter $\gamma$ in (24); form the regressor $\tilde{A}_{i}$ in (23) as described in formulas (18), (19), (24) ;
(3) estimate $h^{|i|}$ applying the GLAR algorithm to problem (23);

[^0]
[^0]:    ${ }^{6}$ Given a nondegenerate Borel measure $v$ on $\mathbb{N}$, such operator $\Lambda^{1 / 2}$ is always well defined and corresponds to the matrix form of the square root of the operator $L_{K}$ mapping $h \in \mathscr{H}_{K}$ into the function $\int_{\mathbb{N}} K(s, t) h(t) d v(t)$, see Section 1 in [48] for details.

### 5.2 Estimation of the hyper-parameters

Note that, in order to run the previous algorithm, the following parameters have to be chosen:
(a) the scale factor $\gamma$ of the $\ell_{2}$ penalty in (24) (regularity of $h^{[i]}$ in the space $\mathscr{H}_{K}$ )
(b) the parameter $\beta$ in (11) (decay rate of the Kernel)
(c) the number of non-zero blocks estimated via the GLAR algorithm.

These can be estimated using a validation based approach as follows: Let $\left\{y_{t}, u_{t}\right\}_{t=1, \ldots, N}$ be the available data. We split the data set in two parts. We call identification data set $\left\{y_{t}, u_{t}\right\}_{t=1, \ldots,|2 N / 3|}$ and validation data set $\left\{y_{t}, u_{t}\right\}_{t=|2 N / 3|, \ldots, N}$. We run the identification algorithms on the identification data set fixing the hyperparameters and computing the entire "GLARS path" [61] which consists, for each choice of hyperparameters, of $m$ models differing by the number of non-zero blocks. We grid the hyperparameter space $\left(\beta \in \mathbb{R}^{+}, \gamma \in \mathbb{R}^{+}\right)$so that only a finite (and possibly small) number of alternatives is tested ${ }^{7}$.

The "best" hyperameters and level of sparsity is then selected testing all these models on the validation data set, performance being measured by the root-mean-squared error in one-step-ahead prediction error $R M S_{1}$, where $R M S_{k}$, $k=1,2, \ldots$ is defined as:

$$
R M S_{k}:=\sqrt{\frac{3}{N} \sum_{t=\left\lfloor\frac{N}{k}\right\rfloor+1}^{N}\left(y_{t}-\hat{y}_{t \mid t-k}\right)^{2}}
$$

Then the hyperparameter vector and the level of sparsity are fixed and the model is re-estimated with all data $\left\{y_{t}, u_{t}\right\}_{t=1, \ldots, N}$.

## 6 Stable Splines with Exponential Hyperprior (SSEH) Algorithm

Recall that the estimator (21) is known up to the following parameters:

- the noise variance $\sigma^{2}$;
- the scale factors $\lambda_{i}$ (in fact recall that $h^{[i]}$ are Gaussian processes with covariance $\lambda_{i}^{2} K(t, s)$ );
- $\beta$ that enters the kernel $K$ and is related to the dominant pole of the predictor;
- $\theta$ that represents the parametric part of the model, as defined in (10).

[^0]In this section we will show how the estimator (21) can be "sparsified" by interpreting all the parameters listed above as random vectors and assigning suitable hyperpriors.

### 6.1 Hyperprior for the hyperparameters and the full Bayesian model

Our Bayesian model for sparse identification is defined as follows:

- the noise variance $\sigma^{2}$ will always be estimated via a preliminary step using a low-bias ARX model, as described in [23]. Thus, this parameter, even if always determined from data during our numerical experiments, will be assumed known in the description of our Bayesian model;
- the hyperparameters $\beta, \theta$ and $\left\{\lambda_{i}\right\}$ are described as mutually independent random vectors;
- $\beta$ is given a non informative probability density on $\mathbb{R}^{+}$;
- $\theta$ has a uniform distribution on the feasible region $\Theta$ that constraints the two roots of $P_{\theta}(z)$ to belong to the open left unit semicircle in the complex plane, see (10);
- each $\lambda_{i}$ is an exponential random variable with inverse of the mean (and standard deviation) $\xi \in \mathbb{R}^{+}$, i.e.

$$
\mathbf{p}\left(\lambda_{i}\right)=\xi \exp \left(-\xi \lambda_{i}\right) \chi\left(\lambda_{i} \geq 0\right), \quad i=1, \ldots, m
$$

with $\chi$ the indicator function. We also interpret $\xi$ as a random variable with a non informative prior on $\mathbb{R}^{+}$. Notice that, differently from the approach described in the previous section, the parameters $\lambda_{i}$ are now allowed to be all different thus increasing the flexibility of our model.

In what follows, $\zeta$ indicates the hyperparameter random vector, i.e. $\zeta:=\left[\lambda_{1}, \ldots, \lambda_{m}, \theta_{1}, \theta_{2}, \beta, \xi\right]$.

To simplify the notation, we define $y^{-}:=\left[y_{i_{0}}, y_{i_{0}-1}, y_{i_{0}-2}, \ldots\right]^{T}$ and $u^{-}:=\left[u_{i_{0}}, u_{i_{0}-1}, u_{i_{0}-2}, \ldots\right]^{T}$ where the unobserved entries are set to zero. In addition, $u^{+}:=u_{i_{0}}^{-}$and recall that $y^{+}:=y_{i_{0}}^{-}$. Further, the following approximation is exploited:

$$
\begin{aligned}
& \mathbf{p}\left(y^{\star},\left\{h^{[i]}\right\}, y^{-}, u \mid \zeta\right)= \\
& \propto\left[\prod_{t=i_{0}}^{N} \mathbf{p}\left(y_{t} \mid\left\{h^{[i]}\right\}, y_{t}^{-}, \zeta, u_{t}^{-}\right)\right] \mathbf{p}\left(y^{-},\left\{h^{[i]}\right\}, u^{-} \mid \zeta\right) \\
& \approx\left[\prod_{t=i_{0}}^{N} \mathbf{p}\left(y_{t} \mid\left\{h^{[i]}\right\}, y_{t}^{-}, \zeta, u_{t}^{-}\right)\right] \mathbf{p}\left(\left\{h^{[i]}\right\} \mid \zeta\right) \mathbf{p}\left(y^{-}, u^{-}\right)
\end{aligned}
$$

The first $\propto$ stems from the fact that the predictor of $u_{t}$ given the past $u_{t}^{-}$and $y_{t-1}^{-}$is assumed not to depend on $\zeta$. The last approximated equality follows from the assumption that the past $y^{-}, u^{-}$does not carry information on the predictor impulse responses and the hyperparameters. Our stochastic model is described by the Bayesian network in Fig. 3 (left side).

### 6.2 Estimation of the hyper-parameters

To simplify the notation, the dependence on $y^{-}$and $u$ is omitted in the sequel, so that all the probability densities are now thought of as implicitly conditional on $y^{-}$and $u$.


[^0]:    ${ }^{7}$ We have chosen a logarithmically spaced grid with 11 values for $\beta$ and 5 for $\gamma$. Experimental evidence shows that the results are not very sensitive to choice of hyperparameters, and finer grids did not yield any significant improvement

![img-2.jpeg](img-2.jpeg)

Fig. 3. Bayesian network describing the new nonparametric model for identification of sparse linear systems where $y_{I}^{-}:=\left[y_{1-1}, y_{1-2}, \ldots\right]$ and, in the reduced model, $\lambda:=\lambda_{1}=\ldots=\lambda_{m}$.

We start reporting a preliminary lemma, whose proof can be found in [44], which will be needed in propositions 3 and 4.

Lemma 2 Let the roots of $P_{\theta}$ in (10) be stable. Then, if $\left\{y_{t}\right\}$ and $\left\{u_{t}\right\}$ are zero mean, finite variance stationary stochastic processes, each operator $\left\{A_{i}\right\}$ is almost surely (a.s.) continuous in $\mathscr{H}_{K}$.

We estimate the hyperparameter vector $\zeta$ by optimizing its marginal posterior, i.e. the joint density of $y^{+}, \zeta$ and $\left\{h^{[i]}\right\}$ where all the $\left\{h^{[i]}\right\}$ are integrated out. This is described in the next proposition that derives from simple manipulations of probability densities whose well-posedness is guaranteed by lemma 2. Below, $I_{N}$ is the $N \times N$ identity matrix while, with a slight abuse of notation, $K$ is now seen as an element of $\mathbb{R}^{m \times m}$, i.e. its $i$-th column is the sequence $K(\cdot, i), i \in \mathbb{N}$. The proof of this proposition follows the same lines as that of Proposition 3 in [42] with minor modifications allowing for the presence of feedback and is therefore omitted.

Proposition 3 Let $\left\{y_{t}\right\}$ and $\left\{u_{t}\right\}$ be zero mean, finite variance stationary stochastic processes. Then, under the approximation (27), the maximum a posteriori estimate of $\zeta$ given $y^{+}$is

$$
\begin{aligned}
\hat{\zeta}=\arg \min _{\zeta} & J\left(y^{+} ; \zeta\right) \quad \text { s.t. } \quad \theta \in \Theta, \quad \xi, \beta>0, \quad \lambda_{i} \geq 0 \\
& (i=1, \ldots, m)
\end{aligned}
$$

where $J$ is almost surely well defined pointwise and, using also (27), given by

$$
\begin{aligned}
J\left(y^{+} ; \zeta\right):= & \log \left[\int \mathbf{p}\left(y^{+},\left\{h^{[i]}\right\}, y^{\wedge}, u|\zeta| d h^{[1]} \ldots d h^{[m]}\right]\right. \\
\approx & \frac{1}{2} \log \left(\operatorname{det}\left[2 \pi V\left[y^{+}\right]\right]\right)+\frac{1}{2}\left(y^{+}\right)^{T}\left(V\left[y^{+}\right]\right)^{-1} y^{+}+ \\
& +\xi \sum_{i=1}^{m} \lambda_{i}-\log (\xi)+\text { const }
\end{aligned}
$$

with $V\left[y^{+}\right]=\sigma^{2} I_{N}+\sum_{i=1}^{m} \lambda_{i}^{2} A_{i} K A_{i}^{T}$.
Notice that the first term $\frac{1}{2} \log \left(\operatorname{det}\left[2 \pi V\left[y^{+}\right]\right]\right)$ in the objective (29) penalizes the complexity of the model, in fact it increases as the $\left\{\lambda_{i}\right\}$ get larger. The second term $\frac{1}{2}\left(y^{+}\right)^{T}\left(V\left[y^{+}\right]\right)^{-1} y^{+}$accounts for adherence of experimental data and decreases as the $\left\{\lambda_{i}\right\}$ augment. The third term is a consequence of the hyperprior (26) whose effect is to include an additional $\ell_{1}$ penalty on $\left\{\lambda_{i}\right\}$. Finally, the last term $\log (\xi)$ derives from the same hyperprior and controls the weight of the $\ell_{1}$ norm which is estimated jointly with the other hyperparameters. Overall, our objective can be interpreted as a Bayesian modified version of that connected with multiple kernel learning, see Section 3 in [15].

An important issue for the practical use of our numerical scheme is the availability of a good starting point for the optimizer. Below, we describe a scheme that achieves a suboptimal solution just solving an optimization problem in $\mathbb{R}^{4}$ related to the reduced Bayesian model of Fig. 3 (right side). Our main idea is to optimize the objective under the constraint $\lambda_{i}=\lambda$, for $i=1, \ldots, m$, and removing the $\ell_{1}$ penalty on $\left\{\lambda_{i}\right\}$. The resulting estimate of $\lambda$ is used to obtain an estimate of $\xi$ which is then exploited to sparsify the solution. This is described below.
i) Obtain $\left\{\hat{\lambda}_{i}\right\}, \hat{\theta}$ and $\hat{\beta}$ solving the following modified version of problem (28)

$$
\begin{gathered}
\arg \min _{\zeta}\left[J\left(y^{+} ; \zeta\right)-\xi \sum_{i=1}^{m} \lambda_{i}+\log (\xi)\right] \\
\text { s.t. } \theta \in \Theta, \quad \beta>0, \quad \lambda_{1}=\ldots=\lambda_{m} \geq 0
\end{gathered}
$$

ii) Set $\hat{\xi}=1 / \hat{\lambda}_{1}$ and $\hat{\zeta}=\left[\hat{\lambda}_{1}, \ldots, \hat{\lambda}_{m}, \hat{\theta}, \hat{\beta}, \hat{\xi}\right]$. For $i=1, \ldots, m$ do:
set $\hat{\zeta}=\hat{\zeta}$ except that the $i$-th component of $\hat{\zeta}$ is set to 0 ; if $J\left(y^{+} ; \hat{\zeta}\right) \leq J\left(y^{+} ; \hat{\zeta}\right)$, set $\hat{\zeta}=\hat{\zeta}$.

The procedure we have outlined in step ii) may suffer when the inputs are highly correlated, possibly making it sensitive to the order in which the components of $\hat{\zeta}$ are set to zero. In order to circumvent this difficulty, an alternative consists of using the following "Bayesian forward-selection" type of algorithm where, at every step, the next variable to be included in the model is that leading to the largest objective's improvement. This is obtained substituting item ii) above with:
ii') Let us denote with $I$ the index set of "selected" variables, define $\hat{\zeta}_{I}=\left[\hat{\lambda}_{1}, \ldots, \hat{\lambda}_{m}, \hat{\theta}, \hat{\beta}, \hat{\xi}\right]$ where $\hat{\lambda}_{i}=\hat{\lambda}_{i}$ if $i \in I$ and $\hat{\lambda}_{i}=0$ otherwise. Initialize $I:=\emptyset$ and repeat the following procedure:
(a) for $j \in\{1, . ., m\} \backslash I$, define $I_{j}^{\prime}:=I \cup j$ and compute $J\left(y^{+} ; \zeta_{I_{j}^{\prime}}\right)$.

(b) select

$$
\hat{j}:=\underset{j \in\{1, \ldots, m\} \backslash I}{\arg \max } J\left(y^{\boldsymbol{+}} ; \hat{\zeta}_{I_{j}^{\prime}}\right)-J\left(y^{\boldsymbol{+}} ; \hat{\zeta}_{I}\right)
$$

(c) if $J\left(y^{\boldsymbol{+}} ; \hat{\zeta}_{I_{j}^{\prime}}\right)-J\left(y^{\boldsymbol{+}} ; \hat{\zeta}_{I}\right)>0$
set $I:=I_{j}^{\prime}$ and go back to (a)
else
finish.
The set $I$ contains the indexes of selected variables and $\hat{\zeta}_{I}$ is used as a starting point for the optimization problem (29).

Remark 1 Note that more elaborated procedures for variable selection have been proposed which combine forward and backward (addition and elimination) steps such as those introduced and analyzed in [2,62]. Our main focus here is not however on this specific step and further comparative analysis with the literature is postponed to future work. Let us also stress that the results in [56] provide support for the use of forward selection procedures for screening purposes.

### 6.3 Estimation of the predictor impulse responses for known $\zeta$

Once all the unknown parameters are learnt from data following the procedure outlined in the previous subsection, the estimator (21) becomes completely known. Hence, the following result, that comes from the representer theorem whose applicability is guaranteed by lemma 2 (see [44] for details), can be utilized to achieve the unknown predictor impulse responses.

Proposition 4 Under the same assumptions of Proposition 3, almost surely we have
$\left\{\hat{h}^{[i]}\right\}_{i=1}^{m}=\underset{\left\{h^{[i]} \in \mathscr{H}_{K}\right\}_{i=1}^{m}}{\arg \min } \quad\left\|y^{\boldsymbol{+}}-\sum_{i=1}^{m} A_{i} h^{[i]}\right\|^{2}+\sigma^{2} \sum_{i=1}^{m} \frac{\left\|h^{[i]}\right\|_{A_{K}^{2}}^{2}}{\lambda_{i}^{2}}$
where $\|\cdot\|$ is the Euclidean norm. Moreover, almost surely we also have for $k=1, \ldots, m$

$$
\hat{h}^{[i]}=\lambda_{i}^{2} K A_{i}^{T} c, \quad c=\left(\sigma^{2} I_{N}+\sum_{i=1}^{m} \lambda_{i}^{2} A_{i} K A_{i}^{T}\right)^{-1} y^{+}
$$

After obtaining the estimates of the $\left\{h^{[i]}\right\}$, simple formulas can then be used to derive the system impulse responses $f$ and $g$ in (2) and hence also the $k$-step ahead predictors, see [32] for details.

## 7 Simulation results

We consider three Monte Carlo studies of 300 runs where at any run an ARMAX linear system with 15 inputs is generated as follows

- the number of $h^{[i]}$ different from zero is randomly drawn from the set $\{1,2, \ldots, 10\}$.
- Then, the order of the ARMAX model is randomly chosen in $[1,30]$ and the model is generated by the MATLAB function drmodel.m. The system and the predictor poles are restricted to have modulus less than 0.95 with the $\ell_{2}$ norm of each $h^{[i]}$ bounded by 10 .

For each run in the Monte Carlo experiments an identification data set of size 500 and a test set of size 1000 are generated.

In the first experimental setup a white noise input with uncorrelated components is used. In the second one the input still has uncorrelated components each being generated via the MATLAB function idinput . m as a realization from a random Gaussian signal with band ${ }^{8}[0,0.8]$ for the identification data and $[0,0.9]$ for the validation data; this clearly makes prediction on new data more challenging. In the third Monte Carlo experiment the inputs used for identification are white but are allowed to be correlated, being generated according to the following model:

$$
u_{k}^{[i+1]}=u_{k}^{[i]}+v_{k}^{[i]} \quad i=1, \ldots, m-2
$$

where $\left\{u_{k}^{[1]}\right\}$ is unit variance white noise sequence while $\left\{v_{k}^{[i]}\right\}$ is a white noise sequence, independent of $\left\{u_{k}^{[1]}\right\},\left\{v_{k}^{[i]}\right\}, j<i$ with variance $\varepsilon^{2}=0.04$. With this choice, the correlation coefficient
$\rho_{i}:=\frac{\mathbb{E}\left(u_{k}^{[i]} u_{k}^{[i+1]}\right)}{\sqrt{\mathbb{E}\left(u_{k}^{[i]} u_{k}^{[i]}\right) \mathbb{E}\left(u_{k}^{[i+1]} u_{k}^{[i+1]}\right)}}=\frac{\operatorname{Var}\left\{u_{k}^{[i]}\right\}}{\sqrt{\operatorname{Var}\left\{u_{k}^{[i]}\right\} \operatorname{Var}\left\{u_{k}^{[i+1]}\right\}}}$
satisfies

$$
\rho_{i} \in[0.9806,0.9871] \quad i \in[1,14]
$$

Note that correlated inputs renders the input selection problem more challenging. The test set, instead is generated using independent zero mean, unit variance white noises as inputs.

We compare the following estimators:
(1) GLAR: this is the GLAR algorithm described in [61] applied to ARX models; the order (between 1 and 30) and the level of sparsity (i.e. the number of null $h^{[i]}$ ) is determined using the first $2 / 3$ of the 500 available data as training set and the remaining part as validation data (the use of $C_{p}$ statistics does not provide better results in this case).
(2) PEM+Oracle: this is the classical PEM approach, as implemented in the pem.m function of the MATLAB

[^0]
[^0]:    8 The boundaries specify the lower and upper limits of the passband, expressed as fractions of the Nyquist frequency.

![img-3.jpeg](img-3.jpeg)

Fig. 4. Boxplot of Coefficient of Determination for one-step-ahead prediction $\left(C O D_{1}\right)$. PEM + Oracle is PEM with an oracle who knows which impulse responses are zero and has access to validation data in order to select the best performing system order. The notation "Plus $x x$ " means that there are $x x$ "outliers" which are left out of the plot.

System Identification Toolbox [33], equipped with an oracle that, at every run, knows which predictor impulse response are zero and, having access to the test set, selects those model orders that provide the best prediction performance.
(3) SSGLAR: this is the approach which combines GLAR and the Stable Spline prior for impulse responses, as detailed in Section 5. The first 40 available input/output pairs enter the $\left\{A_{i}\right\}$ in (20), i.e. $t_{0}=40$ in (19). For computational reasons the predictor length is set to 40 , a number that does not establish any trade-off between bias and variance but is just sufficiently large to capture the predictor dynamics.
(4) SSEH: this is the approach described in Section 6, which is based on the full Bayesian model of Fig. 3. As done before, we set both $t_{0}$ and the predictor length to 40 .
(5) Suboptimal SSEH: the same as above except that we exploit the reduced Bayesian model of Fig. 3 complemented with the procedure described at the end of sub-
section 6.2, with the refined step ii' used only in the third Monte Carlo experiment.
(6) PEM+VAL: this is the classical PEM approach that uses validation data for model order selection. The order of the polynomials in the ARMAX model are not allowed to be different each other since this would lead to a combinatorial explosion of the number of competitive models.
(7) PEM+BIC: this is the classical PEM approach that uses BIC for model order selection. The order of the polynomials in the ARMAX model are not allowed to be different each other since this would lead to a combinatorial explosion of the number of competitive models.
(8) PEM+BIC+or2: this is the same as PEM + BIC with and additional oracle knowing which impulse responses are zero.
(9) PEM+VAL+or2: this is the same as PEM + BIC + or2 besides the fact that the order is estimated using validation data rather than BIC.

![img-4.jpeg](img-4.jpeg)

Fig. 5. Boxplot of Coefficient of Determination for one-step-ahead prediction (COD₁). PEM + Oracle is PEM with an oracle who knows which impulse responses are zero and has access to validation data in order to select the best performing system order. PEM + BIC + or2 and PEM +VAL + or2 are equipped with an oracle who knows which impulse responses are zero. The notation "Plus xx" means that there are xx "outliers" which are left out of the plot.

![img-5.jpeg](img-5.jpeg)

Fig. 6. $\overline{C O D}_{k}$, i.e. average coefficient of determination relative to $k$-step ahead prediction, obtained during the Monte Carlo study \#1 (top), \#2 (center) and \#3 (bottom), using PEM+Oracle $(\bullet)$, SSCH (○), Suboptimal SSCH $(\times)$, SSGLAR (○) GLAR (*)

![img-6.jpeg](img-6.jpeg)

Fig. 7. $\overline{C O D}_{k}$, i.e. average coefficient of determination relative to $k$-step ahead prediction, obtained during the Monte Carlo study \#1 (top), \#2 (center) and \#3 (bottom), using PEM+Oracle ( $\bullet$ ), SSEH ( $\circ$ ), PEM with order estimated via BIC and knowledge of which impulse responses are zero $(\times)$, PEM with order estimated via validation and knowledge of which impulse responses are zero ( $\circ$ )


Table 1
Percentage of the $h^{[i]}$ equal to zero correctly set to zero by the employed estimator.

The following performance indexes are considered:
(1) Percentage of the impulse responses equal to zero correctly set to zero by the estimator.
(2) $k$-step-ahead Coefficient of Determination, denoted by $C O D_{k}$, quantifying how much of the test set variance is explained by the forecast. It is computed at each run as

$$
\begin{gathered}
C O D_{k}:=1-\frac{R M S_{k}^{2}}{\frac{1000}{1000} \sum_{i=1}^{1000}\left(y_{i}^{t e s t}-\hat{y}_{i}^{t e s t}\right)^{2}} \\
R M S_{k}:=\sqrt{\frac{1}{1000} \sum_{i=1}^{1000}\left(y_{i}^{t e s t}-\hat{y}_{i \mid t-k}^{t e s t}\right)^{2}}
\end{gathered}
$$

where $\hat{y}^{t e s t}$ is the sample mean of the test set data $\left\{y_{i}^{t e s t}\right\}_{i=1}^{1000}$ and $\hat{y}_{i \mid t-k}^{t e s t}$ is the $k$-step ahead prediction computed using the estimated model. The average index obtained during the Monte Carlo study, as a function of $k$, is then denoted by $\overline{C O D}_{k}$.

Notice that, in both of the cases, the larger the index, the better is the performance of the estimator.
In every experiment the performance of PEM+VAL and PEM+BIC has been largely unsatisfactory, providing strongly negative values for $\overline{C O D}_{k}$. This is illustrated e.g. in Fig. 4 showing the boxplots of the 300 values of $C O D_{1}$ obtained by the employed estimators on the three Monte Carlo studies. We have also assessed that results do not improve using AIC. In view of this, in what follows other results from PEM+VAL and PEM+BIC will not be shown; for sake of comparison we add in Figs. 7 and 5 comparison with PEM+BIC+or2 and PEM+VAL+or2 which use knowledge of which impulse responses are zero.
Table 1 reports the percentage of the predictor impulse responses equal to zero correctly estimated as zero by the estimators. In terms of predictive performance the Stable Spline estimators (SSEH and SSGLAR) outperform GLAR, with a slight advantage of SSEH; instead, in terms of sparsity of the estimated model, SSEH and Suboptimal SSEH show a definite advantage over GLAR-based techniques, achieving the remarkable performance of $99 \%$ correct detection of the "zero" impulse responses.

We conjecture that the superior performance of SSEH can be attributed to the fact that it combines the advantages of the Stable-Spline regularization (giving good performance in prediction, [44]) and those of the exponential hyperprior favoring sparsity. On the other hand note that the SSGLAR algorithm, which combines $\ell_{2}$ and $\ell_{1}$ penalties like the elastic-
net, tends to overestimate the number of nonzero impulse responses. While a rigorous explanation of this behavior is the subject of current research, its is worth stressing that the SSEH procedure combines a "forward selection" initialization with an optimization based refinement; this can be seen as an instance of the "screening" procedure analyzed in [56].

Finally, Figs. 6 and 7 display $\overline{C O D}_{k}$ as a function of the prediction horizon obtained during the Monte Carlo study $\# 1$ (top), \#2 (center) and \#3 (bottom). The performance of Stable Spline appears superior than that of GLAR and is comparable with that of PEM+Oracle also when the reduced Bayesian model of Fig. 3 is used.

## 8 Conclusions

Identification of large scale dynamical systems in the framework of dynamical Bayesian networks has been discussed. It has been argued that estimation of network connectivity and dynamic interaction can be framed as identification of a sparse multi-input, single-output dynamical system. Two new methods have been presented which combine recently developed non-parametric methods for system identification and sparsity-favoring algorithms. The two methods (SSGLAR and SSEH) have been compared via extensive simulation studies with state-of-the art algorithms such as the Group Least Angle Regression (LARS) algorithm applied to ARX models and Prediction Error Methods (PEM). Several simulation setups have been considered including low pass input excitation as well as highly correlated inputs. The advantages of the new methods (especially SSEH) is apparent both in terms of predictive capabilities on new data as well as regarding the ability of detecting the network connectivity (i.e. the percentage of correctly detected zeros). Future work will concentrate on the analysis of the proposed methods. In particular we envision that properties of the so-called multivariate Laplace distribution [18] may be relevant. In addition also dedicated numerical optimization procedures will be developed.

Acknowledgments This research has been partially supported by the PRIN Project "New Methods and Algorithms for Identification and Adaptive Control of Technological Systems", by the Progetto di Ateneo CPDA090135/09 funded by the University of Padova and by the European Communitys Seventh Framework Programme under agreement n. FP7-ICT-223866-FeedNetBack.
