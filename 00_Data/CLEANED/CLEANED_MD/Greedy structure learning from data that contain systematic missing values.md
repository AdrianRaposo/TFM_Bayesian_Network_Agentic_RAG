# Greedy structure learning from data that contain systematic missing values 

Yang Liu ${ }^{1}$ (D) $\cdot$ Anthony C. Constantinou ${ }^{1}$<br>Received: 15 July 2021 / Revised: 13 May 2022 / Accepted: 19 May 2022 /<br>Published online: 10 August 2022<br>© The Author(s), under exclusive licence to Springer Science+Business Media LLC, part of Springer Nature 2022


#### Abstract

Learning from data that contain missing values represents a common phenomenon in many domains. Relatively few Bayesian Network structure learning algorithms account for missing data, and those that do tend to rely on standard approaches that assume missing data are missing at random, such as the Expectation-Maximisation algorithm. Because missing data are often systematic, there is a need for more pragmatic methods that can effectively deal with data sets containing missing values not missing at random. The absence of approaches that deal with systematic missing data impedes the application of BN structure learning methods to real-world problems where missingness are not random. This paper describes three variants of greedy search structure learning that utilise pairwise deletion and inverse probability weighting to maximally leverage the observed data and to limit potential bias caused by missing values. The first two of the variants can be viewed as subversions of the third and best performing variant, but are important in their own in illustrating the successive improvements in learning accuracy. The empirical investigations show that the proposed approach outperforms the commonly used and state-of-the-art Structural EM algorithm, both in terms of learning accuracy and efficiency, as well as both when data are missing at random and not at random.


Keywords Expectation-maximisation $\cdot$ Inverse probability weighting $\cdot$ Missing data $\cdot$ Score-based learning $\cdot$ Structure learning

[^0]
[^0]:    Editor: Manfred Jaeger.
    $\boxtimes$ Yang Liu
    yangliu@qmul.ac.uk
    Anthony C. Constantinou
    a.constantinou@qmul.ac.uk
    1 Bayesian Artificial Intelligence Research Lab, School of Electronic Engineering and Computer Science, Queen Mary University of London, London, UK

# 1 Introduction 

The field of Bayesian Network (BN) structure learning represents a set of approaches that focus on recovering the conditional or causal relationships between variables from data. Structure learning can be divided into two main categories known as constraint-based and score-based methods. Constraint-based methods such as PC (Spirtes et al. 2000) and IAMB (Tsamardinos et al. 2003) recover a graph by ruling out the structures that violate the conditional independencies discovered from data, and orientating edges by determining colliders. Score-based algorithms such as GES (Chickering 2002) and GOBNILP (Cussens 2011) recover a graph by exploring the search space of possible graphs and returning the graph with the highest objective score. While numerous BN structure learning algorithms have been proposed in the literature over the past few decades, most of them do not efficiently learn from data that contain systematic missing values. This hinders the application of structure learning to real-world problems, since missing data represents a common issue in most applied areas including medicine and healthcare (Constantinou et al. 2016), clinical epidemiology (Pedersen et al. 2017), traffic flow prediction (Tian et al. 2018), anomaly detection (Zemicheal and Dietterich 2019), and financial analysis (John et al. 2019). Therefore, there is a greater need for structure learning algorithms that account for potential data bias due to systematic missing values, without having significant impact on the computational efficiency of structure learning.

According to Rubin (1976), missing data problems can be categorised into three classes. These are the Missing Completely At Random (MCAR), the Missing At Random (MAR) and the Missing Not At Random (MNAR). Specifically, MCAR denotes that the missing values are purely random and independent of other observed variables or parameters. This type of missingness is usually caused by technical error that would not bias the analysis. The definition of MAR, on the other hand, is somewhat counterintuitive in its name and assumes the missing values are dependent on observed data. For example, in an investigation between age and frequency of smoking, missing data are MAR if younger respondents are more likely to not disclose their smoking frequency. Lastly, data missingness are said to be MNAR if it is neither MCAR nor MAR. In the above example, the missingness are MNAR if data on respondent's age also contains missing values.

Methods that deal with missing data typically include naïve approaches such as the complete case analysis (a.k.a list-wise deletion) and multiple imputation (Rubin 2004). Complete case analysis involves removing the data cases that contain missing values and hence, restricting learning to complete data cases. Clearly, while this approach is easy to implement, it can be sample inefficient and may yield bias when missingness are not MCAR (Graham 2009). Multiple imputation, on the other hand, fills - rather than ignoring - the missing values and takes the uncertainty of imputation into consideration by repeating imputation over different possible values (Azur et al. 2011). However, multiple imputation is built under the assumption of MAR which means it may also produce biased outcomes when data are MNAR.

One of the earliest advanced approaches for dealing with missing data is the Expecta-tion-Maximisation (EM) algorithm, which was also later adopted by the structure learning community. The Structural EM algorithm (Friedman 1997) is an iterative process which consists of two steps: the Expectation (E) step and the Maximisation (M) step. In E step, Structural EM makes inferences on the missing values and computes the expected sufficient statistics based on the graph learned in previous iteration. The M step follows where the current state of the learned graph is revised based on the sufficient statistics obtained

at step E. An advantage of Structural EM is that it can be combined with different structure learning algorithms. A disadvantage, however, is that it is computationally inefficient due to the inference process that takes place at step E. Therefore, in practice, the E step of the Structural EM algorithm is usually implemented with single imputation, i.e., imputing the expectation of the missing values derived from the observed values. Ruggieri et al. (2020) compared the performance of the original Structural EM to that of the imputedbased Structural EM, and found that the latter achieves better performance in most of the simulation scenarios.

An increasing number of algorithms are recently proposed to improve structure learning from data containing missing values. In the case of score-based learning, two model selection methods have been proposed based on the likelihood function called Node-Average Likelihood (NAL) for discrete (Balov 2013) and conditional Gaussian BNs (Bodewes and Scutari 2021). While these methods are consistent with MCAR, they are not consistent with MAR or MNAR cases. In constraint-based learning, Strobl et al. (2018) treated missing values as a type of selection bias and showed that performing test-wise deletion during conditional independence (CI) tests represents a sound solution for the FCI algorithm (Spirtes et al. 2000). In the context of constraint-based learning, test-wise deletion is a process that deletes the data cases with missing values amongst the variables involved in a given CI test. Gain and Shpitser (2018) later show that replacing the standard CI test in PC with an Inverse Probability Weighting (IPW) (Horvitz and Thompson 1952) based CI test, enables PC to be applied to data sets which contain systematic missing values without loss of consistency. IPW is an approach to alleviate bias in data distributions by reweighting the data cases which we will describe in detail in Sect. 3. However, IPW CI testing assumes sufficient information of missingness, such as information about the parents of missingness and the total ordering of the missing indicators, which is unlikely to be known in practise. Tu et al. (2019) tried to address this issue by first predicting the parents of missingness using constraint-based learning, for every observed variable that contained missing values, and applying the IPW CI tests using the sufficient information obtained during the constraint-based learning phase.

In this paper, we propose three variants of the greedy search Hill-Climbing algorithm to investigate how they handle missing data values under different assumptions of missingness. These variants can be viewed as fusions between greedy search score-based learning, and the pairwise deletion and IPW methods discussed above that have been previously applied to constraint-based learning. The contribution of this paper is a novel structure learning algorithm suitable for structural learning from data that contain systematic missingness. The empirical results show that, under systematic missingness, the proposed algorithm outperforms the current state-of-the-art Structural EM algorithm, both in terms of learning accuracy and efficiency.

The paper is organised as follows: Sect. 2 provides necessary preliminary information that includes notation and background information, Sect. 3 describes the proposed algorithm, Sect. 4 presents the results, and we provide our concluding remarks in Sect. 5.

# 2 Preliminaries 

In this paper, we consider discrete variables which we denote with uppercase letters (e.g., $U, V$ ), and the assignment of variable states with lowercase letters (e.g., $u, v$ ). We denote a set of variables with bold uppercase letters (e.g., $\boldsymbol{U}, \boldsymbol{V}$ ), and the assignment of a set of variable states with bold lowercase letters (e.g., $\boldsymbol{u}, \boldsymbol{v}$ ).

### 2.1 Bayesian network

A BN $\langle\mathcal{G}, P\rangle$ is a probabilistic graphical model that can be represented by a Directed Acyclic Graph (DAG) $\mathcal{G}=(\boldsymbol{V}, \boldsymbol{E})$ and a joint distribution $P$ defined over $\boldsymbol{V}$, where $\boldsymbol{V}=\left\{V_{1}, \ldots, V_{n}\right\}$ represents a set of random variables and $\boldsymbol{E}$ represents a set of directed edges between pairs of variables. A BN entails the Markov Condition which states that for every variable $V_{i}$ in $\mathcal{G}, V_{i}$ is independent of all its non-descendants conditional on its parents. Given the Markov Condition, the joint distribution $P$ can be factorised as follows:

$$
P\left(V_{1}, \ldots, V_{n}\right)=\prod_{i=1}^{n} P\left(V_{i} \mid \boldsymbol{P a}_{i}\right)
$$

where $\boldsymbol{P a}_{i}$ represents the parent-set of $V_{i}$ in $\mathcal{G}$. Since this study focuses on discrete BNs, we assume that every variable follows an independent multinomial distribution given their parents. We also assume that the set of observed variables $\boldsymbol{V}$ is causally sufficient (Spirtes et al. 2000) and this means that we assume there are no unobserved common causes between any of the variables in $\boldsymbol{V}$. In practice, this means that even though measurement error can be viewed as a hidden variable problem where nodes that contain any form of error must have a hidden parent that causes that error, we assume causal sufficiency such that the graphs reconstructed by SEM are DAGs that contain the observed variables only.

Because an observed distribution can be represented by multiple different DAGs, we work under the assumption that multiple DAGs can be statistically indistinguishable. A collection of DAGs that are statistically indistinguishable, and express the same joint distribution, is also known as a set of Markov equivalent DAGs often referred to as a Completely Partial DAG (CPDAG) (Spirtes et al. 2000). A CPDAG can be obtained from a DAG by (a) preserving all its v-structures, (b) preserving all the directed edges that would create a cycle or a new v-structure if reversed, and (c) converting the residual directed edges to undirected edges.

### 2.2 Hill climbing algorithm

For simplicity, we focus on the Hill-Climbing (HC) structure learning algorithm (Heckerman et al. 1995) which is a classic score-based learning algorithm that greedily searches the space of neighbouring graphs. It typically starts from an empty graph and explores the search space of graphs via edge additions, deletions and reversals that maximally improve the objective score. HC terminates when no neighbouring graph increases the objective score. HC is an approximate learning algorithm that returns a local maximum solution. However, it is acknowledged to be a computationally efficient algorithm that often outperforms other more

complex algorithms (Gámez et al. 2011; Constantinou et al. 2021). The pseudo-code of the standard HC structure learning algorithm is provided in Algorithm 1.

```
Algorithm 1 The Hill-Climbing structure learning algorithm
    Input data set \(D\)
    Output learned DAG \(\mathcal{G}\)
    procedure Hill Climbing
        \(\mathcal{G} \leftarrow\) empty graph
        repeat
            \(\delta \leftarrow 0\)
            repeat
            construct a neighbouring DAG \(\mathcal{G}_{n e i}\) by adding, reversing or deleting an edge
                from \(\mathcal{G}\)
                if \(S\left(\mathcal{G}_{n e i} \mid D\right)-S(\mathcal{G} \mid D)>\delta\) then
                    \(\delta \leftarrow S\left(\mathcal{G}_{n e i} \mid D\right)-S(\mathcal{G} \mid D)\)
                    \(\mathcal{G}_{\text {update }} \leftarrow \mathcal{G}_{n e i}\)
                    end if
            until all possible edge operations have been attempted
            if \(\delta>0\) then
                \(\mathcal{G} \leftarrow \mathcal{G}_{\text {update }}\)
            end if
        until \(\delta=0\)
    end procedure
```

As with most other structure learning algorithms, HC is usually paired with a decomposable score function to evaluate each graph explored relative to the input data. A score function $S(\mathcal{G}, D)$ is decomposable if it can be written as the sum over a set of local scores, each of which corresponds to a variable and its parents in $\mathcal{G}$. While all score-based algorithms can use a decomposable score, this property is particular efficient in the case of HC search since it explores one or two graphical modifications at a time; i.e., one in case of edge addition or removal, and two in the case of edge reversal. Therefore, the objective score for each neighbouring graph $\mathcal{G}_{\text {nei }}$ can be obtained efficiently by only recomputing the local scores of up to two nodes whose parent-set has changed, and obtaining the local scores of the remaining nodes whose parent-set remains intact from the current best graph $\mathcal{G}$.

Many score functions offer the decomposable property, and most commonly include the Bayesian Information Criterion (BIC) (Schwarz 1978), the Bayesian Dirichlet equivalent (BDe) (Heckerman et al. 1995) and the quotient Normalized Maximum Likelihood (qNML) (Silander et al. 2018). In this paper, we employ BIC as the score function in all of our experiments. The formal definition of BIC is:

$$
\begin{aligned}
S_{B I C}(\mathcal{G} \mid D) & =\log L(\mathcal{G} \mid D)-\frac{\log (N)}{2} \cdot|\mathcal{G}| \\
& =\sum_{i=1}^{n}\left(\log P\left(V_{i} \mid \boldsymbol{P a}_{i}, \hat{\Theta}_{i}\right)-\frac{\log (N)}{2} \cdot\left|\hat{\Theta}_{i}\right|\right)
\end{aligned}
$$

where $N$ is the sample size, $\boldsymbol{P a}_{i}$ is the parent set of $V_{i}$ in $\mathcal{G}, \hat{\Theta}_{i}$ is the maximum likelihood estimates of the parameters over the local distribution of $V_{i}$, and $\left|\hat{\Theta}_{i}\right|$ is the number of free parameters in $\hat{\Theta}_{i}$. If $\mathcal{G}$ is defined over a set of discrete multinomial variables $\boldsymbol{V}=\left\{V_{1}, \ldots V_{n}\right\}$, then the BIC score has the following form:

$$
S_{B I C}(\mathcal{G} \mid D)=\sum_{i=1}^{n}\left(\sum_{j=1}^{q_{i}} \sum_{k=1}^{r_{i}} N_{i j k} \cdot \log \frac{N_{i j k}}{N_{i j}}-\frac{\log (N)}{2} \cdot\left(r_{i}-1\right) q_{i}\right)
$$

where $N_{i j k}$ is the number of cases in data set $D$ in which the variable $V_{i}$ takes its $k^{t h}$ value and the parents of $V_{i}$ take the $j^{t h}$ configuration. Similarly, $N_{i j}$ is the number of cases in data set $D$ where the parents of $V_{i}$ take their $j^{t h}$ configuration and, therefore, $N_{i j}=\sum_{k=1}^{r_{i}} N_{i j k}$. Lastly, $r_{i}$ represents the number of distinct values of $V_{i}$ and $q_{i}$ represents the number of configurations of the parents of $V_{i}$.

# 2.3 Missing data assumptions 

We adopt the graphical descriptions of missing data introduced by Mohan et al. (2013) and Mohan and Pearl (2021). In this paper, we denote the set of fully observed variables (i.e, variables without missing values) as $\boldsymbol{V}_{o}$ and the set of partially observed variables (i.e., variables with at least one missing values) as $\boldsymbol{V}_{m}$. For every partially observed variable $V_{i} \in \boldsymbol{V}_{m}$, we define an auxiliary variable $R_{i}$ called missing indicator to reflect the missingness in $V_{i}$, where $R_{i}$ takes the value of 0 when $V_{i}$ is recorded and the value of 1 when $V_{i}$ is missing.

Further, we define the missingness graph (m-graph (Mohan et al. 2013)) $\mathcal{G}(\mathbb{V}, \boldsymbol{E})$ that captures the relationships between observed variables $\boldsymbol{V}$ and missing indicators $\boldsymbol{R}$, where $\mathbb{V}=\boldsymbol{V}_{o} \cup \boldsymbol{V}_{m} \cup \boldsymbol{R}$. Based on m-graph, we define missing data as MCAR if $\boldsymbol{R} \Perp \boldsymbol{V}_{o} \cup \boldsymbol{V}_{m}$, MAR if $\boldsymbol{R} \Perp \boldsymbol{V}_{m} \mid \boldsymbol{V}_{o}$, otherwise MNAR. Figure 1 presents the three possible m-graphs assuming three observe variables with structure $V_{1} \rightarrow V_{2} \rightarrow V_{3}$, depicting the MCAR, MAR and MNAR assumptions respectively.

To ensure the population distributions are recoverable from the observed data, some assumptions need to be employed for the missing indicators. These are:

Assumption 1 Variables in $\boldsymbol{R}$ neither can be the parent of an observed variables in $\boldsymbol{V}$ nor other variables in $\boldsymbol{R}$.

Assumption 2 No partially observed variable can be the parent of its own missing indicator.

Assumption 1 states that a missing indicator in $\boldsymbol{R}$ can only be an effect (leaf) node in an m-graph, whereas Assumption 2 states that the missing value is independent of the variable
![img-0.jpeg](img-0.jpeg)

Fig. 1 The three possible m-graphs assuming three observed variables with structure $V_{1} \rightarrow V_{2} \rightarrow V_{3}$. Shaded nodes represent partially observed variables

value. When both Assumptions 1 and 2 hold, the joint distribution of the observed variables is recoverable from the observed data (Mohan et al. 2013, Theorem 2).

# 3 Handling systematic missing data with hill-climbing 

This section describes the three HC variants that we explore in extending the learning process towards dealing with systematic missing data. Specifically, Sect. 3.1 describes HC with pairwise deletion which we call HC-pairwise, Sect. 3.2 describes HC with both pairwise deletion and Inverse Probability Weighting which we call HC-IPW, and Sect. 3.3 describes an improved version of HC-IPW, the HC-aIPW, that prunes less data samples compared to HC-IPW. The first two HC-variants can be viewed as sub-versions of HCaIPW, but are important in their own in illustrating the successive improvements in learning accuracy.

### 3.1 Hill-climbing with pairwise deletion

Recall that, at each iteration, HC moves to the neighbouring graph that maximally improves the objective score, and that performing HC search with a decomposable scoring function means that there is no need to recompute the local score of variables whose parent-set remains unchanged across graphs. Therefore, an efficient (but not necessarily effective) way of applying HC to missing data is to ignore data cases that contain missing values in variables that form part of the set of variables considered when exploring local score changes to a DAG. We refer to this process as pairwise deletion, where "pair" refers to the current pair of candidate DAGs (the current best DAG and neighbouring DAG), and this deletion process may involve more than two variables. When comparing the current best DAG against a neighbouring DAG, the necessary variables would be the nodes with unequal parent-sets between the two graphs, plus the parents of those nodes in the two graphs. Formally, when exploring a neighbouring DAG $\mathcal{G}_{\text {nei }}$ from the current best DAG $\mathcal{G}$, the set of necessary variables $\boldsymbol{W}$ between $\mathcal{G}$ and $\mathcal{G}_{\text {nei }}$ can be described as:

$$
\boldsymbol{W}=\cup_{V_{i} \in \boldsymbol{V}_{d}}\left\{V_{i}, \boldsymbol{P a}_{i}, \boldsymbol{P a}_{i}^{n e i}\right\}
$$

where $\boldsymbol{V}_{d}$ is the set of variables that have different parent-sets between $\mathcal{G}$ and $\mathcal{G}_{\text {nei }}$, and $\boldsymbol{P a}_{i}$ and $\boldsymbol{P a}_{i}^{\text {nei }}$ are the parent-sets of $V_{i}$ in $\mathcal{G}$ and $\mathcal{G}_{\text {nei }}$ respectively. For simplicity, we refer to the data set obtained after applying pairwise deletion as the pairwise deleted data set.

Example 1 Assume that, during HC, the current state of DAG $\mathcal{G}$ is a graph containing three variables $\left\{V_{1}, V_{2}, V_{3}\right\}$ and the edge $V_{1} \rightarrow V_{2}$, as illustrated in Table 1. Given DAG $\mathcal{G}$, there are six possible edge operations each of which produces a neighbouring graph $\mathcal{G}_{\text {nei }}$. Operation add $V_{1} \rightarrow V_{3}$, for example, can be evaluated by assessing the change in the local score of $V_{3}$, i.e., $S\left(V_{3} \mid V_{1}\right)-S\left(V_{3}\right)$, since $V_{3}$ is the only variable with different parents between $\mathcal{G}$ and $\mathcal{G}_{\text {nei }}$. When the data set contains missing values, we can apply pairwise deletion to data given $\left\{V_{1}, V_{3}\right\}$ in order to obtain a complete data set that will enable us to assess the neighbouring graph resulting from this edge operation. However, there is a risk that this action may lead to biased estimates when missingness is not MCAR.

Table 1 Examples of necessary variables for each edge operation in HC, which we define as the variables with different parent-sets between the current best and neighbouring graphs, plus the parents that make up those parent-sets


Because pairwise deletion leads to edge operations that are assessed based on different subsets of the data, it is possible to get stuck in an infinite loop where previous neighbouring graphs are constantly revisited and re-selected as a higher scoring graph. This can happen when, for example, DAG $\mathcal{G}_{2}$ returns a higher score than $\mathcal{G}_{1}$ based on pairwise deleted data set $D_{1}, \mathcal{G}_{3}$ returns a higher score than $\mathcal{G}_{2}$ based on pairwise deleted data set $D_{2}$, and $\mathcal{G}_{1}$ returns a higher score than $\mathcal{G}_{3}$ based on pairwise deleted data set $D_{3}$. In this example, HC with pairwise deletion would identify the graphical scores as $\mathcal{G}_{1}<\mathcal{G}_{2}<\mathcal{G}_{3}<\mathcal{G}_{1}$ and never converge to a maximal solution. We address this issue by restricting HC search to neighbours not previously identified as the optimal graph. We call this variant of HC as HC-pairwise, and present its pseudo-code in Algorithm 2.

```
Algorithm 2 HC-pairwise algorithm
    Input data set \(D\)
    Output learned DAG \(\mathcal{G}\)
    procedure HC-pairwise
        \(\mathcal{G} \leftarrow\) empty graph
        \(\mathcal{G}_{\text {record }} \leftarrow\{\mathcal{G}\}\)
        repeat
            \(\delta \leftarrow 0\)
            repeat
                construct a neighbouring DAG \(\mathcal{G}_{n e i}\) by adding, reversing or deleting an edge
                    from \(\mathcal{G}\)
                    if \(\mathcal{G}_{n e i} \notin \mathcal{G}_{\text {record }}\) then
                    construct \(D_{p w}\) by pairwise deleting \(D\) given the necessary variables \(W\)
                    if \(S\left(\mathcal{G}_{n e i} \mid D_{p w}\right)-S\left(\mathcal{G} \mid D_{p w}\right)>\delta\) then
                        \(\delta \leftarrow S\left(\mathcal{G}_{n e i} \mid D_{p w}\right)-S\left(\mathcal{G} \mid D_{p w}\right)\)
                    \(\mathcal{G}_{\text {update }} \leftarrow \mathcal{G}_{n e i}\)
                    end if
                    end if
            until all possible edge operations have been attempted
            if \(\delta>0\) then
                \(\mathcal{G} \leftarrow \mathcal{G}_{\text {update }}\)
                \(\mathcal{G}_{\text {record }}=\mathcal{G}_{\text {record }} \cup\{\mathcal{G}\}\)
            end if
            until \(\delta=0\)
    end procedure
```

When data are MCAR, on the basis of $\boldsymbol{R} \Perp \boldsymbol{V}$ the distribution entailed by any pairwise deleted data set is an unbiased estimate of the underlying true distribution:

$$
P\left(V_{i} \mid \boldsymbol{P a}_{i}, \boldsymbol{R}_{s}=\mathbf{0}\right)=P\left(V_{i} \mid \boldsymbol{P a}_{i}\right)
$$

where $\boldsymbol{R}_{s}$ can be any subset of $\boldsymbol{R}$.
From this, we derive Proposition 1, which states that, when the missingness is MCAR, the DAG learned by HC-pairwise is a local maximum graph, at least when BIC is used as the objective function. We define the local maximum graph as the graph with an objective score not lower than the scores of all its valid neighbouring graphs, when these scores are derived from the fully observed data set; i.e., it is independent of missingness generated.

Proposition 1 Assume data $D$ is MCAR and sample size $N \rightarrow \infty$, for any $D A G \mathcal{G}$ and one of its neighbouring $D A G \mathcal{G}_{\text {nei }}$

$$
S_{B I C}\left(\mathcal{G}_{n e i} \mid D_{p w}\right)>S_{B I C}\left(\mathcal{G} \mid D_{p w}\right), \text { iff } S_{B I C}\left(\mathcal{G}_{n e i} \mid D_{f}\right)>S_{B I C}\left(\mathcal{G} \mid D_{f}\right)
$$

where $D_{p w}$ is the pairwise deleted data set which is derived from $D$ by removing the data cases with missing values amongst the necessary variables $\boldsymbol{W}$, and $D_{f}$ is the corresponding fully observed data set.

# 3.2 Hill-climbing with inverse probability weighting 

Although HC-pairwise will progressively learn a better DAG after each iteration when missingness is MCAR, this property does not necessarily hold when missingness is MAR or MNAR, since systematic bias in the data might produce

$$
P\left(V_{i} \mid \boldsymbol{P a}_{i}, \boldsymbol{R}=\mathbf{0}\right) \neq P\left(V_{i} \mid \boldsymbol{P a}_{i}\right)
$$

To diminish data biases caused by potential dependencies between missing and observed data, we further explore applying the IPW method on the pairwise deleted data set.

According to Mohan et al. (2013, Theorem 2) and Tu et al. (2019), when Assumptions 1 and 2 hold, the joint distribution of variables $\boldsymbol{V}$ can be fully recovered from the observed part of the data set (i,e., the data after applying pairwise deletion) by

$$
\begin{aligned}
P(\boldsymbol{V})= & P(\boldsymbol{V} \mid \boldsymbol{R}=\mathbf{0}) \\
& \underbrace{P(\boldsymbol{R}=\mathbf{0})}_{\prod_{R_{i} \in \boldsymbol{R}} P\left(R_{i}=0 \mid \boldsymbol{R}_{\boldsymbol{P a}_{R_{i}}}=\mathbf{0}\right)} \prod_{R_{i} \in \boldsymbol{R}} \underbrace{P\left(\boldsymbol{P a}_{R_{i}} \mid \boldsymbol{R}_{\boldsymbol{P a}_{R_{i}}}=\mathbf{0}\right)}_{P \underbrace{\left(\boldsymbol{P a}_{R_{i}} \mid R_{i}=0, \boldsymbol{R}_{\boldsymbol{P a}_{R_{i}}}=\mathbf{0}\right)}_{\beta_{R_{i}}}
\end{aligned}
$$

where $\boldsymbol{P a}_{R_{i}}$ is the set of parents of missing indicator $R_{i}$, and $\boldsymbol{R}_{\boldsymbol{P a}_{R_{i}}}$ is the set of missing indicator of the partially observed variables in $\boldsymbol{P a}_{R_{i}}$. We further discuss and provide the derivation of Eq. (7) in Appendix B.

Since the term $c$ in Eq. (7) represents a constant value, we can apply pairwise deletion to the missing data cases of variables $\boldsymbol{V}$ and weight the pairwise deleted data set by $\prod_{R i \in B} \beta_{R_{i}}$. This will produce a weighted data set that approximates the unbiased distribution $P(\boldsymbol{V})$. We call this HC variant HC-IPW, and can be viewed as an extension of HC-pairwise that incorporates both the pairwise deletion and IPW methods. Unlike HC-pairwise, the HC-IPW algorithm can be used under the assumption the input data are MAR or MNAR, in addition to MCAR, to diminish data bias caused by systematic missing values.

It should be noted that when $\boldsymbol{P a}_{R_{i}}$ contains partially observed variables, Eq. (7) implies that $\boldsymbol{P a}_{R_{i}} \subseteq \boldsymbol{V}$; otherwise, the columns of $\boldsymbol{P a}_{R_{i}}$ in the pairwise deleted data set may contain missing values that will render the calculation of $\beta_{R_{i}}$ invalid. The following example shows that it might be impossible to recover the underlying true distribution if any $\boldsymbol{P a}_{R_{i}} \nsubseteq \boldsymbol{V}$.

Example 2 Consider that Figure 1c is the true m-graph, the current best DAG $\mathcal{G}$ in HC search is the one shown in Fig. 2a, and b presents one of its neighbouring DAGs, $\mathcal{G}_{\text {nei }}$. Since the difference in score between $\mathcal{G}_{\text {nei }}$ and $\mathcal{G}$ is $S\left(V_{3} \mid V_{1}\right)-S\left(V_{3}\right)$, we need to ensure that missingness does not bias the estimate of distribution $P\left(V_{1}, V_{3}\right)$ when computing distributional score difference. If we apply pairwise deletion directly on the necessary variables $\left\{V_{1}, V_{3}\right\}$ and use Eq. (7) to recover $P\left(V_{1}, V_{3}\right)$. This will result in the following equation:

$$
P\left(V_{1}, V_{3}\right)=P\left(V_{1}, V_{3} \mid R_{1}=0\right) \frac{P\left(R_{1}=0\right)}{P\left(R_{1}=0\right)} \cdot \frac{P\left(V_{2} \mid R_{2}=0\right)}{P\left(V_{2} \mid R_{1}=0, R_{2}=0\right)}
$$

![img-1.jpeg](img-1.jpeg)

Fig. 2 A hill-climbing illustration of the DAG considered in Example 2, discussed in the main text. Shaded nodes represent partially observed variables

However, the problem in the above equation is that we cannot compute the weight term $\frac{P\left(V_{2} \mid R_{2}=0\right)}{P\left(V_{2} \mid R_{1}=0, R_{2}=0\right)}$ for data cases that contain missing values in $V_{2}$.

To avoid this, when assessing the edge operations from $\mathcal{G}$ to $\mathcal{G}_{\text {nei }}$ in HC-IPW, the pairwise deletion for Eq. (7) should be performed on sufficient variables $\boldsymbol{U}$, which is a variable set that contains the necessary variables $\boldsymbol{W}$ plus the parents of missing indicators of all variables in $\boldsymbol{U}$ :

$$
\boldsymbol{U}=\cup_{V_{i} \in V_{d}}\left\{V_{i}, \boldsymbol{P a}_{i}, \boldsymbol{P a}_{i}^{\text {nei }}\right\} \cup \boldsymbol{P a}_{\boldsymbol{R}_{U}}
$$

where $\boldsymbol{V}_{d}$ is the set of variables that have different parent-sets between $\mathcal{G}$ and $\mathcal{G}_{\text {nei }}$, and $\boldsymbol{P a}_{i}$ and $\boldsymbol{P a}_{i}^{\text {nei }}$ are the parent-sets of $V_{i}$ in $\mathcal{G}$ and $\mathcal{G}_{\text {nei }}$ respectively. It is worth noting that Eq. (8) represents a recursive process that iterates over the parents of missing indicators for all involved variables, i.e., not only $\boldsymbol{W}$ but also $\boldsymbol{U} \backslash \boldsymbol{W}$ should be included in $\boldsymbol{U}$ in order to resolve the issue illustrated in Example 2.

Another potential issue with Eq. (7) is that the parents $\boldsymbol{P a}_{R_{i}}$ of each missing indicator $R_{i}$ are generally unknown. Tu et al. (2019) used constraint-based learning to discover the parents of each missing indicator, and this approach has been proven to be sound when both Assumptions 1 and 2 hold. We have, therefore, adopted the constraint-based approach proposed by Tu et al. (2019) to discover the parents of the missing indicators in applying HC-IPW. The intention here is that this approach can be used to exclude variable $V_{j}$ as the parent of $R_{i}$, if $R_{i}$ is found to be independent of $V_{j}$ given any variable set $\boldsymbol{S}$, given the pairwise deleted data set for $\left\{V_{j}\right\} \cup \boldsymbol{S}$. Algorithm 3 provides the pseudo-code.

```
Algorithm 3 Discovering the parents of the missing indicators using constraint-
based learning
    Input data set \(D\)
    Output the parents of missing indicators \(\boldsymbol{P a}_{\boldsymbol{R}}\)
    procedure DETECTING PARENTS OF MISSING INDICATORS
        for each \(V_{i} \in V_{m}\) do
            \(\boldsymbol{P a}_{R_{i}} \leftarrow \boldsymbol{V} \backslash V_{i}\)
            for each \(V_{j} \in \boldsymbol{V} \backslash V_{i}\) do
                remove \(V_{j}\) from \(\boldsymbol{P a}_{R_{i}}\) if \(R_{i} \Perp V_{j} \mid \boldsymbol{S}, R_{j}=0, \boldsymbol{R}_{\boldsymbol{S}}=\mathbf{0}\), for any \(\boldsymbol{S} \subseteq \boldsymbol{P a}_{R_{i}}\)
            end for
        end for
        return \(\boldsymbol{P a}_{\boldsymbol{R}}\)
    end procedure
```

```
Algorithm 4 HC-IPW algorithm
    Input data set \(D\)
    Output learned DAG \(\mathcal{G}\)
    procedure HC-IPW
        \(\mathcal{G} \leftarrow\) empty graph
        \(\mathcal{G}_{\text {record }} \leftarrow\{\mathcal{G}\}\)
        retrieve the parents of missing indicators via Algorithm 3
        repeat
            \(\delta \leftarrow 0\)
            repeat
            construct a neighbouring DAG \(\mathcal{G}_{n e i}\) by adding, reversing or deleting an edge
            from \(\mathcal{G}\)
            if \(\mathcal{G}_{n e i} \notin \mathcal{G}_{\text {record }}\) then
                construct \(D_{p w}\) by pairwise deleting \(D\) given the sufficient variables \(U\)
                compute weight \(\beta\) by Equation 7 for \(D_{p w}\)
                if \(S\left(\mathcal{G}_{n e i} \mid D_{p w}, \beta\right)-S\left(\mathcal{G} \mid D_{p w}, \beta\right)>\delta\) then
                    \(\delta \leftarrow S\left(\mathcal{G}_{n e i} \mid D_{p w}, \beta\right)-S\left(\mathcal{G} \mid D_{p w}, \beta\right)\)
                    \(\mathcal{G}_{\text {update }} \leftarrow \mathcal{G}_{n e i}\)
                    end if
            end if
            until all possible edge operations have been attempted
            if \(\delta>0\) then
                \(\mathcal{G} \leftarrow \mathcal{G}_{\text {update }}\)
                \(\mathcal{G}_{\text {record }}=\mathcal{G}_{\text {record }} \cup\{\mathcal{G}\}\)
            end if
        until \(\delta=0\)
    end procedure
```

Algorithm 4 describes the HC-IPW algorithm, where lines coloured in blue represent the difference in pseudo-code between HC-IPW and HC-pairwise. Note that when computing the objective score for HC-IPW, the weighted statistics $\widetilde{N}_{i j k}, \widetilde{N}_{i j}$ are used instead of the standard $N_{i j k}, N_{i j}$ used in HC, and which are defined as follows:

$$
\begin{gathered}
\widetilde{N}_{i j k}=\sum_{s=1}^{\left|D_{p w}\right|} 1_{i j k}\left(d^{s}\right) \cdot \beta^{s} \\
\widetilde{N}_{i j}=\sum_{k=1}^{r_{i}} \widetilde{N}_{i j k}
\end{gathered}
$$

where $1_{i j k}$ is the indicator function of the event $\left(V_{i}=k, \boldsymbol{P a}_{i}=j\right)$ which returns 1 when the combination of $V_{i}=k, \boldsymbol{P a}_{i}=j$ appears in the input data case, and returns 0 otherwise, $d^{s}$ is the $s^{\text {th }}$ record in pairwise deleted data set $D_{p w}$, and $\beta^{s}$ is the weight corresponding to $d^{s}$. Therefore, we define the BIC score for pairwise deleted data set $D_{p w}$ given $\beta$ as follows:

$$
S_{B I C}\left(\mathcal{G} \mid D_{p w}, \beta\right)=\sum_{i=1}^{n}\left(\sum_{j=1}^{q_{i}} \sum_{k=1}^{r_{i}} \widetilde{N}_{i j k} \cdot \log \frac{\widetilde{N}_{i j k}}{\widetilde{N}_{i j}}-\frac{\log \left(N_{p w}\right)}{2} \cdot\left(r_{i}-1\right) q_{i}\right)
$$

where $N_{p w}$ represents the sample size of $D_{p w}, \widetilde{N}_{i j k}$ and $\widetilde{N}_{i j}$ represent the weighted statistics as defined in Eqs. (9) and (10), and $\beta$ is used for computing the weighted $\widetilde{N}_{i j k}$ and $\widetilde{N}_{i j}$.

The following proposition shows that HC-IPW converges to a local optima when BIC is used as the score function, when both Assumptions 1 and 2 hold, and when sample size $N \rightarrow \infty$.

Proposition 2 Given Assumptions 1 and 2, assume data D is partially observed and sample size $N \rightarrow \infty$, for any $D A G \mathcal{G}$ and one of its neighbouring $D A G \mathcal{G}_{\text {nei }}$

$$
S_{B I C}\left(\mathcal{G}_{n e i} \mid D_{p w}, \beta\right)>S_{B I C}\left(\mathcal{G} \mid D_{p w}, \beta\right), \text { iff } S_{B I C}\left(\mathcal{G}_{n e i} \mid D_{f}\right)>S_{B I C}\left(\mathcal{G} \mid D_{f}\right)
$$

where $D_{p w}$ is the pairwise deleted data set which is derived from $D$ by removing data cases with missing values among sufficient variables $\boldsymbol{U}, \beta=\prod_{R_{i} \in \boldsymbol{R}_{U}} \beta_{R_{i}}$, and $D_{f}$ is the corresponding fully observed data set.

# 3.3 Hill-climbing with adaptive inverse probability weighting 

Although HC-IPW diminishes potential data bias caused by systematic missing values, the learning approach achieves this by removing a greater number of data cases compared to those removed by HC-pairwise when $\boldsymbol{P a}_{\boldsymbol{R}_{\boldsymbol{w}}}$ contains partially observed variables, which is likely to happen when the missingness are MNAR. This can be a problem when data cases are limited. We illustrate this phenomenon with an example.

Example 3 Suppose graph (a) in Fig. 3 represents the ground truth m-graph in which the variables in shaded backcolour $V_{1}, V_{4}$ and $V_{6}$ are partially observed whose missingness are caused by $V_{4}, V_{5}$ and $V_{1}$ respectively, as illustrated with the missing indicators $R_{1}, R_{4}$ and $R_{6}$ corresponding to the missingness of $V_{1}, V_{4}$ and $V_{6}$. Let us assume graph (b) represents the current state of the optimal DAG in the HC-pairwise/HC-IPW search process, and that graphs (c) and (d) represent two of the possible neighbouring graphs. When HC-pairwise compares $\mathcal{G}$ with $\mathcal{G}_{\mathrm{n} 1}$, it applies pairwise deletion on cases in which the necessary variables $\boldsymbol{W}=\left\{V_{5}, V_{2}, V_{6}\right\}$ contain missing values. Since only $V_{6}$ is partially observed out of the three necessary variables, HC-pairwise removes data cases when the value of $V_{6}$ is missing. In contrast, when HC-IPW is applied to this case, and assuming it correctly learns the parents of missingness via Algorithm 3, it computes the weights of the pairwise deleted data set through pairwise deletion based on the sufficient variables $\boldsymbol{U}=\left\{V_{5}, V_{2}, V_{6}\right\} \cup\left\{V_{1}, V_{4}, V_{5}\right\}$. Thus, HC-IPW removes data cases whenever any of the variables in $U$ contain a missing value (in this example, $V_{1}, V_{4}$ and $V_{6}$ do). Therefore, HCIPW performs learning on a smaller set of data cases compared to those in the case of HC-pairwise.

When $\boldsymbol{P a}_{\boldsymbol{R}_{\boldsymbol{w}}}$ (refer to Eq. 4 and Algorithm 4) does not contain any partially observed variables, the HC-IPW algorithm will perform learning on the same number of data cases as in HC-pairwise. This can happen in cases such as when comparing neighbouring DAG $\mathcal{G}_{\mathrm{n} 2}$ against $\mathcal{G}$ in Fig. 3, where the set of necessary variables $\boldsymbol{W}$ in HC-pairwise contains $\left\{V_{4}, V_{2}, V_{5}\right\}$ and the set of sufficient variables $\boldsymbol{U}$ in HC-IPW is $\left\{V_{4}, V_{2}, V_{5}\right\} \cup\left\{V_{5}\right\}$. In this case, because $V_{5}$ is fully observed, applying pairwise deletion given $\boldsymbol{W}$ and $\boldsymbol{U}$ would result in the same pairwise deleted data set.

Because the effectiveness of a scoring function increases with sample size, the scoring efficiency of HC-IPW can decrease considerably when missingness are MNAR for

![img-2.jpeg](img-2.jpeg)

Fig. 3 Example of a searching step in HC-pairwise/HC-IPW
multiple variables. This is because both the number of partially observed variables and MNAR missingness increase the number of data cases removed during the learning process. It is on this basis we investigated a third variant, called the adaptive IPW-based HC (HC-aIPW), and which can be viewed as an extension of HC-IPW. The pseudo-code of HC-aIPW is shown in Algorithm 5. The highlighted section represents the part of the code that differs from HC-IPW.

In essence, HC-aIPW aims to maximise the samples taken into consideration during the learning process. When there are partially observed variables in $\boldsymbol{P a}_{\boldsymbol{R}_{\mathbf{0}}}$, HC-aIPW applies pairwise deletion given $\boldsymbol{W}$ and computes the difference in score between the current optimal DAG and the neighbouring DAG using the original pairwise deleted data set and standard scoring function. This is the only difference between HC-aIPW and HC-IPW. When there are no partially observed variables in $\boldsymbol{P a}_{\boldsymbol{R}_{\mathbf{0}}}$, HC-aIPW uses the same IPW procedure as in HC-IPW to compute the difference in score between the current optimal DAG and the neighbouring DAG given the weighted pairwise deleted data set.

```
Algorithm 5 HC-aIPW algorithm
    Input data set \(D\)
    Output learned DAG \(\mathcal{G}\)
    procedure HC-aIPW
        \(\mathcal{G} \leftarrow\) empty graph
        \(\mathcal{G}_{\text {record }} \leftarrow\{\mathcal{G}\}\)
        retrieve the parents of missing indicators via Algorithm 3
        repeat
            \(\delta \leftarrow 0\)
            repeat
            construct a neighbouring DAG \(\mathcal{G}_{n e i}\) by adding, reversing or deleting an edge
            from \(\mathcal{G}\)
            if \(\mathcal{G}_{n e i} \notin \mathcal{G}_{\text {record }}\) then
                if \(\boldsymbol{P a}_{\boldsymbol{R}_{\boldsymbol{W}}} \cap \boldsymbol{V}_{m} \neq \varnothing\) then
                    construct \(D_{p w}\) by pairwise deleting \(D\) given the necessary variables \(\boldsymbol{W}\)
                    if \(S\left(\mathcal{G}_{n e i} \mid D_{p w}\right)-S\left(\mathcal{G} \mid D_{p w}\right)>\delta\) then
                    \(\delta \leftarrow S\left(\mathcal{G}_{n e i} \mid D_{p w}\right)-S\left(\mathcal{G} \mid D_{p w}\right)\)
                    \(\mathcal{G}_{\text {update }} \leftarrow \mathcal{G}_{n e i}\)
                    end if
                    else
                    construct \(D_{p w}\) by pairwise deleting \(D\) given the sufficient variables \(\boldsymbol{U}\)
                    compute weight \(\beta\) by Equation 7 for \(D_{p w}\)
                    if \(S\left(\mathcal{G}_{n e i} \mid D_{p w}, \beta\right)-S\left(\mathcal{G} \mid D_{p w}, \beta\right)>\delta\) then
                    \(\delta \leftarrow S\left(\mathcal{G}_{n e i} \mid D_{p w}, \beta\right)-S\left(\mathcal{G} \mid D_{p w}, \beta\right)\)
                    \(\mathcal{G}_{\text {update }} \leftarrow \mathcal{G}_{n e i}\)
                    end if
                    end if
                    end if
            until all possible edge operations have been attempted
            if \(\delta>0\) then
                \(\mathcal{G} \leftarrow \mathcal{G}_{\text {update }}\)
                \(\mathcal{G}_{\text {record }}=\mathcal{G}_{\text {record }} \cup\{\mathcal{G}\}\)
            end if
        until \(\delta=0\)
    end procedure
```


# 4 Experiments 

The learning accuracy of each of the three algorithms described in Sect. 3 is investigated and evaluated with reference to the Structural EM algorithm when applied to the same data. The Structural EM algorithm represents a state-of-the-art score-based approach for structure learning from missing data, and also explores the search space of graphs using HC. Since all the involved algorithms are based on HC, we measure their learning accuracy with reference to the results obtained when applying standard HC on complete, rather than incomplete, data. Results from complete data give us the empirical maximum performance we can achieve on these data sets using HC, before making part of the data missing. The HC and Structural EM algorithms used in this paper are those available in the bnlearn R package (Scutari 2010). It is worth noting that the Structural EM algorithm implemented in bnlearn R package is based on single imputation rather than belief propagation.

Therefore, the results presented in this paper approximate the difference between the proposed methods and Friedman's Structural EM. The implementations of the three HC variants described in Sect. 3 are available online at https://github.com/Enderlogic/HC-missi ng-data.

# 4.1 Generating synthetic data and missingness 

To illustrate the performance of the algorithms under different settings, we consider three types of ground truth DAGs: sparse networks, dense networks and real-world networks. We have constructed 50 random sparse and 50 random dense DAGs. Each network contains 20 to 50 nodes with two to six states per node. A sparse DAG $\mathcal{G}$ with $n$ variables is generated from a randomly ordered variable set $V_{1}<V_{2}<\ldots<V_{n}$, where directed edges are sampled from lower ordered variables to higher ordered variables with probability $2 /(n-1)$. Dense DAGs are generated with the same procedure, but the probability of drawing an edge between variables increases to $4 /(n-1)$. The conditional probability distribution of variable $V_{i}$ in sparse and dense DAGs is parameterised, given any configuration of its parents, by drawing a random number from the Dirichlet distribution $\operatorname{Dir}(\boldsymbol{\alpha})$, where $\boldsymbol{\alpha}=\underbrace{\{1, \ldots, 1\}}_{r_{i}}$, and $r_{i}$ is the number of states in $V_{i}$. For real-world DAGs, we use the six real-world BNs investigated in (Constantinou et al. 2021). The structure and parameters of these BNs are set by either real data observations or prior knowledge as defined in the original studies. The properties of these BNs are provided in Table 2.

We generate complete and incomplete synthetic data using the DAGs introduced above. The complete data sets are provided as input to the standard HC algorithm, whereas the corresponding incomplete data sets are provided as input to the Structural EM and the three HC variants described in Sect. 3. We generate five complete data sets per DAG with sample sizes $N \in\{100,500,1000,5000,10000\}$. Each complete data set is then used to construct further three data sets with missing values; one per missingness assumption, MCAR, MAR or MNAR. For the MCAR case, we randomly select $50 \%$ of the variables to represent the partially observed variables, and we then remove observed data of these variables with probability p , where p represents a random value between 0.1 and 0.6 . For case MAR, we had to ensure missingness are dependent on a subset of the fully observed variables, and this is done as follows:

1. Randomly select $50 \%$ of the variables as partially observed variables (same process as in MCAR);

Table 2 The properties of the six real-world BNs


2. Randomly assign a fully observed variable as the parent of missingness of a partially observed variable (repeat for all partially observed variables);
3. Remove observations in partially observed variables with probability $p=0.6$ when the parent of their missingness is at its highest occurring state; otherwise, remove the observation with probability $p=0.1$.

Generating MNAR data also involves the above 3-step procedure, but step 2 is modified as follows:
2. Randomly select $50 \%$ of the partially observed variables and randomly assign a fully observed variable as the parent of their missingness. For the remaining $50 \%$ partially observed variables, randomly assign another partially observed variable as the parent of their missingness.

# 4.2 Evaluation metrics 

The structure learning performance is assessed using two metrics that are fully oriented towards graphical discovery. The first metric is the classic $F_{1}$ score, composed of Precision and Recall. The formal definition of the $F_{1}$ score is:

$$
F_{1}=2 \frac{\text { precision } * \text { recall }}{\text { precision }+ \text { recall }}=\frac{2 T P}{2 T P+F P+F N}
$$

where $T P$ is the number of edges that exist in both the learned graph and true graph, $F P$ is the number of edges that exist in the learned graph but not in true graph, and $F N$ is the number of edges that exist in the true graph but not in the learned graph.

The second metric considered is the Structural Hamming Distance (SHD) which measures graphical differences between the learned graph and the true graph (Tsamardinos et al. 2006). Specifically, the SHD score represents the number of edge operations needed to convert the learned graph to the true graph, where the edge operations involve arc addition, deletion and removal. Therefore, in contrast to the $F_{1}$ score, a lower SHD score indicates a better performance. Because the SHD score is sensitive to the number of edges and variables present in the true graph, we divide the SHD score by the number of edges in the true DAG to reduce bias.

Because the experiments are based on observational data, multiple DAGs can be statistically indistinguishable due to being part of the same Markov Equivalence class. On this basis, we compare the CPDAGs between the learned and true graphs to measure both the $F_{1}$ and SHD graphical scores.

### 4.3 Results when the true DAG is sparse

Figure 4 presents the average accuracy of the algorithms when the true DAGs are sparse. Each averaged score is derived from 50 CPDAGs, corresponding to each of the 50 randomly generated sparse DAGs. Appendix C provides the mean and standard deviation of the scores. The results suggest that the two evaluation metrics are generally consistent in ranking the algorithms from best to worst performance. Both metrics suggest that all of the three proposed HC variants outperform the Structural EM algorithm when the sample size is greater than 1,000, under all three missingness scenarios MCAR, MAR and MNAR.

![img-3.jpeg](img-3.jpeg)

Fig. 4 Average $F_{1}$ and normalised SHD scores learned by HC-pairwise, HC-IPW, HC-aIPW and Structural EM for sparse networks, under different assumptions of missingness and sample sizes. Each score represents the average score over 50 CPDAGs. Note the scores of HC-complete are based on complete data for benchmarking purposes; i.e., the same scores are superimposed in all three missingness cases as a dashed line

Interestingly, the HC-aIPW algorithm almost matches the performance of HC which is applied to complete data (denoted as HC-complete in Fig. 4), particularly for experiments with 10,000 sample size, and this observation is consistent across all three missingness assumptions.

The three variants, HC-pairwise, HC-IPW and HC-aIPW, produce very similar results under MCAR, and this is because missingness under MCAR has no pattern that could be identified by the HC-IPW and HC-aIPW variants. That is, when HC-IPW and HC-aIPW do not discover any parent of missingness, they follow the search process of HC-pairwise. Under MAR, however, both HC-IPW and HC-aIPW outperform HC-pairwise as well as Structural EM when the sample size is larger than 100 and the improvement in performance increases with sample size. From this observation, we can conclude that the IPW method successfully eliminate most of the distributional bias. Interestingly, although the construction of the Structural EM algorithm is based on the MAR assumption, its performance under MAR is considerably lower than its performance under MCAR. A possible explanation is that the single imputation process the bnlearn R package employs during the E step of Structural EM, instead of belief propagation, is unable to capture the uncertainty of the missing values.

Lastly, the results under MNAR suggest that HC-IPW generally performs worse than HC-pairwise across most sample sizes. This observation can be explained by the reduced sample size on which HC-IPW operates, relative to HC-pairwise, as discussed in Sect. 3.3. Specifically, when the parents of missingness of necessary variables $W$ contain partially observed variables (i.e., MNAR case), HC-IPW applies pairwise deletion by taking into consideration a higher number of variables compared to those considered by HC-pairwise. This means that, compared to HC-pairwise, the HC-IPW algorithm typically evaluates

edge operations based on smaller samples when missingness are MNAR, which tends to yield less accurate results. From this, we can also conclude that the negative effect resulting from HC-IPW further pruning samples has not been offset by the data bias adjustments applied by the IPW method. On the other hand, the HC-aIPW algorithm which is designed to apply the IPW method only when no additional samples would be deleted compared to HC-pairwise, generally outperforms all other algorithms under MNAR, particularly under higher sample sizes.

Figure 5 presents the relative execution time between (a) the four algorithms applied to data with missing values, and (b) the HC algorithm applied to the complete data. Because the three HC variants are implemented in Python, we measure their execution time relative to our Python version of HC. On the other hand, Structural EM is implemented in bnlearn R package and makes use of the HC implementation of that package. Therefore, the execution time of Structural EM is measured relative to the HC implementation in bnlearn R package. The mean and standard deviation of the results can be found in Appendix D.

Overall, the results show that HC-pairwise is the most efficient algorithm for missingness. Specifically, HC-pairwise increases execution time relative to HC by approximately $50 \%$, while HC-IPW and HC-aIPW are anywhere between 8 and 15 times slower than HC dependent on sample size, and the relative difference in execution time tends to increase with sample size. This is because a higher number of parents of missingness are likely to be detected in larger sample sizes, and these discoveries increase execution time for IPW-based variants. Still, both the HC-IPW and HC-aIPW variants are more efficient than Structural EM which increases execution time relative to HC by 100 to 700 times.

# 4.4 Results when the true DAG is dense 

In this subsection we investigate the performance of the algorithms when applied to data sets sampled from dense networks. The performance of each algorithm is depicted in Fig. 6, and detailed results are provided in Appendix C. An important distinction between sparse and dense networks is that learning from data sampled from dense networks makes it more likely that local parts of the graph will involve learning from partially observed variables. In other words, the effect of missing values is more severe on dense, compared to sparse, networks as shown in Sect. 4.3.
![img-4.jpeg](img-4.jpeg)

Fig. 5 Average ratio of the execution time between the algorithms running on missing data sets and HC running on complete data sets

![img-5.jpeg](img-5.jpeg)

Fig. 6 Average $F_{1}$ and normalised SHD scores learned by HC-pairwise, HC-IPW, HC-aIPW and Structural EM for dense networks, under different assumptions of missingness and sample sizes. Each score represents the average score over 50 CPDAGs. Note the scores of HC-complete are based on complete data for benchmarking purposes; i.e., the same scores are superimposed in all three missingness cases as a dashed line

The results show that the HC-aIPW algorithm continues to perform best in the case of denser graphs, in terms of overall performance and over the different missingness and sample size assumptions. Specifically, HC-aIPW achieves the highest accuracy in 11 and 8 cases in terms of $F_{1}$ and SHD measures respectively, out of the 15 experiments conducted in this subsection. In contrast, the Structural EM algorithm performs best only in two experiments and only in SHD score. However, compared with the results in Sect. 4.3, the divergence in score between Structural EM and HC-based variants is much smaller.

The performance across the three HC-based variants appears to be similar to that obtained under sparse graphs. When data are MCAR, HC-IPW and HC-aIPW produce scores that are similar to those produced by HC-pairwise, and this is expected since no observed variables should be detected as the parents of missing indicators when missingness is MCAR. When data are MAR, both HC-IPW and HC-aIPW outperform HC-pairwise since, unlike HC-pairwise, they can detect and reduce bias caused by missing values. Lastly, when data are MNAR, HC-IPW performs worst amongst all algorithms, particularly when the sample size is lowest, and this is because it tends to remove a large number of data cases when computing the local scores. On the other hand, HC-aIPW (which aims to resolve this specific drawback of HC-IPW) performs best in almost all MNAR experiments. The consistency of the results across sparse and dense networks suggests that the performance of HC-aIPW, relative to the other algorithms considered in this study, is not sensitive to the sparsity of the network that generates the input data.

# 4.5 Results when the true DAG is a real-world network 

Lastly, we apply the algorithms to data sets sampled from the six real-world networks. Figure 7 shows the average performance of the algorithms across all the six real-world networks and over all the five sample sizes. When the missingness is MCAR, the three HC-based variants achieve similar accuracy, as expected, and generally outperform the Structural EM algorithm when the sample size is larger than 500. When the missingness is MAR or MNAR, the performance of HC-aIPW improves over the other algorithms, especially when the sample size is larger than 500. These results are consistent with those obtained from the randomised sparse and dense networks presented in Sects. 4.3 and 4.4 respectively.

## 5 Conclusion

Learning accurate BN structure from incomplete data remains a challenging task. Most BN structure learning algorithms do not support learning from incomplete data, and this is partly explained by the considerable increase in computational complexity when dealing with incomplete data. The increased computational complexity caused by missing data adds to a problem that is NP-hard even when data are complete. This challenge is even greater when missing values are systematic rather than random.

In this paper, we have investigated three novel HC-based variants that employ pairwise deletion and IPW strategies to deal with random and systematic missing data. The
![img-6.jpeg](img-6.jpeg)

Fig. 7 Average $F_{1}$ and normalised SHD scores learned by HC-pairwise, HC-IPW, HC-aIPW and Structural EM for real-world networks, under different assumptions of missingness and sample sizes. Each score represents the average score over 50 CPDAGs. Note the scores of HC-complete are based on complete data for benchmarking purposes; i.e., the same scores are superimposed in all three missingness cases as a dashed line

HC-pairwise and HC-IPW variants can be viewed as subversions of HC-aIPW, which is the most complete and best performing variant described in this paper. All of the three variants have been applied to different cases of data missingness, and their performance was compared to the state-of-the-art Structural EM algorithm that is available in the bnlearn R package. Moreover, all performances under missingness have been compared to HC when applied to the corresponding complete data sets. The empirical results show:

1. Pairing HC with pairwise deletion (i.e., the HC-pairwise variant) is enough to learn graphs that are more accurate, as well as less computationally expensive, compared to the graphs produced by the Structural EM algorithm.
2. Combining HC with both pairwise deletion and IPW techniques (i.e., the HC-IPW variant) further improves learning accuracy under MCAR and MAR, in general, but decreases accuracy under MNAR due to aggressive pruning employed by HC-IPW on the data cases (refer to Sect. 3.3). Moreover, HC-IPW becomes considerably slower than HC-pairwise, although it remains an order of magnitude faster than Structural EM.
3. The HC-aIPW takes advantage of both strategies, as in HC-IPW, but relaxes the pruning strategy on the data cases and returns the overall best performance, especially under MNAR which represents the most difficult case of missingness.
4. All three HC variants described in this paper outperform Structural EM in most cases. Importantly, the performance of HC-aIPW on missing data approaches the performance of HC on complete data when sample size is 10,000 and the ground truth graph is sparse, and this observation is consistent under all three cases of missingness.

Future research will investigate the application of these learning strategies to search algorithms that are more complex than HC , such as Tabu, or other variants of HC such as the GES algorithm (Chickering 2002) which explores the CPDAG, rather than DAG space. Another possible research direction would be to combine the IPW method with the NAL score (Balov 2013), which is a scoring function intended for missingness under MCAR, and further investigate the possibility of a new decomposable scoring function under systematic missingness cases of MAR and MNAR.

# Appendix A Proofs of propositions 

In this section, we provide proofs of the propositions discussed in Sect. 3. We define the variables used in proofs as follows: $\boldsymbol{V}_{d}$ is the set of variables with different parent-sets between a given DAG $\mathcal{G}$ and its neighbouring DAG $\mathcal{G}_{\text {nei }}, \boldsymbol{W}$ is a set of the necessary variables as defined in Eq. (4), $\boldsymbol{U}$ is a set of the sufficient variables defined in Eq. (8), and $N$ and $N_{p w}$ are the sample sizes of the partially observed data set $D$ and pairwise deleted data set $D_{p w}$ respectively.

Proposition 1 Assume data $D$ is MCAR and sample size $N \rightarrow \infty$, for any $D A G \mathcal{G}$ and one of its neighbouring $D A G \mathcal{G}_{\text {nei }}$

$$
S_{B I C}\left(\mathcal{G}_{n e i} \mid D_{p w}\right)>S_{B I C}\left(\mathcal{G} \mid D_{p w}\right), \text { iff } S_{B I C}\left(\mathcal{G}_{n e i} \mid D_{f}\right)>S_{B I C}\left(\mathcal{G} \mid D_{f}\right)
$$

where $D_{p w}$ is the pairwise deleted data set which is derived from $D$ by removing the data cases with missing values amongst the necessary variables $\boldsymbol{W}$, and $D_{f}$ is the corresponding fully observed data set.

$$
\begin{aligned}
& S_{B I C}\left(\mathcal{G}_{n e i} \mid D_{f}\right)-S_{B I C}\left(\mathcal{G} \mid D_{f}\right) \\
& =\sum_{i=1}^{n}\left(S_{B I C}\left(V_{i} \mid \boldsymbol{P a}_{i}^{n e i}\right)-S_{B I C}\left(V_{i} \mid \boldsymbol{P a}_{i}\right)\right) \\
& =\sum_{i: V_{i} \in \boldsymbol{V}_{d}}\left(S_{B I C}\left(V_{i} \mid \boldsymbol{P a}_{i}^{n e i}\right)-S_{B I C}\left(V_{i} \mid \boldsymbol{P a}_{i}\right)\right) \\
& =\sum_{i: V_{i} \in \boldsymbol{V}_{d}}\left(\sum_{D_{f}}\left(\log P\left(V_{i} \mid \boldsymbol{P a}_{i}^{n e i}\right)-\log P\left(V_{i} \mid \boldsymbol{P a}_{i}\right)\right)\right. \\
& +\frac{\log (N)}{2}\left(\left|\hat{\Theta}_{i}^{n e i}\right|-\left|\hat{\Theta}_{i}\right|\right)\right) \\
& =\frac{N}{N_{p w}} \sum_{i: V_{i} \in \boldsymbol{V}_{d}}\left(\sum_{D_{p w}}\left(\log P\left(V_{i} \mid \boldsymbol{P a}_{i}^{n e i}, \boldsymbol{R}_{\boldsymbol{W}}=\mathbf{0}\right)-\log P\left(V_{i} \mid \boldsymbol{P a}_{i}, \boldsymbol{R}_{\boldsymbol{W}}=\mathbf{0}\right)\right)\right. \\
& +\frac{\log \left(N_{p w}\right)}{2}\left(\left|\hat{\Theta}_{i}^{n e i}\right|-\left|\hat{\Theta}_{i}\right|\right)+\frac{\log \left(N / N_{p w}\right)}{2}\left(\left|\hat{\Theta}_{i}^{n e i}\right|-\left|\hat{\Theta}_{i}\right|\right)\right)
\end{aligned}
$$

Proof

$$
\begin{aligned}
= & \frac{N}{N_{p w}}\left(S_{B I C}\left(\mathcal{G}_{n e i} \mid D_{p w}\right)-S_{B I C}\left(\mathcal{G} \mid D_{p w}\right)\right. \\
& \left.+\frac{\log \left(N / N_{p w}\right)}{2} \sum_{i: V_{i} \in \boldsymbol{V}_{d}}\left(\left|\hat{\Theta}_{i}^{n e i}\right|-\left|\hat{\Theta}_{i}\right|\right)\right) \\
\propto & S_{B I C}\left(\mathcal{G}_{n e i} \mid D_{p w}\right)-S_{B I C}\left(\mathcal{G} \mid D_{p w}\right)+O(1)
\end{aligned}
$$

Equation (12) follows from Eq. (5) given the MCAR assumption and large sample limit. Equation (13) is due to the missing rate of data $D$, i.e., $N_{p w} / N$, does not relate to the sample size $N$ and remains constant with the increase of $N$.

Proposition 2 Given Assumptions 1 and 2, assume data $D$ is partially observed and sample size $N \rightarrow \infty$, for any $D A G \mathcal{G}$ and one of its neighbouring $D A G \mathcal{G}_{\text {nei }}$

$$
S_{B I C}\left(\mathcal{G}_{n e i} \mid D_{p w}, \beta\right)>S_{B I C}\left(\mathcal{G} \mid D_{p w}, \beta\right), \text { iff } S_{B I C}\left(\mathcal{G}_{n e i} \mid D_{f}\right)>S_{B I C}\left(\mathcal{G} \mid D_{f}\right)
$$

where $D_{p w}$ is the pairwise deleted data set which is derived from $D$ by removing data cases with missing values among sufficient variables $\boldsymbol{U}, \beta=\prod_{R_{i} \in \boldsymbol{R}_{U}} \beta_{R_{i}}$, and $D_{f}$ is the corresponding fully observed data set.

$$
\begin{aligned}
& S_{B I C}\left(\mathcal{G}_{n e i} \mid D_{f}\right)-S_{B I C}\left(\mathcal{G} \mid D_{f}\right) \\
& =\sum_{i: V_{i} \in \boldsymbol{V}_{d}}\left(\sum_{D_{f}}\left(\log P\left(V_{i} \mid \boldsymbol{P a}_{i}^{n e i}\right)-\log P\left(V_{i} \mid \boldsymbol{P a}_{i}\right)\right)\right. \\
& \left.+\frac{\log (N)}{2}\left(\left|\hat{\Theta}_{i}^{n e i}\right|-\left|\hat{\Theta}_{i}\right|\right)\right) \\
& =\sum_{i: V_{i} \in \boldsymbol{V}_{d}}\left(\sum_{D_{f}}\left(\log \frac{P\left(V_{i}, \boldsymbol{P a}_{i}^{n e i}\right)}{\sum_{V_{i}} P\left(V_{i}, \boldsymbol{P a}_{i}^{n e i}\right)}-\log \frac{P\left(V_{i}, \boldsymbol{P a}_{i}\right)}{\sum_{V_{i}} P\left(V_{i}, \boldsymbol{P a}_{i}\right)}\right)\right. \\
& +\frac{\log (N)}{2}\left(\left|\hat{\Theta}_{i}^{n e i}\right|-\left|\hat{\Theta}_{i}\right|\right)\right) \\
& =\frac{N}{N_{p w}} \sum_{i: V_{i} \in \boldsymbol{V}_{d}}\left(\sum_{D_{p w}}\left(\log \frac{P\left(V_{i}, \boldsymbol{P a}_{i}^{n e i} \mid \boldsymbol{R}_{\boldsymbol{U}}=\mathbf{0}\right) \beta}{\sum_{V_{i}} P\left(V_{i}, \boldsymbol{P a}_{i}^{n e i} \mid \boldsymbol{R}_{\boldsymbol{U}}=\mathbf{0}\right) \beta}\right.\right. \\
& \left.-\log \frac{P\left(V_{i}, \boldsymbol{P a}_{i} \mid \boldsymbol{R}_{\boldsymbol{U}}=\mathbf{0}\right) \beta}{\sum_{V_{i}} P\left(V_{i}, \boldsymbol{P a}_{i} \mid \boldsymbol{R}_{\boldsymbol{U}}=\mathbf{0}\right) \beta}\right)+\frac{\log (N)}{2}\left(\left|\hat{\Theta}_{i}^{n e i}\right|-\left|\hat{\Theta}_{i}\right|\right)\right) \\
& =\frac{N}{N_{p w}} \sum_{i: V_{i} \in \boldsymbol{V}_{d}}\left(\sum_{j=1}^{\left|\boldsymbol{P a}_{i}^{n e i}\right|} \sum_{k=1}^{\left|V_{i}\right|} \widetilde{N}_{i j k} \log \frac{\widetilde{N}_{i j k}}{\widetilde{N}_{i j}}-\sum_{j=1}^{\left|\boldsymbol{P a}_{i}\right|} \sum_{k=1}^{\left|V_{i}\right|} \widetilde{N}_{i j k} \log \frac{\widetilde{N}_{i j k}}{\widetilde{N}_{i j}}\right. \\
& +\frac{\log (N)}{2}\left(\left|\hat{\Theta}_{i}^{n e i}\right|-\left|\hat{\Theta}_{i}\right|\right)\right) \\
& =\frac{N}{N_{p w}} \sum_{i: V_{i} \in \boldsymbol{V}_{d}}\left(\sum_{j=1}^{\left|\boldsymbol{P a}_{i}^{n e i}\right|} \sum_{k=1}^{\left|V_{i}\right|} \widetilde{N}_{i j k} \log \frac{\widetilde{N}_{i j k}}{\widetilde{N}_{i j}}-\sum_{j=1}^{\left|\boldsymbol{P a}_{i}\right|} \sum_{k=1}^{\left|V_{i}\right|} \widetilde{N}_{i j k} \log \frac{\widetilde{N}_{i j k}}{\widetilde{N}_{i j}}\right. \\
& +\frac{\log \left(N_{p w}\right)}{2}\left(\left|\hat{\Theta}_{i}^{n e i}\right|-\left|\hat{\Theta}_{i}\right|\right)+\frac{\log \left(N / N_{p w}\right)}{2}\left(\left|\hat{\Theta}_{i}^{n e i}\right|-\left|\hat{\Theta}_{i}\right|\right)\right) \\
& =\frac{N}{N_{p w}}\left(S_{B I C}\left(\mathcal{G}_{n e i} \mid D_{p w}, \beta\right)-S_{B I C}\left(\mathcal{G} \mid D_{p w}, \beta\right)\right. \\
& +\frac{\log \left(N / N_{p w}\right)}{2} \sum_{i: V_{i} \in \boldsymbol{V}_{d}}\left(\left|\hat{\Theta}_{i}^{n e i}\right|-\left|\hat{\Theta}_{i}\right|\right)\right) \\
& \propto S_{B I C}\left(\mathcal{G}_{n e i} \mid D_{p w}, \beta\right)-S_{B I C}\left(\mathcal{G} \mid D_{p w}, \beta\right)+O(1)
\end{aligned}
$$

# Proof 

In the above equations, $\beta=\prod_{R_{i} \in \boldsymbol{R}_{U}} \beta_{R_{i}}, \widetilde{N}_{i j k}$ and $\widetilde{N}_{i j}$ are defined by Eqs. (9) and (10). Equation (14) is a consequence of the recoverability of $P(\boldsymbol{U})$ given Eq. (7).

## Appendix B Derivation of Eq. (7)

Based on Mohan et al. (2013), Theorem 2, given Assumptions 1 and 2, the joint distribution $P(\boldsymbol{V})$ can be fully recovered from the observed data via the following equation:

$$
P(\boldsymbol{V})=\frac{P(\boldsymbol{V}, \boldsymbol{R}=\mathbf{0})}{\prod_{R_{i} \in \boldsymbol{R}} P\left(R_{i}=0 \mid \boldsymbol{P a}_{R_{i}}, \boldsymbol{R}_{\boldsymbol{P a}_{R_{i}}}=\mathbf{0}\right)}
$$

where $\boldsymbol{P a}_{R_{i}}$ is the set of parents of missing indicator $R_{i}$, and $\boldsymbol{R}_{\boldsymbol{P a}_{R_{i}}}$ is the set of missing indicator of the partially observed variables in $\boldsymbol{P a}_{R_{i}}$. Then,

$$
\begin{aligned}
P(\boldsymbol{V}) & =\frac{P(\boldsymbol{V}, \boldsymbol{R}=\mathbf{0})}{\prod_{R_{i} \in \boldsymbol{R}} P\left(R_{i}=0 \mid \boldsymbol{P a}_{R_{i}}, \boldsymbol{R}_{\boldsymbol{P a}_{R_{i}}}=\mathbf{0}\right)} \\
& =\frac{P(\boldsymbol{V} \mid \boldsymbol{R}=\mathbf{0}) P(\boldsymbol{R}=\mathbf{0})}{\prod_{R_{i} \in \boldsymbol{R}} P\left(R_{i}=0 \mid \boldsymbol{P a}_{R_{i}}, \boldsymbol{R}_{\boldsymbol{P a}_{R_{i}}}=\mathbf{0}\right)} \\
& =P(\boldsymbol{V} \mid \boldsymbol{R}=\mathbf{0}) \cdot \frac{P(\boldsymbol{R}=\mathbf{0})}{\prod_{R_{i} \in \boldsymbol{R}} \frac{P\left(\boldsymbol{P a}_{R_{i}} \mid R_{i}=0, \boldsymbol{R}_{\boldsymbol{P a}_{R_{i}}}=\mathbf{0}\right) P\left(R_{i}=0 \mid \boldsymbol{R}_{\boldsymbol{P a}_{R_{i}}}=\mathbf{0}\right)}{P\left(\boldsymbol{P a}_{R_{i}} \mid \boldsymbol{R}_{\boldsymbol{P a}_{R_{i}}}=\mathbf{0}\right)}} \\
& =P(\boldsymbol{V} \mid \boldsymbol{R}=\mathbf{0}) \cdot \\
& \underbrace{P(\boldsymbol{R}=\mathbf{0})}_{\prod_{R_{i} \in \boldsymbol{R}} P\left(R_{i}=0 \mid \boldsymbol{R}_{\boldsymbol{P a}_{R_{i}}}=\mathbf{0}\right)} \prod_{R_{i} \in \boldsymbol{R}} \underbrace{\frac{P\left(\boldsymbol{P a}_{R_{i}} \mid \boldsymbol{R}_{\boldsymbol{P a}_{R_{i}}}=\mathbf{0}\right)}{P\left(\boldsymbol{P a}_{R_{i}} \mid R_{i}=0, \boldsymbol{R}_{\boldsymbol{P a}_{R_{i}}}=\mathbf{0}\right)}}_{\beta_{R_{i}}}
\end{aligned}
$$

In the above equation, the term $c$ depends only on the missing indicators $\boldsymbol{R}$ and remains constant with respect to the observed variables $\boldsymbol{V}$. The product $\prod_{R_{i} \in \boldsymbol{R}} \beta_{R_{i}}$ represents the relative probability of a data case from the pairwise deleted data set being observed in the complete data set. For example, if a pairwise deleted data case has $c \prod_{R_{i} \in \boldsymbol{R}} \beta_{R_{i}}$ out of 0.8 , then its occurrence rate is assumed to drop by $20 \%$ in the complete data set compared to its occurrence rate in the pairwise deleted data set. Therefore, we use Eq. (7) to reweight the pairwise deleted data and estimate the underlying true distribution given the pairwise deleted data set.

# Appendix C Supplementary results from the structure learning experiments 

Refer to Tables 3, 4, 5, 6, 7 and 8.

Table 3 Mean and standard deviation of $F_{1}$ scores produced by Structural EM, HC-pairwise, HC-IPW and HC-aIPW for sparse networks, under the different assumptions of missingness and sample sizes


Table 4 Mean and standard deviation of normalised SHD scores produced by Structural EM, HC-pairwise, HC-IPW and HC-aIPW for sparse networks, under the different assumptions of missingness and sample sizes


Table 5 Mean and standard deviation of ${ }_{C}$ scores produced by Structural EM, HC-pairwise, HC-IPW and HC-aIPW for dense networks, under the different assumptions of missingness and sample sizes


Table 6 Mean and standard deviation of normalised SHD scores produced by Structural EM, HC-pairwise, HC-IPW and HC-aIPW for dense networks, under the different assumptions of missingness and sample sizes


Table 7 Mean and standard deviation of ${ }_{C_{1}}$ scores produced by Structural EM, HC-pairwise, HC-IPW and HC-aIPW for real-world networks, under the different assumptions of missingness and sample sizes


Table 8 Mean and standard deviation of normalised SHD scores produced by Structural EM, HC-pairwise, HC-IPW and HC-aIPW for real-world networks, under the different assumptions of missingness and sample sizes


# Appendix D Supplementary results of execution time 

See results in Table 9.

Table 9 Mean and standard deviation of execution times produced by Structural EM, HC-pairwise, HCIPW and HC-aIPW for sparse networks and relative to HC when applied to complete data, under the different assumptions of missingness and sample sizes


Acknowledgements This research was supported by the EPSRC Fellowship project EP/S001646/1 on Bayesian Artificial Intelligence for Decision Making under Uncertainty.

Author contributions All authors contributed to the study conception and design. Material preparation, data collection and analysis were performed by Yang Liu. The first draft of the manuscript was written by Yang Liu and all authors commented on previous versions of the manuscript. All authors read and approved the final manuscript.

Data availability The data used for the simulation results are available upon request to the corresponding author.

# Declarations 

Conflict of interest The authors declare that they have no conflict of interest.
