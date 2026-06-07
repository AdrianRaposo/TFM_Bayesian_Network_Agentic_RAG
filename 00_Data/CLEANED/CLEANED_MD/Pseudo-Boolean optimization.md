# Pseudo-Boolean Optimization 

Yves Crama* Peter L. Hammer ${ }^{\dagger}$

December 20, 2000


#### Abstract

This article briefly surveys some fundamental results concerning pseudo-Boolean functions, i.e. real-valued functions of $0-1$ variables. Hundreds of papers have been devoted to the investigation of pseudo-Boolean functions, and a rich and diversified theory has now emerged from this literature. The article states local optimality conditions, outlines basic techniques for global pseudo-Boolean optimization, and shows connections between best linear approximations of pseudo-Boolean functions and game theory. It also describes models and applications arising in various fields, ranging from combinatorics to management science, and points to several classes of functions of special interest.


Keywords: integer programming, nonlinear 0-1 optimization, max-sat, max-cut, graph stability, game theory.

## 1 Pseudo-Boolean functions

### 1.1 Definitions and representations

A pseudo-Boolean function is a mapping from $\{0,1\}^{n}$ to $\Re$, i.e. a real-valued function of a finite number of $0-1$ variables. Pseudo-Boolean functions have been introduced in [15], and extensively studied in [16] and in numerous subsequent publications; a detailed survey appears in [4].

Pseudo-Boolean functions generalize Boolean functions, which are exactly those pseudoBoolean functions whose values are in $\{0,1\}$, i.e. those $f(X)$ for which $f^{2}(X)-f(X) \equiv 0$ in $\{0,1\}^{n}$. Since the elements of $\{0,1\}^{n}$ are in one-to-one correspondence with the subsets

[^0]
[^0]:    *Ecole d'Administration des Affaires, University of Liège, Boulevard du Rectorat 7 (B31), 4000 Liège, Belgium, Y.Crama@ulg.ac.be
    ${ }^{\dagger}$ RUTCOR, Rutgers University, 640 Bartholomew Road, Piscataway, NJ 08854-8003, U.S.A., Hammer@rutcor.rutgers.edu

of $N=\{1,2, \ldots, n\}$, every pseudo-Boolean function can be interpreted as a real-valued set function defined on $\mathcal{P}(N)$, the power set of $N=\{1,2, \ldots, n\}$. Viewing pseudoBoolean functions as defined on $\{0,1\}^{n}$, rather than on $\mathcal{P}(N)$, provides an algebraic viewpoint which sometimes carries clear advantages. It is easy to see for instance that the set of all pseudo-Boolean functions in $n$ variables forms a vector space over $\Re$, and that the elementary monomials $\prod_{i \in A} x_{i}(A \in \mathcal{P}(N))$ define a basis of this space. In particular, every pseudo-Boolean function $f\left(x_{1}, x_{2}, \ldots, x_{n}\right)$ can be uniquely represented as a multilinear polynomial of the form

$$
f\left(x_{1}, x_{2}, \ldots, x_{n}\right)=c_{0}+\sum_{k=1}^{m} c_{k} \prod_{i \in A_{k}} x_{i}
$$

where $c_{0}, c_{1}, \ldots, c_{m}$ are real coefficients, and $A_{1}, A_{2}, \ldots, A_{m}$ are nonempty subsets of $N$. When viewed as a function on $[0,1]^{n}$, the right-hand side of (1) defines a continuous extension of the pseudo-Boolean function $f$, to be denoted $f^{c}$.
Note that every pseudo-Boolean function also admits (many) representations of the form

$$
f\left(x_{1}, x_{2}, \ldots, x_{n}\right)=b_{0}+\sum_{k=1}^{m} b_{k}\left(\prod_{i \in A_{k}} x_{i} \prod_{j \in B_{k}} \bar{x}_{j}\right)
$$

where $b_{0}, b_{1}, \ldots, b_{m}$ are real coefficients, and $\bar{x}_{j}=1-x_{j}$ for $j=1,2, \ldots, n$. If $b_{k} \geq 0$ for all $k=1,2, \ldots, m$, then we say that the expression (2) is a posiform of $f$. It is easy to see that every pseudo-Boolean function can be expressed as a posiform. Other representations of pseudo-Boolean functions have been recently investigated in [12].

# 1.2 Representative models 

Besides nonlinear binary optimization, pseudo-Boolean functions can also be used to model a wide variety of problems in different fields of appplication.

Maximum satisfiability. Consider a collection of Boolean clauses $\left(\bigvee_{i \in A_{k}} \bar{x}_{i} \vee \bigvee_{j \in B_{k}} x_{j}\right.$ : $k=1,2, \ldots, m)$. The maximum satisfiability problem is to find a vector $\left(x_{1}, x_{2}, \ldots, x_{n}\right)$ in $\{0,1\}^{n}$ which satisfies the largest possible number of clauses in the collection. This problem, which generalizes the NP-complete satisfiability problem, is equivalent to that of minimizing the posiform (2) with $b_{k}=1$ for $k=1,2, \ldots, m$; see e.g. [17].

Graph theory. Consider a graph $G=(N, E)$ with positive weights $w: N \rightarrow \Re$ on its vertices, and capacities $c: E \rightarrow \Re$ on its (undirected) edges. For every $S \subseteq N$, the cut $(S, N \backslash S)$ is the set of edges having exactly one endpoint in $S$; the capacity of this cut is $\sum_{\{i, j\} \in(S, N \backslash S)} c(i, j)$. The max-cut problem is to find a cut of maximum capacity in $G$. This problem is equivalent to maximizing the quadratic pseudo-Boolean function

$$
f\left(x_{1}, x_{2}, \ldots, x_{n}\right)=\sum_{1 i<j} c(i, j)\left(x_{i} \bar{x}_{j}+\bar{x}_{i} x_{j}\right)
$$

under the interpretation that $\left(x_{1}, x_{2}, \ldots, x_{n}\right)$ is the characteristic vector of $S$.
A stable set in $G$ is a set $S \subseteq N$ such that no edge has both of its endpoints in $S$; the weight of $S$ is $\sum_{i \in S} w(i)$. The weighted stability problem is to find a stable set of maximum weight in $G$. This can be seen to be equivalent to maximizing the quadratic pseudo-Boolean function

$$
f\left(x_{1}, x_{2}, \ldots, x_{n}\right)=\sum_{i=1}^{n} w(i) x_{i}-\left(1+\min _{1 \quad i \quad n} w(i)\right) \sum_{i<j} x_{i} x_{j}
$$

where $\left(x_{1}, x_{2}, \ldots, x_{n}\right)$ is the characteristic vector of $S$. Other connections between the weighted stability problem and pseudo-Boolean optimization (in particular, posiforms) have been exploited in [11].

Linear 0-1 programming. Consider the linear 0-1 program

$$
\begin{array}{ll}
\operatorname{maximize} & z\left(x_{1}, x_{2}, \ldots, x_{n}\right)=\sum_{j=1}^{n} c_{j} x_{j} \\
\text { subject to } & \sum_{j=1}^{n} a_{i j} x_{j}=b_{i}, \quad i=1,2, \ldots, m \\
& \left(x_{1}, x_{2}, \ldots, x_{n}\right) \in\{0,1\}^{n}
\end{array}
$$

This problem is equivalent to the quadratic pseudo-Boolean optimization problem

$$
\begin{array}{ll}
\operatorname{maximize} & f\left(x_{1}, x_{2}, \ldots, x_{n}\right)=\sum_{j=1}^{n} c_{j} x_{j}-M \sum_{i=1}^{m}\left(\sum_{j=1}^{n} a_{i j} x_{j}-b_{i}\right)^{2} \\
\text { subject to } & \left(x_{1}, x_{2}, \ldots, x_{n}\right) \in\{0,1\}^{n}
\end{array}
$$

for a sufficiently large $M$.
Management applications. Constraints of the form:

$$
x_{i}=1 \quad \text { if and only if } \quad y=1, \quad i \in A
$$

are encountered in many management applications (e.g., capital budgeting, plant location, tool management problems, etc.; see $[7,16,22])$. Since such constraints simply express that $y=\prod_{i \in A} x_{i}$, pseudo-Boolean formulations of such problems often arise quite naturally by elimination of the $y$-variables.

Game theory. A game in characteristic function form is nothing but a pseudo-Boolean function $f$. If $\left(x_{1}, x_{2}, \ldots, x_{n}\right)$ is the characteristic vector of the set $S$, then $f\left(x_{1}, x_{2}, \ldots, x_{n}\right)$ is interpreted as the payoff that the players indexed in $S$ can secure by acting together. The multilinear representation of $f$ and its continuous extension $f^{c}$ play an interesting role in this context; see e.g. [2] and Section 3 below.

# 1.3 Special classes of pseudo-Boolean functions 

Several authors have investigated special classes of functions with "nice" properties. Let us simply mention here monotonic functions (whose first derivatives - see below - have constant sign on $\{0,1\}^{n}$ ), supermodular functions (whose second derivatives are nonnegative on $\{0,1\}^{n}$ ), polar functions (which have a posiform (2) such that, for every $k$, either $A_{k}=\emptyset$ or $B_{k}=\emptyset$ ), unimodular functions (which are polar up to a switch $x_{i} \leftrightarrow \bar{x}_{i}$ on a subset of variables), (completely) unimodal functions (which have a unique local maximizer in (every face of) $\{0,1\}^{n}$ ), etc. Strongly polynomial combinatorial algorithms for the maximization of supermodular functions have been recently proposed in [20, 21]. Unimodular functions can be maximized by max-flow algorithms [19]. Unimodal and related classes of functions have been introduced in [10], where the applicability of greedy algorithms for their optimization has also been investigated. The recognition problem for all these classes of functions is examined in [5].

## 2 Optimization

Optimization of pseudo-Boolean functions over subsets of $\{0,1\}^{n}$ is also known as nonlinear 0-1 optimization. A survey of this field is presented in [18]. We shall only mention a few fundamental facts, restricting ourselves mostly to the unconstrained case.

### 2.1 Local optima

If $f\left(x_{1}, x_{2}, \ldots, x_{n}\right)$ is a pseudo-Boolean function, let us define its $i$ th derivative $\Delta_{i}$ to be the pseudo-Boolean function

$$
\Delta_{i}=f\left(x_{1}, \ldots, x_{i-1}, 1, x_{i+1}, \ldots, x_{n}\right)-f\left(x_{1}, \ldots, x_{i-1}, 0, x_{i+1}, \ldots, x_{n}\right)
$$

It was shown in [16] that all the local maxima of the function $f$ are characterized by the system of implications:

$$
\text { if } \Delta_{i}>0 \text { then } x_{i}=1, \quad \text { if } \Delta_{i}<0 \text { then } x_{i}=0, \quad \text { for } i=1,2, \ldots, n
$$

Let now $m_{i}$ and $M_{i}$ be arbitrary lower and upper bounds of $\Delta_{i}$, e.g. the sums of the negative, respectively the positive, coefficients in the polynomial representation of $\Delta_{i}$. Then it is clear that an equivalent characterization of the local maxima of the pseudoBoolean function $f$ is given by the system of inequalities

$$
\Delta_{i}-M_{i} x_{i} \quad 0, \Delta_{i}-m_{i} \bar{x}_{i} \geq 0, \quad \text { for } i=1,2, \ldots, n
$$

# 2.2 Global optima 

The continuous extension $f^{c}$ has the attractive feature that its global maximizers are at the vertices of the hypercube $[0,1]^{n}$ and hence, coincide with those of $f$ (this is because (1) is linear in every variable). This implies that continuous global optimization techniques can be applied to $f^{c}$ in order to compute the maximum of $f$. This approach did not prove computationally efficient in past experiments, but remains conceptually valuable. As an amusing corollary, one may note for instance that the optimum of the max-cut function (3) is at least $f^{c}\left(\frac{1}{2}\right)=\frac{1}{2} \sum_{1} i<j n c(i, j)$. Thus, we find that every graph contains a cut of capacity at least equal to one-half the total edge capacity, a well-known result of graph theory. Moreover, such a cut can be found efficiently.
A combinatorial variable elimination algorithm for pseudo-Boolean optimization was proposed by Hammer, Rosenberg and Rudeanu [15, 16]. The following streamlined version and an efficient implementation of this algorithm are described in [8]. Let $f\left(x_{1}, x_{2}, \ldots, x_{n}\right)$ be the function to be maximized. We can write

$$
f\left(x_{1}, x_{2}, \ldots, x_{n}\right)=x_{1} \Delta_{1}\left(x_{2}, x_{3}, \ldots, x_{n}\right)+h\left(x_{2}, x_{3}, \ldots, x_{n}\right)
$$

where $h$ and the first derivative $\Delta_{1}$ do not depend on $x_{1}$. Clearly, there exists a maximizer of $f$, say $\left(x_{1}^{*}, x_{2}^{*}, \ldots, x_{n}^{*}\right)$, with the property that $x_{1}^{*}=1$ if and only if $\Delta_{1}\left(x_{2}^{*}, x_{3}^{*}, \ldots, x_{n}^{*}\right)>$ 0 . This suggests to introduce a function $t\left(x_{2}, x_{3}, \ldots, x_{n}\right)$ such that $t\left(x_{2}, x_{3}, \ldots, x_{n}\right)=$ $\Delta_{1}\left(x_{2}, x_{3}, \ldots, x_{n}\right)$ if $\Delta_{1}\left(x_{2}, x_{3}, \ldots, x_{n}\right)>0$ and $t\left(x_{2}, x_{3}, \ldots, x_{n}\right)=0$ otherwise. Letting $f_{1}=t+h$, we have reduced the maximization of the original function $f$ in $n$ variables to the maximization of $f_{1}$, which only depends on $n-1$ variables. Repeating $n$ times this elimination process eventually allows to determine a maximizer of $f$. An efficient implementation of this algorithm is proposed in [8], where it is also proved that the algorithm runs in polynomial time on pseudo-Boolean functions with bounded tree-width.
Another classical approach consists in transforming the problem $\max \left\{f(X): X \in\{0,1\}^{n}\right\}$ into an equivalent linear $0-1$ programming problem by substituting a variable $y_{k}$ for the $k$ th monomial $T_{k}$ of (1) (or (2)) and setting up a collection of linear constraints which enforce the equality $y_{k}=T_{k}$. The continuous relaxation of this linear formulation yields an easily computable upper-bound on the maximum of $f$. Properties of this upper-bound and of related formulations of $f$ have been investigated in $[1,13]$ and in a series of subsequent paper; see [6] for a brief account and Section 2.3 for related considerations.

### 2.3 Quadratic 0-1 optimization

Quadratic 0-1 optimization is an important special case of pseudo-Boolean optimization, both because numerous applications appear in this form, and because the more general case is easily reduced to it. Indeed, consider a function $f$ of the form (1), assume that $\left|A_{1}\right|>2$ and select $j, l \in A_{1}$. Then, the function
$g\left(x_{1}, x_{2}, \ldots, x_{n}, y\right)=c_{0}+c_{1}\left(\prod_{i \in A_{1} \backslash\{j, l\}} x_{i}\right) y+\sum_{k=2}^{m} c_{k} \prod_{i \in A_{k}} x_{i}-M\left(x_{j} x_{l}-2 x_{j} y-2 x_{l} y+3 y\right)$

where $y$ is a new variable, and $M$ is large enough, has the same maximum value as $f$ ( $y=x_{j} x_{l}$ in every maximizer of $g$ ). Applying recursively this procedure yields eventually a function of degree 2.
Best linear majorants and minorants of pseudo-Boolean functions can provide important information on the function. It was shown in [13] that for any quadratic pseudo-Boolean function $f$, one can construct a linear function

$$
l\left(x_{1}, x_{2}, \ldots, x_{n}\right)=l_{0}+\sum_{j=1}^{n} l_{j} x_{j}
$$

called the roof dual of $f$, majorizing $f\left(x_{1}, x_{2}, \ldots, x_{n}\right)$ in every binary point $\left(x_{1}, x_{2}, \ldots, x_{n}\right)$ and having the following property of strong persistency: if $l_{j}$ is strictly positive (resp. negative), then $x_{j}$ must be equal to 1 (resp. 0 ) in every maximizer of $f$. In other words, roof duality allows the determination of the optimal values of a subset of variables. Moreover, $\max \left\{f(X): X \in\{0,1\}^{n}\right\}=\max \left\{l(X): X \in\{0,1\}^{n}\right\}$ if and only if an associated 2-SAT problem is satisfiable. While the determination of the roof dual in [13] was accomplished via linear programming, it was shown later [3] that this problem can be reduced to a maxflow problem in an associated network.

# 3 Linear approximations 

In order to find the best linear approximation $L(f)$ of a pseudo-Boolean function $f$ in the norm $L_{2}$, it is sufficient to know how to determine the best linear $L_{2}$-approximation of a monomial. Indeed, considering the polynomial representation (1), it is clear that

$$
L(f)=c_{0}+\sum_{k=1}^{m} c_{k} L\left(\prod_{i \in A_{k}} x_{i}\right)
$$

On the other hand, it was shown in [14] that

$$
L\left(\prod_{i \in A} x_{i}\right)=\frac{1}{2^{|A|}}\left(1-|A|+2 \sum_{i \in A} x_{i}\right) \quad \text { for all } A \subseteq N
$$

It was shown in the same paper that the best quadratic, cubic,... $L_{2}$-approximations can also be obtained by similar simple closed formulas.
Important game-theoretical applications of best $L_{2}$-approximations consist in finding the Banzhaf indices of the players of a simple game, or the Shapley values of the players of an $n$-person characteristic function game. Indeed, as shown in [14], these indices are simply the coefficients of best (weighted) linear $L_{2}$-approximations of pseudo-Boolean functions describing these games.
Another important application of these results allows the efficient determination of excellent heuristic solutions of unconstrained nonlinear binary optimization problems [9].

Acknowledgements. This work was partially supported by ONR grants N00014-92-J1375 and N00014-92-J-4083, by NSF grant DMS-9806389, and by research grants from the Natural Sciences and Engineering Research Council of Canada (NSERC).
