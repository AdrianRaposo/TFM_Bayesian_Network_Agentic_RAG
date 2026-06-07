# Multivariate Gaussians, Semidefinite Matrix Completion, and Convex Algebraic Geometry 

Bernd Sturmfels $\cdot$ Caroline Uhler


#### Abstract

We study multivariate normal models that are described by linear constraints on the inverse of the covariance matrix. Maximum likelihood estimation for such models leads to the problem of maximizing the determinant function over a spectrahedron, and to the problem of characterizing the image of the positive definite cone under an arbitrary linear projection. These problems at the interface of statistics and optimization are here examined from the perspective of convex algebraic geometry.


Keywords Convex algebraic geometry $\cdot$ Multivariate normal distribution $\cdot$ Maximum likelihood estimation $\cdot$ Semidefinite matrix completion $\cdot$ Dual convex cone $\cdot$ Dual projective variety

## 1 Introduction

Every positive definite $m \times m$-matrix $\Sigma$ is the covariance matrix of a multivariate normal distribution on $\mathbb{R}^{m}$. Its inverse matrix $K=\Sigma^{-1}$ is also positive definite and known as the concentration matrix of the distribution. We study statistical models for multivariate normal distributions on $\mathbb{R}^{m}$, where the concentration matrix can be written as a linear combination

$$
K=\lambda_{1} K_{1}+\lambda_{2} K_{2}+\cdots+\lambda_{d} K_{d}
$$

of some fixed linearly independent symmetric matrices $K_{1}, \ldots, K_{d}$. Here, $\lambda_{1}, \lambda_{2}, \ldots, \lambda_{d}$ are unknown real coefficients. It is assumed that $K$ is positive definite for some choice of $\lambda_{1}, \lambda_{2}, \ldots, \lambda_{d}$. Such statistical models, which we call linear concentration models, were introduced by Anderson (1970).

Let $\mathbb{S}^{m}$ denote the vector space of real symmetric $m \times m$-matrices. We identify $\mathbb{S}^{m}$ with its dual space via the inner product $\langle A, B\rangle:=\operatorname{trace}(A \cdot B)$. The cone $\mathbb{S}_{\succ 0}^{m}$ of positive semidefinite matrices is a full-dimensional self-dual cone in $\mathbb{S}^{m}$. Its interior is the open cone $\mathbb{S}_{\succ 0}^{m}$ of positive definite matrices. We define a linear concentration model to be any non-empty set of the form

$$
\mathcal{L}_{\succ 0}^{-1}:=\left\{\Sigma \in \mathbb{S}_{\succ 0}^{m}: \Sigma^{-1} \in \mathcal{L}\right\}
$$

BS is supported in part by NSF grants DMS-0456960 and DMS-0757236. CU is supported by an International Fulbright Science and Technology Fellowship.

Bernd Sturmfels
Department of Mathematics \#3840
University of California at Berkeley
970 Evans Hall
Berkeley, CA 94720-3840, U.S.A.
E-mail: bernd@math.Berkeley.edu
Caroline Uhler
Department of Statistics \#3860
University of California at Berkeley
345 Evans Hall
Berkeley, CA 94720-3860, U.S.A.
E-mail: cuhler@stat.Berkeley.edu

where $\mathcal{L}$ is a linear subspace of $\mathbb{S}^{m}$. Given a basis $K_{1}, \ldots, K_{d}$ of the subspace $\mathcal{L}$ as in (1), the basic statistical problem is to estimate the parameters $\lambda_{1}, \ldots, \lambda_{d}$ when $n$ observations $X_{1}, \ldots, X_{n}$ are drawn from a multivariate normal distribution $\mathcal{N}(\mu, \Sigma)$, whose covariance matrix $\Sigma=K^{-1}$ is in the model $\mathcal{L}_{>0}^{-1}$. The $n$ observations $X_{i}$ and their mean $\bar{X}$ are summarized in the sample covariance matrix

$$
S=\frac{1}{n} \sum_{i=1}^{n}\left(X_{i}-\bar{X}\right)\left(X_{i}-\bar{X}\right)^{T} \in \mathbb{S}_{\geq 0}^{m}
$$

In our model, we make no assumptions on the mean vector $\mu$ and always use the sample mean $\bar{X}$ as estimate for $\mu$. Thus, we are precisely in the situation of (Drton et al. 2009, Prop. 2.1.12), with $\Theta_{2}=\mathcal{L}^{-1}$. The log-likelihood function for the linear concentration model (1) equals

$$
\log \operatorname{det}(K)-\langle S, K\rangle=\log \operatorname{det}\left(\sum_{j=1}^{d} \lambda_{j} K_{j}\right)-\sum_{j=1}^{d} \lambda_{j}\left\langle S, K_{j}\right\rangle
$$

times the constant $n / 2$. This is a strictly concave function on the relatively open cone $\mathbb{S}_{>0}^{m} \cap \mathcal{L}$. If a maximum (i.e. the maximum likelihood estimate or MLE) exists, then it is attained by a unique matrix $\hat{K}$ in $\mathbb{S}_{>0}^{m} \cap \mathcal{L}$. Its inverse $\hat{\Sigma}=\hat{K}^{-1}$ is uniquely determined by the linear equations

$$
\left\langle\hat{\Sigma}, K_{j}\right\rangle=\left\langle S, K_{j}\right\rangle \quad \text { for } j=1,2, \ldots, d
$$

This characterization follows from the statistical theory of exponential families (Brown 1986, §5). In that theory, the scalars $\lambda_{1}, \ldots, \lambda_{d}$ are the canonical parameters and $\left\langle S, K_{1}\right\rangle, \ldots,\left\langle S, K_{d}\right\rangle$ are the sufficient statistics of the exponential family (1). For a special case see (Drton et al. 2009, Theorem 2.1.14).

We consider the set of all covariance matrices whose sufficient statistics are given by the matrix $S$. This set is a spectrahedron. It depends only on $S$ and $\mathcal{L}$, and it is denoted

$$
\operatorname{fiber}_{\mathcal{L}}(S)=\left\{\Sigma \in \mathbb{S}_{>0}^{m}:\langle\Sigma, K\rangle=\langle S, K\rangle \text { for all } K \in \mathcal{L}\right\}
$$

The MLE exists for a sample covariance matrix $S$ if and only if fiber $\mathcal{L}(S)$ is non-empty. If $\operatorname{rank}(S)<m$ then it can happen that the fiber is empty, in which case the MLE does not exist for $(\mathcal{L}, S)$. Work of Buhl (1993) and Barrett et al. (1993) addresses this issue for graphical models; see Section 4 below.

Our motivating statistical problem is to identify conditions on the pair $(\mathcal{L}, S)$ that ensure the existence of the MLE. This will involve studying the geometry of the semi-algebraic set $\mathcal{L}_{>0}^{-1}$ and of the algebraic function $S \mapsto \hat{\Sigma}$ which takes a sample covariance matrix to its MLE in $\mathcal{L}_{>0}^{-1}$.
Example 1.1. We illustrate the concepts introduced so far by way of a small explicit example whose geometry is visualized in Fig. 1. Let $m=d=3$ and let $\mathcal{L}$ be the real vector space spanned by

$$
K_{1}=\left(\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 1 \\
0 & 1 & 1
\end{array}\right), \quad K_{2}=\left(\begin{array}{lll}
1 & 0 & 1 \\
0 & 1 & 0 \\
1 & 0 & 1
\end{array}\right) \quad \text { and } \quad K_{3}=\left(\begin{array}{lll}
1 & 1 & 0 \\
1 & 1 & 0 \\
0 & 0 & 1
\end{array}\right)
$$

The linear concentration model (1) consists of all positive definite matrices of the form

$$
K=\left(\begin{array}{cc}
\lambda_{1}+\lambda_{2}+\lambda_{3} & \lambda_{3} & \lambda_{2} \\
\lambda_{3} & \lambda_{1}+\lambda_{2}+\lambda_{3} & \lambda_{1} \\
\lambda_{2} & \lambda_{1} & \lambda_{1}+\lambda_{2}+\lambda_{3}
\end{array}\right)
$$

Given a sample covariance matrix $S=\left(s_{i j}\right)$, the sufficient statistics are

$$
t_{1}=\operatorname{trace}(S)+2 s_{23}, t_{2}=\operatorname{trace}(S)+2 s_{13}, t_{3}=\operatorname{trace}(S)+2 s_{12}
$$

If $S \in \mathbb{S}_{>0}^{3}$ then fiber $\mathcal{L}(S)$ is an open 3-dimensional convex body whose boundary is a cubic surface. This is the spectrahedron shown on the left in Fig. 1. The MLE $\hat{\Sigma}$ is the unique matrix of maximum

![img-0.jpeg](img-0.jpeg)

Fig. 1 Three figures, taken from Nie et al. (2009), illustrate Example 1.1. These figures show the spectrahedron fiber $\mathcal{L}(S)$ (left), a cross section of the spectrahedral cone $\mathcal{K}_{\mathcal{L}}$ (middle), and a cross section of its dual cone $\mathcal{C}_{\mathcal{L}}$ (right).
determinant in the spectrahedron fiber $\mathcal{L}(S)$. Here is an explicit algebraic formula for the MLE $\hat{\Sigma}=\left(\hat{s}_{i j}\right)$ : First, the matrix entry $\hat{s}_{33}$ is determined (e.g. using Cardano's formula ${ }^{1}$ ) from the equation

$$
\begin{aligned}
0= & 240 \hat{s}_{33}^{4}+\left(-32 t_{1}-32 t_{2}-192 t_{3}\right) \hat{s}_{33}^{3}+\left(-8 t_{1}^{2}+16 t_{1} t_{2}+16 t_{1} t_{3}-8 t_{2}^{2}+16 t_{2} t_{3}+32 t_{3}^{2}\right) \hat{s}_{33}^{2} \\
& +\left(8 t_{1}^{3}-8 t_{1}^{2} t_{2}-8 t_{1} t_{2}^{2}+8 t_{2}^{3}\right) \hat{s}_{33}-4 t_{1}^{3} t_{3}-6 t_{1}^{2} t_{2}^{2}+4 t_{1}^{2} t_{3}^{2}+4 t_{1} t_{2}^{3}+4 t_{1} t_{2}^{2} t_{3}+4 t_{1}^{2} t_{2} t_{3}-t_{2}^{4} \\
& -4 t_{2}^{3} t_{3}+4 t_{2}^{2} t_{3}^{2}-8 t_{1} t_{2} t_{3}^{2}-t_{1}^{4}+4 t_{1}^{3} t_{2}
\end{aligned}
$$

Next, we read off $\hat{s}_{23}$ from

$$
\begin{aligned}
-24\left(t_{1}^{2}-2 t_{1} t_{2}+t_{2}^{2}-t_{3}^{2}\right) \hat{s}_{23}= & 120 \hat{s}_{33}^{3}-\left(16 t_{1}+16 t_{2}+36 t_{3}\right) \hat{s}_{33}^{2}+\left(2 t_{1}^{2}-4 t_{1} t_{2}+2 t_{2}^{2}-8 t_{3}^{2}\right) \hat{s}_{33}-6 t_{1}^{3} \\
& +18 t_{1}^{2} t_{2}+t_{1}^{2} t_{3}-18 t_{1} t_{2}^{2}-2 t_{1} t_{2} t_{3}+10 t_{1} t_{3}^{2}+6 t_{2}^{3}+t_{2}^{2} t_{3}-2 t_{2} t_{3}^{2}-4 t_{3}^{3}
\end{aligned}
$$

Then we read off $\hat{s}_{22}$ from

$$
\begin{aligned}
-24\left(t_{1}-t_{2}\right) \hat{s}_{22}= & 60 \hat{s}_{33}^{2}+\left(4 t_{1}-20 t_{2}-24 t_{3}\right) \hat{s}_{33}+24\left(t_{1}-t_{2}-t_{3}\right) \hat{s}_{23} \\
& -11 t_{1}^{2}+10 t_{1} t_{2}+10 t_{1} t_{3}+t_{2}^{2}-2 t_{2} t_{3}-4 t_{3}^{2}
\end{aligned}
$$

Finally, we obtain the first row of $\hat{\Sigma}$ as follows:

$$
\hat{s}_{13}=\hat{s}_{23}-t_{1} / 2+t_{2} / 2, \quad \hat{s}_{12}=\hat{s}_{23}-t_{1} / 2+t_{3} / 2, \quad \hat{s}_{11}=t_{1}-\hat{s}_{33}-2 \hat{s}_{23}-\hat{s}_{22}
$$

The MLE $\hat{\Sigma}=\left(\hat{s}_{i j}\right)$ is an algebraic function of degree 4 in the sufficient statistics $\left(t_{1}, t_{2}, t_{3}\right)$. In short, the model (4) has ML degree 4. We identify our model with the subvariety $\mathcal{L}^{-1}$ of projective space $\mathbb{P}^{5}$ that is parametrized by this algebraic function. The ideal of polynomials vanishing on $\mathcal{L}^{-1}$ equals

$$
\begin{aligned}
P_{\mathcal{L}}= & \left\langle s_{13}^{2}-s_{23}^{2}-s_{11} s_{33}+s_{22} s_{33}, s_{12}^{2}-s_{11} s_{22}-s_{23}^{2}+s_{22} s_{33}\right. \\
& s_{12} s_{13}-s_{13} s_{22}-s_{11} s_{23}+s_{12} s_{23}+s_{13} s_{23}+s_{23}^{2}-s_{12} s_{33}-s_{22} s_{33} \\
& s_{11} s_{13}-s_{13} s_{22}-s_{11} s_{23}+s_{22} s_{23}-s_{11} s_{33}-2 s_{12} s_{33}-s_{13} s_{33}-s_{22} s_{33}-s_{23} s_{33}+s_{33}^{2} \\
& s_{11} s_{12}-s_{11} s_{22}-s_{12} s_{22}-2 s_{13} s_{22}+s_{22}^{2}-s_{11} s_{23}-s_{22} s_{23}-s_{12} s_{33}-s_{22} s_{33}+s_{23} s_{33} \\
& s_{11}^{2}-2 s_{11} s_{22}-4 s_{13} s_{22}+s_{22}^{2}-4 s_{11} s_{23}-2 s_{11} s_{33}-4 s_{12} s_{33}-2 s_{22} s_{33}+s_{33}^{2}
\end{aligned}
$$

The domain of the maximum likelihood map $\left(t_{1}, t_{2}, t_{3}\right) \mapsto \hat{\Sigma}$ is the cone of sufficient statistics $\mathcal{C}_{\mathcal{L}}$ in $\mathbb{R}^{3}$. The polynomial $H_{\mathcal{L}}$ which vanishes on the boundary of this convex cone has degree six. It equals

$$
\begin{aligned}
H_{\mathcal{L}}= & t_{1}^{6}-6 t_{1}^{5} t_{2}+19 t_{1}^{4} t_{2}^{2}-28 t_{1}^{3} t_{2}^{3}+19 t_{1}^{2} t_{2}^{4}-6 t_{1} t_{2}^{5}+t_{2}^{6}-6 t_{1}^{5} t_{3}+14 t_{1}^{4} t_{2} t_{3}-24 t_{1}^{3} t_{2}^{2} t_{3}-24 t_{1}^{2} t_{2}^{3} t_{3} \\
& +14 t_{1} t_{2}^{4} t_{3}-6 t_{2}^{5} t_{3}+19 t_{1}^{4} t_{3}^{2}-24 t_{1}^{3} t_{2} t_{3}^{2}+106 t_{1}^{2} t_{2}^{2} t_{3}^{2}-24 t_{1} t_{2}^{3} t_{3}^{2}+19 t_{2}^{4} t_{3}^{2}-28 t_{1}^{3} t_{3}^{3}-24 t_{1}^{2} t_{2} t_{3}^{3} \\
& -24 t_{1} t_{2}^{2} t_{3}^{3}-28 t_{2}^{3} t_{3}^{3}+19 t_{1}^{2} t_{3}^{4}+14 t_{1} t_{2} t_{3}^{4}+19 t_{2}^{2} t_{3}^{4}-6 t_{1} t_{3}^{5}-6 t_{2} t_{3}^{5}+t_{3}^{6}
\end{aligned}
$$

The sextic curve $\left\{H_{\mathcal{L}}=0\right\}$ in $\mathbb{P}^{2}$ is shown on the right in Fig. 1. It is dual to the cubic curve $\{\operatorname{det}(K)=0\}$, shown in the middle of Fig. 1. The cone over the convex region enclosed by the red part of that cubic curve is the set $\mathcal{K}_{\mathcal{L}}=\mathbb{S}_{>0}^{3} \cap \mathcal{L}$ of concentration matrices in our model (1).

[^0]
[^0]:    1 www.literka.addr.com/mathcountry/algebra/quartic.htm

This paper is organized as follows. In Section 2 we formally define the objects $\mathcal{K}_{\mathcal{L}}, \mathcal{C}_{\mathcal{L}}, P_{\mathcal{L}}$ and $H_{\mathcal{L}}$, which already appeared in Example 1.1, and we derive three guiding questions that constitute the main thread of this paper. These questions are answered for generic linear spaces $\mathcal{L}$ in Subsection 2.2. That subsection is written for algebraists, and readers from statistics or optimization can skip it at their first reading. In Section 3 we answer our three questions for diagonal concentration models, using results from geometric combinatorics. Section 4 deals with Gaussian graphical models, which are the most prominent linear concentration models. We resolve our three questions for chordal graphs, then for chordless cycles, and finally for wheels and all graphs with five or less vertices. We conclude this paper with a study of colored Gaussian graphical models in Section 5. These are special Gaussian graphical models with additional linear restrictions on the concentration matrix given by the graph coloring.

# 2 Linear Sections, Projections and Duality 

Convex algebraic geometry is concerned with the geometry of real algebraic varieties and semi-algebraic sets that arise in convex optimization, especially in semidefinite programming. A fundamental problem is to study convex sets that arise as linear sections and projections of the cone of positive definite matrices $\mathbb{S}_{s \cdot 0}^{m}$. As we saw in the Introduction, this problem arises naturally when studying maximum likelihood estimation in linear concentration models for Gaussian random variables. In particular, the issue of estimating a covariance matrix from the sufficient statistics can be seen as an extension of the familiar semidefinite matrix completion problem (Barrett et al. 1993; Grone et al. 1984). In what follows, we develop an algebraic and geometric framework for systematically addressing such problems.

### 2.1 Derivation of three guiding questions

As before, we fix a linear subspace $\mathcal{L}$ in the real vector space $\mathbb{S}^{m}$ of symmetric $m \times m$-matrices, and we fix a basis $\left\{K_{1}, \ldots, K_{d}\right\}$ of $\mathcal{L}$. The cone of concentration matrices is the relatively open cone

$$
\mathcal{K}_{\mathcal{L}}=\mathcal{L} \cap \mathbb{S}_{s \cdot 0}^{m}
$$

We assume throughout that $\mathcal{K}_{\mathcal{L}}$ is non-empty. Using the basis $K_{1}, \ldots, K_{d}$ of $\mathcal{L}$, we can identify $\mathcal{K}_{\mathcal{L}}$ with

$$
\mathcal{K}_{\mathcal{L}}=\left\{\left(\lambda_{1}, \ldots, \lambda_{d}\right) \in \mathbb{R}^{d}: \sum_{i=1}^{d} \lambda_{i} K_{i} \text { is positive definite }\right\}
$$

This is a non-empty open convex cone in $\mathbb{R}^{d}$. The orthogonal complement $\mathcal{L}^{\perp}$ of $\mathcal{L}$ is a subspace of dimension $\binom{m+1}{2}-d$ in $\mathbb{S}^{m}$, so that $\mathbb{S}^{m} / \mathcal{L}^{\perp} \simeq \mathbb{R}^{d}$, and we can consider the canonical map

$$
\pi_{\mathcal{L}}: \mathbb{S}^{m} \rightarrow \mathbb{S}^{m} / \mathcal{L}^{\perp}
$$

This is precisely the linear map which takes a sample covariance matrix $S$ to its canonical sufficient statistics. The chosen basis of $\mathcal{L}$ allows us to identify this map with

$$
\pi_{\mathcal{L}}: \mathbb{S}^{m} \rightarrow \mathbb{R}^{d}, S \mapsto\left(\left\langle S, K_{1}\right\rangle, \ldots,\left\langle S, K_{d}\right\rangle\right)
$$

We write $\mathcal{C}_{\mathcal{L}}$ for the image of the positive-definite cone $\mathbb{S}_{s \cdot 0}^{m}$ under the map $\pi_{\mathcal{L}}$. We call $\mathcal{C}_{\mathcal{L}}$ the cone of sufficient statistics. The following result explains the duality between the two red curves in Fig. 1.
Proposition 2.1. The cone of sufficient statistics is the convex dual to the cone of concentration matrices. The basis-free version of this duality states

$$
\mathcal{C}_{\mathcal{L}}=\left\{S \in \mathbb{S}^{m} / \mathcal{L}^{\perp}:\langle S, K\rangle>0 \text { for all } K \in \mathcal{K}_{\mathcal{L}}\right\}
$$

The basis-dependent version of this duality, in terms of (5) and (6), states

$$
\mathcal{C}_{\mathcal{L}}=\left\{\left(t_{1}, \ldots, t_{d}\right) \in \mathbb{R}^{d}: \sum_{i=1}^{d} t_{i} \lambda_{i}>0 \text { for all }\left(\lambda_{1}, \ldots, \lambda_{d}\right) \in \mathcal{K}_{\mathcal{L}}\right\}
$$

Proof. Let $\mathcal{K}_{\mathcal{L}}^{\vee}$ denote the right-hand side of (7) and let $M=\binom{m+1}{2}$. Using the fact that the $M$-dimensional convex cone $\mathbb{S}_{>0}^{m}$ is self-dual, general duality theory for convex cones implies

$$
\mathcal{K}_{\mathcal{L}}^{\vee}=\left(\mathbb{S}_{>0}^{m} \cap \mathcal{L}\right)^{\vee}=\left(\mathbb{S}_{>0}^{m}+\mathcal{L}^{\perp}\right) / \mathcal{L}^{\perp}=\mathcal{C}_{\mathcal{L}}
$$

To derive (8) from (7), we pick any basis $U_{1}, \ldots, U_{M}$ of $\mathbb{S}^{m}$ whose first $d$ elements serve as the dual basis to $K_{1}, \ldots, K_{d}$, and whose last $\binom{m+1}{2}-d$ elements span $\mathcal{L}^{\perp}$. Hence $\left\langle U_{i}, K_{j}\right\rangle=\delta_{i j}$ for all $i, j$. Every matrix $U$ in $\mathbb{S}^{m}$ has a unique representation $U=\sum_{i=1}^{M} t_{i} U_{i}$, and its image under the map (6) equals $\pi_{\mathcal{L}}(U)=\left(t_{1}, \ldots, t_{d}\right)$. For any matrix $K=\sum_{j=1}^{d} \lambda_{j} K_{j}$ in $\mathcal{L}$ we have $\langle U, K\rangle=\sum_{i=1}^{d} t_{i} \lambda_{i}$, and this expression is positive for all $K \in \mathcal{K}_{\mathcal{L}}$ if and only if $\left(t_{1}, \ldots, t_{d}\right)$ lies in $\mathcal{C}_{\mathcal{L}}$.

It can be shown that both the cone $\mathcal{K}_{\mathcal{L}}$ of concentration matrices and its dual, the cone $\mathcal{C}_{\mathcal{L}}$ of sufficient statistics, are well-behaved in the following sense. Their topological closures are closed convex cones that are dual to each other, and they are obtained by respectively intersecting and projecting the closed cone $\mathbb{S}_{>0}^{m}$ of positive semidefinite matrices. In symbols, these closed semi-algebraic cones satisfy

$$
\overline{\mathcal{K}_{\mathcal{L}}}=\mathcal{L} \cap \mathbb{S}_{>0}^{m} \quad \text { and } \quad \overline{\mathcal{C}_{\mathcal{L}}}=\pi_{\mathcal{L}}\left(\mathbb{S}_{>0}^{m}\right)
$$

One of our objectives will be to explore the geometry of their boundaries

$$
\partial \mathcal{K}_{\mathcal{L}}:=\overline{\mathcal{K}_{\mathcal{L}}} \backslash \mathcal{K}_{\mathcal{L}} \quad \text { and } \quad \partial \mathcal{C}_{\mathcal{L}}:=\overline{\mathcal{C}_{\mathcal{L}}} \backslash \mathcal{C}_{\mathcal{L}}
$$

These are convex algebraic hypersurfaces in $\mathbb{R}^{d}$, as seen in Example 1.1. The statistical theory of exponential families implies the following corollary concerning the geometry of their interiors:

Corollary 2.2. The map $K \mapsto T=\pi_{\mathcal{L}}\left(K^{-1}\right)$ is a homeomorphism between the dual pair of open cones $\mathcal{K}_{\mathcal{L}}$ and $\mathcal{C}_{\mathcal{L}}$. The inverse map $T \mapsto K$ takes the sufficient statistics to the MLE of the concentration matrix. Here, $K^{-1}$ is the unique maximizer of the determinant over the spectrahedron $\pi_{\mathcal{L}}^{-1}(T) \cap \mathbb{S}_{>0}^{m}$.

One natural first step in studying this picture is to simplify it by passing to the complex numbers $\mathbb{C}$. This allows us to relax various inequalities over the real numbers $\mathbb{R}$ and to work with varieties over the algebraic closed field $\mathbb{C}$. We thus identify our model $\mathcal{L}^{-1}$ with its Zariski closure in the $\left(\binom{m+1}{2}-1\right)$ dimensional complex projective space $\mathbb{P}\left(\mathbb{S}^{m}\right)$. Let $P_{\mathcal{L}}$ denote the homogeneous prime ideal of all polynomials in $\mathbb{R}[\Sigma]=\mathbb{R}\left[s_{11}, s_{12}, \ldots, s_{m m}\right]$ that vanish on $\mathcal{L}^{-1}$. One way to compute $P_{\mathcal{L}}$ is to eliminate the entries of an indeterminate symmetric $m \times m$-matrix $K$ from the following system of equations:

$$
\Sigma \cdot K=\operatorname{Id}_{m}, \quad K \in \mathcal{L}
$$

Given a sample covariance matrix $S$, its maximum likelihood estimate $\hat{\Sigma}$ can be computed algebraically, as in Example 1.1. We do this by solving the following zero-dimensional system of polynomial equations:

$$
\Sigma \cdot K=\operatorname{Id}_{m}, \quad K \in \mathcal{L}, \quad \Sigma-S \in \mathcal{L}^{\perp}
$$

In the present paper we focus on the systems (10) and (11). Specifically, for various classes of linear concentration models $\mathcal{L}$, we seek to answer the following three guiding questions. Example 1.1 served to introduce these three questions. Many more examples will be featured throughout our discussion.
Question 1. What can be said about the geometry of the $(d-1)$-dimensional projective variety $\mathcal{L}^{-1}$ ? What is the degree of this variety, and what are the minimal generators of its prime ideal $P_{\mathcal{L}}$ ?
Question 2. The map taking a sample covariance matrix $S$ to its maximum likelihood estimate $\hat{\Sigma}$ is an algebraic function. Its degree is the ML degree of the model $\mathcal{L}$. See (Drton et al. 2009, Def. 2.1.4). Can we find a formula for this ML degree? Which models $\mathcal{L}$ have their ML degree equal to 1 ?
Question 3. The Zariski closure of the boundary $\partial \mathcal{C}_{\mathcal{L}}$ of the cone of sufficient statistics $\mathcal{C}_{\mathcal{L}}$ is a hypersurface in the complex projective space $\mathbb{P}^{d-1}$. What is the defining polynomial $H_{\mathcal{L}}$ of this hypersurface?

# 2.2 Generic linear concentration models 

In this subsection we examine the case when $\mathcal{L}$ is a generic subspace of dimension $d$ in $\mathbb{S}^{m}$. Here "generic" is understood in the sense of algebraic geometry. In terms of the model representation (1), this means that the matrices $K_{1}, \ldots, K_{d}$ were chosen at random. This is precisely the hypothesis made by Nie et al. (2009), and one of our goals is to explain the connection of Questions 1-3 to that paper.

To begin with, we establish the result that the two notions of degree coincide in the generic case.
Theorem 2.3. The ML degree of the model (1) defined by a generic linear subspace $\mathcal{L}$ of dimension $d$ in $\mathbb{S}^{m}$ equals the degree of the projective variety $\mathcal{L}^{-1}$. That degree is denoted $\phi(m, d)$ and it satisfies

$$
\phi(m, d)=\phi\left(m,\binom{m+1}{2}+1-d\right)
$$

We calculated the ML degree $\phi(m, d)$ of the generic model $\mathcal{L}$ for all matrix sizes up to $m=6$ :


This table was computed with the software Macaulay $2^{2}$, using the commutative algebra techniques discussed in the proof of Theorem 2.3. At this point, readers from statistics are advised to skip the algebraic technicalities in the rest of this section and to go straight to Section 4 on graphical models.

The last three entries in each row follow from Bézout's Theorem because $P_{\mathcal{L}}$ is a complete intersection when the codimension of $\mathcal{L}^{-1}$ in $\mathbb{P}\left(\mathbb{S}^{m}\right)$ is at most two. Using the duality relation (12), we conclude

$$
\phi(m, d)=(m-1)^{d-1} \quad \text { for } d=1,2,3
$$

When $\mathcal{L}^{-1}$ has codimension 3 , it is the complete intersection defined by three generic linear combinations of the comaximal minors. From this complete intersection we must remove the variety of $m \times m$-symmetric matrices of rank $\leq m-2$, which has also codimension 3 and has degree $\binom{m+1}{3}$. Hence:

$$
\phi(m, 4)=(m-1)^{3}-\binom{m+1}{3}=\frac{1}{6}(5 m-3)(m-1)(m-2)
$$

When $d$ is larger than 4 , this approach leads to a problem in residual intersection theory. A formula due to Stückrad (1992), rederived in recent work by Chardin et al. (2009) on this subject, implies that

$$
\phi(m, 5)=\frac{1}{12}(m-1)(m-2)\left(7 m^{2}-19 m+6\right)
$$

For any fixed dimension $d$, our ML degree $\phi(m, d)$ seems to be a polynomial function of degree $d-1$ in $m$, but it gets progressively more challenging to compute explicit formulas for these polynomials.

Proof of Theorem 2.3. Let $I$ be the ideal in the polynomial ring $\mathbb{R}[\Sigma]=\mathbb{R}\left[s_{11}, s_{12}, \ldots, s_{m m}\right]$ that is generated by the $(m-1) \times(m-1)$-minors of the symmetric $m \times m$-matrix $\Sigma=\left(s_{i j}\right)$. Kotzev (1991) proved that the Rees algebra $\mathcal{R}(I)$ of the ideal $I$ is equal to the symmetric algebra of $I$. Identifying the generators of $I$ with the entries of another symmetric matrix of unknowns $K=\left(k_{i j}\right)$, we represent this Rees algebra as $\mathcal{R}(I)=\mathbb{R}[\Sigma, K] / J$ where the ideal $J$ is obtained by eliminating the unknown $t$ from the matrix equation $\Sigma \cdot K=t \cdot \operatorname{Id}_{m}$. The presentation ideal $J=\left\langle\Sigma \cdot K-t \operatorname{Id}_{m}\right\rangle \cap \mathbb{R}[\Sigma, K]$ is prime and it is homogeneous with respect to the natural $\mathbb{N}^{2}$-grading on the polynomial ring $\mathbb{R}[\Sigma, K]$. Its variety $V(J)$ in $\mathbb{P}^{M-1} \times \mathbb{P}^{M-1}$ is the closure of the set of pairs of symmetric matrices that are inverse to each other. Here $M=\binom{m+1}{2}$. Both the dimension and the codimension of $V(J)$ is equal to $M-1$.

[^0]
[^0]:    2 www.math.uiuc.edu/Macaulay2/

We now make use of the notion of multidegree introduced in the text book of Miller and Sturmfels (2004). Namely, we consider the bidegree of the Rees algebra $\mathcal{R}(I)=\mathbb{R}[\Sigma, K] / J$ with respect to its $\mathbb{N}^{2}$ grading. This bidegree is a homogeneous polynomial in two variables $x$ and $y$ of degree $M-1$. Using notation as in (Miller and Sturmfels 2004, Def. 8.45) and (Nie et al. 2009, Thm. 10), we claim that

$$
\mathcal{C}(\mathcal{R}(I) ; x, y)=\sum_{d=1}^{M} \phi(m, d) x^{M-d} y^{d-1}
$$

Indeed, the coefficient of $x^{M-d} y^{d-1}$ in the expansion of $\mathcal{C}(\mathcal{R}(I) ; x, y)$ equals the cardinality of the finite variety $V(J) \cap(\mathcal{M} \times \mathcal{L})$, where $\mathcal{L}$ is a generic plane of dimension $d-1$ in the second factor $\mathbb{P}^{M-1}$ and $\mathcal{M}$ is a generic plane of dimension $M-d$ in the first factor $\mathbb{P}^{M-1}$. We now take $\mathcal{M}$ to be the specific plane which is spanned by the image of $\mathcal{L}^{\perp}$ and one extra generic point $S$, representing a random sample covariance matrix. Thus our finite variety is precisely the same as the one described by the affine equations in (11), and we conclude that its cardinality equals the ML degree $\phi(m, d)$.

Note that $V(J) \cap\left(\mathbb{P}^{M-1} \times \mathcal{L}\right)$ can be identified with the variety $V\left(P_{\mathcal{L}}\right)$ in $\mathbb{P}^{M-1}$. The argument in the previous paragraph relied on the fact that $P_{\mathcal{L}}$ is Cohen-Macaulay, which allowed us to chose any subspace $\mathcal{M}$ for our intersection count provided it is disjoint from $V\left(P_{\mathcal{L}}\right)$ in $\mathbb{P}^{M-1}$. This proves that $\phi(m, d)$ coincides with the degree of $V\left(P_{\mathcal{L}}\right)$. The Cohen-Macaulay property of $P_{\mathcal{L}}$ follows from a result of Herzog et al. (1985) together with the aforementioned work of Kotzev (1991) which shows that the ideal $I$ has sliding depth. Finally, the duality (12) is obvious for the coefficients of the bidegree (13) of the Rees algebra $\mathcal{R}(I)$ since its presentation ideal $J$ is symmetric under swapping $K$ and $\Sigma$.

We now come to our third question, which is to determine the Zariski closure $V\left(H_{\mathcal{L}}\right)$ of the boundary of the cone $\mathcal{C}_{\mathcal{L}}=\mathcal{K}_{\mathcal{L}}^{\vee}$. Let us assume now that $\mathcal{L}$ is any $d$-dimensional linear subspace of $\mathbb{S}^{m}$, not necessarily generic. The Zariski closure of $\partial \mathcal{K}_{\mathcal{L}}$ is the hypersurface $\{\operatorname{det}(K)=0\}$ given by the vanishing of the determinant of $K=\sum_{i=1}^{d} \lambda_{i} K_{i}$. This determinant is a polynomial of degree $d$ in $\lambda_{1}, \ldots, \lambda_{d}$. Our task is to compute the dual variety in the sense of projective algebraic geometry of each irreducible component of this hypersurface. See (Nie et al. 2009, §5) for basics on projective duality. We also need to compute the dual variety for its singular locus, and for the singular locus of the singular locus, etc.

Each singularity stratum encountered along the way needs to be decomposed into irreducible components, whose duals need to be examined. If such a component has a real point that lies in $\partial \mathcal{K}_{\mathcal{L}}$ and if its dual variety is a hypersurface then that hypersurface appears in $H_{\mathcal{L}}$. How to run this procedure in practice is shown in Example 4.10. For now, we summarize the construction informally as follows.
Proposition 2.4. Each irreducible hypersurface in the Zariski closure of $\partial \mathcal{C}_{\mathcal{L}}$ is the projectively dual variety to some irreducible component of the hypersurface $\{\operatorname{det}(K)=0\}$, or it is dual to some irreducible variety further down in the singularity stratification of the hypersurface $\{\operatorname{det}(K)=0\} \subset \mathbb{P}^{d-1}$.

The singular stratification of $\{\operatorname{det}(K)=0\}$ can be computed by applying primary decomposition to the ideal of $p \times p$-minors of $K$ for $1 \leq p \leq m$. If $I$ is any minimal prime of such a determinantal ideal then its dual variety is computed as follows. Let $c=\operatorname{codim}(I)$ and consider the Jacobian matrix of $I$. The rows of the Jacobian matrix are the derivatives of the generators of $I$ with respect to the unknowns $\lambda_{1}, \ldots, \lambda_{d}$. Let $J$ be the ideal generated by $I$ and the $c \times c$-minors of the matrix formed by augmenting the Jacobian matrix by the extra row $\left(t_{1}, t_{2}, \ldots, t_{d}\right)$. We saturate $J$ by the $c \times c$-minors of the Jacobian, and thereafter we compute the elimination ideal $J \cap \mathbb{R}\left[t_{1}, t_{2}, \ldots, t_{d}\right]$. If this elimination ideal is principal, we retain its generator. The desired polynomial $H_{\mathcal{L}}$ is the product of these principal generators, as $I$ runs over all such minimal primes whose variety has a real point on the convex hypersurface $\partial \mathcal{K}_{\mathcal{L}}$.

Proposition 2.4 is visualized also in Fig. 4 below. Let us now apply this result in the case when the subspace $\mathcal{L}$ is generic of dimension $d$. The ideal of $p \times p$-minors of $K$ defines a subvariety of $\mathbb{P}^{d-1}$, which is irreducible whenever it is positive-dimensional (by Bertini's Theorem). It is known from (Nie et al. 2009, Prop. 5) that the dual variety to that determinantal variety is a hypersurface if and only if

$$
\binom{m-p+2}{2} \leq d-1 \quad \text { and } \quad\binom{p}{2} \leq\binom{ m+1}{2}-d+1
$$

Assuming that these inequalities hold, the dual hypersurface is defined by an irreducible homogeneous polynomial whose degree we denote by $\delta(d-1, m, p-1)$. This notation is consistent with Nie et al. (2009) where this number is called the algebraic degree of semidefinite programming (SDP).

Corollary 2.5. For a generic d-dimensional subspace $\mathcal{L}$ of $\mathbb{S}^{m}$, the polynomial $H_{\mathcal{L}}$ is the product of irreducible polynomials of degree $\delta(d-1, m, p-1)$. That number is the algebraic degree of semidefinite programming. Here $p$ runs over integers that satisfy (14) and $\partial \mathcal{K}_{\mathcal{L}}$ contains a matrix of rank $p-1$.

# 3 Diagonal Matrices, Matroids and Polytopes 

This section concerns the case when $\mathcal{L}$ is a $d$-dimensional space consisting only of diagonal matrices in $\mathbb{S}^{m}$. Here, the set $\mathcal{L}_{>0}^{-1}$ of covariance matrices in the model also consists of diagonal matrices only, and we may restrict our considerations to the space $\mathbb{R}^{m}$ of diagonal matrices in $\mathbb{S}^{m}$. Thus, throughout this section, our ambient space is $\mathbb{R}^{m}$, and we identify $\mathbb{R}^{m}$ with its dual vector space via the standard inner product $\langle u, v\rangle=\sum_{i=1}^{m} u_{i} v_{i}$. We fix any $d \times m$-matrix $A$ whose rows space equals $\mathcal{L}$, and we assume that $\mathcal{L} \cap \mathbb{R}_{>0}^{m} \neq \emptyset$. We consider the induced projection of the open positive orthant

$$
\pi: \mathbb{R}_{>0}^{m} \rightarrow \mathbb{R}^{d}, x \mapsto A x
$$

Since $\mathcal{L}=\operatorname{rowspace}(A)$ contains a strictly positive vector, the image of $\pi$ is a pointed polyhedral cone, namely $\mathcal{C}_{\mathcal{L}}=\operatorname{pos}(A)$ is the cone spanned by the columns of $A$. Each fiber of $\pi$ is a bounded convex polytope, and maximum likelihood estimation amounts to finding a distinguished point $\hat{x}$ in that fiber.

The problem of characterizing the existence of the MLE in this situation amounts to a standard problem of geometric combinatorics (see e.g. Ziegler (1995)), namely, to computing the facet description of the convex polyhedral cone spanned by the columns of $A$. For a given vector $t \in \mathbb{R}^{d}$ of sufficient statistics, the maximum likelihood estimate exists in this diagonal concentration model if and only if $t$ lies in the interior of the cone $\operatorname{pos}(A)$. This happens if and only if all facet inequalities are strict for $t$.

This situation is reminiscent of Birch's Theorem for toric models in algebraic statistics (Pachter and Sturmfels 2005, Theorem 1.10), and, indeed, the combinatorial set-up for deciding the existence of the MLE is identical to that for toric models. For a statistical perspective see Eriksson et al. (2006). However, the algebraic structure here is not that of toric models, described in (Pachter and Sturmfels 2005, §1.2.2), but that of the linear models in (Pachter and Sturmfels 2005, §1.2.1).

Our model here is not toric but it is the coordinatewise reciprocal of an open polyhedral cone:

$$
\mathcal{L}_{>0}^{-1}=\left\{u \in \mathbb{R}_{>0}^{m}: u^{-1}=\left(u_{1}^{-1}, u_{2}^{-1}, \ldots, u_{m}^{-1}\right) \in \mathcal{L}\right\}
$$

As in Section 2, we view its Zariski closure $\mathcal{L}^{-1}$ as a subvariety in complex projective space:

$$
\mathcal{L}^{-1}=\left\{u \in \mathbb{P}^{m-1}: u^{-1}=\left(u_{1}^{-1}, u_{2}^{-1}, \ldots, u_{m}^{-1}\right) \in \mathcal{L}\right\}
$$

Maximum likelihood estimation means intersecting the variety $\mathcal{L}^{-1}$ with the fibers of $\pi$.
Example 3.1. Let $m=4, d=2$ and take $\mathcal{L}$ to be the row space of the matrix

$$
A=\left(\begin{array}{llll}
3 & 2 & 1 & 0 \\
0 & 1 & 2 & 3
\end{array}\right)
$$

The corresponding statistical model consists of all multivariate normal distributions on $\mathbb{R}^{4}$ whose concentration matrix has the diagonal form

$$
K=\left(\begin{array}{ccccc}
3 \lambda_{1} & 0 & 0 & 0 \\
0 & 2 \lambda_{1}+\lambda_{2} & 0 & 0 \\
0 & 0 & \lambda_{1}+2 \lambda_{2} & 0 \\
0 & 0 & 0 & 3 \lambda_{2}
\end{array}\right)
$$

Our variety $\mathcal{L}^{-1}$ is the curve in $\mathbb{P}^{3}$ parametrized by the inverse diagonal matrices which we write as $K^{-1}=\operatorname{diag}\left(x_{1}, x_{2}, x_{3}, x_{4}\right)$. The prime ideal $P_{\mathcal{L}}$ of this curve is generated by three quadratic equations:

$$
x_{2} x_{3}-2 x_{2} x_{4}+x_{3} x_{4}=2 x_{1} x_{3}-3 x_{1} x_{4}+x_{3} x_{4}=x_{1} x_{2}-3 x_{1} x_{4}+2 x_{2} x_{4}=0
$$

Consider any sample covariance matrix $S=\left(s_{i j}\right)$, with sufficient statistics

$$
t_{1}=3 s_{11}+2 s_{22}+s_{33}>0 \quad \text { and } \quad t_{2}=s_{22}+2 s_{33}+3 s_{44}>0
$$

The MLE for these sufficient statistics is the unique positive solution $\hat{x}$ of the three quadratic equations above, together with the two linear equations

$$
3 x_{1}+2 x_{2}+x_{3}=t_{1} \quad \text { and } \quad x_{2}+2 x_{3}+3 x_{4}=t_{2}
$$

We find that $\hat{x}$ is an algebraic function of degree 3 in the sufficient statistics $\left(t_{1}, t_{2}\right)$, so the ML degree of the model $K$ equals 3 . This is consistent with formula (16) below, since $\binom{4-1}{2-1}=3$.

We now present the solutions to our three guiding problems for arbitrary $d$-dimensional subspaces $\mathcal{L}$ of the space $\mathbb{R}^{m}$ of $m \times m$-diagonal matrices. The degree of the projective variety $\mathcal{L}^{-1}$ and its prime ideal $P_{\mathcal{L}}$ are known from work of Terao (2002) and its refinements due to Proudfoot and Speyer (2006). Namely, the degree of $\mathcal{L}^{-1}$ equals the beta-invariant of the rank $m-d$ matroid on $[m]=\{1,2, \ldots, m\}$ associated with $\mathcal{L}$. We denote this beta-invariant by $\beta(\mathcal{L})$. For matroid basics see White (1992).

The beta-invariant $\beta(\mathcal{L})$ is known to equal the number of bounded regions in the $(m-d)$-dimensional hyperplane arrangement (cf. Zaslavsky (1975)) obtained by intersecting the affine space $u+\mathcal{L}^{\perp}$ with the $m$ coordinate hyperplanes $\left\{x_{i}=0\right\}$. Here $u$ can be any generic vector in $\mathbb{R}_{>0}^{m}$. One of these regions, namely the one containing $u$, is precisely the fiber of $\pi$. If $\mathcal{L}$ is a generic $d$-dimensional linear subspace of $\mathbb{R}^{m}$, meaning that the above matroid is the uniform matroid, then the beta-invariant equals

$$
\beta(\mathcal{L})=\binom{m-1}{d-1}
$$

For non-generic subspaces $\mathcal{L}$, this binomial coefficient is always an upper bound for $\beta(\mathcal{L})$.
Theorem 3.2. (Proudfoot and Speyer (2006); Terao (2002)) The degree of the projective variety $\mathcal{L}^{-1}$ equals the beta-invariant $\beta(\mathcal{L})$. Its prime ideal $P_{\mathcal{L}}$ is generated by the homogeneous polynomials

$$
\sum_{i \in \operatorname{supp}(v)} v_{i} \cdot \prod_{j \neq i} x_{j}
$$

where $v$ runs over all non-zero vectors of minimal support in $\mathcal{L}^{\perp}$.
For experts in combinatorial commutative algebra, we note that Proudfoot and Speyer (2006) actually prove the following stronger results. The homogeneous polynomials (17) form a universal Gröbner basis of $P_{\mathcal{L}}$. The initial monomial ideal of $P_{\mathcal{L}}$ with respect to any term order is the Stanley-Reisner ideal of the corresponding broken circuit complex of the matroid of $\mathcal{L}$. Hence the Hilbert series of $P_{\mathcal{L}}$ is the rational function obtained by dividing the h-polynomial $h(t)$ of the broken circuit complex by $(1-t)^{d}$. In particular, the degree of $P_{\mathcal{L}}$ is the number $h(1)=\beta(\mathcal{L})$ of broken circuit bases (White 1992, §7).

We next consider Question 2 in the diagonal case. The maximum likelihood map takes each vector $t$ in the cone of sufficient statistics $\mathcal{C}_{\mathcal{L}}=\operatorname{pos}(A)$ to a point of its fiber, namely:

$$
\hat{x}=\operatorname{argmax}\left\{\sum_{i=1}^{m} \log \left(x_{i}\right): x \in \mathbb{R}_{>0}^{m} \text { and } A x=t\right\}
$$

This is the unique point in the polytope $\pi^{-1}(t)=\left\{x \in \mathbb{R}_{>0}^{m}\right.$ and $\left.A x=t\right\}$ which maximizes the product $x_{1} x_{2} \cdots x_{n}$ of the coordinates. It is also the unique point in $\pi^{-1}(t)$ that lies in the reciprocal linear variety $\mathcal{L}^{-1}$. In the linear programming literature, the point $\hat{x}$ is known as the analytic center of the polytope $\pi^{-1}(t)$. In Section 2 we discussed the extension of this concept from linear programming to semidefinite programming: the analytic center of a spectrahedron is the unique point $\hat{\Sigma}$ at which the determinant function attains its maximum. For an applied perspective see Vandenberghe et al. (1996).

For any linear subspace $\mathcal{L}$ in $\mathbb{S}^{m}$, the algebraic degree of the maximum likelihood map $t \mapsto \hat{\Sigma}$ is always less than or equal to the degree of the projective variety $\mathcal{L}^{-1}$. We saw in Theorem 2.3 that these degrees are equal for generic $\mathcal{L}$. We next show that the same conclusion holds for diagonal subspaces $\mathcal{L}$.

Corollary 3.3. The ML degree of any diagonal linear concentration model $\mathcal{L} \subset \mathbb{R}^{m} \subset \mathbb{S}^{m}$ is equal to the beta-invariant $\beta(\mathcal{L})$ of the corresponding matroid of rank $m-d$ on $\{1,2, \ldots, m\}$.

Proof. The beta-invariant $\beta(\mathcal{L})$ counts the bounded regions in the arrangement of hyperplanes arising from the given facet description of the polytope $\pi^{-1}(t)$. Varchenko's Formula for linear models, derived in (Pachter and Sturmfels 2005, Theorem 1.5), states that the optimization problem (18) has precisely one real critical point in each bounded region, and that there are no other complex critical points.

A fundamental question regarding the ML degree of any class of algebraic statistical models is to characterize those models which have ML degree one. These are the models whose maximum likelihood estimator is a rational function in the sufficient statistics (Drton et al. 2009, §2.1). In the context here, we have the following characterization of matroids whose beta-invariant $\beta(\mathcal{L})$ equals one.
Corollary 3.4. The ML degree $\beta(\mathcal{L})$ of a diagonal linear concentration model $\mathcal{L}$ is equal to one if and only if the matroid of $\mathcal{L}$ is the graphic matroid of a series-parallel graph.

Proof. The equivalence of series-parallel and $\beta=1$ first appeared in (Brylawski 1971, Theorem 7.6).
We now come to Question 3 which concerns the duality of convex cones in Proposition 2.1. In the diagonal case, the geometric view on this duality is as follows. The cone of sufficient statistics equals $\mathcal{C}_{\mathcal{L}}=\operatorname{pos}(A)$ and its convex dual is the cone $\mathcal{K}_{\mathcal{L}}=\operatorname{rowspace}(A) \cap \mathcal{L}$. Both cones are convex, polyhedral, pointed, and have dimension $d$. By passing to their cross sections with suitable affine hyperplanes, we can regard the two cones $\mathcal{C}_{\mathcal{L}}$ and $\mathcal{K}_{\mathcal{L}}$ as a dual pair of $(d-1)$-dimensional convex polytopes.

The hypersurface $\{\operatorname{det}(K)=0\}$ is a union of $m$ hyperplanes. The strata in its singularity stratification, discussed towards the end of Section 2, correspond to the various faces $F$ of the polytope $\mathcal{K}_{\mathcal{L}}$. The dual variety to a face $F$ is the complementary face of the dual polytope $\mathcal{C}_{\mathcal{L}}$, and hence the codimension of that dual variety equals one if and only if $F$ is a vertex ( $=0$-dimensional face) of $\mathcal{K}_{\mathcal{L}}$. This confirms that the polynomial $H_{\mathcal{L}}$ sought in Question 3 is the product of all facet-definining linear forms of $\mathcal{C}_{\mathcal{L}}$.

Corollary 2.2 furnishes a homeomorphism $u \mapsto A u^{-1}$ from the interior of the polytope $\mathcal{K}_{\mathcal{L}}$ onto the interior of its dual polytope $\mathcal{C}_{\mathcal{L}}$. The inverse to the rational function $u \mapsto A u^{-1}$ is an algebraic function whose degree is the beta-invariant $\beta(\mathcal{L})$. This homeomorphism is the natural generalization, from simplices to arbitrary polytopes, of the classical Cremona transformation of projective geometry. We close this section with a nice 3-dimensional example which illustrates this homeomorphism.
Example 3.5 (How to morph a cube into an octahedron). Fix $m=8, d=4$, and $\mathcal{L}$ the row space of

$$
A=\left(\begin{array}{cccccc}
1 & -1 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & -1 & 0 & 0 \\
0 & 0 & 0 & 0 & 1 & -1 \\
1 & 1 & 1 & 1 & 1 & 1
\end{array}\right)
$$

We identify the cone $\mathcal{K}_{\mathcal{L}}=\operatorname{rowspace}(A) \cap \mathbb{R}_{>0}^{6}$ with $\left\{\lambda \in \mathbb{R}^{4}: \lambda \cdot A>0\right\}$. This is the cone over the 3 -cube, which is obtained by setting $\lambda_{4}=1$. The dual cone $\mathcal{C}_{\mathcal{L}}=\operatorname{pos}(A)$ is spanned by the six columns of the matrix $A$. It is the cone over the octahedron, which is obtained by setting $t_{4}=1$.

We write the homeomorphism $u \mapsto A u^{-1}$ between these two four-dimensional cones in terms of the coordinates of $\lambda$ and $t$. Explicitly, the equation $t=A \cdot(\lambda A)^{-1}$ translates into the scalar equations:

$$
\begin{aligned}
& t_{1}=\frac{1}{\lambda_{4}+\lambda_{1}}-\frac{1}{\lambda_{4}-\lambda_{1}} \\
& t_{2}=\frac{1}{\lambda_{4}+\lambda_{2}}-\frac{1}{\lambda_{4}-\lambda_{2}} \\
& t_{3}=\frac{1}{\lambda_{4}+\lambda_{3}}-\frac{1}{\lambda_{4}-\lambda_{3}} \\
& t_{4}=\frac{1}{\lambda_{4}+\lambda_{1}}+\frac{1}{\lambda_{4}-\lambda_{1}}+\frac{1}{\lambda_{4}+\lambda_{2}}+\frac{1}{\lambda_{4}-\lambda_{2}}+\frac{1}{\lambda_{4}+\lambda_{3}}+\frac{1}{\lambda_{4}-\lambda_{3}}
\end{aligned}
$$

Substituting $\lambda_{4}=1$, we get the bijection $\left(\lambda_{1}, \lambda_{2}, \lambda_{3}\right) \mapsto\left(t_{1} / t_{4}, t_{2} / t_{4}, t_{3} / t_{4}\right)$ between the open cube $(-1,+1)^{3}$ and the open octahedron $\left\{t \in \mathbb{R}^{3}:\left|t_{1}\right|+\left|t_{2}\right|+\left|t_{3}\right|<1\right\}$. The inverse map $t \mapsto \lambda$ is an algebraic function of degree $\beta(\mathcal{L})=7$. That the ML degree of this model is 7 can be seen as follows. The fibers $\pi^{-1}(t)$ are the convex polygons which can be obtained from a regular hexagon by parallel displacement of its six edges. The corresponding arrangement of six lines has 7 bounded regions.

# 4 Gaussian Graphical Models 

An undirected Gaussian graphical model arises when the subspace $\mathcal{L}$ of $\mathbb{S}^{m}$ is defined by the vanishing of some off-diagonal entries of the concentration matrix $K$. We fix a graph $G=([m], E)$ with vertex set $[m]=\{1,2, \ldots, m\}$ and whose edge set $E$ is assumed to contain all self-loops. A basis for $\mathcal{L}$ is the set $\left\{K_{i j} \mid(i, j) \in E\right\}$ of matrices $K_{i j}$ with a single 1-entry in position $(i, j)$ and 0 -entries in all other positions. We shall use the notation $\mathcal{K}_{G}, \mathcal{C}_{G}, P_{G}$ for the objects $\mathcal{K}_{\mathcal{L}}, \mathcal{C}_{\mathcal{L}}, P_{\mathcal{L}}$, respectively. Given a sample covariance matrix $S$, the set $\operatorname{fiber}_{G}(S)$ consists of all positive definite matrices $\Sigma \in \mathbb{S}_{>0}^{m}$ with

$$
\Sigma_{i j}=S_{i j} \quad \text { for all }(i, j) \in E
$$

The cone of concentration matrices $\mathcal{K}_{G}$ is important for semidefinite matrix completion problems. Its closure was denoted $\mathcal{P}_{G}$ by Laurent (2001a,b). The dual cone $\mathcal{C}_{G}$ consists of all partial matrices $T \in \mathbb{R}^{E}$ with entries in positions $(i, j) \in E$, which can be extended to a full positive definite matrix. So, maximum likelihood estimation in Gaussian graphical models corresponds to the classical positive definite matrix completion problem (Barrett et al. 1993; Grone et al. 1984; Barrett et al. 1996; Laurent 2001b). In this section we investigate our three guiding questions, first for chordal graphs, next for the chordless $m$-cycle $C_{m}$, then for all graphs with five or less vertices, and finally for the $m$-wheel $W_{m}$.

### 4.1 Chordal graphs

A graph $G$ is chordal (or decomposable) if every induced $m$-cycle in $G$ for $m \geq 4$ has a chord. A theorem due to Grone et al. (1984) fully resolves Question 3 when $G$ is chordal. Namely, a partial matrix $T \in \mathbb{R}^{E}$ lies in the cone $\mathcal{C}_{G}$ if and only if all principal minors $T_{C C}$ indexed by cliques $C$ in $G$ are positive definite. The "only if" direction in this statement is true for all graphs $G$, but the "if" direction holds only when $G$ is chordal. This result is equivalent to the characterization of chordal graphs as those that have sparsity order equal to one, i.e., all extreme rays of $\mathcal{K}_{G}$ are matrices of rank one. We refer to Agler et al. (1988) and Laurent (2001a) for details. From this characterization of chordal graphs in terms of sparsity order, we infer the following description of the Zariski closure of the boundary of $\mathcal{C}_{G}$.

Proposition 4.1. For a chordal graph $G$, the defining polynomial $H_{G}$ of $\partial \mathcal{C}_{G}$ is equal to

$$
H_{G}=\prod_{\substack{C \text { maximal } \\ \text { clique of } G}} \operatorname{det}\left(T_{C C}\right)
$$

We now turn to Question 2 regarding the ML degree of a Gaussian graphical model $G$. This number is here simply denoted by ML-degree $(G)$. Every chordal graph is a clique sum of complete graphs. We shall prove that the ML degree is multiplicative with respective to taking clique sums.

Lemma 4.2. Let $G$ be a clique sum of $n$ graphs $G_{1}, \ldots, G_{n}$. Then the following equality holds:

$$
M L \text {-degree }(G)=\prod_{i=1}^{n} M L \text {-degree }\left(G_{i}\right)
$$

Proof. We first prove this statement for $n=2$. Let $G$ be a graph which can be decomposed in disjoint subsets $(A, B, C)$ of the vertex set $V$, such that $C$ is a clique and separates $A$ from $B$. Let $G_{[W]}$ denote the induced subgraph on a vertex subset $W \subset V$. So, we wish to prove:

$$
\text { ML-degree }(G)=\text { ML-degree }\left(G_{[A \cup C]}\right) \cdot \text { ML-degree }\left(G_{[B \cup C]}\right)
$$

Given a generic matrix $S \in \mathbb{S}^{m}$, we fix $\Sigma \in \mathbb{S}^{m}$ with entries $\Sigma_{i j}=S_{i j}$ for $(i, j) \in E$ and unknowns $\Sigma_{i j}=z_{i j}$ for $(i, j) \notin E$. The ML degree of $G$ is the number of complex solutions to the equations

$$
\left(\Sigma^{-1}\right)_{i j}=0 \quad \text { for all }(i, j) \notin E
$$

Let $K=\Sigma^{-1}$ and denote by $K^{1}=\left(\Sigma_{[A \cup C]}\right)^{-1}$ (respectively, $K^{2}=\left(\Sigma_{[B \cup C]}\right)^{-1}$ ) the inverse of the submatrix of $\Sigma$ corresponding to the induced subgraph on $A \cup C$ (respectively, $B \cup C$ ). Using Schur complements, we can see that these matrices are related by the following block structure:

$$
K=\left(\begin{array}{ccc}
K_{A A}^{1} & K_{A C}^{1} & 0 \\
K_{C A}^{1} & K_{C C} & K_{C B}^{2} \\
0 & K_{B C}^{2} & K_{B B}^{2}
\end{array}\right), \quad K^{1}=\left(\begin{array}{ll}
K_{A A}^{1} & K_{A C}^{1} \\
K_{C A}^{1} & K_{C C}^{1}
\end{array}\right), \quad K^{2}=\left(\begin{array}{ll}
K_{C C}^{2} & K_{C B}^{2} \\
K_{B C}^{2} & K_{B B}^{2}
\end{array}\right)
$$

This block structure reveals that, when solving the system (20), one can solve for the variables $z_{i j}$ corresponding to missing edges in the subgraph $A \cup C$ independently from the variables over $B \cup C$ and $A \cup B$. This implies the equation (19). Induction yields the theorem for $n \geq 3$.

The following theorem characterizes chordal graphs in terms of their ML degree. It extends the equivalence of parts (iii) and (iv) in (Drton et al. 2009, Thm. 3.3.5) from discrete to Gaussian models.

Theorem 4.3. A graph $G$ is chordal if and only if ML-degree $(G)=1$.
Proof. The if-direction follows from Lemma 4.2 since every chordal graph is a clique sum of complete graphs, and a complete graph trivially has ML degree one. For the only-if direction suppose that $G$ is a graph that is not chordal. Then $G$ contains the chordless cycle $C_{m}$ as an induced subgraph for some $m \geq 4$. It is easy to see that the ML degree of any graph is bounded below by that of any induced subgraph. Hence what we must prove is that the chordless cycle $C_{m}$ has strictly positive ML degree. This is precisely the content of Lemma 4.7 below.

We now come to Question 1 which concerns the homogeneous prime ideal $P_{G}$ that defines the Gaussian graphical model as a subvariety of $\mathbb{P}\left(\mathbb{S}^{m}\right)$. Fix a symmetric $m \times m$-matrix of unknowns $\Sigma=\left(s_{i j}\right)$ and let $\Sigma_{i j}$ denote the comaximal minor obtained by deleting the $i$ th row and the $j$ th column from $\Sigma$. We shall define several ideals in $\mathbb{R}[\Sigma]$ that approximate $P_{G}$. The first is the saturation

$$
P_{G}^{\prime}=\left(\left\langle\operatorname{det}\left(\Sigma_{i j}\right) \mid(i, j) \in E\right\rangle:\langle\operatorname{det}(\Sigma)\rangle^{\infty}\right)
$$

This ideal is contained in the desired prime ideal, i.e. $P_{G}^{\prime} \subseteq P_{G}$. The two ideals have the same radical, but it might happen that they are not equal. One disadvantage of the ideal $P_{G}^{\prime}$ is that the saturation step (21) is computationally expensive and terminates only for very small graphs.

A natural question is whether the prime ideal $P_{G}$ can be constructed easily from the prime ideals $P_{G_{1}}$ and $P_{G_{2}}$ when $G$ is a clique sum of two smaller graphs $G_{1}$ and $G_{2}$. As in the proof of Lemma 4.2, we partition $[m]=A \cup B \cup C$, where $G_{1}$ is the induced subgraph on $A \cup C$, and $G_{2}$ is the induced subgraph on $B \cup C$. If $|C|=c$ then we say that $G$ is a $c$-clique sum of $G_{1}$ and $G_{2}$.

The following ideal is contained in $P_{G}$ and defines the same algebraic variety in the open cone $\mathbb{S}_{>0}^{m}$ :

$$
P_{G_{1}}+P_{G_{2}}+\langle(c+1) \times(c+1) \text {-minors of } \Sigma_{A \cup C, B \cup C}\rangle
$$

One might guess that (22) is equal to $P_{G}$, at least up to radical, but this fails for $c \geq 2$. Indeed we shall see in Example 4.5 that the variety of (22) can have extraneous components on the boundary $\mathbb{S}_{>0}^{m} \backslash \mathbb{S}_{>0}^{m}$ of the semidefinite cone. We do conjecture, however, that this equality holds for $c \leq 1$. This is easy to prove for $c=0$ when $G$ is disconnected and is the disjoint union of $G_{1}$ and $G_{2}$. The case $c=1$ is considerably more delicate. At present, we do not have a proof that (22) is prime for $c=1$, but we believe that even a lexicographic Gröbner basis for $P_{G}$ can be built by taking the union of such Gröbner basis for $P_{G_{1}}$ and $P_{G_{2}}$ with the $2 \times 2$-minors of $\Sigma_{A \cup C, B \cup C}$. This conjecture would imply the following.
Conjecture 4.4. The prime ideal $P_{G}$ of an undirected Gaussian graphical model is generated in degree $\leq 2$ if and only if each connected component of the graph $G$ is a 1-clique sum of complete graphs. In this case, $P_{G}$ has a Gröbner basis consisting of entries of $\Sigma$ and $2 \times 2$-minors of $\Sigma$.

This conjecture is an extension of the results and conjectures for (directed) trees in (Sullivant 2008, §5). Formulas for the degree of $P_{G}$ when $G$ is a tree are found in (Sullivant 2008, Corollaries 5.5 and 5.6). The "only if" direction in the first sentence of Conjecture 4.4 can be shown as follows. If $G$ is not chordal then it contains an $m$-cycle $(m \geq 4)$ as an induced subgraph, and, this gives rise to cubic generators for $P_{G}$, as seen in Subsection 4.2 below. If $G$ is chordal but is not a 1-clique sum of complete graphs, then its

decomposition involves a $c$-clique sum for some $c \geq 2$, and the right hand side of (22) contributes a minor of size $c+1 \geq 3$ to the minimal generators of $P_{G}$. The algebraic structure of chordal graphical models is more delicate in the Gaussian case then in the discrete case, and there is no Gaussian analogue to the characterizations of chordality in (i) and (ii) of (Drton et al. 2009, Theorem 3.3.5). This is highlighted by the following example which was suggested to us by Seth Sullivant.

Example 4.5. Let $G$ be the graph on $m=7$ vertices consisting of the triangles $\{i, 6,7\}$ for $i=1,2,3,4,5$. Then $G$ is chordal because it is the 2 -clique sum of these five triangles. The ideal $P_{G}$ is minimally generated by 105 cubics and one quintic. The cubics are spanned by the $3 \times 3$-minors of the matrices $\Sigma_{A \cup C, B \cup C}$ where $C=\{6,7\}$ and $\{A, B\}$ runs over all unordered partitions of $\{1,2,3,4,5\}$. These minors do not suffice to define the variety $V\left(P_{G}\right)$ set-theoretically. For instance, they vanish whenever the last two rows and columns of $\Sigma$ are zero. The additional quintic generator of $P_{G}$ equals

$$
\begin{aligned}
& s_{12} s_{13} s_{24} s_{35} s_{45}-s_{12} s_{13} s_{25} s_{34} s_{45}-s_{12} s_{14} s_{23} s_{35} s_{45}+s_{12} s_{14} s_{25} s_{34} s_{35} \\
& +s_{12} s_{15} s_{23} s_{34} s_{45}-s_{12} s_{15} s_{24} s_{34} s_{35}+s_{13} s_{14} s_{23} s_{25} s_{45}-s_{13} s_{14} s_{24} s_{25} s_{35} \\
& -s_{13} s_{15} s_{23} s_{24} s_{45}+s_{13} s_{15} s_{24} s_{25} s_{34}+s_{14} s_{15} s_{23} s_{24} s_{35}-s_{14} s_{15} s_{23} s_{25} s_{34}
\end{aligned}
$$

This polynomial is the pentad which is relevant for factor analysis (Drton et al. 2009, Example 4.2.8).
Given an undirected graph $G$ on $[m]$, we define its Sullivant-Talaska ideal $\mathrm{ST}_{G}$ to be the ideal in $\mathbb{R}[\Sigma]$ that is generated by the following collection of minors of $\Sigma$. For any submatrix $\Sigma_{A, B}$ we include in $\mathrm{ST}_{G}$ all $c \times c$-minors of $\Sigma_{A, B}$ provided $c$ is the smallest cardinality of a set $C$ of vertices that separates $A$ from $B$ in $G$. Here, $A, B$ and $C$ need not be disjoint, and separation means that any path from a node in $A$ to a node in $B$ must pass through a node in $C$. Sullivant and Talaska (2008) showed that the generators of $\mathrm{ST}_{G}$ are precisely those subdeterminants of $\Sigma$ that lie in $P_{G}$, and both ideals cut out the same variety in the positive definite cone $\mathbb{S}_{>0}^{m}$. However, generally their varieties differ on the boundary of that cone, even for chordal graphs $G$, as seen in Example 4.5. In our experiments, we found that $\mathrm{ST}_{G}$ can often be computed quite fast, and it frequently coincides with the desired prime ideal $P_{G}$.

# 4.2 The chordless $m$-cycle 

We next discuss Questions 1, 2, and 3 for the simplest non-chordal graph, namely, the $m$-cycle $C_{m}$. Its Sullivant-Talaska ideal $\mathrm{ST}_{C_{m}}$ is generated by the $3 \times 3$-minors of the submatrices $\Sigma_{A, B}$ where $A=$ $\{i, i+1, \ldots, j-1, j\}, B=\{j, j+1, \ldots, i-1, i\}$, and $|i-j| \geq 2$. Here $\{A, B\}$ runs over all diagonals in the $m$-gon, and indices are understood modulo $m$. We conjecture that

$$
P_{C_{m}}=\mathrm{ST}_{C_{m}}
$$

We computed the ideal $P_{C_{m}}$ in Singular $^{3}$ for small $m$. The following table lists the results:


In all cases in this table, the minimal generators consist of cubics only, which is consistent with the conjecture (23). For the degree of the Gaussian $m$-cycle we conjecture the following formula.

Conjecture 4.6. The degree of the projective variety $V\left(P_{C_{m}}\right)$ associated with the $m$-cycle equals

$$
\frac{m+2}{4}\binom{2 m}{m}-3 \cdot 2^{2 m-3}
$$

[^0]
[^0]:    ${ }^{3}$ www.singular.uni-kl.de/

Regarding Question 2, the following formula was conjectured in (Drton et al. 2009, §7.4):

$$
\operatorname{ML} \text {-degree }\left(C_{m}\right)=(m-3) \cdot 2^{m-2}+1, \quad \text { for } m \geq 3
$$

This quantity is an algebraic complexity measure for the following matrix completion problem. Given real numbers $x_{i}$ between -1 and +1 , fill up the partially specified symmetric $m \times m$-matrix

$$
\left(\begin{array}{ccccccc}
1 & x_{1} & ? & ? & \cdots & ? & x_{m} \\
x_{1} & 1 & x_{2} & ? & \cdots & ? & ? \\
? & x_{2} & 1 & x_{3} & ? & \ddots & ? \\
? & ? & x_{3} & 1 & x_{4} & \ddots & \vdots \\
\vdots & \vdots & & \ddots & \ddots & \ddots & ? \\
? & ? & ? & ? & x_{m-2} & 1 & x_{m-1} \\
x_{m} & ? & ? & ? & ? & x_{m-1} & 1
\end{array}\right)
$$

to make it positive definite. We seek the unique fill-up that maximizes the determinant. The solution to this convex optimization problem is an algebraic function of $x_{1}, x_{2}, \ldots, x_{m}$ whose degree equals ML-degree $\left(C_{m}\right)$. We do not know how to prove (24) for $m \geq 9$. Even the following lemma is not easy.

Lemma 4.7. The ML-degree of the cycle $C_{m}$ is strictly larger than 1 for $m \geq 4$.
Sketch of Proof. We consider the special case of (25) when all of the parameters are equal:

$$
x:=x_{1}=x_{2}=\cdots=x_{m}
$$

Since the logarithm of the determinant is a concave function, the solution to our optimization problem is fixed under the symmetric group of the $m$-gon, i.e., it is a symmetric circulant matrix $\Sigma_{m}$. Hence there are only $\left\lfloor\frac{m-2}{2}\right\rfloor$ distinct values for the question marks in (25), one for each of the symmetry class of long diagonals in the $m$-gon. We denote these unknowns by $s_{1}, s_{2}, \ldots, s_{\left\lfloor\frac{m-2}{2}\right\rfloor}$ where $s_{i}$ is the unknown on the $i$-th circular off-diagonal. For instance, for $m=7$, the circulant matrix we seek has two unknown entries $s_{1}$ and $s_{2}$, and it looks like this:

$$
\Sigma_{7}=\left(\begin{array}{ccccccc}
1 & x & s_{1} & s_{2} & s_{2} & s_{1} & x \\
x & 1 & x & s_{1} & s_{2} & s_{2} & s_{1} \\
s_{1} & x & 1 & x & s_{1} & s_{2} & s_{2} \\
s_{2} & s_{1} & x & 1 & x & s_{1} & s_{2} \\
s_{2} & s_{2} & s_{1} & x & 1 & x & s_{1} \\
s_{1} & s_{2} & s_{2} & s_{1} & x & 1 & x \\
x & s_{1} & s_{2} & s_{2} & s_{1} & x & 1
\end{array}\right)
$$

The key observation is that the determinant of the circular symmetric matrix $\Sigma_{m}$ factors into a product of $m$ linear factors with real coefficients, one for each $m$ th root of unity. For example,

$$
\operatorname{det}\left(\Sigma_{7}\right)=\prod_{w: w^{7}=1}\left(1+\left(w+w^{6}\right) \cdot x+\left(w^{2}+w^{5}\right) \cdot s_{1}+\left(w^{3}+w^{4}\right) \cdot s_{2}\right)
$$

Thus, for fixed $x$, our problem is to maximize a product of linear forms. By analyzing the critical equations, obtained by taking logarithmic derivatives of $\operatorname{det}\left(\Sigma_{m}\right)$, we can show that the optimal solution $\left(\hat{s}_{1}, \hat{s}_{2}, \ldots, \hat{s}_{\left\lfloor\frac{m-2}{2}\right\rfloor}\right)$ is not a rational function in $x$. For example, when $m=7$, the solution $\left(\hat{s}_{1}, \hat{s}_{2}\right)$ is an algebraic function of degree 3 in $x$. Its explicit representation is

$$
\hat{s}_{1}=\frac{x^{2}+\hat{s}_{2} x-\hat{s}_{2}^{2}-\hat{s}_{2}}{1-x} \quad \text { and } \quad \hat{s}_{2}^{3}+(1-2 x) \hat{s}_{2}^{2}+\left(-x^{2}+x-1\right) \hat{s}_{2}+x^{3}=0
$$

A detailed proof, for arbitrary $m$, will appear in the PhD dissertation of the second author.

We now come to our third problem, namely to giving an algebraic description of the cone of sufficient statistics, denoted $\mathcal{C}_{m}:=\mathcal{C}_{C_{m}}$. This is a full-dimensional open convex cone in $\mathbb{R}^{2 m}$. The coordinates on $\mathbb{R}^{2 m}$ are $s_{11}, s_{22}, \ldots, s_{m m}$ and $x_{1}=s_{12}, x_{2}=s_{23}, \ldots, x_{m}=s_{m 1}$. We consider

$$
\mathcal{C}_{m}^{\prime}:=\mathcal{C}_{m} \cap\left\{s_{11}=s_{22}=\cdots=s_{m m}=1\right\}
$$

This is a full-dimensional open bounded spectrahedron in $\mathbb{R}^{m}$. It consists of all $\left(x_{1}, \ldots, x_{m}\right)$ such that (25) can be filled up to a positive definite matrix. The $2 \times 2$-minors of (25) imply that $\mathcal{C}_{m}^{\prime}$ lies in the cube $(-1,1)^{m}=\left\{\left|x_{i}\right|<1\right\}$. The issue is to identify further constraints. We note that any description of the $m$-dimensional spectrahedron $\mathcal{C}_{m}^{\prime}$ leads to a description of the $2 m$-dimensional cone $\mathcal{C}_{m}$ because a vector $s \in \mathbb{R}^{2 m}$ lies in $\mathcal{C}_{m}$ if and only if the vector $x \in \mathbb{R}^{m}$ with the following coordinates lies in $\mathcal{C}_{m}^{\prime}$ :

$$
x_{i}=\frac{s_{i j}}{\sqrt{s_{i i} s_{j j}}} \quad \text { for } i=1,2, \ldots, m
$$

Barrett et al. (1993) gave a beautiful polyhedral description of the spectrahedron $\mathcal{C}_{m}^{\prime}$. The idea is to replace each $x_{i}$ by its arc-cosine, that is, to substitute $x_{i}=\cos \left(\phi_{i}\right)$ into (25). Remarkably, the image of the spectrahedron $\mathcal{C}_{m}^{\prime}$ under this transformation is a convex polytope. Explicit linear inequalities in the angle coordinates $\phi_{i}$ describing the facets of this polytope are given in Barrett et al. (1993).

To answer Question 3, we take the cosine-image of any of these facets and compute its Zariski closure. This leads to the following trigonometry problem. Determine the unique (up to scaling) irreducible polynomial $\Gamma_{m}^{\prime}$ which is obtained by rationalizing the equation

$$
x_{1}=\cos \left(\sum_{i=2}^{m} \arccos \left(x_{i}\right)\right)
$$

We call $\Gamma_{m}^{\prime}$ the $m$-th cycle polynomial. Interestingly, $\Gamma_{m}^{\prime}$ is invariant under all permutations of the $m$ variables $x_{1}, x_{2}, \ldots, x_{m}$. We also define the homogeneous $m$-th cycle polynomial $\Gamma_{m}$ to be the numerator of the image of $\Gamma_{m}^{\prime}$ under the substitution (27). The first cycle polynomials arise for $m=3$ :

$$
\Gamma_{3}^{\prime}=\operatorname{det}\left(\begin{array}{ccc}
1 & x_{1} & x_{3} \\
x_{1} & 1 & x_{2} \\
x_{3} & x_{2} & 1
\end{array}\right) \quad \text { and } \quad \Gamma_{3}=\operatorname{det}\left(\begin{array}{lll}
s_{11} & s_{12} & s_{13} \\
s_{12} & s_{22} & s_{23} \\
s_{13} & s_{23} & s_{33}
\end{array}\right)
$$

The polyhedral characterization of $\mathcal{C}_{m}$ given in Barrett et al. (1993) translates into the following theorem.
Theorem 4.8. The Zariski closure of the boundary of the cone $\mathcal{C}_{m}, m \geq 4$, is defined by the polynomial

$$
H_{C_{m}}\left(s_{i j}\right)=\Gamma_{m}\left(s_{i j}\right) \cdot\left(s_{11} s_{22}-s_{12}^{2}\right) \cdot\left(s_{22} s_{33}-s_{23}^{2}\right) \cdots\left(s_{m m} s_{11}-s_{1 m}^{2}\right)
$$

To compute the cycle polynomial $\Gamma_{m}^{\prime}$, we iteratively apply the sum formula for the cosine,

$$
\cos (a+b)=\cos (a) \cdot \cos (b)-\sin (a) \cdot \sin (b)
$$

and we then use the following relation to write (28) as an algebraic expression in $x_{1}, \ldots, x_{n}$ :

$$
\sin \left(\arccos \left(x_{i}\right)\right)=\sqrt{1-x_{i}^{2}}
$$

Finally, we eliminate the square roots (e.g. by using resultants) to get the polynomial $\Gamma_{m}^{\prime}$.
For example, the cycle polynomial for the square $(m=4)$ has degree 6 and has 19 terms:

$$
\Gamma_{4}^{\prime}=4 \sum_{i<j<k} x_{i}^{2} x_{j}^{2} x_{k}^{2}-4 x_{1} x_{2} x_{3} x_{4} \sum_{i} x_{i}^{2}+\sum_{i} x_{i}^{4}-2 \sum_{i<j} x_{i}^{2} x_{j}^{2}+8 x_{1} x_{2} x_{3} x_{4}
$$

By substituting (27) into this expression and taking the numerator, we obtain the homogeneous cycle polynomial $\Gamma_{4}$ which has degree 8 . Here is a table summarizing what we know about the expansions of these cycle polynomials. Note that $\Gamma_{m}^{\prime}$ and $\Gamma_{m}$ have different degrees but the same number of terms.


Table 1 Our three guiding questions for all non-chordal graphs with $m \leq 5$ vertices. Column 4 reports the degrees of the minimal generators together with the number of occurrence (degree:number). The last column lists the degrees of the irreducible factors of the polynomial $H_{G}$ that defines the Zariski closure of the boundary of $\mathcal{C}_{G}$. For each factor we report in lowercase the rank of the concentration matrices defining its dual irreducible component in the boundary of $\mathcal{K}_{G}$.


The degree of the $m$-th cycle polynomial $\Gamma_{m}^{\prime}$ grows roughly like $2^{m}$, but we do not know an exact formula. However, for the homogeneous cycle polynomial $\Gamma_{m}$ we predict the following behavior.

Conjecture 4.9. The degree of the homogeneous $m$-th cycle polynomial $\Gamma_{m}$ equals $m \cdot 2^{m-3}$.
There is another way of defining and computing the cycle polynomial $\Gamma_{m}$, without any reference to trigonometry or semidefinite programming. Consider the prime ideal generated by the $3 \times 3$-minors of the generic symmetric $m \times m$-matrix $\Sigma=\left(s_{i j}\right)$. Then $\left\langle\Gamma_{m}\right\rangle$ is the principal ideal obtained by eliminating all unknowns $s_{i j}$ with $|i-j| \geq 2$. Thus, geometrically, vanishing of the homogeneous polynomial $\Gamma_{m}$ characterizes partial matrices on the $m$-cycle $C_{m}$ that can be completed to a matrix of rank $\leq 2$. Similarly, vanishing of $\Gamma_{m}^{\prime}$ characterizes partial matrices (25) that can be completed to rank $\leq 2$.

Independently of the work of Barrett et al. (1993), a solution to the problem of characterizing the cone $\mathcal{C}_{m}$ appeared in the same year in the statistics literature, namely by Buhl (1993). For statisticians, the cone $\mathcal{C}_{m}$ is the set of partial sample covariance matrices on the $m$-cycle for which the MLE exists.

# 4.3 Small graphs, suspensions and wheels 

We next examine Questions 1, 2 and 3 for all graphs with at most five vertices. In this analysis we can restrict ourselves to connected graphs only. Indeed, if $G$ is the disjoint union of two graphs $G_{1}$ and $G_{2}$ then the prime ideal $P_{G}$ is obtained from $P_{G_{1}}$ and $P_{G_{2}}$ as in (22) with $c=0$, the ML-degrees multiply by Lemma 4.2, and the two dual cones both decompose as direct products:

$$
\mathcal{C}_{G}=\mathcal{C}_{G_{1}} \times \mathcal{C}_{G_{2}} \quad \text { and } \quad \mathcal{K}_{G}=\mathcal{K}_{G_{1}} \times \mathcal{K}_{G_{2}}
$$

Chordal graphs were dealt with in Section 4.1. We now consider connected non-chordal graphs with $m \leq 5$ vertices. There are seven such graphs, and in Table 1 we summarize our findings for these seven graphs. In the first two rows of Table 1 we find the 4 -cycle and the 5 -cycle which were discussed in Subsection 4.2. As an illustration we examine in detail the graph in the second-to-last row of Table 1.

![img-1.jpeg](img-1.jpeg)

Fig. 2 A Gaussian graphical model on five vertices and seven edges having dimension $d=12$.

Example 4.10. The graph in Fig. 2 defines the Gaussian graphical model with concentration matrix

$$
K=\left(\begin{array}{ccccc}
\lambda_{1} & \lambda_{6} & 0 & \lambda_{9} & \lambda_{10} \\
\lambda_{6} & \lambda_{2} & \lambda_{7} & 0 & \lambda_{11} \\
0 & \lambda_{7} & \lambda_{3} & \lambda_{8} & \lambda_{12} \\
\lambda_{9} & 0 & \lambda_{8} & \lambda_{4} & 0 \\
\lambda_{10} & \lambda_{11} & \lambda_{12} & 0 & \lambda_{5}
\end{array}\right)
$$

We wish to describe the boundary of the cone $\mathcal{C}_{G}$ by identifying the irreducible factors in its defining polynomial $H_{G}$. We first use the Matlab software CVX ${ }^{4}$, which is specialized in convex optimization, to find the ranks of all concentration matrices $K$ that are extreme rays in the boundary of $\mathcal{K}_{G}$. Using CVX, we maximize random linear functions over the compact spectrahedron $\overline{\mathcal{K}_{G}} \cap\{\operatorname{trace}(K)=1\}$, and we record the ranks of the optimal matrices. We found the possible matrix ranks to be 1 and 2, which agrees with the constraints $2 \leq p \leq 3$ seen in (14) for generic subspaces $\mathcal{L}$ with $m=5$ and $d=12$.

We next ran the software Singular to compute the minimal primes of the ideals of $p \times p$-minors of $K$ for $p=2$ and $p=3$, and thereafter we computed their dual ideals in $\mathbb{R}\left[t_{1}, t_{2}, \ldots, t_{12}\right]$ using Macaulay2. The latter step was done using the procedure with Jacobian matrices described in Subsection 2.2. We only retained dual ideals that are principal. Their generators are the candidates for factors of $H_{G}$.

The variety of rank one matrices $K$ has four irreducible components. Two of those components correspond to the edges $(3,4)$ and $(1,4)$ in Fig. 2. Their dual ideals are generated by the quadrics

$$
p_{1}=4 t_{3} t_{4}-t_{8}^{2} \quad \text { and } \quad p_{2}=4 t_{1} t_{4}-t_{9}^{2}
$$

The other two irreducible components of the variety of rank one concentration matrices correspond to the 3 -cycles $(1,2,5)$ and $(2,3,5)$ in the graph. Their dual ideals are generated by the cubics

$$
p_{3}=4 t_{1} t_{2} t_{5}-t_{5} t_{6}^{2}-t_{2} t_{10}^{2}+t_{6} t_{10} t_{11}-t_{1} t_{11}^{2} \quad \text { and } \quad p_{4}=4 t_{2} t_{3} t_{5}-t_{5} t_{7}^{2}-t_{3} t_{11}^{2}+t_{7} t_{11} t_{12}-t_{2} t_{12}^{2}
$$

The variety of rank two matrices $K$ has two irreducible components. One corresponds to the chordless 4 -cycle $(1,2,3,4)$ in the graph and its dual ideal is generated by $p_{5}=\Gamma_{4}$, which is of degree 8 . The other component consists of rank two matrices $K$ for which rows 2 and 5 are linearly dependent. The polynomial $p_{6}$ that defines the dual ideal consists of 175 terms and has degree 10 .

The polynomial $H_{G}$ is the product of those principal generators $p_{i}$ whose hypersurface meets $\partial \mathcal{C}_{G}$. We again used CVX to check which of the six components actually contribute extreme rays in $\partial \mathcal{K}_{G}$. We found that only one of the six components to be missing, namely that corresponding to the chordless 4 -cycle $(1,2,3,4)$. This means that $p_{5}$ is not a factor of $H_{G}$, and we conclude

$$
H_{G}=p_{1} p_{2} p_{3} p_{4} p_{6} \quad \text { and } \quad \operatorname{deg}\left(H_{G}\right)=2 \cdot 2_{1}+2 \cdot 3_{1}+10_{2}
$$

Concerning Question 1 we note that the ideal $P_{G}$ is minimally generated by the four $3 \times 3$-minors of $\Sigma_{1235,134}$ the determinant of $\Sigma_{1245,2345}$, and for Question 2 we note that the ML degree is five because the MLE can be derived from the MLE of the 4-cycle obtained by contracting the edge $(2,5)$.

The graph in the last row of Table 1 is the wheel $W_{4}$. It is obtained from the cycle $C_{4}$ in the first row by connecting all four vertices to a new fifth vertex. We see in Table 1 that the ML degree 5 is the same for both graphs, the two cubic generators of $P_{C_{4}}$ correspond to the two quartic generators of $P_{W_{4}}$, and there is a similar correspondence between the irreducible factors of the dual polynomials $H_{C_{4}}$ and $H_{W_{4}}$. In the remainder of this section we shall offer an explanation for these observations.

[^0]
[^0]:    ${ }^{4}$ www.stanford.edu/ boyd/cvx/

Let $G=(V, E)$ be an undirected graph and $G^{*}=\left(V^{*}, E^{*}\right)$ its suspension graph with an additional completely connected vertex 0 . The graph $G^{*}$ has vertex set $V^{*}=V \cup\{0\}$ and edge set $E^{*}=E \cup\{(0, v) \mid$ $v \in V\}$. The $m$-wheel $W_{m}$ is the suspension graph of the $m$-cycle $C_{m}$; in symbols, $W_{m}=\left(C_{m}\right)^{*}$. We shall compare the Gaussian graphical models for the graph $G$ and its suspension graph $G^{*}$.

Theorem 4.11. The ML degree of a Gaussian graphical model with underlying graph $G$ equals the ML degree of a Gaussian graphical model whose underlying graph is the suspension graph $G^{*}$.

Proof. Let $V=[m]$ and let $S^{*} \in \mathbb{S}_{>0}^{m+1}$ be a sample covariance matrix on $G^{*}$, where the first row and column correspond to the additional vertex 0 . We denote by $S^{\prime}$ the lower right $m \times m$ submatrix of $S^{*}$ corresponding to the vertex set $V$ and by $S$ the Schur complement of $S^{*}$ at $S_{00}^{*}$ :

$$
S:=S^{\prime}-\frac{1}{S_{00}^{*}}\left(S_{01}^{*}, \ldots, S_{0 m}^{*}\right)^{T}\left(S_{01}^{*}, \ldots, S_{0 m}^{*}\right)
$$

Then $S \in \mathbb{S}_{>0}^{m}$ is a sample covariance matrix on $G$. Let $\hat{\Sigma}$ be the MLE for $S$ on the graph $G$. We claim that the MLE $\hat{\Sigma}^{*}$ for $S^{*}$ on the suspension graph $G^{*}$ is given by

$$
\hat{\Sigma}^{*}=\left[\begin{array}{c|cc}
S_{00}^{*} & S_{01}^{*} & \cdots & S_{0 m}^{*} \\
\hline S_{01}^{*} & & & \\
\vdots & & \hat{\Sigma}+S^{\prime}-S
\end{array}\right]
$$

Clearly, $\hat{\Sigma}^{*}$ is positive definite and satisfies $\hat{\Sigma}_{i j}^{*}=S_{i j}^{*}$ for all $(i, j) \in E^{*}$. The inverse of the covariance matrix $\hat{\Sigma}^{*}$ can be computed by using the inversion formula based on Schur complements:

$$
\left(\hat{\Sigma}^{*}\right)^{-1}=\left[\begin{array}{c|c}
\frac{1}{S_{0 m}^{*}}+\left(S_{01}^{*}, \ldots, S_{0 m}^{*}\right)(\hat{\Sigma})^{-1}\left(S_{01}^{*}, \ldots, S_{0 m}^{*}\right)^{T} & \frac{1}{S_{0 m}^{*}}\left(\hat{\Sigma}\right)^{-1}\left(S_{01}^{*}, \ldots, S_{0 m}^{*}\right)^{T} \\
\hline \frac{1}{S_{0 m}^{*}}\left(S_{01}^{*}, \ldots, S_{0 m}^{*}\right)(\hat{\Sigma})^{-1} & (\hat{\Sigma})^{-1}
\end{array}\right]
$$

Since the lower right block equals $(\hat{\Sigma})^{-1}$, its entries are indeed zero in all positions $(i, j) \notin E^{*}$.
We have shown that the MLE $\hat{\Sigma}^{*}$ is a rational function of the MLE $\hat{\Sigma}$. This shows

$$
\text { ML-degree }\left(G^{*}\right) \leq \text { ML-degree }(G)
$$

The reverse inequality is also true since we can compute the MLE on $G$ for any $S \in S_{>0}^{m}$ by computing the MLE on $G^{*}$ for its extension $S^{*} \in \mathbb{S}_{>0}^{m+1}$ with $S_{00}^{*}=1$ and $S_{0 j}^{*}=0$ for $j \in[m]$.

We next address the question of how the boundary of the cone $\mathcal{C}_{G^{*}}$ can be expressed in terms of the boundary of $\mathcal{C}_{G}$. We use coordinates $t_{i j}$ for both $\mathbb{S}^{m}$ and its subspace $\mathbb{R}^{E}$, and we use the coordinates $u_{i j}$ for both $\mathbb{S}^{m+1}$ and its subspace $\mathbb{R}^{E^{*}}$. The Schur complement (30) defines a rational map from $\mathbb{S}^{m+1}$ to $\mathbb{S}^{m}$ which restricts to a rational map from $\mathbb{R}^{E^{*}}$ to $\mathbb{R}^{E}$. The formula is

$$
t_{i j}=u_{i j}-\frac{u_{0 i} u_{0 j}}{u_{00}} \quad \text { for } 1 \leq i \leq j \leq m
$$

A partial matrix $\left(u_{i j}\right)$ on $G^{*}$ can be completed to a positive definite $(m+1) \times(m+1)$-matrix if and only if the partial matrix $\left(t_{i j}\right)$ on $G$ given by this formula can be completed to a positive definite $m \times m$-matrix. The rational map (31) takes the boundary of the cone $\mathcal{C}_{G^{*}}$ onto the boundary of the cone $\mathcal{C}_{G}$. For our algebraic question, we can derive the following conclusion:
Proposition 4.12. The polynomial $H_{G^{*}}\left(u_{i j}\right)$ equals the numerator of the Laurent polynomial obtained from $H_{G}\left(t_{i j}\right)$ by the substitution (31), and the same holds for each irreducible factor.

Example 4.13. The polynomial $H_{W_{4}}\left(u_{00}, u_{01}, u_{02}, u_{03}, u_{04}, u_{11}, u_{22}, u_{33}, u_{44}, u_{12}, u_{23}, u_{34}, u_{14}\right)$ for the 4 -wheel $W_{4}$ has as its main factor an irreducible polynomial of degree 12 which is the sum of 813 terms. It is obtained from the homogeneous cycle polynomial $\Gamma_{4}$ by the substitution (31). Recall that $\Gamma_{4}\left(t_{11}, t_{22}, t_{33}, t_{44}, t_{12}, t_{23}, t_{34}, t_{14}\right)$ has only degree 8 and is the sum of 19 terms.

We briefly discuss an issue raised by Question 1, namely, how to construct the prime ideal $P_{G^{*}}$ from the prime ideal $P_{G}$. Again, we can use the transformation (31) to turn every generator of $P_{G}$ into a Laurent polynomial whose numerator lies in $P_{G^{*}}$. However, the resulting polynomials will usually not suffice to generate $P_{G^{*}}$. This happens already for the 5 -cycle $G=C_{5}$ and the 5 -wheel $G^{*}=W_{5}$. The ideal $P_{C_{5}}$ is generated by 15 linearly independent cubics arising as $3 \times 3$-minors of the matrices $\Sigma_{132,1345}, \Sigma_{243,2451}, \Sigma_{354,3512}, \Sigma_{415,4123}$ and $\Sigma_{521,5234}$, while $P_{W_{5}}$ is generated by 20 linearly independent quartics arising as $4 \times 4$-minors of $\Sigma_{0132,01345}, \Sigma_{0243,02451}, \Sigma_{0354,03512}, \Sigma_{0415,04123}$ and $\Sigma_{0521,05234}$. Here is a table that summarizes what we know about the Gaussian wheels $W_{m}$ :


# 5 Colored Gaussian graphical models 

We now add a graph coloring to the setup and study colored Gaussian graphical models. These were introduced by Højsgaard and Lauritzen (2008) who called them $R C O N$-models. In the underlying graph $G$, the vertices are colored with $p$ different colors and the edges are colored with $q$ different colors:

$$
\begin{array}{ll}
V=V_{1} \sqcup V_{2} \sqcup \cdots \sqcup V_{p}, & p \leq|V| \\
E=E_{1} \sqcup E_{2} \sqcup \cdots \sqcup E_{q}, & q \leq|E|
\end{array}
$$

We denote the uncolored graph by $G$ and the colored graph by $\mathcal{G}$. In addition to the restrictions given by the missing edges in the graph, the entries of the concentration matrix $K$ are now also restricted by equating entries in $K$ according to the edge and vertex colorings. To be precise, the linear space $\mathcal{L}$ of $\mathbb{S}^{m}$ associated with a colored graph $\mathcal{G}$ on $m=|V|$ nodes is defined by the following linear equations:

- For any pair of nodes $\alpha, \beta$ that do not form an edge we set $k_{\alpha \beta}=0$ as before.
- For any pair of nodes $\alpha, \beta$ in a common color class $V_{i}$ we set $k_{\alpha \alpha}=k_{\beta \beta}$.
- For any pair of edges $(\alpha, \beta),(\gamma, \delta)$ in a common color class $E_{j}$ we set $k_{\alpha \beta}=k_{\gamma \delta}$.

The dimension of the model $\mathcal{G}$ is $d=p+q$. We note that, for any sample covariance matrix $S$,

$$
\pi_{G}(S) \in \mathcal{C}_{G} \quad \text { implies } \quad \pi_{\mathcal{G}}(S) \in \mathcal{C}_{\mathcal{G}}
$$

Thus, introducing a graph coloring on $G$ relaxes the question of existence of the MLE.
In this section we shall examine Questions 1-3 for various colorings $\mathcal{G}$ of the 4 -cycle $G=C_{4}$. We begin with an illustration of how colored Gaussian graphical models can be used in statistical applications.
![img-2.jpeg](img-2.jpeg)

Fig. 3 Colored Gaussian graphical model for Frets' heads: $L_{i}, B_{i}$ denote the length and breadth of the head of son $i$.

Example 5.1 (Frets' heads). We revisite the heredity study of head dimensions reported in Mardia et al. (1979) and known to statisticians as Frets' heads. The data reported in this study consists of the length and breadth of the heads of 25 pairs of first and second sons. Because of the symmetry between the two sons, it makes sense to try to fit the colored Gaussian graphical model given in Fig. 3.

This model has $d=5$ degrees of freedom and it consists of all concentration matrices of the form

$$
K=\left(\begin{array}{cccc}
\lambda_{1} & \lambda_{3} & 0 & \lambda_{4} \\
\lambda_{3} & \lambda_{1} & \lambda_{4} & 0 \\
0 & \lambda_{4} & \lambda_{2} & \lambda_{5} \\
\lambda_{4} & 0 & \lambda_{5} & \lambda_{2}
\end{array}\right)
$$

In Fig. 3, the first random variable is denoted $L_{1}$, the second $L_{2}$, the third $B_{2}$, and the fourth $B_{1}$. Given a sample covariance matrix $S=\left(s_{i j}\right)$, the five sufficient statistics for this model are

$$
t_{1}=s_{11}+s_{22}, \quad t_{2}=s_{33}+s_{44}, \quad t_{3}=2 s_{12}, \quad t_{4}=2\left(s_{23}+s_{14}\right), \quad t_{5}=2 s_{34}
$$

The ideal of polynomials vanishing on $K^{-1}$ is generated by four linear forms and one cubic in the $s_{i j}$ :

$$
\begin{aligned}
P_{\mathcal{G}}=\langle & s_{11}-s_{22}, s_{33}-s_{44}, s_{23}-s_{14}, s_{13}-s_{24} \\
& s_{23}^{2} s_{24}-s_{24}^{3}-s_{22} s_{23} s_{34}+s_{12} s_{24} s_{34}-s_{12} s_{23} s_{44}+s_{22} s_{24} s_{44}\rangle
\end{aligned}
$$

Note that the four linear constraints on the sample covariance matrix seen in $P_{\mathcal{G}}$ are also valid constraints on the concentration matrix. Models with this property were studied in general by Jensen (1988) and appear under the name RCOP-models in Højsgaard and Lauritzen (2008).

The data reported in the Frets' heads study results in the following sufficient statistics:

$$
t_{1}=188.256, \quad t_{2}=95.408, \quad t_{3}=133.750, \quad t_{4}=210.062, \quad t_{5}=67.302
$$

Substituting these values into (32) and solving the equations on $V\left(P_{\mathcal{G}}\right)$, we find the MLE for this data:

$$
\hat{\Sigma}=\left(\begin{array}{cccc}
94.1280 & 66.8750 & 44.3082 & 52.5155 \\
66.8750 & 94.1280 & 52.5155 & 44.3082 \\
44.3082 & 52.5155 & 47.7040 & 33.6510 \\
52.5155 & 44.3082 & 33.6510 & 47.7040
\end{array}\right)
$$

Both the degree and the ML-degree of this colored Gaussian graphical model is 3, which answers Questions 1 and 2. It remains to describe the boundary of the cone $\mathcal{C}_{\mathcal{G}}$ and to determine its defining polynomial $H_{\mathcal{G}}$. The variety of rank one concentration matrices has four irreducible components:

$$
\left\langle k_{2}, k_{4}, k_{5}, k_{1}+k_{3}\right\rangle,\left\langle k_{2}, k_{4}, k_{5}, k_{1}-k_{3}\right\rangle,\left\langle k_{1}, k_{3}, k_{4}, k_{2}+k_{5}\right\rangle,\left\langle k_{1}, k_{3}, k_{4}, k_{2}-k_{5}\right\rangle
$$

These are points in $\mathbb{P}^{4}$ and the ideals of their dual hyperplanes are $\left\langle t_{1}-t_{3}\right\rangle,\left\langle t_{1}+t_{3}\right\rangle,\left\langle t_{2}-t_{5}\right\rangle,\left\langle t_{2}+t_{5}\right\rangle$. The variety of rank two concentration matrices is irreducible. Its prime ideal and the dual thereof are

$$
\begin{gathered}
\left\langle k_{2} k_{3}+k_{1} k_{5}, \quad k_{1} k_{2}-k_{4}^{2}+k_{3} k_{5}, \quad k_{3} k_{4}^{2}+k_{1}^{2} k_{5}-k_{3}^{2} k_{5}\right\rangle \\
\left\langle 4 t_{2}^{2} t_{3}^{2}-4 t_{1} t_{2} t_{4}^{2}+t_{4}^{4}+8 t_{1} t_{2} t_{3} t_{5}-4 t_{3} t_{4}^{2} t_{5}+4 t_{1}^{2} t_{5}^{2}\right\rangle
\end{gathered}
$$

This suggests that the hypersurface $\partial \mathcal{C}_{\mathcal{G}}$ is given by the polynomial

$$
H_{\mathcal{G}}=\left(t_{1}-t_{3}\right)\left(t_{1}+t_{3}\right)\left(t_{2}-t_{5}\right)\left(t_{2}+t_{5}\right)\left(4 t_{2}^{2} t_{3}^{2}-4 t_{1} t_{2} t_{4}^{2}+t_{4}^{4}+8 t_{1} t_{2} t_{3} t_{5}-4 t_{3} t_{4}^{2} t_{5}+4 t_{1}^{2} t_{5}^{2}\right)
$$

Using CVX as in Example 4.10 we checked that all five factors meet $\partial \mathcal{C}_{\mathcal{G}}$, so (33) is indeed correct.
We performed a similar analysis for all colored Gaussian graphical models on the 4 -cycle $C_{4}$, which have the property that edges in the same color class connect the same vertex color classes. The results are presented in Table 2, 3 and 4. These models are of special interest because they are invariant under rescaling of variables in the same vertex color class. Such models were introduced and studied by Højsgaard and Lauritzen (2008). For models with an additional permutation property (these are the RCOP-models), we explicitly list the polynomial $H_{\mathcal{G}}$. A census of these models appears in Table 4.

Table 2 Results on Questions 1, 2, and 3 for all colored Gaussian graphical models with some symmetry restrictions (namely, edges in the same color class connect the same vertex color classes) on the 4 -cycle.


Table 3 Continuation of Table 2.
![img-3.jpeg](img-3.jpeg)

Table 4 All RCOP-models (Højsgaard and Lauritzen 2008) when the underlying graph is the 4-cycle.


Example 5.2. We can gain a different perspective on the proof of Lemma 4.7 by considering colored Gaussian graphical models. Under the assumption (26) that all parameters in the partial matrix (25) are equal to some fixed value $x$, the MLE $\hat{K}$ for the concentration matrix has the same structure. Namely, all diagonal entries of $\hat{K}$ are equal, and all non-zero off-diagonal entries of $\hat{K}$ are equal. This means that we can perform our MLE computation for the colored Gaussian graphical model with the chordless $m$-cycle

as underlying graph, where all vertices and all edges have the same color:

$$
K=\left(\begin{array}{cccccc}
\lambda_{1} & \lambda_{2} & 0 & 0 & \cdots & \lambda_{2} \\
\lambda_{2} & \lambda_{1} & \lambda_{2} & 0 & \cdots & 0 \\
0 & \lambda_{2} & \lambda_{1} & \lambda_{2} & \cdots & 0 \\
\vdots & \vdots & \ddots & \ddots & \ddots & 0 \\
0 & 0 & 0 & \lambda_{2} & \lambda_{1} & \lambda_{2} \\
\lambda_{2} & 0 & 0 & 0 & \lambda_{2} & \lambda_{1}
\end{array}\right)
$$

In contrast to the approach in the proof of Lemma 4.7, in this representation we only need to solve a system of two polynomial equations in two unknowns, regardless of the cycle size $m$. The equations are

$$
\left(K^{-1}\right)_{11}=1 \quad \text { and } \quad\left(K^{-1}\right)_{12}=x
$$

By clearing denominators we obtain two polynomial equations in the unknowns $\lambda_{1}$ and $\lambda_{2}$. We need to express these in terms of the parameter $x$, but there are many extraneous solutions. The ML degree is algebraic degree of the special solution $\left(\hat{\lambda}_{1}(x), \hat{\lambda}_{2}(x)\right)$ which makes (34) positive definite.
![img-4.jpeg](img-4.jpeg)

Fig. 4 The cross section of the cone of sufficient statistics in Example 5.3 is the red convex body shown in the left figure. It is dual to Cayley's cubic surface, which is shown in yellow in the right figure and also in Fig. 1 on the left.

Example 5.3. Let $\mathcal{G}$ be the colored triangle with the same color for all three vertices and three distinct colors for the edges. This is an RCOP model with $m=3$ and $d=4$. The corresponding subspace $\mathcal{L}$ of $\mathbb{S}^{3}$ consists of all concentration matrices

$$
K=\left(\begin{array}{lll}
\lambda_{4} & \lambda_{1} & \lambda_{2} \\
\lambda_{1} & \lambda_{4} & \lambda_{3} \\
\lambda_{2} & \lambda_{3} & \lambda_{4}
\end{array}\right)
$$

This linear space $\mathcal{L}$ is generic enough so as to exhibit the geometric behavior described in Subsection 2.2. The four-dimensional cone $\mathcal{K}_{\mathcal{L}}$ is the cone over the 3-dimensional spectrahedron bounded by Cayley's cubic surface as shown on the right in Fig. 4. Its dual $\mathcal{C}_{\mathcal{L}}$ is the cone over the 3-dimensional convex body shown on the left in Fig. 4. The boundary of this convex body consists of four flat 2-dimensional circular faces (shown in black) and four curved surfaces whose common Zariski closure is a quartic Steiner surface. Fig. 4 was made with surfex $^{5}$, a software package for visualizing algebraic surfaces.

Here, the inequalities (14) state $2 \leq p \leq 3$, and the algebraic degree of SDP is $\delta(3,3,2)=\delta(3,3,1)=4$. We find that $H_{\mathcal{L}}$ is a polynomial of degree 8 which factors into four linear forms and one quartic:
$H_{\mathcal{L}}=\left(t_{1}-t_{2}+t_{3}-t_{4}\right)\left(t_{1}+t_{2}-t_{3}-t_{4}\right)\left(t_{1}-t_{2}-t_{3}+t_{4}\right)\left(t_{1}+t_{2}+t_{3}+t_{4}\right)\left(t_{1}^{2} t_{2}^{2}+t_{1}^{2} t_{3}^{2}+t_{2}^{2} t_{3}^{2}-2 t_{1} t_{2} t_{3} t_{4}\right)$
By Theorem 2.3, both the degree and the ML degree of this model are also equal to $\phi(3,4)=4$.

Acknowledgements We wish to thank Seth Sullivant, Bernd Ulrich and Ruriko Yoshida for helpful comments.
