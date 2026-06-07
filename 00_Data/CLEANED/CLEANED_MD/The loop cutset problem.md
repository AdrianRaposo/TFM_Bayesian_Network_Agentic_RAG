# Approximation Algorithms for the Loop Cutset Problem 

Ann Becker and Dan Geiger<br>Computer Science Department<br>Technion<br>Haifa 32000, ISRAEL<br>anyuta@cs.technion.ac.il, dang@cs.technion.ac.il


#### Abstract

We show how to find a small loop cutset in a Bayesian network. Finding such a loop cutset is the first step in the method of conditioning for inference. Our algorithm for finding a loop cutset, called MGA, finds a loop cutset which is guaranteed in the worst case to contain less than twice the number of variables contained in a minimum loop cutset. We test MGA on randomly generated graphs and find that the average ratio between the number of instances associated with the algorithms' output and the number of instances associated with a minimum solution is 1.22 .


## 1 Introduction

Most inference algorithms for the computation of a posterior probability in general Bayesian networks have two conceptual phases. One phase handles operations on the graphical structure itself and the other performs probabilistic computations. For example, the clique tree algorithm requires us to first find a "good" clique tree and then perform probabilistic computations on the clique tree [LS88]. Pearl's method of conditioning requires us first to find a "good" loop cutset and then perform a calculation for each loop cutset [Pe86, Pe88]. Finally, Shachter's algorithm requires us to find a "good" sequence of transformations and then, for each transformation, to compute some conditional probability tables [Sh86].
In the three algorithms just mentioned the first phase is to find a good discrete structure, namely, a clique tree, a cutset, or a sequence of transformations. The goodness of the structure depends on a chosen parameter that, if selected appropriately, reduces the probabilistic computations done in the second phase. Finding a structure that optimizes the selected parameter is usually NP-hard and thus heuristic methods are applied to find a reasonable structure. Most methods in the past had no guarantee of performance and performed very badly when presented with an appropriate
example. For example, the greedy algorithms of [St90] and [SC90] for the method of conditioning may in the worst case perform as bad as a factor of $n / 4$ where $n$ is the number of variables in a Bayesian network. That is to say, the size of their solution instead of being 2 variables may include as many as $n / 2$ variables-a disastrous outcome. Similar situations occur with other inference algorithms.
However, recently, among other results, Bar-Yehuda et al. (1994) have developed an algorithm that finds a loop cutset that is guaranteed in the worst case to contain less than 4 times the number of variables contained by a minimum loop cutset. This guarantee is given only when the number of values of every variable in the network is the same. Note that this result means that the number of instances associated with a loop cutset $F$ found by their algorithm (e.g., $r^{|F|}$ if the number of values of every variable is $r$ ) is no more than the number of instances associated with a minimum loop cutset raised to the forth power. Note also that, the problem of finding a minimum loop cutset was shown to be NP-hard in [SC90].
Our paper offers a new algorithm for finding a loop cutset, called MGA, that finds a loop cutset which is guaranteed in the worst case to contain less than twice the number of variables contained in an optimal loop cutset. That is, the number of instances associated with a loop cutset found by our algorithm is no more than the number of instances associated with an optimal loop cutset raised to the second power. The complexity of MGA is $O(m+n \log n)$ where $m$ and $n$ are the number of edges and vertices respectively. Unlike [BGNR94], our result holds even when the arities of the variables are arbitrary. Like [BGNR94], our solution is based on a reduction to the Weighted Vertex Feedback Set Problem, defined in the next section. We should emphasize that all these performance guarantees are for the worst case.
In Section 4 we test MGA on randomly generated graphs and find that the average ratio between the number of instances associated with the algorithms' output and the number of instances associated with a minimum solution is 1.22 .

From a theoretical point of view, Bar-Yehuda et. al. (1994) note that as the number of variables grows to infinity the worst case ratio between the size of a loop cutset found by any polynomial algorithm and the size of an optimal loop cutset cannot be less than two unless the unlikely event that a similar result is obtained for the weighted vertex cover problem (WVC) ${ }^{1}$. Consequently, we conjecture that no polynomial algorithm for the loop cutset problem performs better in the worst case than the algorithm presented in this paper as graphs grow to infinity in size.
The rest of the paper is organized as follows. In Section 2 we outline the method of conditioning, explain the related loop cutset problem and describe the reduction from the loop cutset problem to the Weighted Vertex Feedback Set (WVFS) Problem. In Section 3 we provide two approximation algorithms for the WVFS problem which is by itself an NP-Complete problem [GJ79, pp. 191-192]. Finally, in Section 4 we present experiments that test the average performance of our algorithms.

## 2 The Loop Cutset Problem

Pearl's method of conditioning is one of the known inference methods for Bayesian networks. A short overview of the method of conditioning and definitions of Bayesian networks are needed. The reader is referred to [Pe88] for more details.
Let $P\left(u_{1}, \ldots, u_{n}\right)$ be a probability distribution where each $u_{i}$ draws values from a finite set called the domain of $u_{i}$. A directed graph $D$ with no directed cycles is called a Bayesian network of $P$ if there is a 1-1 mapping between $\left\{u_{1}, \ldots, u_{n}\right\}$ and vertices in $D$, such that $u_{i}$ is associated with vertex $i$ and $P$ can be written as follows:

$$
P\left(u_{1}, \ldots, u_{n}\right)=\prod_{i=1}^{n} P\left(u_{i} \mid u_{i_{1}}, \ldots, u_{i_{j(i)}}\right)
$$

where $i_{1}, \ldots, i_{j(i)}$ are the source vertices of the incoming edges to vertex $i$ in $D$.
Suppose now that some variables $\left\{v_{1}, \ldots, v_{l}\right\}$ among $\left\{u_{1}, \ldots, u_{n}\right\}$ are assigned specific values $\left\{\mathbf{v}_{1}, \ldots, \mathbf{v}_{l}\right\}$ respectively. The updating problem is to compute the probability $P\left(u_{i} \mid v_{1}=v_{1}, \ldots, v_{l}=v_{i}\right)$ for $i=1, \ldots, n$.
A trail in a Bayesian network is a subgraph whose underlying graph is a simple path. A vertex $b$ is called a sink with respect to a trail $t$ if there exist two consecutive edges $a \rightarrow b$ and $b \leftarrow c$ on $t$. A trail $t$ is active by a set of vertices $Z$ if (1) every sink with respect to $t$ either is in $Z$ or has a descendant in $Z$ and (2) every other vertex along $t$ is outside $Z$. Otherwise, the trail is said to be blocked (d-separated) by $Z$.

[^0]Verma and Pearl [VP88] have proved that if $D$ is a Bayesian network of $P\left(u_{1}, \ldots, u_{n}\right)$ and all trails between a vertex in $\left\{r_{1}, \ldots, r_{l}\right\}$ and a vertex in $\left\{s_{1}, \ldots, s_{k}\right\}$ are blocked by $\left\{t_{1}, \ldots, t_{m}\right\}$, then the corresponding sets of variables $\left\{u_{r_{1}}, \ldots, u_{r_{l}}\right\}$ and $\left\{u_{s_{1}}, \ldots, u_{s_{k}}\right\}$ are independent conditioned on $\left\{u_{t_{1}}, \ldots, u_{t_{m}}\right\}$. Furthermore, Geiger and Pearl [GP90] proved a converse to this theorem. Both results are presented and extended in [GVP90].
Using the close relationship between blocked trails and conditional independence, Kim and Pearl [KP83] developed an algorithm update-tREE that solves the updating problem on Bayesian networks in which every two vertices are connected with at most one trail (singly-connected). Pearl then solved the updating problem on any Bayesian network as follows [Pe86]. First, a set of vertices $S$ is selected such that any two vertices in the network are connected by at most one active trail in $S \cup Z$, where $Z$ is any subset of vertices. Then, update-tree is applied once for each combination of value assignments to the variables corresponding to $S$, and, finally, the results are combined. This algorithm is called the method of conditioning and its complexity grows exponentially with the size of $S$. The set $S$ is called a loop cutset. Note that when the domain size of the variables varies, then UpdatETREE is called a number of times equal to the product of the domain sizes of the variables whose corresponding vertices participate in the loop cutset. If we take the logarithm of the domain size (number of values) as the weight of a vertex, then finding a loop cutset such that the sum of its vertices weights is minimum optimizes Pearl's updating algorithm in the case where the domain sizes may vary.
We now give an alternative definition for a loop cutset $S$ and then provide an approximation algorithm for finding it. This definition is borrowed from [BGNR94]. The underlying graph $G$ of a directed graph $D$ is the undirected graph formed by ignoring the directions of the edges in $D$. A cycle in $G$ is a path whose two terminal vertices coincide. A loop in $D$ is a subgraph of $D$ whose underlying graph is a cycle. A vertex $v$ is a sink with respect to a loop $\Gamma$ if the two edges adjacent to $v$ in $\Gamma$ are directed into $v$. Every loop must contain at least one vertex that is not a sink with respect to that loop. Each vertex that is not a sink with respect to a loop $\Gamma$ is called an allowed vertex with respect to $\Gamma$. A loop cutset of a directed graph $D$ is a set of vertices that contains at least one allowed vertex with respect to each loop in $D$. The weight of a set of vertices $X$ is denoted by $w(X)$ and is equal to $\sum_{v \in X} w(v)$ where $w(x)=\log (|x|)$ and $|x|$ is the size of the domain associated with vertex $x$. A minimum loop cutset of a weighted directed graph $D$ is a loop cutset $F^{*}$ of $D$ for which $w\left(F^{*}\right)$ is minimum over all loop cutsets of $G$. The Loop Cutset Problem is defined as finding a minimum loop cutset of a given weighted directed graph $D$.
The approach we take is to reduce the weighted loop


[^0]:    ${ }^{1}$ The WVC problem is finding a set of vertices that contains an endpoint of every edge in a given undirected graph and which has a minimum weight among all such sets.

cutset problem to the weighted vertex feedback set problem, as done by [BGNR94]. We now define the weighted vertex feedback set problem and then the reduction.

Let $G=(V, E)$ be an undirected graph, and let $w$ : $V \rightarrow \mathbb{R}^{+}$be a weight function on the vertices of $G$. A vertex feedback set of $G$ is a subset of vertices $F \subseteq V$ such that each cycle in $G$ passes through at least one vertex in $F$. In other words, a vertex feedback set $F$ is a set of vertices of $G$ such that by removing $F$ from $G$, along with all the edges incident with $F$, we obtain a set of trees (i.e., a forest). The weight of a set of vertices $X$ is denoted (as before) by $w(X)$ and is equal to $\sum_{v \in X} w(v)$. A minimum vertex feedback set of a weighted graph $G$ with a weight function $w$ is a vertex feedback set $F^{*}$ of $G$ for which $w\left(F^{*}\right)$ is minimumover all vertex feedback sets of $G$. The Weighted Vertex Feedback Set (WVFS) Problem is defined as finding a minimum vertex feedback set of a given weighted graph $G$ having a weight function $w$. Application of this problem for constraint satisfaction is described in [DP90].
In the next section we offer an algorithm, called MGA, for approximately solving the weighted vertex feedback set problem. The algorithm is guaranteed to output a weighted vertex set whose weight is less than twice the optimal weight.
The reduction is as follows. Given a weighted directed graph $(D, w)$ (e.g., a Bayesian network), we define the splitting weighted undirected graph $D_{s}$ with a weight function $w_{s}$ as follows. Split each vertex $v$ in $D$ into two vertices $v_{\text {in }}$ and $v_{\text {out }}$ in $D_{s}$ such that all incoming edges to $v$ in $D$ become undirected incident edges with $v_{\text {in }}$ in $D_{s}$, and all outgoing edges from $v$ in $D$ become undirected incident edges with $v_{\text {out }}$ in $D_{s}$. In addition, connect $v_{\text {in }}$ and $v_{\text {out }}$ in $D_{s}$ by an undirected edge. Now set $w_{s}\left(v_{\text {in }}\right)=\infty$ and $w_{s}\left(v_{\text {out }}\right)=w(v)$. For a set of vertices $X$ in $D_{s}$, we define $\psi(X)$ as the set obtained by replacing each vertex $v_{\text {in }}$ or $v_{\text {out }}$ in $X$ by the respective vertex $v$ in $D$ from which these vertices originated.
Our algorithm can now be easily stated.

## Algorithm LC

Input: A Bayesian network D;
Output: A loop cutset of $D$;

1. Construct the splitting graph $D_{s}$ with weight function $w_{s}$;
2. Apply MGA on $\left(D_{s}, w_{s}\right)$ to obtain a vertex feedback set $F$;
3. Output $\psi(F)$.

It is immediately seen that if MGA outputs a vertex feedback set $F$ whose weight is no more than twice the
weight of a minimum vertex feedback set of $D_{s}$, then $\psi(F)$ is a loop cutset of $D$ with weight no more than twice the weight of a minimum loop cutset of $D$. This observation holds because there is an obvious one-toone and onto correspondence between loops in $D$ and cycles in $D_{s}$ and because MGA never chooses a vertex that has an infinite weight.

## 3 Algorithms For The WVFS problem

Recall that the weighted vertex feedback set problem is defined as finding a minimum vertex feedback set of a given weighted graph $G$.

### 3.1 The Greedy Algorithm

We first analyze the simplest of all approximation algorithms for the weighted vertex feedback set problemthe greedy algorithm. Assume we are given a weighted undirected graph $G$ with a weight function $w$. The greedy algorithm starts with $G$ after removing all vertices with degree 0 or 1 and repeatedly chooses to insert a vertex $v$ into the constructed vertex feedback set if the ratio between $v$ 's weight $w(v)$ and $v$ 's degree $d(v)$ in the current graph is minimal across all vertices in the current graph. When $v$ is selected, it is removed from the current graph and then all vertices with degree 0 or 1 are repeatedly removed as well. This step is repeated until the graph is exhausted.
This algorithm and parts of its analysis are influenced by the work of Chvatal (1979) who analyzed the greedy algorithm for the Weighted Set Cover problem (WSC) and by Lovász (1975) and Johnson (1974) who analyzed the unweighted version of this problem.

## ALGORITHM GA

Input: A weighted undirected graph $G(V, E, w)$.
Output: A vertex feedback set $F$.
$F \leftarrow \emptyset$
$i-1$
Repeatedly remove all vertices with degree 0 or 1 from $V$ and insert the resulting graph into $G_{i}$
While $G_{i}$ is not the empty graph do

1. Pick a vertex $v_{i}$ for which $\frac{w\left(v_{i}\right)}{d\left(v_{i}\right)}$ is minimum in $G_{i}$
2. $F \leftarrow F \cup\left\{v_{i}\right\}$
3. $V \leftarrow V \backslash\left\{v_{i}\right\}$
$4 . i-i+1$
4. Repeatedly remove all vertices with degree 0 or 1 from $V$ and insert the resulting graph into $G_{i}$
end.
In the rest of this section we prove that the performance ratio of this greedy algorithm is bounded by $2(\log d+1)$ where $d=\max _{v \in V} d(v)$ is the degree of the

graph. Recall that the performance ratio of an approximation algorithm is the worst case ratio between the weight of the algorithm's output and the weight of an optimal solution. In Section 4, we show experimentally that even this simple algorithm when combined with the reduction algorithm LC convincingly outperforms the algorithms given by [SC90, St90].
Let $F^{*}$ be an optimal weighted feedback set of $G(V, E, w)$ and let $\bar{F}=V \backslash F^{*}$. Note that the vertices in $F$ (the output of GA) are denoted by $\left\{v_{1}, v_{2}, \ldots, v_{t}\right\}$ where $v_{i}$ are indexed in the order in which they are inserted into $F$ by GA and where $t=|F|$. Let $d_{i}(v)$ denote the degree of vertex $v$ in $G_{i}$-the graph generated in iteration $i$ of GA-and let $V_{t}$ be the set of vertices of $G_{i}$. An edge is covered by the algorithm if for some $i=1, \ldots, t$, one of its endpoints is $v_{i}$ and the edge exists in $G_{i}$. Let $\Gamma_{1}(v)$ denote the set of edges in $G_{1}$ for which at least one endpoint is $v$. Note that the set of vertex feedback sets of $G$ and $G_{1}$ is the same and that the degree of every vertex in $G_{1}$ is smaller or equal to the degree of that vertex in $G$.
Let $c_{i}=w\left(v_{i}\right) / d_{i}\left(v_{i}\right)$ and let $C(e)=c_{i}$ for every edge $e$ removed at iteration $i$. Note that for every $j \leq i$ we have $w\left(v_{j}\right) / d_{j}\left(v_{j}\right) \leq w\left(v_{i}\right) / d_{j}\left(v_{i}\right)$ because vertices are selected in decreasing order of these ratios. Also note that for $j \leq i, d_{j}\left(v_{i}\right) \geq d_{i}\left(v_{i}\right)$ since the algorithm never adds edges. Thus,

$$
c_{j} \equiv w\left(v_{j}\right) / d_{j}\left(v_{j}\right) \leq w\left(v_{i}\right) / d_{i}\left(v_{i}\right) \equiv c_{i}
$$

for $1 \leq j \leq i \leq|F|$, as originally claimed by [Ch79] in the context of the WSC problem.
To analyze the performance ratio we use a lemma that bounds the number of edges in $G_{i}$ covered by the algorithm until its termination. We need the following definitions. Let $d_{X}(v)$ be the number of edges whose one endpoint is $v$ and the other is a vertex in $X$. Denote $F_{i}^{*}=F^{*} \cap V_{i}$ and $\bar{F}_{i}^{*}=\bar{F} \cap V_{i}$. A linkpoint is a vertex that has a degree 2 and A branchpoint is a vertex that has a degree larger than 2. (A self-loop adds 2 to the degree of a vertex).

## Lemma 1

$$
\sum_{j=i}^{t} d_{j}\left(v_{j}\right) \leq 2 \sum_{v \in F_{i}^{*}} d_{i}(v)
$$

Proof: We will actually prove that,

$$
\sum_{j=i}^{t} d_{j}\left(v_{j}\right) \leq \sum_{v \in V_{i}}\left(d_{i}(v)-2\right)+2\left|F_{i}^{*}\right| \leq 2 \sum_{v \in F_{i}^{*}} d_{i}(v)
$$

According to our notations, $\sum_{v \in V_{i}}\left(d_{i}(v)-2\right)$ equals

$$
\sum_{v \in \bar{F}_{i}^{*}}\left(d_{\bar{F}_{i}^{*}}(v)-2\right)+\sum_{v \in \bar{F}_{i}^{*}} d_{F_{i}^{*}}(v)+\sum_{v \in F_{i}^{*}}\left(d_{i}(v)-2\right)
$$

Furthermore, the graph induced by $\bar{F}_{i}^{*}$ is a forest and since the number of edges in a forest is smaller
(or equal) than the number of vertices, we have, $\sum_{v \in \bar{F}_{i}^{*}} d_{\bar{F}_{i}^{*}}(v) / 2 \leq\left|\bar{F}_{i}^{*}\right|$. Thus $\sum_{v \in \bar{F}_{i}^{*}}\left(d_{\bar{F}_{i}^{*}}(v)-2\right) \leq$ 0 . Consequently, $\sum_{v \in V_{i}}\left(d_{i}(v)-2\right)+2\left|F_{i}^{*}\right|$ is less than or equal to

$$
\sum_{v \in \bar{F}_{i}^{*}} d_{\bar{F}_{i}^{*}}(v)+\sum_{v \in \bar{F}_{i}^{*}} d_{i}(v) \leq 2 \sum_{v \in \bar{F}_{i}^{*}} d_{i}(v)
$$

The proof of the first part of Eq. 4 is constructive. We repeatedly apply the following procedure on $G_{i}$ selecting in each step a vertex $v_{j} \in F_{i}$ and showing that there are terms in the right hand side (RHS) of Eq. 4 that contribute $d_{j}\left(v_{j}\right)$ to the RHS and have not been used for any other $v \in F_{i}$. Set $H=G_{i}$ and for $k=i \ldots t$ do as follows:
Pick the vertex $v_{k}$. If $v_{k}$ is a linkpoint in $H$ then follow the two paths $p_{1}$ and $p_{2}$ in $H$ emanating from $v_{k}$ until the first branchpoint on each side is found. There are three cases to consider. Either two distinct branchpoints $b_{1}$ and $b_{2}$ are found, one branchpoint $b_{1}$ (in which case $p_{1}$ and $p_{2}$ define a cycle) or none (if the cycle is isolated). In the first case the two edges on $p_{1}$ and $p_{2}$ whose endpoints are $b_{1}$ and $b_{2}$, respectively, are associated with the terms $d_{k}\left(b_{1}\right)-2>0$ and $d_{k}\left(b_{2}\right)-2>0$ in the RHS and so each of these terms contributes 1 to the sum $\sum_{v \in V_{i}}\left(d_{i}(v)-2\right)$. In the second case, similarly, the two edges on $p_{1}$ and $p_{2}$ whose endpoints is $b_{1}$ are associated with the term $d_{k}\left(b_{1}\right)-2>0$ and so, if $d_{k}\left(b_{1}\right)>3$, this term contributes 2 to the sum $\sum_{v \in V_{i}}\left(d_{i}(v)-2\right)$. If $d_{k}\left(b_{1}\right)=3$ we continue to follow the third path from $b_{1}$ (i.c., not $p_{1}$ or $p_{2}$ ) until another branchpoint $b_{2}$ is found and the last edge on that path is associated with $d_{k}\left(b_{2}\right)-2$ which contributes the extra missing 1 to the RHS. Finally, if no branchpoint is found, then on the cycle in which $v_{k}$ resides there must exist a vertex from $F_{i}^{*}$ that resides on no other cycles of $H$. Now, if $v_{k}$ is a branchpoint, then the term $d_{k}\left(v_{k}\right)-2$ appears in both sides of the inequality. In this case, sequentially remove $d_{k}\left(v_{k}\right)-2$ of the $d_{k}\left(v_{k}\right)$ edges adjacent to $v_{k}$ such that after each removal the vertices with degree 0 or 1 are removed from $H$ as well. Thus, $v_{k}$ remains a linkpoint in which case the procedure for a linkpoint is applied. Finally, remove $v_{k}$, and repeatedly remove all the vertices with degree 0 or 1 from $H$. Repeat until $F_{i}$ is exhausted. $\square$
We now show that $w(F) \leq 2 \cdot(\log d+1) \cdot w\left(F^{*}\right)$.

$$
\begin{gathered}
w(F)=\sum_{i=1}^{t} w\left(v_{i}\right)=\sum_{i=1}^{t} c_{i} \cdot d_{i}\left(v_{i}\right)= \\
c_{1} \sum_{i=1}^{t} d_{i}\left(v_{i}\right)+\sum_{i=2}^{t}\left(c_{i}-c_{i-1}\right) \sum_{j=i}^{t} d_{j}\left(v_{j}\right)
\end{gathered}
$$

Since $c_{i} \geq c_{i-1}$, we can apply Eq. 3 and so,
$w(F) \leq 2 c_{1} \sum_{v \in F_{i}^{*}} d_{1}(v)+\sum_{i=2}^{t} 2\left(c_{i}-c_{i-1}\right) \sum_{v \in F_{i}^{*}} d_{i}(v)=$

$$
\sum_{i=1}^{t} 2 c_{i} \sum_{v \in F_{i}^{*}} d_{i}(v)-\sum_{i=1}^{t-1} 2 c_{i} \sum_{v \in F_{i+1}^{*}} d_{i+1}(v)
$$

Thus,

$$
\begin{aligned}
& w(F) \leq \sum_{i=1}^{t} 2 c_{i} \sum_{v \in F_{i}^{*} \backslash F_{i+1}^{*}} d_{i}(v)+ \\
& \sum_{i=1}^{t} 2 c_{i} \sum_{v \in F_{i+1}^{*}} d_{i}(v)-\sum_{i=1}^{t-1} 2 c_{i} \sum_{v \in F_{i+1}^{*}} d_{i+1}(v)= \\
& 2\left(\sum_{i=1}^{t-1}\left(c_{i} \sum_{v \in F_{i}^{*} \backslash F_{i+1}^{*}} d_{i}(v)+c_{i} \sum_{v \in F_{i+1}^{*}}\left(d_{i}(v)-d_{i+1}(v)\right)\right)\right. \\
& \left.+c_{1} \sum_{v \in F_{i}^{*}} d_{1}(v)\right)
\end{aligned}
$$

However, since the last sum on the right hand side merely counts the edge weights according to the iteration they are assigned a weight, we get,

$$
w(F) \leq 2 \sum_{v \in F^{*}} \sum_{e \in \Gamma_{1}(v)} C(e)
$$

Now, for every $v \in F^{*}$,

$$
H(d(v)) \cdot w(v) \geq \sum_{e \in \Gamma_{1}(v)} C(e)
$$

where $H(m)=\sum_{i=1}^{m} 1 / i$, as shown in [Ch79] using the following argument. Let $s$ be the largest superscript such that $d_{s}(v)>0$ then

$$
\begin{aligned}
\sum_{e \in \Gamma_{1}(v)} C(e) & =\sum_{i=1}^{s}\left(d_{i}(v)-d_{i+1}(v)\right) \cdot\left(w\left(v_{i}\right) / d_{i}\left(v_{i}\right)\right) \\
& \leq w(v) \sum_{i=1}^{s}\left(d_{i}(v)-d_{i+1}(v)\right) / d_{i}(v)
\end{aligned}
$$

where the inequality is due to Eq. 2. Furthermore, by induction,

$$
\sum_{e \in \Gamma_{1}(v)} C(e) \leq w(v) \sum_{i=1}^{s}\left[H\left(d_{i}(v)\right)-H\left(d_{i+1}(v)\right)\right]
$$

Since the right hand side is equal to $w(v) \cdot H(d(v))$, Eq. 7 follows. Combining Eqs. 6, and 7 yields,

$$
w(F) \leq 2 \sum_{v \in F^{*}} H(d(v)) \cdot w(v) \leq 2 H(d) \cdot w\left(F^{*}\right)
$$

Thus, since $H(d) \leq \log d+1$ (equality holds only when $d=1$ ).

Theorem 2 The performance ratio of GA is bounded by $2(\log d+1)$.

We have an example in which the ratio between GA's output and the optimal output is $2 \log d$. Our example is similar to the example for the vertex cover problem given in [Mo92, pp. 47]. Consequently, the upper bound given in Theorem 2 is rather tight.

### 3.2 The Modified Greedy Algorithm

We now present a modified greedy algorithm, called MGA, whose performance ratio is bounded by the constant 2. The changes we introduce into the greedy algorithm are quite minor and so it is interesting that such a vast improvement in the performance ratio is obtained. A similar phenomenon is reported in the context of the weighted vertex cover problem [CI83].
MGA has two phases. In the first phase MGA repeatedly chooses to insert a vertex $v$ into the constructed vertex feedback set if the ratio between $v$ 's weight $w(v)$ and $v$ 's degree $d(v)$ in the current graph is minimal across all vertices in the current graph. When $v$ is selected, it is removed from the current graph and then all vertices with degree 0 or 1 are repeatedly removed as well. For every edge removed in this process, a weight of $w(v) / d(v)$ is subtracted from its endpoint vertices. These steps are repeated until the graph is exhausted. The only difference between this phase and the plain greedy algorithm is the revision of some weights in each step instead of just revising the current degrees. The second phase removes redundant vertices from the constructed vertex feedback set.

## ALGORITHM MGA

Input: A weighted undirected graph $G(V, E, w)$.
Output: A vertex feedback set $F$.
$F^{\prime} \leftarrow \emptyset$
$i \leftarrow 1$
Repeatedly remove all vertices with degree 0 or 1 from $V$ and their adjacent edges from $E$ and insert the resulting graph into $G_{i}$.
While $G_{i}$ is not the empty graph do

1. Pick a vertex $v_{i}$ for which
$\frac{w\left(v_{i}\right)}{d\left(v_{i}\right)}$ is minimum in $G_{i}$
2. $F^{\prime} \leftarrow F^{\prime} \cup\left\{v_{i}\right\}$
3. $V \leftarrow V \backslash\left\{v_{i}\right\}$
4. $i \leftarrow i+1$
5. Repeatedly remove all vertices with degree 0 or 1 from $V$ and their adjacent edges from $E$ and insert the resulting graph into $G_{i}$.
For every edge $e=\left(u_{1}, u_{2}\right)$ removed in this process do

$$
\begin{aligned}
& C(e) \leftarrow \frac{w\left(v_{1}\right)}{d\left(v_{1}\right)} \\
& w\left(u_{1}\right) \leftarrow w\left(u_{1}\right)-C(e) \\
& w\left(u_{2}\right) \leftarrow w\left(u_{2}\right)-C(e)
\end{aligned}
$$

end
$F \leftarrow F^{\prime}$
For $i=|F|$ to 1 do \{Phase 2\}
If every cycle in $G_{i}$ that intersects with $\left\{v_{i}\right\}$ also intersects with $F \backslash\left\{v_{i}\right\}$ then,
$F \leftarrow F \backslash\left\{v_{i}\right\}$
endfor
end

Clearly $F^{\prime}$ computed at the first phase of MGA is a vertex feedback set of $G$ and $F$ created from $F^{\prime}$ by removing all redundant vertices is a minimal vertex feedback set of $G$, that is, if a vertex is removed from $F$, then $F$ ceases to be a vertex feedback set of $G$. Furthermore, as a result of removing redundant vertices the inequality $\sum_{j=1}^{t} d_{j}\left(v_{j}\right) \leq 2 \sum_{v \in F_{i}^{*}} d_{i}(v)$ (Eq. 3), proven to hold for the greedy algorithm becomes,

$$
\sum_{v \in F_{i}} d_{i}(v) \leq 2 \sum_{v \in F_{i}^{*}} d_{i}(v)
$$

where $F_{i}^{*}$ are the vertices in $F$ that appear in graph $G_{i}$. The proof of this equation is postponed to Section 3.3. From the description of the algorithm we have for every vertex $v$ in $G_{1}$,

$$
\sum_{e \in \Gamma_{1}(v)} C(e) \leq w(v)
$$

and if $v \in F$ equality must hold. Eq. 9 replaces the inequality $\sum_{e \in \Gamma_{1}(v)} C(e) \leq H(d(v)) \cdot w(v)$ (Eq. 7) proven for the greedy algorithm. By analogy with the previous section and using similar lines of reasoning, it is clear that Eqs. 8 and 9 which replace Eqs. 3 and 7 show that the bound on the performance ratio drops from $2 \cdot H(d)$ for the greedy algorithm to 2 for the modified greedy algorithm.

Theorem 3 Algorithm MGA always outputs a vertex feedback set whose weight is no more than twice the weight of the optimal vertex feedback set.

Proof. As in Section 3.1, $F^{*}$ denotes a minimum feedback set of $G(V, E, w)$ and $\bar{F}^{*}=V \backslash F^{*}$. Recall that the vertices in the constructed set $F^{\prime}$ are $\left\{v_{1}, v_{2}, \ldots, v_{t}\right\}$ where $v_{i}$ are indexed in the order in which they are inserted into $F$ by MGA and $t=\left|F^{\prime}\right|$. Also, $w_{i}(v)$ and $d_{i}(v)$ denote the weight and degree, respectively, of vertex $v$ in $G_{i}$-the graph generated in iteration $i$ of Step 5 of MGA-and $V_{i}$ denotes the set of vertices of $G_{i}$.
As in the greedy algorithm, for every $j \leq i$ we have $w_{j}\left(v_{j}\right) / d_{j}\left(v_{j}\right) \leq w_{j}\left(v_{i}\right) / d_{j}\left(v_{i}\right)$ and also $w_{j}\left(v_{i}\right) / d_{j}\left(v_{i}\right) \leq w_{i}\left(v_{i}\right) / d_{i}\left(v_{i}\right)$ due to the way that the current weights and degrees are updated in the algorithm. Thus,

$$
c_{j} \equiv w_{j}\left(v_{j}\right) / d_{j}\left(v_{j}\right) \leq w_{i}\left(v_{i}\right) / d_{i}\left(v_{i}\right) \equiv c_{i}
$$

for $1 \leq j \leq i \leq\left|F^{\prime}\right|$.
We also have,

$$
\sum_{e \in \Gamma_{1}\left(v_{i}\right)} C(e)=c_{i} \cdot d_{i}\left(v_{i}\right)+\sum_{j=1}^{i-1} c_{j} \cdot\left(d_{j}\left(v_{i}\right)-d_{j+1}\left(v_{i}\right)\right)
$$

because the right hand side simply groups edges according to the iteration in which they are assigned a weight.

Let $\alpha_{i}=1$ if $v_{i} \in F$ and $\alpha_{i}=0$ if $v_{i} \notin F$. That is, $\alpha_{i}$ is 1 if $v_{i}$ is not removed from $F$ in the final stage of MGA and 0 otherwise. We now prove that $w(F) \leq 2 \cdot w\left(F^{*}\right)$.

$$
w(F)=\sum_{i=1}^{t} \alpha_{i} \cdot w\left(v_{i}\right)=\sum_{i=1}^{t} \alpha_{i} \sum_{e \in \Gamma_{1}\left(v_{i}\right)} C(e)
$$

Now, due to Eq. 11, $w(F)$ is equal to

$$
\sum_{i=1}^{t} \alpha_{i} \cdot\left[c_{i} \cdot d_{i}\left(v_{i}\right)+\sum_{j=1}^{i-1} c_{j} \cdot\left(d_{j}\left(v_{i}\right)-d_{j+1}\left(v_{i}\right)\right)\right]
$$

which in turn equals to

$$
c_{1} \sum_{i=1}^{t} \alpha_{i} \cdot d_{1}\left(v_{i}\right)+\sum_{i=2}^{t}\left(c_{i}-c_{i-1}\right) \sum_{j=i}^{t} \alpha_{j} \cdot d_{i}\left(v_{j}\right)
$$

Furthermore,

$$
\sum_{j=i}^{t} \alpha_{j} \cdot d_{i}\left(v_{j}\right)=\sum_{v \in F_{i}} d_{i}(v) \leq 2 \sum_{v \in F_{i}^{*}} d_{i}(v)
$$

Since $c_{i} \geq c_{i-1}$, we can apply Eq. 12 and so, analogously to the derivation of Eq. 6 , we get,

$$
\begin{aligned}
& w(F) \leq \\
& 2 c_{1} \sum_{v \in F_{i}^{*}} d_{1}(v)+\sum_{i=2}^{t} 2\left(c_{i}-c_{i-1}\right) \sum_{v \in F_{i}^{*}} d_{i}(v) \leq \\
& 2 \sum_{v \in F^{*}} \sum_{e \in \Gamma_{1}(v)} C(e)
\end{aligned}
$$

Now, Eqs. 9 and 13 yield the claimed inequality, $w(F) \leq 2 \sum_{v \in F^{*}} w(v)=2 w\left(F^{*}\right) . \square$
The complexity of the first phase of MGA is $O(|E|+$ $|V| \log |V|)$ using a Fibonacci heap (e.g., [FT87]) because finding and deleting a vertex with minimum ratio $w(v) / d(v)$ from the heap is done $|V|$ times at the cost of $O(\log |V|)$ and decreasing a weight from a vertex in the heap is done $|E|$ times at an amortized cost of $O(1)$. The complexity of the second phase of MGA is also is $O(|E|+|V| \log |V|)$ using a simple implementation of the union-find algorithm because we need to do at most $|V|$ union operations at an amortized cost of $O(\log |V|)$ and at most $|E|$ find operations at the cost of $O(1)$ [CLR90, pp. 445].
Interestingly, if the second phase is removed from MGA (making MGA even closer to GA), then it can be shown that the performance ratio becomes 4 rather than 2. Hence the vast improvement in the worstcase performance of MGA compared to GA stems from changing the vertices' weights in each step rather than from removing redundant vertices.

### 3.3 A Theorem about Minimal Vertex Feedback Sets

In this section we prove Eq. 8 which has been used in the analysis of the modified greedy algorithm. Let

$G$ be a weighted graph for which every vertex has a degree strictly greater than $1, F$ be a minimal vertex feedback set of $G$ and $F^{*}$ be an arbitrary vertex feedback set of $G$ (possibly a minimum weight vertex feedback set). Let $d(v)$ be the degree of vertex $v$ and $d_{X}(v)$ be the number of edges whose one endpoint is $v$ and the other is in a set of vertices $X$.

Theorem 4 Let $G, F$ and $F^{*}$ be defined as above. Then, $\sum_{v \in F} d(v) \leq 2 \sum_{v \in F^{*}} d(v)$.

This theorem is interesting by its own sake since it relates the number of edges adjacent to any minimal weighted vertex feedback set to the number of edges adjacent to any minimum weighted vertex feedback set. Note that $F_{i}^{*}$ is a minimal vertex feedback set of $G_{i}$ and therefore Theorem 4 proves Eq. 8.
To prove this theorem we divide $\sum_{v \in F} d(v)$ into the sum $2|F|+\sum_{v \in F}(d(v)-2)$ and provide an upper bound for each term.

Lemma 5 Let $G, F$ and $F^{*}$ be defined as above. Then,

$$
2|F| \leq \sum_{v \in \bar{F}} d(v)-2\left|\bar{F} \cap \bar{F}^{*}\right|+2\left|F \cap F^{*}\right|
$$

Proof: First note that for every set of vertices $B$ in $G$,

$$
\begin{aligned}
& \sum_{v \in \bar{F}} d(v)-2\left|\bar{F} \cap \bar{F}^{*}\right|=\sum_{v \in \bar{F} \cap B} d(v)+ \\
& \sum_{v \in \bar{F} \backslash B} d(v)-2\left|\bar{F} \cap \bar{F}^{*} \cap B\right|-2\left|(\bar{F} \cap \bar{F}) \backslash B\right|
\end{aligned}
$$

However, the degree of every vertex in $G$ satisfies $d(v) \geq 2$ and therefore $\sum_{v \in \bar{F} \backslash B} d(v) \geq 2\left|\left(\bar{F} \cap \bar{F}^{*}\right) \backslash B\right|$. Consequently,

$$
\sum_{v \in \bar{F}} d(v)-2\left|\bar{F} \cap \bar{F}^{*}\right| \geq \sum_{v \in \bar{F} \cap B} d(v)-2\left|\bar{F} \cap \bar{F}^{*} \cap B\right|
$$

Thus, and since $\left|F \cap F^{*}\right| \geq\left|F \cap F^{*} \cap B\right|$ and $d_{B}(v) \leq$ $d(v)$, to prove the lemma it suffices to show that
$2|F| \leq \sum_{v \in \bar{F} \cap B} d_{B}(v)-2\left|\bar{F} \cap \bar{F}^{*} \cap B\right|+2\left|F \cap F^{*} \cap B\right|$,
or equivalently,

$$
2|F| \leq \sum_{v \in \bar{F} \cap B}\left(d_{B}(v)-2\right)+2\left|F^{*} \cap B\right|
$$

holds for some set of vertices $B$. We now define a set $B$ for which this inequality can be proven. Since $F$ is minimal, each vertex in $F$ can be associated with a cycle in $G$ that contains no other vertices of $F$. We define a graph $H$ that consists of the union of these cycles-one cycle per each vertex. Note that every vertex in $F$ is a linkpoint in $H$, i.e., a vertex with degree 2. Let $B$ be the vertices of $H$.

The proof of Eq. 18 is constructive. We repeatedly apply the following procedure on $H$ selecting in each step a vertex $v \in F$ and showing that there are terms in the right hand side (RHS) of Eq. 18 that contribute 2 to the RHS and have not been used for any other $v \in F$.
Set $H^{\prime}=H$. Pick a vertex $v \in F$ and follow the two paths $p_{1}$ and $p_{2}$ in $H^{\prime}$ emanating from $v$ (which is a linkpoint) until the first branchpoint on each side is found. There are three cases to consider. Either two distinct branchpoints $b_{1}$ and $b_{2}$ are found, one branchpoint $b_{1}$ (in which case $p_{1}$ and $p_{2}$ define a cycle) or none (if the cycle is isolated). In the first case the two edges on $p_{1}$ and $p_{2}$ whose endpoints are $b_{1} \in \bar{F}$ and $b_{2} \in \bar{F}$, respectively, are associated with the terms $d_{B}\left(b_{1}\right)-2>0$ and $d_{B}\left(b_{2}\right)-2>0$ in the RHS and so each of these terms contributes 1 to the sum $\sum_{v \in \bar{F} \cap B}\left(d_{B}(v)-2\right)$. In the second case, similarly, the two edges on $p_{1}$ and $p_{2}$ whose endpoints is $b_{1} \in \bar{F}$ are associated with the term $d_{B}\left(b_{1}\right)-2>0$ and so, if $d_{B}\left(b_{1}\right)>3$, this term contributes 2 to the sum $\sum_{v \in \bar{F} \cap B}\left(d_{B}(v)-2\right)$. If $d_{B}\left(b_{1}\right)=3$ we continue to follow the third path from $b_{1}$ (i.e., not $p_{1}$ or $p_{2}$ ) until another branchpoint $b_{2} \in \bar{F}$ is found and the last edge on that path is associated with $d_{B}\left(b_{2}\right)-2$ which contributes the extra missing 1 to the RHS. Finally, if no branchpoint is found, then on the cycle in which $v$ resides there must exist a vertex from $F^{*}$ that resides on no other cycles of $H^{\prime}$. Thus, the third case could not occur more than $\left|F^{*} \cap B\right|$ times. Now remove the paths $p_{1}$ and $p_{2}$ from $H^{\prime}$ obtaining a graph in which still each vertex in $F$ resides on a cycle that contains no other vertices of $F$. Continue the process until $F$ is exhausted.

Lemma 6 Let $G, F$ and $F^{*}$ be defined as above. Then the sum $\sum_{v \in F}(d(v)-2)$ is upper bounded by,

$$
\sum_{v \in F \cap \bar{F}^{*}} d_{F^{*}}(v)+\sum_{v \in F \cap F^{*}}(d(v)-2)-\sum_{v \in \bar{F} \cap \bar{F}^{*}}\left(d_{\bar{F}^{*}}(v)-2\right)
$$

Proof: First note that,

$$
\begin{gathered}
\sum_{v \in F}(d(v)-2)=\sum_{v \in F \cap \bar{F}^{*}}\left(d_{\bar{F}^{*}}(v)-2\right)+ \\
\sum_{v \in F \cap \bar{F}^{*}} d_{F^{*}}(v)+\sum_{v \in F \cap F^{*}}(d(v)-2)+ \\
\sum_{v \in \bar{F} \cap \bar{F}^{*}}\left(d_{\bar{F}^{*}}(v)-2\right)-\sum_{v \in \bar{F} \cap \bar{F}^{*}}\left(d_{\bar{F}^{*}}(v)-2\right)
\end{gathered}
$$

We now claim that $\sum_{v \in F \cap \bar{F}^{*}}(d_{\bar{F}^{*}}(v)-2)+$ $\sum_{v \in \bar{F} \cap \bar{F}^{*}}\left(d_{\bar{F}^{*}}(v)-2\right)$ is less or equal than 0 and therefore can be omitted from the inequality and conclude this proof. The graph induced by $\bar{F}^{*}$ is a forest and since the number of edges in a forest is smaller than the number of vertices, we have, $\sum_{v \in \bar{F}^{*}} d_{\bar{F}^{*}}(v) / 2 \leq\left|\bar{F}^{*}\right|$. Thus $\sum_{v \in \bar{F}^{*}}\left(d_{\bar{F}^{*}}(v)-2\right) \leq 0$ which is equivalent to the stated claim.

Using the bounds given by Lemmas 5 and 6 we have,

$$
\begin{aligned}
& \sum_{v \in \bar{F}} d(v) \leq \sum_{v \in \bar{F}} d(v)-2\left|\bar{F} \cap \bar{F}^{*}\right|+ \\
& \quad 2\left|F \cap F^{*}\right|+\sum_{v \in F \cap \bar{F}^{*}} d_{F^{*}}(v) \\
& \quad+\sum_{v \in F \cap F^{*}}(d(v)-2)-\sum_{v \in \bar{F} \cap \bar{F}^{*}}\left(d_{\bar{F}^{*}}(v)-2\right)
\end{aligned}
$$

However, $\sum_{v \in F \cap F^{*}}(d(v)-2)+2\left|F \cap F^{*}\right|=$ $\sum_{v \in F \cap F^{*}} d(v)$ and $\sum_{v \in \bar{F} \cap \bar{F}^{*}}\left(d_{\bar{F}^{*}}(v)-2\right)+2\left|\bar{F} \cap \bar{F}^{*}\right|=$ $\sum_{v \in \bar{F} \cap \bar{F}^{*}} d_{\bar{F}^{*}}(v)$. Thus, $\sum_{v \in F} d(v)$ is bounded by

$$
\begin{gathered}
\sum_{v \in \bar{F}} d(v)+\sum_{v \in F \cap F^{*}} d(v)- \\
\sum_{v \in \bar{F} \cap \bar{F}^{*}} d_{\bar{F}^{*}}(v)+\sum_{v \in F \cap \bar{F}^{*}} d_{F^{*}}(v)
\end{gathered}
$$

Now, $\sum_{v \in \bar{F}} d(v)-\sum_{v \in \bar{F} \cap \bar{F}^{*}} d_{\bar{F}^{*}}(v)$ actually equals to $\sum_{\bar{F} \cap F^{*}} d(v)+\sum_{v \in \bar{F} \cap \bar{F}^{*}} d_{F^{*}}(v)$ and therefore

$$
\sum_{v \in F} d(v) \leq \sum_{v \in \bar{F}^{*}} d_{F^{*}}(v)+\sum_{v \in \bar{F}^{*}} d(v) \leq 2 \sum_{v \in \bar{F}^{*}} d(v)
$$

which concludes the proof of Theorem 4.

## 4 Experimental Results

Below we denote by A1 the algorithm described in [SC90] and by A2 the algorithm described in [St90]. We performed six experiments. In the first two experiments we tested how the outputs of the four algorithms, A1, A2, GA, and MGA, compare to a minimum loop cutset. In two additional experiments we checked how the algorithms' outputs compare to each other when given larger graphs for which a minimum loop cutset is hard to obtain. In the above four experiments we have chosen all variables to be binary. The final two experiments compare the performance of these algorithms when the number of values in each vertex is randomly chosen between 2 and 6,2 and 8 , and between 2 and 10. Each instance of the six experiments is based on 100 graphs generated as described by [SC90].
In the first experiment each of the 100 graphs generated had 15 vertices and 25 edges. MGA made only one mistake producing 6 vertices instead of the minimum of 5 vertices. GA made 4 mistakes each by one vertex off. A2 made 7 mistakes one of which was two vertices off the minimum and the other six mistakes were one vertex off. A1 made 11 mistakes one of which was 2 vertices off and the other 10 mistakes were one vertex off. The minimum loop cutsets were between 3 and 6 vertices. Note that the ratio between the number of instances associated with a loop cutset found by MGA in this experiment and the number of instances associated with a minimum loop cutset is 1.002 which is far less than the theoretical ratios guaranteed by

Theorem 4 for this experiment which lie between 8 when the minimum loop cutset contains 3 binary variables and 64 when the minimum loop cutset contains 6 binary variables.
In the second experiment we generated 100 networks each with 25 vertices and 25 edges and tested how the output of the four algorithms compare to a minimum loop cutset when the graphs have a small number of loops. This case is interesting because the conditioning inference algorithm is most appropriate for these networks. MGA made no mistakes while the other three algorithms made between 4 and 5 mistakes each by one vertex (the minimum loop cutsets contained between 2 and 4 vertices).
Next we tested larger graphs. The first portion of the table below compares between GA and A2 showing that GA performs better than A2 in 53 of the 61 graphs ( $87 \%$ ) in which the algorithms disagree (out of 600 graphs tested). Each line in the table is based on 100 randomly generated graphs. The output columns show the number of graphs for which the two algorithms had an output of the same size and the number of graphs each algorithm performed better than the other. Thus even our simple greedy algorithm GA performs much better than A2. The reason for this is the reduction from the loop cutset problem to the weighted vertex feedback set problem which allows the algorithm to select vertices that have parents while A2 unjustifiably does not select such vertices (unless they have no pair of parents residing on the same loop). Similar empirical results and the same explanation applies to A1. The second portion of the table shows that MGA performs better than GA in 67 of the 75 graphs ( $89 \%$ ) in which the algorithms disagreed. Comparing MGA and A2 in the same fashion ( 600 graphs) showed that MGA performed better than A2 in 109 of the 116 graphs in which the algorithms disagreed. Similarly, MGA performed better than A1 in 135 of the 137 graphs in which these algorithms disagreed.


Finally, we repeated some of the experiments except that now each vertex was associated with a random number of values (between 2 and 6,2 and 8 , and 2 and 10). The results are summarized in the table below. The two algorithms, A1 and MGA, output loop cutsets of the same size in $55 \%$ of the graphs and when the algorithms disagreed, then in $81 \%$ of these graphs MGA performed better than A1. The ratio obtained between the number of instances of the algorithms solution and a minimum solution was 1.22 for MGA and

1.44 for Al (using the 300 graphs in the table below for which the number of vertices is 15 and number of edges 25 ).


To repeat this experiment with A2 required us to make a small change in A2 because it is not designed to run with vertices having different number of values. We adopted the approach of A1 which selects vertices (with at most one parent) according to their degree and if there are several candidates the one with the least number of values is selected for the loop cutset. Combining this idea with the A2 algorithm defines an algorithm we call the weighted A2 algorithm. The results obtained were that MGA performed better than WA2 in 175 of the 224 graphs in which the algorithms disagreed (out of 600). The ratio obtained between the number of instances of the algorithms' solution and a minimum solution was 1.22 for MGA and 1.33 for WA2.

## Remark.

While this work was at its final stages of preparation we became aware of a different method for the WVFS problem that achieves a performance ratio of 2 [Be94]. A quick examination of our own work in light of this information revealed that our method also achieves a performance ratio of 2 .
