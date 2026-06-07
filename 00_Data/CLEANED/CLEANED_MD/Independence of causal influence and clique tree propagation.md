# Independence of Causal Influence and Clique Tree Propagation 

Nevin Lianwen Zhang and Li Yan<br>Department of Computer Science, Hong Kong University of Science \& Technology<br>\{lzhang, yanli\}@cs.ust.hk


#### Abstract

This paper explores the role of independence of causal influence (ICI) in Bayesian network inference. ICI allows one to factorize a conditional probability table into smaller pieces. We describe a method for exploiting the factorization in clique tree propagation (CTP) - the state-of-the-art exact inference algorithm for Bayesian networks. We also present empirical results showing that the resulting algorithm is significantly more efficient than the combination of CTP and previous techniques for exploiting ICI.


Keywords: Bayesian networks, independence of causal influence (causal independence), inference, clique tree propagation.

## 1 INTRODUCTION

Bayesian networks (Pearl [16], Howard and Matheson [8]) are a knowledge representation framework widely used by AI researchers for reasoning under uncertainty. They are directed acyclic graphs where each node represents a random variable and is associated with a conditional probability table of the node given its parents. This paper is about inference in Bayesian networks. There exists a rich collection of algorithms. The state-of-the-art is an exact algorithm called clique tree propagation ${ }^{1}$ (CTP) (Lauritzen and Spiegelhalter [12], Jensen et al [10], and Shafer and Shenoy [20]).
Unfortunately, there are applications that CTP cannot deal with or where it is too slow (e.g. [18]). Much recent effort has been spent on speeding up inference. The efforts can be classified into those that approximate (e.g. [15], [2], [9], [6], [7], [17], [22], [11], and [19])

[^0]and those that exploit structures in the probability tables (e.g. [3], [1]).
We are interested in exploiting structures in the probability tables induced by independence of causal influence (ICI). The concept of ICI was first introduced by Heckerman [3] under the name causal independence. It refers to the situation where multiple causes independently influence a common effect. We use the term "independence of causal influence" instead of "causal independence" because many researchers have come to agree that it captures the essence of the situation better than the latter.

Knowledge engineers had been using specific models of ICI in simplifying knowledge acquisition even before the inception of the concept ([5], [13]). Olesen et al [13] and Heckerman [3] have also shown how ICI can be used to simplify the structures of Bayesian networks so that inference can be more efficient.

Zhang and Poole ([23]) made the observation that ICI enables one to factorize a conditional probability table into smaller pieces and showed how the VE algorithm - another exact inference algorithm - can be extended to take advantage of the factorization. This paper extends CTP to exploit conditional probability table factorization. We also present empirical results showing that the extended CTP is more efficient than the combination of CTP and the network simplification techniques. In comparison with Zhang and Poole [23], this paper presents a deeper understanding of ICI. The theory is substantially simplified.

## 2 BAYESIAN NETWORKS

A Bayesian network (BN) is an annotated directed acyclic graph, where each node represents a random variable and is attached with a conditional probability of the node given its parents. In addition to the explicitly represented conditional probabilities, a BN also implicitly represents conditional independence as-


[^0]:    ${ }^{1}$ Also known as junction tree propagation.

sertions. Let $x_{1}, x_{2}, \ldots, x_{n}$ be an enumeration of all the nodes in a BN such that each node appears before its children, and let $\pi_{x_{i}}$ be the set of parents of a node $x_{i}$. The following assertions are implicitly represented:

For $i=1,2, \ldots n, x_{i}$ is conditionally independent of variables in $\left\{x_{1}, x_{2}, \ldots, x_{i-1}\right\} \backslash \pi_{x_{i}}$ given variables in $\pi_{x_{i}}$.

The conditional independence assertions and the conditional probabilities together entail a joint probability over all the variables. As a matter of fact, by the chain rule, we have

$$
\begin{aligned}
P\left(x_{1}, x_{2}, \ldots, x_{n}\right) & =\prod_{i=1}^{n} P\left(x_{i} \mid x_{1}, x_{2}, \ldots, x_{i-1}\right) \\
& =\prod_{i=1}^{n} P\left(x_{i} \mid \pi_{x_{i}}\right)
\end{aligned}
$$

where the second equation is true because of the conditional independence assertions and the conditional probabilities $P\left(x_{i} \mid \pi_{x_{i}}\right)$ are given in the specification of the BN. Consequently, one can, in theory, do arbitrary probabilistic reasoning in a BN.

## 3 INDEPENDENCE OF CAUSAL INFLUENCE

Bayesian networks place no restriction on how a node depends on its parents. Unfortunately this means that in the most general case we need to specify an exponential (in the number of parents) number of conditional probabilities for each node. There are many cases where there is structure in the probability tables. One such case that we investigate in this paper is known as independence of causal influence (ICI).
The concept of ICI was first introduced by Beckerman [4]. The following definition first appeared in Zhang and Poole [24].
In one interpretation, arcs in a BN represent causal relationships; the parents $c_{1}, c_{2}, \ldots, c_{m}$ of a node $e$ are viewed as causes that jointly bear on the effect $e$. ICI refers to the situation where the causes $c_{1}, c_{2} \ldots$, and $c_{m}$ contribute independently to the effect $e$. In other words, the ways by which the $c_{i}$ 's influence $e$ are independent.
More precisely, $c_{1}, c_{2} \ldots$, and $c_{m}$ are said to influence $e$ independently if there exist random variables $\xi_{1}, \xi_{2}$ $\ldots$, and $\xi_{m}$ that have the same frame - set of possible values - as $e$ such that

1. For each $i, \xi_{i}$ probabilistically depends on $c_{i}$ and
is conditionally independent of all other $c_{j}$ 's and all other $\xi_{j}$ 's given $c_{i}$, and
2. There exists a commutative and associative binary operator * over the frame of $e$ such that $e=\xi_{1} * \xi_{2} * \ldots * \xi_{m}$.

We shall refer to $\xi_{i}$ as the contribution of $c_{i}$ to $e$. In less technical terms, causes influence their common effect independently if individual contributions from different causes are independent and the total influence is a combination of the individual contributions.
We call the variable $e$ a convergent variable for it is where independent contributions from different sources are collected and combined (and for the lack of a better name). Non-convergent variables will simply be called regular variables. We also call $*$ the base combination operator of $e$. Different convergent variables can have difference base combination operators.
The reader is referred to [24] for more detailed explanations and examples of ICI.
The conditional probability table $P\left(e \mid c_{1}, \ldots, c_{m}\right)$ of a convergent variable $e$ can be factorized into smaller pieces. To be more specific, let $f_{i}\left(e, c_{i}\right)$ be the function defined by

$$
f_{i}\left(e=\alpha_{i} c_{i}\right)=P\left(\xi_{i}=\alpha \mid c_{i}\right)
$$

for each possible value $\alpha$ of $e$. It will be referred to as the contributing factor of $c_{i}$ to $e$. Zhang and Poole [24] have shown that

$$
P\left(e \mid c_{1}, \ldots, c_{m}\right)=\otimes_{i=1}^{m} f_{i}\left(e, c_{i}\right)
$$

where $\otimes$ is an operator for combining factors to be defined in the following.
Assume there is a fixed list of variables, some of which are designated to be convergent and others are designated to be regular. We shall only consider functions of variables on the list.
Let $f\left(e_{1}, \ldots, e_{k}, A, B\right)$ and $g\left(e_{1}, \ldots, e_{k}, A, C\right)$ be two functions that share convergent variables $e_{1}, \ldots, e_{k}$ and a list $A$ of regular variables. $B$ is the list of variables that appear only in $f$, and $C$ is the list of variables that appear only in $g$. Both $B$ and $C$ can contain convergent variables as well as regular variables. Suppose $*_{i}$ is the base combination operator of $e_{i}$. Then, the combination $f \otimes g$ of $f$ and $g$ is a function of variables $e_{1}, \ldots, e_{k}$ and of the variables in $A, B$, and $C$. It is defined by

$$
\begin{aligned}
& f \otimes g\left(c_{1}=\alpha_{1}, \ldots, e_{k}=\alpha_{k}, A, B, C\right) \\
& =\sum_{\alpha_{11} *, \alpha_{12}=\alpha_{1}} \cdots \sum_{\alpha_{k 1} *, \alpha_{k 2}=\alpha_{k}} \\
& f\left(e_{1}=\alpha_{11}, \ldots, e_{k}=\alpha_{k 1}, A, B\right) \\
& g\left(e_{1}=\alpha_{12}, \ldots, e_{k}=\alpha_{k 2}, A, C\right),
\end{aligned}
$$

![img-0.jpeg](img-0.jpeg)

Figure 1: A Bayesian network.
for each possible value $\alpha_{i}$ of $e_{i}$. We shall sometimes write $f \otimes g$ as $f\left(e_{1}, \ldots, e_{k}, A, B\right) \otimes g\left(e_{1}, \ldots, e_{k}, A, C\right)$ to make explicit the arguments of $f$ and $g$.
The operator $\otimes$ is associative and commutative. When $f$ and $g$ do not share convergent variables, $f \otimes g$ is simply the multiplication $f g$.

## 4 FACTORIZATION OF JOINT PROBABILITIES

A BN represents a factorization of a joint probability. For example, the Bayesian network in Figure 1 factorizes the joint probability $P\left(a, b, c, e_{1}, e_{2}, e_{3}\right)$ into the following list of factors:
$P(a), P(b), P(c), P\left(e_{1} \mid a, b, c\right), P\left(e_{2} \mid a, b, c\right), P\left(e_{3} \mid e_{1}, e_{2}\right)$.
The joint probability can be obtained by multiplying the factors. We say that this factorization is multiplication-homogeneous because all the factors are combined in the same way by multiplication.
Now suppose the $e_{i}$ 's are convergent variables. Then their conditional probabilities can be further factorized as follows:

$$
\begin{aligned}
& P\left(e_{1} \mid a, b, c\right)=f_{11}\left(e_{1}, a\right) \otimes f_{12}\left(e_{1}, b\right) \otimes f_{13}\left(e_{1}, c\right) \\
& P\left(e_{2} \mid a, b, c\right)=f_{21}\left(e_{2}, a\right) \otimes f_{22}\left(e_{2}, b\right) \otimes f_{23}\left(e_{2}, c\right) \\
& P\left(e_{3} \mid e_{1}, e_{2}\right)=f_{31}\left(e_{3}, e_{1}\right) \otimes f_{32}\left(e_{3}, e_{2}\right)
\end{aligned}
$$

where the factor $f_{11}\left(e_{1}, a\right)$, for instance, is the contributing factor of $a$ to $e_{1}$.
We say that the following list of factors

$$
\begin{aligned}
& f_{11}\left(e_{1}, a\right), f_{12}\left(e_{1}, b\right), f_{13}\left(e_{1}, c\right) \\
& f_{21}\left(e_{2}, a\right), f_{22}\left(e_{2}, b\right), f_{23}\left(e_{2}, c\right) \\
& f_{31}\left(e_{3}, e_{1}\right), f_{32}\left(e_{3}, e_{2}\right) \\
& P(a), P(b), \text { and } P(c)
\end{aligned}
$$

constitute a a heterog-
neous factorization of $P\left(a, b, c, e_{1}, e_{2}, e_{3}\right)$ because the joint probability can be obtained by combining those factors in a proper order using either multiplication or the operator $\otimes$. The word heterogeneous is to signify the fact that different factor pairs might be combined in different ways. We shall refer to the factorization as the heterogeneous factorization represented by the BN in Figure 1.

The heterogeneous factorization is of finer grain than the homogeneous factorization. The purpose of this paper is to exploit such finer-grain factorizations to speed up inference.

## 5 DEPUTATION

In a heterogeneous factorization, the order by which factors can be combined is rather restrictive. The contributing factors of a convergent variable must be combined with themselves before they can be multiplied with other factors. This is the main issue that we need to deal with in order to take advantage of conditional probability table factorizations induced by ICI.
To alleviate the problem, we introduce the concept of deputation. It was originally defined in term of BNs [24]. In this paper, we define it in terms of heterogeneous factorizations themselves.
In the heterogeneous factorization represented by a BN, to depute a convergent variable $e$ is to make a copy $e^{\prime}$ of $e$ and replace $e$ with $e^{\prime}$ in all the contributing factors of $e$. The variable $e^{\prime}$ is called the deputy of $e$ and it is designated to be convergent. After deputation, the original convergent variable $e$ is no longer convergent and is called a new regular variable. In contrast, variables that are regular before deputation are called old regular variables.
After deputing all convergent variables, the heterogeneous factorization represented by the BN in Figure 1 becomes the following list of factors:

$$
\begin{aligned}
& f_{11}\left(e_{1}^{\prime}, a\right), \quad f_{12}\left(e_{1}^{\prime}, b\right), \quad f_{13}\left(e_{1}^{\prime}, c\right), \quad f_{21}\left(e_{2}^{\prime}, a\right), \\
& f_{22}\left(e_{2}^{\prime}, b\right), f_{23}\left(e_{2}^{\prime}, c\right), f_{31}\left(e_{2}^{\prime}, e_{1}\right), f_{32}\left(e_{2}^{\prime}, e_{2}\right), \\
& P(a), P(b), P(c) .
\end{aligned}
$$

The rest of this section is to show that deputation renders it possible to combine the factors in arbitrary order.

### 5.1 ELIMINATING DEPUTY VARIABLES IN FACTORS

Eliminating a deputy variable $e^{\prime}$ in a factor $f$ means to replace it with the corresponding new regular variable

$e$. The resulting factor will be denoted by $f\left|{ }_{e^{\prime} \equiv e}\right.$. To be more specific, for any factor $f\left(e, e^{\prime}, A\right)$ of $e, e^{\prime}$ and a list $A$ of other variables,

$$
f\left|{ }_{e^{\prime} \equiv e}(e=\alpha, A)=f\left(e=\alpha, e^{\prime}=\alpha, A\right)\right.
$$

for each possible value $\alpha$ of $e$. For any factor $f\left(e^{\prime}, A\right)$ of $e^{\prime}$ and a list $A$ of other variables not containing $e$,

$$
\left.f\right|_{e^{\prime}=e}(e=\alpha, A)=f\left(e^{\prime}=\alpha, A\right)
$$

for each possible value $\alpha$ of $e$. For any factor $f$ not involving $e^{\prime},\left.f\right|_{e^{\prime}=e}=f$.
Suppose $f$ involve two deputy variables $e_{1}^{\prime}$ and $e_{2}^{\prime}$ and we want to eliminate both of them. It is evident that the order by which the deputy variables are eliminated does not affect the resulting factor. We shall denote the resulting factor by $\left.f\right|_{e_{1}^{\prime}=e_{1}, e_{2}^{\prime}=e_{2}}$.

### 5.2 ๑-HOMOGENEOUS FACTORIZATIONS

For later convenience, we introduce the concept of $\otimes$ homogeneous factorization in term of joint potentials. Let $x_{1}, x_{2}, \ldots, x_{n}$ be a list of variables. A joint potential $P\left(x_{1}, x_{2}, \ldots, x_{n}\right)$ is simply a non-negative function of the variables. Joint probabilities are special joint potentials that sum to one.
Consider a joint potential $P\left(e_{1}, \ldots, e_{k}, x_{k+1}, \ldots, x_{n}\right)$ of new regular variables $e_{i}$ and old regular variables $x_{i}$. A list of factors $f_{1}, \ldots, f_{m}$ of the $e_{i}$ 's, their deputies $e_{i}^{\prime}$, and the $x_{i}$ 's is a $\otimes$-homogeneous factorization (reads circle cross homogeneous factorization) of $P\left(e_{1}, \ldots, e_{k}, x_{k+1}, \ldots, x_{n}\right)$ if

$$
P\left(e_{1}, \ldots, e_{k}, x_{k+1}, \ldots, x_{n}\right)=\left(\otimes_{i=1}^{m} f_{i}\right)\left|{ }_{e_{1}^{\prime}=e_{1}, \ldots, e_{k}^{\prime}=e_{k}}\right.
$$

Theorem 1 Let $\mathcal{F}$ be the heterogeneous factorization represented by a $B N$ and let $\mathcal{F}^{\prime}$ be the list of factors obtained from $\mathcal{F}$ by deputing all convergent variables. Then $\mathcal{F}^{\prime}$ is a $\otimes$-homogeneous factorization of the joint probability entailed by the $B N$.

All proofs are omitted due to space limit. Since the operator $\otimes$ is commetative and associative, the theorem states that factors can be combined in arbitrary order after deputation.

## 6 SUMMING OUT VARIABLES

Summing out a variable from a factorization is a fundamental operation in many inference algorithms. This section shows how to sum out a variable from a $\otimes$ homogeneous factorization of a joint potential.
Let $\mathcal{F}$ be a $\otimes$-homogeneous factorization of a joint potential $P\left(x_{1}, x_{2}, \ldots, x_{n}\right)$. Consider the following procedure.

Procedure $\operatorname{sumoutc}\left(\mathcal{F}, x_{1}\right)$

1. If $x_{1}$ is a new regular variable, remove from $\mathcal{F}$ all the factors that involve the deputy $x_{1}^{\prime}$ of $x_{1}$, combine them by $\otimes$ resulting in, say, $f$. Add the new factor $\left.f\right|_{x_{1}^{\prime}=x_{1}}$ to $\mathcal{F}$. Endif
2. Remove from $\mathcal{F}$ all the factors that involve $x_{1}$, combine them by using $\otimes$ resulting in, say, $g$. Add the new factor $g$ to $\mathcal{F}$.
3. Return $\mathcal{F}$.

Theorem 2 The list of factors returned by $\operatorname{sumoutc}\left(\mathcal{F}, x_{1}\right)$ is a $\otimes$-homoogeneous factorization of $P\left(x_{2}, \ldots, x_{n}\right)=\sum_{x_{1}} P\left(x_{1}, x_{2}, \ldots, x_{n}\right)$.

## 7 MODIFYING CLIQUE TREE PROPAGATION

Theorem 2 allows one to exploit ICI in many inference algorithms, including VE and CTP. This paper shows how CTP can be modified to take advantage of the theorem. The modified algorithm will be referred to as CTPI. As CTP, CTPI consists of five steps; namely clique tree construction, clique tree initialization, evidence absorption, propagation, and posterior probability calculation. We shall discuss the steps one by one. Familiarity with CTP is assumed.

### 7.1 CLIQUE TREE CONSTRUCTION

A clique is simply a subset of nodes. A clique tree is a tree of cliques such that if a node appear in two different cliques then it appears in all cliques on the path between those two cliques.
A clique tree for a BN is constructed in two steps: first obtain an undirected graph and then build a clique tree for the undirected graph. CTPI and CTP differ only in the first step. CTP obtains an undirected graph by marrying the parents of each node (i.e. by adding edges between the parents so that they are pairwise connected) and then drop directions on all arcs. The resulting undirected graph is called a moral graph of the BN.

In CTPI, only the parents of regular nodes (representing old regular variables) are married. The parents of convergent nodes (representing new regular variables) are not married. The clique tree constructed in CTPI has the following properties: (1) for any regular node there is a clique that contain the node as well as all its parents and (2) for any convergent node $e$ and each of its parents $x$ there is a clique that contains both $e$ and $x$.

### 7.2 CLIQUE TREE INITIALIZATION

CTPI initializes a clique tree as follows:

1. For each regular node, find one clique that contains the node as well as all its parents and attach the conditional probability of the node to that clique.
2. For each convergent node $e$
(a) If there is a clique that contains the node and all its parents, regard $e$ as a regular node and proceed as in step 1.
(b) Otherwise for each parent $x$ of $e$, let $f(x, e)$ be the contributing factor of $x$ to $e$. Find one clique that contains both $e$ and $x$, attached to that clique the factor $f\left(x, e^{\prime}\right)$, where $e^{\prime}$ is the deputy of $e$.

After initialization, a clique is associated with a list (possibly empty) of factors.
A couple of notes are in order. Factorizing the conditional probability table of a convergent variable $e$ into smaller pieces can bring about gains in inference efficiency because the smaller pieces can be combined with other factors before being combined with themselves, resulting in smaller intermediate factors. If there is a clique that contains $e$ and all its parents, then all the smaller pieces are combined at the same time when processing the clique. In such a case, we are better off to regard $e$ as a regular node (representing an old regular variable).
Second, in CTP all factors associated with a clique are combined at initialization and the resulting factor still involves only those variables in the clique. It is not advisable to do the same in CTPI because the factors involve not only variables in the clique but also deputies of new regular variables in the clique. Combining them all right away can create an unnecessarily large factor and leads to inefficiency. Experiments have confirmed this intuition.
On the other hand, if all variables that appear in one factor $f$ in the list also appear in another factor $g$ in the list, it does not increase complexity to combine $f$ and $g$. Thus we can reduce the list by carrying out such combinations. Thereafter, we keep the reduced list of factors and combine a factor with others only when we have to.
Since $\otimes$ is commutative and associative, the factors associated the cliques constitute a $\otimes$-homogenous factorization of the joint probability entailed by the BN.

### 7.3 EVIDENCE ABSORPTION

Suppose a variable $x$ is observed to take value $\alpha$. Let $\chi_{x=\alpha}(x)$ be the function that takes value 1 when $x=\alpha$ and 0 otherwise. CTPI absorbs the piece of evidence that $x=\alpha$ as follows: find all factors that involve $x$ and multiply $\chi_{x=\alpha}(x)$ to those factors.
Let $x_{m+1}, \ldots, x_{n}$ be all the observed variables and $\alpha_{m+1}, \ldots, \alpha_{n}$ be their observed values. Let $x_{1}, \ldots$, $x_{m}$ be all unobserved variables. After evidence absorption, the factors associated with the cliques constitute a $\otimes$-homogenous factorization of joint potential $P\left(x_{1}, \ldots, x_{m}, x_{m+1}=\alpha_{m+1}, \ldots, x_{n}=\alpha_{n}\right)$ of $x_{1}, \ldots$, $x_{m}$.

### 7.4 CLIQUE TREE PROPAGATION

Just as in CTP, propagation in CTPI is done in two sweeps. In the first sweep messages are passed from the leaf cliques toward a pivot clique and in the second sweep messages are passed from the pivot clique toward the leaf cliques. Unlike in CTP where messages passed between neighboring cliques are factors, in CTPI messages passed between neighboring cliques are lists of factors.
Let $C$ and $C^{\prime}$ be two neighboring cliques. Messages can be passed from $C$ to $C^{\prime}$ when $C$ has received messages from all the other neighbors. Suppose $x_{1}, \ldots, x_{l}$ are all the variables in $C \backslash C^{\prime}$. Let $\mathcal{F}$ be the list of the factors associated with $C$ and the factors sent to $C$ from all other neighbors of $C$. Messages are passed from $C$ to $C^{\prime}$ by using the following subroutine.

Procedure sendMessage $\left(C, C^{\prime}\right)$

1. For $i=1$ to $l, \mathcal{F}=\operatorname{sumoutc}\left(\mathcal{F}, x_{i}\right)$, Endfor
2. Reduce the list $\mathcal{F}$ of factors and send the reduced list to $C^{\prime}$.

### 7.5 POSTERIOR PROBABILITIES

Theorem 3 Let $C$ be a clique and let $x_{1}, \ldots, x_{l}$ be all unobserved variables in $C$. Then the factors associated with $C$ and the factors sent to $C$ from all its neighbors constitute a $\otimes$-homogeneous factorization of $P\left(x_{1}, \ldots, x_{l}, x_{m+1}=\alpha_{m+1}, \ldots, x_{n}=\alpha_{n}\right)$.

Because of Theorem 3, the posterior probability of any unobserved variable $x$ can be obtained as follows:

Procedure getProb $(x)$

1. Find a clique $C$ that contains $x$. (Let $x_{2}$, $\ldots, x_{l}$ be all other variables in $C$. Let $\mathcal{F}$ be the list of the factors associated with

![img-1.jpeg](img-1.jpeg)

Figure 2: A clique tree for the BN in Figure 1.
$C$ and the factors sent to $C$ from all its neighbors.)
2. For $i=2$ to $l, \mathcal{F}=\operatorname{sumoutc}\left(\mathcal{F}, x_{i}\right)$, Endfor
3. Combine all factors in $\mathcal{F}$. Let $f$ be the resulting factor.
4. If $x$ is a new regular variable return $\left.f\right|_{x^{\prime}=x} / \sum_{x} f \mid x^{\prime}=x$.
5. Else return $f / \sum_{x} f$.

## 8 AN EXAMPLE

A clique tree for the BN in Figure 1 is shown in Figure 2. After initialization, the lists of factors associated with the cliques are as follows:

$$
\begin{aligned}
& l_{1}=\left\{P(a) f_{11}\left(e_{1}^{\prime}, a\right), f_{21}\left(e_{2}^{\prime}, a\right)\right\} \\
& l_{2}=\left\{P(b) f_{12}\left(e_{1}^{\prime}, b\right), f_{22}\left(e_{2}^{\prime}, b\right)\right\} \\
& l_{3}=\left\{P(c) f_{13}\left(e_{1}^{\prime}, c\right), f_{23}\left(e_{2}^{\prime}, c\right)\right\} \\
& l_{4}=\left\{P\left(e_{3} \mid e_{1}, e_{2}\right)\right\}
\end{aligned}
$$

Several factors are combined due to factor list reduction and combination of factors reduces to multiplication because they do not share convergent variables. Also because $e_{3}$ and all its parents appear in clique 4 , its conditional probability is not factorized. It is hence regarded as an old regular variable.
Suppose $e_{1}$ is observed to take value $\alpha$. Since $P\left(e_{3} \mid e_{1}, e_{2}\right)$ is the only factor that involves $e_{1}$, absorbing the piece of evidence changes the list of factors associated with clique 4 to the following:

$$
l_{4}=\left\{P\left(e_{3} \mid e_{1}, e_{2}\right) \chi_{e_{1}=\alpha}\left(e_{1}\right)\right\}
$$

Suppose clique 4 is chosen to be the pivot. Then messages are first propagated from cliques 1,2 , and 3 to clique 4 and then from clique 4 to cliques 1,2 , and 3 . The message from clique 1 to clique 4 is obtained by
summing out variable $a$ from the list $l_{1}$ of factors. It is the following list of one factor:

$$
\left\{\mu_{1 \rightarrow 4}\left(e_{1}^{\prime}, e_{2}^{\prime}\right)\right\}
$$

where $\mu_{1 \rightarrow 4}\left(e_{1}^{\prime}, e_{2}^{\prime}\right)=\sum_{a} P(a) f_{11}\left(e_{1}^{\prime}, a\right) f_{21}\left(e_{2}^{\prime}, a\right)$. Messages from cliques 2 and 3 to 4 are similar.
To figure out the message from clique 4 to clique 1 , we notice that the list of factors associated with clique 4 and sent to clique 4 from cliques 2 and 3 is:

$$
\left\{P\left(e_{3} \mid e_{1}, e_{2}\right) \chi_{e_{1}=\alpha}\left(e_{1}\right), \mu_{2 \rightarrow 4}\left(e_{1}^{\prime}, e_{2}^{\prime}\right), \mu_{3 \rightarrow 4}\left(e_{1}^{\prime}, e_{2}^{\prime}\right)\right\}
$$

The message is obtained by summing out the variable $e_{3}$ from the list of factors. Summing out $e_{3}$ results in a new factor

$$
\psi\left(e_{1}, e_{2}\right)=\sum_{e_{3}} P\left(e_{3} \mid e_{1}, e_{2}\right) \chi_{e_{1}=\alpha}\left(e_{1}\right)
$$

Hence the message is the following list of factors:

$$
\left\{\mu_{2 \rightarrow 4}\left(e_{1}^{\prime}, e_{2}^{\prime}\right) \otimes \mu_{3 \rightarrow 4}\left(e_{1}^{\prime}, e_{2}^{\prime}\right), \psi\left(e_{1}, e_{2}\right)\right\}
$$

where the first two factors are combined due to factor list reduction. Messages from clique 4 to cliques 2 and 3 are similar.

Consider computing the posterior probability of $e_{3}$. The only clique where we can do this computation is clique 4. The list of factors associated with clique 4 and factors sent to clique 4 from all its neighbors is

$$
\begin{array}{lr}
\left\{P\left(e_{3} \mid e_{1}, e_{2}\right) \chi_{e_{1}=\alpha}\left(e_{1}\right)\right. & \mu_{1 \rightarrow 4}\left(e_{1}^{\prime}, e_{2}^{\prime}\right) \\
\left.\mu_{2 \rightarrow 4}\left(e_{1}^{\prime}, e_{2}^{\prime}\right), \mu_{3 \rightarrow 4}\left(e_{1}^{\prime}, e_{2}^{\prime}\right)\right\} & \\
& \mu_{1 \rightarrow 4}\left(e_{1}^{\prime}, e_{2}^{\prime}\right)
\end{array}
$$

There are two variables to sum out, namely $e_{1}$ and $e_{2}$. Assume $e_{1}$ is summed out before $e_{2}$. The first step in summing out $e^{\prime}$ is to eliminate $e_{1}^{\prime}$, yielding a new factor

$$
\begin{aligned}
& \phi_{1}\left(e_{1}, e_{2}^{\prime}\right)= \\
& {\left[m u_{1 \rightarrow 4}\left(e_{1}^{\prime}, e_{2}^{\prime}\right) \otimes m u_{2 \rightarrow 4}\left(e_{1}^{\prime}, e_{2}^{\prime}\right) \otimes m u_{3 \rightarrow 4}\left(e_{1}^{\prime}, e_{2}^{\prime}\right)\right] \|_{e_{1}^{\prime}=e_{1}}}
\end{aligned}
$$

Then $e_{1}$ itself is summed out, yielding a new factor
$\phi_{2}\left(e_{2}, e_{2}^{\prime}, e_{3}\right)=\sum_{e_{1}} P\left(e_{3} \mid e_{1}, e_{2}\right) \chi_{e_{1}=\alpha}\left(e_{1}\right) \phi_{1}\left(e_{1}, e_{2}^{\prime}\right)$.
And then $e_{2}^{\prime}$ is eliminated, yielding a new factor

$$
\phi_{3}\left(e_{2}, e_{3}\right)=\phi_{2}\left(e_{2}, e_{2}^{\prime}, e_{3}\right) \mid e_{2}^{\prime}=e_{2}
$$

And then $e_{2}$ is summed out, yielding a new factor

$$
\phi_{4}\left(e_{3}\right)=\sum_{e_{3}} \phi_{3}\left(e_{2}, e_{3}\right)
$$

Finally,

$$
P\left(e_{3} \mid e_{1}=\alpha\right)=\frac{\phi_{4}\left(e_{3}\right)}{\sum_{e_{3}} \phi_{4}\left(e_{3}\right)}
$$

## 9 EMPIRICAL COMPARISONS WITH OTHER METHODS

This section empirically compares CTPI with CTP. We also compare CTPI with PD\&CTP, the combination of the parent-divorcing transformation [14] and CTP, and with TT\&CTP, the combination temporal transformation [4] and CTP.
The CPCS networks [19] are used in the comparisons. They are a good testbed for algorithms that exploits ICI since all non-root nodes are convergent. The networks vary in the number of nodes, and the average number of parents of a node, and the average number of possible values of a node (variable). Their specifications are given in the following table.


NN: number of nodes;
AN-PN: average number of parents;
AN-PVN: average number of possible values of a node.

Since clique tree construction and initialization need to be carried out only once for each network, we shall not compare in detail the complexities of algorithms in those two steps, except saying that they do not differ significantly. Computing posterior probabilities after propagation requires very little resources compared to propagation. We shall concentrate on propagation time.

In standard CTP, incoming messages of a clique are combined in the propagation module after message passing. In CTPI, on the other hand, incoming messages are not combined in the propagation module. For fairness of comparison, the version of CTP we implemented postpones the combination of incoming messages to the module for computing posterior probabilities.

Let us define a case to consist of a list of observed variables and their observed values. Propagation time and memory consumption varies from case to case. In the first three networks, the algorithms were tested using 150 randomly generated cases consisting of 5,10 , or 15 observed variables. In the fourth network, only 15 cases were used due to time constraints. Propagation times and maximum memory consumptions across the cases were averaged. The statistics are in Figure 3, where the Y -axises are in logscale. All data were collected using a SPARC20.
![img-2.jpeg](img-2.jpeg)

Figure 3: Average space and time complexities of CTP, PD\&CTP, TT\&CTP, and CTPI on the CPCS networks.

We see that CTPI is faster than all other algorithms and it uses much less memory. In network 4, for instance, CTPI is about 5 faster than CTP, 3 times faster than TT\&CTP, and 3.5 times faster than PD\&CTP. On average it requires 7 MB memory, while CTP requires 15 MB , TT\&CTP requires 22 MB , and PD\&CTP require 17 MB .

The networks used in our experiments are quite simple in the sense that the nodes have a average number of less than 1.5 parents. As a consequence, gains due to exploitation of ICI and the differences among the different ways of exploiting ICI are not very significant. Zhang and Poole [24] have reported experiments on more complex versions of the CPCS networks with combinations of the VE algorithm and methods for exploiting ICI. Gains due to exploitation of ICI and the differences among the different ways of exploiting ICI are much larger. Unfortunately, none of the combinations of CTP and methods for exploiting ICI was able to deal with those more complex network; they all ran out memory when initializing clique trees.
The method of exploiting ICI described in this paper is more efficient than previous method because it di-

rectly takes advantage of the fact that ICI implies conditional probability factorization, while previous methods make use of implications of the fact.

## 10 CONCLUSIONS

We have proposed to method for exploiting ICI in CTP. The method has been empirically shown to be more efficient than the combination of CTP and the network simplification methods for exploiting ICI. Theoretical underpinnings for the method have their roots in Zhang and Poole [24] and are significantly simplified due a deeper understanding of ICI.

## ACKNOWLEDGEMENT

This paper has benefited from discussions with David Poole. Research was supported by Hong Kong Research Council under grant HKUST658/95E and Sino Software Research Center under grant SSRC95/96.EG01.
