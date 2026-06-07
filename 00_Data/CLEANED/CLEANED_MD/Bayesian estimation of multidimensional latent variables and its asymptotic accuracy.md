# Bayesian Estimation of Multidimensional Latent Variables and Its Asymptotic Accuracy 

Keisuke Yamazaki<br>k.yamazaki@aist.go.jp<br>Artificial Intelligence Research Center,<br>National Institute of Advanced Industrial Science and Technology<br>2-3-26 Aomi, Koto-ku, Tokyo, Japan


#### Abstract

Hierarchical learning models, such as mixture models and Bayesian networks, are widely employed for unsupervised learning tasks, such as clustering analysis. They consist of observable and latent variables, which represent the given data and their underlying generation process, respectively. It has been pointed out that conventional statistical analysis is not applicable to these models, because redundancy of the latent variable produces singularities in the parameter space. In recent years, a method based on algebraic geometry has allowed us to analyze the accuracy of predicting observable variables when using Bayesian estimation. However, how to analyze latent variables has not been sufficiently studied, even though one of the main issues in unsupervised learning is to determine how accurately the latent variable is estimated. A previous study proposed a method that can be used when the range of the latent variable is redundant compared with the model generating data. The present paper extends that method to the situation in which the latent variables have redundant dimensions. We formulate new error functions and derive their asymptotic forms. Calculation of the error functions is demonstrated in two-layered Bayesian networks.


Keywords: unsupervised learning, hierarchical parametric models, Bayesian statistics, algebraic geometry, singularities

## 1 Introduction

Hierarchical parametric models, such as Gaussian mixtures, Boltzmann machines, and Bayesian networks, are often used for unsupervised learning. These models use two variables to express their structure: observable variables that represent the

given data, and latent variables that imply the hidden structure or labels. The task of unsupervised learning is to estimate the latent variables. For example, in cluster analysis with a Gaussian mixture model, the latent variable expresses a cluster label that indicates which cluster generated the data point, and the task is to assign a label to each of the data points.

Due to their structure, hierarchical models have singularities in their parameter space. Probabilistic learning models generally fall into one of two classes: regular and singular. A regular model has a one-to-one relation between the parameters and the expression of the model as a probability function; a singular model does not. Singularities adversely affect conventional statistical analysis; they reduce the rank of the Fisher information matrix, which is required by the analysis to be positive definite. Thus, results based on regularity are not valid in singular models; this includes asymptotic analysis on the maximum likelihood estimator and the use of model selection criterion, such as the BIC or MDL [12, 10].

To tackle this issue, modern mathematics, such as the field of algebraic geometry, has been applied to the analysis of models using Bayesian statistics [13, 14]. Asymptotic properties of some important functions have been clarified by using this method. As a substitute for the BIC, the marginal likelihood has been used to evaluate various models [21, 22, 23, 11, 3, 2, 24]. The results directly reveal the accuracy of measuring the generalization error when predicting observable variables. A novel model selection criterion based on the asymptotic error has been proposed [15]. The posterior distribution plays an important role in the Bayesian statistics. Specifically, its convergence rate is one of the main concerns in the statistical literature, and has been analyzed (e.g., $[4,7,6]$ ). For the cases with singularities, the rate based on the Wasserstein metrics is elucidated in both finite and infinite mixture models [9]. Using the algebraic techniques, the identifiability of the hierarchical models is discussed in [1].

The estimation accuracy of the latent variables has not been sufficiently studied, even though they are one of the main concerns in unsupervised learning. It is not straightforward to evaluate the estimation result, because the optimality varies due to many factors, such as the intended use of the results and prior knowledge about the given data. In the case of hierarchical models, however, we can estimate the variables and evaluate the results in a distribution-based manner; the probability of the latent variables is naturally formulated from the model expression, and the accuracy can be defined by differences in the distributions. Using this approach, an analysis method has been proposed and the asymptotic form of an error function is available for applying the maximum likelihood method and the Bayes method to regular cases [17]. The algebraic geometrical method is again applicable to singular cases in the Bayes method. It has been found that singularities play an essential role in determining the convergence of the error [18].

Singularities appear when the model is redundant compared with the true distri-

bution, from which the data are generated. There are two cases in which redundancy emerges: the latent value may have a redundant range or it may have redundant dimensions. In our previous studies [17, 18], we considered mixture models, in which there is only one latent variable that expresses to which component the data point belongs. For example, suppose a model has $K$ components, and the latent variable is described by $y \in\{1, \ldots, K\}$, while the true distribution has $K^{*}$ components, where $K^{*}<K$; this is a case where the range has redundancy. In the present paper, we will consider the other case, that is, where the latent variable is multidimensional, and it has redundancy. For example, in a Bayesian network, let the latent nodes be $y=\left(y_{1}, y_{2}, \ldots, y_{K}\right)$. Note that each element has a range, that is, $y_{i} \in\left\{1, \ldots, L_{i}\right\}$. When the true model has the latent nodes $y=\left(y_{1}, \ldots, y_{K^{*}}\right)$ for $K^{*}<K$, singularities appear in the parameter space of the model. The standard error function measures the accuracy with the Kullback-Leibler (KL) divergence; note that the following loss function, which was used in our previous study [17], is not well-defined:

$$
\sum_{y} q(y \mid x) \ln \frac{q(y \mid x)}{p(y \mid x)}
$$

where $x$ is the observable variable, and $q(y \mid x)$ and $p(y \mid x)$ are, respectively, the true and estimated distributions of the latent variable. Since the latent variable $y$ will have different dimensions in $q$ and $p$, this loss function cannot be used when the latent variable is multidimensional.

In the present paper, we provide new definitions for the error function for the multidimensional case and derive the asymptotic form of their Bayesian estimation. Section 2 briefly summarizes the Bayesian estimation of the latent variable. Section 3 introduces some estimation tasks and the definitions of the error for both the non-redundant and the redundant case. Section 4 presents the asymptotic forms, and Section 5 demonstrates the actual error that occurs with two-layered Bayesian networks. A discussion and our conclusions are presented in Sections 6 and 7, respectively.

# 2 Bayesian Estimation of a Latent Variable 

This section formulates the Bayesian estimation of a latent variable. Let a learning model be expressed as

$$
p(x \mid w)=\sum_{y} p(x, y \mid w)
$$

where $x \in R^{M}$ is an observable variable describing $M$-dimensional data, $w$ stands for the parameters, and $y \in\{1, \ldots, L\}^{K}$ is a latent variable describing $K$-dimensional

![img-0.jpeg](img-0.jpeg)


Figure 1: Simple two-layer Bayesian network: structure (left panel), CPTs of nodes $y_{1}$ and $y_{2}$ (middle panel), and CPT of node $x_{m}$ (right panel).
discrete labels. By replacing $\int d x$ with $\sum_{x}$, the results in the present paper still hold when the observable variable is discrete.

We now show some examples of hierarchical models. A Gaussian mixture model is given by

$$
p(x \mid w)=a_{1} \mathcal{N}\left(x \mid b_{1}\right)+a_{2} \mathcal{N}\left(x \mid b_{2}\right)
$$

where $\mathcal{N}(x \mid b)$ is a Gaussian distribution with the parameter $b$. Note that the mean and the variance parameters can be included in $b$. The parameter of this model is $w=\left\{a_{1}, b_{1}, b_{2}\right\}$, where $0 \leq a_{1} \leq 1$ and $a_{2}=1-a_{1}$. The mixture has a onedimensional label $y=\{1,2\}$ that describes the number of components, and the model expression of Eq. (2) is rewritten as

$$
p(x \mid w)=\sum_{y=1,2} a_{y} \mathcal{N}\left(x \mid b_{y}\right)=\sum_{y=1,2} p(x, y \mid w)
$$

Next, we introduce an example with a multidimensional label; the simple twolayered binary Bayesian network described in Fig. 1 is given by

$$
p(x \mid w)=\sum_{y_{1}=0,1} \sum_{y_{2}=0,1} a_{1 y_{1}} a_{2 y_{2}} \prod_{m=1}^{M} b_{y_{1} y_{2} m}^{\left(1-x_{m}\right)}\left(1-b_{y_{1} y_{2} m}\right)^{x_{m}}
$$

where $x=\left(x_{1}, \ldots, x_{M}\right) \in\{0,1\}^{M}$, and the parameter is $w=\left\{a_{10}, a_{20}, b_{i j m}\right\}$ for $i, j=0,1$ and $m=1, \ldots, M$, such that $0 \leq a_{10} \leq 1, a_{11}=1-a_{10}, 0 \leq a_{20} \leq$ $1, a_{21}=1-a_{20}$, and $0 \leq b_{i j m} \leq 1$. This model has a two-dimensional label $y=\left(y_{1}, y_{2}\right) \in\{0,1\}^{2}$. We will show a network with a general-dimensional label in Section 5. It is easily confirmed that the two-layered Bayesian network is a natural extension of the naive Bayesian network, which has a single latent latent node. Since there are more than one latent node, the two-layered networks can deal with the multilabel clustering, where the effect of multiple latent factors on the observable variables is reflected in the result and the necessary and the nuisance factors are distinguished in the unsupervised manner.

Let the data-generating model, referred to as the true model, be expressed as

$$
q(x)=\sum_{y} q(x, y)
$$

where the latent variable is described by $y \in\left\{1, \ldots, L^{*}\right\}^{K^{*}}$. The difference in the dimensions, such that $K>K^{*}$, implies the existence of redundant latent variables. The present paper assumes that the learning model can attain the true model, i.e., $K \geq K^{*}, L \geq L^{*}$, and that the set $W_{t}=\left\{w^{*}: p\left(x \mid w^{*}\right)=q(x)\right\}$ is not empty. Note that the range of each dimension of $y$ can be different; for example, it may be that $y=\left(y_{1}, \ldots, y_{K^{*}}\right), y_{k} \in\left\{1, \ldots, L_{k}^{*}\right\}$. For simplicity, we consider the case $L_{1}^{*}=\cdots=$ $L_{K^{*}}^{*}$. In the present paper, we will formulate error functions for the estimation of the latent variable, both with and without redundant dimensions. Since the error function will based on the KL divergence including the factor $\ln q(y \mid x) / p(y \mid x)$, the situation $K<K^{*}$ or $L<L^{*}$ is not well-defined; the factor diverges to infinity when $p(y \mid x)=0$ and $q(y \mid x) \neq 0$. This is the reason why we consider $K \geq K^{*}$ and $L \geq L^{*}$.

Let us formalize the data set. The true model is assumed to generate data that are independently and identically distributed. Let a set of $n$ given data be $X^{n}=$ $\left\{x_{1}, \ldots, x_{n}\right\}$. The corresponding latent variables are denoted $Y^{n}=\left\{y_{1}, \ldots, y_{n}\right\}$. The detailed expressions are $x_{i}=\left(x_{i 1}, \ldots, x_{i M}\right)$ and $y_{i}=\left(y_{i 1}, \ldots, y_{i L}\right)$, respectively. We will write them as pairs as follows: $\left(X^{n}, Y^{n}\right)=\left\{\left(x_{1}, y_{1}\right), \ldots,\left(x_{n}, y_{n}\right)\right\}$.

To deal with the redundant dimensions of the latent variable, we divide the variable in the learning model into two parts: $y_{i}=\left(y_{i}^{(1)}, y_{i}^{(2)}\right)$, where $y_{i}^{(1)} \in\{1, \ldots, L\}^{K^{*}}$, and $y_{i}^{(2)} \in\{1, \ldots, L\}^{K-K^{*}}$. More precisely, for $y_{i}=\left(y_{i 1}, \ldots, y_{i K}\right)$, the two parts are given by

$$
\begin{aligned}
& y_{i}^{(1)}=\left(y_{i 1}^{(1)}, \ldots, y_{i K^{*}}^{(1)}\right)=\left(y_{i 1}, \ldots, y_{i K^{*}}\right) \\
& y_{i}^{(2)}=\left(y_{i 1}^{(2)}, \ldots, y_{i K-K^{*}}^{(2)}\right)=\left(y_{i K^{*}+1}, \ldots, y_{i K}\right)
\end{aligned}
$$

We also use $Y_{i}^{n}=\left\{y_{1}^{(i)}, \ldots, y_{n}^{(i)}\right\}$ for $i=1,2$.
We consider a distribution-based estimation of the latent variables; that is, estimating $Y^{n}$ from the given data $X^{n}$ is represented by constructing the distribution $p\left(Y^{n} \mid X^{n}\right)$. In general Bayesian statistics, the marginal likelihood is defined by

$$
Z\left(X^{n}\right)=\int \prod_{i=1}^{n} p\left(x_{i} \mid w\right) \varphi(w ; \eta) d w
$$

where $\varphi(w ; \eta)$ is a prior with a hyperparameter $\eta$. We define the marginal likelihood of the complete data as

$$
Z\left(X^{n}, Y^{n}\right)=\int \prod_{i=1}^{n} p\left(x_{i}, y_{i} \mid w\right) \varphi(w ; \eta) d w
$$

where $Z\left(X^{n}\right)=\sum_{Y^{n}} Z\left(X^{n}, Y^{n}\right)$. As introduced in [17], the Bayesian estimation of the latent variables is given by

$$
p\left(Y^{n} \mid X^{n}\right)=\frac{Z\left(X^{n}, Y^{n}\right)}{Z\left(X^{n}\right)}
$$

The true distribution is given by

$$
q\left(Y^{n} \mid X^{n}\right)=\prod_{i=1}^{n} \frac{q\left(x_{i}, y_{i}\right)}{q\left(x_{i}\right)}=\prod_{i=1}^{n} q\left(y_{i} \mid x_{i}\right)
$$

Note that $Y^{n} \in\{1, \ldots, L\}^{K n}$ in $p\left(Y^{n} \mid X^{n}\right)$, while $Y^{n} \in\left\{1, \ldots, L^{*}\right\}^{K^{*} n}$ in $q\left(Y^{n} \mid X^{n}\right)$. To avoid this confusion, we use the following summation symbols:

$$
\begin{aligned}
& \sum_{Y^{n}: K}^{L}=\sum_{y_{11}=1}^{L} \cdots \sum_{y_{1 K}=1}^{L} \sum_{y_{21}=1}^{L} \cdots \sum_{y_{2 K}=1}^{L} \cdots \sum_{y_{n 1}=1}^{L} \cdots \sum_{y_{n K}=1}^{L} \\
& \sum_{Y^{n}: K^{*}}^{L^{*}}=\sum_{y_{11}=1}^{L^{*}} \cdots \sum_{y_{1 K^{*}}=1}^{L^{*}} \sum_{y_{21}=1}^{L^{*}} \cdots \sum_{y_{2 K^{*}}=1}^{L^{*}} \cdots \sum_{y_{n 1}=1}^{L^{*}} \cdots \sum_{y_{n K^{*}}=1}^{L^{*}}
\end{aligned}
$$

# 3 Error Functions for Multidimensional Latent Variables 

In this section, we propose and formulate error functions for measuring the estimation accuracy. We consider two cases: when the latent variable does not have redundant dimensions, $K=K^{*}$; and when it does, $K>K^{*}$.

### 3.1 Non-Redundant Case

If there are no redundant dimensions in the latent variables, i.e., $K=K^{*}$, the error function is given by the KL divergence from the true distribution to the estimated distribution $[16]$ :

$$
D_{n 1}(n)=\frac{1}{n} E_{X^{n}}\left[\sum_{Y^{n}: K^{*}}^{L^{*}} q\left(Y^{n} \mid X^{n}\right) \ln \frac{q\left(Y^{n} \mid X^{n}\right)}{p\left(Y^{n} \mid X^{n}\right)}\right]
$$

where $E_{X^{n}}\left[f\left(X^{n}\right)\right]=\int f\left(X^{n}\right) q\left(X^{n}\right) d X^{n}$. This is a natural extension of a onedimensional latent variable. We refer to this as a joint error function, since it corresponds to measuring the joint probability of the dimensions, i.e., $q\left(Y^{n} \mid X^{n}\right)=$ $\prod_{i=1}^{n} q\left(y_{i 1}, \ldots, y_{i K^{*}} \mid x_{i}\right)$.

We also consider the situation in which there are partial target dimensions to be estimated. Let us divide $y_{i}^{(1)}$ into two parts, as follows:

$$
\begin{aligned}
y_{i}^{(1)} & =\left(y_{i}^{(11)}, y_{i}^{(12)}\right) \\
y_{i}^{(11)} & =\left(y_{i 1}, \ldots, y_{i K_{t}}\right) \\
y_{i}^{(12)} & =\left(y_{i K_{t}+1}, \ldots, y_{i K^{*}}\right)
\end{aligned}
$$

where $k=1, \ldots, K_{t}$ such that $K_{t}<K^{*}$ is the dimensionality of the target. We use the notation $Y_{1 j}^{n}=\left\{y_{1}^{(1 j)}, \ldots, y_{n}^{(1 j)}\right\}$ for $j=1,2$. In this case, the nuisance dimensions $k=K_{t}+1, \ldots, K^{*}$ will be ignored when evaluating the accuracy. The error function is given by

$$
D_{n 2}(n)=\frac{1}{n} E_{X^{n}}\left[\sum_{Y_{11}^{n}: K^{*}}^{L^{*}} q\left(Y_{11}^{n} \mid X^{n}\right) \ln \frac{q\left(Y_{11}^{n} \mid X^{n}\right)}{p\left(Y_{11}^{n} \mid X^{n}\right)}\right]
$$

where the probability of $Y_{11}^{n}$ means that the nuisance dimensions $Y_{12}^{n}$ are marginalized out:

$$
\begin{aligned}
& q\left(Y_{11}^{n} \mid X^{n}\right)=\sum_{Y_{12}^{n}: K^{*}}^{L^{*}} q\left(Y^{n} \mid X^{n}\right) \\
& p\left(Y_{11}^{n} \mid X^{n}\right)=\sum_{Y_{12}^{n}: K^{*}}^{L^{*}} p\left(Y^{n} \mid X^{n}\right)
\end{aligned}
$$

and we use the following summation symbols:

$$
\begin{aligned}
& \sum_{Y_{11}^{n}: K^{*}}^{L^{*}}=\sum_{y_{11}=1}^{L^{*}} \cdots \sum_{y_{1 K_{t}}=1}^{L^{*}} \sum_{y_{21}=1}^{L^{*}} \cdots \sum_{y_{2 K_{t}}=1}^{L^{*}} \cdots \sum_{y_{n 1}=1}^{L^{*}} \cdots \sum_{y_{n K_{t}}=1}^{L^{*}} \\
& \sum_{Y_{12}^{n}: K^{*}}^{L^{*}}=\sum_{y_{1 K_{t}+1}=1}^{L^{*}} \cdots \sum_{y_{1 K^{*}}=1}^{L^{*}} \cdots \sum_{y_{n K_{t}+1}=1}^{L^{*}} \cdots \sum_{y_{n K^{*}}=1}^{L^{*}}
\end{aligned}
$$

We refer to $D_{n 2}(n)$ as the marginal type since the irrelevant dimensions are marginalized out. In the practical situations, the partial target dimensions are not often distinguishable from the irrelevant ones since the estimated labels have symmetry. The present paper considers the marginal type error to investigate the relation between the number of the target dimensions and the accuracy from the theoretical perspective. The label symmetry will be discussed in Section 6.2.

It is easy to prove the following lemma, which holds for any arbitrary number of data points $n$.

Lemma 1 The joint-type error is larger than the marginal-type error:

$$
D_{n 1}(n) \geq D_{n 2}(n)
$$

(Proof): Based on the log-sum inequality on $\sum_{Y_{12}^{n}: K^{*}}^{L^{*}}$, we immediately obtain that

$$
\begin{aligned}
D_{n 2}(n) & =\frac{1}{n} E_{X^{n}}\left[\sum_{Y_{11}^{n}: K^{*}}^{L^{*}} \# Y_{12}^{n}\left\{\sum_{Y_{12}^{n}: K^{*}}^{L^{*}} \frac{1}{\# Y_{12}^{n}} q\left(Y^{n} \mid X^{n}\right)\right\} \ln \frac{\sum_{Y_{12}^{n}: K^{*}}^{L^{*}} \frac{1}{\# Y_{12}^{n}} q\left(Y^{n} \mid X^{n}\right)}{\sum_{Y_{12}^{n}: K^{*}}^{L^{*}} \frac{1}{\# Y_{12}^{n}} p\left(Y^{n} \mid X^{n}\right)}\right] \\
& \leq \frac{1}{n} E_{X^{n}}\left[\sum_{Y_{11}^{n}: K^{*}}^{L^{*}} \# Y_{12}^{n} \sum_{Y_{12}^{n}: K^{*}}^{L^{*}} \frac{1}{\# Y_{12}^{n}} q\left(Y^{n} \mid X^{n}\right) \ln \frac{\frac{1}{\# Y_{12}^{n}} q\left(Y^{n} \mid X^{n}\right)}{\frac{1}{\# Y_{12}^{n}} p\left(Y^{n} \mid X^{n}\right)}\right] \\
& =D_{n 1}(n)
\end{aligned}
$$

where $\# Y_{12}^{n}=L^{*\left(K^{*}-K_{t}\right)}$. (End of Proof)
This lemma shows the relation between the estimation target and the accuracy: the lower the dimensions of the target, the smaller the error.

Example 2 Let us consider two different target dimensions $K_{t}=K_{A}$ and $K_{t}=K_{B}$, where $K_{A}<K_{B}$. Define the error functions $D_{n 2 A}(n)$ and $D_{n 2 B}(n)$ in the marginaltype manner for these two dimensions, respectively. Using the same way of the proof of Lemma 1, we can easily obtain the following relation,

$$
D_{n 2 A}(n)<D_{n 2 B}(n)
$$

# 3.2 Redundant Case 

We now consider the redundant case, i.e., $K>K^{*}$. The definition in Eq. (15) is not applicable to this case, since the domain spaces of $q\left(Y^{n} \mid X^{n}\right)$ and $p\left(Y^{n} \mid X^{n}\right)$ are different. In the expression for the latent variable, the true and estimated distributions are described by $q\left(Y_{1}^{n} \mid X^{n}\right)$ and $p\left(Y_{1}^{n}, Y_{2}^{n} \mid X^{n}\right)$, respectively. These notations clarify that the KL divergence of Eq. (15) is not well-defined in this case.

To measure the distribution on $Y_{1}^{n}$, we can define the following two error functions:

$$
\begin{aligned}
& D_{r 1}(n)=\frac{1}{n} E_{X^{n}}\left[\sum_{Y_{1}^{n}: K^{*}}^{L^{*}} q\left(Y_{1}^{n} \mid X^{n}\right) \ln \frac{q\left(Y_{1}^{n} \mid X^{n}\right)}{p\left(Y_{1}^{n}, Y_{2}^{n}=1 \mid X^{n}\right)}\right] \\
& D_{r 2}(n)=\frac{1}{n} E_{X^{n}}\left[\sum_{Y_{1}^{n}: K^{*}}^{L^{*}} q\left(Y_{1}^{n} \mid X^{n}\right) \ln \frac{q\left(Y_{1}^{n} \mid X^{n}\right)}{\sum_{Y_{2}^{n}: K-K^{*}}^{L} p\left(Y_{1}^{n}, Y_{2}^{n} \mid X^{n}\right)}\right]
\end{aligned}
$$

where $p\left(Y_{1}^{n}, Y_{2}^{n}=1 \mid X^{n}\right)$ means that all elements of $Y_{2}^{n}$ are unity. The first error, $D_{r 1}(n)$, can be regarded as a joint-type error when the values in $Y_{2}^{n}$ are fixed. The second is a marginal-type error; the target dimensionality is $Y_{1}^{n}$, and the nuisance dimensionality is $Y_{2}^{n}$.

These two errors use different definitions for the estimated distribution on $Y_{1}^{n}$. In the marginal-type error, the redundant dimensions $Y_{2}^{n}$ are marginalized out. This means that the error only evaluates the target dimensions $Y_{1}^{n}$, even if probabilities have been assigned in $Y_{2}^{n}$. In the joint-type error, the estimation is expected to construct the probabilities only on $Y_{1}^{n}$, even though the latent variable has redundant dimensions; the essential dimensions must be detected successfully, and the redundant ones must be assigned a fixed value that does not affect the result. In general, latent variables are equivalent to nought if their values are deterministically assigned. For simplicity, the definition selects $Y_{2}^{n}=1$ as an example. The jointtype error evaluates the effect that the redundant dimensions have on the estimation result.

From the above definitions, we have the following lemma, which holds for arbitrary $n$.

Lemma 3 The magnitudes of the errors are related as follows:

$$
D_{r 1}(n) \geq D_{r 2}(n)
$$

(Proof): We have

$$
\sum_{Y_{2}^{n}: K-K^{*}}^{L} p\left(Y_{1}^{n}, Y_{2}^{n} \mid X^{n}\right) \geq p\left(Y_{1}^{n}, Y_{2}^{n}=1 \mid X^{n}\right)
$$

which directly shows that $D_{r 1}(n) \geq D_{r 2}(n)$. (End of Proof)
When the target dimension is restricted to $Y_{11}^{n}$ in the similar way to $D_{n 2}(n)$, the nuisance dimensions consist of $Y_{12}^{n}$ and $Y_{2}^{n}$. The error function is thus of the marginal type and is given by

$$
D_{r 3}(n)=\frac{1}{n} E_{X^{n}}\left[\sum_{Y_{11}^{n}: K^{*}}^{L^{*}} q\left(Y_{11}^{n} \mid X^{n}\right) \ln \frac{q\left(Y_{11}^{n} \mid X^{n}\right)}{p\left(Y_{11}^{n} \mid X^{n}\right)}\right]
$$

where the marginal probabilities are defined by

$$
\begin{aligned}
& q\left(Y_{11}^{n} \mid X^{n}\right)=\sum_{Y_{12}^{n}: K^{*}}^{L^{*}} q\left(Y_{1}^{n} \mid X^{n}\right) \\
& p\left(Y_{11}^{n} \mid X^{n}\right)=\sum_{Y_{12}^{n}: K^{*}}^{L} \sum_{Y_{2}^{n}: K}^{L} p\left(Y_{1}^{n}, Y_{2}^{n} \mid X^{n}\right)
\end{aligned}
$$

By combining Lemmas 1 and 3, we obtain the following lemma.

Lemma 4 The magnitudes of the errors are related as follows:

$$
D_{r 1}(n) \geq D_{r 2}(n) \geq D_{r 3}(n)
$$

# 4 Asymptotic Analysis of the Error Functions 

In this section, we present the asymptotic forms of the error function for the nonredundant and the redundant cases. These results are based on an extension of the methods provided in $[17,18]$. In the following Sections 4.2 and 4.3, we assume $L=L^{*}$, which means that the range of the latent variables has no redundancy. Then, we show their extensions to the case $L>L^{*}$ in Section 4.4.

### 4.1 Free Energy Functions

We now introduce free energy functions, which play an important role in deriving the asymptotic form of the error functions. First, we define the following marginal likelihood functions:

$$
\begin{aligned}
Z\left(X^{n}\right) & =\int \prod_{i=1}^{n} p\left(x_{i} \mid w\right) \varphi(w ; \eta) d w \\
Z\left(X^{n}, Y^{n}\right) & =\int \prod_{i=1}^{n} p\left(x_{i}, y_{i} \mid w\right) \varphi(w ; \eta) d w \\
Z_{X Y_{11}}\left(X^{n}, Y_{11}^{n}\right) & =\int \prod_{i=1}^{n} p\left(x_{i}, y_{i}^{(11)} \mid w\right) \varphi(w ; \eta) d w \\
Z_{X Y_{1}}\left(X^{n}, Y_{1}^{n}\right) & =\int \prod_{i=1}^{n} \sum_{y_{i}^{(2)}=1}^{L} p\left(x_{i}, y_{i}^{(1)}, y_{i}^{(2)} \mid w\right) \varphi(w ; \eta) d w \\
Z_{X Y_{1} C}\left(X^{n}, Y_{1}^{n}\right) & =\int \prod_{i=1}^{n} p\left(x_{i}, y_{i}^{(1)}, y_{i}^{(2)}=1 \mid w\right) \varphi(w ; \eta) d w
\end{aligned}
$$

Note that $Z\left(X^{n}, Y^{n}\right)$ is used for only the non-redundant case, and $p\left(x_{i}, y_{i}^{(11)} \mid w\right)$ in $Z_{X Y_{11}}\left(X^{n}, Y_{11}^{n}\right)$ has two different definitions. It is defined as

$$
\begin{aligned}
& p\left(x, y_{i}^{(11)} \mid w\right)=\sum_{y_{i}^{(12)}=1}^{L} p\left(x, y_{i}^{(11)}, y_{i}^{(12)} \mid w\right) \\
& p\left(x, y_{i}^{(11)} \mid w\right)=\sum_{y_{i}^{(12)}=1}^{L} \sum_{y_{i}^{(2)}=1}^{L} p\left(x, y_{i}^{(11)}, y_{i}^{(12)}, y_{i}^{(2)} \mid w\right)
\end{aligned}
$$

in the non-redundant and the redundant case, respectively.
The negative log marginal likelihood is referred to as the free energy. We consider the following variants of functions of the average energy:

$$
\begin{aligned}
F_{X}(n) & =-n S_{X}-E_{X^{n}}\left[\ln Z\left(X^{n}\right)\right] \\
F_{X Y}(n) & =-n S_{X Y}-E_{X^{n}, Y_{1}^{n}}\left[\ln Z\left(X^{n}, Y^{n}\right)\right] \\
F_{X Y_{11}}(n) & =-n S_{X Y}-E_{X^{n}, Y_{1}^{n}}\left[\ln Z_{X Y_{11}}\left(X^{n}, Y_{11}^{n}\right)\right] \\
F_{X Y_{1}}(n) & =-n S_{X Y}-E_{X^{n} Y_{1}^{n}}\left[\ln Z_{X Y_{1}}\left(X^{n}, Y_{1}^{n}\right)\right] \\
F_{X Y_{1} C}(n) & =-n S_{X Y}-E_{X^{n} Y_{1}^{n}}\left[\ln Z_{X Y_{1} C}\left(X^{n}, Y_{1}^{n}\right)\right]
\end{aligned}
$$

where

$$
\begin{aligned}
S_{X} & =-\int q(x) \ln q(x) d x \\
S_{X Y} & =-\int \sum_{y=1}^{L^{*}} q(x, y) \ln q(x, y) d x
\end{aligned}
$$

and the expectation is defined as

$$
E_{X^{n} Y_{1}^{n}}\left[f\left(X^{n}, Y_{1}^{n}\right)\right]=\int \sum_{Y_{1}^{n}: K^{*}}^{L^{*}} q\left(X^{n}, Y_{1}^{n}\right) f\left(X^{n}, Y_{1}^{n}\right) d X^{n}
$$

It is easy to find the following relations between the error functions and the free energy functions:

$$
\begin{aligned}
D_{n 1}(n) & =\frac{1}{n}\left\{F_{X Y}(n)-F_{X}(n)\right\} \\
D_{n 2}(n) & =\frac{1}{n}\left\{F_{X Y_{11}}(n)-F_{X}(n)\right\} \\
D_{r 1}(n) & =\frac{1}{n}\left\{F_{X Y_{1} C}(n)-F_{X}(n)\right\} \\
D_{r 2}(n) & =\frac{1}{n}\left\{F_{X Y_{1}}(n)-F_{X}(n)\right\} \\
D_{r 3}(n) & =\frac{1}{n}\left\{F_{X Y_{11}}(n)-F_{X}(n)\right\}
\end{aligned}
$$

For example, the equation for $D_{n 1}(n)$ is derived as follows:

$$
\begin{aligned}
D_{n 1}(n) & =\frac{1}{n} E_{X^{n}}\left[\sum_{Y^{n}: K^{*}}^{L^{*}} q\left(Y^{n} \mid X^{n}\right) \ln \frac{q\left(X^{n}, Y^{n}\right)}{p\left(X^{n}, Y^{n}\right)}-\ln \frac{q\left(X^{n}\right)}{p\left(X^{n}\right)}\right] \\
& =\frac{1}{n}\left\{-n S_{X Y}-E_{X^{n} Y^{n}}\left[\ln Z\left(X^{n}, Y^{n}\right)\right]\right\}-\frac{1}{n}\left\{-n S_{X}-E_{X^{n}}\left[\ln Z\left(X^{n}\right)\right]\right\} \\
& =\frac{1}{n}\left\{F_{X Y}(n)-F_{X}(n)\right\}
\end{aligned}
$$

where $p\left(X^{n}, Y^{n}\right)$ and $p\left(X^{n}\right)$ correspond to $Z\left(X^{n}, Y^{n}\right)$ and $Z\left(X^{n}\right)$, respectively, and $q\left(X^{n}, Y^{n}\right)=q\left(Y^{n} \mid X^{n}\right) q\left(X^{n}\right)$.

Due to these relations, we will consider the asymptotic forms of the free energy functions in the following subsections.

# 4.2 Asymptotic Errors in the Non-Redundant Case 

According to the analysis in [17], the asymptotic free energy can be expressed in terms of the Fisher information matrix. Let us here define these matrices by defining their elements, as follows:

$$
\begin{aligned}
I_{X}(w) & =\left\{E_{x}\left[\frac{\partial}{\partial w_{i}} \ln p(x \mid w) \frac{\partial}{\partial w_{j}} \ln p(x \mid w)\right]\right\}_{i j} \\
I_{X Y}(w) & =\left\{E_{x y}\left[\frac{\partial}{\partial w_{i}} \ln p(x, y \mid w) \frac{\partial}{\partial w_{j}} \ln p(x, y \mid w)\right]\right\}_{i j} \\
I_{X Y_{11}}(w) & =\left\{E_{x y}\left[\frac{\partial}{\partial w_{i}} \ln p\left(x, y^{(11)} \mid w\right) \frac{\partial}{\partial w_{j}} \ln p\left(x, y^{(11)} \mid w\right)\right]\right\}_{i j}
\end{aligned}
$$

The expectations are defined as

$$
\begin{aligned}
E_{x}[f(x)] & =\int f(x) q(x) d x \\
E_{x y}[f(x, y)] & =\int \sum_{y} f(x, y) q(x, y) d x
\end{aligned}
$$

Using these matrices, we can describe the asymptotic forms of the free energy functions.

Lemma 5 Let $w_{X Y}^{*} \in W_{t}$ be the true parameter, where $p\left(x, y \mid w_{X Y}^{*}\right)=q(x, y)$. The free energy functions have the following asymptotic forms:

$$
\begin{aligned}
F_{X}(n) & =\frac{\operatorname{dim} w}{2} \ln \frac{n}{2 \pi e}+\ln \frac{\sqrt{\operatorname{det} I_{X}\left(w_{X Y}^{*}\right)}}{\varphi\left(w_{X Y}^{*} ; \eta\right)}+o(1) \\
F_{X Y}(n) & =\frac{\operatorname{dim} w}{2} \ln \frac{n}{2 \pi e}+\ln \frac{\sqrt{\operatorname{det} I_{X Y}\left(w_{X Y}^{*}\right)}}{\varphi\left(w_{X Y}^{*} ; \eta\right)}+o(1) \\
F_{X Y_{11}}(n) & =\frac{\operatorname{dim} w}{2} \ln \frac{n}{2 \pi e}+\ln \frac{\sqrt{\operatorname{det} I_{X Y_{11}}\left(w_{X Y}^{*}\right)}}{\varphi\left(w_{X Y}^{*} ; \eta\right)}+o(1)
\end{aligned}
$$

Based on the relations given in Eqs. (51) and (52), we obtain the following theorem.

Theorem 6 The error functions in the non-redundant case have the following asymptotic forms:

$$
\begin{gathered}
D_{n 1}(n)=\frac{1}{2 n} \ln \operatorname{det} I_{X Y}\left(w_{X Y}^{*}\right) I_{X}\left(w_{X Y}^{*}\right)^{-1}+o\left(\frac{1}{n}\right) \\
D_{n 2}(n)=\frac{1}{2 n} \ln \operatorname{det} I_{X Y_{11}}\left(w_{X Y}^{*}\right) I_{X}\left(w_{X Y}^{*}\right)^{-1}+o\left(\frac{1}{n}\right)
\end{gathered}
$$

This theorem shows that the leading term has the order $1 / n$, and its coefficient depends on the true parameter $w_{X Y}^{*}$. Let us look at $D_{n 1}(n)$ in order to evaluate how the true parameter affects this coefficient. This coefficient can be rewritten as

$$
\ln \operatorname{det} I_{X}\left(w_{X Y}^{*}\right)^{-1}-\ln \operatorname{det} I_{X Y}\left(w_{X Y}^{*}\right)^{-1}
$$

Since the inverse Fisher information matrix corresponds to the variance of the unbiased estimator, this coefficient shows the difference between the variance of the estimator based on the incomplete dataset $X^{n}$ and that based on the complete dataset $\left(X^{n}, Y^{n}\right)$. This is regarded as the gain in information when we obtain the latent variable $Y^{n}$. For example, when the clustering is difficult, i.e., when the clusters are close together, a partially given label $y$ considerably improves the result. In this case, the difference between the variances will be large and so will the error. The location of the true parameter $w_{X Y}^{*}$ determines the degree of difficulty of the clustering task, and the coefficient of the error reflects this difficulty through the variances of the unbiased estimators.

Lemma 1 stated the relation between the magnitudes of the error functions. According to Theorem 6, the difference between the errors is revealed in detail in the asymptotic situation.

Corollary 7 The asymptotic difference between $D_{n 1}(n)$ and $D_{n 2}(n)$ is

$$
D_{n 1}(n)-D_{n 2}(n)=\frac{1}{2 n} \ln \operatorname{det} I_{X Y}\left(w_{X Y}^{*}\right) I_{X Y_{11}}\left(w_{X Y}^{*}\right)^{-1}+o\left(\frac{1}{n}\right)
$$

Because $I_{X Y}\left(w_{X Y}^{*}\right) I_{X Y_{11}}\left(w_{X Y}^{*}\right)^{-1}$ is not the unit matrix, the coefficient of the leading term is positive; thus, this difference is of the order of $1 / n$.

# 4.3 Asymptotic Errors in the Redundant Case 

In the redundant case, it is known that the Fisher information matrix is not positive definite, and the asymptotic form of the free energy is not described by that matrix. The parameter space includes singularities, but there is an analysis method based on algebraic geometry that is able to deal effectively with singularities [13, 14, 18].

Let us first define some functions:

$$
\begin{aligned}
H_{X}(w) & =\int q(x) \ln \frac{q(x)}{p(x \mid w)} d x \\
H_{X Y_{11}}(w) & =\int \sum_{y^{(1)}: K_{t}}^{L^{*}} q\left(x, y^{(11)}\right) \ln \frac{q\left(x, y^{(11)}\right)}{\sum_{y^{(12)}=1}^{L} \sum_{y^{(2)}=1}^{L} p\left(x, y^{(11)}, y^{(12)}, y^{(2)}\right)} d x \\
H_{X Y_{1}}(w) & =\int \sum_{y^{(1)}: K^{*}}^{L^{*}} q\left(x, y^{(1)}\right) \ln \frac{q\left(x, y^{(1)}\right)}{\sum_{y^{(2)}=1}^{L} p\left(x, y^{(1)}, y^{(2)} \mid w\right)} d x \\
H_{X Y_{1} C}(w) & =\int \sum_{y^{(1)}: K^{*}}^{L^{*}} q\left(x, y^{(1)}\right) \ln \frac{q\left(x, y^{(1)}\right)}{p\left(x, y^{(1)}, y^{(2)}=1\right)} d x
\end{aligned}
$$

Instead of the Fisher information matrix, the following zeta function plays an important role in expressing the asymptotic form of the error in the redundant case:

$$
\zeta_{A}(z)=\int H_{A}(w)^{z} \varphi(w ; \eta) d w
$$

where $z$ is a one-dimensional complex variable, and the symbol $A$ is replaced by $X, X Y_{11}, X Y_{1}$, or $X Y_{1} C$. When $H_{A}(w)$ is an analytic function, the poles of the zeta function are all real, negative, and rational. Let the largest pole and the order of the corresponding zeta function be $z=-\lambda_{A}$ and $m_{A}$, respectively; the zeta function is

$$
\zeta_{A}(z)=\frac{f_{c}(z)}{\left(z+\lambda_{A}\right)^{m_{A}}}+\ldots
$$

where $f_{c}$ is holomorphic and does not have a factor $\left(z+\lambda_{A}\right)$. Using this information about the pole, we can obtain the asymptotic form of the free energy function.

Lemma 8 (Corollary 6.1 in [14]) Let $H_{A}(w)$ be an analytic function, and let $\varphi(w ; \eta)$ be analytic in its support. Then, the free energy function has the asymptotic form

$$
F_{A}(n)=\lambda_{A} \ln n-\left(m_{A}-1\right) \ln \ln n+O(1)
$$

We can then obtain the asymptotic errors from the relations given in Eqs. (53), (54), and (55).

Theorem 9 If $W_{t} \neq \emptyset$ and the conditions of Lemma 8 are satisfied, the errors have the following asymptotic form:

$$
\begin{aligned}
& D_{r 1}(n)=\left(\lambda_{X Y_{1} C}-\lambda_{X}\right) \frac{\ln n}{n}-\left(m_{X Y_{1} C}-m_{X}\right) \frac{\ln \ln n}{n}+o\left(\frac{\ln \ln n}{n}\right) \\
& D_{r 2}(n)=\left(\lambda_{X Y_{1}}-\lambda_{X}\right) \frac{\ln n}{n}-\left(m_{X Y_{1}}-m_{X}\right) \frac{\ln \ln n}{n}+o\left(\frac{\ln \ln n}{n}\right) \\
& D_{r 3}(n)=\left(\lambda_{X Y_{11}}-\lambda_{X}\right) \frac{\ln n}{n}-\left(m_{X Y_{11}}-m_{X}\right) \frac{\ln \ln n}{n}+o\left(\frac{\ln \ln n}{n}\right)
\end{aligned}
$$

The following lemma guarantees that the largest order of any of these errors is $\ln n / n$.

Lemma 10 In the asymptotic forms of Theorem 9, the coefficients of the leading terms on the right-hand side are all positive.

The errors in the redundant case are much larger than those in the non-redundant case. Since this lemma is not directly derived from the asymptotic forms of the free energy functions, we will show the proof.
(Proof of Lemma 10): The magnitude relation $H_{1}(w) \leq H_{2}(w)$ ensures that $\lambda_{1} \leq \lambda_{2}$, where $z=-\lambda_{1}$ and $z=-\lambda_{2}$ are the largest poles of $\int H_{1}(w)^{z} \varphi(w) d w$ and $\int H_{2}(w)^{z} \varphi(w) d w$, respectively $[13,21,19,14]$.

Based on the log-sum inequality, we easily obtain

$$
\begin{aligned}
H_{X Y_{1} C}(w) & >H_{X}(w) \\
H_{X Y_{1}}(w) & >H_{X}(w) \\
H_{X Y_{11}}(w) & >H_{X}(w)
\end{aligned}
$$

For example,

$$
\begin{aligned}
H_{X Y_{1} C}(w) & =\int \sum_{y^{(1)}: K^{*}}^{L^{*}} q\left(x, y^{(1)}\right) \ln \frac{q\left(x, y^{(1)}\right)}{p\left(x, y^{(1)}, y^{(2)}=1 \mid w\right)} d x \\
& \geq \int q(x) \ln \frac{q(x)}{p\left(x, y^{(2)}=1 \mid w\right)} d x \\
& >\int q(x) \ln \frac{q(x)}{p(x \mid w)} d x=H_{X}(w)
\end{aligned}
$$

Therefore, $\lambda_{X Y_{1} C}>\lambda_{X}, \lambda_{X Y_{1}}>\lambda_{X}$, and $\lambda_{X Y_{11}}>\lambda_{X}$, which shows that the coefficients are positive. (End of Proof)

The differences between the errors can be derived directly.

Corollary 11 The asymptotic difference between $D_{r 1}(n)$ and $D_{r 2}(n)$ can be expressed as

$$
\begin{aligned}
D_{r 1}(n)-D_{r 2}(n)= & \left(\lambda_{X Y_{1} C}-\lambda_{X Y_{1}}\right) \frac{\ln n}{n} \\
& -\left(m_{X Y_{1} C}-m_{X Y_{1}}\right) \frac{\ln \ln n}{n}+o\left(\frac{\ln \ln n}{n}\right)
\end{aligned}
$$

and the one between $D_{r 2}(n)$ and $D_{r 3}(n)$ can be expressed as

$$
\begin{aligned}
D_{r 2}(n)-D_{r 3}(n)= & \left(\lambda_{X Y_{1}}-\lambda_{X Y_{11}}\right) \frac{\ln n}{n} \\
& -\left(m_{X Y_{1}}-m_{X Y_{11}}\right) \frac{\ln \ln n}{n}+o\left(\frac{\ln \ln n}{n}\right)
\end{aligned}
$$

# 4.4 Extension to $L>L^{*}$ 

In this subsection, the extension to the case $L>L^{*}$ is introduced in both nonredundant and redundant cases. The non-redundant case, where $K=K^{*}$ and $L>L^{*}$, corresponds to the one-dimensional latent variable in each dimension. As stated in [18], the redundancy of the range of variable causes singularities of the parameter space even in the non-redundant case. According to this study, the following lemma holds,
Corollary 12 The error functions in the non-redundant case have the following asymptotic forms;

$$
\begin{aligned}
& D_{n 1}(n)=\left(\lambda_{X Y}-\lambda_{X}\right) \frac{\ln n}{n}-\left(m_{X Y}-m_{X}\right) \frac{\ln \ln n}{n}+o\left(\frac{\ln \ln n}{n}\right) \\
& D_{n 2}(n)=\left(\lambda_{X Y_{11}}-\lambda_{X}\right) \frac{\ln n}{n}-\left(m_{X Y_{11}}-m_{X}\right) \frac{\ln \ln n}{n}+o\left(\frac{\ln \ln n}{n}\right)
\end{aligned}
$$

Note that the coefficients $\lambda_{X}$ and $\lambda_{X Y_{11}}$ are different from the ones in Theorem 9, since $H_{X}(w)$ and $H_{X Y_{11}}(w)$ depend on the relation between $L$ and $L^{*}$. Corollary 12 can be extended to the case, where $K=K^{*}$ and at least one of the ranges $L_{1}, \ldots, L_{K^{*}}$ is larger than the true range. More precisely, the corollary still holds when there exists $1 \leq i \leq K^{*}$ such that $L_{i}>L_{i}^{*}$.

In redundant case, all results in Section 4.3 still hold; the asymptotic form based on $\lambda_{A}$ does not change though the function $H_{A}(w)$ such as Eqs. (70), and (71) and the value of $\lambda_{A}$ will change due to the extension. Even in the case, where $L_{1}^{*}, \ldots, L_{K^{*}}^{*}$ are different and at least one of them has redundancy such as $L_{i}>L_{i}^{*}$, Lemma 8 still holds. Therefore, the asymptotic form of the error functions in Theorem 9, the analysis of the largest order in Lemma 10, and the asymptotic differences between the error functions in Corollary 11 are available even in the more general cases on L.

![img-1.jpeg](img-1.jpeg)

Figure 2: Structure of a two-layered Bayesian network.

# 5 Errors in Two-Layered Bayesian Networks 

In the non-redundant case, we can interpret the asymptotic forms of the errors, since the Fisher information matrices indicate the variance of the estimators. However, in the redundant case, it is not straightforward to understand the meaning of the coefficients of the errors. In this section, we provide a demonstration of a method for calculating the error in a Bayesian network, and we ascertain the main factor determining $\lambda_{A}$. For simplicity, we focus on the errors $D_{r 1}(n)$ and $D_{r 2}(n)$, individually and in comparison.

### 5.1 Model Settings

Let the learning model be the two-layered Bayesian network in which all the observable and hidden nodes are binary. The model structure is shown in Fig. 2. There are $M$ observable nodes directly affected by $K$ hidden ones. Data are expressed as $x \in\{0,1\}^{M}$, and the corresponding latent variables are $y \in\{0,1\}^{K}$. Assume that $n$ data points are obtained. The $i$ th data point and the latent variables are given by $x_{i}=\left(x_{i 1}, \ldots, x_{i M}\right)$ and $y_{i}=\left(y_{i 1}, \ldots, y_{i K}\right)$, respectively. The model is formulated as

$$
\begin{aligned}
p\left(x_{i} \mid w\right) & =\sum_{y_{i 1}=0,1} \cdots \sum_{y_{i K}=0,1} \prod_{k=1}^{K} g\left(y_{i k}, a_{k}\right) \prod_{m=1}^{M} g\left(x_{i m}, b_{y_{i} m}\right) \\
g(j, p) & =p^{1-j}(1-p)^{j}
\end{aligned}
$$

where $j \in\{0,1\}$ and $0 \leq p \leq 1$. The parameter $w$ consists of $a_{k}$ and $b_{y_{i} m}$. The dimension is $\operatorname{dim} w=K+2^{K} M$.

Let the prior be the product of the beta distributions:

$$
\varphi(w ; \eta)=\prod_{k=1}^{K} \mathrm{~B}\left(a_{k} ; \eta_{1}\right) \prod_{y_{i 1}=0,1} \cdots \prod_{y_{i K}=0,1} \prod_{m=1}^{M} \mathrm{~B}\left(b_{y_{i} m} ; \eta_{2}\right)
$$

where $\mathrm{B}\left(\cdot ; \eta_{i}\right)$ for $i=1,2$ is the symmetric beta function, and $\eta=\left(\eta_{1}, \eta_{2}\right)$ is the hyperparameter.

Let the true model be a two-layered Bayesian network with $K^{*}$ hidden nodes. The model has constant parameters $0<a_{k}^{*}<1$ for $1 \leq k \leq K^{*}$ and $0<b_{y_{i} m}^{*}<1$ for $y_{i} \in\{0,1\}^{K^{*}}$.

# 5.2 Asymptotic Errors 

In the two-layered Bayesian networks, the errors of the latent variable estimation have the following behavior.

Theorem 13 In a two-layered Bayesian network, the errors have the following upper bound:

$$
\begin{aligned}
& D_{r 1}(n)<\left(K-K^{*}\right) \eta_{1} \frac{\ln n}{n}+o\left(\frac{\ln n}{n}\right) \\
& D_{r 2}(n)<\min \left\{\frac{\left(K-K^{*}\right) \eta_{1}}{2}, 2^{K-K^{*}-1} M\right\} \frac{\ln n}{n}+o\left(\frac{\ln n}{n}\right)
\end{aligned}
$$

Moreover, the difference has the lower bound

$$
D_{r 1}(n)-D_{r 2}(n)>\min \left\{\frac{\left(K-K^{*}\right) \eta_{1}}{2}, 2^{K-K^{*}-1} M\right\} \frac{\ln n}{n}+o\left(\frac{\ln n}{n}\right)
$$

In both Eqs. (89) and (90), the coefficients of the bounds change at

$$
\eta_{1}=\frac{2^{K-K^{*}} M}{K-K^{*}}
$$

From Eq. 90, we immediately obtain the lower bound on $D_{r 1}(n)$ :

$$
D_{r 1}(n)>\min \left\{\frac{\left(K-K^{*}\right) \eta_{1}}{2}, 2^{K-K^{*}-1} M\right\} \frac{\ln n}{n}+o\left(\frac{\ln n}{n}\right)
$$

Let us consider the case in which $\eta_{1}$ is smaller than $\frac{2^{K-K^{*}} M}{K-K^{*}}$. Combining the lower and the upper bound, we find that

$$
\frac{\left(K-K^{*}\right) \eta_{1}}{2} \frac{\ln n}{n}+o\left(\frac{\ln n}{n}\right)<D_{r 1}(n)<\left(K-K^{*}\right) \eta_{1} \frac{\ln n}{n}+o\left(\frac{\ln n}{n}\right)
$$

which holds for arbitrary $M$. This relation indicates that the error $D_{r 1}(n)$ is essentially determined by the factor $K-K^{*}$, which is the redundancy of the latent variable in the model.

# 5.3 Proof of Theorem 13 

Based on the relations to the free energy function, we will show the following lemma and then prove Theorem 13.

Lemma 14 The free energy functions have the following asymptotic bounds:

$$
\begin{aligned}
F_{X}(n) & >\frac{K^{*}+2^{K^{*}} M}{2} \ln n+o(\ln n) \\
F_{X Y_{1} C}(n) & =\left\{\frac{K^{*}+2^{K^{*}} M}{2}+\left(K-K^{*}\right) \eta_{1}\right\} \ln n+o(\ln n) \\
F_{X Y_{1}}(n) & \leq \frac{K^{*}+2^{K^{*}} M+\min \left\{\left(K-K^{*}\right) \eta_{1}, 2^{K-K^{*}} M\right\}}{2} \ln n+o(\ln n)
\end{aligned}
$$

(Proof of Lemma 14): Since $F_{X}(n)$ is the free energy with respect to the probability of the observable variable $p(x \mid w)$, its asymptotic properties have been clarified thoroughly (cf. $[12,13,14]$ ). It is known that the coefficient $2 \lambda_{X}$ requires a value other than the number of dimensions of the true constant parameters. In our case, the true model has a constant parameter consisting of $a_{k}^{*}$ and $b_{y_{i} m}^{*}$, where $1 \leq k \leq K^{*}$ and $y_{i} \in\left\{1, \ldots, 2^{K^{*}}\right\}$. Then, we have

$$
\lambda_{X}>\frac{K^{*}+2^{K^{*}} M}{2}
$$

where $2^{K^{*}} M$ is the number of dimensions of the parameter in the true model. Thus, we have derived the lower bound on $F_{X}(n)$.

Next, we consider $\zeta_{X Y_{1} C}(z)$ for $F_{X Y_{1} C}(n)$. We need to calculate the integral of the zeta function to obtain the pole. The calculation is easy if $H_{A}(w)$ is in product form:

$$
\zeta_{A}(z)=\int \prod_{i} w_{i}^{\alpha z} \varphi(w ; \eta) d w
$$

Assuming that the prior is described by $\prod_{i} w_{i}^{\beta_{i}}$, then we have the poles $z=-(\beta_{i}+$ 1) $/ \alpha_{i}$, because

$$
\int w_{i}^{\alpha_{i} z} w_{i}^{\beta_{i}} d w_{i}=\frac{1}{\alpha_{i} z+\beta_{i}+1}
$$

However, $H_{A}(w)$ is usually in polynomial form. One way to resolve the singularities is to use a procedure that finds a mapping that transforms $H_{A}(w)$ into the product form $[5,13]$. This mapping is referred to as a blow-up, and it can be used to obtain the largest pole.

The function $H_{X Y_{1} C}(w)$ can be rewritten as

$$
\begin{aligned}
H_{X Y_{1} C}(w) & =H_{11}(w)+H_{12}(w) \\
H_{11}(w) & =\sum_{k=1}^{K^{*}} \sum_{j=0,1} g\left(j, a_{k}^{*}\right) \ln \frac{g\left(j, a_{k}^{*}\right)}{g\left(j, a_{k}\right)} \\
& +\sum_{y^{(1)}: K^{*}} \sum_{m=1}^{M} \sum_{x} g\left(x_{\cdot m}, b_{y^{(1)} m}^{*}\right) \ln \frac{g\left(x_{\cdot m}, b_{y^{(1)} m}^{*}\right)}{g\left(x_{\cdot m}, b_{y^{(1)} 1 \ldots 1 m}\right)} \\
H_{12}(w) & =-\sum_{k=K^{*}+1}^{K} \ln \left(1-a_{k}\right)
\end{aligned}
$$

The magnitude relation $\lambda_{1} \leq \lambda_{2}$ holds for $H_{1}(w) \leq H_{2}(w)$, where $z=-\lambda_{1}$ and $z=-\lambda_{2}$ are the largest poles of $\int H_{1}(w)^{z} \varphi(w) d w$ and $\int H_{2}(w)^{z} \varphi(w) d w$, respectively (cf. the proof of Lemma 10). Moreover, $\lambda_{1}=\lambda_{2}$ when there are positive constants $c_{1}$ and $c_{2}$ such that $c_{1} H_{1}(w) \leq H_{2}(w) \leq c_{2} H_{1}(w)$. In this sense, we use the equivalence relation $H_{1}(w) \equiv H_{2}(w)$.

Thus we have

$$
H_{X Y_{1} C}(w) \equiv \sum_{k=1}^{K^{*}}\left(a_{k}-a_{k}^{*}\right)^{2}+\sum_{y^{(1)}: K^{*}} \sum_{m=1}^{M}\left(b_{y^{(1)} 1 \ldots 1 m}-b_{y^{(1)} m}^{*}\right)^{2}+\sum_{k=K^{*}+1}^{K} a_{k}
$$

We will denote the right-hand side as $H_{13}(w)$. We define the blow-up $\Psi_{1}: \bar{w}=$ $(u, v) \rightarrow w$ as follows:

$$
\begin{aligned}
u_{1} & =a_{1}-a_{1}^{*} \\
u_{k} u_{1} & =a_{k}-a_{k}^{*} \quad\left(1<k \leq K^{*}\right) \\
u_{k} u_{1}^{2} & =a_{k}\left(K^{*}<k \leq K\right) \\
v_{y^{(1)} 1 \ldots 1 m} u_{1} & =b_{y^{(1)} 1 \ldots 1 m}-b_{y^{(1)} m}^{*}
\end{aligned}
$$

We focus on the factor $u_{1}$ in the zeta function

$$
\int H_{13}\left(\Psi_{1}(\bar{w})\right)^{z} \varphi\left(\Psi_{1}(\bar{w}) ; \eta\right)\left|\Psi_{1}\right| d \bar{w}
$$

where $\left|\Psi_{1}\right|$ is a Jacobian. Consider the exponential part of $u_{1}$. In the factor $H_{13}\left(\Psi_{1}(\bar{w})\right)^{z}$ and $K^{*}+2^{K^{*}} M+2\left(K-K^{*}\right) \eta_{1}-1$ in the beta prior $\varphi\left(\Psi_{1}(\bar{w}) ; \eta\right)$, we have $2 z$, which results in the pole

$$
z=-\frac{K^{*}+2^{K^{*}} M}{2}-\left(K-K^{*}\right) \eta_{1}
$$

Even if we focus on different factors $u_{i}$ for $i=2, \ldots, K^{*}$, we will obtain the same pole; this is due to the symmetry of $a_{2}, \ldots, a_{K^{*}}$. Thus, this is the largest pole among the transformed coordinates of $w$. According to the equivalence relation, the pole has the value $-\lambda_{X Y_{1} C}$.

For the bounds on $F_{X Y_{1}}(n)$, we analyze $H_{X Y_{1}}(w)$. According to [19, 14], this is equivalent to the squared-error form for discrete models. Applying this property to our model, we obtain

$$
H_{X Y_{1}}(w) \equiv \sum_{x} \sum_{y^{(1)}}\left(\sum_{y^{(2)}} p\left(x, y^{(1)}, y^{(2)}\right)-q\left(x, y^{(1)}\right)\right\}^{2}
$$

Let us define the blow-up $\Psi_{2}: \bar{w} \rightarrow w$ such that

$$
\begin{aligned}
u_{1} & =a_{1}-a_{1}^{*} \\
u_{k} u_{1} & =a_{k}-a_{k}^{*} \quad\left(1<k \leq K^{*}\right) \\
u_{k} u_{1} & =a_{k}\left(K^{*}<k \leq K\right) \\
v_{y^{(1)} 1 \ldots 1 m} u_{1} & =b_{y^{(1)} 1 \ldots 1 m}-b_{y^{(1)} m}^{*}
\end{aligned}
$$

Then, there is a positive constant $c_{3}$ such that

$$
H_{X Y_{1}}\left(\Psi_{2}(\bar{w})\right) \leq c_{3} u_{1}^{2}
$$

in the support of $\varphi\left(\Psi_{2}(\bar{w}) ; \eta\right)$. In the zeta function

$$
\int u_{1}^{2 z} \varphi\left(\Psi_{2}(\bar{w}) ; \eta\right)\left|\Psi_{2}\right| d \bar{w}
$$

$u_{1}$ has the exponential part $2 z+K^{*}+2^{K^{*}} M+\left(K-K^{*}\right) \eta_{1}-1$, which results in the pole $z=-\mu_{1}=-\left(K^{*}+2^{K^{*}} M+\left(K-K^{*}\right) \eta_{1}\right) / 2$.

Let us define the blow-up $\Psi_{3}: \bar{w} \rightarrow w$ such that

$$
\begin{aligned}
u_{1} & =a_{1}-a_{1}^{*} \\
u_{k} u_{1} & =a_{k}-a_{k}^{*} \quad\left(1<k \leq K^{*}\right) \\
v_{y^{(1)} y^{(2)} m} u_{1} & =b_{y^{(1)} y^{(2)} m}-b_{y^{(1)} m}^{*}
\end{aligned}
$$

Then there is a positive constant $c_{4}$ such that

$$
H_{X Y_{1}}\left(\Psi_{3}(\bar{w})\right) \leq c_{4} u_{1}^{2}
$$

in the support of $\varphi\left(\Psi_{3}(\bar{w}) ; \eta\right)$. In the zeta function

$$
\int u_{1}^{2 z} \varphi\left(\Psi_{3}(\bar{w}) ; \eta\right)\left|\Psi_{3}\right| d \bar{w}
$$

$u_{1}$ has the exponential part $2 z+K^{*}+2^{K^{*}} M+2^{K-K^{*}} M-1$, which results in the pole $z=-\mu_{2}=-\left(K^{*}+2^{K^{*}} M+2^{K-K^{*}} M\right) / 2$.

Then, it holds that $\lambda_{X Y_{1}} \leq \min \left\{\mu_{1}, \mu_{2}\right\}$, which proves the upper bound on $F_{X Y_{1}}(n)$. (End of Proof)
(Proof of Theorem 13): Using Eqs. (53) and (54), the asymptotic bounds in Lemma 14 immediately show the bounds on $D_{r 1}(n)$ and $D_{r 2}(n)$. Their difference is written as

$$
D_{r 1}(n)-D_{r 2}(n)=\frac{1}{n}\left\{F_{X Y_{1} C}(n)-F_{X Y_{1}}(n)\right\}
$$

and its lower bound is also derived from the asymptotic properties of the free energy functions. (End of Proof)

# 6 Discussion 

In this section, we first explain the phase and its transition in the free energy function, which indicates how the redundant dimensions of the latent variable are used and affects the accuracy of the estimation. Then, we discuss the symmetry of dimension in the latent variable.

### 6.1 Phase Transition and Its Effect on the Estimation

Here, we introduce the phase transition of the free energy function and discuss parameter subspaces used to determine the phases. The relation between the phases and the subspaces provides an interpretation of the coefficient of the dominant term in the energy function.

Previous studies, such as [20], have shown that at some points, there is a change in the shape of the free energy function with respect to the hyperparameter. This change is referred to as a phase transition, and the point at which the change occurs is the phase transition point. For example, in Lemma 14, the bound on $F_{X Y_{1}}(n)$ has two phases:

$$
\begin{aligned}
\frac{K^{*}+2^{K^{*}} M+\left(K-K^{*}\right) \eta_{1}}{2} \ln n+o(\ln n) & \left(\eta_{1}<\eta_{t}\right) \\
\frac{K^{*}+2^{K^{*}} M+2^{K-K^{*}} M}{2} \ln n+o(\ln n) & \left(\eta_{1} \geq \eta_{t}\right)
\end{aligned}
$$

and the transition point is

$$
\eta_{t}=\frac{2^{K-K^{*}} M}{K-K^{*}}
$$

The difference between the coefficients in Eqs. (123) and those in (124) is based on the blow-up mappings $\Psi_{2}(\bar{w})$ and $\Psi_{3}(\bar{w})$ in the proof of Lemma 14 defined by Eqs. (111)-(114) and (117)-(119), respectively. These mappings show the subspaces of the parameter space, which provide dominant values in the calculation of the integral of the zeta function $\zeta_{X Y_{1}}(z)$ and determine the locations of the poles. In the redundant case, the true parameter $w_{X Y}^{*}$ is expressed as not an isolated point but a solution set of some equations such as Eqs. (111)-(114).

Since the subspace generally appears in the analysis of the hierarchical models and it is not straightforward to elucidate its complicated structure, let us consider a simple case, where the model is the two-layered Bayesian network shown in Fig. 1, and the true distribution has a one-dimensional latent variable; thus, we have $K^{*}=1$ and $K=2$. The model and the true distribution are given by

$$
\begin{aligned}
p(x \mid w) & =\sum_{y_{1}=0,1} \sum_{y_{2}=0,1} a_{1 y_{1}} a_{2 y_{2}} \prod_{m=1}^{M} b_{y_{1} y_{2} m}^{\left(1-x_{m}\right)}\left(1-b_{y_{1} y_{2} m}\right)^{x_{m}} \\
q(x) & =\sum_{y_{1}=0,1} a_{1 y_{1}}^{*} \prod_{m=1}^{M} b_{y_{1} m}^{*\left(1-x_{m}\right)}\left(1-b_{y_{1} m}^{*}\right)^{x_{m}}
\end{aligned}
$$

where Eq. (126) is the same expression as Eq. (5). The necessary and redundant dimensions are expressed as $Y_{1}=\left\{y_{1}\right\}$ and $Y_{2}=\left\{y_{2}\right\}$, respectively. The distribution of the estimation is given by

$$
p\left(Y_{1} \mid X^{n}\right)=\sum_{y_{2}=0,1} p\left(Y_{1}, Y_{2} \mid X^{n}\right)
$$

We can find at least two ways to express the true distribution while satisfying $p\left(Y_{1} \mid X^{n}\right)=q\left(Y_{1} \mid X^{n}\right)$ :
(P1) $a_{20}=0$,
(P2) $b_{y_{1} y_{2} m}=b_{y_{1} m}^{*}$ for any $y_{2}$.
The first way (P1) directly eliminates the effect of $y_{2}$, since $y_{2}$ is always unity, and the actual latent variable is reduced to $y_{1}$ in Eq. (126). The conditional probability tables (CPTs) are presented in Fig. 3. We refer to this as the eliminating way. In the CPT of $x_{m}, \mathrm{FV}$ indicates a free variable. For example, in the first row of the CPT, $p\left(x_{m}=0 \mid y_{1}=0, y_{2}=0, w\right)=b_{00 m}$ is an FV and may take any value in the range $[0,1] ; p\left(x_{m}=1 \mid y_{1}=0, y_{2}=0, w\right)=1-b_{00 m}$ is omitted from the CPT.

The second way (P2) determines the value of $p\left(x \mid y_{1}, y_{2}, w\right)$, which depends only on $y_{1}$. The CPTs are shown in Fig. 4. We refer to this as the replicating way, since the rows in the CPT of $x_{m}$ are replicated so that we can ignore the value of $y_{2}$. Naturally, $p\left(y_{2}=0 \mid w\right)=a_{20}$ is the free variable.




Figure 3: Parameter of (P1): the CPT of the nodes $y_{1}$ and $y_{2}$ (left panel) and the CPT of the node $x_{m}$ (right panel); FV indicates a free variable.




Figure 4: Parameter of (P2): the CPT of the nodes $y_{1}$ and $y_{2}$ (left panel) and the CPT of the node $x_{m}$ (right panel); FV indicates a free variable.

Let us describe the subspaces for (P1) and (P2). According to the CPTs, the eliminating way can be expressed as

$$
\begin{aligned}
a_{10} & =a_{10}^{*} \\
a_{20} & =0 \\
b_{y_{1} 1 m} & =b_{y_{1} m}^{*}
\end{aligned}
$$

which corresponds to the subspace defined by the blow-up $\Psi_{2}$ in Section 5.3. The replicating way can be expressed as

$$
\begin{aligned}
a_{10} & =a_{10}^{*} \\
b_{y_{1} y_{2} m} & =b_{y_{1} m}^{*}
\end{aligned}
$$

which corresponds to the subspace defined by $\Psi_{3}$. Based on the proof of Lemma 14, $\Psi_{2}$ and $\Psi_{3}$ provide the poles of the zeta function, and the coefficients in Eqs. (123) and (124) are then derived. Therefore, the first phase, represented by Eq. (123), implies that the eliminating way can be used to express the true distribution, while the second phase, represented by Eq. (124), implies the replicating way can be used.

On the other hand, there is no transition point in $F_{X Y_{1} C}(n)$. Its definition includes the factor $p\left(x_{i}, y_{i}^{(1)}, y_{i}^{(2)}=1 \mid w\right)$, where the redundant dimension must have a fixed value, and the other values of $y_{i}^{(2)}$ do not have any effect on the observation $x_{i}$. Then, the probabilities for $y_{i}^{(2)} \neq 1$ must be zero, which corresponds to (P1). This is why only the eliminating way can be used to express the true distribution, and $F_{X Y_{1} C}(n)$ does not have different phases.

Now we discuss the effect of the phase transition on the estimation of the latent variable. According to Theorem 13, the bound of the error $D_{r 2}(n)$ depends on the phase;

$$
\begin{aligned}
& D_{r 2}(n)<\frac{\left(K-K^{*}\right) \eta_{1}}{2} \frac{\ln n}{n}+o\left(\frac{\ln n}{n}\right) \quad\left(\eta_{1}<\eta_{t}\right) \\
& D_{r 2}(n)<\frac{2^{K-K^{*}} M}{2} \frac{\ln n}{n}+o\left(\frac{\ln n}{n}\right) \quad\left(\eta_{1} \geq \eta_{t}\right)
\end{aligned}
$$

Considering the way to express the true distribution, we find that the upper expression is derived from the eliminating way while the lower one is from the replicating way. Therefore, (P2) makes the error smaller than (P1) in $\eta_{1} \geq \eta_{t}$, that is, to minimize the error requires not only to express the true distribution but also how to express it according to the value of the hyperparameter.

# 6.2 Symmetry of Latent Variable 

In this subsection, we consider the symmetry of the latent variable and its effect on the accuracy. As mentioned in the previous study, the label values have symmetry [18]. For example, the labels of the Gaussian mixture model in Eq.(3) are determined by the locations of the components and swapping the components essentially shows the same clustering result; the label probabilities of $w=\left\{a_{1}^{*}, b_{1}^{*}, b_{2}^{*}\right\}$ are expressed as

$$
\begin{aligned}
& p(x, y=1 \mid w)=a^{*} \mathcal{N}\left(x \mid b_{1}^{*}\right) \\
& p(x, y=2 \mid w)=\left(1-a^{*}\right) \mathcal{N}\left(x \mid b_{2}^{*}\right)
\end{aligned}
$$

and the ones of $w=\left\{1-a_{1}^{*}, b_{2}^{*}, b_{1}^{*}\right\}$ are

$$
\begin{aligned}
& p(x, y=1 \mid w)=\left(1-a^{*}\right) \mathcal{N}\left(x \mid b_{2}^{*}\right) \\
& p(x, y=2 \mid w)=a^{*} \mathcal{N}\left(x \mid b_{1}^{*}\right)
\end{aligned}
$$

They are equivalent when the labels 1 and 2 are swapped.
The multidimensional case, that the present paper focuses on, has two types of symmetry: the label values and the dimension of the latent value. In the simple two-layered binary Bayesian network defined by Eq. (5), the label probability with the parameter

$$
w=\left\{a_{01}^{*}, a_{02}^{*}, b_{00}^{*}, b_{01}^{*}, b_{10}^{*}, b_{11}^{*}\right\}
$$

and the one with

$$
w=\left\{a_{02}^{*}, a_{01}^{*}, b_{00}^{*}, b_{10}^{*}, b_{01}^{*}, b_{11}^{*}\right\}
$$

are equivalent, where $y_{1}$ and $y_{2}$ have symmetric relation. This is the symmetry of the dimension. Note that the symmetry of the label value also exists in each dimension. When $L_{1}=\cdots=L_{K}=L$, there are $K!\times(L!)^{K}$ symmetric assignments of the labels since permutations of the dimension and the label value are $K$ ! and $(L!)^{K}$, respectively.

Let us now consider the effect of the symmetry on the definitions of the error functions. Since the symmetric assignments should have equivalent probabilities, the estimated value $p\left(Y^{n} \mid X^{n}\right)$ has also $K!\times(L!)^{K}$ symmetric structure. The previous study [18] has shown that the redundancy of the label range $\left(L>L^{*}\right)$ does not adversely affect the accuracy in the case $K=K^{*}=1$. In the rest of this section, we will extend this result to the multidimensional case, where there is the range redundancy or the dimension redundancy. Section 6.2.1 explains that the error functions asymmetrically evaluate the estimation results when there is redundancy of the latent variables and the symmetry of the estimated distribution is different from that of the true distribution. Section 6.2.2 shows that the asymptotic forms of the error functions are determined by the local parameter area, which is the neighborhood of the true parameter. Then, in Section 6.2.3, we will confirm that the asymmetric evaluation does not make the error functions biased and their convergence rates are expressed as the forms of Theorem 6 and Corollary 12. We mainly consider the general case $K>K^{*}$ and $L>L^{*}$ in $D_{r 1}(n)$, which has the largest difference of the symmetry between the estimated and the true distributions, since we can show the similar results on the other error functions.

# 6.2.1 Asymmetric evaluation of the error functions with redundancy 

When there is the redundancy of the range or the dimension of the latent variables, the error functions define how the true distribution should be expressed. The error functions $D_{n 1}(n)$ and $D_{n 2}(n)$ limit the summation from $L$ to $L^{*}$, which implicitly assumes that the first $L^{*}$ values estimates the labels of the true distribution $y_{i k}^{(1)}=$ $1, \ldots, L^{*}$ in this order. For the dimension redundancy, $D_{r 1}(n)$ and $D_{r 2}(n)$ limit the summations to $Y_{1}^{n}$, which assumes that the first $K^{*}$ dimension in $y$ estimates the true distribution and the rest of $y$ is the redundant part. These definitions break the symmetry in the estimated distribution; some parameters essentially indicating the true distribution are not regarded as the true parameter. For example, there are two parameters $w_{X Y_{1} Y_{2}=1}^{*}$ and $w_{X Y_{1} Y_{2}=2}^{*}$ defined by

$$
\begin{aligned}
& \prod_{i=1}^{n} q\left(x_{i}, y_{i}^{(1)}\right)=\prod_{i=1}^{n} p\left(x_{i}, y_{i}^{(1)} \mid y_{i}^{(2)}=1, w_{X Y_{1} Y_{2}=1}^{*}\right) \\
& \prod_{i=1}^{n} q\left(x_{i}, y_{i}^{(1)}\right)=\prod_{i=1}^{n} p\left(x_{i}, y_{i}^{(1)} \mid y_{i}^{(2)}=2, w_{X Y_{1} Y_{2}=2}^{*}\right)
\end{aligned}
$$

respectively. In the eliminating way, either $w_{X Y_{1} Y_{2}=1}^{*}$ or $w_{X Y_{1} Y_{2}=2}^{*}$ can express the true distribution under the condition $y^{(2)}=1$ or $y^{(2)}=2$. Only the former one $w_{X Y_{1} Y_{2}=1}^{*}$ is regarded as the true parameter in $D_{r 1}(n)$ because the error function has the condition $y^{(2)}=1$. So we find that, when there is redundancy $L>L^{*}$ or $K>K^{*}$, the error functions asymmetrically evaluate the estimation results according to their definitions.

# 6.2.2 The asymptotic errors determined by the local parameter area 

For the eliminating way, the number of the symmetric assignments of the labels is calculated as

$$
C_{r}=\frac{K!}{\left(K-K^{*}\right)!} \times\left(\frac{L!}{\left(L-L^{*}\right)!}\right)^{K^{*}} \times L^{K-K^{*}}
$$

where $\frac{K!}{\left(K-K^{*}\right)!} \times\left(\frac{L!}{\left(L-L^{*}\right)!}\right)^{K^{*}}$ is the corresponding part to the true distribution and $L^{K-K^{*}}$ is the redundant one with fixed values. The true parameter $w_{X Y_{1} Y_{2}=1}^{*}$ provides the assignment, where the first $K^{*}$ dimension has the same as the true distribution and the remaining dimension is fixed as one. Then, the parameter space also has symmetric structure; the parameter space is divided into $C_{r}$ localized areas. Let the set of these areas be denoted by $\Sigma_{W}$. The estimated probability $p\left(Y_{1}^{n}, Y_{2}^{n} \mid X^{n}\right)$ is written as

$$
\begin{aligned}
p\left(Y_{1}^{n}, Y_{2}^{n} \mid X^{n}\right) & \propto p\left(X^{n}, Y_{1}^{n}, Y_{2}^{n}\right) \\
& =\int \prod_{i=1}^{n} p\left(x_{i}, y_{i}^{(1)}, y_{i}^{(2)} \mid w\right) \varphi(w \mid \eta) d w \\
& =\sum_{A_{W} \in \Sigma_{W}} \exp \left\{\ln \int_{A_{W}} \prod_{i=1}^{n} p\left(x_{i}, y_{i}^{(1)}, y_{i}^{(2)} \mid w\right) \varphi(w \mid \eta) d w\right\}
\end{aligned}
$$

Assume that the assignment $\bar{Y}^{n}=\left(\bar{Y}_{1}^{n}, \bar{Y}_{2}^{n}=1\right)$ is obtained from the model with the true parameter $w_{X Y_{1} Y_{2}=1}^{*}$ and $\bar{A}$ is its area. When the area is focused, we also use $w_{A}^{*}$ for the true parameter. Recall that the asymptotic form of $F_{X Y}(n)$ is derived from the calculation of the integral over the localized area determined by the blow-up mapping such as $\Phi_{1}$. By using the same coefficient such as $\lambda_{X Y_{1} C}$, the asymptotic

form of $p\left(X^{n}, \bar{Y}_{1}^{n}, \bar{Y}_{2}^{n}=1\right)$ is expressed as

$$
\begin{aligned}
p\left(X^{n}, \bar{Y}_{1}^{n}, \bar{Y}_{2}^{n}=1\right)= & \exp \left\{\ln \int_{A} \prod_{i=1}^{n} p\left(x_{i}, y_{i}^{(1)}, y_{i}^{(2)}=1 \mid w\right) \varphi(w \mid \eta) d w\right\} \\
& +\sum_{A_{W} \in \Sigma_{W} \backslash\{\bar{A}\}} \exp \left\{\ln \int_{A_{W}} \prod_{i=1}^{n} p\left(x_{i}, y_{i}^{(1)}, y_{i}^{(2)}=1 \mid w\right) \varphi(w \mid \eta) d w\right\} \\
= & \exp \left\{-n S_{w_{A}^{*}}\left(X^{n}, \bar{Y}_{1}^{n}, \bar{Y}_{2}^{n}=1\right)-\lambda_{X Y_{1} C} \ln n+O_{p}(\ln \ln n)\right\} \\
& +\sum_{A_{W} \in \Sigma_{W} \backslash\{\bar{A}\}} \exp \left\{\ln \int_{A_{W}} \prod_{i=1}^{n} p\left(x_{i}, y_{i}^{(1)}, y_{i}^{(2)}=1 \mid w\right) \varphi(w \mid \eta) d w\right\}
\end{aligned}
$$

where the empirical entropy is defined by

$$
S_{w}\left(X^{n}, Y_{1}^{n}, Y_{2}^{n}\right)=-\frac{1}{n} \sum_{i=1}^{n} \ln p\left(x_{i}, y_{i}^{(1)}, y_{i}^{(2)} \mid w\right)
$$

This asymptotic form shows that the dominant term of $-\ln p\left(X^{n}, Y_{1}^{n}, Y_{2}^{n}=1\right)$ is the entropy term with respect to the true parameter such as $w_{A}^{*}$. The empirical entropy is always larger than that of the different parameter areas. For example, though the assignment $Y^{n}=\left(\bar{Y}_{1}^{n}, Y_{2}=2\right)$ is correct in terms of the eliminating way, it makes the entropy term larger in the area $\bar{A}$;

$$
S_{w_{A}^{*}}\left(X^{n}, \bar{Y}_{1}^{n}, Y_{2}^{n}=2\right)>S_{w_{A}^{*}}\left(X^{n}, \bar{Y}_{1}^{n}, \bar{Y}_{2}^{n}=1\right)
$$

Then, the asymptotic form is written as

$$
-\ln p\left(X^{n}, \bar{Y}_{1}^{n}, \bar{Y}_{2}^{n}=1\right)=n S_{w_{A}^{*}}\left(X^{n}, \bar{Y}_{1}^{n}, \bar{Y}_{2}^{n}=1\right)+\lambda_{X Y_{1} C} \ln n+O_{p}(\ln \ln n)
$$

because the second term of the last expression in Eq.146, which is the integral on the different areas $\Sigma_{W} \backslash\{\bar{A}\}$, is much smaller than the first term and does not appear in the leading terms. In other words, this integral works as the operator selecting the true parameter to minimize the entropy term. The asymptotic form is determined by the integral on the local area, which is the neighborhood of the true parameter.

# 6.2.3 Effect on the accuracy 

We now introduce the relation between the entropy factors $S_{w_{A}^{*}}\left(X^{n}, \bar{Y}_{1}^{n}, \bar{Y}_{2}^{n}=1\right)$ and $S_{X Y}$. The error function is divided into two terms;

$$
D_{r 1}(n)=\frac{1}{n} E_{X^{n} Y_{1}^{n}}\left[\ln \frac{q\left(X^{n}, Y_{1}^{n}\right)}{p\left(X^{n}, Y_{1}^{n}, Y_{2}^{n}=1\right)}\right]-\frac{1}{n} E_{X^{n}}\left[\ln \frac{q\left(X^{n}\right)}{Z\left(X^{n}\right)}\right]
$$

Because the second term does not include $Y^{n}$, we focus on the first term.
The true distribution has $C_{q}$ symmetric areas of $Y_{1}^{n}$, where

$$
C_{q}=K^{*}!\times\left(L^{*}!\right)^{K^{*}}
$$

Since the estimated result has $C_{r}$ symmetric areas,

$$
\prod_{i=1}^{n} p\left(x_{i}, y_{i}^{(1)}, y_{i}^{(2)}=1 \mid w_{X Y_{1} Y_{2}=1}^{*}\right)=\frac{C_{q}}{C_{r}} \prod_{i=1}^{n} q\left(x_{i}, y_{i}^{(1)}\right)
$$

where the redundancy makes the estimated joint probability discounted due to the larger symmetric areas. By considering the relation Eq.142, this implies that

$$
\begin{aligned}
\prod_{i=1}^{n} p\left(y_{i}^{(2)}=1 \mid w_{X Y_{1} Y_{2}=1}^{*}\right) & =\frac{C_{q}}{C_{r}} \\
& =\left(\frac{K!}{\left(K-K^{*}\right)!K^{*}!}\right)^{-1} \times\left(\frac{L!}{\left(L-L^{*}\right)!L^{*}!}\right)^{-K^{*}} \times\left(L^{K-K^{*}}\right)^{-1}
\end{aligned}
$$

where the first factor $\left(\frac{K!}{\left(K-K^{*}\right)!K^{*}!}\right)^{-1}$ is the probability to select $K^{*}$ dimension from $K$, the second one $\left(\frac{L!}{\left(L-L^{*}\right)!L^{*}!}\right)^{-K^{*}}$ is the probability to select $L^{*}$ range from $L$ in $K^{*}$ dimension, and the third one $\left(L^{K-K^{*}}\right)^{-1}$ is the probability to fix the values as $Y_{2}^{n}=1$.

Based on Eq. 152, $S_{w_{X Y_{1} Y_{2}=1}}\left(X^{n}, Y_{1}^{n}, Y_{2}^{n}=1\right)$ is written as

$$
\begin{aligned}
S_{w_{X Y_{1} Y_{2}=1}}\left(X^{n}, Y_{1}^{n}, Y_{2}^{n}=1\right) & =-\frac{1}{n} \sum_{i=1}^{n} \ln p\left(x_{i}, y_{i}^{(1)}, y_{i}^{(2)}=1 \mid w_{X Y_{1} Y_{2}=1}^{*}\right) \\
& =-\frac{1}{n} \sum_{i=1}^{n} \ln q\left(x_{i}, y_{i}^{(1)}\right)+\frac{1}{n} \ln \frac{C_{r}}{C_{q}} \\
& =-\ln q\left(X^{n}, Y_{1}^{n}\right)+\frac{1}{n} \ln \frac{C_{r}}{C_{q}}
\end{aligned}
$$

The first term of Eq. 150 is then rewritten as

$$
\begin{aligned}
\frac{1}{n} E_{X^{n} Y_{1}^{n}}\left[\ln \frac{q\left(X^{n}, Y_{1}^{n}\right)}{p\left(X^{n}, Y_{1}^{n}, Y_{2}^{n}=1\right)}\right]= & -S_{X Y}+E_{X^{n} Y_{1}^{n}}\left[S_{w_{X Y_{1} Y_{2}=1}}\left(X^{n}, Y_{1}^{n}, Y_{2}^{n}=1\right)\right] \\
& +\lambda_{X Y_{1} C} \frac{\ln n}{n}+O\left(\frac{\ln \ln n}{n}\right) \\
= & -S_{X Y}+\frac{1}{n} E_{X^{n} Y_{1}^{n}}\left[-\ln q\left(X^{n}, Y_{1}^{n}\right)+\ln \frac{C_{r}}{C_{q}}\right] \\
& +\lambda_{X Y_{1} C} \frac{\ln n}{n}+O\left(\frac{\ln \ln n}{n}\right) \\
= & -S_{X Y}+S_{X Y}+\frac{1}{n} \ln \frac{C_{r}}{C_{q}} \\
& +\lambda_{X Y_{1} C} \frac{\ln n}{n}+O\left(\frac{\ln \ln n}{n}\right) \\
= & \lambda_{X Y_{1} C} \frac{\ln n}{n}+O\left(\frac{\ln \ln n}{n}\right)
\end{aligned}
$$

Combining the asymptotic form of the second term of Eq.150, we find that the error converges to zero and its convergence rate is the one shown in Theorem 9. We can easily prove that the other error functions are unbiased, replacing the constant $C_{r}$ with

$$
C_{r}=\frac{K!}{\left(K-K^{*}\right)!} \times\left(\frac{L!}{\left(L-L^{*}\right)!}\right)^{K^{*}}
$$

for $D_{r 2}(n)$, and with

$$
C_{r}=\left(\frac{L!}{\left(L-L^{*}\right)!}\right)^{K^{*}}
$$

for $D_{n 1}(n)$ and $D_{n 2}(n)$ in the case $K=K^{*}$ and $L>L^{*}$. Due to the marginalization on $Y_{2}^{n}$ in $D_{r 2}(n)$, Eq. 156 does not have the fixed value factor compared to the expression for $D_{r 1}(n)$. When there is no redundancy on the dimension $K=K^{*}, C_{r}$ in Eq. 157 consists of the single factor to select the range. Note that the error functions $D_{n 1}(n)$ and $D_{n 2}(n)$ do not have the difference on the symmetry when $K=K^{*}$ and $L=L^{*}$, that is $C_{r}=C_{q}$, and the estimated probability of the symmetric areas has the equivalent value to the true distribution. Thus, the symmetric estimation and the limitation of the true assignment defined by the error functions do not change the asymptotic forms of our results.

# 7 Conclusions 

The present paper formulated the error functions of the Bayesian estimation of multidimensional latent variables, and derived their asymptotic forms. According to the number of the dimensions of the latent variables, there are redundant and non-redundant cases. For the asymptotic analysis, the Fisher information matrices play an important role in the non-redundant case while the zeta functions of the algebraic geometrical method do in the redundant case.

Precise calculation of the coefficient $\lambda_{A}$ is necessary to clarify the dominant order in the redundant case, and as seen in Section 5, this calculation is complex. Even in a simpler structure, such as a naive Bayesian network or a tree model, an additional mathematical technique is required [11, 24]. The exact form of $\lambda_{X}$ can be derived for certain limited models, and the algebraic geometrical approach is still being developed (e.g., $[19,8]$ ). It is an important goal to obtain a detailed analysis of these coefficients.

## Acknowledgements

This research was partially supported by a research grant by the Support Center for Advanced Telecommunications Technology Research Foundation and by KAKENHI 15 K 00299 .
