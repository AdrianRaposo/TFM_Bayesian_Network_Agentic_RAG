# Article 

## Long- and Medium-Term Financial Strategies on Equities Using Dynamic Bayesian Networks

Karl Lewis ${ }^{1}$ (D) Mark Anthony Caruana ${ }^{1}$ (D) and David Paul Suda ${ }^{\circ, 1}$ (D)

## check for updates

Citation: Lewis, K.; Caruana, M.A.; Suda D. Long- and Medium-Term Financial Strategies on Equities Using Dynamic Bayesian Networks. AppliedMath 2024, 4, 843-855. https://doi.org/10.3390/ appliedmath4030045

Academic Editor: Tommi Sottinen
Received: 28 April 2024
Revised: 21 June 2024
Accepted: 24 June 2024
Published: 3 July 2024

## (0)

Copyright: (c) 2024 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

Department of Statistics and Operations Research, Faculty of Science, University of Malta, 2080 Msida, Malta; karl.lewis.17@um.edu.mt (K.L.); mark.caruana@um.edu.mt (M.A.C.)

* Correspondence: david.suda@um.edu.mt; Tel.: +356-9986-9884
${ }^{\dagger}$ These authors contributed equally to this work.


#### Abstract

Devising a financial trading strategy that allows for long-term gains is a very common problem in finance. This paper aims to formulate a mathematically rigorous framework for the problem and compare and contrast the results obtained. The main approach considered is based on Dynamic Bayesian Networks (DBNs). Within the DBN setting, a long-term as well as a shortterm trading strategy are considered and applied on twelve equities obtained from developed and developing markets. It is concluded that both the long-term and the medium-term strategies proposed in this paper outperform the benchmark buy-and-hold (B\&H) trading strategy. Despite the clear advantages of the former trading strategies, the limitations of this model are discussed along with possible improvements.


Keywords: finance; dynamic Bayesian networks; trading strategies; equities

## 1. Introduction

In this paper, Dynamic Bayesian Networks (DBNs) are used to study the problem of obtaining and testing a financial strategy whose return is higher than the buy and hold strategy for a given equity. A Bayesian Network (BN) is a graphical and compact representation of a joint probability density function (PDF) that makes use of conditional independence and can be used to model a system under one time instance. DBNs extend the BN to more than one time period, which is to say that DBNs are a temporally driven extension of BNs.

Some benefits of using DBNs over other models, such as basic time series models, are the following. Firstly, DBNs have the capacity to incorporate what are known as hidden (or latent) variables, which either govern, or are thought to govern, the observations of the observable random variable. These hidden variables are random variables whose true value cannot be measured directly, sometimes due to instrumental inadequacies, and other times simply because the existence of these variables is hypothesized. Examples of such hidden variables are the intelligence of an individual (which cannot be measured precisely using any instrument) or the state (bull or bear) of a financial market (whose existence itself is hypothetical). Secondly, since they are an offshoot of BNs, DBNs allow for compact representations of an otherwise possibly cumbersome joint distribution. Russell and Norvig [1] argue that due to conditional independence, representing a joint distribution as a DBN may eliminate any redundant terms, which, in turn, also makes parameter estimation simpler. Murphy [2] state that another benefit of DBNs is the ease with which variations to the model at hand can be introduced. DBNs can be used to alternatively represent both basic Hidden Markov Models (HMMs), and HMMs with variations, such as HMMs with a mixture-of-Gaussian outputs, Auto-regressive HMMs, Input-Output HMMs and Hierarchical HMMs. DBNs can also be used to represent Kalman Filter Models where, contrary to HMMs, the hidden state is continuous rather than discrete. Lastly, DBNs also have the capacity to answer questions about different types of reasoning or inference, such

as diagnostic inference (from effects to causes), causal inference (from causes to effects), intercausal inference (between causes of the same effect), and mixed inference (a mixture of any two of the above types of inference).

In this research paper, we use the price-earnings (PE) ratio in the models discussed. In the literature, various papers can be found which apply the said PE ratio to examine investment strategies. Most notably, one can mention Basu [3]. This ratio has also been used in a vast range of literature including that of Lleo [4] and Angelini [5]. Chang and Tian [6] also use BNs to model the qualitative and quantitative relationships between several variables that affect the dynamics of the S\&P 500 stock index, with the aim of optimizing trading decisions, namely when to open a short position and when to invest in a long position. Damiano et al. [7] base their work on a previous study, that of Tayal [8], which employs HHMMs to analyze financial data. The results obtained by Tayal are reproduced in Damiano et al.'s paper, and further insight is given. Damiano et al. [7] conclude that probabilistic inference allows the identification of two distinct states in high-frequency data that are mainly marked by buying and selling pressure.

Historically, Paul Dagum is thought to have kick-started the development of DBNs in the early 1990s, namely, in the work by Dagum et al. [9] in 1992 and by Dagum et al. [10] in 1995. Ever since, DBNs have been used in various areas, namely, in finance and economics. However, other areas include (but are not limited to) speech recognition (Murphy [2], Zweig, Russell [11], and Nefian et al. [12]), biology(Yao et al. [13], Raval et al. [14], Murphy and Mian [15]), robotics (Prembida et al. [16], Patel et al. [17]), image processing (Delage et al. [18]), and fault detection (Cozar et al. [19]). Parameter estimation techniques of DBNs are discussed by Benhamou et al. [20], whereas Murphy [21] works on the theoretical foundations of DBNs.

The rest of this paper is structured as follows. Section 2 introduces the theoretical underpinnings of DBNs. In Section 3, DBNs are applied to twelve equities from both developed and developing markets, and the return on investment is presented. The reason for considering both developed and developing markets is to test model robustness under different economic conditions and growth patterns. Finally, in the concluding section, the key points and results obtained are highlighted.

# 2. Theoretical Framework 

This model is based on the work by Wang [22] and exploits two behavioral finance phenomena-behavioral volatility and mean reversion. Behavioral volatility refers to the phenomenon whereby market-related events such as irrational trades executed by inexperienced traders cause the trading price of a stock to deviate away from its 'true' value. Events like these continually affect market price either until the effects caused cancel each other out, or until rational investors balance these effects out with their rational trades. This phenomenon is known as mean reversion. The theory of mean reversion is applicable not only to the price of a stock, but to any price-related metric, such as the price-earnings (PE) ratio (share price divided by the earnings per share). As a result, one can decide to buy (or sell) a stock only when some metric that follows the mean reversion theory is far away from the mean, knowing that the 'true' value of the metric will be returned to at some point in the future.

A Directed Graphical Model (DGM) is a representation of a probabilistic model that uses conditional independence assumptions through a directed graph, where the vertices (note that the terms "state", "random variable", "node" and "vertex" may be used interchangeably) of the graph represent random variables and the arcs represent conditional dependence between pairs of random variables. An arc from vertex $A$ to vertex $B$ represents the statement " $A$ causes $B$ " (Murphy [2]). DGMs are convenient due to their compactness in exhibiting some joint probability distribution-for $N$ binary random variables, the general closed form of the joint probability distribution of these random variables may need $O\left(2^{N}\right)$ parameters, whereas the graphical model may give the same information using fewer parameters due to the omission of terms via conditional independence statements.

A Bayesian Network is a DGM that represents a set of random variables $X_{1}, \ldots, X_{n}$ and their conditional dependencies through a directed acyclic graph (DAG), denoted by $G=(\mathcal{V}, \mathcal{E})$. Each vertex in $\mathcal{V}$ represents a random variable $X_{i}$, and each directed edge in $\mathcal{E}$ represents the conditional dependence a random variable has on another. A conditional probability distribution is associated to each node $X_{i}$, and the joint probability distribution on the vertex set $\mathcal{V}$ is given by $\mathbb{P}[\mathcal{V}]=\prod_{i=1}^{n} \mathbb{P}\left[X_{i} \mid\right.$ parents $\left.\left(X_{i}\right)\right]$. The generalization of a BN to multiple time slices gives rise to the definition of a DBN. A Dynamic Bayesian Network is defined to be a pair $\left(B_{0}, B_{\rightarrow}\right)$, where $B_{0}$ is the BN representing the prior probability (or the initial state probability), that is, the probability distribution of the random variables at time 0 , and $B_{\rightarrow}$ is a two-slice temporal BN which describes transition probabilities from time $t-1$ to time $t$ for any node $X$ in the vertex set $\mathcal{V}$ of the $\operatorname{DAG} G=(\mathcal{V}, \mathcal{E})$, denoted by $\mathbb{P}\left[X_{t} \mid X_{t-1}\right]$. The joint probability distribution of the vertex set $\mathcal{V}$ over all time slices is given by:

$$
\mathbb{P}[\mathcal{V}]=\mathbb{P}\left[\mathcal{V}_{0}\right] \mathbb{P}\left[\mathcal{V}_{1: T}\right]=\prod_{X_{i} \in \mathcal{V}} \mathbb{P}\left[X_{i_{0}} \mid\right. \text { parents }\left(X_{i_{0}}\right)] \prod_{t=1}^{T} \prod_{X_{i} \in \mathcal{V}} \mathbb{P}\left[X_{i_{t}} \mid\right. \text { parents }\left(X_{i_{t}}\right)]
$$

where $\mathcal{V}_{t_{1}: t_{2}}$ refers to the set of all vertices indexed from time $t_{1}$ up to time $t_{2}$. A DBN can be parametrized by its transition matrix $\mathbb{A}_{t}=\mathbb{P}\left[X_{t}=j \mid X_{t-1}=i\right]$, and its prior distribution $\pi(i)=\mathbb{P}\left[X_{1}=i\right]$. If the transition probabilities are assumed to be constant for all time slices $\left(\mathbb{A}_{t}=\mathbb{A}\right)$, then they are said to be homogeneous and have a much more compact joint distribution function. When representing a DBN pictorially, two or three time slices are typically shown-the initial time slice and the subsequent one or two-since its structure is assumed to replicate throughout time.

An important property of DAGs is that "nodes can be ordered such that parents come before children. This is called a topological ordering, and it can be constructed from any DAG." (Murphy [23]). Given such an ordering, the Ordered Markov property (or Local Markoo property) is defined to be the "assumption that a node only depends on its parents, not on all its predecessors in the ordering" (Murphy [23]). This assumption is in fact a generalization of the Markov property for Markov chains.

# 2.1. Inference for DBNs 

The objective in inference is to infer the value of the latent states given the observations of the observable states, that is, inferring the marginals $\mathbb{P}\left[X_{t}=i \mid y_{1: \tau}\right]$. If $\tau=t$, the process is known as filtering (or 'now-casting'); if $\tau>t$, then this is smoothing; and if $\tau<t$, then one would be performing prediction (or forecasting). A commonly used inference algorithm for DBNs is the forward-backward algorithm. In this algorithm, dynamic programming is implemented through two steps, known as passes, that run in a counter-directional manner-one runs forward in time, whilst the other runs backward. Note that it is assumed that the transition probability matrix, emission probability matrix, and prior probabilities are all known. In the forward pass, the value of $\alpha_{t}(i):=\mathbb{P}\left[X_{t}=i \mid y_{1: t}\right]$ is found in a recursive manner. In the backward pass, the value of $\beta_{t}(i):=\mathbb{P}\left[y_{t+1: T} \mid X_{t}=i\right]$ is also found recursively but moving in counter chronological order (from time $T$ to time 2). After the forward and backward passes are complete, the value for $\gamma_{t}(i):=\mathbb{P}\left[X_{t}=i \mid y_{1: T}\right]$ can finally be obtained:

$$
\gamma_{t}(i)=\mathbb{P}\left[X_{t}=i \mid y_{1: T}\right]=\frac{\mathbb{P}\left[y_{t+1: T} \mid X_{t}=i\right] \mathbb{P}\left[X_{t}=i \mid y_{1: t}\right]}{\mathbb{P}\left[y_{1: T}\right]}
$$

where $\mathbb{P}\left[y_{1: T}\right]=\prod_{t=1}^{T} c_{t}$.

### 2.2. Learning DBNs

In this context, learning refers to the parameter estimation process. In parameter estimation, learning can be tackled either through a Maximum Likelihood (ML) approach or through the Maximum A Posteriori (MAP) approach. If using ML, then the data are used to obtain parameter estimates via the solution of the optimization problem:

$\theta_{M L}^{*}=\arg \max _{\theta}\{\mathbb{P}[Y \mid \theta]\}=\arg \max _{\theta}\{\log \mathbb{P}[Y \mid \theta]\}$, where $\theta$ is the set of parameters to be estimated. Typically, $\theta$ contains the transition matrix and parameters pertaining to the probability distribution used in the emission matrix. On the other hand, if using the MAP method, the optimization problem above is adjusted slightly to become $\theta_{M A P}^{*}=$ $\arg \max _{\theta}\{\log \mathbb{P}[Y \mid \theta]+\log \mathbb{P}[\theta]\}$, where $\mathbb{P}[\theta]$ is the parameter prior distribution. The approach to solving the optimization problems above is through an adaptation of the Expectation-Maximization (EM) algorithm known as the Baum-Welch algorithm, proven to give a local optimum to the optimization problems above (Baum et al. [24], Dempster et al. [25]). It uses the forward-backward algorithm as a subroutine. Hence, in cases where the model parameters are unknown, the Baum-Welch algorithm is first used to estimate (or learn) the model parameters. Then, the forward-backward algorithm is used to infer the posterior marginals.

# 2.3. Application of Theory 

The main hypothesis of the model is that the stock price of a firm is not always equal to the firm's 'true' intrinsic value. Utilizing the phenomena of behavioral volatility and mean reversion, temporary effects that cause stock metrics to deviate from their 'true' value are classified into two: short-term effects (length of a few days) and medium-term effects (length of several weeks).

It is hypothesized that the fundamental value of a company $i$ at time $t$, denoted by $P_{i, t}^{*}$, is directly proportional to its annual earnings at time $t$, denoted by $E_{i, t}$, with the fundamental $P E$ ratio, denoted by $P E_{i, t}^{*}$, acting as the constant of proportionality:

$$
P_{i, t}^{*}=\left(P E_{i, t}^{*}\right)\left(E_{i, t}\right)
$$

On the other hand, the observed PE ratio (openly available on the public domain), denoted by $P E_{i, t}$, is given by $P E_{i, t}=\frac{P_{i, t}}{E_{i, t}}$ where $P_{i, t}$ denotes the actual trading price of a company $i$ at time $t$.

Note that from this point onward, the index $i$ is dropped, as the analysis on stocks is performed univariately. The model equation that results from the above is given by:

$$
\begin{aligned}
P_{t}=P_{t}^{*}\left(1+Z_{t}\right)\left(1+\varepsilon_{t}\right) & \Longrightarrow y_{t}=\ln \left[P E^{*}\left(1+Z_{t}\right)\right]+\ln \left[1+\varepsilon_{t}\right] \\
& \Longrightarrow y_{t}=\ln \left[P E^{*}\left(1+Z_{t}\right)\right]+\varepsilon_{t}
\end{aligned}
$$

where $y_{t}=\ln \left[\frac{P_{t}}{E_{t}}\right],\left\{Z_{t}\right\}_{t \in \mathbb{N}}$ is a discrete-time Markov chain modeling the medium-term noise effects, and $\varepsilon_{t} \sim \mathcal{N}\left(0, \sigma^{2}\right)$ is a random variable modeling the short-term noise effects. Due to the above model equation, the model used is only applicable for firms that have positive earnings throughout the period under study. Furthermore, one must note that $y_{t}$ is an observable quantity (since both $P_{t}$ and $E_{t}$ are); however, $P E^{*}$ and $Z_{t}$ are not. It is assumed that both $Z_{t}$ and $P E^{*}$ are discrete-valued; hence, $Z_{t} \in\left\{a_{1}, \ldots, a_{M}\right\}$ and $P E^{*} \in\left\{b_{1}, \ldots, b_{N}\right\}$ where $M$ and $N$ represent the number of possible latent states of $Z_{t}$ and $P E^{*}$, respectively.

The conditional independence assumptions used in this model are presented next:

$$
\forall t \geq 1, \forall i, j \geq 1
$$

$$
\begin{array}{ll}
Z_{t} \perp P E^{*} \mid \varnothing \\
Z_{i} \perp Z_{j} \mid Z_{k} & \exists k \in\{i+1, \ldots, j-1\} \\
y_{i} \perp Z_{j} \mid Z_{k}, P E^{*} & \exists k \in\{i, \ldots, j-1\} \text { or } k \in\{j+1, \ldots, i\} . \\
y_{i} \perp y_{j} \mid Z_{k}, P E^{*} & \exists k \in\{i, \ldots, j\}
\end{array}
$$

For $t \geq 2$ and $r, s \in\{1, \ldots, M\}$, the matrix $\mathbb{W}:=\left[w_{r s}\right]_{M \times M}$ is defined to be the transition probability matrix, where

$$
w_{r s}:=\mathbb{P}\left[Z_{t}=a_{s} \mid Z_{t-1}=a_{r}\right]
$$

Note that $w_{r s} \in[0,1]$ and $\sum_{s=1}^{M} w_{r s}=1$. For $t \geq 1, m \in\{1, \ldots, M\}$ and $n \in\{1, \ldots, N\}$, the matrix $\mathbb{D}_{t}:=\left[d_{m n}\left(y_{t}\right)\right]_{M \times N}$ is defined to be the emission probability matrix at time $t$, where

$$
d_{m n}\left(y_{t}\right):=\mathbb{P}\left[y_{t} \mid Z_{t}=a_{m}, P E^{*}=b_{n}\right]
$$

where $d_{m n}\left(y_{t}\right) \sim \mathcal{N}\left(\ln \left[b_{n}\left(1+a_{m}\right)\right], \sigma^{2}\right)$. For $m \in\{1, \ldots, M\}$ and $n \in\{1, \ldots, N\}$, the vectors $\boldsymbol{u}:=\left(u_{m}\right)_{m \in \mathbb{N}}$ and $\boldsymbol{v}:=\left(v_{n}\right)_{n \in \mathbb{N}}$ are defined to be the initial probability vectors that contain the initial probability distributions, where

$$
u_{m}:=\mathbb{P}\left[Z_{1}=a_{m}\right] ; \quad v_{n}:=\mathbb{P}\left[P E^{*}=b_{n}\right]
$$

Note that $u_{m}, v_{n} \in[0,1], \sum_{m=1}^{M} u_{m}=1$ and $\sum_{n=1}^{N} v_{n}=1$. These prior distributions serve to incorporate any expert knowledge that the researcher may have available. A graphical representation of the model described above can be found in Figure 1.

Having laid out the principles needed for inference, the aim of the analysis now makes itself clearer-that of inferring the value of $P E^{*}$ so as to estimate the fundamental price of a stock and formulate a trading strategy based on this knowledge. Furthermore, inferring the value of $Z_{t}$ is also useful, as it can be used to test an alternative trading strategy. In this context, the data used will be split into a training and a test set. The set of model parameters is given by $\theta=\left\{\mathbb{W}, \boldsymbol{u}, \boldsymbol{v}, \sigma^{2}\right\}$. The space of possible parameters is given by the set:

$$
\Theta=\left\{\theta: u_{m}, v_{n}, w_{r s} \in[0,1], \sum_{m=1}^{M} u_{m}=1, \sum_{n=1}^{N} v_{n}=1, \sum_{s=1}^{M} w_{r s}=1, \sigma^{2}>0\right\}
$$

![img-0.jpeg](img-0.jpeg)

Figure 1. Representation of the model described above using a DBN, where $y_{t}$ is observable and $P E^{*}$ and $Z_{t}$ are latent, discrete variables.

Learning and inference then follow. Since the parameters in $\theta$ are unknown, they will first need to be estimated (learning procedure). As mentioned, the algorithm used to obtain the MAP estimates is the Baum-Welch algorithm. After the unknown model parameters are estimated, the forward-backward algorithm is used on the parameter estimates to infer the constant value of $P E^{*}$ for the training set and test set, and to infer the value of $Z_{t}$ through smoothing for the training set, and through filtering for the test set:

- Filtering probabilities: $\mathbb{P}\left[Z_{T}, P E^{*} \mid y_{1: T}, \theta\right]$;
- Smoothing probabilities: $\mathbb{P}\left[Z_{t}, P E^{*} \mid y_{1: T}, \theta\right]$, where $t \in\{1, \ldots, T-1\}$.


# 2.4. Inference with Known Parameters 

As per the forward pass of the forward-backward algorithm, the following definitions are made and equations derived for the filtering probabilities:

$$
\forall t \in\{1, \ldots, T\}, m \in\{1, \ldots, M\}, n \in\{1, \ldots, N\}
$$

$$
\begin{gathered}
\alpha_{t m n}:=\mathbb{P}\left[Z_{t}=a_{m}, P E^{*}=b_{n} \mid y_{1: t}, \theta\right] \\
\alpha_{1 m n}=\frac{d_{m n}\left(y_{1}\right) u_{m} v_{n}}{\sum_{m^{\prime}=1}^{M} \sum_{n^{\prime}=1}^{N} d_{m^{\prime} n^{\prime}}\left(y_{1}\right) u_{m^{\prime}} v_{n^{\prime}}} \\
\alpha_{t m n}=\frac{d_{m n}\left(y_{t}\right) \sum_{i=1}^{M} \mathbb{P}\left[Z_{t-1}=a_{i}, P E^{*}=b_{n} \mid y_{1: t-1}\right] w_{m i}}{c_{t}} \\
c_{t}:=\sum_{m=1}^{M} \sum_{n=1}^{N} d_{m n}\left(y_{t}\right) \sum_{i=1}^{M} \mathbb{P}\left[Z_{t-1}=a_{i}, P E^{*}=b_{n} \mid y_{1: t-1}\right] w_{m i}
\end{gathered}
$$

After defining the filtering probabilities, the smoothing probabilities are given through the estimate denoted by $\gamma_{t m n}$ :

$$
\begin{gathered}
\forall t \in\{1, \ldots, T-1\}, m \in\{1, \ldots, M\}, n \in\{1, \ldots, N\} \\
\gamma_{t m n}:=\mathbb{P}\left[Z_{t}=a_{m}, P E^{*}=b_{n} \mid y_{1: T}\right]
\end{gathered}
$$

Next, as per the backward pass of the forward-backward algorithm, the definition of $\beta_{t m n}$ is to be given so as to be able to obtain the values for $\gamma_{t m n}$ :

$$
\beta_{t m n}:=\frac{\mathbb{P}\left[y_{t+1: T} \mid Z_{t}=a_{m}, P E^{*}=b_{n}\right]}{\mathbb{P}\left[y_{t+1: T} \mid y_{1: t}\right]}=\frac{\mathbb{P}\left[y_{t+1: T} \mid Z_{t}=a_{m}, P E^{*}=b_{n}\right]}{\prod_{t^{\prime}=t+1}^{T} c_{t^{\prime}}}
$$

Therefore, as per the forward-backward algorithm, one has:

$$
\gamma_{t m n}=\alpha_{t m n} \beta_{t m n}
$$

What remains to be derived are the expressions for $\beta_{t m n} \forall t \in\{1, \ldots, T-1\}$ :

$$
\beta_{(T-1) m n}=\frac{\beta_{(T-1) m n}^{\prime}}{c_{T}}=\frac{\sum_{i=1}^{M} d_{i n}\left(y_{T}\right) w_{i m}}{\sum_{m=1}^{M} \sum_{n=1}^{N} c_{T}}
$$

For $\beta_{t m n} \forall t \in\{1, \ldots, T-2\}, m \in\{1, \ldots, M\}, n \in\{1, \ldots, N\}$ :

$$
\beta_{t m n}^{\prime}=\sum_{i=1}^{M} \beta_{(t+1) i n}^{\prime} d_{i n}\left(y_{t+1}\right) w_{i m} ; \quad \beta_{t m n}=\frac{\sum_{i=1}^{M} \beta_{(t+1) i n} d_{i n}\left(y_{t+1}\right) w_{i m}}{c_{t+1}}
$$

With expressions found for both the smoothing and filtering probabilities, the most probable values of the latent variables $P E^{*}$ and $Z_{t}$ are found through marginalization:

$$
\overline{P E^{*}}=\underset{b_{n}}{\arg \max }\left\{\sum_{m=1}^{M} \mathbb{P}\left[Z_{t}=a_{m}, P E^{*}=b_{n} \mid y_{1: T}\right]\right\}=\underset{b_{n}}{\arg \max }\left\{\sum_{m=1}^{M} \gamma_{t m n}\right\}
$$

To find the estimate $\widehat{Z}_{t}$ for the latent state $Z_{t}$, smoothing is used on the training , set whilst filtering is applied on the test set:

$$
\begin{aligned}
& \widehat{Z}_{t}=\underset{a_{m}}{\arg \max }\left\{\sum_{n=1}^{N} \gamma_{t m n}\right\} \quad \forall t \in\left\{t: y_{t} \in \mathbb{X}_{\text {train }}\right\} ; \\
& \widehat{Z}_{t}=\underset{a_{m}}{\arg \max }\left\{\sum_{n=1}^{N} \alpha_{t m n}\right\} \quad \forall t \in\left\{t: y_{t} \in \mathbb{X}_{\text {test }}\right\} .
\end{aligned}
$$

where $\mathbb{X}_{\text {train }}$ and $\mathbb{X}_{\text {test }}$ denote the training set and test set, respectively.

# 2.5. Learning Unknown Parameters 

The optimization problem in learning is given by $\widehat{\theta_{M A P}}=\underset{\theta \in \Theta}{\arg \max }\left\{\mathbb{P}\left[\theta \mid y_{1}^{\top}\right]\right\}$ and is solved using the Baum-Welch algorithm (note that in the forthcoming expressions, $\theta$ should technically be written with a hat superscript (') since it is a set of parameter estimates):

1. Set $j=1$.
2. Set $\theta^{(1)}-\theta^{(0)}>\delta$
3. while $\theta^{(j)}-\theta^{(j-1)}>\delta$ do
(i) Calculate probabilities $\mathbb{P}\left[Z_{t}=a_{m}, P E^{*}=b_{n} \mid y_{1: T}, \theta^{(j)}\right] \forall t, m, n$
(ii) Solve the constrained maximization problem

$$
\widehat{\theta^{(j+1)}}=\underset{\theta \in \Theta}{\arg \max }\left\{Q\left(\theta ; \theta^{(j)}\right)+\ln \mathbb{P}[\theta]\right\}
$$

where $Q\left(\theta ; \theta^{(j)}\right)=\mathbb{E}_{Z_{1: T}, P E^{*} \mid y_{1: T}, \theta^{(j)}}\left[\ln \mathbb{P}\left[y_{1: T}, Z_{1: T}, P E^{*} \mid \theta\right]\right]$.
(iii) Increment $j$

An expression in closed form can be obtained for $Q\left(\theta ; \theta^{(j)}\right)$ by using the smoothing probabilities:

$$
\begin{aligned}
& Q\left(\theta ; \theta^{(j)}\right)=\sum_{t=1}^{T-1} \sum_{m=1}^{M} \sum_{n=1}^{N} \alpha_{t m n}^{(j-1)} \beta_{t m n}^{(j-1)} \ln \left[d_{m n}\left(y_{t}\right)\right]+\sum_{m=1}^{M} \sum_{n=1}^{N} \alpha_{T m n}^{(j-1)} \ln \left[d_{m n}\left(y_{T}\right)\right] \\
& +\sum_{t^{\prime}=2}^{T-1} \sum_{i, m=1}^{M} \sum_{n=1}^{N} \beta_{t m n}^{(j-1)}\left(\frac{d_{m n}^{(j-1)}\left(y_{t}\right)}{c_{t}^{(j-1)}}\right) w_{m i}^{(j-1)} \alpha_{(i-1) i n}^{(j-1)} \ln \left[w_{m i}\right] \\
& +\sum_{i, m=1}^{M} \sum_{n=1}^{N}\left(\frac{d_{m n}^{(j-1)}\left(y_{T}\right)}{c_{T}^{(j-1)}}\right) w_{m i}^{(j-1)} \alpha_{T-1, i n}^{(j-1)} \ln \left[w_{m i}\right] \\
& +\sum_{m=1}^{M} \sum_{n=1}^{N} \alpha_{1 m n}^{(j-1)} \beta_{1 m n}^{(j-1)}\left(\ln \left[u_{m}\right]+\ln \left[v_{n}\right]\right) .
\end{aligned}
$$

In the argument of the maximization problem above, $\ln \mathbb{P}[\theta]$ is the logarithm of the prior distribution $\mathbb{P}[\theta]$, where $\mathbb{P}[\theta]=\mathbb{P}[\boldsymbol{u}] \mathbb{P}[\boldsymbol{v}] \mathbb{P}[\mathbb{W}] \mathbb{P}\left[\sigma^{2}\right]$ since the independence of priors is assumed. Within this prior distribution, two types of expert knowledge can be included-prior knowledge of the ballpark value of $P E^{*}$ and prior knowledge of the persistence of the medium-term noise effects, which are encoded through the prior $\mathbb{P}[\boldsymbol{v}]$ and the prior $\mathbb{P}[\mathbb{W}]$, respectively.

The prior for the vector $\boldsymbol{v}$ is represented by the Dirichlet distribution:

$$
f(\boldsymbol{v})=\frac{\Gamma\left(k_{1}+k_{2}+\ldots+k_{N}\right)}{\Gamma\left(k_{1}\right) \Gamma\left(k_{2}\right) \ldots \Gamma\left(k_{N}\right)} \prod_{n=1}^{N} v_{n}^{k_{n}-1}
$$

The values $k_{n}$ for $n \in\{1, \ldots, N\}$ intuitively correspond to the degree of belief an expert has on the event that $b_{n}$ is the 'true' value for $P E^{*}$. For this analysis, $k_{n}=1 \quad \forall n$. The prior for the matrix $\mathbb{W}$ is also derived from the Dirichlet distribution $f(\mathbb{W})=\prod_{m=1}^{M} f\left(\boldsymbol{w}_{m}\right)$, where $\boldsymbol{w}_{m}=\left(w_{i m}\right)_{i=1, \ldots, M}$ and

$$
f\left(\boldsymbol{w}_{\boldsymbol{m}}\right)=\frac{\Gamma\left(k_{1 m}+k_{2 m}+\ldots+k_{M m}\right)}{\Gamma\left(k_{1 m}\right) \Gamma\left(k_{2 m}\right) \ldots \Gamma\left(k_{M n}\right)} \prod_{m=1}^{M} w_{i m}^{k_{i m}-1}
$$

Since $\mathbb{W}$ is the transition matrix for the hidden Markov chain $\left\{Z_{t}\right\}_{t \in \mathbb{N}}$, then the diagonal entries of $\mathbb{W}$ represent the probability that a particular state persists (stays as is in the next time point). The greater the value of $Z_{t}$ (or, correspondingly, $a_{m}$ ), the greater that

state's persistence. In this analysis, the off-diagonal entries (the reader is suggested to refer to Wang [22] for more information on the values of the off-diagonals) are set to 0 .

Taking all the above into consideration, the logarithm of the prior $\mathbb{P}[\theta]$ becomes

$$
\ln \mathbb{P}[\theta]=\ln \mathbb{P}[\mathbb{W}]+\ln \mathbb{P}[\boldsymbol{v}]=\sum_{m=1}^{M} \sum_{i=1}^{M}\left(k_{i m}-1\right) \ln \left[w_{i m}\right]+\sum_{n=1}^{N}\left(k_{n}-1\right) \ln \left[v_{n}\right]+s_{1}
$$

where $s_{1}=\ln \left[\frac{\Gamma\left(k_{1}+k_{2}+\ldots+k_{N}\right)}{\Gamma\left(k_{1}\right) \Gamma\left(k_{2}\right) \ldots \Gamma\left(k_{N}\right)}\right]+\ln \left[\frac{\Gamma\left(k_{1 m}+k_{2 m}+\ldots+k_{M m}\right)}{\Gamma\left(k_{1 m}\right) \Gamma\left(k_{2 m}\right) \ldots \Gamma\left(k_{M n}\right)}\right]$.
The constant $s_{1}$ is only included for completeness' sake-it is rendered irrelevant when maximizing in the Baum-Welch algorithm.

With the priors set, the constrained optimization problem is now fully defined. Note that only the equality constraints in (6) will be considered, as the inequality constraints will end up being satisfied still. Therefore, the method of Lagrange multipliers can be used to solve this optimization problem. The expressions for the estimators of the four variables in question are given below:

$$
\begin{gathered}
\widehat{u_{m}^{(j)}}=\sum_{n=1}^{N} \alpha_{1 m n}^{(j-1)} \beta_{1 m n}^{(j-1)} \\
\widehat{v_{n}^{(j)}}=\frac{\sum_{m=1}^{M} q_{1 m n}^{(j)}\left(Z_{1}, P E^{*}\right)+\left(k_{n}-1\right)}{1+\sum_{n^{\prime}=1}^{N}\left(k_{n^{\prime}}-1\right)}=\frac{\sum_{m=1}^{M} \alpha_{1 m n}^{(j-1)} \beta_{1 m n}^{(j-1)}+\left(k_{n}-1\right)}{1+\sum_{n^{\prime}=1}^{N}\left(k_{n^{\prime}}-1\right)} \\
\widehat{w_{m i}^{(j)}}=-\frac{\sum_{t^{\prime}=2}^{T} \sum_{n=1}^{N} q_{t^{\prime}, m, i, n}^{(j)}\left(Z_{t^{\prime}}, Z_{t^{\prime}-1}, P E^{*}\right)+\left(k_{m i}-1\right)}{\sum_{t^{\prime}=2}^{T} \sum_{m=1}^{M} \sum_{n=1}^{N} q_{t^{\prime}, m, i, n}^{(j)}\left(Z_{t^{\prime}}, Z_{t^{\prime}-1}, P E^{*}\right)+\sum_{m^{\prime}=1}^{M}\left(k_{m^{\prime} i}-1\right)} \\
=\frac{\omega_{t t, m, i, n}^{(j)}}{\sum_{m^{\prime}=1}^{M} \omega_{t t, m, i, n}^{(j)}}
\end{gathered}
$$

where

$$
\begin{gathered}
\omega_{t t, m, i, n}^{(j)}=\sum_{t^{\prime}=2}^{T-1} \sum_{n=1}^{N} \beta_{t^{\prime} m n}^{(j-1)}\left(\frac{d_{m n}^{(j-1)}\left(y_{t^{\prime}}\right)}{c_{t^{\prime}}^{(j-1)}}\right) w_{m i}^{(j-1)} \alpha_{t^{\prime}-1, i, n}^{(j-1)} \\
+\sum_{n=1}^{N}\left(\frac{d_{m n}^{(j-1)}\left(y_{T}\right)}{c_{T}^{(j-1)}}\right) w_{m i}^{(j-1)} \alpha_{(T-1) i n}^{(j-1)}+\left(k_{m i}-1\right) \\
\widehat{\sigma^{2^{(j-1)}}}=\frac{\sum_{t=1}^{T-1} \sum_{m=1}^{M} \sum_{n=1}^{N} \alpha_{t m n}^{(j-1)} \beta_{t m n}^{(j-1)}\left(y_{t}-\ln \left[b_{n}\left(1+a_{m}\right)\right]\right)^{2}}{\sum_{t=1}^{T-1} \sum_{m=1}^{M} \sum_{n=1}^{N} \alpha_{t m n}^{(j-1)} \beta_{t m n}^{(j-1)}+\sum_{m=1}^{M} \sum_{n=1}^{N} \alpha_{T m n}^{(j-1)}} \\
+\frac{\sum_{m=1}^{M} \sum_{n=1}^{N} \alpha_{T m n}^{(j-1)}\left(y_{T}-\ln \left[b_{n}\left(1+a_{m}\right)\right]\right)^{2}}{\sum_{t=1}^{T-1} \sum_{m=1}^{M} \sum_{n=1}^{N} \alpha_{t m n}^{(j-1)} \beta_{t m n}^{(j-1)}+\sum_{m=1}^{M} \sum_{n=1}^{N} \alpha_{T m n}^{(j-1)}}
\end{gathered}
$$

# 3. Methodology of Analysis and Results 

Twelve equities were chosen to be analyzed in this paper (see Table 1)—nine from a developed market (US) and three from emerging markets (Brazil and China). The training set contains data from the 1st of January 2011 to the 31st of December 2019 whilst the test set contains data from the 1st of January 2020 to the 30st of September 2020. Using a 12-month rolling Sharpe ratio as a point of reference, all equities displayed average or above average returns (with respect to an S\&P benchmark) in the test period, with the exception of the two underperforming Brazilian equities [26]. Two datasets were collected for each stock for the above-mentioned period-daily price data and quarterly earnings per share data.

Table 1. Table of results, showing the return on investment as a percentage of the sum invested. Values in brackets are negative.


After the preliminary data cleaning and preparation phase, the initial values of vectors $\boldsymbol{a}=\left(a_{m}\right)$ and $\boldsymbol{b}=\left(b_{n}\right)$ are set next. Priors of the vector $\boldsymbol{v}$ and matrix $\mathbb{W}$ are set as discussed earlier; the prior for $\boldsymbol{u}$ is set to be the discrete uniform distribution, and the initial value of $\sigma^{2}$ is set to 5 . Parameter learning is then performed before inference of the latent states $\widehat{P E^{\mathrm{x}}}$ and $\widehat{Z}_{t}$. Simulation of the trading strategies follows. The trading strategies proposed by Wang [22] and used in this paper will be compared to the benchmark B\&H strategy. For both the proposed trading strategies, let $I_{t}$ denote the amount of cash available at time $t$; let $N_{t}$ denote the units of a security held at time $t$; let $T_{\text {train }}$ represent the size of the training set; and let $T$ represent the size of the dataset (sum of sizes of training and test sets). Both the long-term and the medium-term trading strategies can be described by three possible courses of action (labeled (i), (ii) and (iii) below) at time $t$; that is, courses of action (i) through (ii) are common to both trading strategies:
(i) If $P E_{t} \leq A_{t}(1-T r)$ and $I_{t}>0$, then buy the security using all the available cash $I_{t}$. Hence, $N_{t+1}=\frac{I_{t}}{P_{t}}$ and $I_{t+1}=0$.
(ii) If $P E_{t} \geq A_{t}(1+T r)$ and $I_{t}=0$, then sell all the units held $N_{t}$. Hence, $N_{t+1}=0$ and $I_{t+1}=P_{t} N_{t}$.
(iii) If neither (i) or (ii) are satisfied, do not execute any trades. Hence, $N_{t+1}=N_{t}$ and $I_{t+1}=I_{t}$.

Note that $A_{t}$ is considered to be a baseline and depends on the trading strategy. The threshold value $\operatorname{Tr} \in(0,1)$ acts as a sensitivity gauge defining how much the investor wants to allow $P E_{t}=\frac{P_{t}}{P_{t}}$ to deviate from the baseline $A_{t}$ before triggering a particular course of action in the trading strategies. This is clear from how the courses of action are defined. The total profit at the end of the trading period is given by $I_{T}+P_{T} N_{T}-I_{T_{\text {train }}+1}$.

The first trading strategy is the so-called 'long-term strategy', where trading is performed with respect to the constant value of $\widehat{P E^{\mathrm{x}}}$, so $A_{t}=\widehat{P E^{\mathrm{x}}}$. The alternative strategy is the 'medium-term strategy', where trading is performed with respect to the dynamic values of $\widehat{P E^{\mathrm{x}}}\left(1+\widehat{Z}_{t}\right)$, where each $\widehat{Z}_{t}$ is dynamically estimated through filtering. Therefore, for the medium-term strategy, $A_{t}=\widehat{P E^{\mathrm{x}}}\left(1+\widehat{Z}_{t}\right)$.

The results on the BLK and ITUB stocks are presented in graphical detail in this paper. Firstly, the long-term strategy on the BLK stock data suggests that the investor buys the stock at time point $2265=T_{\text {train }}+1$ and holds the stock for the rest of the period. Clearly, this strategy coincides with the B\&H strategy and, as a result, profit from the long-termstrategy would be equal to profit from the B\&H strategy which is equal to USD1298.04, equaling a $12.98 \%$ return on the initial investment of USD 10,000. On the other hand, the

medium-term strategy suggests that the investor buys the stock at time points 2265, 2301 and 2437, sells it at time points 2289 and 2431, and holds it for the rest of the time points. This would yield a profit of USD 3391.85; equalling a $33.92 \%$ return on the initial investment of USD 10,000 in the nine-month period that the testing set covers. This means that the medium-term strategy beats the B\&H strategy by $20.94 \%$. Figure 2 illustrates the long-term strategy and medium-term strategy.

Next, we discuss the ITUB stock data. The long-term strategy suggests that the investor buys the stock at time point 2308 and holds the stock for the rest of the period. Implementing this strategy would yield a loss of USD 3986.16, which equates to a $39.86 \%$ loss on the initial investment of USD 10,000. The buy-and-hold strategy, however, would yield a greater loss of USD 5584.67. In contrast, the medium-term strategy suggests that the investor buys the stock at time points 2313, 2315 and 2376, sells it at time points 2314 and 2372, and holds it for the rest of the time points. This would actually yield a profit of USD 909.81. Although this is only a $9.1 \%$ return on the initial investment of USD 10,000, the medium-term strategy provides the investor with a strategy whereby he or she can make a profit in a period when the stock is actually crashing. Figure 3 illustrates the long-term strategy and medium-term strategy, respectively.
![img-1.jpeg](img-1.jpeg)

Figure 2. Simulated strategies for the BLK stock.
More generally, we see in Table 1 that the medium strategy has been consistently superior (for various thresholds) for BLK, COST, HD, ITUB, MA, MCD, NVDA and UNH. For ITUB, for all but one threshold, the strategy turns a slight profit even though a loss is registered for other strategies. The long-term strategy has been consistently superior for NTES and SAN. Neither strategy has offered any advantages on ADBE, while for AAPL, the success of the medium-term strategy depends on the choice of threshold. Some further analysis on these results will be given in the conclusion.
![img-2.jpeg](img-2.jpeg)

Figure 3. Simulated strategies for the IUTB stock.

# 4. Conclusions 

Through the use of DBNs, the model for stock movement by Wang [22] is built for our existing equity dataset. This model includes two latent states-one modeling the medium-term noise effects, and the other modeling the true fundamental PE ratio of a firm, the latter assumed to be constant throughout the period under study. The forwardbackward algorithm and the Baum-Welch algorithm (variant of the EM algorithm) are used to perform parameter learning and inference. Based on this fitted model, the longand medium-term strategies are applied to the twelve stocks studied here, with nine of these stocks trading on a developed market and the rest on an emerging one. Overall, both the long-term and medium-term strategies outperform the benchmark B\&H trading strategy 17 and 31 times, respectively, out of a total of 48 experiment runs for each strategy (four for each of the twelve stocks). The strategies proposed by Wang only lose out to the $\mathrm{B} \& \mathrm{H}$ four and three times, respectively. Furthermore, the outperformance of these trading strategies is substantial. Whereas the average profit over all stocks when using the $\mathrm{B} \& \mathrm{H}$ is $20.83 \%$, the average profit over all stocks and over all thresholds for the long-term strategy is $27.78 \%$ and that for the medium-term strategy is $36.23 \%$. Lastly, it results that these trading strategies provide the investor with trading suggestions that, in certain cases, can even turn a loss under the B\&H strategy into a profit as was shown to be the case for the ITUB stock. This stock was on a downfall, but the medium-term strategy still yielded a profit on the sum invested. All these results are as displayed in Table 1.

As with any statistical model, the model implemented in this work has room for improvement. The first and most significant limitation is the fact that only stocks that had a positive EPS during the period under study can be modeled by the model. This is due to the left-hand side of the model equation, that is, Equation (1). In certain times such as during pandemics or during recessions, it may be considerably difficult to find a firm who has not registered a loss in at least one quarter for the period under study. A second limitation is the lack of use of expert knowledge. In real-world investing, expertise in the field is considered highly valuable, and only seasoned investors are generally advised to trade actively. Since the model in this paper allows for the incorporation of expert knowledge, it is indeed a limitation that such knowledge is not made use of. Another limitation related to expert knowledge is the limitation that no trading fees or commissions are taken into account in this analysis. Although the proposed model allows for commissions to be considered in the trading strategies, no knowledge on the actual values of fees or commissions charged was available at the time of writing, and hence, such expenses could not be taken into account. It is well known that certain trading fees can sometimes tally up when executing numerous trades in such a way that a profit can turn into a loss when these fees are brought to the fore, which would make the buy-and-hold strategy more profitable.

Improvements on the above-mentioned limitations can add value to the model and should be considered in future works. In addition, another improvement that makes the model here more applicable in real-life scenarios is the incorporation of some variable that measures the liquidity of a stock. This is because the suggestions provided by the trading strategies on when to buy and sell a stock are rendered useless if the stock itself is not liquid. Prices may change by the time the stock becomes liquid enough for an actual trading opportunity to arise, and if the price changes significantly, that obviously renders the suggestion itself useless. In this study, liquidity was not envisaged to be of concern since all 12 stocks considered are large-cap stocks.

The choice of historical data used is always an important decision due to the fact that the length of the time series plays a major role. In principle, longer time series are preferred to shorter ones, but if the historical data contain changes in regime, this may inhibit the model in its forecasting performance. Furthermore, future regime changes that may occur in the test period may also impact the model's forecasting performance.

Finally, other improvements that can be implemented in future studies are further and deeper experimentation and testing, and the possibility of short-selling stock. To begin with, experimentation at a portfolio level can be implemented with the stocks studied here

to understand how the profits change when a group of stocks are considered together-for instance, samples of nine stocks from the twelve studied here can be taken to form portfolios, and the 'optimal' portfolio can be identified. Apart from this, more time can be spent on cross-validation in future studies to further improve on the suggestions provided by the trading strategies in this work. Also, the properties of all the estimators used could be derived in future works, to better understand their behavior. Finally, this strategy does not allow the short-selling of stock; extensions to the model which allow for this could be proposed.

Author Contributions: All the three authors worked equally hard to write this paper. K.L. took care of the coding in MATLAB and the results section, M.A.C. and D.P.S. took care of the methodology and theoretical content of the paper. All authors have read and agreed to the published version of the manuscript.

Funding: This research received no external funding.
Data Availability Statement: All the data is openly available from Yahoo Finance at https:// finance.yahoo.com/.

Conflicts of Interest: The authors declare no conflicts of interest.

# Abbreviations 

The following abbreviations are used in this manuscript:

