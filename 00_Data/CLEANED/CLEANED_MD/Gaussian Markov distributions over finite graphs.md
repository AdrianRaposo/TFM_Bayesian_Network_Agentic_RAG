# GAUSSIAN MARKOV DISTRIBUTIONS OVER FINITE GRAPHS 

By T. P. Speed and H. T. Kiiveri<br>CSIRO Division of Mathematics and Statistics, Canberra and Perth, Australia


#### Abstract

Gaussian Markov distributions are characterised by zeros in the inverse of their covariance matrix and we describe the conditional independencies which follow from a given pattern of zeros. Describing Gaussian distributions with given marginals and solving the likelihood equations with covariance selection models both lead to a problem for which we present two cyclic algorithms. The first generalises a published algorithm for covariance selection whilst the second is analogous to the iterative proportional scaling of contingency tables. A convergence proof is given for these algorithms and this uses the notion of $I$-divergence.


1. Introduction. Most modelling of jointly Gaussian (normal) random variables involves the specification of a structure on the mean and the covariance matrix $K$. However, models which specify structure on $K^{-1}$ have also been developed, although they are seemingly less popular. Our interest in this paper focuses on the covariance selection models, introduced by Dempster (1972) and studied by Wermuth (1976a, b), in which certain elements of $K^{-1}$ are assumed to be zero.

In Section 2 we show how zeros in $K^{-1}$ correspond to conditional independence statements and characterise all such statements consequent upon a given pattern of zeros. The characterisation is achieved by associating a simple graph [Behdzad et al. (1979)] with the elements of $K^{-1}$ and providing rules for reading the graph. The results are a direct analogue of those given in Darroch et al. (1980) for contingency table models; see also Speed (1979).

The likelihood equations for covariance selection models lead naturally to a consideration of the problem of finding Gaussian distributions with prescribed margins. The results in Sections 3 and 4 provide a solution to this problem and a general algorithm for constructing the required distributions is given. Two special cases of this algorithm are considered. The first one is a generalisation of an algorithm in Wermuth and Scheidt (1977) whilst the second one has properties analogous to iterative proportional scaling for contingency tables [Haberman (1974)]. The notion of $I$-divergence [Csiszár (1975)] or discrimination information in the terminology of Kullback (1959), plays an important role in the convergence proof of this algorithm.

Finally, in Section 5 we show how the $I$-divergence geometry of Csiszár (1975) provides a framework in which both algorithms can be seen to be an iterated sequence of $I$-projections.

[^0]
[^0]:    Received November 1983; revised September 1985.
    AMS 1980 subject classifications. Primary 62F99; secondary 60K35.
    Key words and phrases. Conditional independence, Markov property, simple graph, covariance selection, $I$-divergence geometry.

2. Conditional independence for Gaussian random variables. In the following we consider a random vector $\mathbf{X}$ having a Gaussian distribution with mean 0 and positive definite covariance matrix $K$. The components of $\mathbf{X}$ will be indexed by a finite set $C$ and for $a \subset C$ we write $\mathbf{X}_{a}$ for the subset of the components of $\mathbf{X}$ indexed by $a$, namely ( $X_{\gamma}: \gamma \in a$ ). The covariance matrix $K=(K(\alpha, \beta): \alpha, \beta \in C)$ on $C$ is defined by $K(\alpha, \beta)=\mathbb{E}\left\{X_{\alpha} X_{\beta}\right\}, \alpha, \beta \in C$, where $\mathbb{E}$ denotes expected value. For subsets $a, b \subseteq C, K_{a, b}=\{K(\alpha, \beta): \alpha \in$ $a, \beta \in b\}$ denotes the cross covariance matrix of $\mathbf{X}_{a}$ and $\mathbf{X}_{b}$. When $a=b$ we write $K_{a}$ instead of $K_{a, a}$. Note that care must be taken to distinguish between $K_{a}^{-1}$ and $\left(K^{-1}\right)_{a}$. The density $p(\mathbf{x})$ of $\mathbf{X}$ is, of course,

$$
p(\mathbf{x})=(2 \pi)^{-|C| / 2}(\operatorname{det} K)^{-1 / 2} \exp \left\{-\frac{1}{2} \mathbf{x}^{T} K^{-1} \mathbf{x}\right\}, \quad x \in \mathbb{R}^{|C|}
$$

where $|\cdot|$ denotes the cardinality of the argument. Marginal densities are subscripted by their defining sets, e.g., $p_{a}\left(\mathbf{x}_{a}\right)$ or simply $p_{a}$, refers to the marginal density of $\mathbf{X}_{a}$, where $a$ is an arbitrary subset of $C$.

Proposition 1 relates the conditional independence of two components of $\mathbf{X}$ to the structure of $K$. In the proposition and following we abbreviate the set intersection $a \cap b$ to $a b$ and write $a \backslash b$ for the complement of $b$ in $a$. The set $C \backslash b$ will be denoted $b^{\prime}$.

Proposition 1. For subsets $a, b$ of $C$ with $a \cup b=C$ the following statements are equivalent.
(i) $K_{a, b}=K_{a, a b} K_{a b}^{-1} K_{a b, b}$.
(i') $K_{a \backslash b, b \backslash a}=K_{a \backslash b, a b} K_{a b}^{-1} K_{a b, b \backslash a}$.
(ii) $\left(K^{-1}\right)_{a \backslash b, b \backslash a}=0$.
(iii) $\mathbf{X}_{a}$ and $\mathbf{X}_{b}$ are conditionally independent given $\mathbf{X}_{a b}$.

Proof. (i) and (i') are easily seen to be equivalent by partitioning the rows of $K$ over $a \backslash b$ and $a b$ and the columns over $b \backslash a$ and $a b$. By partitioning over $a \backslash b, b \backslash a$, and $a b$, a straightforward use of the expression for the inverse of a partitioned matrix [Rao (1973, page 33)] proves that (i') is equivalent to (ii). The standard formula (2) for the conditional covariance matrix gives the connection between (iii) and (i'),

$$
\operatorname{cov}\left(\mathbf{X}_{a \backslash b}, \mathbf{X}_{b \backslash a} \mid \mathbf{X}_{a b}\right)=K_{a \backslash b, b \backslash a}-K_{a \backslash b, a b} K_{a b}^{-1} K_{a b, b \backslash a}
$$

A useful special case of the above proposition is the following corollary, given by Wermuth (1976a).

Corollary 1. For distinct elements $\alpha, \beta$ of $C, X_{\alpha}$ and $X_{\beta}$ are conditionally independent given $X_{(\alpha, \beta)^{\prime}}$ iff $K^{-1}(\alpha, \beta)=0$.

Proof. Put $a=C \backslash\{\alpha\}=\{\alpha\}^{\prime}$ and $b=\{\beta\}^{\prime}$ in Proposition 1.
Having shown that zeros in $K^{-1}$ correspond to conditional independence statements we now describe all such statements which follow from a given

pattern of zeros in $K^{-1}$. To do this we associate a simple undirected graph with the pattern of zeros and then give rules for reading the graph to obtain the independence relations.

To begin, some graph-theoretic notation and definitions are needed; for a general reference see Behdzad et al. (1979). Our simple undirected graph will be denoted by $\mathbf{C}=(C, E(C))$ where $C$ is the vertex set, and $E(\mathbf{C})$ the edge set which consists of unordered pairs of distinct vertices. Pairs of vertices $\{\alpha, \beta\} \in$ $E(\mathbf{C})$ are said to be adjacent. A maximal set of $(\geq 2)$ vertices for which every pair is adjacent is called a clique. For any vertex $\gamma$ we write $\partial \gamma=\{\alpha:\{\alpha, \gamma\} \in E(\mathbf{C})\}$ for the set of neighbours of $\gamma$. We also write $\bar{\gamma}=\gamma \cup \partial \gamma$.

An important notion is the separation of sets of vertices in $\mathbf{C}$. To define this we first need to define a chain which is a sequence $\gamma=\gamma_{0}, \gamma_{1}, \ldots, \gamma_{m}=\beta$ of vertices such that $\left\{\gamma_{l}, \gamma_{l+1}\right\} \in E(\mathbf{C})$ for $l=0,1, \ldots, m-1$. If $\gamma_{0}=\gamma_{m}$ the chain is called a cycle. Two sets of vertices $a, b$ are said to be separated by a third set $d$ if every chain connecting an $\alpha \in a$ to a $\beta \in b$ intersects $d$.

The graph $\mathbf{C}$ is said to be triangulated [see Lauritzen et al. (1984)] iff all cycles $\gamma_{0}, \gamma_{1}, \ldots, \gamma_{p}=\gamma_{0}$ of length $p \geq 4$ possess a chord, where a chord is an edge connecting two nonconsecutive vertices of the cycle.

Finally, the graph $\tilde{\mathbf{C}}$ complementary to $\mathbf{C}$ has vertex set $C$ and edge set $E(\tilde{\mathbf{C}})$ with the property that $\{\alpha, \beta\} \in E(\tilde{\mathbf{C}})$ iff $\alpha \neq \beta$ and $\{\alpha, \beta\} \notin E(\mathbf{C})$. Example 1 illustrates these ideas.

Example 1. The graph $\mathbf{C}$ with vertex set $\{1,2,3,4\}$ and edge set $\{\{1,2\}$, $\{1,3\},\{1,4\},\{2,3\},\{3,4\}\}$ could be depicted as in Figure 1. For this graph the set of neighbours of 1 is $\{2,3,4\}$; the cliques are $\{1,2,3\},\{1,3,4\}$; a chain from $\{2\}$ to $\{4\}$ is $2,3,1,4$ and $\{2\}$ is separated from $\{4\}$ by $\{1,3\}$. Figure 2 shows the complementary graph.

As it stands the graph in Figure 1 is triangulated. However, if the edge $\{1,3\}$ were removed we would have the simplest example of a nontriangulated graph.

The characterisation of all conditional independence relations consequent upon a given pattern of zeros in $K^{-1}$ is presented in Proposition 2.

Proposition 2. Let $\mathbf{C}$ be a simple graph with vertex set $C$ indexing the Gaussian random variables $\mathbf{X}$. Then the following are equivalent.
(i) $K^{-1}(\alpha, \beta)=0$ if $\{\alpha, \beta\} \notin E(\mathbf{C})$ and $\alpha \neq \beta$;
![img-0.jpeg](img-0.jpeg)

Fig. 1
![img-1.jpeg](img-1.jpeg)

Fig. 2

The local Markov property:
(ii) For every $\gamma \in C, X_{\gamma}$ and $\mathbf{X}_{\{\gamma\}^{\prime}}$ are conditionally independent given $\mathbf{X}_{\partial \gamma}$; The global Markov property:
(iii) For every $a, b$ and $d$ with $d$ separating a from $b$ in $\mathbf{C}, \mathbf{X}_{a}$ and $\mathbf{X}_{b}$ are conditionally independent given $\mathbf{X}_{d}$.

Proof. To show the equivalence of (i) and (ii) we note that (i) is equivalent to $K^{-1}\left(\gamma,\{\gamma\}^{\prime}\right)=0$. Putting $a=\{\gamma\}$ and $b=\{\gamma\}^{\prime}$ in Proposition 1 then proves the result.

The equivalence of (i) and (iii) for the case $a \cup b \cup d=C$ follows in a similar way if we put " $a$ " $=a \cup d$ and " $b$ " $=b \cup d$ in Lemma 1. When $a \cup b \cup d \neq C$ a simple maximality argument as in Vorobev (1963) shows that maximal sets $a^{*}, b^{*}$ exist such that $a \subseteq a^{*}, b \subseteq b^{*}, a^{*} \cup b^{*} \cup d=C$, and $a^{*}$ is separated from $b^{*}$ by $d$. Proposition 1 then gives us $p=p_{a^{*}} p_{b^{*}} / p_{d}$ and integration to obtain the marginal density of $\mathbf{X}_{\alpha \cup b \cup d}$ shows that (i) implies (iii).

The implication in the reverse direction follows on noting that if $(\alpha, \beta) \notin E(\mathbf{C})$ then $\alpha, \beta$ are separated by $\{\alpha, \beta\}^{\prime}$. Hence by (iii) $X_{\alpha}$ and $X_{\beta}$ are conditionally independent given $X_{\{\alpha, \beta\}^{\prime}}$ and Corollary 1 shows that $K^{-1}(\alpha, \beta)=0$.

The results of Proposition 2 are illustrated in Example 2.
Example 2. Suppose $K^{-1}$ has the following pattern with * denoting a nonzero element:


Then the corresponding graph $\mathbf{C}$ would be as shown in Figure 3. If we put $\gamma=\{2\}, \partial \gamma=\{1,3,5\}$, and use the local Markov property we deduce that $X_{2}$ and $X_{4}$ are conditionally independent given $\mathbf{X}_{\{1,3,5\}}$. Similarly with $a=\{1\}$, $b=\{4\}$, and $d=\{2\}$, the global Markov property can be used to assert that $X_{1}$ and $X_{4}$ are conditionally independent given $X_{2}$.
3. Gaussian Markov distributions with prescribed marginals. In this section we consider the problem of finding a Gaussian probability measure with prescribed marginals, i.e., we seek a joint probability density $p$ whose marginals

$$
p_{c_{1}}, \ldots, p_{c_{n}}
$$

are known beforehand, $c_{1}, \ldots, c_{n}$ being proper subsets of $C$. (The notation is explained after (1) above.) Clearly if our marginal specifications are consistent it is necessary to give only the maximal $c_{i}$ in (3).

![img-2.jpeg](img-2.jpeg)

Fig. 3

As motivation for this problem consider the following. Suppose we have $n$ independent and identically distributed observations $\mathbf{x}_{1}, \ldots, \mathbf{x}_{n}$ from (1) and we wish to find a maximum likelihood estimate of $K$ subject to certain elements of $K^{-1}$ being zero. When written in our notation, the likelihood equations for such a model (Dempster, 1972) are:

$$
\begin{aligned}
K(\alpha, \beta)=S(\alpha, \beta) & \text { if }\{\alpha, \beta\} \in E(\mathbf{C}) \text { or } \alpha=\beta \\
K^{-1}(\alpha, \beta)=0 & \text { if }\{\alpha, \beta\} \notin E(\mathbf{C}) \text { and } \alpha \neq \beta
\end{aligned}
$$

where $n S=\sum_{i=1}^{n} \mathbf{x}_{i} \mathbf{x}_{i}^{T}$. The first equation in (4) is easily shown to be equivalent to

$$
K_{c}=S_{c} \quad \text { if } c \in \mathscr{C}(\mathbf{C})
$$

where $\mathscr{C}(\mathbf{C})$ is the class of cliques of $\mathbf{C}$. Since a Gaussian distribution with mean zero is completely specified by its covariance matrix, (4') amounts to specifying the marginal distributions $p_{c}$ for $c \in \mathscr{C}(\mathbf{C})$.

Theorem 1 can be used to describe the class of Gaussian measures with prescribed margins.

Theorem 1. Given positive definite matrices $L$ and $M$ defined on the vertices $C$ of a graph $\mathbf{C}=(C, E(\mathbf{C}))$ there exists a unique positive definite matrix $K$ such that
(i) $K(\alpha, \beta)=L(\alpha, \beta)$ if $\{\alpha, \beta\} \in E(\mathbf{C})$ or $\alpha=\beta$,
(ii) $K^{-1}(\alpha, \beta)=M(\alpha, \beta)$ if $\{\alpha, \beta\} \notin E(\mathbf{C})$ and $\alpha \neq \beta$.

Equivalently
(i') $K_{c}=L_{c}$ if $c \in \mathscr{C}(\mathbf{C})$;
(ii') $K^{-1}(\bar{c}, \bar{c})$ and $M(\bar{c}, \bar{c})$ agree except on the diagonals, $\bar{c} \in \mathscr{C}(\overline{\mathbf{C}})$.

Proof. The equivalence of (i) and (i') follows from the relation

$$
E(\mathbf{C})=\bigcup_{c \in \mathscr{C}(\mathbf{C})} \bigcup_{\{\alpha, \beta\} \subseteq c}\{\alpha, \beta\}
$$

Replacing $\mathbf{C}$ by $\tilde{\mathbf{C}}$ in (5) enables the equivalence of (ii) and (ii') to be demonstrated.

The main result of Theorem 1 can be established using the theory of exponential families [Barndorff-Nielsen (1978), Johansen (1979)] and such a proof is sketched by Dempster (1972, Appendixes A and B).

The results in Section 4 will show how to generate a sequence of matrices converging to the $K$ of Theorem 1 and thus provide an alternative proof. We prefer this proof as it provides a basis for simple numerical algorithms which do not require Newton-Raphson type iterations or storage of large matrices to compute $K$.

Replacing the $L$ in Theorem 1 by the sample covariance matrix and setting $M=I$ shows that the estimation problem for covariance selection models has a well defined solution. When $M=I$, the $K$ in Theorem 1 gives the Gaussian distribution with maximum entropy satisfying (i) or (i') [see Dempster (1972)].

Note that varying the $M$ in Theorem 1 gives the family of distributions with margins prescribed by $L_{c}, c \in \mathscr{C}(\mathbf{C})$.

In the next section we will make use of the notion of the I-divergence of two positive definite matrices. This is defined by

$$
\mathscr{I}(P \mid R)=-\frac{1}{2}\left\{\log \operatorname{det}\left(P R^{-1}\right)+\operatorname{tr}\left(I-P R^{-1}\right)\right\}
$$

The definition (6) results from evaluating the discrimination information measure of Kullback (1959), namely $/ p(\mathbf{x}) \log \{p(\mathbf{x}) / r(\mathbf{x})\} d \mathbf{x}$ for the two Gaussian distributions with densities $p(\mathbf{x}), r(\mathbf{x})$ defined by covariance matrices $P, R$. When it exists, the $I$-divergence behaves somewhat like a norm on a space of probability measures (Csiszár, 1975), although it is not.

Some properties of (6) which we will use later are given in Lemma 1. We write $\mathscr{P}$ for the set of $|C| \times|C|$ positive definite matrices and regard this as a (convex) subset of $\mathbb{R}^{q}$ where $q=|C|^{2}$. In the following a set of unordered pairs of (not necessarily distinct) elements of $C$ will be denoted by $E$.

Lemma 1. The I-divergence $\mathscr{I}(\cdot \mid \cdot)$ has the following properties.
(i) If $P, R \in \mathscr{P}, \mathscr{I}(P \mid R) \geqq 0$ with equality iff $P=R$.
(ii) Given $P, R \in \mathscr{P}$, if there exists a $Q \in \mathscr{P}$ such that
(a) $Q(\alpha, \beta)=P(\alpha, \beta)$ if $(\alpha, \beta) \in E$, and
(b) $Q^{-1}(\alpha, \beta)=R^{-1}(\alpha, \beta)$ if $(\alpha, \beta) \notin E$, then

$$
\mathscr{I}(P \mid R)=\mathscr{I}(P \mid Q)+\mathscr{I}(Q \mid R)
$$

If such a $Q$ exists it is unique.
(iii) If $\left\{K_{n}\right\}$ and $\left\{L_{n}\right\}$ are sequences contained in compact subsets of $\mathscr{P}$ then $\mathscr{I}\left(K_{n} \mid L_{n}\right) \rightarrow 0$ implies $K_{n}-L_{n} \rightarrow 0$.

Proof. The first assertion is a well known property of the Kullback information measure so we focus on (ii) and (iii).

(ii) A simple calculation shows that for $Q \in \mathscr{P}$

$$
\mathscr{I}(P \mid Q)+\mathscr{I}(Q \mid R)=\mathscr{I}(P \mid R)-\frac{1}{2} \operatorname{tr}\{(Q-P) \Delta\}
$$

where $\Delta=Q^{-1}-R^{-1}$. Conditions (a) and (b) then ensure that the trace term in (8) is zero.

To prove uniqueness suppose $Q_{1}$ and $Q_{2}$ satisfy (a) and (b) of (ii). Then setting $P=R=Q_{1}$ shows that

$$
\mathscr{I}\left(Q_{1} \mid Q_{1}\right)=\mathscr{I}\left(Q_{1} \mid Q_{2}\right)+\mathscr{I}\left(Q_{2} \mid Q_{1}\right)
$$

and since $I$-divergences are positive unless both arguments are equal we must have $Q_{1}=Q_{2}$.
(iii) Suppose $\mathscr{I}\left(K_{n} \mid L_{n}\right) \rightarrow 0$ but $K_{n}-L_{n} \nrightarrow 0$. Then there exist convergent subsequences $K_{n^{\prime}} \rightarrow K$ and $L_{n^{\prime}} \rightarrow L$ with $K \neq L$. By continuity $\mathscr{I}\left(K_{n^{\prime}} \mid L_{n^{\prime}}\right) \rightarrow$ $\mathscr{I}(K \mid L) \neq 0$, which is a contradiction. $\square$
4. Algorithms. This section develops two algorithms for constructing the $K$ of Theorem 1. The first algorithm preserves ( $\mathrm{i}^{\prime}$ ) of Theorem 1 throughout the iterations and cycles through $\tilde{c} \in \mathscr{C}(\tilde{\mathbf{C}})$ forcing the off-diagonal elements of $K^{-1}(\tilde{c}, \tilde{c})$ to zero. The second algorithm preserves (ii') whilst forcing $K_{c}=L_{c}$ as it cycles through $c \in \mathscr{C}(\mathbf{C})$. Both of these algorithms are special cases of a more general cyclic algorithm and we begin by presenting this algorithm. Throughout the discussion $E_{1}, E_{2}, \ldots, E_{m}$ denote sets of unordered pairs of (not necessarily distinct) elements of $C$ whose union is denoted by $E$.
4.1. A general cyclic algorithm. The general cyclic algorithm is designed to solve the following problem. Given $G, H \in \mathscr{P}$ find an $F \in \mathscr{P}$ with the property that

$$
\begin{aligned}
F(\alpha, \beta) & =G(\alpha, \beta) & & \text { if }(\alpha, \beta) \in E \\
F^{-1}(\alpha, \beta) & =H(\alpha, \beta) & & \text { if }(\alpha, \beta) \notin E
\end{aligned}
$$

The algorithm is defined as follows. Generate a sequence $\left\{F_{n}\right\}$ of positive definite matrices satisfying $F_{0}=H^{-1}$ and, for $n \geqq 1$,

$$
\begin{aligned}
F_{n}(\alpha, \beta) & =G(\alpha, \beta) & & \text { if }(\alpha, \beta) \in E_{n^{\prime}} \\
F_{n}^{-1}(\alpha, \beta) & =F_{n-1}^{-1}(\alpha, \beta) & & \text { if }(\alpha, \beta) \notin E_{n^{\prime}}
\end{aligned}
$$

where $n^{\prime}=n(\bmod m)$. Basically the idea is to maintain (10) throughout the sequence whilst cycling through the $E_{m}$ and forcing (9). The crucial step in the algorithm involves going from $F_{n-1}$ to $F_{n}$. Assuming for the moment that this step can be performed, a convergence proof for this algorithm, modelled upon that found in Csiszár (1975, Theorem 3.2), is given in Proposition 3. The two algorithms to be discussed are examples for which the sequence $\left\{F_{n}\right\}$ can be easily constructed. We write $\mathbb{N}$ for the set of nonnegative integers.

Proposition 3. The sequence $\left\{F_{n}\right\}$ generated by the general cyclic algorithm converges to the unique $F \in \mathscr{P}$ with the properties (9) and (10).

Proof. By (ii) of Lemma 1 we can write for $r \geqq 1$

$$
\mathscr{I}\left(G \mid F_{r-1}\right)=\mathscr{I}\left(G \mid F_{r}\right)+\mathscr{I}\left(F_{r} \mid F_{r-1}\right)
$$

Summing relations of the form (11) over $r$ gives for $u \geqq 1$

$$
\mathscr{I}\left(G \mid F_{0}\right)=\mathscr{I}\left(G \mid F_{a}\right)+\sum_{r=1}^{u} \mathscr{I}\left(F_{r} \mid F_{r-1}\right)
$$

and from (12) we deduce that

$$
\left\{F_{n}\right\} \in\left\{F: \mathscr{I}(G \mid F) \leqq \mathscr{I}\left(G \mid F_{0}\right)\right\}=A \quad \text { (say) }
$$

The set $A$ is compact since $\mathscr{I}(G \mid F)$ is strictly convex (as a function of $F^{-1}$ ) with a unique minimum. From (12) it also follows that

$$
\sum_{r=1}^{u} \mathscr{I}\left(F_{r} \mid F_{r-1}\right) \leqq \mathscr{I}\left(G \mid F_{0}\right)
$$

Hence $\sum_{r=1}^{\infty} \mathscr{I}\left(F_{r} \mid F_{r-1}\right)$ is convergent and $\mathscr{I}\left(F_{r} \mid F_{r-1}\right) \rightarrow 0$ as $r \rightarrow \infty$.
Now by (13) the vector sequence $\left\{F_{s m+1}, F_{s m+2}, \ldots, F_{s m+m}\right)$ : $s \geqq 0\}$ has a convergent subsequence, defined by $s \in \mathbb{N}_{1} \subseteq \mathbb{N}$, with limit $\left(F_{1}^{*}, F_{2}^{*}, \ldots, F_{m}^{*}\right)$ say. For any $2 \leqq t \leqq m$ we can write

$$
\left(F_{t}-F_{t-1}\right)=\left(F_{t}-F_{s m+t}\right)+\left(F_{s m+t}-F_{s m+t-1}\right)+\left(F_{s m+t-1}-F_{t-1}\right)
$$

Letting $s \in \mathbb{N}_{1} \rightarrow \infty$ and using (iii) of Lemma 1 with $L_{n}=K_{n-1}$ shows that $F_{1}^{*}=F_{2}^{*}=\cdots F_{m}^{*}=F$ (say). Note that (10) holds for each $F_{r}$ and hence for the limit $F$. Similarly for each $s \in \mathbb{N}_{1}$ and $t, F_{s m+t}(\alpha, \beta)=G(\alpha, \beta)$ if $(\alpha, \beta) \in E_{t}$, so the same property holds for the limit $F$, i.e., (9) holds.

A similar argument for any other convergent subsequence shows that the limit point satisfies (9) and (10) of our proposition. Lemma 1, part (ii) then establishes that all convergent subsequences have the same limit and hence $\left\{F_{n}\right\}$ converges.

The next lemma enables sequences $\left\{F_{n}\right\}$ satisfying ( $9^{\prime}$ ) or ( $10^{\prime}$ ) to be constructed when either

$$
E_{i}=\left\{(\alpha, \beta): \alpha, \beta \in a_{i} \subseteq C\right\}
$$

or

$$
E_{i}=\left\{(\alpha, \beta): \alpha, \beta \in a_{i} \subseteq C, \alpha \neq \beta\right\}
$$

Lemma 2. Suppose $Q, R$, and $B \in \mathscr{P}$. Then
(i) for $a \subseteq C$ the matrix

$$
Q^{-1}=R^{-1}+\left[\begin{array}{cc}
B_{a}^{-1}-R_{a}^{-1} & 0 \\
0 & 0
\end{array}\right]
$$

is positive definite and satisfies
(a) $Q(\alpha, \beta)=B(\alpha, \beta)$ if $\alpha \in a$ and $\beta \in a$; and
(b) $Q^{-1}(\alpha, \beta)=R^{-1}(\alpha, \beta)$ if $\alpha \notin a$ or $\beta \notin a$.

(ii) The matrix $Q$ is given by

$$
Q=\left[\begin{array}{cc}
B_{\alpha} & B_{\alpha} R_{\alpha}^{-1} R_{\alpha, \alpha^{\prime}} \\
R_{\alpha^{\prime}, \alpha} R_{\alpha}^{-1} B_{\alpha} & R_{\alpha^{\prime}}-R_{\alpha^{\prime}, \alpha} R_{\alpha}^{-1}\left(I-B_{\alpha} R_{\alpha}^{-1}\right) R_{\alpha, \alpha^{\prime}}
\end{array}\right]
$$

(iii) We have the expression:

$$
\mathscr{I}(Q \mid R)=-\frac{1}{2}\left\{\log \operatorname{det} B_{\alpha} R_{\alpha}^{-1}+\operatorname{tr}\left(I_{\alpha}-B_{\alpha} R_{\alpha}^{-1}\right)\right\}
$$

Proof. (i) We use the density scaling of Kullback (1968). In the Gaussian case, given densities $b(\mathbf{x})$ and $r(\mathbf{x})$ corresponding to positive definite matrices $B$ and $R$, scaling so that $r_{\alpha}\left(\mathbf{x}_{\alpha}\right)$ agrees with $b_{\alpha}\left(\mathbf{x}_{\alpha}\right)$ corresponds to computing

$$
q(\mathbf{x})=\frac{r(\mathbf{x}) b_{\alpha}\left(\mathbf{x}_{\alpha}\right)}{r_{\alpha}\left(\mathbf{x}_{\alpha}\right)}
$$

Expanding the right-hand side of (21) gives

$$
\begin{aligned}
q(\mathbf{x})= & (2 \pi)^{-|C| / 2}\left(\frac{\operatorname{det} R \operatorname{det} B_{\alpha}}{\operatorname{det} R_{\alpha}}\right)^{-1 / 2} \\
& \times \exp \left\{-\frac{1}{2} \mathbf{x}^{T}\left[R^{-1}+\left(\begin{array}{cc}
B_{\alpha}^{-1}-R_{\alpha}^{-1} & 0 \\
0 & 0
\end{array}\right)\right] \mathbf{x}\right\}
\end{aligned}
$$

which by (18) is just

$$
(2 \pi)^{-|C| / 2}(\operatorname{det} Q)^{-1 / 2} \exp \left\{-\frac{1}{2} \mathbf{x}^{T} Q^{-1} \mathbf{x}\right\}
$$

The properties (a) and (b) are now immediate. A direct proof using matrix algebra can also be given.

The proofs of (ii) and (iii) are straightforward so we omit them.
The two algorithms discussed below correspond to choosing the $a_{i}$ in (16) and (17) to be the cliques of $\mathbf{C}$ or $\overline{\mathbf{C}}$, respectively. In the following we will abbreviate the class of cliques of $\mathbf{C}$ by $\mathscr{C}$ and the class of cliques of $\overline{\mathbf{C}}$ by $\overline{\mathscr{C}}$. The notation $\operatorname{diag}(A)$ refers to a diagonal matrix whose diagonals are the same as those of $A$.
4.2. The first cyclic algorithm. List the cliques of the complementary graph $\overline{\mathbf{C}}$ as $\bar{c}_{1}, \ldots, \bar{c}_{m}$ and generate a sequence $\left\{K_{n}\right\}$ as follows: $K_{0}=L$; for $s \in \mathbb{N}$, $1 \leqq t \leqq m, K_{s m+t}=Z_{t}\left(K_{s m+t-1}\right)$, where $Z_{t}(K)=Q^{-1}, Q$ being the matrix (18) of Lemma 2 with $R=K^{-1}, a=\bar{c}_{t}$, and $B_{\alpha}=\operatorname{diag}\left(\left(K^{-1}\right)_{\alpha}^{-1}\right)^{-1}$. The fact that this sequence converges to the required matrix $K$ when $M=I$ follows from Proposition 3 on replacing $a_{i}$ in (17) by $\bar{c}_{i}$ and making the identifications $F_{n}=K_{n}^{-1}, G=M$, and $H=L$. It does not seem possible to give an explicit expression for $B_{\alpha}$ in the case when $M \neq I$.

For this algorithm the elements of the sequence $\left\{K_{n}\right\}$ are fixed over $\mathscr{C}$ whilst the elements of $\left\{K_{n}^{-1}\right\}$ vary over $\overline{\mathscr{C}}$. From a computational point of view it is not necessary to compute the sequence $\left\{K_{n}\right\}$ by inverting $K_{n}^{-1}$ at each step. The expression (18) provides a simple updating formula for $K_{n}$ given $K_{n-1}$. Hence it

is only necessary to invert $|\tilde{c}| \times|\tilde{c}|$ positive definite matrices when cycling through $\tilde{c} \in \overline{\mathscr{C}}$.

The cyclic algorithm of Wermuth and Scheidt (1977) is also a special case of the general algorithm. Instead of using the cliques of $\tilde{\mathbf{C}}$ these authors cycle through the edges $\{\alpha, \beta\} \in E(\tilde{\mathbf{C}})$. The $2 \times 2$ matrix inversions required are explicitly performed and used to give a simple updating formula. Their algorithm is defined in the same way as above but they have $a \in E(\tilde{\mathbf{C}})$ and

$$
B_{a}=\delta\left[\begin{array}{cc}
w^{-1} & 0 \\
0 & u^{-1}
\end{array}\right]
$$

where

$$
\left(K^{-1}\right)_{a}=\left[\begin{array}{cc}
u & v \\
v & w
\end{array}\right]
$$

and $\delta=u w-v^{2}$. It is easily seen that at each step the current value of $K(\alpha, \beta)$ is changed by $-v / \delta$ so that $K^{-1}(\alpha, \beta)=0$. A computer program for performing the adjustments is given in Wermuth and Scheidt's paper.
4.3. The second cyclic algorithm. Enumerate the cliques of $\mathbf{C}$ as $c_{1}, c_{2}, \ldots, c_{m}$ and define a sequence $\left\{K_{r}\right\}$ as follows: $K_{0}=M^{-1}$; for $s \geqq 0,1 \leqq t \leqq m$, $K_{s m+t}=Y_{t}\left(K_{s m+t-1}\right)$, where $Y_{t}(K)=Q, Q$ being the matrix (6) of Lemma 1 with $R=K, a=c_{t}$, and $B=L$. Making the identifications $a_{i}=c_{i}$ in (16) and $F_{n}=K_{n}, G=L$, and $H=M$ in Proposition 3 shows that the second algorithm converges to the $K$ of Theorem 1. This result also gives an alternative proof of Theorem 1. Note that $\left\{K_{n}^{-1}\right\}$ is held fixed over $\overline{\mathscr{C}}$ whilst $\left\{K_{n}\right\}$ varies over $\mathscr{C}$.

That this second algorithm is analogous to iterative proportional scaling for contingency tables should be clear. At each step we "scale" the current covariance matrix to match the relevant "margin" $L_{c}$. We can also connect this algorithm with a general procedure in Kullback (1968) where, however, the proofs are incomplete. Using our notation, Kullback's procedure can be described as follows. Given the required marginal densities $g_{c_{1}}, \ldots, g_{c_{m}}$ and an initial density $\pi(\mathbf{x})$ construct the sequence $\left\{f_{n}\right\}$ (assumed to exist) defined by

$$
f_{0}(\mathbf{x})=\pi(\mathbf{x})
$$

and for $s \geqq 0,1 \leqq t \leqq m$

$$
f_{s m+t}(\mathbf{x})=\frac{f_{s m+t-1}(\mathbf{x}) g_{c_{t}}\left(\mathbf{x}_{c_{t}}\right)}{\left(f_{s m+t-1}\right)_{c_{t}}\left(\mathbf{x}_{c_{t}}\right)}
$$

Note that this simply amounts to scaling the previous density to ensure the desired marginals and this is how we obtain the matrix $Q$ of Lemma 2. Hence the second cyclic algorithm is a Gaussian version of Kullback's general procedure. It can also be shown to be a cyclic ascent algorithm.
4.4. Finite termination. When the graph $\mathbf{C}$ is triangulated and $M=I$ the second cyclic algorithm converges after one cycle if the cliques are suitably ordered. This result is completely analogous to the one cycle convergence of

iterative proportional scaling for contingency tables when the generating class is decomposable [see Haberman (1974, Chapter 5)].

To demonstrate the result we need the following two lemmas. Without loss of generality we assume that the graph $\mathbf{C}$ is connected.

Lemma 3. If $\mathbf{C}$ is triangulated then there exists an enumeration $c_{1}, \ldots, c_{m}$ of the cliques such that for $i=2, \ldots, m$

$$
c_{i} \backslash \bigcup_{l=1}^{i-1} c_{l} \neq \varnothing
$$

Proof. The result is obtained by successively removing detachable cliques from C [see Lauritzen et al. (1984)].

Note that (24) states that for each $i$ the clique $c_{i}$ contains a vertex not in $c_{l}$ for $l=1, \ldots, i-1$.

The second lemma gives an expression for the determinant of the matrix $K$ in Proposition 1 which is useful in proving the finite termination of the second algorithm.

Lemma 4. Suppose $K \in \mathscr{P}$ and $K_{a \backslash b, b \backslash a}^{-1}=0$ for $a, b$ with $a \cup b=C$. Then

$$
\operatorname{det} K=\left(\operatorname{det} K_{a}\right)\left(\operatorname{det} K_{b}\right) / \operatorname{det} K_{a b}
$$

Proof. Note that (iii) of Proposition 1 implies $p=p_{a} p_{b} / p_{a b}$. Evaluation at $x=0$ then gives the result.

Proposition 4. If the cliques of $\mathbf{C}$ are ordered as in Lemma 3 and we start the second cyclic algorithm with $K_{0}=I$, then
(i) $\left(K_{m}\right)_{c}=L_{c}$ for $c \in \mathscr{C}$;
(ii) $\left(K_{m}^{-1}\right)_{\bar{c}}$ is diagonal for $\bar{c} \in \overline{\mathscr{C}}$.

Proof. We will prove that $\mathscr{I}\left(K \mid K_{m}\right)=0$ where $K$ is the unique matrix of Theorem 1 with $M=I$. This will follow directly from (12) provided we can show that

$$
\mathscr{I}(K \mid I)=\sum_{i=1}^{m} \mathscr{I}\left(K_{i} \mid K_{i-1}\right)
$$

and we prove this by induction on $m$, the number of cliques. It is clearly true for $m=1$ and so we assume that it is true for all $m \leqq q$ where $q \geqq 1$. If we can prove

$$
\mathscr{I}(K \mid I)=\mathscr{I}\left(K_{q+1} \mid K_{q}\right)+\mathscr{I}\left(K_{\bar{c}} \mid I_{\bar{c}}\right)
$$

where $\bar{c}=\cup_{i=1}^{q} c_{i}$, then (26) will follow for $m=q+1 ; q$ steps of the second algorithm starting from $K_{0}=I$ generate matrices having the form

$$
K_{i}=\left[\begin{array}{cc}
I & 0 \\
0 & \bar{K}_{i}
\end{array}\right], \quad i=1, \ldots, q
$$

where $\tilde{K}_{i}$ is $|\bar{c}| \times|\bar{c}|$ and from the inductive hypothesis

$$
\mathscr{I}\left(K_{i} \mid I_{\bar{c}}\right)=\sum_{1}^{q} \mathscr{I}\left(\tilde{K}_{i} \mid \tilde{K}_{i-1}\right)=\sum_{1}^{q} \mathscr{I}\left(K_{i} \mid K_{i-1}\right)
$$

Turning now to the proof of (27) we remark that it follows from Lemma 4 with $a=c_{q+1}$ and $b=\bar{c}$, the relationship (20) with $Q=K_{q+1}, R=K_{q}$, and $a=c_{q+1}$ as before, and the fact that

$$
\left(K_{q}\right)_{a}=\left[\begin{array}{cc}
I & 0 \\
0 & L_{a b}
\end{array}\right]
$$

The $\log$ det terms in the definition of $\mathscr{I}$ match up by Lemma 4 and the trace terms correspond by (20) and the fact just noted.

We conclude this section with a few remarks comparing the two algorithms. When $M=I$, the main drawback of the first algorithm is the need to invert $L$ at the beginning. It is possible that a numerical inversion of $L$ could be difficult or impossible yet the second algorithm would work. This problem aside, it should be clear that the choice of which algorithm is to be favoured in any given situation is very much dependent on the number and sizes of the cliques in $\mathscr{C}$ and $\tilde{\mathscr{C}}$. However, if $\mathbf{C}$ is triangulated and $M=I$, the finite termination property of the second algorithm makes it attractive.
5. Some comments about the geometry. To give a geometric interpretation of the two algorithms it is convenient to define the "subspaces" $\mathscr{P}_{L, c}=$ $\left\{P \in \mathscr{P}: P_{c}=L_{c}\right\}, \mathscr{Q}_{M, \bar{c}}=\left\{Q \in \mathscr{P}:\left(Q^{-1}\right)_{\bar{c}}\right.$ agrees with $M_{\bar{c}}$ except on the diagonal $\}$, and $\mathscr{P}_{L, \mathscr{C}}=\cap\left\{\mathscr{P}_{L, c}: c \in \mathscr{C}\right\}, \mathscr{Q}_{M, \tilde{\mathscr{C}}}=\cap\left\{\mathscr{Q}_{M, \bar{c}}: \bar{c} \in \tilde{\mathscr{C}}\right\}$.

Equation (7) bears a resemblance to Pythagoras' theorem and clearly for all $P \in \mathscr{P}_{L, c}$ we have $\mathscr{I}(P \mid R) \geqq \mathscr{I}(Q \mid R)$ with equality iff $Q=P$. Hence one can call the matrix $Q$ the $I$-projection of $R$ on to $\mathscr{P}_{L, c}$ [see Csiszár (1975)].

Viewing the adjustment defined by $Q$ in Lemma 2 as an $I$-projection we can give an interpretation of the two cyclic algorithms as follows.

The first algorithm begins with a $K_{0} \in \mathscr{P}_{L, \mathscr{C}}$ and cycles through $\bar{c} \in \tilde{\mathscr{C}}$, $I$-projecting the current estimate of $K$ onto $\mathscr{P}_{L, \mathscr{C}} \cap \mathscr{Q}_{I, \bar{c}}$ in order to obtain the required element in $\mathscr{P}_{L, \mathscr{C}} \cap \mathscr{Q}_{I, \tilde{\mathscr{C}}}$. The fact that we are $I$-projecting follows from (ii) of Lemma 1. Using this, for all $K \in \mathscr{Q}_{I, c}$ we have

$$
\mathscr{I}\left(K^{-1} \mid R^{-1}\right)=\mathscr{I}\left(K^{-1} \mid Q\right)+\mathscr{I}\left(Q \mid R^{-1}\right)
$$

or equivalently

$$
\mathscr{I}(R \mid K)=\mathscr{I}\left(Q^{-1} \mid K\right)+\mathscr{I}\left(R \mid Q^{-1}\right)
$$

and so $\mathscr{I}(R \mid K) \geqq \mathscr{I}\left(R \mid Q^{-1}\right)$ for all $K \in \mathscr{Q}_{I, c}$ with equality iff $K=Q^{-1}$.
For the second algorithm we begin with $K_{0} \in \mathscr{Q}_{M, \tilde{\mathscr{C}}}$ and cycle through $c \in \mathscr{C}$, $I$-projecting the current estimate $K$ onto $\mathscr{Q}_{M, \tilde{\mathscr{C}}} \cap \mathscr{P}_{L, c}$.

Both of the above algorithms are analogous to computing the projection onto the intersection of nonorthogonal (linear) subspaces by successively projecting onto each subspace [see for example von Neumann (1950, Chapter 13)].

Acknowledgment. The referees made many valuable suggestions and are warmly thanked for their contribution.
