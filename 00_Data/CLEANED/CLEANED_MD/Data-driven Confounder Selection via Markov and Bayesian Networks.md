# Data-Driven Confounder Selection via Markov and Bayesian Networks 

Jenny Häggström*<br>Department of Statistics, USBE, Umeå University, SE-901 87 Umeå, Sweden<br>*email: jenny.haggstrom@umu.se


#### Abstract

Summary: To unbiasedly estimate a causal effect on an outcome unconfoundedness is often assumed. If there is sufficient knowledge on the underlying causal structure then existing confounder selection criteria can be used to select subsets of the observed pretreatment covariates, $X$, sufficient for unconfoundedness, if such subsets exist. Here, estimation of these target subsets is considered when the underlying causal structure is unknown. The proposed method is to model the causal structure by a probabilistic graphical model, e.g., a Markov or Bayesian network, estimate this graph from observed data and select the target subsets given the estimated graph. The approach is evaluated by simulation both in a high-dimensional setting where unconfoundedness holds given $X$ and in a setting where unconfoundedness only holds given subsets of $X$. Several common target subsets are investigated and the selected subsets are compared with respect to accuracy in estimating the average causal effect. The proposed method is implemented with existing software that can easily handle high-dimensional data, in terms of large samples and large number of covariates. The results from the simulation study show that, if unconfoundedness holds given $X$, this approach is very successful in selecting the target subsets, outperforming alternative approaches based on random forests and LASSO, and that the subset estimating the target subset containing all causes of outcome yields smallest MSE in the average causal effect estimation.


Key words: Bayesian networks; Causal inference; Confounding; Covariate selection; Markov networks; Matching; TMLE.

## 1 Introduction

To get an unbiased estimate of a causal effect, of a treatment on some outcome, the treatment assignment is often assumed to be unconfounded, which is the case, e.g., when assignment to treatment is randomized. In an observational study treatment assignment is not randomized, and to get unbiased causal effect estimates we need to make sure that the assumption of unconfoundedness is plausible when conditioning on some set of covariates. Two important questions are: 1) Which set of covariates should we aim to condition on? and 2) How should we in practice go about to select the latter set of covariates? Often the answer to the first question has been "the set of covariates that are common causes of treatment and outcome" or "all observed pretreatment covariates", hereinafter referred to as 'the common cause criterion' and 'the pretreatment criterion', respectively. However, in response to Rubin (2007), in a series of letters to the editor and author's replies (Shrier, 2008; Rubin, 2008a; Pearl, 2009b; Sjölander, 2009; Rubin, 2009) and later on in VanderWeele and Shpitser (2011) it was discussed under what circumstances conditioning on the covariate set defined by the common cause criterion or the pretreatment criterion will in fact induce bias in the causal effect estimate instead of reducing it.

In an attempt to mediate between the standpoints of Pearl, Shrier, Sjölander and Rubin VanderWeele and Shpitser (2011) proposed an alternative covariate selection criterion, 'the disjunctive cause criterion'. The disjunctive cause criterion entails selecting all covariates that are causes of treatment and/or causes of outcome, and will, under certain assumptions, result in unconfoundedness. Specifically, the disjunctive cause criterion is similar to 'the backdoor path criterion' (Pearl, 1995) in the sense that the covariate set selected by the disjunctive cause criterion will suffice to block all backdoor paths from treatment to outcome if such a set exists. The main practical difference between these two criteria is that to use the backdoor path criterion, knowledge of the full causal structure of the data is needed but to use the disjunctive cause criterion it is sufficient to know which covariates are causes of the treatment and which covariates are causes of the outcome. VanderWeele and Shpitser (2011) dismiss the practical usefulness of the backdoor path criterion and point out that "In a number of analyses in the biomedical and social sciences, such complete knowledge of causal structures is unlikely" (Section 1, p.1406). Regarding the knowledge of the causal structure that is required for use of the disjunctive cause criterion, they are however optimistic, stating that "In many epidemiological and biomedical applications, subject matter experts have intuitive knowledge of whether each covariate is a cause of the treatment or the outcome" (Section 6, p.1411). If it is indeed the case, that we have the knowledge required

to use the disjunctive cause criterion (or the backdoor path criterion), then the problem of covariate selection, with respect to unconfoundedness, is solved and the question in 2) is redundant.

However, when knowledge of the causal structure is not sufficient for use of the disjunctive cause criterion the process of covariate selection can be aided by data-driven procedures. Moreover, even in cases where the disjunctive cause criterion can be used, mean squared error of nonparametric estimators of causal effects may be improved by further reducing the dimensionality of the covariate set (de Luna, Waernbaum, and Richardson, 2011). Given a set of covariates such that conditioning on this set unconfoundedness is upheld the latter authors propose general algorithms, in line with the common cause criterion, for selecting minimal sets of covariates such that unconfoundedness still holds when conditioning on the selected sets. These algorithms are implemented using marginal coordinate hypothesis testing (continuous covariates) and kernel smoothing (continuous and/or discrete covariates) in the R package CovSel (Häggström, Persson, Waernbaum, and de Luna, 2015). These implementations have in simulation studies (Persson, Häggström, Waernbaum, and de Luna, 2017) been shown to perform well in reducing the dimensionality of the covariate set while still upholding unconfoundedness, thereby resulting in improved mean squared error. For other recently proposed covariate selection procedures see, e.g., Persson et al. (2017), Schnitzer et al. (2016) and references therein. Existing proposals have in common that they are computer intensive, yielding prohibitive running times in high dimensional applications (in terms of number of covariates and number of units).

In this paper we propose and study the use of Markov and Bayesian network algorithms, more precisely Max-Min Parents and Children (MMPC) and Max-Min Hill-Climbing (MMHC) (Tsamardinos, Brown, and Aliferis, 2006), in conjunction with the covariate selection algorithms in de Luna et al. (2011). MMHC has in empirical evaluations been shown to outperform the PC algorithm (Spirtes et al., 2000), previously studied by Maathuis, Kalisch, and Bühlmann (2009) in a similar causal inference setting (although not for explicitly selecting covariates), both with regard to computation time and in ability to accurately estimate the true causal structure (Tsamardinos et al., 2006). To the author's knowledge, using estimated graphs to explicitly select covariates to control for, as a step completely separated from the nonparametric estimation of causal effects, has not been proposed and studied elsewhere.

The performance of the proposed data-driven covariate selection procedures is investigated, using simulations, in two general high-dimensional scenarios: 1) Unconfoundedness holds given the full covariate set, 2) Unconfoundedness does not hold given the full covariate set, but it does hold given a subset of the full covariate set. In scenario 1), the results show that this approach is very successful in selecting the target covariate subsets. Furthermore, targeting the subset containing all causes of outcome often yields smallest MSE in the average causal effect (ACE) estimation, but the magnitude of the reduction in MSE (relative to conditioning on the full covariate set) depends on the ACE estimator. The proposed covariate selection algorithms are implemented in the R package CovSelHigh (Häggström, 2016).

The remainder of this paper is organized as follows. In Section 2 relevant notation and concepts from causal inference are reviewed. Section 3 focuses on covariate selection when the causal structure is known and Section 4 on covariate selection using Markov and Bayesian network algorithms when the causal structure is unknown. In Section 5 the simulation study is presented. In Section 6 the proposed approach is illustrated using a large register data set with which the ACE of C-section delivery on asthma medication early in life is estimated. The paper is concluded with a discussion in Section 7.

# 2 Context and Terminology 

### 2.1 Potential Outcomes and Unconfoundedness

Let $T$ denote a binary treatment, $Y$ denote outcome and $X$ denote the set of observed pretreatment covariates, i.e., the full covariate set. Within the potential outcome framework (Neyman, 1923; Rubin, 1974) we let $Y(1)$ and $Y(0)$ denote the potential outcomes for $Y$ under the two treatments $T=1$ and $T=0$, respectively. Since only one treatment assignment is possible for each unit only one of the two potential outcomes is observed, $Y=Y(0)(1-T)+Y(1) T$. In this paper, the ACE, $\beta=E\{Y(1)-Y(0)\}$, is the parameter of interest.

If treatment assignment is not randomized, $\beta$ is identified if a unit's potential outcomes does not depend on the treatments received by other units (stable unit treatment assumption, SUTVA) (Rubin, 1990) and we have available a set of pretreatment covariates $S$ such that the probability of receiving either treatment conditional on $S$ is bounded away from 0 (overlap assumption) and such that the treatment assignment is unconfounded conditional on $S$. Letting $\Perp$ mean "is independent of" (Dawid, 1979) the assumption of unconfoundedness is upheld if $Y(1), Y(0) \Perp T \mid S$.

### 2.2 Graphical Models

A graph $G=(V, E)$ consists of a set of vertices $V=\left\{V_{i}: i \in 1, \ldots, p\right\}$ and a set of edges $E$. The vertices represent random variables, and the edges describe pairwise relationships among the variables. Here, the two

types of graphs considered are undirected graphs and directed acyclic graphs (DAGs). In an undirected graph all edges are undirected $(-)$ and in a directed graph all edges are directed $(\rightarrow)$. A directed graph with no cycles is a DAG. Two vertices are adjacent if they are connected by an edge and the neighbors of a vertex $V_{i}$ consists of all vertices adjacent to $V_{i}$. Furthermore, we define a path in a graph as a sequence of edges connecting vertices such that each vertex on the path is visited only once. In a DAG a vertex is a collider on a path if the path enters and leaves the vertex via arrowheads. In this paper we interpret directed edges as causal, i.e., $V_{1} \rightarrow V_{2}$ means that $V_{1}$ is a cause of $V_{2}$, also $V_{1}$ is said to be a parent of $V_{2}$ and $V_{2}$ the child $V_{1}$ (Pearl, 2009a). In an undirected graph the Markov blanket of a vertex consists of the vertex's neighbors and in a DAG the Markov blanket of a vertex consists of the vertex's parents, children and children's other parents. The local Markov property holds with respect to an undirected graph $G$ if there exists a joint probability distribution for $V$ such that, for each $V_{i} \in V, V_{i}$ is conditionally independent of its non-neighbors given its neighbors. For a DAG the local Markov property holds if there exists a joint probability distribution for $V$ such that, for each $V_{i} \in V, V_{i}$ is conditionally independent of its non-descendants given its parents.

A Markov network is a model consisting of an undirected graph, $G=(V, E)$, and a joint probability distribution $P$ defined over $V$ such that the local Markov property holds with respect to $G$. Similarly, a Bayesian network is a model consisting of a DAG, $G=(V, E)$, and a joint probability distribution $P$ defined over $V$ such that the local Markov property holds with respect to $G$. A probability distribution is faithful to the graph if it obeys no further conditional independence relations than what are entailed by the local Markov property.

# 3 Target Covariate Subsets 

In this section, target covariate subsets are defined using the languages of potential outcomes and graphical models. Let $G_{t}=\left(V_{t}, E_{t}\right)$ with $V_{t}=\{X, T, Y(t)\}$ for $t=0,1$. The subset of $X$ that includes all causes of treatment is defined as $X_{\rightarrow T}=\left\{X_{i} \in X: X_{i} \rightarrow T \in E_{0} \cup E_{1}\right\}$. Similarly, let $X_{\rightarrow Y}=X_{\rightarrow Y}^{0} \cup X_{\rightarrow Y}^{1}=$ $\left\{X_{i} \in X: X_{i} \rightarrow Y(0) \in E_{0}\right\} \cup\left\{X_{i} \in X: X_{i} \rightarrow Y(1) \in E_{1}\right\}$ be the subset of $X$ that includes all causes of outcome. Furthermore, let the subset of $X_{\rightarrow T}$ consisting of elements dependent with outcome be defined as $Q_{\rightarrow T}=Q_{\rightarrow T}^{0} \cup Q_{\rightarrow T}^{1}$ where $Q_{\rightarrow T}^{t} \subseteq X_{\rightarrow T}$ such that $Y(t) \Perp X_{\rightarrow T} \backslash Q_{\rightarrow T}^{t} \mid Q_{\rightarrow T}^{t}$, for $t=0,1$, and let the subset of $X_{\rightarrow Y}$ consisting of elements dependent with treatment be defined as $Z_{\rightarrow Y}=Z_{\rightarrow Y}^{0} \cup Z_{\rightarrow Y}^{1}$ where $Z_{\rightarrow Y}^{t} \subseteq X_{\rightarrow Y}^{t}$ such that $T \Perp X_{\rightarrow Y}^{1} \backslash Z_{\rightarrow Y}^{t} \mid Z_{\rightarrow Y}^{t}$, for $t=0,1$. Defined in line with the common cause criterion, $Q_{\rightarrow T}$ is a subset of the covariates that cause treatment, and $Z_{\rightarrow Y}$ a subset of the covariates that cause outcome.

The following, similar but not identical to the above, sets are defined in de Luna et al. (2011): $X_{T} \subseteq X$ such that $T \Perp X \backslash X_{T} \mid X_{T}, X_{Y}=X_{0} \cup X_{1}$ where $X_{t} \subseteq X$ such that $Y(t) \Perp X \backslash X_{t} \mid X_{t}$ for $t=0,1, Q_{t} \subseteq X_{T}$ such that $Y(t) \Perp X_{T} \backslash Q_{t} \mid Q_{t}$ for $t=0,1$ and $Z_{t} \subseteq X_{Y}$ such that $T \Perp X_{Y} \backslash Z_{t} \mid Z_{t}$ for $t=0,1$. As long as we have unconfoundedness given $X$ the following equalities hold: $X_{\rightarrow T}=X_{T}, X_{\rightarrow Y}=X_{Y}, Q_{\rightarrow T}=Q$ and $Z_{\rightarrow Y}=Z$. The latter authors also state assumptions under which these sets are unique (de Luna et al., 2011, Lemmas A2-A5) and $Z$ and $Q$ are minimal sets that cannot be reduced without violating unconfoundedness (de Luna et al., 2011, Proposition 8). The above equalities do not hold in general since $X_{\rightarrow T}$ and $X_{\rightarrow Y}$ are defined in terms of edges present in a DAG while de Luna et al. (2011) define all sets in terms of conditional independencies.

The subset of $X$ that includes all causes of treatment and/or outcome, i.e., the disjunctive cause criterion subset, is defined as $X_{\rightarrow T, Y}=X_{\rightarrow T} \cup X_{\rightarrow Y}$. VanderWeele and Shpitser (2011) suggest a criterion where covariates unassociated with the outcome are iteratively discarded from $X_{\rightarrow T, Y}$, henceforth 'the disjunctive cause criterion with backward selection', and the subset of $X_{\rightarrow T, Y}$ consisting of elements that are associated with outcome is defined as $W_{\rightarrow Y}=W_{\rightarrow Y}^{0} \cup W_{\rightarrow Y}^{1}$ where $W_{\rightarrow Y}^{t} \subseteq X_{\rightarrow T, Y}$ such that $Y(t) \Perp X_{\rightarrow T, Y} \backslash W_{\rightarrow Y}^{t} \mid W_{\rightarrow Y}^{t}$, for $t=0,1$. If $X_{\rightarrow T}$ and $X_{\rightarrow Y}$ are uniquely defined then it follows that $X_{\rightarrow T, Y}$ is unique and under assumptions similar to Lemma A3 in de Luna et al. (2011) so is $W_{\rightarrow Y}$.

For illustrative purposes consider the causal diagram in Figure 1. Here, the observed pretreatment covariates $X=\left\{X_{i}: i \in 1, \ldots, 10\right\}$ are the only variables affecting $T$ and $Y$ and thus all of the covariate selection criteria mentioned in Section 1 would result in unconfoundedness. The target sets are $X_{\rightarrow T}=$ $X_{T}=\left\{X_{1}, X_{2}, X_{3}, X_{4}, X_{7}\right\}, X_{\rightarrow Y}=X_{Y}=\left\{X_{1}, X_{2}, X_{5}, X_{6}, X_{8}\right\}, Q_{\rightarrow T}=Q=\left\{X_{1}, X_{2}, X_{7}\right\}, Z_{\rightarrow Y}=Z=$ $\left\{X_{1}, X_{2}, X_{8}\right\}, X_{\rightarrow T, Y}=\left\{X_{1}, X_{2}, X_{3}, X_{4}, X_{5}, X_{6}, X_{7}, X_{8}\right\}$ and $W_{\rightarrow Y}=\left\{X_{1}, X_{2}, X_{5}, X_{6}, X_{7}, X_{8}\right\}$.

The common cause criterion would select $S=\left\{X_{1}, X_{2}, X_{7}\right\}=Q_{\rightarrow T}$, the pretreatment criterion would select $S=X$, the backdoor path criterion would select $S=\left\{X_{1}, X_{2}, X_{3}, X_{4}, X_{7}\right\}$, the disjunctive cause criterion would select $S=X_{\rightarrow T, Y}$ and the disjunctive cause criterion with backward selection would select $S=W_{\rightarrow Y}$.

Now consider the causal diagram in Figure 2. Here, in addition to $T, Y$ and $X=\left\{X_{i}: i \in 1, \ldots, 10\right\}$ we have a set of unobserved variables $U=\left\{U_{1}, U_{2}, U_{3}\right\}$ affecting $T$ and/or $Y$. The target sets $X_{\rightarrow T}, X_{\rightarrow Y}, Z_{\rightarrow Y}$, and $X_{\rightarrow T, Y}$ remain as for Figure 1 but now $Q_{\rightarrow T}=\left\{X_{1}, X_{2}, X_{4}, X_{7}\right\}$, and $W_{\rightarrow Y}=\left\{X_{1}, X_{2}, X_{4}, X_{5}, X_{6}, X_{7}, X_{8}\right\}$.

As pointed out by VanderWeele and Shpitser (2011), in this setting not all of the above covariate selection criteria would result in unconfoundedness. Except for the disjunctive cause criterion with backward selection,

![img-0.jpeg](img-0.jpeg)

Figure 1
A causal DAG without unobservables.
![img-1.jpeg](img-1.jpeg)

Figure 2
A causal DAG with unobservables.
all of the criteria would in this setting select the same sets as in the previous setting. However, the set selected by the common cause criterion, $\left\{X_{1}, X_{2}, X_{7}\right\} \neq Q_{\rightarrow T}$, would not result in unconfoundedness since it does not include the covariate $X_{4}$, which is now related to both $T$ and $Y$, the latter through the unobserved variable $U_{3}$. The set selected by the pretreatment criterion would fail to achieve unconfoundedness due to the inclusion of the covariate $X_{9}$, which is now a collider on the path between $T$ and $Y$ due to the unobserved variables $U_{1}$ and $U_{2}$. Conditioning on $X_{9}$ will thus open up this path between $T$ and $Y$ and introduce the so called $M$-bias (Greenland, 2003). The sets selected by the backdoor path criterion and the disjunctive cause criterion would however achieve unconfoundedness since both sets would include $X_{4}$ but not $X_{9}$. The disjunctive cause criterion with backward selection would select $S=\left\{X_{1}, X_{2}, X_{4}, X_{5}, X_{6}, X_{7}, X_{8}\right\}=W_{\rightarrow Y}$ which includes $X_{4}$ since it is now associated with the outcome and conditioning on this set upholds unconfoundedness. Conditioning on $Q_{\rightarrow T}$ would also, in this case, result in unconfoundedness.

Note that here the sets defined in de Luna et al. (2011) are $X_{T}=X_{\rightarrow T} \cup\left\{X_{9}\right\}, X_{Y}=X_{\rightarrow Y} \cup\left\{X_{4}, X_{9}\right\}$, $Q=Q_{\rightarrow T} \cup\left\{X_{9}\right\}$ and $Z=Z_{\rightarrow Y} \cup\left\{X_{4}, X_{9}\right\}$, all including $X_{9}$.

# 4 Covariate Selection When the Causal Structure is Unknown 

Given the setup stated in Section 2, and no further knowledge on the causal structure, only the pretreatment criterion can be readily used without aid of data-driven procedures. If we, in some way, from data estimate the dependence structure in the form of an undirected or directed graph then we can use the estimated graph to select covariates by reading off which covariates are related to $T$ and/or $Y \mid T=t$ for $t=0,1$.

There are many different methods available for estimating Markov and Bayesian networks (see, e.g., Friedman et al., 1999; Spirtes et al., 2000; Chickering, 2002; Tsamardinos et al., 2006, and references therein). In this paper, the Max-Min Parents and Children Algorithm (MMPC) and the Max-Min Hill-Climbing Algorithm (MMHC) are used to estimate the underlying structure of the data. Algorithms used for estimating such networks can be classified as either constraint-based or score-based. MMHC is a hybrid algorithm which as a first step uses the constraint-based MMPC algorithm to estimate a Markov network, i.e., an undirected graph, and

as a second step uses the score-based local optimization technique hill-climbing (similar to steepest ascent) to find the Bayesian network, i.e., the DAG, that best fits the data. For the purpose of estimating the graphs we assume that we have a copy of the data $\{X, T, Y\}$ where any continuous variables have been discretized.

# 4.1 The Max-Min Parents and Children Algorithm 

MMPC estimates the underlying graph structure by testing if the conditional independencies between the variables implied by a Markov network hold. One commonly used conditional independence test is based on the information-theoretic measure mutual information. Using the observed frequencies for variables $V_{i}, V_{j}$ and all the configurations of the variables in the conditioning set MI is estimated by $\widetilde{\mathrm{MI}}\left(V_{i}, V_{j} \mid V_{k}=\left\{V \backslash\left\{V_{i}, V_{j}\right\}\right\}\right)=$ $n^{-1} \sum_{a b c} n_{i j k}^{a b c} \ln \left\{n_{i j k}^{a b c} n_{k}^{c}\left(n_{i k}^{a c} n_{j k}^{b c}\right)^{-1}\right\}$, where $n_{i j k}^{a b c}$ is the size of the subsample where $V_{i}=a, V_{j}=b$ and $V_{k}=c$. $n_{k}^{c}, n_{i k}^{a c}$ and $n_{j k}^{b c}$ are defined analogously. $\widetilde{\mathrm{MI}}$ is proportional to the likelihood-ratio test (by a factor of $2 n$ ) and is asymptotically $\chi^{2}$-distributed with $(A-1)(B-1) C$ degrees of freedom, where $A, B$ and $C$ are the number of distinct configurations of $V_{i}, V_{j}$ and $V_{k}$.

The goal of MMPC is, for each variable $V_{i}, i=1, \ldots, p$, to return the set containing the variable's neighbors, i.e., the variable's Markov blanket, $M B^{i}$. For the variable $V_{i}$ and supposing that the rest of the variables in the graph are ordered as $\left(V_{1}, \ldots, V_{J}\right)$ MMPC starts in phase 1 with the empty set as the candidate $M B^{i}$, $C M B_{0}^{i}=\emptyset$, and updates the candidate $M B^{i}$ as follows, $j=1, \ldots, J$,

$$
C M B_{j}^{i}= \begin{cases}C M B_{j-1}^{i} & \text { if } V_{j} \Perp V_{i} \mid C M B_{j-1}^{i} \\ C M B_{j-1}^{i} \cup\left\{V_{j}\right\} & \text { otherwise }\end{cases}
$$

In phase 2 MMPC starts with the set $C M B_{J}^{i}$ from phase 1 as the candidate $M B^{i}$, i.e., $C M B_{0}^{i}=C M B_{J}^{i}$. Suppose that the variables in the set $C M B_{J}^{i}$ are ordered as $\left(V_{1}, \ldots, V_{K}\right)$ then the set is updated as follows, $k=1, \ldots, K$,

$$
C M B_{k}^{i}= \begin{cases}C M B_{k-1}^{i} \backslash\left\{V_{k}\right\} & \text { if } \exists A \subseteq C M B_{k-1}^{i} \backslash\left\{V_{k}\right\} \\ & \text { s.t. } V_{i} \Perp V_{k} \mid A \\ C M B_{k-1}^{i} & \text { otherwise }\end{cases}
$$

After running phase 1 and phase 2 for all $V_{i}, i=1, \ldots, p$, an attempt to remove any variables included in the final CMBs that are not a neighbor (false positives) is made in phase 3. Start with the set $C M B_{0}^{i}=C M B_{K}^{i}$ and suppose that the variables in the set $C M B_{K}^{i}$ are ordered as $\left(V_{1}, \ldots, V_{L}\right)$ then the set is updated as follows, $l=1, \ldots, L$,

$$
C M B_{l}^{i}= \begin{cases}C M B_{l-1}^{i} & \text { if } V_{i} \in C M B_{K}^{i} \\ C M B_{l-1}^{i} \backslash\left\{V_{l}\right\} & \text { otherwise }\end{cases}
$$

The final set for variable $V_{i}$ is $M B^{i}=C M B_{L}^{i}$. With the knowledge of all neighbors of all the variables in the graph the undirected graph can be constructed.

### 4.2 The Max-Min Hill-Climbing Algorithm

In the first step MMPC is performed. In the second step MMHC attempts to identify the Bayesian network that maximizes a score function indicating how well the graph fits the data, e.g., AIC, BIC or similar criteria. An empty graph is the starting point and a new candidate graph is generated by performing one of the following alterations to the current candidate graph: single-edge addition, single-edge deletion, or single-edge direction reversal. The alteration that leads to the largest increase in score is performed. The procedure is iterated until there is no alteration that increases the score. The optimization is constrained to only consider adding an edge if it is present in the undirected graph returned by MMPC in the first step.

### 4.3 Estimation of Target Covariate Subsets

The target covariate sets defined earlier are estimated by fitting a number of discrete Markov or Bayesian networks in a stepwise manner adhering to the covariate selection algorithms in de Luna et al. (2011). To be clear, we only estimate certain graphs and the sets of covariates in the Markov blankets of these estimated graphs are what is meant by "estimated target covariate sets". Given the assumed temporal order between $X, T$ and $Y$ we always incorporate the constraints that $T$ and $Y \mid T=t$ for $t=0,1$ have no children in $X$. Consider estimating the subgraph including only vertices $V=\{X, T\}$ then $\widetilde{X}_{\rightarrow T}$ is defined as the estimated Markov blanket of $T$. Given $\widetilde{X}_{\rightarrow T}$ we estimate the subgraphs including only vertices $V=\left\{\widetilde{X}_{\rightarrow T}, Y \mid T=t\right\}$ for $t=0,1$ and define $\widetilde{Q}_{\rightarrow T}=\widetilde{Q}_{\rightarrow T}^{0} \cup \widetilde{Q}_{\rightarrow T}^{1}$ as the union of the estimated Markov blankets for $Y \mid T=t$ for $t=0,1$. Similarly, we estimate $\widetilde{X}_{\rightarrow Y}$ by estimating the subgraphs including only vertices $V=\{X, Y \mid T=t\}$

for $t=0,1$ and define $\widehat{X}_{\rightarrow Y}=\widehat{X}_{\rightarrow Y}^{0} \cup \widehat{X}_{\rightarrow Y}^{1}$ as the union of the estimated Markov blankets for $Y \mid T=t$ for $t=0,1$. Given $\widehat{X}_{\rightarrow Y}$ we estimate the subgraphs including only vertices $V=\left\{\widehat{X}_{\rightarrow Y}^{t}, T\right\}$ for $t=0,1$ and define $\widehat{Z}_{\rightarrow}=\widehat{Z}_{\rightarrow Y}^{0} \cup \widehat{Z}_{\rightarrow Y}^{1}$ as the union of the estimated Markov blankets for $T$. Furthermore, $\widehat{X}_{\rightarrow T, Y}=\widehat{X}_{\rightarrow T} \cup \widehat{X}_{\rightarrow Y}$ and given $\widehat{X}_{\rightarrow T, Y}$ we estimate the subgraphs including only vertices $V=\left\{\widehat{X}_{\rightarrow T, Y}, Y \mid T=t\right\}$ for $t=0,1$ and define $\widehat{W}_{\rightarrow Y}=\widehat{W}_{\rightarrow Y}^{0} \cup \widehat{W}_{\rightarrow Y}^{1}$ as the estimated Markov blankets for $Y \mid T=t$ for $t=0,1$. Although MMHC results in a DAG, for our purposes, the directionality of the edges give no added information since we assume that $T$ and $Y \mid T=t$, for $t=0,1$, have no children in $X$ and we are not interested in the relations between the covariates. MMHC can however result in a graph with fewer edges than those present in the undirected graph produced by MMPC.

Note that technically this estimation strategy violates Rubin's "no outcome data"-policy (Rubin, 2007; Rubin, 2008b) which entails that study design, e.g., confounder selection, should be performed without any use of outcome data. However, the ACE is never estimated in the confounder selection process and outcome data are only considered separately for each treatment group, thus avoiding any difference in outcome between the treatment groups to influence the confounder selection and subsequent ACE estimation.

# 4.4 Theoretical Results 

C1. $X, T$ and $Y(t), t=0,1$ are all discrete random variables.
C2. $Y(t)$ and $T$ have no children in $X$ and $Y(t), t=0,1$ is not a parent of $T$. All confounders are observed.
C3. The underlying true causal structures are DAGs, denoted $G_{X, T, Y(t)}$ for $t=0,1$, involving the set of vertices $V_{X, T, Y(t)}=\{X, T, Y(t)\}$.
C4. There exist joint probability functions, denoted $p_{X, T, Y(0)}$ and $p_{X, T, Y(1)}$, such that the local Markov property holds with respect to $G_{X, T, Y(t)}$, for $t=0,1$.
C5. $p_{X, T, Y(0)}$ and $p_{X, T, Y(1)}$ are faithful to $G_{X, T, Y(t)}$, for $t=0,1$, respectively.
C6. A perfect conditional independence oracle is available.
Theorem 1: When conditions $C 1-C 6$ are satisfied, the estimated target covariate sets resulting from using MMPC will equal the true target covariate sets. That is, $\widehat{X}_{\rightarrow T}=X_{\rightarrow T}, \widehat{Q}_{\rightarrow T}=Q_{\rightarrow T}, \widehat{X}_{\rightarrow Y}=X_{\rightarrow Y}$, $\widehat{Z}_{\rightarrow}=Z_{\rightarrow Y}, \widehat{X}_{\rightarrow T, Y}=X_{\rightarrow T, Y}$ and $\widehat{W}_{\rightarrow Y}=W_{\rightarrow Y}$.

A proof of Theorem 1 appear in Appendix A.
Remark 1: Conditions C2-C5 are fairly reasonable and common assumptions in settings like these. If the outcome and/or some of the covariates are continuous variables (C1 violated) and there is a need for discretizing prior to performing confounder selection via MMPC, information will be lost and this can affect the performance of the confounder selection procedure in practice. Most notably, we do not have access to a perfect conditional independence oracle (C6 violated) and hence the quality of the confounder selection procedure will depend on the properties of the method used for determining conditional independencies.

As far as the author knows, there is no theoretical results regarding the final output of MMHC. However, since MMHC performs MMPC in the first step, when conditions C1-C6 are satisfied the estimated target covariate sets resulting from using MMHC will be equal to, or subsets of, the estimated target covariate sets resulting from MMPC.

## 5 Simulation Study

A simulation study is performed to evaluate 1) the ability of MMPC and MMHC, respectively, to retrieve the target covariate subsets $X_{\rightarrow T}, Q_{\rightarrow T}, X_{\rightarrow Y}, Z_{\rightarrow Y}, X_{\rightarrow T, Y}$ and $W_{\rightarrow Y}$ and 2) to what extent the retrieved covariate sets result in unconfoundedness and 3) the impact of the selected sets on the estimation of the ACE. Comparisons are made with two other methods sometimes used for variable selection, namely random forests (RF; Breiman, 2001) and LASSO (Tibshirani, 1996).

### 5.1 Simulation design

All simulations are repeated with 1000 iterations each, with sample sizes $n=500,1000,2000,10000$ and 100 covariates included in $X$. Data generation and all computations are performed with the software R (R Core Team, 2016) using the R package CovSelHigh (Häggström, 2016).

# 5.1.1 Setting 1: Unconfoundedness holds given $X$ 

In this setting the core causal structure corresponds to Figure 1. In addition to the ten covariates visible in Figure 190 additional covariates are generated, related to each other but not to the first ten covariates. Hence, the complete covariate set consists of 100 covariates,$X=\left\{X_{i}: i \in 1, \ldots, 100\right\}$. A mixture of continuous and discrete covariates are simulated and the ten covariates in the core causal structure are generated according to the following specification: $\left(R_{1}, X_{2}\right)^{T},\left(X_{5}, R_{2}\right)^{T} \sim \mathrm{~N}\left((0,0)^{T},\left((1,0.5)^{T}(1,0.5)^{T}\right)\right), X_{1}=I\left(R_{1}>0\right), X_{6}=$ $I\left(R_{2}>0\right),\left(X_{7}, X_{8}\right)^{T} \sim \operatorname{Bernoulli}\left((0.5,0.5)^{T}\right.$, $\left.\left((1,0.7)^{T}(1,0.7)^{T}\right)\right), X_{3}, X_{10} \sim \operatorname{Bernoulli}(0.5), X_{4}, X_{9} \sim \mathrm{~N}(0,1)$.

We have that $\operatorname{Corr}\left(X_{1}, X_{2}\right)=\operatorname{Corr}\left(X_{5}, X_{6}\right)=0.4$ and $\operatorname{Corr}\left(X_{7}, X_{8}\right)=0.7$. For a full specification of how the rest of the covariates are generated see the function cov.sel.high.sim in the R package CovSelHigh. Let $f_{T}(X)=3-2 X_{1}-2 X_{2}-2 X_{3}-X_{4}-2 X_{7}$ and $f_{Y}(X)=4 X_{1}+2 X_{2}+2 X_{5}+4 X_{6}+4 X_{8}$, then the treatment variable, $T$, is generated from $n$ Bernoulli trials with the treatment probability $\mathrm{P}(T=1 \mid X)=\left[1+\exp \left\{f_{T}(X)\right\}\right]^{-1}$. The coefficients are chosen such that $\mathrm{E}(T)=0.5$. Three outcome models are generated: one linear, one binary and one nonlinear. The linear outcome model, for $t=0,1$, is $Y(t)=2+2 t+f_{Y}(X)+\varepsilon_{t}$, where $\varepsilon_{t} \sim \mathrm{~N}(0,1)$. The binary outcome model, for $t=0,1$, is generated as Bernoulli trials with probabilities $\mathrm{P}\{Y(t)=1 \mid X\}=$ $\left[1+\exp \left\{-2-2 t+f_{Y}(X)\right\}\right]^{-1}$. The more complex nonlinear outcome model, for $t=0,1$, is specified as $Y(t)=2+4.4 t+f_{t}(X)+\varepsilon_{t}$, where $f_{t}(X)=(7-4 t) X_{1}-\left\{(6+3 t) X_{6}\right\}\left\{0.5+\left(X_{2}+1.4\right)^{(2+2 t)}\right\}^{-1}+2 X_{5}^{2}+4 X_{8}$, and $\varepsilon_{t} \sim \mathrm{~N}(0,1)$. In order to uphold the assumption of unconfoundedness, a selected subset has to include one of the subsets, $\left\{X_{1}, X_{2}, X_{7}\right\}$ or $\left\{X_{1}, X_{2}, X_{8}\right\}$.

### 5.1.2 Setting 2: $M$-bias given $X$

In this setting the causal structure corresponds to Figure 2. Here $X_{4}, X_{9}, T, Y(0)$ and $Y(1)$ all depend on the unobservable variables $U_{1}, U_{2}$ and $U_{3}$. Everything else is analogous to the data generating process described in Section 5.1.1. Now, let $U_{1}, U_{2}, U_{3} \sim \mathrm{~N}(0,1), \nu_{1}, \nu_{2} \sim \mathrm{~N}(0,0.5), X_{4}=0.2+0.8 U_{3}+\nu_{1}$, and $X_{9}=1+2 U_{1}+3 U_{2}+\nu_{2}$. Here the outcome model functions are $f_{T}(X)=3-2 X_{1}-2 X_{2}-2 X_{3}-X_{4}-2 X_{7}-U_{1}$, $f_{Y}(X)=4 X_{1}+2 X_{2}+2 X_{5}+4 X_{6}+4 X_{8}+7 U_{2}+2 U_{3}$, and, for $t=0,1, f_{t}(X)=(7-3 t) X_{1}-\left\{(6+3 t) X_{6}\right\}\{0.5+$ $\left.\left(X_{2}+1.4\right)^{(2+2 t)}\right\}^{-1}+2 X_{5}^{2}+4 X_{8}+7 U_{2}+2 U_{3}$. With these alterations the treatment variable $T$ and outcomes for the linear, binary and nonlinear models are generated following the specification in Section 5.1.1.

### 5.2 Estimation of the ACE

To illustrate the impact of the estimated target subsets on the estimation of the ACE we consider two different strategies: propensity score matching (PSM; Abadie and Imbens, 2006) and targeted maximum likelihood estimation (TMLE; van der Laan and Rubin, 2006). PSM has several downsides (see, e.g., King and Nielsen, 2016) but is possibly the most popular strategy in practice. TMLE is a doubly robust estimator, i.e., consistent if either propensity score or outcome model is correct, and consistent and efficient if both models are correct. For PSM the propensity score is estimated by main effects logistic regression. One-to-one matching with replacement, and Euclidean distance as matching criterion, is used. For TMLE both the propensity score and outcome model is estimated by Bayesian additive regression trees (BART; Chipman et al., 2010). BART is a nonparametric regression method that have been shown to perform well in finite samples (Hill, 2011).

### 5.2.1 Implementation details

MMPC and MMHC are computed using the functions mmpc and mmhc in the package bnlearn (Scutari, 2010). The argument optimized is set to FALSE and for MMHC score="aic". RF is computed using the function randomForest in the package randomForest (Liaw and Wiener, 2002). Variables with importance larger than $25 \%$ of the largest importance are included in the estimated set. LASSO is computed using the function cv.glmnet in the package glmnet (Friedman, Hastie, and Tibshirani, 2010) and variables with nonzero coefficients at lambda. 1se are included in the estimated set. The LASSO model is specified to always include main effects, quadratic terms for the continuous covariates and all two-way interactions. $T$ and the discrete covariates are treated as factors for all four methods. For MMPC and MMHC continuous covariates and $Y$ are first discretized (using discretize with method="quantile" in bnlearn) and subsequently treated as factors. For RF, LASSO and when estimating the propensity score, continuous variables are not discretized. If $\widehat{S}=\emptyset$, where $\widehat{S}$ is an estimate of the target covariate subset $S$, the propensity score is estimated as the proportion of treated units. The ACE estimators are evaluated with $\widehat{S}$ equal to each of the following covariate sets: $X, \widehat{X}_{\rightarrow T}, \widehat{Q}_{\rightarrow T}$, $\widehat{X}_{\rightarrow Y}, \widehat{Z}_{\rightarrow Y}, \widehat{X}_{\rightarrow T, Y}$ and $\widehat{W}_{\rightarrow Y}$. PSM is performed using the function Match in the package Matching (Sekhon, 2011). TMLE estimates are computed using the functions bartMachine in package bartMachine (Kapelner and Bleich, 2016) and tmle in package tmle (Gruber and van der Laan, 2012), default argument values are used.

# 5.3 Simulation Results 

The results from the covariate selection algorithms are summarized in Tables 1-24 in Appendix B, where selection success rates and median cardinality of the selected sets are presented. Three definitions of success are used for the selected subset, $\widehat{S}$; i) unconfoundedness holds, i.e., $(Y(1), Y(0)) \Perp T \mid \widehat{S}$, ii) the target subset is included in the selected subset $(S \subseteq \widehat{S})$, and iii) equal subsets $(S=\widehat{S})$. The tables also include empirical bias, standard deviation and MSE for the ACE estimation as well as confidence interval coverage, mean width and mean lower and upper confidence interval limits. Results for Setting 1, $n=2000$, are illustrated in Figures 3-5. Results for $\widehat{W}_{\rightarrow Y}$ are omitted throughout due to the fact that when the causal structure is estimated $\widehat{W}_{\rightarrow Y}$ and $\widehat{X}_{\rightarrow Y}$ turn out to be virtually identical.

In Setting 1, when the sample size is relatively small $(n=500, n=1000)$ neither of the network algorithms succeed in selecting only sets that uphold unconfoundedness. MMPC has in these cases higher rates of success than MMHC. For the linear outcome model, when $n=500$ the success rates for MMPC and MMHC are in the range $[63.6,99.2]$ and $[31.6,88.2]$, respectively, and for $n=1000$ the ranges are $[94.9,100.0]$ and $[66.1$, $98.8]$. However, when the sample size is relatively large $(n=2000, n=10000)$ virtually all selected sets have $100 \%$ success rate in upholding unconfoundedness (the exception is the $\widehat{Q}_{\rightarrow T}$ sets with success rates 99.8 when $n=2000$ ), and this is the case for both network algorithms. For the larger sample sizes MMPC and MMHC not only select sets that uphold unconfoundedness, they frequently manage to exactly select the target subsets. For the binary outcome model, when $n=500$ the success rates for MMPC and MMHC are in the range [57.3, $97.7]$ and $[29.0,85.4]$, respectively, and for $n=1000$ the ranges are $[92.8,100.0]$ and $[70.7,99.2]$. For the larger sample sizes the results are similar to the linear outcome case. For the nonlinear outcome model, when $n=500$ the success rates for MMPC and MMHC are in the range [83.2, 99.9] and [43.6, 99.7], respectively, and for $n=1000$ the success rates are 100.0 for all sets selected by MMPC and in the range [96.9, 100.0] for MMHC. For the larger sample sizes all sets have $100 \%$ success rate and both methods frequently manage to exactly select the target subsets.

RF performs similar to MMPC and MMHC with the important exception that it is, regardless of outcome model, unable to select the minimal target subsets $Q_{\rightarrow T}$ and $Z_{\rightarrow Y}$ with any desirable accuracy. Also, for the nonlinear outcome model case, RF fails when estimating the set $X_{\rightarrow Y}$.

Due to the fact that implementing the LASSO in a high-dimensional covariate space was much more time consuming than the other three methods, the investigation of LASSO is limited to $n=500,1000,2000$. LASSO is the only method that is able, regardless of sample size, to select sets that virtually always uphold unconfoundedness. However, sets selected by LASSO have much higher cardinality than the sets selected by the other three methods. Thus the dimension reduction is not as pronounced as with the other methods and the exact target sets are rarely selected. When $n=500,1000$, LASSO performs better than the other methods, while for the larger sample sizes sets selected by any of the network methods often result in smaller MSE than sets selected by LASSO.

The simulation settings for the linear and binary outcome cases in this paper are similar to the linear and binary outcome cases in Persson et al. (2017) which allow us to make some comparisons of the methods used here and the kernel smoothing method used in the latter paper. Note that the kernel smoothing procedure is very computer intensive and is not feasible for the relatively high dimensions studied in this paper. For $n=1000$ (the largest sample size studied in Persson et al. (2017)) and only 10 covariates in $X$ kernel smoothing performs marginally better than MMPC does (when $n=1000$ and 100 covariates), in terms of success rates in upholding unconfoundedness, but MMPC manages to exactly retrieve the target subsets much more frequently. MMHC on the other hand is outperformed by kernel smoothing for such a relatively small sample size.

When PSM is used, conditioning on one of the sets $X, \widehat{X}_{\rightarrow T}$ or $\widehat{X}_{\rightarrow T, Y}$ results in a considerable larger bias and variance than conditioning on any of the other sets (where success rates of upholding unconfoundedness are $100 \%$ ). These results corroborates the results for PSM in Persson et al. (2017) in so far that, with very few exceptions, conditioning on $\widehat{Q}_{\rightarrow T}$ results in lower MSE than conditioning on $\widehat{X}_{\rightarrow T}$ but that conditioning on $\widehat{X}_{\rightarrow Y}$ or $\widehat{Z}_{\rightarrow Y}$ in turn results in lower MSE than conditioning on $\widehat{Q}_{\rightarrow T}$. However, as pointed out by an anonymous referee, these results are probably, at least partly, driven by the fact that PSM with main effects logistic regression is a poor estimation strategy, and not by the selected sets per se. Consequently, when TMLE together with BART is used, first of all we see that MSEs generally are much lower than when using PSM with logistic regression. Secondly, we see that in many cases reducing the covariate set prior to estimating ACE results in higher MSE compared to using $X$. Still, for large sample sizes, conditioning on $\widehat{X}_{\rightarrow Y}$ results in a reduction in MSE compared to conditioning on $X$ and conditioning on $\widehat{X}_{\rightarrow T, Y}$ results in reduced or equal MSE compared to $X$.

In Setting 2, when unconfoundedness does not hold given $X$ the success rates are, as expected, very low. In Setting 2 there are two ways in which a set can fail to uphold unconfoundedness: 1) if it does not include $X_{4}$ and/or 2) if it includes $X_{9}$. For the larger sample sizes all methods select sets that include both $X_{4}$ and $X_{9}$ or include too few covariates, thus failing the unconfoundedness assumption. However, for PSM, except for $\widehat{X}_{\rightarrow T, Y}$, the sets selected by MMPC or MMHC often result in smaller bias and MSE compared to bias and MSE

![img-2.jpeg](img-2.jpeg)

Figure 3
Simulation results for Setting 1, $n=2000$. Selection success rates ( $\%$ ) for the covariate sets ( $\hat{S}$ ) selected by MMPC, MMHC, RF or LASSO. Definitions of success are; i) unconfoundedness holds ( $Y_{t} \perp T \mid \hat{S}$ ), ii) the target subset is included in the selected subset ( $S \subseteq \hat{S}$ ) and iii) equal subsets ( $S=\hat{S}$ ). The selected covariates sets are: covariates predicting treatment $\widetilde{X}_{\rightarrow T}$, covariates predicting outcome $\widetilde{X}_{\rightarrow Y}$, covariates predicting both treatment and outcome $\widetilde{Q}_{\rightarrow T} \subseteq \widetilde{X}_{\rightarrow T}, \widetilde{Z}_{\rightarrow Y} \subseteq \widetilde{X}_{\rightarrow Y}$ and $\widetilde{X}_{\rightarrow T, Y}=\widetilde{X}_{\rightarrow T} \cup \widetilde{X}_{\rightarrow Y}$.

![img-3.jpeg](img-3.jpeg)

Figure 4
Simulation results for Setting 1, $n=2000$. Absolute bias and MSE are for the ACE estimated using different sets of covariates as selected by MMPC and either propensity score matching (PSM) or targeted maximum likelihood estimation (TMLE). The different covariates sets are: $X$, covariates predicting treatment $\widehat{X}_{\rightarrow T}$, covariates predicting outcome $\widehat{X}_{\rightarrow Y}$, covariates predicting both treatment and outcome $\widehat{Q}_{\rightarrow T} \subseteq \widehat{X}_{\rightarrow T}$, $\widehat{Z}_{\rightarrow Y} \subseteq \widehat{X}_{\rightarrow Y}$ and $\widehat{X}_{\rightarrow T, Y}=\widehat{X}_{\rightarrow T} \cup \widehat{X}_{\rightarrow Y}$

Table 1
Computation time in seconds (and relative to MMPC) for $n=10000$ when only running the step were $X_{T}$ is estimated from $\{X, T\}$, i.e., mmpc, mmhc, cv.glmnet and randomForest are each run only once.


when conditioning on $X$. For TMLE it is only $\widehat{Q}_{\rightarrow T}, \widehat{X}_{\rightarrow Y}$ and $\widehat{Z}_{\rightarrow Y}$ that results in reduced MSE compared to $X$ for $n=10000$. Thus, in a situation where we are not perfectly sure that unconfoundedness is upheld when conditioning on $X$, at least for PSM, it does not seem to be harmful to use this confounder selection procedure for reducing the covariate set.

As mentioned in Section 5.3 implementing LASSO was more computer intensive than any of the methods MMPC, MMHC or RF. In Table 1 the computational times (measured by system.time) for $n=10000$ when only running the step where $\widehat{X}_{\rightarrow T}$ is estimated from $X$, i.e., mmpc, mmhc, cv.glmnet and randomForest are each run only once. Timings differ slightly between runs but the example in Table 1 give an accurate description of the difference between methods. The computations were run on a MacBook Pro (Early 2015) with 3,1 GHz Intel Core i7 Processor and 16 GB 1867 MHz DDR3 Memory.

# 6 Data Analysis 

Previous studies have indicated that children delivered by C-section are at an increased risk of developing wheezing and asthma (see, e.g., Magnus et al., 2011; Brábäck et al., 2013). Here, we select covariates for estimating the ACE of being delivered by C-section on, before the age of four, being prescribed medication commonly used to treat asthma. Using record linkage register data from the Umeå SIMSAM Lab (Lindgren, Nilsson, de Luna, and Ivarsson, 2016) all children being the result of first-time mothers giving birth to full term ( 37 or more full weeks of gestation) singleton live offspring in the year 2006 in Sweden were identified $(n=41857)$. From this population the subset of children being delivered by C-section or non-instrumental vaginal delivery, who were residents in Sweden during the whole study period, were offspring of two native Swedish parents and had no major malformations reported at birth were selected $(n=23817)$. Using data from the Swedish Prescribed Drug Registry all children being prescribed drugs with one of the ATC-codes (WHO Collaborating Centre for Drug Statistics Methodology, 2014) R03AC, R03AK, R03BA, R03BC, R03CC, R03DC (hereinafter "asthma drugs") at least once before the age of four were identified.

As potential confounders we included 24 variables, listed in Table 25 in Appendix C. All observations with missing data on any of the covariates were excluded $(n=2950)$, resulting in a complete cases sample containing $n=20867$ children. The proportion of children delivered by C-section was $20.9 \%$ and $39.7 \%$ of the children had been prescribed asthma drugs at least once before the age of four. MMPC and MMHC resulted in equal sets, namely: $\widehat{X}_{\rightarrow T}=\{$ Maternal BMI at first antenatal visit, Gestational age $\}, \widehat{Q}_{\rightarrow T}=\{$ Maternal BMI at first antenatal visit $\}, \widehat{X}_{\rightarrow Y}=\{$ Maternal asthma, Paternal asthma drugs prescription within 6 months before delivery, Offspring sex, Birth place $\}, \widehat{Z}_{\rightarrow Y}=\{$ Offspring sex, Birth place $\}, \widehat{X}_{\rightarrow T, Y}=\widehat{X}_{\rightarrow T} \cup \widehat{X}_{\rightarrow Y}$. The DAGs estimated by MMHC are given in Figures 1-7 in Appendix C (Cytoscape was used to visualize the graphs (Shannon et al., 2003)). PSM and TMLE were implemented as described in Section 5.2 and estimates of the ACE, i.e., risk difference, are presented in Table 2. For PSM the distributions of the estimated propensity scores for the different treatment groups were similar and exact matches were found when controlling for all sets except $X$ (where a caliper of 0.1 standard deviations of the estimated propensity score was used). The estimate based on raw data, not controlling for any confounders, suggest on average an $3.5 \%$ risk increase in being prescribed asthma drugs before the age of four if you are delivered by C-section compared to what would be the risk in case of non-instrumental vaginal delivery. For both PSM and TMLE, controlling for any of the selected covariate sets results in slightly lower point estimates, although all still statistically significant. Assuming that we have unconfoundedness given the 24 potential confounders we started with, and taking into consideration the results from the simulation study where controlling for $\widehat{X}_{\rightarrow Y}$ often was the best choice, the results in Table 2 suggest that the ACE lies in the range $[0.012,0.047]$.

Table 2 Estimates of the ACE. The cardinalities of the covariate sets (\#), ACE estimates ( $\hat{\beta}$ ), standard errors (SE; Abadie-Imbens for PSM and influence-curved based for TMLE), lower (CIL) and upper (CIU) limits of 95\% confidence intervals.


# 7 Discussion

In this paper, we have introduced the network algorithms MMPC and MMHC in conjunction with the covariate selection algorithms in de Luna et al. (2011) as methods for confounder selection in causal inference when the true causal structure is not known. Given that unconfoundedness holds when conditioning on $X$, the approach was shown, for sufficiently large sample sizes, to accurately estimate certain target covariate subsets. Compared to RF and LASSO, the network algorithms were preferable both with regard to estimation of the ACE and with regard to computational efficiency. However, it is very likely that the performance of RF and LASSO could be improved upon by carefully selecting their respective tuning parameter (variable importance cut-off and regularization parameter). Also, as expected, none of the four methods investigated were able to select covariate sets that uphold unconfoundedness when the true causal structure included a collider of unmeasured causes of the outcome and treatment. This is due to the fact that the methods cannot distinguish association from causation and thus a collider will frequently be included in the selected covariate set. How much one in practice should worry about the $M$-bias scenario exemplified in Setting 5.1.2 is debatable. Rubin (2009), Liu et al. (2012) and Ding and Miratrix (2015) suggest that it is rather uncommon and might be more of mathematical than practical interest. Moreover, the simulation results show that even if $M$-bias is present reducing the the dimension of the covariate set might still be beneficial.

The real data analysis consisted of 20867 observations and 24 covariates and this relatively high dimensional data proved to be more than feasible for MMPC and MMHC.

## Acknowledgements

This work was supported by the Swedish Research Council (Dnr: 2013-672). The simulations were performed on resources provided by the Swedish National Infrastructure for Computing (SNIC) at High Performance Computing Centre North (HPC2N). The Umeå SIMSAM Lab data infrastructure used in this study was developed with support from the Swedish Research Council and by strategic funds from Umeå University. The author is grateful to the Co-Editor, the Associate Editor, and the referee for their helpful and constructive comments.

# Appendix A: Proof of Theorem 1 in Section 4.4 

Proof. Let $G_{A, B}$ denote a graph involving only the variables in the sets $A$ and $B$. Consider the graphs $G_{X, T}$, $G_{X_{\rightarrow T}, Y(t)}, G_{X, Y(t)}, G_{X_{\rightarrow Y}, T}$ and $G_{X_{\rightarrow T, Y}, Y(t)}, t=0,1$.

It follows from C3 that the above graphs are all DAGs since each of them is a subgraph of a DAG.
It follows from C4-C5 that there exist joint probability distributions $p_{X, T}, p_{X_{\rightarrow T}, Y(t)}, p_{X, Y(t)}, p_{X_{\rightarrow Y}, T}$ and $p_{X_{\rightarrow T, Y}, Y(t)}, t=0,1$, such that the local Markov property holds and which are faithful to the respective subgraph.

Then, together with conditions C1-C2 and C6, it follows from Theorem 3 in Tsamardinos et al. (2006) that if in the estimated skeleton of $G_{X, T}$, produced by MMPC with input variables $\{X, T\}$, there is an edge connecting $T$ to $X_{j} \in X$ then $X_{j}$ is a parent of $T$. Hence, $\widehat{X}_{\rightarrow T}=X_{\rightarrow T}$. Similarly, if in the estimated skeleton of $G_{X_{\rightarrow T}, Y(t)}$, $t=0,1$, produced by MMPC with input variables $\left\{X_{\rightarrow T}, Y \mid T=t\right\}$, there is an edge connecting $Y \mid T=t$ to $X_{j} \in X_{\rightarrow T}$ then $X_{j}$ is a parent of $Y \mid T=t$, i.e., a parent of $Y(t)$ since $Y(t) \Perp T \mid X$. Hence, $\widehat{Q}_{\rightarrow T}^{t}=Q_{\rightarrow T}^{t}$, $t=0,1$ and therefore $\widehat{Q}_{\rightarrow T}=Q_{\rightarrow T}$. Analogously, $\widehat{X}_{\rightarrow Y}=X_{\rightarrow Y}$ and $\widehat{Z}_{\rightarrow}=Z_{\rightarrow Y}$. Since $\widehat{X}_{\rightarrow T, Y}=\widehat{X}_{\rightarrow T} \cup \widehat{X}_{\rightarrow Y}$ it follows that if $\widehat{X}_{\rightarrow T}=X_{\rightarrow T}$ and $\widehat{X}_{\rightarrow Y}=X_{\rightarrow Y}$ then $\widehat{X}_{\rightarrow T, Y}=X_{\rightarrow T, Y}$. Finally, according to the same reasoning as above using MMPC with input variables $\left(X_{\rightarrow T, Y}, Y \mid T=t\right)$ results in $\widehat{W}_{\rightarrow Y}=W_{\rightarrow Y}$

## Appendix B: Simulation results from Section 5.3

Table 3
Setting 1, linear outcome model, $n=500,1000$. The proportion (\%) of times the selected subset, $\widetilde{S}$, satisfies three conditions of unconfoundedness and the median cardinality of $\widetilde{S}$ (\#). Average bias (Bias), standard deviation (SD) and mean square error (MSE) from estimating ACE with PSM and TMLE.


Table 4
Setting 1, linear outcome model, $n=2000,10000$. The proportion (\%) of times the selected subset, $\widehat{S}$, satisfies three conditions of unconfoundedness and the median cardinality of $\widehat{S}$ (\#). Average bias (Bias), standard deviation (SD) and mean square error (MSE) from estimating ACE with PSM and TMLE.


Table 5
Setting 1, binary outcome model, $n=500,1000$. The proportion (\%) of times the selected subset, $\widehat{S}$, satisfies three conditions of unconfoundedness and the median cardinality of $\widehat{S}$ (\#). Average bias (Bias), standard deviation $(S D)$ and mean square error (MSE) from estimating ACE with PSM and TMLE.


Table 6
Setting 1, binary outcome model, $n=2000,10000$. The proportion (\%) of times the selected subset, $\widehat{S}$, satisfies three conditions of unconfoundedness and the median cardinality of $\widehat{S}$ (#). Average bias (Bias), standard deviation (SD) and mean square error (MSE) from estimating ACE with PSM and TMLE.


Table 7
Setting 1, nonlinear outcome model, $n=500,1000$. The proportion (\%) of times the selected subset, $\widehat{S}$, satisfies three conditions of unconfoundedness and the median cardinality of $\widehat{S}$ (\#). Average bias (Bias), standard deviation (SD) and mean square error (MSE) from estimating ACE with PSM and TMLE.


Table 8
Setting 1, nonlinear outcome model, $n=2000,10000$. The proportion (\%) of times the selected subset, $\widehat{S}$, satisfies three conditions of unconfoundedness and the median cardinality of $\widehat{S}$ (\#). Average bias (Bias), standard deviation (SD) and mean square error (MSE) from estimating ACE with PSM and TMLE.


Table 9
Setting 2, linear outcome model, $n=500,1000$. The proportion (\%) of times the selected subset, $\widetilde{S}$, satisfies three conditions of unconfoundedness and the median cardinality of $\widetilde{S}$ (\#). Average bias (Bias), standard deviation (SD) and mean square error (MSE) from estimating ACE with PSM and TMLE.


Table 10
Setting 2, linear outcome model, $n=2000,10000$. The proportion (\%) of times the selected subset, $\widehat{S}$, satisfies three conditions of unconfoundedness and the median cardinality of $\widehat{S}$ (\#). Average bias (Bias), standard deviation (SD) and mean square error (MSE) from estimating ACE with PSM and TMLE.


Table 11
Setting 2, binary outcome model, $n=500,1000$. The proportion (\%) of times the selected subset, $\widehat{S}$, satisfies three conditions of unconfoundedness and the median cardinality of $\widehat{S}$ (\#). Average bias (Bias), standard deviation $(S D)$ and mean square error (MSE) from estimating ACE with PSM and TMLE.


Table 12
Setting 2, binary outcome model, $n=2000,10000$. The proportion (\%) of times the selected subset, $\widehat{S}$, satisfies three conditions of unconfoundedness and the median cardinality of $\widehat{S}$ (\#). Average bias (Bias), standard deviation (SD) and mean square error (MSE) from estimating ACE with PSM and TMLE.


Table 13
Setting 2, nonlinear outcome model, $n=500,1000$. The proportion (\%) of times the selected subset, $\widehat{S}$, satisfies three conditions of unconfoundedness and the median cardinality of $\widehat{S}$ (\#). Average bias (Bias), standard deviation (SD) and mean square error (MSE) from estimating ACE with PSM and TMLE.


Table 14
Setting 2, nonlinear outcome model, $n=2000,10000$. The proportion (\%) of times the selected subset, $\widehat{S}$, satisfies three conditions of unconfoundedness and the median cardinality of $\widehat{S}$ (\#). Average bias (Bias), standard deviation (SD) and mean square error (MSE) from estimating ACE with PSM and TMLE.


Table 15
Setting 1, linear outcome model, $n=500,1000$. The proportion (\%) of times the selected subset, $\widehat{S}$, upholds unconfoundedness and coverage probability ( $C P$ ), width of confidence interval (CIW) as well as average lower and upper limits (CIL, CIU) of confidence intervals when estimating ACE by PSM and TMLE.


Table 16
Setting 1, linear outcome model, $n=2000,10000$. The proportion (\%) of times the selected subset, $\widetilde{S}$, upholds unconfoundedness and coverage probability (CP), width of confidence interval (CIW) as well as average lower and upper limits (CIL, CIU) of confidence intervals when estimating ACE by PSM and TMLE.


Table 17
Setting 1, binary outcome model, $n=500,1000$. The proportion (\%) of times the selected subset, $\widehat{S}$, upholds unconfoundedness and coverage probability ( $C P$ ), width of confidence interval (CIW) as well as average lower and upper limits (CIL, CIU) of confidence intervals when estimating ACE by PSM and TMLE.


Table 18
Setting 1, binary outcome model, $n=2000,10000$. The proportion (\%) of times the selected subset, $\widehat{S}$, upholds unconfoundedness and coverage probability ( $C P$ ), width of confidence interval (CIW) as well as average lower and upper limits (CIL, CIU) of confidence intervals when estimating ACE by PSM and TMLE.


Table 19
Setting 1, nonlinear outcome model, $n=500,1000$. The proportion (\%) of times the selected subset, $\widetilde{S}$, upholds unconfoundedness and coverage probability (CP), width of confidence interval (CIW) as well as average lower and upper limits (CIL, CIU) of confidence intervals when estimating ACE by PSM and TMLE.


Table 20
Setting 1, nonlinear outcome model, $n=2000,10000$. The proportion (\%) of times the selected subset, $\widetilde{S}$, upholds unconfoundedness and coverage probability (CP), width of confidence interval (CIW) as well as average lower and upper limits (CIL, CIU) of confidence intervals when estimating ACE by PSM and TMLE.


Table 21
Setting 2, linear outcome model, $n=500,1000$. The proportion (\%) of times the selected subset, $\widehat{S}$, upholds unconfoundedness and coverage probability ( $C P$ ), width of confidence interval (CIW) as well as average lower and upper limits (CIL, CIU) of confidence intervals when estimating ACE by PSM and TMLE.


Table 22
Setting 2, linear outcome model, $n=2000,10000$. The proportion (\%) of times the selected subset, $\widetilde{S}$, upholds unconfoundedness and coverage probability ( $C P$ ), width of confidence interval (CIW) as well as average lower and upper limits (CIL, CIU) of confidence intervals when estimating ACE by PSM and TMLE.


Table 23
Setting 2, binary outcome model, $n=500,1000$. The proportion (\%) of times the selected subset, $\widehat{S}$, upholds unconfoundedness and coverage probability ( $C P$ ), width of confidence interval (CIW) as well as average lower and upper limits (CIL, CIU) of confidence intervals when estimating ACE by PSM and TMLE.


Table 24
Setting 2, binary outcome model, $n=2000,10000$. The proportion (\%) of times the selected subset, $\widehat{S}$, upholds unconfoundedness and coverage probability ( $C P$ ), width of confidence interval (CIW) as well as average lower and upper limits (CIL, CIU) of confidence intervals when estimating ACE by PSM and TMLE.


Table 25
Setting 2, nonlinear outcome model, $n=500,1000$. The proportion (\%) of times the selected subset, $\widetilde{S}$, upholds unconfoundedness and coverage probability ( $C P$ ), width of confidence interval (CIW) as well as average lower and upper limits (CIL, CIU) of confidence intervals when estimating ACE by PSM and TMLE.


Table 26
Setting 2, nonlinear outcome model, $n=2000,10000$. The proportion (\%) of times the selected subset, $\widetilde{S}$, upholds unconfoundedness and coverage probability ( $C P$ ), width of confidence interval (CIW) as well as average lower and upper limits (CIL, CIU) of confidence intervals when estimating ACE by PSM and TMLE.


Appendix C: Table and Figures from Section 6

# Table 27 

Distribution of demographic and perinatal factors by mode of delivery. The first antenatal visit takes place around pregnancy week 12. Median disposable income in the total Swedish population was 184700SEK in the year 2005.


Table 25
Continued.


![img-4.jpeg](img-4.jpeg)

Figure 5. DAG resulting from MMHC, $\tilde{X}_{\rightarrow T}$.

![img-5.jpeg](img-5.jpeg)

Figure 6. DAG resulting from MMHC, $\tilde{X}_{-s Y}^{1}$

![img-6.jpeg](img-6.jpeg)

Figure 7. DAG resulting from MMHC, $\tilde{X}_{-x y}^{0}$

![img-7.jpeg](img-7.jpeg)

Figure 8. DAG resulting from MMHC, $\widehat{Q}_{\rightarrow T}^{1}$
![img-8.jpeg](img-8.jpeg)

Figure 10. DAG resulting from MMHC, $\widehat{Z}_{\rightarrow Y}^{1}$
![img-9.jpeg](img-9.jpeg)

Figure 9. DAG resulting from MMHC, $\widehat{Q}_{\rightarrow T}^{0}$
![img-10.jpeg](img-10.jpeg)

Figure 11. DAG resulting from MMHC, $\widehat{Z}_{\rightarrow Y}^{0}$