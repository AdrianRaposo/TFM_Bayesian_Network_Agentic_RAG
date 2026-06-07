# Discrete statistical models with rational maximum likelihood estimator 

ELIANA DUARTE ${ }^{1}$, ORLANDO MARIGLIANO ${ }^{2, *}$ and BERND STURMFELS ${ }^{2, \dagger}$<br>${ }^{1}$ Fakultät für Mathematik, Otto-von-Guericke Universität Magdeburg, 39106 Magdeburg, Germany. E-mail: eliana.duarte@ovgu.de<br>${ }^{2}$ Max-Planck-Institut für Mathematik in den Naturwissenschaften, Inselstraße 22, 04103 Leipzig, Germany. E-mail: *orlando.marigliano@mis.mpg.de; ${ }^{\dagger}$ bernd@mis.mpg.de

A discrete statistical model is a subset of a probability simplex. Its maximum likelihood estimator (MLE) is a retraction from that simplex onto the model. We characterize all models for which this retraction is a rational function. This is a contribution via real algebraic geometry which rests on results on Horn uniformization due to Huh and Kapranov. We present an algorithm for constructing models with rational MLE, and we demonstrate it on a range of instances. Our focus lies on models familiar to statisticians, like Bayesian networks, decomposable graphical models and staged trees.

Keywords: algebraic statistics; discrete statistical models; graphical models; likelihood geometry; maximum likelihood estimator; real algebraic geometry

## 1. Introduction

A discrete statistical model is a subset $\mathcal{M}$ of the open probability simplex $\Delta_{n}$. Each point $p$ in $\Delta_{n}$ is a probability distribution on the finite state space $\{0,1, \ldots, n\}$, that is, $p=\left(p_{0}, p_{1}, \ldots, p_{n}\right)$, where the $p_{i}$ are positive real numbers that satisfy $p_{0}+p_{1}+\cdots+p_{n}=1$. The model $\mathcal{M}$ is the set of all distributions $p \in \Delta_{n}$ that are relevant for an application.

In data analysis, we are given an empirical distribution $u=\left(u_{0}, u_{1}, \ldots, u_{n}\right)$. This is the point in $\Delta_{n}$ whose $i$ th coordinate $u_{i}$ is the fraction of samples in state $i$. The maximum likelihood estimator (MLE) of $\mathcal{M}$ is a function $\Phi: \Delta_{n} \rightarrow \mathcal{M}$ that takes the empirical distribution $u$ to a distribution $\hat{p}=$ $\left(\hat{p}_{0}, \hat{p}_{1}, \ldots, \hat{p}_{n}\right)$ that best explains the given observations. Here "best" is understood in the sense of likelihood inference, so that $\hat{p}=\Phi(u)$ is the point in $\mathcal{M}$ that maximizes the log-likelihood function $p \mapsto \sum_{i=0}^{n} u_{i} \cdot \log \left(p_{i}\right)$. For any vector $u$ in $\mathbb{R}_{>0}^{n+1}$, we set $\Phi(u):=\Phi(u /|u|)$ where $|u|=u_{0}+\cdots+u_{n}$.

Likelihood inference is consistent. This means that $\Phi(u)=u$ for $u \in \mathcal{M}$. This follows from the fact that the log-likelihood function is strictly concave on $\Delta_{n}$ and its unique maximizer is $p=u$. Hence, the MLE $\Phi$ is a retraction from the simplex onto the model.

This point is fundamental for two fields at the crossroads of mathematics and data science. Information Geometry [1] views the MLE as the nearest point map of a Riemannian metric on $\Delta_{n}$, given by the Kullback-Leibler divergence of probability distributions. Algebraic Statistics [4,17] is concerned with models $\mathcal{M}$ whose MLE $\Phi$ is an algebraic function of $u$. This happens when the constraints that define $\mathcal{M}$ are given in terms of polynomials in $p$. In this article, we address a question that is fundamental for both fields:

For which models $\mathcal{M}$ is the MLE $\Phi$ a rational function in the empirical distribution $u$ ?
The most basic example where the MLE is rational is the independence model for two binary random variables $(n=3)$. Here, $\mathcal{M}$ is a surface in the tetrahedron $\Delta_{3}$. That surface is a familiar picture that serves as a point of entry for both Information Geometry and Algebraic Statistics. Points in $\mathcal{M}$ are

positive rank one $2 \times 2$ matrices $\left[\begin{array}{cc}p_{0} & p_{1} \\ p_{2} & p_{3}\end{array}\right]$ whose entries sum to one. The data takes the form of a nonnegative integer $2 \times 2$ matrix $u$ of counts of observed frequencies. Hence $|u|=u_{0}+u_{1}+u_{2}+u_{3}$ is the sample size, and $u /|u|$ is the empirical distribution. The MLE $\hat{p}=\Phi(u)$ is evaluated by multiplying the row and column sums of $u$ :

$$
\begin{array}{ll}
\hat{p}_{0}=\frac{\left(u_{0}+u_{1}\right)\left(u_{0}+u_{2}\right)}{|u|^{2}}, & \hat{p}_{1}=\frac{\left(u_{0}+u_{1}\right)\left(u_{1}+u_{3}\right)}{|u|^{2}} \\
\hat{p}_{2}=\frac{\left(u_{2}+u_{3}\right)\left(u_{0}+u_{2}\right)}{|u|^{2}}, & \hat{p}_{3}=\frac{\left(u_{2}+u_{3}\right)\left(u_{1}+u_{3}\right)}{|u|^{2}}
\end{array}
$$

These four expressions are rational, homogeneous of degree zero and their sum is equal to 1. See [10], Example 2, for a discussion of these formulas from our present perspective.

The surface $\mathcal{M}$ belongs to the class of graphical models [14]. Fix an undirected graph $G$ whose nodes represent random variables with finitely many states. The undirected graphical model $\mathcal{M}_{G}$ is a subset of $\Delta_{n}$, where $n+1$ is the number of states in the joint distribution. The graphical model $\mathcal{M}_{G}$ is decomposable if and only if the graph $G$ is chordal. Each coordinate $\hat{p}_{i}$ of its MLE is an alternating product of linear forms given by maximal cliques and minimal separators of $G$. A similar formula exists for directed graphical models, which are also known as Bayesian networks.

In both cases, the coordinates of the MLE are not only rational functions, but even alternating products of linear forms in $u=\left(u_{0}, u_{1}, \ldots, u_{n}\right)$. This is no coincidence. Huh [10] proved that if $\Phi$ is a rational function then each of its coordinates is an alternating product of linear forms, with numerator and denominator of the same degree. Huh further showed that this alternating product must take a very specific shape. That shape was discovered by Kapranov [12], who named it the Horn uniformization. The results by Kapranov and Huh are valid for arbitrary complex algebraic varieties. They make no reference to a context where the coordinates are real, positive and add up to 1.

The present paper makes the leap from complex varieties back to statistical models. Building on the remarkable constructions by Kapranov and Huh, we here work in the setting of real algebraic geometry that is required for statistical applications. Our main result (Theorem 1) characterizes all models $\mathcal{M}$ in $\Delta_{n}$ whose MLE is a rational function. It is stated in Section 2 and all its ingredients are presented in a self-contained manner.

In Section 3, we examine models with rational MLE that are familiar to statisticians, such as decomposable graphical models and Bayesian networks. Our focus lies on staged tree models, a far-reaching generalization of discrete Bayesian networks, described in the book by Collazo, Görgen and Smith [3]. We explain how our main result applies to these models. The proof of Theorem 1 is presented in Section 4. This is the technical heart of our paper, building on the likelihood geometry of [11], §3. We also discuss the connection to toric geometry and geometric modeling developed by Clarke and Cox [2]. In Section 5, we present our algorithm for constructing models with rational MLE, and we discuss its implementation and some experiments. The input is an integer matrix representing a toric variety, and the output is a list of models derived from that matrix. Our results suggest that only a very small fraction of Huh's varieties in [10] are statistical models.

# 2. How to be rational 

Let $\mathcal{M}$ be a discrete statistical model in the open simplex $\Delta_{n}$ that has a well-defined maximum likelihood estimator $\Phi: \Delta_{n} \rightarrow \mathcal{M}$. We also write $\Phi: \mathbb{R}_{>0}^{n+1} \rightarrow \mathcal{M}$ for the induced map $u \mapsto \Phi(u /|u|)$ on positive vectors. If the $n+1$ coordinates of $\Phi$ are rational functions in $u$, then we say that $\mathcal{M}$ has rational MLE. The following is our main result.

Theorem 1. The following are equivalent for the statistical model $\mathcal{M}$ with MLE $\Phi$ :
(1) The model $\mathcal{M}$ has rational MLE.
(2) There exists a Horn pair $(H, \lambda)$ such that $\mathcal{M}$ is the image of the Horn map

$$
\varphi_{(H, \lambda)}: \quad \mathbb{R}_{>0}^{n+1} \rightarrow \mathbb{R}_{>0}^{n+1}
$$

(3) There exists a discriminantal triple $(A, \Delta, \mathbf{m})$ such that $\mathcal{M}$ is the image under the monomial map $\phi_{(\Delta, \mathbf{m})}$ of precisely one orthant (9) of the dual toric variety $Y_{A}^{*}$.
The MLE of the model satisfies the following relation on the open orthant $\mathbb{R}_{>0}^{n+1}$ :

$$
\Phi=\varphi_{(H, \lambda)}=\phi_{(\Delta, \mathbf{m})} \circ H
$$

This theorem matters for statistics because it reveals when a model has an MLE of the simplest possible closed form. Property (2) says that the polynomials appearing in the numerators and denominators of the rational formulas must factor into linear forms with positive coefficients. Property (3) offers a recipe, based on toric geometry, for explicitly constructing such models. The advance over [10] is that Theorem 1 deals with positive real numbers. It hence furnishes the definitive solution in the case of applied interest.

The goal of this section is to define all the terms seen in parts (2) and (3) of Theorem 1.
Example 2. We first discuss Theorem 1 for a simple experiment: Flip a biased coin. If it shows heads, flip it again. This is the model with $n=2$ given by the tree diagram below. The model $\mathcal{M}$ is a curve in
![img-0.jpeg](img-0.jpeg)
the probability triangle $\Delta_{2}$. The tree shows its parametrization

$$
\Delta_{1} \rightarrow \Delta_{2}, \quad\left(s_{0}, s_{1}\right) \mapsto\left(s_{0}^{2}, s_{0} s_{1}, s_{1}\right) \quad \text { where } s_{0}, s_{1}>0 \text { and } s_{0}+s_{1}=1
$$

The implicit representation of the curve $\mathcal{M}$ is the equation $p_{0} p_{2}-\left(p_{0}+p_{1}\right) p_{1}=0$. Let $\left(u_{0}, u_{1}, u_{2}\right)$ be the counts from repeated experiments. A total of $2 u_{0}+2 u_{1}+u_{2}$ coin tosses were made. We estimate the parameters as the empirical frequency of heads, respectively, tails:

$$
\hat{s}_{0}=\frac{2 u_{0}+u_{1}}{2 u_{0}+2 u_{1}+u_{2}} \quad \text { and } \quad \hat{s}_{1}=\frac{u_{1}+u_{2}}{2 u_{0}+2 u_{1}+u_{2}}
$$

The MLE is the retraction from the triangle $\Delta_{2}$ to the curve $\mathcal{M}$ given by the formula

$$
\Phi\left(u_{0}, u_{1}, u_{2}\right)=\left(\hat{s}_{0}^{2}, \hat{s}_{0} \hat{s}_{1}, \hat{s}_{1}\right)=\left(\frac{\left(2 u_{0}+u_{1}\right)^{2}}{\left(2 u_{0}+2 u_{1}+u_{2}\right)^{2}}, \frac{\left(2 u_{0}+u_{1}\right)\left(u_{1}+u_{2}\right)}{\left(2 u_{0}+2 u_{1}+u_{2}\right)^{2}}, \frac{u_{1}+u_{2}}{2 u_{0}+2 u_{1}+u_{2}}\right)
$$

Hence $\mathcal{M}$ has rational MLE. We see that the Horn pair from part (2) in Theorem 1 has

$$
H=\left(\begin{array}{ccc}
2 & 1 & 0 \\
0 & 1 & 1 \\
-2 & -2 & -1
\end{array}\right) \quad \text { and } \quad \lambda=(1,1,-1)
$$

We next exhibit the discriminantal triple $(A, \Delta, \mathbf{m})$ in part (3) of Theorem 1. The matrix $A=(111)$ gives a basis of the left kernel of $H$. The second entry is the polynomial

$$
\Delta=x_{3}^{2}-x_{1}^{2}-x_{1} x_{2}+x_{2} x_{3}=\left(x_{3}-x_{1}\right)\left(x_{1}+x_{2}+x_{3}\right)
$$

The third entry marks the leading term $\mathbf{m}=x_{3}^{2}$. These data define the monomial map

$$
\phi_{(\Delta, \mathbf{m})}: \quad\left(x_{1}, x_{2}, x_{3}\right) \mapsto\left(\frac{x_{1}^{2}}{x_{3}^{2}}, \frac{x_{1} x_{2}}{x_{3}^{2}},-\frac{x_{2}}{x_{3}}\right)
$$

The toric variety of the matrix $A$ is the point $Y_{A}=\{(1: 1: 1)\}$ in $\mathbb{P}^{2}$. Our polynomial $\Delta$ vanishes on the line $Y_{A}^{*}=\left\{x_{1}+x_{2}+x_{3}=0\right\}$ that is dual to $Y_{A}$. The relevant orthant is the open line segment $Y_{A, \sigma}^{*}:=\left\{\left(x_{1}: x_{2}: x_{3}\right) \in Y_{A}^{*}: x_{1}, x_{2}>0\right.$ and $\left.x_{3}<0\right\}$. Part (3) in Theorem 1 says that $\mathcal{M}$ is the image of $Y_{A, \sigma}^{*}$ under $\phi_{(\Delta, \mathbf{m})}$. The MLE is $\Phi=\phi_{(\Delta, \mathbf{m})} \circ H$.

We now come to the definitions needed for Theorem 1. Let $H=\left(h_{i j}\right)$ be an $m \times(n+1)$ integer matrix whose columns sum to zero, that is, $\sum_{i=1}^{m} h_{i j}=0$ for $j=0, \ldots, n$. We call such a matrix a Horn matrix and denote its columns by $h_{0}, h_{1}, \ldots, h_{n}$. The following alternating products of linear forms are rational functions of degree zero:

$$
(H u)^{h_{j}}:=\prod_{i=1}^{m}\left(h_{i 0} u_{0}+h_{i 1} u_{1}+\cdots+h_{i n} u_{n}\right)^{h_{i j}} \quad \text { for } j=0,1, \ldots, n
$$

We use the notation $v^{h}:=\prod_{i} v_{i}^{h_{i}}$ for two vectors $v, h$ of the same size. The Horn matrix $H$ is friendly if there exists a real vector $\lambda=\left(\lambda_{0}, \ldots, \lambda_{n}\right)$ with $\lambda_{i} \neq 0$ for all $i$ such that the following identity holds in the rational function field $\mathbb{R}\left(u_{0}, u_{1}, \ldots, u_{n}\right)$ :

$$
\lambda_{0}(H u)^{h_{0}}+\lambda_{1}(H u)^{h_{1}}+\cdots+\lambda_{n}(H u)^{h_{n}}=1
$$

If this holds, then we call $(H, \lambda)$ a friendly pair, and we consider the rational function

$$
\mathbb{R}^{n+1} \rightarrow \mathbb{R}^{n+1}, \quad u \mapsto\left(\lambda_{0}(H u)^{h_{0}}, \lambda_{1}(H u)^{h_{1}}, \ldots, \lambda_{n}(H u)^{h_{n}}\right)
$$

The friendly pair $(H, \lambda)$ is called a Horn pair if the function (4) is defined for all positive vectors, and it maps these to positive vectors. If these conditions hold, then we write $\varphi_{(H, \lambda)}: \mathbb{R}_{>0}^{n+1} \rightarrow \mathbb{R}_{>0}^{n+1}$ for the restriction of (4) to the positive orthant. We call $\varphi_{(H, \lambda)}$ the Horn map associated to the Horn pair $(H, \lambda)$.

The difference between our Horn pairs and the more general pairs considered by Huh in [10] is the positivity condition we just introduced, along with the "friendliness" condition. These conditions guarantee that the image of the Horn map lies in the probability simplex, which is necessary for its interpretation as a statistical model. They also imply special properties for the Horn pair; see Propositions 22 and 23 in Section 4. The examples in Section 5 show that only a fraction of Huh's pairs $(H, \lambda)$ are Horn pairs.

Different Horn pairs may give rise to the same Horn map. For example, the Horn pair

$$
H^{\prime}=\left(\begin{array}{ccc}
0 & 2 & 2 \\
2 & 1 & 0 \\
0 & -1 & -1 \\
-2 & -2 & -1
\end{array}\right) \quad \text { and } \quad \lambda^{\prime}=\left(1,-\frac{1}{4}, \frac{1}{4}\right)
$$

also gives the map in Example 2. This is because the first and third rows of $H^{\prime}$ are collinear, causing the cancellation of linear factors in the Horn map. Following [2], a Horn pair $(H, \lambda)$ is minimal if the matrix $H$ has no zero rows and no pair of collinear rows.

Lemma 3. Let $\left(H^{\prime}, \lambda^{\prime}\right)$ be a Horn pair arising from the Horn pair $(H, \lambda)$ by replacing two collinear rows $r_{k}$ and $r_{\ell}$ in $H$ such that $r_{\ell}=\mu r_{k}$ with their sum $r_{k}+r_{\ell}$ and setting

$$
\lambda_{j}^{\prime}=\frac{\lambda_{j} \mu^{\mu \cdot h_{k j}}}{(1+\mu)^{(1+\mu) h_{k j}}} \quad \text { for all } j=0, \ldots, n
$$

Then the Horn maps $\varphi_{\left(H^{\prime}, \lambda^{\prime}\right)}$ and $\varphi_{(H, \lambda)}$ are equal.
Proof. Let $w_{k}$ and $w_{\ell}$ be the linear forms associated to the rows $r_{k}$ and $r_{\ell}$, respectively. Fix a column index $j$. We have $w_{\ell}=\mu w_{k}$ and $h_{\ell j}=\mu h_{k j}$. The factors of the $j$ th coordinates of the Horn maps $\varphi_{(H, \lambda)}$ and $\varphi_{\left(H^{\prime}, \lambda^{\prime}\right)}$ that have changed after the operation are $\lambda_{j} w_{k}^{b_{k j}} w_{\ell}^{b_{\ell j}}=\lambda_{j} \mu^{\mu \cdot h_{k j}} w_{k}^{(1+\mu) h_{k j}}$ for $(H, \lambda)$ and $\lambda_{j}^{\prime}\left(w_{k}+w_{\ell}\right)^{(1+\mu) h_{k j}}=\lambda_{j}^{\prime}(1+\mu)^{(1+\mu) h_{k j}} w_{k}^{(1+\mu) h_{k j}}$ for $\left(H^{\prime}, \lambda^{\prime}\right)$. Equating these two gives the desired formula.

Every Horn map is represented by a unique minimal Horn pair. This follows by unique factorization; see also [2], Proposition 6.11. To make a Horn pair minimal, while retaining the Horn map, we can use Lemma 3 repeatedly, deleting zero rows as they appear.

Example 4. We illustrate the equivalence of (1) and (2) in Theorem 1 for the model described in [11], Example 3.11. Here, $n=3$ and $m=4$ and the Horn matrix equals

$$
H=\left(\begin{array}{cccc}
-1 & -1 & -2 & -2 \\
1 & 0 & 3 & 2 \\
1 & 3 & 0 & 2 \\
-1 & -2 & -1 & -2
\end{array}\right)
$$

This Horn matrix is friendly because the following vector satisfies the identity (3):

$$
\lambda=\left(\lambda_{0}, \lambda_{1}, \lambda_{2}, \lambda_{3}\right)=\left(\frac{2}{3},-\frac{4}{27},-\frac{4}{27}, \frac{1}{27}\right)
$$

The pair $(H, \lambda)$ is a Horn pair, with associated Horn map

$$
\begin{aligned}
\varphi_{(H, \lambda)}: \quad \mathbb{R}_{>0}^{4} & \rightarrow \mathbb{R}_{>0}^{4} \\
\left(\begin{array}{l}
u_{0} \\
u_{1} \\
u_{2} \\
u_{3}
\end{array}\right) & \mapsto\left(\begin{array}{c}
\frac{2\left(u_{0}+3 u_{2}+2 u_{3}\right)\left(u_{0}+3 u_{1}+2 u_{3}\right)}{3\left(u_{0}+u_{1}+2 u_{2}+2 u_{3}\right)\left(u_{0}+2 u_{1}+u_{2}+2 u_{3}\right)} \\
\frac{4\left(u_{0}+3 u_{1}+2 u_{3}\right)^{3}}{27\left(u_{0}+u_{1}+2 u_{2}+2 u_{3}\right)\left(u_{0}+2 u_{1}+u_{2}+2 u_{3}\right)^{2}} \\
\frac{4\left(u_{0}+3 u_{2}+2 u_{3}\right)^{3}}{27\left(u_{0}+u_{1}+2 u_{2}+2 u_{3}\right)^{2}\left(u_{0}+2 u_{1}+u_{2}+2 u_{3}\right)} \\
\frac{\left(u_{0}+3 u_{2}+2 u_{3}\right)^{2}\left(u_{0}+3 u_{1}+2 u_{3}\right)^{2}}{27\left(u_{0}+u_{1}+2 u_{2}+2 u_{3}\right)^{2}\left(u_{0}+2 u_{1}+u_{2}+2 u_{3}\right)^{2}}
\end{array}\right)
\end{aligned}
$$

Indeed, this rational function takes positive vectors to positive vectors. The image of the map $\varphi_{(H, \lambda)}$ is a subset $\mathcal{M}$ of the tetrahedron $\Delta_{3}=\left\{p \in \mathbb{R}_{>0}^{4}: p_{0}+p_{1}+p_{2}+p_{3}=1\right\}$. We regard the subset $\mathcal{M}$ as a discrete statistical model on the state space $\{0,1,2,3\}$. The model $\mathcal{M}$ is the curve of degree 4 inside $\Delta_{3}$ defined by the two quadratic equations

$$
9 p_{1} p_{2}-8 p_{0} p_{3}=p_{0}^{2}-12 p_{3}=0
$$

As in [11], Example 3.11, one verifies that $\mathcal{M}$ has rational MLE, namely $\Phi=\varphi_{(H, \lambda)}$.
We next define all the terms used in part (3) of Theorem 1. Fix a matrix $A=\left(a_{i j}\right) \in \mathbb{Z}^{r \times m}$ of rank $r$ that has the vector $(1, \ldots, 1)$ in its row span. The connection to part (2) of Theorem 1 will be that the rows of $A$ span the left kernel of $H$. We identify the columns of $A$ with Laurent monomials in $r$ unknowns $t_{1}, \ldots, t_{r}$. The associated monomial map is

$$
\gamma_{A}: \quad\left(\mathbb{R}^{*}\right)^{r} \rightarrow \mathbb{R} \mathbb{P}^{m-1}, \quad\left(t_{1}, \ldots, t_{r}\right) \mapsto\left(\prod_{i=1}^{r} t_{i}^{a_{i 1}}: \prod_{i=1}^{r} t_{i}^{a_{i 2}}: \cdots: \prod_{i=1}^{r} t_{i}^{a_{i m}}\right)
$$

Here, $\mathbb{R}^{*}=\mathbb{R} \backslash\{0\}$ and $\mathbb{R} \mathbb{P}^{m-1}$ denotes the real projective space of dimension $m-1$. Let $Y_{A}$ be the closure of the image of $\gamma_{A}$. This is the projective toric variety given by $A$.

Every point $x=\left(x_{1}: \cdots: x_{m}\right)$ in the dual projective space $\left(\mathbb{R P}^{m-1}\right)^{\vee}$ corresponds to a hyperplane $H_{x}$ in $\mathbb{R} \mathbb{P}^{m-1}$. The dual variety $Y_{A}^{*}$ to the toric variety $Y_{A}$ is the closure of

$$
\left\{x \in\left(\mathbb{R} \mathbb{P}^{m-1}\right)^{\vee} \mid \gamma_{A}^{-1}\left(H_{x} \cap Y_{A}\right) \text { is singular }\right\}
$$

Here, the term singular means that the variety $\gamma_{A}^{-1}\left(H_{x} \cap Y_{A}\right)$ has a singular point in $\left(\mathbb{R}^{*}\right)^{r}$. A general point $x$ in $Y_{A}^{*}$ hence corresponds to a hyperplane $H_{x}$ that is tangent to the toric variety $Y_{A}$ at a point $\gamma_{A}(t)$ with nonzero coordinates. We identify sign vectors $\sigma \in\{-1,+1\}^{m}$ with orthants in $\mathbb{R}^{m}$. These map in a 2-to-1 manner to orthants in $\mathbb{R} \mathbb{P}^{m-1}$. If we intersect them with $Y_{A}^{*}$, then we get the orthants of the dual toric variety:

$$
Y_{A, \sigma}^{*}=\left\{x \in Y_{A}^{*}: \sigma_{i} \cdot x_{i}>0 \text { for } i=1,2, \ldots, m\right\} \subset \mathbb{R} \mathbb{P}^{m-1}
$$

One of these is the distinguished orthant in Theorem 1, part (3).
Example 5. Fix $m=4$ and $r=2$. The following matrix has $(1,1,1,1)$ in its row span:

$$
A=\left(\begin{array}{llll}
3 & 2 & 1 & 0 \\
0 & 1 & 2 & 3
\end{array}\right)
$$

As in [11], Example 3.9, the toric variety of $A$ is the twisted cubic curve in 3-space:

$$
Y_{A}=\overline{\left\{\left(t_{1}^{3}: t_{1}^{2} t_{2}: t_{1} t_{2}^{2}: t_{2}^{3}\right) \in \mathbb{R P}^{3}: t_{1}, t_{2} \in \mathbb{R}^{*}\right\}}
$$

The dual toric variety $Y_{A}^{*}$ is a surface in $\left(\mathbb{R P}^{3}\right)^{\vee}$. Its points $x$ represent planes in $\mathbb{R P}^{3}$ that are tangent to the curve $Y_{A}$. Such a tangent plane corresponds to a cubic $x_{1} t^{3}+x_{2} t^{2}+x_{3} t+x_{4}$ with a double root. Just as we recognize quadrics with a double root by the vanishing of the quadratic discriminant, a cubic with coefficients $\left(x_{1}, x_{2}, x_{3}, x_{4}\right)$ has a double root if and only if the following discriminant vanishes:

$$
\Delta_{A}=\underline{27 x_{1}^{2} x_{4}^{2}}-18 x_{1} x_{2} x_{3} x_{4}+4 x_{1} x_{3}^{3}+4 x_{2}^{3} x_{4}-x_{2}^{2} x_{3}^{2}
$$

Hence, $Y_{A}^{*}$ is the surface of degree 4 in $\left(\mathbb{RP}^{3}\right)^{\vee}$ defined by $\Delta_{A}$. All eight orthants $Y_{A, \sigma}^{*}$ are nonempty. The coefficient vectors of the following eight cubics lie on different orthants:

$$
\begin{array}{llll}
(t+1)^{2}(t+3), & (t+5)^{2}(t-1), & (t-1)^{2}(t+3), & (t+5)^{2}(t-8) \\
(t-3)^{2}(t+1), & (t-1)^{2}(t-3), & (t-2)^{2}(t+3), & (t+1)^{2}(t-3)
\end{array}
$$

For instance, the underlined cubic corresponds to the point $x=(1,-1,-8,12)$ in the orthant $Y_{A, \sigma}^{*}$ associated with the sign vector $\sigma=(+1,-1,-1,+1)$.

Let $\Delta$ be a homogeneous polynomial in $m$ variables with $n+2$ monomials and $\mathbf{m}$ one of these monomials. There is a one-to-one correspondence between such pairs $(\Delta, \mathbf{m})$ and pairs $(H, \lambda)$ where $H$ is a Horn matrix of size $m \times(n+1)$ and $\lambda$ is a coefficient vector. Namely, for $k=0, \ldots, n$ write $h_{k}^{+}$, respectively, $h_{k}^{-}$for the positive, respectively, negative part of the column vector $h_{k}$, so that $h_{k}=$ $h_{k}^{+}-h_{k}^{-}$. In addition, let $\max _{k}\left(h_{k}^{-}\right)$be the entrywise maximum of the $h_{k}^{-}$. We pass from pairs $(H, \lambda)$ to pairs $(\Delta, \mathbf{m})$ as follows:

$$
\mathbf{m}=x^{\max _{k}\left(h_{k}^{-}\right)} \quad \text { and } \quad \Delta=\mathbf{m} \cdot\left(1-\sum_{k=0}^{n} \lambda_{k} x^{h_{k}}\right)
$$

For the converse, from pairs $(\Delta, \mathbf{m})$ to pairs $(H, \lambda)$, we divide $\Delta$ by $\mathbf{m}$ and use the same equations to determine the pair $(H, \lambda)$. Note that the polynomial $\Delta$ being homogeneous and the matrix $H$ being a Horn matrix are equivalent conditions using the equations (12). Given a pair $(\Delta, \mathbf{m})$ with associated pair $(H, \lambda)$, we define the monomial map

$$
\phi_{(\Delta, \mathbf{m})}: \quad\left(\mathbb{R}^{*}\right)^{m} \rightarrow \mathbb{R}^{n+1}, \quad x \mapsto\left(\lambda_{0} x^{h_{0}}, \lambda_{1} x^{h_{1}}, \ldots, \lambda_{n} x^{h_{n}}\right)
$$

We now present the definition that is needed for part (3) of Theorem 1.
Definition 6. A discriminantal triple $(A, \Delta, \mathbf{m})$ consists of

1. an $r \times m$ integer matrix $A$ of rank $r$ having $(1,1, \ldots, 1)$ in its row span,
2. an $A$-homogeneous polynomial $\Delta$ that vanishes on the dual toric variety $Y_{A}^{*}$,
3. a distinguished term $\mathbf{m}$ among those that occur in the polynomial $\Delta$,
such that the pair $(H, \lambda)$ associated to $(\Delta, \mathbf{m})$ is a Horn pair. Here, the polynomial $\Delta$ being $A$ homogeneous means that $A v=A w$ for any two exponent vectors $v$ and $w$ of $\Delta$.

All definitions are now complete. We illustrate Definition 6 for our running example:
Example 7. Let $A$ be the $2 \times 4$ matrix in (10), $\Delta=\Delta_{A}$ its discriminant in (11), and $\mathbf{m}=$ $27 x_{1}^{2} x_{4}^{2}$ the special term. Then $(A, \Delta, \mathbf{m})$ is a discriminantal triple with associated sign vector $\sigma=(+1,-1,-1,+1)$. The orthant $Y_{A, \sigma}^{*}$, highlighted in Example 5, is a semialgebraic surface in $Y_{A}^{*} \subset \mathbb{R}^{3}$. This surface is mapped into the tetrahedron $\Delta_{3}$ by

$$
\phi_{(\Delta, \mathbf{m})}: \quad\left(x_{1}, x_{2}, x_{3}, x_{4}\right) \mapsto\left(\frac{2}{3} \frac{x_{2} x_{3}}{x_{1} x_{4}},-\frac{4}{27} \frac{x_{3}^{3}}{x_{1} x_{4}^{2}},-\frac{4}{27} \frac{x_{2}^{3}}{x_{1}^{2} x_{4}}, \frac{1}{27} \frac{x_{2}^{2} x_{3}^{2}}{x_{1}^{2} x_{4}^{2}}\right)
$$

The image of this map is a curve in $\Delta_{3}$, namely the model $\mathcal{M}$ in Example 4. We verify (1) by comparing (7) with (13). The former is obtained from the latter by setting $x=H u$.

# 3. Staged trees 

We consider contingency tables $u=\left(u_{i_{1} i_{2} \cdots i_{m}}\right)$ of format $r_{1} \times r_{2} \times \cdots \times r_{m}$. Following [4,14], these represent joint distributions of discrete statistical models with $n+1=r_{1} r_{2} \cdots r_{m}$ states. Namely, the contingency table $u$ represents the probability distribution $p:=u /|u|$. For any subset $C \subset\{1, \ldots, m\}$, one considers the marginal table $u_{C}$ that is obtained by summing out all indices not in $C$. The entries of the marginal table $u_{C}$ are sums of entries in $u$. To obtain the entry $u_{I, C}$ of $u_{C}$ for any state $I=$ $\left(i_{1}, i_{2}, \ldots, i_{m}\right)$, we fix the indices of the states in $C$ and sum over the indices not in $C$. For example, if $m=4, C=\{1,3\}, I=(i, j, k, l)$, then $u_{C}$ is the $r_{1} \times r_{3}$ matrix with entries

$$
u_{I, C}=u_{i+k+}=\sum_{j=1}^{r_{2}} \sum_{l=1}^{r_{4}} u_{i j k l}
$$

Such linear forms are the basic building blocks for familiar models with rational MLE.
Consider an undirected graph $G$ with vertex set $\{1, \ldots, m\}$ which is assumed to be chordal. The associated decomposable graphical model $\mathcal{M}_{G}$ in $\Delta_{n}$ has the rational MLE

$$
\hat{p}_{I}=\frac{\prod_{C} u_{I, C}}{\prod_{S} u_{I, S}}
$$

where the product in the numerator is over all maximal cliques $C$ of $G$, and the product in the denominator is over all separators $S$ in a junction tree for $G$. See [14], §4.4.1. We shall regard $G$ as a directed graph, with edge directions given by a perfect elimination ordering on the vertex set $\{1, \ldots, m\}$. This turns $\mathcal{M}_{G}$ into a Bayesian network. More generally, a Bayesian network $\mathcal{M}_{G}$ is given by a directed acyclic graph $G$. We write $\mathrm{pa}(j)$ for the set of parents of the node $j$. The model $\mathcal{M}_{G}$ in $\Delta_{n}$ has the rational MLE

$$
\hat{p}_{I}=\prod_{j=1}^{m} \frac{u_{I, \mathrm{pa}(j) \cup\{j\}}}{u_{I, \mathrm{pa}(j)}}
$$

If $G$ comes from an undirected chordal graph, then (14) arises from (15) by cancellations.
Example $8(m=4)$. We revisit two examples from on page 36 in [4], §2.1. The star graph $G=$ [14][24][34] is chordal. The MLE for $\mathcal{M}_{G}$ is the map $\Phi$ with coordinates

$$
\hat{p}_{i j k l}=\frac{u_{i++l} \cdot u_{+j+l} \cdot u_{++k l}}{u_{++++} \cdot u_{+++l}^{2}}=\frac{u_{i+++}}{u_{++++}} \cdot \frac{u_{+j+l}}{u_{+++l}} \cdot \frac{u_{++k l}}{u_{++++}} \cdot \frac{u_{i++l}}{u_{i+++}}
$$

The left expression is (14). The right is (15) for the directed graph $1 \rightarrow 4,4 \rightarrow 2,4 \rightarrow 3$.
The chain graph $G=[12][23][34]$ is chordal. Its MLE is the map $\Phi$ with coordinates

$$
\hat{p}_{i j k l}=\frac{u_{i j++} \cdot u_{+j k+} \cdot u_{++k l}}{u_{+j++} \cdot u_{++k+} \cdot u_{++++}}=\varphi_{(H, \lambda)}(u)_{i j k l}
$$

This is the Horn map given by the matrix $H$ in Figure 1 and $\lambda=(1, \ldots, 1)$.
The formulas (14) and (15) are familiar to statisticians. Theorem 1 places them into a larger context. However, some readers may find our approach too algebraic and too general. Our aim in this section is to lay out a useful middle ground: staged tree models.

Staged trees were introduced by Smith and Anderson [16] as a generalization of discrete Bayesian networks. They furnish an intuitive representation of many situations that the above graphs $G$ cannot capture. In spite of their wide scope, staged tree models are appealing because of their intuitive formalism for encoding events. For an introduction, see the textbook [3]. In what follows, we study parts (1) and (2) in Theorem 1 for staged trees.

To define a staged tree model, we consider a directed rooted tree $\mathcal{T}$ with at least two edges emanating from each nonleaf vertex, a label set $S=\left\{s_{i} \mid i \in I\right\}$ and a labeling $\theta: \mathrm{E}(\mathcal{T}) \rightarrow S$ of the edges of the tree. Each vertex of $\mathcal{T}$ has a corresponding floret, which is the multiset of edge labels emanating from it. The labeled tree $\mathcal{T}$ is a staged tree if any two florets are either equal or disjoint. Two vertices in $\mathcal{T}$ are in the same stage if their corresponding florets are the same. From now on, $F$ denotes the set of florets of $\mathcal{T}$.

Definition 9. Let $J$ be the set of root-to-leaf paths in the tree $\mathcal{T}$. We set $|J|=n+1$. For $i \in I$ and $j \in J$, let $\mu_{i j}$ denote the number of times edge label $s_{i}$ appears in the $j$ th root-to-leaf path. The staged tree model $\mathcal{M}_{\mathcal{T}}$ is the image of the parametrization

$$
\phi_{\mathcal{T}}: \quad \Theta \rightarrow \Delta_{n}, \quad\left(s_{i}\right)_{i \in I} \mapsto\left(p_{j}\right)_{j \in J}
$$

where the parameter space is $\Theta:=\left\{\left(s_{i}\right)_{i \in I} \in(0,1)^{|I|}: \sum_{s_{i} \in f} s_{i}=1\right.$ for all florets $\left.f \in F\right\}$, and $p_{j}=$ $\prod_{i \in I} s_{i}^{\mu_{i j}}$ is the product of the edge parameters on the $j$ th root-to-leaf path.

In the model $\mathcal{M}_{\mathcal{T}}$, the tree $\mathcal{T}$ represents possible sequences of events. The parameter $s_{i}$ associated to an edge $v v^{\prime}$ is the transition probability from $v$ to $v^{\prime}$. All parameter labels in a floret sum to 1 . The fact that distinct nodes in $\mathcal{T}$ can have the same floret of parameter labels enables staged tree models to encode conditional independence statements [16]. This allows us to represent any discrete Bayesian network or decomposable model as a staged tree model. Our first staged tree was seen in Example 2. Here is another specimen.

Example $10(n=15)$. Consider the decomposable model for binary variables given by the 4 -chain $G=[12][23][34]$ as in Example 8. Figure 1 shows a realization of $\mathcal{M}_{G}$ as a staged tree model $\mathcal{M}_{\mathcal{T}}$. The leaves of $\mathcal{T}$ represent the outcome space $\{0,1\}^{4}$. Nodes with the same color have the same associated floret. The blank nodes all have different florets. The seven florets of $\mathcal{T}$ are

$$
\begin{aligned}
& f_{1}=\left\{s_{0}, s_{1}\right\}, \quad f_{2}=\left\{s_{2}, s_{3}\right\}, \quad f_{3}=\left\{s_{4}, s_{5}\right\}, \quad f_{4}=\left\{s_{6}, s_{7}\right\}, \quad f_{5}=\left\{s_{8}, s_{9}\right\}, \\
& f_{6}=\left\{s_{10}, s_{11}\right\}, \quad f_{7}=\left\{s_{12}, s_{13}\right\} .
\end{aligned}
$$

Next, we show that staged tree models have rational MLE, so they satisfy part (1) of Theorem 1. Our formula for $\Phi$ uses the notation for $I, J$ and $\mu_{i j}$ introduced in Definition 9. This formula is known in the literature on chain event graphs (see, e.g., [15]).

Proposition 11. Let $\mathcal{M}_{\mathcal{T}}$ be a staged tree model, and let $u=\left(u_{j}\right)_{j \in J}$ be a vector of counts. For $i \in I$, let $f$ be the floret containing the label $s_{i}$, and define the estimates

$$
\hat{s}_{i}:=\frac{\sum_{j} \mu_{i j} u_{j}}{\sum_{s_{i} \in f} \sum_{j} \mu_{i j} u_{j}} \quad \text { and } \quad \hat{p}_{j}:=\prod_{i \in I}\left(\hat{s}_{i}\right)^{\mu_{i j}}
$$

The rational function $\Phi$ that sends $\left(u_{j}\right)_{j \in J}$ to $\left(\hat{p}_{j}\right)_{j \in J}$ is the MLE of the model $\mathcal{M}_{\mathcal{T}}$.

![img-1.jpeg](img-1.jpeg)

Figure 1. A staged tree $\mathcal{T}$ and its Horn matrix $H$ from Proposition 11. Entries - indicate -1 .

Proof. We prove that the likelihood function $L(p, u)$ has a unique maximum at $p=\left(\hat{p}_{j}\right)_{j \in J}$. For a floret $f \in F$, we fix the vector of parameters $s_{f}=\left(s_{i}\right)_{s_{i} \in f}$, and we define the local likelihood function $L_{f}\left(s_{f}, u\right)=\prod_{s_{i} \in f} s_{i}^{\alpha_{i}}$, where $\alpha_{i}=\sum_{j} \mu_{i j} u_{j}$. We have

$$
L(p, u)=\prod_{j} p_{j}^{\alpha_{j}}=\prod_{j} \prod_{i} s_{i}^{\alpha_{j} \mu_{i j}}=\prod_{i} s_{i}^{\alpha_{i}}=\prod_{f \in F} L_{f}\left(s_{f}, u\right)
$$

Since the $L_{f}$ depend on disjoint sets of unknowns, maximizing $L$ is achieved by maximizing the factors $L_{f}$ separately. But $L_{f}$ is the likelihood function of the full model $\Delta_{|f|-1}$, given the data vector $\left(\alpha_{i}\right)_{s_{i} \in f}$. The MLE of that model is $\hat{s}_{i}=\alpha_{i} / \sum_{s_{\ell} \in f} \alpha_{\ell}$, where $s_{i} \in f$. We conclude that $\operatorname{argmax}_{s_{f}}\left(L_{f}\left(s_{f}, u\right)\right)=\left(\hat{s}_{i}\right)_{s_{i} \in f}$ and $\operatorname{argmax}_{p}(L(p, u))=\left(\hat{p}_{j}\right)_{j \in J}$.

Remark 12. Here is a method for evaluating the MLE in Proposition 11. Let $[v] \subset J$ be the set of root-to-leaf paths through a node $v$ in the tree $\mathcal{T}$ and define $u_{[v]}=\sum_{j \in[v]} u_{j}$. The ratio $\frac{u_{[v]}}{u_{[v]}}$ is the empirical transition probability from $v$ to $v^{\prime}$ given arrival at $v$. To obtain $\hat{s}_{i}$ we first compute the quotients $\frac{u_{[v^{\prime}]}}{u_{[v]}}$ for all edges $v v^{\prime}$ with parameter label $s_{i}$. We aggregate them by adding their numerators and denominators separately. This gives $\hat{s}_{i}=\left(\sum u_{[v^{\prime}]}\right) /\left(\sum u_{[v]}\right)$, where both sums range over all edges $v v^{\prime}$ with parameter label $s_{i}$.

Proposition 11 yields an explicit description of the Horn pair $(H, \lambda)$ associated to $\mathcal{M}_{\mathcal{T}}$.
Corollary 13. Fix a staged tree model $\mathcal{M}_{\mathcal{T}}$ as above. Let $H$ be the $(|I|+|F|) \times|J|$ matrix whose rows are indexed by the set $I \sqcup F$ and entries are given by

$$
\begin{aligned}
h_{i j} & =\mu_{i j} \quad \text { for } i \in I, \quad \text { and } \\
h_{f j} & =-\sum_{s_{\ell} \in f} \mu_{\ell j} \quad \text { for } f \in F
\end{aligned}
$$

Define $\lambda \in\{-1,+1\}^{|J|}$ by $\lambda_{j}=(-1)^{\sum_{f} h_{f j}}$. Then $(H, \lambda)$ is a Horn pair for $\mathcal{M}_{\mathcal{T}}$.

Given a staged tree $\mathcal{T}$, we call the matrix $H$ in Corollary 13 the Horn matrix of $\mathcal{T}$.
Remark 14. In Corollary 13, for a floret $f$, let $H_{f}$ be the submatrix of $H$ with row indices $\left\{i: s_{i} \in\right.$ $f\} \cup\{f\}$. Then $H$ is the vertical concatenation of the matrices $H_{f}$ for $f \in F$.

Example 15. For the tree $\mathcal{T}$ in Example 10, the Horn matrix $H$ of $\mathcal{M}_{\mathcal{T}}$ is given in Figure 1. The vector $\lambda$ of the Horn pair $(H, \lambda)$ is the vector of ones $(1, \ldots, 1) \in \mathbb{R}^{16}$. The rows of $H$ are indexed by the florets and labels

$$
\left(s_{0}, s_{1}, f_{1}, s_{2}, s_{3}, f_{2}, s_{4}, s_{5}, f_{3}, s_{6}, s_{7}, f_{4}, s_{8}, s_{9}, f_{5}, s_{10}, s_{11}, f_{6}, s_{12}, s_{13}, f_{7}\right)
$$

Note that $(H, \lambda)$ is not minimal. Following the recipe in Lemma 3, we can delete the rows $s_{0}, s_{1}, f_{2}, f_{3}$ of the matrix $H$ by summing the pairs $\left(s_{0}, f_{2}\right)$ and $\left(s_{1}, f_{3}\right)$ and deleting zero rows. The result is the minimal Horn pair $\left(H^{\prime}, \lambda^{\prime}\right)$, where $\lambda^{\prime}=(-1, \ldots,-1)$.

Two staged trees $\mathcal{T}$ and $\mathcal{T}^{\prime}$ are called statistically equivalent in [8] if there exists a bijection between the sets of root-to-leaf paths of $\mathcal{T}$ and $\mathcal{T}^{\prime}$ such that, after applying this bijection, $\mathcal{M}_{\mathcal{T}}=\mathcal{M}_{\mathcal{T}^{\prime}}$ in the open simplex $\Delta_{n}$. A staged tree model may have different but statistically equivalent tree representations. In [8], Theorem 1, it is shown that statistical equivalence of staged trees can be determined by a sequence of operations on the trees, named swap and resize. One of the advantages of describing a staged tree model via its Horn pair is that it gives a new criterion to decide whether two staged trees are statistically equivalent. This is simpler to implement than the criterion given in [8].

Corollary 16. Two staged trees are statistically equivalent if and only if their associated Horn pairs reduce to the same minimal Horn pair.

One natural operation on a staged tree $\mathcal{T}$ is identifying two florets of the same size. This gives a new staged tree $\mathcal{T}^{\prime}$ whose Horn matrix is easy to get from that of $\mathcal{T}$.

Corollary 17. Let $\mathcal{T}^{\prime}$ be a staged tree arising from $\mathcal{T}$ by identifying two florets $f$ and $f^{\prime}$, say by the bijection $(-)^{\prime}: f \rightarrow f^{\prime}$. The Horn matrix $H^{\prime}$ of $\mathcal{M}_{\mathcal{T}^{\prime}}$ arises from the Horn matrix $H$ of $\mathcal{M}_{\mathcal{T}}$ by replacing the blocks $H_{f}$ and $H_{f^{\prime}}$ in $H$ by the block $H_{f}^{\prime}$ defined by

$$
\begin{aligned}
h_{i j}^{\prime} & =h_{i j}+h_{i^{\prime} j} \quad \text { for } s_{i} \in f \\
h_{f j}^{\prime} & =h_{f j}+h_{f^{\prime} j}
\end{aligned}
$$

Proof. This follows from the definition of the Horn matrices for $\mathcal{M}_{\mathcal{T}}$ and $\mathcal{M}_{\mathcal{T}^{\prime}}$.
Example 18. Let $\mathcal{T}^{\prime}$ be the tree obtained from Example 10 by identifying florets $f_{4}$ and $f_{5}$ in $\mathcal{T}$. Then $\mathcal{M}_{\mathcal{T}^{\prime}}$ is the independence model of two random variables with four states.

Now we turn to part (3) of Theorem 1. We describe the triple $(A, \Delta, \mathbf{m})$ for a staged tree model $\mathcal{M}_{\mathcal{T}}$. The pair $(H, \lambda)$ was given in Corollary 13. Let $A$ be any matrix whose rows span the left kernel of $H$, set $m=|I|+|F|$, and write $s$ for the $m$-tuple of parameters $\left(s_{i}, s_{f}\right)_{i \in I, f \in F}$. From the Horn matrix in Corollary 13, we see that

$$
\Delta=\mathbf{m} \cdot\left(1-\sum_{j}(-1)^{e_{j}} \prod_{i}\left(\frac{s_{i}}{s_{f}}\right)^{\mu_{i j}}\right)
$$

where $f$ depends on $i, \mathbf{m}=\operatorname{lcm}\left(\prod_{i} s_{f}^{\mu_{i j}}: f \in F\right)$ and $\epsilon_{j}=\sum_{i} \mu_{i j}$. The sign vector $\sigma$ for the triple $(A, \Delta, \mathbf{m})$ is given by $\sigma_{i}=+1$ for $i \in I$ and $\sigma_{f}=-1$ for $f \in F$. Then $Y_{A, \sigma}^{*}$ gets mapped to $\mathcal{M}_{\mathcal{T}}$ via $\phi_{(\Delta, \mathbf{m})}$. Moreover, the map $\phi_{\mathcal{T}}$ from Definition 9 factors through $\phi_{(\Delta, \mathbf{m})}$. Indeed, if we define $\iota: \Theta \rightarrow Y_{A, \sigma}^{*}$ by $\left(s_{i}\right)_{i \in I} \mapsto\left(s_{i},-1\right)_{i \in I, f \in F}$, then $\phi_{\mathcal{T}}=\phi_{(\Delta, \mathbf{m})} \circ \iota$. The following derivation is an extension of that in [11], Example 3.13.

Example 19. Let $\mathcal{M}_{\mathcal{T}}$ be the 4 -chain model in Example 10. Here, the discriminant is

$$
\begin{aligned}
\Delta= & f_{1} f_{2} f_{3} f_{4} f_{5} f_{6} f_{7} \\
& -s_{0} s_{2} s_{6} s_{10} f_{3} f_{5} f_{7}-s_{0} s_{2} s_{6} s_{11} f_{3} f_{5} f_{7}-s_{0} s_{2} s_{7} s_{12} f_{3} f_{5} f_{6}-s_{0} s_{2} s_{7} s_{13} f_{3} f_{5} f_{6} \\
& -s_{0} s_{3} s_{8} s_{10} f_{3} f_{4} f_{7}-s_{0} s_{3} s_{8} s_{11} f_{3} f_{4} f_{7}-s_{0} s_{3} s_{9} s_{12} f_{3} f_{4} f_{6}-s_{0} s_{3} s_{9} s_{13} f_{3} f_{4} f_{6} \\
& -s_{1} s_{4} s_{6} s_{10} f_{2} f_{5} f_{7}-s_{1} s_{4} s_{6} s_{11} f_{2} f_{5} f_{7}-s_{1} s_{4} s_{7} s_{12} f_{2} f_{5} f_{6}-s_{1} s_{4} s_{7} s_{13} f_{2} f_{5} f_{6} \\
& -s_{1} s_{5} s_{8} s_{10} f_{2} f_{4} f_{7}-s_{1} s_{5} s_{8} s_{11} f_{2} f_{4} f_{7}-s_{1} s_{5} s_{9} s_{12} f_{2} f_{4} f_{6}-s_{1} s_{5} s_{9} s_{13} f_{2} f_{4} f_{6} .
\end{aligned}
$$

Our notation for the parameters matches the row labels of the Horn matrix $H$ in Figure 1. This polynomial of degree 7 is irreducible, so it equals the $A$-discriminant: $\Delta=\Delta_{A}$. The underlying matrix $A$ has format $13 \times 21$, and we represent it by its associated toric ideal

$$
\begin{aligned}
I_{A}= & \left\langle s_{10}-s_{11}, s_{1} s_{5} f_{2}-s_{0} s_{3} f_{3}, s_{1} s_{4} f_{2}-s_{0} s_{2} f_{3}, s_{5} s_{9} f_{4}-s_{4} s_{7} f_{5}, s_{3} s_{9} f_{4}-s_{2} s_{7} f_{5}\right. \\
& s_{12}-s_{13}, s_{5} s_{8} f_{4}-s_{4} s_{6} f_{5}, s_{3} s_{8} f_{4}-s_{2} s_{6} f_{5}, s_{9} s_{13} f_{6}-s_{8} s_{11} f_{7}, s_{7} s_{13} f_{6}-s_{6} s_{11} f_{7} \\
& s_{0} s_{2} s_{6} s_{11}-f_{1} f_{2} f_{4} f_{6}, s_{0} s_{2} s_{7} s_{13}-f_{1} f_{2} f_{4} f_{7}, s_{0} s_{3} s_{8} s_{11}-f_{1} f_{2} f_{5} f_{6} \\
& s_{0} s_{3} s_{9} s_{13}-f_{1} f_{2} f_{5} f_{7}, s_{1} s_{4} s_{6} s_{11}-f_{1} f_{3} f_{4} f_{6}, s_{1} s_{4} s_{7} s_{13}-f_{1} f_{3} f_{4} f_{7} \\
& s_{1} s_{5} s_{9} s_{13}-f_{1} f_{3} f_{5} f_{7}, s_{1} s_{5} s_{8} s_{11}-f_{1} f_{3} f_{5} f_{6}\right\rangle
\end{aligned}
$$

The toric variety $Y_{A}=\mathcal{V}\left(I_{A}\right)$ has dimension 12 and degree 141. It lives in a linear space of codimension 2 in $\mathbb{P}^{20}$, where it is defined by eight cubics and eight quartics. The dual variety $Y_{A}^{*}=\mathcal{V}\left(\Delta_{A}\right)$ is the above hypersurface of degree seven. We have $\mathbf{m}=f_{1} f_{2} f_{3} f_{4} f_{5} f_{6} f_{7}$, and $\sigma$ is the vector in $[-1,+1]^{21}$ that has entry +1 at the indices corresponding to the $s_{i}$ and entry -1 at the indices corresponding to the $f_{i}$.

It would be interesting to study the combinatorics of discriminantal triples for staged tree models. Our computations suggest that, for many such models, the polynomial $\Delta$ is irreducible and equals the $A$-discriminant $\Delta_{A}$ of the underlying configuration $A$. However, this is not true for all staged trees, as seen in equation (2) of Example 2. We close this section with a familiar class of models with rational MLE whose associated $\Delta$ factor.

Example 20. The multinomial distribution encodes the experiment of rolling a $k$-sided die $m$ times and recording the number of times one observed the $j$ th side, for $j=1, \ldots, k$. The associated model $\mathcal{M}$ is the independence model for $m$ identically distributed random variables on $k$ states. We have $n+1=\binom{k+m-1}{m}$. The Horn matrix $H$ is the $(k+1) \times(n+1)$ matrix whose columns are the vectors $\left(-m, i_{1}, i_{2}, \ldots, i_{k}\right)^{T}$ where $i_{1}, i_{2}, \ldots, i_{k}$ are nonnegative integers whose sum equals $m$. Here, $A=$ $(11 \cdots 1)$, so the $A$-discriminant equals $\Delta_{A}=x_{0}+x_{1}+\cdots+x_{k}$. The following polynomial is a multiple of $\Delta_{A}$ :

$$
\Delta=\left(-x_{0}\right)^{m}-\left(x_{1}+x_{2}+\cdots+x_{k}\right)^{m}
$$

This $\Delta$, with its marked term $\mathbf{m}=\left(-x_{0}\right)^{m}$, encodes the MLE for the model $\mathcal{M}$ :

$$
\hat{p}_{\left(i_{1}, \ldots, i_{k}\right)}=\prod_{j=1}^{k}\left(\frac{\sum_{|I|=m} u_{I} \cdot I_{j}}{m \sum_{|I|=m} u_{I}}\right)^{i_{j}}
$$

Here, $I$ ranges over all vectors in $\mathbb{N}^{k}$ that sum to $m$, and $I_{j}$ denotes the $j$ th entry of $I$.

# 4. Proof of the main theorem 

In this section, we prove Theorem 1. For a pair $(H, \lambda)$ consisting of a Horn matrix $H$ and a coefficient vector $\lambda$, let $\varphi$ be the rational map defined in (4). We use $\varphi$ and $\varphi_{(H, \lambda)}$ interchangeably in this section, as well as $\phi$ and $\phi_{(\Delta, \mathbf{m})}$. Recall that its $j$ th coordinate is

$$
\varphi_{j}(v)=\lambda_{j} \prod_{i=1}^{m}\left(\sum_{k=0}^{n} h_{i k} v_{k}\right)^{h_{i j}}
$$

For a fixed data vector $u \in \mathbb{N}^{n+1}$, we define the likelihood function for the image of $\varphi$ :

$$
L_{u}: \quad \mathbb{R}^{n+1} \rightarrow \mathbb{R}, \quad v \mapsto \prod_{j=0}^{n} \varphi_{j}(v)^{u_{j}}
$$

Lemma 21. Let $H=\left(h_{i j}\right)$ be a Horn matrix, $\lambda$ a vector satisfying (3) and $u \in \mathbb{N}^{n+1}$. Then $u$ is a critical point of its own likelihood function $L_{u}$. Furthermore, if $u^{\prime}$ is another critical point of $L_{u}$, then $\varphi(u)=\varphi\left(u^{\prime}\right)$.

Proof. We compute the partial derivatives of $L_{u}$. For $\ell=0, \ldots, n$, we find

$$
\begin{aligned}
\frac{\partial}{\partial v_{\ell}} L_{u}(v) & =\sum_{j=0}^{n} u_{j} \frac{L_{u}(v)}{\varphi_{j}(v)} \frac{\partial}{\partial v_{\ell}} \varphi_{j}(v) \\
& =\sum_{j=0}^{n} u_{j} \frac{L_{u}(v)}{\varphi_{j}(v)} \sum_{i=1}^{m} h_{i j} \frac{\varphi_{j}(v)}{\sum_{k=0}^{n} h_{i k} v_{k}} h_{i \ell} \\
& =L_{u}(v) \sum_{i=1}^{m} \sum_{j=0}^{n} \frac{u_{j} h_{i j} h_{i \ell}}{\sum_{k=0}^{n} h_{i k} v_{k}}=L_{u}(v) \sum_{i=1}^{m} \frac{h_{i \ell} \sum_{j=0}^{n} h_{i j} u_{j}}{\sum_{k=0}^{n} h_{i k} v_{k}}
\end{aligned}
$$

For $v=u$, this evaluates to zero, since the sums in the fraction cancel and the $\ell$ th column of $H$ sums to zero. This shows that $u$ is a critical point.

Next, let $u^{\prime}$ be another critical point of $L_{u}$. Using terminology from [10], Theorem 1, this means that $\varphi\left(u^{\prime}\right)$ is a critical point of the likelihood function $L(p, u)$ of the model $\mathcal{M}$ defined as the image of $\varphi$. The same holds for $\varphi(u)$. By the implication (ii) to (i) in [10], Theorem 1, the model $\mathcal{M}$ has ML degree one. This implies $\varphi(u)=\varphi\left(u^{\prime}\right)$.

We use [10] to explain the relation between models with rational MLE and Horn pairs.

Proof of Theorem 1, Equivalence of (1) and (2). Let $\mathcal{M}$ be a model with rational MLE $\Phi$. The Zariski closure of $\mathcal{M}$ is a variety whose likelihood function has a unique critical point. By [10], Theorem 1, there is a Horn matrix $H$ and a coefficient vector $\lambda$ such that $\varphi_{(H, \lambda)}=\Phi$. Now, the required sum-to-one and positivity conditions for $\varphi_{(H, \lambda)}$ are satisfied because they are satisfied by the MLE $\Phi$. Indeed, the MLE of any discrete statistical model maps positive vectors $u$ in $\mathbb{R}_{>0}^{n+1}$ into the simplex $\Delta_{n}$. Conversely, we claim that every Horn pair $(H, \lambda)$ specifies a nonempty model $\mathcal{M}$ with rational MLE. Indeed, define $\mathcal{M}$ to be the image of $\varphi_{(H, \lambda)}$. By the defining properties of the Horn pair, we have $\mathcal{M} \subset \Delta_{n}$. Lemma 21 shows that $\varphi_{(H, \lambda)}$ is the MLE of $\mathcal{M}$.

Next, we relate Horn pairs to discriminantal triples.
Proof of Theorem 1, Equivalence of (2) and (3). We already exhibited a bijection between pairs $(H, \lambda)$ and pairs $(\Delta, \mathbf{m})$ given by Equation (12). The matrix $A$ is the left kernel of $H$ and forms the triple $(A, \Delta, \mathbf{m})$. It is a matrix of size $r \times m$ of rank $r$. When $H$ is a Horn matrix, $A$ contains $(1, \ldots, 1)$ in its row span. This implies that the polynomial $\Delta$ is homogeneous, which in turn implies that it is $A$-homogeneous by $A H=0$.

Next, we show that the pair $(H, \lambda)$ being friendly corresponds to the polynomial $\Delta$ vanishing on $Y_{A}^{*}$. This is part of the desired equivalence.

Claim. The pair $(H, \lambda)$ is friendly if and only if the $A$-homogeneous polynomial $\Delta$ vanishes on the dual toric variety $Y_{A}^{*}$.

Proof of Claim. Let $(H, \lambda)$ be friendly and $A$ as above. The Laurent polynomial $q:=\Delta / \mathbf{m}$ is a rational function on $\mathbb{P}^{m-1}$ that vanishes on the dual toric variety $Y_{A}^{*}$. To see this, consider the exponentiation map $\varphi_{2}: \mathbb{P}^{m-1} \rightarrow \mathbb{R}^{n+1}, x \mapsto \lambda * x^{H}$, where $*$ is the entrywise product and $x^{H}:=\left(x^{h_{0}}, \ldots, x^{h_{n}}\right)$. Let $f=1-\left(p_{0}+\cdots+p_{n}\right)$. We have $q=f \circ \varphi_{2}$. By [10], Theorems 1 and 2, the function $\varphi_{2}$ maps an open dense subset of $Y_{A}^{*}$ dominantly to the closure $\overline{\mathcal{M}}$ of the image of $\varphi_{(H, \lambda)}$. Since $f=0$ on $\overline{\mathcal{M}}$, we have $f \circ \varphi_{2}=0$ on an open dense subset of $Y_{A}^{*}$, hence $q=0$ on $Y_{A}^{*}$, so $\Delta=0$ there as well.

Conversely, let $\Delta$ vanish on $Y_{A}^{*}$. We claim that $q(x)$ is zero for all $x=H u$ in the image of the linear map $H$. We may assume $\mathbf{m}(x) \neq 0$. We only need to show that $x$ is in the dual toric variety $Y_{A}^{*}$, since $\Delta$ vanishes on it. So, let $x_{i}=\sum_{j=0}^{n} h_{i j} u_{j}$ for $i=1, \ldots, m$. We claim that $t=(1, \ldots, 1)$ is a singular point of the hypersurface

$$
\gamma_{A}^{-1}\left(H_{s} \cap Y_{A}\right)=\left\{t \in \mathbb{C}^{r} \mid \sum_{i=1}^{m} x_{i} t^{a_{i}}=0\right\}
$$

First, the point $t$ lies on that hypersurface since the columns of $H$ sum to zero:

$$
\sum_{i=1}^{m} x_{i}=\sum_{i=1}^{m} \sum_{j=0}^{n} h_{i j} u_{j}=\sum_{j=0}^{n} u_{j} \sum_{i=1}^{m} h_{i j}=0
$$

For $s=1, \ldots, r$ we have $\frac{\partial}{\partial t_{s}} t^{a_{i}}=a_{s i} t^{a_{i}-e_{s}}$, with $e_{s}$ the standard basis vector of $\mathbb{Z}^{r}$, and

$$
\frac{\partial}{\partial t_{s}} \sum_{i=1}^{m} x_{i} t^{a_{i}}=\sum_{i=1}^{m} \sum_{j=0}^{n} h_{i j} u_{j} a_{s i} t^{a_{i}-e_{s}}=\sum_{j=0}^{n} u_{j} \sum_{i=1}^{m} a_{s i} h_{i j} t^{a_{i}-e_{s}}
$$

This is zero at $t=(1, \ldots, 1)$ because $A H=0$.

We now prove the rest of the equivalence. Let $(H, \lambda)$ be a Horn pair, let $\varphi$ be its Horn map and let $\phi$ be the associated monomial map. Let $\mathcal{M}$ be the statistical model with MLE $\varphi$, so $\mathcal{M}=\varphi\left(\mathbb{R}_{>0}^{n+1}\right)$. We have $\varphi=\phi \circ H$. By Proposition 23, there exists a unique sign vector $\sigma$ such that $\left.\operatorname{im} H\right|_{\mathbb{R}_{>0}^{n+1}} \subseteq \mathbb{R}_{\sigma}^{m}$. From the proof of the above claim, we know that $\operatorname{im} H \subseteq Y_{A}^{*}$. Together, we have

$$
\mathcal{M}=\varphi\left(\mathbb{R}_{>0}^{n+1}\right)=\left.\phi\left(\operatorname{im} H\right|_{\mathbb{R}_{>0}^{n+1}}\right) \subseteq \phi\left(Y_{A, \sigma}^{*}\right)
$$

By [10], Theorems 1 and 2, we have $\phi\left(Y_{A}^{*}\right) \subseteq \mathcal{M}^{\prime}$, where $\mathcal{M}^{\prime}$ is the real part of $\overline{\varphi\left(\mathbb{C}^{n+1}\right)}$. We also have $\phi\left(Y_{A, \sigma}^{*}\right) \subseteq \mathbb{R}_{>0}^{n+1}$ by definition of the orthant. Thus $\phi\left(Y_{A, \sigma}^{*}\right) \subseteq \mathcal{M}^{\prime} \cap \mathbb{R}_{>0}^{n+1}$. Every element in the latter set is a fixed point of the rational function $\varphi$, by a similar argument as in Lemma 21 for complex space. Hence $\mathcal{M}^{\prime} \cap \mathbb{R}_{>0}^{n+1}=\mathcal{M}$, so $\phi\left(Y_{A, \sigma}^{*}\right) \subseteq \mathcal{M}$.

Finally, if $(A, \Delta, \mathbf{m})$ is a discriminantal triple then $(H, \lambda)$ is a Horn pair by definition. This completes the proof of Theorem 1.

In the next two propositions, we formulate simple criteria to decide whether the image of the map $\varphi_{(H, \lambda)}$ associated to a Horn matrix $H$ and a coefficient vector $\lambda$ is a statistical model. These are essential for constructing models with rational MLE in Algorithm 1.

Proposition 22. Let $(H, \lambda)$ be a friendly pair. If there exists a vector $u_{0} \in \mathbb{R}^{n+1}$ such that $\varphi\left(u_{0}\right)>0$, then we have $\varphi(u)>0$ for all $u$ in $\mathbb{R}_{>0}^{n+1}$ where it is defined.

Proof. The function $\varphi$ is homogeneous of degree zero. It suffices to prove that each coordinate of $\varphi(u)$ is a positive real number, for all vectors $u$ with positive integer entries. Indeed, every positive $u$ in $\mathbb{R}^{n+1}$ can be approximated by rational vectors, which can be scaled to be integral. The open subset $U=\varphi^{-1}\left(\Delta_{n}\right)$ of $\mathbb{R}^{n+1}$ contains $u_{0}$ by our assumptions. If $U=\mathbb{R}^{n+1}$, then we are done. Else, $U$ has a nonempty boundary $\partial U$. By continuity, $\partial U \subseteq \varphi^{-1}\left(\partial \Delta_{n}\right)$. The likelihood function $L_{u}$ for the data vector $u$ vanishes on $\partial U$.

We claim that $L_{u}$ has a critical point in $U$. The closed subset $\bar{U}$ is homogeneous. Seen in projective space $\mathbb{P}^{n}$, it becomes compact. The likelihood function $L_{u}$ is well defined on this compact set in $\mathbb{P}^{n}$, since it is homogeneous of degree zero, and $L_{u}$ vanishes on the boundary. Hence the restriction $\left.L_{u}\right|_{U}$ is either identically zero or it has a critical point in $U$. But, since $u_{0} \in U$ is a point with $L_{u}\left(u_{0}\right) \neq 0$, the second statement must be true.

Pick such a critical point $u^{\prime}$. Since $U$ is open in $\mathbb{R}^{n+1}$, the point $u^{\prime}$ is also critical point of $L_{u}$. By Lemma 21 and since $u^{\prime} \in U$, we have $\varphi(u)=\varphi\left(u^{\prime}\right)>0$.

Proposition 23. Let $(H, \lambda)$ be a friendly pair, with no zero or collinear rows in $H$. Then $(H, \lambda)$ is a Horn pair if and only if for every row $r_{i}$ of $H$ all nonzero entries of $r_{i}$ have the same sign $\sigma_{i}$, and the sign vector $\sigma=\left(\sigma_{i}\right)$ satisfies $\lambda_{j} \sigma^{h_{j}}>0$ for all columns $j$.

Proof. Let $(H, \lambda)$ be a Horn pair. Let $\ell_{1}, \ldots, \ell_{k}$ be the linear forms corresponding to the rows in $H$ that have both positive and negative entries. Since $\ell_{1}$ has positive and negative coefficients, there exists a positive vector $u$ such that $\ell_{1}(u)=0$. Since $(H, \lambda)$ is minimal, we may choose $u>0$ such that $\ell_{1}(u)=0$ but $\ell_{k^{\prime}}(u) \neq 0$ for all $k^{\prime} \neq 1$. The form $\ell_{1}$ appears in the numerator of some coordinate of $\varphi$, making this coordinate zero at $u$. But this contradicts the fact that $(H, \lambda)$ is a Horn pair. Therefore, we cannot have rows with both positive and negative entries. The inequalities $\lambda_{j} \sigma^{h_{j}}>0$ then follow from the definition of a Horn pair by evaluating $\varphi(u)$ for some positive vector $u$.

Conversely, if the sign vector $\sigma$ is well-defined, the inequalities $\lambda_{j} \sigma^{h_{j}}>0$ imply that $\varphi(u)>0$ for all positive $u$. Hence $(H, \lambda)$ is a Horn pair.

Every model with rational MLE arises from a toric variety $Y_{A}$. In some cases, the model is itself a toric variety $Y_{C}$. It is crucial to distinguish the two matrices $A$ and $C$. The two toric structures are very different. For instance, every undirected graphical model is toric [4], Proposition 3.3.3. The toric varieties $Y_{C}$ among staged tree models $\mathcal{M}_{\mathcal{T}}$ were classified in [5]. The 4 -chain model $\mathcal{M}_{\mathcal{T}}=Y_{C}$ is itself a toric variety of dimension 7 in $\mathbb{P}^{15}$. But it arises from a toric variety $Y_{A}$ of dimension 12 in $\mathbb{P}^{20}$, seen in Example 19.

Toric models with rational MLE play an important role in geometric modeling [2|6]. Given a matrix $C \in \mathbb{Z}^{r \times(n+1)}$ and a vector of weights $w \in \mathbb{R}_{>0}^{n+1}$, one considers the scaled projective toric variety $Y_{C, w}$ in $\mathbb{R} \mathbb{P}^{n}$. This is defined as the closure of the image of

$$
\gamma_{C, w}: \quad\left(\mathbb{R}^{*}\right)^{r} \rightarrow \mathbb{R} \mathbb{P}^{n}, \quad\left(t_{1}, \ldots, t_{r}\right) \mapsto\left(w_{0} \prod_{i=1}^{r} t_{i}^{c_{i 0}}, w_{1} \prod_{i=1}^{r} t_{i}^{c_{i 1}}, \ldots, w_{n} \prod_{i=1}^{r} t_{i}^{c_{i n}}\right)
$$

The set $\mathcal{M}_{C, w}$ of positive points in $Y_{C, w}$ is a statistical model in $\Delta_{n}$. There is a natural homeomorphism from the toric model $\mathcal{M}_{C, w}$ onto the polytope of $C$. This is known in geometry as the moment map. For a reference from algebraic statistics, see [4], Proposition 2.1.5. In geometric modeling, the pair $(C, w)$ defines toric blending functions [13].

It is desirable for the toric blending functions to have rational linear precision [2|13]. The property is rare and it depends in a subtle way on $(C, w)$. Garcia-Puente and Sottile [6] established the connection to algebraic statistics. They showed that rational linear precision holds for $(C, w)$ if and only if the statistical model $\mathcal{M}_{C, w}$ has rational MLE.

Example 24. The most classical blending functions with rational linear precision live on the triangle $\left\{x \in \mathbb{R}_{>0}^{3}: x_{1}+x_{2}+x_{3}=1\right\}$. They are the Bernstein basis polynomials

$$
\frac{m!}{i!j!(m-i-j)!} x_{1}^{i} x_{2}^{j} x_{3}^{m-i-j} \quad \text { for } i, j \geq 0, i+j \leq m
$$

Here, $C$ is the $3 \times\binom{m+1}{2}$ matrix whose columns are the vectors $(i, j, m-i-j)$. The weights are $w_{(i, j)}=\frac{m!}{i!j!(m-i-j)!}$. The toric model $\mathcal{M}_{C, w}$ is the multinomial family, where (19) is the probability of observing $i$ times $1, j$ times 2 and $m-i-j$ times 3 in $m$ trials. This model has rational MLE, as seen in Example 20. Again, notice the distinction between the two toric varieties. Here, $Y_{A}$ is a point in $\mathbb{P}^{m}$, whereas $Y_{C}$ is a surface in $\mathbb{P}^{\binom{m}{2}-1}$.

Clarke and Cox [2] raise the problem of characterizing all pairs $(C, w)$ with rational linear precision. This was solved by Duarte and Görgen [5] for pairs arising from staged trees. While the problem remains open in general, our theory in this paper offers new tools. We may ask for a characterization of discriminantal triples whose models are toric.

# 5. Constructing models with rational MLE 

Part (3) in Theorem 1 allows us to construct models with rational MLE starting from a matrix $A$ that defines a projective toric variety $Y_{A}$. To carry out this construction effectively, we propose Algorithm 1. In most cases, the dual variety $Y_{A}^{*}$ is a hypersurface, and we can compute its defining polynomial $\Delta_{A}$, the discriminant [7]. The polynomial $\Delta$ in a discriminantal triple can be any homogeneous multiple of $\Delta_{A}$, but we just take $\Delta=\Delta_{A}$. For all terms $\mathbf{m}$ in $\Delta_{A}$, we check whether $\left(A, \Delta_{A}, \mathbf{m}\right)$ is a discriminantal triple. We implemented this algorithm in Macaulay2 [9], and our code is available online at [18].

```
Algorithm 1: From toric varieties to statistical models
    Input : An integer matrix \(A\) of size \(r \times m\) with \((1, \ldots, 1)\) in its row span
    Output: An integer \(n\) and a collection of statistical models \(\mathcal{M}^{(\ell)}=\left(\Phi^{(\ell)}, I^{(\ell)}\right)\), where
        \(\Phi^{(\ell)}: \mathbb{R}^{n+1} \rightarrow \mathbb{R}^{n+1}\) is a rational MLE for \(\mathcal{M}^{(\ell)}\) ， and \(I^{(\ell)} \subseteq \mathbb{R}\left[p_{0}, \ldots, p_{n}\right]\) is the
        defining prime ideal of \(\mathcal{M}^{(\ell)}\).
    Compute the \(A\)-discriminant \(\Delta_{A} \in \mathbb{Z}\left[x_{1}, \ldots, x_{m}\right]\);
    \(n \leftarrow \# \operatorname{terms}\left(\Delta_{A}\right)-2\);
    models \(\leftarrow\{\}\)
    for \(0 \leq \ell \leq n+1\) do
        \(\mathbf{m} \leftarrow \operatorname{terms}\left(\Delta_{A}\right)_{\ell}\);
        \(q \leftarrow 1-\Delta_{A} / \mathbf{m}\)
        for \(0 \leq j \leq n\) do
            \(\lambda_{j} \leftarrow\) coefficients \((q)_{j}\);
            \(h_{j} \leftarrow\) exponent_vectors \((q)_{j}\);
            \(\Phi_{j}^{(\ell)} \leftarrow\left(u \mapsto \lambda_{j} \prod_{i=1}^{m}\left(\sum_{k=0}^{n} h_{i k} u_{k}\right)^{h_{i j}}\right)\);
    end
    \(H \leftarrow\left(h_{i j}\right)\);
    Choose any positive vector \(v\) in \(\mathbb{R}_{>0}^{n+1}\);
    if \(\Phi_{j}^{(\ell)}(v)>0\) for \(j=0,1, \ldots, n\) then
        Compute the ideal \(I^{(\ell)}\) of the image of \(\Phi^{(\ell)}\);
        models \(\leftarrow\) models \(\cup\left\{\left(\Phi^{(\ell)}, I^{(\ell)}\right)\right\}\);
    end
end
18
```

19 return models;

Lines 1 and 15 of Algorithm 1 are computations with Gröbner bases. Executing Line 15 can be very slow. It may be omitted if one is satisfied with obtaining the parametric description and MLE $\Phi^{(\ell)}$ of the model $\mathcal{M}_{\ell}$. For the check in Line 14, we rely on Proposition 22 for correctness. A check based on the criterion in Proposition 23 is also possible.

Example $25(r=2, m=4)$. For distinct integers $\alpha, \beta, \gamma>0$ with $\operatorname{gcd}(\alpha, \beta, \gamma)=1$ let

$$
A_{\alpha, \beta, \gamma}=\left(\begin{array}{llll}
1 & 1 & 1 & 1 \\
0 & \alpha & \beta & \gamma
\end{array}\right)
$$

We ran Algorithm 1 for all 613 such matrices with $0<\alpha<\beta<\gamma \leq 17$. Line 1 computes the discriminant $\Delta_{A}$ of the univariate polynomial $f(t)=x_{1}+x_{2} t^{\alpha}+x_{3} t^{\beta}+x_{4} t^{\gamma}$. The number $n+2$ of terms of these discriminants equals $7927 / 613=12.93$ on average. Thus a total of 7927 candidate triples $\left(A, \Delta_{A}, \mathbf{m}\right)$ were tested in Lines 12 to 21 . Precisely, 123 of these were found to be discriminantal triples. This is a fraction of $1.55 \%$. Hence, only $1.55 \%$ of the resulting complex varieties permitted by [10] are actually statistical models.

Here is a typical model that was discovered. Take $\alpha=1, \beta=4, \gamma=7$. The discriminant

$$
\begin{aligned}
\Delta_{A}= & 729 x_{2}^{4} x_{3}^{6}-6912 x_{1}^{3} x_{3}^{7}-8748 x_{2}^{5} x_{3}^{4} x_{4}+84672 x_{1}^{3} x_{2} x_{3}^{5} x_{4}+34992 x_{2}^{6} x_{3}^{2} x_{4}^{2} \\
& -351918 x_{1}^{3} x_{2}^{2} x_{3}^{3} x_{4}^{2}-46656 x_{2}^{7} x_{4}^{3}+518616 x_{1}^{3} x_{2}^{3} x_{3} x_{4}^{3}-823543 x_{1}^{6} x_{4}^{4}
\end{aligned}
$$

has 9 terms, so $n=7$. The term $\mathbf{m}$ is underlined. The associated model is a curve of degree ten in $\Delta_{7}$. Its prime ideal $I^{(\ell)}$ is generated by 18 quadrics. Among them are 15 binomials that define a toric surface of degree six: $49 p_{1} p_{2}-48 p_{0} p_{3}, 3 p_{0} p_{4}-p_{2}^{2}, \ldots, 361 p_{3} p_{7}-128 p_{5}^{2}$. Inside that surface, our curve is cut out by three quadrics, like $26068 p_{2}^{2}+73728 p_{0} p_{5}+703836 p_{0} p_{6}+234612 p_{2} p_{6}+78204 p_{4} p_{6}+$ $612864 p_{0} p_{7}+212268 p_{2} p_{7}+78204 p_{4} p_{7}-8379 p_{7}^{2}$.

Example $26(r=3, m=6)$. For any positive integers $\alpha, \beta, \gamma, \varepsilon$, we consider the matrix

$$
A=\left(\begin{array}{cccccc}
0 & \alpha & \beta & 0 & \gamma & \varepsilon \\
0 & 0 & 0 & 1 & 1 & 1 \\
1 & 1 & 1 & 1 & 1 & 1
\end{array}\right)
$$

The discriminant $\Delta_{A}$ is the resultant of two trinomials $x_{1}+x_{2} t^{\alpha}+x_{3} t^{\beta}$ and $x_{4}+x_{5} t^{\gamma}+x_{6} t^{\varepsilon}$. We ran Algorithm 1 for all 138 such matrices with $0<\alpha<\beta \leq 17,0<\gamma<\varepsilon \leq 17, \operatorname{gcd}(\alpha, \beta)=\operatorname{gcd}(\gamma, \varepsilon)=$ 1 . The number $n+2$ of terms of these discriminants equals $2665 / 138=19.31$ on average. Thus a total of 2665 candidate triples $\left(A, \Delta_{A}, \mathbf{m}\right)$ were tested in Line 13. Precisely, 93 of these are discriminantal triples. This is only $3.49 \%$.

We now shift gears by looking at polynomials $\Delta$ that are multiples of the $A$-discriminant.
Example $27(r=1, m=4)$. We saw in Examples 2 and 20 that interesting models arise from the matrix $A=(11 \cdots 1)$ whose toric variety is just a point. Any homogeneous multiple $\Delta$ of the linear form $\Delta_{A}=x_{1}+x_{2}+\cdots+x_{m}$ can be the input in Line 1 of Algorithm 1. Here, taking $\Delta=\Delta_{A}$ results in the model given by the full simplex $\Delta_{m-2}$.

Let $m=4$ and abbreviate $x^{a}=x_{1}^{a_{1}} x_{2}^{a_{2}} x_{3}^{a_{3}} x_{4}^{a_{4}}$ and $|a|=a_{1}+a_{2}+a_{3}+a_{4}$ for $a \in \mathbb{N}^{4}$. We conducted experiments with two families of multiples. The first uses binomial multipliers:

$$
\Delta=\left(x^{a}+x^{b}\right) \Delta_{A} \quad \text { or } \quad \Delta=\left(x^{a}-x^{b}\right) \Delta_{A}
$$

where $|a|=|b| \in\{1,2, \ldots, 8\}$ and $\operatorname{gcd}\left(x^{a}, x^{b}\right)=1$. This gives 1028 polynomials $\Delta$. The numbers of polynomials of degree $2,3,4,5,6,7,8,9$ is $6,21,46,81,126,181,246,321$. For the second family, we use the trinomial multiples

$$
\Delta=\left(x^{a}+x^{b}+x^{c}\right) \Delta_{A} \quad \text { or } \quad \Delta=\left(x^{a}+x^{b}-x^{c}\right) \Delta_{A}
$$

where $|a|=|b|=|c| \in\{1,2,3\}$ and $\operatorname{gcd}\left(x^{a}, x^{b}, x^{c}\right)=1$. Each list contains 4 quadrics, 104 cubics and 684 quartics. We report our findings in Table 1.

All 12 Horn pairs in the first family represent the same model, up to permuting coordinates. All are coming from the six quadrics of the family. The model is the surface in $\Delta_{4}$ defined by the $2 \times 2$ minors

Table 1. Horn pairs from families of multiples of $\Delta_{A}=x_{1}+\cdots+x_{m}$


of the matrix $\left(\begin{array}{cc}p_{0} & p_{1} \\ p_{0}+p_{1}+p_{2} & p_{3} & p_{4}\end{array}\right)$. This is a staged tree model similar to Example 2, but now with three choices at each blue node instead of two. The eight Horn pairs in the third family represent two distinct models. Four of the eight Horn pairs represent a surface in $\Delta_{5}$ and the rest represent a surface in $\Delta_{6}$.

Our construction of models with rational MLE starts with families where $r$ and $m$ are fixed. However, as the entries of the matrix $A$ go up, the number $n+1$ of states increases. This suggests the possibility of listing all models for fixed values of $n$. Is this list finite?

Problem. Suppose that $n$ is fixed. Are there only finitely many models with rational MLE in the simplex $\Delta_{n}$ ? Can we find absolute bounds, depending only on $n$, for the dimension, degree and number of ideal generators of the associated varieties in $\mathbb{P}^{n}$ ?

Algorithm 1 is a tool for studying these questions experimentally. At present, we do not have any clear answers, even for $n=3$, where the models are curves in a triangle.

# Acknowledgments 

The first author was supported by the Deutsche Forschungsgemeinschaft DFG under grant 314838170, GRK 2297 MathCoRe.

Eliana Duarte: Partial affiliation with Max-Planck-Institut für Mathematik in den Naturwissenschaften, Leipzig. Bernd Sturmfels: Partial affiliation with University of California, Berkeley.
