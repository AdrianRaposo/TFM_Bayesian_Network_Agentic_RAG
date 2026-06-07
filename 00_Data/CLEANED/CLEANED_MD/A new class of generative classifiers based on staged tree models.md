# A new class of generative classifiers based on staged tree models 

Federico Carli<br>CARLI@DIMA.UNIGE.IT<br>Dipartimento di Matematica, Università degli Studi di Genova, Genova, Italy<br>Manuele Leonelli<br>MANUELE.LEONELLI@IE.EDU<br>School of Science and Technology, IE University, Madrid, Spain<br>Gherardo Varando<br>GHERARDO.VARANDO@UV.ES<br>Image Processing Laboratory, Universitat de València, València, Spain


#### Abstract

Generative models for classification use the joint probability distribution of the class variable and the features to construct a decision rule. Among generative models, Bayesian networks and naive Bayes classifiers are the most commonly used and provide a clear graphical representation of the relationship among all variables. However, these have the disadvantage of highly restricting the type of relationships that could exist, by not allowing for context-specific independences. Here we introduce a new class of generative classifiers, called staged tree classifiers, which formally account for context-specific independence. They are constructed by a partitioning of the vertices of an event tree from which conditional independence can be formally read. The naive staged tree classifier is also defined, which extends the classic naive Bayes classifier whilst retaining the same complexity. An extensive simulation study shows that the classification accuracy of staged tree classifiers is competitive with that of state-of-the-art classifiers and an example showcases their use in practice.


Keywords: Bayesian networks; Model selection; Staged trees; Statistical classification

## 1. Introduction

The aim of statistical classification is to assign labels to instances described by a vector of feature variables. The classification task is guided by a statistical model learnt using data containing labelled instances. The array of models designed to perform classification is constantly increasing and includes, among others, random forests (Ho, 1995), recursive partitioning (Breiman et al., 1984) and probabilistic neural networks (Specht, 1990).

Bayesian network classifiers (BNCs) (Bielza and Larrañaga, 2014; Friedman et al., 1997) are special types of Bayesian networks (BNs) designed for classification problems. These have been applied to a wide array of real-world applications with competitive classification performance against state-of-the-art classifiers (Flores et al., 2012). There are numerous advantages associated to BNCs. First, they provide an explicit and intuitive representation of the relationship among features represented by a graph. Second, they are a fully coherent probabilistic model thus giving uncertainty measures about the chosen labels. Third, many of the methods and algorithms developed for general BNs can be simply adapted and used for BNCs (see e.g. Benjumeda et al., 2019). Last, they are implemented in various pieces of user-friendly software (see e.g. the bnclassify R package of Mihaljevic et al., 2018). More

generally, BNCs are generative classifiers which give an estimate of the joint distribution of both the features and the class.

One of the main limitations of BNs is that they can only explicitly represent symmetric conditional independences among variables of interest. However, in many applied domains, conditional independences are context-specific, meaning that they only hold for specific instantiations of the conditioning variables. For this reason, numerous extensions of BNs have been proposed that can take into account asymmetric independences (Boutilier et al., 1996; Cano et al., 2012; Jaeger et al., 2006; Pensar et al., 2015, 2016; Poole and Zhang, 2003). With the exception of Jaeger et al. (2006) and Pensar et al. (2015), all these models somehow lose the intuitiveness of BNs since they cannot represent all the models' information into a unique graph.

Despite the efforts in accommodating asymmetries in BNs, the development of BNCs embedding context-specific information has been limited. Solutions proposed to address this issue use the idea of Bayesian multinets (Geiger and Heckerman, 1996), which consist of several networks each associated with a subset of the domain of one variable, often called distinguished. Bayesian multinets have been used for classification in Friedman et al. (1997), Gurwicz and Lerner (2006), Huang et al. (2003) and Hussein and Santos (2004), among others.

In this paper a novel class of generative classifiers based on staged trees (Collazo et al., 2018; Smith and Anderson, 2008) embedding asymmetric conditional independences is considered, and henceforth called staged tree classifiers. Staged trees are defined as probability trees (Shafer, 1996) embellished with asymmetric conditional independence information, represented by a partitioning of the vertices of the tree. Staged tree classifiers are staged trees whose topology is specifically designed for classification problems. Although staged trees have been used in a variety of applications, including the modelling of health problems (Barclay et al., 2013; Keeble et al., 2017) and criminal activities (Collazo and Smith, 2016), their specific use for classification problems has been limited.

Staged tree classifiers are generative classifiers which, whilst extending the class of BNCs to deal with asymmetric conditional independences, share the same advantages of BNCs: first, the relationship between the random variables is still intuitively depicted in a unique graph; second, they are fully coherent probabilistic models; third, learning algorithms already defined for staged trees (e.g. Freeman and Smith, 2011; Silander and Leong, 2013; Leonelli and Varando, 2022a,b) can simply be adapted for classification purposes; fourth, the freely-available R package stagedtrees (Carli et al., 2020) gives an implementation of a variety of learning algorithms and inferential routines to apply the methods in practice.

Mirroring the theory of BNCs, staged tree classifiers of different complexity are discussed and their properties investigated. Notably, the naive staged tree classifier is introduced which is shown to have the same complexity of the standard naive Bayes classifier, but relaxing the strict conditional independence assumptions of naive Bayes. Experimental studies demonstrate that staged tree classifiers have comparable classification rates to state-of-the-art classifiers and outperform other generative classifiers.

The paper is structured as follows. Section 2 introduces the notation and reviews BNCs. Staged trees are reviewed in Section 3. Staged tree classifiers are introduced and studied in Section 4. Section 5 discusses learning algorithms. Section 6 presents an experimental

![img-0.jpeg](img-0.jpeg)

Figure 1: A simple DAG with vertex set $\{1,2,3,4,5\}$ and edge set $\{(1,3),(1,4),(2,4),(3,5),(4,5)\}$.
study and Section 7 discusses a classification application in details. The paper is concluded with a discussion.

# 2. Bayesian network classifiers 

### 2.1 The Bayesian network model

Let $G=\left([p], E_{G}\right)$ be a directed acyclic graph (DAG) with vertex set $[p]=\{1, \ldots, p\}$ and edge set $E_{G}$. Let $\boldsymbol{X}=\left(X_{i}\right)_{i \in[p]}$ be categorical random variables with joint mass function $P$ and sample space $\mathbb{X}=\times_{i \in[p]} \mathbb{X}_{i}$. For $A \subset[p]$, we let $\boldsymbol{X}_{A}=\left(X_{i}\right)_{i \in A}$ and $\boldsymbol{x}_{A}=\left(x_{i}\right)_{i \in A}$ where $\boldsymbol{x}_{A} \in \mathbb{X}_{A}=\times_{i \in A} \mathbb{X}_{i}$. We say that $P$ is Markov to $G$ if, for $\boldsymbol{x} \in \mathbb{X}$,

$$
P(\boldsymbol{x})=\prod_{k \in[p]} P\left(x_{k} \mid \boldsymbol{x}_{\Pi_{k}}\right)
$$

where $\Pi_{k}$ is the parent set of $k$ in $G$ and $P\left(x_{k} \mid \boldsymbol{x}_{\Pi_{k}}\right)$ is a shorthand for $P\left(X_{k}=x_{k} \mid \boldsymbol{X}_{\Pi_{k}}=\right.$ $\boldsymbol{x}_{\Pi_{k}}$ ). Henceforth, we assume the existence of a linear ordering $\sigma$ of $[p]$ for which only pairs $(i, j)$ where $i$ appears before $j$ in the order can be in the edge set.

The ordered Markov condition implies conditional independences of the form

$$
X_{i} \Perp \boldsymbol{X}_{[i-1]} \mid \boldsymbol{X}_{\Pi_{i}}
$$

Definition 1 Let $G$ be a $D A G$ and $P$ Markov to $G$. The Bayesian network model (associated to $G)$ is

$$
\mathcal{M}_{G}=\left\{P \in \Delta_{|\mathbb{X}|-1} \mid P \text { is Markov to } G\right\}
$$

where $\Delta_{|\mathbb{X}|-1}$ is the $(|\mathbb{X}|-1)$-dimensional probability simplex.
Figure 1 reports a simple DAG with five vertices. Any Markov distribution to this DAG must factorize as $P\left(x_{5} \mid x_{3}, x_{4}\right) P\left(x_{4} \mid x_{1}, x_{2}\right) P\left(x_{3} \mid x_{1}, x_{2}\right) P\left(x_{2}\right) P\left(x_{1}\right)$.

Let $\mathcal{G}$ be the set of DAGs with vertex set $[p]$ and ordering $\sigma$. We define the space of BN models over $\boldsymbol{X}$ as $\mathcal{M}_{\mathcal{G}}=\cup_{G \in \mathcal{G}} \mathcal{M}_{G}$

### 2.2 Bayesian networks for classification

Supppose now that $\boldsymbol{X}=\left(X_{1}, \ldots, X_{p}\right)$ is a $p$-dimensional vector of categorical feature variables and $C$ a categorical class variable with sample space $\mathbb{C}$ and $c \in \mathbb{C}$. Given a training

![img-1.jpeg](img-1.jpeg)

Figure 2: Examples of BNCs with three features and one class.
set of labelled observations $\mathcal{D}=\left\{\left(\boldsymbol{x}^{1}, c^{1}\right), \ldots,\left(\boldsymbol{x}^{N}, c^{N}\right)\right\}$, where $\boldsymbol{x}^{i} \in \mathbb{X}$ and $c^{i} \in \mathbb{C}$, the aim of a generative classifier is to learn a joint probability $p(c, \boldsymbol{x})$ and assign a non-labelled instance $\boldsymbol{x}$ to the most probable a posteriori class found as

$$
\arg \max _{c \in \mathbb{C}} p(c \mid \boldsymbol{x})=\arg \max _{c \in \mathbb{C}} p(c, \boldsymbol{x})
$$

Such a classifier is referred to as Bayes classifier.
BNCs are Bayes classifiers that factorize $p(c, \boldsymbol{x})$ according to a BN over the variables $X_{1}, \ldots, X_{p}$ and $C$. Although any BN model could be used for classification purposes, most often the underlying DAG is restricted so that the class variable $C$ has no parents. Therefore, in BNCs the class variable is the root of the DAG and there is a direct link from $C$ to $X_{i}$, for $i \in[p]$, since otherwise features not connected to the class would not provide any information for classification. The simplest possible model is the so-called naive Bayes classifier (Minsky, 1961) which assumes the features are conditionally independent given the class (Figure 2a). BNCs of increasing complexity can then be defined by adding dependences between the feature variables. For instance, the super-parent-one-dependenceestimator (SPODE) BNC (Keogh and Pazzani, 2002) assumes there is a feature parent of all others (Figure 2b). Another commonly used classifier is the tree-augmented naive (TAN) BNC (Friedman et al., 1997) for which each feature has at most two parents: the class and possibly another feature (Figure 2c).

Although BNCs of any complexity can be learnt and used in practice, empirical evidence demonstrates that model complexity does not necessarily implies better classification accuracy (Bielza and Larrañaga, 2014). Despite of their simplicity, naive BNCs have been shown to lead to good accuracy in classification problems (Bielza and Larrañaga, 2014; Flores et al., 2012).

Alongside these empirical evaluations of BNCs, theoretical studies about the expressiveness of such models have appeared. Recently, Varando et al. (2015) and Varando et al. (2016) fully characterized the decision functions induced by various BNCs and consequently derived bounds for their expressive power. They built on the work of Ling and Zhang (2002) that demonstrated that any BNC whose vertices have at most $k$ parents cannot represent any decision function containing $(k+1)$-XORs (also known as parity functions O'Donnell, 2014). Thus naive BNCs are not capable of capturing any 2-XORs. On the positive side, Domingos and Pazzani (1997) demonstrated that naive BNCs are optimal under a $0-1$ loss even when the assumption of conditional independence among features does not hold.

![img-2.jpeg](img-2.jpeg)

Figure 3: An example of an $\mathbf{X}$-compatible staged tree.

# 3. Staged trees 

Because of the strict assumptions on the symmetry of independences among variables in BNs, models accommodating asymmetric conditional independence statements have been developed. Staged trees are one extension of BNs whose conditional independences can still directly be read from the associated graphical representation (Collazo et al., 2018; Smith and Anderson, 2008). However, differently to BNs, whose graphical representation is a DAG, staged trees are constructed from probability trees as detailed next.

## 3.1 $X$-compatible staged trees

Consider a $p$-dimensional random vector $\boldsymbol{X}$ taking values in the product sample space $\mathbb{X}$. Let $(V, E)$ be a directed, finite, rooted tree with vertex set $V$, root node $v_{0}$ and edge set $E$. For each $v \in V$, let $E(v)=\{(v, w) \in E\}$ be the set of edges emanating from $v$ and $\mathcal{L}$ be a set of labels.

Definition 2 An $\mathbf{X}$-compatible staged tree is a triple $(V, E, \theta)$, where $(V, E)$ is a rooted directed tree and:

1. $V=v_{0} \cup \bigcup_{i \in[p]} \mathbb{X}_{[i]}$;
2. For all $v, w \in V,(v, w) \in E$ if and only if $w=\boldsymbol{x}_{[i]} \in \mathbb{X}_{[i]}$ and $v=\boldsymbol{x}_{[i-1]}$, or $v=v_{0}$ and $w=x_{1}$ for some $x_{1} \in \mathbb{X}_{1}$;
3. $\theta: E \rightarrow \mathcal{L}^{*}=\mathcal{L} \times \cup_{i \in[p]} \mathbb{X}_{i}$ is a labelling of the edges such that $\theta\left(v, \boldsymbol{x}_{[i]}\right)=\left(\kappa(v), x_{i}\right)$ for some function $\kappa: V \rightarrow \mathcal{L}$. The function $k$ is called the colouring of the staged tree $T$.

If $\theta(E(v))=\theta(E(w))$ then $v$ and $w$ are said to be in the same stage.
Therefore, the equivalence classes induced by $\theta(E(v))$ form a partition of the internal vertices of the tree in stages.

Definition 2 first constructs a rooted tree where each root-to-leaf path, or equivalently each leaf, is associated to an element of the sample space $\mathbb{X}$. Then a labeling of the edges of such a tree is defined where labels are pairs with one element from a set $\mathcal{L}$ and the other from the sample space $\mathbb{X}_{i}$ of the corresponding variable $X_{i}$ in the tree. By construction, $\mathbf{X}$-compatible staged trees are such that two vertices can be in the same stage if and only if they correspond to the same sample space. Although staged trees can be more generally defined without imposing this condition (see e.g. Collazo et al., 2018), henceforth, and as common in practice, we focus on $\mathbf{X}$-compatible staged trees only (see Leonelli, 2019, for an example of a non $\mathbf{X}$-compatible tree).

Figure 3 reports an $\left(X_{1}, X_{2}, X_{3}\right)$-compatible staged tree over three binary variables. The coloring given by the function $\kappa$ is shown in the vertices and each edge $\left(\cdot,\left(x_{1}, \ldots, x_{i}\right)\right)$ is labeled with $X_{i}=x_{i}$. The edge labeling $\theta$ can be read from the graph combining the text label and the color of the emanating vertex. The staging of the staged tree in Figure 3 is given by the partition $\left\{v_{0}\right\},\left\{v_{1}\right\},\left\{v_{2}\right\},\left\{v_{3}, v_{4}\right\}$ and $\left\{v_{5}, v_{6}\right\}$.

The parameter space associated to an $\mathbf{X}$-compatible staged tree $T=(V, E, \theta)$ with labeling $\theta: E \rightarrow \mathcal{L}^{*}$ is defined as

$$
\Theta_{T}=\left\{\boldsymbol{y} \in \mathbb{R}^{|\theta(E)|} \mid \forall e \in E, y_{\theta(e)} \in(0,1) \text { and } \sum_{e \in E(v)} y_{\theta(e)}=1\right\}
$$

Equation (3) defines a class of probability mass functions over the edges emanating from any internal vertex coinciding with conditional distributions $P\left(x_{i} \mid \boldsymbol{x}_{[i-1]}\right), \boldsymbol{x} \in \mathbb{X}$ and $i \in[p]$. In the staged tree in Figure 3 the staging $\left\{v_{3}, v_{4}\right\}$ implies that the conditional distribution of $X_{3}$ given $X_{1}=0$, and $X_{2}=0$, represented by the edges emanating from $v_{3}$, is equal to the conditional distribution of $X_{3}$ given $X_{1}=0$ and $X_{2}=1$. A similar interpretation holds for the staging $\left\{v_{5}, v_{6}\right\}$. This in turn implies that $X_{3} \perp X_{2} \mid X_{1}$, thus illustrating that the staging of a tree is associated to conditional independence statements.

Let $\boldsymbol{l}_{T}$ denote the leaves of a staged tree $T$. Given a vertex $v \in V$, there is a unique path in $T$ from the root $v_{0}$ to $v$, denoted as $\lambda(v)$. The number of edges in $\lambda(v)$ is called the distance of $v$, and the set of vertices at distance $k$ is denoted by $V_{k}$. For any path $\lambda$ in $T$, let $E(\lambda)=\{e \in E: e \in \lambda\}$ denote the set of edges in the path $\lambda$.

Definition 3 The staged tree model $\mathcal{M}_{T, \theta}$ associated to the $\mathbf{X}$-compatible staged tree $(V, E, \theta)$ is the image of the map

$$
\begin{aligned}
& \phi_{T}: \Theta_{T} \rightarrow \Delta_{\left|\boldsymbol{l}_{T}\right|-1}^{\circ} \\
& \phi_{T}: y \mapsto p_{l}=\left(\prod_{e \in E(\lambda(l))} y_{\theta(e)}\right)_{l \in \boldsymbol{l}_{T}}
\end{aligned}
$$

Therefore, staged trees models are such that atomic probabilities are equal to the product of the edge labels in root-to-leaf paths and coincide with the usual factorization of mass functions via recursive conditioning.

Let $\Theta$ be the set of functions $\theta$ from $E$ to $\mathcal{L}^{*}$, that is all possible partitions, or staging, of the staged tree. We define $\mathcal{M}_{T}=\cup_{\theta \in \Theta} \mathcal{M}_{T, \theta}$. So as $\mathcal{M}_{\mathcal{G}}$ is the union of all possible BN models given a specific ordering, $\mathcal{M}_{T}$ is the union of all possible staged tree models, that is of all possible stagings, given a specific ordering of the variables.

![img-3.jpeg](img-3.jpeg)

Figure 4: An example of a staged tree not associated to any BN $G$.

# 3.2 Staged trees and Bayesian networks 

Smith and Anderson (2008) demonstrated that any BN can be represented as an equivalent staged tree, whilst the converse is not true. We next illustrate how to construct a staged tree equivalent to a BN. Consider a DAG $G$ and an $\mathbf{X}$-compatible staged tree with vertex set $V$, edge set $E$ and labeling $\theta$ defined via the coloring $\kappa\left(\boldsymbol{x}_{[i]}\right)=\boldsymbol{x}_{\Pi_{i}}$ of the vertices. The staged tree $T_{G}$, with vertex set $V$, edge set $E$ and labeling $\theta$ so constructed, is called the staged tree model of $G$. Importantly, $\mathcal{M}_{G}=\mathcal{M}_{T_{G}, \theta}$, i.e. the two models are exactly the same, since they entail exactly the same factorization of the joint probability (Varando et al., 2021). The staging of $T_{G}$ represents the Markov conditions associated to the graph $G$.

For instance, the staged tree in Figure 3 can be constructed as the $T_{G}$ from the BN with DAG $X_{2} \leftarrow X_{1} \rightarrow X_{3}$. Conversely, consider the staged tree in Figure 4. The blue staging implies that the conditional distribution of $X_{3}$ given $X_{2}=X_{1}=0$ is equal to the conditional distribution of $X_{3}$ given $X_{2}=X_{1}=1$. Such a constraint cannot be explicitly represented by the DAG of a BN and therefore there is no DAG $G$ such that $\mathcal{M}_{G}=\mathcal{M}_{T_{G}, \theta}$, i.e. there is no BN which is equivalent to the staged tree in Figure 4. More generally, it holds that $\mathcal{M}_{\mathcal{G}} \subset \mathcal{M}_{T}$ (Varando et al., 2021).

## 4. Staged tree classifiers

The technology of staged trees has been refined over the years and methods to investigate causal relationships (Genewein et al., 2020; Thwaites et al., 2010), perform statistical inference (Görgen et al., 2015), check model's robustness (Leonelli et al., 2017) and carry out causal discovery (Leonelli and Varando, 2021) are now available. However, the specific use of staged trees for classification has not been investigated in the literature. Thus, just as BNCs have been defined as a specific subclass of BNs whose graph entertains some properties, the class of staged tree classifiers is defined here.

As in Section 2, suppose $\boldsymbol{X}=\left(X_{1}, \ldots, X_{n}\right)$ is a vector of features and $C$ is the class variable.

![img-4.jpeg](img-4.jpeg)

Figure 5: Representation of BNCs as staged trees classifiers: (a): naive BNC in Figure 2a as a staged tree classifier; (b): SPODE BNC in Figure 2b as a staged tree classifier; (c): TAN BNC in Figure 2c as a staged tree classifier. All variables are assumed binary.

Definition 4 A staged tree classifier for the class $C$ and features $\boldsymbol{X}$ is a $(C, \boldsymbol{X})-$ compatible staged tree.

The requirement of $C$ being the root of the tree follows from the idea that in most BNCs the class has no parents, so to maximise the information provided by the features for classification.

# 4.1 The relationship between BNCs and staged tree classifiers 

The BNCs reviewed in Section 2 can now be represented as staged tree classifiers. Since a BNC is a BN with a DAG $G$, one can construct its equivalent staged tree $T_{G}$ as in Section 3.2. For instance naive BNCs (Figure 5a), SPODE BNCs (Figure 5b) and TAN BNCs (Figure 5c) can concisely be represented as staged tree classifiers. However, the class of staged trees classifiers is much larger than that of BNCs, as formalized in Proposition 5. For a class $C$ and features $\boldsymbol{X}$, let $\mathcal{M}_{\mathcal{G}}^{\mathrm{C}}$ be the space of BNCs (where $C$ is the root), and $\mathcal{M}_{T}^{\mathrm{C}}$ the space of $(C, \boldsymbol{X})$-compatible staged trees.

Proposition $5 \mathcal{M}_{\mathcal{G}}^{\mathrm{C}} \subset \mathcal{M}_{T}^{\mathrm{C}}$.
The proof follows from Varando et al. (2021).
In particular naive Bayes, SPODE, and TAN classifiers are all staged tree classifiers with a specific staging structure as described next for the naive Bayes. Recall that the set $V_{k}$ includes the nodes of the tree at distance $k$ from the root and let $T(v)$ be the subtree of $T$ rooted at a vertex $v$.

Proposition 6 Let $G$ be the $D A G$ of a naive $B N C$. Then $T_{G}$ is a $(C, \boldsymbol{X})$-compatible staged tree where, for all $v \in V_{1}$, the subtree $T_{G}(v)$ is a $\boldsymbol{X}$-compatible staged tree where all nodes at the same distance from the root are in the same stage. In particular, $T_{G}$ has $|\mathcal{C}|$ stages per each feature.

![img-5.jpeg](img-5.jpeg)

Figure 6: Staged trees classifiers embedding conditional independence statements between features and the class. (a): $X_{3} \Perp C$; (b): $X_{3} \Perp C \mid X_{1}, X_{2}$.

# 4.2 Conditional independence in staged tree classifiers 

For the specific task of classification, it is possible to derive two results about the dependence between the features and the class in staged tree classifiers.

Proposition 7 If all $v \in V_{k}$ of a staged tree classifier are in the same stage then $\left(C, X_{1}, X_{2}, \ldots, X_{k-1}\right)$ and $X_{k}$ are marginally independent, i.e. $\left(C, X_{1}, \ldots, X_{k-1}\right) \Perp X_{k}$.

Proposition 8 If for all $v \in V_{1}, T(v)$ has the same stage structure over the vertices at distance $k-2$ from the root, then $X_{k}$ is independent of $C$ conditionally on $X_{1}, \ldots, X_{k-1}$, i.e. $C \Perp X_{k} \mid X_{1}, \ldots, X_{k-1}$.

These two results are illustrated in Figure 6. For instance, consider the features associated to the last random variable in Figure 6b. The vertices in the upper half are framed as the vertices in the bottom half thus implying that the class variable is conditionally independent of the last feature given all others.

### 4.3 Naive staged tree classifiers

The class of staged tree classifiers is extremely rich and for any classification task the number of candidate models that could explain the relationship between class and features increases exponentially. One first common assumption that we make here is to consider only $(C, \boldsymbol{X})$-compatible staged trees, ones where only vertices at the same distance from the root can be in a same stage. However, even with this assumption the model class of staged tree classifiers is still much richer than that of BNCs. Therefore, just like BNCs whose DAGs have restricted topologies (as SPODE and TAN classifiers) have been studied, next we introduce a class of simpler staged tree classifiers.

We have discussed that in many practical applications the naive BNC has very good classification performance despite of its simplicity. A naive BNC has a total of $\sum_{j=1}^{n}|\mathbb{C}|$. $\left(\left|\mathbb{X}_{j}\right|-1\right)+|\mathbb{C}|-1$ free parameters that need to be learnt, whilst its DAG is always fixed. Similarly, we introduce a class of staged tree classifiers which has the constraint of having the same number of free parameters as naive BNCs, and therefore has the same complexity, whilst being a much richer class of models then the naive BNC.

Definition $9(A(C, \boldsymbol{X})$-compatible staged tree classifier such that for every $k \leq p$, the set $V_{k}$ is partitioned into $|\mathbb{C}|$ stages is called naive.

It staightforwardly follows from the definition that naive staged tree classifiers have the same number of free parameters as naive Bayes classifiers.

Despite of the strict constraint on the number of parameters, the class of naive staged tree classifiers is still rich and extends naive BNCs in a non-trivial way. More formally, let $\mathcal{M}_{\mathcal{G}}^{\text {naive }}$ and $\mathcal{M}_{T}^{\text {naive }}$ be the space of naive BNCs and of naive staged tree classifiers, respectively, for a class $C$ and features $\boldsymbol{X}$.

Proposition $10 \mathcal{M}_{\mathcal{G}}^{\text {naive }} \subset \mathcal{M}_{T}^{\text {naive }}$.
Differently to naive BNCs, it is not sufficient to simply learn the probabilities of the naive staged tree classifier, but also the staging structure has to be discovered. However, because of the strict restriction on the number of parameters, fast algorithms can be devised to efficiently explore the model space. Notice that in a binary classification problem the set $V_{k}$ must be partitioned into two subsets.

Critically and differently to naive Bayes classifiers, naive staged trees are capable of representing complex decision rules. For instance, consider the simplest scenario of a binary class with two binary features. The naive staged tree classifier in Figure 4 (assuming the first variable is the class variable), which, as already noticed, does not have a naive BNC representation, is capturing the only 2-XOR present.

To investigate further the capabilities of naive staged tree classifiers in expressing complex decision rules, we simulate $N_{\text {train }}=200$ observations from $n=10$ binary variables $X_{1}, \ldots, X_{10}$ taking values in $\mathbb{X}=\{-1,+1\}^{n}$. We define the class variable as the parity (or XOR) function $C=\prod_{i=1}^{n} X_{i}$ and compare naive Bayes, random forest and naive staged tree classifiers over $N_{\text {test }}=10000$ test instances, obtaining the results in Table 1. See Section 4.3 for details on the learning of naive staged tree classifiers. As expected, the Naive Bayes classifier is unable to represent the parity function (Varando et al., 2015) and wrongly classifies the class in more than $40 \%$ of the test data. Similar performances are obtained by random forests (implemented with the randomForest R package using 500 trees), even if theoretically they have much larger expressive power. Conversely, the naive staged tree correctly learns the parity function with an accuracy of $90 \%$.

# 5. Learning staged tree classifiers 

The learning of the structure of a staged tree from data is challenging due to the exponential increase of the size of the tree with the number of random variables. The first learning algorithm used for this purpose was the agglomerative hierarchical clustering proposed by


Table 1: Proportion of predicted instances in the simulated XOR example for the naive staged tree classifier (ST_Naive), random forest (RFor) and naive Bayes (NB).

Freeman and Smith (2011). Other learning algorithms were then introduced by Silander and Leong (2013) and Collazo and Smith (2016), among others. Recently, a staged trees implementation in R was made available in the stagedtrees package (Carli et al., 2020) with various searching algorithms to estimate stage structures from data.

In this article we present different methods for learning staged tree classifiers. All methods follow three main steps: (i) an optimal order of the variables is identified; (ii) the full probability tree based on all random variables is pruned to speed-up computations; (iii) model search heuristics are used to identify high-scoring structures. We next give details about each of these phases. Furthermore, in Section 5.4 we introduce algorithms specifically designed for naive staged tree classifiers.

# 5.1 Choosing a features' order 

It is well known that the ordering of the variables affect the quality of a statistical classifier (e.g. Hruschka Jr and Ebecken, 2007). Thus, choosing the order of the features in a staged tree classifier is expected to be important in order to obtain good performances.

To confirm this, we perform an empirical study where we compute classification accuracies for different staged tree classifiers over all possible features' orders. Given the combinatorial explosion of the number of orders we limit this study to two illustrative datasets with a small amount of features, namely puffin and monks3 (see Table 2 for details). From Figure 7 we can observe that, as expected, the order of the features is highly relevant with respect to classification performance. For instance, the naive staged tree learnt with hierarchical clustering, ST_Naive (as described in Section 5.4), and the staged tree classifier learnt with the fast backward-hill climbing algorithm, ST_FBHC (maximizing BIC score, see Section 5.3), exhibit a variety of accuracies (from 0.5 to 1) for the same dataset.

It is therefore critical to couple any algorithm to learn a staged tree with an appropriate method to select a good ordering of the variables. For staged tree classifiers, we tested various ordering heuristics and we propose here the use of the conditional mutual information (CMI) criterion. The order of the features given by the CMI criterion is obtained by iteratively selecting the feature that maximise the conditional mutual information with respect to the class variable, given the features previously selected. The performance of such ordering is shown with a cross symbol in Figure 7. We can observe that in both puffin and monks 3 problems, the CMI order leads to a staged tree which perfrom better than the majority of the possible orders.

![img-6.jpeg](img-6.jpeg)

Figure 7: Distribution of accuracy for different orders of features. Accuracies obtained with the CMI ordering are shown with a cross. Results using two learning algorithms for datasets puffin and monks3.

# 5.2 Dealing with unobserved instances 

Once the order of the variables is selected, it is possible that some of the nodes in the tree are not observed in the training data. For such nodes, estimating the associated probabilities is not possible without further assumptions. As implemented in the R package stagedtrees, for each feature, unobserved situations are joined in a common stage, called unobserved stage, and a uniform probability is imposed for their distribution. Furthermore, such unobserved stages are excluded from the stage structure search. This has the effect of drastically reducing the number of nodes for which a stage structure must be learnt, thus critically reducing training time.

From a statistical point of view, this does not affect the number of free parameters of the corresponding statistical model, since probability distributions of these unobserved stages have not to be estimated. This procedure can be seen as the usual pruning step of learning algorithms for classification trees. From the naive staged tree classifier perspective, it follows that the number of stages in the tree is unaffected, since its complexity, i.e. number of free parameters, does not change.

### 5.3 Learning algorithms

Different heuristic algorithms can be used to search the space of possible stage structures. We rely on the available implementations in the stagedtrees package, in particular we use greedy approaches that maximise the BIC score (Görgen et al., 2020) or iterative methods that join nodes into the same stages based on the distance between their associated probabilities. More details of the algorithms are described in Carli et al. (2020) and in the stagedtrees documentation.


Table 2: Details about the 14 datasets included in the experimental study.

# 5.4 Learning naive staged tree classifiers 

As described in Section 4.3, a naive staged tree classifier is a staged tree where the class is the first variable in the tree and nodes at the same distance from the root are assigned to a fixed number of stages equal to the number of possible values of the class (e.g. two for a binary classification problem).

The two algorithms based on clustering (hierarchical and k-means) available in the stagedtrees package can be used to learn naive staged tree classifiers. They cluster probabilities into a user-selected number of stages which, for the purposes of classification, can be fixed to number of possible values of the class variable.

## 6. Experimental study

The classification accuracy for binary classification of staged tree classifiers is investigated in a comprehensive simulation study involving 14 datasets, whose details are given in Table 2. Each dataset is randomly divided ten times in train set ( $80 \%$ of the data) to learn the classifiers and test set (remaining $20 \%$ ) to predict the response. The reported performance measures, area under the curve (AUC) and balanced accuracy, are computed as the mean over the ten replications.

First, 9 model search algorithms to learn staged tree classifiers are compared, namely: ST_BHC (backward hill-climbing); ST_BJ_01 (backward joining of vertices that have KullbackLeibler divergence between their floret probability distributions less than 0.01); ST_BJ_20 (as ST_BJ_01 but with threshold at 0.20 ); ST_FBHC (a fast backward hill-climbing where two vertices are joined whenever the score is increased); ST_Full (each vertex is in its own stage); ST_HC_Full (hill-climbing algorithm starting from ST_Full); ST_HC_Indep (hillclimbing algorithm starting from a tree where all vertices associated to the same variable

![img-7.jpeg](img-7.jpeg)

Figure 8: AUC, balanced accuracy and logarithm of time spent for structure learning for nine staged tree classifiers algorithms over fourteen datasets.
are in the same stage); ST_Naive_HC (naive staged tree learnt with hierarchical clustering); ST_Naive_KM (naive staged tree learnt with k-means). Further details about these algorithms can be found in Carli et al. (2020). Due to computational restrictions, for ST_HC_Full the model search is restricted to the first five features according to the variable ordering chosen through CMI, whilst for ST_BHC and ST_HC_Indep only the first seven are considered. The vertices corresponding to the remaining variables are still used for classification but left as in the starting tree of the model search.

The results of the experiment are reported in Figure 8, which suggests the following conclusions:

- The ST_Full model (in yellow), which does not require any model search and has the largest number of parameters, has in general lower AUC and balanced accuracy than other staged trees. This highlights the need of a model-based search of simpler models;
- Models based on hill-climbing (in blue) overall perform better than others (in particular ST_HC_Full). This is expected since these are the most refined learning algorithms and, as a consequence, they are also the slowest.
- Models based on backward joining (in green) have a satisfactory performance, often comparable to that of hill-climbing models, whilst being much quicker to learn.
- Naive staged trees (in red) can be learnt extremely quickly and whilst often they have a lower performance, there are cases where they are comparable to the one of much more complex trees (see e.g. the balanced accuracy for the titanic dataset)

Next, we compare staged trees classifiers with their competitor generative classifier, namely BNCs. For ease of exposition, three representative staged trees are selected (ST_BJ_01, ST_HC_Full and ST_Naive_KM) and three BNCs are fitted: (i) the TAN BNC (BNC_TAN);

![img-8.jpeg](img-8.jpeg)

Figure 9: AUC, balanced accuracy and logarithm of time spent for structure learning for three staged tree classifiers (in red) and three BNCs (in blue) over fourteen datasets.
![img-9.jpeg](img-9.jpeg)

Figure 10: AUC, balanced accuracy and logarithm of time spent for structure learning for three staged tree classifiers (in red), two BNCs (in blue) and other discriminative models (in green) over fourteen datasets.
(ii) the 3-dependence BNC (BNC_KDB); (iii) the naive Bayes (BNC_NB). The results are reported in Figure 9. We can see that for most datasets there is one staged tree classifier (in red) that outperforms BNCs (in blue). Due to the complexity of the models, staged trees are in general slower to learn, but the ST_Naive_KM, due to its simplicity, has learning times comparable to those of generic BNCs.

Figure 10 reports the results of the simulation experiments for three staged tree classifiers (ST_BJ_01, ST_HC_Full and ST_Naive_KM) as well as other state-of-the-art generative and discriminative classifiers, namely: (i) the naive Bayes (BNC_NB); (ii) the TAN BNC

![img-10.jpeg](img-10.jpeg)

Figure 11: AUC, balanced accuracy and logarithm of time spent for structure learning for two naive staged tree classifiers (in red) and two implementations of naive Bayes classifiers (in blue) over fourteen datasets.
(BNC_TAN); (iii) Classification trees (CTree) (iv) Logistic regression (Logistic); (v) Neural Networks with 20 hidden layers and 0.01 weight decay (NNet); (vi) Random Forests combining 100 classification trees (RFor). Although in some cases discriminative classifiers (in green) outperform staged trees (in red), in many others they have comparable AUC and balanced accuracy. However, as shown in the next section, staged tree classifiers have the capability of producing an understanding of the relationship between the class and the features, since they are generative models. As already noticed, staged trees have an advantage over BNCs (in blue). Although the learning time for generic staged trees is larger, the learning time for naive staged tree classifiers is comparable to that of state-of-the-art classifiers.

Last, we compare the performance of naive Bayes classifiers with the one of naive staged tree classifiers in Figure 11. The overall conclusion is that in most cases naive staged trees (in red) outperform naive Bayes in terms of AUC and balanced accuracy. Furthermore, although naive staged trees require more learning time since their structure has to be discovered, these can be learnt very quickly and most times in less than one second.

# 7. An example of a staged tree classifier 

To illustrate the capabilities of staged trees classifiers we next develop an example classification analysis over the freely available titanic dataset, which provides information on the fate of the Titanic passengers. It has three binary variables (Survived, Sex and Age) and a categorical variable Class taking four levels (1st, 2nd, 3rd and Crew). The aim is to correctly classify whether the Titanic passengers survived or not based on their gender, age and travelling class.

From Figure 8 we can see that one of the best staged tree classifiers is the ST_BJ_01 learnt using a backward joining of the vertices based on the Kullback-Leibler divergence

![img-11.jpeg](img-11.jpeg)

Figure 12: Staged tree classifier ST_BJ_01 learnt over the full Titanic dataset.
and a threshold of 0.1. In Figure 12 we report the staged tree classifier ST_BJ_01 learnt over the full Titanic dataset using the R package stagedtrees. By investigating the staging structure we can deduce conditional independence statements relating to the classification variable (Survived) and the features. From stages associated to Class we can deduce that $P($ Class $\mid$ Sex $=$ Male, Survived $)=P($ Class $\mid$ Sex $=$ Male $)$ since the second and the fourth vertices (starting from the top) are in the same stage. This implies the asymmetric conditional independence

$$
\text { Class } \Perp \text { Survived } \mid \text { Sex }=\text { Male }
$$

The complex staging structure over the Age variable also implies asymmetric conditional independences. We can notice that all paths going through an edge labelled Crew are in the same stage for the variable Age. This implies that

$$
\text { Age } \Perp \text { Survived } \mid \text { Class }=\text { Crew }
$$

The same conclusion can also be drawn for Class $=3 \mathrm{rd}$.
As an additional illustration in Figure 13 is reported the naive staged tree classifier learnt over the full Titanic dataset using the k-means hierarchical clustering algorithm. The staging structure over the variables Sex and Class implies that Sex and Survived are not independent and that Class is conditionally independent of Survived given Sex. The staging structure over the Age variable is a lot more complex describing highly asymmetric constraints on the associated probabilities. Whilst imposing much more flexible dependence structures, the naive staged tree classifier has the same complexity of the naive Bayes classifier, meaning they have the same number of independent parameters.

BNCs of different complexity are also learnt over the full titanic dataset using the bnclassify R package. Irrespective of the complexity chosen, the model selection search always returns the simple naive Bayes classifier. Given that staged tree classifiers outperfom BNCs in classification measures for the Titanic dataset (see Figure 9), as well as for other datasets, this observations highlights the need of context-specific generative classifiers that

![img-12.jpeg](img-12.jpeg)

Figure 13: Naive staged tree classifier learnt over the full Titanic dataset using the stages_kmeans algorithm.
can more flexibly model the dependence structure between the classification variable and the features.

# 8. Discussion 

Staged trees classifiers are a highly-expressive new class of generative classifiers with classification performance comparable to that of state-of-the-art classifiers. They embed contextspecific conditional independence statements which can be easily read by the staging of the vertices of the tree. These are implemented in the freely available stagedtrees R package.

A special staged tree classifier is the naive staged tree classifier which, whilst having the same complexity as the naive Bayes classifier, can flexibly represent complex classification rule. Naive staged trees not only relax the assumption of conditional indepedence of the features as in naive Bayes classifiers but also have better performances in classification, as highlighted by the simulation study.

Naive staged trees are learnt from data using a clustering algorithm of the probability distributions over the non-leaf vertices of the tree. Such algorithms divide the vertices at the same distance from the root in $|\mathbb{C}|$ stages. More generally, we could devise clustering algorithms were, for each variable, the number of stages is automatically selected according to an optimality criterion. The development of these algorithms is the focus of ongoing research.

Furthermore, many model search algorithms implemented in stagedtrees are based on the maximization of a model score, by the default the negative BIC. We are currently investigating algorithms based on the minimization of the classification error, as commonly implemented for BNCs.

# Acknowledgments 

Gherardo Varando's work was partly funded by the European Research Council (ERC) Synergy Grant "Understanding and Modelling the Earth System with Machine Learning (USMILE)" under Grant Agreement No 855187.
