# Recursive max-linear models with propagating noise 

Johannes Buck<br>Center for Mathematical Sciences, Technical University of Munich, Boltzmanstrasse 3, 85748 Garching, Germany<br>e-mail: j.buck@tum.de<br>and

## Claudia Klüppelberg

Center for Mathematical Sciences, Technical University of Munich, Boltzmanstrasse 3, 85748 Garching, Germany
e-mail: cklu@ma.tum.de


#### Abstract

Recursive max-linear vectors model causal dependence between node variables by a structural equation model, expressing each node variable as a max-linear function of its parental nodes in a directed acyclic graph (DAG) and some exogenous innovation. For such a model, there exists a unique minimum DAG, represented by the Kleene star matrix of its edge weight matrix, which identifies the model and can be estimated. For a more realistic statistical modeling we introduce some random observational noise. A probabilistic analysis of this new noisy model reveals that the unique minimum DAG representing the distribution of the non-noisy model remains unchanged and identifiable. Moreover, the distribution of the minimum ratio estimators of the model parameters at their left limits are completely determined by the distribution of the noise variables up to a positive constant. Under a regular variation condition on the noise variables we prove that the estimated Kleene star matrix converges to a matrix of independent Weibull entries after proper centering and scaling.


MSC2020 subject classifications: 60G70, 62F12, 62G32, 62H22.
Keywords and phrases: Graphical model, Bayesian network, directed acyclic graph, extreme value analysis, max-linear model, noisy model, regular variation.

Received May 2020.

## 1. Introduction

Graphical modeling has shown to be a powerful tool for understanding causal dependencies in a multivariate random vector. However, most models are linear and limited to discrete or Gaussian distributions (see e.g. [25] and [27]). Such models lead to severe underestimation of large risks and, therefore, are not suitable in the context of extreme risk assessment. First examples combining

extreme value methods with graphical models include flooding in river networks ([12]), financial risk ([10], [23]), and nutrients ([23]).

We consider the class of recursive max-linear (ML) models, which has been defined in [14]. A recursive ML model is defined by a structural equation model (SEM) of the form

$$
X_{i}=\bigvee_{j \in \mathrm{pa}(i)} c_{j i} X_{j} \vee Z_{i}, \quad i=1, \ldots, d
$$

where the dependence structure between random variables is represented by a DAG $\mathcal{D}:=(V, E)$ with node set $V:=\{1, \ldots, d\}$ and edge set $E=E(\mathcal{D}) \subseteq$ $V \times V$, and each variable $X_{i}$ for $i \in V$ has a representation in terms of ML functions of its parental nodes $\mathrm{pa}(i)=\{j \in V:(j, i) \in E\}$ and an independent innovation $Z_{i}$.

Both, SEMs (e.g. [5], [31]) and directed graphical models (e.g. [25], [27], [35]) are well-established models and widely used to understand causality.

ML models similar to (1.1) have been proposed and studied in a time series context (e.g. [9]), in terms of moving maxima processes (e.g. [16]), or as tropical models in algebra (e.g. [21], [30]) with applications to various optimization problems (e.g. [2], [6], [36]).

As shown in [24], recursive ML models respect the basic Markov properties associated with DAGs (e.g. [28], [29]). Moreover, the equation system (1.1) has the solution

$$
X_{i}=\bigvee_{j \in \mathrm{pa}(i)} b_{j i} Z_{j}, \quad i=1, \ldots, d
$$

with ML coefficient matrix (in tropical algebra called the Kleene star matrix) $\boldsymbol{B}:=\left(b_{i j}\right)_{d \times d}$, see [6], Corollary 1.6.16. Unlike the edge weight matrix $\boldsymbol{C}=$ $\left(c_{i j}\right)_{d \times d}, \boldsymbol{B}$ is identifiable and completely determines the distribution of $\boldsymbol{X}:=$ $\left(X_{1}, \ldots, X_{d}\right)$ (see [15], Theorem 1). Also, $\boldsymbol{B}$ is idempotent with respect to the tropical matrix multiplication defined in (2.4) below, and defines a graphical model on a DAG with node set $V$ and an edge $j \rightarrow i$ whenever there is a path from $j$ to $i$ in $\mathcal{D}$. Furthermore, [15] proposes a minimum ratio estimator for $\boldsymbol{B}$, which itself is idempotent, and is a generalized maximum likelihood estimator in the sense of [22].

The model (1.1) states that an extreme node observation $X_{i}$ in the DAG is either the result of a large external innovation $Z_{i}$, or the weighted maximum of observations from the parent nodes of $i$ in $\mathcal{D}$. As we see from the solution (1.2), all past innovations drive this observation. Our aim is to generalise this rather restricted recursive structure as to allow for certain observation errors, independent of this model.

More precisely, we extend the original model (1.1) by allowing for multiplicative observation errors and define

$$
U_{i}=\left(\bigvee_{j \in \mathrm{pa}(i)} c_{j i} U_{j} \vee Z_{i}\right) \varepsilon_{i}, \quad i=1, \ldots, d
$$

with $\varepsilon_{i} \geq 1$ and iid for $i=1, \ldots, d$. By taking advantage of tropical algebra, we

present in Theorem 3.2 a solution of (1.3) which represents each node variable $U_{i}$ in terms of a ML function of its ancestral nodes and an independent innovation $Z_{i}$ given by

$$
U_{i}=\bigvee_{j \in \operatorname{an}(i) \cup\{i\}} \bar{b}_{j i} Z_{j}, \quad i=1, \ldots, d
$$

where an $(i)$ denotes the ancestors of $i$ and $\bar{b}_{j i}$ are random variables involving the edge weights and the noise variables.

It comes as no surprise that the true DAG and edge weights for a recursive ML model with propagating noise inherit the non-identifiability property from the non-noisy model. However, as we will prove in Section 4, the ML coefficient matrix $\boldsymbol{B}=\left(b_{i j}\right)_{d \times d}$ remains identifiable in spite of the observational noise and even if we do not know the underlying DAG.

To link up our new model (1.3) with existing literature, observe that a logtransformation of (1.3) yields

$$
\tilde{U}_{i}=\bigvee_{j \in \operatorname{pa}(i)}\left(\tilde{c}_{j i}+\tilde{U}_{j}\right) \vee \tilde{Z}_{i}+\tilde{\varepsilon}_{i}, \quad i=1, \ldots, d
$$

with $\tilde{\varepsilon}_{i} \geq 0$. However, due to the maximum operator, the class of max-linear models is highly non-smooth such that most standard methods do not apply. For every $j \in \mathrm{pa}(i)$, the difference $\tilde{U}_{i}-\tilde{U}_{j}$ is lower-bounded by $\tilde{c}_{j i}$ and

$$
\mathbb{P}\left(\tilde{U}_{i}-\tilde{U}_{j} \leq \tilde{c}_{j i}+x \mid \tilde{U}_{i}=\tilde{c}_{j i}+\tilde{U}_{j}+\tilde{\varepsilon}_{i}\right)=\mathbb{P}\left(\tilde{\varepsilon}_{i} \leq x\right)
$$

Example 1.2.2 of [6] might then serve as motivating example for model (1.4). Assume that $i$ is a priority flight and there are several feeder flights to $i$. Assume that the departure of a feeder flight $j$ is delayed by $X_{j}$, and there are passengers, who have to catch flight $i$. Moreover, let $c_{j i}$ be the departure time of flight $i$ minus arrival time of flight $j$ minus transit time according to schedule. There may be a further delay $Z_{i}$ of flight $i$ caused by non-connecting passengers. Assuming that flight $i$ also waits for such non-connecting passengers, the delay of flight $i$ is given by $\tilde{U}_{i}=\bigvee_{j \in \operatorname{pa}(i)}\left(\tilde{c}_{j i}+\tilde{U}_{j}\right) \vee \tilde{Z}_{i}$. Some other delays are independent of possible passenger like bad weather conditions, delayed start clearance etc. Then we find exactly model (1.4), the max-linear model with positive noise.

The estimation of (linear) functions with one-sided errors has been considered in the literature before. For instance, in [17] and [20] observations are given by $Y_{j}=f\left(X_{j}\right)+\varepsilon_{j}$ for $j=1, \ldots, n$ with observation errors $\varepsilon_{j}>0$, with density given conditionally or unconditionally on $X_{j}=x$, and $f$ describes some frontier or boundary curve, which has to be estimated. To present an archetypical example, consider the linear regression problem stated in [33] and [34] as $Y_{i}=\beta+\varepsilon_{i}$ for $i=1, \ldots, n$ and observation errors, which have density $g(x) \sim \alpha c x^{\alpha-1}$ as $x \downarrow 0$ for $\alpha, c>0$. In these papers, the focus is on the non-regular case, when $\alpha<2$. Then $\beta$ can be estimated by the sample minimum $Y_{1, n}$ which has a Weibull limit law:

$$
\lim _{n \rightarrow \infty} \mathbb{P}\left((n c)^{-1 / \alpha}\left(Y_{1, n}-\beta_{0}\right) \leq x\right)=1-\exp \left(-x^{-\alpha}\right), \quad 0<x<\infty
$$

The work in [33] has been used in [8] to estimate the coefficient $\phi$ of a first order autoregressive time series with positive innovations. They propose the minimum ratio estimator $\hat{\phi}=\bigwedge_{j=1}^{n} X_{j} / X_{j-1}$ and show in their Corollary 2.4 that it also has a Weibull limit law similar to (1.5).

In our model (1.3) we find two interpretations for the noise variables. Firstly, in the log-transformed version (1.4) we consider a ML model as baseline model, which is observed with some additive noise. A second representation is given in Corollary 3.3 below, where the edge and path weights become noisy by the noise variables. This gives rise to the interpretation that we observe the model parameters with noise similarly as in the regression examples above. As a consequence, a path from $j$ to $i$ realizing the ML coefficient $b_{j i}$ is no longer deterministic but depends on the individual realizations of the noise variables. However, in Theorem 3.12 we show that at the left limit of support the distribution of the ratio of two model components is determined by all noise variables along the path between the two nodes. Assuming noise variables with regularly varying distribution in their left limit of support, we propose a minimum ratio estimator and show in Theorem 5.2 that the estimated ML coefficient matrix converges to a matrix of independent Weibull entries after proper centering and rescaling.

The paper is organized as follows. In Section 2, we summarize the properties of recursive ML models as defined in (1.1) and state the most important results relevant for our paper. In Section 3 we consider the extension of the recursive ML model given in (1.3), which we coin the max-linear model with propagating noise and present its solution and the main properties of this new model. In Section 4 we address the identifiability of the ML model with propagating noise. Similarly as in (1.5) we suggest minimum ratio estimators for the model parameters $\boldsymbol{B}$. In Section 5 we assume regular variation of the noise variables. Under this assumption, we show that the minimum ratios are asymptotically independent and Weibull distributed. Finally, in Section 6, we provide a data example and apply the theory that we have derived in the previous sections. All proofs are postponed to an Appendix.

Throughout we use the following notation. $\mathbb{R}_{+}=(0, \infty)$ and $\overline{\mathbb{R}}_{+}=[0, \infty)$, $x \wedge y=\min \{x, y\}$ and $x \vee y=\max \{x, y\}$ with $\bigwedge_{i \in \emptyset} x_{i}=\infty$ and $\bigvee_{i \in \emptyset} x_{i}=0$ for $x_{i} \in \mathbb{R}_{+}$. Bold letters denote vectors and matrices, e.g. $\boldsymbol{I}_{d}$ denotes the $d \times d$ identity matrix. Moreover, all vectors are row vectors unless stated otherwise. For two functions $f, g$ we write $f(x) \sim g(x)$ as $x \downarrow c$ if $\lim _{x \downarrow c} f(x) / g(x)=1$ and $\mathbf{1}$ denotes the indicator function. For a random variable $Y$ with distribution function $F_{Y}$, the symbol $F_{Y}^{*-}$ denotes its quantile function.

# 2. Preliminaries - recursive max-linear models 

### 2.1. Graph terminology

We use the same graph notation as in [14]. A directed graph is a pair $(V, E)$ of a node set $V=\{1, \ldots, d\}$ and an edge set $E=\{j \rightarrow i: i, j \in V, i \neq j\}$. A node $j$ is called a parent of $i$ if $j \rightarrow i \in E$ and write $(j, i) \in E$. A (directed) path from $j$ to

$i$ is a sequence of distinct nodes $\left[j=k_{0}, k_{1}, \ldots, k_{n}=i\right]$ such that $k_{r-1} \rightarrow k_{r}$ for each $r \in\{1, \ldots, n\}$, and a directed cycle is a path where $j=i$. A node $j$ is called an ancestor of $i$, if there exists a path from $j$ to $i$, then $i$ is called a descendant of $j$. The node sets $\mathrm{pa}(i), \mathrm{an}(i)$ and $\operatorname{de}(i)$ denote the parents, ancestors, and the descendants of node $i$, respectively, and we abbreviate $\operatorname{An}(i):=\operatorname{an}(i) \cup\{i\}$.

Finally, for a path $p=\left[k_{0}, k_{1}, \ldots, k_{n}\right]$ we define the node set on the path (excluding the initial node) by $S_{p}:=\left\{k_{1}, \ldots, k_{n}\right\}$ and its path length by $\left|S_{p}\right|$.

Throughout this paper $\mathcal{D}=(V, E)$ is a directed acyclic graph (DAG), and we recall that a complete DAG is a complete graph with directed edges.

A matrix $\boldsymbol{C} \in \overline{\mathbb{R}}_{+}^{d \times d}$ defines a weighted directed graph, where $j \rightarrow i \in \mathcal{D}$ if and only if its edge weight $c_{j i}$ is positive. The path weight of a path in $\mathcal{D}$ is then the product of its edge weights.

For a DAG $\mathcal{D}$ on $V$ with edge weight matrix $\boldsymbol{C}$, its reachability $D A G$ is defined as a DAG on $V$ having edge $j \rightarrow i$ if and only if $\mathcal{D}$ has a path from $j \rightarrow i$; moreover, $\boldsymbol{B}$ represents the edge weight matrix of the reachability DAG. We call $\boldsymbol{B}$ the $M L$ coefficient matrix and remark that it is a weighted reachability matrix for $\mathcal{D}$.

# 2.2. Recursive max-linear models 

We first formally introduce the class of recursive ML models and state their most important results for this paper. Let $\mathcal{D}=(V, E)$ be a DAG. Then a random vector $\boldsymbol{X}:=\left(X_{1}, \ldots, X_{d}\right)$ is a recursive max-linear vector or follows a max-linear Bayesian network on $\mathcal{D}$ if

$$
X_{i}:=\bigvee_{k \in \operatorname{pa}(i)} c_{k i} X_{k} \vee Z_{i}, \quad i \in 1, \ldots, d
$$

with positive edge weights $c_{k i}$ for $i \in V$ and $k \in \mathrm{pa}(i)$, and independent positive random variables $Z_{1}, \ldots, Z_{d}$ with support $\mathbb{R}_{+}$and atom-free distributions. We shall refer to $\boldsymbol{Z}:=\left(Z_{1}, \ldots, Z_{d}\right)$ as the vector of innovations.

For a path $p=\left[j=k_{0} \rightarrow k_{1} \rightarrow \ldots \rightarrow k_{n}=i\right]$ from $j$ to $i$ we define the path weight

$$
d_{j i}(p):=\prod_{l=0}^{n-1} c_{k_{l} k_{l+1}}
$$

Denoting the set of all paths from $j$ to $i$ by $P_{j i}$, we define the ML coefficient matrix $\boldsymbol{B}=\left(b_{i j}\right)_{d \times d}$ of $\boldsymbol{X}$ with entries

$$
b_{i j}:=\bigvee_{p \in P_{i j}} d_{i j}(p) \quad \text { for } i \in \operatorname{an}(j), \quad b_{i i}=1, \quad \text { and } \quad b_{i j}=0 \quad \text { for } i \in V \backslash \operatorname{An}(j)
$$

The components of $\boldsymbol{X}$ can also be expressed as ML functions of their ancestral innovations and an independent one; the corresponding ML coefficients are the

entries of $\boldsymbol{B}$ :

$$
X_{i}=\bigvee_{k \in \operatorname{An}(i)} b_{k i} Z_{k}, \quad i \in 1, \ldots, d
$$

which can be shown by a path analysis as in Theorem 2.2 in [14] or by tropical algebra as in (2.6) below, and as we explain now.

For two non-negative matrices $\boldsymbol{F}$ and $\boldsymbol{G}$, where the number of columns in $\boldsymbol{F}$ is equal to the number of rows in $\boldsymbol{G}$, we define the matrix product $\odot$ : $\overline{\mathbb{R}}_{+}^{m \times n} \times \overline{\mathbb{R}}_{+}^{n \times p} \rightarrow \overline{\mathbb{R}}_{+}^{m \times p}$ by

$$
\left(\boldsymbol{F}=\left(f_{i j}\right)_{m \times n}, \boldsymbol{G}=\left(g_{i j}\right)_{n \times p}\right) \mapsto \boldsymbol{F} \odot \boldsymbol{G}:=\left(\bigvee_{k=1}^{n} f_{i k} g_{k j}\right)_{m \times p}
$$

The triple $\left(\overline{\mathbb{R}}_{+}, \vee, \cdot\right)$, is an idempotent semiring with 0 as 0 -element and 1 as 1-element and the operation $\odot$ is therefore a matrix product over this semiring; see for example [6]. Denoting by $\mathcal{M}$ all $d \times d$ matrices with non-negative entries and by $\vee$ the componentwise maximum between two matrices, $(\mathcal{M}, \vee, \odot)$ is also a semiring with the null matrix as 0 -element and the $d \times d$ identity matrix $\boldsymbol{I}_{d}$ as 1-element.

The matrix product $\odot$ allows us to represent the ML coefficient matrix $\boldsymbol{B}$ of $\boldsymbol{X}$ in terms of the edge weight matrix $\boldsymbol{C}:=\left(c_{i j} \mathbf{1}_{\operatorname{pa}(j)}(i)\right)_{d \times d}$ of $\mathcal{D}$, since (2.1) can be rewritten as

$$
\boldsymbol{X}=(\boldsymbol{X} \odot \boldsymbol{C}) \vee \boldsymbol{Z}
$$

with unique solution (equivalent to (2.3)) given by

$$
\boldsymbol{B}=\left(\boldsymbol{I}_{d} \vee \boldsymbol{C}\right)^{\odot(d-1)}=\bigvee_{k=0}^{d-1} \boldsymbol{C}^{\odot k}, \quad \boldsymbol{X}=\boldsymbol{Z} \odot \boldsymbol{B}
$$

where $\boldsymbol{B}$ is the Kleene star matrix and $\boldsymbol{A}^{\odot 0}=\boldsymbol{I}_{d}$ and $\boldsymbol{A}^{\odot k}=\boldsymbol{A}^{\odot(k-1)} \odot \boldsymbol{A}$ for $\boldsymbol{A} \in \overline{\mathbb{R}}_{+}^{d \times d}$ and $k \in \mathbb{N}$; see Proposition 1.6.15 of [6] as well as Theorem 2.4 and Corollary 2.5 of [14]. For more information on the max-times (tropical) algebra in ML models, see Section 2.2 in [1].

We have seen that a recursive ML vector $\boldsymbol{X}$ has two representations, one in terms of parental nodes $X_{j}$ and edge weights $c_{j i}$ and another in terms of innovations $Z_{j}$ and ML coefficients $b_{j i}$. However, while the ML coefficient matrix $\boldsymbol{B}$ of $\boldsymbol{X}$ is identifiable from the distribution of $\boldsymbol{X}$, the edge weight matrix $\boldsymbol{C}$ is generally not, see Theorem 5.4(b) in [14]. Theorem 5.3 in that paper and Theorem 2 in [15] show that an edge with edge weight $c_{j i}$ is identifiable from $\boldsymbol{B}$ if and only if it is the unique path from $j$ to $i$ with $d_{j i}(p)=b_{j i}$.

For a recursive ML vector $\boldsymbol{X}$ on a DAG $\mathcal{D}=(V, E)$ and ML coefficient matrix $\boldsymbol{B}$ this result leads to the following definition.

Definition 2.1. Let $\boldsymbol{X} \in \mathbb{R}_{+}^{d}$ be a recursive $M L$ vector on the $D A G \mathcal{D}=(V, E)$ with ML coefficient matrix $\boldsymbol{B}$. We define the minimum ML DAG of $\boldsymbol{X}$ as

$$
\mathcal{D}^{B}=\left(V, E^{B}\right):=\left(V,\left\{(j, i) \in E: b_{j i}>\bigvee_{k \in \operatorname{de}(j) \cap \operatorname{pa}(i)} \frac{b_{j k} b_{k i}}{b_{k k}}\right\}\right)
$$

Moreover, it has been shown that the support of a ratio of components of a recursive ML vector $\boldsymbol{X}$ satisfies

$$
\operatorname{supp}\left(X_{i} / X_{j}\right)= \begin{cases}\left[b_{j i}, \infty\right) & \text { for } j \in \operatorname{an}(i) \\ \left[0,1 / b_{i j}\right] & \text { for } i \in \operatorname{an}(j) \\ \{1\} & \text { for } i=j \\ \mathbb{R}_{+} & \text {otherwise }\end{cases}
$$

with $\mathbb{P}\left(X_{i} / X_{j}=b_{j i}\right)>0$ for all $j \in \operatorname{an}(i)$; see Lemma 1 of [15]. Hence, for a given iid sample $\boldsymbol{X}^{1}, \ldots, \boldsymbol{X}^{n}$ from $\boldsymbol{X}$ define a minimum ratio estimator $\hat{\boldsymbol{B}}$ of $\boldsymbol{B}$ by $\hat{b}_{i j}:=\bigwedge_{k=1}^{n}\left(X_{i}^{k} / X_{j}^{k}\right)$ for $i, j \in V$. Moreover, when the DAG $\mathcal{D}$ is known, we define $\boldsymbol{B}_{0}$ by
$\boldsymbol{B}_{0}=\left(B_{0}(i, j)\right)_{d \times d}:=\left(\bigwedge_{k=1}^{n} \frac{X_{j}^{k}}{X_{i}^{k}} \mathbf{1}_{\mathrm{pa}(j)}(i)\right)_{d \times d} \quad$ and set $\quad \hat{\boldsymbol{B}}=\left(\boldsymbol{I}_{d} \vee \boldsymbol{B}_{0}\right)^{\otimes(d-1)}$.
Theorem 4 of [15] ensures that $\hat{\boldsymbol{B}}$ is a generalized maximum likelihood estimate (GMLE) in the sense of [22].

# 2.3. Minimum domain of attraction and regular variation 

Introducing propagating noise into the recursive ML model will smooth out the atoms in (2.7). The minimum ratio estimators will still estimate the left endpoints $\boldsymbol{B}=\left(b_{j i}\right)$ and we will be able to provide distributional limit results. These will be based on minimum domain of attraction results and regular variation. Extreme value theory is more focused nowadays on running maximima (e.g. [11]), but results for running minima are obtained by noting that $\bigwedge_{i=1}^{n} Y_{i}=-\bigvee_{i=1}^{n}\left(-Y_{i}\right)$. From this we obtain that the family of Weibull distributions are limit distributions of running minima of i.i.d. random variables, see equation (2.9).
Definition 2.2. A positive random variable $\Psi_{\alpha}$ is Weibull distributed with left endpoint $x_{L}>-\infty$, shape $\alpha>0$ and scale $s>0$ and we write $Y \sim$ Weibull $\left(\alpha, x_{L}, s\right)$ if the distribution function of $Y$ is given by

$$
\Psi_{\alpha, x_{L}, s}(x)=1-\exp \left(-\left(\frac{x-x_{L}}{s}\right)^{\alpha}\right), \quad x \geq x_{L}
$$

Random variables, whose running minima have such a Weibull limit satisfy certain conditions. Here the following definition is essential and we refer to [4] for details.

Definition 2.3. Let $Y$ be a random variable with distribution function $F$ and left endpoint $x_{L}$. Then we call $Y$ or $F$ regularly varying at $x_{L}$ with exponent $\alpha>0$, if

$$
\lim _{t \downarrow 0} \frac{F\left(x_{L}+t x\right)}{F\left(x_{L}+t\right)}=x^{\alpha}, \quad x>0
$$

We abbreviate this by $Y \in R V_{\alpha}^{x_{L}}$ or $F \in R V_{\alpha}^{x_{L}}$, respectively. We also note that $Y \in R V_{\alpha}^{x_{L}}$ is equivalent to $Y-x_{L} \in R V_{\alpha}^{0}$.

Then, adapting Theorem 3.3.12 of [11] to the minimum of i.i.d. random variables $X_{1}, \ldots, X_{d}$ with distribution function $F$, we obtain

$$
\begin{aligned}
& \exists\left(a_{n}>0\right) \text { s.t. } \frac{1}{a_{n}}\left(\bigwedge_{i=1}^{n} X_{i}-x_{L}\right) \xrightarrow{d} \Psi_{\alpha}, n \rightarrow \infty \\
\Longleftrightarrow & x_{L}>-\infty, F\left(x_{L}+\cdot\right) \in R V_{\alpha}^{0}
\end{aligned}
$$

Let $\varepsilon$ be a random variable with left endpoint $x_{L}=1$, and $\tilde{\varepsilon}:=\ln (\varepsilon)$. Then for $x>0$,

$$
\begin{aligned}
\lim _{t \downarrow 0} \frac{P(\ln (\varepsilon) \leq t x)}{P(\ln (\varepsilon) \leq t)} & =\lim _{t \downarrow 0} \frac{P\left(\varepsilon \leq e^{t x}\right)}{P\left(\varepsilon \leq e^{t}\right)}=\lim _{t \downarrow 0} \frac{P(\varepsilon-1 \leq t x(1+o(1))}{P(\varepsilon-1 \leq t(1+o(1))} \\
& =\lim _{t \downarrow 0} \frac{P(\varepsilon-1 \leq t x)}{P(\varepsilon-1 \leq t)}
\end{aligned}
$$

such that $\varepsilon \in R V_{\alpha}^{1}$ if and only if $\tilde{\varepsilon} \in R V_{\alpha}^{0}$. Two relevant families of distribution functions are given in the next example.

Example 2.4. (a) [Weibull distribution] Let $\tilde{\varepsilon}$ have distribution function as in Definition 2.2 with $x_{L}=0$. Then by a l'Hospital argument,

$$
\lim _{t \downarrow 0} \frac{\Psi_{\alpha, s}(t x)}{\Psi_{\alpha, s}(t)}=x^{\alpha}
$$

which implies that $\tilde{\varepsilon} \in R V_{\alpha}^{0}$ and $\varepsilon \in R V_{\alpha}^{1}$.
(b) [Gamma distribution] Let $\tilde{\varepsilon}$ have density $g(x)=\lambda^{\alpha} e^{-\lambda x} x^{\alpha-1} / \Gamma(\alpha)$ for $x>0$ and parameters $\lambda>0, \alpha>0$. Then by a l'Hospital argument,

$$
\lim _{t \downarrow 0} \frac{G(t x)}{G(t)}=\lim _{t \downarrow 0} \frac{e^{-\lambda t x} t^{\alpha-1} x^{\alpha}}{e^{-\lambda t} t^{\alpha-1}}=x^{\alpha}, \quad x>0
$$

which implies that $\tilde{\varepsilon} \in R V_{\alpha}^{0}$ and $\varepsilon \in R V_{\alpha}^{1}$.
We provide here also some preliminary results.
Proposition 2.5 (Karamata's Tauberian Theorem 1.7.1, [4]). Let $U$ be a nondecreasing function on $\mathbb{R}$ with $U(x)=0$ for all $x<0$, and Laplace-Stieltjes transform $\hat{U}(s)=\int_{[0, \infty)} e^{-s x}$

$d U(x)<\infty$ for all large $s$. For $l \in R V_{0}^{\infty}$ and $c \geq 0, \rho \geq 0$, the following are equivalent

$$
\begin{array}{ll}
U(x) \sim c x^{\rho} l(1 / x) / \Gamma(1+p), & x \downarrow 0 \\
\dot{U}(s) \sim c s^{-\rho} l(s), & s \rightarrow \infty
\end{array}
$$

From this, we obtain the following corollary.
Corollary 2.6. a) Let $X \in R V_{\alpha_{1}}^{0}, Y \in R V_{\alpha_{2}}^{0}$ be independent, then $X+Y \in$ $R V_{\alpha_{1}+\alpha_{2}}^{0}$,
b) Let $X, Y \geq 1$ be independent and such that $\tilde{X}=\ln (X) \in R V_{\alpha_{1}}^{0}, \tilde{Y}=$ $\ln (Y) \in R V_{\alpha_{2}}^{0}$. Then $(X Y-1) \in R V_{\alpha_{1}+\alpha_{2}}^{0}$.

Proof of Corollary 2.6 (a) We use Proposition 2.5 a) for $U$ being $F_{X}$ or $F_{Y}$, the distribution function of $X$ or $Y$, respectively. Since the Laplace-Stieltjes transforms $\hat{F}_{X}(s)=\int_{[0, \infty)} e^{-s x} d F_{X}(x) \leq 1$ and $\hat{F}_{Y}(s)=\int_{[0, \infty)} e^{-s x} d F_{Y}(x) \leq 1$ for all $s \geq 0$, by Proposition 2.5, they are both regularly varying at $\infty$ in the sense of (2.11); i.e., $\hat{F}_{X} \in R V_{\alpha_{1}}^{\infty}, \hat{F}_{Y} \in R V_{\alpha_{2}}^{\infty}$. By independence, the convolution theorem for Laplace-Stieltjes transforms gives $\hat{F}_{X+Y}(s)=\hat{F}_{X}(s) \hat{F}_{Y}(s)$ and, therefore, $\hat{F}_{X+Y} \in R V_{\alpha_{1}+\alpha_{2}}^{\infty}$. Applying again Proposition 2.5 we find that $X_{1}+$ $X_{2} \in R V_{\alpha_{1}+\alpha_{2}}^{0}$.
(b) This follows from a Taylor expansion.

# 3. Recursive ML model with propagating noise 

In this section we define the recursive ML model with propagating noise, present structural results, investigate which properties of the non-noisy model prevail, and derive distributional results for component ratios of the model in preparation for the structure learning results to follow.

### 3.1. Definitions and representations

Definition 3.1. A vector $\boldsymbol{U} \in \mathbb{R}_{+}^{d}$ is a recursive ML vector with propagating noise on a $D A G \mathcal{D}=(V, E)$, if

$$
U_{i}:=\left(\bigvee_{k \in \mathrm{pa}(i)} c_{k i} U_{k} \vee Z_{i}\right) \varepsilon_{i}, \quad i \in 1, \ldots, d
$$

with edge weight matrix $\boldsymbol{C}:=\left(c_{i j} \mathbf{1}_{\mathrm{pa}(j)}(i)\right)_{d \times d}$. The noise variables $\varepsilon_{1}, \ldots, \varepsilon_{d}$ are iid and atom-free random variables with $\varepsilon_{i} \geq 1$ and unbounded above for all $i \in$ $V$, and independent of the innovations vector $\boldsymbol{Z}:=\left(Z_{1}, \ldots, Z_{d}\right)$. For simplicity, we denote by $\varepsilon$ a generic noise variable and by $Z$ a generic innovation.

Although the noise variables act on the observations, formally we can view them as random scalings of edge weights. More precisely, for a path $p=|j=$

$\left.k_{0} \rightarrow k_{1} \rightarrow \ldots \rightarrow k_{n}=i\right]$ from $j$ to $i$ we define the random path weight $\bar{d}_{j i}$ similarly to the definition of $d_{j i}$ in (2.2) as

$$
\bar{d}_{j i}(p):=\varepsilon_{j} \prod_{l=0}^{n-1} c_{k_{l} k_{l+1}} \varepsilon_{k_{l+1}}=d_{j i}(p) \varepsilon_{j} \prod_{l=0}^{n-1} \varepsilon_{k_{l+1}}
$$

If we define the random edge weight matrix

$$
\bar{\boldsymbol{C}}=\left(\bar{c}_{i j}\right)_{d \times d}:=\left(c_{i j} \varepsilon_{j} \mathbf{1}_{\mathrm{pa}(j)}(i)\right)_{d \times d}
$$

we can rewrite (3.2) as

$$
\bar{d}_{j i}(p):=\varepsilon_{j} \prod_{l=0}^{n-1} \bar{c}_{k_{l} k_{l+1}}
$$

for every path $p=\left[j=k_{0} \rightarrow k_{1} \rightarrow \ldots \rightarrow k_{n}=i\right]$ from $j$ to $i$. Hence, we can view the noise variables as random scalings for the edge weights $c_{j i}$. Since $\varepsilon \geq 1$, the edge weights $c_{j i}$ of the non-noisy model are lower bounds for the random edge-weights $\bar{c}_{j i}$ of the propagating noise model.

Again denoting the set of all paths from $j$ to $i$ by $P_{j i}$, we define the random ML coefficient matrix $\overline{\boldsymbol{B}}=\left(\bar{b}_{i j}\right)_{d \times d}$ of $\boldsymbol{U}$ with entries
$\bar{b}_{j i}:=\bigvee_{p \in P_{j i}} \bar{d}_{j i}(p) \quad$ for $j \in \operatorname{an}(i), \quad \bar{b}_{j j}=\varepsilon_{j}, \quad$ and $\quad \bar{b}_{j i}=0 \quad$ for $j \in V \backslash \operatorname{An}(i)$.

We next show that there exists a solution of (3.1) in terms of the ancestral innovations $\boldsymbol{Z}$ and $\overline{\boldsymbol{B}}$. All proofs of this section are postponed to Appendix A.

Theorem 3.2. Let $\boldsymbol{U} \in \mathbb{R}_{+}^{d}$ be a recursive $M L$ vector with propagating noise on a $D A G \mathcal{D}$ as in (3.1). Define $\left(\boldsymbol{E}_{d}\right)_{d \times d}$ as the diagonal matrix given by

$$
E_{d}(i, i)=\varepsilon_{i} \quad \text { for } i \in V \quad \text { and } \quad E_{d}(i, j)=0 \quad \text { for } i, j \in V \text { and } i \neq j
$$

We rewrite (3.1) in matrix form by means of the matrix multiplication (2.4) as

$$
\boldsymbol{U}=(\boldsymbol{U} \odot \boldsymbol{C} \vee \boldsymbol{Z}) \odot \boldsymbol{E}_{d}
$$

Then $\boldsymbol{U}$ has a unique solution in terms of the tropical matrix multiplication with random matrix $\overline{\boldsymbol{B}}$ given by

$$
\overline{\boldsymbol{B}}=\boldsymbol{E}_{d} \odot\left(\boldsymbol{I}_{d} \vee \overline{\boldsymbol{C}}\right)^{\odot(d-1)}, \quad \boldsymbol{U}=\boldsymbol{Z} \odot \overline{\boldsymbol{B}}
$$

with $\overline{\boldsymbol{C}}$ as defined in (3.3).
Since $\bar{b}_{j i}=0$ whenever $j \notin \operatorname{An}(i)$, the representation (3.5) can be rewritten as follows.

Corollary 3.3. Let $\boldsymbol{U}$ be as in Theorem 3.2 and $\bar{b}_{j i}$ be the random ML coefficients defined in (3.4). Then (3.5) is equivalent to

$$
U_{i}=\bigvee_{j \in \operatorname{An}(i)} \bar{b}_{j i} Z_{j}, \quad i \in 1, \ldots, d
$$

Note that the definition in (3.1) is equivalent to

$$
U_{i}=\tilde{U}_{i} \varepsilon_{i} \quad \text { with } \quad \tilde{U}_{i}:=\bigvee_{k \in \operatorname{pa}(i)} c_{k i} U_{k} \vee Z_{i}, \quad i \in 1, \ldots, d
$$

Since $\boldsymbol{B}$ is idempotent, the solution of $\boldsymbol{X}$ as in (2.6) can also be written as $\boldsymbol{X}=\boldsymbol{X} \odot \boldsymbol{B}$. This is no longer the case for the solution $\boldsymbol{U}$ in (3.5). However, from the above result we can compute the following representation, which is used in Definition 3.5(e) below.
Corollary 3.4. Let $\boldsymbol{U}$ and $\bar{b}_{j i}$ be as in Corollary 3.3. Then (3.6) is equivalent to

$$
U_{i}=\bigvee_{j \in \operatorname{An}(i)} \bar{b}_{j i} \tilde{U}_{j}, \quad i=1, \ldots, d
$$

with $\tilde{U}_{j}$ as in (3.7).

# 3.2. Paths classification and graph reduction in the noisy model 

We define critical and generic paths which play an essential role for the distributional properties of the model. Similarly as shown for the non-noisy model in Section 5 of [14], the vector $\boldsymbol{U}$ may also be a recursive ML model on a subgraph of $\mathcal{D}$. This subgraph depends on the ML coefficients, which are now random. Hence, we start by comparing the ML coefficient matrices $\boldsymbol{B}$ and $\overline{\boldsymbol{B}}$ of the non-noisy and noisy models.
Definition 3.5. Let $\mathcal{D}$ be a $D A G$ with edge weight matrix $\boldsymbol{C}$ and let $\boldsymbol{B}$ be the corresponding ML coefficient matrix (i.e., the Kleene star of $\boldsymbol{C}$ ). Let $p$ be a path from $j$ to $i$ with node set $S_{p}$.
(a) $p$ is called a (non-random) critical path if $d_{j i}(p)=b_{j i}$.
(b) $p$ is called a generic path if it is the only path satisfying $d_{j i}(p)=b_{j i}$.
(c) We call $\boldsymbol{C}$ generic, if two nodes are connected by at most one critical path.
(d) For a fixed $\omega \in \Omega$, we call $p$ a random critical path if $\bar{d}_{j i}(p)=\bar{b}_{j i}$.
(e) $p$ is called a possible critical path realization, if $U_{i}=U_{j} d_{j i}(p) \prod_{k \in S_{p}} \varepsilon_{k}=$ $\tilde{U}_{j} \bar{d}_{j i}(p)$ happens with positive probability.
Remark 3.6. We have defined a non-random critical path and a random critical path. We want to emphasize, however, that while the first path property is simply inherited from $\boldsymbol{C}$ via $\boldsymbol{B}$, the second one is inherited from $\boldsymbol{C}$ and the noise variables. We also note that by continuity of the innovations and the noise variables, any random critical path between a pair of nodes must be a.s. unique, although it may vary with the realizations of the noise variables.

We explain the model and the notions of Definition 3.5 in an example.
Example 3.7. Consider the DAG:
![img-0.jpeg](img-0.jpeg)

Then, $\boldsymbol{C}$ is generic if and only if $c_{13} \neq c_{12} c_{23}$. Moreover, we have

$$
U_{3}=\left(\bar{c}_{13} \vee \bar{c}_{12} \bar{c}_{23}\right) \varepsilon_{1} Z_{1} \vee \bar{c}_{23} \varepsilon_{2} Z_{2} \vee \varepsilon_{3} Z_{3}
$$

with $\bar{c}_{j i}=c_{j i} \varepsilon_{i}$ as defined in (3.3).
Now assume that $c_{13}>c_{12} c_{23}$. In that case, $[1 \rightarrow 3]$ is the critical path, while the path $[1 \rightarrow 2 \rightarrow 3]$ is not critical. However, $\mathbb{P}\left(\bar{c}_{13}<\bar{c}_{12} \bar{c}_{23}\right)=\mathbb{P}\left(\varepsilon_{2}>\right.$ $\left.c_{13} /\left(c_{12} c_{23}\right)\right)>0$. If $\mathbb{P}\left(\bar{c}_{13}<\bar{c}_{12} \bar{c}_{23}\right)$, then the edge $1 \rightarrow 3$ is random critical, otherwise $1 \rightarrow 2 \rightarrow 3$ is random critical. Since both paths can be random critical with positive probability, all paths in $\mathcal{D}$ can be possible critical path realizations.

In contrast, if $c_{13}<c_{12} c_{23}$ we have $\mathbb{P}\left(\bar{c}_{13}>\bar{c}_{12} \bar{c}_{23}\right)=\mathbb{P}\left(\varepsilon_{2}<c_{13} /\left(c_{12} c_{23}\right)\right)=$ 0 . In this case, the path $[1 \rightarrow 3]$ can be random critical only on a null set and therefore $[1 \rightarrow 3]$ is not a possible critical path realization.

This illustrates that a path $p$ from $j$ to $i$ with path weight $d_{j i}(p)<b_{j i}$ may as well contribute to the distribution of $U_{i}$. However, an edge $p=[j \rightarrow i]$ with $d_{j i}(p)<b_{j i}$ is still not identifiable and does not change the distribution of $\boldsymbol{U}$.

Recall from (2.6) and (3.5) that

$$
\boldsymbol{X}=\boldsymbol{Z} \odot \boldsymbol{B} \quad \text { and } \quad \boldsymbol{U}=\boldsymbol{Z} \odot \overline{\boldsymbol{B}}
$$

We present some useful properties of $\boldsymbol{B}$ and $\overline{\boldsymbol{B}}$ providing a link between the noisy and non-noisy model as defined in (2.1) and (3.1), respectively. Such properties have been shown for $\boldsymbol{B}$ in $[13,14,15]$, and we investigate here which of them remain valid for $\overline{\boldsymbol{B}}$.
Lemma 3.8. Let $\boldsymbol{U} \in \mathbb{R}_{+}^{d}$ be a recursive ML vector with propagating noise on a $D A G \mathcal{D}$ as defined in (3.1) with $\boldsymbol{B}$ and $\overline{\boldsymbol{B}}$ defined in (2.6) and (3.5), respectively. Then the following assertions hold:
a) $\bar{b}_{j i}=\bigvee_{k \in V} \frac{\bar{b}_{j k} \bar{b}_{k i}}{\bar{b}_{k k}} \geq \bigvee_{k \in \operatorname{de}(j) \cap \operatorname{an}(i)} \frac{\bar{b}_{j k} \bar{b}_{k i}}{\bar{b}_{k k}}$, where the inequality is strict, whenever the random critical path from $j$ to $i$ is the edge $j \rightarrow i$, or $j=i$.
b) There exists some path $p:=[j \rightarrow \ldots \rightarrow k \rightarrow \ldots \rightarrow i]$ from $j$ to $i$ that passes through $k$ such that

$$
\bar{d}_{j i}(p)=\bar{b}_{j i} \quad \text { if and only if } \quad \bar{b}_{j i}=\frac{\bar{b}_{j k} \bar{b}_{k i}}{\bar{b}_{k k}}
$$

c) $\frac{U_{i}}{U_{j}} \geq \frac{\bar{b}_{j i}}{\bar{b}_{j j}} \geq b_{j i} \quad$ with $b_{j i}=0$ for $j \notin \operatorname{An}(i)$

d) $\operatorname{supp}\left(U_{i} / U_{j}\right)= \begin{cases}\left[b_{j i}, \infty\right) & \text { for } j \in \operatorname{an}(i), \\ {\left[0,1 / b_{i j}\right]} & \text { for } i \in \operatorname{an}(j), \\ \{1\} & \text { for } i=j, \\ \mathbb{R}_{+} & \text {otherwise. }\end{cases}$

Moreover, for $j \neq i$, neither the distribution of $U_{i} / U_{j}$ nor the distribution of $U_{j} / U_{i}$ have any atoms.
e) If $b_{j i}=\bigvee_{k \in \operatorname{de}(j) \cap \operatorname{an}(i)} \frac{\bar{b}_{j k} b_{k i}}{b_{k k}}$, then $\bar{b}_{j i}=\bigvee_{k \in \operatorname{de}(j) \cap \operatorname{an}(i)} \frac{\bar{b}_{j k} \bar{b}_{k i}}{\bar{b}_{k k}}$.
f) If $b_{j i}>\bigvee_{k \in \operatorname{de}(j) \cap \operatorname{an}(i)} \frac{\bar{b}_{j k} \bar{b}_{k i}}{b_{k k}}$ and $\operatorname{de}(j) \cap \operatorname{an}(i) \neq \emptyset$, then

$$
\mathbb{P}\left(\bar{b}_{j i}>\bigvee_{k \in \operatorname{de}(j) \cap \operatorname{an}(i)} \frac{\bar{b}_{j k} \bar{b}_{k i}}{\bar{b}_{k k}}\right)>0 \quad \text { and } \quad \mathbb{P}\left(\bar{b}_{j i}=\bigvee_{k \in \operatorname{de}(j) \cap \operatorname{an}(i)} \frac{\bar{b}_{j k} \bar{b}_{k i}}{\bar{b}_{k k}}\right)>0
$$

Definition 5.1 of [14] presents the smallest subgraph of $\mathcal{D}$ such that $\boldsymbol{X}$ is a recursive ML model on this DAG as

$$
\mathcal{D}^{B}=(V, E):=\left(V,\left\{(j, i) \in E: b_{j i}>\bigvee_{k \in \operatorname{de}(j) \cap \operatorname{pa}(i)} \frac{b_{j k} b_{k i}}{b_{k k}}\right\}\right)
$$

This means that $\mathcal{D}^{B}$ contains an edge $j \rightarrow i$ of $\mathcal{D}$ if and only if this edge is the only critical path from $j \rightarrow i$ in $\mathcal{D}$.

Lemma 3.8 b) and f) motivate the following definition as the random analog of $\mathcal{D}^{B}$.

Definition 3.9. Let $\boldsymbol{U} \in \mathbb{R}_{+}^{d}$ be a recursive ML vector with propagating noise on the $D A G \mathcal{D}=(V, E)$ as defined in (3.1). Then we define the minimum ML DAG $\overline{\mathcal{D}}^{B}$ as

$$
\overline{\mathcal{D}}^{B}=(V, \bar{E}):=\left(V,\left\{(j, i) \in E: \mathbb{P}\left(\bar{b}_{j i}>\bigvee_{k \in \operatorname{de}(j) \cap \operatorname{pa}(i)} \frac{\bar{b}_{j k} \bar{b}_{k i}}{\bar{b}_{k k}}\right)>0\right\}\right)
$$

This means that $\overline{\mathcal{D}}^{B}$ contains an edge $j \rightarrow i$ of $\mathcal{D}$ if and only if this edge is a possible critical path realization from $j \rightarrow i$ in $\mathcal{D}$.

In addition, applying first Lemma 3.8 e) and f), and in the second part Lemma 3.8 b) yields the following result.

Corollary 3.10. Let $\boldsymbol{X} \in \mathbb{R}_{+}^{d}$ be a recursive ML vector on a $D A G \mathcal{D}=(V, E)$ as defined in (2.1) and $\boldsymbol{U} \in \mathbb{R}_{+}^{d}$ be a recursive ML vector with propagating noise as defined in (3.1) on the same $D A G \mathcal{D}$ with the same edge weight matrix $\boldsymbol{C}$. Then

$$
\mathcal{D}^{B}=\overline{\mathcal{D}}^{B}
$$

which is the smallest $D A G$ that preserves the distributions of $\boldsymbol{X}$ and of $\boldsymbol{U}$.

We will henceforth only use the term $\mathcal{D}^{B}$.
The next lemma summarizes properties of possible critical path realizations from Definition 3.5(e).

Lemma 3.11. Let $\boldsymbol{U} \in \mathbb{R}_{+}^{d}$ be a recursive $M L$ vector with propagating noise on a $D A G \mathcal{D}$ as defined in (3.1). Then the following assertions hold:
a) A path $p=\left[j=k_{0} \rightarrow \ldots \rightarrow k_{n}=i\right]$ in $\mathcal{D}$ is a possible critical path realization from $j$ to $i$ if and only if all edges of $p$ belong to the minimum $M L D A G \mathcal{D}^{B}$.
b) Let $p_{1}$ and $p_{2}$ be two possible critical path realizations from $j$ to $i$ and from $l$ to $m$, respectively. Then

$$
\left\{U_{i}=U_{j} d_{j i}\left(p_{1}\right) \prod_{k \in S_{p_{1}}} \varepsilon_{k}, U_{m}=U_{l} d_{l m}\left(p_{2}\right) \prod_{k \in S_{p_{2}}} \varepsilon_{k}\right\}
$$

has positive probability if and only if $S_{p_{1}} \cap S_{p_{2}}=\emptyset$, or for every $r \in$ $S_{p_{1}} \cap S_{p_{2}}$ the sub-path of $p_{1}$ from $j$ to $r$ is a sub-path of $p_{2}$ or the sub-path of $p_{2}$ from $l$ to $r$ is a sub-path of $p_{1}$.

We illustrate part b) with Figure 1 and Figure 2.
![img-1.jpeg](img-1.jpeg)

FIG 1. Both dashed paths $p_{1}:=\left[j \rightarrow k_{5} \rightarrow k_{6} \rightarrow i\right]$ and $p_{2}:=\left[l \rightarrow k_{4} \rightarrow j \rightarrow k_{5} \rightarrow k_{6} \rightarrow m\right]$ can be possible critical path realizations from the same realized noise variables along the nodes.

# 3.3. Distributions of component ratios of the noisy model 

The next result is important as it not only helps us to understand the model better, but is also an important step for learning the model.

Theorem 3.12. Let $\boldsymbol{U} \in \mathbb{R}_{+}^{d}$ be a recursive ML vector with propagating noise on a $D A G \mathcal{D}$ as defined in (3.1). Suppose that $p_{\max }:=\left[j=k_{0} \rightarrow \cdots \rightarrow k_{n}=i\right]$

is generic. Let $S_{p_{\max }}=\left\{k_{1}, \ldots, k_{n}\right\}$ be the set of nodes on $p_{\max }$. Then

$$
\begin{aligned}
& \mathbb{P}\left(\frac{U_{i}}{U_{j}} \leq b_{j i} x\right) \\
\sim & \mathbb{P}\left(\prod_{k \in S_{p_{\max }}} \varepsilon_{k} \leq x, \frac{U_{i}}{U_{j}}=b_{j i} \prod_{k \in S_{p_{\max }}} \varepsilon_{k}\right) \sim c \mathbb{P}\left(\prod_{k \in S_{p_{\max }}} \varepsilon_{k} \leq x\right), \quad x \downarrow 1
\end{aligned}
$$

for some constant $c \in(0,1)$.
Remark 3.13. If the distributions of the noise variables and the innovations as well as the path weights of the underlying $D A G \mathcal{D}$ are given, the constant $c$ in Theorem 3.12 can be calculated explicitly.
![img-2.jpeg](img-2.jpeg)

FIG 2. Both dashed paths $p_{1}:=\left[j \rightarrow k_{5} \rightarrow k_{6} \rightarrow i\right]$ and $p_{2}:=\left[l \rightarrow k_{5} \rightarrow k_{6} \rightarrow m\right]$ can only on a null-set be possible critical path realizations from the same realized noise variables along the nodes.

Theorem 3.12 also shows that, while a path $p$ from $j$ to $i$ with $d_{j i}(p)<b_{j i}$ can contribute to the distribution of $\boldsymbol{U}$ (as we have seen in Example 3.7), they influence the distribution of $U_{i} / U_{j}$ at their left limit of support only by the constant $c \in(0,1)$.

We now extend the result to situations with several critical paths.
Corollary 3.14. Let $\boldsymbol{U}$ be as in Theorem 3.12. Suppose that exactly the paths $p_{1}, \ldots, p_{n}$ from $j$ to $i$ are critical; i.e., $d_{j i}\left(p_{1}\right)=\ldots=d_{j i}\left(p_{n}\right)=b_{j i}$. Then

$$
\mathbb{P}\left(\frac{U_{i}}{U_{j}} \leq b_{j i} x\right) \sim c \mathbb{P}\left(\bigcap_{p \in\left\{p_{1}, \ldots, p_{n}\right\}}\left\{\prod_{k \in S_{p}} \varepsilon_{k} \leq x\right\}\right), \quad x \downarrow 1
$$

for some constant $c \in(0,1)$.
For simplicity, we assume from now on that $\boldsymbol{C}$ is generic in the sense of Definition 3.5. However, we want to remark that all such results can be extended to the case of several non-random critical paths between two nodes. The proofs of such results work similarly as the proof of Corollary 3.14.

We continue with another consequence of Theorem 3.12.

Corollary 3.15. Let $\boldsymbol{U}$ be as in Theorem 3.12 and suppose that $p:=\left[j=k_{0} \rightarrow\right.$ $\left.\cdots \rightarrow k_{n}=i\right]$ is generic. Let $\boldsymbol{U}^{1}, \ldots, \boldsymbol{U}^{n}$ for $n \in \mathbb{N}$ be an iid sample from $\boldsymbol{U}$. Then, for the same constant $c \in(0,1)$ as in Theorem 3.12, we have

$$
\mathbb{P}\left(\bigwedge_{k=0}^{n} \frac{U_{i}^{k}}{U_{j}^{k}} \leq b_{j i} x\right) \sim c n \mathbb{P}\left(\prod_{i=1}^{n} \varepsilon_{k_{i}} \leq x\right), \quad x \downarrow 1
$$

We conclude this section by extending Theorem 3.12 to multivariate distributions, which is an important structural result of the new model. We only formulate and prove the bivariate case, the general case is then obvious. Recall that in Lemma 3.11 we gave a necessary and sufficient condition for (3.10) below.

Theorem 3.16. Let $\boldsymbol{U} \in \mathbb{R}_{+}^{d}$ be a recursive $M L$ vector with propagating noise on a $D A G \mathcal{D}$ as defined in (3.1). Suppose generic paths $p_{1}$ from $j$ to $i$ and $p_{2}$ from $l$ to $m$. Assume that

$$
\mathbb{P}\left(U_{i}=U_{j} b_{j i} \prod_{k \in S_{p_{1}}} \varepsilon_{k}, U_{m}=U_{l} b_{l m} \prod_{k \in S_{p_{2}}} \varepsilon_{k}\right)>0
$$

Then

$$
\begin{aligned}
& \mathbb{P}\left(\frac{U_{i}}{U_{j}} \leq b_{j i} x_{1}, \frac{U_{m}}{U_{l}} \leq b_{l m} x_{2}\right) \sim c \mathbb{P}\left(\prod_{k \in S_{p_{1}}} \varepsilon_{k} \leq x_{1}, \prod_{k \in S_{p_{2}}} \varepsilon_{k} \leq x_{2}\right) \\
\sim & \mathbb{P}\left(\prod_{k \in S_{p_{1}}} \varepsilon_{k} \leq x_{1}, \prod_{k \in S_{p_{2}}} \varepsilon_{k} \leq x_{2}, \frac{U_{i}}{U_{j}}=b_{j i} \prod_{k \in S_{p_{1}}} \varepsilon_{k}, \frac{U_{m}}{U_{l}}=b_{l m} \prod_{k \in S_{p_{2}}} \varepsilon_{k}\right)
\end{aligned}
$$

for $x_{1}, x_{2} \downarrow 1$ and some constant $c \in(0,1)$.

# 4. Identification and estimation 

We first address the question of identifiability of $\boldsymbol{B}$ from the distribution of $\boldsymbol{U}$. In particular, we are going to show that even though innovations and noise variables are generally not identifiable, $\boldsymbol{B}$ remains identifiable also in the propagating noise model.

We discuss three settings (1)-(3) below. For each setting, we propose an appropriate minimum ratio estimator for $\boldsymbol{B}$. Afterwards, we will show the almost sure convergence of each of the estimators.

### 4.1. Identifiability of the model

In this section we discuss the question of identifiability of the DAG $\mathcal{D}$ and the edge weights $\boldsymbol{C}$ of a ML model with recursive noise from the distribution of $\boldsymbol{U}$. As we have already seen in Example 3.7, the true DAG $\mathcal{D}$ and the edge weight matrix $\boldsymbol{C}$ underlying $\boldsymbol{U}$ in representation (3.1) are generally not identifiable

from the distribution of $\boldsymbol{U}$. The smallest DAG with a chance to be identified from the distribution of $\boldsymbol{U}$ is the minimum ML DAG $\overline{\mathcal{D}}^{B}$ of Definition 3.9, which in turn can be identified from $\boldsymbol{B}$ by Corollary 3.10.

By the equivalence of $\mathcal{D}^{B}$ and $\overline{\mathcal{D}}^{B}$, Theorem 2 in [15] also holds for the propagating noise model defined in (3.1), i.e., the theorem defines the class of DAGs that preserve the distribution of $\boldsymbol{U}$. As by Lemma 3.8 d) the ML coefficients are limits of supports of component ratios of $\boldsymbol{U}$, the following is immediate.

Corollary 4.1. Let $\boldsymbol{U} \in \mathbb{R}_{+}^{d}$ be a recursive ML model with propagating noise on a DAG $\mathcal{D}$ as defined in (3.1). Then the ML coefficient matrix $\boldsymbol{B}$ is identifiable from the distribution of $\boldsymbol{U}$.

Since we can identify $\boldsymbol{B}$ from the distribution of $\boldsymbol{U}$, we can also identify the minimum ML DAG $\mathcal{D}^{B}$ from Definition 2.1 (which by Definition 3.9 and Corollary 3.10 is the minimum DAG preserving the distribution of $\boldsymbol{U}$ ). Therefore, since $\varepsilon \geq 1$, Theorem 2 of [15] also holds for the propagating noise model as defined in (3.1). Therefore, as exemplified in Example 3.7, we can identify the class of all DAGs and edge weights that could have generated $\boldsymbol{U}$.

However, unlike for the non-noisy model, we can generally not identify innovations or noise variables. To see this assume a source node $U_{i}$ in a DAG $\mathcal{D}$ such that an $(i)=\emptyset$. If $\boldsymbol{U}$ follows a recursive ML model with propagating noise, then $U_{i}:=Z_{i} \varepsilon_{i}$. In particular, we can not identify $Z_{i}$ or $\varepsilon_{i}$.

When estimating a recursive ML model with propagating noise, we distinguish between three settings. We point out that all algorithms below work equally, if the data is generated from a noise-free max-linear model as defined in (2.1).
(1) All ancestral relations are known; i.e., we know the set of edges $E$, hence the DAG. This might be the case when modeling networks that contain natural information about edges. The problem then reduces to finding appropriate estimates $\hat{b}_{j i}$ for $j \in \operatorname{an}(i)$.
(2) The ancestral relations are unknown; however, we know a topological order of the nodes. Then, in contrast to setting 1 , we need to decide if a path from $j$ to $i$ with $j<i$ exists.
(3) Neither the underlying DAG nor a topological order of the nodes is known. Then we need to find a topological order of the nodes and proceed then as in setting 2 .

We next want to estimate $\boldsymbol{B}$ for each of the three settings (1)-(3).

# 4.2. Known DAG structure with unknown edge weights 

Given an iid sample $\boldsymbol{U}^{1}, \ldots, \boldsymbol{U}^{n}$ from a recursive ML model with propagating noise on a known DAG $\mathcal{D}$ as defined in (3.1) and knowing all ancestral relations

of $\mathcal{D}$, we could choose the simple estimate

$$
\hat{\boldsymbol{B}}:=(\bar{b}_{i j})_{d \times d}=\left(\bigwedge_{k=1}^{n} \frac{U_{j}^{k}}{U_{i}^{k}} \mathbf{1}_{\operatorname{An}(j)}(i)\right)_{d \times d}
$$

However, as in the non-noisy model, the estimate (4.1) may not define any recursive ML model on the given DAG $\mathcal{D}$, cf. Example 3 of [15].

We use instead

$$
\boldsymbol{B}_{0}=\left(B_{0}(i, j)\right)_{d \times d}:=\left(\bigwedge_{k=1}^{n} \frac{U_{j}^{k}}{U_{i}^{k}} \mathbf{1}_{\operatorname{pa}(j)}(i)\right)_{d \times d} \quad \text { and set } \quad \hat{\boldsymbol{B}}=\left(\boldsymbol{I}_{d} \vee \boldsymbol{B}_{0}\right)^{\odot(d-1)}
$$

Applying Lemma 2 in [15] to $\boldsymbol{B}_{0}$, the estimator $\hat{\boldsymbol{B}}$ yields a valid estimate of the given DAG in the sense that $\hat{\boldsymbol{B}}$ defines a recursive ML model and for any pair $(j, i) \notin E(\mathcal{D})$ we have $\hat{b}_{j i}=\bigvee_{k \in\{1, \ldots, d\} \backslash\{j, i\}} \bar{b}_{j k} \bar{b}_{k i}$. Moreover, by the idempotency of $\hat{\boldsymbol{B}}$ and Lemma 3.8 c ), similarly to the non-noisy model, it also holds that

$$
b_{j i} \leq \bar{b}_{j i} \leq \bar{b}_{j i}, \quad j \in \operatorname{an}(i)
$$

# 4.3. Known topological order 

Given an iid sample $\boldsymbol{U}^{1}, \ldots, \boldsymbol{U}^{n} \in \mathbb{R}_{+}^{d}$ from a recursive ML model with propagating noise without knowing $\mathcal{D}$, but knowing the topological order of nodes, we adapt the estimator (4.1) to this situation and define

$$
\hat{\boldsymbol{B}}:=(\bar{b}_{i j})_{d \times d}=\left(\bigwedge_{k=1}^{n} \frac{U_{j}^{k}}{U_{i}^{k}} \mathbf{1}_{(i<j)}\right)_{d \times d}
$$

### 4.4. Unknown DAG and unknown topological order

Given an iid sample $\boldsymbol{U}^{1}, \ldots, \boldsymbol{U}^{n} \in \mathbb{R}_{+}^{d}$ from a recursive ML model with propagating noise without knowing $\mathcal{D}$ or the topological order, we will recover a topological order first and then proceed as in Section 4.3.

Estimating the topological order of an underlying DAG is often done by learning algorithms that successively identify source nodes and succeeding generations. For additive models, usually regression techniques are applied (see e.g. [7] or [32]). In the recursive ML model, the noise is not additive and the model is highly non-linear. Hence, such regression methods cannot be applied. However, under the condition of multivariate regular variation, the paper [23] suggests a learning algorithm for the model without noise as given in (1.1). We propose a different approach, which to the best of our knowledge has not been considered in the literature before. It applies to the propagating noise model without any

distributional assumptions on the innovations and noise variables and learns the DAG by using minimum ratios. We first consider the matrix of all minimum ratios given by

$$
\hat{\boldsymbol{B}}:=(\bar{b}_{i j})_{d \times d}=\left(\bigwedge_{k=1}^{n} \frac{U_{j}^{k}}{U_{i}^{k}}\right)_{d \times d}
$$

Let $\Pi$ denote the set of all topological orders of $V$. Furthermore, denote an equivalence class of topological orders induced by the underlying (unknown) $\operatorname{DAG} \mathcal{D}=(V, E)$ by

$$
R_{\mathcal{D}}:=\{\pi \in \Pi: \pi(j)<\pi(i) \quad \text { for all }(j, i) \in E\}
$$

By Lemma 3.8 d), $\bar{b}_{j i}$ is lower bounded by $b_{j i}$ for $j \in \operatorname{an}(i)$ and $\bar{b}_{j i} \rightarrow 0$ a.s. as $n \rightarrow \infty$ for $j \notin \operatorname{An}(i)$. This is a direct result from Lemma 3.8 c) and the fact that the minimum is non-increasing. Hence, for any $\pi \in R_{\mathcal{D}}$ it holds that $\bar{b}_{j i} \rightarrow 0$ a.s. as $n \rightarrow \infty$ whenever $\pi(j)>\pi(i)$. Therefore, also

$$
\max _{\substack{(j, i) \in V \times V: \\ \pi(j)>\pi(i)}} \bar{b}_{j i} \rightarrow 0 \quad \text { a.s. for } n \rightarrow \infty
$$

In contrast, for any $\pi \notin R_{D}$, there is a pair of nodes $(j, i)$ such that $b_{j i}>0$ although $\pi(j)>\pi(i)$. For this reason,

$$
\max _{\substack{(j, i) \in V \times V: \\ \pi(j)>\pi(i)}} \bar{b}_{j i} \rightarrow c_{\pi}>0 \quad \text { a.s. for } n \rightarrow \infty
$$

As a consequence, for a given topological order $\pi$, by (4.7) and (4.8), the maximum converges almost surely to zero if and only if $\pi \in R_{\mathcal{D}}$. Hence we propose a topological order that minimizes this expression, i.e.,

$$
\underset{\pi \in \Pi}{\operatorname{argmin}} \max _{\substack{(j, i) \in V \times V: \\ \pi(j)>\pi(i)}} \hat{b}_{j i}
$$

A topological order found by (4.9) generally is not unique. Algorithm 1 returns a unique topological order for any fixed estimated matrix $\hat{\boldsymbol{B}}$.

Proposition 4.2. Algorithm 1 solves the optimization problem in equation (4.9).
Proof. Let $\pi$ be the topological order from Algorithm 1 and denote by $S(\pi)$ the objective function in (4.9). Algorithm 1 sorts all pairs $(j, i)$ by the size of $\bar{b}_{j i}$ and draws an edge from $j$ to $i$ whenever there is no path from $i$ to $j$. Now consider the first pair $(j, i)$ in the algorithm where we do not draw an edge since $i \in \operatorname{an}(j)$. Consider a permutation $\pi^{\prime}$ that is obtained by exchanging the order of nodes $i$ and $j$ in $\pi$. Since there exists already a path from $i$ to $j$, it follows that $S(\pi) \leq S\left(\pi^{\prime}\right)$.

```
Algorithm 1 Estimating a topological order
Input: A matrix of minimum ratios \(\hat{\boldsymbol{B}}\) as in (4.5)
Output: An estimated topological order \(\hat{\pi}\)
    Set \(\hat{\mathcal{D}}=(V, E)\) with \(V=\{1, \ldots, d\}\) and \(E=\emptyset\).
    Set \(S:=\{(j, i) \in V \times V: j \neq i\}\) and sort the elements \((j, i)\) of \(S\) by the size of \(\hat{b}_{j i}\) from
        large to small.
    for \((j, i)\) in S do
        if \(i \notin \operatorname{an}(j)\) in \(\hat{\mathcal{D}}\) then
            \(E=E \cup(j, i)\)
        end if
    end for
    return the topological order \(\hat{\pi}\) of the DAG \(\hat{\mathcal{D}}\)
```

The DAG $\hat{\mathcal{D}}$ constructed in Algorithm 1 works as an auxiliary instrument to infer a topological order. Observe that $\hat{\mathcal{D}}$ is a complete DAG, with directed edges between every node pair in $V$ and, hence, there is a unique topological order representing $\hat{\mathcal{D}}$. Moreover, since we sort the weights by size, the algorithm solves (4.9) in an optimal way for given $\hat{B}$. At first sight the algorithm bears some similarity to Kruskal's classical algorithm for finding a minimum spanning tree; see [26]. However, Algorithm 1 works with directed edges and, of course, the optimization problem itself is very different.

Adding an edge and checking the presence of a path between any pair of nodes both can be implemented in $O(d)$ amortized complexity (see [18]). Hence, since $S$ as computed in line 2 of Algorithm 1 contains $d(d-1)$ pairs of nodes, we have an overall amortized complexity of $O\left(d^{3}\right)$. After Algorithm 1 we can again use the minimum ratio estimator

$$
\hat{\boldsymbol{B}}:=\left(\hat{b}_{i j}\right)_{d \times d}=\left(\bigwedge_{k=1}^{n} \frac{U_{j}^{k}}{U_{i}^{l}} \mathbf{1}_{(\hat{\pi}(i)<\hat{\pi}(j))}\right)_{d \times d}
$$

# 4.5. Strong consistence of $\hat{\boldsymbol{B}}$ and learning the minimum ML DAG $\mathcal{D}^{\boldsymbol{B}}$ 

We first want to formally state the a.s. convergence of the proposed estimators for the ML coefficient matrix $\boldsymbol{B}$. Afterwards, we discuss how to learn the minimum ML DAG $\mathcal{D}^{B}$. The proofs of Proposition 4.3 and Lemma 4.4 can be found in Appendix B.

Proposition 4.3. Let $\boldsymbol{U} \in \mathbb{R}_{+}^{d}$ be a recursive ML vector with propagating noise as defined in (3.1) and let $\boldsymbol{U}^{1}, \ldots, \boldsymbol{U}^{n} \in \mathbb{R}_{+}^{d}$ be an iid sample from $\boldsymbol{U}$. Then the estimates (4.2), (4.4) and (4.10) of $\boldsymbol{B}$ are strongly consistent, i.e., it holds a.s. for $n \rightarrow \infty$ that

$$
\hat{b}_{j i} \longrightarrow b_{j i} \quad \text { for } j \in \operatorname{an}(i), \quad \hat{b}_{i i}=1, \quad \text { and } \quad \hat{b}_{j i} \longrightarrow 0 \quad \text { for } j \in V \backslash \operatorname{An}(i)
$$

In Sections 4.2-4.4 we have been discussing how to estimate $\boldsymbol{B}$ under the settings (1)-(3). However, as we know from Corollary 3.10, only critical edges

of $\mathcal{D}$ contribute to the distribution of $\boldsymbol{U}$. Asymptotically, we can almost surely identify $\mathcal{D}^{B}$ since there is an edge $j \rightarrow i$ in $\mathcal{D}^{B}$ if and only if $b_{j i}>b_{j l} b_{l i}$ for all $l \in \operatorname{de}(j) \cap \operatorname{an}(i)$.

However, in real life we estimate the edges of $\mathcal{D}^{B}$ for a finite data set. Since $\bigwedge_{k=1}^{n}\left(U_{i}^{k} / U_{j}^{k}\right)>0$ holds for all $n \in \mathbb{N}$ and all $i, j \in V$, the estimators (4.4) or (4.10) would result in a matrix representing a complete DAG.

Since small estimated values $\hat{b}_{j i}$ may well be 0 in the true model, we use a threshold $\delta_{1}>0$ with the aim to set an estimator $\hat{b}_{j i}<\delta_{1}$ equal to 0 . However, setting single values $\hat{b}_{j i}:=0$ may destroy the idempotency of $\hat{\boldsymbol{B}}$ since idempotency requires for any triple of nodes $(j, l, i)$,

$$
\hat{b}_{j l} \hat{b}_{l i}=\bigwedge_{k=1}^{n} \frac{U_{l}^{k}}{U_{j}^{k}} \bigwedge_{k=1}^{n} \frac{U_{i}^{k}}{U_{l}^{k}} \leq \bigwedge_{k=1}^{n} \frac{U_{l}^{k}}{U_{j}^{n}} \frac{U_{i}^{k}}{U_{l}^{k}}=\hat{b}_{j i}
$$

For the estimates however, it might be possible that $\hat{b}_{j i}<\delta_{1}$, while $\hat{b}_{j l}>\delta_{1}$ and $\hat{b}_{l i}>\delta_{1}$. In this case, setting $\hat{b}_{j i}=0$ would result in $\hat{b}_{j i}<\hat{b}_{j l} \hat{b}_{l i}$ violating (4.11). To preserve the idempotency of $\hat{\boldsymbol{B}}$ while setting some small values to 0 , we propose a simple adapted thresholding algorithm.

```
Algorithm 2 Thresholding while maintaining idempotency
Input: A (known or estimated) topological order \(\pi: 1, \ldots, d\) and an idempotent estimate \(\hat{\boldsymbol{B}}\)
    as in (4.4) or (4.10) and a threshold value \(\delta_{1}>0\)
Output: An idempotent estimate \(\hat{\boldsymbol{B}}\)
    \(E:=\left\{(j, i) \in V \times V: \operatorname{sgn}\left(\hat{b}_{j i}\right)=1\right.\) and \(i \neq j\}\)
    \(\mathcal{D}:=(V, E)\)
    \(S:=\left\{(j, i) \in E: 0<\hat{b}_{j i}<\delta_{1}\right\}\)
    Sort the pairs \((j, i)\) in \(S\) by the distance \(i-j\) from low to high
    for \((j, i)\) in S do
        if \((j-i)==1\) then
            \(\hat{b}_{j i}=0\)
        end if
        if for every \(l\) with \(j<l<i: (j, l)\) or \((l, i) \in S\) then
            \(\hat{b}_{j i}=0\)
        else
            \(S=S \backslash\{(j, i)\}\)
        end if
    end for
    return \(\hat{\boldsymbol{B}}\)
```

Lemma 4.4. Algorithm 2 with threshold $\delta_{1}>0$ outputs an idempotent matrix, i.e., $\hat{\boldsymbol{B}} \odot \hat{\boldsymbol{B}}=\hat{\boldsymbol{B}}$ and there is no other idempotent matrix $\boldsymbol{B}^{\prime}$ such that $b_{j i}^{\prime}=\hat{b}_{j i}$ whenever $\hat{b}_{j i}>\delta_{1}$ that contains more zero entries than $\hat{\boldsymbol{B}}$.

Remark 4.5. If we choose $\delta_{1} \leq \min \left\{\hat{b}_{j i}: j<i\right\}$ no entry is set to 0 , and if $\delta_{1}>\max \left\{\hat{b}_{j i}: j<i\right\}$ all entries are set to 0 except for the diagonal. So in the first case, we obtain the complete $D A G$ and in the second case the $D A G$ consists of isolated nodes only.

In order to estimate the minimum ML DAG $\mathcal{D}^{B}$ it is not sufficient to decide if a path from $j$ to $i$ exists, i.e., if $b_{j i}>0$. We need in particular to decide if the edge $j \rightarrow i$ belongs to $\mathcal{D}^{B}$. By continuity of the noise variables we may observe for the estimated path weights

$$
\hat{b}_{j i}>\hat{b}_{j l} \hat{b}_{l i}
$$

even if $b_{j i}=b_{j l} b_{l i}$. However, by Proposition 4.3, in this situation the difference $\left(\hat{b}_{j i}-\hat{b}_{j l} \hat{b}_{l i}\right) \rightarrow 0$ a.s. as $n \rightarrow \infty$. Therefore, we introduce another threshold $\delta_{2}>$ 0 enforcing an edge in $\mathcal{D}^{B}$ if this difference is greater than $\delta_{2}$. In Theorem 3.12 we have seen that the distribution of the ratio $\mathbb{P}\left(U_{i} / U_{j} \leq b_{j i} x\right)$ is asymptotically determined by $\mathbb{P}\left(\prod_{k \in S_{p}} \varepsilon_{k}-1 \leq x\right)$ for $x \downarrow 0$. Hence, the rate of convergence of $\left(\hat{b}_{j i}-\hat{b}_{j l} \hat{b}_{l i}\right)$ depends crucially on the path length $m=\left|S_{p}\right|$. Ideally, we therefore choose $\delta_{2}=\delta_{2}(n, m)$ depending not only on the sample size $n$, but also on the path length $m$.

More precisely, since $F_{\sum_{k \in S_{p}} \varepsilon_{k}}^{\leftarrow}(1 / n) \sim F_{\prod_{k \in S_{p}} \varepsilon_{k}-1}^{\leftarrow}(1 / n)$ (see Theorem 5.2 and its proof below), and assuming that $\boldsymbol{C}$ is generic, we find that Algorithm 3 asymptotically identifies $\mathcal{D}^{B}$, if

$$
F_{\sum_{k \in S_{p}} \varepsilon_{k}}^{\leftarrow}(1 / n)=o\left(\delta_{2}(n, m)\right) \quad \text { for } \quad n \rightarrow \infty
$$

In real life we do not know the number of critical edges in either of the three settings. We distinguish between setting (1) and settings (2)-(3) and propose Algorithm 3 with $\delta_{2}(m):=\delta_{2}(n, m)$, i.e., for a fixed sample size $n$ we focus on the path length $m$. For setting (1) we do know the underlying unweighted DAG $\mathcal{D}$. Therefore, we do not need to decide whether some small value $\hat{b}_{j i}$ corresponds to a path from $j$ to $i$. However, we do not know the minimum ML DAG $\mathcal{D}^{B}$ such that we would apply Algorithm 3 to estimate $\mathcal{D}^{B}$. For settings (2) and (3) we would apply first Algorithm 2 and afterwards Algorithm 3.

To further illustrate this, observe the diagram below. In setting 3, we start with $\hat{\boldsymbol{B}}$, while in setting 2 with $\hat{\boldsymbol{B}}$ and for setting 1 , we start with $\hat{\boldsymbol{B}}$.

In the next section we derive the asymptotic distribution of the estimators.

# 5. Asymptotic distribution of the minimum ratio estimators 

With the goal of proving asymptotic distributional properties of the minimum ratio estimators for the different settings (1)-(3), we require regular variation of the noise variable $\varepsilon$ in its left endpoint. Under this condition we first prove that also the minimum ratio estimators $\bigwedge_{k=1}^{n}\left(U_{i}^{k} / U_{j}^{k}\right)$ are regularly varying. Moreover, we show that their joint limit distribution is the product of Weibull distributions. In this section we assume $\boldsymbol{C}$ is generic in the sense of Definition 3.5.

```
Algorithm 3 Approximating max-weighted paths
Input: Threshold sequences \(\delta_{2}(1), \ldots, \delta_{2}(d)\) and settings
    (1): a known underlying DAG \(\mathcal{D}:=(V, E)\) and an estimate \(\hat{B}\) as in (4.2), or
    (2-3): a (known or estimated) topological order \(\pi: 1, \ldots, d\) and a thresholded matrix \(\hat{B}\)
    obtained from Algorithm 2.
Output: An estimated minimum DAG \(\mathcal{D}^{\hat{B}}=\left(V, E^{\hat{B}}\right)\)
    \(E^{\hat{B}}:=\emptyset\) and \(\mathcal{D}^{\hat{B}}:=\left(V, E^{\hat{B}}\right)\)
    (1): \(\quad S:=\{(j, i) \in V \times V: j \in \mathrm{pa}(i)\}\) and infer a topological order \(\pi: 1, \ldots, d\) from \(\mathcal{D}\)
    (2)-(3): \(S:=\{(j, i) \in V \times V: j<i\}\)
    Sort pairs \((j, i)\) in \(S\) by their distance \((i-j)\) according to the topological order from low to
    high
    for \((j, i)\) in S do
        if \(\exists\) path \(p\) from \(j\) to \(i\) in \(\mathcal{D}^{\hat{B}}\) then
            Set \(m\) as the maximum path length in \(\mathcal{D}^{\hat{B}}\)
            Set \(l:=\underset{l \in V \backslash\{j, i\}}{\arg \max }\left(\hat{b}_{j l} \hat{b}_{l i}\right)\)
            if \(\left(\hat{b}_{j i}-\hat{b}_{j l} \hat{b}_{l i}\right)>\delta_{2}(m)\) then
                \(E^{\hat{B}}:=E^{\hat{B}} \cup\{(j, i)\}\)
            end if
    else
        if \(\hat{b}_{j i}>0\) then
            \(E^{\hat{B}}:=E^{\hat{B}} \cup\{(j, i)\}\)
            end if
    end if
    end for
    \(\operatorname{return} \mathcal{D}^{\hat{B}}=\left(V, E^{\hat{B}}\right)\)
```

The results can be extended to a non-generic model by similar methods as used in Corollary 3.14.

In what follows we assume that the random variables $\tilde{\varepsilon}_{i}:=\ln \left(\varepsilon_{i}\right)>0$ for $i=1, \ldots, d$ are iid regularly varying at zero with exponent $\alpha>0$ and recall from Corollary 2.6(b) that this is equivalent to $(\varepsilon-1) \in R V_{\alpha}^{0}$ or $\varepsilon \in R V_{\alpha}^{1}$.

We first prove that $\ln \left(U_{i} / U_{j}\right)-\ln \left(b_{j i}\right)$ is regularly varying at zero which will be a consequence of Theorem 3.12. In this auxiliary result as well as in the theorems below we need that $\boldsymbol{C}$ is generic. Further, for a path $p$ we denote by $\zeta(p)=\left|S_{p}\right|$ its path length.

Lemma 5.1. Let $\boldsymbol{U} \in \mathbb{R}_{+}^{d}$ be a recursive ML vector with propagating noise on a $D A G \mathcal{D}$ as defined in (3.1) and assume that the path $p:=[j \rightarrow \ldots \rightarrow i]$ from $j$ to $i$ is generic. If $\ln (\varepsilon) \in R V_{\alpha}^{0}$, then $\ln \left(U_{i} / U_{j}\right)-\ln \left(b_{j i}\right) \in R V_{\zeta(p) \alpha}^{0}$.

The following is the main result of this section and describes the asymptotic distribution of the minimum ratio estimator $\hat{\boldsymbol{B}}$ from (4.10). In particular, it shows that its entries are asymptotically independent.

Theorem 5.2. Let $\boldsymbol{U} \in \mathbb{R}_{+}^{d}$ be a recursive ML vector with propagating noise as defined in (3.1). Assume that $\boldsymbol{C}$ is generic and that $\tilde{\varepsilon}=\ln (\varepsilon) \in R V_{\alpha}^{0}$. For every path $p_{j i}$ from $j$ to $i$ and node set $S_{p_{j i}}$ choose $a_{n}^{(j i)} \sim F_{\sum_{k \in S_{p_{j i}}} \tilde{\varepsilon}_{k}}^{\leftarrow}(1 / n)$ as $n \rightarrow \infty$. If $\boldsymbol{U}^{1}, \ldots, \boldsymbol{U}^{n}$ is an iid sample from $\boldsymbol{U}$, then

$$
\begin{aligned}
& \lim _{n \rightarrow \infty} \mathbb{P}\left(\frac{1}{a_{n}^{(j i)} b_{j i}}\left(\bigwedge_{k=1}^{n} \frac{U_{i}^{k}}{U_{j}^{k}}-b_{j i}\right) \leq x_{j i} \forall(j, i) \in V \times V \text { with } b_{j i}>0\right) \\
= & \prod_{\substack{(j, i) \in V \times V: \\
b_{j i}>0}} \Psi_{\zeta\left(p_{j i}\right) \alpha,\left(c^{(j i)}\right)^{1 /\left(\zeta\left(p_{j i}\right) \alpha\right)}}\left(x_{j i}\right), \quad x_{j i}>0
\end{aligned}
$$

where $c^{(j i)} \in(0,1)$ is defined as in Theorem 3.12.
If we know the minimum ML DAG $\mathcal{D}^{B}=\left(V, E\left(\mathcal{D}^{B}\right)\right)$, it is preferable to estimate $b_{j i}$ as in (4.2). Then Theorem 5.2 reduces as follows.

Corollary 5.3. Let the assumptions of Theorem 5.2 hold and assume that the minimum ML DAG $\mathcal{D}^{B}\left(V, E\left(\mathcal{D}^{B}\right)\right)$ is known. Then

$$
\begin{aligned}
& \lim _{n \rightarrow \infty} \mathbb{P}\left(\frac{1}{a_{n}^{(i)} b_{j i}}\left(\bigwedge_{k=1}^{n} \frac{U_{i}^{k}}{U_{j}^{k}}-b_{j i}\right) \leq x_{j i} \forall(j, i) \in E\left(\mathcal{D}^{B}\right)\right) \\
= & \prod_{(j, i) \in E\left(\mathcal{D}^{B}\right)} \Psi_{\alpha,\left(c^{(j i)}\right)^{1 / \alpha}}\left(x_{j i}\right), \quad x_{j i}>0
\end{aligned}
$$

# 6. Data analysis and simulation study 

We want to apply the methods that we have developed over the past sections and consider a data example. For a quality assessment we also perform a simulation study.

### 6.1. Data example

We consider dietary supplement data of $n=8327$ independent interviews taken from the NHANES report for the year 2015-2016, which is available at https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DR1TOT_I.XPT. They have been part of a questionnaire as to "What We Eat in America", which recorded the food and beverage consumed by all participants during the 24 hours period prior to the interview. The data contains 168 food components with the object of estimating the total intake of calories, macro and micro nutrients from foods and beverages. More details can be found on the website.

In [19], the data set has been considered in terms of an adapted $k$-means clustering algorithm for extremal observations. Moreover, assuming a recursive ML model and standardising the marginal data to regular variation at $\infty$ with $\alpha=2,[23]$ investigated the causal relationship between four nutrients using a different estimation method based on scalings.

In our data example we consider the same four nutrients, namely vitamin A (DR1TVARA), $\alpha$-carotene (DR1TACAR), $\beta$-carotene (DR1TBCAR) and lutein+zeaxanthin (DR1TLZ) as in [23]. We abbreviate them by VA, AC, BC and LZ. In order to make results comparable to those of [23], we also use the empirical integral transform to standardize the data to Fréchet(2) margins (see e.g. [3], p. 381) by setting for $i=1,2,3,4$,

$$
U_{l i}:=\left(-\log \left(\frac{1}{n+1} \sum_{j=1}^{n} \mathbf{1}_{\left\{\hat{U}_{j i} \leq \hat{U}_{l i}\right\}}\right)\right)^{-1 / 2}, \quad l=1, \ldots, n=8327
$$

where multiple ranks are uniformly randomly ordered.
We first consider the full matrix of minimum ratios $\hat{\boldsymbol{B}}=\left(\hat{b}_{i j}\right)_{d \times d}$ with $\hat{b}_{i j}=$ $\bigwedge_{t=1}^{n}\left(X_{j}^{t} / X_{i}^{t}\right)$ given by

$$
\begin{array}{cccc}
\text { VA } & A C & B C & L Z \\
\left(\begin{array}{cccc}
1 & 0.014 & 0.011 & 0.007 \\
0.146 & 1 & 0.177 & 0.019 \\
0.321 & 0.010 & 1 & 0.025 \\
0.132 & 0.007 & 0.168 & 1
\end{array}\right) & VA \\
A C \\
B C \\
\hline
\end{array}
$$

We next apply Algorithm 1 to obtain an estimated topological order $\hat{\pi}:=$ $(A C, L Z, B C, V A)$. First we want to assess the quality of the estimated topological order $\hat{\pi}$, which also supports or contradicts the model assumption of a Bayesian network. Motivated by the coefficient $R^{2}$ of determination in regression we define the following.

Definition 6.1. For a given topological order $\pi$ and an estimator $\hat{B}$ of the ML coefficient matrix we define the ML coefficient of determination

$$
R_{\max }(\pi)=\frac{\sum_{\substack{(j, i) \in V \times V: \\ \pi(j)<\pi(i)}} \hat{b}_{j i}}{\sum_{\substack{(j, i) \in V \times V: \\ j \neq i}} \hat{b}_{j i}}
$$

The coefficient $R_{\max }(\pi)$ can take any value in the interval $[0,1]$. Large $R_{\max }(\pi)$ supports the hypothesis that the underlying graph is a DAG and the estimated topological order lies in the equivalence class of topological orders defined in (4.6).

In our data example, we have $R_{\max }(\hat{\pi})=0.929$, strongly supporting the hypothesis of a recursive ML model. Now using the estimator (4.10), and applying Algorithms 2 and 3 with $\delta_{1}=0.02$ and $\delta_{2}(k)=0.02$ for $k \in\{1,2,3\}$, we get the estimated minimum ML DAG $\mathcal{D}^{\hat{B}}$ and ML coefficient matrix $\hat{\boldsymbol{B}}$, where we sorted the matrix according to $\hat{\pi}$. These are shown in Figure 3.
![img-3.jpeg](img-3.jpeg)

Fig 3. Estimated minimum $M L$ DAG $\mathcal{D}^{\hat{B}}$ with estimated ML coefficient matrix $\hat{B}$.

Observe that, since we estimate the edge from AC to LZ to be absent, there are two possible topological orders.

From the estimates we observe that both, $\alpha$-carotene and $\beta$-carotene lead to high amounts of vitamin A. This is in line with our expectation since $\beta$ carotene is a precursor to vitamin A and can be converted by $\beta$-carotene 15,15 monoxygenase by many animals including humans. Similarly, also $\alpha$-carotene can be converted to vitamin A. However, it is only half as active as $\beta$-carotene which explains that the edge weight from $\alpha$-carotene to vitamin A is approximately half compared to the edge weight from $\beta$-carotene to vitamin A ( 0.146 compared to 0.321 ). Moreover, we can see that high amounts of lutein+ zeaxanthin also lead to high amounts of $\beta$-carotene and high amounts of $\alpha$ carotene also lead to high amounts of $\beta$-carotene. However, we did not find a significant connection between $\alpha$-carotene and lutein+zeaxanthin. Observe that [23] inferred the same topological order, yet with one additional edge from $\alpha$ carotene to lutein+zeaxanthin. However, it is also the edge with the smallest estimated edge weight. Similarly as in [23], we plot bivariate extremes in Figure 4 to underline our finding. The first 5 plots in Figure 4 look rather similar. For every large value of the substance on the vertical axis, we can see a large value of the substance on the horizontal axis. Moreover, these observations are shaped closely to a line. In contrast, a large value of the substance on the horizontal axis might as well coincide with a small value of the substance on the vertical axis. Therefore, e.g. a high amount of $\alpha$-carotene leads to a high amount of vitamin A but a high amount of vitamin A does not necessarily lead to a high amount of $\alpha$-carotene. This also supports that the dependence is not mutual and hence we can model it by a DAG. The same can be seen for any pair given in the plots 1-5. Moreover, since parts of the observations are shaped closely along a line, which we would expect for a recursive ML model, we can conclude that the recursive ML model fits the data very well.

The sixth plot is different from the other 5 plots, since for most large observations of $\alpha$-carotene the level of lutein+zeaxanthin is not increased as most large observations in lutein+zeaxanthin do also not result in a high level of $\alpha$ carotene. Therefore, the two substances do not seem to affect each other and we rightly concluded that there is no edge.

# 6.2. Simulation study 

We want to illustrate the effect of observational noise in the ML model. We simulate recursive ML vectors with propagating noise, where the innovations $Z_{1}, \ldots, Z_{4}$ are Fréchet(2) distributed and we use the estimated $\hat{\boldsymbol{B}}$ from (6.1) from the data analysis above for the ML coefficient matrix $\boldsymbol{B}$. Moreover, we simulate three different scenarios. In the first scenario, we assume the non-noisy model as given in (1.1), while for the second scenario we choose the propagating noise model with a medium sized noise and in the third setting we choose a noise variable which is stochastically larger. The scenarios are given as follows:

![img-4.jpeg](img-4.jpeg)

FIG 4. The empirical bivariate extremes (25 largest observations).
(1) No noise
(2) $\ln \left(\varepsilon_{i}\right) \sim \operatorname{Gamma}(\lambda=1, \alpha=2)$ for $i \in\{1,2,3,4\}$, which corresponds to $\mathbb{E}\left(\varepsilon_{i}\right)=2$

Table 1
Empirical success probability for estimated topolgical order being in the equivalence class of topological orders for (1) No noise, (2): Gamma(1,2), (3); Gamma(2,2).


(3) $\ln \left(\varepsilon_{i}\right) \sim \operatorname{Gamma}(\lambda=2, \alpha=2)$ for $i \in\{1,2,3,4\}$, which corresponds to $\mathbb{E}\left(\varepsilon_{i}\right)=4$

We assume to have no information on the underlying DAG and we only consider the quality of the estimator $\hat{b}_{j i}$ given in (4.5). We choose the sample sizes $n \in\{50,200,500,1000\}$ and 1000 simulation runs for each sample size. We first assess the success probabilities for Algorithm 1. Table 1 shows that the topological order can be correctly estimated even for small sample sizes. Moreover, the number of correct runs increases for larger noise variables. This is expected since the noise variables are one-sided. Therefore, for a path $p$ from $j$ to $i$ the ratio $U_{i} / U_{j} \geq d_{j i}(p) \prod_{k \in S_{p}} \varepsilon_{k}$ increases, while the ratio $U_{j} / U_{i} \leq$ $1 /\left(d_{j i}(p) \prod_{k \in S_{p}} \varepsilon_{k}\right)$ decreases. Therefore, it is easier to identify the paths in $\mathcal{D}$ for larger noise.

Next, we want to assess the quality of the estimated ML coefficient matrix $\hat{\boldsymbol{B}}$. To do so, for every pair $(j, i)$ with $b_{j i}>0$ and every simulation run $k \in$ $\{1, \ldots, 1000\}$, we denote the minimum ratio estimator given in (4.5) by $\hat{b}_{j i}^{k}$.

We consider the empirical RMSE, standard deviation and bias for each $b_{j i}>0$ in each model (1)-(3). In what follows we compare the three classical quantities

$$
\begin{aligned}
\operatorname{bias}\left(\hat{b}_{j i}\right) & :=\frac{1}{1000} \sum_{k=1}^{1000} \hat{b}_{j i}^{k}-b_{j i} \\
\operatorname{SD}\left(\hat{b}_{j i}\right) & :=\sqrt{\frac{1}{1000} \sum_{k=1}^{1000}\left(\hat{b}_{j i}^{k}-\hat{\bar{b}}_{j i}\right)^{2}} \quad \text { with } \quad \hat{\bar{b}}_{j i}=\frac{1}{1000} \sum_{k=1}^{1000} \hat{b}_{j i}^{k} \\
\operatorname{RMSE}\left(\hat{b}_{j i}\right) & :=\sqrt{\frac{1}{1000} \sum_{k=1}^{1000}\left(\hat{b}_{j i}^{k}-b_{j i}\right)^{2}}
\end{aligned}
$$

All three quantities are comparatively small even for small sample sizes and decrease whenever the sample size increases. Moreover, they are larger in the propagating noise model and larger noise terms also increase the three quantities. This is in line with what we can expect from the model as noise terms increase the ratios $U_{i} / U_{j}$ and hence also increase the minimum ratio estimator. On the other hand, recall from above that with increasing noise the estimation of the DAG improves.

Table 2
Empirical Bias (6.2) for (1): No noise, (2): Gamma(1,2), (3): Gamma(2,2)


Table 3
Empirical Standard Deviation (6.3) for (1): No noise, (2): Gamma(1,2), (3): Gamma(2,2)


# Appendix A: Proofs of Section 3 

Proof of Theorem 3.2 Rewrite (3.1) in matrix form by means of the tropical matrix multiplication (2.4) as

$$
\boldsymbol{U}=(\boldsymbol{U} \odot \boldsymbol{C} \vee \boldsymbol{Z}) \odot \boldsymbol{E}_{d}
$$

Table 4
Empirical RMSE (6.4) for (1): No noise, (2): Gamma(1,2), (3): Gamma(2,2)


The associative law implies

$$
\boldsymbol{U}=\left(\boldsymbol{U} \odot \boldsymbol{C} \odot \boldsymbol{E}_{d}\right) \vee\left(\boldsymbol{Z} \odot \boldsymbol{E}_{d}\right) \quad \Leftrightarrow \quad \boldsymbol{U}=(\boldsymbol{U} \odot \overline{\boldsymbol{C}}) \vee \overline{\boldsymbol{Z}}
$$

with $\overline{\boldsymbol{C}}=\boldsymbol{C} \odot \boldsymbol{E}_{d}$, which is identical to (3.3), and $\overline{\boldsymbol{Z}}=\boldsymbol{Z} \odot \boldsymbol{E}_{d}$. The right-most equation in (A.1) is of the same form as the non-noisy model in (2.5), so that analogously to its solution given in (2.6), we get the solution

$$
\boldsymbol{B}^{*}=\left(\boldsymbol{I}_{d} \vee \overline{\boldsymbol{C}}\right)^{\odot(d-1)}, \quad \boldsymbol{U}=\overline{\boldsymbol{Z}} \odot \boldsymbol{B}^{*}=\boldsymbol{Z} \odot \boldsymbol{E}_{d} \odot \boldsymbol{B}^{*}
$$

where $\boldsymbol{B}^{*}$ is the Kleene star matrix of $\overline{\boldsymbol{C}}$. Therefore, defining $\overline{\boldsymbol{B}}=\boldsymbol{E}_{d} \odot \boldsymbol{B}^{*}$ yields the result.

Proof of Corollary 3.4 From (3.6) and the continuity of $Z$ and $\varepsilon$ we have

$$
U_{i}=\bigvee_{j \in \operatorname{An}(i)} \bar{b}_{j i} Z_{j}=\bar{b}_{k i} Z_{k}
$$

for some unique $k \in \operatorname{An}(i)$. We want to show that this implies $U_{i}=\bar{b}_{k i} \tilde{U}_{k}$, i.e., $\tilde{U}_{k}=Z_{k}$. Applying first (3.7), then (3.6) and finally (3.4), we obtain

$$
\tilde{U}_{k}=\frac{U_{k}}{\varepsilon_{k}}=\frac{\bigvee_{l \in \operatorname{An}(k)} \bar{b}_{l k} Z_{l}}{\varepsilon_{k}} \geq \frac{\bar{b}_{k k} Z_{k}}{\varepsilon_{k}}=Z_{k}
$$

Now assume that $\tilde{U}_{k}>Z_{k}$. Then there exists an $l \in \operatorname{an}(k) \subset \operatorname{An}(i)$ with $\bar{b}_{l k} Z_{l}>\varepsilon_{k} Z_{k}$. Note also that the maximum random path weight from $l$ to $i$

must be greater or equal than the maximum random path weight from $l$ to $i$ passing through node $k$. These two facts lead to

$$
U_{i}=\bigvee_{j \in \operatorname{An}(i)} \bar{b}_{j i} Z_{j} \geq \bar{b}_{l i} Z_{l} \geq \frac{\bar{b}_{l k} \bar{b}_{k i}}{\varepsilon_{k}} Z_{l}>\bar{b}_{k i} Z_{k}
$$

The above inequality, however, contradicts (A.2). Therefore, since $k \in \operatorname{An}(i)$, we have

$$
U_{i} \leq \bigvee_{j \in \operatorname{An}(i)} \bar{b}_{j i} \tilde{U}_{j}
$$

Now assume that $U_{i}<\vee_{j \in \operatorname{An}(i)} \bar{b}_{j i} \tilde{U}_{j}$. Then, with the same arguments as above, $U_{i}<\vee_{j \in \operatorname{An}(i)} \bar{b}_{j i} Z_{j}$ which is a contradiction.

Proof of Lemma 3.8 (a) We first assume that $j=i$. Since $\mathcal{D}$ is a DAG, $\operatorname{de}(i) \cap \operatorname{pa}(i)=\emptyset$ and $\bar{b}_{i k} \bar{b}_{k i}=0$ for all $k \neq i$. Therefore, the equality holds and the inequality is equivalent to $\bar{b}_{i i} \geq 0$ which obviously holds.

Next, assume $j \neq i$ and $j \notin \operatorname{an}(i)$. Then by (3.4) $\bar{b}_{j i}=0$ and there is no path from $j$ to $i$. Therefore, $\operatorname{de}(j) \cap \operatorname{pa}(i)=\emptyset$. Hence, the right-hand side of the inequality equals zero. Moreover, the equality holds as well, otherwise $\bar{b}_{j k}>0$ and $\bar{b}_{k i}>0$ for some $k \in V$ and therefore, by (3.4) there would be a path from $j$ to $k$ and from $k$ to $i$ which contradicts $j \notin \operatorname{an}(i)$.

For $j \in \mathrm{pa}(i)$ with $\operatorname{de}(j) \cap \mathrm{pa}(i)=\emptyset$, the critical path must be the edge $j \rightarrow i$ since it is the only path from $j$ to $i$. Furthermore, the equality $\bar{b}_{j i}=\frac{\bar{b}_{j k} \bar{b}_{k i}}{\bar{b}_{k k}}$ holds for $k=i$ and $k=j$ while for all $k \notin\{i, j\}$ it must hold that $\frac{\bar{b}_{j k} \bar{b}_{k i}}{\bar{b}_{k k}}=0$. Therefore, the equality holds. Moreover, the right-hand side of the inequality again equals zero and we have strict inequality.

Now assume $j \in \operatorname{an}(i)$ and $\operatorname{de}(j) \cap \operatorname{pa}(i) \neq \emptyset$. Then for every path $p=[j=$ $\left.k_{0} \rightarrow k_{1} \rightarrow \ldots \rightarrow k_{n}=i\right]$ with $n \geq 2$ from $j$ to $i$ and every $k_{m} \in\left\{k_{1}, \ldots, k_{n-1}\right\}$, by $(3.2)$,

$$
\begin{aligned}
\bar{d}_{j i}(p) & =\varepsilon_{j} \prod_{l=0}^{n-1} c_{k_{l} k_{l+1}} \varepsilon_{k_{l+1}} \\
& =\frac{\varepsilon_{j} \prod_{l=0}^{m-1} c_{k_{l} k_{l+1}} \varepsilon_{k_{l+1}} \cdot \varepsilon_{k_{m}} \prod_{l=m}^{n-1} c_{k_{l} k_{l+1}} \varepsilon_{k_{l+1}}}{\varepsilon_{k_{m}}} \\
& =\frac{\bar{d}_{j k_{m}}\left(p_{1}\right) \bar{d}_{k_{m} i}\left(p_{2}\right)}{\bar{b}_{k_{m} k_{m}}}
\end{aligned}
$$

with $p_{1}=\left[j=k_{0} \rightarrow k_{1} \rightarrow \ldots \rightarrow k_{m}\right]$ and $p_{2}=\left[k_{m} \rightarrow \ldots \rightarrow k_{n}=i\right]$, where in the last step we have used that $\varepsilon_{k_{m}}=\bar{b}_{k_{m} k_{m}}$. Therefore, for the random critical path $p$ with $\bar{b}_{j i}=\bar{d}_{j i}(p)$ it holds that every sub-path of this path is itself critical, otherwise we could find a path of larger random path weight by replacing the sub-path by a path of larger random weight. It follows that

$$
\bar{b}_{j i} \geq \bigvee_{k \in \operatorname{de}(j) \cap \operatorname{an}(i)} \frac{\bar{b}_{j k} \bar{b}_{k i}}{\bar{b}_{k k}}
$$

with equality whenever the critical path $p$ from $j$ to $i$ contains a node $k \in$ $\operatorname{de}(j) \cap \operatorname{an}(i)$. Since for $k=i$ or $k=j$ we have $\bar{b}_{j i}=\frac{\bar{b}_{j k} \bar{b}_{k i}}{\bar{b}_{k k}}$ and for $k \in$ $V \backslash((\operatorname{an}(i) \cap \operatorname{de}(j)) \cup\{j, i\})$ we have $\frac{\bar{b}_{j k} \bar{b}_{k i}}{\bar{b}_{k k}}=0$, the equality holds as well.
(b) First assume that there is a path $p:=[j \rightarrow \ldots \rightarrow k \rightarrow \ldots \rightarrow i]$ with $\bar{d}_{j i}(p)=\bar{b}_{j i}$. Then by (A.3) we have $\bar{b}_{j i}=\frac{\bar{d}_{j k}\left(p_{1}\right) \bar{d}_{k i}\left(p_{2}\right)}{\bar{b}_{k k}}$. Now every sub-path of a random critical path must be itself critical, as explained in the proof of part a). Hence, $\bar{b}_{j k}=\bar{d}_{j k}\left(p_{1}\right)$ and $\bar{b}_{k i}=\bar{d}_{k i}\left(p_{2}\right)$ and for this reason $\bar{b}_{j i}=\frac{\bar{b}_{j k} \bar{b}_{k i}}{\bar{b}_{k k}}$.

In contrast, let $\bar{d}_{j i}(p)<\bar{b}_{j i}$ for all $p \in P_{j k i}$, where $P_{j k i}$ denotes all paths from $j$ to $i$ that pass through $k$. Now choose $p_{1}=[j \rightarrow \ldots \rightarrow k]$ and $p_{2}=[k \rightarrow \ldots \rightarrow$ $i]$ such that $\bar{d}_{j k}\left(p_{1}\right)=\bar{b}_{j k}$ and $\bar{d}_{k i}\left(p_{2}\right)=\bar{b}_{k i}$. Then, for the path $p \in P_{j k i}$ that results from concatenation of $p_{1}$ and $p_{2}$ we have by (3.4)

$$
\bar{b}_{j i}>\bar{d}_{j i}(p)=\frac{\bar{b}_{j k} \bar{b}_{k i}}{\bar{b}_{k k}}
$$

which proves the reverse direction.
(c) For $j=i$ the inequality obviously holds, since $b_{i i}=1$. If $j \notin \operatorname{An}(i)$, then by definition $\bar{b}_{j i}=b_{j i}=0$ and $\bar{b}_{j j}=\varepsilon_{j} \geq 1$. Therefore, the inequality is equivalent to $U_{i} / U_{j} \geq 0$, which is true. Now let $j \in \operatorname{an}(i)$. Then by (3.2) and (3.4) the center ratio can be written as

$$
\frac{\bar{b}_{j i}}{\bar{b}_{j j}}:=\bigvee_{p \in P_{j i}} \frac{\bar{d}_{j i}(p)}{\bar{b}_{j j}}=\bigvee_{p \in P_{j i}} d_{j i}(p) \prod_{l=0}^{n-1} \varepsilon_{k_{l+1}} \geq \bigvee_{p \in P_{j i}} d_{j i}(p)=b_{j i}
$$

since $\bar{b}_{j j}=\varepsilon_{j}$ and $\varepsilon_{i} \geq 1$. Now we use (3.8) and obtain by (A.4)

$$
\frac{U_{i}}{U_{j}}=\frac{\bigvee_{k \in \operatorname{An}(i)} \bar{b}_{k i} \tilde{U}_{k}}{U_{j}} \geq \frac{\bar{b}_{j i} \tilde{U}_{j}}{U_{j}}=\frac{\bar{b}_{j i} U_{j}}{\varepsilon_{j} U_{j}}=\frac{\bar{b}_{j i}}{\bar{b}_{j j}} \geq b_{j i}
$$

(d) We first prove by contradiction that there is no lower bound for $U_{i} / U_{j}$ of larger value than the one given in part (c). Assume $j \in \operatorname{an}(i)$ and there is a lower bound $c>b_{j i}$. Since $Z_{1}, \ldots, Z_{d}$ are iid, every innovation $Z_{l}$ can realize the maximum with positive probability, such that for every $l \in \operatorname{An}(j)$,

$$
\mathbb{P}\left(\left\{U_{j}=\bigvee_{k \in \operatorname{An}(j)} \bar{b}_{k j} Z_{k}=\bar{b}_{l j} Z_{l}\right\} \cap\left\{U_{i}=\bigvee_{k \in \operatorname{An}(i)} \bar{b}_{k i} Z_{k}=\bar{b}_{l i} Z_{l}\right\}\right)>0
$$

Hence, without loss of generality we assume that this holds for $l=j$. Denote the random critical path $p:=\left[j=k_{0} \rightarrow \ldots \rightarrow k_{n}=i\right]$ such that $\bar{d}_{j i}(p)=\bar{b}_{j i}$. Then, it follows on the event in (A.5) with $l=j$ from (3.2) that

$$
\mathbb{P}\left(\frac{U_{i}}{U_{j}}<c\right)=\mathbb{P}\left(\frac{\bar{b}_{j i}}{\bar{b}_{j j}}<c\right)=\mathbb{P}\left(\frac{\varepsilon_{j} d_{j i}(p) \prod_{l=0}^{n-1} \varepsilon_{k_{l+1}}}{\varepsilon_{j}}<c\right)
$$

$$
=\mathbb{P}\left(d_{j i}(p) \prod_{l=0}^{n-1} \varepsilon_{k_{l+1}}<c\right)>0
$$

since $d_{j i}(p) \leq b_{j i}<c$ and $\varepsilon \geq 1$. Hence, $c$ is no lower bound and together with part c) this entails the support for $j \in \operatorname{an}(i)$.

Now assume $j \notin \operatorname{An}(i)$ such that $b_{j i}=0$. Assume that $U_{i} / U_{j}$ is lower bounded by some $c>0$. Then by (3.6),

$$
\frac{U_{i}}{U_{j}} \geq c \quad \Leftrightarrow \quad \bigvee_{k \in \operatorname{An}(i)} \bar{b}_{k i} Z_{k} \geq c \bigvee_{k \in \operatorname{An}(j)} \bar{b}_{k j} Z_{k}
$$

which is equivalent to

$$
\bigvee_{k \in \operatorname{An}(i)} \bar{b}_{k i} Z_{k} \geq c\left(\bigvee_{k \in \operatorname{An}(i) \cap \operatorname{An}(j)} \bar{b}_{k j} Z_{k} \vee \bigvee_{k \in \operatorname{An}(j) \backslash \operatorname{An}(i)} \bar{b}_{k j} Z_{k}\right)
$$

Therefore, it holds in particular, that

$$
\bigvee_{k \in \operatorname{An}(i)} \bar{b}_{k i} Z_{k} \geq c \bar{b}_{l j} Z_{l}
$$

for every $l \in \operatorname{An}(j) \backslash \operatorname{An}(i)$. This set is non-empty since $j \notin \operatorname{An}(i)$, so it contains at least $j$. However, since the innovation and the noise variables are all independent and unbounded above, we have for every $l \in \operatorname{An}(j) \backslash \operatorname{An}(i)$

$$
\mathbb{P}\left(Z_{l} \geq \frac{\bigvee_{k \in \operatorname{An}(i)} \bar{b}_{k i} Z_{k}}{c \bar{b}_{l j}}\right)>0
$$

contradicting (A.6) and, hence, the assumption of a lower positive bound $c$ for $U_{i} / U_{j}$.

The upper interval limits of $U_{i} / U_{j}$ for $j \in \operatorname{an}(i)$ and and $j \notin \operatorname{An}(i)$ follow from changing the roles of $i$ and $j$. For $j \neq i$, the ratio $U_{i} / U_{j}$ always contains $\varepsilon_{i}$ or $\varepsilon_{j}$ and both random variables are atom-free and independent of all innovations $Z_{1}, \ldots, Z_{d}$ and $\varepsilon_{k}$ for $k \neq i$ and $k \neq j$. Therefore, the ratio inherits the continuity of the noise variables and part d) follows.
(e) For $j=i$ we have $b_{j i}=1 \neq 0=\bigvee_{k \in \operatorname{de}(j) \cap \operatorname{an}(i)} \frac{b_{j k} b_{k i}}{b_{k k}}$. If $j \notin \operatorname{An}(i)$ we have $b_{j i}=\bar{b}_{j i}=0$ by (3.4).

Next assume that $j \in \operatorname{an}(i)$, and $b_{j i}=\bigvee_{k \in \operatorname{de}(j) \cap \operatorname{an}(i)} \frac{b_{j k} b_{k i}}{b_{k k}} \neq 0$. Then there is a path $p=\left[j=k_{0} \rightarrow k_{1} \rightarrow \ldots \rightarrow k_{n}=i\right]$ from $j$ to $i$ with non-random path weight $d_{j i}(p)=b_{j i}$, which is not the edge $j \rightarrow i$.

For a contradiction, assume that $\bar{b}_{j i}>\bigvee_{k \in \operatorname{de}(j) \cap \operatorname{an}(i)} \frac{\bar{b}_{j k} b_{k i}}{b_{k k}}$. This is equivalent to the edge $j \rightarrow i$ being the random critical path. However, every path $p \in P_{j i}$ has random path weight, which depends on both noise variables $\varepsilon_{i}$ and $\varepsilon_{j}$, so in particular, the non-random critical path $p=\left[j=k_{0} \rightarrow k_{1} \rightarrow \ldots \rightarrow k_{n}=i\right]$

from $j$ to $i$ with path weight $d_{j i}(p)=b_{j i}$ is one of these paths. Therefore, by (3.2) and since $b_{j i}>c_{j i}$, the random path weight of $p$ is

$$
\bar{d}_{j i}(p)=b_{j i} \varepsilon_{j} \prod_{l=0}^{n-1} \varepsilon_{k_{l+1}} \geq b_{j i} \varepsilon_{j} \varepsilon_{i}>c_{j i} \varepsilon_{j} \varepsilon_{i}=\bar{b}_{j i}
$$

where we have used that $\varepsilon \geq 1$. This is a contradiction and hence $\bar{b}_{j i}=$ $\bigvee_{k \in \operatorname{de}(j) \cap \operatorname{an}(i)} \frac{\bar{b}_{j k} \bar{b}_{k i}}{\bar{b}_{k k}}$.
(f) The assumptions $b_{j i}>\bigvee_{k \in \operatorname{de}(j) \cap \operatorname{an}(i)} \frac{b_{j k} \bar{b}_{k i}}{\bar{b}_{k k}}$ and $\operatorname{de}(j) \cap \operatorname{an}(i) \neq \emptyset$ are equivalent to the edge $p_{\max }=[j \rightarrow i]$ being the only non-random critical path.

Let $p^{\prime}=\left[j=k_{0} \rightarrow k_{1} \rightarrow \ldots \rightarrow k_{n}=i\right] \neq p_{\max }$ be the path such that $\bigvee_{p \in P_{j i} \backslash\left\{p_{\max }\right\}} \bar{d}_{j i}(p)=\bar{d}_{j i}\left(p^{\prime}\right)$. Then

$$
\bigvee_{p \in P_{j i} \backslash\left\{p_{\max }\right\}} \bar{d}_{j i}(p)=\bar{d}_{j i}\left(p^{\prime}\right)=\bigvee_{k \in \operatorname{de}(j) \cap \operatorname{an}(i)} \frac{\bar{b}_{j k} \bar{b}_{k i}}{\bar{b}_{k k}}
$$

otherwise we can construct a path of larger random path weight from $j$ to $i$ passing through $k$ as explained in the proof of part a). First assume that $\bar{b}_{j i}=\bar{d}_{j i}\left(p_{\max }\right)$. Then, $\bar{b}_{j i}>\bigvee_{k \in \operatorname{de}(j) \cap \operatorname{an}(i)} \frac{\bar{b}_{j k} \bar{b}_{k i}}{\bar{b}_{k k}}$ and $\operatorname{de}(j) \cap \operatorname{an}(i) \neq \emptyset$ is by (3.2) and (3.4) equivalent to

$$
\bar{b}_{j i}>\bar{d}_{j i}\left(p^{\prime}\right)=\varepsilon_{i} \varepsilon_{j} d_{j i}\left(p^{\prime}\right) \prod_{l=0}^{n-2} \varepsilon_{k_{l+1}} \quad \Longleftrightarrow \quad \frac{b_{j i}}{d_{j i}\left(p^{\prime}\right)}>\prod_{l=0}^{n-2} \varepsilon_{k_{l+1}}
$$

Since $\varepsilon \geq 1$, also $b_{j i} / d_{j i}\left(p^{\prime}\right)>1$. Hence, the event given by (A.7) has positive probability which is however, strictly smaller than one, since the noise variables do not have an upper bound. Therefore, since $\bar{b}_{j i} \geq \bigvee_{k \in \operatorname{de}(j) \cap \operatorname{an}(i)} \frac{\bar{b}_{j k} \bar{b}_{k i}}{\bar{b}_{k k}}$, by part a), the complementary event

$$
\left\{\bar{b}_{j i}=\bigvee_{k \in \operatorname{de}(j) \cap \operatorname{an}(i)} \frac{\bar{b}_{j k} \bar{b}_{k i}}{\bar{b}_{k k}}\right\}
$$

is also having positive probability.
Proof of Lemma 3.11 (a) Suppose there is an edge $k_{l} \rightarrow k_{l+1}$ in $p$ such that $c_{k_{l} k_{l+1}} \notin \mathcal{D}^{\mathcal{B}}$. Then, $\operatorname{de}(j) \cap \operatorname{an}(i) \neq \emptyset$ and by Lemma 3.8 e) $\mathbb{P}\left(\bar{b}_{k_{l} k_{l+1}}=\right.$ $\left.c_{k_{l} k_{l+1}} \varepsilon_{k_{l}} \varepsilon_{k_{l+1}}\right)=0$, so we can replace the edge $k_{l} \rightarrow k_{l+1}$ by some other path to get a new path from $j$ to $i$ of larger random path weight than $p$. Hence, $p$ is not a possible critical path realization. The same argument can be used for the reverse.
(b) First consider $\neg\left(S_{p_{1}} \cap S_{p_{2}}=\emptyset\right.$ or for every $r \in S_{p_{1}} \cap S_{p_{2}}$ the sub-path of $p_{1}$ from $j$ to $r$ is a sub-path of $p_{2}$ or the sub-path of $p_{2}$ from $l$ to $r$ is a sub-path of $p_{1}$ ). Then there exists some node $r \in S_{p_{1}} \cap S_{p_{2}}$ such that $p_{1}=[j \rightarrow$

$\ldots \rightarrow s \rightarrow r \rightarrow \ldots \rightarrow i]$ and $p_{2}=[l \rightarrow \ldots \rightarrow t \rightarrow r \rightarrow \ldots \rightarrow m]$ with $s \neq t$. Denote by $p_{11}:=[j \rightarrow \ldots \rightarrow s]$ the sub-path of $p_{1}$ from $j$ to $s$. We want to show by contradiction that the event (3.9) has probability zero. Therefore, we consider the subset of $\Omega$ such that (3.9) holds and show that it is a null-set. Since on this subset, $p_{1}$ is the random critical path and passes through $s$, by Lemma 3.8 b) we have $\bar{b}_{j i}=\frac{\bar{b}_{j s} \bar{b}_{s i}}{\bar{b}_{s s}}$ and $U_{s}=U_{j} \bar{b}_{j s} / \varepsilon_{j}=U_{j} d_{j s}\left(p_{11}\right) \prod_{k \in S_{p_{11}}} \varepsilon_{k}$. With the same argument it also holds that $\bar{b}_{j i}=\frac{\bar{b}_{j s} \bar{b}_{s i}}{\bar{b}_{s s}}$ and $U_{r}=U_{j} \bar{b}_{j r} / \varepsilon_{j}=$ $U_{j} d_{j s}\left(p_{11}\right) \prod_{k \in S_{p_{11}}} \varepsilon_{k} c_{s r} \varepsilon_{r}$. Hence, it must holds that $U_{r}=U_{s} c_{s r} \varepsilon_{r}$. By the same arguments, we also must have $U_{r}=U_{t} c_{t r} \varepsilon_{r}$, which together leads to

$$
U_{s} c_{s r}=U_{t} c_{t r}
$$

This is by (3.4) and (3.6) equivalent to

$$
c_{s r} \bigvee_{l \in \operatorname{An}(s)} \varepsilon_{l} \bigvee_{p \in P_{l s}} d_{l s}(p) \prod_{k \in S_{p}} \varepsilon_{k} Z_{l}=c_{t r} \bigvee_{l \in \operatorname{An}(t)} \varepsilon_{l} \bigvee_{p \in P_{l t}} d_{l t}(p) \prod_{k \in S_{p}} \varepsilon_{k} Z_{l}
$$

Now since $\mathcal{D}$ is acyclic, there cannot be a path from $s$ to $t$ and from $t$ to $s$; so without loss of generality we can assume that there is no path from $t$ to $s$. However, the right-hand side of the equation always contains $\varepsilon_{t}$ which is not part of the left-hand side. Since $Z_{1}, \ldots, Z_{d}$ as well as $\varepsilon_{1}, \ldots, \varepsilon_{i}$ are atom-free and independent random variables, this can only happen on a null-set.

Next consider the reverse, i.e., $S_{p_{1}} \cap S_{p_{2}}=\emptyset$ or for every $r \in S_{p_{1}} \cap S_{p_{2}}$ the sub-path of $p_{1}$ from $j$ to $r$ is a sub-path of $p_{2}$ or the sub-path of $p_{2}$ from $l$ to $r$ is a sub-path of $p_{1}$.

If $S_{p_{1}} \cap S_{p_{2}}=\emptyset$, then the probability of (3.9) is obviously positive. Without loss of generality we now assume that for every $r \in S_{p_{1}} \cap S_{p_{2}}$ the sub-path of $p_{2}$ from $l$ to $r$ is a sub-path of $p_{1}$. We now define $r$ to be the last common node of the two paths $p_{1}$ and $p_{2}$. Then, $p_{1}$ and $p_{2}$ induce the paths $p^{\prime}=[j \rightarrow \ldots \rightarrow l \rightarrow \ldots r]$, $p^{\prime \prime}=[r \rightarrow \ldots \rightarrow i]$ and $p^{\prime \prime \prime}=[r \rightarrow \ldots \rightarrow m]$. Then

$$
\begin{aligned}
& \left\{U_{i}=U_{j} d_{j i}\left(p_{1}\right) \prod_{k \in S_{p_{1}}} \varepsilon_{k}, U_{m}=U_{l} d_{l m}\left(p_{2}\right) \prod_{k \in S_{p_{2}}} \varepsilon_{k}\right\} \\
& =\left\{U_{r}=U_{j} d_{j r}\left(p^{\prime}\right) \prod_{k \in S_{p^{\prime}}} \varepsilon_{k}, U_{i}=U_{r} d_{r i}\left(p^{\prime \prime}\right) \prod_{k \in S_{p^{\prime \prime}}} \varepsilon_{k}, U_{m}=U_{r} d_{r m}\left(p^{\prime \prime \prime}\right) \prod_{k \in S_{p^{\prime \prime}}} \varepsilon_{k}\right\}
\end{aligned}
$$

which has positive probability, since $S_{p^{\prime}} \cap S_{p^{\prime \prime}} \cap S_{p^{\prime \prime \prime}}=\emptyset$.
Proof of Theorem 3.12 By the law of total probability we have for $x \geq 1$,

$$
\begin{aligned}
I(x) & :=\mathbb{P}\left(\frac{U_{i}}{U_{j}} \leq b_{j i} x\right)=\mathbb{P}\left(\frac{U_{i}}{U_{j}} \leq b_{j i} x, U_{i}=\tilde{U}_{j} \bar{b}_{j i}\right)+\mathbb{P}\left(\frac{U_{i}}{U_{j}} \leq b_{j i} x, U_{i} \neq \tilde{U}_{j} \bar{b}_{j i}\right) \\
& =: I_{1}(x)+I_{2}(x)
\end{aligned}
$$

We denote all paths from $j$ to $i$ by $P_{j i}=\left\{p_{1}, \ldots, p_{r}, p_{\max }\right\}$. There are two situations, either $r=0$ (where we interpret the above set of paths as $\left\{p_{\max }\right\}$ ), or

$r \geq 1$. We first give a proof for $r \geq 1$. We start with $I_{1}(x)$. Since $p_{\max }$ is generic, every path $p \neq p_{\max }$ from $j$ to $i$ has non-random edge weight $d_{j i}(p)<b_{j i}$. Therefore, with (3.7) in the first line, (3.4) in the third and (3.2) in the last, we have for $x>1$,

$$
\begin{aligned}
I_{1}(x) & =\mathbb{P}\left(U_{i} /\left(\tilde{U}_{j} \varepsilon_{j}\right) \leq b_{j i} x, U_{i}=\tilde{U}_{j} \bar{b}_{j i}\right) \\
& =\mathbb{P}\left(\bar{b}_{j i} / \varepsilon_{j} \leq b_{j i} x, U_{i}=\tilde{U}_{j} \bar{b}_{j i}\right) \\
& =\mathbb{P}\left(\bigvee_{p \in P_{j i}} \bar{d}_{j i}(p) / \varepsilon_{j} \leq b_{j i} x, U_{i}=\tilde{U}_{j} \bar{b}_{j i}\right) \\
& =\mathbb{P}\left(\bigvee_{p \in P_{j i}} d_{j i}(p) \prod_{k \in S_{p}} \varepsilon_{k} \leq b_{j i} x, U_{i}=\tilde{U}_{j} \bar{b}_{j i}\right)
\end{aligned}
$$

By definition of $\bar{b}_{j i}$ in (3.4), there is a path $p \in\left\{p_{\max }, p_{1}, \ldots, p_{r}\right\}$ such that $\bar{d}_{j i}(p)=\bar{b}_{j i}$ and by continuity of $\varepsilon$ the probability that multiple paths satisfy the equation is equal to 0 . Therefore, again applying the law of total probability, we find

$$
\begin{aligned}
I_{1}(x) & =\mathbb{P}\left(\bigvee_{p \in P_{j i}} d_{j i}(p) \prod_{k \in S_{p}} \varepsilon_{k} \leq b_{j i} x, \bar{d}_{j i}\left(p_{\max }\right)=\bar{b}_{j i}, U_{i}=\tilde{U}_{j} \bar{b}_{j i}\right) \\
& +\mathbb{P}\left(\bigvee_{p \in P_{j i}} d_{j i}(p) \prod_{k \in S_{p}} \varepsilon_{k} \leq b_{j i} x, \bigvee_{p \in\left\{p_{1}, \ldots, p_{r}\right\}} \bar{d}_{j i}(p)=\bar{b}_{j i}, U_{i}=\tilde{U}_{j} \bar{b}_{j i}\right) \\
& =\mathbb{P}\left(\bigvee_{p \in P_{j i}} d_{j i}(p) \prod_{k \in S_{p}} \varepsilon_{k} \leq b_{j i} x, \bar{d}_{j i}\left(p_{\max }\right)=\bar{b}_{j i}, U_{i}=\tilde{U}_{j} \bar{b}_{j i}\right) \\
& +\sum_{s=1}^{r} \mathbb{P}\left(\bigvee_{p \in P_{j i}} d_{j i}(p) \prod_{k \in S_{p}} \varepsilon_{k} \leq b_{j i} x, \bar{d}_{j i}\left(p_{s}\right)=\bar{b}_{j i}, U_{i}=\tilde{U}_{j} \bar{b}_{j i}\right) \\
& =: I_{11}(x)+I_{12}(x) .
\end{aligned}
$$

We first find upper and lower bounds for $I_{11}(x)$. We denote by $P_{k j i}$ all paths from $k$ to $i$ which pass through $j$. Using the simple identity

$$
\left\{z_{1} \vee z_{2} \leq a, z_{1} \vee z_{2}=z_{1}\right\}=\left\{z_{1} \leq a, z_{2} \leq z_{1}\right\}
$$

(3.4) and (3.6) imply

$$
\begin{aligned}
& \left\{\bigvee_{p \in P_{j i}} d_{j i}(p) \prod_{k \in S_{p}} \varepsilon_{k} \leq b_{j i} x\right\} \bigcap\left\{\bar{d}_{j i}\left(p_{\max }\right)=\bar{b}_{j i}\right\} \bigcap\left\{U_{i}=\tilde{U}_{j} \bar{b}_{j i}\right\} \\
= & \left\{\bigvee_{p \in P_{j i}} d_{j i}(p) \prod_{k \in S_{p}} \varepsilon_{k} \leq \bar{d}_{j i}\left(p_{\max }\right)\right\} \bigcap\left\{\bar{d}_{j i}\left(p_{\max }\right) \leq b_{j i} x\right\} \bigcap\left\{U_{i}=\tilde{U}_{j} \bar{b}_{j i}\right\} \\
= & \left\{\bigvee_{p \in P_{j i}} d_{j i}(p) \prod_{k \in S_{p}} \varepsilon_{k} \leq b_{j i} \prod_{k \in S_{p_{\max }}} \varepsilon_{k}\right\} \bigcap\left\{\prod_{k \in S_{p_{\max }}} \varepsilon_{k} \leq x\right\} \bigcap\left\{U_{i}=\tilde{U}_{j} \bar{b}_{j i}\right\} \\
= & \bigcap_{p \in P_{j i} \backslash\left\{p_{\max }\right\}}\left\{\prod_{k \in S_{p}} \varepsilon_{k} \leq \frac{b_{j i}}{d_{j i}(p)} \prod_{k \in S_{p_{\max }}} \varepsilon_{k}\right\} \bigcap\left\{\prod_{k \in S_{p_{\max }}} \varepsilon_{k} \leq x\right\} \bigcap
\end{aligned}
$$

$$
\bigcap_{l \in \operatorname{An}(i)}\left\{\bigcap_{p \in P_{1 i} \backslash P_{1 j i}}\left\{d_{l i}(p) \prod_{k \in S_{p} \cup\{l\}} \varepsilon_{k} Z_{l} \leq b_{j i} \prod_{k \in S_{p_{\max }}} \varepsilon_{k} \bigvee_{l \in \operatorname{An}(j)} \bar{b}_{l j} Z_{l}\right\}\right\}
$$

Cancelling all noise variables possible, and since $\varepsilon>1$, we find a lower bound

$$
\begin{aligned}
I_{11}(x) & =\mathbb{P}\left(\bigcap_{p \in P_{j i} \backslash\left\{p_{\max }\right\}}\left\{\prod_{k \in S_{p} \backslash S_{p_{\max }}} \varepsilon_{k} \leq \frac{b_{j i}}{d_{j i}(p)} \prod_{k \in S_{p_{\max }} \backslash S_{p}} \varepsilon_{k}\right\} \bigcap\right. \\
& \left\{\prod_{k \in S_{p_{\max }}} \varepsilon_{k} \leq x\right\} \bigcap_{l \in \operatorname{An}(i)}\left\{\bigcap_{p \in P_{1 i} \backslash P_{1 j i}}\left\{d_{l i}(p) \prod_{k \in\left(S_{p} \cup\{l\}\right) \backslash S_{p_{\max }}} \varepsilon_{k} Z_{l}\right.\right. \\
& \left.\left.\left.\leq b_{j i} \prod_{k \in S_{p_{\max }} \backslash\left(S_{p} \cup\{l\}\right)} \varepsilon_{k} \bigvee_{l \in \operatorname{An}(j)} \bar{b}_{l j} Z_{l}\right\}\right\}\right) \\
& \geq \mathbb{P}\left(\bigcap_{p \in P_{j i} \backslash\left\{p_{\max }\right\}}\left\{\prod_{k \in S_{p} \backslash S_{p_{\max }}} \varepsilon_{k} \leq \frac{b_{j i}}{d_{j i}(p)}\right\} \bigcap\left\{\prod_{k \in S_{p_{\max }}} \varepsilon_{k} \leq x\right\} \bigcap\right. \\
& \left.\bigcap_{l \in \operatorname{An}(i)}\left\{\bigcap_{p \in P_{1 i} \backslash P_{1 j i}}\left\{d_{l i}(p) \prod_{k \in\left(S_{p} \cup\{l\}\right) \backslash S_{p_{\max }}} \varepsilon_{k} Z_{l} \leq b_{j i} \bigvee_{l \in \operatorname{An}(j)} \bar{b}_{l j} Z_{l}\right\}\right\}\right) \\
& =\mathbb{P}\left(\bigcap_{l \in \operatorname{An}(i)}\left\{\bigcap_{p \in P_{1 i} \backslash P_{1 j i}}\left\{d_{l i}(p) \prod_{k \in\left(S_{p} \cup\{l\}\right) \backslash S_{p_{\max }}} \varepsilon_{k} Z_{l} \leq b_{j i} \bigvee_{l \in \operatorname{An}(j)} \bar{b}_{l j} Z_{l}\right\}\right\}\right. \\
& \bigcap_{p \in P_{j i} \backslash\left\{p_{\max }\right\}}\left\{\prod_{k \in S_{p} \backslash S_{p_{\max }}} \varepsilon_{k} \leq \frac{b_{j i}}{d_{j i}(p)}\right\}) \mathbb{P}\left(\prod_{k \in S_{p_{\max }}} \varepsilon_{k} \leq x\right) \\
& =: c_{1} \mathbb{P}\left(\prod_{k \in S_{p_{\max }}} \varepsilon_{k} \leq x\right)
\end{aligned}
$$

for some constant $c_{1} \in[0,1]$ by independence of the noise variables.
We show that $c_{1}>0$. To do so, recall that $b_{j i} / d_{j i}(p)>1$ for every $p \neq p_{\max }$. Therefore, since $\left\{p \in P_{j i} \backslash\left\{p_{\max }\right\}\right\} \neq \emptyset$ and $\varepsilon>1$,

$$
\mathbb{P}\left(\bigcap_{p \in P_{j i} \backslash\left\{p_{\max }\right\}}\left\{\prod_{k \in S_{p} \backslash S_{p_{\max }}} \varepsilon_{k} \leq \frac{b_{j i}}{d_{j i}(p)}\right\}\right)>0
$$

Next, we want to show that also

$$
\mathbb{P}\left(\bigcap_{l \in \operatorname{An}(i)}\left\{\bigcap_{p \in P_{1 i} \backslash P_{1 j i}}\left\{d_{l i}(p) \prod_{k \in\left(S_{p} \cup\{l\}\right) \backslash S_{p_{\max }}} \varepsilon_{k} Z_{l} \leq b_{j i} \bigvee_{l \in \operatorname{An}(j)} \bar{b}_{l j} Z_{l}\right\}\right\}\right)>0
$$

For this, observe that the left-hand side of the inequality in (A.15) does not contain $Z_{j}$, since all paths from $j$ to $i$ pass through $j$. Since $\bar{b}_{l j}$ and the lefthand side of the inequality in (A.15) is independent of $Z_{j}$ for all $l \in\{1, \ldots, d\}$ and $Z_{j}$ has unbounded support, $Z_{j}$ can become arbitrarily large with positive probability such that (A.15) holds.

The intersection of the two events has also positive probability since (A.14) is independent of $Z_{j}$. This implies that $c_{1}>0$ and a positive lower bound for $I_{11}(x)$.

To get an upper bound, observe that $\varepsilon \geq 1$ and, hence, for every set $S_{p}$ we have
$\left\{\varepsilon_{k}: k \in S_{p_{\max }}\right.$ and $\left.\prod_{k \in S_{p_{\max }} \varepsilon_{k} \leq x\right\} \subseteq\left\{\varepsilon_{k}: k \in S_{p_{\max }}\right.$ and $\left.\prod_{k \in S_{p_{\max }} \backslash S_{p}} \varepsilon_{k} \leq x\right\}$.
Therefore, starting with (A.13) we find the upper bound

$$
\begin{aligned}
& I_{11}(x) \leq \mathbb{P}\left(\bigcap_{p \in P_{j i} \backslash\left\{p_{\max }\right\}}\left\{\prod_{k \in S_{p} \backslash S_{p_{\max }}} \varepsilon_{k} \leq \frac{b_{j i}}{d_{j i}(p)} x\right\} \bigcap\left\{\prod_{k \in S_{p_{\max }}} \varepsilon_{k} \leq x\right\} \bigcap\right. \\
& \left.\bigcap_{l \in \operatorname{An}(i)}\left\{\bigcap_{p \in P_{l i} \backslash P_{l j i}}\left\{d_{l i}(p) \prod_{k \in\left(S_{p} \cup\{l\}\right) \backslash S_{p_{\max }}} \varepsilon_{k} Z_{l} \leq b_{j i} x \bigvee_{l \in \operatorname{An}(j)} \bar{b}_{l j} Z_{l}\right\}\right\}\right) \\
& =\mathbb{P}\left(\bigcap_{l \in \operatorname{An}(i)}\left\{\bigcap_{p \in P_{l i} \backslash P_{l j i}}\left\{d_{l i}(p) \prod_{k \in\left(S_{p} \cup\{l\}\right) \backslash S_{p_{\max }}} \varepsilon_{k} Z_{l} \leq b_{j i} x \bigvee_{l \in \operatorname{An}(j)} \bar{b}_{l j} Z_{l}\right\}\right\}\right. \\
& \bigcap_{p \in P_{j i} \backslash\left\{p_{\max }\right\}}\left\{\prod_{k \in S_{p} \backslash S_{p_{\max }}} \varepsilon_{k} \leq \frac{b_{j i}}{d_{j i}(p)} x\right\}\right) \mathbb{P}\left(\prod_{k \in S_{p_{\max }}} \varepsilon_{k} \leq x\right) \\
& =c_{2}(x) \mathbb{P}\left(\prod_{k \in S_{p_{\max }}} \varepsilon_{k} \leq x\right)
\end{aligned}
$$

Since the innovations and the noise variables are atom-free, it follows that $\lim _{x \downarrow 1} c_{2}(x)=c_{1}$ and, therefore,

$$
I_{11}(x) \sim c_{1} \mathbb{P}\left(\prod_{k \in S_{p_{\max }}} \varepsilon_{k} \leq x\right), \quad x \downarrow 1
$$

We next show that $I_{12}(x)=o\left(I_{11}(x)\right)$ as $x \downarrow 1$. We have for each summand $m \in\{1, \ldots, r\}$, using the simple identity (A.10) to obtain the third line,

$$
\begin{aligned}
& \mathbb{P}\left(\bigvee_{p \in P_{j i}} d_{j i}(p) \prod_{k \in S_{p}} \varepsilon_{k} \leq b_{j i} x, \bar{d}_{j i}\left(p_{m}\right)=\bar{b}_{j i}, U_{i}=\tilde{U}_{j} \bar{b}_{j i}\right) \\
\leq & \mathbb{P}\left(\bigvee_{p \in P_{j i}} d_{j i}(p) \prod_{k \in S_{p}} \varepsilon_{k} \leq b_{j i} x, \bar{d}_{j i}\left(p_{m}\right)=\bar{b}_{j i}\right) \\
= & \mathbb{P}\left(\bigvee_{p \in P_{j i}} d_{j i}(p) \prod_{k \in S_{p}} \varepsilon_{k} \leq \bar{d}_{j i}\left(p_{m}\right), \bar{d}_{j i}\left(p_{m}\right) \leq b_{j i} x\right) \\
= & \mathbb{P}\left(\bigcap_{p \in P_{j i} \backslash\left\{p_{m}\right\}}\left\{\prod_{k \in S_{p}} \varepsilon_{k} \leq \frac{d_{j i}\left(p_{m}\right)}{d_{j i}(p)} \prod_{k \in S_{p_{m}}} \varepsilon_{k}\right\} \bigcap\left\{\prod_{k \in S_{p_{m}}} \varepsilon_{k} \leq \frac{b_{j i} x}{d_{j i}\left(p_{m}\right)}\right\}\right) \\
\leq & \mathbb{P}\left(\left\{\prod_{k \in S_{p_{\max }}} \varepsilon_{k} \leq \frac{d_{j i}\left(p_{m}\right)}{b_{j i}} \prod_{k \in S_{p_{m}}} \varepsilon_{k}\right\} \bigcap\left\{\prod_{k \in S_{p_{m}}} \varepsilon_{k} \leq \frac{b_{j i} x}{d_{j i}\left(p_{m}\right)}\right\}\right)
\end{aligned}
$$

Now the first event rewrites as $\left\{\frac{b_{j i}}{d_{j i}\left(p_{m}\right)} \prod_{k \in S_{p_{\max }}} \varepsilon_{k} \leq \prod_{k \in S_{p_{m}}} \varepsilon_{k}\right\} \subseteq\left\{\frac{b_{j i}}{d_{j i}\left(p_{m}\right)} \leq\right.$ $\left.\left.\prod_{k \in S_{p_{m}}} \varepsilon_{k}\right\}$, since $\varepsilon>1$. Moreover,
$\left\{\prod_{k \in S_{p_{\max }}} \varepsilon_{k} \leq \frac{d_{j i}\left(p_{m}\right)}{b_{j i}} \prod_{k \in S_{p_{m}}} \varepsilon_{k}\right\} \bigcap\left\{\prod_{k \in S_{p_{m}}} \varepsilon_{k} \leq \frac{b_{j i} x}{d_{j i}\left(p_{m}\right)}\right\} \subseteq\left\{\prod_{k \in S_{p_{\max }}} \varepsilon_{k} \leq x\right\}$.
Hence,

$$
(\mathrm{A} .18) \leq \mathbb{P}\left(\left\{\prod_{k \in S_{p_{\max }}} \varepsilon_{k} \leq x\right\} \bigcap\left\{\prod_{k \in S_{p_{m}}} \varepsilon_{k} \in\left[\frac{b_{j i}}{d_{j i}\left(p_{m}\right)}, \frac{b_{j i} x}{d_{j i}\left(p_{m}\right)}\right]\right\}\right)
$$

Moreover, since $\varepsilon \geq 1$, we have for every subset $S \subseteq S_{p_{\max }}$ that $1 \leq \prod_{k \in S} \varepsilon_{k} \leq x$, whenever $1 \leq \prod_{k \in S_{p_{\max }}} \varepsilon_{k} \leq x$. Therefore, for another node set $\tilde{S}$ with $S \cap \tilde{S}=\emptyset$ we have

$$
\prod_{k \in S} \varepsilon_{k} \prod_{k \in \tilde{S}} \varepsilon_{k} \in[a, b] \quad \Rightarrow \quad \prod_{k \in \tilde{S}} \varepsilon_{k} \in[a / x, b]
$$

Finally, since $\bar{d}_{j i}\left(p_{m}\right)=\bar{b}_{j i}$ and $d_{j i}\left(p_{m}\right)<d_{j i}\left(p_{\max }\right)$ we have $S_{p_{m}} \backslash S_{p_{\max }} \neq \emptyset$. In total, we obtain

$$
\begin{aligned}
(\mathrm{A} .18) & \leq \mathbb{P}\left(\left\{\prod_{k \in S_{p_{\max }}} \varepsilon_{k} \leq x\right\} \bigcap\left\{\prod_{k \in S_{p_{m}}} \varepsilon_{k} \in\left[\frac{b_{j i}}{d_{j i}\left(p_{m}\right)}, \frac{b_{j i} x}{d_{j i}\left(p_{m}\right)}\right]\right\}\right) \\
& \leq \mathbb{P}\left(\prod_{k \in S_{p_{\max }}} \varepsilon_{k} \leq x\right) \mathbb{P}\left(\prod_{k \in S_{p_{m}} \backslash S_{p_{\max }}} \varepsilon_{k} \in\left[\frac{b_{j i}}{x d_{j i}\left(p_{m}\right)}, \frac{b_{j i} x}{d_{j i}\left(p_{m}\right)}\right]\right) \\
& =\mathbb{P}\left(\prod_{k \in S_{p_{\max }}} \varepsilon_{k} \leq x\right) o(1), \quad x \downarrow 1
\end{aligned}
$$

as the interval in the second probability gets arbitrarily small and the distribution of $\varepsilon$ is atom-free. Comparing this upper bound with (A.17) we can see that every summand of $I_{12}(x)$ is negligible with respect to $I_{11}(x)$ as $x \downarrow 1$. Since there are only finitely many nodes and hence finitely many paths from $j$ to $i$, we have proved that $I_{12}(x)=o\left(I_{11}(x)\right)$ as $x \downarrow 1$. Hence,

$$
I_{1}(x) \sim c_{1} \mathbb{P}\left(\prod_{k \in S_{p_{\max }}} \varepsilon_{k} \leq x\right), \quad x \downarrow 1
$$

Next, we assume that $r=0$, i.e., that there is only one path $p_{\max }$ from $j$ to $i$. Then from (A.9) we find that $I_{1}(x)=I_{11}(x)$ and simplifies (A.13) to

$$
\begin{aligned}
& I_{1}(x)=\mathbb{P}\left(\left\{\prod_{k \in S_{p_{\max }}} \varepsilon_{k} \leq x\right\} \bigcap\right. \\
& \left.\bigcap_{l \in \operatorname{An}(i)}\left\{\bigcap_{p \in P_{l i} \backslash P_{l j i}}\left\{d_{l i}(p) \prod_{k \in S_{p} \cup\{l\}} \varepsilon_{k} Z_{l} \leq b_{j i} \prod_{k \in S_{p_{\max }}} \varepsilon_{k} \bigvee_{l \in \operatorname{An}(j)} \bar{b}_{l j} Z_{l}\right\}\right\}\right)
\end{aligned}
$$

$$
\begin{aligned}
& \geq \mathbb{P}\left(\left\{\prod_{k \in S_{p_{\max }}} \varepsilon_{k} \leq x\right\} \bigcap\right. \\
& \left.\bigcap_{l \in \operatorname{An}(i)}\left\{\bigcap_{p \in P_{1 i} \backslash P_{1 j i}}\left\{d_{l i}(p) \prod_{k \in\left(S_{p} \cup\{l\}\right) \backslash S_{p_{\max }}} \varepsilon_{k} Z_{l} \leq b_{j i} \bigvee_{l \in \operatorname{An}(j)} \bar{b}_{l j} Z_{l}\right\}\right\}\right) \\
& =\mathbb{P}\left(\bigcap_{l \in \operatorname{An}(i)}\left\{\bigcap_{p \in P_{1 i} \backslash P_{1 j i}}\left\{d_{l i}(p) \prod_{k \in\left(S_{p} \cup\{l\}\right) \backslash S_{p_{\max }}} \varepsilon_{k} Z_{l} \leq b_{j i} \bigvee_{l \in \operatorname{An}(j)} \bar{b}_{l j} Z_{l}\right\}\right\}\right) \\
& \mathbb{P}\left(\prod_{k \in S_{p_{\max }}} \varepsilon_{k} \leq x\right)=c_{1} \mathbb{P}\left(\prod_{k \in S_{p_{\max }}} \varepsilon_{k} \leq x\right)
\end{aligned}
$$

for $c_{1}>0$. On the other hand,

$$
\begin{aligned}
I_{1}(x) \leq & \mathbb{P}\left(\bigcap_{l \in \operatorname{An}(i)}\left\{\bigcap_{p \in P_{1 i} \backslash P_{1 j i}}\left\{d_{l i}(p) \prod_{k \in\left(S_{p} \cup\{l\}\right) \backslash S_{p_{\max }}} \varepsilon_{k} Z_{l} \leq b_{j i} x \bigvee_{l \in \operatorname{An}(j)} \bar{b}_{l j} Z_{l}\right\}\right\}\right) \\
& \mathbb{P}\left(\prod_{k \in S_{p_{\max }}} \varepsilon_{k} \leq x\right)=c_{2}(x) \mathbb{P}\left(\prod_{k \in S_{p_{\max }}} \varepsilon_{k} \leq x\right)
\end{aligned}
$$

and, since $Z$ and $\varepsilon$ are atom-free it again follows that $\lim _{x \downarrow 1} c_{2}(x)=c_{1}$ and therefore (A.20) holds also for $r=0$.

We next show that $I_{2}(x)=o\left(I_{1}(x)\right)$ as $x \downarrow 1$. Since $I_{12}(x)=o\left(I_{11}(x)\right.$ as $x \downarrow 1$, we can and do assume that

$$
\bar{b}_{j i}=b_{j i} \varepsilon_{j} \prod_{k \in S_{p_{\max }}} \varepsilon_{k}
$$

Moreover, since for all paths $p \in P_{1 j i}$ we have $l \in \operatorname{An}(i)$ if and only if $l \in \operatorname{An}(j)$,

$$
\begin{aligned}
U_{i} & =\bigvee_{l \in \operatorname{An}(i)} \bigvee_{p \in P_{1 i} \backslash P_{1 j i}} d_{l i}(p) \prod_{k \in S_{p} \cup\{l\}} \varepsilon_{k} Z_{l} \vee \bigvee_{l \in \operatorname{An}(j)} \bigvee_{p \in P_{1 j i}} d_{l i}(p) \prod_{k \in S_{p} \cup\{l\}} \varepsilon_{k} Z_{l} \\
& =\bigvee_{l \in \operatorname{An}(i)} \bigvee_{p \in P_{1 i} \backslash P_{1 j i}} d_{l i}(p) \prod_{k \in S_{p} \cup\{l\}} \varepsilon_{k} Z_{l} \vee b_{j i} \prod_{k \in S_{p_{\max }}} \varepsilon_{k} U_{j}
\end{aligned}
$$

by (A.21). If $\bigvee_{l \in \operatorname{An}(i)} \bigvee_{p \in P_{1 i} \backslash P_{1 j i}} d_{l i}(p) \prod_{k \in S_{p} \cup\{l\}} \varepsilon_{k} Z_{l}>b_{j i} \prod_{k \in S_{p_{\max }}} \varepsilon_{k} U_{j}$, then it follows that

$$
U_{i}=\bigvee_{l \in \operatorname{An}(i)} \bigvee_{p \in P_{1 i} \backslash P_{1 j i}} d_{l i}(p) \prod_{k \in S_{p} \cup\{l\}} \varepsilon_{k} Z_{l}
$$

Moreover, it holds by (3.8), (3.4) and (3.2)

$$
U_{i}=\bigvee_{k \in \operatorname{An}(i)} \bar{b}_{k i} \tilde{U}_{k} \geq \bar{b}_{j i} \tilde{U}_{j} \geq b_{j i} \prod_{k \in S_{p_{\max }}} \varepsilon_{k} U_{j}
$$

Hence, $U_{i} / U_{j} \leq b_{j i} x$ implies that $\prod_{k \in S_{p_{\max }}} \varepsilon_{k} \leq x$. Therefore, using (3.7), (A.22) and (A.21) we get

$$
I_{2}(x)=\mathbb{P}\left(\frac{U_{i}}{U_{j}} \leq b_{j i} x, U_{i}>\tilde{U}_{j} \bar{b}_{j i}\right)=\mathbb{P}\left(U_{i} \in\left(\tilde{U}_{j} \bar{b}_{j i}, \tilde{U}_{j} \varepsilon_{j} b_{j i} x\right]\right)
$$

$$
\begin{aligned}
& \leq \mathbb{P}\left(\left\{\prod_{k \in S_{p_{\max }}} \varepsilon_{k} \leq x\right\} \bigcap\right. \\
& \left.\left\{\bigvee_{l \in \operatorname{An}(i)} \bigvee_{p \in P_{l i} \backslash P_{l j i}} d_{l i}(p) \prod_{k \in S_{p} \cup\{l\}} \varepsilon_{k} Z_{l} \in\left(b_{j i} \tilde{U}_{j} \varepsilon_{j} \prod_{k \in S_{p_{\max }}} \varepsilon_{k}, b_{j i} \tilde{U}_{j} \varepsilon_{j} x\right]\right\}\right) \\
& \leq \mathbb{P}\left(\left\{\prod_{k \in S_{p_{\max }}} \varepsilon_{k} \leq x\right\} \bigcap\right. \\
& \left.\left\{\bigvee_{l \in \operatorname{An}(i)} \bigvee_{p \in P_{l i} \backslash P_{l j i}} d_{l i}(p) \prod_{k \in S_{p} \cup\{l\}} \varepsilon_{k} Z_{l} \in\left(b_{j i} \tilde{U}_{j} \varepsilon_{j}, b_{j i} \tilde{U}_{j} \varepsilon_{j} x\right]\right\}\right)
\end{aligned}
$$

since $\varepsilon \geq 1$. Using that $U_{j}=\tilde{U}_{j} \varepsilon_{j}$ and $j \notin S_{p_{\max }}$ and the same argument as in (A.19), we get

$$
\begin{aligned}
& I_{2}(x) \leq \mathbb{P}\left(\left\{\prod_{k \in S_{p_{\max }}} \varepsilon_{k} \leq x\right\} \bigcap\right. \\
& \left\{\bigvee_{l \in \operatorname{An}(i)} \bigvee_{p \in P_{l i} \backslash P_{l j i}} d_{l i}(p) \prod_{k \in\left(S_{p} \cup\{l\}\right) \backslash S_{p_{\max }}} \varepsilon_{k} Z_{l} \in\left(\frac{b_{j i} \tilde{U}_{j} \varepsilon_{j}}{x}, b_{j i} \tilde{U}_{j} \varepsilon_{j} x\right]\right\}\right) \\
& =\mathbb{P}\left(\left\{\prod_{k \in S_{p_{\max }}} \varepsilon_{k} \leq x\right\}\right) \\
& \mathbb{P}\left(\left\{\bigvee_{l \in \operatorname{An}(i)} \bigvee_{p \in P_{l i} \backslash P_{l j i}} \frac{d_{l i}(p)}{\varepsilon_{j}} \prod_{k \in\left(S_{p} \cup\{l\}\right) \backslash S_{p_{\max }}} \varepsilon_{k} Z_{l} \in\left(\frac{b_{j i} \tilde{U}_{j}}{x}, b_{j i} \tilde{U}_{j} x\right]\right\}\right)
\end{aligned}
$$

since $\mathcal{D}$ being acyclic implies that $\tilde{U}_{j}$ and $\varepsilon_{j}$ are independent of $\varepsilon_{k}$ for every $k \in S_{p_{\max }}$. For $x \downarrow 1$ the interval in the second probability gets arbitrarily small. Since the distribution of the noise-variables is atom-free and the left-hand side contains $\varepsilon_{j}$ that is not included in $\tilde{U}_{j}$, this probability tends to zero as $x \downarrow 1$. Comparing this upper bound with (A.20) we can see that $I_{2}(x)=o\left(I_{1}(x)\right)$ as $x \downarrow 1$. Since $I_{12}(x)=o\left(I_{11}(x)\right)$, we have

$$
I(x) \sim I_{1}(x) \sim I_{11}(x) \sim c_{1} \mathbb{P}\left(\prod_{k \in S_{p_{\max }}} \varepsilon_{k} \leq x\right), \quad x \downarrow 1
$$

holds, where the last asymptotic equivalence follows from (A.20). Moreover, we have by (A.9), using (3.2), (3.4) and (3.7),

$$
\begin{aligned}
I(x) \sim I_{11}(x) & =\mathbb{P}\left(\bigvee_{p \in P_{j i}} d_{j i}(p) \prod_{k \in S_{p}} \varepsilon_{k} \leq b_{j i} x, \bar{d}_{j i}\left(p_{\max }\right)=\bar{b}_{j i}, U_{i}=\tilde{U}_{j} \bar{b}_{j i}\right) \\
& =\mathbb{P}\left(\bar{d}_{j i}\left(p_{\max }\right) / \varepsilon_{j} \leq b_{j i} x, U_{i}=\tilde{U}_{j} \bar{d}_{j i}\left(p_{\max }\right)\right) \\
& =\mathbb{P}\left(\prod_{k \in S_{p_{\max }}} \varepsilon_{k} \leq x, U_{i}=U_{j} b_{j i} \prod_{k \in S_{p_{\max }}} \varepsilon_{k}\right), \quad x \downarrow 1
\end{aligned}
$$

which, together with (A.24), proves the result.

Proof of Corollary 3.14. We first show the result for $P_{j i} \backslash\left\{p_{1}, \ldots, p_{n}\right\} \neq$ $\emptyset$, i.e., there exists a path $p$ from $j$ to $i$ with $d_{j i}<b_{j i}$. We start as in the proof of Theorem 3.12 for $x \geq 1$

$$
I(x)=I_{1}(x)+I_{2}(x)
$$

and similarly to (A.8), we again apply the law of total probability to $I_{1}(x)$

$$
\begin{aligned}
I_{1}(x) & =\mathbb{P}\left(\bigvee_{p \in P_{j i}} d_{j i}(p) \prod_{k \in S_{p}} \varepsilon_{k} \leq b_{j i} x, U_{i}=\tilde{U}_{j} \bar{b}_{j i}\right) \\
& =\mathbb{P}\left(\bigvee_{p \in P_{j i}} d_{j i}(p) \prod_{k \in S_{p}} \varepsilon_{k} \leq b_{j i} x, \bigvee_{p \in\left\{p_{1}, \ldots, p_{n}\right\}} \bar{d}_{j i}(p)=\bar{b}_{j i}, U_{i}=\tilde{U}_{j} \bar{b}_{j i}\right) \\
& +\mathbb{P}\left(\bigvee_{p \in P_{j i}} d_{j i}(p) \prod_{k \in S_{p}} \varepsilon_{k} \leq b_{j i} x, \bigvee_{p \in P_{j i} \backslash\left\{p_{1}, \ldots, p_{n}\right\}} \bar{d}_{j i}(p)=\bar{b}_{j i}, U_{i}=\tilde{U}_{j} \bar{b}_{j i}\right) \\
& =\mathbb{P}\left(\bigvee_{p \in P_{j i}} d_{j i}(p) \prod_{k \in S_{p}} \varepsilon_{k} \leq b_{j i} x, \bigvee_{p \in P_{j i} \backslash\left\{p_{1}, \ldots, p_{n}\right\}} \bar{d}_{j i}(p) \leq\right. \\
& \bigvee_{p \in\left\{p_{1}, \ldots, p_{n}\right\}} \bar{d}_{j i}(p), U_{i}=\tilde{U}_{j} \bar{b}_{j i}\right)+\mathbb{P}\left(\bigvee_{p \in P_{j i}} d_{j i}(p) \prod_{k \in S_{p}} \varepsilon_{k} \leq b_{j i} x\right. \\
& \bigvee_{p \in P_{j i} \backslash\left\{p_{1}, \ldots, p_{n}\right\}} \bar{d}_{j i}(p)>\bigvee_{p \in\left\{p_{1}, \ldots, p_{n}\right\}} \bar{d}_{j i}(p), U_{i}=\tilde{U}_{j} \bar{b}_{j i}) \\
& =: \tilde{I}_{11}(x)+\tilde{I}_{12}(x) .
\end{aligned}
$$

With the same arguments as in the proof of Theorem 3.12 we find upper and lower bounds for $\tilde{I}_{11}(x)$. Analogously to (A.12) and (A.13) we find

$$
\begin{aligned}
& \tilde{I}_{11}(x)=\mathbb{P}\left(\bigcap_{p \in P_{j i} \backslash\left\{p_{1}, \ldots, p_{n}\right\}}\left\{\prod_{k \in S_{p}} \varepsilon_{k} \leq \frac{b_{j i}}{d_{j i}(p)} \bigvee_{\tilde{p} \in\left\{p_{1}, \ldots, p_{n}\right\}} \prod_{k \in S_{\tilde{p}}} \varepsilon_{k}\right\} \bigcap\right. \\
& \bigcap_{p \in\left\{p_{1}, \ldots, p_{n}\right\}}\left\{\prod_{k \in S_{p}} \varepsilon_{k} \leq x\right\} \bigcap \bigcap_{l \in \operatorname{An}(i)}\left\{\bigcap_{p \in P_{l i} \backslash P_{l j i}}\left\{d_{l i}(p) \prod_{k \in S_{p} \cup\{l\}} \varepsilon_{k} Z_{l} \leq\right.\right. \\
& \left.\left.b_{j i} \bigvee_{\tilde{p} \in\left\{p_{1}, \ldots, p_{n}\right\}} \prod_{k \in S_{\tilde{p}}} \varepsilon_{k} \bigvee_{l \in \operatorname{An}(j)} \bar{b}_{l j} Z_{l}\right\}\right\}\right) \\
& \geq \mathbb{P}\left(\bigcap_{p \in P_{j i} \backslash\left\{p_{1}, \ldots, p_{n}\right\}}\left\{\prod_{k \in S_{p} \backslash\left(\cup_{i=1}^{n} S_{p_{i}}\right)} \varepsilon_{k} \leq \frac{b_{j i}}{d_{j i}(p)}\right\} \bigcap \bigcap_{p \in\left\{p_{1}, \ldots, p_{n}\right\}}\left\{\prod_{k \in S_{p}} \varepsilon_{k} \leq x\right\}\right. \\
& \bigcap \bigcap_{l \in \operatorname{An}(i)}\left\{\bigcap_{p \in P_{l i} \backslash P_{l j i}}\left\{d_{l i}(p) \prod_{k \in S_{p} \cup\{l\} \backslash\left(\cup_{i=1}^{n} S_{p_{i}}\right\}} \varepsilon_{k} Z_{l} \leq b_{j i} \bigvee_{l \in \operatorname{An}(j)} \bar{b}_{l j} Z_{l}\right\}\right\}\right) \\
& =c_{1} \mathbb{P}\left(\bigcap_{p \in\left\{p_{1}, \ldots, p_{n}\right\}}\left\{\prod_{k \in S_{p}} \varepsilon_{k} \leq x\right\}\right)
\end{aligned}
$$

and analogously to (A.16) we have

$$
\tilde{I}_{11}(x) \leq \mathbb{P}\left(\bigcap_{p \in P_{j i} \backslash\left\{p_{1}, \ldots, p_{n}\right\}}\left\{\prod_{k \in S_{p} \backslash\left(\cup_{i=1}^{n} S_{p_{i}}\right)} \varepsilon_{k} \leq \frac{b_{j i}}{d_{j i}(p)} x\right\} \bigcap\right.
$$

$$
\begin{aligned}
& \bigcap_{p \in\left\{p_{1}, \ldots, p_{n}\right\}}\left\{\prod_{k \in S_{p}} \varepsilon_{k} \leq x\right\} \\
& \bigcap_{l \in \operatorname{An}(i)}\left\{\bigcap_{p \in P_{l i} \backslash P_{l j i}}\left\{d_{l i}(p) \prod_{k \in S_{p} \cup\{l\} \backslash\left(\cup_{i=1}^{n} S_{p_{i}}\right)} \varepsilon_{k} Z_{l} \leq b_{j i} x \bigvee_{l \in \operatorname{An}(j)} \bar{b}_{l j} Z_{l}\right\}\right\}\right) \\
& =c_{2}(x) \mathbb{P}\left(\bigcap_{p \in\left\{p_{1}, \ldots, p_{n}\right\}}\left\{\prod_{k \in S_{p}} \varepsilon_{k} \leq x\right\}\right)
\end{aligned}
$$

With the same arguments as in the previous proof, we can show that $c_{1} \in(0,1)$ and $c_{2}(x) \rightarrow c_{1}$ for $x \downarrow 1$ and $\tilde{I}_{12}(x)=o\left(\tilde{I}_{11}(x)\right)$ and $I_{2}(x)=o\left(I_{1}(x)\right)$. Hence, the result follows. If $P_{j i} \backslash\left\{p_{1}, \ldots, p_{n}\right\}=\emptyset$ the result follows analogously.

Proof of Corollary 3.15 From Theorem 3.12 we have as $x \downarrow 1$,

$$
\begin{aligned}
& \mathbb{P}\left(\bigwedge_{k=0}^{n} \frac{U_{i}^{k}}{U_{j}^{k}} \leq b_{j i} x\right)=1-\left(1-\mathbb{P}\left(\frac{U_{i}}{U_{j}} \leq b_{j i} x\right)\right)^{n} \\
& =1-(1-c(1+o(1)) \mathbb{P}\left(\prod_{k \in S_{p}} \varepsilon_{k} \leq x\right))^{n} \\
& =1-\sum_{k=0}^{n}\binom{n}{k}(-c(1+o(1)) \mathbb{P}\left(\prod_{k \in S_{p}} \varepsilon_{k} \leq x\right))^{k} \sim c n \mathbb{P}\left(\prod_{i=1}^{n} \varepsilon_{k_{i}} \leq x\right)
\end{aligned}
$$

where we have used the binomial theorem and the fact that the summands for $k \geq 2$ are negligible when $n$ is fixed.

Proof of Theorem 3.16. We give a proof for $P_{j i} \backslash\left\{p_{1}\right\} \neq \emptyset$ and $P_{l m} \backslash$ $\left\{p_{2}\right\} \neq \emptyset$, i.e., $p_{1}$ and $p_{2}$ are not the only paths from $j$ to $i$ and from $l$ to $m$, respectively. All other cases follow analogously. By the law of total probability, we have

$$
\begin{aligned}
& \mathbb{P}\left(\frac{U_{i}}{U_{j}} \leq b_{j i} x_{1}, \frac{U_{m}}{U_{l}} \leq b_{l m} x_{2}\right) \\
= & \mathbb{P}\left(\prod_{k \in S_{p_{1}}} \varepsilon_{k} \leq x_{1}, \prod_{k \in S_{p_{2}}} \varepsilon_{k} \leq x_{2}, U_{i}=U_{j} b_{j i} \prod_{k \in S_{p_{1}}} \varepsilon_{k}, U_{m}=U_{l} b_{l m} \prod_{k \in S_{p_{2}}} \varepsilon_{k}\right) \\
+ & \mathbb{P}\left(\prod_{k \in S_{p_{1}}} \varepsilon_{k} \leq x_{1}, \frac{U_{m}}{U_{l}} \leq b_{l m} x_{2}, U_{i}=U_{j} b_{j i} \prod_{k \in S_{p_{1}}} \varepsilon_{k}, U_{m} \neq U_{l} b_{l m} \prod_{k \in S_{p_{2}}} \varepsilon_{k}\right) \\
+ & \mathbb{P}\left(\frac{U_{i}}{U_{j}} \leq b_{j i} x_{1}, \prod_{k \in S_{p_{2}}} \varepsilon_{k} \leq x_{2}, U_{i} \neq U_{j} b_{j i} \prod_{k \in S_{p_{1}}} \varepsilon_{k}, U_{m}=U_{l} b_{l m} \prod_{k \in S_{p_{2}}} \varepsilon_{k}\right) \\
+ & \mathbb{P}\left(\frac{U_{i}}{U_{j}} \leq b_{j i} x_{1}, \frac{U_{m}}{U_{l}} \leq b_{l m} x_{2}, U_{i} \neq U_{j} b_{j i} \prod_{k \in S_{p_{1}}} \varepsilon_{k}, U_{m} \neq U_{l} b_{l m} \prod_{k \in S_{p_{2}}} \varepsilon_{k}\right) \\
= & I_{1}\left(x_{1}, x_{2}\right)+I_{2}\left(x_{1}, x_{2}\right)+I_{3}\left(x_{1}, x_{2}\right)+I_{4}\left(x_{1}, x_{2}\right)
\end{aligned}
$$

We first consider $I_{1}\left(x_{1}, x_{2}\right)$. Observe that for $I_{11}(x)$ defined in (A.9) we have by (A.25)

$$
I_{11}(x)=\mathbb{P}\left(\prod_{k \in S_{p_{\max }}} \varepsilon_{k} \leq x, U_{i}=U_{j} b_{j i} \prod_{k \in S_{p_{\max }}} \varepsilon_{k}\right)
$$

and hence, $I_{1}\left(x_{1}, x_{2}\right)$ is the bivariate extension to $I_{11}(x)$. For this reason, we can follow the proof of Theorem 3.12 at (A.11), we again find upper and lower bounds based on the decomposition

$$
\begin{aligned}
& \left\{\bigvee_{p \in P_{j i} \backslash\left\{p_{1}\right\}} \prod_{k \in S_{p}} \varepsilon_{k} \leq \frac{b_{j i}}{d_{j i}(p)} \prod_{k \in S_{p_{1}}} \varepsilon_{k}\right\} \cap\left\{\bigvee_{p \in P_{l m} \backslash\left\{p_{2}\right\}} \prod_{k \in S_{p}} \varepsilon_{k} \leq \frac{b_{l m}}{d_{l m}(p)} \prod_{k \in S_{p_{2}}} \varepsilon_{k}\right\} \cap \\
& \left\{\prod_{k \in S_{p_{1}}} \varepsilon_{k} \leq x_{1}\right\} \cap \bigcap_{n \in \operatorname{An}(i)}\left\{\bigcap_{p \in P_{n i} \backslash P_{n j i}}\left\{d_{n i}(p) \prod_{k \in S_{p} \cup\{n\}} \varepsilon_{k} Z_{n} \leq\right.\right. \\
& \left.b_{j i} \prod_{k \in S_{p_{1}}} \varepsilon_{k} \bigvee_{n \in \operatorname{An}(j)} \bar{b}_{n j} Z_{n}\right\}\right\} \cap\left\{\prod_{k \in S_{p_{2}}} \varepsilon_{k} \leq x_{2}\right\} \cap \\
& \bigcap_{n \in \operatorname{An}(m)}\left\{\bigcap_{p \in P_{n m} \backslash P_{n l m}}\left\{d_{n m}(p) \prod_{k \in S_{p} \cup\{n\}} \varepsilon_{k} Z_{n} \leq b_{l m} \prod_{k \in S_{p_{2}}} \varepsilon_{k} \bigvee_{n \in \operatorname{An}(l)} \bar{b}_{n l} Z_{n}\right\}\right\} .
\end{aligned}
$$

Now for three paths $p, p_{1}$ and $p_{2}$ and a node $i$ we denote

$$
S_{p+i \backslash p_{1}+p_{2}}:=\left(S_{p} \cup\{i\}\right) \backslash\left(S_{p_{1}} \cup S_{p_{2}}\right) \quad \text { and } \quad S_{p \backslash p_{1}+p_{2}}:=S_{p} \backslash\left(S_{p_{1}} \cup S_{p_{2}}\right)
$$

On the set $\left\{\prod_{k \in S_{p_{1}}} \varepsilon_{k} \leq x_{1}\right\} \cap\left\{\prod_{k \in S_{p_{2}}} \varepsilon_{k} \leq x_{2}\right\}$ we have for $x_{1}, x_{2}>1$, since $\varepsilon>1$,

$$
\begin{aligned}
& \left\{\bigvee_{p \in P_{j i} \backslash\left\{p_{1}\right\}} \prod_{k \in S_{p}} \varepsilon_{k} \leq \frac{b_{j i}}{d_{j i}(p)} \prod_{k \in S_{p_{1}}} \varepsilon_{k}\right\} \\
= & \left\{\bigvee_{p \in P_{j i} \backslash\left\{p_{1}\right\}} \prod_{k \in S_{p} \backslash S_{p_{1}}} \varepsilon_{k} \leq \frac{b_{j i}}{d_{j i}(p)} \prod_{k \in S_{p_{1}} \backslash S_{p}} \varepsilon_{k}\right\} \\
\supseteq & \left\{\bigvee_{p \in P_{j i} \backslash\left\{p_{1}\right\}} \prod_{k \in S_{p} \backslash S_{p_{1}}} \varepsilon_{k} \leq \frac{b_{j i}}{d_{j i}(p)}\right\} \supseteq\left\{\bigvee_{p \in P_{j i} \backslash\left\{p_{1}\right\}} \prod_{k \in S_{p \backslash p_{1}+p_{2}}} \varepsilon_{k} \leq \frac{b_{j i}}{d_{j i}(p) x_{2}}\right\}
\end{aligned}
$$

as well as

$$
\begin{aligned}
& \bigcap_{n \in \operatorname{An}(i)}\left\{\bigcap_{p \in P_{n i} \backslash P_{n j i}}\left\{d_{n i}(p) \prod_{k \in S_{p} \cup\{n\}} \varepsilon_{k} Z_{n} \leq b_{j i} \prod_{k \in S_{p_{1}}} \varepsilon_{k} \bigvee_{n \in \operatorname{An}(j)} \bar{b}_{n j} Z_{n}\right\}\right\} \\
= & \bigcap_{n \in \operatorname{An}(i)}\left\{\bigcap_{p \in P_{n i} \backslash P_{n j i}}\left\{d_{n i}(p) \prod_{k \in\left(S_{p} \cup\{n\}\right) \backslash S_{p_{1}}} \varepsilon_{k} Z_{n} \leq b_{j i} \prod_{k \in S_{p_{1}} \backslash S_{p}} \varepsilon_{k}\right.\right. \\
& \left.\bigvee_{n \in \operatorname{An}(j)} \bar{b}_{n j} Z_{n}\right\}\right\} \supseteq \bigcap_{n \in \operatorname{An}(i)}\left\{\bigcap_{p \in P_{n i} \backslash P_{n j i}}\left\{d_{n i}(p) \prod_{k \in\left(S_{p} \cup\{n\}\right) \backslash S_{p_{1}}} \varepsilon_{k} Z_{n} \leq\right.\right. \\
& \left.\left.b_{j i} \bigvee_{n \in \operatorname{An}(j)} \bigvee_{p \in P_{n j}} d_{n j}(\tilde{p}) \prod_{k \in S_{\tilde{p}+n \backslash p_{1}+p_{2}}} \varepsilon_{k} Z_{n}\right\}\right\}
\end{aligned}
$$

$$
\begin{aligned}
& \geqslant \bigcap_{n \in \operatorname{An}(i)}\left\{\bigcap_{p \in P_{n i} \backslash P_{n j i}}\left\{d_{n i}(p) \prod_{k \in S_{p+n \backslash p_{1}+p_{2}}} \varepsilon_{k} Z_{n} \leq\right.\right. \\
& \left.\left.\frac{b_{j i}}{x_{2}} \bigvee_{n \in \operatorname{An}(j)} \bigvee_{\tilde{p} \in P_{n j}} d_{n j}(\tilde{p}) \prod_{k \in S_{\tilde{p}+n \backslash p_{1}+p_{2}}} \varepsilon_{k} Z_{n}\right\}\right\}
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
& I_{1}\left(x_{1}, x_{2}\right) \geq \mathbb{P}\left(\left\{\bigvee_{p \in P_{j i} \backslash\left\{p_{1}\right\}} \prod_{k \in S_{p \backslash p_{1}+p_{2}}} \varepsilon_{k} \leq \frac{b_{j i}}{d_{j i}(p) x_{2}}\right\} \bigcap\left\{\bigvee_{p \in P_{l m} \backslash\left\{p_{1}\right\}} \prod_{k \in S_{p \backslash p_{1}+p_{2}}}\right.\right. \\
& \left.\varepsilon_{k} \leq \frac{b_{l m}}{d_{l m}(p) x_{1}}\right\} \bigcap_{n \in \operatorname{An}(i)}\left\{\bigcap_{p \in P_{n i} \backslash P_{n j i}}\left\{d_{n i}(p) \prod_{k \in S_{p+n \backslash p_{1}+p_{2}}} \varepsilon_{k} Z_{n} \leq \frac{b_{j i}}{x_{2}} \bigvee_{n \in \operatorname{An}(j)}\right.\right. \\
& \left.\left.\bigvee_{\tilde{p} \in P_{n j}} d_{n j}(\tilde{p}) \prod_{k \in S_{\tilde{p}+n \backslash p_{1}+p_{2}}} \varepsilon_{k} Z_{n}\right\}\right\} \bigcap_{n \in \operatorname{An}(m)}\left\{\bigcap_{p \in P_{n m} \backslash P_{n l m}}\left\{d_{n m}(p) \prod_{k \in S_{p+n \backslash p_{1}+p_{2}}}\right.\right. \\
& \left.\left.\varepsilon_{k} Z_{n} \leq \frac{b_{l m}}{x_{1}} \bigvee_{n \in \operatorname{An}(l)} \bigvee_{\tilde{p} \in P_{n l}} d_{n l}(\tilde{p}) \prod_{k \in S_{\tilde{p}+n \backslash p_{1}+p_{2}}} \varepsilon_{k} Z_{n}\right\}\right\} \\
& \bigcap\left\{\prod_{k \in S_{p_{1}}} \varepsilon_{k} \leq x_{1}\right\} \bigcap\left\{\prod_{k \in S_{p_{2}}} \varepsilon_{k} \leq x_{2}\right\}\right) \\
& =: c_{3}\left(x_{1}, x_{2}\right) \mathbb{P}\left(\left\{\prod_{k \in S_{p_{1}}} \varepsilon_{k} \leq x_{1}\right\} \bigcap\left\{\prod_{k \in S_{p_{2}}} \varepsilon_{k} \leq x_{2}\right\}\right)
\end{aligned}
$$

For an upper bound, observe that on $\left\{\prod_{k \in S_{p_{1}}} \varepsilon_{k} \leq x_{1}\right\} \cap\left\{\prod_{k \in S_{p_{2}}} \varepsilon_{k} \leq x_{2}\right\}$ we have

$$
\begin{aligned}
& \left\{\bigvee_{p \in P_{j i} \backslash\left\{p_{1}\right\}} \prod_{k \in S_{p}} \varepsilon_{k} \leq \frac{b_{j i}}{d_{j i}(p)} \prod_{k \in S_{p_{1}}} \varepsilon_{k}\right\}=\left\{\bigvee_{p \in P_{j i} \backslash\left\{p_{1}\right\}} \prod_{k \in S_{p} \backslash S_{p_{1}}} \varepsilon_{k} \leq \frac{b_{j i}}{d_{j i}(p)}\right. \\
& \left.\prod_{k \in S_{p_{1}} \backslash S_{p}} \varepsilon_{k}\right\} \subseteq\left\{\bigvee_{p \in P_{j i} \backslash\left\{p_{1}\right\}} \prod_{k \in S_{p} \backslash S_{p_{1}}} \varepsilon_{k} \leq \frac{b_{j i} x_{1}}{d_{j i}(p)}\right\} \\
& \subseteq\left\{\bigvee_{p \in P_{j i} \backslash\left\{p_{1}\right\}} \prod_{k \in S_{p \backslash p_{1}+p_{2}}} \varepsilon_{k} \leq \frac{b_{j i} x_{1}}{d_{j i}(p)}\right\}
\end{aligned}
$$

as well as

$$
\begin{aligned}
& \bigcap_{n \in \operatorname{An}(i)}\left\{\bigcap_{p \in P_{n i} \backslash P_{n j i}}\left\{d_{n i}(p) \prod_{k \in S_{p} \cup\{n\}} \varepsilon_{k} Z_{n} \leq b_{j i} \prod_{k \in S_{p_{1}}} \varepsilon_{k} \bigvee_{n \in \operatorname{An}(j)} \bar{b}_{n j} Z_{n}\right\}\right\} \\
& \subseteq \bigcap_{n \in \operatorname{An}(i)}\left\{\bigcap_{p \in P_{n i} \backslash P_{n j i}}\left\{d_{n i}(p) \prod_{k \in\left(S_{p} \cup\{n\}\right) \backslash S_{p_{1}}} \varepsilon_{k} Z_{n} \leq\right.\right. \\
& \left.\left.b_{j i} x_{1} x_{2} \bigvee_{n \in \operatorname{An}(j)} \bigvee_{\tilde{p} \in P_{n j}} d_{n j}(\tilde{p}) \prod_{k \in S_{\tilde{p}+n \backslash p_{1}+p_{2}}} \varepsilon_{k} Z_{n}\right\}\right\} \\
& \subseteq \bigcap_{n \in \operatorname{An}(i)}\left\{\bigcap_{p \in P_{n i} \backslash P_{n j i}}\left\{d_{n i}(p) \prod_{k \in S_{p+n \backslash p_{1}+p_{2}}} \varepsilon_{k} Z_{n} \leq\right.\right.
\end{aligned}
$$

$$
b_{j i} x_{1} x_{2} \bigvee_{n \in \operatorname{An}(j)} \bigvee_{\tilde{p} \in P_{n j}} d_{n j}(\tilde{p}) \prod_{k \in S_{\tilde{p}+n \backslash p_{1}+p_{2}}} \varepsilon_{k} Z_{n}\}
$$

For this reason,

$$
I_{1}\left(x_{1}, x_{2}\right) \leq c_{4}\left(x_{1}, x_{2}\right) \mathbb{P}\left(\left\{\prod_{k \in S_{p_{1}}} \varepsilon_{k} \leq x_{1}\right\} \bigcap\left\{\prod_{k \in S_{p_{2}}} \varepsilon_{k} \leq x_{2}\right\}\right)
$$

with

$$
\begin{aligned}
& c_{4}\left(x_{1}, x_{2}\right):=\mathbb{P}\left(\left\{\bigvee_{p \in P_{j i} \backslash\left\{p_{1}\right\}} \prod_{k \in S_{p \backslash p_{1}+p_{2}}} \varepsilon_{k} \leq \frac{b_{j i} x_{1}}{d_{j i}(p)}\right\} \bigcap\left\{\bigvee_{p \in P_{l m} \backslash\left\{p_{1}\right\}} \prod_{k \in S_{p \backslash p_{1}+p_{2}}}\right.\right. \\
& \varepsilon_{k} \leq \frac{b_{l m} x_{2}}{d_{l m}(p)}\left\{\bigcap_{n \in \operatorname{An}(i)}\left\{\bigcap_{p \in P_{n i} \backslash P_{n j i}}\left\{d_{n i}(p) \prod_{k \in S_{p+n \backslash p_{1}+p_{2}}} \varepsilon_{k} Z_{n} \leq b_{j i} x_{1} x_{2}\right.\right.\right. \\
& \left.\left.\bigvee_{n \in \operatorname{An}(j)} \bigvee_{p \in P_{n j}} d_{n j}(\tilde{p}) \prod_{k \in S_{\tilde{p}+n \backslash p_{1}+p_{2}}} \varepsilon_{k} Z_{n}\right\}\right\} \bigcap_{n \in \operatorname{An}(m)}\left\{\bigcap_{p \in P_{n m} \backslash P_{n l m}}\left\{d_{n m}(p)\right.\right. \\
& \left.\left.\prod_{k \in S_{p+n \backslash p_{1}+p_{2}}} \varepsilon_{k} Z_{n} \leq b_{l m} x_{1} x_{2} \bigvee_{n \in \operatorname{An}(l)} \bigvee_{p \in P_{n l}} d_{n l}(\tilde{p}) \prod_{k \in S_{\tilde{p}+n \backslash p_{1}+p_{2}}} \varepsilon_{k} Z_{n}\right\}\right\} \text { ). }
\end{aligned}
$$

Since all random variables are continuous, $c_{4}\left(x_{1}, x_{2}\right)$ tends to $c_{3}\left(x_{1}, x_{2}\right)$ for $x_{1}, x_{2} \downarrow 1$, and

$$
c_{3}\left(x_{1}, x_{2}\right) \leq c \leq c_{4}\left(x_{1}, x_{2}\right)
$$

with

$$
\begin{aligned}
& c:=\mathbb{P}\left(\left\{\bigvee_{p \in P_{j i} \backslash\left\{p_{1}\right\}} \prod_{k \in S_{p \backslash p_{1}+p_{2}}} \varepsilon_{k} \leq \frac{b_{j i}}{d_{j i}(p)}\right\} \bigcap\left\{\bigvee_{p \in P_{l m} \backslash\left\{p_{1}\right\}} \prod_{k \in S_{p \backslash p_{1}+p_{2}}} \varepsilon_{k} \leq\right.\right. \\
& \frac{b_{l m}}{d_{l m}(p)}\left\{\bigcap_{n \in \operatorname{An}(i)}\left\{\bigcap_{p \in P_{n i} \backslash P_{n j i}}\left\{d_{n i}(p) \prod_{k \in S_{p+n \backslash p_{1}+p_{2}}} \varepsilon_{k} Z_{n} \leq b_{j i} \bigvee_{n \in \operatorname{An}(j)} \bigvee_{p \in P_{n j}}\right.\right.\right. \\
& \left.\left.d_{n j}(\tilde{p}) \prod_{k \in S_{\tilde{p}+n \backslash p_{1}+p_{2}}} \varepsilon_{k} Z_{n}\right\}\right\} \bigcap_{n \in \operatorname{An}(m)}\left\{\bigcap_{p \in P_{n m} \backslash P_{n l m}}\left\{d_{n m}(p) \prod_{k \in S_{p+n \backslash p_{1}+p_{2}}} \varepsilon_{k} Z_{n}\right.\right. \\
& \left.\left.\left.\leq b_{l m} \bigvee_{n \in \operatorname{An}(l)} \bigvee_{p \in P_{n l}} d_{n l}(\tilde{p}) \prod_{k \in S_{\tilde{p}+n \backslash p_{1}+p_{2}}} \varepsilon_{k} Z_{n}\right\}\right\}\right) .
\end{aligned}
$$

Since $i \neq m$ we can use the same arguments as for $c_{1}$ in the proof of Theorem 3.12 to show that $c>0$. Therefore, we only need to show that $I_{i}\left(x_{1}, x_{2}\right)=$ $o\left(I_{1}\left(x_{1}, x_{2}\right)\right)$ for $i \in\{2,3,4\}$. It is obvious that $I_{2}\left(x_{1}, x_{2}\right)=o\left(I_{1}\left(x_{1}, x_{2}\right)\right)$ implies the other two cases. Using the same arguments from the proof of Theorem 3.12 regarding $I_{2}(x)=o\left(I_{1}(x)\right)$ and $I_{12}(x)=o\left(I_{11}\right)(x)$, the result follows.

# Appendix B: Proofs of Section 4 

Proof of Proposition 4.3 We first consider the convergence of the simple minimum ratio $\bigwedge_{k=1}^{n}\left(U_{i}^{k} / U_{j}^{k}\right)$. For $j=i$ the result is obvious. Moreover, for

$j \in \operatorname{an}(i)$ we have with Lemma 3.8 d$)$, for $x>0$,

$$
\lim _{n \rightarrow \infty} \mathbb{P}\left(\left|\bigwedge_{k=1}^{n} \frac{U_{i}^{k}}{U_{j}^{k}}-b_{j i}\right|>x\right)=\lim _{n \rightarrow \infty}\left(\mathbb{P}\left(\frac{U_{i}}{U_{j}}-b_{j i}>x\right)\right)^{n}=0
$$

showing that the minimum ratio converges for $n \rightarrow \infty$ in probability to $b_{j i}$. Since $\bigwedge_{k=1}^{n} U_{i}^{k} / U_{j}^{k}$ is non-increasing, it converges almost surely. For $j \notin \operatorname{an}(i)$ we have $b_{j i}=0$ and the same result holds. Therefore, the estimators (4.1), (4.4) and (4.5) converge almost surely. Considering the inequality (4.3) for the estimator (4.2), this estimator as well converges almost surely. Finally using (4.7) and (4.8), the same also holds for the estimator (4.10).

Proof of Lemma 4.4 Assume first that the output $\hat{\boldsymbol{B}}$ is not idempotent. Then there exists an entry $\hat{b}_{j i}$ in $\hat{\boldsymbol{B}}$ such that $\hat{b}_{j i}<\hat{b}_{j k} \hat{b}_{k i}$. Therefore, since the input matrix $\hat{\boldsymbol{B}}$ is idempotent, we have $\hat{b}_{j i}=0$ while $\hat{b}_{j k}>0$ and $\hat{b}_{k i}>0$. This is a contradiction to the if-condition on line 9 in the algorithm.

Now assume that there is an idempotent matrix $\boldsymbol{B}^{\prime}$ that preserves all values that are larger than $\delta_{1}$ but contains more zero entries. Then there is an entry $b_{j i}^{\prime}$ such that $b_{j i}^{\prime}=0$ while $\hat{b}_{j i}>0$. Since $\hat{b}_{j i}>0$ there must be some $k \in$ $\{j+1, \ldots, i-1\}$ such that $\hat{b}_{j k} \notin S$ and $\hat{b}_{k i} \notin S$, otherwise we would have set $\hat{b}_{j i}$ equal to zero. Because we sort pairs $(j, i)$ by distance and $(j, k)$ and $(k, i)$ both have smaller distance it must also hold that both, $\hat{b}_{j k}$ and $\hat{b}_{k i}$ are strictly greater than zero. In comparison, since $\boldsymbol{B}^{\prime}$ is idempotent, either $b_{j k}^{\prime}$ or $b_{k i}^{\prime}$ is equal to zero.

Therefore, we have $b_{j k}^{\prime}=0$ while $\hat{b}_{j k}>0$ or $b_{k i}^{\prime}=0$ while $\hat{b}_{k i}>0$. In both cases, the distance compared to the pair $(j, i)$ is decreased. Repeating this argument we can assume that $(j-i)=1$. This, however, leads to a contradiction since $\hat{b}_{j i}$ is set to zero for all pairs $(j, i)$ of distance one if $\hat{b}_{j i}<\delta_{1}$.

# Appendix C: Proofs of Section 5 

Proof of Lemma 5.1 By Theorem 3.12 we get for $x \downarrow 1$,

$$
\begin{aligned}
& \lim _{t \downarrow 0} \frac{\mathbb{P}\left(\ln \left(U_{i} / U_{j}\right)-\ln \left(b_{j i}\right) \leq t x\right)}{\mathbb{P}\left(\ln \left(U_{i} / U_{j}\right)-\ln \left(b_{j i}\right) \leq t\right)}=\lim _{t \downarrow 0} \frac{\mathbb{P}\left(U_{i} / U_{j} \leq b_{j i} \exp (t x)\right)}{\mathbb{P}\left(U_{i} / U_{j} \leq b_{j i} \exp (t)\right)} \\
= & \lim _{t \downarrow 0} \frac{c \mathbb{P}\left(\prod_{k \in S_{p}} \varepsilon_{k} \leq \exp (t x)\right)}{c \mathbb{P}\left(\prod_{k \in S_{p}} \varepsilon_{k} \leq \exp (t)\right)}=\lim _{t \downarrow 0} \frac{\mathbb{P}\left(\sum_{k \in S_{p}} \ln \left(\varepsilon_{k}\right) \leq t x\right)}{\mathbb{P}\left(\sum_{k \in S_{p}} \ln \left(\varepsilon_{k}\right) \leq t\right)}=x^{\zeta(p) \alpha}
\end{aligned}
$$

for $\zeta(p)=\left|S_{p}\right|$ by Corollary 2.6 a) and the fact that $\ln \left(\varepsilon_{k}\right) \in R V_{\alpha}^{0}$.
For the proof of Theorem 5.2 we need the following distribution family.
Definition C.1. A positive random variable $Y$ is Fréchet distributed with shape $\alpha>0$ and scale $s>0$ and we write $Y \sim \operatorname{Fréchet}(\alpha, s)$ if the distribution

function of $Y$ is given by

$$
\Phi_{\alpha, s}(x)=\exp \left(-\binom{x}{s}^{-\alpha}\right), \quad x>0
$$

The proof of Theorem 5.2 is divided into a proof of the one-dimensional marginal limit distributions, followed by the proof of the multidimensional result. We start with the one-dimensional limits.

Proposition C.2. Let $\boldsymbol{U}$ be a recursive ML vector with propagating noise on a DAG $\mathcal{D}$ as defined in (3.1) and assume that the path $p:=[j \rightarrow \cdots \rightarrow i]$ from $j$ to $i$ is generic. Assume further that $\tilde{\varepsilon}=\ln (\varepsilon) \in R V_{n}^{0}$. For the node set $S_{p}$ choose $a_{n} \sim F_{\sum_{k \in S_{p}} \tilde{\varepsilon}_{k}}^{+-}(1 / n)$ as $n \rightarrow \infty$. Let $\boldsymbol{U}^{1}, \ldots, \boldsymbol{U}^{n}$ be an iid sample from $\boldsymbol{U}$. Then

$$
\lim _{n \rightarrow \infty} \mathbb{P}\left(\frac{1}{a_{n} b_{j i}}\left(\bigwedge_{k=1}^{n} U_{i}^{k} / U_{j}^{k}-b_{j i}\right) \leq x\right)=\Psi_{\left\{\zeta(p) \alpha, c^{1 /(\zeta(p) \alpha)}\right\}}(x), \quad x>0
$$

for the same constant $c$ as in Theorem 3.12, and $\Psi_{\alpha, s}$ denotes the Weibull distribution from Definition 2.2 with $x_{L}=0$.

Proof. Define $X:=\ln \left(U_{i} / U_{j}\right)-\ln \left(b_{j i}\right)$ with distribution function $F_{X}$. Then by Lemma 5.1, $X \in R V_{\zeta(p) \alpha}^{0}$, which implies that $1 / X \in R V_{\zeta(p) \alpha}^{\infty}$. Using e.g. Theorem 3.3.7 of [11], for

$$
a_{1 / X}(n) \sim F_{1 / X}^{+-}(1-1 / n) \sim 1 / F_{X}^{+-}(1 / n) \rightarrow \infty, \quad n \rightarrow \infty
$$

we get

$$
\begin{aligned}
& \lim _{n \rightarrow \infty} \mathbb{P}\left(\bigvee_{k=1}^{n}\left(\frac{1}{X}\right)^{k} \leq a_{1 / X}(n) x\right)=\lim _{n \rightarrow \infty} \mathbb{P}\left(\bigwedge_{k=1}^{n} X^{k} \geq \frac{1}{a_{1 / X}(n) x}\right) \\
= & \Phi_{\zeta(p) \alpha, 1}(x), \quad x>0
\end{aligned}
$$

which implies by the continuity of $X$,

$$
\lim _{n \rightarrow \infty} \mathbb{P}\left(\bigwedge_{k=1}^{n} X^{k} \leq \frac{x}{a_{1 / X}(n)}\right)=1-\Phi_{\zeta(p) \alpha, 1}(1 / x), \quad x>0
$$

Choose now

$$
\tilde{a}_{n} \sim F_{X}^{+-}(1 / n) \sim 1 / a_{1 / X}(n) \downarrow 0, \quad n \rightarrow \infty
$$

Hence, we have with (C.2) and (C.3) by Lemma 5.1,

$$
\lim _{n \rightarrow \infty} \mathbb{P}\left(\frac{1}{\tilde{a}_{n}}\left(\bigwedge_{k=1}^{n} \ln \left(U_{i}^{k} / U_{j}^{k}\right)-\ln \left(b_{j i}\right)\right) \leq x\right)=1-\Phi_{\zeta(p) \alpha, 1}(1 / x), \quad x>0
$$

Recall from Theorem 3.12 and the regular variation of $\tilde{\varepsilon}$, that for the same $c$ as defined in Theorem 3.12 we have

$$
\begin{aligned}
& F_{X}(x) \sim c \mathbb{P}\left(\sum_{k \in S_{p}} \widetilde{\varepsilon}_{k} \leq x\right) \sim \mathbb{P}\left(\sum_{k \in S_{p}} \widetilde{\varepsilon}_{k} \leq x c^{1 /(\zeta(p) \alpha)}\right) \\
= & F_{\sum_{k \in S_{p}} \widetilde{\varepsilon}_{k}}\left(x c^{1 /(\zeta(p) \alpha)}\right), \quad x \downarrow 0
\end{aligned}
$$

which implies that $1 / n \sim F_{X}\left(\tilde{a}_{n}\right) \sim F_{\sum_{k \in S_{p}} \widetilde{\varepsilon}_{k}}\left(\tilde{a}_{n} c^{1 /(\zeta(p) \alpha)}\right)$. For the generalized inverses this implies that

$$
\tilde{a}_{n} \sim F_{X}^{*-}(1 / n) \sim c^{-1 /(\zeta(p) \alpha)} F_{\sum_{k \in S_{p}} \widetilde{\varepsilon}_{k}}^{\leftarrow}(1 / n) \sim c^{-1 /(\zeta(p) \alpha)} a_{n}, \quad n \rightarrow \infty
$$

From this we find
$\mathbb{P}\left(\frac{1}{\tilde{a}_{n}}\left(\bigwedge_{k=1}^{n} \ln \left(U_{i}^{k} / U_{j}^{k}\right)-\ln \left(b_{j i}\right)\right) \leq x\right)=\mathbb{P}\left(\bigwedge_{k=1}^{n} U_{i}^{k} / U_{j}^{k} \leq \exp \left(\tilde{a}_{n} x\right) b_{j i}\right), x>0$.
A Taylor expansion around 0 yields $\exp \left(\tilde{a}_{n} x\right)=1+\tilde{a}_{n} x(1+o(1))$ as $n \rightarrow \infty$, because $\tilde{a}_{n} \downarrow 0$. Since for $x>0$,

$$
\begin{aligned}
& \lim _{n \rightarrow \infty} \mathbb{P}\left(\frac{1}{\tilde{a}_{n} b_{j i}}\left(\bigwedge_{k=1}^{n} U_{i}^{k} / U_{j}^{k}-b_{j i}\right) \leq x\right)=\lim _{n \rightarrow \infty} \mathbb{P}\left(\frac{1}{a_{n} b_{j i}}\left(\bigwedge_{k=1}^{n} U_{i}^{k} / U_{j}^{k}-b_{j i}\right)\right. \\
\leq & \left.c^{1 /(\zeta(p) \alpha)} x\right)
\end{aligned}
$$

we obtain with (C.4)

$$
\begin{aligned}
& \lim _{n \rightarrow \infty} \mathbb{P}\left(\frac{1}{a_{n} b_{j i}}\left(\bigwedge_{k=1}^{n} U_{i}^{k} / U_{j}^{k}-b_{j i}\right) \leq x\right)=1-\Phi_{\zeta(p) \alpha, c^{-1 /(\zeta(p) \alpha)}}(1 / x) \\
= & \Psi_{\zeta(p) \alpha, c^{1 /(\zeta(p) \alpha)}}(x)
\end{aligned}
$$

which proves the assertion.
Now we can prove Theorem 5.2.
Proof of Theorem 5.2 As we shall find asymptotic independence of estimates between different node pairs, it suffices to prove the bivariate result.

We first simplify notation as follows. Assume pairs of nodes $(j, i) \neq(l, m)$ and denote the generic paths $p_{1}=p_{j i}$ with node set $S_{p_{1}}$ and $p_{2}=p_{l m}$ with node set $S_{p_{2}}$, respectively. Further denote $a_{n}^{1}=a_{n}^{(j i)}$ and $a_{n}^{2}=a_{n}^{(l m)}$.

By Proposition C. 2 we have

$$
\begin{aligned}
& \lim _{n \rightarrow \infty} \mathbb{P}\left(\frac{1}{a_{n}^{1} b_{j i}}\left(\bigwedge_{k=1}^{n} U_{i}^{k} / U_{j}^{k}-b_{j i}\right) \geq x_{1}\right)=\Phi_{\zeta\left(p_{1}\right) \alpha, c_{1}^{-1 /\left(\zeta\left(p_{1}\right) \alpha\right)}\left(1 / x_{1}\right) \\
= & \exp \left(-\frac{x_{1}^{\zeta\left(p_{1}\right) \alpha}}{c_{1}}\right)
\end{aligned}
$$

for $x_{1}>0$. Since $\lim _{n \rightarrow \infty}\left(1-\frac{a}{n}\right)^{n}=\exp (-a)$ for $a \in \mathbb{R}$, we get by independence of the ratios $U_{i}^{k} / U_{j}^{k}$ for $k=1, \ldots, n$ as $n \rightarrow \infty$,

$$
\mathbb{P}\left(\frac{1}{a_{n}^{1} b_{j i}}\left(U_{i} / U_{j}-b_{j i}\right) \leq x_{1}\right)=\frac{x_{1}^{\zeta\left(p_{1}\right) \alpha}}{c_{1} n}(1+o(1)), \quad x_{1}>0
$$

With the same argument, we have

$$
\mathbb{P}\left(\frac{1}{a_{n}^{2} b_{l m}}\left(U_{m} / U_{l}-b_{l m}\right) \leq x_{2}\right)=\frac{x_{2}^{\zeta\left(p_{2}\right) \alpha}}{c_{2} n}(1+o(1)), \quad x_{2}>0
$$

Therefore, we have on the one hand

$$
\begin{aligned}
& \lim _{n \rightarrow \infty} \mathbb{P}\left(\frac{1}{a_{n}^{1} b_{j i}} \bigwedge_{k=1}^{n}\left(U_{i}^{k} / U_{j}^{k}-b_{j i}\right) \geq x_{1}\right) \mathbb{P}\left(\frac{1}{a_{n}^{2} b_{l m}} \bigwedge_{k=1}^{n}\left(U_{m}^{k} / U_{l}^{k}-b_{l m}\right) \geq x_{2}\right) \\
& =\exp \left(-\frac{x_{1}^{\zeta\left(p_{1}\right) \alpha}}{c_{1}}\right) \exp \left(-\frac{x_{2}^{\zeta\left(p_{2}\right) \alpha}}{c_{2}}\right)=\exp \left(-\frac{x_{1}^{\zeta\left(p_{1}\right) \alpha}}{c_{1}}-\frac{x_{2}^{\zeta\left(p_{2}\right) \alpha}}{c_{2}}\right), x_{1}, x_{2}>0
\end{aligned}
$$

whereas, on the other hand, we have by independence of the bivariate ratios $\left(U_{i}^{k} / U_{j}^{k}, U_{m}^{k} / U_{l}^{k}\right)$ for $k=1, \ldots, n$,

$$
\begin{aligned}
& \lim _{n \rightarrow \infty} \mathbb{P}\left(\frac{1}{a_{n}^{1} b_{j i}} \bigwedge_{k=1}^{n}\left(U_{i}^{k} / U_{j}^{k}-b_{j i}\right) \geq x_{1}, \frac{1}{a_{n}^{2} b_{l m}} \bigwedge_{k=1}^{n}\left(U_{m}^{k} / U_{l}^{k}-b_{l m}\right) \geq x_{2}\right) \\
& =\lim _{n \rightarrow \infty}\left\{\mathbb{P}\left(\frac{1}{a_{n}^{1} b_{j i}}\left(U_{i}^{k} / U_{j}^{k}-b_{j i}\right) \geq x_{1}, \frac{1}{a_{n}^{2} b_{l m}}\left(U_{m}^{k} / U_{l}^{k}-b_{l m}\right) \geq x_{2}\right)\right\}^{n} \\
& =\lim _{n \rightarrow \infty}\left\{1-\mathbb{P}\left(\frac{1}{a_{n}^{1} b_{j i}}\left(U_{i} / U_{j}-b_{j i}\right) \leq x_{1}\right)-\mathbb{P}\left(\frac{1}{a_{n}^{2} b_{l m}}\left(U_{m} / U_{l}-b_{l m}\right) \leq x_{2}\right)\right. \\
& \left.+\mathbb{P}\left(\frac{1}{a_{n}^{1} b_{j i}}\left(U_{i} / U_{j}-b_{j i}\right) \leq x_{1}, \frac{1}{a_{n}^{2} b_{l m}}\left(U_{m} / U_{l}-b_{l m}\right) \leq x_{2}\right)\right\}^{n}
\end{aligned}
$$

By (A.23) we have $U_{i} \geq b_{j i} \prod_{k \in S_{p_{1}}} \varepsilon_{k} U_{j}$ and $U_{m} \geq b_{l m} \prod_{k \in S_{p_{2}}} \varepsilon_{k} U_{l}$, which implies

$$
\begin{aligned}
& \mathbb{P}\left(\frac{1}{a_{n}^{1} b_{j i}}\left(U_{i} / U_{j}-b_{j i}\right) \leq x_{1}, \frac{1}{a_{n}^{2} b_{l m}}\left(U_{m} / U_{l}-b_{l m}\right) \leq x_{2}\right) \\
& \leq \mathbb{P}\left(\frac{1}{a_{n}^{1}}\left(\prod_{k \in S_{p_{1}}} \varepsilon_{k}-1\right) \leq x_{1}, \frac{1}{a_{n}^{2}}\left(\prod_{k \in S_{p_{2}}} \varepsilon_{k}-1\right) \leq x_{2}\right)
\end{aligned}
$$

Since $(j, i) \neq(l, m)$, either $S_{p_{1}} \backslash S_{p_{2}} \neq \emptyset$ or $S_{p_{2}} \backslash S_{p_{1}} \neq \emptyset$ and without loss of generality, we assume $S_{p_{2}} \backslash S_{p_{1}} \neq \emptyset$. Since $\varepsilon \geq 1$ and all $\varepsilon_{k}$ are independent, we get

$$
(\mathrm{C} .9) \leq \mathbb{P}\left(\frac{1}{a_{n}^{1}}\left(\prod_{k \in S_{p_{1}}} \varepsilon_{k}-1\right) \leq x_{1}, \frac{1}{a_{n}^{2}}\left(\prod_{k \in S_{p_{2}} \backslash S_{p_{1}}} \varepsilon_{k}-1\right) \leq x_{2}\right)
$$

$$
=\mathbb{P}\left(\frac{1}{a_{n}^{1}}\left(\prod_{k \in S_{p_{1}}} \varepsilon_{k}-1\right) \leq x_{1}\right) \mathbb{P}\left(\frac{1}{a_{n}^{2}}\left(\prod_{k \in S_{p_{2}} \backslash S_{p_{1}}} \varepsilon_{k}-1\right) \leq x_{2}\right)
$$

By Corollary 2.6 b) we know that $\left(\prod_{k \in S_{p_{1}}} \varepsilon_{k}-1\right) \in R V_{\zeta\left(p_{1}\right) \alpha}^{0}$. Moreover, observe that by a Taylor expansion we have $a_{n}^{1} \sim F_{\sum k \in S_{p}}^{\leftarrow} \varepsilon_{k}(1 / n) \sim F_{\prod_{k \in S_{p}} \varepsilon_{k}-1}^{\leftarrow}(1 / n)$ as $n \rightarrow \infty$. Therefore, by Theorem 3.3.7 of [11] as in the proof of Proposition C.2, similarly to (C.4), it holds that

$$
\begin{aligned}
& \lim _{n \rightarrow \infty} \mathbb{P}\left(\frac{1}{a_{n}^{1}}\left(\bigwedge_{t=1}^{n} \prod_{k \in S_{p_{1}}} \varepsilon_{k}^{t}-1\right) \geq x_{1}\right)=\Phi_{\zeta\left(p_{1}\right) \alpha, 1}\left(1 / x_{1}\right) \\
= & \exp \left(-x_{1}^{\zeta\left(p_{1}\right) \alpha}\right), \quad x_{1}>0
\end{aligned}
$$

We proceed as in (C.5) and (C.6) to obtain as $n \rightarrow \infty$

$$
\mathbb{P}\left(\frac{1}{a_{n}^{1}}\left(\prod_{k \in S_{p_{1}}} \varepsilon_{k}-1\right) \leq x_{1}\right)=\left(\frac{x_{1}^{\zeta\left(p_{1}\right) \alpha}}{n}\right)(1+o(1)), \quad x_{1}>0
$$

Moreover, since $S_{p_{2}} \backslash S_{p_{1}} \neq \emptyset, \varepsilon$ is atom-free and $a_{n}^{2} \rightarrow 0$ as $n \rightarrow \infty$, we have

$$
\mathbb{P}\left(\frac{1}{a_{n}^{2}}\left(\prod_{k \in S_{p_{2}} \backslash S_{p_{1}}} \varepsilon_{k}-1\right) \leq x_{2}\right)=o(1), \quad x_{2}>0
$$

Therefore, we have by (C.10), (C.11) and (C.12)

$$
(\mathrm{C} .9)=\left(\frac{x_{1}^{\zeta\left(p_{1}\right) \alpha}}{n}\right)(1+o(1)) o(1), \quad x_{1}, x_{2}>0
$$

Comparing this with (C.5) and (C.6), we find that the last term in (C.8) is negligible. Hence, we obtain

$$
\begin{aligned}
& \lim _{n \rightarrow \infty} \mathbb{P}\left(\frac{1}{a_{n}^{1} b_{j i}} \bigwedge_{k=1}^{n}\left(U_{i}^{k} / U_{j}^{k}-b_{j i}\right) \geq x_{1}, \frac{1}{a_{n}^{2} b_{l m}} \bigwedge_{k=1}^{n}\left(U_{m}^{k} / U_{l}^{k}-b_{l m}\right) \geq x_{2}\right) \\
= & \lim _{n \rightarrow \infty}\left(1-\frac{x_{1}^{\zeta\left(p_{1}\right) \alpha}}{c_{1} n}(1+o(1))-\frac{x_{2}^{\zeta\left(p_{2}\right) \alpha}}{c_{2} n}(1+o(1))\right)^{n} \\
= & \exp \left(-\frac{x_{1}^{\zeta\left(p_{1}\right) \alpha}}{c_{1}}-\frac{x_{2}^{\zeta\left(p_{2}\right) \alpha}}{c_{2}}\right)
\end{aligned}
$$

Comparing this to (C.7) yields the result.
