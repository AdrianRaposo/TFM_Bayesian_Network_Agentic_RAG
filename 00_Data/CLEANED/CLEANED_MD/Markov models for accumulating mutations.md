# Markov models for accumulating mutations 

## Journal Article

Author(s):
Beerenwinkel, Niko; Sullivant, Seth

Publication date:
2009

## Permanent link:

https://doi.org/10.3929/ethz-b-000015574

## Rights / license:

In Copyright - Non-Commercial Use Permitted
Originally published in:
Biometrika 96(3), https://doi.org/10.1093/biomet/asp023

# Markov models for accumulating mutations 

BY N. BEERENWINKEL<br>Department of Biosystems Science and Engineering, ETH Zurich, Mattenstrasse 26, 4058 Basel, Switzerland<br>niko.beerenwinkel@bsse.ethz.ch<br>AND S. SULLIVANT<br>Department of Mathematics, North Carolina State University, Raleigh, North Carolina 27607, U.S.A.<br>smsulli2@ncsu.edu

## SUMMARY

We introduce and analyze a waiting time model for the accumulation of genetic changes. The continuous-time conjunctive Bayesian network is defined by a partially ordered set of mutations and by the rate of fixation of each mutation. The partial order encodes constraints on the order in which mutations can fixate in the population, shedding light on the mutational pathways underlying the evolutionary process. We study a censored version of the model and derive equations for an EM algorithm to perform maximum likelihood estimation of the model parameters. We also show how to select the maximum likelihood partially ordered set. The model is applied to genetic data from cancer cells and from drug resistant human immunodeficiency viruses, indicating implications for diagnosis and treatment.

Some key words: Bayesian network; Cancer; Genetic progression; HIV; Partially ordered set; Poset.

## 1. INTRODUCTION

Pathogen evolution is characterized by recurrent phases of evolutionary escape from opposing selective pressure. During these stages several mutations are available to the population that increase fitness. Adaptive evolution proceeds by accumulating these beneficial genetic changes. For example, in HIV infection, the virus acquires mutations in cytotoxic T lymphocyte epitopes that interfere with the human immune response, while drug resistant mutations develop under antiviral treatment. Similarly, the genetic progression of cancer is characterized by the accumulation of mutations in oncogenes and tumor suppressor genes, which confer a selective advantage.

Evolutionary escape dynamics have been analyzed from a population genetics perspective. This approach clarified the influence of basic parameters such as population size and mutation rate on the risk of escape. It also highlighted the importance of the topology of escape, i.e. the structure of the possible mutational pathways (Iwasa et al., 2003; Beerenwinkel et al., 2006).

Here we introduce a model for the accumulation of genetic changes that allows for inference about the topology and the speed of evolutionary escape. The continuous-time conjunctive Bayesian network is a continuous-time Markov chain model, defined by a partially ordered set of advantageous mutations and their rates of fixation. The partial order encodes constraints on the succession in which mutations can occur and fixate in the population. We assume that the fixation

times follow independent exponential distributions. The waiting process for a mutation starts only when all of its predecessor mutations have occurred. The order constraints and waiting times reveal important information on the underlying biological process with implications for diagnosis and treatment. We exemplify the use of these Bayesian network models with the development of drug resistance in HIV and the genetic progression of prostate cancer.

The continuous-time conjunctive Bayesian network is a continuous-time analogue of the discrete conjunctive Bayesian network introduced by Beerenwinkel et al. (2006), which was shown to have very desirable statistical and algebraic properties (Beerenwinkel et al., 2007). Both networks are natural exponential families with closed-form expressions for maximum likelihood estimation and model selection. We argue that the continuous-time network is the more natural model for accumulating mutations, and we explore the connection to the discrete network.

One difference between the discrete and the continuous-time model is the state space. A state for the continuous-time model is a vector of time-points of the mutational events, while a state for the discrete model is a vector of binary indicators of the mutations. Despite the biological realism of the continuous-time model, the observed data rarely consist of the time-points of the genetic changes. Instead, we typically observe discrete genotypes at randomly sampled time-points. To address this discrepancy, we study a censored version of the continuous-time conjunctive Bayesian network and we derive an iterative algorithm for maximum likelihood estimation.

A special case of the discrete model, where the partially ordered set is a tree, is known as the oncogenetic or mutagenetic tree model (Desper et al., 1999; Beerenwinkel et al. 2005b, 2005c; Beerenwinkel \& Drton, 2007). It has been applied to the somatic evolution of cancer (Radmacher et al., 2001; Rahnenführer et al., 2005) and to the evolution of drug resistance in HIV (Beerenwinkel et al., 2005a). A related tree model by von Heydebreck et al. (2004) represents the genetic changes at the leaves of the tree and regards the interior vertices as hidden events. Several authors have considered larger model classes, including general Bayesian networks (Simon et al., 2000; Deforche et al., 2006) and more general Markov chain models (Foulkes \& DeGruttola, 2003; Hjelm et al., 2006). As compared to trees and partially ordered sets, these models are more flexible in describing mutational pathways, but parameter estimation and model selection is considerably more difficult. In fact, the number of free parameters of these models is typically exponential in the number of mutations, whereas in the continuous-time conjunctive Bayesian network, it is equal to the number of mutations. We demonstrate that parameter estimation and selection of an optimal partially ordered set can be performed efficiently for continuous-time conjunctive Bayesian networks which thus provide an attractive framework for modelling the accumulation of mutations, even if the number of mutations is moderate or large.

# 2. CONTINUOUS-TIME CONJUNCTIVE BAYESIAN NETWORKS 

In this section, we introduce and describe some of the basic properties of continuous-time conjunctive Bayesian networks. These models are continuous-time Markov chain models on the distributive lattice of a partially ordered set. We first review some background material from combinatorics; see also the introductory sections of Beerenwinkel et al. (2006) or Stanley (1999).

A partially ordered set $P$ has a binary relation $\prec$, which is reflexive, antisymmetric and transitive. In our models, the set $P$ will be a set of genetic events, and the relation specifies constraints on the order in which they occur: $p \prec q$ means that event $p$ happens before or at the same time as event $q$. We assume throughout that events that occur simultaneously have been collapsed in a pre-processing step. We say that $p$ is a parent of $q$ if $p \prec q$ and there is no element $r \in P$ such that $r \neq p, q$ and $p \prec r \prec q$. We use the notation $p \rightarrow q$ to denote that $p$ is a parent of $q$ and call $p \rightarrow q$ a cover relation. The set of all parents of an element $q$ is denoted

![img-0.jpeg](img-0.jpeg)

Fig. 1. Running example of a continuous-time conjunctive Bayesian network model.
by $\mathrm{pa}(q)$. The set of cover relations is used to visualize a partially ordered set by means of its Hasse diagram.

The distributive lattice of order ideals of $P$, denoted by $J(P)$, consists of all subsets $S \subseteq P$, that are closed downward, i.e. $S \in J(P)$ if and only if, for all $q \in S$ and $p \prec q$, we have that $p \in S$. The order ideals of $P$ correspond to the genotypes, or mutational patterns, that are compatible with the order constraints. We refer to $\emptyset \in J(P)$ as the wild type.

Example 1. As a running example, consider the partially ordered set $P$ on the four element set $[4]=\{1,2,3,4\}$ subject to the order relations $1 \prec 3,2 \prec 3,2 \prec 4$. The distributive lattice $J(P)$ of order ideals of $P$ consists of eight elements. Both sets are displayed in Fig. 1.

Let $P$ be a partially ordered set that equals $[n]$ as a set. For each event $i \in P$, we define a random variable $Z_{i} \sim \operatorname{Exp}\left(\lambda_{i}\right)$. Then we define the random variables $T_{i}=\max _{j \in \mathrm{pa}(i)} T_{j}+Z_{i}$ $(i=1, \ldots, n)$. The random variable $T_{i}$ describes how long we have to wait until event $i$ occurs, assuming that we start at time zero with no events. Mutation $i$ cannot occur until all the mutations preceding it in the partial order $P$ have occurred. The family of joint distributions of $T$ defined in this manner is the continuous-time conjunctive Bayesian network. It has state space $\mathbb{R}_{>0}^{n}$ consisting of vectors of waiting times and parameters $\lambda=\left(\lambda_{1}, \ldots, \lambda_{n}\right) \in \mathbb{R}_{>0}^{n}$.

The family of conjunctive Bayesian networks is not an a priori Bayesian family of models. The terminology Bayesian network comes from the graphical models community. For brevity, we will often refer to the continuous-time conjunctive Bayesian network as the continuous-time network, and to the discrete conjunctive Bayesian network as the discrete network.

The recursive definition of the discrete model implies that its probability density function is

$$
f_{P, \lambda}(t)= \begin{cases}\prod_{i=1}^{n} \lambda_{i} \exp \left\{-\lambda_{i}\left(t_{i}-\max _{j \in \mathrm{pa}(i)} t_{j}\right)\right\}, & t_{i}>\max _{j \in \mathrm{pa}(i)} t_{j}, i \in[n] \\ 0, & \text { otherwise }\end{cases}
$$

The continuous-time network is a regular exponential family, with minimal sufficient statistic consisting of the vector of time differences $\left(t_{i}-\max _{j \in \mathrm{pa}(i)} t_{j}\right)_{t \in[n]}$.

One instance of the random variable $T$ is a vector of time-points $t=\left(t_{1}, \ldots, t_{n}\right)$ that satisfy the inequality relations implied by $P$, i.e. $t_{i}>\max _{j \in \mathrm{pa}(i)} t_{j}$ for all $i \in[n]$. A set of time-points satisfying these constraints is compatible with the partially ordered set. The data for the model is a matrix of time-points $\left(t_{k i}\right)_{k \in[N], i \in[n]}$, where $N$ is the number of observations.

Proposition 1. Let $P$ be a partially ordered set and $\left(t_{k i}\right)$ be a collection of data. If any of the observations $t_{k}$. are incompatible with $P$, then the likelihood function is identical to zero.

Otherwise, the maximum likelihood estimate of $\lambda$ is

$$
\hat{\lambda}_{i}=\frac{N}{\sum_{k=1}^{N}\left(t_{k i}-\max _{j \in \mathrm{pa}(i)} t_{k j}\right)}, \quad i \in[n]
$$

Proof. If $t_{1}, \ldots, t_{N}$. are compatible with $P$, then the loglikelihood function is

$$
\ell\left(\lambda_{1}, \ldots, \lambda_{n}\right)=\sum_{k=1}^{N} \sum_{i=1}^{n}\left\{\log \lambda_{i}-\lambda_{i}\left(t_{k i}-\max _{j \in \mathrm{pa}(i)} t_{k j}\right)\right\}
$$

Differentiating with respect to $\lambda_{i}$ yields the equations

$$
\sum_{k=1}^{N}\left\{\frac{1}{\lambda_{i}}-\left(t_{k i}-\max _{j \in \mathrm{pa}(i)} t_{k j}\right)\right\}=0
$$

and the claimed formula follows by solving for $\lambda_{i}$.
THEOREM 1. Given data $\left(t_{k i}\right)$, the maximum likelihood partially ordered set is the largest partially ordered set that is compatible with the data.

Proof. Suppose that the data is compatible with two partially ordered sets $\left(P^{1}, \prec_{1}\right)$ and $\left(P^{2}, \prec_{2}\right)$, and that $P^{1}$ is a refinement of $P^{2}$ (i.e. every relation that holds in $P^{2}$ also holds in $P^{1}$ ). We show that the likelihood function at the maximum likelihood estimate is larger for $P^{1}$ than for $P^{2}$. This implies that adding relations compatible with the data increases the likelihood.

According to Proposition 1, the maximum likelihood estimates $\hat{\lambda}^{1}$ for $P^{1}$ and $\hat{\lambda}^{2}$ for $P^{2}$ are

$$
\hat{\lambda}_{i}^{l}=\frac{N}{\sum_{k=1}^{N}\left(t_{k i}-\max _{j \in \mathrm{pa}_{l}(i)} t_{k j}\right)}, \quad i \in[n], \quad l \in[2]
$$

We can replace $\mathrm{pa}_{l}(i)$ with the set $\left\{j \in P^{l} \mid j \prec_{l} i\right\}$. Since $P^{1}$ has more relations than $P^{2}$, this implies that the maximum is taken over a strictly larger set, and thus $\hat{\lambda}_{i}^{1} \geqslant \hat{\lambda}_{i}^{2}$ for all $i$.

However, the loglikelihood function evaluated at $\hat{\lambda}^{l}$ is

$$
\begin{aligned}
\ell_{l}\left(\hat{\lambda}^{l}\right) & =\sum_{k=1}^{N} \sum_{i=1}^{n}\left\{\log \hat{\lambda}_{i}^{l}-\hat{\lambda}_{i}^{l}\left(t_{k i}-\max _{j \in \mathrm{pa}_{l}(i)} t_{k j}\right)\right\} \\
& =\sum_{i=1}^{n}\left\{N \log \hat{\lambda}_{i}^{l}-\hat{\lambda}_{i}^{l} \sum_{k=1}^{N}\left(t_{k i}-\max _{j \in \mathrm{pa}_{l}(i)} t_{k j}\right)\right\} \\
& =\sum_{i=1}^{n}\left(N \log \hat{\lambda}_{i}^{l}-N\right)
\end{aligned}
$$

Since the logarithm is a monotone function, we deduce that $\ell_{1}\left(\hat{\lambda}^{1}\right) \geqslant \ell_{2}\left(\hat{\lambda}^{2}\right)$.
One of the most interesting quantities we can compute using the continuous-time network is the expected waiting time until a particular pattern $S \in J(P)$ is reached. Assuming that the parameters $\lambda$ are known, we are asking how long it takes until a set of genetic events have occurred. The expected waiting time is an important measure of genetic progression. Rahnenführer et al. (2005) have shown that it is a prognostic factor of survival and time to relapse in glioblastoma and prostate cancer patients, respectively, even after adjustment for traditional clinical markers.

Since the exponential distribution is memoryless, calculating the waiting time from the wild type will also determine the waiting time between any two patterns. Furthermore, the nature of

the conditional factorization for the joint density of $T$ implies that we can restrict attention to the case where $S=P$, i.e. to determining the waiting time until all events have occurred.

Let $S \in J(P)$ be an observable genotype. We define $\operatorname{Exit}(S)=\{j \in P \mid j \notin S, S \cup\{j\} \in$ $J(P)\}$ to be the set of events that have not occurred in $S$, but could occur next. For any subset $T \subseteq P$, we set $\lambda_{T}=\sum_{j \in T} \lambda_{j}$. A chain in the distributive lattice $J(P)$ is a collection of subsets $C_{0}, C_{1}, \ldots, C_{k} \in J(P)$ that satisfy $C_{i} \subset C_{i+1}$ and $C_{i} \neq C_{i+1}$, for all $i$. A chain is maximal, if it is as long as possible. All maximal chains in the distributive lattice $J(P)$ have length $n+1$ with $n=|P|$ and start with $C_{0}=\emptyset$ and end with $C_{n}=P$. Let $\mathcal{C}\{J(P)\}$ denote the collection of maximal chains in $J(P)$; a typical element is denoted by $C=\left(C_{0}, \ldots, C_{n}\right)$.

THEOREM 2. The expected waiting time until all events have occurred is

$$
E\left(\max _{i \in P} T_{i}\right)=\lambda_{1} \cdots \lambda_{n} \sum_{C \in \mathcal{C}\{J(P)\}}\left(\prod_{i=0}^{n-1} \frac{1}{\lambda_{\operatorname{Exit}\left(C_{i}\right)}}\right)\left(\sum_{i=0}^{n-1} \frac{1}{\lambda_{\operatorname{Exit}\left(C_{i}\right)}}\right)
$$

Before proving Theorem 2, we sketch the idea of the proof, which is a common technique for proofs throughout the paper. The indicated expectation involves the integral of a function that depends on maxima, which are not simple to integrate directly. We first decompose the integral into a sum of integrals over many different regions, one for each maximal chain in $J(P)$. Over these simpler regions, the maximum function disappears. Furthermore, these regions are each simplicial cones and the integral can then be computed by a simple change of coordinates.

Proof. Let $f(t)$ be the density function from equation (1). We must compute

$$
\int_{\mathbb{R}_{>0}^{n}} \max _{i \in P} t_{i} f(t) d t
$$

Let $S_{n}$ denote the symmetric group on $n$ letters with $\sigma=\left(\sigma_{1}, \ldots, \sigma_{n}\right)$ a typical element. The integral (2) over the positive orthant breaks up as the sum

$$
\sum_{\sigma \in S_{n}} \int_{t_{\sigma_{1}}=0}^{\infty} \int_{t_{\sigma_{2}}=t_{\sigma_{1}}}^{\infty} \cdots \int_{t_{\sigma_{n}}=t_{\sigma_{n-1}}}^{\infty} t_{\sigma_{n}} f(t) d t
$$

That is, the sum breaks up the integral into smaller integrals over regions $0<t_{\sigma_{1}}<\cdots<t_{\sigma_{n}}$. The integrand is zero unless $\sigma_{1}, \ldots, \sigma_{n}$ is a linear extension of $P$. In other words, the integrand is zero unless the sets $C_{i}=\cup_{j=1}^{i}\left\{\sigma_{j}\right\}$ for $i=0, \ldots, n$ form a maximal chain in the distributive lattice $J(P)$. So suppose that $\sigma$ is a linear extension of $P$. Without loss of generality, we may suppose that this linear extension is $1 \prec \cdots \prec n$. We must compute the integral

$$
\int_{t_{1}=0}^{\infty} \int_{t_{2}=t_{1}}^{\infty} \cdots \int_{t_{n}=t_{n-1}}^{\infty} t_{n} f(t) d t
$$

where, over this restricted region, $f(t)$ now has the form

$$
f(t)=\prod_{i=1}^{n} \lambda_{i} \exp \left\{-\lambda_{i}\left(t_{i}-t_{j(i)}\right)\right\}
$$

where $j(i)$ is the largest number with $j(i) \prec i$ in $P$.
Now introduce the change of coordinates $u_{0}=t_{1}, u_{i}=t_{i+1}-t_{i}, i \in[n-1]$. The determinant of this linear transformation is one, so the integral becomes

$$
\int_{u_{0}=0}^{\infty} \cdots \int_{u_{n-1}=0}^{\infty}\left(u_{0}+\cdots+u_{n-1}\right) \prod_{i=1}^{n} \lambda_{i} \exp \left\{-\lambda_{i}\left(u_{i-1}+u_{i-2}+\cdots+u_{j(i)}\right)\right\} d u
$$

The multiple integral is now over a product domain, and involves a function in product form, so we want to break (3) into the product of integrals. To do this, we must collect the $\lambda_{i}$ terms that go with the various $u_{k}$ terms. In the exponent, we have that $\lambda_{i}$ appears as a coefficient of $u_{k}$ if and only if $i>k \geqslant j(i)$. This, in turn, implies that when all the events $1, \ldots, k$ have occurred, all the predecessor events of $i$ have occurred. This means that $i \in \operatorname{Exit}\left(C_{k}\right)$, where $C_{k}=\{1, \ldots, k\}$. Thus, the transformed integral breaks up as a sum of $n$ integrals that have the form:

$$
\lambda_{1} \cdots \lambda_{n} \int_{u_{0}=0}^{\infty} \cdots \int_{u_{n-1}=0}^{\infty} u_{j} \prod_{i=0}^{n-1} \exp \left\{-\lambda_{\operatorname{Exit}\left(C_{i}\right)} u_{i}\right\} d u
$$

The integral is over a product domain of a product function, so equals

$$
\lambda_{1} \cdots \lambda_{n} \frac{1}{\lambda_{\operatorname{Exit}\left(C_{j}\right)}} \prod_{i=0}^{n-1} \frac{1}{\lambda_{\operatorname{Exit}\left(C_{i}\right)}}
$$

which completes the proof.
Theorem 2 yields a formula for the expected waiting time until all mutations have occurred, which, at first glance seems to require the enumeration of all maximal chains in the distributive lattice $J(P)$. However, this sum can be computed by a dynamic programming algorithm.

Proposition 2. For each $S \in J(P)$ define $P_{S}$ and $E_{S}$ by

$$
\begin{aligned}
& P_{S}=\sum_{j \in S: S \backslash\{j\} \in J(P)} \frac{\lambda_{j}}{\lambda_{\operatorname{Exit}\left(S \backslash\{j\}\right)}} P_{S \backslash\{j\}} \\
& E_{S}=\sum_{j \in S: S \backslash\{j\} \in J(P)}\left(\frac{\lambda_{j}}{\lambda_{\operatorname{Exit}\left(S \backslash\{j\}\right)}} E_{S \backslash\{j\}}+\frac{\lambda_{j}}{\lambda_{\operatorname{Exit}\left(S \backslash\{j\}\right)}^{2}} P_{S \backslash\{j\}}\right)
\end{aligned}
$$

subject to the initial conditions $P_{\emptyset}=1$ and $E_{\emptyset}^{i}=0$. Then $E\left(\max _{i \in P} T_{i}\right)=E_{[n]}$.
We omit the proof of Proposition 2, which closely follows the proof of Proposition 4 below.

# 3. Relation to the Discrete Conjunctive Bayesian Network 

In this section, we explore the connection between the continuous-time and the discrete network (Beerenwinkel et al., 2007). We want to understand how the models relate to each other and how structural information from one model yields information about the other. We are naturally led to study discrete models because we rarely have access to the times at which the individual events occurred, but can only observe which events have occurred after a certain sampling time.

We will show that the discrete network gives a first-order approximation to the transition probabilities in the continuous-time network. This suggests that the discrete network is not optimal from a modelling standpoint as the nature of our applications is to wait until mutations occur. However, the discrete model is much simpler to work with, and its maximum likelihood estimates can be used as an initial step in iterative algorithms for maximum likelihood estimation in the censored versions of the continuous-time network described in $\S 4$.

To derive this result, we consider the continuous-time network as a continuous-time Markov chain on the distributive lattice $J(P)$. See Norris (1997) for background on Markov chains. The

rate matrix for the Markov chain is the $m \times m$ matrix $Q$, where $m=|J(P)|$, defined by

$$
Q_{S, T}= \begin{cases}\lambda_{j}, & S \subset T, T \backslash S=\{j\} \\ -\lambda_{\operatorname{Exit}(S)}, & S=T \\ 0, & \text { otherwise }\end{cases}
$$

for all $S, T \in J(P)$. If we fix a linear extension of $J(P)$ and order the rows and columns of $Q$ according to this linear extension, $Q$ will be an upper triangular matrix.

Let $p(t)$ be the $m \times m$ matrix where, for $S, T \in J(P)$, the entry $p_{S, T}(t)$ denotes the probability that the continuous-time Markov chain with state space $J(P)$, is in state $T$ at time $t$ starting from state $S$ at time 0 . This quantity can be calculated by integrating the density function from the continuous-time model. However, it is simpler to use standard theory of Markov chains. The matrix $p(t)$ is the solution of the system of differential equations $d p(t) / d t=Q p(t)$ subject to the initial conditions $p(0)=I$, the identity matrix. The solution to this first-order differential equation is the matrix exponential $p(t)=\exp (Q t)$. It satisfies $\left.d^{k} p(t) / d t^{k}\right|_{t=0}=Q^{k}$. So a firstorder approximation to $p(t)$ is a function $\tilde{p}(t)$ that satisfies $\tilde{p}(0)=I$ and $d \tilde{p}(t) / d t \mid t=0=Q$.

The first-order approximation can be derived as follows. Associated to the discrete network are $n$ parameters $\theta_{1}, \ldots, \theta_{n}$, where $\theta_{i}$ is the conditional probability that event $i$ has occurred, given that all its predecessor events have occurred. By setting $\theta_{i}=1-\exp \left(-\lambda_{i} t\right)$ and defining

$$
\tilde{p}_{S, T}(t)= \begin{cases}\prod_{i \in T \backslash S} \theta_{i} \prod_{i \in \operatorname{Exit}(T)}\left(1-\theta_{i}\right), & S \subseteq T \\ 0, & \text { otherwise }\end{cases}
$$

the discrete model is naturally interpreted as a continuous-time model, where $\tilde{p}_{S, T}(t)$ is the probability that the discrete model is in state $T$ at time $t$ given an initial state $S$ at time 0 .

Proposition 3. The model $\tilde{p}(t)$ derived from the discrete conjunctive Bayesian network is a first-order approximation to the continuous-time conjunctive Bayesian network $p(t)$.

Proof. Diagonal entries of $\tilde{p}(t)$ have the form $\prod \exp \left(-\lambda_{i} t\right)$, and off-diagonal entries are either identical to zero or are a product of terms, at least one of which is of the form $1-\exp \left(-\lambda_{i} t\right)$. This implies that $\tilde{p}(0)=I$.

If $T=S$, then $\tilde{p}_{S, S}(t)=\prod_{i \in \operatorname{Exit}(S)} \exp \left(-\lambda_{i} t\right)$. So, by the product rule

$$
\frac{d}{d t} \tilde{p}_{S, S}(t)=\sum_{i \in \operatorname{Exit}(S)}-\lambda_{i} \tilde{p}_{S, S}(t)
$$

and thus $\left.d \tilde{p}_{S, S}(t) / d t\right|_{t=0}=-\lambda_{\operatorname{Exit}(S)}=Q_{S, S}$. If $S \subset T$ then

$$
\tilde{p}_{S, T}(t)=\prod_{i \in T \backslash S}\left\{1-\exp \left(-\lambda_{i} t\right)\right\} \prod_{i \in \operatorname{Exit}(T)} \exp \left(-\lambda_{i} t\right)
$$

and thus

$$
\frac{d}{d t} \tilde{p}_{S, T}(t)=\sum_{i \in T \backslash S} \lambda_{i} \frac{\exp \left(-\lambda_{i} t\right)}{1-\exp \left(-\lambda_{i} t\right)} \tilde{p}_{S, T}(t)-\sum_{i \in \operatorname{Exit}(T)} \lambda_{i} \tilde{p}_{S, T}(t)
$$

If $T \backslash S$ has cardinality greater than one, then $\left.d \tilde{p}_{S, T}(t) / d t\right|_{t=0}=0=Q_{S, T}$, because every term in the sum involves at least one expression of the form $1-\exp \left(-\lambda_{i} t\right)$. On the other hand, if $T=S \cup\{j\}$, then $\left.d \tilde{p}_{S, T}(t) / d t\right|_{t=0}=\lambda_{j}=Q_{S, T}$, because only the first term in the sum does not contain an expression of the form $1-\exp \left(-\lambda_{i} t\right)$. As all other entries in $\tilde{p}(t)$ and $Q$ are zero, this proves that $\tilde{p}(t)$ is a first-order approximation to $p(t)$.

Given that the discrete model is a first-order approximation to the continuous-time model, it seems natural to conjecture that these two models are equal. If $P$ is the partially ordered set with no relations, then the two models coincide. However, if $P$ contains at least one relation, the models are no longer the same, and the discrete network is not even a second-order approximation to the continuous-time network. This is illustrated in the following example.

Example 2. Let $P$ be the partially ordered set on two elements with one relation $1 \prec 2$ and fix the natural order $\emptyset,\{1\},\{1,2\}$ in $J(P)$. If $\lambda_{1} \neq \lambda_{2}$, then

$$
\begin{aligned}
& \tilde{p}(t)=\left\{\begin{array}{ccc}
e^{-\lambda_{1} t} & \left(1-e^{-\lambda_{1} t}\right) e^{-\lambda_{2} t} & \left(1-e^{-\lambda_{1} t}\right)\left(1-e^{-\lambda_{2} t}\right) \\
0 & e^{-\lambda_{2} t} & 1-e^{-\lambda_{2} t} \\
0 & 0 & 1
\end{array}\right\}, \\
& p(t)=\left\{\begin{array}{ccc}
e^{-\lambda_{1} t} & \left\{\lambda_{1} /\left(\lambda_{1}-\lambda_{2}\right)\right\}\left(e^{-\lambda_{2} t}-e^{-\lambda_{1} t}\right) & 1-\left(\lambda_{1} e^{-\lambda_{2} t}-\lambda_{2} e^{-\lambda_{1} t}\right) /\left(\lambda_{1}-\lambda_{2}\right) \\
0 & e^{-\lambda_{2} t} & 1-e^{-\lambda_{2} t} \\
0 & 0 & 1
\end{array}\right\} .
\end{aligned}
$$

In particular, $\left.d^{2} \tilde{p}_{\emptyset,\{1\}}(t) /\left.d t^{2}\right|_{t=0}=-\lambda_{1}^{2}-2 \lambda_{1} \lambda_{2}$, whereas $\left(Q^{2}\right)_{\emptyset,\{1\}}=-\lambda_{1}^{2}-\lambda_{1} \lambda_{2}$.
The discrepancies exhibited in this example become more dramatic as $P$ develops longer chains. While the discrete network is not identical to the continuous-time network, its nice properties can be exploited at various points during optimization.

# 4. CENSORING 

In this section, we define and analyze the censored continuous-time conjunctive Bayesian network model that we will apply to genetic data in $\S 5$. The reason for introducing censoring is that we typically do not know the time-points $t_{1}, \ldots, t_{n}$ at which the events have occurred. Often we can only measure, at a particular time, which of the events have occurred so far. It is natural to assume that the observation times are also random. For example, HIV drug resistance mutations can only be detected after therapy failure.

We introduce a new event $s$ for the sampling process, such that the random variable $T_{s}$ is an independent, exponentially distributed waiting time (the sampling time, or observation time), $T_{s} \sim \operatorname{Exp}\left(\lambda_{s}\right)$. We define a new partially ordered set $P_{s}=P \cup\{s\}$ by adding the element $s$ with no relations to the other elements in $P$. An observed mutational pattern $S \subseteq[n]$ results from the event $T_{i}<T_{s}$ for all $i \in S$ and $T_{s}<T_{i}$ for all $i \in[n] \backslash S$.

An observed set of events, $S$, imposes extra relations $i \prec s$ for $i \in S$ and $s \prec i$ for $i \in[n] \backslash S$ on the partially ordered set $P_{s}$, and we are led to study this refined poset $Q_{S}$.

A realization of the random vector $T$ is said to be compatible with $Q$, denoted by $T \vdash Q$, if $T_{i}<T_{j}$ whenever $i \prec j$ in $Q$. We can directly compute the probability of the event $T \vdash Q$ in terms of the distributive lattices $J(Q)$ and $J\left(P_{s}\right)$. Throughout this section, we abuse notation and say that $T \sim P_{s}$ if $T=\left(T_{s}, T_{1}, \ldots, T_{n}\right)$ is distributed according to the continuous-time conjunctive Bayesian network associated to $P_{s}$ with parameter vector $\lambda=\left(\lambda_{s}, \lambda_{1}, \ldots, \lambda_{n}\right)$.

THEOREM 3. The probability that $T \sim P_{s}$ is compatible with the partially ordered set $Q$ is

$$
\operatorname{pr}(T \vdash Q)=\lambda_{s} \lambda_{1} \cdots \lambda_{n} \sum_{C \in C(J(Q))} \prod_{i=0}^{n} \frac{1}{\lambda_{\operatorname{Exit}\left(C_{i}\right)}}
$$

where the sum runs over all maximal chains in the distributive lattice $J(Q)$.

Remark 1. In this formula, and in all formulae throughout this section, the expression Exit $(S)$ always refers to the underlying partially ordered set $P_{s}$ and not to the refinement $Q$.

Proofof Theorem 3. We must compute the integral

$$
\int_{\mathbb{R}_{>0}^{n+1}} \mathbb{I}_{Q}(t) f(t) d t
$$

where $\mathbb{I}_{Q}(t)$ is the indicator function of compatibility with $Q$. The integral breaks up into a sum over the linear extensions of $Q$ over regions over the form $t_{\sigma_{0}}<\cdots<t_{\sigma_{n}}$. Without loss of generality and after renaming the elements of $P_{s}$, we can assume that the linear extension of interest is $0 \prec \cdots \prec n$. We must calculate the integral

$$
\int_{t_{0}=0}^{\infty} \int_{t_{1}=t_{0}}^{\infty} \cdots \int_{t_{n}=t_{n-1}}^{\infty} f(t) d t
$$

where over the restricted region, the integrand has the form

$$
f(t)=\prod_{i=0}^{n} \lambda_{i} \exp \left\{-\lambda_{i}\left(t_{i}-t_{j(i)}\right)\right\}
$$

With the change of variables $u_{0}=t_{0}$ and $u_{i+1}=t_{i+1}-t_{i}, i \in[n]$, the integral becomes

$$
\prod_{i=0}^{n} \int_{u_{i}=0}^{\infty} \exp \left(-\lambda_{\operatorname{Exit}\left(C_{i}\right)} u_{i}\right) d u_{i}
$$

where $C_{i}=\{0,1, \ldots, i-1\}$. This yields the desired contribution to the integral.
Example 3. Let $P$ be the partially ordered set from Example 1 with relations $1 \prec 3,2 \prec 3$ and $2 \prec 4$, and consider the partially ordered set $P_{s}=P \cup\{s\}$ with no additional relations. Suppose we want to calculate the probability of mutations 2 and 4 occurring before measurement. The refinement $Q_{2,4}$ corresponding to the genotype $\{2,4\}$ is a chain $2 \prec 4 \prec s \prec 1 \prec 3$, and so the distributive lattice $J\left(Q_{2,4}\right)$ is also a chain. From equation (4), the probability of $T \vdash Q_{2,4}$ is

$$
\lambda_{1} \lambda_{2} \lambda_{3} \lambda_{4} \lambda_{s} \frac{1}{\lambda_{1}+\lambda_{2}+\lambda_{s}} \frac{1}{\lambda_{1}+\lambda_{4}+\lambda_{s}} \frac{1}{\lambda_{1}+\lambda_{s}} \frac{1}{\lambda_{1}} \frac{1}{\lambda_{3}}
$$

On the other hand, the distributive lattice $J\left(Q_{1,2}\right)$ has four chains and $\operatorname{pr}\left(T \vdash Q_{1,2}\right)$ is the sum of four terms of product form. The expression can be written as

$$
\frac{\lambda_{1} \lambda_{2} \lambda_{3} \lambda_{4} \lambda_{s}}{\left(\lambda_{1}+\lambda_{2}+\lambda_{s}\right)\left(\lambda_{3}+\lambda_{4}+\lambda_{s}\right)\left(\lambda_{3}+\lambda_{4}\right)}\left(\frac{1}{\lambda_{2}+\lambda_{s}}+\frac{1}{\lambda_{1}+\lambda_{4}+\lambda_{s}}\right)\left(\frac{1}{\lambda_{3}}+\frac{1}{\lambda_{4}}\right)
$$

A general recursive formula for this probability is given in Proposition 4.
We now consider binary random variables $X_{1}, \ldots, X_{n}$, each indicating the occurrence of a genetic event. Given a partially ordered set $P$, we define the discrete censored continuous-time conjunctive Bayesian network as the family of probability distributions

$$
\operatorname{pr}\left(X_{1}=x_{1}, \ldots, X_{n}=x_{n}\right)=\operatorname{pr}\left(T \vdash Q_{S}\right)
$$

where $x_{i} \in\{0,1\}, T \sim P_{s}$ and $S=\left\{i \in[n] \mid x_{i}=1\right\}$. This model has state space $\{0,1\}^{n}$, the set of all genotypes of length $n$, and parameters $\lambda=\left(\lambda_{s}, \lambda_{1}, \ldots, \lambda_{n}\right) \in \mathbb{R}_{>0}^{n+1}$. Although $n+1$ parameters specify the model, it has dimension $n$, because $\lambda$ can be rescaled.

Unlike in the fully observed continuous-time network or the discrete network, we have found no general closed-form expressions for the maximum likelihood estimates of the parameters of

the censored model. However, as the censored model is a marginalization of the continuous-time network, which is a regular exponential family, we can use the EM algorithm to find maximum likelihood estimates. While the EM algorithm is only guaranteed to find a local maximum of the likelihood function, our computational experience has been that using exact maximum likelihood estimates from the discrete conjunctive Bayesian network for $\theta_{i}$ and solving for $\lambda_{i}$ in the approximate expression $\theta_{i}=\lambda_{i} /\left(\lambda_{i}+\lambda_{s}\right)$ works as a good starting guess.

In the EM algorithm, we start with a guess for the maximum likelihood parameters $\lambda^{*}$ and compute the expected values of the sufficient statistics of the fully observed model, given the data. Specifically, for each observed $S \subseteq[n]$ and each $i \in[n]$, we compute the expected value

$$
E\left(T_{i}-\max _{j \in \mathrm{pa}(i)} T_{j} \mid T \vdash Q_{S}\right)
$$

This is the E-step of the algorithm. In the M-step, the expected sufficient statistics are used to compute maximum likelihood estimates for $\lambda$ in the fully observed model. The EM algorithm iterates alternations of the E-step and the M-step. In each iteration, the likelihood function increases and a fixed point is a critical point of the likelihood function. The M-step is calculated by Proposition 1, while, in the E-step, we have the following formula for the expected value (5).

THEOREM 4. The expected value of $T_{i}-\max _{j \in \mathrm{pa}(i)} T_{j}$ given that $T$ is compatible with $Q$ is

$$
E\left(T_{i}-\max _{j \in \mathrm{pa}(i)} T_{j} \mid T \vdash Q\right)=\frac{\lambda_{s} \lambda_{1} \cdots \lambda_{n}}{\operatorname{pr}(T \vdash Q)} \sum_{C \subset \mathcal{C}[J(Q)]} \frac{1}{\lambda_{\operatorname{Exit}\left(C_{k}\right)}}\left\{\sum_{l=0}^{n} \frac{\iota\left(i, C_{l}\right)}{\lambda_{\operatorname{Exit}\left(C_{l}\right)}}\right\}
$$

where the first sum is over all maximal chains in $J(Q)$ and

$$
\iota\left(i, C_{k}\right)= \begin{cases}1, & i \notin C_{k}, \mathrm{pa}(i) \subseteq C_{k} \\ 0, & \text { otherwise }\end{cases}
$$

Proof. The proof follows the pattern of the proof of Theorem 2. The expected value is

$$
E\left(T_{i}-\max _{j \in \mathrm{pa}(i)} T_{j} \mid T \vdash Q\right)=\frac{1}{\operatorname{pr}(T \vdash Q)} \int_{\mathbb{R}_{\geqslant 0}^{n+1}}\left(t_{i}-\max _{j \in \mathrm{pa}(i)} t_{j}\right) \mathbb{I}_{Q}(t) f(t) d t
$$

We can calculate the integral by decomposing it into a sum over the linear extensions of $Q$, i.e. the chains in the distributive lattice $J(Q)$. Without loss of generality, we can suppose that the linear extension is called $0 \prec \cdots \prec n$. For this linear extension, the integral becomes

$$
\int_{t_{0}=0}^{\infty} \int_{t_{1}=t_{0}}^{\infty} \cdots \int_{t_{n}=t_{n-1}}^{\infty}\left(t_{i}-t_{j(i)}\right) f(t) d t
$$

and over this region $f(t)=\prod_{k=0}^{n} \lambda_{k} \exp \left\{-\lambda_{k}\left(t_{k}-t_{j(k)}\right)\right\}$. Applying the usual change of coordinates, we can rewrite the integral in product form as

$$
\int_{u_{0}=0}^{\infty} \cdots \int_{u_{n}=0}^{\infty}\left(u_{i-1}+\cdots+u_{j(i)}\right) \prod_{k=0}^{n} \lambda_{k} \exp \left\{-\lambda_{k}\left(u_{k-1}+u_{k-2}+\cdots+u_{j(k)}\right)\right\} d u
$$

Breaking this integral up as a sum yields a collection of integrals we have already computed in the proof of Theorem 2. However, each term

$$
\prod_{k=0}^{n} \frac{1}{\lambda_{\operatorname{Exit}\left(C_{k}\right)}} \frac{1}{\lambda_{\operatorname{Exit}\left(C_{l}\right)}}
$$

contributes to the sum, if and only if $i \in \operatorname{Exit}\left(C_{l}\right)$, i.e. if and only if $\iota\left(i, C_{l}\right)=1$.

Rather than computing the expectation from Theorem 4 by explicitly listing all maximal chains in the distributive lattice $J(Q)$, the expected value can be computed recursively, by summing up the distributive lattice. This dynamic programming approach reduces the computational burden of computing the expectation, because one need not enumerate all maximal chains in $J(Q)$.

Proposition 4. For each $S \in J(Q)$ define $P_{S}$ and $E_{S}^{i}$ by the formulae

$$
\begin{aligned}
& P_{S}=\sum_{j \in S: S \backslash\{j\} \in J(Q)} \frac{\lambda_{j}}{\lambda_{\operatorname{Exit}(S \backslash\{j\})}} P_{S \backslash\{j\}} \\
& E_{S}^{i}=\sum_{j \in S: S \backslash\{j\} \in J(Q)}\left\{\frac{\lambda_{j}}{\lambda_{\operatorname{Exit}(S \backslash\{j\})}} E_{S \backslash\{j\}}^{i}+\iota(i, S \backslash\{j\}) \frac{\lambda_{j}}{\lambda_{\operatorname{Exit}(S \backslash\{j\})}^{2}} P_{S \backslash\{j\}}\right\}
\end{aligned}
$$

subject to the initial conditions $P_{\emptyset}=1$ and $E_{\emptyset}^{i}=0$, where

$$
\iota(i, S \backslash\{j\})=\left\{\begin{array}{ll}
1, & i \notin S \backslash\{j\}, \operatorname{pa}(i) \subseteq S \backslash\{j\} \\
0, & \text { otherwise }
\end{array}\right.
$$

Then $\operatorname{pr}(T \vdash Q)=P_{\{s\} \cup[n]}$ and $E\left(T_{i}-\max _{j \in \operatorname{pa}(i)} T_{j} \mid T \vdash Q\right)=E_{\{s\} \cup[n]}^{i} / P_{\{s\} \cup[n]}$.
Proof. Both results follow from writing down a closed-form expression for $P_{S}$ and $E_{S}^{i}$, proving that these formulae hold inductively, and showing that $P_{\{s\} \cup[n]}=\operatorname{pr}(T \vdash Q)$ and $E_{\{s\} \cup[n]}^{i} /$ $P_{\{s\} \cup[n]}=E\left(T_{i}-\max _{j \in \operatorname{pa}(i)} T_{j} \mid T \vdash Q\right)$.

To this end, let $\left.Q\right|_{S}$ be the induced sub-partially ordered set of $Q$ with element set $S$. Then

$$
P_{S}=\prod_{i \in S} \lambda_{i} \sum_{C \in \mathcal{C}\left\{J\left(Q_{S}\right)\right\}} \prod_{i=0}^{\lfloor S \mid-1} \frac{1}{\lambda_{\operatorname{Exit}\left(C_{i}\right)}}
$$

with $P_{\emptyset}=1$. The recurrence

$$
P_{S}=\sum_{j \in S: S \backslash\{j\} \in J(Q)} \frac{\lambda_{j}}{\lambda_{\operatorname{Exit}(S \backslash\{j\})}} P_{S \backslash\{j\}}
$$

is satisfied because every maximal chain in $J\left(\left.Q\right|_{S}\right)$ comes from a maximal chain in exactly one of the $J\left(\left.Q\right|_{S \backslash\{j\}}\right)$ by adding $j$ to $\left.Q\right|_{S \backslash\{j\}}$ as the last element. Also, $P_{\{s\} \cup[n]}$ has the desired form.

Similarly, it is straightforward to show that

$$
E_{S}^{i}=\prod_{k \in S} \lambda_{k} \sum_{C \subset \mathcal{C}\left\{J\left(Q_{S}\right)\right\}}\left(\prod_{k=0}^{\mid S \mid-1} \frac{1}{\lambda_{\operatorname{Exit}\left(C_{k}\right)}}\right)\left\{\sum_{k=0}^{\mid S \mid-1} \frac{\iota\left(i, C_{k}\right)}{\lambda_{\operatorname{Exit}\left(C_{k}\right)}}\right\}
$$

which, together with $P_{S}$, above, satisfies the desired recurrence relation.

# 5. Applications 

## 5$\cdot$1. Noise model

Theorem 1 states that the structure of the maximum likelihood continuous-time conjunctive Bayesian network is given by the maximal partially ordered set that is compatible with the data. In practice, however, the observations are subject to noise, either due to deviations of the data generating process from the model, or due to technical limitations in assessing genetic changes experimentally. Thus, for most biomedical datasets, the maximum likelihood partially ordered

set will have few relations, although many observations might support more order constraints. We address this problem using a simple mixture model (Beerenwinkel et al., 2007).

For the censored model (4) and observed data $u:\{0,1\}^{n} \rightarrow \mathbb{N}_{\geqslant 0}$, where $u_{g}$ denotes the count of genotype $g$ in the data, we define a family of partially ordered sets $P_{\epsilon}, 0 \leqslant \epsilon \leqslant 1$, as follows. We consider all possible relations in ascending order of the number of observations that they violate. Starting with the partially ordered set $P_{\epsilon}$ with no relation, we add, in a greedy fashion, each relation $i \prec j$, if the number of its violations is smaller than $N \epsilon$ and if $j \prec i$ is not in $P_{\epsilon}$.

We assume that incompatible genotypes are generated with uniform probability $q_{\epsilon}=1 /\left(2^{n}-\right.$ $\left.\left|J\left(P_{\epsilon}\right)\right|\right)$ and consider the extended censored model with probabilities

$$
\operatorname{pr}\left(T_{\epsilon} \vdash Q \mid \alpha, \lambda\right)= \begin{cases}\alpha \operatorname{pr}\left(T_{\epsilon} \vdash Q \mid \lambda\right), & \text { if } Q \text { refines } P_{\epsilon} \\ (1-\alpha) q_{\epsilon}, & \text { otherwise }\end{cases}
$$

where $T_{\epsilon} \sim P_{\epsilon}$ and $\alpha=\sum_{g \in J\left(P_{\epsilon}\right)} u_{g} / \sum_{g \in 2^{[\alpha]}} u_{g}$ denotes the fraction of data compatible with $P_{\epsilon}$. The model can be regarded as a mixture model with $\alpha$ the maximum likelihood estimate of the mixing parameter.

In the applications, we construct partially ordered sets $P_{\epsilon}$ for various values of $\epsilon$ and select the one that maximizes the likelihood of the extended model. A software implementation of the model including the algorithms for model selection and parameter estimation is available at http://www.cbg.ethz.ch/software/ct-cbn.

# 5.2. Cancer data 

We first use the extended censored model to analyze the genetic progression of prostate cancer. The random variables $T_{i}$ denote the times of fixation of genetic changes in the population of cancer cells. Genetic changes were assessed by comparative genome hybridization experiments. This technique detects large-scale genomic alterations, namely the gain or loss of chromosome arms.

For example, the event $4 \mathrm{q}+$ denotes the gain $(+)$ of additional copies of the large (q) arm of chromosome 4. Likewise, $8 \mathrm{p}-$ refers to the loss $(-)$ of the small arm (p) of chromosome 8. We consider 54 prostate cancer samples, each defined by the presence or absence of the nine alterations $3 \mathrm{q}^{+}, 4 \mathrm{q}^{+}, 6 \mathrm{q}^{+}, 7 \mathrm{q}^{+}, 8 \mathrm{p}-, 8 \mathrm{q}^{+}, 10 \mathrm{q}-, 13 \mathrm{q}+$ and $\mathrm{Xq}+$ (Rahnenführer et al., 2005).

In Fig. 2(a), the loglikelihood is shown as a function of the fraction of incompatible genotypes. The partially ordered set that maximizes the likelihood explains $89 \%$ of the data and is displayed in Fig. 2(b). Four of the nine genetic changes do not obey any relation, two events have one direct predecessor and one event occurs only after two parent events have occurred. The second best partially ordered set is the one with no relations, corresponding to $\alpha=1$.

In order to assess the uncertainty associated with parameter estimation and model selection, we performed two independent bootstrap analyses comprising 10000 samples, each of size $N=\sum_{g} u_{g}=54$. First, we fixed the optimal partially ordered set, Fig. 2(b), and re-estimated the model parameters $\lambda_{i}$. The quartiles of the distributions are displayed in Table 1. The stability of optimal partially ordered sets was assessed by repeated model selection with a fixed tolerance parameter of $\epsilon=0.05$, the value that had given rise to the optimal partial order with $\alpha=0.89$. Figure 3 summarizes separately the cover relations and all relations that appeared in the bootstrap partially ordered sets. This analysis supports exactly the relations encoded in the partially ordered set of Fig. 2(b), especially the sequence $4 \mathrm{q}^{+} \prec 8 \mathrm{q}^{+} \prec 13 \mathrm{q}^{+}$, and $3 \mathrm{q}^{+}$as a late event.

### 5.3. HIV data

Our second application is concerned with the evolution of drug resistance in HIV. We study the accumulation of amino acid changes in the viral target protein reverse transcriptase. The seven

![img-1.jpeg](img-1.jpeg)

Fig. 2. Maximum likelihood estimation of the discrete censored continuous-time conjunctive Bayesian network model for the prostate cancer data. In (a), the loglikelihood is displayed as a function of the fraction of data that is incompatible with the partially ordered set. The curve has been generated by densely sampling $\epsilon$ from the unit interval and estimation of the extended models $P_{\epsilon}$. The optimal prostate cancer partially ordered set corresponding to the maximum of the graph is displayed in panel (b). An arrow $p \rightarrow q$ between two genetic events represents the cover relation $p \prec q$ in the Hasse diagram.

Table 1. Bootstrap analysis of model parameters for the optimal prostate cancer partially ordered set of Fig. 2. The partially ordered set structure is repeated by listing the parents of each genetic event, i.e. chromosomal alteration. The quartiles of the distribution of each parameter $\lambda_{i}$ are given in columns Q1, $25 \%$ quantiles; Q2, $50 \%$ quantiles, median; and $Q 3,75 \%$ quantiles


resistance-associated mutations 41L, 67N, 69D, 70R, 210W, 215Y and 219Q (Johnson et al., 2008) are considered, where, for example, 41 L indicates the presence of the amino acid leucine at position 41 of the reverse transcriptase. A total of 364 viruses are analyzed that have been isolated from infected patients under antiretroviral therapy. Here the random variables $T_{i}$ denote the fixation times of the mutations in the virus population.

The optimal partially ordered set for the HIV drug resistance data explains $87 \%$ of the observations, Fig. 4(a). Its Hasse diagram has two connected components, Fig. 4(b). The first one represents the linear pathway $215 \mathrm{Y} \prec 41 \mathrm{~L} \prec 210 \mathrm{~W}$, and in the second one, mutations $70 \mathrm{R}, 67 \mathrm{~N}$, 219 Q and 69 D , form a rhombus beginning with 70 R and ending with 69 D . This finding supports

![img-2.jpeg](img-2.jpeg)

Fig. 3. Bootstrap analysis of partially ordered set structures for the prostate cancer comparative genome hybridization data. The entry and the degree of shading in matrix cell $(i, j)$ denote the relative frequency in percent of the relation $i \prec j$ among the bootstrap samples. In panel (a) only cover relations are recorded, whereas in panel (b) all relations are considered. Diagonal entries and entries identical to zero have been omitted.
![img-3.jpeg](img-3.jpeg)

Fig. 4. Maximum likelihood estimation of the continuous-time conjunctive Bayesian network model for the HIV drug resistance data (a), and optimal HIV drug resistance partially ordered set corresponding to the maximum of the graph (b).
previous studies in which the same clustering of mutations has been described (Boucher et al., 1992). The two groups of mutations are known as the '215-41 pathway' and the '70-219 pathway', respectively. They provide alternative but not exclusive routes to resistance for HIV. The continuous-time conjunctive Bayesian network model captures this escape behaviour and suggests order constraints within each group.

A similar bootstrap analysis was performed for the HIV data and the results are summarized in Table 2 and Fig. 5. We find high stability of the maximum likelihood partially ordered set under re-sampling. All cover relations of Fig. 4 are supported with high confidence, and additional relations reach only less than half of these values. Overall, these findings strengthen the picture

Table 2. Bootstrap analysis of model parameters for the optimal HIV partially ordered set of Fig. 4. Events are amino acid changes in the HIV reverse transcriptase. See caption of Table 1 for further details


![img-4.jpeg](img-4.jpeg)

Fig. 5. Bootstrap analysis of partially ordered set structures for the HIV mutation data. See caption of Fig. 3 for further details.
of two separate groups of mutations, one occurring in a linear order, $215 \mathrm{Y} \prec 41 \mathrm{~L} \prec 210 \mathrm{~W}$, and the other exhibiting two intermediate branches, $70 \mathrm{R} \prec(67 \mathrm{~N}, 219 \mathrm{Q}) \prec 69 \mathrm{D}$.

For both applications, the best tree model shows inferior performance as compared to the more general model based on partially ordered sets. For example, the mutagenetic tree model for prostate cancer found in Fig. 2 of Rahnenführer et al. (2005) explains only $56 \%$ of the data at a loglikelihood of only -248.4 . Unlike mutagenetic trees, continuous-time conjunctive Bayesian networks can model the requirement of multiple parent mutations. This type of order constraint was found in both the prostate cancer and the HIV data set.

# 6. Discussion 

Conjuctive Bayesian networks are statistical models for the accumulation of mutations. They are defined by a partially ordered set of mutations, which encodes constraints on the order in which mutations can occur. Here we have introduced the continuous-time conjunctive Bayesian network, a continuous-time version of this model in which each mutation appears after an exponentially distributed waiting time, provided that all predecessor mutations have occurred. In an evolutionary process, this waiting time includes the generation of the mutation plus the time it takes for the allele to reach fixation in the population. Since we consider only mutations

with a selective advantage, the waiting time will be dominated by the mutation process in large populations and by the fixation process in small populations. The parameters $\lambda$ correspond to the rate of evolution, i.e. the product of population size, mutation rate and fixation probability.

The continuous-time conjunctive Bayesian network gives information on the order in which mutations tend to occur. For a set of $n$ mutations, the number of possible pathways to evolve the wild type into the type harbouring all $n$ mutations is the number of linear extensions of the partially ordered set. This cardinality increases rapidly with $n$ (Brightwell \& Winkler, 1991). However, protein evolution appears to use few mutational pathways (Weinreich et al., 2006). Thus, we can expect to find partially ordered sets with much smaller lattices of order ideals than the full Boolean lattice. In this reduced genotype space, evolution can be modelled more efficiently.

Knowledge of the partial order of genetic events helps our understanding of the phenotypic changes and biological mechanisms driving the evolutionary process. Furthermore, it allows for identifying early and essential mutational steps that may be predictive of clinical outcome or point to promising drug targets. In cancer research, Fearon \& Vogelstein (1990) have proposed linear pathways of genetic alterations as a model of tumorigenesis. These models are known as Vogelgrams (Gatenby \& Maini, 2003; Jones et al., 2008). The continuous-time conjunctive Bayesian network can be regarded as a generalization of the Vogelgram that is equipped with a statistical methodology for model selection and parameter estimation. In particular, it allows for multiple evolutionary pathways and makes explicit the timeline for the genetic alterations.

We have derived equations for the maximum likelihood estimates of the model parameters and for the expected waiting time of any genotype. These results are used in the EM algorithm for the censored model. Censoring is modelled by an exponentially distributed sampling time of the observed genotypes. This model appears most relevant for the data sets available, which often comprise cross-sectional data sampled after unknown time periods with respect to the evolutionary process. Other censoring schemes might be applicable in the future. For example, the sampling time, but not the time of appearance of each mutation, can be observed in some situations, giving rise to a different marginalization of the continuous-time network.

Because model selection relies on a simple combinatorial criterion and the number of model parameters is only linear in the number of mutations, we expect the continuous-time conjunctive Bayesian network to scale well with increasing data sets both in the number of observations and the number of mutations. In the cancer and HIV applications presented here, there are between 7 and 12 genetic events and 35-364 observations. It is likely, however, that the number of genes associated with cancer progression is much larger than currently known. Because the running time of the EM algorithm is dominated by the size of the genotype lattice, many mutations can be modelled as long as the number of mutational pathways is limited.

# AcKNOWLEDGMENTS 

Seth Sullivant was partially supported by the U.S. National Science Foundation. Part of this work was done while Niko Beerenwinkel was affiliated with the Program for Evolutionary Dynamics at Harvard University and funded by a grant from the Bill \& Melinda Gates Foundation through the Grand Challenges in Global Health Initiative.
