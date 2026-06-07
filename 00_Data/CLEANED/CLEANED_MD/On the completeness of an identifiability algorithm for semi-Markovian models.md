# On the Completeness of an Identifiability Algorithm for Semi-Markovian Models 

Yimin Huang<br>huang6@cse.sc.edu<br>Marco Valtorta<br>mgv@cse.sc.edu<br>Computer Science and Engineering Department<br>University of South Carolina

July 11, 2006

#### Abstract

This paper addresses the problem of identifying causal effects from nonexperimental data in a causal Bayesian network, i.e., a directed acyclic graph that represents causal relationships. The identifiability question asks whether it is possible to compute the probability of some set of (effect) variables given intervention on another set of (intervention) variables, in the presence of nonobservable (i.e., hidden or latent) variables. It is well known that the answer to the question depends on the structure of the causal Bayesian network, the set of observable variables, the set of effect variables, and the set of intervention variables. Sound algorithms for identifiability have been proposed, but no complete algorithm is known. We show that the identify algorithm that Tian and Pearl defined for semi-Markovian models [1, 2, 3], an important special case of causal Bayesian networks, is both sound and complete. We believe that this result will prove useful to solve the identifiability question for general causal Bayesian networks.

# 1 Introduction 

This paper focuses on the feasibility of inferring the strength of cause-andeffect relationships from a causal graph [4], which is an acyclic directed graph expressing nonexperimental data and causal relationships. Because of the existence of unmeasured variables, the following identifiability questions arise: "Can we assess the strength of causal effects from nonexperimental data and causal relationships? And if we can, what is the total causal effect in terms of estimable quantities?"

The questions just given can partially be answered using a graphical approach due to Pearl and his collaborators. More precisely, graphical conditions have been devised to show whether a causal effect, that is, the joint response of any set $S$ of variables to interventions on a set $T$ of action variables, denoted $P_{T}(S)^{1}$ is identifiable or not. Those results are summarized in [4]. For example, "back-door" and "front-door" criteria and do-calculus [5]; graphical criteria to identify $P_{T}(S)$ when $T$ is a singleton [6]; graphical conditions under which it is possible to identify $P_{T}(S)$ where $T$ and $S$ are, possibly non-singleton, sets, subject to a special condition called Q-identifiability [7]. Some further study can be also found in [8] and [9].

Recently, J. Tian by himself and in collaboration with J. Pearl published a series of papers $[1,2,3,10]$ related to this topic. Their new methods combine the graphical characters of causal graph and the algebraic definition of causal effect. They used both algebraic and graphical methods to identify causal effects. The basic idea is first to transfer causal graphs to semi-Markovian graphs [2], then to use Algorithm 2 in [3] to calculate the causal effects we want to know.

Tian and Pearl's method is a great contribution to this study area, but there are still two open questions left. First, even though we believe, as Tian and Pearl do, that the semi Markovian models obtained from the transforming Projection algorithm in [2] are equal to the original causal graphs, and therefore the causal effects should be the same in both models, still, to the best of our knowledge, there is no formal proof for this equivalence. Second, the completeness question of the indentification algorithm in [3] (which we will simply call the identify algorithm from now on) is still open, so that it is unknown whether a causal effect is identifiable if the identify algorithm fails.

In this paper, we focus on the second question. Our conclusion shows that Tian and Pearl's identify algorithm on semi-Markovian models is sound and complete, which means that a causal effect on a semi-Markovian model is identifiable if and only if the given algorithm can run successfully and finally return an expression which is the target causal effect in terms of estimable quantities.

Using the result of this paper, it becomes possible to rewrite the identify algorithm on general Markovian models and prove that the new algorithm is still sound and complete. This work is not included in this paper, but we believe that we provide the foundations for the more general result.

In the next section we present the definitions and notation that we use in

[^0]
[^0]:    ${ }^{1}$ Pearl and Tian used notation $P(s \mid d o(t))$ and $P(s \mid \hat{t})$ in [4] and $P_{t}(s)$ in [2], [3].

this paper. In section three, we present some important lemmas that will be used to support the analysis of the identify algorithm. In section four, we describe the algorithm that answers the identifiability question for a special causal effect case $(Q[S])$, and show that the algorithm is sound and complete. We present the identify algorithm for general causal effect $P_{T}(S)$ in section five and show that it is also sound and complete. Conclusions are included in section six.

# 2 Definitions and Notations 

Markovian models are popular graphical models for encoding distributional and causal relationships. A Markovian model consists of a DAG $G$ over a set of variables $V=\left\{V_{1}, \ldots, V_{n}\right\}$, called a causal graph and a probability distribution over $V$, which has some constraints on it that will be specified precisely below. We use $V(G)$ to indicate that $V$ is the variable set of graph $G$. If it is clear in the context, we also use $V$ directly. The interpretation of such kind of model consists of two parts. The probability distribution must satisfy two constraints. The first one is that each variable in the graph is independent of all its non-descendants given its direct parents. The second one is that the directed edges in $G$ represent causal influences between the corresponding variables. A Markovian model for which only the first constraint holds is called a Bayesian network. This explains why Markovian models are also called causal Bayesian networks. As far as the second condition is concerned, some authors prefer to consider equation 3 (below) as definitional; others take equation 3 as following from more general considerations about causal links, and in particular the account of causality that requires that, when a variable is set, the parents of that variable be disconnected from it. See [11] and [4].

In this paper, capital letters, like $V$, are used for variable sets; lower-case letters, like $v$, stand for the instances of variable set $V$. Capital letters like $X$, $Y$ and $V_{i}$ are also used for single variables, and their values can be $x, y$ and $v_{i}$. Normally, we use $F(V)$ to denote a function on variable set $V$. An instance of this function is denoted as $F(V)(V=v)$, or $F(V)(v)$, or just $F(v)$. Because each variable is in one-to-one correspondence to one node in the causal graph, we sometimes use node or node set instead of variable and variable set.

We use $P a\left(V_{i}\right)$ to denote parent node set of variable $V_{i}$ in graph $G$ and $p a\left(V_{i}\right)$ as an instance of $P a\left(V_{i}\right) . C h\left(V_{i}\right)$ is $V_{i}$ 's children node set; $c h\left(V_{i}\right)$ is an instance of $C h\left(V_{i}\right)$.

Based on the probabilistic interpretation, we get that the joint probability function $P(v)=P\left(v_{1}, \ldots, v_{n}\right)$ can be factorized as

$$
P(v)=\prod_{V_{i} \in V} P\left(v_{i} \mid p a\left(V_{i}\right)\right)
$$

The causal interpretation of Markovian model enables us to predict the intervention effects. Here, intervention means some kind of modification of factors in product (1). The simplest kind of intervention is fixing a subset $T \subseteq V$

of variables to some constants $t$, denoted by $d o(T=t)$ or just $d o(t)$, and then the post-intervention distribution

$$
P_{T}(V)(T=t, V=v)=P_{t}(v)
$$

is given by:

$$
P_{t}(v)=P(v \mid d o(t))= \begin{cases}\prod_{V_{i} \in V \backslash T} P\left(v_{i} \mid p a\left(V_{i}\right)\right) & v \text { consistent with } t \\ 0 & v \text { inconsistent with } t\end{cases}
$$

We note explicitly that the post-intervention distribution $P_{T}(V)(T=t, V=$ $v)=P_{t}(v)$ is a probability distribution.

When all the variables in $V$ are observable, since all $P\left(v_{i} \mid p a\left(V_{i}\right)\right)$ can be estimated from nonexperimental data, all causal effects are computable. But when some variables in $V$ are unobservable, the situation is much more complex.

Let $N(G)$ and $U(G)$ (or simply $N$ and $U$ when the graph is clear from the context) stand for the sets of observable and unobservable variables in graph $G$ respectively, that is $V=N \cup U$. The observed probability distribution $P(n)=$ $P(N=n)$, is a mixture of products:

$$
P(n)=\sum_{U_{k} \in U} \prod_{V_{i} \in V} P\left(v_{i} \mid p a\left(V_{i}\right)\right)=\sum_{U_{k} \in U} \prod_{V_{i} \in N} P\left(v_{i} \mid p a\left(V_{i}\right)\right) \prod_{V_{j} \in U} P\left(v_{j} \mid p a\left(V_{j}\right)\right)
$$

The post-intervention distribution $P_{t}(n)=P_{T=t}(N=n)^{2}$ is defined as:

$$
P_{t}(n)=\left\{\begin{array}{cl}
\sum_{U_{k} \in U} \prod_{V_{i} \in N \backslash T} P\left(v_{i} \mid p a\left(V_{i}\right)\right) & \prod_{V_{j} \in U} P\left(v_{j} \mid p a\left(V_{j}\right)\right) \\
& n \text { consistent with } t \\
0 & n \text { inconsistent with } t
\end{array}\right.
$$

Sometimes what we want to know is not the post-intervention distribution for the whole $N$, but the post-intervention distribution $P_{t}(s)$ of an observable variable subset $S \subseteq N$. For those two observable variable sets $S$ and $T, P_{t}(s)=$ $P_{T=t}(S=s)$ is given by:
$P_{t}(s)= \begin{cases}\sum_{V_{l} \in(N \backslash S) \backslash T} \sum_{U_{k} \in U} \prod_{V_{i} \in N \backslash T} P\left(v_{i} \mid p a\left(V_{i}\right)\right) & \prod_{V_{j} \in U} P\left(v_{j} \mid p a\left(V_{j}\right)\right) \\ 0 & s \text { consistent with } t \\ & s \text { inconsistent with } t\end{cases}$
The identifiability question is defined as whether the causal effect $P_{T}(S)$, that is all $P_{t}(s)$ given by (6), can be determined uniquely from the distribution $P(N=n)$ given by (4), and thus independently of the unknown quantities $P\left(v_{i} \mid p a\left(V_{i}\right)\right)$ s, where $V_{i} \in U$ or $V_{j} \in U$ for some $V_{j} \in P a\left(V_{i}\right)$.

We give a formal definition of identifiability below, which follows [3].

[^0]
[^0]:    ${ }^{2}$ In this paper, we only consider the situation in which $T \subseteq N$.

A Markovian model consists of four elements

$$
M=<N, U, G_{N \cup U}, P\left(v_{i} \mid p a\left(V_{i}\right)\right)>
$$

where, (i) $N$ is a set of observable variables; (ii) $U$ is a set of unobservable variables; (iii) $G$ is a directed acyclic graph with nodes corresponding to the elements of $V=N \cup U$; and (iv) $P\left(v_{i} \mid p a\left(V_{i}\right)\right)$, is the conditional probability of variable $V_{i} \in V$ given its parents $P a\left(V_{i}\right)$ in $G$.

Definition 1 The causal effect of a set of variables $T$ on a disjoint set of variables $S$ is said to be identifiable from a graph $G$ if all the quantities $P_{t}(s)$ can be computed uniquely from any positive probability of the observed variables - that is, if $P_{t}^{M_{1}}(s)=P_{t}^{M_{2}}(s)$ for every pair of models $M_{1}$ and $M_{2}$ with $P^{M_{1}}(n)=P^{M_{2}}(n)>0$ and $G\left(M_{1}\right)=G\left(M_{2}\right)$.

This definition means that, given the causal graph $G$, the quantity $P_{t}(s)$ can be determined from the observed distribution $P(n)$ alone; the probability tables that include unobservable variables are irrelevant.

Next, we define $Q[S]$ function and c-components in causal graphs. These definitions follow [2].

Normally, when we talk about $S$ and $T$, we think they are both observable variable subsets of $N$ and mutually disjoint. So, any configuration of $S$ is consistent with any configuration of $T$, and equation 6 can be replaced by

$$
P_{t}(s)=\sum_{V_{l} \in(N \backslash S) \backslash T} \sum_{U_{k} \in U} \prod_{V_{i} \in N \backslash T} P\left(v_{i} \mid p a\left(V_{i}\right)\right) \prod_{V_{j} \in U} P\left(v_{j} \mid p a\left(V_{j}\right)\right)
$$

From now on, we will use this definition instead of equation 6.
We are sometimes interested in the causal effect on a set of observable variables $S$ due to all other observable variables. In this case, keeping the convention that $N$ stands for the set of all observable variables and $T$ stands for the set of variables whose effect we want to compute, $T=N \backslash S$, and equation 7 simplifies to

$$
P_{n \backslash s}(s)=\sum_{U_{k} \in U} \prod_{V_{i} \in S} P\left(v_{i} \mid p a\left(V_{i}\right)\right) \prod_{V_{j} \in U} P\left(v_{j} \mid p a\left(V_{j}\right)\right)
$$

In formula 8 , the subscript $n \backslash s$ indicates a configuration of the variable or variables in the set $N \backslash S$. For convenience and for uniformity with [2], we define

$$
Q[S]=P_{N \backslash S}(S)
$$

and interpret this equation as stating that the causal effect of $N \backslash S$ on $S$ is $Q[S]$.
Note that $Q[S]$ is identifiable if $Q[S]^{M_{1}}(s)=Q[S]^{M_{2}}(s)$ for every pair of models $M_{1}$ and $M_{2}$ with $Q[N]^{M_{1}}(n)=Q[N]^{M_{2}}(n)>0$ and $G\left(M_{1}\right)=G\left(M_{2}\right)$.

We define the $c$-component relation on the unobserved variable set $U$ of graph $G$ as follows. For any $U_{1} \in U$ and $U_{2} \in U$, they are related under the ccomponent relation if and only if one of conditions below is satisfied:

(i) there is an edge between $U_{1}$ and $U_{2}$,
(ii) $U_{1}$ and $U_{2}$ are both parents of the same observable node,
(iii) both $U_{1}$ and $U_{2}$ are in the c-component relation with respect to another node $U_{3} \in U$.

Observe that the c-component relation in $U$ is reflexive, symmetric and transitive, so it defines a partition of $U$. Based on this relation, we can therefore divide $U$ into disjoint and mutually exclusive c-component related parts.

A c-component (short for "confounded component," [3]) of variable set $V$ on graph $G$ consists of all the unobservable variables belonging to the same c-component related part of $U$ and all observable variables that have an unobservable parent which is a member of that c-component. According to the definition of c-component relation, it is clear that an observable node can only appear in one c-component. If an observable node has no unobservable parent, then itself is a c-component on $V$. Therefore, the c-components form a partition on all of the variables.

For any pair of variables $V_{1}$ and $V_{2}$ in causal graph $G$, if there is an unobservable node $U_{i}$ which is a parent for both of them, then path $V_{1} \leftarrow U_{i} \rightarrow V_{2}$ is called a bidirected link ${ }^{3}$. If for nodes $V_{1}, \ldots, V_{n}$, there are bidirected links between all $V_{i}, V_{i+1}, 1 \leqslant i<n$, then we say there is a bidirected path from $V_{1}$ to $V_{n}$.

We now introduce a way of reducing the size of causal graphs that preserves the answer to an identifiability question. It is more convenient to work with the reduced graphs than with the original, larger ones. Studying definition (4) and (5), we can see if there is an unobservable variable in graph $G$ that has no child, then it can be summed out in both (4) and (5) and removed. Formally, if we have a model $M=<N, U, G_{N \cup U}, P\left(v_{i} \mid p a\left(V_{i}\right)\right)>, U^{\prime} \in U$ and $U^{\prime}$ has no child in $G_{N \cup U}$, then the identification problem in $M$ is equal to the identification problem in $M^{\prime}=<N, U \backslash\left\{U^{\prime}\right\}, G^{\prime}, P^{\prime}\left(v_{i} \mid p a_{i}\right)>$, where $G^{\prime}$ is the subgraph of $G_{N \cup U}$ obtained by removing node $U^{\prime}$ and all links attached with it. $P^{\prime}\left(v_{i} \mid p a\left(V_{i}\right)\right)$ is obtained by removing all $P\left(u^{\prime} \mid p a\left(U^{\prime}\right)\right)$ in the set of conditional probability tables $P\left(v_{i} \mid p a\left(V_{i}\right)\right)$. The overall distribution (of all remaining variables) and the causal distribution (of only the observable variables) in these two models are still the same.

By repeating the transformation given above, any causal model can be transformed to a model in which each unobservable variable is an ancestor of one or more observable variables without changing the identifiability property. (This is analogous to barren node removal in Bayesian networks.) From now on in this paper, we assume that all models we study satisfy this property.

If in a Markovian model each unobserved variable is a root node with exactly two observed children, we call it a semi-Markovian model. Verma [12] defines a projection by which every Markovian model on graph $G$ can be transferred to a semi-Markovian model on graph $P J(G, V)$. Tian and Pearl [2] show

[^0]
[^0]:    ${ }^{3}$ We use this term because the three-node structure can be replaced by the two observable nodes with a special bidirected edge between them.

that $G$ and $P J(G, V)$ have the same topological relations over $V$ and the same partition of $V$ into c-components. They conclude that if $P_{T}(S)$ is identified in $P J(G, V)$, then it is identified in $G$ with the same expression. This is a very important statement. From now on in this paper we will just deal with semiMarkovian models.

In semi-Markovian models, equation 7 can be rewritten as:

$$
P_{t}(s)=\sum_{V_{i} \in(N \backslash S) \backslash T} \sum_{U_{k} \in U} \prod_{V_{i} \in N \backslash T} P\left(v_{i} \mid p a\left(V_{i}\right)\right) \prod_{V_{j} \in U} P\left(v_{j}\right)
$$

And equation 8 can be rewritten as:

$$
P_{t}(s)=Q[s]=P_{n \backslash s}(s)=\sum_{U_{k} \in U} \prod_{V_{i} \in S} P\left(v_{i} \mid p a\left(V_{i}\right)\right) \prod_{V_{j} \in U} P\left(v_{j}\right)
$$

As in Tian and Pearl [3], for the sake of convenience, we represent a semiMarkovian model with a causal graph $G$ without showing the elements of $U$ explicitly, but represent the confounding effects of $U$ variables using bidirected edges. We explicitly represent $U$ nodes only when it is necessary.

So, from know on, unless otherwise noted, all the nodes we mention are observable nodes in graph $G$. We still use $N$ to denote the set of observable nodes.

We conclude this section by giving several simple graphical definitions that will be needed later. For a given variable set $C \subseteq N$, let $G_{C}$ denote the subgraph of $G$ composed only of variables in $C$ and all the bidirected links between variable pairs in $C$. We define $A n(C)$ be the union of $C$ and the set of observable ancestors of the variables in $C$ in graph $G$ and $D e(C)$ be the union of $C$ and the set of observable descendents of the variables in $C$ in graph $G$.

An observable variable set $S \subseteq N$ in graph $G$ is called an ancestral set if it contains all its own observed ancestors (i.e., $S=A n(S)$ ).

# 3 Theorems and Lemmas 

Because our definition of $Q[S]$ is equal to the definition of $Q[S]$ in [2], Lemma 1 in [2] is still correct, and therefore we have:

Theorem 1 Let $W \subseteq C \subseteq N$. If $W$ is an ancestral set in $G_{C}$, then

$$
\sum_{V_{i} \in C \backslash W} Q[C]=Q[W]
$$

We recall that subgraph $G_{C}$ includes all variables in $C$ and the subset of the unobservable variables in $G$ for which their children are all in in $C$. The lemma says that in such a subgraph, if $W$ is a set of observable variables whose ancestor set includes no other observable variables in the subgraph, then $Q[W]$ can be calculated directly from $Q[C]$ by marginalizing variables in $C \backslash W$. In

particular, note that if $Q[C]$ is identifiable, then $Q[W]$ is also identifiable. We will exploit this observation later on.

Another very important theorem is given in [2]. We only use the first two parts of it, which are:

Theorem 2 Let $H \subseteq N$, and let $H_{1}^{\prime}, \ldots, H_{l}^{\prime}$ be c-components in the subgraph $G_{H}$. Let $H_{i}=H_{i}^{\prime} \cap N, 1 \leqslant i \leqslant l$. Then we have
(i) $Q[H]$ can be decomposed as

$$
Q[H]=\prod_{i=1}^{l} Q\left[H_{i}\right]
$$

(ii) Each $Q\left[H_{i}\right]$ is computable from $Q[H]$. Let $k$ be the number of variables in $H$, and let a topological order of variables in $H$ be $V_{1}<\ldots<V_{k}$ in $G_{H}$. Let $H^{(i)}=$ $\left\{V_{1}, \ldots, V_{i}\right\}$ be the set of variables in $H$ ordered before $V_{i}$ (including $V_{i}$ ), $i=1, \ldots, k$, and $H^{(0)}=\phi$. Then each $Q\left[H_{j}\right], j=1, \ldots, l$, is given by

$$
Q\left[H_{j}\right]=\prod_{\left\{i \mid V_{i} \in H_{j}\right\}} \frac{Q\left[H^{(i)}\right]}{Q\left[H^{(i-1)}\right]}
$$

where each $Q\left[H^{(i)}\right], i=0,1, \ldots, k$, is given by

$$
Q\left[H^{(i)}\right]=\sum_{H \backslash H^{(i)}} Q[H]
$$

Theorem 2 means that if $Q[H]$ is identifiable, then each $Q\left[H_{i}\right], 1 \leqslant i \leqslant l$, is also identifiable. In the special case for which $H=N, Q(H)=Q(N)=P(N)$, which is obviously identifiable, and therefore theorem 2 implies that $Q\left[N_{i}^{\prime} \cap N\right]$ is always identifiable for each c-component $N_{i}^{\prime}$ of a given causal graph $G$.
Lemma 1 Let $S, T \subset N$ be two disjoint sets of observable variables. If $P_{T}(S)$ is not identifiable in $G$, then $P_{T}(S)$ is not identifiable in the graph resulting from adding a directed or bidirected edge to G. Equivalently, if $P_{T}(S)$ is identifiable in $G$, then $P_{T}(S)$ is still identifiable in the graph resulting from removing a directed or bidirected edge from $G$.

Intuitively, this lemma says that unidentifiability does not change by adding links. This property is mentioned in [4]. A formal proof of this lemma for semiMarkovian model can be found in [3].

Lemma 2 Let $S, T \subset N$ be two disjoint sets of observable variables. If $S_{1}$ and $T_{1}$ are subsets of $S, T$, and $P_{T_{1}}\left(S_{1}\right)$ is not identifiable in a subgraph of $G$, which does not include nodes $S \backslash S_{1} \cup T \backslash T_{1}$, then $P_{T}(S)$ is not identifiable in the graph $G$.

Proof: Assume that $P_{T_{1}}\left(S_{1}\right)$ is not identifiable in a subgraph of $G$, which we will name $G^{\prime}$, and which does not include nodes $S \backslash S_{1} \cup T \backslash T_{1}$. We can add all nodes in $G$ but not in $G^{\prime}$ into $G^{\prime}$ as isolated nodes. Then we have (trivially) that $P_{T}(S)$ is not identifiable in this new graph. According to lemma $1, P_{T}(S)$ is not identifiable in graph $G$ either.

Lemma 3 Let $A \subset B \subset N . Q[A]$ is computable from $Q[B]$ if and only if $Q[A]_{G_{B}}$ is computable from $Q[B]_{G_{B}}$

Recall that $Q[A]=P_{V \backslash A}(A)$. The only if part of this lemma follows from lemma 2. A formal proof of the if part can be found in [3].

# 4 Identify Algorithm for $Q[S]$ 

Let $S$ be a subset of observable variables (i.e., $S \subset N$ ). Recall that $Q[S]=$ $P_{N \backslash S}(S)$. Based the theorems in the previous section, Tian and Pearl [3] gave an algorithm to solve the identifibility problem of $Q[S]$ and showed that this algorithm is sound. We present their algorithm here and show that it is also complete. We begin with a lemma.

Lemma 4 Assume that $N$ is partitioned into c-components $N_{1}, \ldots, N_{k}$ in $G$, and $S$ is partitioned into c-components $S_{1}, \ldots, S_{l}$ in graph $G_{S}$. Because each $S_{j}, j=1, \ldots, l$, is a c-component in $G_{S}$, which is a subgraph of $G$, it must be included in exactly one $N_{j}, N_{j} \in\left\{N_{1}, \ldots, N_{k}\right\} . Q[S]$ is identifiable if and only if each $Q\left[S_{j}\right]$ is identifiable in graph $G_{N_{j}}$.

Proof:
First note that, because of theorem 2 (part i), in any model on graph $G$, we have

$$
Q[S]=\prod_{j=1}^{l} Q\left[S_{j}\right]
$$

Only if part:
From lemma 3, it follows that, if each $Q\left[S_{j}\right]$ is identifiable in graph $G_{N_{j}}$, then each $Q\left[S_{j}\right]$ is identifiable from $Q\left[N_{j}\right]$ on graph $G$. When we have $Q[N]$, according to theorem 2 (part ii), we can compute all the $Q\left[N_{j}\right]$ s. So, each $Q\left[S_{j}\right]$ is identifiable from $Q[N]$. Based on equation $16, Q[S]$ is identifiable.

If part:
If one $Q\left[S_{j}\right]$ is unidentifiable in $Q\left[N_{j}\right]$ in graph $G_{N_{i}}$, then from lemma 2, we have $Q[S]$ is unidentifiable. $\square$

Let us now consider how to compute $Q\left[S_{j}\right]$ from $Q\left[N_{j}\right]$. This discussion will lead to an algorithm, expressed below as function identify.

Let $F=A n\left(S_{j}\right)_{G_{N_{j}}}$.
If $F=S_{j}$, that is, if $S_{j}$ is an ancestral set in $G_{N_{j}}$, then by theorem $1, Q\left[S_{j}\right]$ is computable as: $Q\left[S_{j}\right]=\sum_{N_{j} \backslash S_{j}} Q\left[N_{j}\right]$.

If $F=N_{j}$, we will prove (theorem 3, below) that $Q\left[S_{j}\right]$ is not identifiable in $G_{N_{j}}$.

If $S_{j} \subset F \subset N_{j}$, by theorem 1, we know $Q[F]=\sum_{N_{j} \backslash F} Q\left[N_{j}\right]$.
Assume that in the graph $G_{F}, S_{j}$ is contained in a c-component $H$. Note that $S_{j}$ must belong to one c-component. By theorem $1, Q[H]$ is computable from $Q[F]$ and is given by $Q[H]=\sum_{H \backslash S_{j}} Q[F]$. We obtain that the problem of

whether $Q\left[S_{j}\right]$ is computable from $Q\left[N_{i}\right]$ is reduced to whether $Q\left[S_{j}\right]$ is computable from $Q[H]$.

Based on lemma 3, we know that $Q\left[S_{j}\right]$ is computable from $Q\left[N_{j}\right]$ if and only if $Q\left[S_{j}\right]$ is computable from $Q\left[N_{j}\right]$ in $G_{N_{j}}$.

Using lemma 3 again, we know that $Q\left[S_{j}\right]$ is computable from $Q\left[N_{j}\right]$ in $G_{N_{j}}$ if and only if $Q\left[S_{j}\right]$ is identifiable form $Q[H]$ in graph $G_{H}$.

We now restate Tian and Pearl's algorithm [3] to obtain $Q[C]$ from $Q[T]$.
Function Identify $(C, T, Q)$
INPUT: $C \subseteq T \subseteq N, Q=Q[T], G_{T}$ and $G_{C}$ are both composed of one single $c$-component.

OUTPUT: Expression for $Q[C]$ in terms of $Q$ or FAIL.
Let $A=A n(C)_{G_{T}}$
i) If $A=C$, output $Q[C]=\sum_{T \backslash C} Q[T]$.
ii) If $A=T$, output FAIL.
iii) If $C \subset A \subset T$

1. Assume that in $G_{A}, C$ is contained in a c-component $T_{1}$.
2. Compute $Q\left[T_{1}\right]$ from $Q[A]=\sum_{T \backslash A} Q[T]$ with theorem 2
3. Output Identify $\left(C, T_{1}, Q\left[T_{1}\right]\right)$.

From the discussions above, we know that cases i) and iii) are correct. Case ii) is handled by the theorem below.

Theorem 3 In a semi-Markovian graph $G$, if

1. $G$ itself is a c-component, and
2. $S \subset N$ in $G$, and $G_{S}$ has only one c-component, and
3. All variables in $N \backslash S$ are ancestors of $S$,
then $Q[S]$ is unidentifiable in $G$.
The proof of this theorem is in appendix A.
Based on the analysis above we have
Theorem 4 The identify algorithm for computing $Q[S]$ in causal graph $G$ is sound and complete.

From theorem 4 above, the corollaries below follow.
Corollary 1 Let $S \subset N$ in graph $G$, e be an outgoing link from one $S$ node, and graph $G^{\prime}$ be the same as graph $G$ except that it does not have link e. Then $Q[S]$ is identifiable in graph $G$ if and only if $Q[S]$ is identifiable in graph $G^{\prime}$.

Proof: Since $e$ is a link exiting an $S$ node, graph $G$ and $G^{\prime}$ have the same ccomponent partition. Any c-component in $G$ is also a c-component in $G^{\prime}$, and vice versa. Graph $G_{S}$ and $G_{S}^{\prime}$ also have the same c-component partition. Any c-component in $G_{S}$ is also a c-component in $G_{S}^{\prime}$, and vice versa. From Algorithm Identify(C,T,Q), Algorithm Computing $Q[S]$, and theorem 4, we know that $Q[S]$ is identifiable in graph $G$ if and only if $Q[S]$ is identifiable in graph $G^{\prime}$.

From corollary 1, we have the following, which will be used in the next section:

Corollary 2 Let $S \subset N$ in graph $G$ and graph $G^{\prime}$ be obtained by removing all outgoing links from $S$ nodes in graph $G$. Then $Q[S]$ is identifiable in graph $G$ if and only if $Q[S]$ is identifiable in graph $G^{\prime}$.

# 5 Identify Algorithm for $P_{T}(S)$ 

Lemma 5 Assume $S \subset N$ and $T \subset N$ are disjunct node sets in graph $G,<X_{1}, X_{2}>$ is a directed link in $G, X_{1} \in S$, and $X_{2} \in S$. Assume that graph $G^{\prime}$ is obtained by removing link $<X_{1}, X_{2}>$ from graph $G$. If $P_{T}(S)$ is unidentifiable in graph $G^{\prime}$, then $P_{T}\left(S \backslash\left\{X_{1}\right\}\right)$ is unidentifiable in $G$.

The proof of this lemma is in Appendix B.
A direct ancestor set of $S$ in $G$ is a variable set $D$ such that $S \subseteq D \subseteq N$, and if node $X \in D$, then $X \in S$ or there is a directed path from $X$ to a node in $S$, and all the nodes on that path are in $D$.

Lemma 6 Assume $D$ is a direct ancestor set of node set $S$ on graph $G . \sum_{D \backslash S} Q[D]$ is identifiable if and only if $Q[D]$ is identifiable.

Proof:
If part:
By definition, if $Q[D]$ is identifiable, $\sum_{D \backslash S} Q[D]$ is identifiable.
If $Q[D]$ is unidentifiable, then we know from corollary 2 that $Q[D]$ is unidentifiable in graph $G^{\prime}$, where $G^{\prime}$ is obtained by removing from $G$ all outgoing links from nodes in $D$.

Since $D$ is a directed ancestor set of $S$, we can find an order of nodes in $D \backslash S$, say $X_{1}, \ldots, X_{k}$, for which $X_{i}, 1 \leqslant i \leqslant k$, is a parent of at least one node in $S \cup\left\{X_{1}, \ldots, X_{i-1}\right\}$ in graph $G$. Assume that for $X_{i}, 1 \leqslant i \leqslant k$, the link outgoing from $X_{i}$ that is removed from $G$ to get $G^{\prime}$ is $e_{i}$, that graph $G_{i}$ is obtained by adding link $e_{i}$ to graph $G_{i-1}$, and that $G_{0}=G^{\prime}$.

Note that $Q[D]=P_{N \backslash D}(D)$ is unidentifiable in $G^{\prime}$. From lemma 5, $P_{N \backslash D}\left(D \backslash\left\{X_{1}\right\}\right)$ is unidentifiable in graph $G_{1}$. Using this lemma again, we have $P_{N \backslash D}\left(D \backslash\left\{X_{1}, X_{2}\right\}\right)$ is unidentifiable in graph $G_{2}$, and repeating, we have $P_{N \backslash D}(S)$ is unidentifiable in graph $G_{k}$. Since $G_{k}$ is a subgraph of $G$, according to lemma $1, P_{N \backslash D}(S)$ is unidentifiable in $G$ too. and $P_{N \backslash D}(S)=\sum_{D \backslash S} P_{N \backslash D}(D)=\sum_{D \backslash S} Q[D] . \square$

Based on the lemmas above, we can get a general algorithm to solve the identifibility problem on semi-Markovian models.

Let variable set $N$ in causal graph $G$ be partitioned into c-components $N_{1}, \ldots, N_{k}$, and $S$ and $T$ be disjoint observable variable sets in $G$. According to theorem 2, we have

$$
P(N)=Q[N]=\prod_{i=1}^{k} Q\left[N_{i}\right]
$$

where each $Q\left[N_{i}\right], 1 \leqslant i \leqslant k$ is computable from $Q[N]$.
What we want to compute is:

$$
P_{t}(s)=\sum_{N \backslash(T \cup S)} P_{t}(n \backslash t)=\sum_{N \backslash(T \cup S)} Q[N \backslash T]
$$

Let $D=A n(S)_{G_{N \backslash T}}$. Since $D$ is an ancestral set in graph $G_{N \backslash T}$, theorem 1 allows us to conclude that $\sum_{N \backslash(T \cup D)} Q[N \backslash T]=Q[D]$. Therefore, we can rewrite $P_{t}(s)$ from equation (18) as:

$$
P_{t}(s)=\sum_{N \backslash(T \cup S)} Q[N \backslash T]=\sum_{D \backslash S} \sum_{N \backslash(T \cup D)} Q[N \backslash T]=\sum_{D \backslash S} Q[D]
$$

Since $D$ is a directed ancestor set of $S$, according to lemma $6, \sum_{D \backslash S} Q[D]$ is identifiable if and only if $Q[D]$ is identifiable. Now the identifiability problem of $P_{T}(S)$ is transferred to the identifiability problem of $Q[D]$, which can be solved by the algorithm in the last section.

Summarizing the discussion following lemma 6, we present the identify algorithm [3].

Algorithm Identify
INPUT: two disjoint observable variable sets $S, T \subset N$. OUTPUT: the expression for $P_{T}(S)$ or FAIL.

1. Find all c-components of $G: N_{1}, \ldots, N_{k}$.
2. Compute all $Q\left[N_{i}\right], 1 \leqslant i \leqslant k$, by theorem 2 .
3. Let $D=A n(S)_{G_{N \backslash T}}$
4. Let c-components in graph $G_{D}$ be $D_{1}, \ldots, D_{l}$.
5. For each $D_{j}, 1 \leqslant j \leqslant l$, where $D_{j} \subseteq N_{i}, 1 \leqslant i \leqslant k$, we compute $Q\left[D_{k}\right]$ by calling the function identify $\left(D_{j}, N_{i}, Q\left[N_{i}\right]\right)$. If the function returns FAIL, then stop and output FAIL.
6. Output $P_{T}(S)=\sum_{D \backslash S} \prod_{j=1}^{l} Q\left[D_{j}\right]$

Our discussion above shows:
Theorem 5 The identify algorithm for computing $P_{T}(S)$ is sound and complete.

# 6 Conclusion 

We prove that the identification algorithm given by J.Tian and J.Pearl, which can be used on semi-Markovian graphs, a special case of causal Bayesian networks, is complete. This complements the proof of soundness in [3] and is a stepping stone towards the solution of the longstanding problem of finding a sound and complete algorithm for the general identifiability question in general Bayesian networks. We conjecture that a straightforward extension of the same algorithm is sound and complete for general causal Bayesian networks.

# Appendix A 

Recall that $G_{S}$ is the subgraph of $G$ that includes all nodes in the observable node set $S$ and all bidirected links between two $S$ nodes.

Theorem 3 In a semi-Markovian graph $G$, if

1. $G$ itself is a c-component.
2. $S \subset N$ in $G$, and $G_{S}$ has only one c-component.
3. All variables in $N \backslash S$ are ancestors of $S$.
then $Q[S]$ is unidentifiable in $G$.
See Fig. 1 for an example of a graph that has the three properties in the premise of Theorem 3. Tian and Pearl [3] have proved that this theorem is true when $T$ just includes one node. Here we show that this theorem is true in the general case.

## General Unidentifiable Subgraph

For a given $G$ that satifies the properties given in theorem 3 , assume $G^{\prime}$ is a subgraph of $G$ that satisfies the three properties below

1. $G^{\prime}$ is a c-component.
2. Let the observable node set in $G^{\prime}$ be $N^{\prime}$, and let $S^{\prime}=N^{\prime} \cap S$. Then, $S^{\prime}$ is not empty and $G_{S^{\prime}}$ is a c-component.
3. $N^{\prime} \backslash S^{\prime}$ is not empty and all nodes in $N^{\prime} \backslash S^{\prime}$ are ancestors of $S^{\prime}$ in $G^{\prime}$.

Then we say that $G^{\prime}$ is an unidentifiable subgraph of $G$. From lemma 1 and lemma 2, if $Q\left[S^{\prime}\right]$ is unidentifiable in $G^{\prime}, Q[S]$ is unidentifiable in $G$. See Fig. 2 for an example.

Assume $G^{m}$ is an unidentifiable subgraph of $G$ and no subgraph of $G^{m}$ obtained by removing edges from $G^{m}$ is an unidentifiable subgraph of $G$. We say $G^{m}$ is a general unidentifiable subgraph. See Fig. 3 for an example. For any semiMarkovian graph $G$ we study here, we can find at least one general unidentifiable subgraph, and we may therefore focus on general unidentifiable subgraphs.

From now on, in this appendix, we assume the graph $G$ we studying is a general unidentifiable subgraph.

Any general unidentifiable subgraph has the four properties below:

![img-0.jpeg](img-0.jpeg)

Figure 1: A graph that satisfies the properties of Theorem 3
![img-1.jpeg](img-1.jpeg)

Figure 2: An unidentifiable subgraph of Fig. 1
![img-2.jpeg](img-2.jpeg)

Figure 3: Three general unidentifiable subgraphs of Fig. 1

Graph Property 1 If we take each bidirected link as an edge, then $G_{N}$ by itself is a free tree.

Recall that a free tree (sometimes called an unrooted tree) is a connected undirected graph with no cycles. Note that $G_{N}$ can be obtained by removing all links between observable nodes from $G$. This property says that graph $G$ is connected by bidirected links. If $|N|=m$, then we have just $m-1$ bidirected links in $G$.

Graph Property 2 If we take each bidirected link as an edge in $G_{S}$, then $G_{S}$ by itself is a free tree.

This property says that subgraph $G_{S}$ is also connected by bidirected links. If $|S|=n$, then we have just $n-1$ bidirected links in $G_{S}$.

Graph Property 3 For each $T_{i} \in T=N(G) \backslash S$, there is a unique directed path from it to an $S$ node.

This property is true because if there are two paths, we can break one of them and $T_{i}$ is still an ancestor of $S$, so $G$ is not a general unidentifiable subgraph.

This property also tells us there are just $|T|$ directed links in $G$, and each $T_{i}$ has just one directed link out from it.

Graph Property 4 There are no directed links out of $S$ nodes.

# Extension of $S$ Node 

From graph property 4, we know that no node in $S$ has outgoing links. But there are three kind of links that can enter an $S$ node $S_{j}$. The first type includes directed links from $T$ nodes to $S_{j}$, the second type includes bidirected links between $T$ nodes and $S_{j}$, and the third type includes bidirected links between $S_{j}$ and other $S$ nodes.

Lemma 7 Assume that $e$ is a first type or second type link into node $S_{j} \in S$. Add an extra $S$ node $S_{j}^{\prime}$ to graph $G$, make e point to $S_{j}^{\prime}$ instead of $S_{j}$ and add a bidirected link between $S_{j}$ and $S_{j}^{\prime}$. Call the new graph $G^{\prime}$. If $Q\left[S \cup\left\{S_{j}^{\prime}\right\}\right]$ is unidentifiable in $G^{\prime}$ then $Q[S]$ is unidentifiable in $G$.

Proof:
Note that in $G^{\prime}, S_{j}^{\prime}$ has only two links into it. One is the $e$ we are dealing with and the other is the bidirected link between $S_{j}$ and $S_{j}^{\prime}$.
A) If $e$ is a first type link, then we conclude that for $S_{j}$ in $G^{\prime}$, in addition the bidirected link between $S_{j}$ and $S_{j}^{\prime}, S_{j}$ has at least one other bidirected link get into it. (See Fig. 4).

In $G^{\prime}$, we call the observable parent of $S_{j}^{\prime} T_{0}$, the unobservable node on the bidirected link between $S_{j}^{\prime}$ and $S_{j} U_{0}$, and the another unobservable node, which is a parent of $S_{j}, U_{1} . U_{1}$ has two observable children: one is $S_{j}$, and the other we call $S_{i}$. (See Fig. 4).

![img-3.jpeg](img-3.jpeg)

Figure 4: S node extension: Case A

If $Q\left[S \cup\left\{S_{j}^{\prime}\right\}\right]$ is unidentifiable in $G^{\prime}$ then we have two models $M_{1}$ and $M_{2}$ on $G^{\prime}$ that

$$
P^{M_{1}}\left(N(G) \cup\left\{S_{j}^{\prime}\right\}\right)=P^{M_{2}}\left(N(G) \cup\left\{S_{j}^{\prime}\right\}\right)
$$

but for some $\left(t, s, s_{j}^{\prime}\right)$,

$$
P_{t}^{M_{1}}\left(s, s_{j}^{\prime}\right) \neq P_{t}^{M_{2}}\left(s, s_{j}^{\prime}\right)
$$

where $t$ is an instance of variable set $T(G)=N(G) \backslash S(G), s$ is an instance of variable set $S, s_{j}^{\prime}$ is a value for variable $S_{j}^{\prime}$. We assume in $s, S_{i}=s_{i}$ and $S_{j}=s_{j}$.

Now, we create two models $M_{1}^{\prime}$ and $M_{2}^{\prime}$ on graph $G$ based on models $M_{1}$ and $M_{2}$.

For any node $X$ in $G$, which is not in $\left\{S_{j}, U_{1}, S_{i}\right\}, k=1,2$, we define

$$
P^{M_{k}^{\prime}}(x \mid p a(X))=P^{M_{k}}(x \mid p a(X))
$$

The state space of $S_{j}$ in $M_{k}^{\prime}$ is given by $S\left(S_{j}^{\prime}\right) \times S\left(S_{j}\right)$, where $S\left(S_{j}^{\prime}\right)$ and $S\left(S_{j}\right)$ are the state spaces of $S_{j}^{\prime}$ and $S_{j}$ in $M_{k}$.

Note that the parent set of $S_{j}$ in $G$ is the parent set of $S_{j}$ in $G^{\prime}$ minus $U_{0}$ plus $T_{0}$.

The state space of $U_{1}$ in $M_{k}^{\prime}$ is defined as $S\left(U_{0}\right) \times S\left(U_{1}\right)$, where $S\left(U_{0}\right)$ and $S\left(U_{1}\right)$ are the state spaces of $U_{0}$ and $U_{1}$ in $M_{k}$.

The state space of node $S_{i}$ in $M_{k}^{\prime}$ is the same as the state space of $S_{i}$ in $M_{k}$.
Now we define:

$$
P^{M_{k}^{\prime}}\left(u_{1}^{\prime}\right)=P^{M_{k}^{\prime}}\left(\left(u_{0}, u_{1}\right)\right)=P^{M_{k}}\left(u_{0}\right) \times P^{M_{k}}\left(u_{1}\right)
$$

Here $u_{1}^{\prime}$ is an instance of $U_{1}$ in $M_{k}^{\prime}, u_{0}$ and $u_{1}$ are instances for $U_{0}$ and $U_{1}$ in $M_{k}$. We define

$$
\begin{aligned}
& P^{M_{k}^{\prime}}\left(\left(s_{j}, s_{j}^{\prime}\right) \mid t_{0},\left(u_{0}, u_{1}\right), p a^{\prime}\left(S_{j}\right)\right)= \\
& P^{M_{k}}\left(s_{j}^{\prime} \mid t_{0}, u_{0}\right) \times P^{M_{k}}\left(s_{j} \mid u_{0}, u_{1}, p a^{\prime}\left(S_{j}\right)\right)
\end{aligned}
$$

where $p a^{\prime}\left(S_{j}\right)$ is an instance of the parent set of $S_{j}$ in $G$ except for $U_{1}$ and $T_{0}$. Note that $p a^{\prime}\left(S_{j}\right)$ is also an instance of parent set of $S_{j}$ in $G^{\prime}$ except $U_{0}$ and $U_{1}$.

We also define

$$
P^{M_{k}^{\prime}}\left(s_{i} \mid p a^{\prime}\left(S_{i}\right),\left(u_{0}, u_{1}\right)\right)=P^{M_{k}^{\prime}}\left(s_{i} \mid p a^{\prime}\left(S_{i}\right), u_{1}\right)
$$

where $p a^{\prime}\left(S_{i}\right)$ is an instance of the parent set of $S_{i}$ on $G$ except $U_{1}$.
From these definitions, it follows that

$$
P^{M_{1}^{\prime}}\left(n^{\prime},\left(s_{j}, s_{j}^{\prime}\right)\right)=P^{M_{1}}\left(n^{\prime}, s_{j}, s_{j}^{\prime}\right)=P^{M_{2}}\left(n^{\prime}, s_{j}, s_{j}^{\prime}\right)=P^{M_{1}^{\prime}}\left(n^{\prime},\left(s_{j}, s_{j}^{\prime}\right)\right)
$$

where, $n^{\prime}$ is an instance of $N \backslash\left\{S_{j}\right\}$ in $G$.
But for any $\left(t, s^{\prime},\left(s_{j}, s_{j}^{\prime}\right)\right)$,

$$
P_{t}^{M_{1}^{\prime}}\left(s^{\prime},\left(s_{j}, s_{j}^{\prime}\right)\right)=P_{t}^{M_{1}}\left(s^{\prime}, s_{j}, s_{j}^{\prime}\right) \neq P_{t}^{M_{2}}\left(s^{\prime}, s_{j}, s_{j}^{\prime}\right) P_{t}^{M_{2}^{\prime}}\left(s^{\prime},\left(s_{j}, s_{j}^{\prime}\right)\right)
$$

where, $s^{\prime}=s \backslash\left\{s_{j}\right\}$. Therefore, $Q[S]$ is unidentifiable in $G$.
B) If $e$ is alink of the second type, note that in $G^{\prime}, S_{j}$ may just has only one unobservable parent, the one on the bidirected link between $S_{j}$ and $S_{j}^{\prime}$. This happens when $S$ just has one node.

Call $U_{1}$ the unobservable node on the bidirected link between $S_{j}^{\prime}$ and $S_{j}$, and call $U_{0}$ the unobservable node that is parent of $S_{j}^{\prime}$ and of the $T$ node $T_{0}$.

Just as in case A, we can construct new models of $G$ based on models for $G^{\prime}$. We define models for $G$ by letting the state space of $U_{1}$ be the product of $U_{0}$ and $U_{1}$ in models for $G^{\prime}$, and by letting the state space of $S_{j}$ be the product of the state spaces of $S_{j}^{\prime}$ and $S_{j}$ in models for $G^{\prime}$.
![img-4.jpeg](img-4.jpeg)

Figure 5: S node extension: Case B

From this point on, the proof of the lemma for case B is analogous to that for case A. $\square$

From the lemma above, and noting that this kind of extension will not affect the four graph properties of general unidentifiable subgraphs, the graph $G$ we are studying satisfies also the property below:

Graph Property 5 Any $S$ node connected with a $T$ node through a directed link or a bidirected link has just two incoming links. One link is connected to a $T$ node, and the other link is a bidirected link connected to another $S$ node.

In Fig. 6, we present the process of $S$ node extension on graph $B$ of Fig. 3.
![img-5.jpeg](img-5.jpeg)

Figure 6: S node extension example

From now on, we assume the graph $G$ we study satisfies all these five graph properties.

# Math Properties 

Next, we need some math knowledge.
Math Property 1 Assume we have a number $a, 0.5<a<1$, then for any $c, 1-a<$ $c<a$, we can always find a number $b, 0<b<1$, to make that $a b+(1-a)(1-b)=c$.

Proof: from $a b+(1-a)(1-b)=c$, we can get $b=(c+a-1) /(2 a-1)$. Since $c+a-1>0$ and $c+a<2 a$, we have $0<b<1 . \square$

Math Property 2 For given $0.5<m<1, n>0$, if we have $0.5<m+n<1$, then we can find $a, b, c$, such that $0.5<a<1,0<b<1,0<c<1, c \neq 1-b$, $a b+(1-a)(1-b)=m$, and $a c+(1-a)(1-c)=n$.

Proof: Assign a value in $(1-n / 2,1)$ to $a$. Note that $0.5<m$ and $m+n<1$, and therefore $0.5<a<1$ and $a>m$. From math property 1 , we can find $b$

such that $a b+(1-a)(1-b)=m$. Since $1-a<n / 2<n<1-n<a$, using math property 1 again, we can find $c$ such that $a c+(1-a)(1-c)=n$.

If we have $c=1-b$, then

$$
\begin{aligned}
& m+n=a b+(1-a)(1-b)+a c+(1-a)(1-c)= \\
& a b+(1-a)(1-b)+a(1-b)+(1-a) b= \\
& a+1-a=1
\end{aligned}
$$

But this is impossible because $m+n<1$.
Math Property 3 If we have $a, b$, and $c$ such that $0.5<b<a<1$, and $c a+(1-$ $c)(1-a)=b$, then $0.5<c<1$. If we have $a, b$, and $c$ such that $0<a<b<0.5$, and $c a+(1-c)(1-a)=b$, then $0.5<c<1$.

Proof: For the first part, from $c a+(1-c)(1-a)=b$, we have $c=(b+a-$ 1) $/(2 a-1)$. From this, $b+a-1>0$, and $2 a-1>0$, we obtain $c>0$. Also, $b+a-1<2 a-1$, so $c<1$, and since $(2 a-1) / 2=a-1 / 2<a-1 / 2+b-1 / 2=$ $b+a-1$, we obtain $c>0.5$.

For the second part, from $c a+(1-c)(1-a)=b$, we have $c=(1-b-a) /(1-$ $2 a)$. From this, $1-b-a>0$, and $1-2 a>0$, we obtain $c>0$. Also, $1-b-a<$ $1-2 a$, so $c<1$, and since $(1-2 a) / 2=1 / 2-a<1 / 2-a+1 / 2-b=1-b-a$, we obtain $c>0.5$. $\square$

Math Property 4 If we have two numbers $a, b$, with $0<a<0.5$ and $0.5<b<1$, then $a b+(1-a)(1-b)<0.5$.

Proof: we have

$$
\begin{aligned}
& 0.5-(a b+(1-a)(1-b))= \\
& 0.5-(a b+1-a-b+a b)= \\
& b-2 a b-0.5+a= \\
& b(1-2 a)-0.5(1-2 a)= \\
& (1-2 a)(b-0.5)>0
\end{aligned}
$$

Math Property 5 If we have a number a such that $0.5<a<1$, and two numbers $b, c \in(0,1)$ then $a b+(1-a)(1-b)=a c+(1-a)(1-c)$ if and only if $b=c$

Proof: we have.

$$
\begin{aligned}
& a b+(1-a)(1-b)=a c+(1-a)(1-c) \Longleftrightarrow \\
& a b-a c+(1-a)(1-b)-(1-a)(1-c)=0 \Longleftrightarrow \\
& a(b-c)+(1-a)(b-c)=0 \Longleftrightarrow \\
& b-c=0 \Longleftrightarrow \\
& b=c
\end{aligned}
$$

Math Property 6 Assume that we have positive numbers $c, d, 0.5<c<1$ and $c+d<1$. Then, for any number $n \in[0.5, c)$ we can always find a number $a$, $0<a<1$, such that: $a \times c+(1-a) \times d=n$

Proof: from $a \times c+(1-a) \times d=n$, we get $a=(n-d) /(c-d)$. From $c+d<1$ and $c>0.5$, we obtain $d<0.5$, and therefore $c>d$, and $c-d>0$. We also have $n-d>0$ and $n-d<c-d$ when $n \in[0.5, c)$. Therefore $0<a=(n-d) /(c-d)<1$.

# $E G$ Graph and $E G^{S}$ graph 

To prove that all graphs that satisfy the 5 graph properties are unidentifiable, we first show that a class of special graphs, which we call $E G$ graphs, are unidentifiable. Then we extend the result to show that all graphs that satisfy the five graph properties are also unidentifiable.

Let $G$ be a graph that satisfies the five graph properties. We define how to construct $E G$ from $G$ first.

Based on graph property 5 , the node set $S$ of $G$ can be divided into three disjunct sets: $S=S^{d} \cup S^{m} \cup S^{i}$. Here $S^{d}$ contains exactly the $S$ nodes that have a $T$ node as parent. $S^{i}$ contains exactly the $S$ nodes that have bidirected links with $T$ nodes. $S^{m}=S \backslash\left\{S^{d} \cup S^{i}\right\}$ contains exactly the $S$ nodes that have no directed link or bidirected link from any $T$ node.

Note that $\left|S^{i}\right|>0$, because $G$ is a c-component.
Assume that in graph $G, S^{i}=\left\{S_{1}^{i}, S_{2}^{i}, \ldots, S_{n_{1}}^{i}\right\}$, and these nodes are connected with $T$ nodes $T_{1}, T_{2}, \ldots, T_{n_{1}}$ with bidirected links. Graph $E G(G)$ is obtained by adding $n_{1}-1$ bidirected links between $\left(T_{1}, T_{j}\right), j=2, \ldots, n_{1}$ on $G$. See Fig. 7 for an example.
![img-6.jpeg](img-6.jpeg)

Figure 7: EG graph for extension result of Fig. 6

So, for any graph $G$ that satisfies the five graph properties given above, we can generate an $E G$ graph $E G(G)$. Any graph that can be constructed in the way just described from a graph $G$ that satisfies the 5 properties is called a $E G$ graph. If in graph $G,\left|S^{i}\right|=1$, then $E G(G)=G$, and we call any graph that satisies this property an $E G^{S}$ graph. We have $E G^{S} \subset E G$.

Note that for any $E G$ graph $G$, when we take bidirected links as edges, $G_{T}$ is a free tree and a c-component. For observable nodes $T_{1}, T_{2} \in T$ in graph $G$, there is a unique bidirected path from $T_{1}$ to $T_{2}$ that includes only nodes in $T$.

Also note that for any $E G$ graph with $\left|S_{i}\right|=n_{1}$, if we remove $n_{1}-1 S_{i}$ nodes and the bidirected links attached with them, we get an $E G^{S}$ graph. We will exploit this property in our model construction later.

![img-7.jpeg](img-7.jpeg)

Figure 8: $E G^{S}$ graph obtained by removing node $S_{3}$ in Fig. 7

# Unidentifiability of $E G$ Graphs 

## Model Construction

Assume that, in graph $G,\left|S^{i}\right|=n_{1},\left|S^{m}\right|=n_{2},\left|S^{d}\right|=n_{3}$, and $|T|=n_{4}$. Based on the graph property 1 and the construction of $E G$ graphs, the number of unobservable nodes (equivalently, bidirected links) in graph $E G(G)$ is $m=$ $n_{1}+n_{2}+n_{3}+n_{4}-1+n_{1}-1$.

To show that any $E G$ graph is unidentifiable, we create two models $M_{1}$ and $M_{2}$ and show that they have different causal effects on $P_{t}(s)$ but the same probabilities on the observable variables.

We define a function $c f(v)$, where $v$ is an instance of vector $v=\left(v_{1}, \ldots, v_{k}\right)$, as

$$
c f(v)=\sum_{i=1}^{k} v_{i}
$$

Our construction for $M_{1}$ and $M_{2}$ is as below:
For the models we create, we assume all the variables are binary, with state space $(0,1)$, and for each unobservable node $U_{j}, P^{M_{i}}\left(u_{j}=0\right)=1 / 2, i \in\{1,2\}$, and $j \in\{1, \ldots, m\}$.

We assign a value $0<\nu_{x}<1$ to each observable node $X \in T \cup S^{m}$, and

$$
\left\{\begin{array}{ll}
P^{M_{i}}(X=x \mid p a(X))=\nu_{x} & \text { if } c f((p a(X), x)) \bmod 2=0 \\
P^{M_{i}}(X=x \mid p a(X))=1-\nu_{x} & \text { if } c f((p a(X), x)) \bmod 2=1
\end{array}\right.
$$

where $(p a(X), x)$ is a vector obtained by adding $x$ at the end of vector $p a(X)$.
![img-8.jpeg](img-8.jpeg)

Figure 9: A node with three parents

Example 1 In Fig. 9, node $X$ has three parents, and the CPT of $X$ is as follows:


We also assign a value $0<\nu_{x}<1$ to each node $X \in S^{d}$. Note that $X$ has just two parents. Assume $T_{x} \in T$ is a parent of $X$, and $U_{x}$ is the other parent. We define:


Note that $P^{M_{k}}\left(X=1 \mid t_{x}, u_{x}\right)=1-P^{M_{k}}\left(X=0 \mid t_{x}, u_{x}\right)$.
We assign two values $0<\nu_{x}^{1}<1$ and $0<\nu_{x}^{2}<1, \nu_{x}^{1} \neq 1-\nu_{x}^{2}$ with each node $X \in S^{i}$. Note that $X$ has two unobservable parents. Assume $U_{1}$ is the parent on the bidirected link between $X$ and a $T$ node, and $U_{2}$ is the other parent, which is on the bidirected link between $X$ and an $S$ node. We define:


Note that $P^{M_{k}}\left(X=1 \mid u_{1}, u_{2}\right)=1-P^{M_{k}}\left(X=0 \mid u_{1}, u_{2}\right)$.

# Construction Properties 

Here are some properties of this construction.

First, for each node $X \in T \cup S^{m}$ and for any unobservable node $U^{\prime} \in P a(X)$,

$$
\sum_{U^{\prime}} P^{M_{i}}(X=x \mid p a(X))=1
$$

Second, for each node $X \in S^{d}$ and for $U_{x} \in P a(X)$,

$$
\sum_{U_{x}} P^{M_{i}}\left(X=x \mid t_{x}, u_{x}\right)=1
$$

Third, for each node $X \in S^{i}$ and for $U_{2} \in P a(X)$,

$$
\sum_{U_{2}} P^{M_{i}}\left(X=x \mid u_{1}, u_{2}\right)=1
$$

This means that if we marginalize over the $U_{2}$ node, which is the $U$ node on the $S$ side, we obtain 1 .

Recall that $n_{1}+n_{2}+n_{3}+n_{4}$ is the number of observable variables, and therefore $|U|=2 n_{1}+n_{2}+n_{3}+n_{4}-2$ in any $E G$ graph.
Lemma 8 Under the construction above, if we can find parameter values for which

$$
P^{M_{k}}(T=0, S=0)=\sum_{U} \prod_{v \in T \cup S \cup U} P(v \mid p a(v))=(1 / 2)^{n_{1}+n_{2}+n_{3}+n_{4}}
$$

then for any $(s, t)$, we have $P^{M_{k}}(T=t, S=s)=(1 / 2)^{n_{1}+n_{2}+n_{3}+n_{4}}$, and $P^{M_{1}}(N)=$ $P^{M_{2}}(N)$ is always satisfied.

Proof: Since $P(u)=1 / 2$ for all unobservable variables, we just need to show that when $t=0, s=0$,

$$
\sum_{U} \prod_{V \in T \cup S} P(v \mid p a(v))=1 / 2 \times 2^{n_{1}-1}
$$

holds for any $(t, s)$ pair if it holds for $t=0, s=0$.
(a) For a particular set of values $(s, t)=\left(s_{1}, \ldots, s_{n_{1}+n_{2}+n_{3}}, t_{1}, \ldots, t_{i}, \ldots, t_{n_{4}}\right)$, if $T_{i}$ is a parent of a $S$ node, and $t_{i}=1$, then equation (40) is satisfied.

Assume the $S$ node which is child of $T_{i}$ is $S_{i}$,notes when $t_{i}=1, P^{M_{k}}\left(t_{i} \mid p a\left(S_{i}\right)\right)=$ $1 / 2$, which is a constant and can be put out. In the remain part, we can always have a $U_{i}$, which only appears as one observable node $X_{j}$ 's parent, we can repeatly remove $P\left(X_{j} \mid P a\left(X_{j}\right)\right)$ and finally get 1 , and $n_{1}-1$ extra $U$ nodes we added when we construct $E G$ graph, so 40 is satisfied.
(b) If for a particular set of values $(s, t)=\left(s_{1}, \ldots, s_{n_{1}+n_{2}+n_{3}}, t_{1}, \ldots, t_{n_{4}}\right)$, equation (40) is satisfied, then for the set of values

$$
\left(s_{1}, \ldots, s_{i-1}, 1-s_{i}, s_{i+1}, \ldots, s_{n_{1}+n_{2}+n_{3}}, t_{1}, \ldots, t_{n_{4}}\right)
$$

Equation (39) is also satisfied, because

$$
\begin{aligned}
& \sum_{U} \prod_{V \in T \cup S} P(v \mid p a(v))\left((S, T)=\left(s_{1}, \ldots, s_{n_{1}+n_{2}+n_{3}}, t_{1}, \ldots, t_{n_{4}}\right)\right)+ \\
& \sum_{U} \prod_{V \in T \cup S} P(v \mid p a(v))\left((S, T)=\right. \\
& \left.\left(s_{1}, \ldots, s_{i-1}, 1-s_{i}, s_{i+1}, \ldots, s_{n_{1}+n_{2}+n_{3}}, t_{1}, \ldots, t_{n_{4}}\right)\right)=2^{n_{1}-1}
\end{aligned}
$$

First for the node $S_{i}$, we know $P\left(S_{i}=0 \mid p a\left(S_{i}\right)+P\left(S_{i}=1 \mid p a\left(S_{i}\right)=1\right.\right.$ for any given $p a\left(S_{i}\right)$. so this $P\left(s_{i} \mid p a\left(S_{i}\right)\right.$ can be removed. Then we can always select $U_{i}$, which only appears as one observable node $X_{j}$ 's parent, repeatedly remove $P\left(X_{j} \mid P a\left(X_{j}\right)\right)$ from (42), and finally obtain $2^{n_{1}-1}$.
(c)If for a particular ser of values $(s, t)=\left(s_{1}, \ldots, s_{n_{1}+n_{2}+n_{3}}, t_{1}, \ldots, t_{n_{4}}\right)$, equation (39) is satisfied, then for the set of values $\left(s_{1}, \ldots, s_{n_{1}+n_{2}+n_{3}}, t_{1}, \ldots, t_{i-1}, 1-\right.$ $\left.t_{i}, t_{i+1}, \ldots, t_{n_{4}}\right)$ eq. (39) is also satisfied, when $T_{i}$ is not a parent of any $S$ node.

We prove this by showing

$$
\begin{aligned}
& \sum_{U} \prod_{V \in T \cup S} P(v \mid p a(v))\left((S, T)=\left(s_{1}, \ldots, s_{n_{1}+n_{2}+n_{3}}, t_{1}, \ldots, t_{n_{4}}\right)\right)= \\
& \sum_{U} \prod_{V \in T \cup S} P(v \mid p a(v)) \\
& \left((S, T)=\left(s_{1}, \ldots, s_{n_{1}+n_{2}+n_{3}}, t_{1}, \ldots, t_{i-1}, 1-t_{i}, t_{i+1}, \ldots, t_{n_{4}}\right)\right)
\end{aligned}
$$

Since $T_{i}$ is an ancestor of $S$, there must be a directed path from $T_{i}$ to an $S$ node, and $T_{i}$ must have a child in $T$. Assume $T_{j}$ is the observable child of $T_{i}$. From the construction of $E G$, we know that we can find an unique bidirected path from $T_{i}$ to $T_{j}$ and that all the observable nodes on that path are $T$ nodes. We name the unobservable variable set on that path $U_{i, j}$.

For the instantiation of $P^{M_{k}}\left(s_{1}, \ldots, s_{n_{1}+n_{2}+n_{3}}, t_{1}, \ldots, t_{n_{4}}, u_{i, j}, u / u_{i, j}\right), u_{i, j}$ is an instance of variable set $U_{i, j}, u \backslash u_{i, j}$ is an instance of $U \backslash U_{i, j}$, and based on our construction we know that it equals $P^{M_{k}}\left(s_{1}, \ldots, s_{n_{1}+n_{2}+n_{3}}, t_{1}, \ldots, t_{i-1}, 1-\right.$ $\left.t_{i}, t_{i+1}, \ldots, t_{n_{4}}, u_{i, j}^{\prime}, u / u_{i, j}\right)$, where $u_{i, j}^{\prime}$ is given by reversing all the values in $u_{i, j}$.

This is because: for node $T_{i}$,

$$
P^{M_{k}}\left(T_{i}=t_{i} \mid p a^{\prime}\left(T_{i}\right), u_{i}\right)=P^{M_{k}}\left(T_{i}=1-t_{i} \mid p a^{\prime}\left(T_{i}\right), 1-u_{i}\right)
$$

where $u_{i}$ is an instance of unobservable node $U_{i} \in U_{i, j}$, and $p a^{\prime}\left(T_{i}\right)$ is an instance of $P a^{\prime}\left(T_{i}\right)=P a\left(t_{i}\right) \backslash\left\{U_{i}\right\}$, and for any node $X$ which has two unobservable parents $U_{0} \in U_{i, j}, U_{1} \in U_{i, j}$,

$$
P^{M_{k}}\left(X=x \mid p a^{\prime}(X), u_{0}, u_{1}\right)=P^{M_{k}}\left(X=x \mid p a^{\prime}(X), 1-u_{0}, 1-u_{1}\right)
$$

where $u_{0}, u_{1}$ are instances of $U_{0}, U_{1}$, and $p a^{\prime}(X)$ is an instance of $P a^{\prime}(X)=$ $P a(X) \backslash\left\{U_{0}, U_{1}\right\}$.

For node $T_{j}$,

$$
P^{M_{k}}\left(T_{j}=t_{j} \mid p a^{\prime}\left(T_{j}\right), t_{i}, u_{j}\right)=P^{M_{k}}\left(T_{j}=t_{j} \mid p a^{\prime}\left(T_{j}\right), 1-t_{i}, 1-u_{j}\right)
$$

where $u_{j}$ is an instance of unobservable node $U_{j} \in U_{i, j}, p a^{\prime}\left(T_{j}\right)$ is an instance of $P a^{\prime}\left(T_{j}\right)=P a\left(t_{i}\right) \backslash\left\{T_{i}, U_{j}\right\}$

This equation gives us a one-one map between $P^{M_{k}}(s, t, u)$ and

$$
P^{M_{k}}\left(s, t_{1}, \ldots, t_{i-1}, 1-t_{i}, t_{i+1}, \ldots, t_{n_{4}}, u\right)
$$

so equation (43) is satisfied.
Before we determine the values attached with the observable nodes in $M_{k}$, $k=1,2$, we give a lemma/

Lemma 9 Let $M_{k}$ be one of the models we create on an $E G$ graph $G$. Let between $\left(T_{1}, T_{2}\right)$ and $\left(T_{2}, T_{3}\right), T_{1}, T_{2}, T_{3} \in T$ be bidirected links. Let $M_{k}^{\prime}$, be defined on a graph equal to $G$ but with bidirected link $\left(T_{1}, T_{3}\right)$ instead of $\left(T_{1}, T_{2}\right)$. If in both $M_{k}$ and $M_{k}^{\prime}$, the variables attached all nodes are the same, and in model $M_{k}$, equation 40 is satisfied, then equation 40 is also satisified in $M_{k}^{\prime}$, and we have $P^{M_{k}}(N)=P^{M_{k}^{\prime}}(N)$ and $Q^{M_{k}}[S]=Q^{M_{k}^{\prime}}[S]$.

Proof: first, note that we just need to consider the situation in which $P(N=$ 0 ). From cases a, b, and c in the proof of lemma 8, we know we just need to consider $\sum_{u} P(s=0, t=0)$ in these two different models. We assume that in the first graph the unobservable node in bidirected link $\left(T_{1}, T_{2}\right)$ is $U_{12}$, the unobservable node in bidirected link $\left(T_{2}, T_{3}\right)$ is $U_{23}$. In the second graph the unobservable node in bidirected link $\left(T_{1}, T_{3}\right)$ is $U_{13}^{\prime}$, the unobservable node in bidirected link $\left(T_{2}, T_{3}\right)$ is $U_{23}^{\prime}$.

For any instantiation $u^{\prime}$ of $U \backslash\left\{U_{12}, U_{23}\right\}$, we have

$$
\begin{gathered}
P^{M}\left(S=0, T=0, u^{\prime}, U_{12}=0, U_{23}=0\right)=P^{M^{\prime}}\left(S=0, T=0, u^{\prime}, U_{13}=0, U_{23}=0\right) \\
P^{M}\left(S=0, T=0, u^{\prime}, U_{12}=0, U_{23}=1\right)=P^{M^{\prime}}\left(S=0, T=0, u^{\prime}, U_{13}=0, U_{23}=1\right) \\
P^{M}\left(S=0, T=0, u^{\prime}, U_{12}=1, U_{23}=0\right)=P^{M^{\prime}}\left(S=0, T=0, u^{\prime}, U_{13}=1, U_{23}=1\right) \\
P^{M}\left(S=0, T=0, u^{\prime}, U_{12}=1, U_{23}=1\right)=P^{M^{\prime}}\left(S=0, T=0, u^{\prime}, U_{13}=1, U_{23}=0\right) \\
\text { So, } \sum_{u} P^{M}(S=0, T=0)=\sum_{u} P^{M^{\prime}}(S=0, T=0) \cdot \square
\end{gathered}
$$

# Unidentifiability of $E G^{S}$ Graph 

Note that any $E G^{S}$ graph is also a $E G$ graph and we follow the same model construction we defined above.

Graph $G_{S_{d} \cup S_{m}}$ is a subgraph of a $E G^{S}$ graph. (It is the same when we take it as a subgraph of the graph $G$, which generates the $E G^{S}$ graph.). It just includes observable nodes in $S_{d} \cup S_{m}$ plus all bidirected links between them. Note that when we treat bidirected links as edges, $G_{S_{d} \cup S_{m}}$ is a free tree.

Fig. 10 shows the $G_{S_{d} \cup S_{m}}$ graph of $E G^{S}$ in Fig. 8

$$
\mathbf{S}_{0} \sim \sim \mathbf{S}_{1}
$$

Figure 10: $G_{S_{d} \cup S_{m}}$ for $E G^{S}$ graph Fig. 7

Lemma 10 In graph $G_{S_{d} \cup S_{m}}, \sum_{U} \prod_{X \in S_{d} \cup S_{m}} P^{M_{k}}(X=0 \mid p a(X))$ can take any value in $(0.5,1)$.

Proof: From the graph properties, we know that for any $E G^{S}$ graph $G$, $G_{S_{d} \cup S_{m}}$ is a free tree when we take the bidirected links as edges. We prove this lemma by induction.

First, when there is just one node in $S_{d} \cup S_{m}, G_{S_{d} \cup S_{m}}$ just has that one node, and there are no unobservable nodes. And as we defined before, that

observable node is binary. $\sum_{U} \prod_{X \in S_{d} \cup S_{m}} P^{M_{k}}(X=0 \mid p a(X))=P(X=0)=$ $\nu_{x}$, which can be any value in $(0.5,1)$.

The inductive assumption is that when there are $k$ nodes in $G_{S_{d} \cup S_{m}}$,

$$
a=\sum_{U} \prod_{X \in S_{d} \cup S_{m}} P^{M_{k}^{\prime}}(X=0 \mid p a(X))
$$

can be any value in $(0,1)$.
Any particular $G_{S_{d} \cup S_{m}}$ has $k+1$ nodes can be obtained by adding an observable node $S_{i}$ in another $G_{S_{d} \cup S_{m}}$ with $k$ nodes. We can assume that the added $S_{i}$ is a leaf in the free tree and assume the unobservable parent of $S_{i}$ in $G_{S_{d} \cup S_{m}}$ is $U_{i}$.

Based on our construction property, in the new graph with $S_{i}$ and $U_{i}$, and in the old graph plus $U_{i}, \sum_{U_{i}=\{0,1\}} \sum_{U} \prod_{X \in S_{d} \cup S_{m}} P(X=0 \mid p a(X))=1$

So, in the new graph, for $S_{d}=0, S_{m}=0$ and $S_{i}=0$,

$$
\begin{aligned}
& \sum_{U_{i}} \sum_{U} \prod_{X \in S_{d} \cup S_{m} \cup\left\{S_{i}\right\}} P(X=0 \mid p a(X))= \\
& \sum_{U_{i}=0} \sum_{U} \prod_{X \in S_{d} \cup S_{m} \cup\left\{S_{i}\right\}} P(X=0 \mid p a(X))+ \\
& \sum_{U_{i}=1} \sum_{U} \prod_{X \in S_{d} \cup S_{m} \cup\left\{S_{i}\right\}} P(X=0 \mid p a(X))= \\
& \nu_{S_{i}} \times a+\sum_{U_{i}=1} \sum_{U} \prod_{X \in S_{d} \cup S_{m}} P(X=0 \mid p a(X))(1-a)= \\
& \nu_{S_{i}} \times a+\left(\sum_{U_{i}=0,1} \sum_{U} \prod_{X \in S_{d} \cup S_{m}} P(X=0 \mid p a(X))\right)- \\
& \sum_{U_{i}=0} \sum_{U} \prod_{X \in S_{d} \cup S_{m}} P(X=0 \mid p a(X)))(1-a)= \\
& \nu_{S_{i}} \times a+\left(1-\nu_{S_{i}}\right) \times(1-a)
\end{aligned}
$$

For any value $b \in(0.5,1)$, we can set $a=(1+b) / 2$, and therefore $a \in(0.5,1)$. Based on math property 1 , we can now choose $\nu_{S_{i}} \in(0,1)$ in such a way that 50 is $b$.

Example 2 Consider the graph $G_{S_{d} \cup S_{m}}$ shown in Fig. 10. To make

$$
\sum_{U} \prod_{X \in S_{d} \cup S_{m}} P^{M_{k}}(X=0 \mid p a(X))
$$

equal to 0.8 , we can select, for example, $\nu_{S_{0}}=0.9$ and $\nu_{S_{1}}=7 / 8=0.875$. To make it equal to 0.9 , we can select, for example, $\nu_{S_{0}}=0.95$ and $\nu_{S_{1}}=0.9444444$. To make it equal to 0.95 , we can select, for example, $\nu_{S_{0}}=0.975$ and $\nu_{S_{1}}=0.97368421$.

Next, we study graph $G_{S^{d} \cup S^{m} \cup\{S\}}$ ). This is the subgraph of an $E G^{S}$ graph obtained by adding node $S_{1}^{i}$ and the bidirected link between it and a $S$ node to graph $G_{S^{d} \cup S^{m}}$.

We know that the $S_{1}^{i}$ node has two $U$ parents in the $E G^{S}$ graph, $U_{2}$ on the bidirected link to a $S$ node and $U_{1}$ on the bidirected link to a $T$ node.

We name $G^{i n i}$ the graph obtained by adding node $U_{1}$ and the directed link from $U_{1}$ to $S_{1}^{i}$ to $G_{S^{d} \cup S^{m} \cup\{S\}}$ ).

Then we have the lemma below:

![img-9.jpeg](img-9.jpeg)

Figure 11: $G^{\text {ini }}$ graph gotten from Fig. 8

Lemma 11 For any value $0.5<a<1$ and $0.5<b<a$, in any $G^{\text {ini }}$ graph $G$, we can force

$$
\sum_{U} \prod_{X \in S^{d} \cup S^{m} \cup\left\{S_{1}^{1}\right\}} P^{M_{k}}(X=0 \mid p a(X))=a
$$

and

$$
\sum_{U_{1}=0} \sum_{U \backslash\left\{U_{1}\right\}} \prod_{X \in S^{d} \cup S^{m} \cup\left\{S_{1}^{1}\right\}} P^{M_{k}}(X=0 \mid p a(X))=b
$$

Proof:
Assume in the graph $G_{S^{d} \cup S^{m}}$, which is a subgraph for the given $G^{\text {int }}$ graph,

$$
\sum_{U} \prod_{X \in S_{d} \cup S_{m}} P(X=0 \mid P a(X))=c
$$

then in the $G^{\text {ini }}$ graph, just like in quantity (50), we have

$$
\begin{aligned}
& \sum_{U_{1}=0} \sum_{U \backslash\left\{U_{1}\right\}} \prod_{X \in S^{d} \cup S^{m} \cup\left\{S_{1}^{1}\right\}} P(X=0 \mid p a(X))= \\
& \nu_{S_{1}^{1}}^{1} c+\left(1-\nu_{S_{1}^{1}}^{1}\right)(1-c)
\end{aligned}
$$

and

$$
\begin{aligned}
& \sum_{U_{1}=1} \sum_{U \backslash\left\{U_{1}\right\}} \prod_{X \in S^{d} \cup S^{m} \cup\left\{S_{1}^{1}\right\}} P(X=0 \mid p a(X))= \\
& \nu_{S_{1}^{1}}^{2} c+\left(1-\nu_{S_{1}^{1}}^{2}\right)(1-c)
\end{aligned}
$$

We want to find $\nu_{S_{1}^{1}}^{1}$ and $\nu_{S_{1}^{1}}^{2}$, so that quantity (55) is $b$, quantity (56) is $a-b$, and $\nu_{S_{1}^{1}}^{1} \neq \nu_{S_{1}^{1}}^{2}$. From lemma 10 we know that $c$ can be any value in $(0.5,1)$, and based on math property 2 we know that the desired result can always be achieved. $\square$

Example 3 Consider the $G^{\text {ini }}$ graph in Fig. 11, and $b=0.7, a=0.8$. to satisfy equations (52) and (53), we can set $\nu_{S_{2}}^{1}=0.722222, \nu_{S_{2}}^{2}=0.055555556, \nu_{S_{0}}=0.975$ and $\nu_{S_{1}}=0.97368421$.

For $b=0.6, a=0.9$, we can set $\nu_{S_{2}}^{1}=0.642857, \nu_{S_{2}}^{2}=0.2142857, \nu_{S_{0}}=0.925$ and $\nu_{S_{1}}=0.9117647$.

For a $G^{\text {ini }}$ graph, we denote

$$
\sum_{U} \prod_{X \in S^{d} \cup S^{m} \cup\left\{S_{1}^{1}\right\}} P^{M_{k}}(X=0 \mid p a(X))
$$

as $N_{0}$ and

$$
\sum_{U_{1}=0} \sum_{U \backslash\left\{U_{1}\right\}} \prod_{X \in S^{d} \cup S^{m} \cup\left\{S_{1}^{t}\right\}} P^{M_{k}}(X=0 \mid p a(X))
$$

as $M_{0}$. Our discussion above shows that we can set values on $S$ nodes to make $N_{0}, M_{0}$ be any values for which $0.5<M_{0}<N_{0}<1$.

Next, we focus on the $E G^{S}$ graphs, which form a subset of the $E G$ graphs.
Note that in $E G^{S}$ graph $G, G_{T}$ and $G_{S}$ are both c-components, and these two c-components are bidirectly connected by one and only one bidirected link, which goes through $S_{1}^{t}$. The 5 graphical properties are still satisfied in $G$.

We define on any $E G$ graph $G$

$$
M(G)=\sum_{U} \prod_{X \in N(G)} P^{M_{k}}(x \mid p a(X))(s=0, t=0)
$$

and

$$
N(G)=\sum_{U} \prod_{X \in S(G)} P^{M_{k}}(x \mid p a(X))(s=0, t=0)
$$

Lemma 12 For any $E G^{S}$ graph $G$, and any $0.5<n<1$, there is a model with $N(G)=n$ and in which $M(G)$ is any value in $[0.5, n)$.

Proof: We prove this lemma by induction. First consider there is just one
![img-10.jpeg](img-10.jpeg)

Figure 12: An $E G^{S}$ graph with just one $T$ node
$T$ node $T_{1}$ in $G$ (see Fig. 12). Assume the unobservable parent of $T_{1}$ is $U_{1}$. For given $0.5<n<1$ and any $0.5 \leqslant m<n$, let $m^{\prime}=(m+n) / 2$. Then from lemma 11, we can force in the $G^{i n i}$ graph obtained from $G$ that $N_{0}=n$ and $M_{0}=m^{\prime}$. Note that $N(G)=N_{0}=n$ and

$$
\begin{aligned}
& M(G)=\sum_{U} \prod_{X \in S \cup T} P^{M_{k}}(X=0 \mid p a(X))= \\
& \sum_{U_{1}=0} \sum_{U \backslash\left\{U_{1}\right\}} \prod_{X \in S \cup T} P^{M_{k}}(X=0 \mid p a(X))+ \\
& \sum_{U_{1}=1} \sum_{U \backslash\left\{U_{1}\right\}} \prod_{X \in S \cup T} P^{M_{k}}(X=0 \mid p a(X))= \\
& \nu_{T_{1}} \times \sum_{U_{1}=0} \sum_{U \backslash\left\{U_{1}\right\}} \prod_{X \in S} P^{M_{k}}(X=0 \mid p a(X))+ \\
& \left(1-\nu_{T_{1}}\right) \times \sum_{U_{1}=1} \sum_{U \backslash\left\{U_{1}\right\}} \prod_{X \in S} P^{M_{k}}(X=0 \mid p a(X))= \\
& \nu_{T_{1}} \times M_{0}+\left(1-\nu_{T_{1}}\right) \times\left(\sum_{U} \prod_{X \in S} P^{M_{k}}(X=0 \mid p a(X))\right)- \\
& \sum_{U_{1}=0} \sum_{U \backslash\left\{U_{1}\right\}} \prod_{X \in S} P^{M_{k}}(X=0 \mid p a(X)))= \\
& \nu_{T_{1}} \times M_{0}+\left(1-\nu_{T_{1}}\right) \times\left(N_{0}-M_{0}\right)
\end{aligned}
$$

Based on math property 2, we know there must be a $\nu_{T_{1}}$ for which $M(G)=1 / 2$. And for any positive number in $[0.5, n)$, we can always find a value for $\nu_{T_{1}}$ to

make $M(G)$ equal that number. The proof continues with the inductive step after an example.

Example 4 For Fig. 12, if we want to set $N(G)=0.8$, and $M(G)=0.6$, we can set: $\nu_{S_{2}}^{1}=0.722222, \nu_{S_{2}}^{2}=0.05555556, \nu_{S_{0}}=0.975, \nu_{S_{1}}=0.9736841$, and $\nu_{T_{1}}=0.83333$.

If we want $N(G)=0.8$, and $M(G)=0.5$, we can set: $\nu_{S_{2}}^{1}=0.625, \nu_{S_{2}}^{2}=0.125$, $\nu_{S_{0}}=0.95, \nu_{S_{1}}=0.9444444$, and $\nu_{T_{1}}=0.75$.

If we want $N(G)=0.7$, and $M(G)=0.5$, we can set: $\nu_{S_{2}}^{1}=0.6111111, \nu_{S_{2}}^{2}=$ $0.055555556, \nu_{S_{0}}=0.975, \nu_{S_{1}}=0.97368421$, and $\nu_{T_{1}}=0.8$.

Assume that this lemma is true for each graph $E G^{S}$ with $|T|=k$. Now consider an $E G^{S}$ graph $G$ with $|T|=k+1$.

From graph property 1 , when we take $G_{n}$ as a free tree, in $E G^{S}$ graph $G$, we can find a $T$ node $X$, which is a leaf of the free tree.
A), This $T$ node $X$ has no observable parent. Since it is a leaf of the free tree, we know there is only one bidirected link into it. Clearly, that bidirected link connects it with another $T$ node.

From lemma 9, we can change the bidirected link until it is between $X$ and its child. When $X$ is $T_{0}$, Fig. 14 gives an example of this situation. Note when we remove $X$ and the bidirected link attached with it, we will get a $E G^{S}$ graph with $|T|=k$.
B), This $T$ node $X$ has only one observable parent, as node $T_{2}$ in Fig. 8. Note that $X$ has one observable parent and one unobservable parent. Because we just consider the case that all observables are 0 , so, for $X$ 's only child $V$, $P(v|P a(v) \cap N=0, p a(v) \cap U)$, where $P a(v) \cap N$ is the observable parents set of $V$ and $P a(v) \cap U$ is the unobservable parents set of $V$, is unchanged before and after we add $X$ and the bidirected link attached with it into the original which by itself is an $E G^{S}$ graph with $|T|=k$.
C), This $X$ node has more than one observable parent, as node $T_{2}$ in Fig. 13.
![img-11.jpeg](img-11.jpeg)

Figure 13: Bidirected link free tree leaf $X$ has more than one parent

Consider the tree of directed links between observable nodes, and reverse the direction of these links. On this tree, we can find at least two leaves, which are $X$ 's observable ancestors. In our example, they are nodes $T_{0}$ and $T_{1}$. Based on the definition of $E G^{S}$ node, we know at least one of them has no bidirected link to any $S$ nodes. We take that node as the new $X$ we select, and from lemma 9 we know that if there are more than one bidirected links into this new $X$, we can always find an equivalent $E G^{S}$ graph with just one bidirected link into this

new $X$. Fig. 14 shows the equivalent graph of Fig. 13. Note that we are back in
![img-12.jpeg](img-12.jpeg)

Figure 14: Graph Equivalent to that of Fig. 13
the situation of case A).
In both case A) and case B), consider the graph $G^{\prime}$ obtained by removing $X$ and the bidirected link attached with it from $G$. This subgraph $G^{\prime}$ is still an $E G^{S}$ graph with $|T|=k$. Based on the inductive assumption, for any given $0.5<n<1$, any $0.5 \leqslant m<n$, and $m^{\prime}=(m+n) / 2$, we can always have $N\left(G^{\prime}\right)=n$ and $M\left(G^{\prime}\right)=m^{\prime}$.

Note that we have $N(G)=N\left(G^{\prime}\right)$. Assuming that the observable parent of $X$ is $U_{1}$, we have

$$
\begin{aligned}
& M(G)=\sum_{U} \prod_{X \in S \cup T} P^{M_{k}}(X=0 \mid p a(X))= \\
& \sum_{U_{1}=0} \sum_{U \backslash\left\{U_{1}\right\}} \prod_{X \in S \cup T} P^{M_{k}}(X=0 \mid p a(X))+ \\
& \sum_{U_{1}=1} \sum_{U \backslash\left\{U_{1}\right\}} \prod_{X \in S \cup T} P^{M_{k}}(X=0 \mid p a(X))= \\
& \nu_{x} \times M\left(G^{\prime}\right)+\left(1-\nu_{x}\right)\left(\sum_{U} \prod_{X \in S \cup T \backslash\{X\}} P^{M_{k}}(X=0 \mid p a(X))-\right. \\
& \sum_{U_{1}=0} \sum_{U \backslash\left\{U_{1}\right\}} \prod_{X \in S \cup T \backslash\{X\}} P^{M_{k}}(X=0 \mid p a(X)))= \\
& \nu_{x} \times M\left(G^{\prime}\right)+\left(1-\nu_{x}\right)\left(N\left(G^{\prime}\right)-M\left(G^{\prime}\right)\right)= \\
& \nu_{x} \times m^{\prime}+\left(1-\nu_{x}\right)\left(n-m^{\prime}\right)
\end{aligned}
$$

Note that in the above equation we have

$$
\sum_{U} \prod_{X \in S \cup T \backslash\{X\}} P^{M_{k}}(X=0 \mid p a(X))=N\left(G^{\prime}\right)
$$

because if we just insert node $U_{1}$ and the link from it to a $T$ node $T_{1}$ in $G^{\prime}$, from equation (36), we have that $U_{1}$ and $P\left(T_{1}=0 \mid p a\left(T_{1}\right)\right)$ can be removed from the above equation. Since $G_{T}$ is a c-component, this kind of removing can continue until all $T$ nodes and $U$ nodes on bidirected links between the $T$ nodes are removed, and we finally get $N\left(G^{\prime}\right)$.

Based on math property 6 , we can always find a solution $\nu_{x}$ to make $M(G) \in$ $\left[1 / 2, m^{\prime}\right)$. So $M(G)$ can be $m$, which is in $\left[0.5, m^{\prime}\right)$. $\square$

With lemma 8 and lemma 12, we have already proved that any $E G^{S}$ graph $G$ is unidentifiable. We can generate two models $M_{1}$ and $M_{2}$ following our construction process, and select different $N$ values for them, but force in both models the $M$ value to be $1 / 2$, which means equation 39 holds.

Example 5 For Fig. 8,if we want to set $N(G)=0.8$, and $M(G)=0.6$, we can set: $\nu_{S_{2}}^{1}=0.72222222, \nu_{S_{2}}^{2}=0.055555556, \nu_{S_{0}}=0.975, \nu_{S_{1}}=0.97368421, \nu_{T_{1}}=0.9$ and $\nu_{T_{2}}=0.91666667$.

If we want to set $N(G)=0.8$, and $M(G)=0.5$, we can set: $\nu_{S_{2}}^{1}=0.72222222, \nu_{S_{2}}^{2}=$ $0.055555556, \nu_{S_{0}}=0.975, \nu_{S_{1}}=0.97368421, \nu_{T_{1}}=0.75$ and $\nu_{T_{2}}=0.8333333$.

If we want to set $N(G)=0.9$, and $M(G)=0.5$, we can set: $\nu_{S_{2}}^{1}=0.75, \nu_{S_{2}}^{2}=$ $0.125, \nu_{S_{0}}=0.95, \nu_{S_{1}}=0.94444444, \nu_{T_{1}}=0.6666667$ and $\nu_{T_{2}}=0.8$.

Example 6 For Fig. 13, if we want to set $N(G)=0.8$, and $M(G)=0.6$, we can set: $\nu_{S_{2}}^{1}=0.7222222, \nu_{S_{2}}^{2}=0.05555556, \nu_{S_{0}}=0.975, \nu_{S_{1}}=0.97368421, \nu_{T_{0}}=$ $0.94444444, \nu_{T_{1}}=0.9285714$ and $\nu_{T_{2}}=0.9375$.

If we want to set $N(G)=0.8$, and $M(G)=0.5$, we can set: $\nu_{S_{2}}^{1}=0.625, \nu_{S_{2}}^{2}=$ $0.125, \nu_{S_{0}}=0.95, \nu_{S_{1}}=0.94444444, \nu_{T_{0}}=0.91666667, \nu_{T_{1}}=0.875$ and $\nu_{T_{2}}=$ 0.9 .

If we want to set $N(G)=0.9$, and $M(G)=0.5$, we can set: $\nu_{S_{2}}^{1}=0.75, \nu_{S_{2}}^{2}=$ $0.125, \nu_{S_{0}}=0.95, \nu_{S_{1}}=0.9444444, \nu_{T_{0}}=0.8666667, \nu_{T_{1}}=0.7142857$ and $\nu_{T_{2}}=0.818181818$.

Example 7 All setting for Fig. 13 can also be used on Fig. 14.

# Unidentifiability of $E G$ Graph 

In a general $E G$ graph $G$, assume $\left|S^{i}\right|>1$, For each node $X \in\left\{S_{2}^{i}, \ldots, S_{n_{1}-1}^{i}\right\}$, there is a bidirected link between $X$ and a $T$ node and a bidirected link between $X$ and a $S$ node. Note that when we remove $X$ and the two bidirected links attached with it, the result is still a $E G$ graph. As we mentioned before, by repeatingly removing all nodes in $\left\{S_{2}^{i}, \ldots, S_{n_{1}-1}^{i}\right\}$, we finally obtain an $E G^{S}$ graph.

In the example of Fig. 15, if we remove node $S_{3}, U_{1}$ and $U_{2}$, we obtain an $E G^{S}$ graph.
![img-13.jpeg](img-13.jpeg)

Figure 15: $E G$ graph with two named $U$ nodes

Lemma 13 In any $E G$ graph $G$ with $\left|S^{i}\right|=n_{1}$, we can find $a, b$ such that $0.5<b<$ $a<1$, and make $M(G)=b \times 2^{n_{1}-1}, N(G)=a \times 2^{n_{1}-1}$.

Proof: We will prove this lemma by induction.
When $\left|S^{i}\right|=1, G$ is an $E G^{S}$ graph, and the result follows from lemma 12.

Assume for all $E G$ graphs with $\left|S^{i}\right|=k$ this lemma is still true, and consider an $E G$ graph with $\left|S^{i}\right|=k+1$. Note that if we remove an $S^{i}$ node $X$ and the bidirected links attached to it from $G$, we obtain an $E G$ graph $G^{\prime}$ with $\left|S^{i}\right|=k$.

From the inductive assumption, we know that we can have $0.5<b<a<1$, $M\left(G^{\prime}\right)=b \times 2^{k-1}$, and $N\left(G^{\prime}\right)=a \times 2^{k-1}$. Assume the $U$ node on the bidirected link connecting $X$ with a $T$ node is $U_{1}$ and the $U$ node on the bidirected link connected $X$ with a $S$ node is $U_{2}$, and remember that the CPT we create for $X$ is


In the graph $G$,

$$
\begin{aligned}
& M(G)=\sum_{U} \prod_{X \in S \cup T} P^{M_{k}}(X=0 \mid p a(X))= \\
& \sum_{U_{1}=0, U_{2}=0} \sum_{U \backslash\left\{U_{1}, U_{2}\right\}} \prod_{X \in S \cup T} P^{M_{k}}(X=0 \mid p a(X))+ \\
& \sum_{U_{1}=1, U_{2}=0} \sum_{U \backslash\left\{U_{1}, U_{2}\right\}} \prod_{X \in S \cup T} P^{M_{k}}(X=0 \mid p a(X))+ \\
& \sum_{U_{1}=0, U_{2}=1} \sum_{U \backslash\left\{U_{1}, U_{2}\right\}} \prod_{X \in S \cup T} P^{M_{k}}(X=0 \mid p a(X))+ \\
& \sum_{U_{1}=1, U_{2}=1} \sum_{U \backslash\left\{U_{1}, U_{2}\right\}} \prod_{X \in S \cup T} P^{M_{k}}(X=0 \mid p a(X))= \\
& \nu_{x}^{1} \times \sum_{U_{1}=0, U_{2}=0} \sum_{U \backslash\left\{U_{1}, U_{2}\right\}} \prod_{X \in S \cup T \backslash\{X\}} P^{M_{k}}(X=0 \mid p a(X))+ \\
& \left(1-\nu_{x}^{1}\right) \times \sum_{U_{1}=1, U_{2}=0} \sum_{U \backslash\left\{U_{1}, U_{2}\right\}} \prod_{X \in S \cup T \backslash\{X\}} P^{M_{k}}(X=0 \mid p a(X))+ \\
& \nu_{x}^{2} \times \sum_{U_{1}=0, U_{2}=1} \sum_{U \backslash\left\{U_{1}, U_{2}\right\}} \prod_{X \in S \cup T \backslash\{X\}} P^{M_{k}}(X=0 \mid p a(X))+ \\
& \left(1-\nu_{x}^{2}\right) \times \sum_{U_{1}=1, U_{2}=1} \sum_{U \backslash\left\{U_{1}, U_{2}\right\}} \prod_{X \in S \cup T \backslash\{X\}} P^{M_{k}}(X=0 \mid p a(X))
\end{aligned}
$$

We have

$$
\sum_{U_{1}=0, U_{2}=0} \sum_{U \backslash\left\{U_{1}, U_{2}\right\}} \prod_{X \in S \cup T \backslash\{X\}} P^{M_{k}}(X=0 \mid p a(X))=M\left(G^{\prime}\right)
$$

and

$$
\begin{aligned}
& \sum_{U_{1}=1, U_{2}=0} \sum_{U \backslash\left\{U_{1}, U_{2}\right\}} \prod_{X \in S \cup T \backslash\{X\}} P^{M_{k}}(X=0 \mid p a(X))= \\
& \sum_{U_{2}=0} \sum_{U \backslash\left\{U_{2}\right\}} \prod_{X \in S \cup T \backslash\{X\}} P^{M_{k}}(X=0 \mid p a(X))- \\
& \sum_{U_{1}=0, U_{2}=0} \sum_{U \backslash\left\{U_{1}, U_{2}\right\}} \prod_{X \in S \cup T \backslash\{X\}} P^{M_{k}}(X=0 \mid p a(X))= \\
& N\left(G^{\prime}\right)-M\left(G^{\prime}\right)
\end{aligned}
$$

where,

$$
\sum_{U_{2}=0} \sum_{U \backslash\left\{U_{2}\right\}} \prod_{X \in S \cup T \backslash\{X\}} P^{M_{k}}(X=0 \mid p a(X))=N\left(G^{\prime}\right)
$$

This is true because when we marginalize away $U_{1}$, based on equation (36), the CPT of a $T$ node which is a child of $U_{1}$ can be removed from the left side of

the above equation. Because $G_{T}$ is a c-component, we can repeat this kind of removing and finally get $N\left(G^{\prime}\right)$.

We also have

$$
\begin{aligned}
& \sum_{U_{1}=0, U_{2}=1} \sum_{U \backslash\left\{U_{1}, U_{2}\right\}} \prod_{X \in S \cup T \backslash\{X\}} P^{M_{k}}(X=0 \mid p a(X))= \\
& \sum_{U_{1}=0} \sum_{U \backslash\left\{U_{1}\right\}} \prod_{X \in S \cup T \backslash\{X\}} P^{M_{k}}(X=0 \mid p a(X))- \\
& \sum_{U_{1}=0, U_{2}=0} \sum_{U \backslash\left\{U_{1}, U_{2}\right\}} \prod_{X \in S \cup T \backslash\{X\}} P^{M_{k}}(X=0 \mid p a(X))= \\
& 1-M\left(G^{\prime}\right)
\end{aligned}
$$

We have

$$
\sum_{U_{1}=0} \sum_{U \backslash\left\{U_{1}\right\}} \prod_{X \in S \cup T \backslash\{X\}} P^{M_{k}}(X=0 \mid p a(X))=2^{k-1}
$$

This is true because when we marginalize away $U_{2}$, based on equations (36), (37) and (38), the CPT of the $S$ node which is a child of $U_{2}$ can be removed from the left side of the above equation first. Since $G$ is a c-component, we can repeat this kind of removal and finally remove all $N(G)$ nodes. Note that in $G^{\prime}$, the number of unobservable nodes minus the number of observable nodes equals $k-1$ and all the unobservable nodes are binary. So, we finally obtain equation (70).

We also have

$$
\begin{aligned}
& \sum_{U_{1}=1, U_{2}=1} \sum_{U \backslash\left\{U_{1}, U_{2}\right\}} \prod_{X \in S \cup T \backslash\{X\}} P^{M_{k}}(X=0 \mid p a(X))= \\
& \sum_{U_{1}=1} \sum_{U \backslash\left\{U_{1}\right\}} \prod_{X \in S \cup T \backslash\{X\}} P^{M_{k}}(X=0 \mid p a(X))- \\
& \sum_{U_{1}=1, U_{2}=0} \sum_{U \backslash\left\{U_{1}, U_{2}\right\}} \prod_{X \in S \cup T \backslash\{X\}} P^{M_{k}}(X=0 \mid p a(X))= \\
& 2^{k-1}-\left(N\left(G^{\prime}\right)-M\left(G^{\prime}\right)\right)
\end{aligned}
$$

This is because, by the argument just given,

$$
\sum_{U_{1}=1} \sum_{U \backslash\left\{U_{1}\right\}} \prod_{X \in S \cup T \backslash\{X\}} P^{M_{k}}(X=0 \mid p a(X))=2^{k-1}
$$

We finally obtain

$$
\begin{aligned}
& M(G)=\nu_{x}^{1} M\left(G^{\prime}\right)+\nu_{x}^{2}\left(N\left(G^{\prime}\right)-M\left(G^{\prime}\right)\right)+ \\
& \left(1-\nu_{x}^{1}\right)\left(2^{k-1}-M\left(G^{\prime}\right)\right)+\left(1-\nu_{x}^{2}\right)\left(2^{k-1}-N\left(G^{\prime}\right)+M\left(G^{\prime}\right)\right)= \\
& \nu_{x}^{1} \times 2^{k-1} b+\nu_{x}^{2} \times 2^{k-1}(a-b)+ \\
& \left(1-\nu_{x}^{1}\right) \times 2^{k-1}(1-b)+\left(1-\nu_{x}^{2}\right) \times 2^{k-1}(1-a+b)= \\
& 2^{k-1}\left(\nu_{x}^{1} b+\nu_{x}^{2}(a-b)+\left(1-\nu_{x}^{1}\right)(1-b)+\left(1-\nu_{x}^{2}\right)(1-a+b)\right)
\end{aligned}
$$

Note that here, for any given $0<\alpha<\min (0.5-a+b,(b-0.5) / 2)$. Since $b-\alpha>0.5,1-b<0.5<b-\alpha<b$, based on math property 1 , we can find a $0<\nu_{x}^{1}<1$ to make $\nu_{x}^{1} b+\left(1-\nu_{x}^{1}\right)(1-b)=b-\alpha$. Because we also have $a-b<0.5-\alpha<0.5<1-(a-b)$, still based on math property 1 , we can also find a $\nu_{x}^{2}$ to make $\nu_{x}^{2}(a-b)+\left(1-\nu_{x}^{2}\right)(1-a+b)=0.5-\alpha$. From math property 3 we have that $\nu_{x}^{1}>0.5$ and $\nu_{x}^{2}>0.5$ here. So, $\nu_{x}^{1} \neq 1-\nu_{x}^{2}$. When we use these $\nu_{x}^{1}$ and $\nu_{x}^{2}$ in the equation above, we have $M(G)=2^{k-1}(b+1 / 2-2 \alpha)$.

For $0.5<b-2 \alpha<1$, let $b^{\prime}=(b+1 / 2-2 \alpha) / 2$. We have $0.5<b^{\prime}<1$ and $M(G)=2^{k} b^{\prime}$.

$$
\begin{aligned}
& N(G)=\sum_{U} \prod_{X \in S} P^{M_{k}}(X=0 \mid p a(X))= \\
& \sum_{U_{1}=0, U_{2}=0} \sum_{U \backslash\left\{U_{1}, U_{2}\right\}} \prod_{X \in S} P^{M_{k}}(X=0 \mid p a(X))+ \\
& \sum_{U_{1}=0, U_{2}=1} \sum_{U \backslash\left\{U_{1}, U_{2}\right\}} \prod_{X \in S} P^{M_{k}}(X=0 \mid p a(X))+ \\
& \sum_{U_{1}=1, U_{2}=0} \sum_{U \backslash\left\{U_{1}, U_{2}\right\}} \prod_{X \in S} P^{M_{k}}(X=0 \mid p a(X))+ \\
& \sum_{U_{1}=1, U_{2}=1} \sum_{U \backslash\left\{U_{1}, U_{2}\right\}} \prod_{X \in S} P^{M_{k}}(X=0 \mid p a(X))= \\
& \nu_{x}^{1} \times \sum_{U_{1}=0, U_{2}=0} \sum_{U \backslash\left\{U_{1}, U_{2}\right\}} \prod_{X \in S \backslash\{X\}} P^{M_{k}}(X=0 \mid p a(X))+ \\
& \left(1-\nu_{x}^{1}\right) \times \sum_{U_{1}=1, U_{2}=0} \sum_{U \backslash\left\{U_{1}, U_{2}\right\}} \prod_{X \in S \backslash\{X\}} P^{M_{k}}(X=0 \mid p a(X))+ \\
& \nu_{x}^{2} \times \sum_{U_{1}=0, U_{2}=1} \sum_{U \backslash\left\{U_{1}, U_{2}\right\}} \prod_{X \in S \backslash\{X\}} P^{M_{k}}(X=0 \mid p a(X))+ \\
& \left(1-\nu_{x}^{2}\right) \sum_{U_{1}=1, U_{2}=1} \sum_{U \backslash\left\{U_{1}, U_{2}\right\}} \prod_{X \in S \backslash\{X\}} P^{M_{k}}(X=0 \mid p a(X))= \\
& \nu_{x}^{1} N\left(G^{\prime}\right)+\left(1-\nu_{x}^{1}\right)\left(2^{k}-N\left(G^{\prime}\right)\right)+\nu_{x}^{2} N\left(G^{\prime}\right)+\left(1-\nu_{x}^{2}\right)\left(2^{k}-N\left(G^{\prime}\right)\right)= \\
& 2^{k-1}\left(\left(\nu_{x}^{1}+\nu_{x}^{2}\right) a+\left(2-\nu_{x}^{1}-\nu_{x}^{2}\right)(2-a)\right)
\end{aligned}
$$

Here we have

$$
\begin{aligned}
& \sum_{U_{1}=0, U_{2}=1} \sum_{U \backslash\left\{U_{1}, U_{2}\right\}} \prod_{X \in S \backslash\{X\}} P^{M_{k}}(X=0 \mid p a(X))= \\
& \sum_{U_{1}=0} \sum_{U \backslash\left\{U_{1}\right\}} \prod_{X \in S \backslash\{X\}} P^{M_{k}}(X=0 \mid p a(X))- \\
& \sum_{U_{1}=0, U_{2}=0} \sum_{U \backslash\left\{U_{1}, U_{2}\right\}} \prod_{X \in S \backslash\{X\}} P^{M_{k}}(X=0 \mid p a(X))= \\
& =2^{k}-N(G)
\end{aligned}
$$

and

$$
\begin{aligned}
& \sum_{U_{1}=1, U_{2}=1} \sum_{U \backslash\left\{U_{1}, U_{2}\right\}} \prod_{X \in S \backslash\{X\}} P^{M_{k}}(X=0 \mid p a(X))= \\
& \sum_{U_{1}=1} \sum_{U \backslash\left\{U_{1}\right\}} \prod_{X \in S \backslash\{X\}} P^{M_{k}}(X=0 \mid p a(X))- \\
& \sum_{U_{1}=1, U_{2}=0} \sum_{U \backslash\left\{U_{1}, U_{2}\right\}} \prod_{X \in S \backslash\{X\}} P^{M_{k}}(X=0 \mid p a(X))= \\
& =2^{k}-N(G)
\end{aligned}
$$

If we let $\left(\nu_{x}^{1}+\nu_{x}^{2}\right) / 2=x$, we have $0.5<x<1$, and

$$
N(G)=2^{k}(x a+(1-x)(2-a))
$$

Note that $0.5<a<1,0.25<a / 2<0.5$. If we let $a^{\prime}=x a+(1-x)(2-a)$, we have

$$
a^{\prime}=x a+(1-x)(2-a)>x a+(1-x) a=a>0.5
$$

and

$$
a^{\prime}=x a+(1-x)(2-a)=2(x \times a / 2+(1-x)(1-a / 2))
$$

From math property 4 we have

$$
x \times a / 2+(1-x)(1-a / 2)<0.5
$$

So, finally we have

$$
0.5<a^{\prime}=2(x \times a / 2+(1-x)(1-a / 2))<2 \times 0.5=1
$$

Note that

$$
\begin{aligned}
& a^{\prime}-b^{\prime}= \\
& \left(\nu_{x}^{1}+\nu_{x}^{2}\right) / 2 \times a+\left(2-\nu_{x}^{1}-\nu_{x}^{2}\right) / 2 \times(2-a)- \\
& \left(\nu_{x}^{1} b+\left(1-\nu_{x}^{1}\right)(1-b)+\nu_{x}^{2}(a-b)+\left(1-\nu_{x}^{2}\right)(1-a+b)\right) / 2= \\
& =1 / 2\left(\nu_{x}^{1} a+\nu_{x}^{2} a+\left(1-\nu_{x}^{1}\right)(2-a)+\left(1-\nu_{x}^{2}\right)(2-a)-\right. \\
& \left(\nu_{x}^{1} b+\nu_{x}^{2}(a-b)+\left(1-\nu_{x}^{1}\right)(1-b)+\left(1-\nu_{x}^{2}\right)(1-a+b)\right)= \\
& =1 / 2\left(\nu_{x}^{1}(a-b)+\nu_{x}^{2} b+\left(1-\nu_{x}^{1}\right)(1-a+b)+\left(1-\nu_{x}^{2}\right)(1-b)\right) \\
& >0
\end{aligned}
$$

So we have $0.5<b^{\prime}<a^{\prime}<1$.
Example 8 For Fig. 15, if we set $\nu_{S_{2}}^{1}=0.75, \nu_{S_{3}}^{2}=0.125, \nu_{S_{0}}=0.95, \nu_{S_{1}}=$ $0.9444444, \nu_{T_{1}}=0.9, \nu_{T_{2}}=0.875 . \nu_{S_{3}}^{1}=0.9$ and $\nu_{S_{3}}^{2}=0.55$, we have $N(G)=$ 0.955 , and $M(G)=0.53$.

We now provide a lemma that, when combined with lemma 8, shows that any $E G$ graph is unidentifiable.

Lemma 14 For any $E G$ graph $G$, if $S^{i}=n_{1}$ we can create two models such that in both of them $M(G)=1 / 2 \times 2^{n_{1}-1}$, but the $N(G)$ are not equal.

Proof: When in $G,\left|S^{i}\right|=1$, from lemma 12, this lemma have be proved.
When in $G\left|S^{i}\right|=k+1$, assume node $X \in S^{i}$, and graph $G^{\prime}$ is obtained by removing $X$ and the bidirected links attached to it from $G . G^{\prime}$ is still an $E G$ graph, and from lemma 13 we know we can have a model satisfying $0.5<b<$ $a<1, M\left(G^{\prime}\right)=b \times 2^{k-1}, N\left(G^{\prime}\right)=a \times 2^{k-1}$. Here we show we can get two pairs $\left(\nu_{x}^{1}, \nu_{x}^{2}\right)$ such that make in both of them $M(G)=1 / 2 \times 2^{k}$ but $N(G)$ is not equal. From the proof of lemma 13, we know

$$
M(G)=2^{k-1}\left(\nu_{x}^{1} b+\nu_{x}^{2}(a-b)+\left(1-\nu_{x}^{1}\right)(1-b)+\left(1-\nu_{x}^{2}\right)(1-a+b)\right)
$$

and

$$
N(G)=2^{k-1}\left(\left(\nu_{x}^{1}+\nu_{x}^{2}\right) a+\left(2-\nu_{x}^{1}-\nu_{x}^{2}\right)(2-a)\right)
$$

For any given $0<\alpha<\min (0.5-a+b, b-0.5), b-\alpha>0.5,1-b<0.5<0.5+$ $\alpha<b$, based on math property 1 , we can find a $\nu_{x}^{1}$ to make $\nu_{x}^{1} b+\left(1-\nu_{x}^{1}\right)(1-b)=$ $0.5+\alpha$. Because we also have $a-b<0.5-\alpha<0.5<1-(a-b)$, still based on math property 1 , we can find a $\nu_{x}^{2}$ to make $\nu_{x}^{2}(a-b)+\left(1-\nu_{x}^{2}\right)(1-a+b)=0.5-\alpha$, then we have $M(G)=1 / 2 \times 2^{k}$. From math property 3 we have property $\nu_{x}^{1}>0.5$ and $\nu_{x}^{2}>0.5$ here. So, $\nu_{x}^{1}>\neq 1-\nu_{x}^{2}$.

For different values of $\alpha$ satisifying $0<\alpha<\min (0.5-a+b, b-0.5)$, we can select more than one pair of $\left(\nu_{x}^{1}, \nu_{x}^{2}\right)$ for which $M(G)=1 / 2 \times 2^{k}$. Assume that $(c, d)$ and $\left(c^{\prime}, d^{\prime}\right)$ are two of those pairs. We have $c \neq c^{\prime}$ and $c+d \neq c^{\prime}+d^{\prime}$.

First we know for $(c, d)$ and $\left(c^{\prime}, d^{\prime}\right)$, we have

$$
c b+d(a-b)+(1-c)(1-b)+(1-d)(1-a+b)=1
$$

and

$$
c^{\prime} b+d^{\prime}(a-b)+\left(1-c^{\prime}\right)(1-b)+\left(1-d^{\prime}\right)(1-a+b)=1
$$

If $c+d=c^{\prime}+d^{\prime}$, let $c^{\prime}=c+\gamma, \gamma \neq 0$, then $d^{\prime}=d-\gamma$, and place them into equation (86):

$$
\begin{aligned}
& (c+\gamma) b+(d-\gamma)(a-b)+(1-(c+\gamma))(1-b)+(1-(d-\gamma))(1-a+b)=1 \Longleftrightarrow \\
& c b+d(a-b)+(1-c)(1-b)+(1-d)(1-a+b)+ \\
& \gamma b-\gamma(a-b)-\gamma(1-b)+\gamma(1-a+b)=1 \Longleftrightarrow \\
& \gamma(4 b-2 a)=0 \Longleftrightarrow \\
& 2 b=a(\text { Wrong })
\end{aligned}
$$

So, we have $c+d \neq c^{\prime}+d^{\prime}$,
Note:

$$
\begin{aligned}
& N(G)=2^{k-1}\left(\left(\nu_{x}^{1}+\nu_{x}^{2}\right) a+\left(2-\nu_{x}^{1}-\nu_{x}^{2}\right)(2-a)\right)= \\
& 2^{k+1}\left(\left(\nu_{x}^{1}+\nu_{x}^{2}\right) / 2 \times a / 2+\left(1-\left(\nu_{x}^{1}+\nu_{x}^{2}\right) / 2\right)(1-a / 2)\right)
\end{aligned}
$$

From math property 5 , we know with $(c, d)$ and $\left(c^{\prime}, d^{\prime}\right)$, we will get different $N(G)$ values.

Example 9 For this example, the $E G^{S}$ graph is obtained by removing node $S_{2}$ from the $E G$ graph of Fig. 15. We can set $\nu_{S_{3}}^{1}=0.75, \nu_{S_{3}}^{2}=0.125, \nu_{S_{0}}=0.95, \nu_{S_{1}}=$ $0.9444444, \nu_{T_{2}}=0.9$ and $\nu_{T_{1}}=0.875$.

With these values, if we select $\nu_{S_{2}}^{1}=0.9, \nu_{S_{2}}^{2}=0.7$, we can obtain model 1 with $M^{1}(G)=1 / 2$, and $N^{1}(G)=0.94$.

If we select $\nu_{S_{2}}^{1}=0.8, \nu_{S_{2}}^{2}=0.65$, we can obtain model 2 with $M^{2}(G)=1 / 2$, and $N^{2}(G)=0.955$.

# Unidentifiability of $G$ 

So far we have proved with our construction that we can create two models $M_{1}$ and $M_{2}$ to show any $E G$ graph $G^{\prime}$ is unidentifiable. We need to show that any graph $G$ that satisfies the five graph properties is unidentifiable. We start by showing the following lemma:

Lemma 15 Assume $E G$ graph $G_{0}$ is obtained by adding bidirected links $\left\{e_{1}, \ldots, e_{k}\right\}$ to graph $G$, which satisfies the 5 graph properties. Graphs $\left\{G_{1}, \ldots, G_{k}\right\}$ are defined as: $G_{i}, 1 \leqslant i \leqslant k$, is obtained by removing $e_{i}$ from $G_{i-1}$, and $G_{k}=G$. Then, each $G_{i}, 1 \leqslant i \leqslant k$, is unidentifiable.

Proof: We want to show that for any $G_{i}, 1 \leqslant i \leqslant k$, we can find two models $M^{1}$ and $M^{2}$ on $G_{i}$, which satisfy:

$$
\sum_{U\left(G_{i}\right)} \prod_{N \cup U\left(G_{i}\right)} P^{M^{1}}(x \mid p a(X))(s, t)=\sum_{U\left(G_{i}\right)} \prod_{N \cup U\left(G_{i}\right)} P^{M^{2}}(x \mid p a(X))(s, t)
$$

but for one $\left(s^{\prime}, t^{\prime}\right)$

$$
\sum_{U\left(G_{i}\right)} \prod_{T \cup U\left(G_{i}\right)} P^{M^{1}}(x \mid p a(X))\left(s^{\prime}, t^{\prime}\right) \neq \sum_{U\left(G_{i}\right)} \prod_{T \cup U\left(G_{i}\right)} P^{M^{2}}(x \mid p a(X))\left(s^{\prime}, t^{\prime}\right)
$$

Note that all the $G_{i}$ models have the same $S^{i}, S^{d}, S^{m}$ and $T$ sets, and the same $G_{s}$ graph.

For $G_{0}$, which is an $E G$ graph, we know that we can have two model $M^{1}$ and $M^{2}$, such that:

All nodes are binary and, especially, all observable nodes are binary.
For any unobservable node $U_{j} \in U\left(G_{0}\right)$ we have

$$
P^{M^{1}}\left(U_{j}=u_{j}\right)=P^{M^{2}}\left(U_{j}=u_{j}\right)=\alpha
$$

here, $\alpha$ means a constant, which, for $G_{0}$, is $1 / 2$.
For any node $X \in T \cup S^{m}$, for any unobservable node $U^{\prime} \in P a(X)$, we have

$$
\sum_{U^{\prime}} P^{M_{1}}(X=x \mid p a(X))=\sum_{U^{\prime}} P^{M_{2}}(X=x \mid p a(X))=\alpha
$$

For any node $X \in S^{d}$, for $U_{x} \in P a(X)$, we have

$$
\sum_{U_{x}} P^{M_{1}}\left(X=x \mid t_{x}, u_{x}\right)=\sum_{U_{x}} P^{M_{2}}\left(X=x \mid t_{x}, u_{x}=1\right)=\alpha
$$

For any node $X \in S^{i}$, we have for $U_{2} \in P a(X)$, one of $U_{2}$ 's child is an $S$ node, and

$$
\sum_{U_{2}} P^{M_{1}}\left(X=x \mid u_{1}, u_{2}\right)=\sum_{U_{2}} P^{M_{2}}\left(X=x \mid u_{1}, u_{2}\right)=\alpha
$$

In all the equations above, $\alpha$ is a constant, although it may be different for different $X$ and marginalized $U$ nodes. In $G_{0}$, all the $\alpha$ s are equal to 1 , and we have that equations (89) and (90) are satisfied.

Assume that on graph $G_{i}$, all the equations from (89) to (94) above are satisfied. We will now remove each of the edges added to the $G$ graph to obtain the $E G$ graph. Assume that the bidirected $<T_{1}, T_{2}>$ is the extra link we remove from $G_{i}$ to get graph $G_{i+1} . U_{0}$ is the unobservable node on that link in $G_{i} . T_{1}$ is connected with $S$ node $S_{1}$ through a bidirected link. $T_{2}$ is connected with $S$ node $S_{k}$ through another bidirected link.

We know $G_{S}$ is a c-component and a bidirected link free tree. So, there is a unique bidirected path in $G_{S}$ from $S_{1}$ to $S_{k}$. By adding to this path the bidirected link from $T_{1}$ to $S_{1}$ and $T_{2}$ to $S_{k}$, we have a unique bidirected path from $T_{1}$ to $T_{2}$, and all observable nodes in this path are $S$ nodes. We name them $S_{1}, \ldots, S_{k}$ in order, and the unobservable nodes on this path are named $U_{1}, \ldots, U_{k+1}$, where $U_{1}$ is on the bidirected link between $T_{1}$ and $S_{1}, U_{2}$ is on the bidirected link between $S_{1}$ and $S_{2}, \ldots, U_{k+1}$ is on the bidirected link between $S_{k}$ to $T_{2}$.

We construct two models $M_{1}^{\prime}$ and $M_{2}^{\prime}$ on graph $G_{i+1}$. The construction is based on models $M_{1}$ and $M_{2}$ on graph $G_{i}$.

In model $M_{k}^{\prime}, k=1,2$, for all the unobservable variables that are not in $\left\{U_{1}, \ldots, U_{k+1}\right\}$, we define their state space to be the same as the state space in $M_{k}$. For each $X$ that belongs to this class,

$$
P^{M_{k}^{\prime}}(X=x)=P^{M_{k}}(X=x), k=1,2
$$

We rename all the unobservable variables that are in $\left\{U_{1}, \ldots, U_{k+1}\right\}$ as $\left\{U_{1}^{\prime}, \ldots, U_{k+1}^{\prime}\right\}$ in $M_{k}^{\prime}$. We define their state space in $M_{k}^{\prime}$ as the product of their state space in $M_{k}$ and the state space of $U_{0}$ in $M_{k}$, which is $(0,1)$. For each $X$ that belongs to this class,

$$
P^{M_{k}^{\prime}}\left(X=\left(x, u_{0}\right)\right)=P^{M_{k}}(X=x) \times P^{M_{k}}\left(U_{0}=u_{0}\right)=P^{M_{k}}(X=x) / 2
$$

The state space of all the observable variables is unchanged, i.e., it is the same as in $M_{k}$. Therefore, all the observable variables are still binary variables.

For each observable variable $X$ not in $\left\{T_{1}, T_{2}, S_{1}, \ldots, S_{k}\right\}$, we map an instance $p a(X)$ in model $M_{k}^{\prime}$ to an instance $p a^{\prime}(X)$ in model $M_{k}$ like this: if $Y$ is an observable node in $P a(x)$, or $Y$ is an unobservable node but is not in $\left\{U_{1}^{\prime}, \ldots, U_{k+1}^{\prime}\right\}$, and $Y=y$ is in $p a(X)$, then $Y=y$ is also in $p a^{\prime}(X)$. If $Y$ is an unobservable node in $P a(X)$ and $Y$ is in $\left\{U_{1}^{\prime}, \ldots, U_{k+1}^{\prime}\right\}$, we denote the value of $Y$ in $p a(X)$ as $Y=\left(u^{Y}, u_{0}^{Y}\right)$, and we have $Y=u^{Y}$ in $p a^{\prime}(X)$. We define

$$
P^{M_{k}^{\prime}}(x \mid p a(X))=P^{M_{k}}\left(x \mid p a^{\prime}(X)\right)
$$

For $X=T_{1}$, we define

$$
P^{M_{k}^{\prime}}\left(x \mid p a^{\prime}(X), U_{1}^{\prime}=\left(u_{1}, u_{0}\right)\right)=P^{M_{k}}\left(x \mid p a^{\prime}(X), U_{1}=u_{1}, U_{0}=u_{0}\right)
$$

Here, $p a^{\prime}(X)$ is an instance of $P a\left(T_{1}\right)$, except for $U_{0}$ and $U_{1}$.
For $X=T_{2}$, we define

$$
P^{M_{k}^{\prime}}\left(x \mid p a^{\prime}(X), U_{k+1}^{\prime}=\left(u_{k+1}, u_{0}\right)\right)=P^{M_{k}}\left(x \mid p a^{\prime}(X), U_{k+1}=u_{k+1}, U_{0}=u_{0}\right)
$$

Here, $p a^{\prime}(X)$ is an instance of $P a\left(T_{2}\right)$, except for $U_{0}$ and $U_{k+1}$.
For observable variable $S_{i}$ in $\left\{S_{1}, \ldots, S_{k}\right\}$, we define

$$
\begin{aligned}
P^{M_{k}^{\prime}}\left(s_{i} \mid p a\left(S_{i}\right)\right) & =P^{M_{k}^{\prime}}\left(s_{i} \mid p a^{\prime}\left(S_{i}\right), U_{i}^{\prime}=\left(u_{i}, u_{0}^{i}\right), U_{i+1}^{\prime}=\left(u_{i+1}, u_{0}^{i+1}\right)\right) \\
& = \begin{cases}P^{M_{k}}\left(s_{i} \mid p a^{\prime}\left(S_{i}\right), U_{i}=u_{i}, U_{i+1}=u_{i+1}\right) & u_{0}^{i}=u_{0}^{i+1} \\
1 / 2 & u_{0}^{i} \neq u_{0}^{i+1}\end{cases}
\end{aligned}
$$

Here, $p a^{\prime}\left(S_{i}\right)$ is an instance of $P a\left(S_{i}\right)$ except for $U_{i}$ and $U_{i+1}$.
Note that with this construction equations (91), (92), (93), and (94) still hold, and for any node $S_{i}$ in $S_{1}, \ldots, S_{k}$, we have, for fixed $u_{0}$,

$$
\sum_{U_{i}^{\prime}=\left(U_{i}, u_{0}\right)} P^{M_{i}}\left(s_{i} \mid p a\left(S_{i}\right)\right)=\alpha
$$

$$
\sum_{U_{i+1}^{\prime}=\left(U_{i+1}, u_{0}\right)} P^{M_{i}}\left(s_{i} \mid p a\left(S_{i}\right)\right)=\alpha
$$

From the two equations above and equations (91), (92), (93) and (94), we have in both $M_{k}^{\prime}, k=1,2$

$$
\begin{aligned}
& P(s, t)= \\
& \sum_{U} \prod_{U \cup N} P(x \mid p a(X))(s, t)= \\
& \sum_{U^{\prime}} \sum_{\left\{U_{1}^{\prime}, \ldots, U_{k+1}^{\prime}\right\}} \prod_{U^{\prime} \cup N} P(x \mid p a(X)) \prod_{\left\{U_{1}^{\prime}, \ldots, U_{k+1}^{\prime}\right\}} P(u)(s, t)= \\
& \sum_{U^{\prime}} \sum_{U_{1}} \sum_{U_{0}^{1}} \sum_{\left\{U_{2}^{\prime}, \ldots, U_{k+1}^{\prime}\right\}} \prod_{U^{\prime} \cup N} P(x \mid p a(X)) \prod_{\left\{U_{1}, U_{0}^{1}, U_{2}^{\prime}, \ldots, U_{k+1}^{\prime}\right\}} P(u)(s, t)= \\
& \sum_{U^{\prime}} \sum_{U_{1}, U_{2}} \sum_{U_{0}^{1}, U_{0}^{2}} \sum_{\left\{U_{3}^{\prime}, \ldots, U_{k+1}^{\prime}\right\}} \\
& \prod_{U^{\prime} \cup N} P(x \mid p a(X)) \prod_{\left\{U_{1}, U_{2}, U_{0}^{1}, U_{0}^{2}, U_{3}^{\prime}, \ldots, U_{k+1}^{\prime}\right\}} P(u)(s, t)= \\
& \sum_{U^{\prime}} \sum_{U_{1}, U_{2}} \sum_{U_{0}^{1}, U_{0}^{2}} \sum_{\left\{U_{3}^{\prime}, \ldots, U_{k+1}^{\prime}\right\}} \\
& \prod_{U^{\prime} \cup N} P(x \mid p a(X)) \prod_{\left\{U_{1}, U_{2}, U_{0}^{1}, U_{0}^{2}, U_{3}^{\prime}, \ldots, U_{k+1}^{\prime}\right\}} P(u)\left(s, t, u_{0}^{1} \neq u_{0}^{2}\right)+ \\
& \sum_{U^{\prime}} \sum_{U_{1}, U_{2}} \sum_{U_{0}^{1}, U_{0}^{2}} \sum_{\left\{U_{3}^{\prime}, \ldots, U_{k+1}^{\prime}\right\}} \\
& \prod_{U^{\prime} \cup N} P(x \mid p a(X)) \prod_{\left\{U_{1}, U_{2}, U_{0}^{1}, U_{0}^{2}, U_{3}^{\prime}, \ldots, U_{k+1}^{\prime}\right\}} P(u)\left(s, t, u_{0}^{1} \neq u_{0}^{2}\right)+ \\
& \sum_{U^{\prime}} \sum_{U_{1}, U_{2}, U_{3}} \sum_{U_{0}^{1}, U_{0}^{2}, U_{0}^{3}} \sum_{\left\{U_{3}^{\prime}, \ldots, U_{k+1}^{\prime}\right\}} \prod_{U^{\prime} \cup N} P(x \mid p a(X)) \\
& \prod_{\left\{U_{1}, U_{2}, U_{3}, U_{0}^{1}, U_{0}^{2}, U_{0}^{3}, U_{3}^{\prime}, \ldots, U_{k+1}^{\prime}\right\}} P(u)\left(s, t, u_{0}^{1}=u_{0}^{2} \neq u_{0}^{3}\right)+ \\
& \sum_{U^{\prime}} \sum_{U_{1}, U_{2}, U_{3}} \sum_{U_{0}^{1}, U_{0}^{2}, U_{0}^{3}} \sum_{\left\{U_{3}^{\prime}, \ldots, U_{k+1}^{\prime}\right\}} \prod_{U^{\prime} \cup N} P(x \mid p a(X)) \\
& \prod_{\left\{U_{1}, U_{2}, U_{3}, U_{0}^{1}, U_{0}^{2}, U_{0}^{3}, U_{3}^{\prime}, \ldots, U_{k+1}^{\prime}\right\}} P(u)\left(s, t, u_{0}^{1}=u_{0}^{2}=u_{0}^{3}\right)= \\
& \sum_{U^{\prime}} \sum_{U_{1}, U_{2}} \sum_{U_{0}^{1}, U_{0}^{2}} \sum_{\left\{U_{3}^{\prime}, \ldots, U_{k+1}^{\prime}\right\}} \\
& \prod_{U^{\prime} \cup N} P(x \mid p a(X)) \prod_{\left\{U_{1}, U_{2}, U_{0}^{1}, U_{0}^{2}, U_{3}^{\prime}, \ldots, U_{k+1}^{\prime}\right\}} P(u)\left(s, t, u_{0}^{1} \neq u_{0}^{2}\right)+ \\
& \ldots+ \\
& \sum_{U^{\prime}} \sum_{U_{1}, \ldots, U_{k+1}} \sum_{U_{0}^{1}, \ldots, U_{0}^{k+1}} \prod_{U^{\prime} \cup N} P(x \mid p a(X)) \\
& \prod_{\left\{U_{1}, \ldots, U_{k+1}\right\}} P(u)\left(s, t, u_{0}^{1}=\ldots=u_{0}^{k+1}\right),
\end{aligned}
$$

where, $U^{\prime}=U \backslash\left\{U_{1}, \ldots, U_{k+1}\right\}$. Note that, in the last expression of the above equation, all the terme except the last one are equal to a constant, so they are equal in $M_{1}^{\prime}$ and $M_{2}^{\prime}$. Based on equation (89), we know the last term is also equal in both models. So, we have $P^{M_{1}^{\prime}}(s, t)=P^{M_{2}^{\prime}}(s, t)$ for any $(s, t)$. That is equation (89) still holds in models $M_{1}^{\prime}$ and $M_{2}^{\prime}$, and in both $M_{k}^{\prime}, k=1,2$, for

$(S=0, T=0)$,

$$
\begin{aligned}
& P_{t}(s)= \\
& \sum_{U} \prod_{U \cup S} P(x \mid p a(X))(s, t)= \\
& \sum_{U^{\prime}} \sum_{\left\{U_{1}^{\prime}, \ldots, U_{k+1}^{\prime}\right\}} \prod_{U^{\prime} \cup S} P(x \mid p a(X)) \prod_{\left\{U_{1}^{\prime}, \ldots, U_{k+1}^{\prime}\right\}} P(u)(s, t)= \\
& \sum_{U^{\prime}} \sum_{U_{1}} \sum_{U_{2}^{1}} \sum_{\left\{U_{2}^{\prime}, \ldots, U_{k+1}^{\prime}\right\}} \prod_{U^{\prime} \cup S} P(x \mid p a(X)) \prod_{\left\{U_{1}, U_{2}^{1}, U_{2}^{\prime}, \ldots, U_{k+1}^{\prime}\right\}} P(u)(s, t)= \\
& \sum_{U^{\prime}} \sum_{U_{1}, U_{2}} \sum_{U_{3}^{1}, U_{3}^{2}} \sum_{\left\{U_{3}^{\prime}, \ldots, U_{k+1}^{\prime}\right\}} \\
& \prod_{U^{\prime} \cup S} P(x \mid p a(X)) \prod_{\left\{U_{1}, U_{2}, U_{3}^{1}, U_{3}^{2}, U_{3}^{\prime}, \ldots, U_{k+1}^{\prime}\right\}} P(u)(s, t)= \\
& \sum_{U^{\prime}} \sum_{U_{1}, U_{2}} \sum_{U_{3}^{1}, U_{3}^{2}} \sum_{\left\{U_{3}^{\prime}, \ldots, U_{k+1}^{\prime}\right\}} \\
& \prod_{U^{\prime} \cup S} P(x \mid p a(X)) \prod_{\left\{U_{1}, U_{2}, U_{3}^{1}, U_{3}^{2}, U_{3}^{\prime}, \ldots, U_{k+1}^{\prime}\right\}} P(u)\left(s, t, u_{0}^{1} \neq u_{0}^{2}\right)+ \\
& \sum_{U^{\prime}} \sum_{U_{1}, U_{2}} \sum_{U_{3}^{1}, U_{3}^{2}} \sum_{\left\{U_{3}^{\prime}, \ldots, U_{k+1}^{\prime}\right\}} \\
& \prod_{U^{\prime} \cup S} P(x \mid p a(X)) \prod_{\left\{U_{1}, U_{2}, U_{3}^{1}, U_{3}^{2}, U_{3}^{\prime}, \ldots, U_{k+1}^{\prime}\right\}} P(u)\left(s, t, u_{0}^{1}=u_{0}^{2}\right)= \\
& \sum_{U^{\prime}} \sum_{U_{1}, U_{2}} \sum_{U_{3}^{1}, U_{3}^{2}} \sum_{\left\{U_{3}^{\prime}, \ldots, U_{k+1}^{\prime}\right\}} \\
& \prod_{U^{\prime} \cup S} P(x \mid p a(X)) \prod_{\left\{U_{1}, U_{2}, U_{3}^{1}, U_{3}^{2}, U_{3}^{\prime}, \ldots, U_{k+1}^{\prime}\right\}} P(u)\left(s, t, u_{0}^{1} \neq u_{0}^{2}\right)+ \\
& \sum_{U^{\prime}} \sum_{U_{1}, U_{2}, U_{3}} \sum_{U_{3}^{1}, U_{3}^{2}, U_{3}^{3}} \sum_{\left\{U_{4}^{\prime}, \ldots, U_{k+1}^{\prime}\right\}} \prod_{U^{\prime} \cup S} P(x \mid p a(X)) \\
& \prod_{\left\{U_{1}, U_{2}, U_{3}, U_{3}^{1}, U_{3}^{2}, U_{3}^{3}, U_{4}^{\prime}, \ldots, U_{k+1}^{\prime}\right\}} P(u)\left(s, t, u_{0}^{1}=u_{0}^{2} \neq u_{0}^{2}\right)+ \\
& \sum_{U^{\prime}} \sum_{U_{1}, U_{2}, U_{3}} \sum_{U_{3}^{1}, U_{3}^{2}, U_{3}^{3}} \sum_{\left\{U_{4}^{\prime}, \ldots, U_{k+1}^{\prime}\right\}} \prod_{U^{\prime} \cup S} P(x \mid p a(X)) \\
& \prod_{\left\{U_{1}, U_{2}, U_{3}, U_{3}^{1}, U_{3}^{2}, U_{3}^{3}, U_{4}^{\prime}, \ldots, U_{k+1}^{\prime}\right\}} P(u)\left(s, t, u_{0}^{1}=u_{0}^{2}=u_{0}^{3}\right)= \\
& \sum_{U^{\prime}} \sum_{U_{1}, U_{2}} \sum_{U_{3}^{1}, U_{3}^{2}} \sum_{\left\{U_{3}^{\prime}, \ldots, U_{k+1}^{\prime}\right\}} \\
& \prod_{U^{\prime} \cup S} P(x \mid p a(X)) \prod_{\left\{U_{1}, U_{2}, U_{3}^{1}, U_{3}^{2}, U_{3}^{\prime}, \ldots, U_{k+1}^{\prime}\right\}} P(u)\left(s, t, u_{0}^{1} \neq u_{0}^{2}\right)+ \\
& \ldots+ \\
& \sum_{U^{\prime}} \sum_{U_{1}, \ldots, U_{k+1}} \sum_{U_{n}^{1}, \ldots, U_{n}^{k+1}} \prod_{U^{\prime} \cup S} P(x \mid p a(X)) \\
& \prod_{\left\{U_{1}, \ldots, U_{k+1}\right\}} P(u)\left(s, t, u_{0}^{1}=\ldots=u_{0}^{k+1}\right)
\end{aligned}
$$

Note that in the last expression of the above equation, all the terms except the last one are equal to a constant, so they are equal in $M_{1}^{\prime}$ and $M_{2}^{\prime}$. Based on equation (90), we know that the last term is not equal in $M_{1}^{\prime}$ and $M_{2}^{\prime}$. So, we have $P_{t}^{M_{1}^{\prime}}(s)(S=0, T=0) \neq P_{t}^{M_{2}^{\prime}}(s)(S=0, T=0)$, which means equation (90) still holds for $M_{k}^{\prime}, k=1,2$.

By repeating this construction, we conclude that all graph models $\left\{G_{0}, G_{1}, \ldots, G_{k}\right\}$ are unidentifiable.

Example 10 The Hugin files for the models constructed in this appendix for the $G$ graph of Fig. 6 (D) can be downloaded from
http://www.cse.sc.edu/ huang6/test/exampleD1TS.net
and http://www.cse.sc.edu/ huang6/test/exampleD2TS.net.

# Appendix B 

Lemma 5 Assume $S \subset N$ and $T \subset N$ are disjunct node sets in graph $G,<$ $X_{1}, X_{2}>$ is a directed link in $G, X_{1} \in S$, and $X_{2} \in S$. Assume that graph $G^{\prime}$ is

obtained by removing link $<X_{1}, X_{2}>$ from graph $G$. If $P_{T}(S)$ is unidentifiable in graph $G^{\prime}$, then $P_{T}\left(S \backslash\left\{X_{1}\right\}\right)$ is unidentifiable in $G$.

Proof:
By definition, in graph $G^{\prime}, P_{t}(s)$ is given by:

$$
P_{t}(s)=\sum_{V_{i} \in(N \backslash S) \backslash T} \sum_{U_{k} \in U} \prod_{V_{i} \in N \backslash T} P\left(v_{i} \mid p a\left(V_{i}\right)\right) \prod_{V_{j} \in U} P\left(v_{j}\right)
$$

In graph $G$,

$$
P_{t}\left(s \backslash\left\{x_{1}\right\}\right)=\sum_{V_{i} \in(N \backslash S) \backslash T \cup\left\{X_{1}\right\}} \sum_{U_{k} \in U} \prod_{V_{i} \in N \backslash T} P\left(v_{i} \mid p a\left(V_{i}\right)\right) \prod_{V_{j} \in U} P\left(v_{j}\right)
$$

When $P_{T}(S)$ is unidentifiable in graph $G^{\prime}$, we know there are two models $M_{1}$ and $M_{2}$ on $G^{\prime}$ such that: $P^{M_{1}}(n)=P^{M_{2}}(n)$, which means:

$$
\sum_{U_{k} \in U} \prod_{V_{i} \in N} P^{M_{1}}\left(v_{i} \mid p a\left(V_{i}\right)\right) \prod_{V_{j} \in U} P^{M_{1}}\left(v_{j}\right)=\sum_{U_{k} \in U} \prod_{V_{i} \in N} P^{M_{2}}\left(v_{i} \mid p a\left(V_{i}\right)\right) \prod_{V_{j} \in U} P^{M_{2}}\left(v_{j}\right)
$$

but for at least one $(s, t), P_{t}^{M_{1}}(s) \neq P_{t}^{M_{2}}(s)$.
Now based on $M_{1}$ and $M_{2}$, we create models $M_{1}^{\prime}$ and $M_{2}^{\prime}$ on graph $G$. First, we define a probability function $F$ from $S\left(X_{1}\right)$ to $(0,1)$, where $S\left(X_{1}\right)$ is the state space of $X_{1}$ in model $M_{i}, i=1,2$. For any $a \in S\left(X_{1}\right), P(F(a)=0)>0$, $P(F(a)=1)>0$ and $P(F(a)=0)+P(F(a)=1)=1$.

For any node $X$, which is an unobservable node or a node in $N \backslash\left(\left\{X_{2}\right\} \cup\right.$ $\left.C H\left(X_{2}\right)\right)$, we define, for $i=1,2$

$$
P^{M_{1}^{\prime}}(x \mid p a(X))=P^{M_{i}}(x \mid p a(X))
$$

The state space of $X_{2}$ in $M_{i}^{\prime}$ is defined as $S\left(X_{2}\right) \times\{0,1\}$, where $S\left(X_{2}\right)$ is the state space of $X_{2}$ in $M_{i}, i=1,2$.

For $x_{2} \in S\left(X_{2}\right), i=1,2, k=0,1$, we define

$$
P^{M_{i}^{\prime}}\left(\left(x_{2}, k\right) \mid p a\left(X_{2}\right), x_{1}\right)=P^{M_{i}}\left(x_{2} \mid p a\left(X_{2}\right)\right) \times P\left(F\left(x_{1}\right)=k\right)
$$

where $P a\left(X_{2}\right)$ is the parent set of $X_{2}$ in graph $G^{\prime}$. So, $P a\left(X_{2}\right) \cup\left\{X_{1}\right\}$ is the parent set of $X_{2}$ in graph $G$.

Note that, for a given $\left(p a\left(X_{2}\right), x_{1}\right)$, we have

$$
\sum_{x_{2}, k} P^{M_{i}^{\prime}}\left(\left(x_{2}, k\right) \mid p a\left(X_{2}\right), x_{1}\right)=\sum_{x_{2}} P^{M_{i}}\left(x_{2} \mid p a\left(X_{2}\right)\right) \times \sum_{k} P\left(F\left(x_{1}\right)=k\right)=1
$$

For any node $X \in C h\left(X_{2}\right)$, we define

$$
P^{M_{i}^{\prime}}\left(x \mid p a^{\prime}(X),\left(x_{2}, k\right)\right)=P^{M_{i}}\left(x \mid p a^{\prime}(X), x_{2}\right)
$$

where $P a^{\prime}(X)=P a(X) \backslash\left\{X_{2}\right\}$ is the parent set of $X$ in graph $G$, except for node $X_{2}$. Then for any instance $n$ of $N$ in model $M_{1}^{\prime}$ and $M_{2}^{\prime}$, if $X_{1}=x_{1}$ and $X_{2}=\left(x_{2}, k\right)$ in $n$, we have

$$
\begin{aligned}
& P^{M_{1}^{\prime}}(n)= \\
& \sum_{U_{k} \in U} \prod_{V_{i} \in N} P^{M_{1}^{\prime}}\left(v_{i} \mid p a\left(V_{i}\right)\right) \prod_{V_{j} \in U} P^{M_{1}^{\prime}}\left(v_{j}\right)= \\
& \sum_{U_{k} \in U} \prod_{V_{i} \in N} P^{M_{1}}\left(v_{i} \mid p a\left(V_{i}\right)\right) \prod_{V_{j} \in U} P^{M_{1}}\left(v_{j}\right)(n) \times P\left(F\left(x_{1}\right)=k\right)= \\
& \sum_{U_{k} \in U} \prod_{V_{i} \in N} P^{M_{2}}\left(v_{i} \mid p a\left(V_{i}\right)\right) \prod_{V_{j} \in U} P^{M_{2}}\left(v_{j}\right)(n) \times P\left(F\left(x_{1}\right)=k\right)= \\
& \sum_{U_{k} \in U} \prod_{V_{i} \in N} P^{M_{2}^{\prime}}\left(v_{i} \mid p a\left(V_{i}\right)\right) \prod_{V_{j} \in U} P^{M_{2}^{\prime}}\left(v_{j}\right)= \\
& P^{M_{2}^{\prime}}(n) .
\end{aligned}
$$

We know that for a given $(s, t), P_{t}^{M_{1}}(s) \neq P_{t}^{M_{2}}(s)$, and we assume that $X_{1}=$ $x_{1}$ and $X_{2}=x_{2}$ in $s$.

Note that $\sum_{X_{1}} P_{t}^{M_{1}}\left(s \backslash\left\{x_{1}\right\}\right) \leqslant 1$, because after setting the values of the $T$ nodes, the result model is still a Bayesian network.

Assume that $P_{t}^{M_{1}}(s)=a>P_{t}^{M_{2}}(s)=b>0$. If we define $P\left(F\left(x_{1}\right)=0\right)=$ 0.5 , but $P(F(x)=0)=(a-b) / 4$ for all $x \in S\left(X_{1}\right), x \neq x_{1}$, we have that for $\left(s \backslash\left\{x_{2}\right\},\left(x_{2}, 0\right), t\right)$

$$
\begin{aligned}
& P_{t}^{M_{1}^{\prime}}\left(s \backslash\left\{x_{1}\right\}\right)\left(S \backslash\left\{X_{1}\right\}=\left(s \backslash\left\{x_{1}, x_{2}\right\},\left(x_{2}, 0\right)\right), T=t\right)= \\
& \sum_{V_{i} \in(N \backslash S) \backslash T \cup\left\{X_{1}\right\}} \sum_{U_{k} \in U} \prod_{V_{i} \in V \backslash T} P^{M_{1}^{\prime}}\left(v_{i} \mid p a\left(V_{i}\right)\right) \\
& \left(S \backslash\left\{X_{1}\right\}=\left(s \backslash\left\{x_{1}, x_{2}\right\},\left(x_{2}, 0\right)\right), T=t\right)> \\
& \sum_{X_{1}=x_{1}} \sum_{V_{i} \in(N \backslash S) \backslash T} \sum_{U_{k} \in U} \prod_{V_{i} \in V \backslash T} P^{M_{1}^{\prime}}\left(v_{i} \mid p a\left(V_{i}\right)\right) \\
& \left(S \backslash\left\{X_{1}\right\}=\left(s \backslash\left\{x_{1}, x_{2}\right\},\left(x_{2}, 0\right)\right), T=t\right)= \\
& \sum_{V_{i} \in(N \backslash S) \backslash T} \sum_{U_{k} \in U} \prod_{V_{i} \in V \backslash T} P^{M_{1}}\left(v_{i} \mid p a\left(V_{i}\right)\right)\left(S=s, T=t\right) \times P\left(F\left(x_{1}\right)=0\right)= \\
& =0.5 a,
\end{aligned}
$$

but

$$
\begin{aligned}
& P_{t}^{M_{2}^{\prime}}\left(s \backslash\left\{x_{1}\right\}\right)\left(S \backslash\left\{X_{1}\right\}=\left(s \backslash\left\{x_{1}, x_{2}\right\},\left(x_{2}, 0\right)\right), T=t\right)= \\
& \sum_{V_{i} \in(N \backslash S) \backslash T \cup\left\{X_{1}\right\}} \sum_{U_{k} \in U} \prod_{V_{i} \in V \backslash T} P^{M_{2}^{\prime}}\left(v_{i} \mid p a\left(V_{i}\right)\right) \\
& \left(S \backslash\left\{X_{1}\right\}=\left(s \backslash\left\{x_{1}, x_{2}\right\},\left(x_{2}, 0\right)\right), T=t\right)= \\
& \sum_{X_{1}=x_{1}} \sum_{V_{i} \in(N \backslash S) \backslash T} \sum_{U_{k} \in U} \prod_{V_{i} \in V \backslash T} P^{M_{2}^{\prime}}\left(v_{i} \mid p a\left(V_{i}\right)\right) \\
& \left(S \backslash\left\{X_{1}\right\}=\left(s \backslash\left\{x_{1}, x_{2}\right\},\left(x_{2}, 0\right)\right), T=t\right)+ \\
& \sum_{X_{1} \neq x_{1}} \sum_{V_{i} \in(N \backslash S) \backslash T} \sum_{U_{k} \in U} \prod_{V_{i} \in V \backslash T} P^{M_{2}^{\prime}}\left(v_{i} \mid p a\left(V_{i}\right)\right) \\
& \left(S \backslash\left\{X_{1}\right\}=\left(s \backslash\left\{x_{1}, x_{2}\right\},\left(x_{2}, 0\right)\right), T=t\right)< \\
& \sum_{V_{i} \in(N \backslash S) \backslash T} \sum_{U_{k} \in U} \prod_{V_{i} \in V \backslash T} P^{M_{2}}\left(v_{i} \mid p a\left(V_{i}\right)\right)\left(S=s, T=t\right) \times P\left(F\left(x_{1}\right)=0\right)+ \\
& \sum_{V_{i} \in(N \backslash S) \backslash T \cup\left\{X_{1}\right\}} \sum_{U_{k} \in U} \prod_{V_{i} \in V \backslash T} P^{M_{2}}\left(v_{i} \mid p a\left(V_{i}\right)\right) \\
& \left(S \backslash\left\{X_{1}\right\}=s \backslash\left\{x_{1}\right\}, T=t\right) \times P\left(F\left(X_{i} \neq x_{1}\right)=0\right) \leqslant \\
& 0.5 b+\sum_{X_{1}} P_{t}^{M_{2}}\left(s \backslash\left\{x_{1}\right\}\right) \times(a-b) / 4 \leqslant \\
& 0.5 b+(a-b) / 4<0.5 a
\end{aligned}
$$

From the models $M_{1}^{\prime}$ and $M_{2}^{\prime}$ thus constructed, we know $P_{T}\left(S \backslash\left\{X_{1}\right\}\right.$ is unidentifiable in $G . \square$