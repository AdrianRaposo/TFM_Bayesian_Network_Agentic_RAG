# A NEW SECOND-ORDER CONE PROGRAMMING RELAXATION FOR MAX-CUT PROBLEMS 

Masakazu Muramatsu<br>The University of Electro-Communications<br>Tsunehiro Suzuki<br>Sophia University

(Received: May 16, 2002; Revised: January 17, 2003)


#### Abstract

We propose a new relaxation scheme for the MAX-CUT problem using second-order cone programming. We construct relaxation problems to reflect the structure of the original graph. Numerical experiments show that our relaxation gives better bounds than those based on the spectral decomposition proposed by Kim and Kojima [16], and that the efficiency of the branch-and-bound method using our relaxation is comparable to that using semidefinite relaxation in some cases.


Keywords: Combinatorial optimization, second-order cone programming, MAX-CUT, relaxation, branch-and-bound method

## 1. Introduction

In branch-and-bound methods for solving integer programming problems or nonconvex quadratic problems, the choice of relaxation problem significantly affects overall performance of the algorithm. It is now popular to use semidefinite programming (SDP) ([8, $10,11,21,24,30])$ for relaxation problems whenever possible. Although SDP relaxation gives a good bound, the computational cost of solving SDP is so expensive, despite efforts to develop better algorithms to solve SDP (e.g., [13]), that it is still difficult to use SDP problems in branch-and-bound methods for solving large problems. On the other hand, the so-called lift-and-project (reformulation-linearization) method ( $[2,25]$ ) has been developed to use linear programming (LP) for relaxation. Generally, LP can be solved much more easily than SDP. However, the bounds obtained by the lift-and-project method are worse than those of SDP relaxation unless other effective constraints are added.

Second-order cone programming (SOCP) is an optimization problem having linear constraints and second-order cone constraints. SOCP is a special case of symmetric cone programming ([7]), which also includes SDP and LP as special cases. Recently, primal-dual interior-point algorithms were developed for both SOCP ( $[19,28,29]$ ) and symmetric cone programming ( $[22,26,20])$. Several programs have been implemented to solve SOCP (e.g., [1]) and symmetric cone programming (e.g., [27]). Numerical experiments show that the computational cost of solving SOCP is much less than that of SDP, and similar to LP. It is natural to consider the use of SOCP for relaxation of integer programming or nonconvex quadratic problems, and this is the subject of this paper.

Kim and Kojima [16] first pointed out that SOCP can be used to relax nonconvex quadratic problems. The bounds their relaxation problems provided are worse than those of SDP relaxation, but better than those of lift-and-project LP formulations. It was reported in [16] that their problems spent much less CPU time than SDP in practice.

Their way of constructing SOCP is based on the spectral decomposition of indefinite matrices. When we want to solve problems based on graphs, such as MAX-CUT problems, spectral decomposition destroys the graph's (possibly sparse) structure, and it is difficult to use more information about the graph. For example, it is not obvious with their method how to use the 'triangle inequalities' (see [12] for example) of MAX-CUT problems.

The aim of this paper is to provide an efficient SOCP relaxation suitable for graph-based combinatorial optimization problems. We propose a new relaxation problem for the MAXCUT problem using SOCP. Our relaxation uses the same framework as [16], but our strategy for choosing valid inequalities is different. We obtain effective convex quadratic inequalities that reflect the structure of the original graph. Numerical experiments show that, while consuming slightly more CPU time, our relaxation problem always gives a better bound than that of Kim and Kojima's method. Furthermore, we obtain the 'triangle inequalities', which restrict the feasible region of the relaxed problem efficiently.

We compare the efficiency of the relaxation methods in the context of the branch-andbound method. Specifically, we implemented the branch-and-bound method to solve the MAX-CUT problems by using three SOCP relaxations ((i) Kim and Kojima's method, (ii) our original method, (iii) (ii) + triangle inequalities), and the SDP relaxation. The results show that the overall performance of our methods is always much better than that of Kim and Kojima's method. Furthermore, our SOCP relaxation outperforms the SDP relaxation in sparse graphs.

There are several papers concerning exact solution of MAX-CUT problems for random graphs. Barahona, Jünger and Reinelt [3] solved sparse random MAX-CUT problems of up to 100 nodes using linear relaxation and the branch-and-cut method. For dense graphs which is more difficult to solve, Helmberg and Rendl ([12]) reported that it takes several days for their workstation to compute an optimal solution of dense 100-nodes problem using the branch-and-bound method with the SDP relaxation. It was also reported in [12] that SDP relaxation has some troubles in solving sparse or nearly planar graphs. It will be seen in Section 4 that the SDP relaxation outperforms our SOCP relaxation for dense graphs, while for sparse graphs our SOCP relaxation has better performance than the SDP relaxation.

After the first version of this paper was released, Barahona and Ladányi reported in [4] that their branch-and-cut algorithm solved several 100-nodes problems having edge density $30 \%$ (see Section 4 for the definition of edge density) exactly. This may be one of the best results to date for intermediate (i.e., neither sparse nor dense) graphs.

This paper is organized as follows. In the next section, we describe Kim and Kojima's SOCP relaxation scheme for nonconvex quadratic problems, because we use the same framework of relaxation. Section 3 introduces the MAX-CUT problem and our SOCP relaxation, together with our version of the 'triangle inequalities'. Section 4 is devoted to showing the results of the numerical experiments. In Section 5, we give some concluding remarks.

We denote by $\mathcal{S}(n)$ the set of $n \times n$ real symmetric matrices. Also $\mathcal{S}(n)^{+}$denotes the set of $n \times n$ positive semidefinite matrices. For $X, Y \in \mathcal{S}(n)$,

$$
X \bullet Y:=\sum_{i, j} X_{i j} Y_{i j}
$$

and $X \succeq Y$ if and only if $X-Y \in \mathcal{S}(n)^{+}$. The second-order cone $\mathcal{K}(r)$ is defined by

$$
\mathcal{K}(r)=\left\{x \in \mathbb{R}^{r} \mid x_{1} \geq \sqrt{\sum_{j=2}^{r} x_{j}^{2}}\right\}
$$

The vector $e_{j} \in \mathbb{R}^{n}$ is the zero vector except for the $j$-th component, which is 1 .

# 2. A Nonconvex Quadratic Problem and its Relaxation Problems 

In this section, we consider the following nonconvex quadratic problem:

$$
\langle Q P\rangle\left\{\begin{array}{cl}
\operatorname{minimize} & c^{T} x \\
\text { subject to } & x^{T} Q_{p} x+q_{p}^{T} x+\gamma_{p} \leq 0, \quad p=1, \ldots, m
\end{array}\right.
$$

where $Q_{p} \in \mathcal{S}(n), c \in \mathbb{R}^{n}, q_{p} \in \mathbb{R}^{n}$, and $\gamma_{p} \in \mathbb{R}$. We assume that $Q_{p}, p=1, \ldots, m$ are indefinite matrices in general. Because $x^{T} Q_{p} x=Q_{p} \bullet x x^{T},\langle Q P\rangle$ can also be written as

$$
\begin{cases}\operatorname{minimize} & c^{T} x \\ \text { subject to } & Q_{p} \bullet X+q_{p}^{T} x+\gamma_{p} \leq 0, \quad p=1, \ldots, m \\ & X=x x^{T}\end{cases}
$$

This problem is NP-hard because of the last constraint. We now consider relaxing the problem by replacing this constraint by some other relations between $X$ and $x x^{T}$.

If we simply ignore the constraint $X=x x^{T}$, we obtain the following LP:

$$
\langle L P-Q P\rangle\left\{\begin{array}{cl}
\operatorname{minimize} & c^{T} x \\
\text { subject to } & Q_{p} \bullet X+q_{p}^{T} x+\gamma_{p} \leq 0 \quad(p=1, \ldots, m)
\end{array}\right.
$$

This type of relaxation problem is often called 'lift-and-project' relaxation or the 'reformulationlinearization' technique.

The second idea is to use the property $X \succeq x x^{T}$ instead of $X=x x^{T}$. This constraint is called a semidefinite constraint, and using this we obtain the SDP relaxation:

$$
\langle S D P-Q P\rangle\left\{\begin{array}{cl}
\operatorname{minimize} & c^{T} x \\
\text { subject to } & Q_{p} \bullet X+q_{p}^{T} x+\gamma_{p} \leq 0 \quad(p=1, \ldots, m) \\
& X \succeq x x^{T}
\end{array}\right.
$$

Obviously, $\langle S D P-Q P\rangle$ gives a bound no worse than $\langle L P-Q P\rangle$. On the other hand, the computational cost of $\langle L P-Q P\rangle$ is much less than that of $\langle S D P-Q P\rangle$.

The third relaxation using SOCP proposed by Kim and Kojima [16] is as follows. First, suppose that we are given $\mathcal{C} \subseteq \mathcal{S}(n)^{+}$. It is easy to see that for $Z \in \mathcal{S}(n)$,

$$
Z \succeq 0 \Rightarrow \forall C \in \mathcal{C}, C \bullet Z \geq 0
$$

Using this relation, we relax the constraint $X \succeq x x^{T}$ to $\left(X-x x^{T}\right) \bullet C \geq 0$ for $C \in \mathcal{C}$, which are convex quadratic constraints. Note that if $\mathcal{C}=\mathcal{S}(n)^{+}$, then the right-hand side of (1) also implies the left-hand side.

A convex quadratic constraint can easily be transformed into a second-order cone constraint. To do this, for $C \in \mathcal{C}$, we first decompose $C=U U^{T}$, where $U \in \mathbb{R}^{n \times k}$ and $k=\operatorname{Rank}(C)$. Such a decomposition is always possible, as $C$ is symmetric and positive semidefinite. The constraint $C \bullet X \geq x^{T} C x$ is equivalent to

$$
x^{T} U U^{T} x \leq C \bullet X
$$

Observe that for any $w \in \mathbb{R}^{n}, \eta, \xi \in \mathbb{R}$,

$$
w^{T} w \leq \xi \eta, \xi \geq 0, \eta \geq 0 \Leftrightarrow\left(\begin{array}{c}
\xi+\eta \\
\xi-\eta \\
2 w
\end{array}\right) \in \mathcal{K}(n+2)
$$

Therefore, (2) is equivalent to

$$
\left(\begin{array}{c}
1+C \bullet X \\
1-C \bullet X \\
2 U^{T} x
\end{array}\right) \in \mathcal{K}(k+2)
$$

This is the basic idea of the SOCP relaxation for nonconvex quadratic programming. The final form of the SOCP is as follows:

$$
\langle S O C P-Q P\rangle\left\{\begin{array}{cl}
\operatorname{minimize} & c^{T} x \\
\text { subject to } & Q_{p} \bullet X+q_{p}^{T} x+\gamma_{p} \leq 0, \quad p=1, \ldots, m \\
& \left(\begin{array}{c}
1+C \bullet X \\
1-C \bullet X \\
2 U^{T} x
\end{array}\right) \in \mathcal{K}(\operatorname{Rank}(C)+2), \quad i=1, \ldots, r \\
& C \in \mathcal{C}, C=U U^{T}
\end{array}\right.
$$

The problem $\langle S O C P-Q P\rangle$ has $O\left(n^{2}\right)$ variables. This number of variables makes it difficult to solve the resulting SOCP when $n$ is large. Kim and Kojima [16] proposed a technique to reduce the number of variables, and demonstrated that with this technique, the SOCP relaxation could have overall performance as good as that of LP relaxation and SDP relaxation. We next explain their method.

For the sake of simplicity, we omit the subscript $p$ and consider the linear inequality

$$
Q \bullet X+q^{T} x+\gamma \leq 0
$$

Let

$$
Q=\sum_{j=1}^{n} \lambda_{j} u_{j} u_{j}^{T}
$$

be the spectral decomposition of $Q$, where $\lambda_{j}$ are eigenvalues and $u_{j}$ are corresponding unit eigenvectors. Without loss of generality, we assume that

$$
\lambda_{1} \geq \ldots \geq \lambda_{l} \geq 0>\lambda_{l+1} \geq \ldots \geq \lambda_{n}
$$

and put $Q^{+}:=\sum_{j=1}^{l} \lambda_{j} u_{j} u_{j}^{T}$. We choose $Q^{+}$and $u_{j} u_{j}^{T}, j=l+1, \ldots, n$ for $\mathcal{C}$ to obtain the following inequalities:

$$
\begin{aligned}
x^{T} Q^{+} x-Q^{+} \bullet X & \leq 0 \\
x^{T} u_{j} u_{j}^{T} x-u_{j} u_{j}^{T} \bullet X & \leq 0 \quad j=l+1, \ldots, n
\end{aligned}
$$

Then, summing up (3) and (4), we produce a new (weaker) inequality:

$$
x^{T} Q^{+} x+\sum_{j=l+1}^{n} \lambda_{j} u_{j} u_{j}^{T} \bullet X+q^{T} x+\gamma \leq 0
$$

If $(x, X)$ satisfies (3) and (4), then it also satisfies (6), but the converse is not generally true. Putting $z_{j}=u_{j} u_{j}^{T} \bullet X$, we obtain the following convex quadratic constraints that do not contain $X$ :

$$
\begin{aligned}
x^{T} Q^{+} x+\sum_{j=l+1}^{n} \lambda_{j} z_{j}+q^{T} x+\gamma & \leq 0 \\
x^{T} u_{j} u_{j}^{T} x-z_{j} & \leq 0, \quad j=l+1, \ldots, n
\end{aligned}
$$

The relaxation problem using this parameter-reducing technique is called the Kim and Kojima's SOCP relaxation in this paper.

A substantial advantage of the Kim and Kojima's SOCP relaxation is that we can reduce the number of variables from $O\left(n^{2}\right)$ to the total number of negative eigenvalues of $Q_{p} \mathrm{~s}$. On the other hand, the inequalities (7) and (8) are weaker than the original constraints (3),(4), and (5). In fact, if we do not impose any upper bound on $z_{j}$, then any $x$ can satisfy (7) and (8) with large $z_{j} \mathrm{~s}$ (note that $\lambda_{j}<0$ for $j>l$ ). Therefore, we require some restriction on $z_{j}$ in advance.

# 3. The MAX-CUT Problem and its Relaxations 

### 3.1. The MAX-CUT problem

Let $\mathcal{G}=(V, \mathcal{E})$ be an undirected graph where $V=\{1, \ldots, n\}$ and $\mathcal{E}$ are the sets of vertices and edges, respectively. We assume that a weight $w_{i j}$ is attached to each edge $[i, j] \in \mathcal{E}$. For a partition $(S, \bar{S})$ of $V$, we define

$$
w(S, \bar{S}):=\sum_{[i, j] \in \mathcal{E}, i \in S, j \in \bar{S}} w_{i j}
$$

The MAX-CUT problem is to find a partition maximizing $w(S, \bar{S})$.
For each $i \in V$, we put

$$
x_{i}= \begin{cases}1 & \text { if } i \in S \\ -1 & \text { if } i \in \bar{S}\end{cases}
$$

Because $\left(x_{i}-x_{j}\right)^{2}=4$ if $i$ and $j$ belong to different sets and 0 otherwise, we see that

$$
w(S, \bar{S})=\frac{1}{4} \sum_{[i, j] \in \mathcal{E}} w_{i j}\left(x_{i}-x_{j}\right)^{2}=\frac{1}{2} \sum_{[i, j] \in \mathcal{E}} w_{i j}-\frac{1}{2} \sum_{[i, j] \in \mathcal{E}} w_{i j} x_{i} x_{j}
$$

Let us now define $L \in \mathcal{S}(n)$ by

$$
L_{i j}=L_{j i}= \begin{cases}\sum_{[i, k] \in \mathcal{E}} w_{i k} & \text { if } i=j \\ -w_{i j} & \text { if }[i, j] \in \mathcal{E} \\ 0 & \text { otherwise }\end{cases}
$$

Then the objective function can be written as $x^{T} L x / 4$. Therefore, we can write the MAXCUT problem as

$$
\langle M C\rangle \begin{cases}\text { maximize } & x^{T} L x / 4 \\ \text { subject to } & x \in\{-1,1\}^{n}\end{cases}
$$

Because

$$
x_{j}=1 \text { or }-1 \Leftrightarrow x_{j}^{2}=1 \Leftrightarrow x_{j}^{2} \leq 1 \text { and } x_{j}^{2} \geq 1 \Leftrightarrow x^{T} e_{j} e_{j}^{T} x \leq 1 \text { and } x^{T}\left(-e_{j} e_{j}^{T}\right) x \leq-1
$$

and

$$
\text { maximize } x^{T} L x / 4 \Leftrightarrow \text { minimize } \theta \text { subject to }-x^{T} L x / 4 \leq \theta
$$

$\langle M C\rangle$ belongs to the nonconvex quadratic problems introduced in Section 2.
Now we introduce the Kim and Kojima's SOCP relaxation of $\langle M C\rangle$. First, we convert $\langle M C\rangle$ into the following nonconvex quadratic problem:

$$
\left\{\begin{array}{ll}
\operatorname{minimize} & \theta \\
\text { subject to } & -x^{T} L x / 4-\theta \leq 0 \\
& x^{T} e_{j} e_{j}^{T} x \leq 1, j=1, \ldots, n \\
& x^{T}\left(-e_{j} e_{j}^{T}\right) x \leq-1, j=1, \ldots, n
\end{array}\right.
$$

Let

$$
L=\sum_{j=1}^{n} \lambda_{j} q_{j} q_{j}^{T}
$$

be the eigenvalue decomposition with

$$
\lambda_{1} \geq \ldots \geq \lambda_{l} \geq 0>\lambda_{l+1} \geq \ldots \geq \lambda_{n}
$$

and put $L^{+}=\sum_{j=1}^{l} \lambda_{j} q_{j} q_{j}^{T}$. As in Section 2, Kim and Kojima's SOCP relaxation of $\langle M C\rangle$ is as follows:

$$
\langle S O C P 1-M C\rangle\left\{\begin{array}{ll}
\operatorname{minimize} & \theta \\
\text { subject to } & -x^{T} L^{+} x / 4+\sum_{j=l+1}^{n} \lambda_{j} z_{j}-\theta \leq 0 \\
& x^{T} q_{j} q_{j}^{T} x-z_{j} \leq 0, j=l+1, \ldots, n \\
& x^{T} e_{j} e_{j}^{T} x \leq 1, j=1, \ldots, n \\
& z_{j} \leq \sqrt{n}, j=l+1, \ldots, n
\end{array}\right.
$$

Here, the bound for $z_{j}=q_{j}^{T} X q_{j}$ comes from the fact that $X_{i j}$ is either +1 or -1 , and $\left\|q_{j}\right\|=1$.

# 3.2. An SOCP relaxation for MAX-CUT problem 

We now state our new SOCP relaxation for $\langle M C\rangle$ based on the general framework $\langle S O C P-$ $Q P\rangle$. Our aim is to use the structure of $L$. To do this, we first put

$$
\begin{aligned}
u_{i j} & :=e_{i}+e_{j} \\
v_{i j} & :=e_{i}-e_{j}
\end{aligned}
$$

Our choice of $\mathcal{C}$ consists of the following:

$$
\begin{aligned}
e_{i} e_{i}^{T}, & i=1, \ldots, n \\
u_{i j} u_{i j}^{T}, & {[i, j] \in \mathcal{E}} \\
v_{i j} v_{i j}^{T}, & {[i, j] \in \mathcal{E}}
\end{aligned}
$$

The corresponding convex quadratic constraints are:

$$
\begin{gathered}
x^{T} e_{i} e_{i}^{T} x-e_{i} e_{i}^{T} \bullet X \leq 0, \quad i=1, \ldots, n \\
x^{T} u_{i j} u_{i j}^{T} x-u_{i j} u_{i j}^{T} \bullet X \leq 0, \quad[i, j] \in \mathcal{E} \\
x^{T} v_{i j} v_{i j}^{T} x-v_{i j} v_{i j}^{T} \bullet X \leq 0 . \quad[i, j] \in \mathcal{E}
\end{gathered}
$$

We show that, like Kim and Kojima's SOCP relaxation, we can reduce the number of variables in a simpler and more efficient way by using the structure of the MAX-CUT problem. From (13) and the fact that $X_{i i}=1$, we have

$$
x^{T} e_{i} e_{i}^{T} x \leq 1, \quad i=1, \ldots, n
$$

or $x_{i}^{2} \leq 1$. By introducing new variables

$$
\begin{aligned}
& s_{i j}:=u_{i j}^{T} X u_{i j}, \quad[i, j] \in \mathcal{E} \\
& z_{i j}:=v_{i j}^{T} X v_{i j}, \quad[i, j] \in \mathcal{E}
\end{aligned}
$$

we obtain convex quadratic inequalities from (14) and (15):

$$
\begin{array}{ll}
\left(x_{i}+x_{j}\right)^{2} & \leq s_{i j}, \quad[i, j] \in \mathcal{E} \\
\left(x_{i}-x_{j}\right)^{2} & \leq z_{i j}, \quad[i, j] \in \mathcal{E}
\end{array}
$$

For those variables, we have the following bound:

$$
s_{i j}+z_{i j}=X \bullet\left(u_{i j} u_{i j}^{T}+v_{i j} v_{i j}^{T}\right)=2\left(X_{i i}+X_{j j}\right)=4
$$

Furthermore, we have the following proposition:

# Proposition 1 

$$
L=-\sum_{[i, j] \in \mathcal{E}} L_{i j} v_{i j} v_{i j}^{T}
$$

Proof: Let us define

$$
\delta_{i j}:=e_{i}^{T} e_{j}= \begin{cases}1 & \text { if } i=j \\ 0 & \text { otherwise }\end{cases}
$$

The $(k, l)$ component of the negative of the right-hand side of (22) is:

$$
\begin{aligned}
e_{k}^{T}\left(\sum_{[i, j] \in \mathcal{E}} L_{i j} v_{i j} v_{i j}^{T}\right) e_{l} & =\sum_{[i, j] \in \mathcal{E}} L_{i j} e_{k}^{T}\left(e_{i}-e_{j}\right)\left(e_{i}-e_{j}\right)^{T} e_{l} \\
& =\sum_{[i, j] \in \mathcal{E}} L_{i j}\left(\delta_{k i} \delta_{i l}+\delta_{k j} \delta_{j l}-\delta_{k i} \delta_{j l}-\delta_{k j} \delta_{i l}\right) \\
& = \begin{cases}\sum_{[k, j] \in \mathcal{E}} L_{k j} & \text { if } k=l \\
-L_{k l} & \text { if }[k, l] \in \mathcal{E} \\
0 & \text { otherwise }\end{cases} \\
& =-L_{k l}
\end{aligned}
$$

where the last equality is due to the definition of $L$. This proves the proposition.
For $v \in \mathbb{R}^{n}$ and $X \in \mathcal{S}(n)$, it holds that $v v^{T} \bullet X=\sum_{i, j} v_{i} v_{j} X_{i j}=v^{T} X v$. Using this relation, we can rewrite the objective function of $\langle M C\rangle$ as

$$
L \bullet X=-\sum_{[i, j] \in \mathcal{E}} L_{i j} v_{i j} v_{i j}^{T} \bullet X=-\sum_{[i, j] \in \mathcal{E}} L_{i j} v_{i j}^{T} X v_{i j}=-\sum_{[i, j] \in \mathcal{E}} L_{i j} z_{i j}
$$

(Notice that $v_{i j}$ is a vector.)
With $X$ removed from the problem, we obtain the relaxation problem:

$$
\langle S O C P 2-M C\rangle\left\{\begin{array}{ll}
\text { maximize } & -\sum_{[i, j] \in \mathcal{E}} L_{i j} z_{i j} \\
\text { subject to } & x_{i}^{2} \leq 1, \quad i=1, \ldots, n \\
& \left(x_{i}+x_{j}\right)^{2} \leq s_{i j}, \quad[i, j] \in \mathcal{E} \\
& \left(x_{i}-x_{j}\right)^{2} \leq z_{i j}, \quad[i, j] \in \mathcal{E} \\
& s_{i j}+z_{i j}=4, \quad[i, j] \in \mathcal{E}
\end{array}\right.
$$

Because $\langle S O C P 2-M C\rangle$ is a convex quadratic program, the conversion of this to SOCP is straightforward by using the technique described in Section 2.

Notice that the number of variables in $\langle S O C P 2-M C\rangle$ depends on the graph structure. Because the number is $O(|\mathcal{E}|)$, if the graph is sparse, then the size of $\langle S O C P 2-M C\rangle$ is relatively small. On the other hand, if the graph is dense, there will be $O\left(n^{2}\right)$ variables and it will be difficult to solve $\langle S O C P 2-M C\rangle$. In that case, we should consider eliminating several inequalities to fit our purpose.

# 3.3. The triangle inequalities 

Let us consider $\langle M C\rangle$ as $\langle Q P\rangle$. Then it is true that

$$
\begin{aligned}
X_{i j}+X_{j k}+X_{i k} & \geq-1 \\
X_{i j}-X_{j k}-X_{i k} & \geq-1 \\
-X_{i j}-X_{j k}+X_{i k} & \geq-1 \\
-X_{i j}+X_{j k}-X_{i k} & \geq-1
\end{aligned}
$$

as at least two of nodes $i, j, k$ should be contained in the same set. These inequalities are called 'triangle inequalities' and play an important role in obtaining better bounds in the SDP relaxation and the lift-and-project method.

In Kim and Kojima's SOCP relaxation, it is difficult to utilize these inequalities, because their method does not use $X$. Our SOCP relaxation also does not use $X$. However, we can make use of these kinds of inequality, as our problem inherits the graph structure of the original problem.
Proposition 2 if $[i, j],[j, k],[k, l] \in \mathcal{E}$, then

$$
\begin{aligned}
& z_{i j}+z_{j k}+z_{i k} \leq 8 \\
& z_{i j}+s_{j k}+s_{k i} \leq 8 \\
& s_{i j}+s_{j k}+z_{k i} \leq 8 \\
& s_{i j}+z_{j k}+s_{k i} \leq 8
\end{aligned}
$$

Proof: Because the diagonal elements of $X$ are always 1,

$$
\begin{aligned}
z_{i j}+z_{j k}+z_{i k} & =v_{i j}^{T} X v_{i j}+v_{j k}^{T} X v_{j k}+v_{i k}^{T} X v_{i k} \\
& =2\left(X_{i i}+X_{j j}+X_{k k}\right)-2\left(X_{i j}+X_{j k}+X_{i k}\right) \\
& =6-2\left(X_{i j}+X_{j k}+X_{i k}\right)
\end{aligned}
$$

From (23), it follows that

$$
z_{i j}+z_{j k}+z_{i k} \leq 8
$$

The rest of the proposition can be proved similarly, and thus we omit the proof.

### 3.4. A relationship to linear relaxation

Suppose that we put $x_{i}=0$ for all $i$. Then we can eliminate the variables $x$ and $s$ from $\langle S O C P 2-M C\rangle$ to have

$$
\left\{\begin{array}{l}
\operatorname{maximize}-\sum_{[i, j] \in \mathcal{E}} L_{i j} z_{i j} \\
\text { subject to } 0 \leq z_{i j} \leq 4, \quad[i, j] \in \mathcal{E}
\end{array}\right.
$$

which is the trivial linear relaxation of $\langle M C\rangle$ (see $[2,25,3]$ ). In other words, if we do not fix any node, then $x$ can be zero thus the feasible region of $\langle S O C P 2-M C\rangle$ includes that of (32). This means that the bound given by $\langle S O C P 2-M C\rangle$ is no better than that of (32). However, once we fix several nodes to +1 or -1 in the branch-and-bound method, $\langle S O C P 2-M C\rangle$ is no longer equivalent with the linear relaxation. Notice also that we can fix at least one node to +1 without loss of generality, thus our relaxation is different from the linear relaxation even at the first step of the branch-and-bound method.

# 4. Numerical Experiments 

In this section we numerically compare the following four relaxation problems:

1. SDP: the SDP relaxation.
2. SOCP1: the SOCP relaxation proposed by Kim and Kojima.
3. SOCP2: the SOCP relaxation by $\langle S O C P 2-M C\rangle$.
4. SOCP3: SOCP2 with the triangle inequalities (27).

SDPA 5.01 ([9]), an implementation of primal-dual interior-point method, was used to solve SDP. SOCP was solved by our own implementation of the primal-dual interior-point method. In both solvers, the HKM direction ( $[14,17,18]$ ) was used and the Mehrotratype predictor-corrector method was adopted. All computations were performed on an Intel Pentium-based computer (CPU: Intel Celeron 733 MHz , Memory: 512 MB , OS: VINE Linux 2.1, C and $\mathrm{C}++$ compilers: egcs-2.91.66).

Our SOCP solver, which we implemented from scratch to exploit sparse data structures, is preliminary and has a lot of room for improvement. In speed, it is not yet competitive with some commercial codes such as the MOSEK solver ( $[1]$ ). There are two reasons why we use our own code.

One is that when we started this research, it was difficult to find a callable C library function for solving SOCP, which is indispensable for implementation of the branch-andbound method where we have to solve many SOCP problems.

The other is that we could devise some techniques to improve the efficiency of the interiorpoint method using special structure of our SOCP relaxation. One of such techniques is as follows. Suppose that in the branch-and-bound method, we fix values of some nodes to +1 or -1 . If the set of non-fixed nodes is $\tilde{V}$ and $\tilde{\mathcal{E}}=\{[i, j] \in \mathcal{E} \mid i \in \tilde{V}$ or $j \in \tilde{V}\}$, then the variables in $\langle S O C P 2-M C\rangle$ are $x_{j}, j \in \tilde{V}, s_{i j},[i, j] \in \tilde{\mathcal{E}}$, and $z_{i j},[i, j] \in \tilde{\mathcal{E}}$. Observe that the locations of nonzero coefficients of those variables depend only on $\tilde{V}$ and $\tilde{\mathcal{E}}$. The nonzero pattern of the coefficient matrix of SOCP is identical regardless of the values +1 or -1 of the fixed nodes. As a result, when the problems have the same $\tilde{V}$ and $\tilde{\mathcal{E}}$, we solve the linear system having the same non-zero pattern to calculate the search direction of the interior-point method. We could reuse our sparse data areas between such problems to save CPU time for symbolic Choleskey factorizations.

We generated the following two types of MAX-CUT problems by using rudy, a graph generator written by Giovanni Rinaldi (See [13]).

1. $G_{w r}$ : a general random graph. $1 \leq w_{i j} \leq 50$.
2. $G_{p 2}$ : a union of two planar random graphs having the same set of vertices. The weight was always 1 .
Each figure in the tables is an average of 10 trials, if not otherwise stated.
The edge density of a general graph is defined by $2|\mathcal{E}| /|V|(|V|-1)$, while the density of a planar graph (p-density) is defined by $|\mathcal{E}| / 3(|V|-2)$. For $G_{p 2}$, which is not a planar graph in general, we use the term 'p2-density' for the p-density of the original planar graphs. Notice that the number of edges of $G_{p 2}$ is between $d$ and $2 d$, where $d$ is the number of edges in the original planar graphs.

### 4.1. Comparison in quality of relaxed problems

We check the quality of the solutions of the relaxed problems. The relative error, denoted by $\epsilon$ in the tables, is defined by

$$
\epsilon:=\frac{\theta_{\mathrm{ubd}}-\theta_{\mathrm{opt}}}{\theta_{\mathrm{opt}}}
$$

Table 1: Relative error of relaxed problems: $G_{w r}$ (density 10\%)


Table 2: Relative error of relaxed problems: $G_{p 2}$ (p2-density 30\%)


where $\theta_{\text {ubd }}$ and $\theta_{\text {opt }}$ are the optimal values of the relaxed and original problems, respectively.
In Table 1, we see the relative errors of relaxed problems for $G_{w r}$ with running time of the solvers. The tri column in SOCP3 shows the average number of triangle inequalities. We used all the possible triangle inequalities of the given graphs.

According to this table, SOCP3 gives better bounds than SOCP2, as is theoretically assured. Even SOCP2 gives much better bounds than SOCP1. On the other hand, SOCP1 used the least CPU time, while SOCP3 used the most. In this table, SDP always gives the best bounds, while consuming as much CPU time as SOCP1.

Table 2 shows that the ratio of the errors between SOCP1 and SOCP2 in $G_{p 2}$ is larger than that in $G_{w r}$. This implies that our relaxation will be more efficient for nearly planar graphs. Furthermore, the errors of SOCP3 are less than half those of SOCP2. It seems that, because $G_{p 2}$ is close to a planar graph, we can choose more of the triangle inequalities that effectively bound the feasible region. In $G_{p 2}$, SDP gives slightly better bounds than SOCP3, consuming slightly more CPU time.

# 4.2. Results of branch-and-bound methods 

We have implemented a branch-and-bound method for $\langle M C\rangle$. In branching, we pick up a node and fix its value to +1 or -1 . The node is chosen from the ones having the maximum number of edges. We use a depth-first search.

Tables 3,4 , and 5 are the results of the branch-and-bound method. The time column and node column show the CPU time spent and the number of relaxed problems solved in the branch-and-bound method, respectively. In the cell marked *, only seven of the ten test problems could be solved in the predefined time.

From Table 3 showing the results for $G_{w r}$, we see immediately that SOCP1 does not work efficiently in the branch-and-bound methods for solving MAX-CUT problems. Both the number of nodes and CPU time are very large in SOCP1; SOCP1 could not give effective upper bound of the optimal value. The difference in performance between SOCP1 and the other methods was so large that we did not use SOCP1 in the following experiments.

In Table 3, the results for $G_{w r}$ of $10 \%$ edge density, SOCP2 and SOCP3 spent approxi-

Table 3: Branch-and-Bound: $G_{w r}$ (density 10\%)


Table 4: Branch-and-Bound: $G_{w r}$ (density 2\%)


mately the same CPU time when the graph is small, but for larger graphs, SOCP3 uses less time. SDP is far superior to the other methods in this case.

Comparing Tables 3 and 4, we notice that the edge density significantly affects the performance of SOCP2 and SOCP3; they perform better if the edge density is small. This is not surprising, because in SOCP2 and SOCP3, the problem size is proportional to the number of edges. On the other hand, it seems that SDP cannot deal with sparse graphs efficiently. Both SOCP2 and SOCP3 outperform SDP in Table 4.

In Table 5 showing the results for $G_{p 2}$, SOCP2 and SOCP3 also outperform SDP, and the performance gap becomes large compared to Table 4. SOCP3 is far superior to the others in terms of CPU time used. The use of the triangle inequalities seems very effective for nearly planar graphs, as we observed in the previous subsection.

In view of Table 2, SDP gives a better bound than SOCP3, while consuming a comparable amount of CPU time. Furthermore, Table 5 shows that SOCP3 uses more nodes than SDP. Nevertheless, the total time of the branch-and-bound method using SOCP3 is much less than that using SDP. One reason for this may be as follows. In our branch-and-bound method, we choose the value-fixing node from nodes having the maximum number of edges.

Table 5: Branch-and-Bound: $G_{p 2}$ (p2-density 30\%)


This implies that, as the branch-and-bound method goes down the branching tree, the child problems become more and more sparse. For our SOCP relaxation, sparser data means a smaller problem, which can be solved in shorter time. As a result, the branch-and-bound method speeds up as it goes down the tree. On the other hand, since it is hard for SDP relaxation to exploit sparsity, this kind of speed-up cannot be expected.

# 5. Concluding Remarks 

In this paper, we proposed a new relaxation scheme for MAX-CUT problems using SOCP. Numerical experiments show that our method is superior to Kim and Kojima's SOCP relaxation applied to MAX-CUT problems. Compared to the SDP relaxation, our method gives a better performance when solving MAX-CUT problems for sparse or structured graphs.

If we could incorporate the triangle inequality into SDP relaxation, we would obtain tighter bounds. However, in our case, SDPA will not work with triangle inequalities. It seems that the number of linear inequality constraints heavily affects the CPU time required by SDPA.

There are several algorithms to solve the SDP relaxation of MAX-CUT problems other than the primal-dual interior-point methods. The dual-scaling method by Benson, Ye, and Zhang ([5]), the spectral-bundle method by Helmberg and Rendl ([13]), and nonlinear programming formulation by Burer and Monteiro ([6]) are such algorithms. Most of such algorithms are said to be more efficient for solving the SDP relaxation of MAX-CUT problems, mainly because by exploiting sparsity of the coefficient matrices. However, their interest seems to solve as large SDP problems as possible, and not to solve the MAX-CUT problem itself. The efficiency of their methods when used in the branch-and-bound method is unknown. Checking the efficiency of these algorithms in the branch-and-bound method and comparing them to the SOCP relaxation proposed in this paper is another topic of research.

Application of the proposed SOCP relaxation to other graph-based problems is obvious in some cases. For example, consider the MAX-DICUT problem, which is the same problem as the MAX-CUT except the two partitioned sets must have the same number of nodes. It is easy to see that this problem can be formulated as $\langle M C\rangle$ with an additional equality constraint $e^{T} x=0$. Since SOCP can handle arbitrary linear equalities, it is straightforward to apply our SOCP relaxation to the MAX-DICUT problems.

Proving a theoretical bound of our SOCP relaxation and investigating a connection to other relaxations will be the subjects of further research. In addition, checking the efficiency of our SOCP relaxation by extensive numerical experiments using more sophisticated SOCP solvers is another important issue.

## Acknowledgments

The authors would like to thank Dr. K. Fujisawa of Kyoto University for giving us a chance to use SDPA and sometimes rewriting his code in response to our requests. The authors would like to thank two anonymous referees for their valuable comments to improve the presentation of this paper. The second author thanks Dr. Y. Ishizuka of Sophia University for his supervision and helpful comments.

This research is supported in part by the Ministry of Education, Culture, Sports, Science and Technology of Japan.
