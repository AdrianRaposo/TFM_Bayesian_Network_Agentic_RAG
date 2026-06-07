# Causal inference and Bayesian network structure learning from nominal data 

Guiming Luo ${ }^{1} \cdot$ Boxu Zhao ${ }^{1}$ (D) $\cdot$ Shiyuan Du ${ }^{1}$

Published online: 25 August 2018
(c) Springer Science+Business Media, LLC, part of Springer Nature 2018


#### Abstract

This study investigates a discrete causal method for nominal data (DCMND) which is one of the important issues of causal inference. It is utilized to learn the causal Bayesian network to reflect the interconnections between variables in our paper. This article also proposes a Bayesian network construction algorithm based on discrete causal inference (BDCI) and an extended BDCI Bayesian network construction algorithm based on DCMND. Furthermore, the paper studies the alarm data of mobile communication system in practice. The results suggest that decision criterion based our method is effective in causal inference and the Bayesian network constructed by our method has better classification accuracy compared to other methods.


Keywords Causal inference $\cdot$ Bayesian network $\cdot$ Discrete causal method $\cdot$ Nominal data $\cdot$ Alarm analysis

## 1 Introduction

The causality analysis problem can be divided into two parts: correlation analysis and direction analysis. Correlation analysis can generally be resolved by the statistical method, while direction analysis requires more in-depth theoretical study. In many research areas, inferring causal direction from observation data has been an important research topic. For example, in the network management field, fault may cause a number of alarms collected by devices. Not all of these alarms can instruct the root cause of failure, resulting in that critical alarms are buried under unnecessary ones. So we need to analyze the causality of different alarms to find out the root fault. Recently, causality analysis and calculation methods from observation data have been paid much attention to.

Subsequently, Hoyer proposed a causality analysis method based on additive noise model (ANM) [1]. In this method, the model function can be a linear function, can also be a non-linear function and expand the expression of the model to a certain extent.

[^0]The principle of causality analysis based on asymmetric property [2] is to judge the causal relationship between variables according to the asymmetric property of the model or data distribution in causal and non-causal directions. Such methods mainly study the distribution function of a particular mathematical model, analyze some of their properties in causal direction, and this property is often not valid in the non-causal direction, then we get a relationship and infer the causal direction between the variables according to the asymmetric relationship in the observation data.

Causality analysis based on asymmetric properties has been proposed in recent years, and has been followed by continuous development. The embryonic form of this method originated from Shimizu's acyclic linear nonGaussian model (LiNGAM) [3]. The LiNGAM model assumes that the causal mechanism of the data is a linear function. The noise variables of the model follow nonGaussian distributions with non-zero variance, and the model is not disturbed by potential causal variables. In a subsequent study, causality analysis method based on asymmetry mainly uses some kind of asymmetric property of the observed data in probability distribution. The basis of this method is that if the causal relationship between $X$ and $Y$ is $X \rightarrow Y$, the probability distributions $p(X)$ and $p(Y \mid X)$ should satisfy some independence condition, and the independence condition is generally not true for


[^0]:    Boxu Zhao
    boxu.zhao@foxmail.com
    1 School of Software, Tsinghua University, Beijing 100084, China

$p(Y)$ and $p(X \mid Y)$. Thus an asymmetric property for causal direction inference can be derived. According to this idea, Janzing proposed IGCI (information geometric causal inference) causality analysis [4]. Zscheischler proposed the LTr (linear trace) method for the causality analysis of high-dimensional data [5]. IGCI method first assumes that the probability density of the causal variable and the nonlinear model function satisfy a certain independence condition, but the probability density of the result variable and the inverse function do not satisfy the independence condition. Then according to this asymmetry, IGCI gives an entropy-based approach to find causality. Although the IGCI method can achieve good results in the experiment, this method mainly studies the noise-free condition, which is too ideal in practical problems. Zscheischler proposed the LTr (linear trace) method for the causality analysis of high-dimensional data [5]. Although the LTr method can be used to analyze the causal direction of multidimensional data, the method needs to be based on the assumption that the causal mechanism is a linear function, and does not consider the influence of noise. Subsequently, EMD method proposed by Chen [6] has improved the above methods. EMD method is a model-independent causality analysis method, the independence condition defined by this method is only related to the probability density function of the observed data, but not to the model function. The EMD method can be applied to both one-dimensional data and multidimensional data, and the influence of the method on noise is also considered.

For causality analysis of discrete variables, Budhathoki and Vreeken [7] proposed CISC to inference casuality for pairs of univariate discrete variables. Peters [8] extended the notion of additive noise models to the discrete variables. (DANM) Liu [9] proposed a causal inference method on discrete data via estimating distance correlations. (CIEDC) Sun [10] proposed a method based on the Markov kernel confidence. The method can be applied to both continuous variables and discrete variables. However, because the method involves the Markov conditional hypothesis, this method can not show stable causal direction discrimination ability. In the follow-up study, Peters extended the additive noise model [11], and proposed a causality analysis method for discrete variables. Based on whether the range of variables is finite, this paper presents two additive noise extension models, which are integer model and cyclic model. The extended additive noise model is still based on the independence of the noise variables and input variables to determine causal direction, but in doing regression analysis for discrete variables regression method. Causality analysis based on EMD method can be more effective for discrete variables, but for nonnumerical nominal data and can not achieve very good results.

## 2 Discrete causal method for nominal data

### 2.1 Additive noise model

The additive noise model is a commonly used as causality analysis model between two variables. The typical additive noise model is defined as (1) and (2):
$Y=f(X)+N_{p}, N_{p} \perp X$.
$X=g(Y)+N_{r}, N_{r} \perp Y$.
Where $f$ and $g$ are linear functions, $N_{p}$ denotes an additive noise variable independent of $X, N_{r}$ represents an additive noise variable independent of $Y$. Equation (1) shows an additive noise model with a causal direction of $X \rightarrow Y$, (2) shows the additive noise model with causal direction $Y \rightarrow X$. In order to allow the model to be applied to discrete data, Peters obtained two extended models [11]. Among the two models, the cyclic model is the focus of this paper.

The cyclic model is mainly used for finite discrete data. The definition of the model is the same as (1) and (2), only the value of the variable and the meaning of the plus sign operator have changed. In the cyclic model, the range of $X$ and $N_{r}$ is all the elements of the residue class ring $Z / m Z$ of $m, Y$ and $N_{p}$ are in the range of all the elements in the residue class ring $Z / n Z$ of $n$. Correspondingly, $f$ is an arbitrary function mapped from $Z / m Z$ to $Z / n Z, \mathrm{~g}$ is an arbitrary function mapped from $Z / n Z$ to $Z / m Z$, and the addition sign in the definition formula represents the addition in the corresponding residue class ring. Let $N_{p}^{\prime}$ and $N_{r}^{\prime}$ denote the actual fitting values of the noise variables $N_{p}$ and $N_{r}$ after regression analysis, respectively. The causal direction analysis of the cyclic model is as fellows:

1. $N_{p}^{\prime}$ and $X$ independent, $N_{r}^{\prime}$ and $Y$ are not independent, then the causal direction of $X \rightarrow Y$;
2. $N_{p}^{\prime}$ and $X$ are not independent, $N_{r}^{\prime}$ and $Y$ independent, then the causal direction of $Y \rightarrow X$;
3. $N_{p}^{\prime}$ is independent of $X, N_{r}^{\prime}$ is independent of $Y$; or $N_{p}^{\prime}$ is not independent from $X$, and $N_{r}^{\prime}$ is not independent of $Y$, then causal direction can not be determined.

It is worth noting that Peters notes that the cyclic model can be applied to nominal data if the cyclic model satisfies some special constraints [11]. While it can be found from the experiment that the method may not achieve good results when the cyclic model is applied to the nominal data set.

### 2.2 EMD algorithm

In the EMD algorithm, $x$ represents an $n$-dimensional variable, $y$ represents an $m$-dimensional variable, $R_{x}$ and $R_{y}$ represent the range of values of $x$ and $y$, respectively. And

$R_{x}=[0,1]^{n}, R_{y}=[0,1]^{m}$. EMD algorithm also defines two functions, as shown in (3), (4):
$h_{1}(x)=\int p(y \mid x) d y$.
$h_{2}(x)=\int p^{2}(y \mid x) d y$.
Assuming that the causal relationship between $x$ and $y$ is $x \rightarrow y$, then the probability density $p(x)$ and the conditional probability density $p(y \mid x)$ should be independent. The EMD algorithm defines that $p(x)$ and $p(y \mid x)$ are independent if the irrelevant condition shown in (5) is satisfied when given any specific value of $y$.
$\int h_{u}(x) p(x) d x=\int h_{u}(x) d x \int p(x) d x, u=1,2$.
The EMD algorithm states that if the irrelevant condition shown in (5) is true in the causal direction, then the uncorrelated condition is not true in the non-causal direction, and thus an asymmetric property is obtained. In order to measure the difference between the two probability densities, the EMD algorithm defines the function $D_{c}$ as shown in (6), where $p_{1}(x)$ and $p_{2}(x)$ represent the two probability density functions on $R_{x}$.
$D_{c}\left[p_{1}(x) \| p_{2}(x)\right]=\int_{R_{X}}\left[p_{1}(x)-p_{2}(x)\right]^{2} d x$
The EMD algorithm defines two equations shown in (7) and (8), where $u_{x}$ is a uniform distribution over $R_{x}$, $u_{y}$ is a uniform distribution over $R_{y}$, and both $p_{x y}$ and $p_{y x}$ represent the joint probability density $p(x, y)$, $p_{y \mid x}$ represents the probability density $p(y \mid x)$, and $p_{x \mid y}$ represents the probability density $p(x \mid y)$.
$C_{x \rightarrow y}=D_{c}\left[p_{y x} \| p_{y \mid x} u_{x}\right]+D_{c}\left[p_{y \mid x} u_{x} \| u_{y} u_{x}\right]$.
$C_{y \rightarrow x}=D_{c}\left[p_{x y} \| p_{x \mid y} u_{y}\right]+D_{c}\left[p_{x \mid y} u_{y} \| u_{x} u_{y}\right]$.
Under the premise of non-relevant conditions, EMD algorithm derives the following derivation criterion:

1. $C_{x \rightarrow y}<C_{y \rightarrow x}$, then the causal direction is $x \rightarrow y$;
2. $C_{x \rightarrow y}>C_{y \rightarrow x}$, then the causal direction is $y \rightarrow x$;
3. $C_{x \rightarrow y}=C_{y \rightarrow x}$, the causal direction can not be determined.

### 2.3 Discrete causal model for nominal data

In this part, we first define a discrete stochastic noise model, which is based on the extended additive noise model and makes the model more suitable for the analysis of the nominal data by introducing new noise variable constraints. Then the reversibility of discrete stochastic noise model is analyzed in this part, and the condition that the model can distinguish causal direction effectively is obtained.

### 2.3.1 Discrete stochastic noise model

Before the definition of the model is given, some relevant definitions are made. Assuming that $Z_{M}$ is a set of integers 0 to $M-1, Z_{N}$ is a set of integers 0 to $N-1, Z_{M}$ and $Z_{N}$ are defined as shown in (9) and (10)
$Z_{M}=\{x \mid x \in Z, 0 \leq x \leq M-1\}$
$Z_{N}=\{x \mid x \in Z, 0 \leq x \leq N-1\}$
Let $X, Y$ be two discrete variables, and $X \in Z_{M}, Y \in$ $Z_{N}$, define an arbitrary function $f$ that maps from $Z_{M}$ to $Z_{N}$, and the function definition is as shown in (11):
$Y=f(X), \quad X \in Z_{M}, Y \in Z_{N}$
To characterize the interference of other factors, we define the noise variable $E_{Y} \in Z_{N}$, and $E_{Y}$ needs to satisfy the probability distribution defined by (12) and (13).
$P\left(E_{Y}=0\right)>\sum_{y \in Z_{N}, y \neq 0} P\left(E_{Y}=y\right)$
$P\left(E_{Y}=y\right)=\frac{1-P\left(E_{Y}=0\right)}{N-1}, y \in Z_{N}, y \neq 0$
In conjunction with the above definition, a discrete stochastic noise model with a causal direction of $X \rightarrow Y$ is shown in (14). Where $E_{Y}$ is independent of $X$.
$Y=\left(f(X)+E_{Y}\right) \bmod N$
Compared with the extended additive noise model, the discrete stochastic noise model has made some changes in the definition of the form, and added the formula (12), (13) to the noise variable $E_{Y}$ to limit the probability distribution. This is done in response to the application scenario for the nominal data set and to ensure that the discrete stochastic noise model can exhibit good causality.

### 2.3.2 Model reversibility condition

For a discrete stochastic noise model, the reversibility of the model is: for a discrete stochastic noise model with a causal direction of $X \rightarrow Y(Y \rightarrow X)$, if from the opposite direction, ie $Y \rightarrow X(X \rightarrow Y)$ Still can fit a discrete stochastic noise model, then the model is reversible, and the model constructed from the opposite direction is called the inverse model of the original model. Taking the discrete stochastic noise model defined by (14) as an example, if a model of the form (15) can be fitted from its opposite direction $Y \rightarrow X$, then the model defined by (14) is reversible, and the model (15) is the inverse model of the model (14).
$X=\left(g(Y)+E_{X}\right) \quad \bmod M$

$g$ is an arbitrary function from $Z_{N}$ to $Z_{M}, E_{X}$ is a noise variable, independent of $Y$, and $E_{X} \in Z_{M}$, and satisfies the restrictions defined by formulas (16) and (17).
$P\left(E_{X}=0\right)>\sum_{x \in Z_{M}, x \neq 0} P\left(E_{X}=x\right)$
$P\left(E_{X}=x\right)=\frac{1-P\left(E_{X}=0\right)}{M-1}, x \in Z_{M}, x \neq 0$
In general, the irreversibility of the model is the basis of causal direction inference. This is because, for an irreversible causal model, the causal direction can be found by using the asymmetric property of causality as inference criterion. However, if the model is reversible, or reversible conditions are easily available, it will make the original asymmetric property disappearance or dilute, reducing the ability of the model to determine causality. Therefore, analyzing the reversibility conditions of the model will help to determine the applicable scenario for the causal inference method.

Table 1 shows the reversibility in 4 different situation. Peters et al. [11] $p_{x}\left(x_{i}\right)$ represents $P\left(X=x_{i}\right)$. We can see in situation 1 and situation 2, there are reversible conditions. However, as the reversible conditions have strict requirements, the discrete random noise model can be considered irreversible in most cases.

### 2.4 Formula derivation and causal inference criterion

In this part, a causal inference method based on discrete stochastic noise model is presented. This method borrows the thought from EMD algorithm for causal decision, and then uses the discrete method to extend it. Combined with the discrete stochastic noise model, this paper deduces the causal direction inference method for the nominal data.

As the premise of probability independence conditions, EMD algorithm derives asymmetric property based on probability density and applies it to causal discovery. But the method is for continuous variables, not for discrete variables, as independent conditions will no longer hold. Nevertheless, the idea of causal inference from the perspective of probability is still an effective solution. For this reason, this paper will discretize the EMD algorithm and re-derive the analysis to give a causal inference method.

Corresponding to the EMD algorithm, a function $D$ is defined here to measure the difference between the two probability distributions in the discrete case. Assuming that $P_{1 x}$ and $P_{2 x}$ represent two probability distributions of $X$, $P_{1}(X)$ and $P_{2}(X)$ denote the probability values of these two distributions respectively, then the definition of function $D$ is shown in (18)
$D\left(P_{1 x} \| P_{2 x}\right)=\sum_{x \in Z_{M}}\left[P_{1}(X=x)-P_{2}(X=x)\right]^{2}$

Let $U_{x}$ and $U_{y}$ denote the uniform distribution about $X$ and $Y, U_{x y}$ represents the two-dimensional uniform distribution about $X$ and $Y$ respectively; we set $D I_{x \rightarrow y}$ and $D I_{y \rightarrow x}$ correspond to $C_{x \rightarrow y}$ and $C_{y \rightarrow x}$ in the EMD algorithm, then,
$D I_{x \rightarrow y}=D\left(P_{x y} \| P_{y \mid x} U_{x}\right)+D\left(P_{y \mid x} U_{x} \| U_{x y}\right)$
$D I_{y \rightarrow x}=D\left(P_{x y} \| P_{x \mid y} U_{y}\right)+D\left(P_{x \mid y} U_{y} \| U_{x y}\right)$
In order to facilitate the deduction next, the relevant symbol definitions are introduced: $x_{i}$ is the $i$-th element of $X, y_{j}$ is the $j$-th element of $Y, p_{x}\left(x_{i}\right)$ represents $P\left(X=x_{i}\right), p_{y}\left(y_{j}\right)$ represents $P\left(Y=y_{j}\right), p_{x \mid y}\left(x_{i} \mid y_{j}\right)$ represents $P(X=$ $\left.x_{i} \mid Y=y_{j}\right), p_{y \mid x}\left(y_{j} \mid x_{k}\right)$ represents $P\left(Y=y_{j} \mid X=x_{i}\right)$, $p_{x y}\left(x_{i}, y_{j}\right)$ represents $P\left(X=x_{i}, Y=y_{j}\right), p_{e}$ represents $P\left(E_{Y} \neq 0\right)$.

$$
\begin{aligned}
D\left(P_{x y} \| U_{x y}\right)= & \sum_{x \in Z_{M}} \sum_{y \in Z_{N}}\left[p_{x y}(x, y)-\frac{1}{M N}\right]^{2} \\
= & \sum_{x \in Z_{M}} \sum_{y \in Z_{N}}\left[p_{x y}^{2}(x, y)-\frac{1}{M N} p_{x y}(x, y)+\frac{1}{\left(M N\right)^{2}}\right] \\
= & \sum_{x \in Z_{M}} \sum_{y \in Z_{N}}\left\{p_{x y}^{2}(x, y)\right\}-\frac{1}{M N}+\frac{1}{M N} \\
= & \sum_{x \in Z_{M}} \sum_{y \in Z_{N}} p_{x y}^{2}(x, y)-\frac{1}{M N}
\end{aligned}
$$

$$
\begin{aligned}
D\left(P_{x y} \| P_{y \mid x} U_{x}\right) & =\sum_{x} \sum_{y}\left[p_{x y}(x, y)-\frac{1}{M} p_{y \mid x}(y \mid x)\right]^{2} \\
& =\sum_{x} \sum_{y}\left[p_{y \mid x}\left(y \mid x\right) p_{x}(x)-\frac{1}{M} p_{y \mid x}(y \mid x)\right]^{2} \\
& =\sum_{x} \sum_{y} p_{y \mid x}^{2}\left(y \mid x\right)\left[p_{x}^{2}(x)-\frac{2}{M} p_{x}(x)+\frac{1}{M^{2}}\right] \\
& =\sum_{x} \sum_{y}\left[p_{x y}^{2}(x, y)-p_{y \mid x}^{2}(y \mid x)\left[\frac{2}{M} p_{x}(x)-\frac{1}{M^{2}}\right]\right]
\end{aligned}
$$

$$
\begin{aligned}
D\left(P_{y \mid x} U_{x} \| U_{x y}\right) & =\sum_{x} \sum_{y}\left[\frac{1}{M} p_{y \mid x}(y \mid x)-\frac{1}{M N}\right]^{2} \\
& =\sum_{x} \sum_{y}\left[\frac{1}{M^{2}} p_{y \mid x}^{2}(y \mid x)-\frac{2}{M^{2} N} p_{y \mid x}(y \mid x)+\frac{1}{\left(M N\right)^{2}}\right] \\
& =\sum_{x} \sum_{y}\left[\frac{1}{M^{2}} p_{y \mid x}^{2}(y \mid x)\right]-\frac{2 M}{M^{2} N}+\frac{1}{M N} \\
& =\sum_{x} \sum_{y}\left[\frac{1}{M^{2}} p_{y \mid x}^{2}(y \mid x)\right]-\frac{1}{M N}
\end{aligned}
$$

From (22) and (23), we can deduce $D I_{x \rightarrow y}$ as shown in formula (24).

$$
\begin{aligned}
D I_{x \rightarrow y}= & D\left(P_{x y} \| P_{y \mid x} U_{x}\right)+D\left(P_{y \mid x} U_{x} \| U_{x y}\right) \\
= & \sum_{x} \sum_{y}\left[p_{x y}^{2}(x, y)\right]-\frac{1}{M N} \\
& +\sum_{x} \sum_{y}\left[\frac{2}{M^{2}} p_{y \mid x}^{2}(y \mid x)-\frac{2}{M} p_{x}(x) p_{y \mid x}^{2}(y \mid x)\right]
\end{aligned}
$$

Similarly, for $D\left(P_{x y} \| P_{x \mid y} U_{y}\right)$ and $D\left(P_{x \mid y} U_{y} \| U_{x y}\right)$, we can get (25) and (26):
$D\left(P_{x y} \| P_{x \mid y} U_{y}\right)=\sum_{x} \sum_{y}\left[p_{x y}^{2}(x, y)-p_{x \mid y}^{2}(x \mid y)\left[\frac{2}{N} p_{y}(y)-\frac{1}{N^{2}}\right]\right]$

Table 1 Reversibility when $f$ in different situation


$D\left(P_{x \mid y} U_{y} \| U_{x y}\right)=\sum_{x} \sum_{y}\left[\frac{1}{N^{2}} p_{x \mid y}^{2}(x \mid y)\right]-\frac{1}{M N}$
From (25) and (26), we can deduce $D I_{y \rightarrow x}$ as shown in formula (27).

$$
\begin{aligned}
D I_{y \rightarrow x}= & D\left(P_{x y} \| P_{x \mid y} U_{y}\right)+D\left(P_{x \mid y} U_{y} \| U_{x y}\right) \\
= & \sum_{x} \sum_{y}\left[p_{x \mid y}^{2}(x, y)\right]-\frac{1}{M N} \\
& +\sum_{x} \sum_{y}\left[\frac{2}{N^{2}} p_{x \mid y}^{2}(x \mid y)-\frac{2}{N} p_{y}(y) p_{x \mid y}^{2}(x \mid y)\right]
\end{aligned}
$$

We can set
$R_{1}=\sum_{x \in Z_{M}} \sum_{y \in Z_{N}}\left[\frac{2}{M^{2}} p_{y \mid x}^{2}(y \mid x)-\frac{2}{M} p_{x}(x) p_{y \mid x}^{2}(y \mid x)\right]$
$R_{2}=\sum_{x \in Z_{M}} \sum_{y \in Z_{N}}\left[\frac{2}{N^{2}} p_{x \mid y}^{2}(x \mid y)-\frac{2}{N} p_{y}(y) p_{x \mid y}^{2}(x \mid y)\right]$
then we can get
$D I_{x \rightarrow y}=D\left(P_{x y} \| U_{x y}\right)+R_{1}$
$D I_{y \rightarrow x}=D\left(P_{x y} \| U_{x y}\right)+R_{2}$
Next, the paper analyzes $R_{1}$ and $R_{2}$ based on the model whose causal direction is $X \rightarrow Y$. For $R_{1}$, according to the definition of the model and the constraints of (13), we can conclude that (32) holds for any $x_{i} \in Z_{M}$. Here, $C_{\text {sum }}$ in (32) is a constant, and $C_{\text {sum }}$ is introduced to simplify the following analysis.
$C_{\text {sum }}=\left(1-p_{e}\right)^{2}+(N-1)\left(\frac{p_{e}}{N-1}\right)^{2}$
According to formula (32), we can derive the formula (33) for $R_{1}$ :

$$
\begin{aligned}
R_{1} & =\sum_{x \in Z_{M}} \sum_{y \in Z_{N}}\left[\frac{2}{M^{2}} p_{y \mid x}^{2}(y \mid x)-\frac{2}{M} p_{x}(x) p_{y \mid x}^{2}(y \mid x)\right] \\
& =\sum_{x \in Z_{M}}\left[\frac{2}{M^{2}} C_{\text {sum }}-\frac{2}{M} p_{x}(x) C_{\text {sum }}\right] \\
& =C_{\text {sum }} \frac{2 M}{M^{2}}-C_{\text {sum }} \frac{2}{M} \\
& =0
\end{aligned}
$$

For $R_{2}$, in the case that the model is not reversible, the conclusion of (33) can not be obtained, so additional analysis is required. Suppose that $f$ is bijective. Let $f\left(x_{1}\right)=y_{1}, f\left(x_{2}\right)=y_{2}$ for any two different $x_{1}$ and $x_{2}$. Let $p_{y}\left(y_{1}\right)>p_{y}\left(y_{2}\right)$, we can get $p_{x}\left(x_{1}\right)>p_{x}\left(x_{2}\right)$ then

$$
\begin{aligned}
& =\frac{p_{x \mid y}\left(f^{-1}\left(y_{1}\right) \mid y_{1}\right)-p_{x \mid y}\left(f^{-1}\left(y_{2}\right) \mid y_{2}\right)=p_{x \mid y}\left(x_{1} \mid y_{1}\right)-p_{x \mid y}\left(x_{2} \mid y_{2}\right)}{p_{x}\left(x_{1}\right)\left(1-p_{e}\right)+\sum_{r \neq x_{1}} \frac{p_{x}\left(x_{2}\right)}{N-1}-\frac{p_{x}\left(x_{2}\right)\left(1-p_{e}\right)}{p_{x}\left(x_{2}\right)\left(1-p_{e}\right)+\sum_{r \neq x_{2}} \frac{p_{x}\left(x_{2}\right) x_{2}}{N-1}}} \\
& =\frac{\left(1-p_{e}\right)\left[\frac{p_{e}}{N-1}\left(p_{x}^{2}\left(x_{1}\right)-p_{e}^{2}\left(x_{2}\right)\right)+\left(p_{x}\left(x_{1}\right)-p_{x}\left(x_{2}\right)\right) \sum_{r \neq x_{1}, x_{2}} \frac{p_{x}\left(x_{2}\right) x_{2}}{N-1}\right]}{p_{x}\left(x_{1}\right)\left(1-p_{e}\right)+\sum_{r \neq x_{1}} \frac{p_{x}\left(x_{2}\right) x_{2}}{N-1}\left[\left[p_{x}\left(x_{2}\right)\left(1-p_{e}\right)+\sum_{r \neq x_{2}} \frac{p_{x}\left(x_{2}\right) x_{2}}{N-1}\right]\right.} \\
& >0
\end{aligned}
$$

From the above analysis, it can be seen that when $f$ is bijective, $p_{x \mid y}\left(f^{-1}(y) \mid y\right)$ increases with the increase of $p_{y}(y)$, they show a proportional relationship. For the convenience of the following analysis, $p_{y}(y)$ is divided into two parts: $p_{y}(y)>1 / N$ and $p_{y}(y) \leqslant 1 / N$, respectively denoted as $y_{\alpha}^{i}$ and $y_{\beta}^{j}$, then we can express:
$p_{y}\left(y_{\alpha}^{i}\right)=\frac{1}{N}+\alpha_{i}, \alpha_{i}>0$
$p_{y}\left(y_{\beta}^{j}\right)=\frac{1}{N}-\beta_{j}, \beta_{j} \geq 0$
From the proportional relationship between $p_{y}(y)$ and $p_{x \mid y}\left(f^{-1}(y) \mid y\right)$, we can get the following formula:
$p_{x \mid y}\left(f^{-1}\left(y_{\alpha}^{1}\right) \mid y_{\alpha}^{1}\right)>p_{x \mid y}\left(f^{-1}\left(y_{\beta}^{n}\right) \mid y_{\beta}^{n}\right)$
Equation (38) can be obtained from the property that the probability sum is 1 :
$\sum_{1 \leq i \leq m} \alpha_{i}=\sum_{1 \leq j \leq n} \beta_{j}$
Under normal circumstances, if not considering $p_{x}(x)$ in a particularly large extreme situation, the value of $p_{x}(x) p_{e} /(N-1)$ is very small, while $p_{x}(x)\left(1-p_{e}\right)$ is really large. $p_{x \mid y}\left(f^{-1}(y) \mid y\right)$ is generally much larger than the value of $p_{x \mid y}\left(x f^{-1}(y) \mid y\right)$, so $p_{x \mid y}\left(f^{-1}(y) \mid y\right)$ can be

neglected to a certain extent in the calculation of $R_{2}$. Combining (37) and (28), we can get:

$$
\begin{aligned}
R_{2} & =\sum_{x \in Z_{M}} \sum_{y \in Z_{N}}\left[\frac{2}{\sqrt{7}} p_{x \mid y}^{2}(x \mid y)-\frac{2}{N} p_{y}(y) p_{x \mid y}^{2}(x \mid y)\right] \\
& =\sum_{y \in Z_{N}} \frac{2 p_{x \mid y}^{2}(f^{-1}(y \mid \mid y)}{N}\left(\frac{1}{N}-p_{y}(y)\right) \\
& =\sum_{1 \leq j \leq n} \frac{2 p_{x \mid y}^{2}\left(f^{-1}\left(y_{p}^{1} \mid \mid y_{p}^{1}\right)\right.}{N} \beta_{j}-\sum_{1 \leq i \leq m} \frac{2 p_{x \mid y}^{2}\left(f^{-1}\left(y_{p}^{1} \mid \mid y_{p}^{1}\right)\right.}{N} \alpha_{i} \\
& \left\langle\frac{2 p_{x \mid y}^{2}\left(f^{-1}\left(y_{p}^{0} \mid \mid y_{p}^{0}\right)\right.}{N} \sum_{1 \leq j \leq n} \beta_{j}-\frac{2 p_{x \mid y}^{2}\left(f^{-1}\left(y_{p}^{1} \mid \mid y_{p}^{1}\right)\right.}{N} \sum_{1 \leq i \leq m} \alpha_{i} \\
& =\left(\frac{2\left(p_{x \mid y}^{2}\left(f^{-1}\left(y_{p}^{0} \mid \mid y_{p}^{0}\right)-p_{x \mid y}^{2}\left(f^{-1}\left(y_{p}^{1} \mid \mid y_{p}^{1}\right)\right)\right.}{N}\right) \sum_{1 \leq i \leq m} \alpha_{i}\right. \\
& <0
\end{aligned}
$$

Combining formulas (34) and (39), we can get $R_{1}>$ $R_{2}$, then we can get a conclusion $D I_{x \rightarrow y}>D I_{y \rightarrow x}$. Analogously, for a model with a causal direction of $Y \rightarrow X$, we can get similar conclusions under the same conditions. In the above analysis, in addition to requiring the model irreversible, we also need $f$ is bijection to deduce $D I_{x \rightarrow y}>$ $D I_{y \rightarrow x}$. However, it doesn't strictly require $f$ for bijection in practical application, as long as $f$ is not extreme "many to one" mapping. Similarly, for the causal direction $Y \rightarrow X$, when the model is not reversible and the function $g$ meet similar conditions, we can get the conclusion $D I_{y \rightarrow x}>$ $D I_{x \rightarrow y}$.

Then, we can get the following causal inference criterion:

1. When $D I_{x \rightarrow y}>D I_{y \rightarrow x}, X \rightarrow Y$;
2. When $D I_{x \rightarrow y}<D I_{y \rightarrow x}, Y \rightarrow X$;
3. When $D I_{x \rightarrow y}=D I_{y \rightarrow x}$, can not determine causal direction.

## 3 Causal network construction

For the causal analysis, the network construction algorithm has been one area of the research focus. A variety of methods [12-14] has been proposed through extracting the causal relation between variables. In other research described in [15], event threading is used to construct a causal network. In the paper, we construct the causal network using Bayesian network theory. In Bayesian networks, conditional dependency relationship exists between the connected nodes, which makes the Bayesian network to some extent reflect the interrelations among variables. However, the Bayesian network is not a causal network, and the edges in the Bayesian network do not represent the true causal relationship between the nodes. In order to construct a Bayesian network with causality, this chapter starts from the discrete causal analysis method and obtains the causal relationship between the variables. Then, the edges with causal relationship are organized according to certain rules to construct complete Bayesian network. The paper proposes a Bayesian network construction algorithm based on discrete causal inference(BCDI) and an extended

BDCI Bayesian network construction algorithm. In this chapter, we first define a causal association score function to describe the degree of causal association between two variables. Then we define a Bayesian network scoring function to evaluate the network constructed according to the discrete causality. A BDCI and extended BDCI Bayesian network construction algorithm are presented. Finally, some experiments about the algorithm are given.

### 3.1 Causal relevance and Bayesian network scoring function

When constructing a Bayesian network by using the causal relationship between variables, it is likely to lead to the network ring, or the network is too complex if causal variables are connected. The appearance of rings violates the definition of Bayesian networks, while complex networks can cause over-fitting. Therefore, when constructing a Bayesian network using causality, it should be possible to choose to link variables with strong causal associations and ignore the weak ones. To achieve this, there is a need for a way to measure causality.

Let $Z_{x}$ and $Z_{y}$ be a finite set of $M$ and $N$ elements respectively, $X$ and $Y$ are two discrete variables, and $X \in$ $Z_{x}, Y \in Z_{y}$; For the observation data of $X$ and $Y, S\left(x_{i}\right)$ represents the number of $X=x_{i}$ in the data set, $S_{t}(x i, y j)$ is the number of $X=x_{i}$ and $Y=y_{j}$. Assuming that the causal relationship between $X$ and $Y$ is $X Y$, we define $C_{r}(X Y)$ to measure the causality strength between $X$ and $Y$.
$C_{r}(X \rightarrow Y)=\left(\frac{1}{M} \sum_{x_{i} \in Z_{x}} \min _{y \in Z_{x}} V_{r}\left(x_{i}, y\right)\right)^{-1}$
where
$V_{r}(x, y)=\left\{\begin{array}{l}\frac{S(x)}{S(x, y)} \sqrt{\frac{1}{N-1} \sum_{y_{i} \in Z_{y}, y_{i} \notin y}\left(\frac{S_{t}(x, y_{i})-\frac{S(x) \cdot S(y, y)}{N-1}}{S(x)-S_{t}(x, y)}\right)^{\frac{2}{2}}}, N>2 \\ \alpha \frac{S(x)-S_{t}(x, y)}{S(x)}, N=2\end{array}\right.$

Since the scoring function $C_{r}$ is for the discrete random noise model, the definition of $C_{r}$ is mainly to measure the degree of fitting the variables $X$ and $Y$ to the discrete random noise model. The higher the degree of fitting the model is, the stronger the causality and the greater the value of $C_{r}$ is. On the other hand, the lower the degree of fitting is, the smaller the $C_{r}$ value is. The function $V_{r}(x, y)$ computes the degree of fitting for the discrete random noise model when $X=x, f(x)=y$, and the smaller the value of $V_{r}$, the higher the degree of fit.

The Bayesian network is represented by $G=(V, E)$. $V$ represents the set of nodes and $E$ represents the set of directed edges. Let $\operatorname{card}(E)$ denote the number of edges in set $E$, and then define the Bayesian network scoring

function $S_{c}$ as shown in (...), where $\lambda$ and $\beta$ are adjustable parameters.
$\operatorname{Sc}(G)=\left(\lambda e^{\beta \operatorname{card}(E)}\right)^{-1} \sum_{e \in E} C_{r}(e)$
The Bayesian network is constructed by discrete causal inference method. Its main purpose is to make the constructed Bayesian network show good causality, so the network scoring function $S_{c}$ measures the causality of the whole network.

The definition of the function $S_{c}$ consists of two parts, the right side of the cumulative part calculates causality relevance score of each edge, and then computes the sum, giving an overall causal evaluation of the network. In the definition formula, the left part of the accumulated symbol is an adjustment item which decreases with the increase of the number of edges in the network. The significance of the adjustment is that the number of edges in the network should not be excessive to prevent overfitting.

### 3.2 BDCI Bayesian network construction

BDCI has two main operations, one is to use the discrete causal inference algorithm to analyze the causality between each pair of nodes, and the other is to add causal edges to the Bayesian network. Before the construction of the network, the causal relationship and direction between the nodes is analyzed by the discrete causal inference algorithm. Through causal analysis, we can filter out the weaker edges in the network and determine the edges with strong causal connection, which narrows the possible network search space. After obtaining the set of candidate edges using discrete causal analysis, each side of the set of candidate edges is scored using the causal relevance scoring function. The higher the score, the greater the causal association. Then, from the candidate set, a Bayesian network is constructed which maximizes the Bayesian network scoring function $S_{c}$ so that the entire network exhibits good causality.

The discrete causal analysis subroutine in the BDCI algorithm is shown in (Algorithm 1). In this subroutine, for each pair of different node combinations in the node set $V$, the discrete causal inference algorithm is called to analyze the causal relationship between the pair of nodes. If there is no causal association between the pairs of nodes, the nodes are not connected with edges when constructing the network. If there is causal relationship between the pair of nodes, the directed edges represented by the causal direction between the nodes are added to the candidate edges of the network. At the same time calculate the causal relationship between the node pairs using (40) and add the corresponding relation between the relevance score and the directed edge to the weight set $W$ for subsequent algorithm calls.

Algorithm 1 Subroutine of BDCI algorithm: discrete causal analysis

Input: Node set $V$, data set $D$.
Output: Weighted set $W$, made up of candidate edges and its corresponding causal association score.
1: Let $W=\{ \}$
2: for Combination of two different nodes $v_{i}, v_{j}$ in $V$ do
3: Determine causality between $v_{i}$ and $v_{j}$ using discrete causal inference algorithm.
4: if There is causality between $v_{i}$ and $v_{j}$ then
5: if Can not determine causal direction then
6: $\quad$ Append $\left(v_{i} \rightarrow v_{j}, C_{r}\left(v_{i} \rightarrow v_{j}\right)\right)$ and $\left(v_{j} \rightarrow v_{i}, C_{r}\left(v_{j} \rightarrow v_{i}\right)\right)$ to $W$.
7: else if $v_{i} \rightarrow v_{j}$ then
8: $\quad$ Append $\left(v_{i} \rightarrow v_{j}, C_{r}\left(v_{i} \rightarrow v_{j}\right)\right)$ to $W$.
9: else
10: $\quad$ Append $\left(v_{i} \rightarrow v_{j}, C_{r}\left(v_{i} \rightarrow v_{j}\right)\right)$ to $W$.
11: end if
12: else
13: $\quad$ Continue.
14: end if
15: end for
return $W$
Algorithm 2 shows the network initialization algorithm based on the greedy principle. The algorithm starts from a Bayesian network with no edges and then adds edges with the highest causal associative score and meets the Bayesian network requirements at the same time. The process of adding edges to the network is repeated until the network score reaches the maximum, or all edges in the weight set $W$ have been traversed out of date, and the algorithm stops and returns the current Bayesian network $G$ and its network scoring Score. In addition to requiring the Bayesian network to be an acyclic graph, it also adds restrictions on node in-degree in the network initialization algorithm. Algorithm 3 is a complete BDCI Bayesian network construction process. The algorithm first calls the discrete causal analysis subroutine to obtain the weight set $W$ containing all candidate edges, and then invokes the network initialization algorithm based on the greedy principle to obtain an initial Bayesian network $G_{0}$. Then, the simulated annealing algorithm is implemented to adjust the initialized Bayesian network $G_{0}$. The algorithm will iterate through the simulated annealing process until the current temperature $T_{0}$ reaches the "Termination temperature" $T_{\mathrm{e}} n d$. In each iteration, an edge $e_{i j}$ is randomly selected from the weight set $W$, and if $e_{i j}$ is in the current network, $e_{i j}$ is deleted; On the other hand, if $e_{i j}$ is not in the current network and $e_{i j}$ is added to the network without loops and does not violate the indegree limit, $e_{i j}$ is added to the current network. If the Score ${ }^{\prime}$ is greater than or equal to Score $e_{1}$ of the previous iteration, then the current network is accepted as the new solution $G_{1}$; if Score ${ }^{\prime}$ is less than Score $e_{1}$, then the probability of

accepting the current network as the new solution $G_{1}$ is $\exp \left(\left(\operatorname{Score}^{\prime}-\operatorname{Score}_{1}\right) / T_{0}\right)$. After the simulated annealing process, the network scores of Bayesian networks $G_{0}$ and $G_{1}$ are compared and the Bayesian network with higher score is returned as the final solution.
Algorithm 2 Network initialization algorithm
Input: Node set $V$, weight set $W$, in-degree limit $n_{0}$.
Output: Bayesian network: $G=(V, E)$, Score of $G$.
Let $G=(V, E=\{ \}), W_{0}=W$, Score $=0$, Score $^{\prime}=$ 0 .
2: while $W_{0}$ is not empty do
Take out the element $w_{m n}$ with highest association score from the $W_{0}$ and remove $w_{m n}$.
4: $\quad$ Add the corresponding edge $e_{m n}$ the set $E$, and get the new network $G$.
if $G$ has a ring or $G^{\prime} s$ in-degree is greater than $n_{0}$ then
6: $\quad$ Remove $e_{m n}$ from $E$. Continue.
8: else
Calculate $G^{\prime} s$ Score, let $\operatorname{Score}^{\prime}=\operatorname{Sc}(G)$.
10: $\quad$ if Score ${ }^{\prime}$ Score then
Let Score $=$ Score $^{\prime}$.
12: $\quad$ Continue.
else
14: $\quad$ Remove $e_{m n}$ from $E$. Break.
16: end if
18: end if
end whilereturn $G$ and Score.

### 3.3 Extended BDCI Bayesian network construction

BDCI Bayesian network construction algorithm is mainly based on the causality between nodes to construct Bayesian network, so that the network reflects a good cause and effect. If there is a situation that multiple reason nodes lead to one result node, then the BDCI algorithm will be difficult to achieve good results. In order to cope with this situation, BDCI algorithm needs to be extended.

Assume that there are $n+1$ nodes in the network, and these nodes are denoted as node $e_{1}, \ldots$, node $e_{n}$, node $e_{n+1}$, and these nodes have the values of $n s 1, \ldots, n s_{n}, n s_{n+1}$ respectively. Let the causality is from (node $e_{1}, \ldots$, node $e_{n}$ ) to node $e_{n+1}$. To some extent, node $e_{1}, \ldots$, node $e_{n}$ can be combined into a node, and the combined nodes have $\Pi_{i=1}^{n} n s_{i}$ values. Each value of node $e_{n+1}$ corresponds to each value combination of the $n$ nodes, so that the causality between multiple nodes can be transformed into a two-node causal relationship between the composite node and node node $e_{n+1}$, which can be causally analyzed using the discrete causal inference algorithm.

Algorithm 3 BDCI Bayesian Network Construction Algorithm
Input: Node set $V$, weight set $W$, in-degree limit $n 0$.
Output: Bayesian network: $G=(V, E)$. Bud:17
Call the discrete causal analysis subroutine to get the weight set $W$.
Call the Bayesian network initialization algorithm, obtain the initial network $G_{0}=\left(V, E_{0}\right)$ and score of $G_{0}:$ Score $_{0}$.
3: Initializing cooling rate Rate, current temperature $T_{0}$, termination temperature $T_{\text {end }}$, let $G_{1}=G_{0}, G_{t}=$ $\left(V, E_{t}\right)=G_{0}$, Score $^{\prime}=0$, Score $_{1}=$ Score $_{0}$.
while $T_{0}>T_{\text {end }}$ do
Let $G_{t}=\left(V, E_{t}\right)=G_{1}$.
6: $\quad$ Randomly select an edge $e_{i} j$ from the weight set $W$. if $e_{i} j$ is contained in $E_{t}$ then
Remove $e_{i} j$ from $E_{t}$.
9: else
Add $e_{i j}$ to $E_{t}$ to obtain a new network $G_{t}$. end if
12: if $G$ has a ring or $G^{\prime} s$ in-degree is greater than $n_{0}$ then

## Continue.

else
15: $\quad$ Calculate the score of $G_{t}$ such that Score $^{\prime}=$ $\operatorname{Sc}\left(G_{t}\right)$.
if Score ${ }^{\prime} \operatorname{Score}_{1}$ then
Let Score $_{1}=$ Score $^{\prime}, G_{1}=G_{t}$.
18: else
Accept Score $_{1}=$ Score $^{\prime}$ with the probability $\exp \left(\left(\right.\right.$ Score $\left.^{\prime}-\right)$ Score $_{1}$ ) $/ T_{0}$ ). end if
21: $\quad T_{0}=$ Rate $\cdot T_{0}$.
end if
end while
24: if Score $_{1}>$ Score $_{0}$ then return $G_{1}$. else
return $G_{0}$.
end if
The main idea of the extended BDCI Bayesian network construction algorithm is to add a certain number of composite nodes on the basis of BDCI algorithm, use the discrete causal inference algorithm to analyze the causality between the composite nodes and other nodes. Considering the complexity of the extended BDCI algorithm, the causality between the composite nodes is not analyzed in the algorithm. However, for causality between the composite nodes, it can be split into the causality composite node and single node. Therefore, the extended BDCI algorithm is still useful for causality decision between multi nodes.

The main difference between the extended BDCI algorithm and the BDCI algorithm is the discrete causal

analysis subroutine.In the extended BDCI algorithm, the causality between the single node and the composite node is also analyzed in addition to analyzing the causal relationship between single nodes. In the extended BDCI algorithm, $n_{0}$ is also used to denote the network in-degree constraint, and the composite node in the algorithm consists of $n_{0}$ nodes at most. When there is a causality between a single node and a composite node, a single node and each node that makes up the composite node are connected in causal direction, and then all of the connected edges are treated as a single "candidate" to the weight set $W$, and the weight of the candidate edge is calculated by the function $C_{r}$. The complete discrete causal analysis subroutine of extended BDCI algorithm is shown in Algorithm 4, where $u_{j}=\left(b_{1}, \ldots, b_{d}\right)$ represents the combined node $u_{j}$ composed of nodes $b_{1}, \ldots, b_{d}$. In the third loop, when $d=$ $1, u_{j}$ actually represents a single node, but for the sake of simplicity of writing, it will be treated as a composite node, but the composition node consists of only one node.

```
Algorithm 4 Subroutine of extended BDCI algorithm:
discrete causal analysis
Input: Node set \(V\), data set data, in-degree limit \(n_{0}\).
Output: Weighted set \(W\), made up of candidate edges and
    its corresponding causal association score.
    Let \(W=\{ \}\).
    for Any node \(v_{i}\) in the set \(V\) do
        for \(d=1\) to \(n_{0}\) do
        for Composite node \(u_{j}=\left(b_{1}, \ldots, b_{d}\right)\) randomly
    composed of \(d\) nodes except for \(v_{i}\) do
            Determine causality between \(v_{i}\) and \(u_{j}\)
    using discrete causal inference algorithm.
            if There is causality between \(v_{i}\) and \(u_{j}\) then
                if Can not determine causal direction
    then
    8: \(\quad\) Append \(\left(\left(v_{i} \rightarrow b_{1}, \ldots, v_{i} \rightarrow b_{d}\right)\right.\),
    \(\left.C_{r}\left(v_{i} \rightarrow u_{j}\right)\right)\) and \(\left(\left(b_{1} \rightarrow v_{i}, \ldots, b_{d} \rightarrow v_{i}\right), C_{r}\left(u_{j} \rightarrow\right.\right.
    \(\left.v_{i}\right)\right)\) to \(W\).
                else if \(v_{i} \rightarrow v_{j}\) then
                    Append \(\left(\left(v_{i} \rightarrow b_{1}, \ldots, v_{i} \rightarrow b_{d}\right)\right.\)
    \(C_{r}\left(v_{i} \rightarrow u_{j}\right)\) ) to \(W\).
                else
            12: \(\quad\) Append \(\left(\left(b_{1} \rightarrow v_{i}, \ldots, b_{d} \rightarrow v_{i}\right)\right.\),
    \(C_{r}\left(u_{j} \rightarrow v_{i}\right)\) ) to \(W\).
                end if
                else
                    Continue.
16: end if
            end for
            end for
    end for
    return \(W\).
```

![img-0.jpeg](img-0.jpeg)

Fig. 1 Ratio of effective causal inference for irreversible model

The network initialization process and the simulated annealing process of the extended BDCI algorithm are similar to the BDCI algorithm. The only difference is that, since the composite node is actually composed of multiple nodes, the candidate edge composed of the composite node and a single node is actually composed of multiple edges. However, in joining and deleting the candidate edge, all these edges are considered as a whole. When joining the network, make sure that the added edge does not overlap with the existing edge in the network. When deleting, pay attention to distinguish the edge having the composite node and the edge having the single node.

## 4 Experiments and alarm data causality analysis

In order to verify the general applicability of the causal direction determination criteria, several simulations will be performed in this section. Each simulation experiment will be repeated according to the data set length of the variable, and then the results of the experiment statistics. First, based on the analysis of section $4, f$ is bijective and the model is irreversible. We obtained experimental results shown in Fig. 1.
![img-1.jpeg](img-1.jpeg)

Fig. 2 Ratio of effective causal inference for reversible model

Fig. 3 Comparison of different method
![img-2.jpeg](img-2.jpeg)
$X$ is data set length, $Y$ is ratio of effective causal reference. As can be seen from Fig. 1, with the data set length increases, the effective inference tends to be $100 \%$. In the low-dimension, the inference criterion have certain degree of error, but the proportion of error is not very big. Therefore, the experimental results in Fig. 1 show that the criterion can be used to deduce the causal direction correctly when $f$ is bijective and the model is irreversible.

Figure 2 shows an experiment in which the model tends to be reversible. Similarity, $X$ is data set length, $Y$ is ratio of effective causal reference. In addition to maintaining the experiment $f$ bijective conditions, the experiment added $p_{x}\left(x_{i}\right) \approx 1 / M$ conditions and make model reversible. From the experimental results in Fig. 2, it can be seen that when the model is reversible, the proportion decreases compared to Fig. 1. And there is a tendency of decreasing proportion with the increase of the dimension. Therefore, it is difficult to distinguish the causal direction by using the criterion of discrete stochastic noise model in reversible situation. This also confirms the effect of reversibility on the ability of model causal inference.

To illustrate the inference effect of DCMND on nominal data, we use the additive noise model with the causal direction $X \rightarrow Y$ to generate data. That is, the cause is X and effect is Y , and the model form is
$Y=f(X)+N, X \perp N$, in which $f$ is a causal function, $N$ is additive noise, and additive noise and $X$ are independent. Following [7], we make X satisfy the following distributions, using independently generated uniform noise:

1. uniform from $\{1, \ldots, L\}$,
2. binomial with parameters $(n, p)$,
3. geometric with parameter $p$,
4. hypergeometric with parameters $(M, K, N)$,
5. poisson with parameter $\lambda$,
6. multinomial with parameters $\theta$
7. negative binomial with parameters $(n, p)$.

We chose parameters of the distributions randomly for each model class. The model parameter is the same as the paper [7]. We compare the percentage of correct decisions using different method. In Fig. 3, EA: Expert analysis, DCMND: Discrete Causal Model for Nominal Data, CISC [7]:Causal Inference by Stochastic Complexity, DANM [8]:Additive Noise Models for Discrete Variables, CIEDC [9]:Causal Inference Method via Estimating Distance Correlations. We show the accuracy on 7 samples of different model class. We can see that the DCMND, CISC and DANM are highly on the cause-effect pairs compared with CIEDC.

Table 2 Causality in alarm data attributes


![img-3.jpeg](img-3.jpeg)

Fig. 4 Different Bayesian networks constructed on the alarm data

In the process of telecom network system operation, some abnormalities and faults often occur. In order to monitor the fault, often there is management system to monitor these anomalies, and feedback the corresponding alarm data to the system administrator. Through analyzing the alarm data, we can dig out some causality among alarms, so that we can analyze the mechanism of alarm. The alarm data used in this section is provided by China Mobile.

The NMS system of China Mobile Corporation monitors the multiple devices of the company. When the device has an alarm (such as process CPU alarm, host memory threshold alarm, etc.), the system will feedback the corresponding alarm data. In the China Mobile Corporation network management system, a large number of alarm data related to equipment failure are collected. Through analysis it is found that there is a strong causal relationship between alarms of these data. There are 7 different alarm variables: 1. severity, 2. device name, 3. IP address, 4. processing state, 5. shutdown reason, 6. alarm classification, 7. alarm type. Our task is to analyze the causality between alarm variables.
Based on domain knowledge and expert analysis, it can be determined that there are at least a few distinct causality in the mobile alarm data set, as shown in in Table 2, which reflects the real causality in the alarm dataset.

There is a strong causality between the attributes in the dataset. Therefore, the BDCI algorithm and the extended BDCI algorithm can be used to construct the Bayesian network.

Figure 4 shows the Bayesian network constructed by the BDCI algorithm, the extended BDCI algorithm, the K2 algorithm, and the MCMC algorithm for the mobile alarm data set. Compared with the knowledge given by the experts, it can be found that the four algorithms construct the network to find out the causality between IP address and device name. BDCI, extended BDCI and MCMC algorithms can find out the causality $7 \rightarrow 1,2 \rightarrow 7$. The K2 algorithm also finds the association between them, but gives the wrong direction. The network constructed by the MCMC algorithm indicates that there is an association between 1 and 4 , but there is no strong causality between the two. The network constructed by BDCI algorithm can not give $7 \rightarrow 6$. This is mainly because the networks constructed from K2 and extended BDCI algorithm can be seen that it is more likely $\{2,7\} \rightarrow 6$, a multi-node decision single-node causal relationship, while the BDCI algorithm is not good at finding the causal relationship between multiple variables.

Table 3 shows the comparison between network structure in Fig. 4 and real causality. We can see that the extended BDCI algorithm get most well-judged edges. BDCI can find our edges, but 3 edges have wrong directions. MCMC has more superfluous edges than other methods. In general, the networks constructed by the extended BDCI algorithm have stronger causal explanatory properties.

## 5 Conclusions

The paper defines discrete causal model and introduces a new noise variable restriction conditions which are more suitable for causality analysis of nominal data. The discrete causal method is proposed for nominal data. The paper also presents complete BDCI and extended BDCI Bayesian network construction algorithm, which shows good effect in the alarm classification. However, DCMND

Table 3 Comparison between network structure in Fig. 4 and real casuality


has certain requirements on noise variables. In solving practical problems, the noise variable may not meet this requirement, which will reduce the effectiveness of the method. Therefore, we need to relax the restrictions on noise variables and give a more general causality analysis method in the future work. In addition, the complexity of the extended BDCI algorithm is relatively high. So in the following work, we need to study how to discover the causality among the variables in the network more effectively, and propose more efficient algorithms.

Acknowledgments The research reported here was supported by the National Natural Science Foundation of China under contract number NSFC61572279.
