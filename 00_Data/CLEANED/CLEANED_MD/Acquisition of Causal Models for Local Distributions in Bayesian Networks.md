# Acquisition of Causal Models for Local Distributions in Bayesian Networks 

Yang Xiang and Minh Truong, University of Guelph, Canada


#### Abstract

To specify a Bayesian network, a local distribution in the form of a conditional probability table, often of an effect conditioned on its $n$ causes, needs to be acquired, one for each non-root node. Since the number of parameters to be assessed is generally exponential in $n$, improving the efficiency is an important concern in knowledge engineering. Non-impeding noisy-AND (NIN-AND) tree causal models reduce the number of parameters to being linear in $n$, while explicitly expressing both reinforcing and undermining interactions among causes. The key challenge in NIN-AND tree modeling is the acquisition of the NIN-AND tree structure. In this work, we formulate a concise structure representation and an expressive causal interaction function of NIN-AND trees. Building on these representations, we propose two structural acquisition methods, which are applicable to both elicitation-based and machine learning-based acquisitions. Their accuracy is demonstrated through experimental evaluations.


## 1 INTRODUCTION

To specify a Bayesian network (BN), for each non-root node, a local distribution in the form of a conditional probability table (CPT) needs to be acquired. A BN is often constructed in the causal direction, in which case a CPT is defined over an effect conditioned on its $n$ causes. In general, the number of parameters to be assessed for specifying a CPT is exponential in $n$. The noisy-OR [Pea88] and several extensions, e.g., [HB96], [GD00], [LG04], reduce the number to being linear in $n$. However, these methods are limited to expressing reinforcing causal interactions [XJ07]. Other methods also exist, e.g., the binary factorization [NCF12].

NIN-AND tree [XJ07] causal models, including their DeMorgan special cases [MD08], extend the noisy-OR by explicitly expressing reinforcing and undermining causal interactions as well as their mixtures at multiple levels. Each model is specified by a linear (in $n$ ) number of parameters and a tree of NIN-AND gates whose number is linear in $n$. A common noisy-AND gate is impeding, where falsity of any cause obstructs the causal influence of remaining causes, forcing the causal probability to zero. An NIN-AND gate is nonimpeding and its causal probability is non-zero if at least one cause is true.

In an NIN-AND tree model, the tree topology encodes types and the order of interactions among causes. To acquire local distributions in BNs by NINAND tree modeling, the main challenge is structural acquisitions, namely, acquisitions of NIN-AND trees. Elicitation of the topology requires nontrivial training of a domain expert on the syntax and semantics of NIN-AND tree models. It also demands nontrivial mental exercise by the expert in order to articulate the partial order of interactions among causes. The usability of NIN-AND tree causal modeling will be enhanced if such training and mental exercise can be
avoided. This paper presents several advancements towards this goal.

We formulate a concise structure representation of NIN-AND trees, called root-labeled trees (RLTs), and present a new algorithm for their enumeration. We define a function, named PCI, that captures pairwise causal interactions encoded by an NIN-AND tree. We prove the expressiveness of PCI functions in the sense that they uniquely identify their generating NIN-AND trees. Based on the RLT enumeration and PCI functions, we propose two methods to acquire NIN-AND trees indirectly through a small subset of acquired probabilities. These numerical parameters can be elicited from a domain expert without abovementioned training and mental exercise. They can also be learned from data, thereby bypassing the need of a domain expert. Hence, the methods apply to both elicitation-based and machine learning-based model acquisitions.

It is important to differentiate between acquisition for the acyclic directed graph (DAG) of a BN and that for the topology of an NIN-AND tree model. The DAG encodes conditional independence among BN variables, while the NIN-AND tree encodes causal interactions and causal independence among cause variables in a BN family (including a child variable and its parents). For instance, the building block patterns previously studied facilitate the construction of DAGs [NFN00]. However, this work concerns NINAND tree acquisitions. Their relation and difference are illustrated in Section 7.4.

Causal modeling with reinforcement and undermining is also studied under the terms synergy and antagonism [CBS08]. Their approach considers only variable based interactions and produces a partially specified BN. The dual NIN-AND gate (see Section 2) is a special case of synergy and the direct NINAND gate is a special case of antagonism. The NIN-

AND tree allows reinforcing (undermining) among variables in a group and undermining (reinforcing) between multiple such groups, and allows multiple levels of such mixtures. Thus, it expresses both variable and group based interactions in a specified and precise manner, which goes beyond the referenced work. Assuming the DAG is specified, the methods proposed enable efficient CPT specification at each node, which leads to a completely defined BN.

The RLT enumeration is an important component of our proposed methods for NIN-AND tree acquisition. Most methods for tree enumeration in the literature do not address this issue. Earlier investigations on RLT enumeration followed an approach of indirect enumeration. A set $\Omega_{n}$ of unlabelled trees of $n$ roots (one leaf) are first enumerated and then each is rootlabeled to produce the set $\Psi_{n}$ of RLTs. Two methods have been proposed under the indirect approach. One is based on local insertion [XLZ09]. Since isomorphic trees may be generated, it requires detection and removal of duplicated trees. Another is based on enumerating partitions of integer $n$ [XZL09], which does not suffer from the duplication generation. A limitation of the indirect approach is that it must deal with mirror-subtrees [XZL09] during root-labeling, whose detection becomes fairly complicated for $n>7$.

In this paper, we instead take a direct approach for RLT enumeration by extending a method [Fel04] for counting evolutionary trees. This method [Fel04] is closely related to our task of RLT enumeration, although it has several limitations. It considers trees of a single root while RLTs have a single leaf. Its tree format differs from standard graphs, where a link may connect to a single node, instead of two (e.g., Fig. 3.5 [Fel04]). It deals with counting, not enumeration. We extend the method into a new algorithm for directly enumerating RLTs of $n$ roots. In comparison with the indirect approach, the direct approach is not as spaceefficient. This is because the indirect approach generates $\Psi_{n}$ from $\Omega_{n}$ while the direct approach generates $\Psi_{n}$ from $\Psi_{n-1}$, and $\left|\Psi_{n-1}\right|$ is much larger than $\left|\Omega_{n}\right|$. The advantage of the direct approach is that it does not suffer from the complication of mirror-subtrees and is therefore much simpler to implement.

Whether PCI functions uniquely identify minimal NIN-AND trees is fundamental to the soundness of one of the structure acquisition methods presented here. This issue is studied empirically [XLZ09] by exhaustively testing for $n \leq 10$. The theorem on the expressiveness of PCI functions in this paper resolves the issue formally and conclusively for all $n$.

The experimental methods used in this work extends those in earlier empirical evaluations of causal models, such as noisy-OR [ZD04] and DeMorgan [MD08]. Their evaluations are based on elicitation only while ours are also enhanced by machine learning-based experiments. Their studies compare between the elicited model CPT and the observed
relative frequency parameters, while we compare the acquired model with the true model. This difference enables a refined analysis of impacts of factors contributing to the acquisition process, including the sampling errors, the retention-articulation (RA) errors, as well as the acquisition method used. Our experimental design more accurately evaluates the effectiveness of the proposed methods, since it is the true model, not its observed version (which contains the sampling and RA errors), that is the target of acquisition. We compare the earlier experimental procedure with ours in Section 7.3.

We show that if the RA errors can be properly controlled, conducting machine learning-based experiments is equivalent to carrying out elicitation-based experiments. Since human participants are costly, the machine learning-based experiments are preferable.

Preliminary results on the proposed acquisition methods were previously presented [XTZ+11]. The remainder of the paper is organized as follows. The background on NIN-AND tree models is covered in Section 2. Section 3 presents the RLT representation and the direct enumeration algorithm. Section 4 defines PCI functions and proves their expressiveness. The structural acquisition methods are presented in Section 5. Section 6 considers parameter acquisition errors and their control. Section 7 reports the experimental study of the proposed methods.

## 2 NIN-AND Tree CAUSAL MODELS

An uncertain cause is a cause that can produce an effect but does not always do so. Flu is a uncertain cause of fever. We focus on binary variables. Denote an effect by $e$ and a set of causes of $e$ by $X=\left\{c_{1}, \ldots, c_{n}\right\}$. Denote $e=$ true by $e^{+}$and $e=$false by $e^{-}$. For each $c_{i}$, where $1 \leq i \leq n$, denote $c_{i}=$ true (active) by $c_{i}^{+}$and $c_{i}=$ false (inactive) by $c_{i}^{-}$.

A causal success is an event that a cause $c_{i}$ caused $e$ to occur when other causes are false. Denote the event by $e^{+} \leftarrow c_{i}^{+}$and its probability by $P\left(e^{+} \leftarrow c_{i}^{+}\right)$. A causal failure is an event where $e$ is false, when $c_{i}$ is true and other causes of $e$ are false. It is denoted by $e^{-} \leftarrow c_{i}^{+}$. Denote the causal success that a set $X=$ $\left\{c_{1}, \ldots, c_{n}\right\}$ of causes caused $e$ by $e^{+} \leftarrow c_{1}^{+} \ldots, c_{n}^{+}$or $e^{+} \leftarrow \underline{x}^{+}$. Denote the set of all causes of $e$ by $C$.

The CPT $P(e \mid C)$ relates to causal probabilities as follows. If $C=\left\{c_{1}, c_{2}, c_{3}\right\}$, then

$$
P\left(e^{+}\left|c_{1}^{+}, c_{2}^{+}, c_{3}^{-}\right)=P\left(e^{+} \leftarrow c_{1}^{+}, c_{2}^{+}\right)\right.
$$

A causal probability (the right-hand side) is always equivalent to a conditional probability (the left-hand side). The converse may not be true. $C$ is assumed to include a leak variable (if any) for causes that are left implicit, and hence $P\left(e^{+}\left|c_{1}^{-}, c_{2}^{-}, c_{3}^{-}\right)=0\right.$.

Causes reinforce each other if they are collectively at least as effective as when only some are acting. For example, consider the effect of curing cancer

with radiotherapy and chemotherapy being its causes. When both are applied, the probability of curing the cancer is improved. Causes undermine each other if they are collectively less effective. Consider a person's well-being as the effect and taking either one of two desirable jobs as the causes. When taking both, the chance of well-being is reduced due to overstress. If $C=\left\{c_{1}, c_{2}\right\}$, and $c_{1}$ and $c_{2}$ undermine each other, the following holds.

$$
\begin{gathered}
P\left(e^{+}\left|c_{1}^{-}, c_{2}^{-}\right)=0, P\left(e^{+}\left|c_{1}^{+}, c_{2}^{-}\right)>0, P\left(e^{+}\left|c_{1}^{-}, c_{2}^{+}\right)>0\right.\right. \\
\left.\left.P\left(e^{+}\left|c_{1}^{+}, c_{2}^{+}\right)<\min \left(P\left(e^{+}\left|c_{1}^{+}, c_{2}^{-}\right), P\left(e^{+}\left|c_{1}^{-}, c_{2}^{+}\right)\right)\right.\right.\right.
\end{gathered}
$$

Def. 1 defines the two types of causal interactions.
Definition 1. Let $R=\left\{W_{1}, W_{2}, \ldots\right\}$ be a partition of a set $X$ of causes, $R^{\prime} \subset R$, and $Y=\cup_{W_{i} \in R^{\prime}} W_{i}$. Sets of causes in $R$ reinforce each other iff

$$
\forall R^{\prime} P\left(e^{+} \leftarrow \underline{y}^{+}\right) \leq P\left(e^{+} \leftarrow \underline{x}^{+}\right)
$$

and they undermine each other iff

$$
\forall R^{\prime} P\left(e^{+} \leftarrow \underline{y}^{+}\right)>P\left(e^{+} \leftarrow \underline{x}^{+}\right)
$$

Reinforcing and undermining occur between individual variables as well as sets of them. In individual cases, $W_{i}$ is a singleton. Otherwise, $W_{i}$ is a generic set. Consider $X=\left\{c_{1}, c_{2}, c_{3}, c_{4}, c_{5}\right\}$

$$
W_{1}=\left\{c_{1}, c_{2}\right\}, W_{2}=\left\{c_{3}, c_{4}, c_{5}\right\}, R=\left\{W_{1}, W_{2}\right\}
$$

While $c_{1}$ and $c_{2}$ undermine each other, and so do $c_{3}$, $c_{4}$ and $c_{5}, W_{1}$ and $W_{2}$ may reinforce each other.
$W_{1}, \ldots, W_{m}$ (disjoint subsets of $X$ ) satisfy failure conjunction iff

$$
\left(e^{-} \leftarrow \underline{w}_{1}^{+}, \ldots, \underline{w}_{m}^{+}\right)=\left(e^{-} \leftarrow \underline{w}_{1}^{+}\right) \wedge \ldots \wedge\left(e^{-} \leftarrow \underline{w}_{m}^{+}\right)
$$

That is, the collective failure is attributed to individual failures. They also satisfy failure independence iff

$$
\begin{aligned}
& P\left(\left(e^{-} \leftarrow \underline{w}_{1}^{+}\right) \wedge \ldots \wedge\left(e^{-} \leftarrow \underline{w}_{m}^{+}\right)\right) \\
= & P\left(e^{-} \leftarrow \underline{w}_{1}^{+}\right) \times \ldots \times P\left(e^{-} \leftarrow \underline{w}_{m}^{+}\right)
\end{aligned}
$$

$W_{1}, \ldots, W_{m}$ (disjoint) satisfy success conjunction iff

$$
\left(e^{+} \leftarrow \underline{w}_{1}^{+}, \ldots, \underline{w}_{m}^{+}\right)=\left(e^{+} \leftarrow \underline{w}_{1}^{+}\right) \wedge \ldots \wedge\left(e^{+} \leftarrow \underline{w}_{m}^{+}\right)
$$

That is, the collective success requires individual effectiveness. They also satisfy success independence iff

$$
\begin{aligned}
& P\left(\left(e^{+} \leftarrow \underline{w}_{1}^{+}\right) \wedge \ldots \wedge\left(e^{+} \leftarrow \underline{w}_{m}^{+}\right)\right) \\
= & P\left(e^{+} \leftarrow \underline{w}_{1}^{+}\right) \times \ldots \times P\left(e^{+} \leftarrow \underline{w}_{m}^{+}\right)
\end{aligned}
$$

Causes are undermining when success conjunction and independence hold. Hence, undermining can be modeled by a direct NIN-AND gate (Fig. 1 (left)). Each root (top) is a single-causal success and the leaf (bottom) is the causal success in question. Success conjunction is encoded by an AND gate and independence is encoded by the disconnection of roots other than through the gate. The leaf event probability is computed by Eqn. (2).
![img-0.jpeg](img-0.jpeg)

Fig. 1. Direct (left) and dual (right) NIN-AND gates

Causes are reinforcing when failure conjunction and independence hold. Hence, reinforcement can be modeled by a dual NIN-AND gate in Fig. 1 (right). Each root is a single-causal failure and the leaf is the causal failure in question. The leaf event probability is computed by Eqn. (1).

By organizing direct and dual gates into a tree, reinforcing, undermining, as well as their mixtures at multiple levels, can be expressed by an NIN-AND tree.

Definition 2. An NIN-AND tree $T$ is a directed tree for an effect $e$ and its active causes $X=\left\{c_{1}, \ldots, c_{n}\right\}$.

An event node (black oval) has an in-degree $\leq 1$ and an out-degree $\leq 1$. A gate node has an in-degree $\geq 2$ and an out-degree 1. A forward link connects an event and a gate. A negation link has a white oval at the gate end. A direct gate is connected to causal successes only and a dual gate is connected to causal failures only.

Each terminal is an event labelled by $e^{+} \leftarrow \underline{y}^{+}$or $e^{-} \leftarrow$ $\underline{y}^{+}$, where $Y \subseteq X$. A single leaf with $\underline{y}^{+}=\underline{x}^{+}$connects to the leaf gate. Each root (indexed by $\bar{i}$ ) satisfies $\underline{y}_{i}^{+} \subset \underline{x}^{+}$, $\underline{y}_{j}^{+} \cap \underline{y}_{k}^{+}=\emptyset$ for $j \neq k$, and $\bigcup_{i} \underline{y}_{i}^{+}=\underline{x}^{+}$.
Example 1. Consider $C=\left\{c_{1}, c_{2}, c_{3}\right\}$. Suppose that $c_{1}$ and $c_{3}$ reinforce each other and collectively they undermine $c_{2}$. The two-level mixture of reinforcing and undermining relative to event $e^{+} \leftarrow c_{1}^{+}, c_{2}^{+}, c_{3}^{+}$is encoded in Fig. 2 (a). The top gate is dual and the leaf gate is direct. The left link into the leaf gate is a negation link.
![img-1.jpeg](img-1.jpeg)

Fig. 2. (a) An NIN-AND tree over $C=\left\{c_{1}, c_{2}, c_{3}\right\}$. (b) An NIN-AND tree over $X=\left\{c_{1}, c_{2}\right\}$.

Example 2. From single-causal probabilities

$$
P\left(e^{+} \leftarrow c_{1}^{+}\right)=0.6, P\left(e^{+} \leftarrow c_{2}^{+}\right)=0.9, P\left(e^{+} \leftarrow c_{3}^{+}\right)=0.8
$$

and Fig. 2 (a), $P\left(e^{+} \leftarrow c_{1}^{+}, c_{2}^{+}, c_{3}^{+}\right)=0.828$ can be derived by applying Eqn. (1) to the dual gate and Eqn. (2) to the direct gate. Using trees derived from Fig. 2 (a) (by removing some nodes, gates and links), Table 1 is derived.

To derive $P\left(e^{+} \mid c_{1}^{+}, c_{2}^{+}, c_{3}^{+}\right)$, for instance, reduce Fig. 2 (a) to (b) to obtain $P\left(e^{+} \leftarrow c_{1}^{+}, c_{2}^{+}\right)=0.54$.

TABLE 1
CPT of NIN-AND tree model in Fig. 2 (a)


In Table 1, $P\left(e^{+} \mid c_{1}^{+}, c_{2}^{-}, c_{3}^{+}\right)$is larger than both $P\left(e^{+} \mid c_{1}^{+}, c_{2}^{-}, c_{3}^{-}\right)$and $P\left(e^{+} \mid c_{1}^{-}, c_{2}^{-}, c_{3}^{+}\right)$: the consequence of reinforcement between $c_{1}$ and $c_{3} . P\left(e^{+} \mid c_{1}^{+}, c_{2}^{+}, c_{3}^{+}\right)$ is less than $P\left(e^{+} \mid c_{1}^{+}, c_{2}^{-}, c_{3}^{+}\right)$and $P\left(e^{+} \mid c_{1}^{-}, c_{2}^{+}, c_{3}^{-}\right)$ : the consequence of undermining between the group $\left\{c_{1}, c_{3}\right\}$ and $c_{2}$.

An NIN-AND tree over $e$ and $C$, and a set of singlecausal probabilities (one for each $c_{i} \in C$ ) define an NIN-AND tree model from which a unique CPT is specified. Although a general NIN-AND tree can have a root that involves multiple causes [XJ07], this work focus on NIN-AND trees where each root involves a single cause. Effect and causes in NIN-AND tree models are not limited to binary, but the binary case is the focus of this work. See [Xia12] for NIN-AND tree models over multi-valued variables.

## 3 Concise NIN-AND Tree Encoding

### 3.1 Root-Labeled Trees

Multiple NIN-AND trees may encode the same causal model, as illustrated below.

Example 3. From $P\left(e^{+} \leftarrow c_{i}^{+}\right)=0.95, P\left(e^{+} \leftarrow c_{2}^{+}\right)=$ $0.9, P\left(e^{+} \leftarrow c_{3}^{+}\right)=0.7$, and $P\left(e^{+} \leftarrow c_{4}^{+}\right)=0.8$, both trees in Fig. 3 yield $P\left(e^{+} \mid c_{1}^{+}, c_{2}^{+}, c_{3}^{+}, c_{4}^{+}\right)=0.9197$. They encode the same model, where $c_{1}, c_{2}$ and $c_{3}$ undermine each other and collectively reinforce $c_{4}$.
![img-2.jpeg](img-2.jpeg)

Fig. 3. NIN-AND trees encoding the same model

NIN-AND tree models can be investigated more effectively if each model is encoded by a unique tree topology. We define such trees below.

Definition 3. Let $T$ be an NIN-AND tree. If $T$ contains a gate $t$ that outputs to gate $g$ of the same type (direct
or dual), delete $t$ and direct its inputs to g. Apply such deletions until no longer possible. The resultant NIN-AND tree is minimal.

Every minimal NIN-AND tree $T$ defines an equivalent class, made of all NIN-AND trees that lead to $T$ by Def. 3. They encode the same causal interaction pattern, as shown by Prop. 1.
Proposition 1. Let $T$ be an NIN-AND tree, and $T^{\prime}$ be its minimal tree. For any set of single-causal probabilities, $T$ and $T^{\prime}$ yield identical leaf event probability.

Proof: Convert $T$ to $T^{\prime}$ stepwise according to Def. 3, and we have the sequence $T=T_{1}, T_{2}, \ldots, T_{k}=T^{\prime}$. Consider $T_{i}$ and $T_{i+1}$, where inputs of gate $t$ in $T_{i}$ become inputs of gate $g$ in $T_{i+1}$ with $t$ deleted. For both $T_{i}$ and $T_{i+1}$, if $t$ is direct (dual) the contribution of each input of $t$ to the output of $g$ follows Eqn. (2) (Eqn. (1)). Hence, the leaf event probability from $T_{i}$ is identical to that from $T_{i+1}$.

This equivalence property implies that the space of NIN-AND tree models is equivalently represented by the space of minimal trees. Furthermore, this space can be more compactly represented by a subspace with half of the size, as shown by Prop. 2.

Proposition 2. Let $\Gamma$ be the collection of minimal NINAND trees for $n$ causes with direct leaf gates, and $\Gamma^{\prime}$ collects those with dual leaf gates. An one-to-one mapping exists between elements of $\Gamma$ and $\Gamma^{\prime}$, defined by replacing each gate with the opposite type.

Proof: Prop. 2 follows from a property of minimal trees. If the leaf gate $g$ is direct, then each gate outputting to $g$ is dual, and its inputs are all from direct gates. That is, from the leaf to roots, gates alternate in types. Hence, for every $T \in \Gamma$, there exists a $T^{\prime} \in \Gamma^{\prime}$, obtained by changing the type of each gate in $T$.

Prop. 2 allows NIN-AND tree models over $n$ causes to be studied by focusing on one of the two subspaces ( $\Gamma$ and $\Gamma^{\prime}$ ), whose elements can be equivalently expressed as follows.

Definition 4. Let $T$ be a minimal NIN-AND tree. A root-labeled-tree (RLT) $L$ relative to $T$ is a directed graph obtained by operating on $T$ as follows.

1) Delete each gate and direct its inputs to output.
2) Delete each non-root label.
3) Replace each root label by the name of the corresponding single cause.

Example 4. Fig. 2 (a) is a minimal tree, and its RLT is shown in Fig. 4.

In a RLT, each root corresponds to a single-causal event. Each non-root corresponds to an NIN-AND gate and its output multi-causal event. We therefore may view a non-root from any of its double perspectives. For instance, when a RLT represents a minimal

![img-3.jpeg](img-3.jpeg)

Fig. 4. The RLT of minimal NIN-AND tree in Fig. 2 (a)
tree in $\Gamma$, we say that its leaf type is direct using the gate perspective. When a RLT represents a tree in $\Gamma^{\prime}$, we say that its leaf is dual.

A RLT $L$ may represent a minimal tree in either $\Gamma$ or $\Gamma^{\prime}$ depending on the type of its leaf, as described above. If not mentioned, we assume $L \in \Gamma$ by default, with its leaf being direct.

Example 5. From Fig. 4 and the direct leaf type, Fig. 2 (a) is uniquely recovered.

RLTs encode NIN-AND trees concisely. They provide a basis to effectively study the space of NINAND trees as presented below.

### 3.2 Enumerating Root-Labeled Trees

Enumeration of NIN-AND trees is an important component of our proposed method for NIN-AND tree acquisition. We consider the equivalent task to enumerate RLTs of $n$ roots. Below, we present a new algorithm for the task, by extending a method [Fel04] for counting evolutionary trees.

Let $L_{n, m}$ be a RLT with $n$ roots and $m \in\{1, \ldots, n-1\}$ non-roots. Let $\Psi_{n, m}$ be the set of all such RLTs. Denote the set of RLTs with $n$ roots as $\Psi_{n}=\cup_{m=1}^{n-1} \Psi_{n, m}$.

```
Algorithm 1. EnuRLT( }n
```

1 create $\Psi_{2}$;
2 for $i=3$ to $n$, do
$3 \quad \Psi_{i, 1}=A d d R o o t T o N o n R o o t\left(\Psi_{i-1,1}, c_{i}\right)$;
$4 \quad \Psi_{i, i-1}=A d d R o o t T o A r c\left(\Psi_{i-1, i-2}, c_{i}\right)$;
5 for $m=2$ to $i-2$,
$6 \quad \Phi=A d d R o o t T o N o n R o o t\left(\Psi_{i-1, m}, c_{i}\right)$;
$7 \quad \Phi^{\prime}=A d d R o o t T o A r c\left(\Psi_{i-1, m-1}, c_{i}\right)$;
$8 \quad \Psi_{i, m}=\Phi \cup \Phi^{\prime} ;$
9 return $\Psi_{n}=\cup_{m=1}^{n-1} \Psi_{n, m}$;
Line 1 creates $\Psi_{2}=\Psi_{2,1}$ that contains a single RLT in Fig. 5 (a). Each iteration of the outer
![img-4.jpeg](img-4.jpeg)

Fig. 5. Illustration of RLT enumeration
for loop enumerates RLTs of $i$ roots in terms of subsets $\Psi_{i, 1}, \ldots, \Psi_{i, i-1}$. For $i=3$, line 3 calls $\operatorname{AddRootToNonRoot}\left(\Psi_{2,1}, c_{3}\right)$ below to produce $\Psi_{3,1}$ (from $\Psi_{2,1}$ ) that contains a single RLT in (b).

Procedure 1. $\operatorname{AddRootToNonRoot}\left(\Psi_{i-1, m}, c_{i}\right)$
1 initialize $\Phi=\emptyset$;
2 for each RLT $L \in \Psi_{i-1, m}$, do
3 for each non-root $v$ in $L$, do
$4 \quad$ create RLT $L^{\prime}=L$;
5 add root $c_{i}$ and $\operatorname{arc}\left(c_{i}, v\right)$ in $L^{\prime}$;
$6 \quad$ add $L^{\prime}$ to $\Phi$;
7 return $\Phi$;
Line 4 calls $\operatorname{AddRootToArc}\left(\Psi_{2,1}, c_{3}\right)$ below to produce $\Psi_{3,2}$ that contains RLTs in (c), (d), and (e). The RLT in (c) is obtained when $v$ is the leaf, and that in (d) is obtained when $v=c_{1}$. Lines 5 to 8 of EnuRLT( $n$ ) are not run for $i=3$. Hence, $\Psi_{3}$ contains four RLTs that are used in the next iteration to produce $\Psi_{4}$.

Procedure 2. $\operatorname{AddRootToArc}\left(\Psi_{i-1, m-1}, c_{i}\right)$
1 initialize $\Phi=\emptyset$;
2 for each RLT $L \in \Psi_{i-1, m-1}$, do
for each node $v$ in $L$, do
$4 \quad$ create RLT $L^{\prime}=L$;
5 add node $x$ and $\operatorname{arc}(v, x)$ in $L^{\prime}$;
$6 \quad$ add root $c_{i}$ and $\operatorname{arc}\left(c_{i}, x\right)$ in $L^{\prime}$;
7 if $v$ has child $y$ in $L$,
$8 \quad$ delete $\operatorname{arc}(v, y)$ in $L^{\prime}$ and add $(x, y)$;
$9 \quad$ add $L^{\prime}$ to $\Phi$;
10 return $\Phi$;
Table 2 shows the number of RLTs for $n \leq 7$.

TABLE 2
Number of RLTs for given $n$


## 4 Pairwise Causal Interaction

The PCI function presented below forms an important component of one of our proposed methods for NINAND tree acquisition.

### 4.1 PCI Functions of Minimal NIN-AND Trees

An NIN-AND tree $T$ specifies how each pair of causes interact. Such interaction can be formally captured as a function introduced below.

Definition 5. Let $x$ and $y$ be roots of a minimal NINAND tree. Let path $_{x}$ be the directed path from $x$ to the leaf and path $_{y}$ be that from $y$. The closest common gate (CCG) of $x$ and $y$ is the first gate common to path $_{x}$ and path $_{y}$.
Example 6. In Fig. 2 (a), the CCG of roots $e^{-} \leftarrow c_{1}^{+}$and $e^{-} \leftarrow c_{2}^{+}$is dual (top), and that of $e^{-} \leftarrow c_{1}^{+}$and $e^{+} \leftarrow c_{2}^{+}$ is direct.

Prop. 3 shows that, given a minimal tree, the interaction between each pair of causes is determined through their CCG.

Proposition 3. Let $x$ and $y$ be roots of a minimal NIN$A N D$ tree, $c_{i}$ and $c_{j}$ be their causes, and $g$ be their CCG. If $g$ is direct, then the interaction between $c_{i}$ and $c_{j}$ is undermining. Otherwise, it is reinforcing.

Proof: Assume that all causes are false except $c_{i}$ and $c_{j}$. Now all gates, except $g$, have no more than one active input event and can be removed. The resultant tree has a single gate $g$ with roots $x$ and $y$.

From Prop. 3, a function of pairwise causal interactions is well-defined, as given below.

Definition 6. Given a minimal NIN-AND tree $T$, the PCI function of $T$ is defined from pairs of distinct causes $\left\{c_{i}, c_{j}\right\}$ to the set $\{r i f, u d m\}$, where r if stands for reinforcing and udm stands for undermining.

Example 7. The PCI function for Fig. 2 (a) is as follows.

$$
p c i\left(c_{1}, c_{2}\right)=u d m, p c i\left(c_{1}, c_{3}\right)=r i f, p c i\left(c_{2}, c_{3}\right)=u d m
$$

The PCI function of a minimal tree can be obtained from its RLT, plus its leaf gate type.

Example 8. Fig. 4 shows the RLT for Fig. 2 (a). View each non-root in Fig. 4 as a gate. The leaf gate in Fig. 2 (a) is direct. Hence, the leaf in Fig. 4 is direct and its non-root parent is dual. Now the CCG for each pair of roots in Fig. 4 can be determined and so can the PCI function.

Each RLT encodes two alternative minimal trees of opposite leaf gate types. Given the PCI function of one minimal tree, that of the other is easily obtained.

### 4.2 Expressiveness of PCI Function

Although PCI functions seem simpler than NIN-AND trees, we show that they are sufficiently expressive and uniquely identify their deriving structures. To differentiate minimal NIN-AND trees through their RLTs, we first define isomorphic RLTs recursively in Def. 7 with its notation illustrated in Fig. 6 (a).
![img-5.jpeg](img-5.jpeg)

Fig. 6. (a) Illustration of notation in Def. 7. (b), (c) Illustrations of isomorphic RLTs.

Definition 7. Let $L$ be a RLT over a set $C$ of causes and $f$ be its leaf. Denote the set of root parents of $f$ by $R$ and the set of non-root parents of $f$ by $N$. Let $L^{\prime}$ be another RLT over $C$, with $f^{\prime}, R^{\prime}$, and $N^{\prime}$ defined similarly.

1) When $N=\emptyset, L$ and $L^{\prime}$ are isomorphic denoted $L \equiv L^{\prime}$, iff $N^{\prime}=\emptyset$.
2) When $N \neq \emptyset, L \equiv L^{\prime}$ iff $R=R^{\prime},|N|=\left|N^{\prime}\right|$, and a one-to-one mapping between $x \in N$ and $x^{\prime} \in N^{\prime}$
exists such that the subtree of leaf $x$ and that of leaf $x^{\prime}$ are isomorphic.

In case (1), since $N=N^{\prime}=\emptyset$, we have $R=R^{\prime}=C$.
Example 9. The RLT in Fig. 6 (b) is isomorphic to that in Fig. 5 (b) due to Def. 7 (1). The RLT in Fig. 6 (c) is isomorphic to that in Fig. 5 (c) due to Def. 7 (2).

PCI functions are sufficiently expressive in that whenever $L \not \equiv L^{\prime}$ their PCI functions differ, and vice versa. This is established in Theorem 1 whose proof utilizes Lemma 1 below.

Lemma 1. Let $L$ and $L^{\prime}$ be RLTs over $C$ such that no roots $v$ and $w$ sharing a child in $L$ are so in $L^{\prime}$, and vice versa. Let a root $w$ be deleted from both RLTs resulting in $L_{1}$ and $L_{1}^{\prime}$, respectively. Then, $L_{1} \not \equiv L_{1}^{\prime}$.

Fig. 7 illustrates $L$ and $L^{\prime}$ of Lemma 1 in (a) and (b), and $L_{1}$ and $L_{1}^{\prime}$ in (c) and (d).
![img-6.jpeg](img-6.jpeg)

Fig. 7. Illustration of Lemma 1
Proof: We prove by contradiction. Let $L$ and $L^{\prime}$ be RLTs satisfying the condition of the lemma. Let $v$ and $w$ be roots with a common child in $L$. Denote the child by $c$. Since they do not share a child in $L^{\prime}$, let $y$ be a root that shares a child with $v$ in $L^{\prime}$. Denote the child by $d$. After the deletion of $w$ from both RLTs, suppose the resultant RLTs satisfy $L_{1} \equiv L_{1}^{\prime}$.

From Def. 7 (2), the subtree of leaf $c$ in $L_{1}$ and the subtree of leaf $d$ in $L_{1}^{\prime}$ are isomorphic because $c$ and $d$ both have parent $v$. Therefore, the parent set of $c$ in $L_{1}$ and that of $d$ in $L_{1}^{\prime}$ must be identical. Since $y$ is the parent of $d$ in $L^{\prime}$, it follows that $y$ is the parent of $d$ in $L_{1}^{\prime}, y$ is the parent of $c$ in $L_{1}$, and $y$ is the parent of $c$ in $L$. Now $v$ and $y$ share a child in both $L$ and $L^{\prime}$, which implies that $L$ and $L^{\prime}$ do not satisfy the condition of the lemma: a contradiction.

Theorem 1. Let $L$ and $L^{\prime}$ be RLTs over a set $C$ of causes, and pci and pci' be their PCI functions, respectively.

Then $L \equiv L^{\prime}$, iff $p c i=p c i^{\prime}$.
Proof: The necessity of the condition is obvious. We prove the sufficiency by induction on $n=|C|$ to show

$$
L \not \equiv L^{\prime} \Rightarrow p c i \neq p c i^{\prime}
$$

Without loss of generality, we assume that the leaf type is direct for both RLTs.

For $n=3$, alternative RLTs are shown in Fig. 5 (b), (c), (d), and (e). If $L$ is as (b) and $L^{\prime}$ is as (c), then $N=$ $\emptyset, N^{\prime} \neq \emptyset$, and hence $L \not \equiv L^{\prime}$. We have $p c i\left(c_{1}, c_{2}\right)=$ $u d m$ while $p c i^{\prime}\left(c_{1}, c_{2}\right)=r i f$. If $L$ is as (c) and $L^{\prime}$ is as (d), then $R=\left\{c_{3}\right\}, R^{\prime}=\left\{c_{2}\right\}$, and hence $L \not \equiv L^{\prime}$. We

have $p c i\left(c_{1}, c_{2}\right)=r i f$ while $p c i^{\prime}\left(c_{1}, c_{2}\right)=u d m$. Each other combination of $L$ and $L^{\prime}$ is similar to one of the two cases above.

Assume $L \not \equiv L^{\prime} \Rightarrow p c i \neq p c i^{\prime}$ for $3 \leq n \leq k$ where $k \geq 3$. We consider $n=k+1$ below. When $N=N^{\prime}=\emptyset$, we have $L \equiv L^{\prime}$. Hence, when $L \not \equiv L^{\prime}$, one of $N$ and $N^{\prime}$ must be non-empty. We assume $N \neq \emptyset$. By Def. 7, $L \not \equiv L^{\prime}$ is equivalent to the mutually exclusive and exhaustive cases below.

1) $R \neq R^{\prime}$ and $R \neq \emptyset$
2) $R \neq R^{\prime}$ and $R=\emptyset$
3) $R=R^{\prime} \neq \emptyset$
4) $R=R^{\prime}=\emptyset$, and there exist two roots of a common child in both $L$ and $L^{\prime}$
5) $R=R^{\prime}=\emptyset$, and there exist no two roots of a common child in both $L$ and $L^{\prime}$
![img-7.jpeg](img-7.jpeg)

Fig. 8. Illustration of analysis for case (1)
For case (1), $v \in R \backslash R^{\prime}$ exists as shown in Fig. 8 (a) for $L$. If $N^{\prime} \neq \emptyset$, then $v$ is an ancestor of some $x \in N^{\prime}$ in $L^{\prime}$, and $x$ must have another root ancestor $w \in C \backslash R^{\prime}$ as shown in (b). No matter where $w$ is located in (a), we have $p c i(v, w)=u d m$ and $p c i^{\prime}(v, w)=r i f$.

If $N^{\prime}=\emptyset, L^{\prime}$ is shown as (c) such that $v$ and $w$ exist in $L$ as (d). We have $p c i(v, w)=r i f$ and $p c i^{\prime}(v, w)=$ udm.
![img-8.jpeg](img-8.jpeg)

Fig. 9. Illustration of analysis for case (2)
For case (2), $v$ and $w$ exist in $L$ (Fig. 9 (a)) such that $v$ is located in $L^{\prime}$ as (b). We have $p c i(v, w)=r i f$ and $p c i^{\prime}(v, w)=u d m$ no matter where $w$ is located in $L^{\prime}$.
![img-9.jpeg](img-9.jpeg)

Fig. 10. Illustration of analysis for case (3)
For case (3) (Fig. 10), let $L_{1}$ and $L_{1}^{\prime}$ be RLTs obtained by removing roots $R=R^{\prime}$ from $L$ and $L^{\prime}$, respectively. For $L_{1}$ and $L_{1}^{\prime}$, we have $n \leq k$ and $L_{1} \not \equiv L_{1}^{\prime}$. By inductive assumption, their PCI functions over $C \backslash R$ differ and hence PCI functions for $L$ and $L^{\prime}$ differ.
![img-10.jpeg](img-10.jpeg)

Fig. 11. Illustration of analysis for case (4)

For case (4), e.g., Fig. 11 (a) and (b), $v$ and $w$ share a common child in both $L$ and $L^{\prime}$. After $w$ is deleted, we obtain $L_{1}$ and $L_{1}^{\prime}$, e.g., (c) and (d). From $L \not \equiv L^{\prime}$ and the fact that their non-isomorphism cannot be due to $w$, it follows $L_{1} \not \equiv L_{1}^{\prime}$. Since $n=k$ for $L_{1}$ and $L_{1}^{\prime}$, by inductive assumption $L_{1} \not \equiv L_{1}^{\prime} \Rightarrow p c i_{1} \neq p c i_{1}^{\prime}$, we have $p c i_{1} \neq p c i_{1}^{\prime}$. Because for each pair $x, y \in C \backslash\{w\}$, $p c i(x, y)=p c i_{1}(x, y)$ holds and $p c i^{\prime}(x, y)=p c i_{1}^{\prime}(x, y)$ holds, we conclude $p c i \neq p c i^{\prime}$.

For case (5), delete a root $w$ from $L$ and $L^{\prime}$ to get $L_{1}$ and $L_{1}^{\prime}$. By Lemma 1 and an inductive argument similar to case (4), we conclude $p c i \neq p c i^{\prime}$.

Theorem 1 implies that a minimal NIN-AND tree can be uniquely identified by its PCI function. We will explore this property below.

## 5 NIN-AND Tree Acquisition

Drawing from the results of the last two sections, this section presents two methods for the acquisition of an NIN-AND tree, one based on the structure elimination and another on PCI functions.

### 5.1 Approach and Assumption

Formally, an NIN-AND tree model $M$ is a tuple $M=(e, C, T, S P)$, where $e$ is an effect, $C$ is the set of all causes of $e, T$ is a minimal NIN-AND tree over $e$ and $C$, and $S P$ is a set of single-causal probabilities (single-causals), one for each $c_{i} \in C . M$ uniquely specifies a CPT $P(e \mid C) . M$ and $P(e \mid C)$ are said to be consistent.

Furthermore, two models $M=(e, C, T, S P)$ and $M^{\prime}=\left(e, C, T^{\prime}, S P^{\prime}\right)$ are structurally consistent, if $T$ and $T^{\prime}$ are isomorphic. $M$ and $M^{\prime}$ are said to be consistent, if they are consistent with the same CPT.

Given $e$ and $C$, acquisition of a model $M$ amounts to acquisition of $T$ and $S P . S P$ may be elicited from a domain expert or learned from frequency data. The focus of this paper is on the acquisition of $T$.

The topology $T$ may be elicited directly from an expert. The task requires the expert to have a good understanding of the syntax and semantics of NIN-AND tree causal models in order to assess and articulate the partial order of interactions among causes and cause groups. This demands a nontrivial amount of training of the expert before elicitation and nontrivial mental exercise of the expert during elicitation.

To ease these burdens for structural acquisition, we explore the following idea to bypass direct tree elicitation. Instead, we acquire (by elicitation or machine

learning) a small number of multi-causal probabilities (multi-causals) in addition to probabilities in $S P$ and generate $T$ from the acquired probabilities. Our investigation is based on the following assumption.
Assumption. Let $P_{t}(e \mid C)$ be the true CPT that characterizes the probabilistic relation over $e$ and $C$ such that the following holds.

1) There exists an NIN-AND tree model, $M_{t}=$ $\left(e, C, T_{t}, S P_{t}\right)$, that is consistent with $P_{t}(e \mid C)$.
2) All single-causal and some multi-causal probabilities relative to $P_{t}(e \mid C)$ can be approximately acquired.

The first condition is justified by the following observation. Reinforcement and undermining capture intuitive patterns of causal interactions, and reinforcement-based causal models, such as the noisyOR, have been widely applied, e.g., [PPMH94]. The second condition is justified by the knowledge engineering practice in building BNs, where numerical probabilities have been either elicited from experts or learned from available data. Note that the true CPT is never known in practice.

### 5.2 Structure Elimination (SE) Method

The SE method is based on the RLT enumeration $\Psi_{n}$ (may be obtained before model acquisition). From $\Psi_{n}$, the set $T R$ of minimal NIN-AND trees over $C$ can be obtained by specifying two trees (of opposite leaf types) from each RLT. First, a set $S P_{a}$ of $n=|C|$ single-causals, e.g., $P_{a}\left(e^{+} \leftarrow c_{i}^{+}$), is acquired ('a' for 'acquired'). Combining each $T \in T R$ with $S P_{a}$, a set $N M_{a}$ of NIN-AND tree models is obtained. In general, a unique CPT over $e$ and $C$ is defined by each model in $N M_{a} .{ }^{1}$ A set $C P T S_{a}$ of CPTs is thus defined. Note that there is a one-to-one mapping between $T R$ and $N M_{a}$, and generally also between $N M_{a}$ and $C P T S_{a}$.

Subsequently, some multi-causals are acquired. Suppose $P_{a}\left(e^{+} \leftarrow c_{i}^{+} c_{j}^{+}, c_{k}^{+}\right)$is acquired. For each $T^{\prime} \in T R, M^{\prime}=\left(e, C, T^{\prime}, S P_{a}\right) \in N M_{a}$ and $P^{\prime}(e \mid C) \in$ $C P T S_{a}, P^{\prime}\left(e^{+} \leftarrow c_{i}^{+} c_{j}^{+} c_{k}^{+}\right)$is retrieved from $P^{\prime}(e \mid C)$. If the difference between $P_{a}\left(e^{+} \leftarrow c_{i}^{+} c_{j}^{+}, c_{k}^{+}\right)$and $P^{\prime}\left(e^{+} \leftarrow c_{i}^{+} c_{j}^{+}, c_{k}^{+}\right)$is sufficiently large, $P^{\prime}(e \mid C)$ is deemed inconsistent with the true CPT, and $T^{\prime}, M^{\prime}$ and $P^{\prime}(e \mid C)$ are eliminated from $T R, N M_{a}$ and $C P T S_{a}$, respectively. Based on such comparisons, all trees in $T R$ except one, $T_{a}$, will be eliminated. $T_{a}$ is the acquired NIN-AND tree and $M_{a}=\left(e, C, T_{a}, S P_{a}\right)$ is the acquired model.

Specifically, we adopt the following version of the SE. A set $M P_{a}$ of $K$ multi-causals are acquired, where $K$ is determined based on expert availability in elicitation or data availability in learning. For each $T^{\prime} \in T R$, $M^{\prime}=\left(e, C, T^{\prime}, S P_{a}\right) \in N M_{a}$, and $P^{\prime}(e \mid C) \in C P T S_{a}$, a corresponding set $M P^{\prime}$ of multi-causals is retrieved

[^0]from $P^{\prime}(e \mid C)$. The Euclidean distance between $M P_{a}$ and $M P^{\prime}$ is calculated as follows.
$d m\left(M P_{a}, M P^{\prime}\right)=\sqrt{\frac{1}{K} \sum_{i=1}^{K}\left(P_{a}\left(e^{+} \mid \underline{x}_{i}^{+}\right)-P^{\prime}\left(e^{+} \mid \underline{x}_{i}^{+}\right)\right)^{2}}$.
The tree $T_{a} \in T R$ corresponding to the minimum distance is returned. The algorithm is specified below, where $C$ is a set of $n$ causes of effect $e, \Psi_{n}$ is the enumeration of RLS of $n$ roots by $\operatorname{EnuRLT}(n), S P_{a}$ is a set of $n$ acquired single-causals, and $M P_{a}$ is a set of $K$ acquired multi-causals. Although in general any multi-causals may be used in $M P_{a}$, we use triplecausals in the remainder of the paper.
Algorithm 2. TreeAcqBySE $\left(e, C, \Psi_{n}, S P_{a}, M P_{a}\right)$
Return: a minimal NIN-AND tree;
$1 \quad T R=\emptyset ; N M_{a}=\emptyset ;$
2 for each $L \in \Psi_{n}$,
3 set NIN-AND tree $T$ from $L$ with direct leaf;
4 set NIN-AND tree $T^{\prime}$ from $L$ with dual leaf;
5 add $T$ and $T^{\prime}$ to $T R$;
6 for each $T \in T R$, add $M=\left(e, C, T, S P_{a}\right)$ to $N M_{a}$;
$7 \quad T_{a}=$ null; mindm $=1$;
8 for each $M^{\prime}=\left(e, C, T^{\prime}, S P_{a}\right) \in N M_{a}$,
9 derive $P^{\prime}(e \mid C)$ from $M^{\prime}$;
10 get $M P^{\prime}$ from $P^{\prime}(e \mid C)$ corresponding to $M P_{a}$;
11 if $\operatorname{dm}\left(M P_{a}, M P^{\prime}\right)<$ mindm,
$12 \quad \operatorname{mindm}=\operatorname{dm}\left(M P_{a}, M P^{\prime}\right) ; T_{a}=T^{\prime}$;
13 return $T_{a}$;

### 5.3 PCI Function-Based Method

Based on Theorem 1, we propose a PCI function-based method for acquiring a minimal NIN-AND tree as follows. Suppose $\Psi_{n}$ is given from which the set $T R$ is obtained. From $T R$, a set $P C I F$ of PCI functions is defined, one for each tree $T \in T R$. First, the set $S P_{a}$ is acquired as in the SE method. Then, a set $D P_{a}$ of all double-causals (a total of $n(n-1) / 2$ values) is acquired. From $S P_{a}$ and $D P_{a}$, a PCI function $p c i_{a}()$ is derived and compared against each function $p c i^{\prime}() \in$ $P C I F$. If $p c i_{a}()$ matches $p c i^{\prime}()$, then the NIN-AND tree $T^{\prime} \in T R$ that produces $p c i^{\prime}()$ is the acquired NINAND tree and $M_{a}=\left(e, C, T^{\prime}, S P_{a}\right)$ is the acquired model.

## Practical derivation of PCI function

The key operation is the derivation of $p c i_{a}()$ function from $S P_{a}$ and $D P_{a}$. For any pair of causes $c_{i}, c_{j}$ in an NIN-AND tree model and their causal probabilities

$$
P\left(e^{+} \leftarrow c_{i}^{+}\right), P\left(e^{+} \leftarrow c_{j}^{+}\right), P\left(e^{+} \leftarrow c_{i}^{+}, c_{j}^{+}\right)
$$

Def. 1 dictates that the PCI function pci must satisfy $p c i\left(c_{i}, c_{j}\right)=r i f$ iff

$$
P\left(e^{+} \leftarrow c_{i}^{+} c_{j}^{+}\right) \geq \max \left(P\left(e^{+} \leftarrow c_{i}^{+}\right), P\left(e^{+} \leftarrow c_{j}^{+}\right)\right)
$$


[^0]:    1. When elements of $S P_{a}$ are not unique, multiple models in $N M_{a}$ may be consistent.

and $p c i\left(c_{i}, c_{j}\right)=u d m$ iff

$$
P\left(e^{+} \leftarrow c_{i}^{+}, c_{j}^{+}\right)<\min \left(P\left(e^{+} \leftarrow c_{i}^{+}\right), P\left(e^{+} \leftarrow c_{j}^{+}\right)\right)
$$

In theory, the above decision rule is equivalent to
$p c i\left(c_{i}, c_{j}\right)=\left\{\begin{array}{ll}\text { rif } & \text { if } P\left(e^{+} \leftarrow c_{i}^{+}, c_{j}^{+}\right) \geq P\left(e^{+} \leftarrow c_{i}^{+}\right) \\ \text {udm } & \text { otherwise }\end{array}\right.$
and $P\left(e^{+} \leftarrow c_{j}^{+}\right)$needs not even be involved.
In practice however, due to probability acquisition errors, it is possible that

$$
P_{a}\left(e^{+} \leftarrow c_{i}^{+}\right)<P_{a}\left(e^{+} \leftarrow c_{i}^{+}, c_{j}^{+}\right)<P_{a}\left(e^{+} \leftarrow c_{j}^{+}\right)
$$

Example 10. Suppose that $P_{t}\left(e^{+} \leftarrow c_{i}^{+}\right)=0.6$, $P_{t}\left(e^{+} \leftarrow c_{j}^{+}\right)=0.9$, and $c_{i}$ undermines $c_{j}$. We have $P_{t}\left(e^{+} \leftarrow c_{i}^{+}, c_{j}^{+}\right)=0.54$. Acquired probabilities, however, may satisfy

$$
\begin{aligned}
& P_{a}\left(e^{+} \leftarrow c_{i}^{+}\right)=0.56<P_{a}\left(e^{+} \leftarrow c_{i}^{+}, c_{j}^{+}\right)=0.59 \\
& P_{a}\left(e^{+} \leftarrow c_{i}^{+}, c_{j}^{+}\right)=0.59<P_{a}\left(e^{+} \leftarrow c_{j}^{+}\right)=0.93
\end{aligned}
$$

Alternatively, suppose $c_{i}$ reinforces $c_{j}$. We have instead $P_{t}\left(e^{+} \leftarrow c_{i}^{+}, c_{j}^{+}\right)=1-(0.4 * 0.1)=0.96$. Acquired probabilities may satisfy

$$
\begin{aligned}
& P_{a}\left(e^{+} \leftarrow c_{i}^{+}\right)=0.56<P_{a}\left(e^{+} \leftarrow c_{i}^{+}, c_{j}^{+}\right)=0.91 \\
& P_{a}\left(e^{+} \leftarrow c_{i}^{+}, c_{j}^{+}\right)=0.91<P_{a}\left(e^{+} \leftarrow c_{j}^{+}\right)=0.93
\end{aligned}
$$

In either case, applying Eqn. (6) has a 50\% probability of assigning the PCI function value incorrectly. Applying Eqns. (4) and (5) is not even feasible, because both fail.

To address this issue, we develop the decision rule described in Procedure 3.
Procedure 3. GetPciValue $\left(S P_{a}, D P_{a}, c_{i}, c_{j}\right)$
Return: PCI function value $p c i_{a}\left(c_{i}, c_{j}\right)$;
1 get $p_{i}=P_{a}\left(e^{+} \leftarrow c_{i}^{+}\right)$from $S P_{a}$;
2 get $p_{j}=P_{a}\left(e^{+} \leftarrow c_{j}^{+}\right)$from $S P_{a}$;
3 get $p_{i j}=P_{a}\left(e^{+} \leftarrow c_{i}^{+}, c_{j}^{+}\right)$from $D P_{a}$;
4 if $p_{i j} \geq \max \left(p_{i}, p_{j}\right)$, return rif;
5 else if $p_{i j}<\min \left(p_{i}, p_{j}\right)$, return udm;
$6 \delta_{1}=\left|p_{i j}-\min \left(p_{i}, p_{j}\right)\right| ;$
$7 \delta_{2}=\left|p_{i j}-\max \left(p_{i}, p_{j}\right)\right| ;$
8 if $\delta_{1}<\delta_{2}$, return udm;
9 return rif;
Normal cases are handled by lines 4 and 5 according to Eqns. (4) and (5). When these equations fail due to probability acquisition errors, the PCI function value is determined by lines 6 to 9 . The following example demonstrates correct PCI value assignment when acquisition errors are small.

Example 11. Consider cases in Example 10. For the undermining case, we have $\delta_{1}=0.03$ and $\delta_{2}=0.34$. Hence, $p c i_{a}\left(c_{i}, c_{j}\right)=u d m$ is returned correctly in line 8. For the reinforcing case, we have $\delta_{1}=0.35$ and $\delta_{2}=0.02$. Hence, $p c i_{a}\left(c_{i}, c_{j}\right)=r i f$ is returned correctly in line 9 .

## Handling invalid PCI functions

To derive a PCI function, GetPciValue should be applied to each cause pair. The number of cause pairs is $n(n-1) / 2$. The collection of the $n(n-1) / 2$ function values defines a PCI function. Hence, the number of alternative PCI functions for $n$ causes is $2^{n(n-1) / 2}$.

TABLE 3
Number of PCI functions and minimal NIN-AND trees


Table 3 shows the number of alternative PCI functions and that of minimal NIN-AND trees given $n$. The right-most column is the ratio between the two.

A PCI function is valid if it is derivable from a minimal NIN-AND tree. Otherwise, it is invalid. Table 3 shows that beyond $n=3$, there are more PCI functions than valid ones. It follows that a PCI function derived from GetPciValue may be invalid (due to probability acquisition errors), and there does not exist any corresponding NIN-AND tree.

Let $p c i$ and $p c i^{\prime}$ be PCI functions over $n$ causes. We define their distance by counting the number of cause pairs whose function values differ,

$$
d f\left(p c i, p c i^{\prime}\right)=\sum_{1 \leq i, j \leq n ; i \neq j} d i f f\left(p c i\left(c_{i}, c_{j}\right), p c i^{\prime}\left(c_{i}, c_{j}\right)\right)
$$

where the function $\operatorname{diff}($ ) returns 0 if its arguments are identical and 1 otherwise.

Algorithm 3. TreeAcqByPCI $\left(e, C, \Psi_{n}, S P_{a}, D P_{a}\right)$
Return: a minimal NIN-AND tree;
1 for each pair $c_{i}, c_{j} \in C$,
$2 \quad p c i_{a}\left(c_{i}, c_{j}\right)=$ GetPciValue $\left(S P_{a}, D P_{a}, c_{i}, c_{j}\right)$;
3 create the minimal NIN-AND tree set $T R$ from $\Psi_{n}$;
$4 \quad T_{a}=$ null; mindf $=n^{2}$;
5 for each $T^{\prime} \in T R$,
6 derive PCI function $p c i^{\prime}$ from $T^{\prime}$;
7 if $d f\left(p c i_{a}, p c i^{\prime}\right)=0$, return $T^{\prime}$;
8 if $d f\left(p c i_{a}, p c i^{\prime}\right)<$ mindf,
$9 \quad \operatorname{mindf}=d f\left(p c i_{a}, p c i^{\prime}\right) ; T_{a}=T^{\prime}$;
10 return $T_{a}$;
Let $p c i_{a}$ be obtained by GetPciValue and $p c i^{\prime} \in$ $P C I F$. If $d f\left(p c i_{a}, p c i^{\prime}\right)=0, p c i_{a}$ is valid and we return $T^{\prime} \in T R$ that produces $p c i^{\prime}$. If $d f\left(p c i_{a}, p c i^{\prime}\right)>0$ for each $p c i^{\prime} \in P C I F$, then $p c i_{a}$ is invalid. We select a PCI function $p c i^{*}$, such that $d f\left(p c i_{a}, p c i^{*}\right)$ is minimal (breaking ties arbitrarily) and return $T^{*} \in T R$ that produces $p c i^{*}()$. The PCI function-based method with the above enhancements is specified in Algorithm 3, where $D P_{a}$ is a set of acquired double-causals.

## 6 Parameter Acquisition Errors

This section presents the design of experiments for evaluation of the SE and PCI methods. We discuss potential sources of errors and measures we take to control them.

## Experiment Design

The experiments were divided into elicitation-based (EL-based) and machine learning-based (ML-based). First, a true NIN-AND tree model $M_{t}=\left(e, C, T_{t}, S P_{t}\right)$ was created from which causal scenarios were generated by Monte Carlo simulations. In EL-based experiments, each human participant was trained into an expert with causal scenarios and then a subset of causal probabilities was elicited. In ML-based experiments, the causal scenarios were used to estimate the causal probabilities.

Once the causal probabilities were acquired, they were used to derive a structure $T_{a}$ and corresponding model $M_{a}$ by the SE or PCI method. Effectiveness of the method was measured by the model acquisition error $\operatorname{dm}\left(M_{a}, M_{t}\right)$. In the following, we refer to these acquired causal probabilities as acquired parameters.

In particular, for scenario simulations, the true CPT $P_{t}(e \mid C)$ was derived from $M_{t}$. Given a subset $X \subseteq C$ of active causes, a scenario $\left(e, \underline{x}^{+}\right)$where $e \in\left\{e^{+}, e^{-}\right\}$ was randomly simulated according to $P_{t}\left(e^{+} \leftarrow \underline{x}^{+}\right)$. For EL-based experiments, after seeing a sufficient number of scenarios, for a sufficient number of distinctive $\underline{x}^{+}$(more below), a participant was deemed to be an expert on $M_{t}$. Subsequently, (s)he was asked to articulate the parameters $P_{a}\left(e^{+} \leftarrow \underline{x}^{+}\right)$.

To ensure that a participant's knowledge on $M_{t}$ is entirely from the training and is not biased by other experiences, we created $M_{t}$ to be about phenomena in an imaginary planet, where atmospheric conditions are influenced by conditions of the moon, clouds, certain insects, and plants. An Environment Simulator (ES) was implemented accordingly to allow (s)he to specify active causes $\underline{x}^{+}$and observe simulated effects $e$ in terms of picture icons. This setup ensures the condition (1) in the Assumption.

It is important to note that training experts according to a generated model $M_{t}$ is more advantageous than using real experts from some application environment. The mental model of a real expert is not directly accessible and hence acquisition errors cannot be accurately measured. On the other hand, training experts according to a generated $M_{t}$ allows convenient error measurement as shown below.

## Parameter acquisition errors

In the ML-based experiments, $P_{a}\left(e^{+} \leftarrow \underline{x}^{+}\right)$is estimated from the relative frequency

$$
F\left(e^{+} \leftarrow \underline{x}^{+}\right)=N\left(e^{+} \leftarrow \underline{x}^{+}\right) / N\left(\underline{x}^{+}\right)
$$

where $N\left(e^{+} \leftarrow \underline{x}^{+}\right)$is the number of occurrences of scenario $\left(e^{+}, \underline{x}^{+}\right)$and $N\left(\underline{x}^{+}\right)$is that for $\underline{x}^{+}$. Since
$N\left(\underline{x}^{+}\right)$is finite, the parameter acquisition suffers from sampling errors:

$$
P_{a}\left(e^{+} \leftarrow \underline{x}^{+}\right)=F\left(e^{+} \leftarrow \underline{x}^{+}\right) \neq P_{t}\left(e^{+} \leftarrow \underline{x}^{+}\right)
$$

In the EL-based experiments, since each participant forms $P_{a}\left(e^{+} \leftarrow \underline{x}^{+}\right)$from the training experience on $F\left(e^{+} \leftarrow \underline{x}^{+}\right)$, the parameter acquisition also suffers from the sampling errors.

Furthermore, in the EL-based experiments, a participant may not be able to retain and articulate either $N\left(e^{+} \leftarrow \underline{x}^{+}\right)$and $N\left(\underline{x}^{+}\right)$, or $F\left(e^{+} \leftarrow \underline{x}^{+}\right)$ accurately [KST82]. We refer to these additional errors as retention-articulation (RA) errors.

## Controlling parameter acquisition errors

Without adequately controlling the parameter acquisition errors, the effectiveness of SE and PCI methods cannot be accurately evaluated. To control the sampling errors, we analyze the number $\eta=N\left(\underline{x}^{+}\right)$ required for $F\left(e^{+} \leftarrow \underline{x}^{+}\right)$to be sufficiently close to $p=P_{t}\left(e^{+} \leftarrow \underline{x}^{+}\right)$.

Scenarios $\left(e, \underline{x}^{+}\right)$are simulated through a Bernoulli process. Denote $\theta=N\left(e^{+} \leftarrow \underline{x}^{+}\right) \in\{0,1,2, \ldots, \eta\}$ and it has a binomial distribution

$$
P(\theta)=C(\eta, \theta) p^{\theta}(1-p)^{\eta-\theta}
$$

where $C(\eta, \theta)$ denotes the number of $\theta$-combinations from $\eta$ elements. Now $F\left(e^{+} \leftarrow \underline{x}^{+}\right)=p$ iff $\theta=\eta p$. Define a threshold $\gamma \in(0,1) . F\left(e^{+} \leftarrow \underline{x}^{+}\right)$is deemed close to $p$ iff $\left|F\left(e^{+} \leftarrow \underline{x}^{+}\right)-p\right| \leq \gamma$, which is equivalent to

$$
\left|\eta F\left(e^{+} \leftarrow \underline{x}^{+}\right)-\eta p\right|=|\theta-\eta p| \leq \eta \gamma
$$

Hence, $P(|\theta-\eta p| \leq \eta \gamma)$ signifies the chance with which $F\left(e^{+} \leftarrow \underline{x}^{+}\right)$is close to $p$.

TABLE 4


Table 4 lists $P(|\theta-\eta p| \leq \eta \gamma)$ for $p=0.1,0.2, \ldots, 0.9$ when $\eta=100$ and $\gamma=0.1$. Therefore, if each $\underline{x}^{+}$is simulated $\eta=100$ times, the probability by which $F\left(e^{+} \leftarrow \underline{x}^{+}\right)$differs from $P_{t}\left(e^{+} \leftarrow \underline{x}^{+}\right)$by no more than 0.1 will be at least 0.965 no matter what value $P_{t}\left(e^{+} \leftarrow \underline{x}^{+}\right)$is.

Based on the analysis, we simulated each $\underline{x}^{+}$for 100 scenarios in ML-based experiments. For EL-based experiments, we implemented the ES so that a participant was required to observe at least 100 scenarios for each distinct training $\underline{x}^{+}$before the elicitation starts.

To control RA errors, for each distinct training $\underline{x}^{+}$, the pair of relative frequencies $F\left(e^{+} \leftarrow \underline{x}^{+}\right)$and $F\left(e^{-} \leftarrow \underline{x}^{+}\right)$experienced by the participant during training was made available during elicitation and was shown in a stacked bar graph (Fig. 12). This

![img-11.jpeg](img-11.jpeg)

Fig. 12. Stacked bar graph for $F\left(e^{+} \leftarrow \underline{x}^{+}\right)=0.83$ visual hint for the experienced $F\left(e^{+} \leftarrow \underline{x}^{+}\right)$essentially eliminates retention errors. While it reduces articulation errors, it does not eliminate them as it is visual whereas $P_{a}\left(e^{+} \leftarrow \underline{x}^{+}\right)$is elicited numerically.

The stacked bar graph also allows us to identify outliers in acquired parameters from careless or disinterested participants. For each $P_{a}\left(e^{+} \leftarrow \underline{x}^{+}\right)$, its articulation error can be calculated from the corresponding frequency in the ES log. Since the stacked bar graph bounds articulation errors to below 0.1, any error larger than 0.1 is detected as an outlier.

## 7 EXPERIMENTAL EVALUATION

The objective of experiments was to evaluate whether the SE and PCI methods effectively acquire NINAND trees, under the Assumption (Section 5.1). In addition to EL-based and ML-based experiments, we also compared with the Chow-Liu method [CL68].

### 7.1 Elicitation-Based Experiments

## EL-based experimental setup

Participants were recruited from computer science and engineering students (second year or above). Each participant was trained with a distinct true model $M_{t}=\left(e, C, T_{t}, S P_{t}\right)$, where $n=4 . T_{t}$ was randomly selected from 52 alternatives (see Table 3) and $S P_{t}$ was randomly generated. A training session lasted 10 minutes, during which a participant selected $\underline{x}^{+}$(in the ES) to observe its causal scenarios according to the required parameters and the minimum number (100) of scenarios.

To facilitate evaluation, the SE and PCI methods were compared with the direct numerical (DN) method, where each causal probability in $P_{t}(e \mid C)$ was directly elicited. The total number of parameters is $2^{4}-1=15$, where -1 is due to $P_{t}\left(e^{+} \mid c_{1}^{-}, \ldots, c_{4}^{-}\right)=0$ (Section 2). For PCI, we elicited 10 parameters ( 4 single-causals and $C(4,2)=6$ double-causals). For SE, we elicited 8 parameters ( 4 single-causals and $C(4,3)=4$ triplecausals) so that the parameters differ from PCI.

Each data set consists of a number of causal probabilities elicited from one participant. A data set for evaluation of DN, SE, or PCI method contains 15, 8, or 10 elicited probabilities, respectively. If any acquired parameter was found to be an outlier (Section 6), the entire dataset was dropped from further analysis. After removing 3 outlier datasets, the number of data sets collected are 23, 29, 29, respectively.

The distance between sets of probabilities was measured by Euclidean distance similar to Eqn. (3). If eight parameters were elicited from a participant, his or her parameter acquisition error was calculated using the eight and their counterparts in $P_{t}(e \mid C)$. For a model acquired by any method, its acquisition error was calculated using the 15 parameters of the acquired model and their counterparts in $P_{t}(e \mid C)$.

## EL-based experimental results

Parameter acquisition errors consist of sampling and RA errors. For each participant, these errors were computed from the true CPT $P_{t}(e \mid C)$, a set $F(e \mid C)$ of relative frequencies of simulated scenarios in the ES log, and a set $P_{a}(e \mid C)$ of probability parameters directly elicited. $F(e \mid C)$ and $P_{a}(e \mid C)$ from a given participant may contain less than 15 parameters, when only the PCI or SE method was applied. In particular, for each participant, the sampling error was obtained by $d m\left(P_{t}(e \mid C), F(e \mid C)\right)$, the RA error was obtained by $d m\left(F(e \mid C), P_{a}(e \mid C)\right)$, and the parameter acquisition error was by $d m\left(P_{t}(e \mid C), P_{a}(e \mid C)\right)$.

The three types of errors over all participants are summarized in Table 5. As shown, the elicitation aid by stacked bar graphs had an effective control of RA errors. As a result, parameter acquisition errors are mainly composed of sampling errors.

TABLE 5 Sample means $(\hat{\mu})$ and standard deviations $(\hat{\sigma})$ of parameter acquisition errors over all participants


The DN method directly elicits the CPT $P_{a}^{D N}(e \mid C)$, which is referred to as the CPT elicited by DN. For the SE method, a structure $T_{a}$ (by TreeAcqBySE) and a model $M_{a}$ are derived from elicited probabilities and $P_{a}^{S E}(e \mid C)$ (the CPT elicited by $S E$ ) is defined from $M_{a}$. Similarly, $P_{a}^{P C I}(e \mid C)$ (the CPT elicited by PCI) through TreeAcqByPCI is defined.

For each data set, the Euclidean distance between the true CPT and the CPT elicited by each method was calculated. For each method, DN, SE, and PCI, the distances from corresponding data sets are summarized in Table 6. Out of the 29 data sets applicable

TABLE 6 Sample means $(\hat{\mu})$ and standard deviations $(\hat{\sigma})$ of model acquisition errors by DN, SE and PCI methods


to the PCI method, the true NIN-AND tree topology was recovered in 28 of them (recovery rate $96.6 \%$ ). Out of the 29 data sets applicable to SE, the true topology was recovered in 26 (recovery rate $89.7 \%$ ).

To compare the three methods, the Friedman test ( 3 columns, 23 rows) was performed, based on results from 23 data sets (the remaining data set each contains only parameters sufficient for one of PCI and SE). A rank 1 is associated with the lowest distance. The rank sums for DN, PCI, and SE are 50.0, 42.5, and 45.5 , respectively, and the test statistic is 1.239 . Hence, model acquisition errors from the three methods are comparable (the null hypothesis is not rejected). Since the PCI method acquired 10 parameters, SE acquired 8 , while DN acquired all 15 , the results demonstrate that SE and PCI methods improve efficiency in model acquisition, while maintaining comparable accuracy.

### 7.2 Machine Learning-Based Experiments

## ML-based experimental setup

Although EL-based experiments provided useful empirical evaluations, they were tedious and time consuming due to its human-based nature. The size of our datasets was limited by the participants that we could recruit. The true models used were limited to $n=4$ to reduce the session length for participants. During these experiments, it became clear that, the inputs needed to evaluate the SE and PCI methods are the acquired parameters, and it does not matter whether they are elicited from humans or estimated from data. Hence, ML-based experiments are also valid as long as parameter acquisition errors are comparable. They are advantageous because the feasibility for larger $n$ values and sample sizes, which allows more accurate measure of relative merits of the methods.

ML-based experiments were conducted for 4,000 simulated true models. They were divided into four groups with $n=4,5,6$, and 7 , respectively. Each group consists of 1,000 true models. For each true model $M_{t}=\left(e, C, T_{t}, S P_{t}\right), T_{t}$ was randomly selected (e.g., for $n=7$, from 78416 enumerated alternatives) and $S P_{t}$ was randomly generated. Each $T_{t}$ has between 1 and $n-1$ non-roots. Each method of DN, PCI and SE was applied to each model in each group.

For each true model $M_{t}$, the relative frequency $F\left(e^{+} \leftarrow \underline{x}^{+}\right)$was simulated from $P_{t}(e \mid C)$ for each subset $X \subseteq C$ of active causes. We have chosen the number $\eta$ of simulated scenarios to be 100 to make sampling errors comparable with parameter acquisition errors in EL-based experiments. The acquired parameter $P_{a}\left(e^{+} \leftarrow \underline{x}^{+}\right)$was then estimated by $F\left(e^{+} \leftarrow \underline{x}^{+}\right)$. A total of $2^{n}-1$ parameters were acquired for each $M_{t}$.

The CPT $P_{a}^{D N}(e \mid C)$ acquired by DN is defined directly by the $2^{n}-1$ acquired parameters. For the PCI method, the input is a proper subset of the above $2^{n}-1$ acquired parameters: $n$ single causals and $C(n, 2)$ double-causals (a total of $n *(n+1) / 2$ ). The output is the acquired model CPT $P_{a}^{P C I}(e \mid C)$ (consisting of $2^{n}-1$ parameters). For the SE method, the input is a proper subset of $n$ single causals and
$C(n, 3)$ triple causals, and the acquired model CPT is $P_{a}^{S E}(e \mid C)$. Table 7 summarizes the number of acquired parameters by each method.

TABLE 7
Number of input parameters by DN, SE and PCI


## ML-based experimental results

Table 8 summarizes ML-based experimental results. For the DN method, sample means and standard deviations of $d m\left(P_{t}(e \mid C), P_{a}^{D N}(e \mid C)\right)$ for each group is shown as $\bar{\mu}$-dm and $\bar{\sigma}$-dm in column 2. Corresponding results for PCI and SE are shown in columns 3 and 5. For the PCI method, the true topology recovery rate Rev and the typical model learning time $t t$ (by a 2.9 GHz laptop) are shown in column 4. Corresponding results for SE are shown in column 6.

TABLE 8
Summary of ML-based experimental result


Since $d m\left(P_{t}(e \mid C), P_{a}^{D N}(e \mid C)\right)$ is equivalent to the parameter acquisition error, results in column 2 indicate the magnitudes of parameter acquisition errors for all three methods. They are comparable to that of EL-based experiments (Table 5).

To compare model acquisition errors of the three methods, the Friedman test ( 3 columns, 1,000 rows) was performed for each group. The test statistics for $n=4,5,6$, and 7 are $159.9,256.8,364.4$, and 418.2 , respectively. Hence, the null hypothesis (no significant difference between the three methods) is rejected for each group at the level of significance $\alpha=0.01$.

For the post-hoc analysis, rank sums for each group and each method are shown in Table 9. The rank sum differences for three pairs of methods are derived in Table 10. With an one-sided test for each of the three pairs, the result is the following. PCI is significantly better than DN for $n=4,5,6,7$ at $\alpha=0.01$. SE is significantly better than DN for $n=4,5,6,7$ at $\alpha=$ 0.01 . PCI is significantly better than SE for $n=4,5,6$

TABLE 9
Rank sums of model acquisition errors


TABLE 10
Rank sum differences for post-hoc analysis


TABLE 11
True-model and frequency-based rank sums for PCI


at $\alpha=0.01$, but for $n=7$, it is only better than SE at $\alpha=0.11$. We attribute the improved performance of SE (relative to PCI) for $n=7$ to the use of $50 \%$ more parameters than PCI (42 versus 28).

The superior performance of PCI over SE is also reflected by its true topology recovery rate Rev (columns 4 and 6 in Table 8). The Rev from PCI is at least $6 \%$ higher than SE, for each $n$.

The analysis shows that PCI and SE perform better than DN, and PCI is the best among the three. The PCI and SE methods also used fewer number of acquired parameters (Table 7). The number of acquired parameters by DN is $O\left(2^{n}\right)$, that by SE is $O\left(n^{3}\right)$, and that by PCI is $O\left(n^{2}\right)$. The performance of the PCI method makes it particularly attractive, as it uses the least number of acquired parameters (except for $n=4$ ) but has the best model acquisition accuracy and topology recovery rate.

### 7.3 On True Model Based Approach

Our experiments extended empirical evaluations that were previously performed for causal models [ZD04], [MD08] by including ML-based experiments. Previous methods compared the elicited model CPT and the observed relative frequency parameters (frequency-based), while we compared the acquired model with the true model (true-model-based).

To evaluate the relative merit of the true-modelbased and frequency-based evaluations, the Friedman test ( 3 columns, 1,000 rows) was performed to compare $\operatorname{dm}\left(P_{t}(e \mid C), P_{e}^{D N}(e \mid C)\right), \operatorname{dm}\left(P_{t}(e \mid C), P_{e}^{P C I}(e \mid C)\right)$ (true-model-based), and $\operatorname{dm}\left(P_{e}^{D N}(e \mid C), P_{e}^{P C I}(e \mid C)\right)$ (frequency-based), with rank sums for each group shown in Table 11.

The Friedman test statistics for $n=4,5,6,7$ are much large than the critical value at $\alpha=0.01$. Hence, the null hypothesis is rejected for each $n$. In the post-hoc analysis, one-sided pairwise tests show that, for each $n$, the true-model-based PCI model acquisition error is significantly better than DN, but
the frequency-based error is significantly worse than DN. For instance, when $n=7$, the difference between $R S^{D N}$ and $R S^{P C I}$ is 560 , and that between $R S^{P C I-f}$ and $R S^{D N}$ is 1178 , both exceeding the critical value 104.07 at $\alpha=0.01$.

Similar analysis was also performed for the SE method, with the rank sums shown in Table 12. Again,

TABLE 12
True-model and frequency-based rank sums for SE


the null hypothesis is rejected for each $n$. Pairwise tests in the post-hoc analysis show that the true-model-based SE model acquisition error is significantly better than DN, but the frequency-based error is significantly worse than DN.

These observations suggest that the true-modelbased approach is more accurate, while the frequencybased evaluation may lead to biased conclusions.

### 7.4 Comparing PCI with Chow-Liu Tree Method

To illustrate the fundamental difference between the acquisition of NIN-AND trees and that of BN DAGs, the PCI method was compared against the wellknown C-L method [CL68].

Given a set of discrete variables, the C-L method learns a tree structured BN. To apply C-L in the context of NIN-AND tree acquisition, we assume that the set of variables is the BN family $C e=C \cup\{e\}$, where causes in $C$ are marginally independent of each other (the typical case in an NIN-AND tree model).

To compare PCI with C-L, we generate a true NINAND tree model, sample it, and acquire an NINAND tree and a C-L tree from the frequency data. To apply PCI, a set of single-causals and doublecausals is to be estimated. To apply C-L, however, a set of double-variable marginal probabilities is to be estimated. Note that neither set can be derived from the other set. This means that PCI and C-L must be applied to different sets of input data, which generally contain different levels of sampling errors. This makes it difficult for us to make a fair comparison between the performance of PCI and that of C-L.

To make a fair comparison, we assume that the frequency data are perfect, without sampling errors. That is, input probabilities to each method are directly defined by the true joint probability distribution (JPD) $P(e, C)$ (the subscript $t$ is removed for simplicity). In particular, the input to PCI consists of $P\left(e \leftarrow c_{i}\right)$ for $i=1, \ldots, n$, and $P\left(e \leftarrow c_{i}, c_{j}\right)$ for each pair of $i$ and $j \neq i$. The input to C-L consists of $P(x, y)$ for each pair of $x$ and $y \neq x$, where $x, y \in C e$.

The C-L method identifies a tree skeleton (of undirected links) as a maximum spanning tree, where the weight of a link is defined as the mutual information between the pair of variables. If we apply C-L to the family $C e$, no link between any pair of causes is included in the tree, due to the marginal independence (and hence zero link weight). It follows that the skeleton must be a star, with $e$ at the center.

Next, the skeleton is directed. The C-L requires that each variable has a single parent except for the root. Pearl [Pea88] extended C-L trees to polytrees, where a variable may have multiple parents, by directing a V structure, $x \rightarrow z \leftarrow y$, such that $x$ and $y$ are independent and the other two pairs are dependent. If Pearl's method is applied to the above star, $e$ will be the common child of all causes, whose associated numerical distribution is $P(e \mid C)$. As the result, we have made no progress in reducing its space complexity.

We therefore direct links of the star by following the original C-L method: allowing no more than one parent per variable. The root $r$ can be arbitrarily chosen, and be associated with $P(r)$. Each other variable $x$ with parent $y$ is associated with $P(x \mid y)$. Since the JPD of the resultant BN is independent of the choice of root, we choose $e$ as the root. The JPD of the C-L tree BN is $P^{C L}(e, C)=P(e) P\left(c_{1} \mid e\right) \ldots P\left(c_{n} \mid e\right)$, whose corresponding causal CPT is

$$
P^{C L}(e \mid C)=P(e) P\left(c_{1} \mid e\right) \ldots P\left(c_{n} \mid e\right) /\left(P\left(c_{1}\right) \ldots P\left(c_{n}\right)\right)
$$

To compare PCI with C-L, we compare $\operatorname{dm}\left(P(e \mid C), P^{P C I}(e \mid C)\right)$ with $\operatorname{dm}\left(P(e \mid C), P^{C L}(e \mid C)\right)$. Since applying the PCI method to the perfect data always returns the true model, it follows that $\operatorname{dm}\left(P(e \mid C), P^{P C I}(e \mid C)\right)=0$. Hence, the relative merit of PCI versus C-L is completely characterized by $\operatorname{dm}\left(P(e \mid C), P^{C L}(e \mid C)\right)$. Table 13 shows the experimental result over 4,000 randomly simulated true model JPDs (each consisting of an NIN-AND tree model plus a marginal for each cause), with 1,000 true models for each $n$ value. The result

TABLE 13
Summary of model acquisition errors by C-L method


indicates that the causal CPT acquired by the C-L
method has on average at least 0.13 absolute error per conditional probability, given perfect input data. Since the corresponding error by the PCI method is zero, the PCI method is clearly superior. Note that the acquired C-L BN encodes that any $c_{i}$ and $c_{j}$, where $i \neq j$, are independent given $e$. Since $C e$ is a BN family, this is false. The NIN-AND tree acquired by PCI makes no such false encoding.

The experiment illustrates the fundamental difference between BN DAG learning and NIN-AND tree acquisition. Both are techniques for reducing the $2^{n}$ parameter complexity. DAG learning does so by encoding conditional independence. Since there is none within a BN family, when forced to do so, C-L encodes false conditional independence relations and results in an inaccurate model. NIN-AND tree acquisition does so by encoding causal interaction and causal independence within the BN family, and therefore is able to reduce the number of parameters from $2^{n}$ to $n$ with an accurate model.

## 8 CONCLUSION

NIN-AND tree causal models are based on intuitive notions of reinforcing and undermining interactions, among causes. Since they are expressive while requiring only a linear number of parameters, they provide a powerful tool for modeling local distributions in graphical models (e.g., BNs). This paper meets a major challenge in the NIN-AND tree modeling: the structural acquisition.

The contributions of this work include the compact RLT representation of NIN-AND trees, a direct RLT enumeration algorithm, the formal establishment of the expressiveness of PCI functions, and the PCI and SE algorithms for NIN-AND tree acquisition through the acquisition of a small set of low order causal probabilities. Both methods are shown to have significantly better model acquisition accuracy than the direct method, while requiring $O\left(n^{2}\right)$ (by PCI) or $O\left(n^{3}\right)$ (by SE) acquired parameters. Both methods are applicable to elicitation-based and machine learningbased acquisitions.

We decomposed parameter acquisition errors into sampling and RA (in elicitation) errors. RA errors may be reduced through training and/or technical aids. For sampling errors, we have shown that, about 100 scenarios per causal combination is sufficient for our methods to work well.

The PCI method extracts the PCI function from acquired single and double-causal probabilities. Alternatively, the function may be directly elicited from the expert by asking for each pair of causal interaction, saving the acquisition of double-causal probabilities. Using such qualitative information in BN construction has been previously studied [DG95], [RG02]. This variation, however, is not applicable to machine learning-based model acquisition.

Although the number of NIN-AND trees grows super-exponentially in $n$ (faster than $n!$ ), it is not an insurmountable obstacle for many reasons. First, RLTs of $n$ roots can be enumerated offline once and reused for acquisition of multiple models. Second, although the number of variables in a BN is unbounded, because an NIN-AND tree models a single CPT (over a single family of variables) in a BN and BNs are intended to be sparse, $n$ is not unbounded. It is expected to be small and commonly no more than 10. Third, when $n$ becomes large, techniques such as divorcing [JN07] can be applied to split the family before applying NIN-AND tree modelling to each reduced family. Finally, the PCI and SE methods, as presented, have time complexities that are linear on the number of NIN-AND trees, and hence are also super-exponential. However, algorithms that only examine a subspace of NIN-AND trees but are based on the fundamental ideas of PCI and SE are possible.

This paper assumes an unknown true NIN-AND tree model. Future work may relax this assumption and explore NIN-AND tree modeling for arbitrary local distributions. In addition, we have proposed SE and PCI methods in the context of binary variables. Another avenue of future research would be to extend this method to allow for multi-valued variables. We have measured modeling errors using the Euclidean distance. Alternative measures, e.g., KL divergence, may also be applied and compared. In our experiments, all acquired parameters assumed roughly the same levels of acquisition errors. It is conceivable that such errors may grow larger in practice as the number of active causes involved in a parameter grows. In that case, comparisons of model acquisition errors are expected to be more favorable for the SE and PCI methods. This is because they need to acquire probabilities over no more than a few active causes (three in our experiments), while the DN method must acquire probabilities over all active causes. More refined experiments may verify such a conjecture.

## ACKNOWLEDGMENT

Support from NSERC is acknowledged. We thank J. Zhu, D. Stanley, and B. Nonnecke for assistance.
