# Learning Gaussian Networks 

Dan Geiger<br>geiger02@gmail.com<br>David Heckerman<br>heckerma@hotmail.com

July 1994, Revised May 2021


#### Abstract

We describe scoring metrics for learning Bayesian networks from a combination of user knowledge and statistical data. Previous work has concentrated on metrics for domains containing only discrete variables, under the assumption that data represents a multinomial sample. In this paper, we extend this work, developing scoring metrics for domains containing only continuous variables under the assumption that continuous data is sampled from a multivariate normal distribution. Our work extends traditional statistical approaches for identifying vanishing regression coefficients in that we identify two important assumptions, called event equivalence and parameter modularity, that when combined allow the construction of prior distributions for multivariate normal parameters from a single prior Bayesian network specified by a user.


Corrections to the original text in red are taken from the 2021 update of J. Kuipers, G. Moffa, and D. Heckerman, Addendum on the scoring of Gaussian directed acyclic graphical models. Annals of Statistics 42, 1689-1691, Aug 2014 (arXiv:1402.6863). Other updates to the original are in blue.

## 1 Introduction

Several researchers have examined methods for learning Bayesian networks from data, including Cooper and Herskovits (1991,1992), Buntine (1991), Spiegelhalter et al. (1993), and Heckerman et al. (1994) (herein referred to as CH, Buntine, SDLC, and HGC, respectively). These methods all have the same basic components: a scoring metric and a search procedure. The metric computes a score that is proportional to the posterior probability of a network structure, given data and a user's prior knowledge. The search procedure generates networks for evaluation by the scoring metric. These methods use the two components to identify a network or set of networks with high relative posterior probabilities, and these networks are then used to predict future events.

Previous work has concentrated on domains containing only discrete variables, under the assumption that data is sampled from a multivariate discrete distribution. In this paper, we develop metrics for domains containing only continuous variables, under the assumption that continuous data is sampled from a multivariate normal (Gaussian) distribution. Previously, when working with continuous variables, the standard solution had been to transform each such variable $x_{i}$ to a discrete one by splitting its domain into several mutually exclusive and exhaustive regions. Our metrics eliminate the need for this transformation. In addition, our metrics have the advantage that they use the low polynomial dimentionality of the parameter space of a mulitivariate normal distribution, whereas their discrete counterparts often require a parameter space that is exponential in the number of domain variables.

Our work can be viewed as an extension of traditional statistical approaches for identifying vanishing regression coefficients, such as those described in DeGroot (1970, Chapter 11). In particular, we translate two assumptions that we identified in HGC for domains containing only discrete variables, called parameter modularity and event equivalence, to domains containing continuous variables. The assumption of parameter modularity, addresses the relationship among prior distributions of parameters for different Bayesian-network structures. The property of event equivalence says that two Bayesian-network structures that represent the same set of independence assertions should correspond to the same event and thus receive the same score. We show that, when combined, these assumptions allow the construction of reasonable prior distributions for multivariate normal parameters from a single prior Bayesian network specified by a user.

Our identification of event equivalence arises from a subtle distinction between two types of Bayesian networks. The first type, called belief networks, represents only assertions of conditional independence and dependence. The second type, called causal networks, represents assertions of cause and effect as well as assertions of independence and dependence. In this paper, we argue that metrics for belief networks should satisfy event equivalence, whereas metrics for causal networks need not.

Our score-equivalent metrics for belief networks are similar to the metrics described by Dawid and Lauritzen (1993), except that our metrics score directed networks, whereas their metrics score undirected networks. In this paper, we concentrate on directed models rather than on undirected models, because we believe that users find the former easier to build and interpret.

We note that much of the mathematics involved in our derivations is borrowed from DeGroot's book, "Optimal Statistical Decisions," (1970).

# 2 Gaussian Belief Networks 

Throughout this discussion, we consider a domain $\vec{x}$ of $n$ continuous variables $x_{1}, \ldots, x_{n}$. We use $\rho(\vec{x} \mid \xi)$ to denote the joint probability density function (pdf) over $\vec{x}$ of a person with background knowledge $\xi$. We use $p(e \mid \xi)$ to denote the probability of a discrete event $e$.

A belief network for $\vec{x}$ represents a joint pdf over $\vec{x}$ by encoding assertions of conditional independence as well as a collection of pdfs. From the chain rule of probability, we know

$$
\rho\left(x_{1}, \ldots, x_{n} \mid \xi\right)=\prod_{i=1}^{n} \rho\left(x_{i} \mid x_{1}, \ldots, x_{i-1}, \xi\right)
$$

For each variable $x_{i}$, let $\Pi_{i} \subseteq\left\{x_{1}, \ldots, x_{i-1}\right\}$ be a set of variables that renders $x_{i}$ and $\left\{x_{1}, \ldots, x_{i-1}\right\}$ conditionally independent. That is,

$$
\rho\left(x_{i} \mid x_{1}, \ldots, x_{i-1}, \xi\right)=\rho\left(x_{i} \mid \Pi_{i}, \xi\right)
$$

A belief network is a pair $\left(B_{S}, B_{P}\right)$, where $B_{S}$ is a belief-network structure that encodes the assertions of conditional independence in Equation 2, and $B_{P}$ is a set of pdfs corresponding to that structure. In particular, $B_{S}$ is a directed acyclic graph such that (1) each variable in $U$ corresponds to a node in $B_{S}$, and (2) the parents of the node corresponding to $x_{i}$ are the nodes corresponding to the variables in $\Pi_{i}$. (In the remainder of this paper, we use $x_{i}$ to refer to both the variable and its corresponding node in a graph.) Associated with node $x_{i}$ in $B_{S}$ are the pdfs $\rho\left(x_{i} \mid \Pi_{i}, \xi\right) . B_{P}$ is the union of these pdfs. Combining Equations 1 and 2, we see that any belief network for $\vec{x}$ uniquely determines a joint pdf for $\vec{x}$. That is,

$$
\rho\left(x_{1}, \ldots, x_{n} \mid \xi\right)=\prod_{i=1}^{n} \rho\left(x_{i} \mid \Pi_{i}, \xi\right)
$$

A minimal belief network is a belief network where Equation 2 is violated if any arc is removed. Thus, a minimal belief network represents both assertions of independence and assertions of dependence.

Let us suppose that the joint probability density function for $\vec{x}$ is a multivariate (nonsingular) normal distribution. In this case, we write

$$
\begin{aligned}
& \rho(\vec{x} \mid \xi)=n\left(\vec{m}, \Sigma^{-1}\right) \\
& \quad \equiv(2 \pi)^{-n / 2}|\Sigma|^{-1 / 2} e^{-1 / 2(\vec{x}-\vec{m})^{\prime} \Sigma^{-1}(\vec{x}-\vec{m})}
\end{aligned}
$$

where $\vec{m}$ is an $n$-dimensional mean vector, and $\Sigma=\left(\sigma_{i j}\right)$ is an $n \times n$ covariance matrix, both of which are implicitly functions of $\xi$, and where $|\Sigma|$ is the determinant of $\Sigma$. We shall often find it convenient to refer to the precision matrix $W=\Sigma^{-1}$, whose elements are denoted by $w_{i j}$.

This distribution can be written as a product of conditional distributions each being an independent normal distribution. Namely,

$$
\begin{gathered}
\rho(\vec{x} \mid \xi)=\prod_{i=1}^{n} \rho\left(x_{i} \mid x_{1}, \ldots, x_{i-1}, \xi\right) \\
\rho\left(x_{i} \mid x_{1}, \ldots, x_{i-1}, \xi\right)=n\left(m_{i}+\sum_{j=1}^{i-1} b_{i j}\left(x_{j}-m_{j}\right), 1 / v_{i}\right)
\end{gathered}
$$

where $m_{i}$ is the unconditional mean of $x_{i}, v_{i}$ is the conditional variance of $x_{i}$ given values for $x_{1}, \ldots, x_{i-1}$, and $b_{i j}$ is a linear coefficient reflecting the strength of the relationship between $x_{i}$ and $x_{j}$ (e.g., DeGroot, p.55). ${ }^{1}$ Thus, we may interpret a multivariate normal distribution as a belief network, where $b_{i j}=0(j<i)$ implies that $x_{j}$ is not a parent of $x_{i}$. We call this special form of a belief network a Gaussian belief network. The name is adopted from Shachter and Kenley (1989) who first described Gaussian influence diagrams.

More formally, a Gaussian belief network is a pair $\left(B_{S}, B_{P}\right)$, where (1) $B_{S}$ is a belief-network structure containing nodes $x_{1}, \ldots, x_{n}$ and no arc from $x_{j}$ to $x_{i}$ whenever $b_{i j}=0, j<i$, (2) $B_{P}$ is the collection of parameters $\vec{m}=\left(m_{1}, \ldots, m_{n}\right), \vec{v}=\left\{v_{1}, \ldots, v_{n}\right\}$, and $\left\{b_{i j} \mid j<i\right\}$, and (3) the joint distribution over $\vec{x}$ is determined by Equations 3 and 4. Due to special properties of nonsingular normal distributions, a minimal Gaussian belief network is one were there is an arc from $x_{j}$ to $x_{i}$ if and only if $b_{i j} \neq 0$.

Given a multivariate normal density, we can generate a Gaussian belief network, and vice versa. The unconditional means $\vec{m}$ are the same in both representations. Shachter and Kenley (1989) describe the general transformation from $\vec{v}$ and $\left\{b_{i j} \mid i<j\right\}$ of a given Gaussian belief network $G$ to the precision matrix $W$ of the normal distribution represented by $G$. They use the following recursive formula in which $W(i)$ denotes the $i \times i$ upper left submatrix of $W, \vec{b}_{i}$ denotes the column vector $\left(b_{1, i}, \ldots, b_{i-1, i}\right)$ and $\vec{b}_{i}^{\prime}$ denotes the transposed vector $\vec{b}_{i}$ (i.e., the line vector $\left.\left(b_{1, i}, \ldots, b_{i-1, i}\right)\right)$ :

$$
W(i+1)=\left(\begin{array}{cc}
W(i)+\frac{\vec{b}_{i+1} \vec{b}_{i+1}^{\prime}}{v_{i+1}} & -\frac{\vec{b}_{i+1}}{v_{i+1}} \\
-\frac{\vec{b}_{i+1}^{\prime}}{v_{i+1}} & \frac{1}{v_{i+1}}
\end{array}\right)
$$

for $i>0$, and $W(1)=\frac{1}{v_{1}}$. Equation 5 plays a key role in this paper.
For example, suppose $x_{1}=n\left(m_{1}, 1 / v_{1}\right), x_{2}=n\left(m_{2}, 1 / v_{2}\right)$, and $x_{3}=n\left(m_{3}+b_{13}\left(x_{1}-m_{1}\right)+\right.$ $\left.b_{23}\left(x_{2}-m_{2}\right), 1 / v_{3}\right)$. The belief-network structure defined by these equations is shown in Figure 1. The precision matrix is given by

$$
W=\left(\begin{array}{ccc}
\frac{1}{v_{1}}+\frac{b_{13}^{3}}{v_{3}} & \frac{b_{13} b_{23}}{v_{3}} & -\frac{b_{13}}{v_{3}} \\
\frac{b_{13} b_{23}}{v_{3}} & \frac{1}{v_{2}}+\frac{b_{23}^{3}}{v_{3}} & -\frac{b_{23}}{v_{3}} \\
-\frac{b_{13}}{v_{3}} & -\frac{b_{23}}{v_{3}} & \frac{1}{v_{3}}
\end{array}\right)
$$

[^0]
[^0]:    ${ }^{1}$ The coefficients $b_{i j}$ can be thought of as regression coefficients or expressed in terms of Yule's (1907) partial regression coefficient $\beta$.

![img-0.jpeg](img-0.jpeg)

Figure 1: A belief-network structure for three variables.

Table 1: An complete database for the domain associated with the network shown in Figure 1.


The Gaussian-belief-network representation of a multivariate normal distribution is better suited to model elicitation and understanding than is the standard representation [Shachter and Kenley, 1989]. To assess a Gaussian belief network, the user needs to specify (1) the unconditional mean of each variable $x_{i}\left(m_{i}\right),(2)$ the relative importance of each parent $x_{j}$ in determining the values of its child $x_{i}\left(b_{i j}\right)$, and (3) a conditional variance for $x_{i}$ given that its parents are fixed $\left(v_{i}\right)$. Equation 5 then determines $W$. In contrast, when assessing a normal distribution directly, one needs to guarantee that the assessed covariance matrix is positive-definite-a task done by altering in some ad hoc manner the correlations stated by the user.

# 3 A Metric for Gaussian Belief Networks 

We are interested in computing a score for a Gaussian belief-network structure, given a set of cases $D=\left\{\vec{x}_{1}, \ldots, \vec{x}_{m}\right\}$. Each case $\vec{x}_{i}$ is the observation of one or more variables in $\vec{x}$. We sometimes refer to $D$ as a database. Table 1 is an example of a database for the three-node domain of the Gaussian belief network shown in Figure 1.

Our scoring metrics are based on five assumptions, the first of which is the following:
Assumption 1 The database $D$ is a random sample from a multivariate normal distribution with unknown means $\vec{m}$ and unknown precision matrix $W$.

Because every Gaussian belief network is equivalent to a multivariate normal distribution, Assumption 1 is equivalent to stating that the database $D$ is a random sample from a Gaussian belief network with unknown parameters, $\vec{v}, B=\left\{b_{i j} \mid j<i\right\}, \vec{m}$.

A Bayesian measure of the goodness of a network structure is its posterior probability given a database:

$$
p\left(B_{S} \mid D, \xi\right)=c p\left(B_{S} \mid \xi\right) \rho\left(D \mid B_{S}, \xi\right)
$$

where $c=1 / \rho(D \mid \xi)=1 / \sum_{B_{S}} p\left(B_{S} \mid \xi\right) \rho\left(D \mid B_{S}, \xi\right)$ is a normalization constant. For even small domains, however, there are too many network structures to sum over in order to determine the constant. Therefore we use $p\left(B_{S} \mid \xi\right) \rho\left(D \mid B_{S}, \xi\right)=\rho\left(D, B_{S} \mid \xi\right)$ as our score.

Also problematic is our use of the term $B_{S}$ as an argument of a probability. In particular, $B_{S}$ is a belief-network structure, not an event. Thus, we need a definition of an event $B_{S}^{e}$ that corresponds to structure $B_{S}$ (the superscript " $e$ " stands for event). A natural definition for this event is that $B_{S}^{e}$ holds true iff the database is a random sample from a minimal Gaussian belief network with structure $B_{S}$-that is, iff for all $j<i, b_{i j} \neq 0$ if and only if there is an arc from $x_{j}$ to $x_{i}$ in $B_{S}$. For example the event $B_{S}^{e}$ corresponding to the Gaussian belief network of Figure 1, is the event $\left\{b_{12}=0, b_{13} \neq 0, b_{23} \neq 0\right\}$.

This definition has the following desirable property. When two belief-network structures represent the same assertions of conditional independence, we say that they are isomorphic. For example, in the three variable domain $\left\{x_{1}, x_{2}, x_{3}\right\}$, the network structures $x \rightarrow x_{2} \rightarrow x_{3}$ and $x_{1} \leftarrow x_{2} \rightarrow x_{3}$ represent the same assertion: $x_{1}$ and $x_{3}$ are independent given $x_{2}$. Given the definition of $B_{S}^{e}$, it can be shown that events $B_{S 1}^{e}$ and $B_{S 2}^{e}$ are equivalent if and only if the structures $B_{S 1}$ and $B_{S 2}$ are isomorphic. That is, the relation of isomorphism induces an equivalence class on the set of events $B_{S}^{e}$. We call this property event equivalence.

There is a problem with the definition, however. In particular, events corresponding to some non-isomorphic network structures are not mutually exclusive. For example, in the four-variable domain $\left\{x_{1}, x_{2}, x_{3}, x_{4}\right\}$, consider the structures $x_{1} \Rightarrow B \Leftarrow x_{4}$ and $x_{1} \Rightarrow B \Rightarrow x_{4}$, where $B$ is the subnetwork structure $x_{2} \rightarrow x_{3}$, and $x \Rightarrow B$ means that there is an arc from $x$ to both variables in $B$. The events corresponding to these structures both include the situation where $x_{1}$ and $x_{4}$ are marginally independent. Arbitrary overlaps between events can make scores difficult to interpret and use. For example, the prediction of future events by averaging over multiple models cannot be justified. In our case, however, we can repair the definition of $B_{S}^{e}$ so as to make non-equivalent events mutually exclusive, without affecting our mathematical results or the intuitive understanding of events by the user. In particular, all overlaps will be of measure zero with respect to the events that create the overlap. Thus, given a set of overlapping events, we simply exclude the intersection from all but one of the events. We note that this revised definition retains the property of event equivalence.

Proposition 1 (Event Equivalence) Belief-network structures $B_{S 1}$ and $B_{S 2}$ are isomorphic if and only if $B_{S 1}^{e}=B_{S 2}^{e}$.

Because the score for network structure $B_{S}$ is $\rho\left(D, B_{S}^{e} \mid \xi\right)$, an immediate consequence of the property of event equivalence is score equivalence.

Proposition 2 (Score Equivalence) The scores of two isomorphic belief-network structures must be equal.

Given the property of event equivalence, we technically should score each belief-network-structure equivalence class, rather than each belief-network structure. Nonetheless, users find it intuitive to work with (i.e., construct and interpret) belief networks. Consequently, we continue our presentation in terms of belief networks, keeping Proposition 2 in mind.

# 3.1 Complete Gaussian Belief Networks 

We first derive $\rho\left(D, B_{S}^{e} \mid \xi\right)$, assuming $B_{S}$ is the structure of a complete Gaussian belief network. A complete Gaussian belief network is one with no missing edges. Applying the property of event equivalence, we know that the event associated with any complete belief network is the same; and we use $B_{S_{C}}^{e}$ to denote this event.

To motivate the derivation, consider the following expansion of $\rho\left(D \mid B_{S_{C}}^{e}, \xi\right)$ :

$$
\begin{gathered}
\rho\left(D \mid B_{S_{C}}^{e}, \xi\right)=\prod_{l=1}^{m} \rho\left(C_{l} \mid C_{1}, \ldots, C_{l-1}, B_{S_{C}}^{e}, \xi\right)= \\
\prod_{l=1}^{m} \int \rho\left(C_{l} \mid \vec{m}, W, B_{S_{C}}^{e}, \xi\right) \rho\left(\vec{m}, W \mid C_{1}, \ldots, C_{l-1}, B_{S_{C}}^{e}, \xi\right) d \vec{m} d W
\end{gathered}
$$

Thus, we can derive the metric if we find a conjugate distribution for the parameters $\vec{m}$ and $W$ such that the integral above has a closed form solution.

The next assumption leads to such a conjugate distribution. If all variables in a case are observed, we say that the case is complete. If all cases in a database are complete, we say that the database is complete.

# Assumption 2 All databases are complete. ${ }^{2}$ 

Given this assumption, the following distribution is conjugate for multivariate-normal sampling.
Theorem 3 (DeGroot, p.178) Suppose that $\overrightarrow{x_{1}}, \ldots, \overrightarrow{x_{l}}$ is a random sample from a multivariate normal distribution with an unknown value of the mean vector $\vec{m}$ and an unknown value of the precision matrix $W$. Suppose that the prior joint distribution of $\vec{m}$ and $W$ is the normal-Wishart distribution: the conditional distribution of $\vec{m}$ given $W$ is $n\left(\vec{\mu}_{0}, \nu W\right)$ such that $\nu>0$, and the marginal distribution of $W$ is a Wishart distribution with $\alpha>n-1$ degrees of freedom and precision matrix $T_{0}$, denoted by $w\left(\alpha, T_{0}\right)$. Then the posterior joint distribution of $\vec{m}$ and $W$ given $\overrightarrow{x_{i}}, i=$ $1, \ldots, l$, is as follows: The conditional distribution of $\vec{m}$ given $W$ is a multivariate normal distribution with mean vector $\vec{\mu}_{l}$ and a precision matrix $(\nu+l) W$, where

$$
\bar{X}_{l}=\frac{1}{l} \sum_{i=1}^{l} \vec{x}_{i}, \quad \vec{\mu}_{l}=\frac{\nu \vec{\mu}_{0}+l \bar{X}_{l}}{\nu+l}
$$

and the marginal of $W$ is $w\left(\alpha+l, T_{l}\right)$, where $S_{l}$ and $T_{l}$ are given by

$$
S_{l}=\sum_{i=1}^{l}\left(\vec{x}_{i}-\bar{X}_{l}\right)\left(\vec{x}_{i}-\bar{X}_{l}\right)^{\prime}
$$

and

$$
T_{l}=T_{0}+S_{l}+\frac{\nu l}{\nu+l}\left(\vec{\mu}_{0}-\bar{X}_{l}\right)\left(\vec{\mu}_{0}-\bar{X}_{l}\right)^{\prime}
$$

In this theorem, $\bar{X}_{l}$ and $S_{l}$ are the sample mean and scatter matrix of the database, respectively. Also, an $n$ dimensional Wishart distribution with $\alpha$ degrees of freedom and matrix $T_{0}$ is given by

$$
\rho(W \mid \xi)=w\left(\alpha, T_{0}\right) \equiv c(n, \alpha)\left|T_{0}\right|^{\alpha / 2}|W|^{(\alpha-n-1) / 2} e^{-1 / 2 \operatorname{tr}\left\{T_{0} W\right\}}
$$

where $\operatorname{tr}\left\{T_{0} W\right\}$ is the sum of the diagonal elements of $T_{0} W$ and

$$
c(n, \alpha)=\left[2^{\alpha n / 2} \pi^{n(n-1) / 4} \prod_{i=1}^{n} \Gamma\left(\frac{\alpha+1-i}{2}\right)\right]^{-1}
$$

The parameters $\nu, \alpha, \vec{\mu}_{0}$, and $T_{0}$ are implicit functions of the user's background knowledge $\xi$. The quantities $\nu$ and $\alpha$ can be thought of as the effective sample sizes of the normal and Wishart components of the prior, respectively.

Summarizing our discussion so far, we make the following assumption:

[^0]
[^0]:    ${ }^{2}$ SDLC present a survey of approximation methods for handling missing data in the context of discrete variables. Some of these methods in modified form can be applied to Gaussian networks.

Assumption 3 The prior distribution $\rho\left(\vec{m}, W \mid B_{S_{C}}^{e}, \xi\right)$ is a normal-Wishart distribution as given in Theorem 3.

From Equation 5, this assumption fixes the distribution $\rho\left(\vec{m}, \vec{v}, B \mid B_{S_{C}}^{e}, \xi\right)$. Nonetheless, we shall sometimes find it easier to specify the prior density in the space of $W$, rather then in the space of parameters describing a Gaussian belief network.

If $\rho(\vec{x} \mid \vec{m}, W, B_{S_{C}}^{e}, \xi)=n(\vec{m}, W)$ and if $\rho\left(\vec{m}, W \mid B_{S_{C}}^{e}, \xi\right)$ is a normal-Wishart distribution as specified by Theorem 3, then $\rho\left(\vec{x} \mid B_{S_{C}}^{e}, \xi\right)$, defined by

$$
\rho\left(\vec{x} \mid B_{S_{C}}^{e}, \xi\right)=\int \rho(\vec{x} \mid \vec{m}, W, B_{S_{C}}^{e}, \xi) \rho\left(\vec{m}, W, B_{S_{C}}^{e}, \xi\right) d \vec{m} d W
$$

is an $n$ dimensional multivariate $t$ distribution with $\gamma=\alpha-n+1$ degrees of freedom, location vector $\vec{\mu}_{0}$, and a precision matrix $T_{0}^{t}=\frac{t \cdot \gamma}{\nu+1} T_{0}^{-1}$. This result can be derived by first integrating over $\vec{m}$ using Equation 6 on p. 178 of DeGroot with sample size equal to one, and then integrating over $W$ following an approach similar to that on pp.179-180 of DeGroot. Also, using Equation 3 on p. 180 of DeGroot, the $t$ distribution $\rho\left(\vec{x} \mid B_{S_{C}}^{e}, \xi\right)$ can be written in a less traditional form as follows:

$$
\rho\left(\vec{x} \mid B_{S_{C}}^{e}, \xi\right)=(2 \pi)^{-n / 2}\left(\frac{\nu}{\nu+1}\right)^{n / 2} \frac{c(n, \alpha)}{c(n, \alpha+1)}\left|T_{0}\right|^{\alpha / 2}\left|T_{1}\right|^{-(\alpha+1) / 2}
$$

where $T_{1}$ is defined by Equation 9 with $l=1$.
Combining these facts with Theorem 3, we know that $\rho\left(C_{l} \mid C_{1}, \ldots, C_{l-1}, B_{S_{C}}^{e}, \xi\right)$ is a multivariate $t$ distribution with parameters $\nu+l-1, \alpha+l-1, \vec{\mu}_{l-1}$, and $T_{l-1}$. Consequently, we obtain

$$
\begin{aligned}
\rho\left(D \mid B_{S_{C}}^{e}, \xi\right) & =\prod_{l=1}^{m} \rho\left(C_{l} \mid C_{1}, \ldots, C_{l-1}, B_{S_{C}}^{e}, \xi\right) \\
& =\prod_{l=1}^{m}\left((2 \pi)^{-n / 2}\left(\frac{\nu+l-1}{\nu+l}\right)^{n / 2} \frac{c(n, \alpha+l-1)}{c(n, \alpha+l)} \frac{\left|T_{l-1}\right|^{\frac{\alpha+l-1}{2}}}{\left|T_{l}\right|^{\frac{\alpha+1}{2}}}\right) \\
& =(2 \pi)^{-n m / 2}\left(\frac{\nu}{\nu+m}\right)^{n / 2} \frac{c(n, \alpha)}{c(n, \alpha+m)}\left|T_{0}\right|^{\frac{\alpha}{2}}\left|T_{m}\right|^{-\frac{\alpha+m}{2}}
\end{aligned}
$$

Multiplying Equation 12 by the prior probability $p\left(B_{S_{C}}^{e} \mid \xi\right)$ yields a metric for scoring $B_{S_{C}}^{e}$.

# 3.2 General Gaussian Belief Networks 

We now consider an arbitrary Gaussian belief network $B_{S}$. To form a prior distribution for the parameters of $B_{S}$, we make two additional assumptions:

Assumption 4 (Parameter Independence) For every Gaussian belief network $B_{S}, \rho\left(\vec{v}, B \mid B_{S}^{e}, \xi\right)=$ $\prod_{i=1}^{n} \rho\left(v_{i}, \vec{b}_{i} \mid B_{S}^{e}, \xi\right)$.

We note that this assumption is consistent with Assumption 3, because if $\rho\left(W \mid B_{S_{C}}^{e}, \xi\right)$ is a Wishart distribution, then $\rho\left(\vec{v}, B \mid B_{S_{C}}^{e}, \xi\right)$, obtained from $\rho\left(W \mid B_{S_{C}}^{e}, \xi\right)$ by using Equation 5 and the Jacobian $\partial W / \partial \vec{v} B$ of this transformation, is equal to $\prod_{i=1}^{n} \rho\left(v_{i}, \vec{b}_{i} \mid B_{S_{C}}^{e}, \xi\right)$. The derivation of this claim is given in the Appendix (Theorem 7).

Assumption 5 (Parameter Modularity) If $x_{i}$ has the same parents in two Gaussian belief networks $B_{S 1}$ and $B_{S 2}$, then $\rho\left(v_{i}, \vec{b}_{i} \mid B_{S 1}^{e}, \xi\right)=\rho\left(v_{i}, \vec{b}_{i} \mid B_{S 2}^{e}, \xi\right)$.

Assumption 4 has been made in discrete contexts by many researchers (e.g., CH, Buntine, SDLC, and HGC). Assumption 5 has also been made by these same researchers, but HGC were the first researchers to make the assumption explicit and to emphasize its importance for generating prior distributions. Parameter modularity plays a similar important role in the current development. In particular, this assumption, in conjunction with the property of event equivalence and our previous assumptions allows us to determine the joint prior distribution of the parameters $\vec{m}, \vec{v}, B$ associated with any Gaussian network $B_{S}$ from the joint density $\rho\left(\vec{m}, W \mid B_{S_{C}}^{e}\right)$.

To see this fact, first note that, by the definition of the event $B_{S}^{e}, \rho\left(\vec{m} \mid \vec{v}, B, B_{S}^{e}, \xi\right)=$ $\rho\left(\vec{m} \mid \vec{v}, B, B_{S_{C}}^{e}, \xi\right)$. The latter distribution is determined by $\rho\left(\vec{m} \mid W, B_{S_{C}}^{e}, \xi\right)$, which is given. Second, from Assumption 4, we obtain $\rho\left(\vec{v}, B \mid B_{S}^{e}, \xi\right)$ by determining $\rho\left(v_{i}, \vec{b}_{i} \mid B_{S}^{e}, \xi\right)$ for each $i$. By Assumption 5 , however, $\rho\left(v_{i}, \vec{b}_{i} \mid B_{S}^{e}, \xi\right)$ is equal to $\rho\left(v_{i}, \vec{b}_{i} \mid B_{S_{C}^{e}}^{e}, \xi\right)$ for any complete network structure $B_{S_{C}^{e}}$ where the parents of $x_{i}$ are the same as are those in $B_{S}$. By event equivalence and Assumption 4, we obtain $\rho\left(v_{i}, \vec{b}_{i} \mid B_{S_{C}^{e}}^{e}, \xi\right)$ from the given density $\rho\left(W \mid B_{S_{C}}^{e}, \xi\right)$.

From Assumptions 1 through 5, we derive $\rho\left(D \mid B_{S}^{e}, \xi\right)$. To do so, we need the following theorem whose proof is provided in the Appendix. [Note: a derivation from weaker assumptions is given in D. Geiger and D. Heckerman, Parameter Priors for Directed Acyclic Graphical Models and the Characterization of Several Probability Distributions, The Annals of Statistics, 30: 1412-1440, Oct 2002.]

Theorem 4 If $\rho(\vec{x} \mid \vec{m}, W, D, \xi)$ is a multivariate normal distribution, and $\rho\left(\vec{m} \mid W, D, B_{S}^{e}, \xi\right)$ is a multivariate normal distribution with a precision matrix $\nu W, \nu>0$, then $\rho\left(x_{i} \mid x_{1}, \ldots, x_{i-1}, \vec{v}, B, D, B_{S}^{e}, \xi\right)=$ $\rho\left(x_{i} \mid \Pi_{i}, v_{i}, \vec{b}_{i}, D^{x_{i} \Pi_{i}}, B_{S^{\prime}}^{e}, \xi\right)$, where $B_{S^{\prime}}$ is any network where $x_{i}$ has the same parents as in $B_{S}$, and $D^{x_{i} \Pi_{i}}$ is the database $D$ restricted to the variables in $\left\{x_{i}\right\} \cup \Pi_{i}$. In particular, this claim holds for any complete Gaussian belief network $B_{S_{C}}=B_{S^{\prime}}$ in which $\Pi_{i}$ and $x_{i}$ appear before any other variables, and $\Pi_{i}$ appears before $x_{i}$.

Let $D_{l}=\left\{C_{1}, \ldots, C_{l-1}\right\}$ and $C_{l}$ be an instance of $x_{1}, \ldots, x_{n}$. In the following derivation, we use $x_{i}$ and $\Pi_{i}$ to represent the instance of $x_{i}$ and $\Pi_{i}$ in the $l$ th case. Theorem 4 yields,

$$
\begin{aligned}
\rho\left(D \mid \vec{v}, B, B_{S}^{e}, \xi\right) & =\prod_{l=1}^{m} \prod_{i=1}^{n} \rho\left(x_{i} \mid x_{1}, \ldots, x_{i-1}, \vec{v}, B, D_{l}, B_{S}^{e}, \xi\right) \\
& =\prod_{l=1}^{m} \prod_{i=1}^{n} \frac{\rho\left(x_{i}, \Pi_{i} \mid v_{i}, \vec{b}_{i}, D_{l}^{x_{i} \Pi_{i}}, B_{S}^{e}, \xi\right)}{\rho\left(\Pi_{i} \mid v_{i}, \vec{b}_{i}, D_{l}^{x_{i} \Pi_{i}}, B_{S}^{e}, \xi\right)}
\end{aligned}
$$

and

$$
\rho\left(\Pi_{i} \mid v_{i}, \vec{b}_{i}, D_{l}^{x_{i} \Pi_{i}}, B_{S}^{e}, \xi\right)=\rho\left(\Pi_{i} \mid v_{i}, \vec{b}_{i}, D_{l}^{\Pi_{i}}, B_{S}^{e}, \xi\right)
$$

By combining these equations, we obtain the following likelihood separability property:

$$
\rho\left(D \mid \vec{v}, B, B_{S}^{e}, \xi\right)=\prod_{i=1}^{n} \frac{\rho\left(D^{x_{i} \Pi_{i}} \mid v_{i}, \vec{b}_{i}, B_{S}^{e}, \xi\right)}{\rho\left(D^{\Pi_{i}} \mid v_{i}, \vec{b}_{i}, B_{S}^{e}, \xi\right)}
$$

By Bayes rule, $\rho\left(\vec{v}, B \mid D, B_{S}^{e}, \xi\right)$ is proportional to $\rho\left(D \mid \vec{v}, B, B_{S}^{e}, \xi\right) \rho\left(\vec{v}, B \mid B_{S}^{e}, \xi\right)$. Thus, because $\rho\left(D \mid \vec{v}, B, B_{S}^{e}, \xi\right)$ factors as shown by Equation 13, and $\rho\left(\vec{v}, B \mid B_{S}^{e}, \xi\right)$ factors as given by Assumption 4, we obtain the following posterior parameter independence property:

$$
\rho\left(\vec{v}, B \mid D, B_{S}^{e}, \xi\right)=\prod_{i=1}^{n} \rho\left(v_{i}, \vec{b}_{i} \mid D^{x_{i} \Pi_{i}}, B_{S}^{e}, \xi\right)
$$

In a similar manner, whenever $x_{i}$ has the same parents in two Gaussian belief networks $B_{S}$ and $B_{S^{\prime}}$, by using Equation 13 where $B_{S}^{e}$ in the right hand side is replaced by $B_{S^{\prime}}^{e}$ and using Assumption 5,

we obtain the posterior parameter modularity property:

$$
\rho\left(v_{i}, \vec{b}_{i} \mid D^{x_{i} \Pi_{i}}, B_{S}^{e}, \xi\right)=\rho\left(v_{i}, \vec{b}_{i} \mid D^{x_{i} \Pi_{i}}, B_{S^{\prime}}^{e}, \xi\right)
$$

Now, we have

$$
\begin{aligned}
\rho\left(D \mid B_{S}^{e}, \xi\right) & =\prod_{l=1}^{m} \rho\left(C_{l} \mid D_{l}, B_{S}^{e}, \xi\right) \\
\rho\left(C_{l} \mid D_{l}, B_{S}^{e}, \xi\right) & =\prod_{i=1}^{n} \rho\left(x_{i} \mid x_{1}, \ldots, x_{i-1}, D_{l}, B_{S}^{e}, \xi\right) \\
\rho\left(x_{i} \mid x_{1}, \ldots, x_{i-1}, D_{l}, B_{S}^{e}, \xi\right) & =\int \rho\left(x_{i} \mid x_{1}, \ldots, x_{i-1}, D_{l}, \vec{v}, B, B_{S}^{e}, \xi\right) \rho\left(\vec{v}, B \mid D_{l}, B_{S}^{e}, \xi\right) d \vec{v} B
\end{aligned}
$$

By applying Theorem 4 to the first term of the right-hand-side of Equation 15, and posterior parameter independence and posterior parameter modularity to the second term, we obtain

$$
\begin{aligned}
\rho\left(x_{i} \mid x_{1}, \ldots, x_{i-1}, D_{l}, B_{S}^{e}, \xi\right) & =\int \rho\left(x_{i} \mid \Pi_{i}, v_{i}, \vec{b}_{i}, D_{l}^{x_{i} \Pi_{i}}, B_{S_{C}}^{e}, \xi\right) \rho\left(v_{i}, \vec{b}_{i} \mid D_{l}^{x_{i} \Pi_{i}}, B_{S_{C}}^{e}, \xi\right) d v_{i} \vec{b}_{i} \\
& =\rho\left(x_{i} \mid \Pi_{i}, D_{l}^{x_{i} \Pi_{i}}, B_{S_{C}}^{e}, \xi\right)
\end{aligned}
$$

Therefore,

$$
\rho\left(C_{l} \mid D_{l}, B_{S}^{e}, \xi\right)=\prod_{i=1}^{n} \frac{\rho\left(x_{i}, \Pi_{i} \mid D_{l}^{x_{i} \Pi_{i}}, B_{S_{C}}^{e}, \xi\right)}{\rho\left(\Pi_{i} \mid D_{l}^{x_{i} \Pi_{i}}, B_{S_{C}}^{e}, \xi\right)}
$$

Furthermore, because $\rho\left(\Pi_{i} \mid D_{l}^{x_{i} \Pi_{i}}, B_{S_{C}}^{e}, \xi\right)$ is a multivariate $t$ distribution, we know that

$$
\rho\left(\Pi_{i} \mid D_{l}^{x_{i} \Pi_{i}}, B_{S_{C}}^{e}, \xi\right)=\rho\left(\Pi_{i} \mid D_{l}^{\Pi_{i}}, B_{S_{C}}^{e}, \xi\right)
$$

(DeGroot, p.60). Thus, combining Equations 14 and 16, we have

$$
\rho\left(D \mid B_{S}^{e}, \xi\right)=\prod_{i=1}^{n} \frac{\rho\left(D^{x_{i} \Pi_{i}} \mid B_{S_{C}}^{e}, \xi\right)}{\rho\left(D^{\Pi_{i}} \mid B_{S_{C}}^{e}, \xi\right)}
$$

where each term in 17 is of the form given in Equation 12. Multiplying Equation 17 by $p\left(B_{S}^{e} \mid \xi\right)$, we obtain a metric for an arbitrary Gaussian belief network $B_{S}$. (This development is incomplete, as it requires a recipe for deriving the parameters of the prior for subsets of the domain variables from the prior for all domain variables. The recipe implicit in an example given in the original versiondeleted in this version-is incorrect. For a correction, see the 2021 update of D. Geiger and D. Heckerman, Parameter Priors for Directed Acyclic Graphical Models and the Characterization of Several Probability Distributions, The Annals of Statistics, 30: 1412-1440, Oct 2002.) We call this metric BGe which stands for Bayesian metric for $G$ aussian networks having score equivalence.

# 3.3 Score Equivalence 

In making the assumptions of parameter independence and parameter modularity, we have-in effect-specified the prior densities for the multinomial parameters in terms of the structure of a belief network. Consequently, there is the possibility that this specification violates the property of score equivalence. The following theorem, however, demonstrates that our specification implies score equivalence.

Theorem 5 (Score Equivalence) If $B_{S 1}$ and $B_{S 2}$ are isomorphic belief-network structures, then $\rho\left(D \mid B_{S 1}^{e}, \xi\right)$ and $\rho\left(D \mid B_{S 2}^{e}, \xi\right)$ as computed by Equation 17 are equal.

Proof: In Heckerman et al. (1994, Theorem 10), we show that a belief network structure can be transformed into an isomorphic structure by a series of arc reversals, such that, whenever an arc from $x_{i}$ to $x_{j}$ is reversed, $\Pi_{i}=\Pi_{j} \backslash\left\{x_{i}\right\}$. Thus, our claim follows if we can prove it for the case where $B_{S 1}$ and $B_{S 2}$ differ by a single arc reversal with this restriction.

So, let $B_{S 1}$ and $B_{S 2}$ be two isomorphic network structures that differ only in the direction of the arc between $x_{i}$ and $x_{j}$ (say $x_{i} \rightarrow x_{j}$ in $B_{S 1}$ ). Let $R$ be the parents of $x_{i}$ in $B_{S 1}$. By the cited theorem, $R \cup\left\{x_{i}\right\}$ is the parents of $x_{j}$ in $B_{S 1}, R$ is the parents of $x_{j}$ in $B_{S 2}$, and $R \cup\left\{x_{j}\right\}$ is the parents of $x_{i}$ in $B_{S 2}$. Because the two structures differ only in the reversal of a single arc, the only terms in the product of Equation 17 that can differ are those involving $x_{i}$ and $x_{j}$. For $B_{S 1}$, these terms are

$$
\frac{\rho\left(D^{x_{i} R} \mid B_{S_{C}}^{e}, \xi\right)}{\rho\left(D^{R} \mid B_{S_{C}}^{e}, \xi\right)} \frac{\rho\left(D^{x_{i} x_{j} R} \mid B_{S_{C}}^{e}, \xi\right)}{\rho\left(D^{x_{i} R} \mid B_{S_{C}}^{e}, \xi\right)}=\frac{\rho\left(D^{x_{i} x_{j} R} \mid B_{S_{C}}^{e}, \xi\right)}{\rho\left(D^{R} \mid B_{S_{C}}^{e}, \xi\right)}
$$

whereas for $B_{S 2}$, they are

$$
\frac{\rho\left(D^{x_{j} R} \mid B_{S_{C}}^{e}, \xi\right)}{\rho\left(D^{R} \mid B_{S_{C}}^{e}, \xi\right)} \frac{\rho\left(D^{x_{i} x_{j} R} \mid B_{S_{C}}^{e}, \xi\right)}{\rho\left(D^{x_{j} R} \mid B_{S_{C}}^{e}, \xi\right)}=\frac{\rho\left(D^{x_{i} x_{j} R} \mid B_{S_{C}}^{e}, \xi\right)}{\rho\left(D^{R} \mid B_{S_{C}}^{e}, \xi\right)}
$$

Thus, $\rho\left(D \mid B_{S 1}^{e}, \xi\right)=\rho\left(D \mid B_{S 2}^{e}, \xi\right)$.

# 3.4 Encoding Prior Knowledge: The Prior Gaussian Belief Network 

From the previous discussion, we see that there are three components of a user's prior knowledge that are relevant to learning Gaussian networks: (1) the prior probabilities $p\left(B_{S}^{e} \mid \xi\right)$, (2) the effective sample sizes $\alpha$ and $\nu$, and (3) the parameters $\vec{\mu}_{0}$ and $T_{0}$. The assessment of the prior probabilities $p\left(B_{S}^{e} \mid \xi\right)$ is straightforward. Buntine and HGC, for example, describe methods that facilitate these assessments. In addition, a user can assess the effective sample sizes directly. In this section, we concentrate on the assessment of $\vec{\mu}_{0}$ and $T_{0}$.

Using (1) our previous observation that $p\left(\vec{x} \mid B_{S_{C}}^{e}, \xi\right)$ is a multivariate $t$ distribution, and (2) Equation 11 on p. 61 of DeGroot with $\alpha>n+1$, we obtain

$$
\mathrm{E}\left(\vec{x} \mid B_{S_{C}}^{e}, \xi\right)=\vec{\mu}_{0} \quad \operatorname{Cov}\left(\vec{x} \mid B_{S_{C}}^{e}, \xi\right)=\frac{\nu+1}{\nu} \frac{1}{\alpha-n-1} T_{0}
$$

Thus, a person can assess a Gaussian belief network for $\mathrm{E}\left(\vec{x} \mid B_{S_{C}}^{e}, \xi\right)$ and $\operatorname{Cov}\left(\vec{x} \mid B_{S_{C}}^{e}, \xi\right)$, and then compute $\vec{\mu}_{0}$ and $T_{0}$ using Equations 18. We call this belief network a prior belief network.

## 4 Metrics for Gaussian Causal Networks

People often have knowledge about the causal relationships among variables in addition to knowledge about conditional independence. Such causal knowledge is stronger than is conditional-independence knowledge, because it allows us to derive beliefs about a domain after we intervene. Causal networks, described-for example-by Spirtes et al. (1993), Pearl and Verma (1991), and Heckerman and Shachter (1994) represent such causal relationships among variables. In particular, a causal network for $U$ is a belief network for $U$, wherein it is asserted that each nonroot node $x$ is caused by its parents. The precise meaning of cause and effect is not important for our discussion. The interested reader should consult the previous references.

The event $C_{S}^{e}$ is the same as that for a belief-network structure, except that we also include in the event the assertion that each nonroot node is caused by its parents. Thus, in contrast to the case for belief networks, it is not appropriate to require the properties of event equivalence or score equivalence. For example, consider a domain containing two variables $x$ and $y$. Both the causal network $C_{S 1}$ where $x$ points to $y$ and the causal network $C_{S 2}$ where $y$ points to $x$ represent

the assertion that $x$ and $y$ are dependent. The network $C_{S 1}$, however, in addition represents the assertion that $x$ causes $y$, whereas the network $C_{S 2}$ represents the assertion that $y$ causes $x$. Thus, the events $C_{S 1}^{c}$ are $C_{S 2}^{c}$ are not equal. Indeed, it is reasonable to assume that these events-and the events associated with any two different causal-network structures-are mutually exclusive.

In principle, then, a user may assign a (possibly different) prior distribution to the parameters $\vec{m}, \vec{v}$, and $B$ to every complete Gaussian causal network, constrained only by the assumption of parameter modularity. The prior distributions for parameters of incomplete networks would then be determined by parameter modularity. We call this general metric BG, as it is a superset of the BGe metric. For practical reasons, however, the assessment process should be constrained. One alternative is to use the BGe metric. A more general alternative is to continue to use the prior network to compute $\vec{\mu}_{0}$ and $T_{0}$, but to allow effective sample size to vary for different variables and different parent sets of each variable. We call this metric the BGp metric, where "p" stands for prior network.

# 5 Summary and Future Work 

We have described metrics for learning belief networks and causal networks from a combination of user knowledge and statistical data for domains containing only continuous variables. An important contribution has been our elucidation of the property of event equivalence and the assumption of parameter modularity. We have shown that these properties, when combined, allow a statistician to compute a reasonable prior distribution for the parameters of any Gaussian belief network, given a single prior Gaussian belief network provided by a user.

A legitimate concern with our approach is that the multivariate model is too restrictive. In practice, when this model is inappropriate, statisticians will typically turn to a more general model where each continuous variable conditioned on its parents is assumed to be a mixture of multivariate normal distributions. In Geiger and Heckerman (1994), we derive metrics for domains containing both discrete and continuous variables, subject to the restriction that a domain can be decomposed into disjoint sets of continuous variables where each such set is conditioned by a set of discrete variables. We note that this work, when combined with approximation methods that handle missing data, provides a method for learning with multivariate mixtures.

In the discrete case, a complete network has one parameter for each instance of $\vec{x}$. Consequently, it is easy to overfit such a structure with data; and the metrics developed for discrete domains provide a means by which we can avoid such overfitting. In the continuous case, a complete network has only $n+n(n-1) / 2$ parameters. Thus, it is possible that the errors introduced by our methods, arising from heuristic search in an exponential space to find one or a handful of structures with high scores outweigh the benefits associated with decreasing the degree of overfitting. We leave this concern for future experimentation.

## Acknowledgments

We thank Wray Buntine and anonymous reviewers for useful suggestions.

# Appendix 

Theorem 6 The Jacobian $J$ for the change of variables from $W$ to $\{\vec{v}, B\}$ is given by

$$
J=\partial W / \partial \vec{v} B=\prod_{i=1}^{n} v_{i}^{-(i+1)}
$$

Proof: Let $J(i)$ denote the Jacobian for the first $i$ variables in $W$. Then $J(i)$ has the following matrix form:

$$
\left(\begin{array}{ccc}
J(i-1) & 0 & 0 \\
0 & -\frac{1}{v_{i}} I_{i-1, i-1} & 0 \\
0 & 0 & -\frac{1}{v_{i}^{2}}
\end{array}\right)
$$

where $I_{k, k}$ is the identity matrix of size $k \times k$. Thus, the absolute value of $J(i)$ is given by,

$$
$$

which gives Equation 19 .
Theorem 7 If $\rho(W \mid \xi)$ has an n-dimensional Wishart distribution, then

$$
\rho(\vec{v}, B \mid \xi)=\prod_{i=1}^{n} \rho\left(v_{i}, \vec{b}_{i} \mid \xi\right)
$$

Proof: By assumption, we have

$$
\rho(W \mid \xi)=c|W|^{(\alpha-n-1) / 2} e^{-1 / 2 \operatorname{tr}\left\{T_{0} W\right\}}
$$

Thus, we must express Equation 22 in terms of $\{\vec{v}, B\}$, multiply by the Jacobian given by Theorem 6 , and show that the resulting function factors as a function of $i$. From Equation 5, we get

$$
$$

so that the determinant in Equation 22 factors as a function of $i$. Also, Equation 5 implies (by induction) that each element $w_{i j}$ in $W$ is a sum of terms each being a function of $\vec{b}_{i}$ and $v_{i}$. Consequently, the exponent in Equation 22 factors as a function of $i$. $\square$

Theorem 4 If $\rho(\vec{x} \mid \vec{m}, W, D, B_{S}^{e}, \xi)$ is a multivariate normal distribution, and $\rho(\vec{m} \mid W, D, B_{S}^{e}, \xi)$ is a multivariate normal distribution with precision matrix $\nu W, \nu>0$, then $\rho\left(x_{i} \mid x_{1}, \ldots, x_{i-1}, \vec{v}, B, D, B_{S}^{e}, \xi\right)=$ $\rho\left(x_{i} \mid \Pi_{i}, v_{i}, \vec{b}_{i}, D^{x_{i} \Pi_{i}}, B_{S^{\prime}}^{e}, \xi\right)$ where $B_{S^{\prime}}$ is any network where $x_{i}$ has the same parents as in $B_{S}$, and $D^{x_{i} \Pi_{i}}$ is the database $D$ restricted to the variables in $\left\{x_{i}\right\} \cup \Pi_{i}$.

Proof: Using

$$
\rho(\vec{x} \mid W, D, B_{S}^{e}, \xi)=\int \rho(\vec{x} \mid \vec{m}, W, D, B_{S}^{e}, \xi) \rho\left(\vec{m} \mid W, D, B_{S}^{e}, \xi\right) d \vec{m}
$$

and Assumptions 1 and 3, we obtain

$$
\rho(\vec{x} \mid W, D, B_{S}^{e}, \xi)=c|W|^{1 / 2} \cdot e^{-\frac{1}{2} \frac{c}{\nu+1} \sum_{i, j=1}^{n}\left(x_{i}-\mu_{D i}\right)\left(x_{j}-\mu_{D j}\right) w_{i j}}
$$

where $\vec{\mu}_{D}$ is the posterior mean after seeing $D$, given by Equation 7 of Theorem 3.
The marginal distribution $\rho\left(x_{1}, \ldots, x_{i} \mid \xi\right)$ of a normal distribution $n(\vec{m}, W)$ is a normal distribution $n\left(\vec{m}_{i}, W_{i}\right)$, where $\vec{m}_{i}$ and $W_{i}$ are the terms in $\vec{m}$ and $W$ that correspond to $x_{1}, \ldots, x_{i}$. Thus, using $|W|=\prod_{i=1}^{n} v_{i}^{-1}$, Equation 23 becomes

$$
\rho\left(x_{1}, \ldots, x_{i} \mid W, D, B_{S}^{e}, \xi\right)=c\left|W_{i}\right|^{1 / 2} \cdot e^{-\frac{1}{2} \frac{c}{\nu+1} \sum_{j, k=1}^{i}\left(x_{j}-\mu_{j D}\right)\left(x_{k}-\mu_{k D}\right) w_{j k}}
$$

By expressing $W$ in terms of $\vec{v}$ and $B$ using Equation 5, we obtain

$$
\frac{\rho\left(x_{1}, \ldots, x_{i} \mid \vec{v}, B, D, B_{S}^{e}, \xi\right)}{\rho\left(x_{1}, \ldots, x_{i-1} \mid \vec{v}, B, D, B_{S}^{e}, \xi\right)}=c \cdot v_{i}^{-1 / 2} \cdot e^{-\frac{1}{2} \frac{c}{\nu+1} A}
$$

where

$$
A=\operatorname{tr}\left[\left(\vec{x}-\vec{\mu}_{D}\right)_{i}\left(\vec{x}-\vec{\mu}_{D}\right)_{i}^{\prime}\left(\begin{array}{cc}
\frac{\vec{b}_{i} \vec{b}_{i}}{v_{b_{i}}} & -\frac{\vec{b}_{i}}{v_{i}} \\
-\frac{b_{i}}{v_{i}} & v_{i}
\end{array}\right)\right]
$$

where $\left(\vec{x}-\vec{\mu}_{D}\right)_{i}$ is the column vector of the $i$ elements of $\left(\vec{x}-\vec{\mu}_{D}\right)$ that correspond to $x_{1}, \ldots, x_{i}$. Starting with any network $B_{S^{\prime}}$, such that the parents of $x_{i}$ are the same as in $B_{S}$, we obtain exactly Equations 25 and 26. Furthermore, because $\vec{\mu}_{D}$ depends only on $D^{x_{i} \Pi_{i}}$, the theorem is established.