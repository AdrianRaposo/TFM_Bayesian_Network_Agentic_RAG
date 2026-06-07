# Czechoslovak Mathematical Journal 

Miroslav Fiedler<br>Algebraic connectivity of graphs

Czechoslovak Mathematical Journal, Vol. 23 (1973), No. 2, 298-305

Persistent URL: http://dml.cz/dmlcz/101168

## Terms of use:

(c) Institute of Mathematics AS CR, 1973

Institute of Mathematics of the Czech Academy of Sciences provides access to digitized documents strictly for personal use. Each copy of any part of this document must contain these Terms of use.
![img-0.jpeg](img-0.jpeg)

This document has been digitized, optimized for electronic delivery and stamped with digital signature within the project DML-CZ: The Czech Digital Mathematics Library http://dml.cz

# ALGEBRAIC CONNECTIVITY OF GRAPHS*) 

Miroslav Fiedler, Praha<br>(Received April 14, 1972)

## 1. INTRODUCTION

Let $G=(V, E)$ be a non-directed finite graph without loops and multiple edges. Having chosen a fixed ordering $w_{1}, w_{2}, \ldots, w_{n}$ of the set $V$, we can form a square $n$-rowed matrix $A(G)$ whose off-diagonal entries are $a_{i k}=a_{k l}=-1$ if $\left(w_{i}, w_{k}\right) \in E$ and $a_{i k}=0$ otherwise and whose diagonal entries $a_{i l}$ are equal to the valencies of the vertices $w_{i}$. This matrix $A(G)$, which is frequently used to enumerate the spanning trees of the graph $G$, is symmetric, singular (all the row sums are zero) and positive semidefinite $\left(A(G)=U U^{T}\right.$ where $U$ is the $(0,1,-1)$ vertex-edge adjacency matrix of arbitrarily directed graph $G)$. Let $n \geqq 2$ and $0=\lambda_{1} \leqq \lambda_{2}=a(G) \leqq \lambda_{3} \leqq \ldots$ $\ldots \leqq \lambda_{n}$ be the eigenvalues of the matrix $A(G)$. From the Perron-Frobenius theorem applied to the matrix $(n-1) I-A(G)$ it follows that $a(G)$ is zero if and only if the graph $G$ is not connected. We shall call the second smallest eigenvalue $a(G)$ of the matrix $A(G)$ algebraic connectivity of the graph $G$. It is the purpose of this paper to find its relation to the usual vertex and edge connectivities.

We recall that many authors, e.g. A. J. Hoffman, M. Doob, D. K. Ray-Chaudhuri, J. J. Seidel have characterized graphs by means of the spectra of the $(0,1)$ and $(0,1,-1)$ adjacency matrices.

## 2. NOTATION AND CONVENTIONS

The notation introduced above is used throughout the present paper. All matrices and vectors are considered real. The transpose of a matrix $M$ is denoted by $M^{T}$, the identity matrix by $I$, the vector $(1,1, \ldots, 1)^{T}$ by $e$, the universal matrix $e e^{T}$ by $J$, the cardinality of a set $S$ by $|S|$.

For our purpose it is convenient to denote by $W$ the set of all column vectors $x$ such that $x^{T} x=1, x^{T} e=0$. Any square matrix $M$ with all zero row sums has an

[^0]
[^0]:    *) Presented at the Graph Theory Meeting in Zlatá Idka, May 1971.

eigenvalue 0 and a corresponding eigenvector is $e$. If $M$ is positive semidefinite then the second smallest eigenvalue is equal to $\min x^{T} M x$ by the well known Courant's theorem. We use that principle tacitly. $x \in W$

Further, let us mention two common concepts. Edge connectivity of the graph $G$, i.e. the minimal number of edges whose removal would result in losing connectivity of the graph $G$, is denoted by $e(G)$. Vertex connectivity which is defined analogously (vertices together with adjacent edges are removed) is denoted by $v(G)$. It is convenient to put $v(G)=n-1$ for the complete graph $G$.

Let $G_{1}=\left(V_{1}, E_{1}\right), G_{2}=\left(V_{2}, E_{2}\right)$. By $G_{1} \times G_{2}$ we denote the graph $\left(V_{1} \times V_{2}, E\right)$ such that $\left(\left(u_{1}, u_{2}\right),\left(v_{1}, v_{2}\right)\right) \in E$ if and only if either $u_{1}=v_{1}$ and $\left(u_{2}, v_{2}\right) \in E_{2}$ or $\left(u_{1}, v_{1}\right) \in E_{1}$ and $u_{2}=v_{2}$. Let $R=\left(r_{i j}\right), S$ be matrices. Then by $R \times S$ the partitioned matrix $\left(r_{i j} S\right)$ is denoted.

# 3. PROPERTIES OF $a(G)$ 

3.1. If $G_{1}, G_{2}$ are edge-disjoint graphs with the same set of vertices then $a\left(G_{1}\right)+$ $+a\left(G_{2}\right) \leqq a\left(G_{1} \cup G_{2}\right)$.

Proof. We have $A\left(G_{1} \cup G_{2}\right)=A\left(G_{1}\right)+A\left(G_{2}\right)$. Thus $a\left(G_{1} \cup G_{2}\right)=$ $=\min _{x \in W}\left(x^{T} A\left(G_{1}\right) x+x^{T} A\left(G_{2}\right) x\right) \geqq \min _{x \in W} x^{T} A\left(G_{1}\right) x+\min _{x \in W} x^{T} A\left(G_{2}\right) x=a\left(G_{1}\right)+$ $+a\left(G_{2}\right)$
3.2. Corollary. The function $a(G)$ is non-decreasing for graphs with the same set of vertices, i.e. $a\left(G_{1}\right) \leqq a\left(G_{2}\right)$ if $G_{1} \subseteq G_{2}$ (and $G_{1}, G_{2}$ have the same set of vertices).
3.3. Let $G$ be a graph, let $G_{1}$ arise from $G$ by removing $k$ vertices from $G$ and all adjacent edges. Then

$$
a\left(G_{1}\right) \geqq a(G)-k
$$

Proof. Let $G$ have $n$ vertices and let $G_{1}$ arise from $G$ by removing one vertex, say $u_{n}$. Define a new graph $G^{\prime}$ by completing in $G$ all missing edges from $u_{n}$. Then

$$
A\left(G^{\prime}\right)=\left(\begin{array}{ll}
A\left(G_{1}\right)+I, & -e^{T} \\
-e, & n-1
\end{array}\right)
$$

Let $v$ be an eigenvector of $A\left(G_{1}\right)$ corresponding to the eigenvalue $a\left(G_{1}\right)$. Since

$$
A\left(G^{\prime}\right)\binom{v}{0}=\left[a\left(G_{1}\right)+1\right]\binom{v}{0}
$$

$a\left(G_{1}\right)+1$ is an eigenvalue of $A\left(G^{\prime}\right)$ different from zero, i.e.

$$
a\left(G^{\prime}\right) \leqq a\left(G_{1}\right)+1
$$

By 3.2, $a(G) \leqq a\left(G^{\prime}\right)$ which implies (1) for $k=1$. The general case follows by induction.
3.4. We have $a\left(G_{1} \times G_{2}\right)=\min \left(a\left(G_{1}\right), a\left(G_{2}\right)\right)$.

Proof. Let $G_{1}=\left(V_{1}, E_{1}\right), G_{2}=\left(V_{2}, E_{2}\right)$. Order the set $V_{1} \times V_{2}$ lexicographically. Then $A\left(G_{1} \times G_{2}\right)=A\left(G_{1}\right) \times I_{2}+I_{1} \times A\left(G_{2}\right), I_{j}$ being the $\left|V_{j}\right|$-rowed identity matrix. By a well known result from the matrix theory [1] all eigenvalues of $A\left(G_{1} \times\right.$ $\left.\times G_{2}\right)$ are of the form $\mu+v$ where $\mu, v$ resp. are eigenvalues of $A\left(G_{1}\right), A\left(G_{2}\right)$ respectively. Hence the second smallest eigenvalue of $A\left(G_{1} \times G_{2}\right)$ is either $a\left(G_{1}\right)+0$ or $0+a\left(G_{2}\right)$.
3.5. Let $G=(V, E), v_{j}$ be the valency of the $j$-th vertex. Then

$$
a(G) \leqq[n /(n-1)] \min _{i} v_{i} \leqq 2|E| /(n-1)
$$

Proof. Since $n \min _{i} v_{i} \leqq \sum_{i} v_{i}=2|E|$, the second inequality is true. The first is an immediate consequence of the following lemma.

Lemma. Let $M=\left(m_{i k}\right)$ be a symmetric positive semidefinite $n$ by $n$ matrix such that $M e=0$. Then the second smallest eigenvalue $\lambda_{2}$ of $M$ satisfies

$$
\lambda_{2} \leqq[n /(n-1)] \min _{i} m_{i i}
$$

Proof. Observe that

$$
\lambda_{2}=\min _{x \in W} x^{T} M x
$$

Let us show that the matrix

$$
\bar{M}=M-\lambda_{2}\left(I-n^{-1} J\right)
$$

is also positive semidefinite.
Let $y$ be any vector in $E_{n}$. Then $y$ can be written in the form $y=c_{1} e+c_{2} x$ where $x \in W$. Since $\bar{M} e=0$, it follows that

$$
y^{T} \bar{M} y=c_{2}^{2} x^{T} \bar{M} x=c_{2}^{2}\left(x^{T} M x-\lambda_{2}\right) \geqq 0
$$

by (3). Thus the minimum diagonal entry of $\bar{M}$ is nonnegative:

$$
\min _{i} m_{i i}-\lambda_{2}\left(1-n^{-1}\right) \geqq 0
$$

and (2) is proved.
Remark. A matrix $M=\left(m_{i k}\right)$ satisfying conditions of the preceding lemma has also the property that the numbers $\sqrt{ } m_{i i}$ fulfil the polygonal inequality, i.e.

$$
2 \max _{i} m_{i i}^{1 / 2} \leqq \sum_{i} m_{i i}^{1 / 2}
$$

This follows easily from the well known fact that $M$ can be considered as the Gram matrix of a system of $n$ vectors $u_{1}, \ldots, u_{n}$ with sum zero:

$$
m_{i k}=\left(u_{i}, u_{k}\right)=u_{i}^{T} u_{k}, \quad \sum_{i} u_{i}=0
$$

Then we have for the lengths

$$
\left|u_{i}\right| \leqq \sum_{k+i}\left|u_{k}\right| \text { for } \quad i=1, \ldots, n
$$

or

$$
2 \max _{i}\left|u_{i}\right| \leqq \sum_{i}\left|u_{i}\right|
$$

and $\left|u_{i}\right|=\left(u_{i}, u_{i}\right)^{1 / 2}=m_{i i}^{1 / 2}$ yields the result.
If we apply (4) to the matrix $\tilde{M}=M-\lambda_{2}(I-(1 / n) J)$, we obtain

$$
2 \max _{i}\left(m_{i i}-[(n-1) / n] \lambda_{2}\right)^{1 / 2} \leqq \sum_{i}\left(m_{i i}-[(n-1) / n] \lambda_{2}\right)^{1 / 2}
$$

In terms of the graph $G$, we obtain

$$
2 \max _{i}\left[n v_{i}-(n-1) a(G)\right]^{1 / 2} \leqq \sum_{i}\left[n v_{i}-(n-1) a(G)\right]^{1 / 2}
$$

For sake of completeness, we formulate the assertion
3.6. For the complete graph $K_{n}$ with $n$ vertices $a\left(K_{n}\right)=n$.

In the following theorem, we denote by $b(G)$, for a graph $G$ with $n$ vertices, the number

$$
b(G)=n-a(\bar{G})
$$

where $\bar{G}$ is the complementary graph to $G$.
3.7. The function $b(G)$ has following properties:
$1^{\circ} b(G)$ is the maximum eigenvalue of $A(G)$ or, equivalently

$$
b(G)=\max _{x \in W} x^{T} A(G) x
$$

we have thus

$$
a(G) \leqq b(G)
$$

with equality if and only if $G$ is a complete graph or a void graph (i.e. without edges);

$$
2^{\circ} \quad b(G)=\max _{i=1, \ldots, r} b\left(G_{i}\right)
$$

if $G_{1}, \ldots, G_{r}$ are all components of $G$;

$3^{\circ} b\left(G_{1}\right) \leqq b\left(G_{2}\right)$ if $G_{1} \subseteq G_{2}$, i.e. $V_{1} \subseteq V_{2}$ and $E_{1} \subseteq E_{2}$ where $G_{i}=\left(V_{i}, E_{i}\right)$, $i=1,2 ;$

$$
\begin{aligned}
& 4^{\circ} \\
& b\left(G_{1} \cup G_{2}\right) \leqq b\left(G_{1}\right)+b\left(G_{2}\right)-a\left(G_{1} \cap G_{2}\right)
\end{aligned}
$$

where both graphs $G_{1}$ and $G_{2}$ are considered to have the same set of vertices;

$$
[n /(n-1)] \max _{i} v_{i}(G) \leqq b(G) \leqq 2 \max _{i} v_{i}(G)
$$

where $v_{i}(G)$ means valency of the $i$-th vertex in $G$.
Proof. If $\bar{G}$ is the complementary graph to $G$ (with $n$ vertices so that $\bar{G}$ has also $n$ vertices) then

$$
A(G)+A(\bar{G})=n I-J
$$

Since

$$
a(\bar{G})=\min _{x \in W} x^{T} A(\bar{G}) x
$$

and

$$
x^{T}(n I-J) x=n \text { for } x \in W
$$

we have

$$
\max _{x \in W} x^{T} A(G) x=n-\min _{x \in W} x^{T} A(\bar{G}) x=n-a(\bar{G})=b(G)
$$

This implies (6). Let equality be attained in (6). Then $x^{T} A(G) x$ is constant on $W$. Taking first $x=[n(n-1)]^{-1 / 2}\left(n e_{i}-e\right)$ where $e_{i}$ has all coordinates zero except the $i$-th equal to one, we obtain that all the diagonal entries in $A(G)$ are equal. Choosing then $x=2^{-1 / 2} e_{i}-2^{-1 / 2} e_{k}(i \neq k)$, we obtain that also all off-diagonal entries of $A(G)$ are equal, thus all equal either to -1 , or to zero. This proves $1^{\circ}$.
$2^{\circ}$ follows easily from $1^{\circ}$ since $A(G)$ is the direct sum of $A\left(G_{i}\right)$ if $G$ is not connected and $G_{i}$ are components of $G$.

To prove $3^{\circ}$ and $4^{\circ}$, we shall use (6). This implies $3^{\circ}$ immediately while $4^{\circ}$ follows from

$$
A\left(G_{1} \cup G_{2}\right)=A\left(G_{1}\right)+A\left(G_{2}\right)-A\left(G_{1} \cap G_{2}\right)
$$

The right inequality in $5^{\circ}$ follows from $1^{\circ}$ and the well known fact that the maximum modulus of the eigenvalues is less than or equal to any norm. The maximum norm (i.e. with respect to the vector norm $\|x\|=\max _{i}\left|x_{i}\right|$ ) of $A(G)$ (known to be $\left.\max _{i} \sum_{i} \mid a_{i k}\right|$ ) is $2 \max _{i} v_{i}(G)$ which yields this result. To prove the left inequality in $5^{\circ}$, let us apply 3.5 to the complementary graph $\bar{G}$. We obtain

$$
a(\bar{G}) \leqq[n /(n-1)] \min _{i} v_{i}(\bar{G})
$$

which can be written as

$$
n-b(G) \leqq[n /(n-1)]\left[n-1-\max _{i} v_{i}(G)\right]
$$

This implies the inequality and the proof is complete.

3.8. We have

$$
a(G) \geqq 2 \min _{i} v_{i}(G)-n+2
$$

Proof. Follows immediately from the right inequality in $5^{\circ}$ of 3.7 used for the complementary graph $\bar{G}$.
3.9. Let $G$ with $n$ vertices contain an independent set of $m$ vertices (i.e. no two of them joined by an edge of $G)$. Then

$$
a(G) \leqq n-m
$$

Proof. If $G$ contains an independent set of $m$ vertices then $\bar{G}$ contains a complete subgraph $K_{m}$. Since $b\left(K_{m}\right)=m$, we have by $3^{\circ}$ of 3.7 that

$$
b(\bar{G}) \geqq m
$$

so that $a(G)=n-b(\bar{G}) \leqq n-m$.
3.10. If $G$ is a graph with $n$ vertices which is not complete then $a(G) \leqq n-2$.

Proof follows immediately from 3.9 .
3.11. If $K_{p, q}$ denotes the complete bipartite graph the parts of which contain $p$ and $q$ vertices then $a\left(K_{p, q}\right)=\min (p, q)$.

Proof. Follows from $2^{\circ}$ of 3.7 applied to the complement of $K_{p, q}$.
3.12. Let $G=(V, E)$, let $V=V_{1} \cup V_{2}$ be a decomposition of $V$, let $G_{i}(i=1,2)$ be the subgraph of $G$ generated on $V_{i}$. Then

$$
a(G) \leqq \min \left(a\left(G_{1}\right)+\left|V_{2}\right|, a\left(G_{2}\right)+\left|V_{1}\right|\right)
$$

Proof. This is just a symmetric formulation of 3.3.

# 4. RELATIONS BETWEEN $a(G), e(G)$ AND $v(G)$ 

4.1. Let $G$ be a non-complete graph. Then $a(G) \leqq v(G)$.

Proof. Let $G=(V, E)$ and let $V_{1}$ be a vertex cut such that $V_{2}=V-V_{1} \neq \emptyset$. Since the subgraph $G_{2}$ generated by $G$ on $V_{2}$ is not connected, we have by 3.12

$$
a(G) \leqq\left|V_{1}\right|
$$

This implies the assertion.

4.2. We have $v(G) \leqq e(G)$.

Proof. This well known inequality is an easy consequence of the following theorem [3]:

Let $w, w^{\prime}$ be a pair of vertices of $G$. Then there exist $v(G)$ paths between $w, w^{\prime}$ in $G$, no two of them having any vertices in common (except $w, w^{\prime}$ ).
4.3. Let $C_{1}=2[\cos (\pi / n)-\cos (2 \pi / n)], C_{2}=2 \cos (\pi / n)(1-\cos (\pi / n))$ and let $q(G)$ be the maximum vertex valency of the graph $G$. Then

$$
\begin{aligned}
& a(G) \geqq 2 e(G)(1-\cos (\pi / n)) \\
& a(G) \geqq C_{1} e(G)-C_{2} q(G)
\end{aligned}
$$

the second bound being better if and only if $2 e(G)>q(G)$.
Proof. Consider the eigenvalues $\sigma_{1} \geqq \sigma_{2} \geqq \ldots \geqq \sigma_{n}$ of the matrix $S=\left(s_{i j}\right)=$ $=I-q^{-1}(G) A(G)$. This matrix is symmetric and stochastic (i.e. its row sums are 1 and the entries are nonnegative so that $\sigma_{1}=1$ ). Denote by $\mu$ the "measure of irreducibility" of $S$, the number $\min _{\emptyset+M \leqslant N} \sum_{i \in M, i \in M} s_{i k}$, where $N=\{1,2, \ldots, n\}$. Then according to [2]

$$
\begin{aligned}
& 1-\sigma_{2} \geqq 2(1-\cos (\pi / n)) \mu \\
& 1-\sigma_{2} \geqq 1-2(1-\mu) \cos (\pi / n)-(2 \mu-1) \cos (2 \pi / n)
\end{aligned}
$$

We have $\sigma_{2}=1-a(G) / q(G), \mu=e(G) / q(G)$, thus

$$
\begin{aligned}
& a(G) / q(G) \geqq 2(1-\cos (\pi / n)) e(G) / q(G) \\
& a(G) / q(G) \geqq 1-2(1-e(G) / q(G)) \cos (\pi / n)-(2 e(G) / q(G)-1) \cos (2 \pi / n)
\end{aligned}
$$

which implies the required inequalities.
The last assertion is easy to verify.
4.4. We have the following values for some types of graphs.


Remark. After having finished this paper the author was informed that W. N. Anderson, Jr. and T. D. Morley had obtained some of these results in the paper Eigenvalues of the Laplacian of a graph, University of Maryland Technical Report TR-71-45, October 6, 1971.
