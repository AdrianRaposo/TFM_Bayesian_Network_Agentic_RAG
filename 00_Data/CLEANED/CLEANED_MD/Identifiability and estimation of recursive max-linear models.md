# Identifiability and estimation of recursive max-linear models 

Nadine Gissibl* Claudia Klüppelberg* Steffen Lauritzen ${ }^{\dagger}$<br>January 10, 2019


#### Abstract

We address the identifiablity and estimation of recursive max-linear structural equation models represented by an edge weighted directed acyclic graph (DAG). Such models are generally unidentifiable and we identify the whole class of DAGs and edge weights corresponding to a given observational distribution. For estimation, standard likelihood theory cannot be applied because the corresponding families of distributions are not dominated. Given the underlying DAG, we present an estimator for the class of edge weights and show that it can be considered a generalized maximum likelihood estimator. In addition, we develop a simple method for identifying the structures of the DAGs. With probability tending to one at an exponential rate with the number of observations, this method correctly identifies the class of DAGs and, similarly, exactly identifies the possible edge weights.


MSC 2010 subject classifications: Primary 60E15, 62H12; secondary 62G05, 60G70, 62-09
Keywords and phrases: Causal inference, Bayesian network, directed acyclic graph, extreme value theory, generalized maximum likelihood estimation, graphical model, identifiability, max-linear model, structural equation model.

## 1 Introduction

Establishing and understanding cause-effect relations is an omnipresent desire in science and daily life. It is especially important when dealing with extreme events, because they are mostly dangerous and very costly; knowing and understanding the causes of such events and their causal relations could help us to deal better with them. Examples include incidents at airplane landings (Gissibl et al. [13]), flooding in river networks (Asadi et al. [1]), financial risk (Einmahl et al. [8]), and chemical pollution of rivers (Hoef et al. [15]). Such applications, where extreme risks may propagate through a network, have been the motivation behind the definition of recursive max-linear (ML) models in Gissibl and Klüppelberg [12]. Recursive ML models are structural equation models (SEMs) represented by a directed acyclic graph (DAG) and thereby obey the basic Markov properties associated with directed graphical models (Lauritzen [21], Lauritzen

[^0]
[^0]:    *Center for Mathematical Sciences, Technische Universität München, 85748 Garching, Boltzmannstrasse 3, Germany; e-mail: n.gissibl@tum.de, cklu@tum.de
    ${ }^{\dagger}$ Department of Mathematical Sciences, University of Copenhagen, Universitetsparken 5, 2100 Copenhagen, Denmark; e-mail: lauritzen@math.ku.dk

et al. [22]). Both SEMs (see for example Bollen [3], Pearl [23]) and directed graphical models (see for example Koller and Friedman [19], Lauritzen [20], Spirtes et al. [27]) are well-established concepts for the understanding and quantification of causal inference from observational data. We note that Hitz and Evans [14] and Engelke and Hitz [9] discuss graphical models for extremes that are based un undirected graphs.

Recursive ML models are defined by a DAG, a collection of edge weights, and a vector of independent innovations. Important research problems that are addressed for recursive SEMs are the question of identifiability of the coefficients and the associated DAG from the observational distribution. Although the true DAG and edge weights for a recursive ML model are not identifiable from the observational distribution, the so-called max-linear coefficient matrix is identifiable and determines the possible class of DAGs and edge weights uniquely.

We shall show that estimation and structure learning of recursive ML models can be done in a simple and efficient fashion by exploiting properties of the ratios between observable components of the model. For a sufficiently large number of observations, these ratios identify the true ML coefficient matrix with a probability that converges exponentially fast to 1 . For the situation where the DAG is known, we show that our estimator can be considered a maximum likelihood estimator in an extended sense, originally introduced by Kiefer and Wolfowitz [18].

Our paper is organized as follows. In Section 2 we introduce the model class of recursive ML models and the notation used throughout. In Section 3 we discuss the identifiability of a recursive ML model from its observational distribution. Here we show distributional properties of the ratio between two components. Based on these properties, we suggest an identification method. Section 4 is then devoted to the estimation of recursive ML models where we assume the DAG to be known. Among other outstanding properties, we show that the proposed estimates are generalized maximum likelihood estimates (GMLEs) in the sense of Kiefer-Wolfowitz. The main part is here the derivation of a specific Radon-Nikodym derivative. In Section 5 we complement the theoretical findings on the identifiability of recursive ML models with an efficient procedure to learn recursive ML models from observations only, even when the DAG itself is also unknown. Section 6 concludes and suggests further directions of research.

# 2 Preliminaries - recursive max-linear models 

In this section we introduce notation and summarize the most important properties of recursive ML models needed. A recursive ML model for a random vector $\boldsymbol{X}=\left(X_{1}, \ldots, X_{d}\right)$ is specified by an underlying structure in terms of a DAG $\mathcal{D}$ with nodes $V=\{1, \ldots, d\}$, positive edge weights $c_{k i}$ for $i \in V$ and $k \in \mathrm{pa}(i)$, and independent positive random variables $Z_{1}, \ldots, Z_{d}$ with support $\mathbb{R}_{+}:=(0, \infty)$ and atom-free distributions:

$$
X_{i}=\bigvee_{k \in \mathrm{pa}(i)} c_{k i} X_{k} \vee Z_{i}, \quad i=1, \ldots, d
$$

$\{c h 4: s 2\}$
where $\mathrm{pa}(i)$ are the parents of node $i$ in $\mathcal{D}$. To highlight the DAG $\mathcal{D}$, we say that $\boldsymbol{X}$ follows a recursive ML model on $\mathcal{D}$. Note that this is a slight variation of the original definition in [12]. We shall refer to $\boldsymbol{Z}=\left(Z_{1}, \ldots, Z_{d}\right)$ as the vector of innovations.

In the context of risk analysis, natural candidates for distributions of the innovations are extreme value distributions or distributions in their domain of attraction, resulting in a corresponding multivariate distribution (for details and background on multivariate extreme value models, see for example Beirlant et al. [2], de Haan and Ferreira [7], Resnick [24, 25]).

Throughout the paper we use the following notation. The sets $\operatorname{an}(i), \operatorname{pa}(i)$, and $\operatorname{de}(i)$ contain the ancestors, parents, and descendants of node $i$ in $\mathcal{D}$. We set $\operatorname{An}(i)=\operatorname{an}(i) \cup\{i\}$ and $\operatorname{Pa}(i)=$ $\operatorname{pa}(i) \cup\{i\}$. For $U \subsetneq V$ we write $\boldsymbol{X}_{U}=\left(X_{\ell}, \ell \in U\right)$ and accordingly for $\boldsymbol{x} \in \mathbb{R}_{+}^{d}, \boldsymbol{x}_{U}=\left(x_{\ell}, \ell \in U\right)$.

Instead of $k \in \mathrm{pa}(i)$ we also write $k \rightarrow i$. Assigning the weight $d_{j i}(p)=\prod_{\nu=0}^{n-1} c_{k_{\nu} k_{\nu+1}}$ to every path $p=\left[j=k_{0} \rightarrow k_{1} \rightarrow \cdots \rightarrow k_{n}=i\right]$ and denoting the set of all paths from $j$ to $i$ by $P_{j i}$, the non-negative matrix $B=\left(b_{i j}\right)_{d \times d}$ with entries

$$
b_{j i}=\bigvee_{p \in P_{j i}} d_{j i}(p) \quad \text { for } j \in \operatorname{an}(i), \quad b_{i i}=1, \quad \text { and } \quad b_{j i}=0 \quad \text { for } j \in V \backslash \operatorname{An}(i)
$$

is said to be the $M L$ coefficient matrix of $\boldsymbol{X}$. This means for distinct $i, j \in V, b_{j i}$ is positive if and only if there is a path from $j$ to $i$; in that case $b_{j i}$ is the maximum weight of all paths from $j$ to $i$, where the weight of a path is the product of all edge weights $c_{k i}$ along this path. We say that a path from $j$ to $i$ whose weight equals $b_{j i}$ is max-weighted.

The components of $\boldsymbol{X}$ can also be expressed as max-linear functions of their ancestral innovations and an independent one; the corresponding $M L$ coefficients are the entries of $B$ :

$$
X_{i}=\bigvee_{j=1}^{d} b_{j i} Z_{j}=\bigvee_{j \in \operatorname{An}(i)} b_{j i} Z_{j}, \quad i=1, \ldots, d
$$

see Theorem 2.2 of $[12]$.
For two non-negative matrices $F$ and $G$, where the number of columns in $F$ is equal to the number of rows in $G$, we define the matrix product $\odot: \overline{\mathbb{R}}_{+}^{m \times n} \times \overline{\mathbb{R}}_{+}^{n \times p} \rightarrow \overline{\mathbb{R}}_{+}^{m \times p}$ by

$$
\left(F=\left(f_{i j}\right)_{m \times n}, G=\left(g_{i j}\right)_{n \times p}\right) \mapsto F \odot G:=\left(\bigvee_{k=1}^{n} f_{i k} g_{k j}\right)_{m \times p}
$$

where $\overline{\mathbb{R}}_{+}=[0, \infty)$. The triple $\left(\overline{\mathbb{R}}_{+}, \vee, \cdot\right)$, is an idempotent semiring with 0 as 0 -element and 1 as 1-element and the operation $\odot$ is therefore a matrix product over this semiring; see for example Butkovič [4]. Denoting by $\mathcal{M}$ all $d \times d$ matrices with non-negative entries and by $\vee$ the componentwise maximum between two matrices, $(\mathcal{M}, \vee, \odot)$ is also a semiring with the null matrix as 0 -element and the $d \times d$ identity matrix $I_{d}$ as 1 -element.

The matrix product $\odot$ allows us to represent the ML coefficient matrix $B$ of $\boldsymbol{X}$ in terms of the weighted adjacency matrix $\left(c_{i j} \mathbb{1}_{\operatorname{pa}(j)}(i)\right)_{d \times d}$ of $\mathcal{D}$ since (2.2) and (2.3) simply become

$$
B=\left(I_{d} \vee C\right)^{\odot(d-1)}=\bigvee_{k=0}^{d-1} C^{\odot k}, \quad \boldsymbol{X}=\boldsymbol{Z} \odot B
$$

where we have let $A^{\odot 0}=I_{d}$ and $A^{\odot k}=A^{\odot(k-1)} \odot A$ for $A \in \overline{\mathbb{R}}_{+}^{d \times d}$ and $k \in \mathbb{N}$; see Proposition 1.6.15 of Butkovič [4] as well as Theorem 2.4 and Corollary 2.5 of [12].

# 3 Identifiability of a recursive max-linear model 

In this section we discuss the question of identifiability of the elements of a recursive ML model from the distribution $\mathcal{L}(\boldsymbol{X})$ of $\boldsymbol{X}$. We begin with an example.

Example 3.1. [The DAG and the edge weights are not necessarily identifiable]
Consider a recursive ML model on the DAG $\mathcal{D}$ depicted below with edge weights $c_{12}, c_{23}, c_{13}$.

![img-0.jpeg](img-0.jpeg)

According to (2.1), the components of $\boldsymbol{X}$ have the following representations

$$
X_{1}=Z_{1}, \quad X_{2}=c_{12} X_{1} \vee Z_{2}, \quad \text { and } \quad X_{3}=c_{13} X_{1} \vee c_{23} X_{2} \vee Z_{3}
$$

but also representations in terms of the innovations using (2.3) as

$$
X_{1}=Z_{1}, \quad X_{2}=c_{12} Z_{1} \vee Z_{2}, \quad \text { and } \quad X_{3}=\left(c_{12} c_{23} \vee c_{13}\right) Z_{1} \vee c_{23} Z_{2} \vee Z_{3}
$$

If $c_{13} \leqslant c_{12} c_{23}$ we have for any $c_{13}^{*} \in\left[0, c_{12} c_{23}\right]$ that $b_{13}=c_{12} c_{23} \vee c_{13}^{*}=c_{12} c_{23} \vee c_{13}=c_{12} c_{23}$; so we could also write

$$
X_{3}=c_{13}^{*} X_{1} \vee c_{23} X_{2} \vee Z_{3}
$$

without changing the distribution $\mathcal{L}(\boldsymbol{X})$ of $\boldsymbol{X}$. This implies that if $c_{13} \leqslant c_{12} c_{23}, \boldsymbol{X}$ follows a recursive ML model on $\mathcal{D}$ with edge weights $c_{12}, c_{23}, c_{13}^{*}$ but also on the DAG $\mathcal{D}^{B}$ depicted below with edge weights $c_{12}, c_{23}$. Consequently, we can neither identify $\mathcal{D}$ nor the value $c_{13}$ from the distribution $\mathcal{L}(\boldsymbol{X})$ of $\boldsymbol{X}$. However, note that the ML coefficient $b_{13}=c_{12} c_{23} \vee c_{13}$ is uniquely determined.

$$
\mathcal{D}^{B} \quad \square \longrightarrow \square \longrightarrow
$$

If we however assume that $c_{13}>c_{12} c_{23}$, only $\mathcal{D}$ and the edge weights $c_{12}, c_{23}, c_{13}$ represent $\boldsymbol{X}$ in the sense of (2.1). Thus in this case the DAG and the edge weights are identifiable from the distribution $\mathcal{L}(\boldsymbol{X})$.

As conclusion of Example 3.1, it is generally not possible to identify the true DAG $\mathcal{D}$ and the edge weights $c_{k i}$ underlying $\boldsymbol{X}$ in representation (2.1) from $\mathcal{L}(\boldsymbol{X})$, since several DAGs and edge weights may exist such that $\boldsymbol{X}$ has this representation. The smallest DAG of this kind is the DAG that has an edge $k \rightarrow i$ if and only if $k \rightarrow i$ is the only max-weighted path from $k$ to $i$. We call this DAG $\mathcal{D}^{B}$ the minimum ML DAG of $\boldsymbol{X}$ and note that this is uniquely determined from the ML coefficient matrix $B$. All other DAGs representing $\boldsymbol{X}$ are those that include the edges of $\mathcal{D}^{B}$ and whose nodes have the same ancestors. The edge weights $c_{k i}$ in the representation (2.1) of $\boldsymbol{X}$ are only uniquely determined for edges contained in $\mathcal{D}^{B}$; namely, by $b_{k i}$; otherwise, $c_{k i}$ may be any number in $\left(0, b_{k i}\right]$. All this information can be found in Section 5 of [12] with its main results in Theorems 5.3, 5.4.

Based on the above observations, we investigate the identifiability of the whole class of DAGs and edge weights representing the max-linear structural equations (2.1) of $\boldsymbol{X}$ from $\mathcal{L}(\boldsymbol{X})$. Since this class can be recovered from $B$, it suffices to clarify whether $B$ is identifiable from $\mathcal{L}(\boldsymbol{X})$. There are many ways to prove that this is indeed the case. The way we present in this section suggests a simple procedure to estimate $B$ from independent realizations of $\boldsymbol{X}$ (see Algorithm 5.1 below). An alternative way can be found in Appendix 4.A. 1 of [11].

The ratios $\boldsymbol{Y}=\left\{Y_{i j}=X_{j} / X_{i}, i, j=1 \ldots, d\right\}$ between all pairs of components of $\mathbf{X}$ are the essential quantities used to identify $B$ from $\mathcal{L}(\boldsymbol{X})$. We first present distributional properties of these ratios, where we let $(\Omega, \mathcal{F}, \mathbb{P})$ denote the probability space of $\boldsymbol{Z}$ and, hence, of $\boldsymbol{X}$. In what follows, we use the standard convention and write events such as $\left\{\omega \in \Omega: X_{i}(\omega)<X_{j}(\omega)\right\}$ as

$\left\{X_{i}<X_{j}\right\}$, etc. Unsurprisingly, because of the max-linear representation (2.3) of the components of $\boldsymbol{X}$, the ratios inherit their distributional properties from the innovations. It plays an important role that

$$
\text { the event }\left\{Z_{i}=x Z_{j}\right\} \text { for distinct } i, j \in V \text { and } x \in \mathbb{R}_{+} \text {has probability zero, } \quad \text { (3.1) }\{\text { ch4:noiseNull }\}
$$

which follows from the independence of the innovations and the fact that their distributions are atom-free.

Lemma 3.2. Let $i, j \in V$ be distinct.
(a) The ratio $Y_{j i}=X_{i} / X_{j}$ has an atom in $x \in \mathbb{R}_{+}$if and only if $\operatorname{An}(i) \cap \operatorname{An}(j) \neq \varnothing$ and $x=b_{\ell i} / b_{\ell j}$ for some $\ell \in \operatorname{An}(i) \cap \operatorname{An}(j)$.
(b) We have

$$
\operatorname{supp}\left(Y_{j i}\right)= \begin{cases}\left[b_{j i}, \infty\right) & \text { if } j \in \operatorname{an}(i) \\ \left(0,1 / b_{i j}\right] & \text { if } j \in \operatorname{de}(i) \\ \mathbb{R}_{+} & \text {otherwise }\end{cases}
$$

where $\operatorname{supp}\left(Y_{j i}\right)$ denotes the support of $Y_{j i}$.
Proof. To establish (a) note that (2.3) and (3.1) imply that the sets $\left\{X_{i}=x X_{j}\right\}=\left\{\bigvee_{\ell \in \operatorname{An}(i)} b_{\ell i} Z_{\ell}=\right.$ $\bigvee_{\ell \in \operatorname{An}(j)} x b_{\ell j} Z_{\ell}\}$ and

$$
\left\{\bigvee_{\substack{\ell \in \operatorname{An}(i) \cap \operatorname{An}(j): \\ b_{\ell i}=b_{\ell j} x}} b_{\ell i} Z_{\ell}>\bigvee_{\substack{\ell \in \operatorname{An}(i) \cap \operatorname{An}(j): \\ b_{\ell i} \neq b_{\ell j} x}}\left(b_{\ell i} \vee x b_{\ell j}\right) Z_{\ell} \vee \bigvee_{\ell \in \operatorname{An}(i) \backslash \operatorname{An}(j)} b_{\ell i} Z_{\ell} \vee \bigvee_{\ell \in \operatorname{An}(j) \backslash \operatorname{An}(i)} x b_{\ell j} Z_{\ell}\right\}
$$

differ only by a set of probability zero. Since the innovations are independent and have support $\mathbb{R}_{+}$the conclusion follows.

To establish (b) note that the support $\mathbb{R}_{+}$of the innovations and the representation (2.3) yield

$$
\operatorname{supp}\left(Y_{j i}\right)=\left\{\frac{\bigvee_{\ell \in \operatorname{An}(i)} b_{\ell i} z_{\ell}}{\bigvee_{\ell \in \operatorname{An}(j)} b_{\ell j} z_{\ell}}: \boldsymbol{z}_{\operatorname{An}(i) \cup \operatorname{An}(j)} \in \mathbb{R}_{+}^{|\operatorname{An}(i) \cup \operatorname{An}(j)|}\right\}
$$

The continuity of the function

$$
\mathbb{R}_{+}^{|\operatorname{An}(i) \cup \operatorname{An}(j)|} \rightarrow \mathbb{R}_{+}, \quad \boldsymbol{z}_{\operatorname{An}(i) \cup \operatorname{An}(j)} \mapsto \frac{\bigvee_{\ell \in \operatorname{An}(i)} b_{\ell i} z_{\ell}}{\bigvee_{\ell \in \operatorname{An}(j)} b_{\ell j} z_{\ell}}
$$

implies that $\operatorname{supp}\left(Y_{j i}\right)$ is an interval in $\mathbb{R}_{+}$. Since for $j \in \operatorname{an}(i)$ by Corollary 3.13 of [12] $b_{j i} \leqslant Y_{j i}$ and by (a) $b_{j i}$ is an atom of $Y_{j i}$, it suffices to show that $j \in \operatorname{an}(i)$ if $\operatorname{supp}\left(Y_{j i}\right)$ has a positive lower bound. For this assume that $j \notin \operatorname{an}(i)$. Because of the positive lower bound of $\operatorname{supp}\left(Y_{j i}\right)$, there exists some $a \in \mathbb{R}_{+}$such that

$$
\bigvee_{\ell \in \operatorname{An}(i) \cap \operatorname{An}(j)} a b_{\ell j} z_{\ell} \vee \bigvee_{\ell \in \operatorname{An}(j) \backslash \operatorname{An}(i)} a b_{\ell j} z_{\ell} \leqslant \bigvee_{\ell \in \operatorname{An}(i)} b_{\ell i} z_{\ell}
$$

for all $\boldsymbol{z}_{\operatorname{An}(i) \cup \operatorname{An}(j)} \in \mathbb{R}_{+}^{|\operatorname{An}(i) \cup \operatorname{An}(j)|}$. As $\operatorname{An}(j) \backslash \operatorname{An}(i) \neq \varnothing$, for fixed $\mathbf{z}_{\operatorname{An}(i)} \in \mathbb{R}_{+}^{|\operatorname{An}(i)|}$, we can choose $z_{\ell}$ for some $\ell \in \operatorname{An}(j) \backslash \operatorname{An}(i)$ so large that $a b_{\ell j} z_{\ell}$ is greater than the maximum on the right-hand side of (3.2). This contradicts (3.2). Hence, $j \in \operatorname{an}(i)$.

Table 3.1: Distributional properties of $Y_{j i}$ for distinct $i, j \in V_{J}^{\text {ch4:table:rel }}$


In Table 3.1 we summarize the results of Lemma 3.2: depending on the relationship between $i$ and $j$ in $\mathcal{D}$, the support and atoms of $Y_{j i}$ are shown.

Table 3.1 and the fact that $b_{j i}=0$ for $j \notin \operatorname{An}(i)$ (cf. (2.2)) suggest the following algorithm to find $B$ from $\mathcal{L}(\boldsymbol{X})$ since we can identify the support of $Y_{j i}$ from $\mathcal{L}(\boldsymbol{X})$. This proves the identifiability of $B$ from $\mathcal{L}(\boldsymbol{X})$. In fact, it is sufficient to know $\operatorname{supp}\left(Y_{j i}\right)$ for all $i, j \in V$ with $i \neq j$ rather than the whole distribution $\mathcal{L}(\boldsymbol{X})$.

Algorithm 3.3. $[$ Find $B$ from $\mathcal{L}(\boldsymbol{X})]$
\{ch4:alg1\}

1. For all $i \in V=\{1, \ldots, d\}$, set $b_{i i}=1$.
2. For all $i, j \in V$ with $i \neq j$, find $\operatorname{supp}\left(Y_{j i}\right)$ :
if $\operatorname{supp}\left(Y_{j i}\right)=[a, \infty)$ for some $a \in \mathbb{R}_{+}$, then set $b_{j i}=a$;
else, set $b_{j i}=0$.
So far we have shown that the ML coefficient matrix $B$ of $\boldsymbol{X}$ can be obtained from $\mathcal{L}(\boldsymbol{X})$. Since all DAGs and edge weights that represent $\boldsymbol{X}$ in the sense of (2.1) can be determined from $B$, the only quantities we do not know about yet but appear in the definition of $\boldsymbol{X}$ are the innovations. In what follows we show that the distribution of the innovation vector $\boldsymbol{Z}$ is also identifiable from $\mathcal{L}(\boldsymbol{X})$. For this, due to the identifiability of $B$ from $\mathcal{L}(\boldsymbol{X})$ and the independence of the innovations, it suffices to provide an algorithm that determines the distributions of the innovations from $\mathcal{L}(\boldsymbol{X})$ and $B$. Note that $B$ also determines the ancestral relationships between any pair of nodes in that $j \in \operatorname{An}(i)$ for any DAG representing $\boldsymbol{X}$ if and only if $b_{j i}>0$.

We denote by $F_{Z_{i}}$ the distribution function of the innovation $Z_{i}$. Even with this algorithm, we do not have to know the whole distribution $\mathcal{L}(\boldsymbol{X})$; it is enough to know the ML coefficient matrix $B$ and the univariate marginal distribution functions of $\mathcal{L}(\boldsymbol{X})$.

Algorithm 3.4. $\left[\right.$ Find $F_{Z_{1}}(x), \ldots, F_{Z_{d}}(x)$ for $x \in \mathbb{R}_{+}$from $B$ and $\left.\mathcal{L}(\boldsymbol{X})\right]$
For $\nu=0, \ldots, d-1$,
for $i \in V$ such that $|\operatorname{an}(i)|=\left|\left\{j \in V \backslash\left\{i\right\}\right.\right.$ : $\left.b_{j i} \neq 0\right\} \mid=\nu$, set

$$
F_{Z_{i}}(x)=\frac{\mathbb{P}\left(X_{i} \leqslant x\right)}{\prod_{j \in \operatorname{an}(i)} F_{Z_{j}}\left(x / b_{j i}\right)}
$$

Here we have used the convention that $\prod_{j \in \varnothing} a_{j}=1$. The correctness of Algorithm 3.4 follows from the independence of the innovations and representation (2.3). Finally, we summarize the main result of this section.

Theorem 3.5. Let $\mathcal{L}(\boldsymbol{X})$ be the distribution of $\boldsymbol{X}$ following a recursive ML model. Then its ML coefficient matrix $B$ and the distribution of its innovation vector $\boldsymbol{Z}$ are identifiable from $\mathcal{L}(\boldsymbol{X})$. Furthermore, the class of all DAGs and edge weights that could have generated $\boldsymbol{X}$ by (2.1) can be obtained.

# 4 Estimation with known directed acyclic graph 

In this section we consider independent realizations $\boldsymbol{x}^{(t)}=\left(x_{1}^{(t)}, \ldots, x_{d}^{(t)}\right), t=1, \ldots, n$, of a random vector $\boldsymbol{X}=\left(X_{1}, \ldots, X_{d}\right)$ following a recursive ML model with its DAG $\mathcal{D}$ given. Further, we consider the distribution of the innovation vector to be fixed, but the only information we eventually use is that it has independent, atom-free margins with support $\mathbb{R}_{+}$, hence our estimation results also cover the situation where this distribution is unknown. Our aim is the estimation of the edge weights $c_{k i}$ and the ML coefficient matrix $B$. Since $\boldsymbol{X}$ may satisfy (2.1) with respect to $\mathcal{D}$ for different systems of edge weights $c_{k i}$ (see Example 3.1) and thus these are generally not identifiable from $\mathcal{L}(\boldsymbol{X})$, we usually have no chance to estimate the true edge weights from $\boldsymbol{x}^{(1)}, \ldots, \boldsymbol{x}^{(n)}$ consistently, but only the ML coefficient matrix $B$. Using the fact that the class of possible edge weights can be determined from $B$, we obtain automatically an estimate of this class; see Corollary 4.12 below.

## The ML coefficient matrix $\boldsymbol{B}$

In the following we let $\mathcal{B}(\mathcal{D})$ denote the class of possible ML coefficient matrices of all recursive ML models on $\mathcal{D}$. For $B$ being a matrix with non-negative entries and diagonal elements $b_{i i}=1$ we define $B_{0}:=\left(b_{i j} \mathbb{1}_{\mathrm{pa}(j)}(i)\right)_{d \times d}$. Then it holds that $B \in \mathcal{B}(\mathcal{D})$ if and only if $B$ satisfies the following

$$
\left[b_{j i}>0 \Longleftrightarrow j \in \operatorname{An}(i)\right] \text { and } B=I_{d} \vee\left(B \odot B_{0}\right)
$$

see Theorem 4.2 or Corollary 4.3(a) of [12].

## A simple estimate of $B$

Next we discuss a sensible estimate of $B$. Table 3.1 shows that for $j \in \operatorname{an}(i)$ the minimal value that can be observed for the ratio $Y_{j i}=X_{i} / X_{j}$ is $b_{j i}$, which is an atom of $Y_{j i}$. This suggests the following estimate $\hat{B}$ of the ML coefficient matrix:

$$
\bar{b}_{i i}=1, \quad \bar{b}_{j i}=0 \text { for } j \in V \backslash \operatorname{An}(i), \text { and } \bar{b}_{j i}=\bigwedge_{t=1}^{n} y_{j i}^{(t)}=\bigwedge_{t=1}^{n} \frac{x_{i}^{(t)}}{x_{j}^{(t)}} \text { for } j \in \operatorname{an}(i)
$$

Davis and Resnick [6] suggested such minimal observed ratios as estimates for parameters in maxARMA processes. For $n$ sufficiently large, we can expect to observe the atoms $b_{j i}$ for $j \in \operatorname{an}(i)$ in the sample $\boldsymbol{x}^{(1)}, \ldots, \boldsymbol{x}^{(n)}$ and, hence, to estimate the ML coefficients exactly. However, if $n$ is not large we may with positive probability have that $\hat{B}$ is not an ML coefficient matrix of any recursive ML model on $\mathcal{D}$ as the following simple example shows:

Example 4.1. $[\hat{B}$ is not necessarily in $\mathcal{B}(\mathcal{D})]$
Consider the DAG

$\mathcal{D} \quad 1) \longrightarrow 2) \longrightarrow 3)$
and assume we observe $\breve{b}_{31}>\breve{b}_{32} \breve{b}_{21}$. Then the matrix $\breve{B}$ fails to satisfy (4.1) and hence is not an element of $\mathcal{B}(\mathcal{D})$.

However, if we only estimate the ML coefficients corresponding to edges in $\mathcal{D}$ and then compute an estimate based on Lemma 4.2 below this phenomenon cannot occur.

Lemma 4.2. Let $B_{0} \in \mathbb{R}_{+}^{d \times d}$ be a matrix with $b_{i j}>0 \Longleftrightarrow i \rightarrow j$. A matrix $A \in \mathbb{R}_{+}^{d \times d}$ satisfies

$$
\left[a_{j i}>0 \Longleftrightarrow j \in \operatorname{An}(i)\right] \text { and } A=I_{d} \vee\left(A \odot B_{0}\right)
$$

if and only if $A=\left(I_{d} \vee B_{0}\right)^{\odot(d-1)}$.
Proof. We first show that $A=\left(I_{d} \vee B_{0}\right)^{\odot(d-1)}$ is a solution. We have ([4], Proposition 1.6.10)

$$
\left(I_{d} \vee B_{0}\right)^{\odot(d-1)}=\bigvee_{k=0}^{d-1} B_{0}^{\odot k}=\bigvee_{k=0}^{\infty} B_{0}^{\odot k}
$$

and hence

$$
I_{d} \vee\left(A \odot B_{0}\right)=I_{d} \vee\left\{\left(I_{d} \vee B_{0}\right)^{\odot(d-1)} \odot B_{0}\right\}=I_{d} \vee\left\{\bigvee_{k=1}^{\infty} B_{0}^{\odot k}\right\}=\bigvee_{k=0}^{\infty} B_{0}^{\odot k}=A
$$

It is easy to see directly that $B_{0}^{\odot k}=0$ for $k \geqslant d$ and hence if $\breve{A}$ is a solution to (4.1) we get by iteration, using that $(M \vee N) \odot K=(M \odot K) \vee(N \odot K)$,

$$
\begin{aligned}
\check{A} & =I_{d} \vee\left(\check{A} \odot B_{0}\right) \\
& =I_{d} \vee\left[\left\{I_{d} \vee\left(\check{A} \odot B_{0}\right)\right\} \odot B_{0}\right] \\
& =I_{d} \vee B_{0} \vee\left(\check{A} \odot B_{0}^{\odot 2}\right) \\
& =\cdots \\
& =\left(I_{d} \vee B_{0}\right)^{\odot(d-1)} \vee\left(\check{A} \odot B_{0}^{\odot d}\right)=\left(I_{d} \vee B_{0}\right)^{\odot(d-1)}=A
\end{aligned}
$$

and hence the solution to the equation is unique.
For a path $p=\left[j=k_{0} \rightarrow k_{1} \rightarrow \cdots \rightarrow k_{n}=i\right]$ and a realization $\boldsymbol{x}^{(t)}$ such that $\breve{b}_{j i} x_{j}^{(t)}=x_{i}^{(t)}$ we have

$$
\left(\bigwedge_{s=1}^{n} y_{01}^{(s)}\right)\left(\bigwedge_{s=1}^{n} y_{12}^{(s)}\right) \ldots\left(\bigwedge_{s=1}^{n} y_{n-1, n}^{(s)}\right) \leqslant y_{01}^{(t)} y_{12}^{(t)} \ldots y_{n-1, n}^{(t)}=y_{j i}^{(t)}=\breve{b}_{j i}=\bigwedge_{s=1}^{n} y_{j i}^{(s)}
$$

Thus we may define the estimate $\widehat{B}$ by first calculating the matrix $\breve{B}_{0}=\left(\breve{b}_{i j} \mathbb{1}_{\mathrm{pa}(j)}(i)\right)_{d \times d}$ and then iterating the $\odot$-matrix product as:

$$
\widehat{B}=\left(I_{d} \vee \check{B}_{0}\right)^{\odot(d-1)}
$$

It then follows from (4.2) that $\widehat{B}_{0}=\check{B}_{0}$ and from Lemma 4.2 that $\widehat{B}$ is the unique element of $\mathcal{B}(\mathcal{D})$ with this property. By Lemma 3.2(b), we also have

$$
b_{j i} \leqslant \widehat{b}_{j i} \leqslant \breve{b}_{j i} \text { for } j \in \operatorname{an}(i)
$$

Consequently, when using $\widehat{B}$ or $\breve{B}$ as an estimate of $B$, we never underestimate a ML coefficient; furthermore, the matrix $\widehat{B}$ always estimates $B$ more precisely than $\breve{B}$ and since we always have $\widehat{B} \in \mathcal{B}(\mathcal{D}), \widehat{B}$ seems to be clearly preferable as an estimate of $B$.

The following two examples show how effective the estimate $\widehat{B}$ can be; in particular, $n$ does not necessarily need to be large.

Example 4.3. [One observation may be enough to estimate $B$ exactly] Consider the DAG
![img-1.jpeg](img-1.jpeg)
and assume that the paths $[1 \rightarrow 2 \rightarrow 4]$ and $[1 \rightarrow 3 \rightarrow 4]$ are both max-weighted, which is equivalent to $b_{12} b_{24}=b_{13} b_{34}$. If we observe the event

$$
\left\{X_{2}=b_{12} X_{1}\right\} \cap\left\{X_{3}=b_{13} X_{1}\right\} \cap\left\{X_{4}=b_{24} X_{2}\right\} \cap\left\{X_{4}=b_{34} X_{3}\right\}
$$

then $\widehat{B}=B$ so we estimate all ML coefficients exactly. Note that this event has positive probability and occurs $\mathbb{P}$-almost surely if and only if $Z_{1}$ realizes all node variables; i.e., if $X_{2}=b_{12} Z_{1}$, $X_{3}=b_{13} Z_{1}$, and $X_{4}=b_{14} Z_{1}$.

Example 4.4. Consider the DAG
![img-2.jpeg](img-2.jpeg)

We have four events that may occur, namely,

$$
\begin{array}{ll}
F_{1}=\left\{X_{3}=b_{13} X_{1}\right\} \cap\left\{X_{3}=b_{23} X_{2}\right\}, & F_{2}=\left\{X_{3}=b_{13} X_{1}\right\} \cap\left\{X_{3}>b_{23} X_{2}\right\} \\
F_{3}=\left\{X_{3}>b_{13} X_{1}\right\} \cap\left\{X_{3}=b_{23} X_{2}\right\}, & F_{4}=\left\{X_{3}>b_{13} X_{1}\right\} \cap\left\{X_{3}>b_{23} X_{2}\right\}
\end{array}
$$

When excluding the null event $F_{1}$, we estimate $B$ by $\widehat{B}$ exactly if and only if the observations $\boldsymbol{x}^{(1)}, \ldots, \boldsymbol{x}^{(n)}$ include both of the events $F_{2}$ and $F_{3}$; so two observations may be enough to estimate $B$ exactly.

Since by Table $3.1 \mathbb{P}\left(X_{i}=b_{k i} X_{k}\right)>0$ for $k \in \mathrm{pa}(i)$, it follows from the Borel-Cantelli lemma that $\widehat{b}_{k i} \mathbb{P}$-almost surely equals the true value for $n$ sufficiently large. Thus, if $n$ is large, $\widehat{B}$ finds, with probability 1 , the true $B$. In [6] this is discussed for the time-series framework used there and in Davis and McCormick [5] they show that under suitable assumptions, this estimator is asymptotically Fréchet distributed. Assuming the probability of $\left\{X_{i}=b_{k i} X_{k}\right\}$ is known, we show next how one has to choose $n$ to observe this event with probability greater than $1-p$ for some $p \in(0,1)$. We also prove that the probability for estimating the true $b_{k i}$ converges exponentially fast to 1 .

Proposition 4.5. Let $\boldsymbol{X}^{(t)}=\left(X_{1}^{(t)}, \ldots, X_{n}^{(t)}\right)$ for $t=1, \ldots, n$ be a sample from a recursive $M L$ model on a DAG $\mathcal{D}$ with ML coefficient matrix B. Let $i \in V$ and $k \in \mathrm{pa}(i)$. It then holds that

$$
\mathbb{P}\left(\bigwedge_{t=1}^{n} Y_{k i}^{(t)}=b_{k i}\right) \geqslant 1-p \text { for some } p \in(0,1)
$$

if and only if

$$
n \geqslant \frac{\ln (p)}{\ln \left(\mathbb{P}\left(Y_{k i}>b_{k i}\right)\right)}
$$

Furthermore, the convergence $\mathbb{P}\left(\bigwedge_{t=1}^{n} Y_{k i}^{(t)}=b_{k i}\right) \rightarrow 1$ as $n \rightarrow \infty$ is exponentially fast.
Proof. First note that the events $\left\{X_{i}=b_{k i} X_{k}\right\}$ and $\left\{X_{i}>b_{k i} X_{k}\right\}$ are complementary and both have positive probability. Further, using that $\boldsymbol{X}^{(1)}, \ldots, \boldsymbol{X}^{(n)}$ are independent and identically distributed yields

$$
\mathbb{P}\left(\bigwedge_{t=1}^{n} Y_{k i}^{(t)}=b_{k i}\right)=1-\mathbb{P}\left(\bigwedge_{t=1}^{n} Y_{k i}^{(t)}>b_{k i}\right)=1-\prod_{t=1}^{n} \mathbb{P}\left(Y_{k i}^{(t)}>b_{k i}\right)=1-\mathbb{P}\left(Y_{k i}>b_{k i}\right)^{n}
$$

Altogether, the statements follow.
In conclusion, $\widehat{B}$ has the nice property to be 'geometrically consistent' in the sense that the probability of $\{\widehat{B}=B\}$ converges exponentially fast to one.

# The matrix $\widehat{B}$ is a generalized maximum likelihood estimate 

For $B \in \mathcal{B}(\mathcal{D})$ and a fixed distribution of the innovation vector we let $P_{B}$ denote the probability measure induced by a recursive ML model on $\mathcal{D}$ with ML coefficient matrix $B$, i.e. the distribution of $\boldsymbol{X}$ where $\boldsymbol{X}=\boldsymbol{Z} \odot B$. We shall denote the family of these probability measures by $\mathcal{P}(\mathcal{D})$.

We cannot use standard maximum likelihood methods to estimate $B$, since the family $\mathcal{P}(\mathcal{D})$ is not dominated (cf. Example 4.4.1 of [11]) and hence the standard likelihood function is not well defined. However, there exist generalizations of maximum likelihood estimation (GMLE) that cover the undominated case as well; Kalbfleisch and Prentice [17], Kiefer and Wolfowitz [18], and Scholz [26] suggested such extensions. We essentially follow the Kiefer-Wolfowitz definition of a GMLE; as also done, for example, by Gill et al. [10] and Johansen [16] and in the following we shall show that $\widehat{B}$ can be seen as a maximum likelihood estimate of $B$ in the extended sense introduced by Kiefer and Wolfowitz in [18].

Let $\mathcal{P}$ be a family of probability measures on $\left(\mathbb{R}_{+}^{d}, \mathbb{B}\left(\mathbb{R}_{+}^{d}\right)\right)$ where $\mathbb{B}\left(\mathbb{R}_{+}^{d}\right)$ denotes the Borel $\sigma$-algebra on $\mathbb{R}_{+}^{d}$, and $\boldsymbol{x}^{(1)}, \ldots, \boldsymbol{x}^{(n)}$ a random sample from some $P_{0} \in \mathcal{P}$. For $P, Q \in \mathcal{P}$ and $\boldsymbol{x} \in \mathbb{R}_{+}^{d}$ we define

$$
\rho(\boldsymbol{x}, P, Q):=\frac{d P}{d(P+Q)}(\boldsymbol{x})
$$

where $d P / d(P+Q)$ denotes a density of $P$ with respect to $P+Q$. Then we call $\widehat{P}$ a generalized maximum likelihood estimate of $P_{0}$ if

$$
\prod_{t=1}^{n} \rho\left(\boldsymbol{x}^{(t)}, \widehat{P}, \widehat{P}\right) \neq 0 \quad \text { and } \quad \prod_{t=1}^{n} \rho\left(\boldsymbol{x}^{(t)}, Q, \widehat{P}\right) \leqslant \prod_{t=1}^{n} \rho\left(\boldsymbol{x}^{(t)}, \widehat{P}, Q\right) \text { for all } Q \in \mathcal{P}
$$

\{ch4:propBhat\}
\{ch4:propBhat\}

Since $P$ is absolutely continuous with respect to $P+Q$, the density $d P / d(P+Q)$ always exists according to the Radon-Nikodym theorem. This means that the GMLE is well-defined, save for the usual ambiguity in the method of maximum likelihood that densities are only defined up to null sets and therefore a specific choice of densities must be made. The Kiefer-Wolfowitz definition extends the definition of a MLE in a very natural way as it simply says that $\widehat{P}$ is the MLE in the smaller family $\{\hat{P}, Q\}$ for any $Q \in \mathcal{P}$. In [18] only the second condition in (4.4) is required, but the first condition is implicit. The first step in verfying that $\widehat{B}$ is a GMLE of $B$ is to specify densities of $P_{B}$ with respect to $P_{B}+P_{B^{*}}$ for any two $B, B^{*} \in \mathcal{B}(\mathcal{D})$. For this purpose we determine a partition $\left\{A_{0}\left(B, B^{*}\right), A_{1 / 2}\left(B, B^{*}\right), A_{1}\left(B, B^{*}\right)\right\}$ of $\mathbb{R}_{+}^{d}$ that satisfies the following three properties,
(A): $\quad P_{B}\left(A_{0}\left(B, B^{*}\right)\right)=0$,
(B): $\quad P_{B}\left(A \cap A_{1 / 2}\left(B, B^{*}\right)\right)=P_{B^{*}}\left(A \cap A_{1 / 2}\left(B, B^{*}\right)\right)$ for every $A \in \mathbb{B}\left(\mathbb{R}_{+}^{d}\right)$,
(C): $\quad P_{B^{*}}\left(A_{1}\left(B, B^{*}\right)\right)=0$.
Then we choose as density the measurable function from $\mathbb{R}_{+}^{d}$ to $\{0,1 / 2,1\}$ defined as

$$
\boldsymbol{x} \mapsto \rho\left(\boldsymbol{x}, B, B^{*}\right):=\frac{1}{2} \cdot \mathbb{1}_{A_{1 / 2}\left(B, B^{*}\right)}(\boldsymbol{x})+\mathbb{1}_{A_{1}\left(B, B^{*}\right)}(\boldsymbol{x})= \begin{cases}0, & \text { if } \boldsymbol{x} \in A_{0}\left(B, B^{*}\right) \\ \frac{1}{2}, & \text { if } \boldsymbol{x} \in A_{1 / 2}\left(B, B^{*}\right) \\ 1, & \text { if } \boldsymbol{x} \in A_{1}\left(B, B^{*}\right)\end{cases}
$$

This is a valid density because, using the properties (A), (B), (C), we obtain for every $A \in \mathbb{B}\left(\mathbb{R}_{+}^{d}\right)$,

$$
\int_{A} \rho\left(\boldsymbol{x}, B, B^{*}\right)\left(P_{B}+P_{B^{*}}\right)(d \boldsymbol{x})=P_{B}\left(A \cap A_{1 / 2}\left(B, B^{*}\right)\right)+P_{B}\left(A \cap A_{1}\left(B, B^{*}\right)\right)=P_{B}(A)
$$

We begin with an example that shall help to get an idea and provide insights into the concepts and arguments we shall use in the general case. It is deliberately very detailed.

Example 4.6. [How to find a density and the associated GMLEs]
For $B, B^{*} \in \mathcal{B}(\mathcal{D})$ where $\mathcal{D}=(\{1,2\}, 1 \rightarrow 2)$, we show that the partition

$$
\begin{aligned}
& \left\{A_{0}\left(B, B^{*}\right):=\left\{\boldsymbol{x} \in \mathbb{R}_{+}^{2}: x_{2}<b_{12} x_{1}\right\} \cup\left\{\boldsymbol{x} \in \mathbb{R}_{+}^{2}: x_{2}=b_{12}^{*} x_{1}>b_{12} x_{1}\right\}\right. \\
& A_{1 / 2}\left(B, B^{*}\right):=\left\{\boldsymbol{x} \in \mathbb{R}_{+}^{2}: x_{2}=b_{12} x_{1}=b_{12}^{*} x_{1}\right\} \cup\left\{\boldsymbol{x} \in \mathbb{R}_{+}^{2}: x_{2}>\left(b_{12} \vee b_{12}^{*}\right) x_{1}\right\} \\
& \left.A_{1}\left(B, B^{*}\right):=\left\{\boldsymbol{x} \in \mathbb{R}_{+}^{2}: b_{12}^{*} x_{1}>x_{2} \geqslant b_{12} x_{1}\right\} \cup\left\{\boldsymbol{x} \in \mathbb{R}_{+}^{2}: x_{2}=b_{12} x_{1}>b_{12}^{*} x_{1}\right\}\right\}
\end{aligned}
$$

of $\mathbb{R}_{+}^{2}$ satisfies properties (A), (B), (C) of (4.5). Figure 4.1 shows the corresponding density $\rho\left(\cdot, B, B^{*}\right)$ from (4.6) for the three possible order relations between $b_{12}$ and $b_{12}^{*}$.

Since by Table 3.1, $\operatorname{supp}\left(X_{2} / X_{1}\right)=\left[b_{12}, \infty\right)$ and $b_{12}$ is the only atom of $X_{2} / X_{1}$, property (A) is true. By reversing the roles of $B$ and $B^{*}$, (C) follows from (A). The condition (B) is obvious if $b_{12}=b_{12}^{*}$. Assume that $b_{12} \neq b_{12}^{*}$. We then have by definition of $\boldsymbol{X}$ that $\left\{\boldsymbol{X} \in A_{1 / 2}\left(B, B^{*}\right)\right\}=$ $\left\{X_{2}>\left(b_{12} \vee b_{12}^{*}\right) X_{1}\right\}=\left\{Z_{2}>\left(b_{12} \vee b_{12}^{*}\right) Z_{1}\right\}$ and $X_{2}=Z_{2}$ on $\left\{Z_{2}>\left(b_{12} \vee b_{12}^{*}\right) Z_{1}\right\}$. With this, using that $A_{1 / 2}\left(B^{*}, B\right)=A_{1 / 2}\left(B, B^{*}\right)$. We finally obtain for $A \in \mathbb{B}\left(\mathbb{R}_{+}^{2}\right)$,

$$
\begin{aligned}
P_{B}\left(A \cap A_{1 / 2}\left(B, B^{*}\right)\right) & =\mathbb{P}\left(\left\{\boldsymbol{X} \in A\right\} \cap\left\{Z_{2}>\left(b_{12} \vee b_{12}^{*}\right) Z_{1}\right\}\right) \\
& =\mathbb{P}\left(\left\{\left(Z_{1}, Z_{2}\right) \in A\right\} \cap\left\{Z_{2}>\left(b_{12} \vee b_{12}^{*}\right) Z_{1}\right\}\right) \\
& =P_{B^{*}}\left(A \cap A_{1 / 2}\left(B^{*}, B\right)\right)=P_{B^{*}}\left(A \cap A_{1 / 2}\left(B, B^{*}\right)\right)
\end{aligned}
$$

![img-3.jpeg](img-3.jpeg)

Figure 4.1: The density $\rho\left(\cdot, B, B^{*}\right)$ from Example 4.6 shown as a contour plot (top line) and as a function of $y_{12}=x_{2} / x_{1}$ (bottom line) for the three situations $b_{12}<b_{12}^{*}$ (left-hand side), $b_{12}=b_{12}^{*}$ (middle), and $b_{12}>b_{12}^{*}$ (right-hand side). The area where it is $0 / \frac{1}{2} / 1$ is coloured in red/blue/green.

We now use the density found to determine the GMLE of $B$. The only ML coefficient we have to estimate is $b_{12}$. As before we let $\widetilde{b}_{12}=\bar{b}_{12}$ be the minimal observed ratio of $X_{2} / X_{1}$ and let $\widetilde{B}$ be the corresponding ML coefficient matrix from (4.3). Defining $n\left(B, B^{*}\right)=\mid\left\{t: \boldsymbol{x}^{(t)} \in\right.$ $\left.A_{1 / 2}\left(B, B^{*}\right)\right\} \mid$ and using that $n\left(B, B^{*}\right)=n\left(B^{*}, B\right)$, we obtain

$$
\begin{aligned}
& \prod_{t=1}^{n} \rho\left(\boldsymbol{x}^{(t)}, B, B^{*}\right)=2^{-n\left(B, B^{*}\right)} \prod_{t=1}^{n} \mathbb{1}_{\mathbb{R}_{+}^{d} \backslash A_{0}\left(B, B^{*}\right)}\left(\boldsymbol{x}^{(t)}\right) \\
& \prod_{t=1}^{n} \rho\left(\boldsymbol{x}^{(t)}, B^{*}, B\right)=2^{-n\left(B, B^{*}\right)} \prod_{t=1}^{n} \mathbb{1}_{\mathbb{R}_{+}^{d} \backslash A_{0}\left(B^{*}, B\right)}\left(\boldsymbol{x}^{(t)}\right)
\end{aligned}
$$

Let now $\widetilde{B}$ be an arbitrary potential GMLE of $B$. Then $P_{\widetilde{B}} \in \mathcal{P}(\mathcal{D})$ satisfies the first condition in (4.4) if and only if

$$
\widetilde{b}_{12} x_{1}^{(t)} \leqslant x_{2}^{(t)} \text { for all } t \text {, equivalently } \widetilde{b}_{12} \leqslant \widetilde{b}_{12}
$$

$\left\{\right.$ ch4:cond1:DAG1
and the second if and only if

$$
\text { for all } B \in \mathcal{B}(\mathcal{D}) \text {, if some } \boldsymbol{x}^{(t)} \in A_{0}(\widetilde{B}, B) \text {, then some } \boldsymbol{x}^{(s)} \in A_{0}(B, \widetilde{B})
$$

In summary, some $\widetilde{B} \in \mathcal{B}(\mathcal{D})$ is a GMLE of $B$ if and only if (4.7) and (4.8) are satisfied. We discuss the possible GMLEs of $b_{12}$ in detail.
(a) $\widetilde{b}_{12}<\widehat{b}_{12}$ is no GMLE:

Set $b_{12}=\widetilde{b}_{12}$, and let $\boldsymbol{x}^{(t)}$ be such that $\widehat{b}_{12} x_{1}^{(t)}=x_{2}^{(t)}$. Then $\boldsymbol{x}^{(t)} \in\left\{\boldsymbol{x} \in \mathbb{R}_{+}^{2}: x_{2}=b_{12} x_{1}>\right.$ $\left.\widetilde{b}_{12} x_{2}\right\} \subseteq A_{0}(\widetilde{B}, B)$ but no $\boldsymbol{x}^{(s)} \in A_{0}(B, \widetilde{B})=\left\{\boldsymbol{x} \in \mathbb{R}_{+}^{2}: x_{2}<b_{12} x_{1}\right\}$. This contradicts (4.8); consequently, $\widetilde{b}_{12}$ cannot be a GMLE of $b_{12}$. In Figure 4.2(a) we illustrate this situation. On the left-hand side a contour plot of the density $\rho(\cdot, \widetilde{B}, B)$ is shown, on the right-hand side of $\rho(\cdot, B, \widetilde{B})$. The crosses represent the realizations $\boldsymbol{x}^{(1)}, \ldots, \boldsymbol{x}^{(n)}$. In the left plot crosses are in the 0 -area coloured in red, namely, those that realize $\widetilde{b}_{12}$, but in the right plot not. So $\widetilde{B}$ cannot be a GMLE of $B$.
(b) $\widetilde{b}_{12}>\widehat{b}_{12}$ is no GMLE:

This follows directly from (4.7). Figure 4.2(b) shows a situation that contradicts (4.8), similarly to Figure 4.2(a) in (1).

![img-4.jpeg](img-4.jpeg)

Figure 4.2: Discussion of the GMLEs of $b_{12}$ with respect to the density from Figure 4.1. $\frac{\text { ch4:fig2:DAG12 }}{\text { see further }}$ explanation in (a), (b), and (c) of Example 4.6.
(c) $\widetilde{b}_{12}=\widehat{b}_{12}$ is a GMLE:

Condition (4.7) holds obviously. To prove (4.8), assume for some $B \in \mathcal{B}(\mathcal{D})$ that some $\boldsymbol{x}^{(t)} \in A_{0}(\widehat{B}, B)$. By definition of $A_{0}(\widehat{B}, B), x_{2}^{(t)}=b_{12} x_{1}^{(t)}>\widehat{b}_{12} x_{1}^{(t)}$, which implies that $b_{12}>\widehat{b}_{12}$. For $\boldsymbol{x}^{(s)}$ such that $\widehat{b}_{12} x_{1}^{(s)}=x_{2}^{(s)}$, we then find that $x_{2}^{(s)}<b_{12} x_{1}^{(s)}$. Hence, $\boldsymbol{x}^{(s)} \in A_{0}(B, \widehat{B})$, and $\widehat{b}_{12}$ is a GMLE of $b_{12}$. We learn this informally from Figure 4.2(c). The top line shows contour plots of $\rho(\cdot, \widehat{B}, B)$ for the three different orders between $b_{12}$ and $\widehat{b}_{12}$, and the bottom line shows the corresponding contour plots of $\rho(\cdot, B, \widehat{B})$. The two plots on the left-hand side correspond to the situation from above: in the upper plot there are realizations in the 0 -area, namely those that are on the line $\left\{\boldsymbol{x} \in \mathbb{R}_{+}^{2}: x_{2}=b_{12} x_{1}\right\}$, but then there are also realizations in the 0 -area of the lower plot (those that lie below this line). Hence, (4.8) holds. Since there is no realization in the 0 -area of the middle and right plot in the top line, (4.8) is automatically satisfied if $b_{12} \leqslant \widehat{b}_{12}$.

In what follows we specify, for the general case, one density of $P_{B}$ with respect to $P_{B}+P_{B^{*}}$ that has a representation as in (4.6) and leads to $\widehat{B}$ as a GMLE of $B$.

Our partition $\left\{A_{0}\left(B, B^{*}\right), A_{1 / 2}\left(B, B^{*}\right), A_{1}\left(B, B^{*}\right)\right\}$ of $\mathbb{R}_{+}^{d}$ is based on the following representation for the components of $\boldsymbol{X}$ :

$$
X_{i}=\bigvee_{k \in \mathrm{pa}(i)} b_{k i} X_{k} \vee Z_{i} ; \quad \text { in particular, } X_{i} \geqslant \bigvee_{k \in \mathrm{pa}(i)} b_{k i} X_{k}, \quad i \in V
$$

We begin with the specification of $A_{1 / 2}\left(B, B^{*}\right)$ and prove a property needed subsequently to verify property (B). Have in mind that if $b_{k i}>b_{k i}^{*}$ for all $k \in \mathrm{pa}(i)$ or $b_{k i}<b_{k i}^{*}$ for all $k \in \mathrm{pa}(i)$ then $\left\{\boldsymbol{x} \in \mathbb{R}_{+}^{d}: x_{i}=\bigvee_{k \in \mathrm{pa}(i)} b_{k i}^{*} x_{k}=\bigvee_{k \in \mathrm{pa}(i)} b_{k i} x_{k}\right\}=\varnothing$.

Lemma 4.7. Let $B, B^{*} \in \mathcal{B}(\mathcal{D})$ and define

$$
\begin{aligned}
\Omega\left(B, B^{*}\right): & =\bigcap_{i=1}^{d}\left\{\bigvee_{j \in \operatorname{An}(i): b_{j i}=b_{j i}^{*}} b_{j i} Z_{j}>\bigvee_{j \in \operatorname{an}(i): b_{j i} \neq b_{j i}^{*}}\left(b_{j i} \vee b_{j i}^{*}\right) Z_{j}\right\} \\
A_{1 / 2}\left(B, B^{*}\right): & =\bigcap_{i=1}^{d}\left[\left\{\boldsymbol{x} \in \mathbb{R}_{+}^{d}: x_{i}=\bigvee_{k \in \mathrm{pa}(i)} b_{k i} x_{k}=\bigvee_{k \in \mathrm{pa}(i)} b_{k i}^{*} x_{k}\right\} \cup\left\{\boldsymbol{x} \in \mathbb{R}_{+}^{d}: x_{i}>\bigvee_{k \in \mathrm{pa}(i)}\left(b_{k i} \vee b_{k i}^{*}\right) x_{k}\right\}\right]
\end{aligned}
$$

Then for every $F \in \mathcal{F}$,

$$
\mathbb{P}\left(F \cap\left\{\boldsymbol{X} \in A_{1 / 2}\left(B, B^{*}\right)\right\}\right)=\mathbb{P}\left(F \cap \Omega\left(B, B^{*}\right)\right)
$$

Proof. First, define for $i \in V$

$$
\begin{aligned}
\Omega_{1 / 2}^{1, i} & :=\left\{X_{i}=\bigvee_{k \in \mathrm{pa}(i)} b_{k i} X_{k}=\bigvee_{k \in \mathrm{pa}(i)} b_{k i}^{*} X_{k}\right\}, \quad \Omega_{1 / 2}^{2, i}:=\left\{X_{i}>\bigvee_{k \in \mathrm{pa}(i)}\left(b_{k i} \vee b_{k i}^{*}\right) X_{k}\right\} \\
\Omega_{i} & :=\left\{\bigvee_{j \in \operatorname{An}(i): b_{j i}=b_{j i}^{*}} b_{j i} Z_{j}>\bigvee_{j \in \operatorname{an}(i): b_{j i} \neq b_{j i}^{*}}\left(b_{j i} \vee b_{j i}^{*}\right) Z_{j}\right\}
\end{aligned}
$$

The proof is by induction on the number of nodes of $\mathcal{D}$. For $d=1$ the statement is clear. Assume now that $\mathcal{D}=(V, E)$ has $d+1$ nodes and that the assertion holds with respect to DAGs with at most $d$ nodes. Furthermore, assume without loss of generality that $d+1$ is a terminal node (i.e., $\operatorname{de}(d+1)=\varnothing$ ). Since $\left(X_{1}, \ldots, X_{d}\right)$ follows a recursive ML model on the $\operatorname{DAG}(\{1, \ldots, d\}, E \cap(\{1, \ldots, d\} \times\{1, \ldots, d\}))$ with ML coefficient matrix $B=\left(b_{i j}\right)_{d \times d}$ and $B^{*}=\left(b_{i j}^{*}\right)_{d \times d}$ is the ML coefficient matrix of a recursive ML model on this DAG as well, the induction hypothesis yields that

$$
\mathbb{P}\left(F \cap\left\{\boldsymbol{X} \in A_{1 / 2}\left(B, B^{*}\right)\right\}\right)=\mathbb{P}\left(F \cap \bigcap_{i=1}^{d+1}\left(\Omega_{1 / 2}^{1, i} \cup \Omega_{1 / 2}^{2, i}\right)\right)=\mathbb{P}\left(F \cap \bigcap_{i=1}^{d} \Omega_{i} \cap\left(\Omega_{1 / 2}^{1, d+1} \cup \Omega_{1 / 2}^{2, d+1}\right)\right)
$$

For every $i \in V$ we have by (2.3) on $\Omega_{i}$ that

$$
X_{i}=\bigvee_{j \in \operatorname{An}(i)} b_{j i} Z_{j}=\bigvee_{j \in \operatorname{An}(i)} b_{j i}^{*} Z_{j}
$$

Noting from the proof of Theorem 4.2 of [12] that

$$
\bigvee_{k \in \mathrm{pa}(d+1)} b_{k, d+1} X_{k}=\bigvee_{k \in \mathrm{pa}(d+1)} b_{k, d+1} \bigvee_{j \in \operatorname{An}(k)} b_{j k} Z_{j}=\bigvee_{j \in \operatorname{an}(d+1)} b_{j, d+1} Z_{j}
$$

we obtain from (4.12) on $\bigcap_{i=1}^{d} \Omega_{i}$,

$$
\bigvee_{k \in \mathrm{pa}(d+1)} b_{k, d+1}^{*} X_{k}=\bigvee_{k \in \mathrm{pa}(d+1)} b_{k, d+1}^{*} \bigvee_{j \in \operatorname{An}(k)} b_{j k}^{*} Z_{j}=\bigvee_{j \in \operatorname{an}(i)} b_{j, d+1}^{*} Z_{j}
$$

Thus, again by (2.3),

$$
\begin{aligned}
& \bigcap_{i=1}^{d} \Omega_{i} \cap \Omega_{1 / 2}^{1, d+1}=\bigcap_{i=1}^{d} \Omega_{i} \cap\left\{\bigvee_{j \in \operatorname{An}(d+1)} b_{j, d+1} Z_{j}=\bigvee_{j \in \operatorname{an}(d+1)} b_{j, d+1} Z_{j}=\bigvee_{j \in \operatorname{an}(d+1)} b_{j, d+1}^{*} Z_{j}\right\}, \\
& \bigcap_{i=1}^{d} \Omega_{i} \cap \Omega_{1 / 2}^{2, d+1}=\bigcap_{i=1}^{d} \Omega_{i} \cap\left\{\bigvee_{j \in \operatorname{An}(d+1)} b_{j, d+1} Z_{j}>\bigvee_{j \in \operatorname{an}(d+1)}\left(b_{j, d+1} \vee b_{j, d+1}^{*}\right) Z_{j}\right\} \\
& =\bigcap_{i=1}^{d} \Omega_{i} \cap\left\{b_{j, d+1} Z_{j}>\bigvee_{j \in \operatorname{an}(d+1)}\left(b_{j, d+1} \vee b_{j, d+1}^{*}\right) Z_{j}\right\} .
\end{aligned}
$$

From (3.1) we then finally observe that $\bigcap_{i=1}^{d} \Omega_{i} \cap\left(\Omega_{1 / 2}^{1, d+1} \cup \Omega_{1 / 2}^{2, d+1}\right)$ and $\bigcap_{i=1}^{d} \Omega_{i} \cap \Omega_{d+1}$ only differ by a set of probability zero, and, hence, (4.10) follows from (4.11).

As partition $\left\{A_{0}\left(B, B^{*}\right), A_{1 / 2}\left(B, B^{*}\right), A_{1}\left(B, B^{*}\right)\right\}$ of $\mathbb{R}_{+}^{d}$ we suggest

$$
\begin{aligned}
& \left\{A_{0}\left(B, B^{*}\right)=\bigcup_{i \in V}\left[\left\{\boldsymbol{x} \in \mathbb{R}_{+}^{d}: x_{i}<\bigvee_{k \in \mathrm{pa}(i)} b_{k i} x_{k}\right\} \cup\left\{\boldsymbol{x} \in \mathbb{R}_{+}^{d}: x_{i}=\bigvee_{k \in \mathrm{pa}(i)} b_{k i}^{*} x_{k}>\bigvee_{k \in \mathrm{pa}(i)} b_{k i} x_{k}\right\}\right], \\
& A_{1 / 2}\left(B, B^{*}\right)=\bigcap_{i \in V}\left[\left\{\boldsymbol{x} \in \mathbb{R}_{+}^{d}: x_{i}=\bigvee_{k \in \mathrm{pa}(i)} b_{k i} x_{k}=\bigvee_{k \in \mathrm{pa}(i)} b_{k i}^{*} x_{k}\right\} \cup\left\{\boldsymbol{x} \in \mathbb{R}_{+}^{d}: x_{i}>\bigvee_{k \in \mathrm{pa}(i)}\left(b_{k i} \vee b_{k i}^{*}\right) x_{k}\right\}\right], \\
& A_{1}\left(B, B^{*}\right)=\mathbb{R}_{+}^{d} \backslash\left(A_{0}\left(B, B^{*}\right) \cup A_{1 / 2}\left(B, B^{*}\right)\right)\}
\end{aligned}
$$

With this partition we then have:
Theorem 4.8. Let $B, B^{*} \in \mathcal{B}(\mathcal{D})$. Then the function $\rho: \mathbb{R}_{+}^{d} \rightarrow\{0,1 / 2,1\}$

$$
\boldsymbol{x} \mapsto \rho\left(\boldsymbol{x}, B, B^{*}\right)=\frac{1}{2} \cdot \mathbb{1}_{A_{1 / 2}\left(B, B^{*}\right)}(\boldsymbol{x})+\mathbb{1}_{A_{1}\left(B, B^{*}\right)}(\boldsymbol{x})= \begin{cases}0, & \text { if } \boldsymbol{x} \in A_{0}\left(B, B^{*}\right) \\ \frac{1}{2}, & \text { if } \boldsymbol{x} \in A_{1 / 2}\left(B, B^{*}\right) \\ 1, & \text { if } \boldsymbol{x} \in A_{1}\left(B, B^{*}\right)\end{cases}
$$

is a density of $P_{B}$ with respect to $P_{B}+P_{B *}$.
Proof. We must verify properties (A)-(C) of (4.5).
(A) Since $V$ is finite, it suffices to show for every $i \in V$,

$$
\begin{aligned}
& P_{B}\left(\left\{\boldsymbol{x} \in \mathbb{R}_{+}^{d}: x_{i}<\bigvee_{k \in \mathrm{pa}(i)} b_{k i} x_{k}\right\}\right)=\mathbb{P}\left(X_{i}<\bigvee_{k \in \mathrm{pa}(i)} b_{k i} X_{k}\right)=0 \\
& P_{B}\left(\left\{\boldsymbol{x} \in \mathbb{R}_{+}^{d}: x_{i}=\bigvee_{k \in \mathrm{pa}(i)} b_{k i}^{*} x_{k}>\bigvee_{k \in \mathrm{pa}(i)} b_{k i} x_{k}\right\}\right)=\mathbb{P}\left(X_{i}=\bigvee_{k \in \mathrm{pa}(i)} b_{k i}^{*} X_{k}>\bigvee_{k \in \mathrm{pa}(i)} b_{k i} X_{k}\right)=0
\end{aligned}
$$

The former is immediate by (4.9). By the same argument we have for the latter,

$$
\begin{aligned}
0 & \leqslant \mathbb{P}\left(\bigvee_{k \in \mathrm{pa}(i)} b_{k i} X_{k} \vee Z_{i}=\bigvee_{k \in \mathrm{pa}(i)} b_{k i}^{*} X_{k}>\bigvee_{k \in \mathrm{pa}(i)} b_{k i} X_{k}\right)=\mathbb{P}\left(Z_{i}=\bigvee_{k \in \mathrm{pa}(i)} b_{k i}^{*} X_{k}>\bigvee_{k \in \mathrm{pa}(i)} b_{k i} X_{k}\right) \\
& \leqslant \mathbb{P}\left(Z_{i}=\bigvee_{k \in \mathrm{pa}(i)} b_{k i}^{*} \bigvee_{j \in \operatorname{An}(k)} b_{j k} Z_{j}\right)=0
\end{aligned}
$$

where we have used (2.3) and (3.1) for the last inequality and equality, respectively. Thus we have verified (A).

(B) Recall that $P_{B}$ and $P_{B^{*}}$ share the same innovation vector when represented by a recursive ML model. Furthermore, note that the set $\Omega\left(B, B^{*}\right)$ from Lemma 4.7 is a subset of $\bigcap_{i \in V}\left\{X_{i}=\right.$ $\bigvee_{j \in \operatorname{An}(i): b_{j i}=b_{j i}^{*}} b_{j i} Z_{j}\}$. We have $\Omega\left(B, B^{*}\right)=\Omega\left(B^{*}, B\right)$ and hence we obtain from (4.10) for $A \in \mathbb{B}\left(\mathbb{R}_{+}^{d}\right)$,

$$
\begin{aligned}
P_{B}\left(A \cap A_{1 / 2}\left(B, B^{*}\right)\right) & =\mathbb{P}\left(\{\boldsymbol{X} \in A\} \cap \Omega\left(B, B^{*}\right)\right)=\mathbb{P}\left(\left\{\left(\bigvee_{j \in \operatorname{An}(i): b_{j i}=b_{j i}^{*}} b_{j i} Z_{j}, i \in V\right) \in A\right\} \cap \Omega\left(B, B^{*}\right)\right) \\
& =\mathbb{P}\left(\left\{\left(\bigvee_{j \in \operatorname{An}(i): b_{j i}=b_{j i}^{*}} b_{j i}^{*} Z_{j}, i \in V\right) \in A\right\} \cap \Omega\left(B^{*}, B\right)\right)=P_{B^{*}}\left(A \cap A_{1 / 2}\left(B, B^{*}\right)\right)
\end{aligned}
$$

(C) We observe from the definition of $A_{0}\left(B, B^{*}\right)$ and $A_{1 / 2}\left(B, B^{*}\right)$ that

$$
\begin{aligned}
& A_{1}\left(B, B^{*}\right)=\mathbb{R}_{+}^{d} \backslash\left(A_{0}\left(B, B^{*}\right) \cup A_{1 / 2}\left(B, B^{*}\right)\right) \\
& \subseteq \bigcup_{i \in V}\left[\left\{\boldsymbol{x} \in \mathbb{R}_{+}^{d}: \bigvee_{k \in \mathrm{pa}(i)} b_{k i}^{*} x_{k}>x_{i} \geqslant \bigvee_{k \in \mathrm{pa}(i)} b_{k i} x_{k}\right\} \cup\left\{\boldsymbol{x} \in \mathbb{R}_{+}^{d}: x_{i}=\bigvee_{k \in \mathrm{pa}(i)} b_{k i} x_{k}>\bigvee_{k \in \mathrm{pa}(i)} b_{k i}^{*} x_{k}\right\}\right] \\
& \subseteq A_{0}\left(B^{*}, B\right)
\end{aligned}
$$

Since $A_{0}\left(B^{*}, B\right)$ is a $P_{B^{*}}$-null set by (A), this holds for the subset $A_{1}\left(B, B^{*}\right)$ as well.
We observe an interesting relation between the density (4.13) for $\mathcal{D}$ and corresponding densities for subgraphs of $\mathcal{D}$.

Example 4.9. [Local densities $\rho_{i}$ ]
Consider the DAGs

$$
\mathcal{D} \quad \square \longrightarrow \square \longrightarrow \square \quad \mathcal{D}_{2} \quad \square \longrightarrow \square \quad \mathcal{D}_{3} \quad \square \longrightarrow \square
$$

Let $\rho, \rho_{2}$, and $\rho_{3}$ be the corresponding densities from (4.13). For the ML coefficient matrix $B$ of a recursive ML model on $\mathcal{D}$, let $B_{2}$ and $B_{3}$ be the ML coefficient matrices of recursive ML models on $\mathcal{D}_{2}$ and $\mathcal{D}_{3}$ with edge weight $c_{12}=b_{12}$ and $c_{23}=b_{23}$, and let starred quantities denote the same for $B^{*}$. We then find for $\boldsymbol{x}=\left(x_{1}, x_{2}, x_{3}\right) \in \mathbb{R}_{+}^{3}$,

$$
\begin{aligned}
& \rho\left(\boldsymbol{x}, B, B^{*}\right) \\
& =\left(\rho_{2}\left(\boldsymbol{x}_{\mathrm{Pa}(2)}, B_{2}, B_{2}^{*}\right) \vee \rho_{3}\left(\boldsymbol{x}_{\mathrm{Pa}(3)}, B_{3}, B_{3}^{*}\right)\right) \mathbb{1}_{(0, \infty)}\left(\rho_{2}\left(\boldsymbol{x}_{\mathrm{Pa}(2)}, B_{2}, B_{2}^{*}\right) \wedge \rho_{3}\left(\boldsymbol{x}_{\mathrm{Pa}(3)}, B_{3}, B_{3}^{*}\right)\right)
\end{aligned}
$$

This can be observed from Figure 4.3, where the densities are depicted as functions of $x_{2} / x_{1}$ and/or $x_{3} / x_{2}$ for all nine different orders between the ML coefficients in $B$ and $B^{*}$.

Conversely, $\rho_{2}$ and $\rho_{3}$ can be derived from $\rho$ as follows:

$$
\begin{aligned}
& \rho_{2}\left(\boldsymbol{x}_{\mathrm{Pa}(2)}, B_{12}, B_{12}^{*}\right)=\min _{\left\{y \in \mathbb{R}_{+}: \rho\left(\left(\boldsymbol{x}_{\mathrm{Pa}(2)}, y\right), B, B^{*}\right)>0\right\}} \rho\left(\left(\boldsymbol{x}_{\mathrm{Pa}(2)}, y\right), B, B^{*}\right) \\
& \rho_{3}\left(\boldsymbol{x}_{\mathrm{Pa}(3)}, B_{23}, B_{23}^{*}\right)=\min _{\left\{y \in \mathbb{R}_{+}: \rho\left(\left(y, \boldsymbol{x}_{\mathrm{Pa}(3)}\right), B, B^{*}\right)>0\right\}} \rho\left(\left(y, \boldsymbol{x}_{\mathrm{Pa}(3)}\right), B, B^{*}\right)
\end{aligned}
$$

which we learn from Figure 4.3 again.
We extend the findings from Example 4.9 to the general case. Furthermore, we show that the densities $\rho_{i}$ are densities of regular conditional distributions.

![img-5.jpeg](img-5.jpeg)

Figure 4.3: The densities $\rho\left(\boldsymbol{x}, B, B^{*}\right), \rho_{2}\left(\boldsymbol{x}_{\mathrm{Pa}(2)}, B_{2}, B_{2}^{*}\right), \rho_{3}\left(\boldsymbol{x}_{\mathrm{Pa}(3)}, B_{3}, B_{3}^{*}\right)$ from Example 4.9 as func-
tions of $x_{2} / x_{1}$ and/or $x_{3} / x_{2}$. The area where the density is $0 / \frac{1}{2} / 1$ is coloured in red/blue/green. ${ }^{\text {ch4:ex:fig:mar }}$

Proposition 4.10. Let $B, B^{*} \in \mathcal{B}(\mathcal{D})$ and let $\boldsymbol{X}=\boldsymbol{Z} \odot B, \boldsymbol{X}^{*}=\boldsymbol{Z} \odot B^{*}$ follow corresponding recursive ML models on $\mathcal{D}$. For $i \in V$, let $\rho_{i}$ be the density given in (4.13) with respect to the $D A G \mathcal{D}_{i}=(\mathrm{Pa}(i),\{(k, i): k \in \mathrm{pa}(i)\})$ as well as $B_{i}$ and $B_{i}^{*}$ the ML coefficient matrices of recursive ML models on $\mathcal{D}_{i}$ with edge weights $c_{k i}=b_{k i}$ and $c_{k i}^{*}=b_{k i}^{*}$, respectively.
(a) We have for $\rho\left(\boldsymbol{x}, B, B^{*}\right)$ given in (4.13)

$$
\rho\left(\boldsymbol{x}, B, B^{*}\right)=\left(\bigvee_{i \in V} \rho_{i}\left(\boldsymbol{x}_{\mathrm{Pa}(i)}, B_{i}, B_{i}^{*}\right)\right) \mathbb{1}_{(0, \infty)}\left(\bigwedge_{i \in V} \rho_{i}\left(\boldsymbol{x}_{\mathrm{Pa}(i)}, B_{i}, B_{i}^{*}\right)\right)
$$

(b) The function $\rho_{i}$ can be computed from $\rho$ by

$$
\rho_{i}\left(\boldsymbol{x}_{\mathrm{Pa}(i)}, B_{i}, B_{i}^{*}\right)=\min _{\left\{\boldsymbol{y} \in \mathbb{R}_{+}^{d}: \boldsymbol{y}_{\mathrm{Pa}(i)}=\boldsymbol{x}_{\mathrm{Pa}(i)}, \rho\left(\boldsymbol{y}, B, B^{*}\right)>0\right\}} \rho\left(\boldsymbol{y}, B, B^{*}\right)
$$

where we set $\min _{\boldsymbol{y} \in \varnothing} \rho\left(\boldsymbol{y}, B, B^{*}\right)=0$.
(c) The function $\rho_{i}: \mathbb{R}_{+}^{d} \rightarrow\{0,1 / 2,1\}$ such that $\boldsymbol{x}_{\mathrm{Pa}(i)} \mapsto \rho_{i}\left(\boldsymbol{x}_{\mathrm{Pa}(i)}, B_{i}, B_{i}^{*}\right)$ is a density of $P_{B}^{i \mid \mathrm{pa}(i)}$ with respect to $P_{B}^{i \mid \mathrm{pa}(i)}+P_{B^{*}}^{i \mid \mathrm{pa}(i)}$, where $P_{B}^{i \mid \mathrm{pa}(i)}$ is a regular conditional distribution of $X_{i}$ given $\boldsymbol{X}_{\mathrm{pa}(i)}$ and $P_{B^{*}}^{i \mid \mathrm{pa}(i)}$ one of $X_{i}^{*}$ given $\boldsymbol{X}_{\mathrm{pa}(i)}^{*}$.

Proof. Denoting by $A_{0}^{i}\left(B_{i}, B_{i}^{*}\right), A_{1 / 2}^{i}\left(B_{i}, B_{i}^{*}\right), A_{1}^{i}\left(B_{i}, B_{i}^{*}\right)$ the sets defining $\rho_{i}\left(\cdot, B_{i}, B_{i}^{*}\right)$, we have for the corresponding sets of $\rho$,

$$
\begin{aligned}
A_{0}\left(B, B^{*}\right) & =\bigcup_{i \in V}\left\{\boldsymbol{x} \in \mathbb{R}_{+}^{d}: \boldsymbol{x}_{\mathrm{Pa}(i)} \in A_{0}^{i}\left(B_{i}, B_{i}^{*}\right)\right\} \\
A_{1 / 2}\left(B, B^{*}\right) & =\bigcap_{i \in V}\left\{\boldsymbol{x} \in \mathbb{R}_{+}^{d}: \boldsymbol{x}_{\mathrm{Pa}(i)} \in A_{1 / 2}^{i}\left(B_{i}, B_{i}^{*}\right)\right\} \\
A_{1}\left(B, B^{*}\right) & =\bigcap_{i \in V}\left\{\boldsymbol{x} \in \mathbb{R}_{+}^{d}: \boldsymbol{x}_{\mathrm{Pa}(i)} \in A_{1 / 2}^{i}\left(B_{i}, B_{i}^{*}\right) \cup A_{1}^{i}\left(B_{i}, B_{i}^{*}\right)\right\} \cap\left[\mathbb{R}_{+}^{d} \backslash A_{1 / 2}\left(B_{i}, B_{i}^{*}\right)\right]
\end{aligned}
$$

From this we obtain (a) and (b). Now, to see (c) we reason as follows:

$$
P_{B}^{i \mid \mathrm{pa}(i)}\left(\left(0, x_{i}\right] \mid \boldsymbol{x}_{\mathrm{pa}(i)}\right)=F_{Z_{i}}\left(x_{i}\right) \mathbb{1}_{\left[\bigvee_{k \in \mathrm{pa}(i)} b_{k i} x_{k}, \infty\right)}\left(x_{i}\right), \quad \boldsymbol{x}_{\mathrm{Pa}(i)} \in \mathbb{R}_{+}^{|\mathrm{Pa}(i)|}
$$

is a regular conditional distribution function of $X_{i}$ given $\boldsymbol{X}_{\mathrm{pa}(i)}$. To see this, use (4.9) and the independence of the innovations to obtain

$$
\begin{aligned}
P_{B}^{i \mid \mathrm{pa}(i)}\left(\left(0, x_{i}\right] \mid \boldsymbol{x}_{\mathrm{pa}(i)}\right) & =\mathbb{P}\left(X_{i} \leqslant x_{i} \mid \boldsymbol{X}_{\mathrm{pa}(i)}=\boldsymbol{x}_{\mathrm{pa}(i)}\right) \\
& =\mathbb{P}\left(\bigvee_{k \in \mathrm{pa}(i)} b_{k i} X_{k} \vee Z_{i} \leqslant x_{i} \mid \boldsymbol{X}_{\mathrm{pa}(i)}=\boldsymbol{x}_{\mathrm{pa}(i)}\right) \\
& =F_{Z_{i}}\left(x_{i}\right) \mathbb{1}_{\left[\bigvee_{k \in \mathrm{pa}(i)} b_{k i} x_{k}, \infty\right)}\left(x_{i}\right)
\end{aligned}
$$

Since $\boldsymbol{X}$ and $\boldsymbol{X}^{*}$ share the same innovation vector, we have

$$
P_{B^{*}}^{i \mid \mathrm{pa}(i)}\left(\left(0, x_{i}\right] \mid \boldsymbol{x}_{\mathrm{pa}(i)}\right)=F_{Z_{i}}\left(x_{i}\right) \mathbb{1}_{\left[\bigvee_{k \in \mathrm{pa}(i)} b_{k i}^{*} x_{k}, \infty\right)}\left(x_{i}\right), \quad \boldsymbol{x}_{\mathrm{Pa}(i)} \in \mathbb{R}_{+}^{|\mathrm{Pa}(i)|}
$$

is a regular conditional distribution function of $X_{i}^{*}$ given $\boldsymbol{X}_{\mathrm{pa}(i)}^{*}$. Figure 4.4 depicts the two conditional distribution functions for the three possible orders between $\bigvee_{k \in \mathrm{pa}(i)} b_{k i} x_{k}$ and $\bigvee_{k \in \mathrm{pa}(i)} b_{k i}^{*} x_{k}$. It then suffices to show for all $\boldsymbol{x}_{\mathrm{pa}(i)} \in \mathbb{R}_{+}^{|\mathrm{pa}(i)|}$ and $y \in \mathbb{R}_{+}$,

$$
P_{B}^{i \mid \mathrm{pa}(i)}\left((0, y] \mid \boldsymbol{x}_{\mathrm{pa}(i)}\right)=\int_{(0, y]} \rho_{i}\left(\boldsymbol{x}_{\mathrm{Pa}(i)}, B_{i}, B_{i}^{*}\right)\left(P_{B}^{i \mid \mathrm{pa}(i)}+P_{B^{*}}^{i \mid \mathrm{pa}(i)}\right)\left(d x_{i} \mid \boldsymbol{x}_{\mathrm{pa}(i)}\right)
$$

and for this again by definition of $\rho_{i}$ (cf. (4.6) and the related discussion) that

$$
\begin{aligned}
& P_{B}^{i \mid \mathrm{pa}(i)}\left((0, y] \cap\left(0, \bigvee_{k \in \mathrm{pa}(i)} b_{k i} x_{k}\right) \mid \boldsymbol{x}_{\mathrm{pa}(i)}\right)=0 \\
& P_{B}^{i \mid \mathrm{pa}(i)}\left((0, y] \cap\left\{\bigvee_{k \in \mathrm{pa}(i)} b_{k i}^{*} x_{k}\right\} \mid \boldsymbol{x}_{\mathrm{pa}(i)}\right)=0 \quad \text { if } \bigvee_{k \in \mathrm{pa}(i)} b_{k i}^{*} x_{k}>\bigvee_{k \in \mathrm{pa}(i)} b_{k i} x_{k} \\
& P_{B}^{i \mid \mathrm{pa}(i)}\left((0, y] \cap\left\{\bigvee_{k \in \mathrm{pa}(i)} b_{k i} x_{k}\right\} \mid \boldsymbol{x}_{\mathrm{pa}(i)}\right)=P_{B^{*}}^{i \mid \mathrm{pa}(i)}\left((0, y] \cap\left\{\bigvee_{k \in \mathrm{pa}(i)} b_{k i} x_{k}\right\} \mid \boldsymbol{x}_{\mathrm{pa}(i)}\right) \\
& \text { if } \bigvee_{k \in \mathrm{pa}(i)} b_{k i}^{*} x_{k}=\bigvee_{k \in \mathrm{pa}(i)} b_{k i} x_{k} \\
& P_{B}^{i \mid \mathrm{pa}(i)}\left((0, y] \cap\left(\bigvee_{k \in \mathrm{pa}(i)}\left(b_{k i} \vee b_{k i}^{*}\right) x_{k}, \infty\right) \mid \boldsymbol{x}_{\mathrm{pa}(i)}\right)=P_{B^{*}}^{i \mid \mathrm{pa}(i)}\left((0, y] \cap\left(\bigvee_{k \in \mathrm{pa}(i)}\left(b_{k i} \vee b_{k i}^{*}\right) x_{k}, \infty\right) \mid \boldsymbol{x}_{\mathrm{pa}(i)}\right)
\end{aligned}
$$

Since $F_{Z_{i}}$ is atom-free, this can be read directly from Figure 4.4.
We now show that $\widehat{B}$ is indeed a GMLE in the sense of [18]. Note also that the GMLE is obtained by piecing together individual GMLEs corresponding to conditional distributions

![img-6.jpeg](img-6.jpeg)

Figure 4.4: The conditional distribution functions from the proof of Proposition 4.10(c).ch4:fig:lemA4
of any variable given its parents. Thus this is similar to what is obtained in cases where the distributions have densities with respect to a product measure, as the maximum of the likelihood function is then obtained by maximizing each conditional likelihood function for the density of a node given its parents.
Theorem 4.11. Let $\boldsymbol{x}^{(t)}=\left(x_{1}^{(t)}, \ldots, x_{n}^{(t)}\right)$ for $t=1, \ldots, n$ be a sample from a recursive $M L$ model on a $D A G \mathcal{D}$ with $M L$ coefficient matrix $B \in \mathcal{B}(\mathcal{D})$ unknown.
(a) The matrix $\widehat{B}$ from (4.3) is a GMLE of $B$.
(b) For every $i \in V,\left(\widehat{b}_{k i}, k \in \mathrm{pa}(i)\right)$ is a GMLE of the ML coefficients $\left(b_{k i}, k \in \mathrm{pa}(i)\right)$ of a random vector following a recursive ML model on $\mathcal{D}_{i}=(\operatorname{Pa}(i),\{(k, i): k \in \mathrm{pa}(i)\})$ with edge weights $c_{k i}=b_{k i}$.
(c) For every $i \in V$ and $k \in \mathrm{pa}(i), \widehat{b}_{k i}$ is the only GMLE of the ML coefficient $b_{k i}$ of a random vector following a recursive ML model on $\mathcal{D}_{k i}=(\{k, i\},\{(k, i)\})$ with edge weight $c_{k i}=b_{k i}$.

Proof. (a) First, recall that $\widehat{B}$ is indeed a ML coefficient matrix of a recursive ML model on $\mathcal{D}$. The first condition in the definition of a GMLE in (4.4) is satisfied due to the definition of $\rho(\cdot, \widehat{B}, \widehat{B})$ since $A_{1 / 2}(\widehat{B}, \widehat{B})=\mathbb{R}_{+}^{d}$. Since the densities $\rho(\cdot, \widehat{B}, B)$ and $\rho(\cdot, B, \widehat{B})$ have the values 0,1 , $1 / 2$, and $A_{1 / 2}(\widehat{B}, B)=A_{1 / 2}(B, \widehat{B})$, to verify the second condition in (4.4), it suffices to show that there is some realization $\boldsymbol{x}^{\left(t_{1}\right)} \in A_{0}(B, \widehat{B})$ whenever there is some realization $\boldsymbol{x}^{\left(t_{2}\right)} \in A_{0}(\widehat{B}, B)$; cf. Example 4.6, in particular (4.8). So let $\boldsymbol{x}^{\left(t_{2}\right)} \in A_{0}(\widehat{B}, B)$ for some $t_{2} \in\{1, \ldots, n\}$. We find, for some $i \in V$, from the definition of $A_{0}(\widehat{B}, B)$ and the fact that $x_{i}^{(t)} \geqslant \bigvee_{k \in \mathrm{pa}(i)} \widehat{b}_{k i} x_{k}^{(t)}$,

$$
\boldsymbol{x}^{\left(t_{2}\right)} \in\left\{\boldsymbol{x} \in \mathbb{R}_{+}^{d}: \bigvee_{k \in \mathrm{pa}(i)} \widehat{b}_{k i} x_{k}<x_{i}=\bigvee_{k \in \mathrm{pa}(i)} b_{k i} x_{k}\right\}
$$

Hence, $x_{i}^{\left(t_{2}\right)}=b_{k i} x_{k}^{\left(t_{2}\right)}$ for some $k \in \mathrm{pa}(i)$ with $\widehat{b}_{k i}<b_{k i}$. Let now $t_{1} \in\{1, \ldots, n\}$ such that $\bigwedge_{s=1}^{n} y_{k i}^{(s)}=y_{k i}^{\left(t_{1}\right)}$. As $\widehat{b}_{k i}=\bigwedge_{s=1}^{n} y_{k i}^{(s)}$, we have $x_{i}^{\left(t_{1}\right)}<b_{k i} x_{k}^{\left(t_{1}\right)}$ implying that $\boldsymbol{x}^{\left(t_{1}\right)} \in A_{0}(B, \widehat{B})$.
The statement in (b) is a consequence of (a), and (c) has already been shown in Example 4.6.

Figure 4.5 illustrates the DAGs $\mathcal{D}_{i}$ in Theorem 4.11(b) or Proposition 4.10.
![img-7.jpeg](img-7.jpeg)

Figure 4.5: The DAGs $\mathcal{D}_{i}$ from Theorem 4.11(b) for a recursive ML model on the DAG $\mathcal{D}$ depicted on the left-hand side with ML coefficient matrix $B$. The edges are marked with the corresponding ML coefficients. Note that $b_{12}, b_{14}, b_{34}, b_{24}$ can be arbitary positive numbers but $b_{24} \geqslant b_{23} b_{34}$. Ch4: exam:Di

# Edge weights $\boldsymbol{c}_{\boldsymbol{k i}}$ 

We have started with the estimation of $B$ as it is not possible to recover the true edge weights $c_{k i}$ underlying representation (2.1) of $\boldsymbol{X}$ from $\boldsymbol{x}^{(1)}, \ldots, \boldsymbol{x}^{(n)}$, since different edge weights may lead to $B$. But we know what edge weights that are and, obviously, the probability measure $P_{B}$ induced by $\boldsymbol{X}$ is the same for different edge weights that all result in $B$. As a consequence, all edge weights that lead, together with $\mathcal{D}$, to the GMLE $\widehat{B}$ of $B$ are GMLEs of the true edge weights of $\boldsymbol{X}$ and its properties are inherited.

Corollary 4.12. Let $c_{k i}$ for $i \in V$ and $k \in \mathrm{pa}(i)$ be the edge weights of representation (2.1) of $\boldsymbol{X}$ and $\mathcal{D}^{\widehat{B}}$ the minimum $M L D A G$ based on $\widehat{B}$. We denote by $\mathrm{pa}^{\widehat{B}}(i)$ the parents of $i$ in $\mathcal{D}^{\widehat{B}}$. Then every $\left(\widehat{c}_{k i}, i \in V, k \in \mathrm{pa}(i)\right)$ such that

$$
\widehat{c}_{k i}=\widehat{b}_{k i} \text { if } k \in \mathrm{pa}^{\widehat{B}}(i) \quad \text { and } \quad \widehat{c}_{k i} \in\left(0, \widehat{b}_{k i}\right] \text { if } k \in \mathrm{pa}(i) \backslash \mathrm{pa}^{\widehat{B}}(i)
$$

is a GMLE of $\left(c_{k i}, i \in V, k \in \mathrm{pa}(i)\right)$.

## 5 Learning the structure of a recursive max-linear model

In contrast to the assumptions in the previous section, we now assume independent realizations $\boldsymbol{x}^{(1)}, \ldots, \boldsymbol{x}^{(n)}$ of $\boldsymbol{X}$ following a recursive ML model but the underlying DAG $\mathcal{D}$ is unknown. We know from previous discussions that it is not possible to recover $\mathcal{D}$ and the true edge weights $c_{k i}$ but, based on Corollary 4.12, it is possible to identify the ML coefficient matrix $B$ and the class of all DAGs and edge weights that could have generated $\boldsymbol{X}$ via (2.1). We therefore again focus on the estimation of $B$.

Following Algorithm 3.3, it suffices for any pair of distinct $i, j \in V$ to decide whether $\operatorname{supp}\left(Y_{j i}\right)=\operatorname{supp}\left(X_{j} / X_{i}\right)$ has a positive lower bound, alternatively a finite upper bound, and if so, to estimate the bound. Recall from Table 3.1 that, if there is such a bound, then it is an atom of $Y_{j i}$. Since we can expect to observe atoms more than twice for $n$ sufficiently large, we propose the following estimation method.

Algorithm 5.1. [Find an estimate $\widetilde{B}$ of $B$ from $\boldsymbol{x}^{(1)}, \ldots, \boldsymbol{x}^{(n)}$ ]

1. For all $i \in V=\{1, \ldots, d\}$, set $\widetilde{b}_{i i}=1$.
2. For all $i, j \in V$ with $i \neq j$,

$$
\begin{aligned}
& \text { if } \#\left\{t: \bigwedge_{s=1}^{n} y_{j i}^{(s)}=y_{j i}^{(t)}\right\} \geqslant 2 \text {, then conclude } j \in \operatorname{an}(i) \text {, set } \bar{b}_{j i}=\bigwedge_{t=1}^{n} y_{j i}^{(t)} \\
& \text { else, set } \bar{b}_{j i}=0
\end{aligned}
$$

In the second step rather two steps are summarized. The first step is concerned with estimating the ancestors of the nodes, the second with estimating the ML coefficients.

Note that the estimate $\widehat{B}$ from Algorithm 5.1 is not necessarily a ML coefficient matrix of a recursive ML model. For example, the property that $b_{j i}>0$ if $b_{j k} b_{k i}>0$ (see, for example, Corollary 3.12 of [12]) is not guaranteed. Many modifications of $\widehat{B}$ are possible, and here we shall not discuss this in detail. Rather we notice that Algorithm 5.1 outputs, $\mathbb{P}$-almost surely, the true ML coefficient matrix $B$ if $n$ is sufficiently large. As in the case where the DAG is known — see Proposition 4.5 - the probability that $\bar{b}_{j i}$ is equal to the true value $b_{j i}$ converges to one at an exponential rate.

# 6 Conclusion and outlook 

We studied the identifiability of the elements of a recursive ML model from the distribution $\mathcal{L}(\boldsymbol{X})$ of $\boldsymbol{X}$. The associated DAG and the edge weights are not identifiable, however, the ML coefficient matrix $B$. In other words, we can identify representation (2.3) but not (2.1). The class of all DAGs and edge weights that could have generated $\boldsymbol{X}$ via (2.1) and the distribution of the innovation vector are identifiable from $\mathcal{L}(\boldsymbol{X})$. As a consequence, we can recover $B$, the class of the DAGs and edge weights, and the innovation distributions from realizations of $\boldsymbol{X}$.

Parameter estimation and structure learning for recursive ML models seem to be challenging tasks because assumptions usually made in standard methods are not met. However, in both cases, $B$ can be estimated by a simple procedure. The key idea of our approach is to consider the observed ratios between any pair of components, i.e. to perform a transformation on the realizations. The transformed realizations or rather the distributional properties of the corresponding random variables make it possible to identify, with probability 1 , the true $B$ whenever the number of observations $n$ is sufficiently large. It would be interesting to investigate the relationship between the performance of our procedures and the number $n$ of observations. Here, one possible question is how many observations are at least necessary to estimate $B$ exactly; see, Example 4.3. In addition it would be interesting to study estimation of the DAG structure for moderate sample sizes, where exact estimation is not guaranteed.

We emphasize again that, although our estimates are derived under the assumption that the distribution of the innovation vector $\boldsymbol{Z}$ is fixed, the estimates do not depend on what this distribution is and would therefore also be valid in the situation where the innovations are independent with unkown distributions that are atom-free and have support equal to $\mathbb{R}_{+}$. Algorithm 3.4 provides a recursive procedure to obtain the distribution functions $F_{Z_{i}}$ from $B$ and the marginal distribution functions $F_{X_{i}}$ of $X_{i}$. Estimating $B$ by $\widehat{B}$ and the distributions $F_{X_{i}}$, for example, by their empirical versions, we can apply this procedure to find estimators of the distributions $F_{Z_{i}}$ although it will formally violate the assumption of atom-freeness and thus it is both more efficient and formally correct to estimate these parametrically, or under suitable monotonicity restrictions.

An important goal for future work is to apply the procedures to real-world data. However, it is unreasonable to expect any non-simulated data to follow a recursive ML model exactly and the model should then be modified by adding appropriate noise terms. In particular we

should not expect that we observe a minimal observed ratio more than twice, as we exploit in Algorithm 5.1. It seems to be more reasonable to expect values close to each other. We therefore want to develop methods based on accumulation points.

# Acknowledgements 

We thank Justus Hartl for providing a first discussion about the different estimators suggested in this paper in his master's thesis. NG acknowledges support by Deutsche Forschungsgemeinschaft (DFG) through the TUM International Graduate School of Science and Engineering (IGSSE). All authors benefited from financial support from the Alexander von Humboldt Stiftung.
