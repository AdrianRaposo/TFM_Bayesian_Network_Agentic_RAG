# Research Article 

## NML Computation Algorithms for Tree-Structured Multinomial Bayesian Networks

Petri Kontkanen, Hannes Wettig, and Petri Myllymäki<br>Complex Systems Computation Group (CoSCo), Helsinki Institute for Information Technology (HIIT), P.O. Box 68 (Department of Computer Science), FIN-00014 University of Helsinki, Finland

Received 1 March 2007; Accepted 30 July 2007
Recommended by Peter Grünwald
Typical problems in bioinformatics involve large discrete datasets. Therefore, in order to apply statistical methods in such domains, it is important to develop efficient algorithms suitable for discrete data. The minimum description length (MDL) principle is a theoretically well-founded, general framework for performing statistical inference. The mathematical formalization of MDL is based on the normalized maximum likelihood (NML) distribution, which has several desirable theoretical properties. In the case of discrete data, straightforward computation of the NML distribution requires exponential time with respect to the sample size, since the definition involves a sum over all the possible data samples of a fixed size. In this paper, we first review some existing algorithms for efficient NML computation in the case of multinomial and naive Bayes model families. Then we proceed by extending these algorithms to more complex, tree-structured Bayesian networks.

Copyright © 2007 Petri Kontkanen et al. This is an open access article distributed under the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.

## 1. INTRODUCTION

Many problems in bioinformatics can be cast as model class selection tasks, that is, as tasks of selecting among a set of competing mathematical explanations the one that best describes a given sample of data. Typical examples of this kind of problem are DNA sequence compression [1], microarray data clustering [2-4] and modeling of genetic networks [5]. The minimum description length (MDL) principle developed in the series of papers [6-8] is a well-founded, general framework for performing model class selection and other types of statistical inference. The fundamental idea behind the MDL principle is that any regularity in data can be used to compress the data, that is, to find a description or code of it, such that this description uses less symbols than it takes to describe the data literally. The more regularities there are, the more the data can be compressed. According to the MDL principle, learning can be equated with finding regularities in data. Consequently, we can say that the more we are able to compress the data, the more we have learned about them.

MDL model class selection is based on a quantity called stochastic complexity (SC), which is the description length of a given data relative to a model class. The stochastic complexity is defined via the normalized maximum likelihood (NML) distribution [8, 9]. For multinomial (discrete) data,
this definition involves a normalizing sum over all the possible data samples of a fixed size. The logarithm of this sum is called the regret or parametric complexity, and it can be interpreted as the amount of complexity of the model class. If the data is continuous, the sum is replaced by the corresponding integral.

The NML distribution has several theoretical optimality properties, which make it a very attractive candidate for performing model class selection and related tasks. It was originally $[8,10]$ formulated as the unique solution to a minimax problem presented in [9], which implied that NML is the minimax optimal universal model. Later [11], it was shown that NML is also the solution to a related problem involving expected regret. See Section 2 and [10-13] for more discussion on the theoretical properties of the NML.

Typical bioinformatic problems involve large discrete datasets. In order to apply NML for these tasks one needs to develop suitable NML computation methods since the normalizing sum or integral in the definition of NML is typically difficult to compute directly. In this paper, we present algorithms for efficient computation of NML for both one- and multidimensional discrete data. The model families used in the paper are so-called Bayesian networks (see, e.g., [14]) of varying complexity. A Bayesian network is a graphical representation of a joint distribution. The structure of the graph

corresponds to certain conditional independence assumptions. Note that despite the name, having Bayesian network models does not necessarily imply using Bayesian statistics, and the information-theoretic approach of this paper cannot be considered Bayesian.

The problem of computing NML for discrete data has been studied before. In [15] a linear-time algorithm for the one-dimensional multinomial case was derived. A more complex case involving a multidimensional model family, called naive Bayes, was discussed in [16]. Both these cases are also reviewed in this paper.

The paper is structured as follows. In Section 2, we discuss the basic properties of the MDL principle and the NML distribution. In Section 3, we instantiate the NML distribution for the multinomial case and present a linear-time computation algorithm. The topic of Section 4 is the naive Bayes model family. NML computation for an extension of naive Bayes, the so-called Bayesian forests, is discussed in Section 5. Finally, Section 6 gives some concluding remarks.

## 2. PROPERTIES OF THE MDL PRINCIPLE AND THE NML MODEL

The MDL principle has several desirable properties. Firstly, it automatically protects against overfitting in the model class selection process. Secondly, this statistical framework does not, unlike most other frameworks, assume that there exists some underlying "true" model. The model class is only used as a technical device for constructing an efficient code for describing the data. MDL is also closely related to the Bayesian inference but there are some fundamental differences, the most important being that MDL does not need any prior distribution; it only uses the data at hand. For more discussion on the theoretical motivations behind the MDL principle see, for example, $[8,10-13,17]$.

The MDL model class selection is based on minimization of the stochastic complexity. In the following, we give the definition of the stochastic complexity and then proceed by discussing its theoretical properties.

### 2.1. Model classes and families

Let $\mathbf{x}^{n}=\left(x_{1}, \ldots, x_{n}\right)$ be a data sample of $n$ outcomes, where each outcome $x_{j}$ is an element of some space of observations $\mathcal{X}$. The $n$-fold Cartesian product $\mathcal{X} \times \cdots \times \mathcal{X}$ is denoted by $\mathcal{X}^{n}$, so that $\mathbf{x}^{n} \in \mathcal{X}^{n}$. Consider a set $\Theta \subseteq \mathbb{R}^{d}$, where $d$ is a positive integer. A class of parametric distributions indexed by the elements of $\Theta$ is called a model class. That is, a model class $\mathcal{M}$ is defined as

$$
\mathcal{M}=[P(\cdot \mid \boldsymbol{\theta}): \boldsymbol{\theta} \in \Theta]
$$

and the set $\Theta$ is called the parameter space.
Consider a set $\Phi \subseteq \mathbb{R}^{e}$, where $e$ is a positive integer. Define a set $\mathcal{F}$ by

$$
\mathcal{F}=\{\mathcal{M}(\varphi): \varphi \in \Phi\}
$$

The set $\mathcal{F}$ is called a model family, and each of the elements $\mathcal{M}(\varphi)$ is a model class. The associated parameter space is denoted by $\Theta_{\varphi}$. The model class selection problem can now be
defined as a process of finding the parameter vector $\varphi$, which is optimal according to some predetermined criteria. In Sections 3-5, we discuss three specific model families, which will make these definitions more concrete.

### 2.2. The NML distribution

One of the most theoretically and intuitively appealing model class selection criteria is the stochastic complexity. Denote first the maximum likelihood estimate of data $\mathbf{x}^{n}$ for a given model class $\mathcal{M}(\varphi)$ by $\widehat{\boldsymbol{\theta}}\left(\mathbf{x}^{n}, \mathcal{M}(\varphi)\right)$, that is, $\widehat{\boldsymbol{\theta}}\left(\mathbf{x}^{n}, \mathcal{M}(\varphi)\right)=\arg \max _{\boldsymbol{\theta} \in \Theta_{\varphi}}\left[P\left(\mathbf{x}^{n} \mid \boldsymbol{\theta}\right)\right]$. The normalized maximum likelihood (NML) distribution [9] is now defined as

$$
P_{\mathrm{NML}}\left(\mathbf{x}^{n} \mid \mathcal{M}(\varphi)\right)=\frac{P\left(\mathbf{x}^{n} \mid \widehat{\boldsymbol{\theta}}\left(\mathbf{x}^{n}, \mathcal{M}(\varphi)\right)\right)}{\mathcal{C}(\mathcal{M}(\varphi), n)}
$$

where the normalizing term $\mathcal{C}(\mathcal{M}(\varphi), n)$ in the case of discrete data is given by

$$
\mathcal{C}(\mathcal{M}(\varphi), n)=\sum_{\mathbf{y}^{n} \in \mathcal{X}^{n}} P\left(\mathbf{y}^{n} \mid \widehat{\boldsymbol{\theta}}\left(\mathbf{y}^{n}, \mathcal{M}(\varphi)\right)\right)
$$

and the sum goes over the space of data samples of size $n$. If the data is continuous, the sum is replaced by the corresponding integral.

The stochastic complexity of the data $\mathbf{x}^{n}$, given a model class $\mathcal{M}(\varphi)$, is defined via the NML distribution as

$$
\begin{aligned}
& \mathrm{SC}\left(\mathbf{x}^{n} \mid \mathcal{M}(\varphi)\right) \\
& \quad=-\log P_{\mathrm{NML}}\left(\mathbf{x}^{n} \mid \mathcal{M}(\varphi)\right) \\
& \quad=-\log P\left(\mathbf{x}^{n} \mid \widehat{\boldsymbol{\theta}}\left(\mathbf{x}^{n}, \mathcal{M}(\varphi)\right)\right)+\log \mathcal{C}(\mathcal{M}(\varphi), n)
\end{aligned}
$$

and the term $\log \mathcal{C}(\mathcal{M}(\varphi), n)$ is called the (minimax) regret or parametric complexity. The regret can be interpreted as measuring the logarithm of the number of essentially different (distinguishable) distributions in the model class. Intuitively, if two distributions assign high likelihood to the same data samples, they do not contribute much to the overall complexity of the model class, and the distributions should not be counted as different for the purposes of statistical inference. See [18] for more discussion on this topic.

The NML distribution (3) has several important theoretical optimality properties. The first is that NML provides a unique solution to the minimax problem

$$
\min _{\hat{P}} \max _{\mathbf{x}^{n}} \log \frac{P\left(\mathbf{x}^{n} \mid \widehat{\boldsymbol{\theta}}\left(\mathbf{x}^{n}, \mathcal{M}(\varphi)\right)\right)}{\widehat{P}\left(\mathbf{x}^{n} \mid \mathcal{M}(\varphi)\right)}
$$

as posed in [9]. The minimizing $\widehat{P}$ is the NML distribution, and the minimax regret

$$
\log P\left(\mathbf{x}^{n} \mid \widehat{\boldsymbol{\theta}}\left(\mathbf{x}^{n}, \mathcal{M}(\varphi)\right)\right)-\log \widehat{P}\left(\mathbf{x}^{n} \mid \mathcal{M}(\varphi)\right)
$$

is given by the parametric complexity $\log \mathcal{C}(\mathcal{M}(\varphi), n)$. This means that the NML distribution is the minimax optimal universal model. The term universal model in this context means

that the NML distribution represents (or mimics) the behavior of all the distributions in the model class $\mathcal{M}(\varphi)$. Note that the NML distribution itself does not have to belong to the model class, and typically it does not.

A related property of NML involving expected regret was proven in [11]. This property states that NML is also a unique solution to

$$
\max _{g} \min _{q} E_{g} \log \frac{P\left(\mathbf{x}^{n} \mid \widehat{\boldsymbol{\theta}}\left(\mathbf{x}^{n}, \mathcal{M}(\varphi)\right)\right)}{q\left(\mathbf{x}^{n} \mid \mathcal{M}(\varphi)\right)}
$$

where the expectation is taken over $\mathbf{x}^{n}$ with respect to $g$ and the minimizing distribution $q$ equals $g$. Also the maximin expected regret is thus given by $\log \mathcal{C}(\mathcal{M}(\varphi), n)$.

## 3. NML FOR MULTINOMIAL MODELS

In the case of discrete data, the simplest model family is the multinomial. The data are assumed to be one-dimensional and to have only a finite set of possible values. Although simple, the multinomial model family has practical applications. For example, in [19] multinomial NML was used for histogram density estimation, and the density estimation problem was regarded as a model class selection task.

### 3.1. The model family

Assume that our problem domain consists of a single discrete random variable $X$ with $K$ values, and that our data $\mathbf{x}^{n}=\left(x_{1}, \ldots, x_{n}\right)$ is multinomially distributed. The space of observations $\mathcal{X}$ is now the set $\{1,2, \ldots, K\}$. The corresponding model family $\mathcal{F}_{\mathrm{MN}}$ is defined by

$$
\mathcal{F}_{\mathrm{MN}}=\left\{\mathcal{M}(\varphi): \varphi \in \Phi_{\mathrm{MN}}\right\}
$$

where $\Phi_{\mathrm{MN}}=\{1,2,3, \ldots\}$. Since the parameter vector $\varphi$ is in this case a single integer $K$ we denote the multinomial model classes by $\mathcal{M}(K)$ and define

$$
\mathcal{M}(K)=\left\{P(\cdot \mid \boldsymbol{\theta}): \boldsymbol{\theta} \in \Theta_{K}\right\}
$$

where $\Theta_{K}$ is the simplex-shaped parameter space,

$$
\Theta_{K}=\left\{\left(\pi_{1}, \ldots, \pi_{K}\right): \pi_{k} \geq 0, \pi_{1}+\cdots+\pi_{K}=1\right\}
$$

with $\pi_{k}=P(X=k), k=1, \ldots, K$.
Assume the data points $x_{j}$ are independent and identically distributed (i.i.d.). The NML distribution (3) for the model class $\mathcal{M}(K)$ is now given by (see, e.g., $[16,20]$ )

$$
P_{\mathrm{NML}}\left(\mathbf{x}^{n} \mid \mathcal{M}(K)\right)=\frac{\prod_{k=1}^{K}\left(h_{k} / n\right)^{h_{k}}}{\mathcal{C}(\mathcal{M}(K), n)}
$$

where $h_{k}$ is the frequency (number of occurrences) of value $k$ in $\mathbf{x}^{n}$, and

$$
\begin{aligned}
\mathcal{C}(\mathcal{M}(K), n) & =\sum_{\gamma^{n}} P\left(\gamma^{n} \mid \widehat{\boldsymbol{\theta}}\left(\gamma^{n}, \mathcal{M}(K)\right)\right) \\
& =\sum_{h_{1}+\cdots+h_{K}=n} \frac{n!}{h_{1}!\cdots h_{K}!} \prod_{k=1}^{K}\left(\frac{h_{k}}{n}\right)^{h_{k}}
\end{aligned}
$$

To make the notation more compact and consistent in this section and the following sections, $\mathcal{C}(\mathcal{M}(K), n)$ is from now on denoted by $\mathcal{C}_{\mathrm{MN}}(K, n)$.

It is clear that the maximum likelihood term in (12) can be computed in linear time by simply sweeping through the data once and counting the frequencies $h_{k}$. However, the normalizing sum $\mathcal{C}_{\mathrm{MN}}(K, n)$ (and thus also the parametric complexity $\log \mathcal{C}_{\mathrm{MN}}(K, n)$ ) involves a sum over an exponential number of terms. Consequently, the time complexity of computing the multinomial NML is dominated by (14).

### 3.2. The quadratic-time algorithm

In $[16,20]$, a recursion formula for removing the exponentiality of $\mathcal{C}_{\mathrm{MN}}(K, n)$ was presented. This formula is given by

$$
\begin{aligned}
\mathcal{C}_{\mathrm{MN}}(K, n)= & \sum_{r_{1}+r_{2}=n} \frac{n!}{r_{1}!r_{2}!}\left(\frac{r_{1}}{n}\right)^{r_{1}}\left(\frac{r_{2}}{n}\right)^{r_{2}} \\
& \cdot \mathcal{C}_{\mathrm{MN}}\left(K^{*}, r_{1}\right) \cdot \mathcal{C}_{\mathrm{MN}}\left(K-K^{*}, r_{2}\right)
\end{aligned}
$$

which holds for all $K^{*}=1, \ldots, K-1$. A straightforward algorithm based on this formula was then used to compute $\mathcal{C}_{\mathrm{MN}}(K, n)$ in time $\mathcal{O}\left(n^{2} \log K\right)$. See $[16,20]$ for more details. Note that in $[21,22]$ the quadratic-time algorithm was improved to $\mathcal{O}(n \log n \log K)$ by writing (15) as a convolutiontype sum and then using the fast Fourier transform algorithm. However, the relevance of this result is unclear due to severe numerical instability problems it easily produces in practice.

### 3.3. The linear-time algorithm

Although the previous algorithms have succeeded in removing the exponentiality of the computation of the multinomial NML, they are still superlinear with respect to $n$. In [15], a linear-time algorithm based on the mathematical technique of generating functions was derived for the problem.

The starting point of the derivation is the generating function $B$ defined by

$$
B(z)=\frac{1}{1-T(z)}=\sum_{n \geq 0} \frac{n^{n}}{n!} z^{n}
$$

where $T$ is the so-called Cayley's tree function [23, 24]. It is easy to prove (see $[15,25]$ ) that the function $B^{K}$ generates the sequence $\left(\left(n^{n} / n!\right) \mathcal{C}_{\mathrm{MN}}(K, n)\right)_{n=0}^{\infty}$, that is,

$$
\begin{aligned}
B^{K}(z) & =\sum_{n \geq 0} \frac{n^{n}}{n!} \cdot \sum_{h_{1}+\cdots+h_{K}=n} \frac{n!}{h_{1}!\cdots h_{K}!} \prod_{k=1}^{K}\left(\frac{h_{k}}{n}\right)^{h_{k}} z^{n} \\
& =\sum_{n \geq 0} \frac{n^{n}}{n!} \cdot \mathcal{C}_{\mathrm{MN}}(K, n) z^{n}
\end{aligned}
$$

which by using the tree function $T$ can be written as

$$
B^{K}(z)=\frac{1}{(1-T(z))^{K}}
$$

The properties of the tree function $T$ can be used to prove the following theorem.

Theorem 1. The $\mathcal{O}_{\text {MN }}(K, n)$ terms satisfy the recurrence

$$
\mathcal{O}_{M N}(K+2, n)=\mathcal{O}_{M N}(K+1, n)+\frac{n}{K} \cdot \mathcal{O}_{M N}(K, n)
$$

Proof. See the appendix.
It is now straightforward to write a linear-time algorithm for computing the multinomial NML $P_{\text {NML }}\left(\mathbf{x}^{n} \mid\right.$ $\mathcal{M}(K)$ ) based on Theorem 1. The process is described in Algorithm 1. The time complexity of the algorithm is clearly $\mathcal{O}(n+K)$, which is a major improvement over the previous methods. The algorithm is also very easy to implement and does not suffer from any numerical instability problems.

### 3.4. Approximating the multinomial NML

In practice, it is often not necessary to compute the exact value of $\mathcal{O}_{\mathrm{MN}}(K, n)$. A very general and powerful mathematical technique called singularity analysis [26] can be used to derive an accurate, constant-time approximation for the multinomial regret. The idea of singularity analysis is to use the analytical properties of the generating function in question by studying its singularities, which then leads to the asymptotic form for the coefficients. See $[25,26]$ for details.

For the multinomial case, the singularity analysis approximation was first derived in [25] in the context of memoryless sources, and later [20] re-introduced in the MDL framework. The approximation is given by

$$
\begin{aligned}
& \log \mathcal{O}_{\mathrm{MN}}(K, n) \\
& =\frac{K-1}{2} \log \frac{n}{2}+\log \frac{\sqrt{\pi}}{\Gamma(K / 2)}+\frac{\sqrt{2} K \cdot \Gamma(K / 2)}{3 \Gamma(K / 2-1 / 2)} \cdot \frac{1}{\sqrt{n}} \\
& +\left(\frac{3+K(K-2)(2 K+1)}{36}-\frac{\Gamma^{2}(K / 2) \cdot K^{2}}{9 \Gamma^{2}(K / 2-1 / 2)}\right) \cdot \frac{1}{n} \\
& +\mathcal{O}\left(\frac{1}{n^{3 / 2}}\right) .
\end{aligned}
$$

Since the error term of (20) goes down with the rate $\mathcal{O}\left(1 / n^{3 / 2}\right)$, the approximation converges very rapidly. In [20], the accuracy of (20) and two other approximations (Rissanen's asymptotic expansion [8] and Bayesian information criterion (BIC) [27]) were tested empirically. The results show that (20) is significantly better than the other approximations and accurate already with very small sample sizes. See [20] for more details.

## 4. NML FOR THE NAIVE BAYES MODEL

The one-dimensional case discussed in the previous section is not adequate for many real-world situations, where data are typically multidimensional, involving complex dependencies between the domain variables. In [16], a quadratictime algorithm for computing the NML for a specific multivariate model family, usually called the naive Bayes, was derived. This model family has been very successful in practice in mixture modeling [28], clustering of data [16], casebased reasoning [29], classification [30,31], and data visualization [32].

### 4.1. The model family

Let us assume that our problem domain consists of $m$ primary variables $X_{1}, \ldots, X_{m}$ and a special variable $X_{0}$, which can be one of the variables in our original problem domain or it can be latent. Assume that the variable $X_{i}$ has $K_{i}$ values and that the extra variable $X_{0}$ has $K_{0}$ values. The data $\mathbf{x}^{n}=\left(\mathbf{x}_{1}, \ldots, \mathbf{x}_{n}\right)$ consist of observations of the form $\mathbf{x}_{j}=\left(x_{j 0}, x_{j 1}, \ldots, x_{j m}\right) \in \mathcal{X}$, where

$$
\mathcal{X}=\left\{1,2, \ldots, K_{0}\right\} \times\left\{1,2, \ldots, K_{1}\right\} \times \cdots \times\left\{1,2, \ldots, K_{m}\right\}
$$

The naive Bayes model family $\mathcal{F}_{\mathrm{NB}}$ is defined by

$$
\mathcal{F}_{\mathrm{NB}}=\left\{\mathcal{M}(\varphi): \varphi \in \Phi_{\mathrm{NB}}\right\}
$$

with $\Phi_{\mathrm{NB}}=\{1,2,3, \ldots\}^{m+1}$. The corresponding model classes are denoted by $\mathcal{M}\left(K_{0}, K_{1}, \ldots, K_{m}\right)$ :

$$
\mathcal{M}\left(K_{0}, K_{1}, \ldots, K_{m}\right)=\left\{P_{\mathrm{NB}}(\cdot \mid \boldsymbol{\theta}): \boldsymbol{\theta} \in \Theta_{K_{0}, K_{1}, \ldots, K_{m}}\right\}
$$

The basic naive Bayes assumption is that given the value of the special variable, the primary variables are independent. We have consequently

$$
\begin{aligned}
& P_{\mathrm{NB}}\left(X_{0}=x_{0}, X_{1}=x_{1}, \ldots, X_{m}=x_{m} \mid \boldsymbol{\theta}\right) \\
& \quad=P\left(X_{0}=x_{0} \mid \boldsymbol{\theta}\right) \cdot \prod_{i=1}^{m} P\left(X_{i}=x_{i} \mid X_{0}=x_{0}, \boldsymbol{\theta}\right)
\end{aligned}
$$

Furthermore, we assume that the distribution of $P\left(X_{0} \mid \boldsymbol{\theta}\right)$ is multinomial with parameters $\left(\pi_{1}, \ldots, \pi_{K_{0}}\right)$, and each $P\left(X_{i}\right.$ $X_{0}=k, \boldsymbol{\theta}$ ) is multinomial with parameters $\left(\sigma_{i k 1}, \ldots, \sigma_{i k K_{i}}\right)$. The whole parameter space is then

$$
\begin{aligned}
& \Theta_{K_{0}, K_{1}, \ldots, K_{m}} \\
& =\left\{\left(\pi_{1}, \ldots, \pi_{K_{0}}\right),\left(\sigma_{111}, \ldots, \sigma_{11 K_{1}}\right), \ldots,\left(\sigma_{m K_{0} 1}, \ldots, \sigma_{m K_{0} K_{m}}\right)\right. \\
& \pi_{k} \geq 0, \sigma_{i k l} \geq 0, \pi_{1}+\cdots+\pi_{K_{0}}=1 \\
& \left.\sigma_{i k 1}+\cdots+\sigma_{i k K_{i}}=1, i=1, \ldots, m, k=1, \ldots K_{0}\right\}
\end{aligned}
$$

and the parameters are defined by $\pi_{k}=P\left(X_{0}=k\right), \sigma_{i k l}=$ $P\left(X_{i}=l \mid X_{0}=k\right)$.

Assuming i.i.d., the NML distribution for the naive Bayes can now be written as (see [16])

$$
\begin{aligned}
& P_{\mathrm{NML}}\left(\mathbf{x}^{n} \mid \mathcal{M}\left(K_{0}, K_{1}, \ldots, K_{m}\right)\right) \\
& \quad=\frac{\prod_{k=1}^{K_{0}}\left(h_{k} / n\right)^{h_{k}} \prod_{i=1}^{m} \prod_{l=1}^{K_{i}}\left(f_{i k l} / h_{k}\right)^{f_{i k l}}}{\mathcal{O}\left(\mathcal{M}\left(K_{0}, K_{1}, \ldots, K_{m}\right), n\right)}
\end{aligned}
$$

where $h_{k}$ is the number of times $X_{0}$ has value $k$ in $\mathbf{x}^{n}, f_{i k l}$ is the number of times $X_{i}$ has value $l$ when the special variable has value $k$, and $\mathcal{O}\left(\mathcal{M}\left(K_{0}, K_{1}, \ldots, K_{m}\right), n\right)$ is given by (see [16])

$$
\begin{aligned}
& \mathcal{O}\left(\mathcal{M}\left(K_{0}, K_{1}, \ldots, K_{m}\right), n\right) \\
& \quad=\sum_{h_{1}+\cdots+h_{K_{0}}=n} \frac{n!}{h_{1}!\cdots h_{K_{0}}!} \prod_{k=1}^{K_{0}}\left(\frac{h_{k}}{n}\right)^{h_{k}} \prod_{i=1}^{m} \mathcal{O}_{\mathrm{MN}}\left(K_{i}, h_{k}\right)
\end{aligned}
$$

To simplify notations, from now on we write $\mathcal{O}\left(\mathcal{M}\left(K_{0}\right.\right.$, $\left.\left.K_{1}, \ldots, K_{m}\right), n\right)$ in an abbreviated form $\mathcal{O}_{\mathrm{NB}}\left(K_{0}, n\right)$.

1: Count the frequencies $h_{1}, \ldots, h_{K}$ from the data $\mathbf{x}^{n}$
2: Compute the likelihood $P\left(\mathbf{x}^{n} \mid \widehat{\boldsymbol{\theta}}\left(\mathbf{x}^{n}, \mathcal{M}(K)\right)\right)=\prod_{k=1}^{K}\left(h_{k} / n\right)^{h_{k}}$
3: Set $\mathcal{C}_{\mathrm{MN}}(1, n)=1$
4: Compute $\mathcal{C}_{\mathrm{MN}}(2, n)=\sum_{r_{1}+r_{2}=n}\left(n!/ r_{1}!r_{2}!\right)\left(r_{1} / n\right)^{r_{1}}\left(r_{2} / n\right)^{r_{2}}$
5: for $k=1$ to $K-2$ do
6: Compute $\mathcal{C}_{\mathrm{MN}}(k+2, n)=\mathcal{C}_{\mathrm{MN}}(k+1, n)+(n / k) \cdot \mathcal{C}_{\mathrm{MN}}(k, n)$
7: end for
8: Output $P_{\text {NML }}\left(\mathbf{x}^{n} \mid \mathcal{M}(K)\right)=P\left(\mathbf{x}^{n} \mid \widehat{\boldsymbol{\theta}}\left(\mathbf{x}^{n}, \mathcal{M}(K)\right)\right) / \mathcal{C}_{\mathrm{MN}}(K, n)$

Algorithm 1: The linear-time algorithm for computing $P_{\text {NML }}\left(\mathbf{x}^{n} \mid \mathcal{M}(K)\right)$.

### 4.2. The quadratic-time algorithm

It turns out [16] that the recursive formula (15) can be generalized to the naive Bayes model family case.

Theorem 2. The terms $\mathcal{C}_{N B}\left(K_{0}, n\right)$ satisfy the recurrence

$$
\begin{aligned}
\mathcal{C}_{N B}\left(K_{0}, n\right)= & \sum_{r_{1}+r_{2}=n} \frac{n!}{r_{1}!r_{2}!}\left(\frac{r_{1}}{n}\right)^{r_{1}}\left(\frac{r_{2}}{n}\right)^{r_{2}} \\
& \cdot \mathcal{C}_{N B}\left(K^{*}, r_{1}\right) \cdot \mathcal{C}_{N B}\left(K_{0}-K^{*}, r_{2}\right)
\end{aligned}
$$

where $K^{*}=1, \ldots, K_{0}-1$.
Proof. See the appendix.
In many practical applications of the naive Bayes, the quantity $K_{0}$ is unknown. Its value is typically determined as a part of the model class selection process. Consequently, it is necessary to compute NML for model classes $\mathcal{M}\left(K_{0}, K_{1}, \ldots, K_{m}\right)$, where $K_{0}$ has a range of values, say, $K_{0}=$ $1, \ldots, K_{\max }$. The process of computing NML for this case is described in Algorithm 2. The time complexity of the algorithm is $\mathcal{O}\left(n^{2} \cdot K_{\max }\right)$. If the value of $K_{0}$ is fixed, the time complexity drops to $\mathcal{O}\left(n^{2} \cdot \log K_{0}\right)$. See [16] for more details.

## 5. NML FOR BAYESIAN FORESTS

The naive Bayes model discussed in the previous section has been successfully applied in various domains. In this section we consider, tree-structured Bayesian networks, which include the naive Bayes model as a special case but can also represent more complex dependencies.

### 5.1. The model family

As before, we assume $m$ variables $X_{1}, \ldots, X_{m}$ with given value cardinalities $K_{1}, \ldots, K_{m}$. Since the goal here is to model the joint probability distribution of the $m$ variables, there is no need to mark a special variable. We assume a data matrix $\mathbf{x}^{n}=\left(x_{j i}\right) \in \mathcal{X}^{n}, 1 \leq j \leq n$, and $1 \leq i \leq m$, as given.

A Bayesian network structure $\mathcal{G}$ encodes independence assumptions so that if each variable $X_{i}$ is represented as a node in the network, then the joint probability distribution factorizes into a product of local probability distributions, one for each node, conditioned on its parent set. We define a Bayesian forest to be a Bayesian network structure $\mathcal{G}$ on the node set $X_{1}, \ldots, X_{m}$ which assigns at most one parent $X_{\mathrm{pa}(i)}$
to any node $X_{i}$. Consequently, a Bayesian tree is a connected Bayesian forest and a Bayesian forest breaks down into component trees, that is, connected subgraphs. The root of each such component tree lacks a parent, in which case we write $\mathrm{pa}(i)=\varnothing$.

The parent set of a node $X_{i}$ thus reduces to a single value $\mathrm{pa}(i) \in\{1, \ldots, i-1, i+1, \ldots, m, \varnothing\}$. Let further $\operatorname{ch}(i)$ denote the set of children of node $X_{i}$ in $\mathcal{G}$ and $\operatorname{ch}(\varnothing)$ denote the "children of none," that is, the roots of the component trees of $\mathcal{G}$.

The corresponding model family $\mathcal{F}_{\mathrm{BF}}$ can be indexed by the network structure $\mathcal{G}$ and the corresponding attribute value counts $K_{1}, \ldots, K_{m}$ :

$$
\mathcal{F}_{\mathrm{BF}}=\left\{\mathcal{M}(\varphi): \varphi \in \Phi_{\mathrm{BF}}\right\}
$$

with $\Phi_{\mathrm{BF}}=\{1, \ldots,|\mathcal{G}|\} \times\{1,2,3, \ldots\}^{m}$, where $\mathcal{G}$ is associated with an integer according to some enumeration of all Bayesian forests on $\left(X_{1}, \ldots, X_{m}\right)$. As the $K_{i}$ are assumed fixed, we can abbreviate the corresponding model classes by $\mathcal{M}(\mathcal{G}):=\mathcal{M}\left(\mathcal{G}, K_{1}, \ldots, K_{m}\right)$.

Given a forest model class $\mathcal{M}(\mathcal{G})$, we index each model by a parameter vector $\boldsymbol{\theta}$ in the corresponding parameter space $\Theta_{\mathcal{G}}$ :

$$
\begin{aligned}
\Theta_{\mathcal{G}}=\{ & \boldsymbol{\theta}=\left(\theta_{i k l}\right): \theta_{i k l} \geq 0, \sum_{l} \theta_{i k l}=1 \\
& \left.i=1, \ldots, m, k=1, \ldots, K_{\mathrm{pa}(i)}, l=1, \ldots, K_{i}\right\}
\end{aligned}
$$

where we define $K_{\varnothing}:=1$ in order to unify notation for root and non-root nodes. Each such $\theta_{i k l}$ defines a probability

$$
\theta_{i k l}=P\left(X_{i}=l \mid X_{\mathrm{pa}(i)}=k, \mathcal{M}(\mathcal{G}), \boldsymbol{\theta}\right)
$$

where we interpret $X_{\varnothing}=1$ as a null condition.
The joint probability that a model $M=(\mathcal{G}, \boldsymbol{\theta})$ assigns to a data vector $\mathbf{x}=\left(x_{1}, \ldots, x_{m}\right)$ becomes

$$
\begin{aligned}
& P(\mathbf{x} \mid \mathcal{M}(\mathcal{G}), \boldsymbol{\theta}) \\
& \quad=\prod_{i=1}^{m} P\left(X_{i}=x_{i} \mid X_{\mathrm{pa}(i)}=x_{\mathrm{pa}(i)}, \mathcal{M}(\mathcal{G}), \boldsymbol{\theta}\right)=\prod_{i=1}^{m} \theta_{i, x_{\mathrm{pa}(i)}, x_{i}}
\end{aligned}
$$

1: Compute $\mathcal{C}_{\mathrm{MN}}(k, j)$ for $k=1, \ldots, V_{\max }, j=0, \ldots, n$, where $V_{\max }=\max \left\{K_{1}, \ldots, K_{m}\right\}$
2: for $K_{0}=1$ to $K_{\max }$ do
3: Count the frequencies $h_{1}, \ldots, h_{K_{0}}, f_{\mathrm{ik} 1}, \ldots, f_{\mathrm{ik} K_{i}}$ for $i=1, \ldots, m, k=1, \ldots, K_{0}$ from the data $\mathbf{x}^{n}$
4: Compute the likelihood:

$$
P\left(\mathbf{x}^{n} \mid \widehat{\boldsymbol{\theta}}\left(\mathbf{x}^{n}, \mathcal{M}\left(K_{0}, K_{1}, \ldots, K_{m}\right)\right)\right)=\prod_{k=1}^{K_{0}}\left(h_{k} / n\right)^{h_{k}} \prod_{i=1}^{m_{k}} \prod_{l=1}^{K_{l}}\left(f_{\mathrm{ikl}} / h_{k}\right)^{f_{\mathrm{ikl}}}
$$

5: Set $\mathcal{C}_{\mathrm{NB}}\left(K_{0}, 0\right)=1$
6: if $K_{0}=1$ then
7: Compute $\mathcal{C}_{\mathrm{NB}}(1, j)=\prod_{i=1}^{m} \mathcal{C}_{\mathrm{MN}}\left(K_{i}, j\right)$ for $j=1, \ldots, n$
8: else
9: Compute $\mathcal{C}_{\mathrm{NB}}\left(K_{0}, j\right)=\sum_{r_{1}+r_{2}=j}\left(j!/ r_{1}!r_{2}!\right)\left(r_{1} / j\right)^{r_{2}}\left(r_{2} / j\right)^{r_{2}} \cdot \mathcal{C}_{\mathrm{NB}}\left(1, r_{1}\right) \cdot \mathcal{C}_{\mathrm{NB}}\left(K_{0}-1, r_{2}\right)$ for $j=1, \ldots, n$
10: end if
11: Output $P_{\mathrm{NML}}\left(\mathbf{x}^{n} \mid \mathcal{M}\left(K_{0}, K_{1}, \ldots, K_{m}\right)\right)=P\left(\mathbf{x}^{n} \mid \widehat{\boldsymbol{\theta}}\left(\mathbf{x}^{n}, \mathcal{M}\left(K_{0}, K_{1}, \ldots, K_{m}\right)\right)\right) / \mathcal{C}_{\mathrm{NB}}\left(K_{0}, n\right)$
12: end for

Algorithm 2: The algorithm for computing $P_{\mathrm{NML}}\left(\mathbf{x}^{n} \mid \mathcal{M}\left(K_{0}, K_{1}, \ldots, K_{m}\right)\right)$ for $K_{0}=1, \ldots, K_{\max }$.

For a sample $\mathbf{x}^{n}=\left(x_{j i}\right)$ of $n$ vectors $\mathbf{x}_{j}$, we define the corresponding frequencies as

$$
\begin{aligned}
f_{i k l} & :=\left|\left\{j: x_{j i}=l \wedge x_{j, \mathrm{pa}(i)}=k\right\}\right| \\
f_{i l} & :=\left|\left\{j: x_{j i}=l\right\}\right|=\sum_{k=1}^{K_{\mathrm{pa}(i)}} f_{i k l}
\end{aligned}
$$

By definition, for any component tree root $X_{i}$, we have $f_{i l}=$ $f_{i 1 l}$. The probability assigned to a sample $\mathbf{x}^{n}$ can then be written as

$$
P\left(\mathbf{x}^{n} \mid \mathcal{M}(\mathcal{Y}), \boldsymbol{\theta}\right)=\prod_{i=1}^{m} \prod_{k=1}^{K_{\mathrm{pa}(i)}} \prod_{l=1}^{K_{l}} \theta_{i k l}^{f_{\mathrm{ikl}}}
$$

which is maximized at

$$
\widehat{\theta}_{i k l}\left(\mathbf{x}^{n}, \mathcal{M}(\mathcal{Y})\right)=\frac{f_{i k l}}{f_{\mathrm{pa}(i), k}}
$$

where we define $f_{\mathcal{O}, 1}:=n$. The maximum data likelihood thereby is

$$
\widehat{P}\left(\mathbf{x}^{n} \mid \mathcal{M}(\mathcal{Y})\right)=\prod_{i=1}^{m} \prod_{k=1}^{K_{\mathrm{pa}(i)}} \prod_{l=1}^{K_{l}}\left(\frac{f_{i k l}}{f_{\mathrm{pa}(i), k}}\right)^{f_{\mathrm{ikl}}}
$$

### 5.2. The algorithm

The goal is to calculate the NML distribution $P_{\mathrm{NML}}\left(\mathbf{x}^{n} \mid\right.$ $\mathcal{M}(\mathcal{Y})$ ) defined in (3). This consists of calculating the maximum data likelihood (36) and the normalizing term $\mathcal{C}(\mathcal{M}(\mathcal{Y}), n)$ given in (4). The former involves frequency counting, one sweep through the data, and multiplication of the appropriate values. This can be done in time $\mathcal{O}\left(n+\right.$ $\sum_{i} K_{i} K_{\mathrm{pa}(i)}$ ). The latter involves a sum exponential in $n$, which clearly makes it the computational bottleneck of the algorithm.

Our approach is to break up the normalizing sum in (4) into terms corresponding to subtrees with given frequencies in either their root or its parent. We then calculate the com-
plete sum by sweeping through the graph once, bottom-up. Let us now introduce some necessary notation.

Let $\mathcal{Y}$ be a given Bayesian forest. Then for any node $X_{i}$ denote the subtree rooting in $X_{i}$, by $\mathcal{Y}_{\text {sub }(i)}$ and the forest built up by all descendants of $X_{i}$ by $\mathcal{Y}_{\text {s }}$ s( $i$ ). The corresponding data domains are $\mathcal{X}_{\text {sub }(i)}$ and $\mathcal{X}_{\text {sisc }(i)}$, respectively. Denote the sum over all $n$-instantiations of a subtree by

$$
\mathcal{C}_{i}(\mathcal{M}(\mathcal{Y}), n):=\sum_{\mathbf{x}_{\text {sub }(i)}^{n} \in \mathcal{X}_{\text {sub }(i)}^{n}} P\left(\mathbf{x}_{\text {sub }(i)}^{n} \mid \widehat{\boldsymbol{\theta}}\left(\mathbf{x}_{\text {sub }(i)}^{n}\right), \mathcal{M}\left(\mathcal{Y}_{\text {sub }(i)}\right)\right)
$$

and for any vector $\mathbf{x}_{i}^{n} \in X_{i}^{n}$ with frequencies $\mathbf{f}_{i}=\left(f_{i 1}\right.$, $\left.\ldots, f_{i K_{i}}\right)$, we define

$$
\begin{aligned}
& \mathcal{C}_{i}\left(\mathcal{M}(\mathcal{Y}), n \mid \mathbf{f}_{i}\right) \\
& \quad:=\sum_{\mathbf{x}_{\mathrm{ds}(i)}^{n} \in \mathcal{X}_{\mathrm{ds}(i)}^{n}} P\left(\mathbf{x}_{\mathrm{ds}(i)}^{n}, \mathbf{x}_{i}^{n} \mid \widehat{\boldsymbol{\theta}}\left(\mathbf{x}_{\mathrm{ds}(i)}^{n}, \mathbf{x}_{i}^{n}\right), \mathcal{M}\left(\mathcal{Y}_{\text {sub }(i)}\right)\right)
\end{aligned}
$$

to be the corresponding sum with fixed root instantiation, summing only over the attribute space spanned by the descendants on $X_{i}$.

Note that we use $\mathbf{f}_{i}$ on the left-hand side, and $\mathbf{x}_{i}^{n}$ on the right-hand side of the definition. This needs to be justified. Interestingly, while the terms in the sum depend on the ordering of $\mathbf{x}_{i}^{n}$, the sum itself depends on $\mathbf{x}_{i}^{n}$ only through its frequencies $\mathbf{f}_{i}$. To see this pick, any two representatives $\mathbf{x}_{i}^{n}$ and $\overline{\mathbf{x}}_{i}^{n}$ of $\mathbf{f}_{i}$ and find, for example, after lexicographical ordering of the elements, that

$$
\left\{\left(\mathbf{x}_{i}^{n}, \mathbf{x}_{\mathrm{ds}(i)}^{n}\right): \mathbf{x}_{\mathrm{ds}(i)}^{n} \in \mathcal{X}_{\mathrm{ds}(i)}^{n}\right\}=\left\{\left(\overline{\mathbf{x}}_{i}^{n}, \mathbf{x}_{\mathrm{ds}(i)}^{n}\right): \mathbf{x}_{\mathrm{ds}(i)}^{n} \in \mathcal{X}_{\mathrm{ds}(i)}^{n}\right\}
$$

Next, we need to define corresponding sums over $\mathcal{X}_{\text {sub }(i)}$ with the frequencies at the subtree root parent $X_{\mathrm{pa}(i)}$ given.

For any $\mathbf{f}_{\mathrm{pa}(i)} \sim \mathbf{x}_{\mathrm{pa}(i)}^{n} \in X_{\mathrm{pa}(i)}^{n}$ define

$$
\begin{aligned}
& \mathcal{L}_{i}\left(\mathcal{M}(\mathcal{Y}), n \mid \mathbf{f}_{\mathrm{pa}(i)}\right) \\
& :=\sum_{\mathbf{x}_{\mathrm{sub}(i)}^{n} \in \mathcal{X}_{\mathrm{sub}(i)}^{n}} P\left(\mathbf{x}_{\mathrm{sub}(i)}^{n} \mid \mathbf{x}_{\mathrm{pa}(i)}^{n}, \tilde{\boldsymbol{\theta}}\left(\mathbf{x}_{\mathrm{sub}(i)}^{n}, \mathbf{x}_{\mathrm{pa}(i)}^{n}\right), \mathcal{M}\left(\mathcal{Y}_{\mathrm{sub}(i)}\right)\right)
\end{aligned}
$$

Again, this is well defined since any other representative $\overline{\mathbf{x}}_{\mathrm{pa}(i)}^{n}$ of $\mathbf{f}_{\mathrm{pa}(i)}$ yields summing the same terms modulo their ordering.

After having introduced this notation, we now briefly outline the algorithm and in the following subsections give a more detailed description of the steps involved. As stated before, we go through $\mathcal{Y}$ bottom-up. At each inner node $X_{i}$, we receive $\mathcal{L}_{j}\left(\mathcal{M}(\mathcal{Y}), n \mid \mathbf{f}_{i}\right)$ from each child $X_{j}, j \in \operatorname{ch}(i)$. Correspondingly, we are required to send $\mathcal{L}_{i}\left(\mathcal{M}(\mathcal{Y}), n \mid \mathbf{f}_{\mathrm{pa}(i)}\right)$ up to the parent $X_{\mathrm{pa}(i)}$. At each component tree root $X_{i}$, we then calculate the sum $\mathcal{C}_{i}(\mathcal{M}(\mathcal{Y}), n)$ for the whole connectivity component and then combine these sums to get the normalizer $\mathcal{C}_{i}(\mathcal{M}(\mathcal{Y}), n)$ for the complete forest $\mathcal{Y}$.

### 5.2.1. Leaves

For a leaf node $X_{i}$ we can calculate the $\mathcal{L}_{i}\left(\mathcal{M}(\mathcal{Y}), n \mid\right.$ $\left.\mathbf{f}_{\mathrm{pa}(i)}\right)$ without listing its own frequencies $\mathbf{f}_{i}$. As in (27), $\mathbf{f}_{\mathrm{pa}(i)}$ splits the $n$ data vectors into $K_{\mathrm{pa}(i)}$ subsets of sizes $f_{\mathrm{pa}(i), 1}, \ldots, f_{\mathrm{pa}(i), K_{\mathrm{pa}(i)}}$ and each of them can be modeled independently as a multinomial; we have

$$
\mathcal{L}_{i}\left(\mathcal{M}(\mathcal{Y}), n \mid \mathbf{f}_{\mathrm{pa}(i)}\right)=\prod_{k=1}^{K_{\mathrm{pa}(i)}} \mathcal{C}_{\mathrm{MN}}\left(K_{i}, f_{\mathrm{pa}(i), k}\right)
$$

The terms $\mathcal{C}_{\mathrm{MN}}\left(K_{i}, n^{\prime}\right)$ (for $\left.n^{\prime}=0, \ldots, n\right)$ can be precalculated using recurrence (19) as in Algorithm 1.

### 5.2.2. Inner nodes

For inner nodes $X_{i}$ we divide the task into two steps. First, we collect the child messages $\mathcal{L}_{j}\left(\mathcal{M}(\mathcal{Y}), n \mid \mathbf{f}_{i}\right)$ sent by each child $X_{j} \in \operatorname{ch}(i)$ into partial sums $\mathcal{C}_{i}\left(\mathcal{M}(\mathcal{Y}), n \mid \mathbf{f}_{i}\right)$ over $\mathcal{X}_{\mathrm{ds}(i)}$, and then "lift" these to sums $\mathcal{L}_{i}\left(\mathcal{M}(\mathcal{Y}), n \mid \mathbf{f}_{\mathrm{pa}(i)}\right)$ over $\mathcal{X}_{\mathrm{sub}(i)}$ which are the messages to the parent.

The first step is simple. Given an instantiation $\mathbf{x}_{i}^{n}$ at $X_{i}$ or, equivalently, the corresponding frequencies $\mathbf{f}_{i}$, the subtrees rooting in the children $\operatorname{ch}(i)$ of $X_{i}$ become independent of each other. Thus we have

$$
\begin{aligned}
& \mathcal{C}_{i}\left(\mathcal{M}(\mathcal{Y}), n \mid \mathbf{f}_{i}\right) \\
& =\sum_{\mathbf{x}_{\mathrm{ds}(i)}^{n} \in \mathcal{X}_{\mathrm{ds}(i)}^{n}} P\left(\mathbf{x}_{\mathrm{ds}(i)}^{n}, \mathbf{x}_{i}^{n} \mid \tilde{\boldsymbol{\theta}}\left(\mathbf{x}_{\mathrm{ds}(i)}^{n}, \mathbf{x}_{i}^{n}\right), \mathcal{M}\left(\mathcal{Y}_{\mathrm{sub}(i)}\right)\right) \\
& =P\left(\mathbf{x}_{i}^{n} \mid \tilde{\boldsymbol{\theta}}\left(\mathbf{x}_{\mathrm{ds}(i)}^{n}, \mathbf{x}_{i}^{n}\right), \mathcal{M}\left(\mathcal{Y}_{\mathrm{sub}(i)}\right)\right) \\
& \times\left(\sum_{\mathbf{x}_{\mathrm{ds}(i)}^{n} \in \mathcal{X}_{\mathrm{ds}(i)}^{n}} \prod_{j \in \operatorname{ch}(i)} P\left(\mathbf{x}_{\mathrm{ds}(i) \mid \operatorname{sub}(j)}^{n} \mid \mathbf{x}_{i}^{n}\right.\right. \\
& \left.\left.\tilde{\boldsymbol{\theta}}\left(\mathbf{x}_{\mathrm{ds}(i)}^{n}, \mathbf{x}_{i}^{n}\right), \mathcal{M}\left(\mathcal{Y}_{\mathrm{sub}(i)}\right)\right)\right) \\
& =P\left(\mathbf{x}_{i}^{n} \mid \tilde{\boldsymbol{\theta}}\left(\mathbf{x}_{\mathrm{ds}(i)}^{n}, \mathbf{x}_{i}^{n}\right), \mathcal{M}\left(\mathcal{Y}_{\mathrm{sub}(i)}\right)\right) \\
& \times \prod_{j \in \operatorname{ch}(i)}\left(\sum_{\mathbf{x}_{\mathrm{sub}(i)}^{n} \in \mathcal{X}_{\mathrm{sub}(i)}^{n}} P\left(\mathbf{x}_{\mathrm{sub}(j)}^{n} \mid \mathbf{x}_{i}^{n}\right.\right. \\
& \left.\left.\tilde{\boldsymbol{\theta}}\left(\mathbf{x}_{\mathrm{ds}(i)}^{n}, \mathbf{x}_{i}^{n}\right), \mathcal{M}\left(\mathcal{Y}_{\mathrm{sub}(i)}\right)\right)\right) \\
& =\prod_{l=1}^{K_{i}}\left(\frac{f_{i l}}{n}\right)^{f_{i l}} \prod_{j \in \operatorname{ch}(i)} \mathcal{L}_{j}\left(\mathcal{M}(\mathcal{Y}), n \mid \mathbf{f}_{i}\right)
\end{aligned}
$$

where $\mathbf{x}_{\mathrm{ds}(i) \mid \operatorname{sub}(j)}^{n}$ is the restriction of $\mathbf{x}_{\mathrm{ds}(i)}$ to columns corresponding to nodes in $\mathcal{Y}_{j}$. We have used (38) for (42), (32) for (43) and (44), and finally (36) and (40) for (45).

Now we need to calculate the outgoing messages $\mathcal{L}_{i}\left(\mathcal{M}(\mathcal{Y}), n \mid \mathbf{f}_{\mathrm{pa}(i)}\right)$ from the incoming messages we have just combined into $\mathcal{C}_{i}\left(\mathcal{M}(\mathcal{Y}), n \mid \mathbf{f}_{i}\right)$. This is the most demanding part of the algorithm, for we need to list all possible conditional frequencies, of which there are $\mathcal{O}\left(n^{K_{i} K_{\mathrm{pa}(i)}-1}\right)$ many, the -1 being due to the sum-to- $n$ constraint. For fixed $i$, we arrange the conditional frequencies $f_{i k l}$ into a matrix $\mathbf{F}=\left(f_{i k l}\right)$ and define its marginals

$$
\begin{aligned}
& \boldsymbol{\rho}(\mathbf{F}):=\left(\sum_{k} f_{i k 1}, \ldots, \sum_{k} f_{i k K_{i}}\right) \\
& \gamma(\mathbf{F}):=\left(\sum_{l} f_{l 1 l}, \ldots, \sum_{l} f_{l K_{\mathrm{pa}(i} l}\right)
\end{aligned}
$$

to be the vectors obtained by summing the rows of $\mathbf{F}$ and the columns of $\mathbf{F}$, respectively. Each such matrix then corresponds to a term $\mathcal{C}_{i}\left(\mathcal{M}(\mathcal{Y}), n \mid \boldsymbol{\rho}(\mathbf{F})\right)$ and a term $\mathcal{L}_{i}\left(\mathcal{M}(\mathcal{Y}), n \mid \gamma(\mathbf{F})\right)$. Formally, we have

$$
\mathcal{L}_{i}\left(\mathcal{M}(\mathcal{Y}), n \mid \mathbf{f}_{\mathrm{pa}(i)}\right)=\sum_{\mathbf{F}: \gamma(\mathbf{F})=\mathbf{f}_{\mathrm{pa}(i)}} \mathcal{C}_{i}(\mathcal{M}(\mathcal{Y}), n \mid \boldsymbol{\rho}(\mathbf{F}))
$$

### 5.2.3. Component tree roots

For a component tree root $X_{i} \in \operatorname{ch}(\varnothing)$ we do not need to pass any message upward. All we need is the complete sum over the component tree

$$
\mathcal{C}_{i}\left(\mathcal{M}_{\mathcal{Y}}, n\right)=\sum_{\mathbf{f}_{i}} \frac{n!}{f_{i 1}!\cdots f_{i K_{i}}!} \mathcal{C}_{i}\left(\mathcal{M}_{\mathcal{Y}}, n \mid \mathbf{f}_{i}\right)
$$

where the $\mathcal{C}_{i}\left(\mathcal{M}_{\mathcal{Y}}, n \mid \mathbf{f}_{i}\right)$ are calculated from (45). The summation goes over all nonnegative integer vectors $\mathbf{f}_{i}$ summing to $n$. The above is trivially true since we sum over all instantiations $\mathbf{x}_{i}$ of $X_{i}$ and group like terms, corresponding to the same frequency vector $\mathbf{f}_{i}$, while keeping track of their respective count, namely $n!/ f_{i 1}!\cdots f_{i K_{i}}$ !.

### 5.2.4. The algorithm

For the complete forest $\mathcal{Y}$ we simply multiply the sums over its tree components. Since these are independent of each

1: Count all frequencies $f_{\mathrm{th} 1}$ and $f_{\mathrm{ff}}$ from the data $\mathbf{x}^{n}$
2: Compute $\tilde{P}\left(\mathbf{x}^{n} \mid \mathcal{M}(\mathcal{G})\right)=\prod_{i=1}^{m} \prod_{k=1}^{K_{\mathrm{pa}(i)}} \prod_{i=1}^{K_{i}}\left(f_{\mathrm{th} 2} / f_{\mathrm{pa}(i), k}\right)^{f_{\mathrm{th} 2}}$
3: for $k=1, \ldots, K_{\max }:=\max _{i, X_{i} \in \times \text { leaf }}\left\{K_{i}\right\}$ and $n^{\prime}=0, \ldots, n$ do
4: Compute $\mathcal{C}_{\mathrm{MN}}\left(k, n^{\prime}\right)$ as in Algorithm 1
5: end for
6: for each node $X_{i}$ in some bottom-up order do
7: if $X_{i}$ is a leaf then
8: for each frequency vector $\mathbf{f}_{\mathrm{pa}(i)}$ of $X_{\mathrm{pa}(i)}$ do
9: $\quad$ Compute $\mathcal{L}_{i}\left(\mathcal{M}(\mathcal{G}), n \mid \mathbf{f}_{\mathrm{pa}(i)}\right)=\prod_{k=1}^{K_{\mathrm{pa}(i)}} \mathcal{C}_{\mathrm{MN}}\left(K_{i}, \mathbf{f}_{\mathrm{pa}(i) k}\right)$
10: end for
11: else if $X_{i}$ is an inner node then
12: for each frequency vector $\mathbf{f}_{i} X_{i}$ do
13: $\quad$ Compute $\mathcal{C}_{i}\left(\mathcal{M}(\mathcal{G}), n \mid \mathbf{f}_{i}\right)=\prod_{j=1}^{K_{i}}\left(f_{\mathrm{ff}} / n\right)^{f_{\mathrm{ff}}} \prod_{j \in \mathrm{ch}(i)} \mathcal{L}_{j}\left(\mathcal{M}(\mathcal{G}), n \mid \mathbf{f}_{i}\right)$
14: end for
15: initialize $\mathcal{L}_{i} \equiv 0$
16: for each non-negative $K_{i} \times K_{\mathrm{pa}(i)}$ integer matrix $\mathbf{F}$ with entries summing to $n$ do
17: $\quad \mathcal{L}_{i}\left(\mathcal{M}(\mathcal{G}), n \mid \gamma(\mathbf{F})\right)+=\mathcal{C}_{i}\left(\mathcal{M}(\mathcal{G}), n \mid \rho(\mathbf{F})\right)$
18: end for
19: else if $X_{i}$ is a component tree root then
20: $\quad$ Compute $\mathcal{C}_{i}\left(\mathcal{M}(\mathcal{G}), n\right)=\sum_{\mathbf{f}_{i}} \prod_{i=1}^{K_{i}}\left(f_{\mathrm{ff}} / n\right)^{f_{\mathrm{ff}}} \prod_{j \in \mathrm{ch}(i)} \mathcal{L}_{j}\left(\mathcal{M}(\mathcal{G}), n \mid \mathbf{f}_{i}\right)$
21: end if
22: end for
23: Compute $\mathcal{C}\left(\mathcal{M}(\mathcal{G}), n\right)=\prod_{i \in \mathrm{ch}(\mathscr{Q})} \mathcal{C}_{i}\left(\mathcal{M}(\mathcal{G}), n\right)$
24: $\operatorname{Output} e P_{\mathrm{NML}}\left(\mathbf{x}^{n} \mid \mathcal{M}(\mathcal{G})\right)=\widetilde{P}\left(\mathbf{x}^{n} \mid \mathcal{M}(\mathcal{G})\right) / \mathcal{C}\left(\mathcal{M}(\mathcal{G}), n\right)$

Algorithm 3: The algorithm for computing $P_{\mathrm{NML}}\left(\mathbf{x}^{n} \mid \mathcal{M}(\mathcal{G})\right)$ for a Bayesian forest $\mathcal{G}$.
other, in analogy to (42)-(45) we have

$$
\mathcal{C}\left(\mathcal{M}_{\mathcal{G}}, n\right)=\prod_{i \in \operatorname{ch}(\mathscr{Q})} \mathcal{C}_{i}\left(\mathcal{M}_{\mathcal{G}}, n\right)
$$

Algorithm 3 collects all the above into a pseudocode.
The time complexity of this algorithm is $\mathcal{O}\left(n^{K_{i} K_{\mathrm{pa}(i)}-1}\right)$ for each inner node, $\mathcal{O}\left(n\left(n+K_{i}\right)\right)$ for each leaf, and $\mathcal{O}\left(n^{K_{i}-1}\right)$ for a component tree root of $\mathcal{G}$. When all $m^{\prime}<m$ inner nodes are binary, it runs in $\mathcal{O}\left(m^{\prime} n^{3}\right)$, independently of the number of values of the leaf nodes. This is polynomial with respect to the sample size $n$, while applying (4) directly for computing $\mathcal{C}\left(\mathcal{M}(\mathcal{G}), n\right)$ requires exponential time. The order of the polynomial depends on the attribute cardinalities: the algorithm is exponential with respect to the number of values a non-leaf variable can take.

Finally, note that we can speed up the algorithm when $\mathcal{G}$ contains multiple copies of some subtree. Also we have $\mathcal{C}_{i} / \mathcal{L}_{i}\left(\mathcal{M}_{\mathcal{G}}, n \mid \mathbf{f}_{i}\right)=\mathcal{C}_{i} / \mathcal{L}_{i}\left(\mathcal{M}_{\mathcal{G}}, n \mid \pi\left(\mathbf{f}_{i}\right)\right)$ for any permutation $\pi$ of the entries of $\mathbf{f}_{i}$. However, this does not lead to considerable gain, at least in order of magnitude. Also, we can see that in line 16 of the algorithm we enumerate all frequency matrices $\mathbf{F}$, while in line 17 we sum the same terms whenever the marginals of $\mathbf{F}$ are the same. Unfortunately, computing the number of non-negative integer matrices with given marginals is a \#P-hard problem already when the other matrix dimension is fixed to 2 , as proven in [33]. This suggests that for this task there may not exist an algorithm that is polynomial in all input quantities. The algorithm presented
here is polynomial as well in the sample size $n$ as in the graph size $m$. For attributes with relatively few values, the polynomial is time tolerable.

## 6. CONCLUSION

The normalized maximum likelihood (NML) offers a universal, minimax optimal approach to statistical modeling. In this paper, we have surveyed efficient algorithms for computing the NML in the case of discrete datasets. The model families used in our work are Bayesian networks of varying complexity. The simplest model we discussed is the multinomial model family, which can be applied to problems related to density estimation or discretization. In this case, the NML can be computed in linear time. The same result also applies to a network of independent multinomial variables, that is, a Bayesian network with no arcs.

For the naive Bayes model family, the NML can be computed in quadratic time. Models of this type have been used extensively in clustering or classification domains with good results. Finally, to be able to represent more complex dependencies between the problem domain variables, we also considered tree-structured Bayesian networks. We showed how to compute the NML in this case in polynomial time with respect to the sample size, but the order of the polynomial depends on the number of values of the domain variables, which makes our result impractical for some domains.

The methods presented are especially suitable for problems in bioinformatics, which typically involve multidimensional discrete datasets. Furthermore, unlike the Bayesian methods, information-theoretic approaches such as ours do not require a prior for the model parameters. This is the most important aspect, as constructing a reasonable parameter prior is a notoriously difficult problem, particularly in bioinformatical domains involving novel types of data with little background knowledge. All in all, information theory has been found to offer a natural and successful theoretical framework for biological applications in general, which makes NML an appealing choice for bioinformatics.

In the future, our plan is to extend the current work to more complex cases such as general Bayesian networks, which would allow the use of NML in even more involved modeling tasks. Another natural area of future work is to apply the methods of this paper to practical tasks involving large discrete databases and compare the results to other approaches, such as those based on Bayesian statistics.

## APPENDIX

## PROOFS OF THEOREMS

In this section, we provide detailed proofs of two theorems presented in the paper.

## Proof of Theorem 1 (multinomial recursion)

We start by proving the following lemma.
Lemma 3. For the tree function $T(z)$ we have

$$
z T^{\prime}(z)=\frac{T(z)}{1-T(z)}
$$

Proof. A basic property of the tree function is the functional equation $T(z)=z e^{T(z)}$ (see, e.g., [23]). Differentiating this equation yields

$$
\begin{aligned}
& T^{\prime}(z)=e^{T(z)}+T(z) T^{\prime}(z) \\
& z T^{\prime}(z)(1-T(z))=z e^{T(z)}
\end{aligned}
$$

from which (A.1) follows.

Now we can proceed to the proof of the theorem. We start by multiplying and differentiating (17) as follows:

$$
\begin{aligned}
z \cdot \frac{d}{d z} \sum_{n \geqslant 0} \frac{n^{n}}{n!} \mathcal{C}_{\mathrm{MN}}(K, n) z^{n} & =z \cdot \sum_{n \geqslant 1} n \cdot \frac{n^{n}}{n!} \mathcal{C}_{\mathrm{MN}}(K, n) z^{n-1} \\
& =\sum_{n \geqslant 0} n \cdot \frac{n^{n}}{n!} \mathcal{C}_{\mathrm{MN}}(K, n) z^{n}
\end{aligned}
$$

On the other hand, by manipulating (18) in the same way, we get

$$
\begin{aligned}
& z \cdot \frac{d}{d z} \frac{1}{(1-T(z))^{K}} \\
& =\frac{z \cdot K}{(1-T(z))^{K+1}} \cdot T^{\prime}(z) \\
& =\frac{K}{(1-T(z))^{K+1}} \cdot \frac{T(z)}{1-T(z)} \\
& =K\left(\frac{1}{(1-T(z))^{K+2}}-\frac{1}{(1-T(z))^{K+1}}\right) \\
& =K\left(\sum_{n \geqslant 0} \frac{n^{n}}{n!} \mathcal{C}_{\mathrm{MN}}(K+2, n) z^{n}-\sum_{n \geqslant 0} \frac{n^{n}}{n!} \mathcal{C}_{\mathrm{MN}}(K+1, n) z^{n}\right)
\end{aligned}
$$

where (A.6) follows from Lemma 3. Comparing the coefficients of $z^{n}$ in (A.4) and (A.8), we get

$$
n \cdot \mathcal{C}_{\mathrm{MN}}(K, n)=K \cdot\left(\mathcal{C}_{\mathrm{MN}}(K+2, n)-\mathcal{C}_{\mathrm{MN}}(K+1, n)\right)
$$

from which the theorem follows.

## Proof of Theorem 2 (naive Bayes recursion)

We have

$$
\begin{aligned}
& \mathcal{C}_{\mathrm{NB}}\left(K_{0}, n\right) \\
& =\sum_{h_{1}+\cdots+h_{K_{0}}=n} \frac{n!}{h_{1}!\cdots h_{K_{0}}!} \prod_{k=1}^{K_{0}}\left(\frac{h_{k}}{n}\right)^{h_{k}} \prod_{i=1}^{m} \mathcal{C}_{\mathrm{MN}}\left(K_{i}, h_{k}\right) \\
& =\sum_{h_{1}+\cdots+h_{K_{0}}=n} \frac{n!}{n^{n}} \prod_{k=1}^{K_{0}} \frac{h_{k}^{h_{k}}}{h_{k}!} \prod_{i=1}^{m} \mathcal{C}_{\mathrm{MN}}\left(K_{i}, h_{k}\right) \\
& =\sum_{\substack{h_{1}+\cdots+h_{K^{+}}=r_{1} \\
h_{K^{+}+1}+\cdots+h_{K_{0}}=r_{2}}} \frac{n!}{n^{n}} \frac{r_{1}^{r_{1}}}{r_{1}!} \frac{r_{2}^{r_{2}}}{r_{1}!}\left(\frac{r_{1}!}{r_{1}!} \prod_{k=1}^{K_{1}} \frac{h_{k}^{h_{k}}}{h_{k}!} \frac{r_{2}!}{r_{2}!} \prod_{k=K^{+}+1} \frac{h_{k}^{h_{k}}}{h_{k}!}\right) \\
& \cdot \prod_{i=1}^{m} \prod_{k=1}^{K^{+}} \mathcal{C}_{\mathrm{MN}}\left(K_{i}, h_{k}\right) \prod_{k=K^{+}+1}^{K_{0}} \mathcal{C}_{\mathrm{MN}}\left(K_{i}, h_{k}\right) \\
& =\sum_{\substack{h_{1}+\cdots+h_{K^{+}}=r_{1} \\
h_{K^{+}+1}+\cdots+h_{K_{0}}=r_{2}}} \frac{n!}{r_{1}!r_{2}!}\left(\frac{r_{1}}{n}\right)^{r_{1}}\left(\frac{r_{2}}{n}\right)^{r_{2}} \\
& \cdot\left(\frac{r_{1}!}{h_{1}!\cdots h_{K^{+}}!} \prod_{k=1}^{K^{+}}\left(\frac{h_{k}}{r_{1}}\right)^{h_{k}} \prod_{i=1}^{m} \mathcal{C}_{\mathrm{MN}}\left(K_{i}, h_{k}\right)\right) \\
& \cdot\left(\frac{r_{2}!}{h_{K^{+}+1}!\cdots h_{K_{0}}} \prod_{k=K^{+}+1}^{K_{0}}\left(\frac{h_{k}}{r_{2}}\right)^{h_{k}} \prod_{i=1}^{m} \mathcal{C}_{\mathrm{MN}}\left(K_{i}, h_{k}\right)\right) \\
& =\sum_{r_{1}+r_{2}=n} \frac{n!}{r_{1}!r_{2}!}\left(\frac{r_{1}}{n}\right)^{r_{2}}\left(\frac{r_{2}}{n}\right)^{r_{2}} \cdot \mathcal{C}_{\mathrm{NB}}\left(K^{+}, r_{1}\right) \cdot \mathcal{C}_{\mathrm{NB}}\left(K_{0}-K^{+}, r_{2}\right)
\end{aligned}
$$

and the proof follows.

## ACKNOWLEDGMENTS

The authors would like to thank the anonymous reviewers and Jorma Rissanen for useful comments. This work was supported in part by the Academy of Finland under the project Civi and by the Finnish Funding Agency for Technology and Innovation under the projects Kukot and PMMA. In addition, this work was supported in part by the IST Programme of the European Community, under the PASCAL Network of Excellence, IST-2002-506778. This publication only reflects the authors' views.
