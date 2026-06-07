# Learning Monotonic GenotypePhenotype Maps 

## Journal Article

Author(s):
Beerenwinkel, Niko; Knupfer, Patrick; Tresch, Achim
Publication date:
2011

## Permanent link:

https://doi.org/10.3929/ethz-b-000030573

## Rights / license:

In Copyright - Non-Commercial Use Permitted

## Originally published in:

Statistical Applications in Genetics and Molecular Biology 10(1), https://doi.org/10.2202/1544-6115.1603

# Statistical Applications in Genetics and Molecular Biology 

## Learning Monotonic Genotype-Phenotype Maps

Niko Beerenwinkel, ETH Zürich<br>Patrick Knupfer, ETH Zürich<br>Achim Tresch, Ludwig-Maximilians-Universität München

[^0]
[^0]:    Recommended Citation:
    Beerenwinkel, Niko; Knupfer, Patrick; and Tresch, Achim (2011) "Learning Monotonic Genotype-Phenotype Maps," Statistical Applications in Genetics and Molecular Biology: Vol. 10: Iss. 1, Article 3.
    DOI: $10.2202 / 1544-6115.1603$

# Learning Monotonic Genotype-Phenotype Maps 

Niko Beerenwinkel, Patrick Knupfer, and Achim Tresch


#### Abstract

Evolutionary escape of pathogens from the selective pressure of immune responses and from medical interventions is driven by the accumulation of mutations. We introduce a statistical model for jointly estimating the dynamics and dependencies among genetic alterations and the associated phenotypic changes. The model integrates conjunctive Bayesian networks, which define a partial order on the occurrences of genetic events, with isotonic regression. The resulting genotypephenotype map is non-decreasing in the lattice of genotypes. It describes evolutionary escape as a directed process following a phenotypic gradient, such as a monotonic fitness landscape. We present efficient algorithms for parameter estimation and model selection. The model is validated using simulated data and applied to HIV drug resistance data. We find that the effect of many resistance mutations is non-linear and depends on the genetic background in which they occur.


KEYWORDS: genotype-phenotype map, conjunctive Bayesian networks, HIV drug resistance, isotonic regression

Author Notes: A.T. was supported by an LMUexcellent guest professorship. N.B. was partially supported by the Swiss National Science Foundation under grant no. CR32I2_127017.

# 1 Introduction 

Most pathogens, including viruses, bacteria, eukaryotic parasites, and cancer cells, have a tendency to escape from selective pressure that is meant to control them. Rapid evolutionary change of the pathogen population facilitates escape from natural immune responses and from medical interventions such as chemotherapy. A quantitative understanding of evolutionary escape is at the heart of designing effective vaccines and treatment strategies.

The escape dynamics are governed by the space of possible genotypes that is accessible to the pathogen population, by the fitness landscape over these genotypes, and by additional population genetics parameters, such as population size and mutation rate (Iwasa, Michor, and Nowak, 2003). Here, we focus on the structure of the genotype space and the fitness landscape defined on it. We develop a statistical framework to estimate this fitness landscape from observed data subject to order and monotonicity constraints.

Constraints on the order in which mutations reach fixation in a population are common to many biological systems (Weinreich, Delaney, Depristo, and Hartl, 2006, Poelwijk, Kiviet, Weinreich, and Tans, 2007, Lozovsky, Chookajorn, Brown, Imwong, Shaw, Kamchonwongpaisan, Neafsey, Weinreich, and Hartl, 2009). We represent these constraints by a partial order among mutational events. The genotype space is the lattice of order ideals of this poset (Figure 1). For the fitness landscape, we assume that evolution proceeds in a directed fashion following an evolutionary gradient. We require that whenever a genotype $g$ precedes another genotype $h$, their fitness is non-decreasing, $\phi(g) \leq \phi(h)$. This assumption appears reasonable in the situations indicated above, where the pathogen is under strong selective pressure and can avoid extinction only by accumulating advantageous mutations.

In the present paper, our goal is to jointly estimate both the underlying mutational order constraints and the fitness landscape from observed genotypephenotype data. Estimating a fitness landscape amounts to learning a mapping that assigns each genotype a non-negative fitness value, or more generally, a phenotype. Because of the monotonicity assumption that we make, the regression problem is constraint and known as isotonic regression.

The two tasks of estimating mutational dependencies and of estimating a fitness landscape have been addressed separately before. Regressing phenotype on genotype is a recurrent task, because understanding the genotype-phenotype map is a central question in biology (Sevin, DeGruttola, Nijhuis, Schapiro, Foulkes, Para, and Boucher, 2000, Reidys and Stadler, 2002, Beerenwinkel, Schmidt, Walter, Kaiser, Lengauer, Hoffmann, Korn, and Selbig, 2002, Beerenwinkel, Däumer, Oette, Korn, Hoffmann, Kaiser, Lengauer, Selbig, and Walter, 2003a, Wang and Larder, 2003, Draghici and Potter, 2003, Segal, Barbour, and Grant, 2004, Rabi-

nowitz, Myers, Banjevic, Chan, Sweetkind-Singer, Haberer, McCann, and Wolkowicz, 2006, Rhee, Taylor, Wadhera, Ben-Hur, Brutlag, and Shafer, 2006).

Estimating dependencies among mutations is also a question of general interest in molecular biology and genetics. Several statistical models have been proposed for this purpose, including Bayesian networks (Klingler and Brutlag, 1994, Deforche, Silander, Camacho, Grossman, Soares, Laethem, Kantor, Moreau, and Vandamme, 2006, Poon, Lewis, Pond, and Frost, 2007) and dependency networks (Carlson, Brumme, Rousseau, Brumme, Matthews, Kadie, Mullins, Walker, Harrigan, Goulder, and Heckerman, 2008). Order constraints represent a specific type of dependency and a specialized Bayesian network model, called conjuctive Bayesian network (CBN), has been proposed that uses a partial order to represent these constraints (Beerenwinkel, Eriksson, and Sturmfels, 2006, 2007, Beerenwinkel and Sullivant, 2009, Gerstung, Baudis, Moch, and Beerenwinkel, 2009).

Here, we introduce a more general statistical model based on a partially ordered set and on isotonic regression to describe constraint and directed evolution in genotype space. We present algorithms for estimating both the poset structure and the isotonic regression function from observed data. The resulting genotypephenotype map is optimal in the likelihood sense subject to order constraints and monotonicity. The algorithms have been implemented in the R package i cbn, available at www. cbg.ethz.ch/software/icbn.

The model is applied to a dataset of mutational patterns in the genome of HIV and the corresponding levels of phenotypic drug resistance of the respective viruses. We want to learn mutational order constraints that apply to the evolutionary escape of HIV from drug pressure and, at the same time, the genotype-phenotype map which assigns a resistance phenotype to each genotype and is non-decreasing in the induced genotype space.

In Section 2, we present a self-contained introduction of CBNs following Beerenwinkel et al. (2007), but with some simplifications and advancements. Section 3 is devoted to isotonic regression. In Section 4, we combine the two models to obtain the isotonic CBN (I-CBN) model, which is further developed into the noisy I-CBN (NI-CBN) to handle measurement noise in Section 5. Section 6 reports performance measures of the inference algorithms based on simulated data, and in Section 7, the application of the NI-CBN model to HIV drug resistance data is presented.

# 2 Conjunctive Bayesian networks 

We consider a fixed finite set of genetic events $\mathscr{E}$, and assume that genetic changes are irreversible. To model the accumulation of these mutations, we define the CBN

as a triple $(\mathscr{E}, \prec, \theta)$, where " $\prec$ " is a partial order on $\mathscr{E}$, and $\theta=\left(\theta_{e}\right)_{e \in \mathscr{E}} \in[0,1]^{\mathscr{E}}$ is a set of parameters. A relation $e_{1} \prec e_{2}$ between two distinct events is interpreted as event $e_{2}$ requiring event $e_{1}$ to have happened before. A relation $e_{1} \prec e_{2}$ is called a cover relation, if for all $e^{\prime} \in \mathscr{E}$ with $e_{1} \prec e^{\prime} \prec e_{2}$, either $e^{\prime}=e_{1}$ or $e^{\prime}=e_{2}$.

A subset $g$ of events is called a genotype. The set of all possible genotypes, denoted $\mathscr{G}$, is the power set of $\mathscr{E}$, which is identified in a natural way with the set of all binary strings of length $|\mathscr{E}|$ by assigning $g \subset \mathscr{E}$ to $\left(g_{e}\right)_{e \in \mathscr{E}}$ with $g_{e}=1$ if $e \in g$, and $g_{e}=0$ otherwise. With subset inclusion, $\mathscr{G}$ forms a distributive lattice. We say that a genotype $g \subseteq \mathscr{E}$ and a relation $e_{1} \prec e_{2}$ are compatible, if $\left(e_{2} \in g\right) \Rightarrow\left(e_{1} \in g\right)$ holds. This definition extends to sets of genotypes and to sets of relations in the obvious way. The state space $G(\mathscr{E}, \prec)$ of the CBN model is defined as the set of all genotypes that are compatible with $(\mathscr{E}, \prec)$, The elements of $G(\mathscr{E}, \prec)$ are the order ideals of the poset $(\mathscr{E}, \prec)$, where an order ideal is a subset $g \subseteq \mathscr{E}$ that is closed downwards, i.e., if $e_{2} \in g$ and $e_{1} \prec e_{2}$, then $e_{1} \in g$. Conversely, given any set of genotypes $G \subseteq \mathscr{G}$, let $\left(\mathscr{E}, \prec_{G}\right)$ be the set of all events compatible with $G$. Then $\left(\mathscr{E}, \prec_{G}\right)$ forms a poset, which is the unique largest poset compatible with $G$. For the empty poset with no relation, we have $G\left(\mathscr{E}, \prec_{\text {empty }}\right)=\mathscr{G}$ and $\left(\mathscr{E}, \prec_{\mathscr{G}}\right)=\left(\mathscr{E}, \prec_{\text {empty }}\right.$ ). We refer to the genotype $g=\emptyset$ as the wild type, and to $g=\mathscr{E}$ as the completely mutated type.

For a genotype $g$, we denote by Exit ${ }_{\prec}(g)$ the set of all events that have not yet occurred in $g$ but could happen next. An event $e \in \mathscr{E}$ might happen next if and only if $e$ is minimal in $\mathscr{E} \backslash g$ with respect to the partial order. For $e \in \mathscr{E}$, let $\theta_{e}$ be the conditional probability that the event $e$ has occurred given that all of its predecessor events have already occurred. The CBN defines the following probability distribution for the discrete random variable $X$ with state space $G(\mathscr{E}, \prec)$

$$
\operatorname{Pr}(X=g \mid \mathscr{E}, \prec, \theta)=\prod_{e \in g} \theta_{e} \cdot \prod_{e \in \operatorname{Exit}_{\prec}(g)}\left(1-\theta_{e}\right)
$$

We write $\operatorname{CBN}(\mathscr{E}, \prec, \theta)$ for this statistical model. The probability of observing $g \in G(\mathscr{E}, \prec)$ is the probability that all the events in $g$ have happened times the probability that none of the events that could happen next has occurred.

CBNs are Bayesian network models and they can also be defined as graphical models as follows. Consider the graph $H$ with vertex set $\mathscr{E}$ and edges $e_{1} \rightarrow e_{2}$ for all cover relations $e_{1} \prec e_{2}$. The CBN model is the directed graphical model defined by $H$ and the probability tables

$$
\tau^{e}=\left(\begin{array}{cc}
1 & 0 \\
\vdots & \vdots \\
1 & 0 \\
1-\theta_{e} & \theta_{e}
\end{array}\right)
$$

Event poset
Genotype lattice
![img-0.jpeg](img-0.jpeg)

CBN probabilities
![img-1.jpeg](img-1.jpeg)

Figure 1: Conjunctive Bayesian network (CBN) model. Shown is the event poset (left), the induced genotype lattice (center), and the genotype probabilities (right) of the CBN model introduced in Example 1. In the event poset, each directed edge $e_{1} \rightarrow e_{2}$ stands for a relation $e_{1} \prec e_{2}$.

The entries of $\tau^{e}$ are the conditional probabilities $\tau_{a, b}^{e}=\operatorname{Pr}\left(X_{e}=b \mid X_{\mathrm{pa}(e)}=a\right)$, for all $a \in\{0,1\}^{\mathrm{pa}(e)}$ and $b \in\{0,1\}$, where $\mathrm{pa}(e)$ denotes the parents of $e$ in $H$, $\mathbf{1}=(1, \ldots, 1)$, and $\tau_{\mathbf{1}, 1}^{e}=\operatorname{Pr}\left(X_{e}=1 \mid X_{\mathrm{pa}(e)}=\mathbf{1}\right)=\theta_{e}$. The joint distribution of $X$ factorizes as

$$
\begin{aligned}
& \operatorname{Pr}(X=g \mid H, \tau)=\prod_{e \in \mathscr{E}} \operatorname{Pr}\left(X_{e}=g_{e} \mid X_{\mathrm{pa}(e)}=g_{\mathrm{pa}(e)}\right)=\prod_{e \in \mathscr{E}} \tau_{g_{\mathrm{pa}(e)}, g_{e}}^{e} \\
& =\prod_{\substack{e \in g \\
\mathrm{pa}(e)=\mathbf{1}}} \theta_{e} \prod_{\substack{e \notin g \\
\mathrm{pa}(e)=\mathbf{1}}}\left(1-\theta_{e}\right) \prod_{\substack{e \notin g \\
\mathrm{pa}(e) \neq \mathbf{1}}} 1 \prod_{\substack{e \in g \\
\mathrm{pa}(e) \neq \mathbf{1}}} 0=\operatorname{Pr}(X=g \mid \mathscr{E}, \prec, \theta)
\end{aligned}
$$

because the index sets of the first, second, and last product are, respectively, $g$, Exit $_{\prec}(g)$, and the empty set, for all $g \in G(\mathscr{E}, \prec)$.

Example 1. Let $\mathscr{E}=\{1,2,3,4\}$ with the relations $1 \prec 3,1 \prec 4,2 \prec 3$ and $2 \prec 4$. The lattice of order ideals of this poset consists of the seven genotypes $G(\mathscr{E}, \prec)=$ $\{\emptyset,\{1\},\{2\},\{1,2\},\{1,2,3\},\{1,2,4\},\{1,2,3,4\}\}$ (Figure 1). The CBN model $(\mathscr{E}, \prec, \theta)$ is given by the probabilities

$$
\begin{aligned}
\operatorname{Pr}(\emptyset) & =\left(1-\theta_{1}\right)\left(1-\theta_{2}\right) \\
\operatorname{Pr}(\{1\}) & =\theta_{1}\left(1-\theta_{2}\right) \\
\operatorname{Pr}(\{2\}) & =\left(1-\theta_{1}\right) \theta_{2} \\
\operatorname{Pr}(\{1,2\}) & =\theta_{1} \theta_{2}\left(1-\theta_{3}\right)\left(1-\theta_{4}\right) \\
\operatorname{Pr}(\{1,2,3\}) & =\theta_{1} \theta_{2} \theta_{3}\left(1-\theta_{4}\right) \\
\operatorname{Pr}(\{1,2,4\}) & =\theta_{1} \theta_{2}\left(1-\theta_{3}\right) \theta_{4} \\
\operatorname{Pr}(\{1,2,3,4\}) & =\theta_{1} \theta_{2} \theta_{3} \theta_{4}
\end{aligned}
$$

In the remainder of this section, we recall maximum likelihood (ML) parameter estimation and model selection for CBNs from (Beerenwinkel et al., 2007). Let $(\mathscr{E}, \prec, \theta)$ be a CBN model. The data for this model is a count vector $n=\left(n_{g}\right) \in \mathbb{N}^{\mathscr{G}}$, where $n_{g}$ is the number of observations of genotype $g$. We assume throughout the paper that each event $e \in \mathscr{E}$ has been observed in at least one genotype, i.e., $\sum_{g: e \in g} n_{g}>0$. The log-likelihood function of the CBN model is

$$
\ell_{X}(\theta)=\sum_{g \in G} n_{g}\left[\sum_{e \in \mathscr{E}} \log \left(\theta_{e}\right)+\sum_{e \in \operatorname{Exit}_{\prec}(g)} \log \left(1-\theta_{e}\right)\right]
$$

Proposition 1. Let $(\mathscr{E}, \prec)$ be a fixed poset and $n \in \mathbb{N}^{\mathscr{G}}$ an observed set of genotypes. The ML parameters of the CBN model $(\mathscr{E}, \prec, \theta)$ are given by

$$
\hat{\theta}_{e}=\frac{\sum_{g: e \in g} n_{g}}{\sum_{g: \text { below }_{\prec}(e) \subseteq g} n_{g}}, \quad \text { for all } e \in \mathscr{E}
$$

where below ${ }_{\prec}(e)=\left\{e^{\prime} \in \mathscr{E} \mid e^{\prime} \neq e\right.$ and $\left.e^{\prime} \prec e\right\}$ is the set of events strictly below $e$.
Proof. See (Beerenwinkel et al., 2007, Prop. 2).
We say that a set of genotypes $G \subset \mathscr{G}$ separates the events, if for any two distinct elements $e_{1}, e_{2} \in \mathscr{E}$, there exists a genotype $g \in G$ and $i \in\{1,2\}$ such that $g \cap\left\{e_{1}, e_{2}\right\}=\left\{e_{i}\right\}$. It is easy to see that for $G \subset \mathscr{G}$, the relation $\prec_{G}$ on $\mathscr{E}$ is reflexive and transitive. Furthermore, if $G$ separates the events, then $\prec_{G}$ is a partial order on $\mathscr{E}$. The support of a data set $n \in \mathbb{N}^{\mathscr{G}}$ is defined as the set of genotypes that have actually been observed, $\operatorname{supp}(n)=\left\{g \in \mathscr{G} \mid n_{g}>0\right\}$. If $\operatorname{supp}(n)$ does not separate the events, then there exist events that are always observed in common. The observation of several of those events does not provide additional information. Hence non-separable events may be mapped to one event. The following result has been reported in (Beerenwinkel et al., 2007, Thm. 5). Here, we present a new and simplified proof.

Theorem 1. Let $n \in \mathbb{N}^{\mathscr{G}}$ be a set of observed genotypes. If $\operatorname{supp}(n)$ separates the events, then the ML CBN model is $\left(\mathscr{E}, \prec_{\operatorname{supp}(n)}, \hat{\theta}\right)$, with $\hat{\theta}$ defined as in Proposition 1 for the partial order $\prec_{\operatorname{supp}(n)}$.

Proof. Recall that $\left(\mathscr{E}, \prec_{\operatorname{supp}(n)}\right)$ is the unique largest poset compatible with $\operatorname{supp}(n)$. For any event poset $(\mathscr{E}, \prec)$ that is not compatible with $\operatorname{supp}(n)$, the likelihood function $L_{X}(\theta)=\operatorname{Pr}(n \mid \mathscr{E}, \prec, \theta)$ is identical zero. Thus, it is sufficient to show that if $\prec_{1}$ and $\prec_{2}$ are two partial orders on $\mathscr{E}$ that are compatible with $\operatorname{supp}(n)$ and $\prec_{2}$ is larger than $\prec_{1}$ (i.e., for all $e, e^{\prime} \in \mathscr{E}, e \prec_{1} e^{\prime}$ implies $e \prec_{2} e^{\prime}$ ), then the likelihood is non-decreasing, $\operatorname{Pr}(n \mid \mathscr{E}, \prec_{1}) \leq \operatorname{Pr}(n \mid \mathscr{E}, \prec_{2})$.

Let $g \in \mathscr{G}$ be a genotype. If $\prec_{2}$ is larger than $\prec_{1}$, then

$$
\min _{\prec_{2}} \mathscr{E} \backslash g=\operatorname{Exit}_{\prec_{2}}(g) \subseteq \operatorname{Exit}_{\prec_{1}}(g)=\min _{\prec_{1}} \mathscr{E} \backslash g
$$

To see this, suppose that $e \in \mathscr{E} \backslash g$ is not $\prec_{1}$-minimal. Then there is an element $d \in \mathscr{E} \backslash g$ with $d \prec_{1} e$. But this implies $d \prec_{2} e$ and hence $e$ is not $\prec_{2}$-minimal either.

For any genotype compatible with $\prec_{\operatorname{supp}(n)}$ (and hence also with $\prec_{1}$ and $\prec_{2}$ ), we find

$$
\begin{aligned}
\operatorname{Pr}\left(X=g \mid \mathscr{E}, \prec_{1}, \theta\right) & =\prod_{e \in g} \theta_{e} \cdot \prod_{e \in \operatorname{Exit}_{\prec_{1}}(g)}\left(1-\theta_{e}\right) \\
& \leq \prod_{e \in g} \theta_{e} \cdot \prod_{e \in \operatorname{Exit}_{\prec_{2}}(g)}\left(1-\theta_{e}\right)=\operatorname{Pr}\left(X=g \mid \mathscr{E}, \prec_{2}, \theta\right)
\end{aligned}
$$

We assume that genotype observations are independent, hence

$$
\begin{aligned}
\operatorname{Pr}(n \mid \mathscr{E}, \prec_{1}, \theta) & =\prod_{g \in \operatorname{supp}(n)} \operatorname{Pr}\left(X=g \mid \mathscr{E}, \prec_{1}, \theta\right)^{n_{g}} \\
& \leq \prod_{g \in \operatorname{supp}(n)} \operatorname{Pr}\left(X=g \mid \mathscr{E}, \prec_{2}, \theta\right)^{n_{g}}=\operatorname{Pr}\left(n \mid \mathscr{E}, \prec_{2}, \theta\right)
\end{aligned}
$$

$\left(\mathscr{E}, \prec_{\operatorname{supp}(n)}\right)$ is a partial order, because $\operatorname{supp}(n)$ separates the events. By definition, no compatible poset can contain more relations than $\left(\mathscr{E}, \prec_{\operatorname{supp}(n)}\right)$. Thus

$$
\operatorname{Pr}(n \mid \mathscr{E}, \prec, \theta) \leq \operatorname{Pr}\left(n \mid \mathscr{E}, \prec_{\operatorname{supp}(n)}, \theta\right) \leq \operatorname{Pr}\left(n \mid \mathscr{E}, \prec_{\operatorname{supp}(n)}, \hat{\theta}\right)
$$

for any partial order $\prec$ and any parameter vector $\theta$.

# 3 Isotonic regression 

In this section, we fix a given poset $(\mathscr{E}, \prec)$ with genotype lattice $G=G(\mathscr{E}, \prec)$. We assume that the evolutionary process on $G$, i.e., the partially ordered accumulation

of mutations, follows a certain one-dimensional real-valued phenotype in a monotonic fashion. We require that the genotype-phenotype map $\phi: G \rightarrow \mathbb{R}$ satisfies for all $g_{1}, g_{2} \in G$,

$$
g_{1} \subseteq g_{2} \Rightarrow \phi\left(g_{1}\right) \leq \phi\left(g_{2}\right)
$$

Our goal is to estimate the unknown monotonic function $\phi$ from observed genotypephenotype pairs $(g, y) \in G \times \mathbb{R}$.

We assume that the conditional phenotypes $Y \mid X=g$ are independent normal random variables with unknown means $\mu_{g}$ and common unknown variance $\sigma^{2}$,

$$
Y \mid X=g \sim \operatorname{Norm}\left(\mu_{g}, \sigma^{2}\right), \quad \text { for all } g \in G
$$

Let $y_{g}=\left\{y_{g, 1}, \ldots, y_{g, n_{g}}\right\}$ be the phenotypes observed with genotype $g$. For a given dataset $\left(y_{g}\right)_{g \in G}$, the conditional log-likelihood is

$$
\ell_{Y \mid X=g}(\mu, \sigma)=-\frac{N}{2} \log (2 \pi)-N \log (\sigma)-\frac{1}{2 \sigma^{2}} \sum_{g \in G} \sum_{j=1}^{n_{g}}\left(y_{g, j}-\mu_{g}\right)^{2}
$$

where $N=\sum_{g \in G} n_{g}$ is the total size of the data.
We estimate the parameters $\mu=\left(\mu_{g}\right)_{g \in G}$ and $\sigma^{2}$ from the data using ML subject to the monotonicity constraints

$$
g_{1} \subseteq g_{2} \Rightarrow \mu_{g_{1}} \leq \mu_{g_{2}}, \quad \text { for all } g_{1}, g_{2} \in G
$$

This problem is known as the isotonic regression problem and its solution has the following structure. Let $\bar{y}_{g}=\left(1 / n_{g}\right) \sum_{j=1}^{n_{g}} y_{g, j}$ denote the average phenotype observed with genotype $g$. For fixed $\sigma$, the ML estimates (MLEs) of $\mu$ are found by minimizing the sum of squares

$$
\sum_{g \in G} \sum_{j=1}^{n_{g}}\left(y_{g, j}-\mu_{g}\right)^{2}=\sum_{g \in G}\left[\sum_{j=1}^{n_{g}}\left(y_{g, j}-\bar{y}_{g}\right)^{2}+n_{g}\left(\bar{y}_{g}-\mu_{g}\right)^{2}\right]
$$

subject to the constraints (4), i.e., by solving

$$
\begin{aligned}
& \min _{\mu} \sum_{g \in G}\left(\bar{y}_{g}-\mu_{g}\right)^{2} n_{g} \\
& \text { s.t. } \mu_{g_{1}} \leq \mu_{g_{2}} \text { for all } g_{1} \subseteq g_{2} \text { in } G
\end{aligned}
$$

The optimization problem (5) is a convex quadratic programming problem with a unique local solution $\hat{\mu}$ which is also the global minimum. Several algorithms have been proposed for solving this constraint least squares problem (Barlow, Bartholomew, Bremner, and Brunk, 1972). In our applications, we use the R package isotone

![img-2.jpeg](img-2.jpeg)

Figure 2: Isotonic regression on a genotype lattice. The genotype space (left) is the lattice of order ideals of the event poset shown in Figure 1. A total of 37 phenotypic measurements are summarized by their respective means and counts in the center diagram. The solution of the isotonic regression problem (5) is shown on the right, i.e., the estimated phenotypes $\hat{\mu}_{g}$. See Example 2 for more details.
which implements a solution based on a convex programming formulation with linear constraints and employs an active set algorithm (de Leeuw, Hornik, and Mair, 2009). The MLE of $\sigma^{2}$ is then

$$
\hat{\sigma}^{2}=\frac{1}{N} \sum_{g \in G} \sum_{j=1}^{n_{g}}\left(y_{g, j}-\hat{\mu}_{g}\right)^{2}
$$

Example 2. For the genotype lattice of Example 1 and Figure 1, we consider the phenotype data summarized in the center diagram of Figure 2 by the average phenotypes $\bar{y}_{g}$ and, in parenthesis, the genotype counts $n_{g}$. The MLEs of $\mu$ are found by solving the optimization problem (5). The solution is displayed on the right of Figure 2 and it has the following block structure:

$$
\begin{aligned}
\hat{\mu}_{\emptyset} & =0.03 \\
\hat{\mu}_{\{1\}}=\hat{\mu}_{\{2\}}=\hat{\mu}_{\{1,2\}} & =1.02 \\
\hat{\mu}_{\{1,2,4\}} & =1.31 \\
\hat{\mu}_{\{1,2,3\}}=\hat{\mu}_{\{1,2,3,4\}} & =2.17
\end{aligned}
$$

The MLE of $\sigma$ can not be computed from the average phenotypes $\bar{y}_{g}$, but only from the full data $\left\{y_{g, j}\right\}$ not shown in this example.

The estimated genotype-phenotype map is monotonic along any mutational pathway $g_{1} \subset \cdots \subset g_{k}$ in $G$, and it has two additional properties that are important

in biological applications. First, the mapping is non-linear in the events. It allows for different phenotypic effects of the same genetic event, depending on the genetic context of the mutation. Second, the block structure implies that neighboring genotypes often have the same phenotype. In other words, blocks represent neutral mutational networks with respect to the considered phenotype.

# 4 Isotonic conjunctive Bayesian network model 

We think of the observed genotype-phenotype pairs as intermediate steps of a nonreversible evolutionary process that is subject to partial order constraints and directed by a non-decreasing phenotype. For a fixed poset $(\mathscr{E}, \prec)$ with induced genotype lattice $G=G(\mathscr{E}, \prec)$, we define the joint distribution of genotype-phenotype pairs $(X, Y)$ by the hierarchical model

$$
\begin{aligned}
X & \sim \operatorname{CBN}(\mathscr{E}, \prec, \theta) \\
Y \mid X=g & \sim \operatorname{Norm}\left(\mu_{g}, \sigma^{2}\right), \quad g \in G
\end{aligned}
$$

with $\mu_{g_{1}} \leq \mu_{g_{2}}$ whenever $g_{1} \subseteq g_{2}$ in $G$. We call this model the Isotonic Conjunctive Bayesian Network (I-CBN) model. For a dataset $\left(n_{g}, y_{g}\right)_{g \in G}$, the log-likelihood function of the I-CBN model is the sum of the CBN log-likelihood (2) and the isotonic regression log-likelihood (3), $\ell_{X, Y}\left(\theta, \mu, \sigma^{2}\right)=\ell_{X}(\theta)+\ell_{Y \mid X}\left(\mu, \sigma^{2}\right)$. The results on ML parameter estimation and model selection for CBNs extend to ICBNs as follows.

Proposition 2. The ML parameters of the I-CBN model $(\mathscr{E}, \prec, \theta, \mu, \sigma)$ are given by

$$
\begin{aligned}
\hat{\theta}_{e} & =\frac{\sum_{g: e \in g} n_{g}}{\sum_{g: \text { below } \prec(e) \subseteq g} n_{g}}, \quad \text { for all } e \in \mathscr{E} \\
\hat{\mu} & =\min _{\mu} \sum_{g \in G}\left(\bar{y}_{g}-\mu_{g}\right)^{2} n_{g}, \quad \text { s.t. } \mu_{g_{1}} \leq \mu_{g_{2}} \text { for all } g_{1} \subseteq g_{2} \text { in } G \\
\hat{\sigma}^{2} & =\frac{1}{N} \sum_{g \in G} \sum_{j=1}^{n_{g}}\left(y_{g, j}-\hat{\mu}_{g}\right)^{2}
\end{aligned}
$$

Proof. See Proposition 1 and Section 3, and note that the partial derivatives of $\ell_{X, Y}$ are the same as those of $\ell_{X}$ and $\ell_{Y \mid X}$, respectively.

Theorem 2. Let $n \in \mathbb{N}^{\mathscr{G}}$ be a set of observed genotypes. If $\operatorname{supp}(n)$ separates the events, then the ML I-CBN model is $\left(\mathscr{E}, \prec_{\operatorname{supp}(n)}, \hat{\theta}, \hat{\mu}, \hat{\sigma}^{2}\right)$, with $\hat{\theta}, \hat{\mu}$, and $\hat{\sigma}^{2}$ defined as in Proposition 2 for the partial order $\prec_{\operatorname{supp}(n)}$.

Proof. If $(\mathscr{E}, \prec)$ is not compatible with the data, then the likelihood function is zero. The poset $\left(\mathscr{E}, \prec_{\operatorname{supp}(n)}\right)$ is the unique maximal poset that is compatible with $n$. Suppose there are two different compatible posets $\left(\mathscr{E}, \prec_{i}\right), i=1,2$, such that $\left(\mathscr{E}, \prec_{2}\right.$ ) is larger than $\left(\mathscr{E}, \prec_{1}\right)$. Then $\operatorname{CBN}\left(\mathscr{E}, \prec_{2}\right)$ is more likely than $\operatorname{CBN}\left(\mathscr{E}, \prec_{1}\right)$ and it suffices to shown that the isotonic regression likelihood is also non-decreasing.

The data $n$ is compatible with both posets and we have

$$
\operatorname{supp}(n) \subseteq G\left(\mathscr{E}, \prec_{\operatorname{supp}(n)}\right) \subseteq G\left(\mathscr{E}, \prec_{2}\right) \subset G\left(\mathscr{E}, \prec_{1}\right)
$$

For any genotype $g \in G\left(\mathscr{E}, \prec_{1}\right) \backslash G\left(\mathscr{E}, \prec_{2}\right)$, we must have $n_{g}=0$. Therefore the log-likelihood $\ell_{Y \mid X}$ does not differ whether evaluated on $G\left(\mathscr{E}, \prec_{1}\right)$ or $G\left(\mathscr{E}, \prec_{2}\right)$.

We summarize the results of this section in the following algorithm for learning I-CBN models from data.

# Algorithm 1. (Learning I-CBN models) 

InPut: A dataset $\left(n_{g}, y_{g}\right)_{g \in \mathscr{G}}$ such that $\operatorname{supp}(n)$ separates the events $\mathscr{E}$
Output: The ML I-CBN model $\left(\mathscr{E}, \prec_{\operatorname{supp}(n)}, \hat{\theta}, \hat{\mu}, \hat{\sigma}^{2}\right)$
STEP 1: Construct $\prec_{\operatorname{supp}(n)}$ by setting, for all $e_{1}, e_{2} \in \mathscr{E}, e_{1} \prec_{\operatorname{supp}(n)} e_{2}$ if and only if $g \cap\left\{e_{1}, e_{2}\right\} \neq\left\{e_{2}\right\}$ for all $g \in \operatorname{supp}(n)$. Set $G=G(\mathscr{E}, \prec)$.
STEP 2: Compute the isotonic regression (5) to obtain the MLEs $\hat{\mu}=\left(\hat{\mu}_{g}\right)_{g \in G}$.
STEP 3: Compute the MLEs $\hat{\sigma}^{2}$ and $\hat{\theta}=\left(\hat{\theta}_{e}\right)_{e \in \mathscr{E}}$ according to Proposition 2.
STEP 4: Output the poset $\left(\mathscr{E}, \prec_{\operatorname{supp}(n)}\right)$ and the MLEs $\left(\hat{\theta}, \hat{\mu}, \hat{\sigma}^{2}\right)$.

## 5 Error model

Algorithm 1 for learning I-CBN models using ML is appealing due its efficiency and simplicity. In practice, however, it is limited by the sensitivity of poset reconstruction (Step 1) to noise in the genotype data. A single, possibly erroneous, observed genotype containing $e_{2}$ but not $e_{1}$ is sufficient to remove the relation $e_{1} \prec e_{2}$ from the optimal poset.

In order to account for noisy genotype observations, we extend the I-CBN model in this section. We follow the approach of Gerstung et al. (2009) and devise an error model which assumes that the true genotype $Z$ is generated by the CBN model, but not directly observable, and that the observed genotype $X$ is an erroneous copy of $Z$,

$$
\operatorname{Pr}(X \mid Z)=\varepsilon^{d(X, Z)}(1-\varepsilon)^{n-d(X, Z)}
$$

where $\varepsilon$ is the per-locus probability of a measurement error and $d$ the Hamming distance between genotypes, i.e., the number of genetic events that occurred in exactly one of the two genotypes. We denote this error model by $\operatorname{Err}(Z, \varepsilon)$.

The model for $(X, Y, Z)$ is defined hierarchically as

$$
\begin{aligned}
Z & \sim \operatorname{CBN}(\mathscr{E}, \prec, \theta) \\
X \mid Z & \sim \operatorname{Err}(Z, \varepsilon) \\
Y \mid Z & \sim \operatorname{Norm}\left(\mu_{Z}, \sigma^{2}\right) \quad \text { with } \mu_{g_{1}} \leq \mu_{g_{2}} \text { for all } g_{1} \subseteq g_{2}
\end{aligned}
$$

The observed genotype $X$ is independent of the observed phenotype $Y$ given the true unobserved genotype $Z$. The noisy I-CBN (NI-CBN) model is defined as the marginalization of this model with respect to the unobserved data $Z$.

For fixed $(\mathscr{E}, \prec), G=G(\mathscr{E}, \prec)$, and data $\left\{\left(x_{i}, y_{i}, z_{i}\right)\right\}_{i=1, \ldots, N}$, the completedata log-likelihood of the NI-CBN model is

$$
\ell_{X, Y, Z}\left(\theta, \varepsilon, \mu, \sigma^{2}\right)=\ell_{Z}(\theta)+\ell_{X \mid Z}(\varepsilon)+\ell_{Y \mid Z}\left(\mu, \sigma^{2}\right)
$$

Hence the MLEs are given in Proposition 2 and by $\hat{\varepsilon}=[1 /(N|\mathscr{E}|)] \sum_{i=1}^{N} d\left(x_{i}, z_{i}\right)$. The observed-data log-likelihood is

$$
\ell_{X, Y}\left(\theta, \varepsilon, \mu, \sigma^{2}\right)=\sum_{i=1}^{N} \log \sum_{z_{i} \in G} \operatorname{Pr}\left(x_{i}, y_{i}, z_{i}\right)
$$

In order to maximize this expression, we derive an Expectation Maximization (EM) algorithm (Dempster, Laird, and Rubin, 1977).

The posterior of the hidden data $Z$ given the observations $(X, Y)$ is

$$
\operatorname{Pr}(Z \mid X, Y)=\frac{\operatorname{Pr}(Z) \operatorname{Pr}(X \mid Z) \operatorname{Pr}(Y \mid Z)}{\sum_{Z^{\prime}} \operatorname{Pr}\left(Z^{\prime}\right) \operatorname{Pr}\left(X \mid Z^{\prime}\right) \operatorname{Pr}\left(Y \mid Z^{\prime}\right)}
$$

Let $\gamma_{i, g}=\operatorname{Pr}\left(Z_{i}=g \mid X, Y\right)$ denote the responsibility of genotype $g \in G$ for observation $\left(x_{i}, y_{i}\right)$. Then, for all $g \in G$,

$$
u_{g}=\mathbb{E}_{Z \mid X, Y}\left[\sum_{i=1}^{N} \delta\left(Z_{i}, g\right)\right]=\sum_{i=1}^{N} \gamma_{i g}
$$

is the expected genotype count, where $\delta$ is the Kronecker delta function. This defines the E step.

For the M step, we estimate the model parameters by maximizing the expectation of the complete-data log-likelihood (6) with respect to the conditional

distribution (7). We obtain the following equations for updating the model parameters:

$$
\begin{aligned}
\theta_{e}^{\text {new }} & =\frac{\sum_{g: e \in g} u_{g}}{\sum_{g: e \in \text { below } \prec(e) \subseteq g} u_{g}}, \quad e \in \mathscr{E} \\
\varepsilon^{\text {new }} & =\frac{1}{N|\mathscr{E}|} \sum_{i=1}^{N} \sum_{g \in G} d\left(x_{i}, g\right) \gamma_{i, g} \\
\mu^{\text {new }} & =\min _{\mu} \sum_{g \in G} \frac{1}{u_{g}} \sum_{i=1}^{N} y_{i} \gamma_{i, g}-\mu_{g} \\
\left(\sigma^{\text {new }}\right)^{2} & =\frac{1}{N} \sum_{g \in G} \sum_{i=1}^{N}\left(y_{i}-\mu_{g}\right)^{2} \gamma_{i, g}
\end{aligned}
$$

where the responsibilities are computed with the previous parameter estimates.
For model selection, i.e., finding the optimal poset structure, we employ simulated annealing (Kirkpatrick, Gelatt, and Vecchi, 1983), a heuristic search strategy, to find the ML poset. The poset space is sampled by modifications of relations of the current poset that result in a new poset. In each step, we allow for adding or removing a relation, or replacing two relations $e_{1} \prec e_{2} \prec e_{3}$ by $e_{1} \prec e_{2}$ and $e_{1} \prec e_{3}$. To speed up the procedure, we use the number of incompatible genotypes $|\mathscr{G} \backslash G\left(\mathscr{E}, \prec_{\text {new }}\right)|$ as a filter to discard unpromising poset structures prior to likelihood computation (Gerstung et al., 2009).

# 6 Simulation study 

We analyzed the performance of the simulated annealing algorithm in simulation experiments. Predicted posets were compared to the true posets in terms of the false positive rate (fpr), defined as the number of estimated false relations divided by $|\mathscr{E}|(|\mathscr{E}|-1) / 2$ (the maximum number of possible relations), and the false negative rate (fnr), defined as the number of true relations not included in the estimated poset divided by the number of true relations. Using the cross-validated mean squared error (MSE) $\sum_{g}[\phi(g)-\hat{\phi}(g)]^{2}$, the NI-CBN model was compared to a baseline regression model that is linear in the events $\mathscr{E}$. We report the relative MSE difference, $\Delta_{\mathrm{MSE}}=\left(\mathrm{MSE}^{\text {linear }}-\mathrm{MSE}^{\mathrm{NI}-\mathrm{CBN}}\right) / \mathrm{MSE}^{\text {linear }}$.

We analyzed six posets: two empty posets and two linear posets, each of size $|\mathscr{E}|=4$ and 7, the poset of Example 1 shown in Figure 1, and the poset displayed in Figure 3A which was selected based on real data (see Section 7). For each poset, we investigated models with parameters $\varepsilon \in\{0.001,0.01,0.1\}$ and $\sigma \in\{0.1,1\}$ by drawing $N=500$ or 1000 samples. For the empty and the linear posets, the

Table 1: NI-CBN performance for empty posets. Symbols are defined in the main text. False positive rate (fpr) and false negative rate (fnr) are reported with their standard error (se). In the penultimate column, $p$ is the $p$-value of a one-sided paired Wilcoxon rank sum test of the MSE of the NI-CBN model versus the linear model, based on the number of simulations given in the last column.


conditional probabilities $\theta$ were set such that all genotypes $g \in G(\mathscr{E}, \prec)$ have the same probability, $\theta_{e}^{\text {empty }}=1 / 2$ for all $e \in \mathscr{E}$, and $\theta_{i}^{\text {linear }}=i /(i+1)$ for linear posets $1 \prec 2 \prec 3 \prec \cdots \prec|\mathscr{E}|$. For the poset of Example 1, equal genotype probabilities can not be achieved and $\theta$ was drawn uniformly from the interval $(0.5,0.9)$. For the poset of Figure 3A the fitted values $\theta=(0.42,0.40,0.18,0.59,0.69,0.87,0.65)$ were used. The parameters $\mu$ of the NI-CBN model were generated by drawing uniform random numbers $r_{i}, i=1, \ldots,|\mathscr{E}|-1$, from the interval $(-1,3)$, sorting

Table 2: NI-CBN performance for linear posets. Symbols are defined in the main text and in the legend of Table 1.


them as $-1=r_{0}<r_{1}<\cdots<r_{|\mathscr{E}|-1}<r_{|\mathscr{E}|}=3$, and setting $\mu_{\varepsilon}=r_{|\xi|}$. This defines a graded fitness landscape, i.e., the fitness (or phenotype) depends only on the number of mutations (Beerenwinkel et al., 2006). The runtime for fitting each model was between one minute and two hours on a standard PC.

For the empty posets (Table 1), false negatives can not occur. False positive rates were generally small and always below 5\%. For the linear posets (Table 2), false positive rates are comparably low, but the false negative rate can reach high levels, especially for high error rates $\varepsilon=0.1$ and small sample sizes $N=500$. Similar poset reconstruction performance was observed for the poset of Example 1 and for the poset of Figure 3A with somewhat increased false positive rates (Table 3). In

Table 3: NI-CBN performance for the poset of Example 1 (4 events) and the poset of Figure 3A (7 events). Symbols are defined in the main text and in the legend of Table 1.


general, poset reconstruction is increasingly difficult for larger posets, higher error rates $\varepsilon$, and smaller sample size $N$, while the impact of the phenotype variance $\sigma^{2}$ appears to be small (Tables 1-3).

For most posets and parameter constellations, the NI-CBN model significantly outperformed the linear model in terms of the MSE of predicted phenotypes. This was not the case only for some of the models defined by the empty poset on seven events, which was also the most difficult model to fit (Table 1). This expected superiority of the NI-CBN model confirms that linear models are not appropriate for many types of fitness landscapes.

# 7 Application to HIV drug resistance 

We consider genetic changes in the HIV genome in response to drug therapy and analyze two dataset obtained from the Stanford HIV Drug Resistance Databse (Rhee, Gonzales, Kantor, Betts, Ravela, and Shafer, 2003). The first dataset consists of 617 observations of the HIV reverse transcriptase (RT) genotype and paired measurements of phenotypic resistance to the RT inhibitor zidovudine. Resistance levels are reported as the logarithm of the fold-change in susceptibility of the virus to the drug as compared to the wild type. The genetic events are the amino acid changes $\mathscr{E}=\{41 \mathrm{~L}, 67 \mathrm{~N}, 69 \mathrm{D}, 70 \mathrm{R}, 210 \mathrm{~W}, 215 \mathrm{Y}$, and 219Q\}, where, for example, 41L stands for the occurrence of leucine (L) at position 41 of the HIV RT. These mutations are known to be involved in the development of zidovudine resistance (Shafer and Schapiro, 2008).

The poset of the ML NI-CBN found by simulated annealing is shown in Figure 3A. It exhibits two independent mutational pathways, one involving mutations 41L and 215Y, the other 67 N and 70R, that have been described before (Boucher, O’Sullivan, Mulder, Ramautarsing, Kellam, Darby, Lange, Goudsmit, and Larder, 1992, Larder, 1994). In previous work, a more restrictive model class of tree posets was not able to find the independence of both pathways, but a much more complex mixture model of tree posets was (Beerenwinkel, Rahnenführer, Däumer, Hoffmann, Kaiser, Selbig, and Lengauer, 2005). The model applied here offers more structural flexibility with the same number of free model parameters and it integrates both genotypic and phenotypic data into a single model.

The induced genotype lattice $G(\mathscr{E}, \prec)$ and the predicted drug resistance levels are visualized in Figure 3B and listed in the Appendix (Table 4). The lattice consists of 28 genotypes and the estimated isotonic regression function groups these into twelve genotype blocks of identical resistance to zidovudine. This description of the evolutionary process is much simpler than considering all $|\mathscr{G}|=2^{7}=128$ combinatorially possible genotypes. The model suggests that under the selective pressure of zidovudine, neutral networks of neighboring genotypes of (near) identical fitness exist.

Linear regression of zidovudine resistance on the genetic events $\mathscr{E}$ was slightly less accurate than the NI-CBN predictions with a MSE of $0.45 \pm 0.024$ versus $0.44 \pm 0.025$ as estimated by 10 -fold cross-validation ( $p=0.053$, one-sided, paired Wilcoxon rank sum test). Despite the comparable predictive performance, the two models have a very different structure. The NI-CBN model allows for non-linear effects of mutations and for context dependancy, whereas in the linear model, the effect per mutation is averaged over all genetic contexts. For the zidovudine data, the linear model tends to underestimate resistance in genotypes with few mutations and to overestimate resistance when many mutations have occurred

(Appendix, Table 4).
(A)
![img-3.jpeg](img-3.jpeg)
(B)
![img-4.jpeg](img-4.jpeg)

Figure 3: Cover relations of the optimal poset (A) and induced genotype lattice (B) for the development of HIV resistance to the nucleotide RT inhibitor zidovudine. Genotypes are encoded as binary strings that refer to the seven amino acid substitutions 41L, 67N, 69D, 70R, 210W, 215Y, and 219Q in the RT gene. The predicted levels of phenotypic resistance are color-coded (blue $=$ fully susceptible, red $=$ highly resistant). Further details, including the remaining model parameters and confidence intervals are given in the Appendix, Table 4 and Table 5.

(A)
![img-5.jpeg](img-5.jpeg)
(B)
![img-6.jpeg](img-6.jpeg)

Figure 4: Cover relations of the optimal poset (A) and induced genotype lattice (B) for the development of HIV resistance to the PR inhibitor indinavir. Genotypes are encoded as binary strings that refer to the six amino acid substitutions 46I, 48V, 54V, 82A, 84V, and 90M in the PR gene. The predicted levels of phenotypic resistance are color-coded (blue $=$ fully susceptible, red $=$ highly resistant). Further details, including the remaining model parameters and confidence intervals are given in the Appendix, Table 7 and Table 8.

We assessed the uncertainty associated with model estimation using the bootstrap. For the fixed optimal model structure shown in Figure 3, the model parameters $\theta, \mu, \sigma$, and $\varepsilon$ were re-estimated from 100 bootstrap samples. The resulting $95 \%$ confidence intervals are given in the Appendix, Tables 4 and 5. Another 100 bootstrap samples were used to quantify the uncertainty in estimating the model structure. In Table 6, the abundance of each cover relation (or equivalently, of each edge in the Bayesian network) among the 100 optimal posets is shown. This analysis strongly supports the optimal poset of Figure 3. The only appreciable uncertainty of the model structure that we detected is the order in which mutations 41 L and 215 Y occur. The data appears to favor the relation $41 \mathrm{~L} \prec 215 \mathrm{Y}$, but it also provides some support for $215 \mathrm{Y} \prec 41 \mathrm{~L}$, which indicates that both single mutants are almost equally likely to occur.

The second dataset consists of 1473 genotypes defined on the resistanceassociated amino acid substitutions $\mathscr{E}=\{46 \mathrm{I}, 48 \mathrm{~V}, 54 \mathrm{~V}, 82 \mathrm{~A}, 84 \mathrm{~V}, 90 \mathrm{M}\}$ in the HIV protease (PR) and paired measurements of resistance to the PR inhibitor indinavir (Shafer and Schapiro, 2008). The optimal poset contains only two relations, inducing a genotype lattice of size 36 (Figure 4). The NI-CBN model groups these genotypes into 13 blocks of identical resistance levels (Appendix, Table 7). Again, the effect of several mutations appears to depend on the genetic background in which they occur. Because the linear regression model can not capture these dependencies, it is outperformed by the NI-CBN model in terms of MSE ( $0.27 \pm 0.013$ versus $0.25 \pm 0.013, p=0.003$ ). All model parameters and their bootstrap confidence intervals are given in the Appendix, Tables 7 and 8. The structural uncertainty about the optimal poset is summarized in Table 9 of the Appendix, emphasizing the general stability of the poset while suggesting the cover relation $82 \mathrm{~A} \prec 54 \mathrm{~V}$ as an alternative to $54 \mathrm{~V} \prec 82 \mathrm{~A}$, although with less than half the bootstrap support.

# 8 Conclusions 

We have introduced a statistical model for jointly estimating the dynamics of accumulating mutations in a population and the associated phenotypic changes. The I-CBN model is a CBN model coupled with isotonic regression. It estimates constraints on the order in which mutations occur by a poset and the genotype-phenotype map (or fitness landscape) by a monotonic function. Parameter estimation and model selection are straightforward and efficient for this model. The NI-CBN model accounts for noisy observations and we have presented an EM algorithm for parameter estimation in this setting. For model selection, we propose a stochastic search procedure and we have implemented a simulated annealing algorithm.

The model has been tested on simulated data and applied to paired genotypephenotype HIV drug resistance data. The NI-CBN model generalizes earlier efforts to estimate dependencies among HIV mutations from genotype data alone based on posets (Beerenwinkel et al., 2007, Beerenwinkel and Sullivant, 2009, Gerstung et al., 2009), tree posets or mixtures of trees (Beerenwinkel et al., 2005), and general Bayesian networks (Deforche et al., 2006). It can also be regarded as a model for regressing viral resistance phenotype on genotype. The isotonic regression model on the genotype lattice applied here combines the ability of non-linear models to account for context specificity with model interpretability.

Estimating drug resistance and the probability of evolutionary escape have been shown to improve predictions of clinical outcomes of antiretroviral therapy (Beerenwinkel, Lengauer, Däumer, Kaiser, Walter, Korn, Hoffmann, and Selbig, 2003b, Altmann, Beerenwinkel, Sing, Savenkov, Däumer, Kaiser, Rhee, Fessel, Shafer, and Lengauer, 2007). The NI-CBN model estimates both quantities jointly, and thus, will be a natural choice for enhancing clinical response predictions.

The monotonic block structure of the regression function highlights two features of evolutionary escape from drug pressure: the process is directed towards increasing levels of resistance and genotype blocks of identical resistance phenotype indicate connected neutral networks. Evolutionary escape may thus include neutral mutations within blocks and selectively advantages mutations that cause the transition to a new block. A similar drift-and-shift pattern of evolutionary escape from immune pressure has been described for Influenza A virus (Koelle, Cobey, Grenfell, and Pascual, 2006, van Nimwegen, 2006).

The NI-CBN model presented here can offer new insights into the structure of mutational pathways and the dynamics of evolutionary escape. In the future, the model might be improved in several ways. For example, large genetic event sets can not be handled with the current algorithms and often a pre-selection is necessary. The number of model parameters grows linearly with the lattice size, which in turn can be at worst exponential in the number of events. This raises the issue of overfitting of the regression function, and additional regularization may be beneficial. On the other hand, additional parameters could make the model more flexible and allow for better fitting of the obsevred data. For example, we have chosen to model phenotypic variance by a single parameter $\sigma$ for all genotypes in order to keep the total number of model parameters small and because there was no obvious reason to believe that this term differs between genotypes. In principle, however, one can assume different variance parameters $\sigma_{g}$ for each genotype $g$. Similarly, more detailed error models are conceivable that account separately for false positive and false negative observations (Beerenwinkel and Drton, 2007), or explicitly model the error process of the measuring device.

Although we have restricted our applications here to the development of HIV drug resistance, we expect the NI-CBN model to be useful also for other pathogens and for modeling the genetic progression of cancer, where the events may range from single nucleotide variants to large-scale genomic rearrangements.

# Appendix 

Table 4: HIV RT genotype lattice for zidovudine; see Figure 3.


Table 5: Parameter estimates and their $95 \%$ bootstrap confidence intervals for the zidovudine NI-CBN model displayed in Figure 3. The estimates for the parameters $\mu_{g}$ are shown in Table 4.


Table 6: Bootstrap analysis of the structural stability of the zidovudine NI-CBN model displayed in Figure 3. The entry with row index mutation $e$ and colum index mutation $f$ denotes the number of times the relation $e \prec f$ appeared as a cover relation (or equivalently, the edge $e \rightarrow f$ appeared in the graph of the Bayesian network model) among 100 bootstrap samples. Numbers in bold face indicate the presence of the corresponding edge in the optimal ML poset of Figure 3.


Beerenwinkel et al.: Learning Monotonic Genotype-Phenotype Maps

Table 7: HIV PR genotype lattice for indinavir; see Figure 4.


Table 8: Parameter estimates and their $95 \%$ bootstrap confidence intervals for the zidovudine NI-CBN model displayed in Figure 4. The estimates for the parameters $\mu_{g}$ are shown in Table 7.


Table 9: Bootstrap analysis of the structural stability of the indinavir NI-CBN model displayed in Figure 4. The entry with row index mutation $e$ and colum index mutation $f$ denotes the number of times the relation $e \prec f$ appeared as a cover relation (or equivalently, the edge $e \rightarrow f$ appeared in the graph of the Bayesian network model) among 100 bootstrap samples. Numbers in bold face indicate the presence of the corresponding edge in the optimal ML poset of Figure 4.

