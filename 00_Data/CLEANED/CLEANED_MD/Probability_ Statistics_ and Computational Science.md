# Public <br> University of <br> Zurich 

## Public Open Repository and Archive

University of Zurich
University Library
Strickhofstrasse 39
CH-8057 Zurich
www.zora.uzh.ch

## Public

Year: 2012

## Probability, Statistics, and Computational Science

Beerenwinkel, Niko ; Siebourg, Juliane

DOI: https://doi.org/10.1007/978-1-61779-582-4_3

Posted at the Zurich Open Repository and Archive, University of Zurich
ZORA URL: https://doi.org/10.5167/uzh-80996
Journal Article

Originally published at:
Beerenwinkel, Niko; Siebourg, Juliane (2012). Probability, Statistics, and Computational Science. Methods in Molecular Biology, 855:77-110.
DOI: https://doi.org/10.1007/978-1-61779-582-4_3

# PROBABILITY, STATISTICS, AND COMPUTATIONAL SCIENCE 

NIKO BEERENWINKEL AND JULIANE SIEBOURG


#### Abstract

In this chapter, we review basic concepts from probability theory and computational statistics that are fundamental to evolutionary genomics. We provide a very basic introduction to statistical modeling and discuss general principles, including maximum likelihood and Bayesian inference. Markov chains, hidden Markov models, and Bayesian network models are introduced in more detail as they occur frequently and in many variations in genomics applications. In particular, we discuss efficient inference algorithms and methods for learning these models from partially observed data. Several simple examples are given throughout the text, some of which point to models that are discussed in more detail in subsequent chapters.


Key words: Bayesian inference, Bayesian networks, dynamic programming, EM algorithm, hidden Markov models, Markov chains, maximum likelihood, statistical models.

## 1. Statistical models

Evolutionary genomics can only be approached with the help of statistical modeling. Stochastic fluctuations are inherent to many biological systems. Specifically, the evolutionary process itself is stochastic, with random mutations and random mating being major sources of variation. In general, stochastic effects play an increasingly important role if the number of molecules, or cells, or individuals of a population is small. Stochastic variation also arises from measurement errors. Biological data is often noisy due to experimental limitations, especially for high-throughput technologies, such as microarrays, or next-generation sequencing $[9,6]$.

Statistical modeling addresses the following questions: What can be generalized from a finite sample obtained from an experiment to the population? What can be learned about the underlying biological mechanisms? How certain can we be about our model predictions?

In the frequentist view of statistics, the observed variability in the data is the result of a fixed true value being perturbed by random variation, such as, for example, measurement

noise. Probabilities are thus interpreted as long-run expected relative frequencies. By contrast, from a Bayesian point of view, probabilities represent our uncertainty about the state of nature. There is no true value, but only the data is real. Our prior belief about an event is updated in light of the data.

Statistical models represent the observed variability, or uncertainty by probability distributions $[4,25]$. The observed data are regarded as realizations of random variables. The parameters of a statistical model are usually the quantities of interest, because they describe the amount and the nature of systematic variation in the data. Parameter estimation and model selection will be discussed in more detail in the next section. In this section, we first consider discrete, then continuous random variables and univariate (1-dimensional) before multivariate ( $n$-dimensional) ones. We start by formulating the well-known Hardy-Weinberg principle $[15,29]$ as a statistical model.

Example 1 (Hardy-Weinberg model). The Hardy-Weinberg model is a statistical model for the genotypes in a diploid population of infinite size. Let us assume that there are two alleles, denoted A and a, and hence three genotypes, denoted $\mathrm{AA}, \mathrm{Aa}=\mathrm{aA}$, and aa. Let $X$ be the random variable with state space $\mathcal{X}=\{\mathrm{AA}, \mathrm{Aa}, \mathrm{aa}\}$ describing the genotype. We parametrize the probability distribution of $X$ by the allele frequency $p$ of A and the allele frequency $q=1-p$ of a. The Hardy-Weinberg model is defined by

$$
\begin{aligned}
P(X=\mathrm{AA}) & =p^{2} \\
P(X=\mathrm{Aa}) & =2 p(1-p) \\
P(X=\mathrm{aa}) & =(1-p)^{2}
\end{aligned}
$$

The parameter space of the model is $\Theta=\{p \in \mathbb{R} \mid 0 \leq p \leq 1\}=[0,1]$, the unit interval. We denote the Hardy-Weinberg model by $\operatorname{HW}(p)$ and write $X \sim \operatorname{HW}(p)$ if $X$ follows the distribution (1)-(3).

The Hardy-Weinberg distribution $P(X)$ is a discrete probability distribution (or probability mass function) with finite state space: We have $0 \leq P(X=x) \leq 1$ for all $x \in \mathcal{X}$ and $\sum_{x \in \mathcal{X}} P(X=x)=p^{2}+2 p(1-p)+(1-p)^{2}=[p+(1-p)]^{2}=1$. In general, any statistical model for a discrete random variable with $n$ states defines a subset of the

$(n-1)$-dimensional probability simplex

$$
\Delta_{n-1}=\left\{\left(p_{1}, \ldots, p_{n}\right) \in[0,1]^{n} \mid p_{1}+\cdots+p_{n}=1\right\}
$$

The probability simplex is the set of all possible probability distributions of $X$ and statistical models can be understood as specific subsets of the simplex [23].

The Hardy-Weinberg distribution is of interest because it arises under the assumption of random mating. A population with major allele frequency $p$ has genotype probabilities given in(1)-(3) after one round of random mating. We find that the new allele frequency

$$
p^{\prime}=P(\mathrm{AA})+P(\mathrm{Aa}) / 2=p^{2}+2 p(1-p) / 2=p
$$

is equal to the one in the previous generation. Thus, genetic variation is preserved under this simple model of sexual reproduction and the population is at equilibrium after one generation. In other words, the equations (1)-(3) describe the set of all populations at Hardy-Weinberg equilibrium. The parametric representation

$$
\left\{\left(p_{\mathrm{AA}}, p_{\mathrm{Aa}}, p_{\mathrm{aa}}\right) \in \Delta_{2} \mid p_{\mathrm{AA}}=p^{2}, p_{\mathrm{Aa}}=2 p(1-p), p_{\mathrm{aa}}=(1-p)^{2}\right\}
$$

of this set of distributions is equivalent to the implicit representation as the intersection of the Hardy-Weinberg curve

$$
4 p_{\mathrm{AA}} p_{\mathrm{aa}}-p_{\mathrm{Aa}}^{2}=0
$$

with the probability simplex $\Delta_{2}$ (Figure 1).
The simplest discrete random variable is a binary (or Bernoulli) random variable $X$. The textbook example of a Bernoulli trial is the flipping of a coin. The state space of this random experiment is the set that contains all possible outcomes, namely whether the coin lands on heads $(X=0)$ or tails $(X=1)$. We write $\mathcal{X}=\{0,1\}$ to denote this state space. The parameter space is the set that contains all possible values of the model parameters. In the coin tossing example, the only parameter is the probability of observing tails, $p$, and this parameter can take any value between 0 and 1 , so we write $\Theta=\{p \mid 0 \leq p \leq 1\}$ for the parameter space. In general, the event $X=1$ is often called a 'success', and $p=P(X=1)$ the probability of success.

Example 2 (Binomial distribution). Consider $n$ independent Bernoulli trials, each with success probability $p$. Let $X$ be the random variable counting the number of successes $k$ among the $n$ trials. Then $X$ has state space $\mathcal{X}=\{0, \ldots, n\}$ and

$$
P(X=k)=\binom{n}{k} p^{k}(1-p)^{n-k}
$$

This is the binomial distribution, denoted $\operatorname{Binom}(n, p)$. Its parameter space is $\Theta=$ $\mathbb{N} \times[0,1]$. Examples of binomially distributed random variables are the number of 'heads' in $n$ successive coin tosses, or the number of mutated genes in a group of species.

Important characteristics of a probability distribution are its expectation (or expected value, or mean) and its variance. They are defined, respectively, as

$$
\begin{aligned}
\mathrm{E}(X) & =\sum_{x \in \mathcal{X}} x P(X=x) \\
\operatorname{Var}(X) & =\sum_{x \in \mathcal{X}}[x-\mathrm{E}(X)]^{2} P(X=x)
\end{aligned}
$$

The standard deviation is $\sqrt{\operatorname{Var}(X)}$. For the binomial distribution, $X \sim \operatorname{Binom}(n, p)$, we find $\mathrm{E}(X)=n p$ and $\operatorname{Var}(X)=n p(1-p)$.

Example 3 (Poisson distribution). The Poisson distribution $\operatorname{Pois}(\lambda)$ with parameter $\lambda \geq 0$ is defined as

$$
P(X=k)=\frac{\lambda^{k} e^{-\lambda}}{k!}, \quad k \in \mathbb{N}
$$

It describes the number $X$ of independent events occurring in a fixed period of time (or space) at average rate $\lambda$ and independently of the time since (or distance to) the last event. The Poisson distribution has equal expectation and variance, $\mathrm{E}(X)=\operatorname{Var}(X)=\lambda$.

The Poisson distribution is used frequently as a model for the number of DNA mutations in a gene after a certain time period, where $\lambda$ is the mutation rate. Both the binomial and the Poisson distribution describe counts of random events. In the limit of large $n$ and fixed product $n p$, the two distributions coincide, $\operatorname{Binom}(n, p) \rightarrow \operatorname{Pois}(n p)$, for $n \rightarrow \infty$.

Example 4 (Shotgun sequencing). Let us consider a simplified model of the shotgun approach to DNA sequencing. Suppose that $n$ reads of length $L$ have been obtained

from a genome of size $G$. We assume that all reads have the same probability of being sequenced. Then the probability of hitting a specific base with one read is $p=L / G$ and the average coverage of the sequencing run is $c=n p$. Under this model, the number of times $X$ a single base is sequenced is distributed as $\operatorname{Binom}(n, p)$. For large $n$, we have

$$
P(X=k)=\binom{n}{k} p^{k}(1-p)^{n-k} \approx \frac{c^{k} e^{-c}}{k!}
$$

For example, using next-generation sequencing technology one might obtain $n=10^{8}$ reads of length $L=100$ bases in a single run. For the human genome of length $G=$ $3 \cdot 10^{9}$, we obtain a coverage of $c=3.4$. The distribution of the number of reads per base pair is shown in Figure 2. In particular, the fraction of unsequenced positions is $P(X=0)=e^{-c}=3.57 \%$.

A continuous random variable $X$ takes values in $\mathcal{X}=\mathbb{R}$ and is defined by a nonnegative function $f(x)$ such that

$$
P(X \in B)=\int_{B} f(x) d x, \quad \text { for all subsets } B \subseteq \mathbb{R}
$$

The function $f$ is called the probability density function of $X$. For an interval,

$$
P(X \in[a, b])=P(a \leq X \leq b)=\int_{a}^{b} f(x) d x
$$

The cumulative distribution function is

$$
F(b)=P(X \leq b)=\int_{-\infty}^{b} f(x) d x, \quad b \in \mathbb{R}
$$

Thus, the density is the derivative of the cumulative distribution function, $\frac{d}{d x} F(x)=f(x)$.
In analogy to the discrete case, expectation and variance of a continuous random variable are defined, respectively, as

$$
\begin{aligned}
\mathrm{E}(X) & =\int_{-\infty}^{\infty} x f(x) d x \\
\operatorname{Var}(X) & =\int_{-\infty}^{\infty}[x-\mathrm{E}(X)]^{2} f(x) d x
\end{aligned}
$$

Example 5 (Normal distribution). The normal (or Gaussian) distribution has the density function

$$
f(x)=\left(2 \pi \sigma^{2}\right)^{-1 / 2} \exp \left[-\frac{(x-\mu)^{2}}{2 \sigma^{2}}\right]
$$

The parameter space is $\Theta=\left\{\left(\mu, \sigma^{2}\right) \mid \mu \in \mathbb{R}, \sigma^{2} \in \mathbb{R}_{+}\right\}$. A normal random variable $X \sim \operatorname{Norm}\left(\mu, \sigma^{2}\right)$ has mean $\mathrm{E}(X)=\mu$ and variance $\operatorname{Var}(X)=\sigma^{2} . \operatorname{Norm}(0,1)$ is called the standard normal distribution.

The normal distribution is frequently used as a model for measurement noise. For example, $X \sim \operatorname{Norm}\left(\mu, \sigma^{2}\right)$ might describe the hybridization intensity of a sample to a probe on a microarray. Then $\mu$ is the level of expression of the corresponding gene and $\sigma^{2}$ summarizes the experimental noise associated with the microarray experiment. The parameters can be estimated from a finite sample $\left\{x^{(1)}, \ldots, x^{(N)}\right\}$, i.e., from $N$ replicate experiments, as the empirical mean and variance, respectively,

$$
\begin{aligned}
\bar{x} & =\frac{1}{N} \sum_{i=1}^{N} x^{(i)} \\
s^{2} & =\frac{1}{N-1} \sum_{i=1}^{N}\left(x^{(i)}-\bar{x}\right)^{2}
\end{aligned}
$$

The normal distribution plays a special role in statistics due to the central limit theorem. It asserts that the average $\bar{X}_{N}=\left(X^{(1)}+\cdots+X^{(N)}\right) / N$ of $N$ independent (see below) and identically distributed (i.i.d.) random variables $X^{(i)}$ with equal mean $\mu$ and variance $\sigma^{2}$ converges in distribution to the standard normal distribution,

$$
\sqrt{N}\left(\frac{\bar{X}_{N}-\mu}{\sigma}\right) \xrightarrow{d} \operatorname{Norm}(0,1)
$$

irrespective of the shape of their distribution. As a consequence, many test statistics and estimators are asymptotically normally distributed. For example, the Poisson distribution $\operatorname{Pois}(\lambda)$ is approximately normal $\operatorname{Norm}(\lambda, \lambda)$ for large values of $\lambda$.

We often measure multiple quantities at the same time, for example the expression of several genes, and are interested in correlations among the variables. Let $X$ and $Y$ be two random variables with expected values $\mu_{X}$ and $\mu_{Y}$ and variances $\sigma_{X}^{2}$ and $\sigma_{Y}^{2}$, respectively. The covariance between $X$ and $Y$ is

$$
\operatorname{Cov}(X, Y)=\mathrm{E}\left[\left(X-\mu_{X}\right)\left(Y-\mu_{Y}\right)\right]=\mathrm{E}[X Y]-\mathrm{E}[X] \mathrm{E}[Y]
$$

and the correlation between $X$ and $Y$ is $\rho_{X, Y}=\operatorname{Cov}(X, Y) /\left(\sigma_{X} \sigma_{Y}\right)$. For observations $\left(x^{(1)}, y^{(1)}\right), \ldots,\left(x^{(N)}, y^{(N)}\right)$ the sample correlation coefficient is

$$
r_{x, y}=\frac{\sum_{i=1}^{N}\left(x^{(i)}-\bar{x}\right)\left(y^{(i)}-\bar{y}\right)}{(N-1) s_{X} s_{Y}}
$$

where $s_{X}$ and $s_{Y}$ is the sample standard deviation of $X$ and $Y$, respectively, defined in (20).

So far, we have worked with univariate distributions and we now turn to multivariate distributions, i.e., we consider random vectors $X=\left(X_{1}, \ldots, X_{n}\right)$ such that each $X_{i}$ is a random variable. For the case of discrete random variables $X_{i}$, we first generalize the binomial distribution to random experiments with a finite number of outcomes.

Example 6 (Multinomial distribution). Let $K$ be the number of possible outcomes of a random experiment and $\theta_{k}$ the probability of outcome $k$. We consider the random vector $X=\left(X_{1}, \ldots, X_{K}\right)$ with values in $\mathcal{X}=\mathbb{N}^{K}$, where $X_{k}$ counts the number of outcomes of type $k$. The multinomial distribution $\operatorname{Mult}\left(n, \theta_{1}, \ldots, \theta_{K}\right)$ is defined as

$$
P(X=x)=\frac{n!}{x_{1}!\cdots x_{K}!} \theta_{1}^{x_{1}} \cdots \theta_{K}^{x_{K}}
$$

if $\sum_{k=1}^{K} x_{k}=n$, and 0 otherwise. The parameter space of the model is $\Theta=\mathbb{N} \times \Delta_{K-1}$. For $K=2$, we recover the binomial distribution (8). Each component $X_{k}$ of a multinomial vector has expected value $\mathrm{E}\left(X_{k}\right)=n \theta_{k}$ and $\operatorname{Var}\left(X_{k}\right)=n \theta_{k}\left(1-\theta_{k}\right)$. The covariance of two components is $\operatorname{Cov}\left(X_{k}, X_{l}\right)=-n p_{k} p_{l}$, for $k \neq l$.

In general, the covariance matrix $\Sigma$ of a random vector $X$ is defined by

$$
\Sigma_{i j}=\operatorname{Cov}\left(X_{i}, X_{j}\right)=\mathrm{E}\left[\left(X_{i}-\mu_{i}\right)\left(X_{j}-\mu_{j}\right)\right]
$$

where $\mu_{i}$ is the expected value of $X_{i}$. The matrix $\Sigma$ is also called the variance-covariance matrix, because the diagonal terms are the variances $\Sigma_{i i}=\operatorname{Cov}\left(X_{i}, X_{i}\right)=\operatorname{Var}\left(X_{i}\right)$.

A continuous multivariate random variable $X$ takes values in $\mathcal{X}=\mathbb{R}^{n}$. It is defined by its cumulative distribution function

$$
F(x)=P(X \leq x), \quad x \in \mathbb{R}^{n}
$$

or equivalently, by the probability density function

$$
f(x)=\frac{\partial^{n}}{\partial x_{1} \cdots \partial x_{n}} F\left(x_{1}, \ldots, x_{n}\right), \quad x \in \mathbb{R}^{n}
$$

Example 7 (Multivariate normal distribution). For $n \geq 1$ and $x \in \mathbb{R}^{n}$, the multivariate normal (or Gaussian) distribution has density

$$
f(x)=(2 \pi)^{-n / 2} \operatorname{det}(\Sigma)^{-1 / 2} \exp \left[-\frac{1}{2}(x-\mu)^{t} \Sigma^{-1}(x-\mu)\right]
$$

with parameter space $\Theta=\left\{(\mu, \Sigma) \mid \mu=\left(\mu_{1}, \ldots, \mu_{n}\right) \in \mathbb{R}^{n}\right.$ and $\Sigma=\left(\sigma_{i j}^{2}\right) \in \mathbb{R}^{n \times n}\right\}$, where $\Sigma$ is the symmetric, positive-definite covariance matrix and $\mu$ the expectation. We write $X=\left(X_{1}, \ldots, X_{n}\right) \sim \operatorname{Norm}(\mu, \Sigma)$ for a random vector with such a distribution.

We say that two random variables $X$ and $Y$ are independent if $P(X, Y)=P(X) P(Y)$, or equivalently, if the conditional probability $P(X \mid Y)=P(X, Y) / P(Y)$ is equal to the unconditional probability $P(X)$. If $X$ and $Y$ are independent, denoted $X \perp Y$, then $\mathrm{E}[X Y]=\mathrm{E}[X] \mathrm{E}[Y]$ and $\operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)$. It follows that independent random variables have covariance zero. However, the converse is only true in specific situations, for example if $(X, Y)$ is multivariate normal, but not in general, because correlation captures only linear dependencies.

This limitation can be addressed by using statistical models which allow for a richer dependency structure. Section 7 is devoted to Bayesian networks, a family of probabilistic graphical models based on conditional independences. Let $X, Y$, and $Z$ be three random vectors. Generalizing the notion of statistical independence, we say that $X$ is conditionally independent of $Y$ given $Z$ and write $X \perp Y \mid Z$ if $P(X, Y \mid Z)=P(X \mid Z) P(Y \mid Z)$. Bayes' theorem states that

$$
P(Y \mid X)=\frac{P(X \mid Y) P(Y)}{P(X)}
$$

where $P(Y)$ is called the prior probability and $P(Y \mid X)$ the posterior probability. Intuitively, the prior $P(Y)$ encodes our a priori knowledge about $Y$ (i.e., before observing $X)$, and $P(Y \mid X)$ is our updated knowledge about $Y$ a posteriori (i.e., after observing $X)$.

We have $P(X)=\sum_{Y} P(X, Y)$ if $Y$ is discrete, and similarly, $P(X)=\int_{Y} P(X, Y) d Y$ if $Y$ is continuous. Here, $P(X)$ is called the marginal and $P(X, Y)$ the joint probability. This summation or integration is known as marginalization (Figure 3).

Since $P(X)=\sum_{Y} P(X, Y)=\sum_{Y} P(X \mid Y) P(Y)$, Bayes' theorem can also be rewritten as

$$
P(Y \mid X)=\frac{P(X \mid Y) P(Y)}{\sum_{y^{\prime} \in \mathcal{Y}} P\left(X \mid y^{\prime}\right) P\left(y^{\prime}\right)}
$$

where $P\left(y^{\prime}\right)=P\left(Y=y^{\prime}\right)$ and $\mathcal{Y}$ is the state space of $Y$.

Example 8 (Diagnostic test). We want to evaluate a diagnostic test for a rare genetic disease. The binary random variables $D$ and $T$ indicate disease status ( $D=1$, diseased) and test result ( $T=1$, positive), respectively. Let us assume that the prevalence of the disease is $0.5 \%$, i.e., $0.5 \%$ of all people in the population are known to be infected. The test has a false positive rate (probability that somebody is tested positive who does not have the disease) of $P(T=1 \mid D=0)=5 \%$ and a true positive rate (probability that somebody is tested positive who has the disease) of $P(T=1 \mid D=1)=90 \%$. Then the posterior probability of a person having the disease given that he or she tested positive is

$$
P(D=1 \mid T=1)=\frac{P(T=1 \mid D=1) P(D=1)}{P(T=1 \mid D=0) P(D=0)+P(T=1 \mid D=1) P(D=1)}=0.083
$$

i.e., only $8.3 \%$ of the positively tested individuals actually have the disease. Thus, our prior belief of the disease status, $P(D)$, has been modified in light of the test result by multiplication with $P(T \mid D)$ to obtain the updated belief $P(D \mid T)$.

# 2. STATISTICAL INFERENCE 

Statistical models have parameters and a common task is to estimate the model parameters from observed data. The goal is to find the set of parameters with the best model fit. There are two major approaches to parameter estimation: maximum likelihood and Bayes.

The maximum likelihood approach is based on the likelihood function. Let us consider a fixed statistical model M with parameter space $\Theta$ and assume that we have observed

realizations $\mathcal{D}=\left\{x^{(1)}, \ldots, x^{(N)}\right\}$ of the discrete random variable $X \sim \mathrm{M}\left(\theta_{0}\right)$ for some unknown parameter $\theta_{0} \in \Theta$. For the fixed data set $\mathcal{D}$, the likelihood function of the model is

$$
L(\theta)=P(\mathcal{D} \mid \theta)
$$

where we write $P(\mathcal{D} \mid \theta)$ to emphasize that, here, the probability of the data depends on the model parameter $\theta$. For continuous random variables, the likelihood function is defined similarly in terms of the density function, $L(\theta)=f(\mathcal{D} \mid \theta)$. Maximum likelihood (ML) estimation seeks the parameter $\theta \in \Theta$ for which $L(\theta)$ is maximal. Rather than $L(\theta)$, it is often more convenient to maximize $\ell(\theta)=\log L(\theta)$, the log-likelihood function. If the data are i.i.d., then

$$
\ell(\theta)=\sum_{i=1}^{N} \log P\left(X=x^{(i)} \mid \theta\right)
$$

Example 9 (Likelihood function of the binomial model). Suppose we have observed $k=7$ successes in a total of $N=10$ Bernoulli trials. The likelihood function of the binomial model (8) is

$$
L(p)=p^{k}(1-p)^{N-k}
$$

where $p$ is the success probability (Figure 4). To maximize $L$, we consider the loglikelihood function

$$
\ell(p)=\log L(p)=k \log (p)+(N-k) \log (1-p)
$$

and the likelihood equation $d \ell / d p=0$. The ML estimate (MLE) is the solution $\hat{p}_{\mathrm{ML}}=$ $k / N=7 / 10$. Thus, the MLE of the success probability is just the relative frequency of successes - a reasonable estimate every frequentist would have proposed firsthand.

Example 10 (Likelihood function of the Hardy-Weinberg model). If we genotype a finite random sample of a population of diploid individuals at a single locus, then the resulting data consists of the numbers of individuals $n_{\mathrm{AA}}, n_{\mathrm{Aa}}$, and $n_{\mathrm{aa}}$ with the respective genotypes. Assuming Hardy-Weinberg equilibrium (1)-(3), we want to estimate the allele

frequencies $p$ and $q=1-p$ of the population. The likelihood function of the HardyWeinberg model is $L(p)=P(\mathrm{AA})^{n_{\mathrm{AA}}} P(\mathrm{Aa})^{n_{\mathrm{Aa}}} P(\mathrm{aa})^{n_{\mathrm{aa}}}$ and the log-likelihood is

$$
\begin{aligned}
\ell(p) & =n_{\mathrm{AA}} \log p^{2}+n_{\mathrm{Aa}} \log 2 p(1-p)+n_{\mathrm{aa}} \log (1-p)^{2} \\
& \propto\left(2 n_{\mathrm{AA}}+n_{\mathrm{Aa}}\right) \log p+\left(n_{\mathrm{Aa}}+2 n_{\mathrm{aa}}\right) \log (1-p)
\end{aligned}
$$

where we have dropped the constant $n_{\mathrm{Aa}} \log 2$. The ML estimate of $p \in[0,1]$ can be found by maximizing $\ell$. Solving the likelihood equation

$$
\frac{\partial \ell}{\partial p}=\frac{2 n_{\mathrm{AA}}+n_{\mathrm{Aa}}}{p}-\frac{n_{\mathrm{Aa}}+2 n_{\mathrm{aa}}}{1-p}=0
$$

yields the MLE $\hat{p}_{\mathrm{ML}}=\left(2 n_{\mathrm{AA}}+n_{\mathrm{Aa}}\right) /(2 N)$, where $N=n_{\mathrm{AA}}+n_{\mathrm{Aa}}+n_{\mathrm{aa}}$ is the total sample size. For example, if we sample $N=100$ genotypes with $n_{\mathrm{AA}}=81, n_{\mathrm{Aa}}=18$, and $n_{\mathrm{aa}}=1$, then we find $\hat{p}_{\mathrm{ML}}=(2 \cdot(81+18)) /(2 \cdot 100)=0.9$ for the frequency of the major allele.

MLEs have many desirable properties. Asymptotically, as the sample size $N \rightarrow \infty$, they are normally distributed, unbiased, and have minimal variance. The uncertainty in parameter estimation associated with the sampling variance of the finite data set can be quantified in confidence intervals. There are several ways to construct confidence intervals and statistical tests for MLEs based on the asymptotic behavior of the loglikelihood function $\ell(\theta)=\log L(\theta)$ and its derivatives. For example, the asymptotic normal distribution of the MLE is

$$
\hat{\theta}_{\mathrm{ML}} \stackrel{\circ}{\sim} \operatorname{Norm}\left(\theta, J(\theta)^{-1}\right)
$$

where $I(\theta)=-\partial^{2} \ell / \partial \theta^{2}$ is the Fisher information and $J(\theta)=\mathrm{E}[I(\theta)]$ the expected Fisher information. This result gives rise to the Wald confidence intervals

$$
\left[\hat{\theta}_{\mathrm{ML}} \pm z_{1-\alpha / 2} J(\theta)^{-1}\right]
$$

where $z_{1-\alpha / 2}=\inf \{x \in \mathbb{R} \mid 1-\alpha / 2 \leq F(x)\}$ is the $(1-\alpha / 2)$ quantile and $F$ the cumulative distribution function of the standard normal distribution. Equation (38) still holds after replacing $J(\theta)$ with the standard error $\operatorname{se}\left(\hat{\theta}_{\mathrm{ML}}\right)=\left[I\left(\hat{\theta}_{\mathrm{ML}}\right)\right]^{-\frac{1}{2}}$ or $\left[J\left(\hat{\theta}_{\mathrm{ML}}\right)\right]^{-\frac{1}{2}}$, and it also generalizes to higher dimensions. Other common constructions of confidence intervals

include those based on the asymptotic distribution of the score function $S(\theta)=\partial \ell / \partial \theta$ and the log-likelihood ratio $\log \left(L\left(\hat{\theta}_{\mathrm{ML}}\right) / L(\theta)\right)$ [3].

We now discuss another, more generic approach to quantify parameter uncertainty, not restricted to ML estimation, which is applied frequently in practice due to its simple implementation. Bootstrapping [8] is a resampling method in which independent observations are resampled from the data with replacement. The resulting new data set consists of (some of) the original observations and under i.i.d. assumptions, the bootstrap replicates have asymptotically the same distribution as the data. Intuitively, by sampling with replacement, one is pretending that the collection of replicates thus obtained is a good proxy for the distribution of datasets that one would have obtained, had we been able to actually replicate the experiment. In this way, the variability of an estimator (or more generally the distribution of any test statistic) can be approximated by evaluating the estimator (or the statistic) on a collection of bootstrap replicates. For example, the distribution of the ML estimator of a model parameter $\theta$ can be obtained from the bootstrap samples.

Example 11 (Bootstrap confidence interval for the ML allele frequency). We use bootstrapping to estimate the distribution of the ML estimator $\hat{p}_{\mathrm{ML}}$ of the HardyWeinberg model for the data set $\left(n_{\mathrm{AA}}, n_{\mathrm{Aa}}, n_{\mathrm{aa}}\right)=(81,18,1)$ of Example 10. For each bootstrap sample, we draw $N=100$ genotypes with replacement from the original data to obtain random integer vectors of length three summing to 100 . The ML estimate is computed for each of a total of $B$ bootstrap samples. The resulting distributions of $\hat{p}_{\mathrm{ML}}$ are shown in Figure 5, for $B=100,1000$, and 10,000. The means of these distributions are $0.899,0.9004$, and 0.9001 , respectively, and $95 \%$ confidence intervals can be derived from the $2.5 \%$ and $97.5 \%$ quantiles of the distributions. For $B=100,1000$, and 10,000, we obtain, respectively, $[0.8598,0.9350],[0.860,0.940]$, and $[0.855,0.940]$.

The Bayesian approach takes a different point of view and regards the model parameters as random variables [13]. Inference is then concerned with estimating the joint distribution of the parameters $\theta$ given the observed data $\mathcal{D}$. By Bayes' theorem (Eq. 30)

we have

$$
P(\theta \mid \mathcal{D})=\frac{P(\mathcal{D} \mid \theta) P(\theta)}{P(\mathcal{D})}=\frac{P(\mathcal{D} \mid \theta) P(\theta)}{\int_{\theta \in \Theta} P(\mathcal{D} \mid \theta) P(\theta) d \theta}
$$

i.e., the posterior probability of the parameters is proportional to the likelihood of the data times the prior probability of the parameters. It follows that, for a uniform prior, the mode of the posterior is equal to the MLE.

From the posterior, credible intervals of parameter estimates can be derived such that the parameter lies in the interval with a certain probability, say $95 \%$. This is in contrast to a $95 \%$ confidence interval in the frequentist approach, because, there, the parameter is fixed and the interval boundaries are random variables. The meaning of a confidence interval is that $95 \%$ of similar intervals would contain the true parameter, if intervals were constructed independently from additional identically distributed data.

The prior $P(\theta)$ encodes our a priori belief in $\theta$ before observing the data. It can be used to incorporate domain-specific knowledge into the model, but it may also be uninformative or objective, in which case all observations are equally likely, or nearly so, $a$ priori. However, it can sometimes be difficult to find non-informative priors. In practice, conjugate priors are most often used. A conjugate prior is one that is invariant with respect to the distribution family under multiplication with the likelihood, i.e., the posterior belongs to the same family as the prior. Conjugate priors are mathematically convenient and computationally efficient, because the posterior can be calculated analytically for a wide range of statistical models.

Example 12 (Dirichlet prior). Let $T=\left(T_{1}, \ldots, T_{K}\right)$ be a continuous random variable with state space $\Delta_{K-1}$. The Dirichlet distribution $\operatorname{Dir}(\alpha)$ with parameters $\alpha \in \mathbb{R}_{+}^{K}$ has probability density function

$$
f\left(\theta_{1}, \ldots, \theta_{K}\right)=\frac{\Gamma\left(\sum_{i=1}^{K} \alpha_{i}\right)}{\prod_{i=1}^{K} \Gamma\left(\alpha_{i}\right)} \prod_{i=1}^{K} \theta_{i}^{\alpha_{i}-1}
$$

where $\Gamma$ is the gamma function. The Dirichlet prior is conjugate to the multinomial likelihood: If $T \sim \operatorname{Dir}(\alpha)$ and $(X \mid T=\theta) \sim \operatorname{Mult}\left(n, \theta_{1}, \ldots, \theta_{K}\right)$ then $(\theta \mid X=x) \sim$ $\operatorname{Dir}(\alpha+x)$. For $K=2$, this distribution is called the beta distribution. Hence, the beta distribution is the conjugate prior to the binomial likelihood.

Example 13 (Posterior probability of genotype frequencies). Let us consider the simple genetic system with two loci and two alleles each of Example 1, but without assuming the Hardy-Weinberg model. We regard the observed genotype frequencies $\left(n_{\mathrm{AA}}, n_{\mathrm{Aa}}, n_{\mathrm{aa}}\right)=(81,18,1)$ as the result of a draw from a multinomial distribution $\operatorname{Mult}\left(n, \theta_{\mathrm{AA}}, \theta_{\mathrm{Aa}}, \theta_{\mathrm{aa}}\right)$. Assuming a Dirichlet prior $\operatorname{Dir}\left(\alpha_{\mathrm{AA}}, \alpha_{\mathrm{Aa}}, \alpha_{\mathrm{aa}}\right)$, the posterior genotype probabilities follow the Dirichlet distribution $\operatorname{Dir}\left(\alpha_{\mathrm{AA}}+n_{\mathrm{AA}}, \alpha_{\mathrm{Aa}}+n_{\mathrm{Aa}}, \alpha_{\mathrm{aa}}+n_{\mathrm{aa}}\right)$. In Figure 6, the prior $\operatorname{Dir}(10,10,10)$ is shown on the left, the multinomial likelihood $P\left(\left(n_{\mathrm{AA}}, n_{\mathrm{Aa}}, n_{\mathrm{aa}}\right)=(81,18,1) \mid \theta_{\mathrm{AA}}, \theta_{\mathrm{Aa}}, \theta_{\mathrm{aa}}\right)$ in the center, and the resulting posterior $\operatorname{Dir}(10+81,10+18,10+1)$ on the right. Note that the MLE is different from the mode of the posterior. As compared to the likelihood, the non-uniform prior has shifted the maximum of the posterior toward the center of the probability simplex.

# 3. Hidden data and the EM algorithm 

We often cannot observe all relevant random variables due to, for example, experimental limitations or study designs. In this case, a statistical model $P(X, Z \mid \theta \in \Theta)$ consists of the observed random variable $X$ and the hidden (or latent) random variable $Z$, both of which can be multivariate. In this section, we write $X=\left(X^{(1)}, \ldots, X^{(N)}\right)$ for the random variables describing the $N$ observations and refer to $X$ also as the observed data. The hidden data for this model is $Z=\left(Z^{(1)}, \ldots, Z^{(N)}\right)$ and the complete data is $(X, Z)$. For convenience we assume the parameter space $\Theta$ to be continuous and the state spaces $\mathcal{X}$ of $X$ and $\mathcal{Z}$ of $Z$ to be discrete.

In the Bayesian framework one does not distinguish between unknown parameters and hidden data and it is natural to assess the joint posterior $P(\theta, Z \mid X) \propto P(X \mid$ $\theta, Z) P(\theta, Z)$, which is $P(X, Z \mid \theta) P(\theta)$ if priors are independent, i.e., if $P(\theta, Z)=$ $P(\theta) P(Z)$. Alternatively, if the distribution of the hidden data $Z$ is not of interest, it can be marginalized out. Then the posterior (40) becomes

$$
P(\theta \mid X)=\frac{\sum_{Z} P(X, Z \mid \theta) P(\theta)}{\int_{\theta \in \Theta} \sum_{Z} P(X, Z \mid \theta) P(\theta) d \theta}
$$

In the likelihood framework it can be more efficient to estimate the hidden data, rather than marginalizing over it. The hidden (or complete-data) log-likelihood is

$$
\ell_{\text {hid }}(\theta)=\log P(X, Z \mid \theta)=\sum_{i=1}^{N} \log P\left(X^{(i)}, Z^{(i)} \mid \theta\right)
$$

For ML parameter estimation, we need to consider the observed log-likelihood

$$
\ell_{\text {obs }}(\theta)=\log P(X \mid \theta)=\log \sum_{Z} P(X, Z \mid \theta)=\log \sum_{Z^{(1)} \in Z} \cdots \sum_{Z^{(N)} \in Z} \prod_{i=1}^{N} P\left(X^{(i)}, Z^{(i)} \mid \theta\right)
$$

This likelihood function is usually very difficult to maximize and one has to resort to numerical optimization techniques. Generic local methods such as gradient descent or Newton's method can be used, but there is also a more specific local optimization procedure, which avoids computing any derivatives of the likelihood function, called the Expectation Maximization (EM) algorithm [5].

In order to maximize the likelihood function (44), we consider any distribution $q(Z)$ of the hidden data $Z$ and write

$$
\ell_{\mathrm{obs}}(\theta)=\log \sum_{Z} q(Z) \frac{P(X, Z \mid \theta)}{q(Z)}=\log \mathrm{E}[P(X, Z \mid \theta) / q(Z)]
$$

where the expected value is with respect to $q(Z)$. Jensen's inequality applied to the concave $\log$ function asserts that $\log \mathrm{E}[Y] \geq \mathrm{E}[\log Y]$. Hence, the observed log-likelihood is bounded from below by $\mathrm{E}[\log (P(X, Z \mid \theta) / q(Z))]$, or

$$
\ell_{\mathrm{obs}}(\theta) \geq \mathrm{E}\left[\ell_{\mathrm{hid}}(\theta)\right]+H(q)
$$

where $H(q)=-\mathrm{E}[\log q(Z)]$ is the entropy. The idea of the EM algorithm is to maximize this lower bound instead of $\ell_{\text {obs }}(\theta)$ itself. Intuitively this task is easier, because the big sum over the hidden data in (44) disappears on the right hand side of (46) upon taking expectations.

The EM algorithm is an iterative procedure alternating between an E step and an M step. In the E step, the lower bound (46) is maximized with respect to the distribution $q$ by setting $q(Z)=P\left(Z \mid X, \theta^{(t)}\right)$, where $\theta^{(t)}$ is the current estimate of $\theta$, and computing the expected value of the hidden log-likelihood

$$
Q\left(\theta \mid \theta^{(t)}\right)=\mathrm{E}_{Z \mid X, \theta^{(t)}}\left[\ell_{\text {hid }}(\theta)\right]
$$

In the M step, $Q$ is maximized with respect to $\theta$ to obtain an improved estimate

$$
\theta^{(t+1)}=\arg \max _{\theta} Q\left(\theta \mid \theta^{(t)}\right)
$$

The sequence $\theta^{(1)}, \theta^{(2)}, \theta^{(3)}, \ldots$ converges to a local maximum of the likelihood surface (44). The global maximum and hence the MLE is generally not guaranteed to be found with this local optimization method. In practice the EM algorithm is often run repeatedly with many different starting solutions $\theta^{(1)}$, or with few very reasonable starting solutions obtained from other heuristics or educated guesses.

Example 14 (Naive Bayes). Let us assume we observe realizations of a discrete random variable $\left(X_{1}, \ldots, X_{L}\right)$ and we want to cluster observations into $K$ distinct groups. For this purpose, we introduce a hidden random variable $Z$ with state space $\mathcal{Z}=[K]=\{1, \ldots, K\}$ indicating class membership. The joint probability of $\left(X_{1}, \ldots, X_{L}\right)$ and $Z$ is

$$
P\left(X_{1}, \ldots, X_{L}, Z\right)=P(Z) P\left(X_{1}, \ldots, X_{L} \mid Z\right)=P(Z) \prod_{n=1}^{L} P\left(X_{n} \mid Z\right)
$$

The marginalization of this model with respect to the hidden data $Z$ is the unsupervised naive Bayes model. The observed variables $X_{n}$ are often called features and $Z$ the latent class variable (Figure 7).

The model parameters are the class prior $P(Z)$, which we assume to be constant and will ignore, and the conditional probabilities $\theta_{n, k x}=P\left(X_{n}=x \mid Z=k\right)$. The complete-data likelihood of observed data $X=\left(X^{(1)}, \ldots, X^{(N)}\right)$ and hidden data $Z=$ $\left(Z^{(1)}, \ldots, Z^{(N)}\right)$ is

$$
\begin{aligned}
P(X, Z \mid \theta) & =\prod_{i=1}^{N} P\left(X^{(i)}, Z \mid \theta\right)=\prod_{i=1}^{N} P\left(Z^{(i)}\right) \prod_{n=1}^{L} P\left(X_{n}^{(i)} \mid Z^{(i)}\right) \\
& \propto \prod_{i=1}^{N} \prod_{n=1}^{L} \theta_{n, Z^{(i)} X_{n}^{(i)}}=\prod_{i=1}^{N} \prod_{n=1}^{L} \prod_{k \in[K]} \prod_{x \in \mathcal{X}} \theta_{n, k x}^{I_{n, k x}\left(Z^{(i)}\right)}
\end{aligned}
$$

where $I_{n, k x}\left(Z^{(i)}\right)$ is equal to one if and only if $Z^{(i)}=k$ and $X_{n}^{(i)}=x$, and zero otherwise.
To apply the EM algorithm for estimating $\theta$ without observing $Z$, we consider the hidden log-likelihood

$$
\ell_{\text {hid }}(\theta)=\log P(X, Z \mid \theta)=\sum_{i=1}^{N} \sum_{n=1}^{L} \sum_{k \in[K]} \sum_{x \in \mathcal{X}} I_{n, k x}\left(Z^{(i)}\right) \log \theta_{n, k x}
$$

In the E step, we compute the expected values of $Z^{(i)}$

$$
\gamma_{n, k x}^{(i)}=\mathrm{E}_{Z \mid X=x, \theta^{\prime}}\left[Z^{(i)}\right]=\frac{P\left(X^{(i)}=x \mid Z^{(i)}=k\right)}{\sum_{k^{\prime} \in K} P\left(X^{(i)}=x \mid Z^{(i)}=k^{\prime}\right)}=\frac{\theta_{n, k x}^{\prime}}{\sum_{k^{\prime} \in K} \theta_{n, k^{\prime} x}^{\prime}}
$$

where $\theta^{\prime}$ is the current estimate of $\theta$. The expected value $\gamma_{n, k x}^{(i)}$ is sometimes referred to as the responsibility of class $k$ for observation $X_{n}^{(i)}=x$. The expected hidden log-likelihood can be written in terms of the expected counts $N_{n, k x}=\sum_{i=1}^{N} \gamma_{n, k x}^{(i)}$ as

$$
\mathrm{E}_{Z \mid X, \theta^{\prime}}\left[\ell_{\text {hid }}(\theta)\right]=\sum_{n=1}^{L} \sum_{k \in[K]} \sum_{x \in \mathcal{X}} N_{n, k x} \log \theta_{n, k x}
$$

In the M step, maximization of this sum yields $\hat{\theta}_{n, k x}=N_{n, k x} / \sum_{x^{\prime}} N_{n, k x^{\prime}}$.

# 4. Markov chains 

A stochastic process $\left\{X_{t}, t \in \mathcal{T}\right\}$ is a collection of random variables with common state space $\mathcal{X}$. The index set $\mathcal{T}$ is usually interpreted as time and $X_{t}$ is the state of the process at time $t$. A discrete-time stochastic process $X=\left(X_{1}, X_{2}, X_{3}, \ldots\right)$ is called a Markov chain [22], if $X_{n+1} \perp X_{n-1} \mid X_{n}$ for all $n \geq 2$, or equivalently, if each state depends only on its immediate predecessor,

$$
P\left(X_{n} \mid X_{n-1}, \ldots, X_{1}\right)=P\left(X_{n} \mid X_{n-1}\right), \quad \text { for all } n \geq 2
$$

We consider here Markov chains with finite state space $\mathcal{X}=[K]=\{1, \ldots, K\}$ that are homogeneous, i.e., with transition probabilities independent of time,

$$
T_{k l}=P\left(X_{n+1}=l \mid X_{n}=k\right), \quad \text { for all } k, l \in[K], n \geq 2
$$

The finite-state, homogeneous Markov chain is a statistical model denoted $\mathrm{MC}(\Pi, T)$ and defined by the initial state distribution $\Pi \in \Delta_{K-1}$, where $\Pi_{k}=P\left(X_{1}=k\right)$, and the stochastic $K \times K$ transition matrix $T=\left(T_{k l}\right)$.

We can generalize the one-step transition probabilities $T_{k l}$ to

$$
T_{k l}^{n}=P\left(X_{n+j}=l \mid X_{j}=k\right)
$$

the probability of jumping from state $k$ to state $l$ in $n$ time steps. Any $(n+m)$-step transition can be regarded as an $n$-step transition followed by an $m$-step transition.

Because the intermediate state $i$ is unknown, summing over all possible values yields the decomposition

$$
T_{k l}^{n+m}=\sum_{i=1}^{K} T_{k i}^{n} T_{i l}^{m}, \quad \text { for all } n, m \geq 1, k, l \in[K]
$$

known as the Chapman-Kolmogorov equations. In matrix notation they can be written as $T^{(n+m)}=T^{(n)} T^{(m)}$. It follows that the $n$-step transition matrix is the $n$-th matrix power of the one-step transition matrix, $T^{(n)}=T^{n}$.

A state $l$ of a Markov chain is accessible from state $k$ if $T_{k l}^{n}>0$. We say that $k$ and $l$ communicate with each other and write $k \sim l$ if they are accessible from one another. State communication is reflexive $(k \sim k)$, symmetric $(k \sim l \Rightarrow l \sim k)$, and, by the Chapman-Kolmogorov equations, transitive $(j \sim k \sim l \Rightarrow j \sim l)$. Hence it defines an equivalence relation on the state space. The Markov chain is irreducible if it has a single communication class, i.e., if any state is accessible from any other state.

A state is recurrent if the Markov chain will re-enter it with probability one. Otherwise the state is transient. In finite-state Markov chains, recurrent states are also positive recurrent, i.e., the expected time to return to the state is finite. A state is aperiodic if the process can return to it after any time $n \geq 1$. Recurrence, positive recurrence, and aperiodicity are class properties: If they hold for a state $k$, then they also hold for all sates communicating with $k$.

A Markov chain is ergodic if it is irreducible, aperiodic, and positive recurrent. An ergodic Markov chain has a unique stationary distribution $\pi$ given by

$$
\pi_{l}=\lim _{n \rightarrow \infty} T_{k l}^{n}=\sum_{k=1}^{K} \pi_{k} T_{k l}, \quad l \in[K], \quad \sum_{l=1}^{K} \pi_{l}=1
$$

independent of the initial distribution $\Pi$. In matrix notation, $\pi$ is the solution of $\pi^{t}=\pi^{t} T$.

Example 15 (Two-state Markov chain). Consider the Markov chain with state space $\{1,2\}$ and transition probabilities $T_{12}=\alpha>0$ and $T_{21}=\beta>0$. Clearly, the chain is ergodic and its stationary distribution $\pi$ is given by

$$
\left(\begin{array}{ll}
\pi_{1} & \pi_{2}
\end{array}\right)=\left(\begin{array}{ll}
\pi_{1} & \pi_{2}
\end{array}\right)\left(\begin{array}{cc}
1-\alpha & \alpha \\
\beta & 1-\beta
\end{array}\right)
$$

or equivalently, $\alpha \pi_{1}=\beta \pi_{2}$. With $\pi_{1}+\pi_{2}=1$, we obtain $\pi^{t}=(\alpha+\beta)^{-1}(\alpha, \beta)$.

In Example 15, if $\alpha=0$, then state 1 is called an absorbing state, because once entered it is never left. In evolutionary biology and population genetics, Markov chains are often used to model evolving populations, and the fixation probability of an allele can be computed as the absorption probability in such models.

Example 16 (Wright-Fisher process). We consider two alleles, A and a, in a diploid population of size $N$. The total number of A alleles in generation $n$ is described by a Markov chain $X_{n}$ with state space $\{0,1,2, \ldots, 2 N\}$. We assume that individuals mate randomly and that maternal and paternal alleles are chosen randomly such that $X_{n+1} \mid$ $X_{n} \sim \operatorname{Binom}(2 N, k /(2 N))$, where $k$ is the number of A alleles in generation $n$. The Markov chain has transition probabilities

$$
T_{k l}=\binom{2 N}{l}\left(\frac{k}{2 N}\right)^{l}\left(\frac{2 N-k}{2 N}\right)^{2 N-l}
$$

If the initial number of A alleles is $X_{1}=k$, then $\mathrm{E}\left(X_{1}\right)=k$. After binomial sampling, $\mathrm{E}\left(X_{2}\right)=2 N(k /(2 N))=k$ and hence $\mathrm{E}\left(X_{n}\right)=k$ for all $n \geq 0$. The Markov chain has the two absorbing states 0 and $2 N$, which correspond, respectively, to extinction and fixation of the A allele. To compute the fixation probability $h_{k}$ of A given $k$ initial copies of it,

$$
h_{k}=\lim _{n \rightarrow \infty} P\left(X_{n}=2 N \mid X_{1}=k\right)
$$

we consider the expected value, which is equal to $k$, in the limit as $n \rightarrow \infty$ to obtain

$$
k=\lim _{n \rightarrow \infty} \mathrm{E}\left(X_{n}\right)=0 \cdot\left(1-h_{k}\right)+2 N \cdot h_{k}
$$

Thus, the fixation probability is just $h_{k}=k /(2 N)$, the initial relative frequency of the allele. The Wright-Fisher process $[30,12]$ is a basic stochastic model for random genetic drift, i.e., for the variation in allele frequencies only due to random sampling.

If we observe data $X=\left(X^{(1)}, \ldots, X^{(N)}\right)$ from a finite Markov chain $\mathrm{MC}(\Pi, T)$ of length $L$, then the likelihood is

$$
L(\Pi, T)=\prod_{i=1}^{N} P\left(X^{(i)}\right)=\prod_{i=1}^{N} P\left(X_{1}^{(i)}\right) \prod_{n=1}^{L-1} P\left(X_{n+1}^{(i)} \mid X_{n}^{(i)}\right)=\prod_{i=1}^{N} \Pi_{X_{1}^{(i)}} \prod_{n=1}^{L-1} T_{X_{n}^{(i)}, X_{n+1}^{(i)}}
$$

which can be rewritten as

$$
L(\Pi, T)=\prod_{i=1}^{N} \prod_{k \in[K]} \Pi_{k}^{N_{k}\left(X^{(i)}\right)} \prod_{k \in[K]} \prod_{l \in[K]} T_{k l}^{N_{k l}\left(X^{(i)}\right)}=\prod_{k \in[K]} \Pi_{k}^{N_{k}} \prod_{k \in[K]} \prod_{l \in[K]} T_{k l}^{N_{k l}}
$$

with $N_{k l}\left(X^{(i)}\right)$ the number of observed transitions from state $k$ into state $l$ in observation $X^{(i)}$, and $N_{k l}=\sum_{i=1}^{N} N_{k l}\left(X^{(i)}\right)$ the total number of $k$-to- $l$ transitions in the data, and similarly, $N_{k}\left(X^{(i)}\right)$ and $N_{k}$ the number of times the $i$-th chain, respectively all chains, started in state $k$.

# 5. Continuous-time Markov chains 

A continuous-time stochastic process $\{X(t), t \geq 0\}$ with finite state space $[K]$ is a continuous-time Markov chain if

$$
P[X(t+s)=l \mid X(s)=k, X(u)=x(u), 0 \leq u<s]=P[X(t+s)=l \mid X(s)=k]
$$

for all $s, t \geq 1, k, l, x(u) \in[K], 0 \leq u<s$. The chain is homogeneous if (66) is independent of $s$. The transition probabilities are then denoted

$$
T_{k l}(t)=P[X(t+s)=l \mid X(s)=k]
$$

It can be shown that the transition matrix $T(t)$ is the matrix exponential of a constant rate matrix $R$ times $t$,

$$
T(t)=\exp (R t)=\sum_{j=0}^{\infty} \frac{1}{j!}(R t)^{j}
$$

Example 17 (Jukes-Cantor model). Consider a fixed position in a DNA sequence and let $T_{k l}(t)$ be the probability that, due to mutation, nucleotide $k$ changes to nucleotide $l$ after time $t$ at this position (Figure 8). The Jukes-Cantor model [19] is the simplest DNA substitution model. It assumes that the transition rates from any nucleotide to any other are equal,

$$
R=\left(\begin{array}{cccc}
-3 \alpha & \alpha & \alpha & \alpha \\
\alpha & -3 \alpha & \alpha & \alpha \\
\alpha & \alpha & -3 \alpha & \alpha \\
\alpha & \alpha & \alpha & -3 \alpha
\end{array}\right)
$$

The resulting transition matrix $T(t)=\exp (R t)$ is

$$
T(t)=\frac{1}{4}\left(\begin{array}{cccc}
1+3 e^{-4 \alpha t} & 1-e^{-4 \alpha t} & 1-e^{-4 \alpha t} & 1-e^{-4 \alpha t} \\
1-e^{-4 \alpha t} & 1+3 e^{-4 \alpha t} & 1-e^{-4 \alpha t} & 1-e^{-4 \alpha t} \\
1-e^{-4 \alpha t} & 1-e^{-4 \alpha t} & 1+3 e^{-4 \alpha t} & 1-e^{-4 \alpha t} \\
1-e^{-4 \alpha t} & 1-e^{-4 \alpha t} & 1-e^{-4 \alpha t} & 1+3 e^{-4 \alpha t}
\end{array}\right)
$$

and the stationary distribution as $t \rightarrow \infty$ is uniform, $\pi=(1 / 4,1 / 4,1 / 4,1 / 4)^{t}$.

Example 18 (The Poisson process). A continuous-time Markov chain $X(t)$ is a counting process, if $X(t)$ represents the total number of events that occur by time $t$. It is a Poisson process, if in addition, $X(0)=0$, the increments are independent, and in any interval of length $t$, the number of events is Poisson distributed with rate $\lambda t$,

$$
P[X(t+s)-X(s)=k]=P[X(t)=k]=e^{-\lambda t} \frac{(\lambda t)^{k}}{k!}
$$

The Poisson process is used, for example, to count mutations in a gene.

Example 19 (Exponential distribution). The exponential distribution $\operatorname{Exp}(\lambda)$ with parameter $\lambda>0$ is a common distribution for waiting times. It is defined by the density function

$$
f(x)=\lambda e^{-\lambda x}, \quad \text { for } x \geq 0
$$

If $X \sim \operatorname{Exp}(\lambda)$, then $X$ has expectation $\mathrm{E}(X)=\lambda^{-1}$ and variance $\operatorname{Var}(X)=\lambda^{-2}$. The exponential distribution is memoryless, which means that $P(X>s+t \mid X>t)=$ $P(X>s)$, for all $s, t>0$. An important consequence of the memoryless property is that the waiting times between successive events are i.i.d. For example, the waiting times $\tau_{n}$ $(n \geq 1)$ between the events of a Poisson process, the sequence of inter-arrival times, are exponentially distributed, $\tau_{n} \sim \operatorname{Exp}(\lambda)$, for all $n \geq 1$.

# 6. Hidden Markov models 

A hidden Markov model (HMM) is a statistical model for hidden random variables $Z=$ $\left(Z_{1}, \ldots, Z_{L}\right)$, which form a homogeneous Markov chain, and observed random variables $X=\left(X_{1}, \ldots, X_{L}\right)$. Each observed symbol $X_{n}$ depends on the hidden state $Z_{n}$. The HMM

is illustrated in Figure 9. It encodes the following conditional independence statements:

$$
\begin{array}{cl}
Z_{n+1} \perp Z_{n-1} \mid Z_{n}, & 2 \leq n \leq L-1 \\
X_{n} \perp X_{m} \mid Z_{n}, & 1 \leq m, n \leq L, m \neq n
\end{array}
$$

The parameters of the HMM consist of the initial state probabilities $\Pi=P\left(Z_{1}\right)$, the transition probabilities $T_{k l}=P\left(Z_{n}=l \mid Z_{n-1}=k\right)$ of the Markov chain, and the emission probabilities $E_{k x}=P\left(X_{n}=x \mid Z_{n}=k\right)$ of symbols $x \in \mathcal{X}$. The HMM is denoted $\operatorname{HMM}(\Pi, T, E)$. For simplicity, we restrict ourselves here to finite state spaces $\mathcal{Z}=[K]$ of $Z$ and $\mathcal{X}$ of $X$. The joint probability of $(Z, X)$ factorizes as

$$
P(X, Z)=P\left(Z_{1}\right) \prod_{n=1}^{L-1} P\left(X_{n} \mid Z_{n}\right) P\left(Z_{n+1} \mid Z_{n}\right)=\Pi_{Z_{1}} \prod_{n=1}^{L-1} E_{Z_{n}, X_{n}} T_{Z_{n}, Z_{n+1}}
$$

The HMM is typically used to model sequence data $x=\left(x_{1}, x_{2}, \ldots, x_{L}\right)$ generated by different mechanisms $z_{n}$ which can not be observed. Each observation $x$ can be a time series or any other object with a linear dependency structure [24]. In computational biology, the HMM is frequently applied to DNA and protein sequence data, where it accounts for first-order spatial dependencies of nucleotides or amino acids [7].

Example 20 (CpG islands). CpG islands are CG-enriched regions in a DNA sequence. They are typically a few hundreds to thousands of base pairs long. We want to use a simple HMM to detect CpG islands in genomic DNA. The hidden states $Z_{n} \in \mathcal{Z}=\{-,+\}$ indicate whether sequence position $n$ belongs to a CpG island $(+)$ or not $(-)$. The observed sequence is given by the nucleotide at each position, $X_{n} \in \mathcal{X}=\{\mathrm{A}, \mathrm{C}, \mathrm{G}, \mathrm{T}\}$.

Suppose we observe the sequence $x=(\mathrm{C}, \mathrm{A}, \mathrm{C}, \mathrm{G})$. Then we can calculate the joint probability of $x$ and any state path $z$ by (75). For example, if $z=(+,-,-,+)$, then $P(X=x, Z=z)=\Pi_{+} \cdot E_{+, \mathrm{C}} T_{+,-} \cdot E_{-, \mathrm{A}} T_{-,-} \cdot E_{-, \mathrm{C}} T_{-,+} \cdot E_{+, \mathrm{G}}$.

Typically, one is interested in the hidden state path $z=\left(z_{1}, z_{2}, \ldots, z_{L}\right)$ that gave rise to the observation $x$. For biological sequences, $z$ is often called the annotation of $x$. In Example 20, the genomic sequence is annotated with CpG islands. For generic parameters, any state path can give rise to a given observed sequence, but with different probabilities. The decoding problem is to find the annotation $z^{*}$ that maximizes the joint

probability,

$$
z^{*}=\underset{z \in \mathcal{Z}}{\operatorname{argmax}} P(X=x, Z=z)
$$

There are $K^{L}$ possible state paths, such that, for sequences of only moderate length, the optimization problem (76) cannot be solved in the naive way by enumerating all paths.

However, there is a an efficient algorithm solving (76) based on the following factorization along the Markov chain:

$$
\begin{aligned}
& \max _{\mathcal{Z}} P(X, Z)=\max _{Z_{1}, \ldots, Z_{L}} P\left(Z_{1}\right) \prod_{n=1}^{L-1} P\left(X_{n} \mid Z_{n}\right) P\left(Z_{n+1} \mid Z_{n}\right) \\
& =\max _{Z_{L}} P\left(Z_{L} \mid Z_{L-1}\right) P\left(X_{L} \mid Z_{L}\right)\left[\ldots\left[\max _{Z_{2}} P\left(Z_{3} \mid Z_{2}\right) P\left(X_{2} \mid Z_{2}\right)\left[\right.\right.\right. \\
& \left.\left.\left.\max _{Z_{1}} P\left(Z_{2} \mid Z_{1}\right) P\left(X_{1} \mid Z_{1}\right) \cdot P\left(Z_{1}\right)\right]\right] \ldots\right] .
\end{aligned}
$$

Thus, the maximum can be obtained by recursively computing the terms inside parentheses, which amounts to computing partial solutions $z_{1}^{*}, \ldots, z_{n}^{*}$ for $n=1, \ldots, L$. Each term occurs $K$ times and involves of order $K$ steps, and there are $L$ such terms to compute. Hence the time complexity of the algorithm is $O\left(L K^{2}\right)$, despite the fact that the maximum is over $K^{L}$ paths. This scheme is known as dynamic programming and it is the workhorse of biological sequence analysis. The argument $z^{*}$ of the maximum is obtained from the successive maximizing arguments $z_{1}^{*}, z_{2}^{*}, \ldots, z_{L}^{*}$. For HMMs this procedure is known as the Viterbi algorithm [28].

In order to compute the marginal likelihood $P(X=x)$ of an observed sequence $x$, we need to sum the joint probability $P(Z=z, X=x)$ over all hidden states $z \in \mathcal{Z}$. The length of this sum is exponential in $L$, but it can be computed efficiently by the same dynamic programming principle used for the Viterbi algorithm:

$$
\begin{aligned}
\sum_{Z} P(X, Z)= & \sum_{Z_{1}, \ldots, Z_{L}} P\left(Z_{1}\right) \prod_{n=1}^{L-1} P\left(X_{n} \mid Z_{n}\right) P\left(Z_{n+1} \mid Z_{n}\right) \\
= & \sum_{Z_{L}} P\left(Z_{L} \mid Z_{L-1}\right) P\left(X_{L} \mid Z_{L}\right)\left[\ldots\left[\sum_{Z_{2}} P\left(Z_{3} \mid Z_{2}\right) P\left(X_{2} \mid Z_{2}\right)\left[\right.\right.\right. \\
& \left.\left.\left.\sum_{Z_{1}} P\left(Z_{2} \mid Z_{1}\right) P\left(X_{1} \mid Z_{1}\right) \cdot P\left(Z_{1}\right)\right]\right] \ldots\right]
\end{aligned}
$$

Indeed, this factorization is the same as in (77) with maxima replaced by sums. The recursive algorithm implementing (78) is known as the forward algorithm. It computes the partial solutions $f\left(n, Z_{n}\right)=P\left(X_{1}, \ldots, X_{n}, Z_{n}\right)$.

The factorization along the Markov chain can also be done in the other direction starting the recursion from $Z_{L}$ down to $Z_{1}$. The resulting backward algorithm generates the partial solutions $b\left(n, Z_{n}\right)=P\left(X_{n+1}, \ldots, X_{L} \mid Z_{n}\right)$. From the forward and backward quantities, one can also compute the position-wise posterior state probabilities

$$
P\left(Z_{n} \mid X\right)=\frac{P\left(X, Z_{n}\right)}{P(X)}=\frac{P\left(X_{1}, \ldots, X_{n}, Z_{n}\right) P\left(X_{n+1}, \ldots, X_{L} \mid Z_{n}\right)}{P(X)}=\frac{f\left(n, Z_{n}\right) b\left(n, Z_{n}\right)}{P(X)}
$$

For example, in the CpG island HMM (Example 20), we can compute, for each nucleotide, the probability that it belongs to a CpG island given the entire observed DNA sequence. Selecting the state that maximizes this probability independently at each sequence position is known as posterior decoding. In general, the result will be different from Viterbi decoding.

Example 21 (Pairwise sequence alignment). The pair HMM is a statistical model for pairwise alignment of two observed sequences over a fixed alphabet $\mathcal{A}$. For protein sequences, $\mathcal{A}$ is the set of 20 natural amino acids and for DNA sequences, $\mathcal{A}$ consists of the four nucleotides, plus the gap symbol ('-'). At each position of the alignment, a hidden variable $Z_{n} \in \mathcal{Z}=\{\mathrm{M}, \mathrm{X}, \mathrm{Y}\}$ indicates whether there is a (mis-)match (M), an insertion $(\mathrm{X})$, or a deletion $(\mathrm{Y})$ in sequence $y$ relative to sequence $x$. For example,

$$
\begin{aligned}
z & =\text { MMMMMMMMMMMMMXXMMMMMMMMMMMYMMMMYMMMMM } \\
x & =\text { CTRPNNNTRKSIRPQIGPGQAFYATGD-IGDI-RQAHC } \\
y & =\text { CGRPNNHRIKGLR--IGPGRAFFAMGAIRGGEIRQAHC }
\end{aligned}
$$

The emitted symbols are pairs $\left(X_{n}, Y_{n}\right)$ of aligned sequence characters with state space $(\mathcal{A} \times \mathcal{A}) \backslash\{(-,-)\}$. Thus, a pairwise alignment is a probabilistically generated sequence of pairs of symbols.

The choice of transition and emission probabilities corresponds to fixing a scoring scheme in non-probabilistic formulations of sequence alignment. For example, the emission probabilities $P[(a, b) \mid \mathrm{M}]$ from a match state encode pairwise amino acid preferences and can be modeled by substitution matrices such as PAM and BLOSUM [7].

In the pair HMM, computing an optimal alignment between $x$ and $y$ means to find the most probable state path $z^{*}=\operatorname{argmax}_{z} P(X=x, Y=y, Z=z)$, which can be solved using the Viterbi algorithm. Using the forward algorithm, we can also compute efficiently the marginal probability of two sequences being related independent of their alignment, $P(X, Y)=\sum_{Z} P(X, Y, Z)$. In general, this probability is more informative than the posterior $P(Z \mid X, Y)$ of an optimal alignment $z^{*}$, because many alignments tend to have the same or nearly the same probability such that $P\left(Z=z^{*} \mid X, Y\right)$ can be very small. Finally, we can also compute the probability of two characters $x_{n}$ and $y_{m}$ being aligned by means of posterior decoding.

Example 22 (Profile HMM). Profile hidden Markov models represent groups of related sequences such as protein families. They are used for searching homologous sequences and for building multiple sequence alignments. They can be regarded as unrolled versions of the pair HMM. A profile HMM is a statistical model for observed sequences, which are regarded as i.i.d. realizations. It has site-specific emission probabilities $E_{n}(a)=$ $P\left(X_{n}=a\right)$. In its simplest form allowing only gap-free alignments, the probability of an observation $x$ is just

$$
P(X=x)=\prod_{n=1}^{L} E_{n}\left(x_{i}\right)
$$

The matrix $\left(E_{n}(a)\right)_{1 \leq n \leq L, a \in \mathcal{A}}$ is called a position-specific scoring matrix (PSSM).
Profile HMMs can also model indels. Figure 10 shows the hidden state space of such a model. It has match states $M_{n}$, which can emit symbols according to the probability tables $E_{n}$, insert states $I_{n}$, which usually emit symbols in an unspecific manner, and delete states $D_{n}$, which do not emit any symbols. The possible transitions between those states allow for modeling alignment gaps of any length.

A given profile HMM for a protein family can be used to detect new sequences that belong to the same family. For a query sequence $x$, we can either consider the most probable alignment of the sequence to the HMM, $P\left(X=x, Z=z^{*}\right)$, or the marginal

probability independent of the alignment, $P(X=x)=\sum_{Z} P(X=x, Z)$, to decide about family membership.

Parameter estimation in HMMs is complicated by the presence of hidden variables. In Section 2, the EM algorithm has been introduced for finding a local maximum of the likelihood surface. For HMMs, the EM algorithm is known as the Baum-Welch algorithm [1]. For simplicity, let us ignore the initial state probabilities $\Pi$ and summarize the parameters of the HMM by $\theta=(T, E)$. For ML estimation, we need to maximize the observed log-likelihood

$$
\ell_{\mathrm{obs}}(\theta)=\log P(X \mid \theta)=\log \sum_{Z} P(X, Z \mid \theta)=\log \sum_{Z^{(1)}, \ldots, Z^{(N)}} \prod_{i=1}^{N} P\left(X^{(i)}, Z^{(i)} \mid \theta\right)
$$

where $X^{(1)}, \ldots, X^{(N)}$ are the i.i.d. observations. For each observation, we can rewrite the joint probability as

$$
P\left(X^{(i)}, Z^{(i)} \mid \theta\right)=\prod_{k \in[K]} \prod_{x \in \mathcal{X}} E_{k x}^{N_{k x}\left(Z^{(i)}\right)} \cdot \prod_{k \in[K]} \prod_{l \in[K]} T_{k l}^{N_{k l}\left(Z^{(i)}\right)}
$$

where $N_{k x}\left(Z^{(i)}\right)$ is the number of $x$ emissions when in state $k$ and $N_{k l}\left(Z^{(i)}\right)$ the number of $k$-to- $l$ transitions in state path $Z^{(i)}$ (cf. (64)).
In the E step, the expectation of (81) is computed with respect to $P\left(Z \mid X, \theta^{\prime}\right)$, where $\theta^{\prime}$ is current best estimate of $\theta$. We use (82) and denote by $N_{k x}$ and $N_{k l}$ the expected value of $\sum_{i} N_{k x}\left(Z^{(i)}\right)$ and $\sum_{i} N_{k l}\left(Z^{(i)}\right)$, respectively, to obtain

$$
\begin{aligned}
\mathrm{E}\left[\ell_{\text {hid }}(\theta)\right] & =\sum_{Z} P\left(Z \mid X, \theta^{\prime}\right) \log P(X, Z \mid \theta) \\
& =\sum_{Z^{(1)}, \ldots, Z^{(N)}} P\left(Z \mid X, \theta^{\prime}\right)\left[\sum_{k, x} N_{k x}\left(Z^{(i)}\right) \log E_{k x}+\sum_{k, l} N_{k l}\left(Z^{(i)}\right) \log T_{k l}\right] \\
& =\sum_{k, x} N_{k x} \log E_{k x}+\sum_{k, l} N_{k l} \log T_{k l}
\end{aligned}
$$

The expected counts $N_{k x}$ and $N_{k l}$ are the sufficient statistics [2] of the HMM, i.e., with respect to the model, they contain all information about the parameters available from the data. The expected counts can be computed using the forward and backward algorithms. In the M step, this expression is maximized with respect to $\theta=(T, E)$. We find the MLEs $\hat{T}_{k l}=N_{k l} / \sum_{m} N_{k m}$ and $\hat{E}_{k x}=N_{k x} / \sum_{y} N_{k y}$.

# 7. BAYESIAN NETWORKS 

Bayesian networks are a class of probabilistic graphical models which generalize Markov chains and HMMs. The basic idea is to use a graph for encoding conditional independences among random variables (Figure 11). The graph representation provides not only an intuitive and simple visualization of the model structure, but it is also the basis for designing efficient algorithms for inference and learning in graphical models [17, 20, 18].

A Bayesian network (BN) for a set of random variables $X=\left(X_{1}, \ldots, X_{L}\right)$ consists of a directed acyclic graph (DAG) and local probability distributions (LPDs). The DAG $G=(V, E)$ has vertex set $V=[L]$ and edge set $E \subseteq V \times V$. Each vertex $n \in V$ is identified with the random variable $X_{n}$. If there is an edge $X_{m} \rightarrow X_{n}$ in $G$, then $X_{m}$ is a parent of $X_{n}$ and $X_{n}$ is a child of $X_{m}$. For each vertex $n \in V$, there is a LPD $P\left(X_{n} \mid X_{\mathrm{pa}(n)}\right)$, where $\mathrm{pa}(n)$ is the set of parents of $X_{n}$ in $G$. The Bayesian network model is defined as the family of distributions for which the joint probability of $X$ factors into conditional probabilities as

$$
P\left(X_{1}, \ldots, X_{L}\right)=\prod_{n=1}^{L} P\left(X_{n} \mid X_{\mathrm{pa}(n)}\right)
$$

In this case, we write $X \sim \operatorname{BN}(G, \theta)$, where $\theta=\left(\theta_{1}, \ldots, \theta_{L}\right)$ denotes the parameters of the LPDs.

For the Bayesian network shown in Figure 11, we find $P(U, V, W, X, Y)=P(U) P(Y) P(V \mid$ $U, Y) P(W \mid V) P(X \mid U)$. The graph encodes several conditional independence statements about $(U, V, W, X, Y)$, including for example, $W \perp\{U, X\} \mid V$.

Example 23 (Markov chain). A finite Markov chain is a Bayesian network with the DAG $X_{1} \rightarrow X_{2} \rightarrow \cdots \rightarrow X_{L}$, denoted $C$, and joint distribution

$$
P\left(X_{1}, \ldots, X_{n}\right)=P\left(X_{1}\right) P\left(X_{2} \mid X_{1}\right) P\left(X_{3} \mid X_{2}\right) \cdots P\left(X_{L} \mid X_{L-1}\right)
$$

If $X \sim \mathrm{MC}(\Pi, T)$ is homogeneous, then the LPDs are $\theta_{1}=P\left(X_{1}\right)=\Pi$ and $\theta_{n+1}=$ $P\left(X_{n+1} \mid X_{n}\right)=T$ for all $n \in[L-1]$, such that $\mathrm{MC}(\Pi, T)=\mathrm{BN}(C, \theta)$. Similarly, HMMs are Bayesian networks with hidden variables and factorized joint distribution (75).

The meaning of the parameters $\theta$ of a Bayesian network depends on the family of distributions that has been chosen for the LPDs. In the general case of a discrete random

variable with finite state space, $\theta_{n}$ is a conditional probability table. If each vertex $X_{n}$ has $K$ possible states, then

$$
\theta_{n}=\left(P\left(X_{n}=a \mid X_{\mathrm{pa}(n)}=b\right)\right)_{b \in[K]^{\mathrm{pa}(n)}, a \in[K]}
$$

has $K^{\mathrm{pa}(n)} \times(K-1)$ free parameters. If $X_{n}$ depends on all other variables, then $\theta_{n}$ has the maximal number of $K^{L}-1$ parameters, which is exponential in the number of vertices. If, on the other hand, $X_{n}$ is independent of all other variables, $\mathrm{pa}(n)=\emptyset$, then $\theta_{n}$ has $(K-1)$ parameters, which is independent of $L$. For the chain (Example 23), where each vertex has exactly one outgoing and one incoming edge, we find a total of $(K-1)+(L-1) K(K-1)$ free parameters which is of order $O\left(L K^{2}\right)$.

A popular model for continuous random variables $X_{n}$ is the linear Gaussian model. Here, the LPDs are Gaussian distributions with mean a linear function of the parents,

$$
P\left(X_{n} \mid X_{\mathrm{pa}(n)}\right)=\operatorname{Norm}\left(v_{n}+w_{n}^{t} \cdot X_{\mathrm{pa}(n)}, \sigma_{n}^{2}\right)
$$

with parameters $v_{n} \in \mathbb{R}$ and $w_{i} \in \mathbb{R}^{\mathrm{pa}(n)}$ specifying the mean, and variance $\sigma_{n}^{2}$. The number of parameters increases linearly with the number of parents, but only linear relationships can be modeled.

Learning a Bayesian network $\operatorname{BN}(G, \theta)$ from data $\mathcal{D}$ can be done in different ways following either the Bayesian or the maximum likelihood approach as introduced in Section 2. In general, it involves first finding the optimal network structure

$$
G^{*}=\underset{G}{\operatorname{argmax}} P(G \mid \mathcal{D})
$$

a task known as model selection, and then estimating the parameters

$$
\theta^{*}=\underset{\theta}{\operatorname{argmax}} P\left(\theta \mid G^{*}, \mathcal{D}\right)
$$

for the given optimal structure $G^{*}$.
Model selection is a particularly hard problem, because the number of DAGs increases super-exponentially with the number of vertices rendering exhaustive searches impractical, and the objective function in (88) is often difficult to compute. The posterior

$P(G \mid \mathcal{D})$ is proportional to the product $P(\mathcal{D} \mid G) P(G)$ of marginal likelihood and network prior, and the marginal likelihood

$$
P(\mathcal{D} \mid G)=\int P(\mathcal{D} \mid \theta, G) P(\theta \mid G) d \theta
$$

is often analytically intractable. Here $P(\theta \mid G)$ is the prior distribution of parameters given the network topology.

To address this limitation, the marginal likelihood (90) is often approximated by a function that is easier to evaluate. A popular choice is the Bayesian information criterion (BIC) $[26]$,

$$
\log P(D \mid G) \approx \log P\left(D \mid \hat{\theta}_{\mathrm{ML}}, G\right)-\frac{1}{2} \nu \log N
$$

where $\nu$ is the number of free parameters of the model and $N$ the size of the data. The BIC approximation can be derived under certain assumptions including a unimodal likelihood. It replaces computation of the integral (90) by evaluating the integrand at the MLE and adding the correction term $-(\nu \log N) / 2$, which penalizes models of high complexity.

The model selection problem remains hard even with a tractable scoring function such as BIC, because of the enormous search space. Local search methods, such as greedy hill climbing or simulated annealing, are often used in practice. They return a local maximum as a point estimate for the best network structure. Results can be improved by running several local searches from different starting topologies.

Often data are sparse and we will find diffuse posterior distributions of network structures, which might not be represented very well by a single point estimate. In the fully Bayesian approach, we aim at estimating the full posterior $P(G \mid D) \propto P(D \mid G) P(G)$. One way to approximate this distribution is to draw a finite number of samples from it. Markov chain Monte Carlo (MCMC) methods generate such a sample by constructing a Markov chain that will converge to the target distribution [21].

In the Metropolis-Hastings algorithm [16], we start with a random DAG $G^{(0)}$ and then iteratively generate a new DAG $G^{(n)}$ from the previous one $G^{(n-1)}$ by drawing it from a proposal distribution $Q$,

$$
G^{(n)} \sim Q\left(G^{(n)} \mid G^{(n-1)}\right)
$$

The new DAG will be accepted with acceptance probability

$$
\min \left\{\frac{P\left(D \mid G^{(n)}\right) P\left(G^{(n)}\right) Q\left(G^{(n-1)} \mid G^{(n)}\right)}{P\left(D \mid G^{(n-1)}\right) P\left(G^{(n-1)}\right) Q\left(G^{(n)} \mid G^{(n-1)}\right)}, 1\right\}
$$

Otherwise the model is left unchanged and the next sample is drawn. With this acceptance probability it is guaranteed that the Markov chain converges to the desired distribution. After an initial burn-in phase, samples from the stationary phase of the chain are collected, say $G^{(m)}, \ldots, G^{(N)}$. Any feature $f$ of the network (e.g., the presence of an edge, or a sub-graph) can be estimated as the expected value

$$
\mathrm{E}(f)=\sum_{G} f(G) P(G \mid D) \approx \frac{1}{N} \sum_{n=m}^{N} f\left(G^{(n)}\right)
$$

A critical point of the Metropolis-Hastings algorithm is the choice of the proposal distribution $Q$, which encodes the way the network space is explored. Because not all graphs, but only DAGs, are allowed, computing the transition probabilities $Q\left(G^{(n)} \mid G^{(n-1)}\right)$ is usually the main computational bottleneck.

Parameter estimation, i.e., solving (89), can be done along the lines described in Section 2 following either the ML or the Bayesian approach. If the model contains hidden random variables, then the EM algorithm (Section 3) can be used. However, this approach is feasible only if efficient inference algorithms are available. For hidden Markov models (Section 6), the forward and backward algorithms provided an efficient way to compute marginal probabilities and the expected hidden log-likelihood. These algorithms can be generalized to the sum-product algorithm for tree-like graphs and the junction tree algorithm for general DAGs. The computational complexity of the junction tree algorithm is exponential in the size of the largest clique of the graph [2].

Alternatively, if exact inference is computationally too expensive, then approximate inference can be used. For example, Gibbs sampling [14] is a MCMC technique for generating a sample from the joint distribution $P\left(X_{1}, \ldots, X_{L}\right)$. The idea is to iteratively sample from the conditional probabilities of $P\left(X_{1}, \ldots, X_{L}\right)$, starting with $X_{1}^{(n+1)} \sim P\left(X_{1} \mid\right.$ $\left.X_{2}^{(n)}, \ldots, X_{L}^{(n)}\right)$ and cycling through all variables in turns,

$$
X_{j}^{(n+1)} \sim P\left(X_{j} \mid X_{1}^{(n+1)}, \ldots, X_{j-1}^{(n+1)}, X_{j+1}^{(n)}, \ldots, X_{L}^{(n)}\right) \quad \text { for all } j=2, \ldots, L
$$

Gibbs sampling can be regarded as a special case of the Metropolis-Hastings algorithm. It is particularly useful, if it is much easier to sample from the conditionals $P\left(X_{k} \mid X_{\backslash k}\right)$ than from the joint distribution $P\left(X_{1}, \ldots, X_{L}\right)$, where $X_{\backslash k}$ denotes all variables $X_{n}$ except $X_{k}$. For graphical models, the conditional probability of each vertex $X_{k}$ depends only on its Markov blanket $X_{\mathrm{MB}}(k)$, defined as the set of its parents, children, and co-parents (vertices with the same children), $P\left(X_{k} \mid X_{\backslash k}\right)=P\left(X_{k} \mid X_{\mathrm{MB}(k)}\right)$.

Example 24 (Phylogenetic tree models). A phylogenetic tree model [11] for a set of aligned DNA sequences from different species is a Bayesian network model, where the graph is a tree in which the leaves represent the observed contemporary species and the interior vertices correspond to common extinct ancestors (Figure 12). The topology (graph structure) $S$ defines the branching order and the branch lengths correspond to (phylogenetic) time. The LPDs are defined by a nucleotide substitution model (Section 5).

Let $X^{(i)} \in\{\mathrm{A}, \mathrm{C}, \mathrm{G}, \mathrm{T},-\}^{L}$, denote the $i$-th column of a multiple sequence alignment of $L$ observed species. We regard the alignment columns as independent observations of the evolutionary process. The character states of the hidden (extinct) ancestors are denoted $Z^{(i)}$. The likelihood of the observed sequence data $X=\left(X^{(1)}, \ldots, X^{(N)}\right)$ given the tree topology $S$ and the branch lengths $t$ is

$$
P(X \mid S, t)=\sum_{Z} \prod_{i=1}^{N} P\left(X^{(i)}, Z^{(i)} \mid S, t\right)
$$

where $P\left(X^{(i)}, Z^{(i)} \mid S, t\right)$ factors into conditional probabilities according to the tree structure. This marginal probability can be computed efficiently with an instance of the sum-product algorithm known as the peeling algorithm (or Felsenstein algorithm) [10].

For example, in the tree displayed in Figure 12, each observation $X$ has probability

$$
\begin{aligned}
& P(X)=\sum_{Z} P(X, Z) \\
& =\sum_{Z} P\left(X_{1} \mid Z_{4}\right) P\left(X_{2} \mid Z_{1}\right) P\left(X_{3} \mid Z_{1}\right) P\left(X_{4} \mid Z_{2}\right) P\left(X_{5} \mid Z_{2}\right) P\left(Z_{1} \mid Z_{3}\right) \cdot \\
& \cdot P\left(Z_{2} \mid Z_{3}\right) P\left(Z_{3} \mid Z_{4}\right) P\left(Z_{4}\right) \\
& =\sum_{Z_{4}} P\left(Z_{4}\right) P\left(X_{1} \mid Z_{4}\right)\left[\sum_{Z_{3}} P\left(Z_{3} \mid Z_{4}\right)\left[\sum_{Z_{2}} P\left(Z_{2} \mid Z_{3}\right) P\left(X_{4} \mid Z_{2}\right) P\left(X_{5} \mid Z_{2}\right)\right] \cdot\right. \\
& \left.\cdot\left[\sum_{Z_{1}} P\left(Z_{1} \mid Z_{3}\right) P\left(X_{2} \mid Z_{1}\right) P\left(X_{3} \mid Z_{1}\right)\right]\right],
\end{aligned}
$$

where we have omitted the dependency on the branch length $t$. Several software packages implement ML or Bayesian learning of phylogenetic tree models.

In the simplest case we suppose that the observed alignment columns are independent. However, it is more realistic to assume that nucleotide substitution rates vary across sites because of varying selective pressures. For example, there could be differences between coding and non-coding regions, among different regions of a protein (loops, catalytic sites), or among the three bases of a triplet coding for an amino acid. More sophisticated models can account for this rate heterogeneity. Let us assume site-specific substitution rates $r_{i}$ such that the local probabilities become $P\left(X^{(i)} \mid r_{i}, t, S\right)$. To model the distribution of the rates often a gamma distribution is used.

Example 25 (Gamma distribution). The gamma distribution $\operatorname{Gamma}(\alpha, \beta)$ is parametrized by a shape parameter $\alpha$ and a rate parameter $\beta$. It is defined by the density function

$$
f(x)=\frac{\beta^{\alpha}}{\Gamma(\alpha)} x^{\alpha-1} e^{-\beta x}, \quad \text { for } x \geq 0
$$

Its expectation is $\mathrm{E}(X)=\alpha / \beta$ and its variance $\operatorname{Var}(X)=\alpha / \beta^{2}$. The gamma distribution generalizes several other distributions, for example, $\operatorname{Gamma}(1, \lambda)=\operatorname{Exp}(\lambda)$ (Example 19).

Another approach to account for varying mutation rates are phylogenetic hidden Markov models (phylo-HMMs).

Example 26 (Phylo-HMM). Phylo-HMMs [27] combine HMMs and phylogenetic trees into a single Bayesian network model. The idea is to use a hidden Markov model along the linear chain of the genomic sequence and, at each position, to condition a phylogenetic tree model on the hidden state space (Figure 13). This architecture allows for modeling different evolutionary histories at different sites of the genome. In particular, the model can account for heterogeneity in the rate of evolution, for example, due to functionally conserved elements, but it also allows for a change in tree topology along the sequence, a situation that can result from recombination [17]. Phylo-HMMs are also used for gene finding.

# List of Figures 

1 De Finetti diagram showing the Hardy-Weinberg curve $4 p_{\mathrm{AA}} p_{\mathrm{aa}}-p_{\mathrm{AA}}^{2}=0$ inside the probability simplex $\Delta_{2}=\left\{\left(p_{\mathrm{AA}}, p_{\mathrm{Aa}}, p_{\mathrm{aa}}\right) \mid p_{\mathrm{AA}}+p_{\mathrm{Aa}}+p_{\mathrm{aa}}=1\right\}$. Each point in this space represents a population as described by its genotype frequencies. Points on the curve correspond to populations in Hardy-Weinberg equilibrium.
2 Coverage distribution of a shotgun sequencing experiment with $n=10^{8}$ reads of length $L=100$ of the human genome of length $G=3 \cdot 10^{9}$. The average coverage is $c=n p=3.4$, where $p=L / G$. Dots show the binomial coverage distribution $\operatorname{Binom}(n, p)$ and the solid line its approximation by the Poisson distribution $\operatorname{Pois}(n p)$. Note that the Poisson distribution is also discrete and just shown as a line to distinguish it from the binomial distribution.
3 Marginalization. Left: two-dimensional histogram of a discrete bivariate distribution with the two marginal histograms. Right: contour plot of a two-dimensional Gaussian density with the marginal distributions of each component.
4 Likelihood function of the binomial model. The underlying data set consists of $k=7$ successes out of $N=10$ Bernoulli trials. The likelihood $L(p)=p^{k}(1-p)^{N-k}$ is plotted as a function of the model parameter $p$, the probability of success (solid line). The MLE is the maximum of this function, $\hat{p}_{\mathrm{ML}}=k / N=7 / 10$ (dashed line).
5 Bootstrap analysis of the ML allele frequency. The bootstrap distribution of the maximum likelihood estimator $\hat{p}_{\mathrm{ML}}=\left(2 n_{\mathrm{AA}}+n_{\mathrm{Aa}}\right) /(2 N)$ of the major allele frequency in the Hardy-Weinberg model is plotted for $B=100$ (left), $B=1,000$ (center), and $B=10,000$ (right) bootstrap samples, for the dataset $\left(n_{\mathrm{AA}}, n_{\mathrm{Aa}}, n_{\mathrm{aa}}\right)=(81,18,1)$.
6 Dirichlet prior for multinomial likelihood. The Dirichlet prior is conjugate to the multinomial likelihood. Shown are contour lines of the prior $\operatorname{Dir}(10,10,10)$ on the left, the multinomial likelihood $P\left(\left(n_{\mathrm{AA}}, n_{\mathrm{Aa}}, n_{\mathrm{aa}}\right)=(81,18,1) \mid \theta_{\mathrm{AA}}, \theta_{\mathrm{Aa}}, \theta_{\mathrm{aa}}\right)$ in the center, and the resulting posterior $\operatorname{Dir}(91,28,11)$ on the right. The posterior is the product of prior and likelihood.
7 Graphical representation of the naive Bayes model. Observed features $X_{n}$ are conditionally independent given the latent class variable $Z$.
8 Nucleotide substitution model. The state space and transitions of a general nucleotide substitution model are shown. For the Jukes-Cantor model (Example 17), all transition from any nucleotide to any other nucleotide have the same probability $\frac{1}{4}\left(1-e^{-4 \alpha t}\right)$.
9 Hidden Markov model. Shaded nodes represent observed random variables (or symbols) $X_{n}$, clear nodes represent hidden states (or the annotation). Directed edges indicate statistical dependencies which are given, respectively, by transition and emission probabilities among hidden states and between hidden states and observed symbols.
10 Profile hidden Markov model. The hidden state space and its transitions are shown for the profile hidden HMM of length $L=3$. Match states are denoted $M_{n}$, insert states $I_{n}$, and delete states $D_{n} . B$ and $E$ denote silent begin and end states, respectively. With match and insert states are associated probability tables for the emission of symbols (amino acids or nucleotides, and gaps).

11 Example of a Bayesian network. Vertices correspond to random variables and edges represent conditional probabilities. The graph encodes conditional independence statements about the random variables $U, V, W, X, Y$, and $Z$. Their joint probability factors according to the graph as $P(U, V, W, X, Y)=$ $P(U) P(Y) P(V \mid U, Y) P(W \mid V) P(X \mid U)$.
12 Phylogenetic tree model. The observed random variables $X_{i}$ represent contemporary species and the hidden random variables $Z_{i}$ their unknown common ancestors.
13 Phylo-HMM. Shown are the first four positions of a Phylo-HMM. The hidden Markov chain has random variables $Z$. In the trees, $Y$ denote the hidden common ancestors and $X$ the observed species. Note that the tree topology changes between position 2 and 3 .

![img-0.jpeg](img-0.jpeg)

Figure 1. De Finetti diagram showing the Hardy-Weinberg curve $4 p_{\mathrm{AA}} p_{\mathrm{aa}}-p_{\mathrm{Aa}}^{2}=0$ inside the probability simplex $\Delta_{2}=\left\{\left(p_{\mathrm{AA}}, p_{\mathrm{Aa}}, p_{\mathrm{aa}}\right) \mid\right.$ $\left.p_{\mathrm{AA}}+p_{\mathrm{Aa}}+p_{\mathrm{aa}}=1\right\}$. Each point in this space represents a population as described by its genotype frequencies. Points on the curve correspond to populations in Hardy-Weinberg equilibrium.

![img-1.jpeg](img-1.jpeg)

Figure 2. Coverage distribution of a shotgun sequencing experiment with $n=10^{8}$ reads of length $L=100$ of the human genome of length $G=$ $3 \cdot 10^{9}$. The average coverage is $c=n p=3.4$, where $p=L / G$. Dots show the binomial coverage distribution $\operatorname{Binom}(n, p)$ and the solid line its approximation by the Poisson distribution $\operatorname{Pois}(n p)$. Note that the Poisson distribution is also discrete and just shown as a line to distinguish it from the binomial distribution.

![img-2.jpeg](img-2.jpeg)

Figure 3. Marginalization. Left: two-dimensional histogram of a discrete bivariate distribution with the two marginal histograms. Right: contour plot of a two-dimensional Gaussian density with the marginal distributions of each component.

![img-3.jpeg](img-3.jpeg)

Figure 4. Likelihood function of the binomial model. The underlying data set consists of $k=7$ successes out of $N=10$ Bernoulli trials. The likelihood $L(p)=p^{k}(1-p)^{N-k}$ is plotted as a function of the model parameter $p$, the probability of success (solid line). The MLE is the maximum of this function, $\hat{p}_{\mathrm{ML}}=k / N=7 / 10$ (dashed line).

![img-4.jpeg](img-4.jpeg)

Figure 5. Bootstrap analysis of the ML allele frequency. The bootstrap distribution of the maximum likelihood estimator $\hat{p}_{\mathrm{ML}}=\left(2 n_{\mathrm{AA}}+n_{\mathrm{Aa}}\right) /(2 N)$ of the major allele frequency in the Hardy-Weinberg model is plotted for $B=100$ (left), $B=1,000$ (center), and $B=10,000$ (right) bootstrap samples, for the dataset $\left(n_{\mathrm{AA}}, n_{\mathrm{Aa}}, n_{\mathrm{aa}}\right)=(81,18,1)$.

![img-5.jpeg](img-5.jpeg)

Figure 6. Dirichlet prior for multinomial likelihood. The Dirichlet prior is conjugate to the multinomial likelihood. Shown are contour lines of the prior $\operatorname{Dir}(10,10,10)$ on the left, the multinomial likelihood $P\left(\left(n_{\mathrm{AA}}, n_{\mathrm{Aa}}, n_{\mathrm{aa}}\right)=(81,18,1) \mid \theta_{\mathrm{AA}}, \theta_{\mathrm{Aa}}, \theta_{\mathrm{aa}}\right)$ in the center, and the resulting posterior $\operatorname{Dir}(91,28,11)$ on the right. The posterior is the product of prior and likelihood.

![img-6.jpeg](img-6.jpeg)

Figure 7. Graphical representation of the naive Bayes model. Observed features $X_{n}$ are conditionally independent given the latent class variable $Z$.

![img-7.jpeg](img-7.jpeg)

Figure 8. Nucleotide substitution model. The state space and transitions of a general nucleotide substitution model are shown. For the Jukes-Cantor model (Example 17), all transition from any nucleotide to any other nucleotide have the same probability $\frac{1}{4}\left(1-e^{-4 \alpha t}\right)$.

![img-8.jpeg](img-8.jpeg)

Figure 9. Hidden Markov model. Shaded nodes represent observed random variables (or symbols) $X_{n}$, clear nodes represent hidden states (or the annotation). Directed edges indicate statistical dependencies which are given, respectively, by transition and emission probabilities among hidden states and between hidden states and observed symbols.

![img-9.jpeg](img-9.jpeg)

Figure 10. Profile hidden Markov model. The hidden state space and its transitions are shown for the profile hidden HMM of length $L=3$. Match states are denoted $M_{n}$, insert states $I_{n}$, and delete states $D_{n} . B$ and $E$ denote silent begin and end states, respectively. With match and insert states are associated probability tables for the emission of symbols (amino acids or nucleotides, and gaps).

![img-10.jpeg](img-10.jpeg)

Figure 11. Example of a Bayesian network. Vertices correspond to random variables and edges represent conditional probabilities. The graph encodes conditional independence statements about the random variables $U, V, W, X, Y$, and $Z$. Their joint probability factors according to the graph as $P(U, V, W, X, Y)=P(U) P(Y) P(V \mid U, Y) P(W \mid V) P(X \mid U)$.

![img-11.jpeg](img-11.jpeg)

Figure 12. Phylogenetic tree model. The observed random variables $X_{i}$ represent contemporary species and the hidden random variables $Z_{i}$ their unknown common ancestors.

![img-12.jpeg](img-12.jpeg)

Figure 13. Phylo-HMM. Shown are the first four positions of a PhyloHMM. The hidden Markov chain has random variables $Z$. In the trees, $Y$ denote the hidden common ancestors and $X$ the observed species. Note that the tree topology changes between position 2 and 3.