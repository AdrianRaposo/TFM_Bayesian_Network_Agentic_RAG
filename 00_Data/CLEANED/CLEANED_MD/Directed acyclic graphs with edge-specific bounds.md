# Directed acyclic graphs with edge-specific bounds 

By TYLER J. VANDERWEELE<br>Department of Epidemiology, Harvard School of Public Health, 677 Huntington Avenue, Boston, Massachusetts 02115, U.S.A.<br>tvanderw@hsph.harvard.edu

## AND ZHIQIANG TAN

Department of Statistics, Rutgers, The State University of New Jersey, 110 Frelinghuysen Road, Piscataway, New Jersey 08854, U.S.A.
ztan@stat.rutgers.edu

## Summary

We give a definition of a bounded edge within the causal directed acyclic graph framework. A bounded edge generalizes the notion of a signed edge and is defined in terms of bounds on a ratio of survivor probabilities. We derive rules concerning the propagation of bounds. Bounds on causal effects in the presence of unmeasured confounding are also derived using bounds related to specific edges on a graph. We illustrate the theory developed by an example concerning estimating the effect of antihistamine treatment on asthma in the presence of unmeasured confounding.

Some key words: Bayesian network; Bound; Causal inference; Confounding; Directed acyclic graph.

## 1. Introduction

Building on Wellman (1990), VanderWeele \& Robins $(2009,2010)$ developed theory for signed causal directed acyclic graphs and derived results that relate signed edges to causal effects, to covariance amongst variables, and to the sign of the bias that results when unmeasured confounding is present. Signed edges amount to statements about ratios of survivor probabilities, that the ratios are bounded either between 0 and 1 for negative edges or between 1 and $\infty$ for positive edges, but in certain cases these bounds may be too restrictive. If, for example, the bounds for the ratio are of the form $(a, b)$ with $a<1<b$ and thus include 1 rather than being bounded above or below by 1 , a signed edge cannot be assigned. In other cases, the ratios might be known to lie in ranges of the form $(c, 1)$ or $(1,1 / c)$, where $0<c<1$. In this paper, we generalize the definitions for a weak monotonic effect and a signed edge given by VanderWeele \& Robins (2010) to the case of bounded edges and derive results concerning these bounded edges.

## 2. CAUSAL DIRECTED ACYCLIC GRAPHS AND SIGNED EDGES

A directed graph (Spirtes et al., 1993; Pearl, 1995, 2000; Dawid, 2002) consists of a set of nodes and directed edges amongst nodes. A path is a sequence of distinct nodes connected by edges regardless of arrowhead direction; a directed path is a path which follows the edges in the direction indicated by the graph's arrows. A directed acyclic graph is a directed graph in which no node has a directed path back to itself. The nodes with directed edges into a node

$A$ are said to be the parents of $A$; the nodes into which there are directed edges from $A$ are said to be its children. We say that node $A$ is an ancestor of node $B$ if there is a directed path from $A$ to $B$, and $B$ is then called a descendant of $A$. A node is called a collider for a particular path if both the preceding and subsequent nodes on the path have directed edges going into it. A path between two nodes, $A$ and $B$, is said to be blocked given some set of nodes $C$ if either there is a variable in $C$ on the path that is not a collider for the path or if there is a collider on the path such that neither the collider itself nor any of its descendants are in $C$. For disjoint sets of nodes $A, B$ and $C$, we say that $A$ and $B$ are $d$-separated given $C$ if every path from any node in $A$ to any node in $B$ is blocked given $C$. Directed acyclic graphs are sometimes used as statistical models to encode independence relationships amongst variables represented by the nodes on the graph (Lauritzen, 1996). We will use the notation $A \Perp B \mid C$ to denote that $A$ is conditionally independent of $B$ given $C$. The variables corresponding to the nodes on a graph are said to satisfy the global Markov property for the directed acyclic graph if for any disjoint sets of nodes $A, B, C$ we have that $A \Perp B \mid C$ whenever $A$ and $B$ are $d$-separated given $C$.

Directed acyclic graphs can be interpreted as representing causal relationships (Spirtes et al., 1993; Pearl, 1995, 2000; Dawid, 2002). Let $Y_{a}$ denote the counterfactual value of $Y$ under an intervention to set $A$ to $a$. Pearl (1995) defined a causal directed acyclic graph as a directed acyclic graph with nodes $\left(X_{1}, \ldots, X_{n}\right)$ corresponding to variables such that each variable $X_{i}$ is given by its nonparametric structural equation $X_{i}=f_{i}\left(\mathrm{pa}_{i}, \epsilon_{i}\right)$ where $\mathrm{pa}_{i}$ are the parents of $X_{i}$ on the graph and the $\epsilon_{i}$ are mutually independent. These structural equations generalize the path analysis and linear structural equation models (Pearl, 1995, 2000) developed by Wright (1921) in the genetics literature and Haavelmo (1943) in the econometrics literature. The structural equations encode counterfactual relationships amongst the variables represented on the graph, themselves representing one-step ahead counterfactuals, with other counterfactuals given by recursive substitution. On a causal directed acyclic graph, a node $C$ is said to be a common cause of $A$ and $Y$ if there exists a directed path from $C$ to $Y$ not through $A$ and a directed path from $C$ to $A$ not through $Y$. The requirement that the $\epsilon_{i}$ be mutually independent is essentially a requirement that there is no variable absent from the graph which, if included on the graph, would be a parent of two or more variables (Pearl, 1995, 2000). A causal directed acyclic graph defined by nonparametric structural equations satisfies the global Markov property as stated above (cf. Verma \& Pearl, 1988; Geiger et al., 1990; Lauritzen et al., 1990; Pearl, 2000). We will say that $\left(V_{1}, \ldots, V_{n}\right)$ constitutes an ordered list if $i<j$ implies that $V_{i}$ is not a descendant of $V_{j}$. On some graphs there will be more than one possible ordering. The results below will apply provided that there is some ordering under which the conditions of the propositions and theorems are satisfied. We will use $\bar{V}_{k}$ to denote $\left(V_{1}, \ldots, V_{k}\right)$, with $\bar{V}_{0}=\emptyset$. For further discussion of the causal interpretation of directed acyclic graphs see Spirtes et al. (1993), Pearl (1995, 2000), Dawid (2002) and Robins (2003).

The directed acyclic graph causal framework has proved to be particularly useful in determining whether conditioning on a given set of variables, or none at all, is sufficient to control for confounding. The most important result in this regard is the back-door path criterion (Pearl, 1995). A back-door path from some node $A$ to another node $Y$ is a path into $Y$ which begins with a directed edge into $A$; a front-door path from $A$ to $Y$ is a path into $Y$ which begins with a directed edge emanating from $A$. Pearl (1995) showed that for intervention variable $A$ and outcome $Y$, if a set of variables $X$ is such that no variable in $X$ is a descendant of $A$ and such that $X$ blocks all back-door paths from $A$ to $Y$ then $Y_{a} \Perp A \mid X$, so that conditioning on $X$ suffices to control for confounding for the estimation of the causal effect of $A$ on $Y$. We will use the idea of a back-door path throughout the paper.

Some of the results below only make reference to conditional probability distributions rather than counterfactuals and thus do not require a causal interpretation of directed acyclic graphs. Nevertheless, we believe the results in this paper will be of greatest interest in drawing inferences concerning causal effects.

If $v$ is a vector, then we will say some function $f(v)$ is nondecreasing in $v$ if it is nondecreasing in each component of $v$. If $A$ is a parent of $Y$, we will use $\mathrm{pa}_{Y}^{A}$ to denote the parents of $Y$ other than $A$. Throughout, we assume that the conditional distributions used are well defined (e.g., Billingsley, 1995, §33). For example, we assume that $\operatorname{pr}\left(Y \leqslant y \mid A=a, \mathrm{pa}_{Y}^{A}\right)$ as a function of $y$ for fixed $a$ and $\mathrm{pa}_{Y}^{A}$ is a proper cumulative distribution function. By convention, we interpret the fraction $y / 0$ as infinite for any $y>0$.

VanderWeele \& Robins $(2009,2010)$ gave the following definitions for a weak monotonic effect and a signed edge on a causal directed acyclic graph (cf. Wellman, 1990).

Definition 1. We say that $A$ has a weak positive monotonic effect on $Y$ if the survivor function $S\left(y \mid a, \mathrm{pa}_{Y}^{A}\right)=\operatorname{pr}\left(Y>y \mid A=a, \mathrm{pa}_{Y}^{A}\right)$ is such that whenever $a_{1} \geqslant a_{0}$ we have $S(y \mid$ $\left.a_{1}, \mathrm{pa}_{Y}^{A}\right) \geqslant S\left(y \mid a_{0}, \mathrm{pa}_{Y}^{A}\right)$ for all $y$ and all $\mathrm{pa}_{Y}^{A}$, and a weak negative monotonic effect if whenever $a_{1} \geqslant a_{0}$ we have $S\left(y \mid a_{1}, \mathrm{pa}_{Y}^{A}\right) \leqslant S\left(y \mid a_{0}, \mathrm{pa}_{Y}^{A}\right)$ for all $y$ and all $\mathrm{pa}_{Y}^{A}$.

Corresponding to the notion of a weak monotonic effect is that of a signed edge.
Definition 2. An edge on a causal directed acyclic graph from $A$ to $Y$ is said to be of positive or negative sign if, respectively, $A$ has a weak positive or negative monotonic effect on $Y$; otherwise, it is without sign. The sign of a path is the product of the signs of the edges that constitute that path; the path is without sign if one of the path's edges is without sign.

The definition of a weak positive monotonic effect requires that for all $a_{1} \geqslant a_{0}$ such that at least one of $S\left(y \mid a_{1}, \mathrm{pa}_{Y}^{A}\right)$ or $S\left(y \mid a_{0}, \mathrm{pa}_{Y}^{A}\right)$ is nonzero, $1 \leqslant S\left(y \mid a_{1}, \mathrm{pa}_{Y}^{A}\right) / S\left(y \mid a_{0}, \mathrm{pa}_{Y}^{A}\right) \leqslant \infty$; a weak negative monotonic effect requires that for all $a_{1} \geqslant a_{0}$ such that at least one of $S(y \mid$ $\left.a_{1}, \mathrm{pa}_{Y}^{A}\right)$ or $S\left(y \mid a_{0}, \mathrm{pa}_{Y}^{A}\right)$ is nonzero, $0 \leqslant S\left(y \mid a_{1}, \mathrm{pa}_{Y}^{A}\right) / S\left(y \mid a_{0}, \mathrm{pa}_{Y}^{A}\right) \leqslant 1$ whenever $a_{1} \geqslant a_{0}$. The restriction that such inequalities only need to be satisfied when either the numerator or the denominator is nonzero will be assumed to apply to all ratios throughout and this condition will not be repeatedly stated.

# 3. BOUNDED EDGES AND THE PROPAGATION OF BOUNDS 

We now give a definition for a bounded edge that generalizes the notion of a signed edge.
Definition 3. For some node $Y$ with parent $A$ we will say that the $A \rightarrow Y$ edge is stochastically bounded by $\left(\Lambda^{-}, \Lambda^{+}\right)$if

$$
\Lambda^{-} \leqslant \frac{\operatorname{pr}\left(Y>y \mid A=a_{1}, \mathrm{pa}_{Y}^{A}\right)}{\operatorname{pr}\left(Y>y \mid A=a_{0}, \mathrm{pa}_{Y}^{A}\right)} \leqslant \Lambda^{+}
$$

for all $a_{1}>a_{0}, y$ and $\mathrm{pa}_{Y}^{A}$. If the $A \rightarrow Y$ edge is stochastically bounded by $\left(\Lambda^{-}, \Lambda^{+}\right)$, then we write $\Theta(A, Y)=\left(\Lambda^{-}, \Lambda^{+}\right)$and place the ordered set $\left(\Lambda^{-}, \Lambda^{+}\right)$on the $A \rightarrow Y$ edge of the directed acyclic graph. If there is no edge from $A$ to $Y$ on the graph then we define $\Theta(A, Y)=(1,1)$.

We will refer to a directed acyclic graph with bounds placed on the edges of the graph as a bounded directed acyclic graph. For any edge we must have that $0 \leqslant \Lambda^{-}<1$ and $1<\Lambda^{+} \leqslant \infty$;

the bounds $(0, \infty)$ can be placed on any edge, equivalent to an edge without bounds. By letting $y \rightarrow-\infty$ in the ratio in Definition 3, we see that the interval $\left(\Lambda^{-}, \Lambda^{+}\right)$must contain 1. If $\Theta(A, Y)=(1, b)$, then $A$ has a weak positive monotonic effect on $Y$ and the $A \rightarrow Y$ edge will be of positive sign; if $\Theta(A, Y)=(a, 1)$, then the $A \rightarrow Y$ edge will be of negative sign. If $Y$ is binary, then $\Theta(A, Y)=\left(1, \Lambda^{+}\right)$simply requires that

$$
1 \leqslant \frac{\operatorname{pr}\left(Y=1 \mid A=a_{1}, \mathrm{pa}_{Y}^{\mathrm{d}}\right)}{\operatorname{pr}\left(Y=1 \mid A=a_{0}, \mathrm{pa}_{Y}^{\mathrm{d}}\right)} \leqslant \Lambda^{+}
$$

for all $a_{1}>a_{0}, \mathrm{pa}_{Y}^{\mathrm{d}}$. Definitions 1-3 all apply to any statistical graphical model that satisfies the global Markov property for a directed acyclic graph.

To develop theory on the propagation of bounds on a directed acyclic graph, we rely on the following proposition. Its proof and those of other results are given in the Appendix.

Proposition 1. For fixed $a_{0}, a_{1}$ and $q$, assume that the following conditions hold.
(a) For $i=1, \ldots, n$,

$$
\Lambda_{i}^{-} \leqslant \frac{\operatorname{pr}\left(V_{i}>v_{i} \mid \tilde{V}_{i-1}=\tilde{v}_{i-1}, A=a_{1}, Q=q\right)}{\operatorname{pr}\left(V_{i}>v_{i} \mid \tilde{V}_{i-1}=\tilde{v}_{i-1}, A=a_{0}, Q=q\right)} \leqslant \Lambda_{i}^{+}
$$

for all $v_{i}$ and $\tilde{v}_{i-1}$
(b) $\operatorname{pr}\left(V_{i}>v_{i} \mid \tilde{V}_{i-1}=\tilde{v}_{i-1}, A=a_{1}, Q=q\right)$ and $\operatorname{pr}\left(V_{i}>v_{i} \mid \tilde{V}_{i-1}=\tilde{v}_{i-1}, A=a_{0}, Q=q\right)$ are nondecreasing in $\tilde{v}_{i-1}(i=2, \ldots, n)$; and
(c) $G\left(\tilde{v}_{n}\right)$ is nondecreasing in $\tilde{v}_{n}$.

Then

$$
\prod_{i=1}^{n} \Lambda_{i}^{-} \leqslant \frac{\operatorname{pr}\left\{G\left(\tilde{V}_{n}\right)>g \mid A=a_{1}, Q=q\right\}}{\operatorname{pr}\left\{G\left(\tilde{V}_{n}\right)>g \mid A=a_{0}, Q=q\right\}} \leqslant \prod_{i=1}^{n} \Lambda_{i}^{+}
$$

for all $g$.
Proposition 1 does not require reference to a directed acyclic graph; the conclusion holds for any ordered sequence $V_{1}, \ldots, V_{n}$ that satisfies (a) and (b). The next theorem essentially says that if we can find some set $X$ that blocks all back-door paths from a node $A$ to a node $Y$, and if certain directed paths into $Y$ are signed, then bounds for the effect of $A$ on $Y$ can be derived from the bounds on the edges emanating from $A$.

Theorem 1. Suppose that $A$ is an ancestor of $Y$ and that some set $X$ of nondescendants of $A$ blocks all back-door paths from $A$ to $Y$. Let $\left(V_{1}, \ldots, V_{n}\right)$ be an ordered list of all nodes on directed paths from $A$ to $Y$ and let $V_{n+1}=Y$. We may denote the bounds on the edges from $A$ to $V_{i}$ by $\Theta\left(A, V_{i}\right)=\left(\Lambda_{i}^{-}, \Lambda_{i}^{+}\right)$for $i=1, \ldots, n+1$. If for all $i$ such that there is an edge from $A$ to $V_{i}$ all directed paths from $V_{i}$ to $Y$ are of positive sign, then for all $G\left(\tilde{v}_{n+1}\right)$ nondecreasing in $\tilde{v}_{n+1}$,

$$
\prod_{i=1}^{n+1} \Lambda_{i}^{-} \leqslant \frac{\operatorname{pr}\left\{G\left(\tilde{V}_{n+1}\right)>g \mid A=a_{1}, X=x\right\}}{\operatorname{pr}\left\{G\left(\tilde{V}_{n+1}\right)>g \mid A=a_{0}, X=x\right\}} \leqslant \prod_{i=1}^{n+1} \Lambda_{i}^{+}
$$

for $a_{1}>a_{0}$ and all $g$.
Theorem 1 allows for settings in which there is some node $V_{j}$ on a directed path from $A$ to $Y$ such that there is no edge from $A$ to $V_{j}$; in this case $\Lambda_{j}^{-}=\Lambda_{j}^{+}=1$. If for some $i$, all directed

![img-0.jpeg](img-0.jpeg)

Fig. 1. Example of the propagation of bounds.
paths from $V_{i}$ to $Y$ are of negative, rather than positive, sign and $G\left(\tilde{v}_{n+1}\right)$ is nonincreasing, rather than nondecreasing, in $v_{i}$ then, the result could still be applied by replacing $V_{i}$ with $-V_{i}$ so that all directed paths from $-V_{i}$ to $Y$ are of positive sign. The bounds $\Lambda_{i}^{-}, \Lambda_{i}^{+}$will then have to be specified so that $\Theta\left(A,-V_{i}\right)=\left(\Lambda_{i}^{-}, \Lambda_{i}^{+}\right)$. If $\Theta\left(A, V_{i}\right)$ is of form $(a, 1)$, then $\Theta\left(A,-V_{i}\right)$ is of form $(1, b)$, but $b$ is not in general $1 / a$.

VanderWeele \& Robins (2009) showed that if $X$ is a set of nondescendants of $A$ that blocked all back-door paths from $A$ to $Y$ and if all directed paths from $A$ to $Y$ are of positive sign then, $\operatorname{pr}(Y>y \mid a, x)$ is nondecreasing in $a$. If in Theorem $1 \Theta\left(A, V_{i}\right)=\left(\Lambda_{i}^{-}, \Lambda_{i}^{+}\right)$is of the form $(1, \infty)$ for all $i$, then, equivalently, under the assumptions of Theorem 1, all directed paths from $A$ to $Y$ are positive. This special case of Theorem 1 is still a generalization of the aforementioned result of VanderWeele \& Robins (2009). The reason is that under these assumptions, Theorem 1 would allow one to conclude that $\operatorname{pr}\left\{G\left(\tilde{v}_{n+1}\right)>g \mid a, x\right\}$ was nondecreasing in $a$ for any choice of the function $G\left(\tilde{v}_{n+1}\right)$ nondecreasing in $\tilde{v}_{n+1}$, rather than simply for the special choice of $G\left(\tilde{v}_{n+1}\right)$ as $G\left(\tilde{v}_{n+1}\right)=y$.

If $G\left(\tilde{v}_{n+1}\right)$ is taken as $G\left(\tilde{v}_{n+1}\right)=y$, then by Pearl's back-door path adjustment theorem (Pearl, 1995), it follows immediately from Theorem 1 that

$$
\prod_{i=1}^{n+1} \Lambda_{i}^{-} \leqslant \frac{\operatorname{pr}\left(Y_{a_{1}}>y \mid X=x\right)}{\operatorname{pr}\left(Y_{a_{0}}>y \mid X=x\right)} \leqslant \prod_{i=1}^{n+1} \Lambda_{i}^{+}
$$

We illustrate the use of Theorem 1 in the following example.
Example 1. Consider the bounded directed acyclic graph given in Fig. 1. All directed paths from $V_{1}$ to $Y$ are of positive sign and all directed paths from $V_{2}$ to $Y$ are of positive sign. The path consisting of the edge $V_{1} \rightarrow Y$ is of positive sign since $\Theta\left(V_{1}, Y\right)=(1,4)$; the path $V_{1} \rightarrow$ $V_{3} \rightarrow Y$ is of positive sign since the edge $V_{1} \rightarrow V_{3}$ is of negative sign and the edge $V_{3} \rightarrow Y$ is of negative sign and thus the product of the signs of these edges is positive. Finally, the path consisting of the edge $V_{2} \rightarrow Y$ is also of positive sign. There are edges emanating from $A$ into $V_{1}, V_{2}$ and $Y$ with bounds $\Theta\left(A, V_{1}\right)=(1,3), \Theta\left(A, V_{2}\right)=(1,2), \Theta(A, Y)=(2 / 3,2)$, and by Theorem 1 , we have for all $c$ and all $a_{1}>a_{0}$ that $2 / 3=(1)(1)(2 / 3) \leqslant \operatorname{pr}(Y>y \mid A=a_{1}, C=$ c) $/ \operatorname{pr}(Y>y \mid A=a_{0}, C=c) \leqslant(3)(2)(2)=12$ since $C$ blocks all back-door paths from $A$ to $Y$; similarly, $2 / 3 \leqslant \operatorname{pr}(Y>y \mid A=a_{1}, X=x) / \operatorname{pr}(Y>y \mid A=a_{0}, X=x) \leqslant 12$ since $X$ also blocks all back-door paths from $A$ to $Y$.

Others have tried to generalize the notion of a signed edge in order to account for additional information or numeric bounds. Parsons (1995) provides a set of possible axiomatic rules to

govern the propagation of influences on networks that can be strongly or weakly positive or negative, rather than simply positive or negative. Parsons thus extended Wellman's qualitative influence to the notion of categorical influence. Renooij \& van der Gaag (2008) have recently further developed Parsons' approach, but neither provide the generality of our notion of a bounded edge. A more related approach is that of Liu \& Wellman $(1998,2004)$ who provide bounds for a cumulative distribution function, not by bounding the ratios of survivor probabilities but by postulating that certain cumulative distribution functions stochastically dominate those in fact governing various signed edges on a graph. Their results also differ from ours in another way: while in Theorem 1 bounds of the form $\operatorname{pr}\left(Y>y \mid A=a_{1}, X=x\right) / \operatorname{pr}\left(Y>y \mid A=a_{0}, X=x\right)$ are obtained by information on bounded edges emanating from $A$, their results require bounds on the cumulative distribution functions corresponding to edges pointing into $Y$. Additional research might consider if further inferences concerning bounds would be possible if their results were combined with ours.

# 4. Bounds for causal effects in the presence of unmeasured confounding 

The following result allows us to give bounds for a causal effect in the presence of unmeasured confounding.

Theorem 2. Suppose that for some variable $A$ and some nonnegative outcome $Y$, the set $X=C \cup U$ of nondescendants of $A$ blocks all back-door paths from $A$ to $Y$, where $C$ consists of measured covariates and $U$ unmeasured covariates. Let $S^{a}=\sum_{c} E(Y \mid a, c) \operatorname{pr}(c)$. If for some $u^{\prime}$ and some $\Lambda_{L}, \Lambda_{H}>0$,

$$
\Lambda_{L} E\left(Y \mid a, u^{\prime}, c\right) \leqslant E(Y \mid a, u, c) \leqslant \Lambda_{H} E\left(Y \mid a, u^{\prime}, c\right)
$$

for all $a, c$ and $u$, then

$$
\frac{\Lambda_{L}}{\Lambda_{H}} S^{a} \leqslant E\left(Y_{a}\right) \leqslant \frac{\Lambda_{H}}{\Lambda_{L}} S^{a}
$$

For (2) to hold for $u=u^{\prime}$, the interval $\left(\Lambda_{L}, \Lambda_{H}\right)$ must contain 1.
Corollary 1. Under the assumptions of Theorem 2 we have

$$
\frac{\Lambda_{L}}{\Lambda_{H}} S^{a_{1}}-\frac{\Lambda_{H}}{\Lambda_{L}} S^{a_{0}} \leqslant E\left(Y_{a_{1}}\right)-E\left(Y_{a_{0}}\right) \leqslant \frac{\Lambda_{H}}{\Lambda_{L}} S^{a_{1}}-\frac{\Lambda_{L}}{\Lambda_{H}} S^{a_{0}}
$$

and

$$
\left(\frac{\Lambda_{L}}{\Lambda_{H}}\right)^{2} \frac{S^{a_{1}}}{S^{a_{0}}} \leqslant \frac{E\left(Y_{a_{1}}\right)}{E\left(Y_{a_{0}}\right)} \leqslant\left(\frac{\Lambda_{H}}{\Lambda_{L}}\right)^{2} \frac{S^{a_{1}}}{S^{a_{0}}}
$$

In Theorem 2, if $\Lambda_{L}$ and $\Lambda_{H}$ are known a priori from subject matter knowledge then $S^{a}=$ $\sum_{c} E(Y \mid a, c) \operatorname{pr}(c)$ can be estimated from data and thus, by using Corollary 1 , one can obtain bounds for the causal effect, $E\left(Y_{a_{1}}\right)-E\left(Y_{a_{0}}\right)$ on the additive scale, or $E\left(Y_{a_{1}}\right) / E\left(Y_{a_{0}}\right)$ on the multiplicative scale. If $\Lambda_{L}$ and $\Lambda_{H}$ are unknown, Corollary 1 could still be used in sensitivity analysis (Cornfield et al., 1959) by varying $\Lambda_{L}$ and $\Lambda_{H}$. The assumptions required for the use of these results in sensitivity analysis are much weaker than those required for other techniques (e.g., Lin et al., 1998). Bounded edges in conjunction with Theorem 1 can also be used to yield bounds for inequality (2) by means of the following proposition.

![img-1.jpeg](img-1.jpeg)

Fig. 2. Example concerning bounds for the effect of antihistamine use on asthma in the presence of unmeasured confounding.

Proposition 2. For nonnegative $Y$, if for all $y, \operatorname{pr}(Y>y \mid u, l) \leqslant \Lambda \operatorname{pr}\left(Y>y \mid u^{\prime}, l\right)$, then $E(Y \mid u, l) \leqslant \Lambda E\left(Y \mid u^{\prime}, l\right)$

If in Theorem $2, U$ is univariate and $(A, C)$ contain all parents of $Y$ other than $U$ then the bounds for the $U \rightarrow Y$ edge, say $\Theta(U, Y)=\left(\Lambda_{L}, \Lambda_{H}\right)$, will, by Proposition 2 with $L=(A, C)$, be bounds that satisfy (2) provided there is some minimum value $u^{\prime}$ of $U$. However, although the application of Proposition 2 could be used to draw conclusions about the inequality in (2), (2) is in fact weaker than what is required for a bounded edge and Theorem 2 can thus be employed more generally. For example, suppose $(A, C)$ are nondescendants of $U$ and block all back-door paths from $U$ to $Y$, although $U$ lies on a back-door path from $A$ to $Y$. Then the bounds relating $U$ and $Y$ from Theorem 1, with $U$ and $(A, C)$ taking the roles of $A$ and $X$, can be used to give bounds that satisfy (2) by Proposition 2. In the next section, we apply Theorem 2 to a problem concerning the effect of antihistamine treatment on asthma in the presence of unmeasured confounding.

# 5. Application and further discussion 

We present an example adapted from Greenland et al. (1999) and discussed by VanderWeele et al. (2008). Using bounds for edges rather than signed edges allows us to derive bounds for the causal effect under fewer assumptions.

Example 2. Consider a hypothetical study of the relation of antihistamine treatment, denoted by $A$, and asthma incidence, denoted by $Y$, among first-grade children attending public schools. Suppose that air pollution level, denoted by $W$, is independent of sex, denoted by $C$. Suppose further that sex influences the administration of antihistamine only through its relation to bronchial reactivity, denoted by $U$, but directly influences asthma risk; suppose also that air pollution leads to asthma attacks only through its influence on antihistamine use and bronchial reactivity; and that there are no important confounders beyond air pollution, bronchial reactivity and sex. The causal relationships amongst these variables are then those given in Fig. 2.

Under the assumptions given above, by Pearl's back-door path criterion conditioning on $C$ and $U$ suffices to control for confounding; conditioning on $C, U$ and $W$ or on $U$ and $W$ also suffices. If data were only available for antihistamine use $A$, asthma $Y$ and sex $C$, then we could not produce valid estimates of the causal effect of $A$ on $Y$ because controlling only for $C$ does not suffice to control for confounding. Suppose now that, for the purposes of this study, asthma and bronchial reactivity can be considered binary, comparing high versus low, and that $1 \leqslant \operatorname{pr}(Y=1 \mid a, U=1, c) / \operatorname{pr}(Y=1 \mid a, U=0, c) \leqslant 2$ for all $a, c$. In other words, high bronchial reactivity increases the likelihood of asthma by a factor somewhere between 1 and 2

for all levels of antihistamine treatment for both males and females. Suppose that in the analysis of the available data it was found that $S^{1}=\sum_{c} E(Y \mid A=1, C=c) \operatorname{pr}(C=c)=0 \cdot 06$ and $S^{0}=\sum_{c} E(Y \mid A=0, C=c) \operatorname{pr}(C=c)=0 \cdot 25$. From Corollary 1 we have that

$$
\frac{1}{2} S^{1}-2 S^{0} \leqslant E\left(Y_{a=1}\right)-E\left(Y_{a=0}\right) \leqslant 2 S^{1}-\frac{1}{2} S^{0}
$$

and thus, $-0.47 \leqslant E\left(Y_{a=1}\right)-E\left(Y_{a=0}\right) \leqslant-0.005$. We could then conclude from this study that antihistamine use truly had a beneficial effect on asthma. To draw conclusions about bounds for the causal effect using signed edges, VanderWeele et al. (2008) had to assume that the $W \rightarrow U$, $W \rightarrow A, U \rightarrow A$ and $U \rightarrow Y$ edges all had positive sign. From these assumptions, they concluded that $E\left(Y_{a=1}\right)-E\left(Y_{a=0}\right) \leqslant S^{1}-S^{0}$ and from this it follows that $E\left(Y_{a=1}\right)-E\left(Y_{a=0}\right) \leqslant 0 \cdot 06-$ $0.25=-0.19$. The application of Theorem 2 required assumptions about bounds related to only one edge, namely the $U \rightarrow Y$ edge.

As is clear from Example 2, Theorem 2 in this paper allows the researcher to draw conclusions about bounds on causal effects in the presence of unmeasured confounding by making assumptions concerning fewer edges than were previously required. VanderWeele et al. (2008) showed that to draw conclusions about the sign of the bias in the presence of unmeasured confounding using signed edges the treatment had to be binary or comparison had to be made between the minimum and maximum levels of treatment. Intuition about the sign of the bias could fail if an intermediate level of treatment was considered. In contrast, Theorem 2 makes no assumptions on whether $A$ is binary, ordinal or continuous.

The approach employed in Example 2 to address bounds under unmeasured confounding by use of Theorem 2 is broadly applicable. In cases in which the outcome $Y$ is binary, as in many epidemiologic studies, the approach is straightforward because specifying $\left(\Lambda_{L}, \Lambda_{H}\right)$ that satisfy (2) consists only of specifying bounds on the risk ratio for the effect of $U$ on $Y$ and the inequalities in (3) of Theorem 2 then give bounds on the causal effect. By specifying bounds on the risk ratio for the effect of $U$ on $Y$ one immediately obtains bounds for the effect of $A$ on $Y$.

# Acknowledgement 

The authors thank the editor and two referees for helpful comments. VanderWeele acknowledges support from the National Institutes of Health, U.S.A. Tan acknowledges support from the National Science Foundation, U.S.A.

## APPENDIX

VanderWeele \& Robins (2009) proved Lemmas A1-A3 below, which will be used in this Appendix. Lemmas A2 and A3 are given in a somewhat more general form in VanderWeele \& Robins (2009) but these special cases will suffice for our purposes here.

Lemma A1. If $h\left(z_{2}, z_{1}, q\right)$ is nondecreasing in $z_{1}$ and in $z_{2}$ and $\operatorname{pr}\left(Z_{2}>z_{2} \mid Z_{1}=z_{1}, Q=q\right)$ is nondecreasing in $z_{1}$, for all $z_{2}$, then $E\left\{h\left(Z_{2}, z_{1}, q\right) \mid Z_{1}=z_{1}, Q=q\right\}$ is nondecreasing in $z_{1}$.

Lemma A2. Let $X$ denote some set of nondescendants of $Z_{1}$ that block all back-door paths from $Z_{1}$ to $Z_{2}$. If all directed paths between $Z_{1}$ and $Z_{2}$ are of positive sign then $\operatorname{pr}\left(Z_{2}>z_{2} \mid z_{1}, x\right)$ is nondecreasing in $z_{1}$ for all $z_{2}$ and all $x$.

Lemma A3. Suppose that $Z_{1}$ is a nondescendant of $Z_{2}$ and let $Q$ denote the union of (i) the ancestors of $Z_{1}$ and (ii) the ancestors of $Z_{2}$ which are not descendants of $Z_{1}$. Let $V_{0}=Z_{1}$ and $V_{n}=Z_{2}$ and let

$\left(V_{1}, \ldots, V_{n-1}\right)$ be an ordered list of all the nodes on directed paths from $Z_{1}$ to $Z_{2}$ exclusive of $Z_{1}$ and $Z_{2}$ then $\operatorname{pr}\left(V_{k}>v_{k} \mid z_{1}, \tilde{v}_{k-1}, q\right)=\operatorname{pr}\left(V_{k}>v_{k} \mid \mathrm{pa}_{v_{k}}\right)$ for $k=1, \ldots, n$.

Proof of Proposition 1. Note that $0 \leqslant \Lambda_{i}^{-}<\infty$ and $0<\Lambda_{i}^{+} \leqslant \infty(i=1, \ldots, n)$. We give a proof for the inequality involving $\Lambda_{i}^{-}$. The inequality involving $\Lambda_{i}^{+}$can be proved similarly by exchanging the roles of $a_{0}$ and $a_{1}$. Recall that $\tilde{V}_{k}$ denotes $\left(V_{1}, \ldots, V_{k}\right)$.

We first establish the inequality for $n=1$. Let $G^{-1}(g)=\sup \left\{v_{1}: G\left(v_{1}\right) \leqslant g\right\}$. A useful result is that (i) if $G\left\{G^{-1}(g)\right\} \leqslant g$, then $G\left(v_{1}\right)>g$ if and only if $v_{1}>G^{-1}(g)$ and that (ii) if $G\left\{G^{-1}(g)\right\}>g$, then $G\left(v_{1}\right)>g$ if and only if $v_{1} \geqslant G^{-1}(g)$. We prove (i) by contradiction. Suppose $v_{1}>G^{-1}(g)$. If $G\left(v_{1}\right) \leqslant$ $g$, then $v_{1} \leqslant G^{-1}(g)$ by the definition of $G^{-1}(g)$, which is a contradiction. Suppose $G\left(v_{1}\right)>g$. If $v_{1} \leqslant$ $G^{-1}(g)$, then $G\left(v_{1}\right) \leqslant G\left\{G^{-1}(g)\right\} \leqslant g$ since $G$ is nondecreasing in $v_{1}$, again a contradiction. To prove (ii), if $v_{1}>G^{-1}(g)$, then $G\left(v_{1}\right)>g$, because if $G\left(v_{1}\right) \leqslant g$, then $v_{1} \leqslant G^{-1}(g)$ by the definition of $G^{-1}(g)$, which is a contradiction, and if $v_{1}=G^{-1}(g)$ then $G\left(v_{1}\right)>g$. To show the converse, suppose $G\left(v_{1}\right)>g$. If $v_{1}<G^{-1}(g)$, then there exists $u_{1}$ such that $v_{1}<u_{1}<G^{-1}(g)$ and $G\left(u_{1}\right) \leqslant g$ by the definition of $G^{-1}(g)$ and this contradicts that $G$ is nondecreasing. Due to (i) and (ii), we have that $\left\{v_{1}: G\left(v_{1}\right)>g\right\}$ equals either $\left\{v_{1}: v_{1}>G^{-1}(g)\right\}$ or $\left\{v_{1}: v_{1} \geqslant G^{-1}(g)\right\}$.

Consider the case $\left\{v_{1}: G\left(v_{1}\right)>g\right\}=\left\{v_{1}: v_{1}>G^{-1}(g)\right\}$. Then $\operatorname{pr}\left\{G\left(V_{1}\right)>g \mid A=a_{1}, Q=q\right\}=$ $\operatorname{pr}\left\{V_{1}>G^{-1}(g) \mid A=a_{1}, Q=q\right\}$ and $\operatorname{pr}\left\{G\left(V_{1}\right)>g \mid A=a_{0}, Q=q\right\}=\operatorname{pr}\left\{V_{1}>G^{-1}(g) \mid A=a_{0}, Q=\right.$ $q\}$. The desired inequality is trivial by condition (a). Next, consider the case $\left\{v_{1}: G\left(v_{1}\right)>g\right\}=\left\{v_{1}\right.$ : $\left.v_{1} \geqslant G^{-1}(g)\right\}$. Then $\operatorname{pr}\left\{G\left(V_{1}\right)>g \mid A=a_{1}, Q=q\right\}=\operatorname{pr}\left\{V_{1} \geqslant G^{-1}(g) \mid A=a_{1}, Q=q\right\}$ and $\operatorname{pr}\left\{G\left(V_{1}\right)>\right.$ $\left.g \mid A=a_{0}, Q=q\right\}=\operatorname{pr}\left\{V_{1} \geqslant G^{-1}(g) \mid A=a_{0}, Q=q\right\}$. Note that $p_{1} / p_{0} \geqslant \Lambda_{1}^{-}$if and only if $p_{1} \geqslant \Lambda_{1}^{-} p_{0}$, for $0 \leqslant \Lambda_{1}^{-}<\infty$ and $0 \leqslant p_{0}, p_{1} \leqslant 1$. Let $v_{1 j}$ be a sequence increasing to $G^{-1}(g)$. Then $\operatorname{pr}\left(V_{1}>v_{1 j} \mid\right.$ $\left.A=a_{1}, Q=q\right) \geqslant \Lambda_{1}^{-} \operatorname{pr}\left(V_{1}>v_{1 j} \mid A=a_{0}, Q=q\right)$ by condition (a). Let $j \rightarrow \infty$, we obtain $\operatorname{pr}\left\{V_{1} \geqslant\right.$ $\left.G^{-1}(g) \mid A=a_{1}, Q=q\right\} \geqslant \Lambda_{1}^{-} \operatorname{pr}\left\{V_{1} \geqslant G^{-1}(g) \mid A=a_{0}, Q=q\right\}$ and thus $\operatorname{pr}\left\{G\left(V_{1}\right)>g \mid A=a_{1}, Q=\right.$ $\left.q\right\} / \operatorname{pr}\left\{G\left(V_{1}\right)>g \mid A=a_{0}, Q=q\right\} \geqslant \Lambda_{1}^{-}$.

Suppose that inequality (1) involving $\Lambda_{i}^{-}$holds for $n=k$. We show that it then holds for $n=$ $k+1$. Let $G_{i_{0}}^{-1}(g)=\sup \left\{v_{k+1}: G\left(v_{k+1}, \tilde{v}_{k}\right) \leqslant g\right\}$. Similarly as in the case for $n=1$, we have that $\left\{v_{k+1}: G\left(v_{k+1}, \tilde{v}_{k}\right)>g\right\}$ equals either $\left\{v_{k+1}: v_{k+1}>G_{i_{0}}^{-1}(g)\right\}$ or $\left\{v_{k+1}: v_{k+1} \geqslant G_{i_{0}}^{-1}(g)\right\}$ and, by condition (a), $\operatorname{pr}\left\{G\left(V_{k+1}, \tilde{v}_{k}\right)>g \mid \tilde{V}_{k}=\tilde{v}_{k}, A=a_{1}, Q=q\right\} \geqslant \Lambda_{k+1}^{-} \operatorname{pr}\left\{G\left(V_{k+1}, \tilde{v}_{k}\right)>g \mid \tilde{V}_{k}=\tilde{v}_{k}, A=a_{0}, Q=\right.$ $q\}$. Therefore,

$$
\begin{aligned}
\operatorname{pr}\left\{G\left(\tilde{V}_{k+1}\right)>g \mid A=a_{1}, Q=q\right\} & =E\left[\operatorname{pr}\left\{G\left(V_{k+1}, \tilde{V}_{k}\right)>g \mid \tilde{V}_{k}, A=a_{1}, Q=q\right\} \mid A=a_{1}, Q=q\right] \\
& \geqslant \Lambda_{k+1}^{-} E\left[\operatorname{pr}\left\{G\left(V_{k+1}, \tilde{V}_{k}\right)>g \mid \tilde{V}_{k}, A=a_{0}, Q=q\right\} \mid A=a_{1}, Q=q\right] \\
& =\Lambda_{k+1}^{-} \int_{0}^{1} \operatorname{pr}\left\{\Psi_{g}\left(\tilde{V}_{k}\right)>z \mid A=a_{1}, Q=q\right\} d z
\end{aligned}
$$

where $\Psi_{g}\left(\tilde{v}_{k}\right)=\operatorname{pr}\left\{G\left(V_{k+1}, \tilde{v}_{k}\right)>g \mid \tilde{V}_{k}=\tilde{v}_{k}, A=a_{0}, Q=q\right\}$. Since $G\left(v_{k+1}, \tilde{v}_{k}\right)$ is nondecreasing in $v_{k+1}$ and $\tilde{v}_{k}$ and since $\operatorname{pr}\left(V_{k+1}>v_{k+1} \mid \tilde{V}_{k}=\tilde{v}_{k}, A=a_{0}, Q=q\right)$ is nondecreasing in $\tilde{v}_{k}$, we have by Lemma A1 that $\Psi_{g}\left(\tilde{v}_{k}\right)$ is nondecreasing in $\tilde{v}_{k}$. Since (1) holds for $n=k$ we have that

$$
\begin{aligned}
\operatorname{pr}\left\{G\left(\tilde{V}_{k+1}\right)>g \mid A=a_{1}, Q=q\right\} & =\Lambda_{k+1}^{-} \int_{0}^{1} \operatorname{pr}\left\{\Psi_{g}\left(\tilde{V}_{k}\right)>z \mid A=a_{1}, Q=q\right\} d z \\
& \geqslant \Lambda_{k+1}^{-} \int_{0}^{1}\left(\prod_{i=1}^{k} \Lambda_{i}^{-}\right) \operatorname{pr}\left\{\Psi_{g}\left(\tilde{V}_{k}\right)>z \mid A=a_{0}, Q=q\right\} d z \\
& =\left(\prod_{i=1}^{k+1} \Lambda_{i}^{-}\right) \operatorname{pr}\left\{G\left(\tilde{V}_{k+1}\right)>g \mid A=a_{0}, Q=q\right\}
\end{aligned}
$$

and so (1) holds for $n=k+1$.

Proof of Theorem 1. Fix $a_{1}>a_{0}$. Since $\Theta\left(A, V_{i}\right)=\left(\Lambda_{i}^{-}, \Lambda_{i}^{+}\right)$we have

$$
\Lambda_{i}^{-} \leqslant \frac{\operatorname{pr}\left(V_{i}>v_{i} \mid A=a_{1}, \mathrm{pa}_{T}^{A}\right)}{\operatorname{pr}\left(V_{i}>v_{i} \mid A=a_{0}, \mathrm{pa}_{T}^{A}\right)} \leqslant \Lambda_{i}^{+}
$$

for all $v_{i}$ and $\mathrm{pa}_{T}^{A}$, where $\mathrm{pa}_{T}^{A}$ denote the parents of $V_{i}$ other than $A$. Let $Q$ denote the union of (i) the ancestors of $A$ and (ii) the ancestors of $Y$ which are not descendants of $A$ then by Lemma A3, $\operatorname{pr}\left(V_{i}>v_{i} \mid\right.$ $\left.a, \mathrm{pa}_{T}^{A}\right)=\operatorname{pr}\left(V_{i}>v_{i} \mid \tilde{v}_{i-1}, a, q\right)$ and thus

$$
\Lambda_{i}^{-} \leqslant \frac{\operatorname{pr}\left(V_{i}>v_{i} \mid \tilde{V}_{i-1}=\tilde{v}_{i-1}, A=a_{1}, Q=q\right)}{\operatorname{pr}\left(V_{i}>v_{i} \mid \tilde{V}_{i-1}=\tilde{v}_{i-1}, A=a_{0}, Q=q\right)} \leqslant \Lambda_{i}^{+} \quad(i=1, \ldots, n+1)
$$

for all $v_{i}, \tilde{v}_{i-1}, q$. Under the assumption that for all $i$ such that there is an edge from $A$ to $V_{i}$ all directed paths from $V_{i}$ to $Y$ are of positive sign, relevant nodes can be replaced by their negations so that for all $i$ such that there is an edge from $A$ to $V_{i}$ all edges on all directed paths from $V_{i}$ to $Y$ are of positive sign. By Lemma A2, $\operatorname{pr}\left(V_{i}>v_{i} \mid \tilde{V}_{i-1}=\tilde{v}_{i-1}, A=a, Q=q\right)$ is nondecreasing in $\tilde{v}_{i-1}$ for all $v_{i}, a, q$ since $(A, Q)$ will block all back-door paths from $\tilde{V}_{i-1}$ to $V_{i}$. By Proposition 1 we thus have that

$$
\prod_{i=1}^{n+1} \Lambda_{i}^{-} \leqslant \frac{\operatorname{pr}\left(G\left(\tilde{v}_{n+1}\right)>g \mid A=a_{1}, Q=q\right)}{\operatorname{pr}\left(G\left(\tilde{v}_{n+1}\right)>g \mid A=a_{0}, Q=q\right)} \leqslant \prod_{i=1}^{n+1} \Lambda_{i}^{+}
$$

for all $g$ and $q$. Furthermore,

$$
\begin{aligned}
\operatorname{pr}\left\{G\left(\tilde{v}_{n+1}\right)>g \mid A=a, X=x\right)\} & =E\left[\operatorname{pr}\left\{G\left(\tilde{v}_{n+1}\right)>g \mid A=a, X=x, Q\right\} \mid A=a, X=x\right] \\
& =E\left[\operatorname{pr}\left\{G\left(\tilde{v}_{n+1}\right)>g \mid A=a, Q\right\} \mid A=a, X=x\right] \\
& =E\left[\operatorname{pr}\left\{G\left(\tilde{v}_{n+1}\right)>g \mid A=a, W\right\} \mid A=a, X=x\right]
\end{aligned}
$$

where $W$ is the subset of $Q$ which are parents of one of the nodes in $\tilde{V}_{n+1}$. There can be no unblocked frontdoor paths from $A$ to $W$ given $X$ since the nodes in $W$ are not descendants of $A$ and thus any front-door path from $A$ to $W$ will be blocked given $X$ by a collider. All back-door paths from $A$ to $W$ are blocked given $X$ since $X$ blocks all back-door paths from $A$ to $Y$. From this it follows that all paths from $A$ to $W$ are blocked given $X$ and so $W$ is conditionally independent of $A$ given $X$ and so we have

$$
\begin{aligned}
E\left[\operatorname{pr}\left\{G\left(\tilde{v}_{n+1}\right)>g \mid A=a, W\right\} \mid A=a, X=x\right] & =E\left[\operatorname{pr}\left\{G\left(\tilde{v}_{n+1}\right)>g \mid A=a, W\right\} \mid X=x\right] \\
& =E\left[\operatorname{pr}\left\{G\left(\tilde{v}_{n+1}\right)>g \mid A=a, Q\right\} \mid X=x\right]
\end{aligned}
$$

We have thus shown that

$$
\operatorname{pr}\left\{G\left(\tilde{v}_{n+1}\right)>g \mid A=a, X=x\right\}=E\left[\operatorname{pr}\left\{G\left(\tilde{v}_{n+1}\right)>g \mid A=a, Q\right\} \mid X=x\right]
$$

By (A1) we have that

$$
\left(\prod_{i=1}^{n+1} \Lambda_{i}^{-}\right) \operatorname{pr}\left\{G\left(\tilde{v}_{n+1}\right)>g \mid A=a_{0}, Q=q\right\} \leqslant \operatorname{pr}\left\{G\left(\tilde{v}_{n+1}\right)>g \mid A=a_{1}, Q=q\right\}
$$

and

$$
\operatorname{pr}\left\{G\left(\tilde{v}_{n+1}\right)>g \mid A=a_{1}, Q=q\right\} \leqslant\left(\prod_{i=1}^{n} \Lambda_{i}^{+}\right) \operatorname{pr}\left\{G\left(\tilde{v}_{n+1}\right)>g \mid A=a_{0}, Q=q\right\}
$$

for all $g$ and $q$. Taking conditional expectations given $X=x$ of (A3) and (A4) and making use of relation (A2) we have that

$$
\left(\prod_{i=1}^{n+1} \Lambda_{i}^{-}\right) \operatorname{pr}\left\{G\left(\tilde{v}_{n+1}\right)>g \mid A=a_{0}, X=x\right\} \leqslant \operatorname{pr}\left\{G\left(\tilde{v}_{n+1}\right)>g \mid A=a_{1}, X=x\right\}
$$

and

$$
\operatorname{pr}\left\{G\left(\tilde{v}_{n+1}\right)>g \mid A=a_{1}, X=x\right\} \leqslant\left(\prod_{i=1}^{n} \Lambda_{i}^{+}\right) \operatorname{pr}\left\{G\left(\tilde{v}_{n+1}\right)>g \mid A=a_{0}, X=x\right\}
$$

for all $g$ and $x$. This completes the proof.
Proof of Theorem 2. Let $S^{a}=\sum_{c} E(Y \mid A=a, C=c) \operatorname{pr}(C=c)$. We then have that

$$
\begin{aligned}
S^{a} & =\int_{c} E(Y \mid A=a, C=c) d F(c) \\
& =\int_{c}\left\{\int_{u} E(Y \mid A=a, C=c, U=u) d F(u \mid A=a, C=c)\right\} d F(c) \\
& \leqslant \int_{c}\left\{\int_{u} \Lambda_{H} E\left(Y \mid A=a, C=c, U=u^{\prime}\right) d F(u \mid A=a, C=c)\right\} d F(c) \\
& =\Lambda_{H} \int_{c} E\left(Y \mid A=a, C=c, U=u^{\prime}\right) d F(c) \\
& =\Lambda_{H} \int_{c}\left\{\int_{u} E\left(Y \mid A=a, C=c, U=u^{\prime}\right) d F(u \mid C=c)\right\} d F(c) \\
& \leqslant \Lambda_{H} \int_{c}\left\{\int_{u} \frac{1}{\Lambda_{L}} E(Y \mid A=a, C=c, U=u) d F(u \mid C=c)\right\} d F(c) \\
& =\frac{\Lambda_{H}}{\Lambda_{L}} \int_{c, u} E(Y \mid A=a, C=c, U=u) d F(u, c) \\
& =\frac{\Lambda_{H}}{\Lambda_{L}} E\left(Y_{a}\right)
\end{aligned}
$$

Thus, $\left(\Lambda_{L} / \Lambda_{H}\right) S^{a} \leqslant E\left(Y_{a}\right)$. The proof that $E\left(Y_{a}\right) \leqslant\left(\Lambda_{H} / \Lambda_{L}\right) S^{a}$ is similar.
Proof of Proposition 2. We have that $E(Y \mid u, l)=\int_{0}^{\infty} \operatorname{pr}(Y>y \mid u, l) d y \leqslant \int_{0}^{\infty} \Lambda \operatorname{pr}\left(Y>y \mid u^{\prime}, l\right) d y=$ $\Lambda E\left(Y \mid u^{\prime}, l\right)$.
