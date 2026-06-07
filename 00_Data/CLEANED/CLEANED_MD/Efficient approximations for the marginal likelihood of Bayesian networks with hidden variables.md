# Efficient Approximations for the Marginal Likelihood of Bayesian Networks with Hidden Variables 

DAVID MAXWELL CHICKERING<br>DAVID HECKERMAN<br>Mio crosoft.com<br>Microsoft Research, Redmond, WA 98052-6399

Editor: Padhraic Smyth


#### Abstract

We discuss Bayesian methods for model averaging and model selection among Bayesian-network models with hidden variables. In particular, we examine large-sample approximations for the marginal likelihood of naive-Bayes models in which the root node is hidden. Such models are useful for clustering or unsupervised learning. We consider a Laplace approximation and the less accurate but more computationally efficient approximation known as the Bayesian Information Criterion (BIC), which is equivalent to Rissanen's (1987) Minimum Description Length (MDL). Also, we consider approximations that ignore some off-diagonal elements of the observed information matrix and an approximation proposed by Cheeseman and Stutz (1995). We evaluate the accuracy of these approximations using a Monte-Carlo gold standard. In experiments with artificial and real examples, we find that (1) none of the approximations are accurate when used for model averaging, (2) all of the approximations, with the exception of BIC/MDL, are accurate for model selection, (3) among the accurate approximations, the Cheeseman-Stutz and Diagonal approximations are the most computationally efficient, (4) all of the approximations, with the exception of BIC/MDL, can be sensitive to the prior distribution over model parameters, and (5) the Cheeseman-Stutz approximation can be more accurate than the other approximations, including the Laplace approximation, in situations where the parameters in the maximum a posteriori configuration are near a boundary.


Keywords: Bayesian model averaging, model selection, multinomial mixtures, clustering, unsupervised learning, Laplace approximation

## 1. Introduction

There is growing interest in methods for learning graphical models from data. In this paper, we consider Bayesian methods such as those reviewed in Heckerman (1995) and Buntine (1996). A key step in the Bayesian approach to learning graphical models is the computation of the marginal likelihood of a data set given a model. This quantity is the ordinary likelihood (a function of the data and the model parameters) averaged over the parameters with respect to their prior distribution. Given a complete data set-that is, a data set in which each sample contains observations for every variable in the modelthe marginal likelihood can be computed in closed form under certain assumptions (e.g., Cooper \& Herskovits, 1992; Heckerman \& Geiger, 1995). In contrast, when observations are missing, including situations where some variables are hidden (i.e., never observed), the exact determination of the marginal likelihood is typically intractable (e.g., Cooper \& Herskovits, 1992). Consequently, approximate techniques for computing the marginal likelihood are used.

One class of approximations that has received a great deal of attention in the statistics community is based on Monte-Carlo techniques. In theory, these approximations are known to converge to an accurate result. In practice, however, the amount of computer time needed for convergence can be enormous. An alternative class of approximations is based on the large-sample properties of probability distributions. This class also can be accurate under certain assumptions, and are typically more efficient ${ }^{1}$ than Monte-Carlo techniques.
One large-sample approximation, known as a Laplace approximation, is widely used by Bayesian statisticians (Haughton, 1988; Kass, Tierney, \& Kadane, 1988; Kass \& Raftery, 1995). Although this approximation is efficient relative to Monte-Carlo methods, it has a computational complexity of $O\left(d^{2} N\right)$ or greater, where $d$ is the dimension of the model and $N$ is the sample size of the data. Consequently, the Laplace approximation can be a computational burden for large models.
In this paper, we examine other large-sample approximations that are more efficient than the Laplace approximation. These approximations include the Bayesian Information Criterion (BIC) (Schwarz, 1978), which is equivalent to Rissanen's (1987) Minimum-Description-Length (MDL) measure, diagonal and block diagonal approximations for the Hessian term in the Laplace approximation (Becker \& LeCun, 1988; Buntine \& Weigand, 1994), and an approximation suggested by Cheeseman and Stutz (1995).

Researchers have investigated the accuracy and efficiency of some of these approximations. For example, both theoretical and empirical studies have shown that the Laplace approximation is more accurate than is the BIC/MDL approximation (e.g., Draper, 1993; Raftery, 1994). Also, Becker and LeCun (1989) and MacKay (1992b) report successful and unsuccessful applications of the diagonal approximation, respectively, in the context of parameter learning for probabilistic neural-network models.
In this paper, we fill in some of the gaps that have been left by previous studies. We examine empirically the accuracy and efficiency of all approximations, comparing them to a Monte-Carlo gold standard. We do so using simple Bayesian networks for discrete variables that contain a single hidden variable. To our knowledge, this empirical study is the first that compares these approximations with a Monte-Carlo standard in the context of hiddenvariable Bayesian networks, and the first that examines the accuracy of the Cheeseman-Stutz approximation.
Our study is motivated by a need for accurate and efficient methods for exploratory data analysis. One exploration task is clustering. For example, suppose we have repeated observations for the discrete variables $\mathbf{X}=\left(X_{1}, \ldots, X_{n}\right)$. One possible model for clustering these observations is shown in Figure 1. In this naive-Bayes model, a discrete hidden variable $C$ renders the observations conditionally independent, and the joint distribution over $\mathbf{X}$ is given by a mixture of multinomial distributions

$$
p(\mathbf{x})=\sum_{j=1}^{r_{c}} p\left(C=c^{j}\right) \prod_{i=1}^{n} p\left(x_{i} \mid C=c^{j}\right)
$$

where $r_{c}$ is the number of states of the hidden variable $C$. Each state $c^{j}$ of $C$ corresponds to an underlying cluster or class in the data. Such models for clustering have been used by Cheeseman and Stutz (1995) in their system called AutoClass, and have been studied in

![img-0.jpeg](img-0.jpeg)

Figure 1. A Bayesian-network structure for clustering. The possible states of the hidden variable correspond to the underlying classes in the data.
depth by statisticians (e.g., Clogg, 1995). The approximations we examine can be used to determine the number of classes that is optimal according to the data (and prior information). Alternatively, we can use the approximations to provide weights for combining models with different numbers of classes.
Another important area of exploratory data analysis is causal discovery (Spirtes, Glymour, \& Scheines, 1993), which can also be cast in terms of learning graphical models. Heckerman (1995) describes how approximations for the marginal likelihood can be used for this task.

In this paper, we seek to find one or more marginal-likelihood approximations for exploratory data analysis that are accurate and yet scale to large problems. We examine these approximations for the class of clustering models depicted in Figure 1. In Section 2, we review the basic Bayesian approach for model averaging and model selection, emphasizing the importance of the marginal likelihood. In Section 3, we describe Monte-Carlo and large-sample approximations for computing marginal likelihood when there is missing data. In Section 4, we evaluate the accuracy and efficiency of the various approximations, using a Monte-Carlo gold standard for comparison. We examine the approximations using both synthetic and real-world data.

# 2. Bayesian methods for learning: The basics 

Commonly used Bayesian approaches for learning model structure include model averaging and model selection. These approaches date back to the work of Jeffreys (1939), and refinements can be found in (e.g.) Good (1965), Berger (1985), Gull and Skilling (1991), MacKay (1992a), Cooper and Herskovits (1992), Spiegelhalter, Dawid, Lauritzen, and Cowell (1993), Buntine (1994), Kass and Raftery (1995), and Heckerman, Geiger, and Chickering (1995). In this section, we review these methods and how they apply to learning with Bayesian networks given complete data.
First, we need some notation. We denote a variable by an upper-case letter (e.g., $X, Y, X_{i}, \Theta$ ), and the state or value of a corresponding variable by that same letter in lower case (e.g., $x, y, x_{i}, \theta$ ). We denote a set of variables by a bold-face capitalized letter

or letters (e.g., $\mathbf{X}, \mathbf{Y}, \mathbf{P a}_{i}$ ). We use a corresponding bold-face lower-case letter or letters (e.g., $\mathbf{x}, \mathbf{y}, \mathbf{p a}_{i}$ ) to denote an assignment of state or value to each variable in a given set. We say that variable set $\mathbf{X}$ is in configuration $\mathbf{x}$. We use $p(\mathbf{X}=\mathbf{x} \mid \mathbf{Y}=\mathbf{y})$ (or $p(\mathbf{x} \mid \mathbf{y})$ as a shorthand) to denote the probability or probability density that $\mathbf{X}=\mathbf{x}$ given $\mathbf{Y}=\mathbf{y}$. We also use $p(\mathbf{x} \mid \mathbf{y})$ to denote the probability distribution (both mass functions and density functions) for $\mathbf{X}$ given $\mathbf{Y}=\mathbf{y}$. Whether $p(\mathbf{x} \mid \mathbf{y})$ refers to a probability, a probability density, or a probability distribution should be clear from context.

Now, suppose our problem domain consists of variables $\mathbf{X}=\left(X_{1}, \ldots, X_{n}\right)$. In addition, suppose that we have some data $D=\left(\mathbf{x}_{1}, \ldots, \mathbf{x}_{N}\right)$, which is a random sample from some unknown probability distribution for $\mathbf{X}$. In this section, we assume that each case $\mathbf{x}$ in $D$ consists of an observation of all the variables in $\mathbf{X}$. We assume that the unknown probability distribution can be encoded by some statistical model with structure $\mathbf{m}$ and parameters $\boldsymbol{\theta}_{m}$. We are uncertain about the structure and parameters of the model, andusing the Bayesian approach-we encode this uncertainty using probability. In particular, we define a discrete variable $\mathbf{M}$ whose states $\mathbf{m}$ correspond to the possible true models, and encode our uncertainty about $\mathbf{M}$ with the probability distribution $p(\mathbf{m})$. In addition, for each model structure $\mathbf{m}$, we define a continuous vector-valued variable $\Theta_{m}$, whose configurations $\boldsymbol{\theta}_{m}$ correspond to the possible true parameters. We encode our uncertainty about $\Theta_{m}$ using the probability density function $p\left(\boldsymbol{\theta}_{m} \mid \mathbf{m}\right)$.

Given random sample $D$, we compute the posterior distributions for each $\mathbf{m}$ and $\boldsymbol{\theta}_{m}$ using Bayes' rule:

$$
\begin{aligned}
& p(\mathbf{m} \mid D)=\frac{p(\mathbf{m}) p(D \mid \mathbf{m})}{\sum_{m^{\prime}} p\left(\mathbf{m}^{\prime}\right) p\left(D \mid \mathbf{m}^{\prime}\right)} \\
& p\left(\boldsymbol{\theta}_{m} \mid D, \mathbf{m}\right)=\frac{p\left(\boldsymbol{\theta}_{m} \mid \mathbf{m}\right) p\left(D \mid \boldsymbol{\theta}_{m}, \mathbf{m}\right)}{p(D \mid \mathbf{m})}
\end{aligned}
$$

where

$$
p(D \mid \mathbf{m})=\int p\left(D \mid \boldsymbol{\theta}_{m}, \mathbf{m}\right) p\left(\boldsymbol{\theta}_{m} \mid \mathbf{m}\right) d \boldsymbol{\theta}_{m}
$$

is the marginal likelihood. Given some hypothesis of interest, $h$, we determine the probability that $h$ is true given data $D$ by averaging over all possible models and their parameters according to the rules of probability:

$$
\begin{aligned}
& p(h \mid D)=\sum_{m} p(\mathbf{m} \mid D) p(h \mid D, \mathbf{m}) \\
& p(h \mid D, \mathbf{m})=\int p\left(h \mid \boldsymbol{\theta}_{m}, \mathbf{m}\right) p\left(\boldsymbol{\theta}_{m} \mid D, \mathbf{m}\right) d \boldsymbol{\theta}_{m}
\end{aligned}
$$

For example, $h$ may be the event that the next observation is $\mathbf{x}_{N+1}$. In this situation, we obtain

$$
p\left(\mathbf{x}_{N+1} \mid D\right)=\sum_{m} p(\mathbf{m} \mid D) \int p\left(\mathbf{x}_{N+1} \mid \boldsymbol{\theta}_{m}, \mathbf{m}\right) p\left(\boldsymbol{\theta}_{m} \mid D, \mathbf{m}\right) d \boldsymbol{\theta}_{m}
$$

where $p\left(\mathbf{x}_{N+1} \mid \boldsymbol{\theta}_{m}, \mathbf{m}\right)$ is the likelihood for the model. This approach is often referred to as Bayesian model averaging. Note that no single model structure is learned. Instead, all possible models are weighted by their posterior probability.
Model averaging is not always appropriate for an analysis. For example, only one or a few models may be desired for domain understanding or for fast prediction. In these situations, we select one or a few "good" model structures from among all possible models, and use them as if they were exhaustive. This procedure is known as model selection when one model is chosen and as selective model averaging when more than one model is chosen. Of course, model selection and selective model averaging are also useful when it is impractical to average over all possible model structures.
Whether a model is "good" will depend on the particular application. For example, a good model for understanding the causal relationships in a domain will not necessarily be a good model for a classification or regression task. Also, if a model is to be used for decision making, its quality will likely depend on the alternatives available and the preferences of the decision maker. These issues are discussed in more detail by (e.g.) Spiegelhalter et al. (1993) and Heckerman (1995). Nonetheless, the relative posterior probability of a model structure, $p(D, \mathbf{m})=p(\mathbf{m}) p(D \mid \mathbf{m})$, is often used as a general-purpose criterion for selective model averaging and model selection. ${ }^{2}$ Consequently, the marginal likelihood is important for both model averaging and model selection.
Now let us assume that our statistical model is a Bayesian network. A Bayesian network for $\mathbf{X}$ consists of a directed-acylic-graph structure $\mathbf{m}$ and a set of local distribution functions $p\left(x_{i} \mid \mathbf{p a}_{i}, \boldsymbol{\theta}_{m}, \mathbf{m}\right)$, where $\mathbf{P a}_{i}$ is the set of variables that corresponds to the parents of $X_{i}$ in the graph. The structure $\mathbf{m}$ encodes the independence assumptions

$$
p\left(\mathbf{x} \mid \boldsymbol{\theta}_{m}, \mathbf{m}\right)=\prod_{i=1}^{n} p\left(x_{i} \mid \mathbf{p a}_{i}, \boldsymbol{\theta}_{m}, \mathbf{m}\right)
$$

Under certain assumptions, the computations needed for Bayesian model averaging, selective model averaging, or model selection can be done efficiently and in closed form. Many researchers who have addressed Bayesian-network learning have adopted at least some of these assumptions (e.g., Cooper \& Herskovits, 1992; Spiegelhalter et al., 1993; Buntine, 1994; Heckerman et al., 1995). The assumptions include:

1. Every variable is discrete, having a finite number of states. We use $x_{i}^{k}$ and $\mathbf{p a}_{i}^{j}$ to denote the $k$ th possible state of $X_{i}$ and the $j$ th possible configuration of $\mathbf{P a}_{i}$, respectively. Also, we use $r_{i}$ and $q_{i}$ to denote the number of possible states of $X_{i}$ and the number of possible configurations of $\mathbf{P a}_{i}$, respectively.
2. Each local distribution function $p\left(x_{i} \mid \mathbf{p a}_{i}, \boldsymbol{\theta}_{m}, \mathbf{m}\right)$ consists of a set of multinomial distributions, one multinomial distribution for each $i$ and $j$. That is,

$$
p\left(x_{i}^{k} \mid \mathbf{p a}_{i}^{j}, \boldsymbol{\theta}_{m}, \mathbf{m}\right)=\theta_{i j k}
$$

where the $\theta_{i j k}$ are parameters satisfying $\theta_{i j k}>0$ for all $i, j$, and $k$, and $\sum_{k=1}^{r_{i}} \theta_{i j k}=1$ for all $i$ and $j$. For convenience, we introduce the set of nonredundant parameters $\boldsymbol{\theta}_{i j}=\left(\theta_{i j 2}, \ldots, \theta_{i j r_{i}}\right)$ for all $i$ and $j$.
3. The parameter sets $\boldsymbol{\theta}_{i j}$ are mutually independent, so that

$$
p\left(\boldsymbol{\theta}_{m} \mid \mathbf{m}\right)=\prod_{i=1}^{n} \prod_{j=1}^{q_{i}} p\left(\boldsymbol{\theta}_{i j} \mid \mathbf{m}\right)
$$

4. Each parameter set $\boldsymbol{\theta}_{i j}$ has a Dirichlet distribution, giving

$$
p\left(\boldsymbol{\theta}_{i j} \mid \mathbf{m}\right)=\operatorname{Dir}\left(\boldsymbol{\theta}_{i j} \mid \alpha_{i j 1}, \ldots, \alpha_{i j r_{i}}\right) \propto \prod_{k=1}^{r_{i}} \theta_{i j k}^{\alpha_{i j k}-1}
$$

where hyperparameters $\alpha_{i j k}>0$ for every $i, j$, and $k$.
5. The data set $D$ is complete-that is, every variable is observed in every case of $D$.

Under these assumptions, the parameters remain independent given a random sample $D$ that contains no missing observations, so that

$$
p\left(\boldsymbol{\theta}_{m} \mid D, \mathbf{m}\right)=\prod_{i=1}^{n} \prod_{j=1}^{q_{i}} p\left(\boldsymbol{\theta}_{i j} \mid D, \mathbf{m}\right)
$$

and the posterior distribution of each $\boldsymbol{\theta}_{i j}$ will have the Dirichlet distribution

$$
p\left(\boldsymbol{\theta}_{i j} \mid D, \mathbf{m}\right)=\operatorname{Dir}\left(\boldsymbol{\theta}_{i j} \mid \alpha_{i j 1}+N_{i j 1}, \ldots, \alpha_{i j r_{i}}+N_{i j r_{i}}\right)
$$

where $N_{i j k}$ is the number of cases in $D$ in which $X_{i}=x_{i}^{k}$ and $\mathbf{P a}_{i}=\mathbf{p a}_{i}^{j}$. Note that the collection of counts $N_{i j k}$ are sufficient statistics of the data for the model $\mathbf{m}$. In addition, we obtain the marginal likelihood

$$
p(D \mid \mathbf{m})=\prod_{i=1}^{n} \prod_{j=1}^{q_{i}} \frac{\Gamma\left(\alpha_{i j}\right)}{\Gamma\left(\alpha_{i j}+N_{i j}\right)} \cdot \prod_{k=1}^{r_{i}} \frac{\Gamma\left(\alpha_{i j k}+N_{i j k}\right)}{\Gamma\left(\alpha_{i j k}\right)}
$$

where $\alpha_{i j}=\sum_{k=1}^{r_{i}} \alpha_{i j k}$ and $N_{i j}=\sum_{k=1}^{r_{i}} N_{i j k}$. (See Cooper and Herskovits (1992) for a derivation.)
These assumptions are restrictive; and there has been a great deal of recent work building on general results from Bayesian statistics to relax these assumptions. For example, Geiger and Heckerman (1994) discuss the case where variables are continuous and each local distribution function corresponds to ordinary linear regression; Buntine (1994) discusses the more general case where local distribution functions come from the exponential family; MacKay (1992a) and Gilks, Richardson, and Spiegelhalter (1996) relax the assumption of parameter independence using hierarchical models; and Buntine (1994), Azevedo-Filho and Shachter (1995), Heckerman (1995), and Gilks et al. (1996) have addressed the case where data are missing.

# 3. Methods for missing data 

When observations for some variables are missing in the data, the parameters for a given model become dependent, and known closed-form methods cannot be used to determine marginal likelihood. Approximations for computing marginal likelihood include MonteCarlo approaches such as Gibbs sampling and importance sampling (Neal, 1993; Chib, 1995; Raftery, 1996) and large-sample approximations (Kass et al., 1988; Kass \& Raftery, 1995). As mentioned in the introduction, Monte-Carlo methods are accurate but typically inefficient, whereas large-sample methods are more efficient but known to be accurate only for large data sets. In this paper, we examine the accuracy and efficiency of large-sample methods using a Monte-Carlo approximation as a standard for comparison. In this section, we describe the approximations that we use.
We note that, when treating missing data, an important consideration is whether or not we can ignore the process by which observations are missed. For example, a missing datum in a drug study cannot be ignored if there is the possibility that-as a result of taking the drug-the patient became too ill to be observed. In contrast, if data are missing due to clerical errors, it is often reasonable to ignore this fact. When the process by which observations are missed are not ignorable, the model (or models) should be enhanced to represent these processes. One simple approach for enhancing a model for $\left(X_{1}, \ldots, X_{n}\right)$ is to add variables $\left(I_{1}, \ldots, I_{n}\right)$, where $I_{i}$ is a binary variable that indicates whether or not the observation of variable $X_{i}$ in the original model is missing. Rubin (1976) discusses the concept of ignorability and methods for treating non-ignorable data collection processes. The methods for handling missing data that we discuss here assume that the models under consideration have appropriately represented the data collection process.

### 3.1. The Laplace approximation and related methods

In this subsection and the two that follow, we consider large-sample approximations. The accuracy of some of these approximations depend on the coordinate system used to represent the parameters. In the previous section, where we examined Bayesian networks for discrete variables, we introduced the coordinate system $\Theta_{m}$ corresponding to the parameters $\boldsymbol{\theta}_{m}$. An alternative coordinate system, which we denote by $\Phi_{m}$, corresponds to the parameters

$$
\phi_{i j k}=\log \frac{\theta_{i j k}}{\theta_{i j 1}}
$$

for $i=1, \ldots, n, j=1, \ldots, q_{i}, k=2, \ldots, r_{i}$. This set of parameters (for fixed $i$ and $j$ ) is known as the natural parameter set for the multinomial distribution (e.g., Bernardo \& Smith, 1994, pp. 199-202). Although $\Theta_{m}$ and $\Phi_{m}$ are equivalent in that there is a one-to-one mapping between them, MacKay (1996) has shown that the use of the natural parameters typically leads to a more accurate approximation of the kind that we consider. Consequently, we use this coordinate system for our approximations. We also use $\Phi_{m}$ for most of our discussions, although sometimes it will be more convenient to express our procedures in terms of $\Theta_{m}$.

The basic idea behind large-sample approximations is that, as the sample size $N$ increases, $p\left(\boldsymbol{\phi}_{m} \mid D, \mathbf{m}\right) \propto p\left(D \mid \boldsymbol{\phi}_{m}, \mathbf{m}\right) \cdot p\left(\boldsymbol{\phi}_{m} \mid \mathbf{m}\right)$ can be approximated as a multivariate-Gaussian distribution. In particular, let

$$
g\left(\boldsymbol{\phi}_{m}\right) \equiv \log \left(p\left(D \mid \boldsymbol{\phi}_{m}, \mathbf{m}\right) \cdot p\left(\boldsymbol{\phi}_{m} \mid \mathbf{m}\right)\right)
$$

Also, define $\tilde{\boldsymbol{\phi}}_{m}$ to be the configuration of $\boldsymbol{\phi}_{m}$ that maximizes $g\left(\boldsymbol{\phi}_{m}\right)$. This configuration also maximizes $p\left(\boldsymbol{\phi}_{m} \mid D, \mathbf{m}\right)$, and is known as the maximum a posteriori (MAP) configuration of $\boldsymbol{\phi}_{m}$ given $D$. Using a second degree Taylor polynomial of $g\left(\boldsymbol{\phi}_{m}\right)$ about $\tilde{\boldsymbol{\phi}}_{m}$ to approximate $g\left(\boldsymbol{\phi}_{m}\right)$, we obtain

$$
g\left(\boldsymbol{\phi}_{m}\right) \approx g\left(\tilde{\boldsymbol{\phi}}_{m}\right)-\frac{1}{2}\left(\boldsymbol{\phi}_{m}-\tilde{\boldsymbol{\phi}}_{m}\right) A\left(\boldsymbol{\phi}_{m}-\tilde{\boldsymbol{\phi}}_{m}\right)^{t}
$$

where $\left(\boldsymbol{\phi}_{m}-\tilde{\boldsymbol{\phi}}_{m}\right)^{t}$ is the transpose of row vector $\left(\boldsymbol{\phi}_{m}-\tilde{\boldsymbol{\phi}}_{m}\right)$, and $A$ is the negative Hessian of $g\left(\boldsymbol{\phi}_{m}\right)$ evaluated at $\tilde{\boldsymbol{\phi}}_{m}$. Raising $g\left(\boldsymbol{\phi}_{m}\right)$ to the power of $e$ and using Equation 12, we obtain

$$
\begin{aligned}
& p\left(D \mid \boldsymbol{\phi}_{m}, \mathbf{m}\right) p\left(\boldsymbol{\phi}_{m} \mid \mathbf{m}\right) \\
& \quad \approx p\left(D \mid \tilde{\boldsymbol{\phi}}_{m}, \mathbf{m}\right) p\left(\tilde{\boldsymbol{\phi}}_{m} \mid \mathbf{m}\right) \exp \left\{-\frac{1}{2}\left(\boldsymbol{\phi}_{m}-\tilde{\boldsymbol{\phi}}_{m}\right) A\left(\boldsymbol{\phi}_{m}-\tilde{\boldsymbol{\phi}}_{m}\right)^{t}\right\}
\end{aligned}
$$

Hence, the approximation for $p\left(\boldsymbol{\phi}_{m} \mid D, \mathbf{m}\right) \propto p\left(D \mid \boldsymbol{\phi}_{m}, \mathbf{m}\right) p\left(\boldsymbol{\phi}_{m} \mid \mathbf{m}\right)$ is Gaussian. Integrating both sides of Equation 14 over $\boldsymbol{\phi}_{m}$ and taking the logarithm, we obtain the approximation

$$
\log p(D \mid \mathbf{m}) \approx \log p\left(D \mid \tilde{\boldsymbol{\phi}}_{m}, \mathbf{m}\right)+\log p\left(\tilde{\boldsymbol{\phi}}_{m} \mid \mathbf{m}\right)+\frac{d}{2} \log (2 \pi)-\frac{1}{2} \log |A|
$$

where $d$ is the dimension of $\mathbf{m}$-that is, the number of parameters in $\boldsymbol{\phi}_{m}$. For Bayesian networks satisfying the assumptions described in the previous section, $d=\prod_{i=1}^{n} q_{i}\left(r_{i}-1\right)$. This approximation technique for integration is known as Laplace's method, and we refer to Equation 15 as the Laplace approximation. Kass et al. (1988) have shown that, under certain conditions, the relative error of this approximation, given by

$$
\frac{[p(D \mid \mathbf{m})]_{\text {Laplace }}-[p(D \mid \mathbf{m})]_{\text {correct }}}{[p(D \mid \mathbf{m})]_{\text {correct }}}
$$

is $O_{p}(1 / N)$, where $N$ is the number of cases in $D$. Thus, the Laplace approximation can be extremely accurate.

Several of the conditions used by Kass et al. to characterize the accuracy of the Laplace approximation are worth noting, because they are violated in some of our experiments. One condition is that the MAP configuration $\tilde{\boldsymbol{\phi}}_{m}$ does not lie on the boundary of $\boldsymbol{\phi}_{m}$. In Section 4.5, we examine how violations of this condition affect the accuracy of the Laplace (and other) approximations.

Another condition used by Kass et al. is that, given $D$, there is a unique MAP configuration $\tilde{\boldsymbol{\phi}}_{m}$. When this condition holds, the parameters of the model are said to be identified.

There are two common situations in which the parameters of a Bayesian network with hidden variables are not identified. In one case, known as aliasing, the state labels of a hidden variable can be interchanged without affecting $p\left(\boldsymbol{\phi}_{m} \mid D, \mathbf{m}\right)$. In Section 3.5, we discuss methods for recovering an accurate Laplace approximation when aliasing occurs. In the other case, the likelihoods $p\left(\mathbf{x} \mid \boldsymbol{\phi}_{m}, \mathbf{m}\right)$ for all $\mathbf{x}$ can be encoded by a smaller set of parameters than $\boldsymbol{\phi}_{m}$. That is, the dimension of the model is less than the number of parameters in $\boldsymbol{\phi}_{m}$ (e.g., Geiger, Heckerman, \& Meek, 1996). Consequently, the model will have an (uncountably) infinite number of MAP configurations for $\boldsymbol{\phi}_{m}$. We know of no formal construction of a Laplace approximation that is accurate in this circumstance. Nonetheless, for our experiments, the issue of reduced dimensionality is likely to be mute. In particular, Geiger et al. (1996) provide evidence that the models we examine in this paper do not have redundant parameters.
To compute the Laplace approximation, we must determine $\tilde{\boldsymbol{\phi}}_{m}$ and the Hessian of $-g\left(\boldsymbol{\phi}_{m}\right)$ evaluated at $\tilde{\boldsymbol{\phi}}_{m}$. We discuss methods for finding $\tilde{\boldsymbol{\phi}}_{m}$ in Section 3.2. Meng and Rubin (1991) describe a numerical technique for computing the second derivatives in the Hessian. Raftery (1995) shows how to approximate the Hessian using likelihood-ratio tests that are available in many statistical packages. Thiesson (1997) demonstrates that, for multinomial distributions, the second derivatives can be obtained using Bayesian-network inference. We use Thiesson's method in our experiments.
Although Laplace's approximation is efficient relative to Monte-Carlo approaches, the computation of $|A|$ is nevertheless intensive for large-dimension models. One simplification is to approximate the Hessian $A$ with a block-diagonal matrix, where the entries corresponding to $-\partial^{2} g\left(\boldsymbol{\phi}_{m}\right) / \partial \phi_{i j k} \partial \phi_{a b c}$ are set to zero, for $i \neq a$. A further simplification is to approximate $A$ using only its diagonal elements. These Block and Diagonal approximations have been considered by Buntine (1994) and Becker and LeCun (1989), respectively, in feed-forward neural networks. Roughly speaking, in using these approximations, we are forcing independence among parameters that may not in fact be independent.
We obtain another efficient (but less accurate) approximation by retaining only those terms in Equation 15 that increase with $N: \log p\left(D \mid \hat{\boldsymbol{\phi}}_{m}, \mathbf{m}\right)$, which increases linearly with $N$, and $\log |A|$, which increases as $d \log N$. Also, for large $N, \hat{\boldsymbol{\phi}}_{m}$ can be approximated by $\hat{\boldsymbol{\phi}}_{m}$, the configuration of $\boldsymbol{\phi}_{m}$ that maximizes $p\left(D \mid \boldsymbol{\phi}_{m}, \mathbf{m}\right)$, known as the maximum likelihood (ML) configuration of $\boldsymbol{\phi}_{m}$. Thus, we obtain

$$
\log p(D \mid \mathbf{m}) \approx \log p\left(D \mid \hat{\boldsymbol{\phi}}_{m}, \mathbf{m}\right)-\frac{d}{2} \log N
$$

This approximation is called the Bayesian information criterion (BIC). Schwarz (1978) has shown that the relative error of this approximation is $O_{p}(1)$ for a limited class of models. Haughton (1988) has extended this result to curved exponential models. Kass and Wasserman (1995) and Raftery (1995) have shown that, for particular priors, the BIC has a relative error of $O_{p}\left(N^{-1 / 2}\right)$.
The BIC approximation is interesting in several respects. First, it depends neither on the prior ${ }^{3}$ nor the coordinate system of the parameters. Second, the approximation is quite intuitive. Namely, it contains a term measuring how well the parameterized model predicts the data $\left(\log p\left(D \mid \hat{\boldsymbol{\phi}}_{m}, \mathbf{m}\right)\right)$ and a term that penalizes the complexity of the model

$(d / 2 \log N)$. Third, the BIC approximation is exactly minus the Minimum Description Length (MDL) criterion described by Rissanen (1987).

# 3.2. Computation of MAP and ML configurations 

To compute any of the approximations that we have described, we need to determine either the maximum a posteriori or maximum likelihood configuration for $\boldsymbol{\phi}_{m}$.
One class of techniques for finding a MAP or ML configuration is gradient-based optimization. For example, we can use gradient ascent, where we follow the derivatives of $p\left(\boldsymbol{\phi}_{m} \mid D, \mathbf{m}\right)$ or $p(D \mid \boldsymbol{\phi}_{m}, \mathbf{m})$ to a local maximum. Russell, Binder, Koller, and Kanazawa (1995) and Thiesson (1997) show how to compute the derivatives of the likelihood for a Bayesian network with multinomial distributions. Buntine (1994) discusses the more general case where the local distribution functions come from the exponential family.
Another technique for finding a local MAP or ML configuration is the expectationmaximization (EM) algorithm (Dempster, Laird, \& Rubin, 1977). To find a local MAP or ML configuration, we begin by assigning a configuration to $\boldsymbol{\phi}_{m}$ somehow (e.g., at random). Next, we compute the expected sufficient statistics for a complete data set, where expectation is taken with respect to the joint distribution for $\mathbf{X}$ conditioned on the assigned configuration of $\boldsymbol{\phi}_{m}$ and the known data $D$. For Bayesian networks with discrete variables, we compute

$$
\mathrm{E}_{p\left(\mathbf{x} \mid D, \phi_{m}, \mathbf{m}\right)}\left(N_{i j k}\right)=\sum_{l=1}^{N} p\left(x_{i}^{k}, \mathbf{p a}_{i}^{l} \mid \mathbf{x}_{l}, \boldsymbol{\phi}_{m}, \mathbf{m}\right)
$$

where $\mathbf{x}_{l}$ is the possibly incomplete $l$ th case in $D$. When $X_{i}$ and all the variables in $\mathbf{P a}_{i}$ are observed in case $\mathbf{x}_{l}$, the corresponding term for this case requires a trivial computation: it is either zero or one. Otherwise, we can use any Bayesian-network inference algorithm (e.g., Jensen, Lauritzen, \& Olesen, 1990) to evaluate the term. This computation is called the expectation step of the EM algorithm.
Next, we use the expected sufficient statistics as if they were actual sufficient statistics from a complete random sample $D_{c}$. If we are doing an ML calculation, then we determine the configuration of $\boldsymbol{\phi}_{m}$ that maximizes $p\left(D_{c} \mid \boldsymbol{\phi}_{m}, \mathbf{m}\right)$. This configuration is given by $\phi_{i j k}=\log \left(\theta_{i j k} / \theta_{1 j k}\right)$, where

$$
\theta_{i j k}=\frac{\mathrm{E}_{p\left(\mathbf{x} \mid D, \phi_{m}, \mathbf{m}\right)}\left(N_{i j k}\right)}{\sum_{k=1}^{r_{i}} \mathrm{E}_{p\left(\mathbf{x} \mid D, \phi_{m}, \mathbf{m}\right)}\left(N_{i j k}\right)}
$$

If we are doing a MAP calculation, then we determine the configuration of $\boldsymbol{\phi}_{m}$ that maximizes the posterior density of the parameters. When working with the coordinate system $\Phi_{m}$, this configuration is given by $\phi_{i j k}=\log \left(\theta_{i j k} / \theta_{1 j k}\right)$, where

$$
\theta_{i j k}=\frac{\alpha_{i j k}+\mathrm{E}_{p\left(\mathbf{x} \mid D, \phi_{m}, \mathbf{m}\right)}\left(N_{i j k}\right)}{\sum_{k=1}^{r_{i}}\left(\alpha_{i j k}+\mathrm{E}_{p\left(\mathbf{x} \mid D, \phi_{m}, \mathbf{m}\right)}\left(N_{i j k}\right)\right)}
$$

This assignment is called the maximization step of the EM algorithm. Dempster et al. (1977) showed that iteration of the expectation and maximization steps will converge to a

local maximum. The EM algorithm is typically applied when sufficient statistics exist (i.e., when local distribution functions are in the exponential family), although generalizations of the EM algorithm have been used for more complicated local distributions (e.g., Saul, Jaakkola, \& Jordan, 1996).

The models that we consider often have more than one local maximum. Consequently, these techniques will not necessarily find the global MAP or ML configuration. One often-used partial solution to this problem is to start from many (usually random) initial configurations of $\phi_{m}$. We use a variant of this technique in our experiments.

# 3.3. The Cheeseman-Stutz approximation 

Another approximation for the marginal likelihood is based on the fact that $p(D \mid \mathbf{m})$ can be computed efficiently for complete data. Consider the equality

$$
p(D \mid \mathbf{m})=p\left(D^{\prime} \mid \mathbf{m}\right) \frac{\int p\left(D, \phi_{m} \mid \mathbf{m}\right) d \phi_{m}}{p\left(D^{\prime}, \phi_{m} \mid \mathbf{m}\right) d \phi_{m}}
$$

where $D^{\prime}$ is any completion of the data set $D$. Because $D^{\prime}$ is a complete data set, we can compute $p\left(D^{\prime} \mid \mathbf{m}\right)$ using Equation 11. Now, suppose we apply Laplace approximations to the numerator and denominator of the second term. Roughly speaking, the resulting approximation for $p(D)$ will be best if the quantities $p\left(D, \phi_{m} \mid \mathbf{m}\right)$ and $p\left(D^{\prime}, \phi_{m} \mid \mathbf{m}\right)$-regarded as functions of $\phi_{m}$-are similar in shape, so that errors in the two Laplace approximations tend to cancel. The two functions cannot be similar in an absolute sense, because $D^{\prime}$ contains more information than does $D$, and hence $p\left(D^{\prime}, \phi_{m} \mid \mathbf{m}\right)$ will be more peaked than $p\left(D, \phi_{m} \mid \mathbf{m}\right)$. Nonetheless, we can make the two functions more similar by completing $D^{\prime}$ so that they peak for the same configuration of $\phi_{m}$. That is, we want $\tilde{\phi}_{m}^{\prime}$, the MAP configuration of $\phi_{m}$ given $D^{\prime}$, to be equal to $\tilde{\phi}_{m}$. One way to obtain this equality is to complete $D^{\prime}$ so that its sufficient statistics match the expected sufficient statistics given $D$ and $\mathbf{m}$. In the case of Bayesian networks with discrete variables and multinomial distributions, this completion is given by

$$
N_{i j k}^{\prime}=\mathrm{E}_{p\left(\mathbf{x} \mid D, \phi_{m}, \mathbf{m}\right)}\left(N_{i j k}\right)
$$

for all $i, j$, and $k$, where the $N_{i j k}^{\prime}$ are the sufficient statistics for $D^{\prime}$. This choice for $D^{\prime}$ is also desirable from a computational standpoint, because-when using the EM algorithm to find $\tilde{\phi}_{m}$-the sufficient statistics $N_{i j k}^{\prime}$ are computed in the last expectation step.

Applying the Laplace approximation Equation 15 to the numerator and denominator of Equation 18, and using the fact that $\tilde{\phi}_{m}^{\prime}=\tilde{\phi}_{m}$, we obtain

$$
\log \mathrm{p}(\mathrm{D} \mid \mathbf{m}) \approx \log \mathrm{p}\left(\mathrm{D}^{\prime} \mid \mathbf{m}\right)-\log \mathrm{p}\left(\mathrm{D}^{\prime} \mid \tilde{\phi}_{m}, \mathbf{m}\right)+\frac{1}{2} \log \left|\mathrm{~A}^{\prime}\right|+\log \mathrm{p}\left(\mathrm{D} \mid \tilde{\phi}_{m}, \mathbf{m}\right)-\frac{1}{2} \log |\mathrm{~A}|
$$

where $A^{\prime}$ is the negative Hessian of $\log p\left(D^{\prime}, \phi_{m} \mid \mathbf{m}\right)$ evaluated at $\tilde{\phi}_{m}$. Because we derive this approximation using two Laplace approximations, Equation 20 must have a relative

error that is no worse than $O_{p}(1 / N)$. Nonetheless, a careful derivation may show that it is more accurate.
A more efficient approximation is obtained by applying the BIC/MDL approximation to the numerator and denominator of Equation 18. In this case, we have

$$
\log \mathrm{p}(\mathrm{D} \mid \mathbf{m}) \approx \log \mathrm{p}\left(\mathrm{D}^{\prime} \mid \mathbf{m}\right)-\log \mathrm{p}\left(\mathrm{D}^{\prime} \mid \hat{\phi}_{\mathrm{m}}, \mathbf{m}\right)+\frac{\mathrm{d}^{\prime}}{2} \log \mathrm{~N}+\log \mathrm{p}\left(\mathrm{D} \mid \hat{\phi}_{\mathrm{m}}, \mathbf{m}\right)-\frac{\mathrm{d}}{2} \log \mathrm{~N}
$$

where we have used the MAP rather than ML configuration for $\boldsymbol{\phi}_{m}$, and we have allowed for the possibility that $d^{\prime}$, the dimension of $\mathbf{m}$ for complete data, may be greater than the dimension of $\mathbf{m}$ for the actual data. Equation 21 (without the correction for dimension) was introduced by Cheeseman and Stutz (1995) for use as a model-selection criterion in AutoClass. We shall refer to Equation 21 as the Cheeseman-Stutz approximation. We note that this approximation can be easily extended to any statistical model that has sufficient statistics. For example, the Cheeseman-Stutz approximation can be applied to any Bayesian network with local distribution functions from the exponential family. Our heuristic derivation of the Cheeseman-Stutz approximation does not tell us whether it is better to use the MAP or ML configuration in the approximation. Thus, we examine both alternatives in our experiments.

# 3.4. Monte-Carlo methods 

We now discuss Monte-Carlo methods, concentrating on the method we use to evaluate the accuracy of the large-sample approximations.
A common Monte-Carlo method, introduced by Geman and Geman (1984), is known as Gibbs sampling. Given variables $\mathbf{X}=\left(X_{1}, \ldots, X_{n}\right)$ with some joint distribution $p(\mathbf{x})$, we can use a Gibbs sampler to approximate the expectation of a function $f(\mathbf{x})$ with respect to $p(\mathbf{x})$ as follows. First, we choose an initial state for each of the variables in $\mathbf{X}$, say at random. Next, we unassign the current state of $X_{1}$ and compute its probability distribution given the configuration of the other $n-1$ variables. We repeat this procedure for each variable $X_{2}, \ldots, X_{n}$, thus creating a new sample of $\mathbf{x}$. We then iterate the previous steps, keeping track of the simple average of $f(\mathbf{x})$ over the samples we construct. After a (usually small) number of iterations-known as the "burn-in" phase-the possible configurations of $\mathbf{x}$ will be sampled with probability $p(\mathbf{x}) .{ }^{4}$ Consequently, the simple average of $f(\mathbf{x})$ over these samples will converge to $\mathrm{E}_{p(\mathbf{x})}(f(\mathbf{x}))$. Introductions to Gibbs sampling and other Monte-Carlo methods—including discussions of convergence—are given by Neal (1993) and by Madigan and York (1995).
The particular approach we use to compute the marginal likelihood is known as the Candidate method (Chib, 1995; Raftery, 1996). The approach is based on Bayes' theorem, which says that

$$
p(D \mid \mathbf{m})=\frac{p\left(D \mid \boldsymbol{\phi}_{m}^{*}, \mathbf{m}\right) p\left(\boldsymbol{\phi}_{m}^{*} \mid \mathbf{m}\right)}{p\left(\boldsymbol{\phi}_{m}^{*} \mid D, \mathbf{m}\right)}
$$

for any configuration $\boldsymbol{\phi}_{m}^{*}$. To compute $p(D \mid \mathbf{m})$, we choose some configuration $\boldsymbol{\phi}_{m}^{*}$, evaluate the numerator exactly, and approximate the denominator using a Gibbs sampler.

To approximate $p\left(\phi_{m}^{*} \mid D, \mathbf{m}\right)$, we first initialize the states of the unobserved variables in each case. As a result, we have a complete random sample $D_{c}$. Second, we choose some variable $X_{i l}$ (variable $X_{i}$ in case $l$ ) that is not observed in the original random sample $D$, and reassign its state according to the probability distribution

$$
p\left(x_{i l}^{\prime} \mid D_{c} \backslash x_{i l}, \mathbf{m}\right)=\frac{p\left(x_{i l}^{\prime}, D_{c} \backslash x_{i l} \mid \mathbf{m}\right)}{\sum_{x_{i l}^{\prime \prime}} p\left(x_{i l}^{\prime \prime}, D_{c} \backslash x_{i l} \mid \mathbf{m}\right)}
$$

where $D_{c} \backslash x_{i l}$ denotes the data set $D_{c}$ with observation $x_{i l}$ removed, and the sum in the denominator runs over all states of variable $X_{i l}$. Theterms in the numerator and denominator are marginal likelihoods for complete data, and thus can be computed using Equation 11. Third, we repeat this reassignment for all unobserved variables in $D$, producing a new complete random sample $D_{c}^{\prime}$. Fourth, we compute the posterior density $p\left(\phi_{m}^{*} \mid D_{c}^{\prime}, \mathbf{m}\right)$ using Equations 9 and 10 (adjusted for the coordinate system $\Phi_{m}$ ). Finally, we iterate the previous three steps, and use the simple average of $p\left(\phi_{m}^{*} \mid D_{c}^{\prime}, \mathbf{m}\right)$ as our approximation.

In principle, the Candidate method can be applied using any configuration $\phi_{m}^{*}$. Nonetheless, certain configurations lead to faster convergence of the Gibbs sampler. Chib (1995) and Raftery (1996) suggest that $\hat{\phi}_{m}$ be used. Nonetheless, in experiments with multinomialmixture models, we have found that the use of this configuration underestimates $p\left(\phi_{m}^{*} \mid D, \mathbf{m}\right)$. This error occurs because, when $\hat{\phi}_{m}$ is used, there are configurations of $D_{c}$ such that (1) $p\left(\phi_{m}^{*} \mid D_{c}, \mathbf{m}\right)$ is extremely large, and (2) the configuration $D_{c}$ is extremely unlikely to be visited. Consequently, when these configurations of $D_{c}$ are not visited in a particular run, the simple average of $p\left(\phi_{m}^{*} \mid D_{c}, \mathbf{m}\right)$ is substantially less than $p\left(\phi_{m}^{*} \mid D, \mathbf{m}\right)$.

We have experimented with an alternative method for choosing $\phi_{m}^{*}$. For a fixed number of samples after the burn-in phase, we keep track of the configurations of $D_{c}$. After these samples have been collected, we retain the configuration $D_{c}^{*}$ that occurred most frequently. We break ties by choosing the configuration with the largest value of $p\left(D_{c} \mid \mathbf{m}\right)$. Finally, we set $\phi_{m}^{*}$ to be the configuration that maximizes $p\left(\phi_{m} \mid D_{c}^{*}, \mathbf{m}\right)$. In experiments with multinomial-mixture models, such as those presented in Section 4.4, this choice of $\phi_{m}^{*}$ yields low-noise estimates of $p(D \mid \mathbf{m})$.

# 3.5. Hidden-variable models and aliasing 

Given a Bayesian network $\mathbf{m}$ for $\mathbf{X}$, suppose $X_{i} \in \mathbf{X}$ is never observed in data set $D$. Because $X_{i}$ is hidden, the likelihood $p\left(D \mid \phi_{m}, \mathbf{m}\right)$ will be invariant to arbitrary relabelings of the states of $X_{i}$. Thus, if the prior $p\left(\phi_{m} \mid \mathbf{m}\right)$ is invariant to such relabelings, so will be the posterior $p\left(\phi_{m} \mid D, \mathbf{m}\right)$. It follows that if $\hat{\phi}_{m}$ is a MAP configuration of $\phi_{m}$, then there will be additional MAP configurations corresponding to the relabelings of the states of $X_{i}$. We shall refer to each such configuration and its neighborhood as an alias. If each alias is distinct (i.e., nondegenerate), then there will be $r_{i}$ ! of them.

When there are multiple distinct aliases, the parameters of $\mathbf{m}$ are no longer identifiable. Nonetheless, assuming the aliases are well separated, we can apply the Laplace approximation locally around each of them, summing the contributions of each peak. Assuming one hidden variable and distinct aliases, this procedure amounts to multiplying the marginal

likelihood corresponding to one alias by $r_{i}$ !. This correction applies to the Block, Diagonal, BIC/MDL, and Cheeseman-Stutz approximations as well.
With sufficient computation, the Candidate approximation for $p(D \mid \mathbf{m})$ does not need to be corrected for aliases, because the Gibbs sampler will visit all assignments to the hidden variable(s). In our experiments, however, the Gibbs sampler tends to stay near one alias. We can compensate for this failure to move among aliases by multiplying the approximation for marginal likelihood by $r_{i}$ !, as we do for the large-sample approximations. We obtain a more accurate correction, however, by (in effect) running $r_{i}$ ! Gibbs samplers in parallel. In particular, for every completion $D_{c}$ that we actually visit, we compute $p\left(\boldsymbol{\phi}_{m}^{*} \mid D_{c}^{\prime}, \mathbf{m}\right)$ for each equivalent assignment $D_{c}^{\prime}$, and average the results. To compute $p\left(\boldsymbol{\phi}_{m}^{*} \mid D, \mathbf{m}\right)$, we then average these averages. ${ }^{5}$ This procedure yields an accurate correction factor even when the Gibbs sampler moves among aliases and when there are degenerate aliases. The procedure is expensive for large $r_{i}$, but was not prohibitive for our experiments.

# 3.6. Computational complexity 

The accuracy of these approximations should be balanced against their computation costs. These costs will depend on the topology of the Bayesian network under consideration. Here, we consider costs for an arbitrary Bayesian network with discrete variables and a naiveBayes discrete-variable clustering model of the form shown in Figure 1 (a multinomialmixture model). In both cases, we assume that the EM algorithm is used to find a MAP or ML configuration of $\boldsymbol{\phi}_{m}$.
For an arbitrary Bayesian network, the evaluation of Cheeseman-Stutz, Diagonal, and BIC/MDL is dominated by the determination of the MAP or ML configuration of the parameters. The time complexity of this task is $O(e i N+e d)$, where $e$ is the number of EM iterations and $i$ is the cost of inference in Equation 17. ${ }^{6}$
The evaluation of the Laplace approximation typically is dominated by the computation of the Hessian determinant. The time complexity of this computation (using Thiesson's 1997 method) is $O\left(d i N+d^{3}\right)$. Because $i>d$ and (typically) $N>d$, the computation of the Hessian determinant is $O(d i N)$. The Block approximation has the same complexity as the Laplace approximation, because one block may contain most of the parameters.
For the naive-Bayes clustering model, the evaluation of the Cheeseman-Stutz, Diagonal, and BIC/MDL measures are again dominated by the determination of the MAP or ML configuration. In the expectation step, we compute-for each case-the posterior probability of the hidden variable given the observed variables and the parameters. Thus, the cost of MAP/ML determination is $O(e d N)$.
The Laplace approximation is again dominated by the computation of the Hessian determinant, having a cost of $O\left(d^{2} N\right)$. The computational cost of the Block approximation has two components. The cost of the MAP/ML determination is $O(e d N)$. The Hessian contains $O(n)$ blocks each of size $O\left(r_{c}\right)$, where $r_{c}$ is the number of states of the hidden variable; consequently, the evaluation of the Hessian costs $O\left(r_{c}^{2} n N\right)=O\left(r_{c} d N\right)$. Thus, the overall cost of the Block computation is $O\left(r_{c} d N+e n N\right)$.

# 4. Experiments with multinomial-mixture models 

Our primary goal is to evaluate the accuracy and efficiency of the Block, Diagonal, BIC/MDL, and Cheeseman-Stutz approximations when used for model averaging and model selection among hidden-variable Bayesian networks. We evaluate the Cheeseman-Stutz approximation using both the maximum a posteriori (CS MAP) and maximum likelihood (CS ML) configurations of $\phi_{m}$. Similarly, we evaluate the BIC/MDL approximation using both MAP and ML configurations. A secondary goal is to evaluate the accuracy of the Laplace approximation when applied to hidden-variable Bayesian networks.
Our approach is straightforward. For a variety of models and data sets, we compare values for the marginal likelihood given by the various approximations with that given by a Monte-Carlo method that we believe to be accurate. In addition, we measure the time required to compute each approximation.
The models we evaluate are the naive-Bayes clustering models of the form shown in Figure 1. We consider synthetic models and data sets as well as models for real-world data sets. For a particular data set, we compute approximate marginal likelihoods for a series of naive-Bayes test models, where the only difference among test models is the number of states $r_{c}$ of the hidden variable $C$. We begin with a test model with $r_{c}=1$, which corresponds to a model where the observed variables $\left(X_{1}, \ldots, X_{n}\right)$ are mutually independent. We then increase $r_{c}$, typically observing a peak in the marginal likelihood, until the marginal likelihood as determined by all approximations is clearly decreasing. To evaluate the accuracy of an approximation for the purpose of model selection, we compare the value of $r_{c}$ that would be selected using that approximation with the value of $r_{c}$ that would be selected using the Monte-Carlo standard. To evaluate the accuracy of an approximation for the purpose of model averaging, we examine how each approximation weighs the second most likely model relative to the most likely model.
In our evaluations of data sets generated from synthetic models, the true number of states of the hidden variable ( $r_{c t}$ ) is available. Nonetheless, we do not use these values in our evaluation of the approximations. In particular, we are interested in how well the various methods approximate the marginal likelihood. A comparison between the best value for $r_{c}$ selected by an approximation and $r_{c t}$ would only serve to introduce confounding factors in this evaluation. For example, although the true model may have $r_{c t}=4$, the sample size of the data may not be sufficiently large to support a mixture model with four components. Nonetheless, an approximation that tends to select models that are too large may (by chance) select $r_{c}=4$. Consequently, if we were to use $r_{c t}=4$ for our comparison, we would incorrectly deem this selection to be a success.

### 4.1. Experimental parameters

All experiments were run on a P6 200 MHz machine under the Windows $\mathrm{NT}^{T M}$ operating system. The various algorithms were implemented in $\mathrm{C}++$.
We used the method of Thiesson (1997) to evaluate the Hessian of $-\log p\left(\boldsymbol{\phi}_{m}, D \mid \mathbf{m}\right)$. To compute the Cheeseman-Stutz scoring function, we assumed that dimensions $d^{\prime}$ and $d$

were equal. Although we know of no proof that this assumption is correct, Geiger et al. (1996) provide evidence that the relation holds.

We used the EM algorithm to determine the MAP and ML configurations needed by the approximations. We determined MAP configurations in the coordinate system $\Phi_{m}$. The EM algorithm ran until either the relative difference between successive values for $p\left(\boldsymbol{\phi}_{m} \mid D, \mathbf{m}\right)\left(\right.$ or $\left.p\left(D \mid \boldsymbol{\phi}_{m}, \mathbf{m}\right)\right)$ was less than $10^{-8}$ or 400 iterations were reached. In preliminary experiments, substantial additional iterations led to relative differences in the approximations of less than $10^{-4}$. Such differences did not have a significant effect on results.

In order to avoid local MAP and ML configurations, we used a variant of the multiplerestart approach described in Section 3.2. First, we sampled 64 configurations of the parameters $\boldsymbol{\phi}_{m}$ from distributions that are uniform in $\Theta_{m}$. Next we performed one expectation and maximization step, and retained the 32 initial configurations that led to the largest values of $p\left(\boldsymbol{\phi}_{m} \mid D, \mathbf{m}\right)$. Then we performed two expectation and maximization steps, retaining the 16 best initial configurations. We continued this procedure, doubling the number of expectation-maximization steps at each iteration, until only one configuration remained.

The exact marginal likelihood for test models with a single mixture component $\left(r_{c}=1\right)$ can be computed in closed form (Equation 11). We used these exact values in lieu of approximate values for all experiments. In Section 4.4, we discuss the parameters of the Monte-Carlo standard.

In all experiments, we used a uniform prior distribution over model structures, $p(\mathbf{m})=$ constant. Consequently, $p(\mathbf{m} \mid D) \propto p(D \mid \mathbf{m})$, and the value $r_{c}$ selected by a particular approximation method corresponded to the value of $r_{c}$ for which that method's marginal likelihood was a maximum. We denote this value by $r_{c *}$. We used Dirichlet prior distributions given by $\alpha_{i j k}=1$ (uniform in $\Theta_{m}$ ) in all experiments except the one in which we investigated sensitivity to parameter priors.

# 4.2. Preliminary experiment 

The goal of our first experiment was to gain a rough understanding of the accuracy of the approximations. We performed this study with synthetic models and data. In particular, we generated naive-Bayes models for various values of $n$ and $r_{c t}$. For each $n$ and $r_{c t}$ considered, we created a model in which each observed variable $X_{i}$ had two states. For each model, we set the parameters of the root node to be uniform (in $\Theta_{m}$ ), and sampled the remaining parameters from a uniform distribution (in $\Theta_{m}$ ). We then generated data with sample size $N$ from the model using a forward sampling technique. That is, we sampled a state $C=c^{j}$ according to $p(C)$, and then sampled a state of each $X_{i}$ according to $p\left(x_{i} \mid C=c^{j}\right)$. Finally, we discarded the samples of $C$, retaining only the samples of $X_{1}, \ldots, X_{n}$.

For values that we considered— $n=32,64,128, r_{c t}=4,6,8$, and $N=50,100,200$, 400 -we obtained plots of $\log p(D \mid \mathbf{m})$ versus $r_{c}$ that were similar in form. A typical plot for $n=64, r_{c}=4$, and $N=400$ is shown in Figure 2(a). Overall, the Candidate, Laplace, Block, Diagonal, and Cheeseman-Stutz MAP approximations usually peaked at the same

![img-1.jpeg](img-1.jpeg)

Figure 2. Plots of $\log p(D \mid \boldsymbol{\Pi})$ versus $r_{c}$ for synthetic data sets with $n=64, r_{c t}=4$, and $N=400$. (a) The baseline wherein each variable $x_{i}$ has two states and model parameters are sampled from independent distributions. (b) A higher resolution view of (a). (c) Model parameters are dependent with $\eta=1.4$. (d) Model parameters are dependent with $\eta=0.7$. The separation scores for each experimental condition are shown below its plot. "CS" is an abbreviation for "Cheeseman-Stutz".
value of $r_{c}$. The Laplace, Block, Diagonal, and Cheeseman-Stutz MAP approximations usually agreed with the Monte-Carlo standard for $r_{c} \leq r_{c *}$, but fell below the standard for $r_{c}>r_{c *}$. The BIC/MDL approximation peaked for smaller values of $r_{c}$ and decreased more sharply to the right of the peak than did the other approximations. The CheesemanStutz approximation was more accurate when the MAP configuration was used, whereas the BIC/MDL approximation was more accurate when the ML configuration was used.
These experiments were informative, but they did not help to discriminate the Laplace, Block, Diagonal, and Cheeseman-Stutz approximations. After additional experiments, we identified a likely cause: the clusters were well separated. In Section 4.3, we examine this phenomenon and describe more challenging data sets for analysis.
Before we do so, consider the observation that the large-sample approximations yield values that fall below those of the Monte-Carlo standard for $r_{c}>r_{c *}$. One possible explanation is that many local MAP configurations may exist when $r_{c}>r_{c *}$. If this

![img-2.jpeg](img-2.jpeg)

Figure 3. Gaussian mixtures in which the two components are (a) well separated, (b) partially separated, and (c) poorly separated.
condition occurs, then the marginal likelihood could be significantly underestimated by a Laplace approximation around a single local maximum. To test this hypothesis, we used random restarts in several of our experiments to visit hundreds of different local maxima, summing the contributions to the marginal likelihood from each maximum. In no case, however, did this approach improve performance significantly.
Another explanation is that, when $r_{c}>r_{c *}$, the test model will contain more classes than are needed to fit the data. Thus, it is likely that some of the classes will be empty in the sense that $p\left(C=c^{j} \mid \hat{\boldsymbol{\phi}}_{m}, \mathbf{m}\right)$ will be close to zero for some $c^{j}$, and the parameters corresponding to the conditional probabilities of the empty classes will be superfluous. As a result, the posterior distribution $p\left(\boldsymbol{\phi}_{m} \mid D, \mathbf{m}\right)$ will be a ridge rather than a peak, and the large-sample approximations, which assume the posterior distribution is a peak, will underestimate the marginal likelihood. In almost all of our experiments, we have found that some of the classes are empty when $r_{c}>r_{c *}$.

# 4.3. Cluster separation 

The concept of cluster separation is difficult to visualize for multinomial-mixture models. To understand this concept, let us consider one-dimensional Gaussian-mixture models as shown in Figure 3. Each model contains two Gaussian components. As we move from left to right, the components become less separated. If the mixtures are well separated, as in Figure 3(a), then for most values of $x, p\left(c^{j} \mid x\right)=1$ for either $j=1$ or $j=2$. If the mixtures are poorly separated, as in Figure 3(c), then for most values of $x, p\left(c^{j} \mid x\right)=p\left(c^{j}\right), j=1,2$. Generalizing these observations to mixtures of arbitrary distributions, we can think of cluster separation as the degree to which we are certain about the state of $C$ a posteriori, averaged over all possible observations $\mathbf{x}$.
When clusters are well separated in this sense, the learning task is straightforward. In particular, each observation will belong to one class (i.e., one state of $C$ ) with high probability. Thus, it is not surprising that the approximations do well. To evaluate the degree of separation of our models, we define the separation score of a model $\left(\mathbf{m}, \boldsymbol{\phi}_{m}\right)$ to be the negative expected entropy of the posterior distribution for $C$ scaled to the range $[0,1]$ :

$$
\operatorname{Sep}\left(\mathbf{m}, \phi_{\mathrm{m}}\right)=1-\frac{1}{\log t_{\mathrm{c}}} \sum_{\mathbf{x}} \mathrm{p}\left(\mathbf{x} \mid \phi_{\mathrm{m}}, \mathbf{m}\right)\left[\sum_{\mathrm{k}=1}^{r_{c}}-\mathrm{p}\left(c^{l} \mid \mathbf{x}, \phi_{\mathrm{m}}, \mathbf{m}\right) \log \mathrm{p}\left(c^{l} \mid \mathbf{x}, \phi_{\mathrm{m}}, \mathbf{m}\right)\right]
$$

Because the sum over $\mathbf{x}$ is intractable, we use the finite-sample version of Equation 22, which depends on the random sample $D$ :

$$
\operatorname{Sep}\left(\mathbf{m}, \boldsymbol{\phi}_{m}, D\right)=1-\frac{1}{N \log r_{c}} \sum_{\mathbf{x} \in D} \sum_{k=1}^{r_{c}}-p\left(c^{j} \mid \mathbf{x}, \boldsymbol{\phi}_{m}, \mathbf{m}\right) \log p\left(c^{j} \mid \mathbf{x}, \boldsymbol{\phi}_{m}, \mathbf{m}\right)
$$

Note that values for $\operatorname{Sep}\left(\mathbf{m}, \boldsymbol{\phi}_{m}, D\right)$ increase with increasing separation. The separation score for the model in Figure 2(a) is 1.0000, confirming our observation that the clusters are well separated.

To provide the approximations with more of a challenge, we should decrease model separation. One approach for doing so is to decrease $n$, the number of observed variables. This approach is not useful, however, because we want to evaluate the accuracy and efficiency of the approximations for a wide range of $n$. Another approach is to sample the parameters from a distribution that is biased toward a uniform distribution (in $\Theta_{m}$ ). We do not use this approach either, because we do not believe such parameter distributions are common.

Another approach that produces more realistic models is to introduce dependencies among the parameters such that $p\left(x_{i} \mid c^{j}, \boldsymbol{\phi}_{m}, \mathbf{m}\right)$ and $p\left(x_{i} \mid c^{l}, \boldsymbol{\phi}_{m}, \mathbf{m}\right)$ are more likely to have similar values for $l \neq j$ than if they were chosen independently. Consider a simple approach for introducing such dependencies, in which we let $\theta\left(x_{i}^{k} \mid c^{j}\right)$ and $\phi\left(x_{i}^{k} \mid c^{j}\right)$ be the parameters corresponding to $p\left(x_{i}^{k} \mid c^{j}\right)$ in the coordinate systems $\Theta_{m}$ and $\Phi_{m}$, respectively. First, we sample the parameters $\theta\left(x_{i}^{k} \mid c^{1}\right)$ for all $i$ from uniform distributions and transform these parameters to $\Phi_{m}$. Then, we set

$$
\phi\left(x_{i}^{k} \mid c^{j}\right)=\phi\left(x_{i}^{k} \mid c^{1}\right)+\operatorname{Normal}(0, \eta)
$$

for $i=1, \ldots, n, j=2, \ldots, r_{c}$, and $k=2, \ldots, r_{i}$, where $\operatorname{Normal}(0, \eta)$ is a sample from a normal distribution with mean zero and standard deviation $\eta$. As $\eta$ decreases toward zero, the cluster separation decreases.

As shown in Figure 2, when we decrease cluster separation, the value $r_{c *}$ decreases. This observation is not surprising. In the extreme case $\eta=0$, the clusters are superimposed, and $r_{c *}$ should be one. Given this observation, we want to challenge the approximations with clusters that partially overlap, but not by so much that (in effect) only one cluster remains.

# 4.4. Monte-Carlo standard 

Before we consider additional experiments, let us examine our Monte-Carlo gold standard: the Candidate method.

Recall that the Candidate method uses a Gibbs sampler to determine $p\left(\boldsymbol{\phi}_{m}^{*} \mid D, \mathbf{m}\right)$ (Section 3.4). This Gibbs sampler has four parameters: $\alpha$, the number of samples $D_{c}$ used to burn in the Gibbs sampler; $\beta$, the number of samples used to select $\boldsymbol{\phi}_{m}^{*} ; \gamma$, the number of

samples that separate the phase where $\boldsymbol{\phi}_{m}^{*}$ is selected and the phase where $p\left(\boldsymbol{\phi}_{m}^{*} \mid D, \mathbf{m}\right)$ is computed; and $\delta$, the number of samples used to compute $p\left(\boldsymbol{\phi}_{m}^{*} \mid D, \mathbf{m}\right)$. In preliminary experiments with the Candidate method, we increased these parameters until we obtained a low-noise approximation for $\log p(D \mid \mathbf{m})$ across the spectrum of values $n=32,64,128$, $r_{c t}=4,6,8$, and $N=50,100,200,400$. We evaluated the noise in the approximation for a given value of the parameters by examining plots of $\log p(D \mid \mathbf{m})$ versus $r_{c}$.
We found that the burn-in and $\boldsymbol{\phi}_{m}^{*}$ selection phases could be combined without increasing the noise in the approximation. This observation is not surprising, because typical (and likely) configurations for $D_{c}$ usually do not occur until the Gibbs sampler has burned in. Except when $N$ was small ( $N \leq 50$ ), no configuration of $D_{c}$ was visited more than once. Consequently, in most experiments, the configuration $D_{c}^{*}$ chosen to select $\boldsymbol{\phi}_{m}^{*}$ was the most likely $D_{c}$. For $r_{c t} \leq 4$, we found that $\beta=100, \gamma=10$, and $\delta=100$ produced a low-noise approximation. For $r_{c t} \geq 8$, we found that $\beta=400, \gamma=10$, and $\delta=400$ was adequate. Also, the noise in the approximation was slightly lower when we sampled an initial $D_{c}$ from the MAP configuration of $\boldsymbol{\phi}_{m}$ rather than from a distribution that is uniform in $\Theta_{m}$. We used these algorithm parameters in our experiments (including those on real-world data sets).
As we discussed in Section 4.2, the Candidate and Laplace approximations produced similar values for $p(D \mid \mathbf{m})$ for $r_{c} \leq r_{c *}$ (see Figure 2), and disagreements for $r_{c}>r_{c *}$ could be explained. These observations, combined with the fact that the approximation had low noise, suggested that the Candidate approximation was accurate. Nonetheless, the Candidate approximation became noisy for $n<32$, even when we increased $\beta$ and $\delta$ to 1600. Furthermore, low noise does not guarantee high accuracy. Consequently, we wanted to further evaluate the accuracy of the Candidate method. To do so, we considered data sets with small sample sizes, so that we could determine $p(D \mid \mathbf{m})$ exactly by summing $p\left(D_{c} \mid \mathbf{m}\right)$ over all possible configurations of $D_{c}$ consistent with $D$. We used data generated from synthetic models with $n=64, r_{c t}=2$, and $N=10$. Results for various degrees of overlap $(\eta=1.25,3.5,5.75)$ are shown in Figure 4.
In all plots, the Candidate approximation agreed closely with the exact value for $p(D \mid \mathbf{m})$. In addition, although large-sample approximations are unlikely to be valid for samples of size 10, the relationships among the Candidate, Laplace, Block, and Diagonal approximations for $N=10$ were similar to those for large $N$. In particular, the Laplace, Block, and Diagonal approximations agreed with the Candidate approximation for $r_{c} \leq r_{c *}$, but fell below the Candidate approximation for $r_{c}>r_{c *}$. These results provide additional evidence that the Candidate approximation is accurate.
We note that the Cheeseman-Stutz MAP approximation agreed more closely with the Candidate (and exact) values for $p(D \mid \mathbf{m})$ than did the Laplace approximation. We suggest an explanation for this observation in the following section.

# 4.5. Sensitivity analyses for synthetic data 

We evaluated the approximations for a variety of synthetic models and data sets. First, we examined the accuracy of the approximations as a function of $n$ (the number of input variables), $r_{c t}$ (the number of classes in the generative model), and $N$ (the sample size

![img-3.jpeg](img-3.jpeg)

Figure 4. Plots of $\log p(D \mid \mathbf{m})$ versus $r_{c}$ for synthetic data sets with $n=64, r_{c t}=2, N=10$, and various degrees of cluster overlap.
of the data). For each $n$ and $r_{c t}$ considered, we created a model in which each observed variable $X_{i}$ had two states. For each model, we sampled the parameters for its hidden node from a uniform distribution (in $\Theta_{m}$ ) so as to generate clusters of various sizes. We generated dependent parameters for the conditional distributions as described in Section 4.3 using $\eta=1.75$. For most experiments, this choice for $\eta$ produced clusters that overlapped partially but not completely. For each experiment-defined by a given $n, r_{c}$, and $N$-we evaluated the approximations for five data sets generated with different random seeds.
Figures 5, 6, and 7 show plots of $\log p(D \mid \mathbf{m})$ versus $r_{c}$ for one of the five data sets in the experiments where $n, r_{c}$, and $N$ were varied, respectively. The most surprising aspect of the results was that the introduction of cluster overlap did not lead to significant differences in the accuracy of the approximations. As in the case of no cluster overlap, the Candidate, Laplace, Block, Diagonal, and Cheeseman-Stutz MAP approximations usually peaked at the same value of $r_{c}$. The Laplace, Block, Diagonal, and Cheeseman-Stutz MAP approximations usually agreed with the Monte-Carlo standard for $r_{c} \leq r_{c s}$, but fell below the standard for $r_{c}>r_{c s}$. The BIC/MDL approximation peaked for smaller values of $r_{c}$ and decreased more sharply to the right of the peak than did the other approximations.

The Cheeseman-Stutz approximation was more accurate when the MAP configuration was used, whereas the BIC/MDL approximation was more accurate when the ML configuration was used.
To evaluate the accuracy of the approximations when used for model selection, we computed the quantity $\Delta r_{c *}$-the difference between $r_{c *}$ for the Monte-Carlo standard and $r_{c *}$ for the approximation-and averaged this difference over the five data sets for each experiment. Table 1 contains these averages. With the exception of the Cheeseman-Stutz ML and BIC/MDL approximations, the approximations almost always select the same model.
To evaluate the accuracy of the approximations when used for model averaging, we examined how each approximation penalized the second most likely model relative to the most likely model. In particular, we used the Candidate method to identify the two model structures with the largest $\left(\mathbf{m}_{1}\right)$ and second largest $\left(\mathbf{m}_{2}\right)$ marginal likelihoods. We then computed the log Bayes factor $\log p\left(D \mid \mathbf{m}_{1}\right) / p\left(D \mid \mathbf{m}_{2}\right)$ for each approximation. If an approximation were useful for model averaging, then these scores would be similar to that for the Monte-Carlo standard. The results for the Laplace approximation are shown in Table 2. In 20 of the 40 unique entries, the log Bayes factor was less than $3.6=\ln (37)$ for the Monte-Carlo standard, but greater than $14.4=\ln (1.8$ million) for the Laplace approximation. In these cases, if we had used the Laplace approximation, we would have removed $\mathbf{m}_{2}$ from consideration. In contrast, if we had used the Monte-Carlo standard, $\mathbf{m}_{2}$ would have contributed to the average, perhaps significantly, depending on the hypothesis of interest. Therefore, in (at least) these 20 cases, the Laplace approximation was not a good substitute for the Monte-Carlo standard. The other approximations were at least as inaccurate.
Next, we examined the sensitivity of the approximations to parameter priors. For the experimental condition defined by $n=64, r_{c t}=8, N=400$, and $\eta=1.75$, we evaluated the approximations using three Dirichlet priors: $\alpha_{i j k}=1$ (uniform in $\Theta_{m}$ ); $\alpha_{i j k}=1 / r_{i} q_{i}$; and $\alpha_{i j k}=0.1 / r_{i} q_{i}$. The second and third priors are a special case of the priors described by Heckerman et al. (1995). The results are shown in Figure 8.
All approximations except the BIC/MDL ML were sensitive to the variation in priors. ${ }^{7}$ This result demonstrates that it can be important to choose a prior carefully. In addition, it shows that the BIC/MDL approximation is inferior to the others in the sense that it is unresponsive to the prior. ${ }^{8}$
Recall one of the conditions used to derive the Laplace approximation: the MAP configuration $\hat{\boldsymbol{\phi}}_{m}$ should lie away from the boundary of $\boldsymbol{\phi}_{m}$. We examined the sensitivity of the approximations to violations of this condition. In particular, we generated a model with $n=64$ and $r_{c t}=2$, assigning parameters according to the procedure in Section 4.3 with $\eta=0$. That is, we generated a model with two identical multinomial mixtures. Then, with probability 0.1 , we replaced each conditional probability $p\left(x_{i}^{k} \mid c^{j}, \boldsymbol{\phi}_{m}, \mathbf{m}\right)$ with zero (a boundary value), and then renormalized each conditional distribution. If both probabilities $p\left(x_{i}^{1} \mid c^{j}, \boldsymbol{\phi}_{m}, \mathbf{m}\right)$ and $p\left(x_{i}^{2} \mid c^{j}, \boldsymbol{\phi}_{m}, \mathbf{m}\right)$ were set to zero, then we chose one of the probabilities at random and set it to one. We then generated a data set with $N=400$. For comparison, we ran the experiment defined by $n=64, r_{c t}=2$, and $N=400$, with parameters generated using $\eta=1.75$. For both experimental conditions, the parameters for the hidden node were equal to 0.5 . The interesting result, shown in Figure 9, is

![img-4.jpeg](img-4.jpeg)

Figure 5. Sensitivity to $n$, the number of observed variables. Approximate log marginal likelihood versus $r_{c}$ for models with $r_{c t}=4$ and $\eta=1.75$ and data sets with $N=400$, when (a) $n=32$, (b) $n=64$, and (c) $n=128$.
that the Cheeseman-Stutz MAP approximation yielded almost the same values as did the Monte-Carlo standard, whereas the other approximations performed as usual. That is, the Cheeseman-Stutz MAP approximation was more robust to violations of this assumption than were the other approximations, including the Laplace approximation. The result was reproducible for a variety of models.
This observation offers an explanation for the small $N$ results in Figure 4, in which the Cheeseman-Stutz MAP approximation is more accurate than the other large-sample approximations. In particular, for small $N$, many observations for $\mathbf{X}$ that are possible are not realized in the data set. Consequently, many of the parameters in the MAP configuration for $\phi_{m}$ will be close to the boundary.

# 4.6. Computation times 

As we have discussed, the accuracy of the approximations should be balanced against their computational costs. Figure 10 shows the costs for the experiment defined by $n=64$, $r_{c t}=8, N=400$, and $\eta=1.75$. The costs shown for the Candidate, Laplace, Block,

![img-5.jpeg](img-5.jpeg)

Figure 6. Sensitivity to $r_{c t}$, the number of classes in the true model. Approximate log marginal likelihood versus $r_{c}$ for models with $n=64$ and $\eta=1.75$ and data sets with $N=400$, when (a) $r_{c t}=4$, (b) $r_{c t}=6$, and (c) $r_{c t}=8$.

Diagnonal, Cheeseman-Stutz, and BIC/MDL approximations exclude the computation of the MAP or ML configuration using the EM algorithm. This plot is in agreement with the computational complexities of the algorithms given in Section 3.6. Note that the EM algorithm dominates the cost of the Block, Diagonal, Cheeseman-Stutz, and BIC/MDL approximations. In contrast, the evaluation of the Hessian is more expensive than the cost of finding the MAP configuration using EM. Also, note that the Monte-Carlo standard is almost as efficient as the Laplace approximation for larger models.

# 4.7. Real-world data sets 

To augment our experiments with synthetic data, we evaluated the various approximations on real-world data sets. We checked several data repositories, but could not locate data sets that involved discrete-variable clustering. Instead, we obtained classification data sets from the UCI Machine Learning Repository (Merz \& Murphy, 1996) and discarded the known class information. We used the small soybean (Michalski \& Chilausky, 1980), standard

![img-6.jpeg](img-6.jpeg)

Figure 7. Sensitivity to $N$, sample size. Approximate log marginal likelihood versus $r_{c}$ for models with $n=64$, $r_{c t}=4$, and $\eta=1.75$, when (a) $N=50$, (b) $N=100$, (c) $N=200$, and (d) $N=400$.
audiology (Bareiss \& Porter, 1987), and lung cancer (Hong \& Yang, 1994) databases. For the audiology data set, where both training and test data were available, we merged these data sources.
The results, shown in Figure 11 and Table 3, are similar to those for synthetic data. In particular, the BIC/MDL approximation tended to peak early and fell off more sharply than did the other approximations. The large-sample approximations (except CheesemanStutz MAP) fell off more rapidly than did the Candidate approximation for $r_{c} \geq r_{c *}$. The Cheeseman-Stutz approximation was more accurate when the MAP configuration was used, whereas the BIC/MDL approximation was more accurate when the ML configuration was used. For the audiology data set, most approximations selected only two classes, far less than the specified number. Nonetheless, there were only two classes in the data set with more than 20 instances.
There were three deviations from the studies with synthetic data that occurred in the evaluation of all three data sets. First, there were some values of $r_{c}$ for which the Laplace and/or Block approximation could not be computed, because the determinant of the Hessian (or block) was negative. Second, the Cheeseman-Stutz MAP approximation was more

Table 1. Errors in model selection-mean (s.d.) over five data sets.


![img-7.jpeg](img-7.jpeg)

Figure 8. Sensitivity to parameter priors. In each experiment, $n=64, r_{c t}=8, N=400$, and $\eta=1.75$. The Dirichlet priors are given by (a) $\alpha_{i j k}=1$, (b) $\alpha_{i j k}=1 / r_{i} q_{i}$, and (c) $\alpha_{i j k}=0.1 / r_{i} q_{i}$.
accurate than the other large-sample approximations. Third, many of the parameters were near the boundary in the MAP configurations for $\phi_{m}$. This last observation explains the first two. In particular, when parameters are near the boundary, $\log p\left(\phi_{m} \mid D, \mathbf{m}\right)$ need not

Table 2. Errors in model averaging. Log Bayes factors given by the Candidate (C) and Laplace (L) methods are shown.


![img-8.jpeg](img-8.jpeg)

Figure 9. Sensitivity to parameters at the boundary. In both experiments, $n=64, r_{c t}=2, N=400$. (a) Parameters are generated with $\eta=1.75$. (b) $10 \%$ of the parameters $p\left(x_{i}^{k} \mid c^{j}, \phi_{i n}, \mathbf{m}\right)$ are set to zero.
be concave down around $\tilde{\phi}_{i n}$. Furthermore, as we saw in Section 4.5, the Cheeseman-Stutz MAP is more robust to situations in which parameters in the MAP configuration are near the boundary.

# 5. Discussion 

We have evaluated the accuracy and efficiency of the Laplace, Block-Diagnonal, Diagonal, Cheeseman-Stutz, and BIC/MDL approximations for the marginal likelihood of naiveBayes models with a hidden root node. In this evaluation, we used the Monte-Carlo Candidate method as a gold standard. From our experiments, we draw a number of conclusions:

- None of approximations are accurate when used for model averaging.

![img-9.jpeg](img-9.jpeg)

Figure 10. Computation time in seconds versus model dimension for the experimental condition $n=64, r_{\mathrm{ct}}=8$, $N=400$, and $\eta=1.75$.

- All of the approximations, with the exception of BIC/MDL, are accurate for model selection.
- Among the accurate approximations, the Cheeseman-Stutz and Diagonal approximations are the most efficient.
- All of the approximations, with the exception of BIC/MDL, can be sensitive to the prior distribution over model parameters.
- The Cheeseman-Stutz approximation is more accurate when evaluated using the maximum a posteriori (MAP) configuration of the parameters, whereas the BIC/MDL approximation is more accurate when evaluated using the maximum likelihood (ML) configuration.
- The Cheeseman-Stutz approximation can be more accurate than the other approximations, including the Laplace approximation, in situations where the parameters in the MAP configuration are near a boundary.

Our findings are valid only for naive-Bayes models with a hidden root node, but these results are important, because they apply directly to probability-based clustering. Also, it seems likely that our results will extend to models for discrete variables where each variable that is unobserved has an observed Markov blanket. Under these conditions, each Bayesian inference required by the scoring functions (e.g., Equation 17) reduces to a naive-Bayes computation. Nonetheless, more extensive experiments are warranted to address models with more general structure and non-discrete distributions.

Although we have examined the computation of marginal likelihood for model averaging and model selection, we have not concentrated on how to handle the parameters once a model or set of models have been selected. If computation time is not an issue and one is concerned primarily with prediction, then a Monte-Carlo average over parameters is probably best (Neal, 1991). Nonetheless, one sometimes needs a fast model for prediction

![img-10.jpeg](img-10.jpeg)

Figure 11. Plots of approximate log marginal likelihoods versus $r_{c}$ for the (a) small soybean (b) standard audiology, and (c) lung cancer data sets.

Table 3. Number of classes selected by the approximations.


or one may want point values for the parameters to facilitate an understanding of the domain. What is best in these circumstances remains an open question.

# Acknowledgments 

We thank Wray Buntine, Dan Geiger, Michael Jordan, Daphne Koller, Yan LeCun, Chris Meek, Radford Neal, Adrian Raftery, Padhraic Smyth, Bo Thiesson, and Larry Wasserman for useful discussions. We also thank David MacKay for his suggestions regarding the Candidate method.

# Notes 

1. Throughout this paper, we use "efficiency" to refer to computational efficiency as opposed to statistical efficiency.
2. An equivalent criterion that is often used is
$\log \left(p(\mathbf{m} \mid D) / p\left(\mathbf{m}_{0} \mid D\right)\right)=\log \left(p(\mathbf{m}) / p\left(\mathbf{m}_{0}\right)\right)+\log \left(p(D \mid \mathbf{m}) / p\left(D \mid \mathbf{m}_{0}\right)\right)$.
The ratio $p(D \mid \mathbf{m}) / p\left(D \mid \mathbf{m}_{0}\right)$ is known as a Bayes factor.
3. One of the technical assumptions used to derive this approximation is that the prior distribution is non-zero around $\hat{\phi}_{m}$.
4. For this observation to hold, the Gibbs sampler must be irreducible. That is, the probability distribution $p(\mathbf{x})$ must be such that we can eventually sample any possible configuration of $\mathbf{X}$ given any possible initial configuration of $\mathbf{X}$. For example, if $p(\mathbf{x})$ contains no zero probabilities, then the Gibbs sampler will be irreducible.
5. This procedure was suggested by David MacKay (1996) in a personal communication.
6. Using Jensen et al.'s (1990) inference algorithm, only one inference is needed per expectation step.
7. Marginal likelihoods for $r_{c}=1$ were sensitive to priors because we computed these values exactly using Equation 11 .
8. In previous experiments (Chickering \& Heckerman, 1996), we considered another large-sample approximation for the marginal likelihood suggested by Draper (1995). His approximation suffers from the same lack of sensitivity to the prior as does the BIC/MDL ML approximation.
