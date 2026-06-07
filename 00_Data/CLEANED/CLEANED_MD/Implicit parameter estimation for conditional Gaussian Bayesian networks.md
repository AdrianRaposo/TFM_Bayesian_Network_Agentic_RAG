# Implicit parameter estimation for conditional Gaussian Bayesian networks 

Aida Jarraya ${ }^{1,2}$, Philippe Leray ${ }^{2}$, Afif Masmoudi ${ }^{1}$<br>${ }^{1}$ Laboratory of Probability and Statistics<br>Faculty of Sciences of Sfax, Sfax University. B. P. 1171 Sfax. Tunisia<br>E-mail: jarraya_aida@yahoo.fr, Afif.Masmoudi@fss.rnu.tn<br>${ }^{2}$ LINA Computer Science Lab UMR 6241<br>Knowledge and Decision Team, University of Nantes, France.<br>E-mail: philippe.leray@univ-nantes.fr<br>Received 12 June 2012<br>Accepted 7 August 2013


#### Abstract

The Bayesian estimation of the conditional Gaussian parameter needs to define several a priori parameters. The proposed approach is free from this definition of priors. We use the Implicit estimation method for learning from observations without a prior knowledge. We illustrate the interest of such an estimation method by giving first the Bayesian Expectation A Posteriori estimator for conditional Gaussian parameters. Then, we describe the Implicit estimators for the same parameters. Moreover, an experimental study is proposed in order to compare both approaches.


Keywords: Conditional Gaussian Bayesian networks; Bayesian estimation; Implicit estimation; Parameter learning.

## 1. Introduction

Bayesian Networks (BNs) are probabilistic graphical models widely used for knowledge representation and reasoning within an uncertain framework ${ }^{1,2,3}$. Learning Bayesian networks from data, i.e., obtaining automatically the structure and parameters from information belonging to the available samples, is a NP hard problem ${ }^{4}$. In this paper, we focus on the first component of BN learning which is parameter learning. Classical methods such as Maximum Likelihood (ML) or Bayesian methods such as Maximum A Posteriori (MAP) or Expectation A Posteriori (EAP) can be used for parameter learning, whatever the BN parametrization: discrete BNs, linear Gaussian BNs, or conditional Gaussian BNs.

In fact, by using the Bayesian approach, the pos-
terior distribution is given by multiplying the likelihood function by a known prior distribution and then dividing by a norming constant. Consequently, this prior information is used, together with the data, in order to derive the posterior distribution. The use of prior allows us to take into account the expert knowledge. Nevertheless, this prior is not always available. As we know, the choice of a specific prior information in Bayesian approaches is often problematic and is even considered to represent the major weakness of such methods because a biased result can be obtained if we make a bad choice of the prior distribution. Hence, if we can find the posterior distribution with the data likelihood, the method will be much easier to use. This represents the principle of the Implicit approach ${ }^{5}$. This approach is similar to the Bayesian one, and happens

in a natural context without specifying any prior parameters. We use the Implicit method in order to overcome some of the shortcomings associated with the Bayesian estimation concerning the choice of the prior distribution parameters. The implicit approach has already been applied for learning parameters in discrete BNs ${ }^{6,7}$ with an extension for structure learning ${ }^{8}$. We propose here new theoretical results concerning Implicit learning in Conditional Gaussian Bayesian Networks (CGBNs) in different contexts used in real applications by dealing with tied or untied parameters. In such models, priors implied can be more complex to express as compared with the usual Dirichlet priors for discrete variables. By going back to the classical notations used in the domain, and following Murphy's work ${ }^{9}$ devoted to Maximum Likelihood (ML) and Bayesian Maximum A Posteriori (MAP) estimation for conditional Gaussian models, we enlarge them with Expectation A Posteriori (EAP) and Implicit approaches. The outline of this paper is organized as follows: in section 2, we briefly present the Implicit method and recall the principles of Implicit estimation. In section 3, we discuss the problem of parameter learning in CGBNs by using Bayesian estimation. In section 4, we present parameter estimation in CGBNs using Implicit approach. Then, both approaches are formally compared in section 5 and experimental results are provided in section 6 . Finally, we conclude with perspectives for future work.

## 2. Implicit estimation

### 2.1. Principle

The Bayesian estimation method gathers the information of the data (the data likelihood) with the information collected from past experience (prior distribution) and finds a new updated information (posterior distribution). The Implicit estimation is an alternative to Bayesian estimation and does not need to specify any prior for the parameters. In the context of the Bayesian theory, the unknown parameter $\theta$ in a statistical model is assumed to be a random variable with a known prior distribution. This prior information is used, together with the data, in order to derive the posterior distribution of $\theta$. The
choice of a prior is generally based on the preliminary knowledge of the problem. So, the basic idea of the Bayesian theory is to consider any parameter $\theta$ as a random variable and to determine its posterior distribution given the data and the assumed prior.
Alternatively, the concept of Implicit distribution previously proposed by ${ }^{5}$, can be described as a kind of posterior distribution of a parameter given the data. To explain the principle of Implicit distribution, let us consider a family of probability distributions $\{p(x \mid \theta), \theta \in \Theta\}$ parameterized by an unknown parameter $\theta$ in a set $\Theta$; where $x$ represents the observed data.
The Implicit distribution is computed by multiplying the likelihood function $p(x \mid \theta)$ by a counting measure $\sigma$ if $\Theta$ is a countable set and by a Lebesgue measure $\sigma$ if $\Theta$ is an open set ( $\sigma$ depends only on the topological structure of $\Theta$ ) and then, dividing by the norming constant $c(x)=\int_{\Theta} p(x \mid \theta) \sigma(d \theta)$. Therefore, the Implicit distribution is given by the following formula

$$
Q_{x}(d \theta)=\{c(x)\}^{-1} p(x \mid \theta) \sigma(d \theta)
$$

and plays the role of a posterior distribution of $\theta$ given $x$ in the Bayesian method, corresponding to a particular improper prior which depends only on the topology of $\Theta$ (without any statistical assumption). Provided its existence (which holds for most statistical models), the Implicit distribution can be used for the estimation of the parameter $\theta$ following a Bayesian methodology. The Implicit estimator $\widehat{\theta}$ of $\theta$ is nothing but the mean of the Implicit distribution, that is

$$
\widehat{\theta}=E(\theta \mid x)=\int_{\Theta} \theta Q_{x}(d \theta)
$$

Readers are referred to the paper from ${ }^{5}$ for a presentation of the theoretical foundations of Implicit estimation and some selected applications.

### 2.2. Example with variance estimation

Let $X_{i} \sim N\left(0, \sigma^{2}\right)$ be a centered Gaussian random variable with an unknown variance $\sigma^{2} \in$ $] 0,+\infty[$, the likelihood of $\sigma^{2}$ for $n$ independent observations $\underline{x}=\left(x_{1}, \ldots, x_{n}\right)$ is $l\left(\underline{x}, \sigma^{2}\right)=$ $\left(2 \pi \sigma^{2}\right)^{-\frac{1}{2}} \exp \left\{-\frac{1}{2 \sigma^{2}} \sum_{i=1}^{n} x_{i}^{2}\right\}$.

and then, its sample Implicit distribution $Q_{\lambda}\left(d \sigma^{2}\right)$ is given by

$$
Q_{\lambda}\left(d \sigma^{2}\right)=\frac{\left(\sigma^{2}\right)^{-\frac{n}{2}} \exp \left\{-\frac{1}{2 \sigma^{2}} \sum_{i=1}^{n} x_{i}^{2}\right\}}{\Gamma\left(\frac{n}{2}-1\right)}\left(\frac{1}{2} \sum_{i=1}^{n} x_{i}^{2}\right)^{\frac{n}{2}-1}
$$

By a standard calculation, we show that the Implicit estimator of $\sigma^{2}$ is

$$
\left(\widehat{\sigma}^{2}\right)^{I m p}=E\left(\sigma^{2} \mid X_{1}, \ldots, X_{n}\right)=\frac{1}{n-4} \sum_{i=1}^{n} X_{i}^{2}
$$

with $n>4$, which is different from the ML estimator for which the normalizing factor is $\frac{1}{n}$. We can compare this result with the Bayesian estimation obtained by the EAP (Expectation A Posteriori) approach

$$
\left(\widehat{\sigma}^{2}\right)^{B a y}=\frac{\sum_{i=1}^{n} X_{i}^{2}+2 b}{n+2 a-2}
$$

where the prior distribution of $\sigma^{2}$ is an InverseGamma $I G(a, b)$ with a shape parameter $a$ and a scale parameter $b$.

First, we can see that the Implicit estimator does not need to tune any hyper-parameters such as $a$ and $b$ in the EAP approach. We can also notice that the equality between the two estimators of variance obtained by Bayesian and Implicit approaches is established for $a=-1$ and $b=0$, which is impossible since $a$ and $b$ (parameters of an Inverse Gamma distribution) have to be positive. This shows that the Implicit estimator does not correspond to a Bayesian one for specific prior values. To compare the performances of Implicit and Bayesian method, we start (as a first step) by simulation of data using Matlab software, and (in the second step) we validate our results by comparing them with those of the Bayesian method. To compare two statistical approaches and to appreciate in which measure the result will be more definite, we choose an indicator which is the Mean Squared Errors (MSE) between the estimator and the true value of the parameter. We generated 1000 observations from the Gaussian model, then we compare the Bayesian and Implicit estimators in terms of the mean squared errors (MSE) for different true parameter values of $\sigma^{2}$. We replicate the
process 10000 times and we compute the average estimates and the MSE. We perform two Bayesian simulation studies based on two different prior densities for the parameter $\sigma^{2}$. The results are reported in Table 1.

Bayesian estimation (Bay*) is obtained by specifying true values as prior parameters. Bayesian estimation (Bay**) corresponds to parameters estimated by using prior values different from the true ones.

The comparison of MSE obtained by Bay* and Bay** proves the sensibility of the parameter estimation with respect to the choice of the prior distribution. This result proves the fragility of the Bayesian estimation. A biased result can be obtained if we make a bad choice of the prior distribution. Results obtained by Implicit approach (without need of any prior information) and Bay* approach (based on true values as priors) are close to the true values. We notice a very good concordance between both approaches. However, we may point out a better precision of parameter estimated by Implicit method than the corresponding one for Bay** method (with priors different from true values). These results are illustrated in Fig.1. The yellow part corresponds to the area where the Implicit MSE is smaller than the Bayesian MSE with respect to the values of the prior coefficients $a$ and $b$. Whatever the value of $\sigma^{2}$ (a low or a high one), the Implicit MSE is often lower than the Bayesian one.

### 2.3. Related works

As seen previously, the Implicit estimation does not rely on a prior definition. Another alternative to Bayesian method, with the objective to get a distribution of the unknown parameter $\theta$ without any priors is the Fiducial distribution introduced by ${ }^{10}$. It describes the uncertainty about the value of the fixed unknown parameter $\theta$ by supposing that there is a population characterized by the density function $p(x, \theta)$, where the form of the density $p(x, \theta)$ is known, but there is no prior information available about the true value of the parameter $\theta^{11}$.

Mukhopadhyay ${ }^{12}$ claimed that the Implicit inference is nothing new and that it is either a Fiducial-like approach or a non-informative Bayesian method. Concerning his criticism, our


Table 1: Estimators of $\sigma^{2}$ obtained by Implicit method, Bayesian method with true a priori (Bay ${ }^{\times}$) and different one (Bay ${ }^{\times \times}$), for several prior parameters ( $a$ and $b$ ) and $\sigma^{2}$.
![img-0.jpeg](img-0.jpeg)

Figure 1: Difference between Bayesian and Implicit mean squared errors with respect to prior parameters $a$ and $b$ for $\sigma^{2}=0.1$ and $\sigma^{2}=2$.
comment is to show that Implicit inference is in fact a new paradigm in statistical inference. Using several examples, we show that, in many cases when the parameter space $\theta$ is infinite, Implicit distribution does not coincide with neither Fiducial nor Bayesian distribution. If the parameter space $\theta$ is bounded, then the Implicit distribution coincides with the posterior distribution with uniform prior in Bayesian method. The coincidence of both Implicit and Fiducial distributions in the normal model $N(\theta, 1)$ with a mean $\theta$ and a variance 1 , seems to explain the misleading comments of ${ }^{12}$. In what follows, we give selected examples illustrating clearly the difference between Implicit, Bayesian and Fiducial approaches.

### 2.3.1. Example 1: Binomial model $B(n, \theta)$

In the Binomial case, applying the Implicit method gives:

$$
c(x)=\frac{1}{n+1}
$$

It comes that the Implicit distribution of $\theta$ given $x$ is a Beta distribution with parameters $x+1$ and $n-x+1$, denoted $\operatorname{Beta}(x+1, n-x+1)$. Heike and al ${ }^{11}$ showed that, for the same binomial model, the Fiducial distribution is a Beta distribution denoted $\operatorname{Beta}(x, n-x+1)$, with parameters $x$ and $n-x+1$.

### 2.3.2. Example 2: Exponential model $\varepsilon(\theta)$

Let $X_{1}, \ldots, X_{n}$ be $n$ independent random variables identically distributed according to the exponential distribution with parameter $\theta$. It is well known that

$\sum_{i=1}^{n} X_{i}$ follows a gamma distribution denoted $\gamma(n, \theta)$, with parameters $n$ and $\theta$.
The norming constant is given by

$$
c\left(x_{1}, \ldots, x_{n}\right)=\frac{n!}{\left(\sum_{i=1}^{n} x_{i}\right)^{n+1}}
$$

Then, the Implicit distribution of $\theta$ given $X_{1}, \ldots, X_{n}$ is a gamma distribution denoted $\gamma\left(n+1, \sum_{i=1}^{n} x_{i}\right)$, with parameters $n+1$ and $\sum_{i=1}^{n} x_{i}$. For the same model, ${ }^{11}$ showed that the Fiducial distribution is a gamma distribution denoted $\gamma\left(n, \sum_{i=1}^{n} x_{i}\right)$, with parameters $n$ and $\sum_{i=1}^{n} x_{i}$. Then, the difference between the two methods is very clear. The first parameter is $n+1$ in the case of Implicit method but, in the Fiducial method, it is $n$.

## 3. Parameter estimation in conditional Gaussian Bayesian networks using Bayesian approach

In this section, we formally define Conditional Gaussian Bayesian Networks. We inspire from Murphy's work ${ }^{9}$ devoted to MAP and ML estimation for parameters of such models and we enlarge them with EAP estimation.

### 3.1. Definitions and notations

Bayesian Networks (BNs) are usually defined for discrete variables with a finite number of states. This assumption is not very realistic in several application areas such as medicine, where the elaboration of the diagnosis is generally the result of some mixture of information of continuous type (results of laboratory) and of discrete type (presence / absence of a symptom).

In the literature, previous works have concentrated on the study of probabilistic graphical models with both discrete and continuous variables ${ }^{13,14,15}$.

In this paper, we are interested in domains containing either continuous variables or a mixture of both discrete and continuous variables, under the assumption that continuous data constitute a sample from a multivariate normal (Gaussian) distribution. Consider a finite set $X=\left\{X_{1}, \ldots, X_{n}\right\}$ of random variables. A Bayesian network (BN) is a directed acyclic graph $G$ and a set of conditional probability distributions which represent a joint probability distribution ${ }^{1}$. The nodes of the graph correspond to the random variables and are annotated with a Conditional Probability Density (CPD) of the random variable given its parents $P a_{i}$ in the graph G. The joint distribution is the product over families (variable and its parents)

$$
p\left(X_{1}, \ldots, X_{n}\right)=\prod_{i=1}^{n} p\left(X_{i} \mid P a_{i}\right)
$$

The graph G represents independence properties which are assumed to hold in the underlying distribution: each $X_{i}$ is independent from its nondescendants given its parents $P a_{i}$.
Unlike the case of discrete variables (when the variable $X$ and some or all of its parents are real valued), there is no representation that can integrate all conditional densities. A common choice is the use of linear Gaussian conditional densities ${ }^{16}$, where each variable is a linear function of its parents. When all the variables in a network have linear Gaussian conditional densities, the joint density over $X$ is a multivariate Gaussian. In order to simplify future equations, we summarize below the notations initially proposed by Murphy ${ }^{9}$. We will consider the problem of finding estimators for the parameters of a conditional Gaussian variable $Y$ with continuous parent $X$ and discrete parent $Q$, i.e., $p(y \mid x, Q=$ $i)=c\left|\Sigma_{i}\right|^{-\frac{1}{2}} \exp \left(-\frac{1}{2}\left(y-B_{i} x-\mu_{i}\right)^{\prime} \Sigma_{i}^{-1}\left(y-B_{i} x-\mu_{i}\right)\right)$ where $c$ is a constant and $|y|=d$. We assume that we have $N$ iid training cases $\left\{e_{t}\right\}$ so the complete data log-likelihood is $\log \prod_{t=1}^{N} \prod_{i=1}^{|Q|} p\left(y_{t} \mid x_{t}, Q_{t}=i, e_{t}\right)^{q_{t}^{i}}$ where $q_{t}^{i}=1$ if $Q$ has the value $i$ in the t'th complete case, and 0 otherwise. Since $Q, X$ and $Y$ may all be unobserved, the expected complete-data likelihood is defined by $\widetilde{p}(y \mid x, Q=i)=\exp (l)$ with $l=$ $-\frac{1}{2} \sum_{t} E\left(\sum_{i} q_{t}^{i} \log \left|\Sigma_{i}\right|+q_{t}^{i}\left(y_{t}-B_{i} x_{t}-\mu_{i}\right)^{\prime} \Sigma_{i}^{-1}\left(y_{t}-\right.\right.$

$\left.B_{i} x_{t}-\mu_{i}\right)\left|e_{t}\right\rangle$.
We can write
$E\left(q_{t}^{i} x_{t} x_{t}^{\prime} \mid e_{t}\right)=E\left(q_{t}^{i} \mid e_{t}\right) E\left(x_{t} x_{t}^{\prime} \mid Q_{t}=i, e_{t}\right)=$ $w_{t}^{i} E\left(X X^{\prime}\right)$ where the weights $w_{t}^{i}=p\left(Q=i \mid e_{t}\right)$ are posterior probabilities and $E_{t i}\left(X X^{\prime}\right)$ is a conditional second moment. We get $l=-\frac{1}{2} \sum_{t} \sum_{i} w_{t}^{i} \log \left|\Sigma_{i}\right|-$ $\frac{1}{2} \sum_{t} \sum_{i} w_{t}^{i} E_{t i}\left(\left(y_{t}-B_{i} x_{t}-\mu_{i}\right)^{\prime} \Sigma_{i}^{-1}\left(y_{t}-B_{i} x_{t}-\right.\right.$ $\left.\left.\mu_{i}\right) \mid e_{t}\right)$.
The following expected sufficient statistics are introduced in order to simplify future equations:

$$
\begin{gathered}
w_{i}=\sum_{t} w_{t}^{i} \\
S_{X X^{\prime}, i}=\sum_{t} w_{t}^{i} E_{t i}\left(X X^{\prime}\right) \\
S_{X, i}=\sum_{t} w_{t}^{i} E_{t i}(X) \\
S_{Y Y^{\prime}, i}=\sum_{t} w_{t}^{i} E_{t i}\left(Y Y^{\prime}\right) \\
S_{Y^{\prime} Y, i}=\sum_{t} w_{t}^{i} E_{t i}\left(Y^{\prime} Y\right) \\
S_{Y, i}=\sum_{t} w_{t}^{i} E_{t i}(Y) \\
S_{X Y^{\prime}, i}=\sum_{t} w_{t}^{i} E_{t i}\left(X Y^{\prime}\right) \\
S_{Y X^{\prime}, i}=\sum_{t} w_{t}^{i} E_{t i}\left(Y X^{\prime}\right)
\end{gathered}
$$

Usually, two situations can be considered when dealing with the parameters of CGBNs models. The first one (untied parameters) corresponds to the general one, with the parameters defined in the previous definition. In this situation, if one continuous variable has continuous and discrete parents, we will have to deal with conditional Gaussian parameters (mean, covariance, regression coefficients) for each configuration of the discrete parents. The second situation (tied parameters) considers that the conditional Gaussian parameters are independent from the discrete parents. This assumption reduces the number of parameters which can be interesting when the number of data is limited.

Another way to decrease the number of parameters when estimating the covariance matrix is to
consider a spherical covariance matrix, i.e. the constraint that $\Sigma_{i}=\sigma_{i}^{2} I$ is isotropic.

The remaining of this section will be devoted to the proposition of Bayesian estimation (with Expectation A Posteriori method) of conditional Gaussian parameters (regression coefficients, mean, covariance) for all these situations (untied or tied parameters, full or spherical covariance matrix).

### 3.2. Regression matrix estimation

### 3.2.1. Untied parameters

$\tilde{p}\left(y \mid B_{i}, x_{t}, \Sigma_{i}, \mu_{i}\right) \propto \exp \left(-\frac{1}{2} \sum_{t=1}^{N}\left(y_{t}-B_{i} x_{t}-\right.\right.$ $\left.\left.\mu_{i}\right)^{\prime} \Sigma_{i}^{-1}\left(y_{t}-B_{i} x_{t}-\mu_{i}\right)\right)$.
We classically assume that the prior for $B_{i}$ is a multivariate normal distribution with mean $a$ and covariance matrix $V$.
Hence, the posterior $\tilde{p}\left(B_{i} \mid y_{t}, x_{t}, \Sigma_{i}, \mu_{i}\right)=$ $\exp \left(-\frac{1}{2} \sum_{t=1}^{N} w_{t}^{i} E_{t_{i}}\left(y_{t}-B_{i} x_{t}-\mu_{i}\right)^{\prime} \Sigma_{i}^{-1}\left(y_{t}-B_{i} x_{t}-\right.\right.$ $\left.\left.\mu_{i}\right)\right) \exp \left(-\frac{1}{2}\left(B_{i}-a\right)^{\prime} V^{-1}\left(B_{i}-a\right)\right)$ is also a multivariate normal distribution with a mean given by

$$
\begin{aligned}
\widetilde{B}_{i}^{B a y}= & \left(\Sigma_{i}^{-1}\left(S_{Y X^{\prime}, i}-\mu_{i} S_{X^{\prime}, i}\right)+a V^{-1}\right) \\
& \left(\Sigma_{i}^{-1} S_{X X^{\prime}, i}+V^{-1}\right)^{-1}
\end{aligned}
$$

### 3.2.2. Tied parameters

For the tied case, the estimator of $B_{i}$ becomes

$$
\begin{aligned}
\widehat{B}^{B a y}= & \left(\sum_{i}\left(\Sigma_{i}^{-1}\left(S_{Y X^{\prime}, i}-\mu_{i} S_{X^{\prime}, i}\right)+a V^{-1}\right)\right) \\
& \left(\sum_{i}\left(\Sigma_{i}^{-1} S_{X X^{\prime}, i}+V^{-1}\right)\right)^{-1}
\end{aligned}
$$

### 3.3. Mean estimation

### 3.3.1. Untied parameters

For the mean parameter $\mu_{i}$, the prior density is a multivariate normal distribution with parameters $(m, \psi)^{16,3}$
$\widetilde{P}\left(\mu_{i} / y_{t}, x_{t}, \Sigma_{i}, B_{i}\right) \propto \exp \left(-\frac{1}{2} \sum_{t=1}^{N} w_{t}^{i} E_{t_{i}}\left(y_{t}-B_{i} x_{t}-\right.\right.$

$\left.\mu_{i}\right)^{\prime} \Sigma_{i}^{-1}\left(y_{t}-B_{i} x_{t}-\mu_{i}\right) \exp \left(-\frac{1}{2}\left(\mu_{i}-m\right)^{\prime} \psi^{-1}\left(\mu_{i}-\right.\right.$ $m)$ )

After some calculations applied to the posterior density and using the following identity

$$
\frac{\partial(X A+b)^{\prime} C(X A+b)}{\partial X}=\left(C+C^{\prime}\right)(X A+b) A^{\prime}
$$

we get the following expression

$$
\begin{aligned}
\widehat{\mu}_{i}^{B a y}= & \left(\psi^{-1} m+\Sigma_{i}^{-1}\left(S_{Y, i}-B_{i} S_{X, i}\right)\right) \\
& \left(w_{i} \Sigma_{i}^{-1}+\psi^{-1}\right)^{-1}
\end{aligned}
$$

### 3.3.2. Tied parameters

For the tied case, we get

$$
\begin{aligned}
\widehat{\mu}^{B a y}= & \left(\sum_{i}\left(\psi^{-1} m+\Sigma_{i}^{-1}\left(S_{Y, i}-B_{i} S_{X, i}\right)\right)\right) \\
& \left(\sum_{i}\left(w_{i} \Sigma_{i}^{-1}+\psi^{-1}\right)\right)^{-1}
\end{aligned}
$$

### 3.4. Estimating the regression matrix and the mean simultaneously

Since the equation for $B_{i}$ depends on $\mu$ and vice versa, if both of them have to be estimated, we must estimate them jointly. We can do this by appending $\mu_{i}$ as the last column to $B_{i}$ in order to create $D_{i}$, and also appending a 1 to the last component of $X$ in order to create $Z$. Then, we have
$p(y \mid x, Q=i)=c\left|\Sigma_{i}\right|^{-\frac{1}{2}} \exp \left(-\frac{1}{2}\left(y-D_{i} z\right)^{\prime} \Sigma_{i}^{-1}\left(y-D_{i} z\right)\right)$.
By using the equation 5 with $\mu_{i}=0$ and replacing $S_{X X^{\prime}, i}$ by $S_{Z Z^{\prime}}$ and also $S_{Y X^{\prime}, i}$ by $S_{Y Z^{\prime}, i}$ we get

$$
\widehat{D}_{i}^{B a y}=\left(\Sigma_{i}^{-1} S_{Y Z^{\prime}, i}+a V^{-1}\right)\left(\Sigma_{i}^{-1} S_{Z Z^{\prime}, i}+V^{-1}\right)^{-1}
$$

The substitutions are

$$
E_{t_{i}} Z Z^{\prime}=E_{t_{i}}\left(\begin{array}{cc}
X X^{\prime} & X \\
X^{\prime} & 1
\end{array}\right)
$$

so,

$$
S_{Z Z^{\prime}, i}=\left(\begin{array}{cc}
S_{X X^{\prime}, i} & S_{X, i} \\
S_{X^{\prime}, i} & w_{i}
\end{array}\right)
$$

and

$$
E_{t_{i}} Y Z^{\prime}=E_{t_{i}}\left(\begin{array}{ll}
Y X^{\prime} & Y
\end{array}\right)
$$

Then,

$$
S_{Y Z^{\prime}, i}=\left(\begin{array}{ll}
S_{Y X^{\prime}, i} & S_{Y}
\end{array}\right)
$$

### 3.5. Full Covariance matrix estimation

### 3.5.1. Untied parameters

We classically assume that the prior for $\Sigma_{i}$ is an Inverse-Wishart distribution with $\alpha$ degrees of freedom and a positive definite precision matrix $V$ which implies that the posterior density for the parameter $\Sigma_{i}$ is proportional to the following expression:
$\widetilde{p}\left(\Sigma_{i} \mid y_{t}, x_{t}, B_{i}, \mu_{i}\right) \propto\left|\Sigma_{i}\right|^{-\frac{w_{i}+\alpha+d+1}{2}} \exp \left(-\frac{1}{2} \operatorname{tr}\left(\Sigma_{i}^{-1} \sum_{t} \sum_{i}\right.\right.$ $\left.\left.w_{i}^{t} E_{t i}\left(y_{t}-B_{i} x_{t}-\mu_{i}\right)\left(y_{t}-B_{i} x_{t}-\mu_{i}\right)^{\prime}+V^{-1}\right)\right)$.

Hence, the posterior $\widetilde{p}\left(\Sigma_{i} \mid B_{i}, y_{t}, x_{t}, \mu_{i}\right)$ is also an Inverse-Wishart distribution with $\left(w_{i}+\alpha\right)$ degrees of freedom and a positive definite precision matrix $\sum_{i} w_{i}^{t} E_{t i}\left(y_{t}-B_{i} x_{t}-\mu_{i}\right)\left(y_{t}-B_{i} x_{t}-\mu_{i}\right)^{\prime}+V^{-1}$.
So,

$$
\widehat{\Sigma}_{i}^{B a y}=\frac{1}{w_{i}+\alpha-d-1}\left(A_{i}+V\right)
$$

where $A_{i}=S_{Y Y^{\prime}, i}-S_{Y X^{\prime}, i} B_{i}^{\prime}-S_{Y, i} \mu_{i}^{\prime}-B_{i} S_{X Y^{\prime}, i}+$ $B_{i} S_{X X^{\prime}, i} B_{i}^{\prime}+B_{i} S_{X, i} \mu_{i}^{\prime}-\mu_{i} S_{Y^{\prime}, i}+\mu_{i} S_{X^{\prime}, i} B_{i}^{\prime}+\mu_{i} \mu_{i}^{\prime}$.

If $B_{i}=0$, then we have

$$
\widehat{\Sigma}_{i}^{B a y}=\frac{S_{Y Y^{\prime}, i}-S_{Y, i} \mu_{i}^{\prime}-\mu_{i} S_{Y^{\prime}, i}+\mu_{i} \mu_{i}^{\prime}+V}{w_{i}+\alpha-d-1}
$$

### 3.5.2. Tied parameters

if $\Sigma_{i}$ is tied, we get

$$
\widehat{\Sigma}^{B a y}=\frac{1}{N(\alpha-d)} \sum_{i}\left(A_{i}+V\right)
$$

### 3.6. Spherical covariance matrix estimation

### 3.6.1. Untied parameters

$p(y \mid x, Q=i)=c \sigma_{i}^{-d} \exp \left(-\frac{1}{2} \sigma_{i}^{-2}\left\|y-B_{i} x_{t}-\mu_{i}\right\|^{2}\right)$.
For the $\sigma_{i}^{2}$, we classically assume that the prior is an Inverse-Gamma distribution with parameters $(a, b)$

$$
\widetilde{p}\left(\sigma_{i}^{2} \mid y_{t}, x_{t}, B_{i}, \mu_{i}\right) \quad \propto \quad\left(\sigma_{i}^{2}\right)^{-\frac{\alpha x_{t}}{2}-a-1} \exp \left(-\right.
$$

$\left.\frac{1}{2 \sigma_{i}^{2}}\left(\sum_{t} w_{t}^{t} E_{t i}\left(\left\|y_{t}-B_{i} x_{t}-\mu_{i}\right\|^{2}\right)+b\right)\right)$.
In fact, after some computations applied to the posterior density, we get the following expression for the estimator of $\sigma_{i}^{2}$

$$
\left(\widehat{\sigma_{i}^{2}}\right)^{B a y}=\frac{1}{d w_{i}+2 a-2} \operatorname{tr}\left(C_{i}+2 b\right)
$$

where
$C_{i}=S_{Y^{\prime} Y, i}-B_{i} S_{Y^{\prime} X, i}-S_{Y^{\prime}, i} \mu_{i}-B_{i}^{\prime} S_{X^{\prime} Y, i}+$ $B_{i}^{\prime} B_{i} S_{X^{\prime} X, i}+B_{i}^{\prime} \mu_{i} S_{X^{\prime}, i}-\mu_{i}^{\prime} S_{Y, i}+\mu_{i}^{\prime} B_{i} S_{X, i}+\mu_{i}^{\prime} \mu_{i}$.
If we don't have any regression, then
$\left(\widehat{\sigma}_{i}^{2}\right)^{B a y}=\frac{\operatorname{tr}\left(S_{Y^{\prime} Y, i}-S_{Y^{\prime}, i} \mu_{i}-\mu_{i}^{\prime} S_{Y, i}+\mu_{i}^{\prime} \mu_{i}+2 b\right)}{d w_{i}+2 a-2}$.

### 3.6.2. Tied parameters

If $\sigma_{i}^{2}$ is tied, we have

$$
\left(\widehat{\sigma^{2}}\right)^{B a y}=\frac{1}{N(d+2 a-2)} \operatorname{tr} \sum_{i}\left(C_{i}+2 b\right)
$$

## 4. Parameter estimation in Conditional Gaussian Bayesian Networks using Implicit approach

As seen in section 2.3, if the parameter space is bounded, then the Implicit distribution coincides with the posterior distribution with a uniform prior in Bayesian method, which is not the case for conditional Gaussian parameters.

Using the same notation of the previous section, we propose here the estimation of parameters by the Implicit method.

### 4.1. Regression matrix estimation

### 4.1.1. Untied parameters

Let $\widetilde{p}(y \mid x, Q=i)=\exp (l) \widetilde{p}\left(B_{i} \mid y_{t}, x_{t}, \Sigma_{i}, \mu_{i}\right) \propto$ $\exp \left(-\frac{1}{2} \sum_{t} w_{t}^{t} E_{t i}\left(y_{t}-B_{i} x_{t}-\mu_{i}\right)^{\prime} \Sigma_{i}^{-1}\left(y_{t}-B_{i} x_{t}-\mu_{i}\right)\right)$.
By a standard calculation and using equation 5, we show that the Implicit estimator of $B_{i}$ is

$$
\widehat{B}_{i}^{I m p}=\left(S_{Y X^{\prime}, i}-\mu_{i} S_{X^{\prime}, i}\right)\left(S_{X X^{\prime}, i}\right)^{-1}
$$

### 4.1.2. Tied parameters

For the tied case, we get

$$
\widehat{B}^{I m p}=\sum_{i}\left(S_{Y X^{\prime}, i}-\mu_{i} S_{X^{\prime}, i}\right)\left(\sum_{t} S_{X X^{\prime}, i}\right)^{-1}
$$

### 4.2. Mean estimation

### 4.2.1. Untied parameters

The Implicit estimator of $\mu_{i}$ is a Normal distribution $\widetilde{p}\left(\mu_{i} \mid y_{t}, x_{t}, \Sigma_{i}, B_{i}\right) \propto \exp \left(-\frac{1}{2} \sum_{t} w_{t}^{t} E_{t i}\left(y_{t}-B_{i} x_{t}-\right.\right.$ $\left.\left.\mu_{i}\right)^{\prime} \Sigma_{i}^{-1}\left(y_{t}-B_{i} x_{t}-\mu_{i}\right)\right)$.
Then, by using equation 5, we have

$$
\widehat{\mu}_{i}^{I m p}=\frac{S_{Y, i}-B_{i} S_{X, i}}{\sum_{t} w_{t}^{i}}
$$

If $B_{i}=0$ (No regression), the estimator of $\mu_{i}$ becomes

$$
\widehat{\mu}_{i}^{I m p}=\frac{S_{Y, i}}{\sum_{t} w_{t}^{i}}
$$

### 4.2.2. Tied parameters

For the tied case, we get

$$
\widehat{\mu}^{I m p}=\frac{\sum_{i}\left(S_{Y, i}-B_{i} S_{X, i}\right)}{N}
$$

### 4.3. Estimating the regression matrix and the mean simultaneously

Since both the equation for $B_{i}$ and $\mu$ are mutually dependent on each other, we present the expression estimating them jointly. By applying the same method used in section 3.4, we get

$$
\widehat{D}_{i}^{I m p}=S_{Y Z^{\prime}, i} S_{Z Z^{\prime}, i}^{-1}
$$

### 4.4. Full Covariance matrix estimation

### 4.4.1. Untied parameters

$\widehat{p}\left(\Sigma_{i} \mid y_{t}, x_{t}, B_{i}, \mu_{i}\right) \propto\left|\Sigma_{i}\right|^{-\frac{w_{i}}{2}} \exp \left(-\frac{1}{2} \sum_{t} w_{t}^{i} E_{t i}\left(y_{t}-\right.\right.$ $\left.\left.B_{i} x_{t}-\mu_{i}\right)^{\prime} \Sigma_{i}^{-1}\left(y_{t}-B_{i} x_{t}-\mu_{i}\right)\right) \quad \propto$ $\left|\Sigma_{i}\right|^{-\frac{w_{i}}{2}} \exp \left(-\frac{1}{2} \operatorname{tr}\left(\Sigma_{i}^{-1} \sum_{t} w_{t}^{i} E_{t i}\left(y_{t}-B_{i} x_{t}-\mu_{i}\right)\left(y_{t}-\right.\right.\right.$ $\left.\left.B_{i} x_{t}-\mu_{i}\right)^{\prime}\right)$
where $\widehat{p}\left(\Sigma_{i} \mid y_{t}, x_{t}, B_{i}, \mu_{i}\right)$ is an Inverse-Wishart distribution with $\left(w_{i}-d-1\right)$ degrees of freedom and a positive definite precision matrix
$\sum_{t} w_{t}^{i} E_{t i}\left(y_{t}-B_{i} x_{t}-\mu_{i}\right)\left(y_{t}-B_{i} x_{t}-\mu_{i}\right)^{\prime}$.
Then, the Implicit estimator of $\Sigma_{i}$ is given by

$$
\widehat{\Sigma}_{i}^{I m p}=\frac{1}{w_{i}-2 d-2}\left(A_{i}\right)
$$

If there is no regression, the estimator of $\Sigma_{i}$ becomes

$$
\widehat{\Sigma}_{i}^{I m p}=\frac{S_{Y Y^{\prime}}-S_{Y \mu_{i}^{\prime}}-\mu_{i} S_{Y^{\prime}}+\mu_{i} \mu_{i}^{\prime}}{w_{i}-2 d-2}
$$

### 4.4.2. Tied parameters

For the tied case, we have

$$
\widehat{\Sigma}^{I m p}=\frac{1}{N-2 d N-2 N}\left(\sum_{i} A_{i}\right)
$$

### 4.5. Spherical covariance matrix estimation

### 4.5.1. Untied parameters

If we have the constraint that $\Sigma_{i}=\sigma_{i}^{2} I$ is isotropic, the conditional density of $Y$ becomes
$p(y \mid x, Q=i)=c \sigma_{i}^{-d} \exp \left(-\frac{1}{2} \sigma_{i}^{-2}\left\|y-B_{i} x-\mu_{i}\right\|^{2}\right) l=$ $-d \sum_{t} \sum_{i} w_{t}^{i} \log \left|\sigma_{i}\right|-\frac{1}{2} \sigma_{i}^{-2} \sum_{t} \sum_{i} w_{t}^{i} E_{t i}\left\|y_{t}-B_{i} x_{t}-\right.$ $\left.\mu_{i}\right\|^{2}$.
Hence,
$\widehat{p}(y \mid x, Q=i)=\exp \left(-d \sum_{t} \sum_{i} w_{t}^{i} \log \left|\sigma_{i}\right|-\right.$ $\left.\frac{1}{2} \sigma_{i}^{-2} \sum_{t} \sum_{i} w_{t}^{i} E_{t i}\left\|y_{t}-B_{i} x_{t}-\mu_{i}\right\|^{2}\right)$
where $\sigma_{i}^{2}$ follows an Inverse-Gamma distribution
with a shape parameter $\left(\frac{w_{i} d}{2}-1\right)$ and a scale parameter $\left(\frac{1}{2} \sum_{t} w_{t}^{i} E_{t i}\left\|y_{t}-B_{i} x_{t}-\mu_{i}\right\|^{2}\right)$.
We can easily deduce that the Implicit estimator of $\sigma_{i}^{2}$ is
$\left(\widehat{\sigma}_{i}^{2}\right)^{I m p}=\frac{\sum_{t} w_{t}^{i} E_{t i}\left(\left\|y_{t}-B_{i} x_{t}-\mu_{i}\right\|^{2}\right)}{d w_{i}-4}$.
In order to compute the expected value of this distance, we use the fact that $x^{\prime} A y=\operatorname{tr}\left(x^{\prime} A y\right)=$ $\operatorname{tr}\left(A y x^{\prime}\right)$. So, $E\left[x^{\prime} A y\right]=\operatorname{tr}\left(A E\left[y x^{\prime}\right]\right)$.
Hence,

$$
\left(\widehat{\sigma}_{i}^{2}\right)^{I m p}=\frac{1}{d w_{i}-4} \operatorname{tr}\left(C_{i}\right)
$$

### 4.5.2. Tied parameters

For the tied case, we have

$$
\left(\widehat{\sigma}^{2}\right)^{I m p}=\frac{1}{N d-4 N} \operatorname{tr}\left(\sum_{i} C_{i}\right)
$$

## 5. Comparative study

Table 2 provides us a summary of the estimators of conditional Gaussian distribution parameters $\left(\mu_{i}, B_{i}, \Sigma_{i}\right)$ obtained by Maximum of Likelihood and by Expectation A Posteriori (described in section 3) and our Implicit method (described in section 4).

First, we notice that there is a difference between the Implicit estimator and the classical ML one when estimating the covariance matrix, whereas both estimators coincide for the mean and regression parameters. According to our knowledge, there is no theoretical work which explains these coincidences. Concerning the comparison between Implicit and Bayesian estimation, we point out that the parameters estimated by Bayesian approach depend on the prior parameters and, as we know, the choice of a specific prior information has always been problematic, hence representing the major weakness of this approach. In most cases, we either need an expert to get the prior knowledge or, we have to use non informative priors.

Since Implicit and ML approaches coincide for the estimation of the mean parameter $\mu$ and also the parameter of regression $B$, we only have to compare them with the Bayesian (EAP) estimation of


Table 2: Estimation of conditional Gaussian distribution parameters $\left(\mu_{i}, B_{i}, \Sigma_{i}\right)$ obtained by Implicit method (section 4), Maximum of Likelihood $\left({ }^{9}\right)$ and Expectation A Posteriori (section 3).
the covariance matrix. We can point out that the Implicit estimator of $\hat{\Sigma}$ corresponds to the Bayesian one (EAP) by taking $V=0$ and $\alpha=d-1$. However, this situation is impossible because $V$ is a positive definite precision matrix. This situation is similar to the one described in section 2.2 for $\sigma^{2}$ estimation.

Since the parameter space is infinite, the Implicit distribution does not coincide with neither Fiducial nor Bayesian distribution. Therefore, our Implicit estimation should give more robust results than the Bayesian ones, particularly if the priors used in Bayesian estimation are far away from the true ones.

## 6. Experimentations

### 6.1. Experimental protocol

In order to evaluate the interest of using the Implicit approach for learning parameters in Conditional Gaussian Bayesian Networks and to measure the quality estimation, we have carried out repetitive experiments in several contexts.
In these contexts, we are able to control several parameters such as the number of variables $n(n=10$, $30,50)$ and the size of generated datasets $N(N=$ $100,1.000,10.000)$. The maximal cardinality $K$ of our discrete variables is also controlled for Conditional Gaussian Bayesian Networks ( $K=2,3,5$ ). In such conditions, every dataset generation is iterated $10 \times 10$ times, with 10 randomly generated DAGs, and 10 random parameter values for each of these DAGs.
Our goal is to compare the performance of two estimators working without any prior definition, i.e. the implicit and maximum likelihood estimators.

Our various models and algorithms have been implemented in Matlab with BNT ${ }^{17}$ and BNT Struc-
ture Learning Package ${ }^{18}$.

### 6.2. Evaluation criteria

Accuracy evaluation of each method is estimated by the Kullback-Leibler (KL) divergence between the "original" distribution used for generating a given dataset and the "final" distribution obtained with parameter learning. For large numbers of variable configurations (greater than $10^{5}$ ), a Markov Chain Monte Carlo (MCMC) approximation is used with $10^{5}$ random configurations.
Comparison of both methods is illustrated by plotting absolute values of KL obtained by the Implicit approach versus maximum likelihood for the same datasets. The fact that one method is better than the other can be observed with respect to the first diagonal (upper triangle : ML is better, versus lower triangle : implicit approach is better). In order to determine whether the observed differences are statistically significant, we use the Wilcoxon paired signed rank test, with a significance level equal to 0.05 .

### 6.3. Results and interpretations

Figure 2 proposes the KL divergence obtained by Implicit approach versus the Maximum Likelihood one for the same datasets, for $n=10$. Similar results have been obtained for $n=30$ and 50.

Whatever the values of $K$ (maximum cardinality of variables) and $N$ (dataset size), the Implicit approach gives either similar or better results than the ML one. Both approaches coincide when $N$ is high ( $N=1000$ and 10000, results in magenta and black) but also with a small sample size $(N=100)$ but only when the maximum cardinality is low $(K=2)$.

When the maximum cardinality is high $(K=3$ and $K=5$ ) and the dataset size $N$ is low, the Implicit

![img-1.jpeg](img-1.jpeg)

Figure 2: Comparison of KL divergence obtained by Implicit approach versus the method of maximum likelihood for the same datasets (upper triangle : ML is better, versus lower triangle : Implicit approach is better) with respect to dataset size ( $N=100,1.000,10.000$, resp. blue, magenta and black points) and maximum cardinality $(K=2,3,5)$.
approach gives more interesting results. All these results are also confirmed by the Wilcoxon tests which are not detailed here.

## 7. Conclusion and perspectives

In this paper, we introduce the notion of Implicit approach for the estimation of parameters in Conditional Gaussian Bayesian Networks (CGBNs). This method of estimation is similar to the Bayesian one, but happens in a natural context without specifying any prior parameters. This characteristic can be interesting for CGBNs where priors are not easily understandable or interpretable for users. Bayesian estimation with priors far away from the true values can lead to poor results. the Implicit (prior free) estimators proposed here are then very attractive to avoid such situations and to replace advantageously the ML estimator when the sample size is low.

This Implicit approach can also be used to learn the network structure. Most structure learning approaches use a score function that measures the goodness of fit between the structure and the data and thus try to find a good model optimizing this score. Many scoring functions have been proposed and are based on different principles, such as entropy or Bayesian approaches. Within this framework, our future work will propose an extension of Implicit score function proposed in ${ }^{8}$ (and devoted
to discrete BNs) in which CGBN structure inference can be based without determining any prior.
