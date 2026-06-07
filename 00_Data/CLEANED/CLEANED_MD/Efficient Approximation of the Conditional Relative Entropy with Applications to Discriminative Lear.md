Article

# Efficient Approximation of the Conditional Relative Entropy with Applications to Discriminative Learning of Bayesian Network Classifiers 

Alexandra M. Carvalho ${ }^{1,2, *}$, Pedro Adão ${ }^{3,4}$ and Paulo Mateus ${ }^{4,5}$<br>${ }^{1}$ Department of Electrical Engineering, IST, University of Lisbon, Lisbon 1049-001, Portugal<br>${ }^{2}$ PIA, Instituto de Telecomunicações, Lisbon 1049-001, Portugal<br>${ }^{3}$ Department of Computer Science, IST, University of Lisbon, Lisbon 1049-001, Portugal;<br>E-Mail: pedro.adao@ist.utl.pt<br>${ }^{4}$ SQIG, Instituto de Telecomunicações, Lisbon 1049-001, Portugal; E-Mail: pmat@math.ist.utl.pt<br>${ }^{5}$ Department of Mathematics, IST, University of Lisbon, Lisbon 1049-001, Portugal<br>* Author to whom correspondence should be addressed; E-Mail: asmc@1x.it.pt;<br>Tel.: +351-218-418-454; Fax: +351-218-418-472.

Received: 8 June 2013; in revised form: 3 July 2013 / Accepted: 3 July 2013 /
Published: 12 July 2013


#### Abstract

We propose a minimum variance unbiased approximation to the conditional relative entropy of the distribution induced by the observed frequency estimates, for multi-classification tasks. Such approximation is an extension of a decomposable scoring criterion, named approximate conditional log-likelihood (aCLL), primarily used for discriminative learning of augmented Bayesian network classifiers. Our contribution is twofold: (i) it addresses multi-classification tasks and not only binary-classification ones; and (ii) it covers broader stochastic assumptions than uniform distribution over the parameters. Specifically, we considered a Dirichlet distribution over the parameters, which was experimentally shown to be a very good approximation to CLL. In addition, for Bayesian network classifiers, a closed-form equation is found for the parameters that maximize the scoring criterion.


Keywords: conditional relative entropy; approximation; discriminative learning; Bayesian network classifiers

# 1. Introduction 

Bayesian networks [1] are probabilistic graphical models that represent the joint probability distribution of a set of random variables. They encode specific conditional independence properties pertaining to the joint distribution via a directed acyclic graph (DAG). To achieve this, each vertex (aka node) in the DAG contains a random variable, and edges between them represent the dependencies between the variables. Specifically, given a DAG, a node is conditionally independent of its non-descendants given its parents. Besides serving as a representation of a set of independencies, the DAG also aids as a skeleton for factorizing a distribution via the chain rule of probability. The chief advantage of Bayesian networks is that they can specify dependencies only when necessary, providing compact representations of complex domains that leads to a significant reduction in the cost of learning and inference.

Bayesian networks have been widely used for classification [2-4], being known in this context as Bayesian network classifiers (BNC). The use of generative learning methods in choosing the Bayesian network structure has been pointed out as the likely cause for their poor performance when compared to much simpler methods [2,5]. In contrast to generative learning, where the goal is to be able to describe (or generate) the entire data, discriminative learning focuses on the capacity of a model to discriminate between different classes. To achieve this end, generative methods usually maximize the log-likelihood (LL) or a score thereof, whereas discriminative methods focus on maximizing the conditional log-likelihood (CLL). Unfortunately, maximizing the CLL of a BNC turns out to be computationally much more challenging than maximizing LL. For this reason, the community has resorted to decomposing the learning procedure into generative-discriminative subtasks [3,6,7]. More recently, Carvalho et al. proposed a new scoring criterion, called approximate conditional log-likelihood (aCLL), for fully-discriminative learning of BNCs, exhibiting good performance, both in terms of accuracy and computational cost [8]. The proposed scoring criterion was shown to be the minimum variance unbiased (MVU) approximation to CLL.

Despite the aCLL good performance, the initial proposal has three significant restrictions. First, it was only devised for binary-classification tasks. Second, it was derived under the assumption of uniform distribution over the parameters. Third, the parameters of the network structure that maximize the score resorted in an unknown manner. In this paper, we address all these shortcomings, which makes it possible to apply aCLL in a broader setup, while maintaining the desired property of a MVU approximation to CLL. In order to solve the first two restrictions, we start by deriving the approximation for multi-classification tasks under much more relaxed stochastic assumptions. In this context, we considered multivariate symmetric distributions over the parameters and detailed the pertinent cases of uniform and Dirichlet distributions. The constants required by the approximation are computed analytically for binary and ternary uniform distributions. In addition, a Monte Carlo method is proposed to compute these constants numerically for other distributions, including the Dirichlet. In addressing the third shortcoming, the parameters of the BNC that maximize the proposed approximation to the conditional log-likelihood (CLL) are derived. Finally, maximizing CLL is shown to be equivalent to minimizing the conditional relative entropy of the (conditional) distribution (of the class, given the other variables) induced by the observed frequency estimates and the one induced by the learned BNC model.

To gauge the performance of the proposed approximation, we conducted a set of experiments over 89 biologically relevant datasets already used in previous works [9,10]. The results show that the models that maximized aCLL under a symmetric Dirichlet assumption attain a higher CLL, with great statistical significance, in comparison with the generative models that maximized LL and the discriminative models that maximized aCLL under a symmetric uniform distribution. In addition, aCLL under a symmetric uniform distribution also significantly outperforms LL in obtaining models with higher CLL.

The paper is organized as follows. In Section 2, we review the essentials of BNCs and revise the aCLL approximation. In Section 3, we present the main contribution of this paper, namely, we extend aCLL to multi-classification tasks under general stochastic assumptions and derive the parameters that maximize aCLL for BNCs. Additionally, in Section 4, we relate the proposed scoring criterion with the conditional relative entropy, and in Section 5, we provide experimental results. Finally, we draw some conclusions and mention future work in Section 6.

# 2. Background 

In this section, we review the basic concepts of BNCs required to understand the proposed methods. We then discuss the difference between generative and discriminative learning of BNCs and present the aCLL scoring criterion [8].

### 2.1. Bayesian Network Classifiers

Let $X$ be a discrete random variable taking values in a countable set, $\mathcal{X} \subset \mathbb{R}$. In all that follows, the domain, $\mathcal{X}$, is finite. We denote an $(n+1)$-dimensional random vector by $\mathbf{X}=\left(X_{1}, \ldots, X_{n}, C\right)$, where each component, $X_{i}$, is a random variable over $\mathcal{X}_{i}$ and $C$ is a random variable over $\mathcal{C}=\{1, \ldots, s\}$. The variables, $X_{1}, \ldots, X_{n}$, are called attributes or features, and $C$ is called the class variable. For each variable, $X_{i}$, we denote the elements of $\mathcal{X}_{i}$ by $x_{i 1}, \ldots, x_{i r_{i}}$, where $r_{i}$ is the number of values that $X_{i}$ can take. We say that $x_{i k}$ is the $k$-th value of $X_{i}$, with $k \in\left\{1, \ldots, r_{i}\right\}$. The probability that $\mathbf{X}$ takes value, $\mathbf{x}$, is denoted by $P(\mathbf{x})$, conditional probabilities, $P(\mathbf{x} \mid \mathbf{z})$, being defined correspondingly.

A Bayesian network classifier (BNC) is a triple $B=(\mathbf{X}, G, \Theta)$, where $\mathbf{X}=\left(X_{1}, \ldots, X_{n}, C\right)$ is a random vector. The network structure, $G=(\mathbf{X}, E)$, is a directed acyclic graph (DAG) with nodes in $\mathbf{X}$ and edges $E$ representing direct dependencies between the variables. We denote by $\Pi_{X_{i}}$ the (possibly empty) set of parents of $X_{i}$ in $G$. For efficiency purposes, it is common to restrict the dependencies between the attributes and the class variable, imposing all attributes to have the class variable as the parent; rigorously, these are called augmented naive Bayes classifiers, but it is common to refer to them abusively as BNCs. In addition, the parents of $X_{i}$ without the class variable are denoted by $\Pi_{X_{i}}^{*}=\Pi_{X_{i}} \backslash$ $\{C\}$. We denote the number of possible configurations of the parent set, $\Pi_{X_{i}}^{*}$, by $q_{i}^{*}$. The actual parent configurations are ordered (arbitrarily) and denoted by $w_{i 1}^{*}, \ldots, w_{i q_{i}^{*}}^{*}$, and we say that $w_{i j}^{*}$ is the $j$-th configuration of $\Pi_{X_{i}}^{*}$, with $j \in\left\{1, \ldots, q_{i}^{*}\right\}$. Taking into account this notation, the third element of the BNC triple denotes the parameters, $\Theta$, given by the families, $\left\{\theta_{i j c k}\right\}_{i \in\{1 \ldots n\}, j \in\left\{1, \ldots, q_{i}^{*}\right\}, c \in\{1, \ldots, s\}, k \in\left\{1, \ldots, r_{i}\right\}}$ and $\left\{\theta_{c}\right\}_{c \in\{1, \ldots, s\}}$, which encode the local distributions of the network via:

$$
\begin{aligned}
& P_{B}(C=c)=\theta_{c} \text { and } \\
& P_{B}\left(X_{i}=x_{i k} \mid \Pi_{X_{i}}^{*}=w_{i j}^{*}, C=c\right)=\theta_{i j c k}
\end{aligned}
$$

A BNC, $B$, defines a unique joint probability distribution over $\mathbf{X}$ given by:

$$
P_{B}\left(X_{1}, \ldots, X_{n}, C\right)=P_{B}(C) \prod_{i=1}^{n} P_{B}\left(X_{i} \mid \Pi_{X_{i}}\right)
$$

The conditional independence properties pertaining to the joint distribution are essentially determined by the network structure. Specifically, $X_{i}$ is conditionally independent of its non-descendants given its parents, $\Pi_{X_{i}}$ in $G$ [1]; and so, $C$ depends on all attributes (as desired).

The problem of learning a BNC given data, $D$, consists in finding the BNC that best fits $D$. This can be achieved by a score-based learning algorithm, where a scoring criterion is considered in order to quantify the fitting of a BNC. Contributions in this area of research are typically divided in two different problems: scoring and searching. The scoring problem focuses on devising new scoring criteria to measure the goodness of a certain network structure given the data. On the other hand, the searching problem concentrates on identifying one or more network structures that yield a high value for the scoring criterion in mind. If the search is conducted with respect to a neighborhood structure defined on the space of possible solutions, then we are in the presence of local score-based learning.

Local score-based learning algorithms can be extremely efficient if the scoring criterion employed is decomposable, that is, if the scoring criterion can be expressed as a sum of local scores associated to each network node and its parents. In this case, any change over the network structure carried out during the search procedure is evaluated by considering only the difference to the score of the previously assessed network. The most common scoring criteria employed in BNC learning are reviewed in [11-13]. We refer the interested reader to newly developed scoring criteria in the works of Carvalho et al. [8], de Campos [14] and Silander et al. [15].

Unfortunately, even performing local score-based learning, searching for unrestricted BNC structures from data is NP-hard [16]. Worse than that, finding for unrestricted approximate solutions is also NP-hard [17]. These results led the community to search for the largest subclass of BNCs for which there is an optimal and efficient learning algorithm. The first attempts confined the network to tree-augmented naive (TAN) structures [2] and used Edmonds [18] and Chow-Liu [19] optimal branching algorithms to learn the network. More general classes of BNCs have eluded efforts to develop optimal and efficient learning algorithms. Indeed, Chickering [20] showed that learning networks constrained to have at most two in-degrees is already NP-hard.

# 2.2. Generative versus Discriminative Learning of Bayesian Network Classifiers 

For convenience, we introduce some additional notation. Let data, $D$, be given by:

$$
D=\left\{\mathbf{y}_{1}, \ldots, \mathbf{y}_{N}\right\}, \text { where } \mathbf{y}_{t}=\left(y_{t}^{1}, \ldots, y_{t}^{n}, c_{t}\right)
$$

Generative learning reduces to maximizing the likelihood of the data, by using the log-likelihood scoring criterion or a score thereof (for instance, [14,15]). The log-likelihood scoring criterion can be written as:

$$
\mathrm{LL}(B \mid D)=\sum_{t=1}^{N} \log P_{B}\left(y_{t}^{1}, \ldots, y_{t}^{n}, c_{t}\right)
$$

On the other hand, discriminative learning concerns maximizing the conditional likelihood of the data. The reason why this is a form of discriminative learning is that it focuses on correctly discriminating between classes by maximizing the probability of obtaining the correct classification. The conditional log-likelihood (CLL) scoring criterion can be written as:

$$
\operatorname{CLL}(B \mid D)=\sum_{t=1}^{N} \log P_{B}\left(c_{t} \mid y_{t}^{1}, \ldots, y_{t}^{n}\right)
$$

Unlike LL, CLL does not decompose over the network structure, and therefore, there is no closed-form equation for optimal parameter estimates for the CLL scoring criterion. This issue was first approached by splitting the problem into two distinct tasks: find optimal-CLL parameters [6,7] and find optimal-CLL structures [3,21]. Although showing promising results, these approaches still present a problem of computational nature. Indeed, optimal-CLL parameters have been achieved by resorting to gradient descent methods, and optimal-CLL structures have been found only with global search methods, which cause both approaches to be very inefficient. Recently, a least-squares approximation to CLL, called approximate conditional log-likelihood (aCLL), was proposed, which enables full discriminative learning of BNCs in a very efficient way [8]. The aCLL scoring criterion is presented in detail in the next section.

# 2.3. A First Approximation to the Conditional Log-Likelihood 

In this section, we present the approximation to the conditional log-likelihood proposed in [8]. Therein, it was assumed that the class variable was binary, that is, $\mathcal{C}=\{0,1\}$. For the binary case, the conditional probability of the class variable can then be written as:

$$
P_{B}\left(c_{t} \mid y_{t}^{1}, \ldots, y_{t}^{n}\right)=\frac{P_{B}\left(y_{t}^{1}, \ldots, y_{t}^{n}, c_{t}\right)}{P_{B}\left(y_{t}^{1}, \ldots, y_{t}^{n}, c_{t}\right)+P_{B}\left(y_{t}^{1}, \ldots, y_{t}^{n}, 1-c_{t}\right)}
$$

For convenience, the two terms in the denominator were denoted by:

$$
\begin{aligned}
U_{t} & =P_{B}\left(y_{t}^{1}, \ldots, y_{t}^{n}, c_{t}\right) \quad \text { and } \\
V_{t} & =P_{B}\left(y_{t}^{1}, \ldots, y_{t}^{n}, 1-c_{t}\right)
\end{aligned}
$$

so that Equation (6) becomes simply:

$$
P_{B}\left(c_{t} \mid y_{t}^{1}, \ldots, y_{t}^{n}\right)=\frac{U_{t}}{U_{t}+V_{t}}
$$

The BNC, $B$, was omitted from the notation of both $U_{t}$ and $V_{t}$ for the sake of readability.

The log-likelihood (LL) and the conditional log-likelihood (CLL) now take the form:

$$
\begin{aligned}
\operatorname{LL}(B \mid D) & =\sum_{t=1}^{N} \log U_{t}, \quad \text { and } \\
\operatorname{CLL}(B \mid D) & =\sum_{t=1}^{N} \log U_{t}-\log \left(U_{t}+V_{t}\right)
\end{aligned}
$$

As mentioned in Section 2.1, an efficient scoring criterion must be decomposable. The LL score decomposes over the network structure. To better see why this is the case, substitute the expression for the joint probability distribution, in Equations (1)-(3), into the LL criterion, in Equation (9), to obtain:

$$
\operatorname{LL}(B \mid D)=\sum_{i=1}^{n} \sum_{j=1}^{q_{i}} \sum_{k=1}^{r_{i}} \sum_{c=1}^{s} N_{i j c k} \log \theta_{i j c k}+\sum_{c=1}^{s} N_{c} \log \theta_{c}
$$

where $N_{i j c k}$ is the number of instances in $D$, where $X_{i}$ takes its $k$-th value, its parents (excluding the class variable) take their $j$-th value and $C$ takes its $c$-th value, and $N_{c}$ is the number of instances where $C$ takes its $c$-th value.

Unfortunately, CLL does not decompose over the network structure, because $\log \left(U_{t}+V_{t}\right)$ cannot be expressed as a sum of local contributions. To achieve the decomposability of CLL, an approximation:

$$
\hat{f}\left(U_{t}, V_{t}\right)=\alpha \log U_{t}+\beta \log V_{t}+\gamma
$$

of the original function:

$$
f\left(U_{t}, V_{t}\right)=\log U_{t}-\log \left(U_{t}+V_{t}\right)
$$

was proposed in [8], where $\alpha, \beta$ and $\gamma$ are real numbers to be chosen, so as to minimize the approximation error. To determine suitable values of $\alpha, \beta$ and $\gamma$, uniformity assumptions about $U_{t}$ and $V_{t}$ were made. To this end, let $\Delta^{2}=\{(x, y): x+y \leq 1$ and $x, y \geq 0\}$ be the two-simplex set. As $U_{t}$ and $V_{t}$ are expected to become exponentially small as the number of attributes grows, it was assumed that

$$
U_{t}, V_{t} \leq p<\frac{1}{2}
$$

for some $0<p<\frac{1}{2}$. Combining this constraint with

$$
\left(U_{t}, V_{t}\right) \sim \operatorname{Uniform}\left(\Delta^{2}\right)
$$

yielded the following assumption:
Assumption 2.1 There exists a small positive $p<\frac{1}{2}$, such that:

$$
\left.\left(U_{t}, V_{t}\right) \sim \operatorname{Uniform}\left(\Delta^{2}\right)\right|_{U_{t}, V_{t} \leq p}=\operatorname{Uniform}([0, p] \times[0, p])
$$

In [8], it was shown that under Assumption 2.1, the values of $\alpha, \beta$ and $\gamma$ that minimize the mean square error (MSE) of $\hat{f}$ w.r.t. $f$ are given by:

$$
\alpha=\frac{\pi^{2}+6}{24}, \quad \beta=\frac{\pi^{2}-18}{24} \quad \text { and } \quad \gamma=\frac{\pi^{2}}{12 \ln (2)}-\left(2+\frac{\left(\pi^{2}-6\right) \log p}{12}\right)
$$

This resulted in a decomposable approximation for the CLL, called approximate CLL, defined as:

$$
\operatorname{aCLL}(B \mid D)=\sum_{c=0}^{1}\left(\alpha N_{c}+\beta N_{1-c}\right) \log \theta_{c}+\sum_{i=1}^{n} \sum_{j=1}^{q_{i}} \sum_{k=1}^{r_{i}} \sum_{c=0}^{1}\left(\alpha N_{i j c k}+\beta N_{i j(1-c) k}\right) \log \theta_{i j c k}+N \gamma
$$

This decomposable approximation has some desirable properties. It is unbiased, that is, the mean difference between $\hat{f}$ and $f$ is zero for all values of $p$. In addition, $\hat{f}$ is the approximation with the lowest variance amongst unbiased ones, leading to a minimum variance unbiased (MVU) approximation of $f$. Moreover, since the goal is to maximize $\operatorname{CLL}(B \mid D)$, the constant $\gamma$ from Equation (14) can be dropped, yielding an approximation that disregards the value, $p$ (used in Assumption 2.1). For this reason, $p$ needs not to be known to maximize aCLL. Despite these advantageous properties, the parameters that maximize aCLL resorted in an unknown manner. In addition, the aCLL score is not directly applied to multi-classification tasks, and no other stochastic assumptions rather than the uniformity of $U_{t}$ and $V_{t}$ were studied.

# 3. Extending the Approximation to CLL 

The shortcomings of the initial aCLL proposal make it natural to explore a variety of extensions. Specifically, in this section, we derive a general closed-form expression for aCLL grounding in regression theory. This yields a new scoring criterion for multi-classification tasks, with broader stochastic assumptions than the uniform one, while maintaining the desirable property of an MVU approximation to CLL. In addition, we also provide the parameters that maximize this new general form in the context of BNCs.

### 3.1. Generalizing aCLL to Multi-Classification Tasks

We now set out to consider multi-classification tasks under a generalization of Assumption 2.1. In this case, let

$$
U_{t, c_{t}}=P_{B}\left(y_{t}^{1}, \ldots, y_{t}^{n}, c_{t}\right)
$$

, so that the conditional probability, $P_{B}\left(c_{t} \mid y_{t}^{1}, \ldots, y_{t}^{n}\right)$, in Equation (8) becomes, now,

$$
P_{B}\left(c_{t} \mid y_{t}^{1}, \ldots, y_{t}^{n}\right)=\frac{U_{t, c_{t}}}{\sum_{c=1}^{s} U_{t, c}}
$$

where $U_{t, c}=P_{B}\left(y_{t}^{1}, \ldots, y_{t}^{n}, c\right)$, for all $1 \leq c \leq s$. Observe that the vectors, $\left(y_{t}^{1}, \ldots, y_{t}^{n}, c\right)$, for all $1 \leq c \leq s$ with $c \neq c_{t}$, called the complement samples, may or may not occur in $D$. Hence, for multi-classification tasks, the conditional log-likelihood in Equation (10) can be rewritten as:

$$
\operatorname{CLL}(B \mid D)=\sum_{t=1}^{N} \log U_{t, c_{t}}-\log \left(\sum_{c=1}^{s} U_{t, c}\right)
$$

In this case, the approximation, $\hat{f}$, in Equation (12) consists now in approximating:

$$
f\left(U_{t, 1}, \ldots, U_{t, s}\right)=\log U_{t, c_{t}}-\log \left(\sum_{c=1}^{s} U_{t, c}\right)
$$

by a function of the form:

$$
\hat{f}\left(U_{t, 1}, \ldots, U_{t, s}\right)=\alpha \log U_{t, c_{t}}+\sum_{c \neq c_{t}} \beta_{c} \log U_{t, c}+\gamma
$$

Notice that $\beta_{c_{t}}$ is not defined in Equation (15); hence, considering $\beta_{c_{t}}=\alpha-1$, the approximation in Equation (15) is equivalent to the following linear approximation:

$$
\begin{aligned}
-\log \left(\sum_{c=1}^{s} U_{t, c}\right) & =f\left(U_{t, 1}, \ldots, U_{t, s}\right)-\log U_{t, c_{t}} \\
& \approx \hat{f}\left(U_{t, 1}, \ldots, U_{t, s}\right)-\log U_{t, c_{t}} \\
& =(\alpha-1) \log U_{t, c_{t}}+\sum_{c \neq c_{t}} \beta_{c} \log U_{t, c}+\gamma \\
& =\sum_{c=1}^{s} \beta_{c} \log U_{t, c}+\gamma
\end{aligned}
$$

Therefore, we aim at minimizing the expected squared error for the approximation in Equation (16). We are able to achieve this if we assume that the joint distribution, $\left(U_{t, 1}, \ldots, U_{t, s}\right)$, is symmetric.

Assumption 3.1 For all permutations, $\left(\pi_{1}, \ldots, \pi_{s}\right)$, we have that $\left(U_{t, 1}, \ldots, U_{t, s}\right) \sim\left(U_{t, \pi_{1}}, \ldots, U_{t, \pi_{s}}\right)$.
Assumption 3.1 imposes that $U_{t, c}$ and $U_{t, c^{\prime}}$ are identically distributed, for all $1 \leq c, c^{\prime} \leq s$, that is, $U_{t, c} \sim U_{t, c^{\prime}}$. This is clearly much more general than the symmetric uniformity imposed in Assumption 2.1 for binary classification.

Under Assumption 3.1, the approximation in Equation (16) is such that $\beta_{1}=\cdots=\beta_{s}$. Let $\beta$ denote the common value, and consider that:

$$
A=-\log \left(\sum_{c=1}^{s} U_{t, c}\right) \quad \text { and } \quad B=\sum_{c=1}^{s} \log U_{t, c}
$$

Our goal is to find $\beta$ and $\gamma$ that minimize the following expected value:

$$
E\left[(A-(\beta B+\gamma))^{2}\right]
$$

Let $\sigma_{A}^{2}$ and $\sigma_{B}^{2}$ denote the variance of $A$ and $B$, respectively, and let $\sigma_{A B}$ denote the covariance between $A$ and $B$. Standard regression allows us to derive the next result [22].

Theorem 3.2 Assume that $\sigma_{B}^{2}>0$. The unique values of $\beta$ and $\gamma$ that minimize Equation (18) are given by:

$$
\beta=\frac{\sigma_{A B}}{\sigma_{B}^{2}} \quad \text { and } \quad \gamma=E[A-\beta B]
$$

Moreover, it follows that:

$$
\begin{aligned}
E[A-(\beta B+\gamma)] & =0, \quad \text { and } \\
E\left[(A-(\beta B+\gamma))^{2}\right] & =\sigma_{A}^{2}-\frac{\sigma_{A B}^{2}}{\sigma_{B}^{2}}
\end{aligned}
$$

From Equation (20), we conclude that the approximation in Equation (16) is unbiased, and since it minimizes Equation (18), it is an MVU approximation. As in [8], we are adopting estimation terminology for approximations. In this case, by taking $\hat{A}=(\beta B+\gamma)$, Equation (18) is precisely $E\left[(A-\hat{A})^{2}\right]=\operatorname{MSE}(\hat{A})$, where MSE is the mean squared error of the approximation/estimation. The MSE coincides with the variance when the approximation/estimator is unbiased, and so, the approximation in Theorem 3.2 is MVU. In addition, the standard error of the approximation in Equation (16) is given by the square root of Equation (21).

The previous result allows us to generalize the aCLL scoring criterion for multi-classification tasks. The values of $\beta$ and $\gamma$ needed by the approximation in Equation(16) are given by Equation(19). This results in a decomposable approximation of CLL and a generalization of aCLL for multi-classification as:

$$
\operatorname{aCLL}(B \mid D)=\sum_{t=1}^{N}\left(\log U_{t, c_{t}}+\sum_{c=1}^{s} \beta \log U_{t, c}+\gamma\right)
$$

# 3.1.1. Symmetric Uniform Assumption for Multi-Classification Tasks 

Herein, we analyze aCLL under the symmetric uniform assumption. We start by providing a general explanation on why aCLL approximation is robust to the choice of $p$, which was already noticed for the binary case. In addition, we confirm that the analysis in Section 2.3 for the binary case coincides with that given in Section 3.1 when $s=2$. Finally, we provide the constants $\beta$ and $\gamma$ for ternary-classification tasks, under the symmetric uniform assumption of $\left(U_{t, 1}, U_{t, 2}, U_{t, 3}\right)$.

Assumption 3.3 Let $\left(U_{t, 1}, \ldots, U_{t, s}\right) \sim \operatorname{Uniform}\left([0, p]^{s}\right)$.
Start by noticing that under Assumption 3.3, changes in $p$ correspond to multiplying the random vector, $\left(U_{t, 1}, \ldots, U_{t, s}\right)$, by a scale factor. Indeed, if each random variable is multiplied by a common scale factor, $\kappa$, it results in the addition of constant values to $A$ and $B$. To this end, note that:

$$
-\log \left(\sum_{c=1}^{s} \kappa U_{t, c}\right)=-\log \left(\kappa \sum_{c=1}^{s} U_{t, c}\right)=-\log (\kappa)-\log \left(\sum_{c=1}^{s} U_{t, c}\right)
$$

and:

$$
\sum_{c=1}^{s} \log \left(\kappa U_{t, c}\right)=\sum_{c=1}^{s} \log \kappa+\log U_{t, c}=s \log (\kappa)+\sum_{c=1}^{s} \log U_{t, c}
$$

Since these additive terms have no effect on variances and covariances, it follows that $\beta$ is not affected with changes in $p$. Therefore, the choice of $p$ is irrelevant for maximizing aCLL when a uniform distribution is chosen. Moreover, it is enough to obtain the parameter, $\beta$, as by Equation (22) aCLL maximization is insensitive to the constant factor, $\gamma$.

We also stress that for the binary case, with $\left(U_{t, 1}, U_{t, 2}\right) \sim \operatorname{Uniform}\left([0, p]^{2}\right)$, the values of $\beta$ and $\gamma$, given by Equation (19), with $\alpha=1+\beta$, coincide with those given by Equation (13).

Finally, by using Mathematica 9.0, we were able to obtain an analytical expression of $\beta$ for ternary classification tasks.

Example 3.4 For the ternary case where $\left(U_{t, 1}, U_{t, 2}, U_{t, 3}\right) \sim \operatorname{Uniform}\left([0, p]^{3}\right)$, the constant, $\beta$, that minimizes Equation (18) is

$$
\frac{1}{36}\left(-15 \pi^{2}-2\left(-11+9 \ln (3)-12 \ln (2)+60 \ln ^{2}(2)+72 L i_{2}(-2)+24 L i_{2}(1 / 4)\right)\right)
$$

where $\operatorname{Li}_{n}(z)$ is the polylogarithm function of order $n$.

# 3.1.2. Symmetric Dirichlet Assumption for Multi-Classification Tasks 

In this section, we provide an alternative assumption, which will lead us to a very good approximation of CLL. Instead of a symmetric uniform distribution, we assume that the random vector, $\left(U_{t, 1}, \ldots, U_{t, s}, W_{t}\right)$, where $W_{t}=1-\sum_{c=1}^{s} U_{t, c}$, follows a symmetric Dirichlet distribution. In the following, we omit the random variable, $W_{t}$, from the vector, as it is completely defined given $U_{t, 1}, \ldots, U_{t, s}$. The use of the Dirichlet distribution is attributed to the fact that it is a conjugate family of the distribution for a multinomial sample; this ties perfectly with the fact that data is assumed to be a multinomial sample when learning BNCs [23].

In order to take profit of Theorem 3.2, we consider the following symmetric Dirichlet assumption:
Assumption 3.5 Let $\left(U_{t, 1}, \ldots, U_{t, s}\right) \sim \operatorname{Dir}\left(a_{1}, \ldots, a_{s}, b\right)$, where $a_{c}=a$, for all $c=1, \ldots, s$.
Assumption 3.5 implies that the tuple, $\left(y_{t}^{1}, \ldots, y_{t}^{n}, c\right)$, occurs in the data exactly $a-1$ times, for all $c=1, \ldots, s$. Moreover, there are $b-1$ instances in the data different from $\left(y_{t}^{1}, \ldots, y_{t}^{n}, c\right)$, for all $c=1, \ldots, s$. Given a dataset of size $N$, it is reasonable to assume $a=1$ and $b=N$. Indeed, probabilities $U_{t, c}$ are expected to be very low, becoming exponentially smaller as the number of attributes, $n$, grows; therefore, it is reasonable to assume that $\left(y_{t}^{1}, \ldots, y_{t}^{n}, c_{t}\right)$ occurs only once in the data and that its complement instances, $\left(y_{t}^{1}, \ldots, y_{t}^{n}, c\right)$, with $c \neq c_{t}$, do not even occur in the data. Thus, by starting with a non-informative prior, that is, with distribution $\operatorname{Dir}(1, \ldots, 1,1)$ over the $s$-simplex and, then, conditioning this distribution over the multinomial observation of the data of size $N$, we obtain the prior:

$$
\left(U_{t, 1}, \ldots, U_{t, s}\right) \sim \operatorname{Dir}\left(a_{1}, \ldots, a_{s}, N\right)
$$

where $a_{c}=1$ for $c \neq c_{t}$ and $a_{c_{t}}=2$. However, such a distribution is asymmetric, and it is not in the conditions of Theorem 3.2. We address this problem by considering the symmetric distribution:

$$
\left(U_{t, 1}, \ldots, U_{t, s}\right) \sim \operatorname{Dir}(1, \ldots, 1, N)
$$

which is very close to the distribution in Equation (23). We stress that the goal of any assumption is to find good approximations for the constants, $\beta$ and $\gamma$, and that the conditions upon which such approximations were performed need not hold true exactly.

### 3.1.3. Estimating Parameters $\beta$ and $\gamma$

We now focus our attention in finding, numerically, the values of $\beta$ and $\gamma$, via a Monte-Carlo method. To this end, several random vectors, $\left(u_{1}, \ldots, u_{s}\right)$, are generated with the envisaged Dirichlet distribution in order to define a set, $\mathcal{S}$, of pairs $(\mathrm{B}, \mathrm{A})$ given by $\mathrm{A}=-\log \left(\sum_{c=1}^{s} u_{c}\right)$ and $\mathrm{B}=\sum_{c=1}^{s} \log \left(u_{c}\right)$.

In this way, we are sampling the random variables, $A$ and $B$, as defined in Equation (17). Given $\mathcal{S}$, it is straightforward to find the best linear fit of the form $\mathrm{A}=\hat{\beta} \mathrm{B}+\hat{\gamma}$ and moreover, by the strong law of large numbers, $\hat{\beta}$ and $\hat{\gamma}$, converge in probability to $\beta$ and $\gamma$, respectively, as the set, $\mathcal{S}$, grows. The general method is described in Algorithm 1.

```
Algorithm 1 General Monte-Carlo method to estimate \(\beta\) and \(\gamma\)
Input: number of samples, \(m\).
    For \(i=1\) to \(m\);
    For \(c=1\) to \(s\);
    Generate a sample, \(u_{c}=\operatorname{CDF}_{A}^{-1}(\operatorname{Uniform}([0,1]))\), where \(P(X=x)=P\left(U_{t, c}=x \mid U_{t, 1}=u_{1}, \ldots, U_{t, c-1}=u_{c-1}\right)\).
    Add the point \(\left(\sum_{c=1}^{s} \log \left(u_{c}\right),-\log \left(\sum_{c=1}^{s} u_{c}\right)\right)\) to \(\mathcal{S}\).
    Perform simple linear regression to \(\mathcal{S}\), obtaining \(\mathrm{A}=\hat{\beta} \mathrm{B}+\hat{\gamma}\).
```

Algorithm 1 works for any distribution (even for non-symmetric ones). The idea in Step 3 is to use the standard simulation technique of using the cumulative distribution function (CDF) of the univariate marginal for $U_{t, 1}$ to generate a sample for the first component, $u_{1}$, of the vector and, afterwards, apply the CDF of the univariate conditional distributions, to generate samples for the remaining components, $u_{2}, \ldots, u_{s}$.

We used Algorithm 1 to cross-check the values of $\beta$ and $\gamma$ for the case of a symmetric uniform distribution obtained analytically in Equation (13) and Example 3.4, for binary and ternary classification tasks, respectively.

Example 3.6 For binary classification under Assumption 3.3 and for $m=20,000$, we obtained an exact approximation of the analytical expression in Equation (13) up to four decimal places. For ternary classification, we required 80,000 samples to achieve the same precision for the analytical expression given in Example 3.4. We estimated the values of $\beta$ and $\gamma$ to be in this case $\hat{\beta}=-0.198873$ and $\hat{\gamma}=1.85116$.

Although Algorithm 1 works well for Dirichlet distributions, we note that there are simpler and more efficient ways to generate samples for a distribution, $\operatorname{Dir}\left(a_{1}, \ldots, a_{s}, a_{s+1}\right)$. Consider $s+1$ independent Gamma random variables, $Y_{i} \sim \operatorname{Gamma}\left(a_{i}, 1\right)$, for $i=1, \ldots, s+1$, and let $Y_{0}=\sum_{i=1}^{s+1} Y_{i}$. Then, it is well known that $\left(Y_{1} / Y_{0}, \ldots, Y_{s} / Y_{0}\right) \sim \operatorname{Dir}\left(a_{1}, \ldots, a_{s}, a_{s+1}\right)$. Clearly, it is much more simple to sample $s+1$ independent random variables than sampling marginal and conditional distributions. The modified algorithm is presented in Algorithm 2.


Next, we illustrate the use of the Algorithm 2 in the conditions discussed in Equation (24).
Example 3.7 For binary classification under Assumption 3.5 and with $a_{1}=a_{2}=1, b=1,000$ and $m=100,000$, the estimated values for $\beta$ and $\gamma$ are $\hat{\beta}=-0.39291$ and $\hat{\gamma}=0.61698$, respectively. For ternary classification, and under the same assumptions, the estimated values for $\beta$ and $\gamma$ are $\hat{\beta}=-0.239266$ and $\hat{\gamma}=0.6085$, respectively.

# 3.2. Parameter Maximization for aCLL 

The main goal for devising an approximation to CLL is to obtain an expression that decomposes over the BNC structure. By plugging in the probability expansion of Equation (3) in the general aCLL scoring criterion for multi-classification given in Equation (22), we obtain:

$$
\operatorname{aCLL}(B \mid D)=\sum_{c=1}^{s}\left(\alpha N_{c}+\beta \sum_{c^{\prime} \neq c} N_{c^{\prime}}\right) \log \left(\theta_{c}\right)+\sum_{i=1}^{n} \sum_{j=1}^{q_{i}^{s}} \sum_{k=1}^{r_{i}} \sum_{c=1}^{s}\left(\alpha N_{i j c k}+\beta \sum_{c^{\prime} \neq c} N_{i j c^{\prime} k}\right) \log \left(\theta_{i j c k}\right)+N \gamma
$$

where $\alpha=1+\beta$. This score is decomposable, as it allows one to compute, independently, the contribution of each node (and its parents) to the global score. However, the values of the parameters, $\theta_{i j c k}$ and $\theta_{c}$, that maximize the aCLL score in Equation (25) remain unknown. This problem was left open in [8], and a further approximation was required to obtain optimal BNC parameters.

We are able to obtain the optimal values of $\theta_{i j c k}$ and $\theta_{c}$ by assuming that they are lower-bounded. This lower bound follows naturally by adopting pseudo-counts, commonly used in BNCs to smooth observed frequencies with Dirichlet priors and increase the quality of the classifier [2]. Pseudo-counts intend to impose the common sense assumption that there are no situations with the probability of zero. Indeed, it is a common mistake to assign a probability of zero to an event that is extremely unlikely, but not impossible [24].

Theorem 3.8 Let $N^{\prime}>0$ be the number of pseudo-counts. The parameters, $\theta_{i j c k}$, that maximize the aCLL scoring criterion in Equation (25) are given by:

$$
\theta_{i j c k}=\frac{N_{i j+c k}}{N_{i j+c}} \text { and } \theta_{c}=\frac{N_{+c}}{N_{+}}
$$

where:

$$
\begin{gathered}
N_{i j+c k}= \begin{cases}\alpha N_{i j c k}+\beta \sum_{c^{\prime} \neq c} N_{i j c^{\prime} k} & \text { if } \alpha N_{i j c k}+\beta \sum_{c^{\prime} \neq c} N_{i j c^{\prime} k} \geq N^{\prime} \\
N^{\prime} & \text { otherwise }\end{cases} \\
N_{+c}= \begin{cases}\alpha N_{c}+\beta \sum_{c^{\prime} \neq c} N_{c^{\prime}} & \text { if } \alpha N_{c}+\beta \sum_{c^{\prime} \neq c} N_{c^{\prime}} \geq N^{\prime} \\
N^{\prime} & \text { otherwise }\end{cases} \\
N_{i j+c}=\sum_{k=1}^{r_{i}} N_{i j+c k} \text { and } N_{+}=\sum_{c=1}^{s} N_{+c}
\end{gathered}
$$

constrained to $\theta_{i j c k} \geq \frac{N^{\prime}}{N_{i j+c}}$ and $\theta_{c} \geq \frac{N^{\prime}}{N_{+}}$, for all $i, j, c$ and $k$.
Proof: We only show the maximization for the parameters, $\theta_{i j c k}$, as the maximization for $\theta_{c}$ is similar. Then, by taking the summand of Equation (25), which depends only on the parameters, $\theta_{i j c k}$, we have:

$$
\begin{aligned}
& \sum_{i=1}^{n} \sum_{j=1}^{q_{i}^{*}} \sum_{k=1}^{r_{i}} \sum_{c=1}^{s}\left(\alpha N_{i j c k}+\beta \sum_{c^{\prime} \neq c} N_{i j c^{\prime} k}\right) \log \left(\theta_{i j c k}\right) \\
& =\sum_{i=1}^{n} \sum_{j=1}^{q_{i}^{*}} \sum_{k=1}^{r_{i}} \sum_{c=1}^{s} \underbrace{N_{i j+c k} \log \left(\theta_{i j c k}\right)}_{\text {(a) }}+\underbrace{\left(\left(\alpha N_{i j c k}+\beta \sum_{c^{\prime} \neq c} N_{i j c^{\prime} k}\right)-N_{i j+c k}\right) \log \left(\theta_{i j c k}\right)}_{\text {(b) }}
\end{aligned}
$$

Observe that if $N_{i j+c k} \geq N^{\prime}$, then $N_{i j+c k}=\alpha N_{i j c k}+\beta \sum_{c^{\prime} \neq c} N_{i j c^{\prime} k}$. Thus, summand (b) in Equation (27) is only different from zero when $\alpha N_{i j+c k}+\beta \sum_{c^{\prime} \neq c} N_{i j c^{\prime} k}<N^{\prime}$. In this case, $N_{i j+c k}=N^{\prime}$, which implies that $\left(\alpha N_{i j c k}+\beta \sum_{c^{\prime} \neq c} N_{i j c^{\prime} k}\right)-N^{\prime}<0$. Therefore, the value for $\theta_{i j c k}$ that maximizes summand (b) is the minimal value for $\theta_{i j c k}$, that is, $\frac{N^{\prime}}{N_{i j+c}}=\frac{N_{i j+c k}}{N_{i j+c}}$. Finally, by Gibb's inequality, we derive that the distribution for $\theta_{i j c k}$ that maximizes summand (a) in Equation (27) is $\theta_{i j c k}=\frac{N_{i j+c k}}{N_{i j+c}}$. Since the maximality of the summands, (a) and (b), is obtained with the same values for $\theta_{i j c k}$, we have that the values for $\theta_{i j c k}$ that maximize Equation (25) are given by: $\theta_{i j c k}=\frac{N_{i j+c k}}{N_{i j+c}}$.

The role of the pseudo-counts is to guarantee that the values, $N_{i j+c k}$ or $N_{+c}$, cannot be smaller than $N^{\prime}$. By plugging in the parameters given in Theorem 3.8 in Equation (26) into the aCLL criterion in Equation (25), we obtain:

$$
\tilde{a C L}(G \mid D)=\sum_{c=1}^{s}\left(\alpha N_{c}+\beta \sum_{c^{\prime} \neq c} N_{c^{\prime}}\right) \log \left(\frac{N_{+c}}{N_{+}}\right)+\sum_{i=1}^{n} \sum_{j=1}^{q_{i}^{*}} \sum_{k=1}^{r_{i}} \sum_{c=1}^{s}\left(\alpha N_{i j c k}+\beta \sum_{c^{\prime} \neq c} N_{i j c^{\prime} k}\right) \log \left(\frac{N_{i j+c k}}{N_{i j+c}}\right)+N_{7}
$$

The notation using $G$ as an argument instead of $B$ emphasizes that once the parameters, $\Theta$, are decided upon, the criterion is a function of the network structure, $G$, only.

Finally, we show that aCLLobserved frequency estimates (OFE) (aCLL) is not scoreequivalent. Two BNCs are said to be equivalent if they can represent precisely the same set of distributions. Verma and Pearl [25] showed that this is equivalent to checking if the underlying DAG of the two BNCs have the same skeleton and the same $v$-structures. A score-equivalent scoring criterion is one that assigns the same score to equivalent BNC structures $[12,14,26]$.

Theorem 3.9 The àCLL scoring criterion is decomposable and non-score equivalent.
Proof: Decomposability follows directly from the definition in Equation (28). Concerning non-score equivalence, it suffices to provide a counter-example, where two equivalent structures do not score the same. To this purpose, consider a BNC with two attributes, $(n=2)$ and $D=$ $\{(0,0,1),(0,1,1),(1,1,0),(1,1,1)\}$, as the training set. The structures, $G \equiv X_{1} \rightarrow X_{2}$ and $H \equiv$ $X_{2} \rightarrow X_{1}$ (we omitted the node representing the class variable, C , pointing to $X_{1}$ and $X_{2}$ ), for $B$ are equivalent, but it is straightforward to check that $\hat{\mathrm{a}} \operatorname{CLL}(G \mid D) \neq \hat{\mathrm{a}} \operatorname{CLL}(H \mid D)$.

Interesting scoring criteria in the literature are decomposable, since it is infeasible to learn undecomposable scores. On the other hand, both score-equivalent and non-score-equivalent decomposable scores can be learned efficiently, although the algorithms to learn them are different. In general, the score-equivalence property does not seem to be important, as non-score-equivalent scores typically perform better than score-equivalent ones $[12,14]$.

# 4. Information-Theoretic Interpretation of the Conditional Log-Likelihood 

Herein, we provide some insights about information-theoretic concepts and how they relate with the CLL. These results are well known in the literature [2,27]; nonetheless, they are presented here in detail to provide a clear understanding that approximating the CLL is equivalent to approximating the conditional relative entropy. We refer the interested reader to the textbook of Cover and Thomas [28] for further details.

The relative entropy is a measure of the distance between two distributions. The relative entropy, also known as Kullback-Leibler divergence, between two probability mass functions, $p(x)$ and $q(x)$, for a random variable, $X$, is defined as:

$$
D_{K L}(p(x) \| q(x))=\sum_{x} p(x) \log \frac{p(x)}{q(x)}
$$

This quantity is always non-negative and is zero if and only if $p=q$. Although interpreted as a distance between distributions, it is not a true distance, as it is not symmetric and it does not satisfy the triangle inequality. However, it is a measure of the inefficiency of assuming that the distribution is $q$ when the true distribution is $p$. In terms of encoding, this means that if instead of using the true distribution, $p$, to encode $X$, we used the code for a distribution, $q$; we would need $H_{p}(X)+D_{K L}(p(x) \| q(x))$ bits on the average to describe $X$. In addition, the conditional relative entropy is the average of the relative entropies between the conditional probability mass functions, $p(y \mid x)$ and $q(y \mid x)$, averaged over the probability mass function, $p(x)$, that is:

$$
D_{K L}(p(y \mid x) \| q(y \mid x))=E_{X}\left[D_{K L}(p(y \mid X) \| q(y \mid X)\right]=\sum_{x} p(x) \sum_{y} p(y \mid x) \log \frac{p(y \mid x)}{q(y \mid x)}
$$

The relationship between log-likelihood and entropy is well established. Lewis had already shown that maximizing the log-likelihood is equivalent to minimizing the entropy [27]. In addition, Friedman et al. [2] came into the same conclusion and related it with the relative entropy. They concluded that minimizing the Kullback-Leibler divergence between the distribution, $\hat{P}_{D}$, induced by the

observed frequency estimates (OFE) and the distribution, $P_{B}$, given by the Bayesian network classifier, $B$, is equivalent to minimizing the entropy, $H_{P_{B}}$, and, thus, maximizing $\operatorname{LL}(B \mid D)$.

Friedman et al. [2] also hinted that maximizing the conditional log-likelihood is equivalent to minimizing the conditional relative entropy. Assuming that $\mathbf{A}=\mathbf{X} \backslash\{C\}$, and for the case of BNCs, this fact can be taken from:

$$
\begin{aligned}
\operatorname{CLL}(B \mid D)= & \sum_{t=1}^{N} \log P_{B}\left(c_{t} \mid \mathbf{y}_{t}^{-}\right) \\
= & N \sum_{\mathbf{y}_{t}^{-}} \sum_{c_{t}} \hat{P}_{D}\left(\mathbf{y}_{t}^{-}, c_{t}\right) \log P_{B}\left(c_{t} \mid \mathbf{y}_{t}^{-}\right) \\
= & N \sum_{\mathbf{y}_{t}^{-}} \sum_{c_{t}} \hat{P}_{D}\left(\mathbf{y}_{t}^{-}, c_{t}\right) \log P_{B}\left(c_{t} \mid \mathbf{y}_{t}^{-}\right)+N H_{\hat{P}_{D}}(C \mid \mathbf{A})-N H_{\hat{P}_{D}}(C \mid \mathbf{A}) \\
= & N \sum_{\mathbf{y}_{t}^{-}} \sum_{c_{t}} \hat{P}_{D}\left(\mathbf{y}_{t}^{-}, c_{t}\right) \log P_{B}\left(c_{t} \mid \mathbf{y}_{t}^{-}\right)-N \sum_{\mathbf{y}_{t}^{-}} \sum_{c_{t}} P_{\hat{P}_{D}}\left(\mathbf{y}_{t}^{-}, c_{t}\right) \log P_{\hat{P}_{D}}\left(c_{t} \mid \mathbf{y}_{t}^{-}\right) \\
& -N H_{\hat{P}_{D}}(C \mid \mathbf{A}) \\
= & -N \sum_{\mathbf{y}_{t}^{-}} \sum_{c_{t}} \hat{P}_{D}\left(\mathbf{y}_{t}^{-}, c_{t}\right) \log \frac{\hat{P}_{D}\left(c_{t} \mid \mathbf{y}_{t}^{-}\right)}{P_{B}\left(c_{t} \mid \mathbf{y}_{t}^{-}\right)}-N H_{\hat{P}_{D}}(C \mid \mathbf{A}) \\
= & -N \sum_{\mathbf{y}_{t}^{-}} \sum_{c_{t}} \hat{P}_{D}\left(\mathbf{y}_{t}^{-}\right) \hat{P}_{D}\left(c_{t} \mid \mathbf{y}_{t}^{-}\right) \log \frac{\hat{P}_{D}\left(c_{t} \mid \mathbf{y}_{t}^{-}\right)}{P_{B}\left(c_{t} \mid \mathbf{y}_{t}^{-}\right)}-N H_{\hat{P}_{D}}(C \mid \mathbf{A}) \\
= & -N \sum_{\mathbf{y}_{t}^{-}} \hat{P}_{D}\left(\mathbf{y}_{t}^{-}\right) \sum_{c_{t}} \hat{P}_{D}\left(c_{t} \mid \mathbf{y}_{t}^{-}\right) \log \frac{\hat{P}_{D}\left(c_{t} \mid \mathbf{y}_{t}^{-}\right)}{P_{B}\left(c_{t} \mid \mathbf{y}_{t}^{-}\right)}-N H_{\hat{P}_{D}}(C \mid \mathbf{A}) \\
= & -N D_{K L}\left(\hat{P}_{D}(C \mid \mathbf{A}) \| P_{B}(C \mid \mathbf{A})\right)-N H_{\hat{P}_{D}}(C \mid \mathbf{A})
\end{aligned}
$$

Indeed, the main goal in classification is to learn the model that best approximates the conditional probability, induced by the OFE, of $C$, given $\mathbf{A}$. It follows from Equation (29) that by maximizing $\operatorname{CLL}(B \mid D)$, such a goal is achieved, since we are minimizing $D_{K L}\left(\hat{P}_{D}(C \mid \mathbf{A}) \| P_{B}(C \mid \mathbf{A})\right)$, which is the conditional relative entropy between the conditional distribution induced by the OFE and the conditional distribution given by the target model, $B$.

In conclusion, since aCLL is an MVU approximation of CLL, by finding the model, $B$, that maximizes $\operatorname{aCLL}(B \mid D)$, we expect to minimize the conditional relative entropy between $\hat{P}_{D}(C \mid \mathbf{A})$ and $P_{B}(C \mid \mathbf{A})$.

# 5. Experimental Results 

We implemented the TAN learning algorithm (c.f. Section 2.1), endowed with the aCLL scoring criterion, in Mathematica 7.0 on top of the Combinatorica package [29]. For the experimental results, we considered optimal TAN structures learned with LL and aCLL under both (symmetric) uniform and Dirichlet assumptions. The main goal of this empirical assessment is to compare the CLL attained with these optimal structures, in order to unravel which one better approximates CLL. To this end, only the scoring criteria vary, and the searching procedure is fixed to yield an optimal TAN structure; this ensures that only the choice of the scoring criterion affects the learned model. To avoid overfitting, which arises

naturally when complex structures are searched, we improved the performance of all BNCs by smoothing parameter estimates according to a Dirichlet prior [13]. The smoothing parameter, $N^{\prime}$, was set to 5, as suggested in [2].

We performed our evaluation on 89 benchmark datasets used by Barash et al. [9]. These datasets constitute biologically validated data retrieved from the TRANSFACdatabase [30] for binary classification tasks. The aCLL constants considered for the uniform assumption are those given in Equation (13). The constants considered under the Dirichlet assumption are those given in Example 3.7, since all the datasets have a size around 1,000 .

The CLL of the optimal TAN learned by each scoring criterion was computed, and it is depicted in Figure 1. From the figure, it is clear that the scoring criterion that obtained the highest CLL was aCLL under $\operatorname{Dir}(1,1,1000)$, followed by aCLL under $\operatorname{Unif}\left([0, p]^{2}\right)$. We numerically computed the standard relative error of the approximation under the Dirichlet assumption and obtained $13.92 \%$, which is half of the relative error for the uniform case [8]. For this reason, we expect aCLL under Dirichlet to be more stable than under the uniform assumption. To evaluate the statistical significance of these results, we used Wilcoxon signed-rank tests. This test is applicable when paired scoring differences, along the datasets, are independent and not necessarily normally distributed [31]. Results are presented in Table 1.

Figure 1. Conditional log-likelihood (CLL) score achieved by optimal tree-augmented naive (TAN) structures with different scoring criteria.
![img-0.jpeg](img-0.jpeg)

Table 1. Wilcoxon signed-rank tests for the CLL score obtained by optimal TANs in binary classification tasks.


Each entry of the table gives the $z$-test and $p$-value of the significance test for the corresponding pairs of BNCs. The arrow points to the superior scoring criterion, in terms of higher CLL.

From Table 1, it is clear that aCLL is significantly better than LL for obtaining a model with higher CLL. In addition, the Dirichlet assumption is more suitable than the uniform one for learning BNCs.

To illustrate the usage for multi-classification tasks, we applied our method for ternary classification. For that, we used the same 89 datasets as for the binary classification to create synthetic data for ternary classification tasks. We added to each dataset, $i$, a third class that corresponded to a class of the dataset, $i+1$. The aCLL constants considered for the uniform and Dirichlet assumptions are those given in Examples 3.4 and 3.7, respectively, since all the datasets have a size around 1,000 .

To compute our scoring, we also considered the number of pseudo-counts, $N^{\prime}=5$, and, similarly to the binary case, we performed a Wilcoxon signed-rank test to evaluate the statistical significance of the CLL computed by each scoring criterion. The results are presented in Table 2.

Table 2. Wilcoxon signed-rank tests for the CLL score obtained by optimal TANs in ternary classification tasks.


From Table 2, it is clear that aCLL also outperforms LL in ternary classification for obtaining a model with higher CLL. For the ternary case, the uniform assumption for learning BNCs outperformed the Dirichlet assumption.

# 6. Conclusions 

In this work, we explored three major shortcomings of the initial proposal of the aCLL scoring criterion [8]: (i) it addressed only binary-classification tasks; (ii) it assumed only a uniform distribution over the parameters; (iii) in the context of discriminative learning of BNCs, it did not provide the optimal parameters that maximize it. The effort of exploring the aforementioned limitations culminated with the proposal of a non-trivial extension of aCLL for multi-classification tasks under diverse stochastic assumptions. Whenever possible, the approximation constants were computed analytically; this included binary and ternary classification tasks under a symmetric uniform assumption. In addition, a Monte-Carlo method was proposed to compute the constants required for the approximation under a symmetric Dirichlet assumption. In the context of discriminative learning of BNCs, we showed that the extended score is decomposable over the BNC structure and provided the parameters that maximize it. This decomposition allows score-based learning procedures to be employed locally, making full (structure and parameters) discriminative learning of BNCs very efficient. Such discriminative learning is equivalent to minimizing the conditional relative entropy between the conditional distribution of the class given the attributes induced by the OFE and the one given by the learned discriminative model.

The merits of the devised scoring criteria under two different assumptions were evaluated in real biological data. These assumptions adopted a symmetrically uniform and a symmetric Dirichlet distribution over the parameters. Optimal discriminative models learned with aCLL both with symmetrically uniform and symmetric Dirichlet assumptions, showed higher CLL than those learned generatively with LL. Moreover, among the proposed criteria, the symmetric Dirichlet assumption also was shown to approximate CLL better than the symmetrically uniform one. This was expected, as the Dirichlet is a conjugate distribution for a multinomial sample, which ties perfectly with the fact that data is assumed to be a multinomial sample when learning BNCs.

Directions for future work include extending aCLL to unsupervised learning and to deal with missing data.

## Acknowledgments

This work was partially supported by Fundação para a Ciência e Tecnologia (FCT), under grant, PEstOE/EEI/LA0008/2013, and by the projects, NEUROCLINOMICS (PTDC/EIA-EIA/111239/2009), ComFormCrypt (PTDC/EIA-CCO/113033/2009) and InteleGen (PTDC/DTP-FTO/1747/2012), also funded by FCT.

## Conflict of Interest

The authors declare no conflict of interest.
