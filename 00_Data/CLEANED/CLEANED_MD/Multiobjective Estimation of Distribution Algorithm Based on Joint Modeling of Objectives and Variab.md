# Multi-objective Estimation of Distribution Algorithm Based on Joint Modeling of Objectives and Variables 

Hossein Karshenas, Roberto Santana, Concha Bielza, and Pedro Larrañaga


#### Abstract

This paper proposes a new multi-objective estimation of distribution algorithm (EDA) based on joint modeling of objectives and variables. This EDA uses the multi-dimensional Bayesian network as its probabilistic model. In this way it can capture the dependencies between objectives, variables and objectives, as well as the dependencies learnt between variables in other Bayesian network-based EDAs. This model leads to a problem decomposition that helps the proposed algorithm to find better trade-off solutions to the multi-objective problem. In addition to Pareto set approximation, the algorithm is also able to estimate the structure of the multi-objective problem. To apply the algorithm to many-objective problems, the algorithm includes four different ranking methods proposed in the literature for this purpose. The algorithm is applied to the set of walking fish group (WFG) problems, and its optimization performance is compared with an evolutionary algorithm and another multi-objective EDA. The experimental results show that the proposed algorithm performs significantly better on many of the problems and for different objective space dimensions, and achieves comparable results on some compared with the other algorithms.


Index Terms-Estimation of distribution algorithm, Joint objective-variable modeling, Many-objective problem, Multiobjective optimization, Objectives relationship.

## I. INTRODUCTION

MULTI-OBJECTIVE problems (MOPs) comprise several criteria that should be satisfied simultaneously, none of which can be preferred over others. Let $\mathcal{F}=\left\{f_{1}, \ldots, f_{m}\right\}$ be the set of objective functions. Then, given an MOP of the form

$$
\begin{aligned}
\min _{\boldsymbol{x}} & \boldsymbol{q}=\left(f_{1}(\boldsymbol{x}), \ldots, f_{m}(\boldsymbol{x})\right) \\
\text { subject to } & \left\{\begin{array}{l}
\boldsymbol{x} \in \mathcal{D} \subseteq \mathbb{R}^{n} \\
\boldsymbol{q} \in \mathcal{Q} \subseteq \mathbb{R}^{m}
\end{array}\right.
\end{aligned}
$$

the goal of a multi-objective optimization algorithm is to search for solutions that satisfy all or obtain an optimal trade-off between objectives. Note that here, without loss of generality, it is assumed that all objective functions are to be minimized.

[^0]Multi-objective evolutionary algorithms (MOEAs) [1]-[5] are considered as promising optimizers that have been successfully applied to a variety of MOPs. These algorithms use their nature-inspired operators to evolve a population of candidate solutions. This population-based optimization parallelizes the algorithm which can then simultaneously optimize several areas of the search space to arrive at several compromise solutions, as it is necessary when solving MOPs.

It is well known that in the presence of specific problem properties, traditional evolutionary algorithms (EAs) may find optimization difficult [6]. Estimation of distribution algorithms (EDAs) [7]-[10] are a relatively new computational paradigm proposed to overcome these difficulties. EDAs have also been applied to solve many MOPs [11]-[14]. Instead of genetic operators, these algorithms generate new candidate solutions from a probabilistic model, which is learnt from a set of promising solutions. The probabilistic model captures certain statistics about the values of problem variables and the important dependencies existing between these variables.

An important issue concerning MOEAs is how well they scale as the number of objectives in the MOP increases [15], [16]. This is especially important because real-world problems usually have many criteria that can be formulated as a many-objective problem. One way of accounting for this is to consider the relationships between objectives and explicitly reduce the number of objectives according to these relationships. Different methods, like correlation and principal component analysis [17]-[21], extending the definition of conflicting objectives [22], and linear programming [23] have been proposed for this purpose. These methods reduce optimization complexity by searching for a minimum subset of objectives.

In this study, we propose learning a joint probabilistic model of both objectives and variables within the context of EDAs. This allows the algorithm not only to capture the dependencies between variables, as in other EDAs, but also to learn the relationships between objectives and between objectives and variables. The relationships learnt can have more complex patterns of interaction than just linear correlation. These relationships are then implicitly used by the algorithm to generate new solutions in the search space. In addition to the set of solutions obtained in the Pareto set approximation, the joint probabilistic model learnt in this EDA provides the decision maker with an approximation of the MOP structure, i.e., the relationships among variables and objectives in MOP.

A preliminary study of this notion was presented in [24], discussing the incorporation of objectives into EDA model


[^0]:    This work has been partially supported by Consolider Ingenio 2010-CSD2007-00018, TIN2010-20900-C04-04, TIN2010-14931 and Cajal Blue Brain projects (Spanish Ministry of Science and Innovation), and Saiotek and Research Groups 2007-2012 (IT-242-07) programs (Basque Government).
    H. Karshenas, C. Bielza and P. Larrañaga are with the Computational Intelligence Group, Facultad de Informática, Universidad Politécnica de Madrid, Campus de Montegancedo, 28660 Boadilla del Monte, Madrid, Spain. E-mail: \{hkarshenas, mchielza, Pedro.larranaga\}@fi.upm.es
    R. Santana is with Intelligent System Group, Department of Computer Science and Artificial Intelligence, University of the Basque Country, Paseo Manuel de Lardizbal 1, 20080 San Sebastián-Donostia, Spain. Email: roberto.santana@ehu.es

building. In this paper, we extend the study by using a specific probabilistic modeling adapted from a multi-dimensional Bayesian network (MBN), usually used for multi-label classification tasks [25], [26]. In this type of problems, each instance or data point can have several class labels. The goal of learning a probabilistic model is then to predict the class labels of new unseen data points. On the other hand, in multi-objective optimization with EDAs, each solution in the search space has several objective values, and the goal is to generate new solutions from the probabilistic model that have better objective values. Clearly, there are similarities between the two problems that motivate the use of an MBN to capture the relationships between variables and objectives. For this purpose, the objectives are modeled as class variables in the probabilistic model and the dependencies learnt between objectives and variables in the model are exploited to generate new solutions. Using this type of model estimation, the structure of the MOP can be obtained systematically, and the proposed algorithm can be applied to many-objective problems. This paper examines how this algorithm performs on many-objective problems, using different ranking methods, and studies some of the MOP structures obtained by the algorithm.

The use of Bayesian network classifiers as the probabilistic model of an EDA has been previously reported for singleobjective optimization in the evolutionary Bayesian classifierbased optimization algorithm (EBCOA) [27], [28]. However, there are several key differences between EBCOA and the algorithm presented in this paper. First, the presence of multiple objectives in an MOP increases the information about the quality of solutions (possibly contradictory) that should be addressed during modeling. Second, instead of classifying the solutions into disjoint classes, which may blur the differences in the quality of the solutions, here the continuous objective values are directly used in model learning. Third, in contrast to a fixed dependency between the objectives and variables, the algorithm presented here dynamically learns the relationships between the objectives and variables. In this way, the model can select a subset of variables that has more influence on each objective.

The rest of this paper is organized as follows. Section II briefly reviews some background required to follow the discussion in this paper. The proposed EDA based on joint modeling of objectives and variables is described in Section III. Section IV presents the numerical results of applying the algorithm on a set of MOPs and analyzes the results. Possible MOP structures learnt by the algorithm are also analyzed. Finally, the paper is concluded in Section V and some lines of future research are proposed.

## II. PRELIMINARIES

## A. Estimation of Distribution Algorithms

Traditional genetic operators used for generating new solutions in evolutionary algorithms act almost blindly and are very likely to disrupt the good sub-solutions found so far which will affect the optimization convergence. This disruption is more likely to occur as the correlation between problem

ESTIMATION OF DISTRIBUTION ALGORITHM
Inputs:
Representation of solutions
Objective function $f$
$1 P_{0} \leftarrow$ Generate initial population according to the given representation
$2 F_{0} \leftarrow$ Evaluate each individual $x$ of $P_{0}$ using $f$
$3 t \leftarrow 0$
4 while termination criteria are not met do
$5 \quad S_{t} \leftarrow$ Select a subset of $P_{t}$ according to $F_{t}$
$6 \quad \hat{\rho}_{t}(\boldsymbol{x}) \leftarrow$ Estimate the probability density of solutions in $S_{t}$
$7 \quad U_{t} \leftarrow$ Sample from $\hat{\rho}_{t}(\boldsymbol{x})$ according to the given representation
$8 \quad H_{t} \leftarrow$ Evaluate $U_{t}$ using $f$
$9 \quad P_{t+1} \leftarrow$ Incorporate $U_{t}$ into $P_{t}$ according to $F_{t}$ and $H_{t}$
$10 \quad F_{t+1} \leftarrow$ Update $F_{t}$ according to the solutions in $P_{t+1}$
$11 \quad t \leftarrow t+1$
12 end while
Output: The best solution(s) in $P_{t}$
Fig. 1. The basic steps of an EDA
variables increases, rendering the algorithm inefficient for such problems. Estimation of distribution algorithms (EDAs) make use of probabilistic models to replace the genetic operators in order to overcome this shortcoming. Fig. 1 shows the basic steps of a typical EDA.

The set of selected solutions $S_{t}$ serves as a training dataset to estimate the probabilistic model and leads the search towards regions with better fitness (represented by the selected solutions). The set of new solutions $U_{t}$ is generated using the probabilities encoded in the probabilistic model in accordance with the statistics collected from the solutions in $S_{t}$. The choice of probabilistic model can have a major influence on the performance and efficiency of EDAs. For example, some probabilistic models can also encode the dependencies between the variables, which they can use to identify and preserve these dependencies in the sampling process. Bayesian networks (see below) are one of these probabilistic models that can encode dependencies between any number of variables. Thus EDAs using this probabilistic model can be applied to problems with highly correlated variables and a complex structure.

In the context of multi-objective optimization, when there is more than one objective function in the problem, $F_{t}$ is a matrix with $m$ columns not a vector. A successful strategy adopted by many MOEAs (including multi-objective EDAs) [29], [30] is to modify the solution selection and replacement mechanisms and use solution reproduction (model learning and sampling for EDAs) as in single objective optimization. However, as we discuss later, the inclusion of more objectives into the problem can also affect how the new solutions are being generated.

## B. Multi-dimensional Bayesian Network Classifiers

Bayesian networks [31] are multivariate probabilistic graphical models, consisting of two components:

- the structure, represented by a directed acyclic graph (DAG), where the nodes are the problem variables and the arcs are conditional (in)dependencies between triplets of variables, and
- the parameters, expressing for each variable $X_{i}$ the conditional probability of each of its values, given different

![img-0.jpeg](img-0.jpeg)

Fig. 2. An example of a multi-dimensional Bayesian network structure, used for multi-label classification

Value combinations of its parent variables (Pa(Xi)) according to the structure, i.e.,

$$p(x_i | pa(X_i)),$$

where pa(Xi) is a value combination for the parent variables in Pa(Xi).

By introducing a special node C into the network as the class node, Bayesian networks can be used for classification tasks to obtain the posterior probability of a class value c, given feature values x1,...,xn, i.e., p(c | x1,...,xn). Several types of Bayesian network classifiers have been proposed in the literature (naïve Bayes, seminaïve Bayes, tree augmented naïve Bayes, etc.).

If a data point can simultaneously belong to several (say m) classes, then a multi-dimensional Bayesian network (MBN) can be learnt to perform multi-label classification, where the posterior probability is now given by

$$p(c_1, \dots, c_m | x_1, \dots, x_n).$$

Fig. 2 shows an example of the structure of an MBN used for multi-label classification. In this type of model, the nodes are organized in two separate layers: the top layer comprises class variables and the bottom layer contains feature variables. The set of arcs in the structure is partitioned into three subsets, resulting in the following subgraphs:

- the class subgraph, containing the class nodes and the interactions between them,
- the feature subgraph, comprising the feature variables and their relations, and
- the bridge subgraph, depicting the one-way dependencies from class nodes to feature nodes.

The probabilistic model can answer several types of questions: the class labels of a given data point, the most probable feature values for a given combination of class labels, and the most probable values for a subset of features or classes given the value of the others. Considering the similarity between multi-labeled classification and MOPs, the respective questions will be: what are the estimated objective values of a given solution, what is the most probable solution resulting in a specific value combination for the objectives, and, having found the values of some objectives or variables, what will the most probable values of the others be. Also worthy of note is that the existence of specific types of decomposability in the MBN structure can make these types of inference questions simpler to answer [26].

## *C. Gaussian Bayesian Networks*

In domains with continuous valued variables, it is usually assumed that the variables follow a Gaussian distribution. The Bayesian network learnt from a set of variables, having a multivariate Gaussian distribution p(x) = N(μ, Σ) as their joint probability function, is called a Gaussian Bayesian network (GBN). Here, μ is the mean vector and Σ is the covariance matrix of the distribution.

The structure of a GBN is similar to any other Bayesian network. However, the network parameters define a conditional (linear) Gaussian distribution for the variable corresponding to each node, given the values of the parent variables [32], [33]

$$p(x_i | pa(X_i)) = \mathcal{N}(\mu_i + \sum_{X_j \in Pa(X_i)} w_{ij}(x_j - \mu_j), \nu_i^2), \qquad (2)$$

where µ<sub>i</sub> is the mean of variable X<sub>i</sub>, ν<sub>i</sub> is the standard deviation of the univariate conditional distribution, regression coefficients w<sub>ij</sub> specify the importance of each of the parents, and x<sub>j</sub> is the corresponding value of X<sub>j</sub> in pa(X<sub>i</sub>).

## III. MBN-EDA

### *A. Joint Modeling of Variables and Objectives*

It is common practice in EDAs to estimate a probabilistic model of the problem variables only encoding the characteristics of the selected solutions S<sub>t</sub> (see Algorithm 1). The sampling algorithm is then expected to generate a new set of solutions U<sub>t</sub> from this model according to the statistics collected from the solutions in S<sub>t</sub>. Apart from this, there is no requirement for the solutions in U<sub>t</sub> to have better or comparable objective values to those in S<sub>t</sub>.

Using this solution generation scheme, exploration of the search space, driven by the characteristics encoded in the probabilistic model, is usually good. To extend the scheme in order to account for objective values, the objectives can also be encoded in the model. In this way, preferences concerning objective values (obtained from the selected solutions) can be encoded in the model. This applies especially to MOPs, where more information about the quality of the solutions is available because there are several objectives. In this study, we show that this type of information, handled by expressive probabilistic models, turns out to be useful for solving multi-objective problems.

The joint learning of objectives and variables also suggests a new way for estimating the relationships between MOP variables and objectives. These relationships can be exploited by the optimization algorithm to facilitate the search, focusing only on variables that influence the values of an objective. Thus, an implicit variable selection is taking place for each of the objectives. Moreover, the relationships between the objectives are also captured, helping to identify how the values of some objectives might change against the values of some others, using the conditional independence relationships encoded in the model.

### *B. An EDA based on MBN Estimation*

The probabilistic model used in this paper for joint model learning is the multi-dimensional Bayesian network (MBN).

![img-1.jpeg](img-1.jpeg)

Fig. 3. An overview of the proposed MBN-EDA

The variables are modeled as feature nodes and objectives as continuous-valued class nodes. The feature subgraph encodes the dependencies between problem variables like the models learnt by other EDAs that use Bayesian networks as their probabilistic model [34]–[39]. The bridge and class subgraphs, however, encode new types of dependencies. The bridge subgraph shows the interdependencies between each objective and the variables, and the class subgraph represents the direct relationships between objectives.

Let (X, Q) = (X₁, ..., Xₙ, Q₁, ..., Qₙ) denote the joint vector of problem variables and objectives respectively (of size n + m). Then, like any other Bayesian network, the learnt MBN encodes a factorization of the joint probability distribution of its constituent variables. This will give an implicit decomposition of the MOP for this joint vector. The joint probability distribution of this MBN is given by

$$p\left(x₁, \dots, xₙ, q₁, \dots, qₙ\right) = \prod_{i=1}^{m} p\left(x_i | pa(X_i)\right) \cdot \prod_{j=1}^{m} p(q_j | pa(Q_j)),\qquad (3)$$

where Pa(Xᵢ) ⊆ {X ∪ Q ∖Xᵢ} and Pa(Qᵢ) ⊆ {Q ∖Qᵢ} respectively are the parents of each variable and objective, and pa(Xᵢ) and pa(Qᵢ) represent one of their possible value combinations.

The proposed algorithm, which is called MBN-EDA, uses this probabilistic model to capture the characteristics of selected solutions and their objective values, and generates new candidate solutions for MOP in search of the Pareto optimal solutions. Fig. 3 shows the algorithm layout. After selecting a subset of solutions according to a selection mechanism, e.g., non-dominated sorting+truncation selection, the solutions are joined with their objective values to form extended solutions. These extended solutions, comprising values for both variables and objectives, are used to serve as a data set for estimating an MBN. The model sampler generates new candidate solutions from the learnt MBN, taking into consideration the values of both objectives and variables. Finally, these new solutions are added to the population based on a replacement mechanism. The following sections provide more details about the algorithm.

### *C. Solution Ranking for Elitist Selection*

In contrast to single objective optimization, where the objective values can be used directly to rank solutions, the existence of multiple objectives in MOPs necessitates the application of an intermediate function of the form

$$G: Q ⊆ ℝ^m \mapsto T ⊆ ℝ,\tag{4}$$

whose output will be used to rank the solutions. One of the most commonly used techniques in multi-objective optimization is the non-dominated sorting algorithm [40], which sorts the solutions into non-dominated Pareto fronts and then sorts the solutions within each front according to their crowding distances. However, it has been shown that the effectiveness of this ranking method drops as the number of objectives increases [41]–[43].

Finding efficient ranking methods for many-objective optimization (when there are more than three objectives) is the topic of ongoing research, and several methods have been proposed in the literature. In this study, we adopt four methods, which have been reported to show better performance for evolutionary many-objective optimization [44]–[47], to rank the solutions in the MBN-EDA selection step. Let q = (q₁, ..., qₙ) = (f₁(x), ..., fₙ(x)) and r = (r₁, ..., rₙ) = (f₁(y), ..., fₙ(y)) be the objective values obtained for two solutions x and y, where x, y ∈ D ⊆ ℝ^n, and assume all objectives are to be minimized. Then the considered ranking methods are as follows:

- Weighted sum of the objectives, using a weight vector w = (w₁, ..., wₙ) showing the importance of each objective:

$$G_{\text{WS}}(\mathbf{q}) = \sum_{i=1}^{m} w_i q_i.\tag{4}$$

- Distance to the best objective values b = (b₁, ..., bₙ), using some distance measure d(·, ·) in the objective space (e.g., Euclidean distance):

$$G_{\text{DB}}(\mathbf{q}) = \mathbf{d}(\mathbf{b},\mathbf{q}).\tag{5}$$

When the best objective values are not known beforehand (which is usually the case), the best objective values achieved so far (considering each objective individually) in the current population (Fᵢ in Algorithm 1) can be used, i.e., the best value bᵢ for objective fᵢ is

$$b_i = \min_{\mathbf{q} ∈ F_i} \{ q_i \}.$$

- Global detriment or the total gain lost by each solution against other solutions in the population:

$$G_{\text{GD}}(\mathbf{q}) = \sum_{\forall \mathbf{r} ∈ F_i, \mathbf{r} \neq \mathbf{q}} \text{gain}(\mathbf{r}, \mathbf{q}),\tag{6}$$

where the function gain $(\cdot, \cdot)$ computes the gain obtained in the objective values by a solution $\boldsymbol{q}$ compared to another solution $\boldsymbol{r}$ :

$$
\operatorname{gain}(\boldsymbol{q}, \boldsymbol{r})=\sum_{i=1}^{m} \max \left\{0, r_{i}-q_{i}\right\}
$$

- Profit of the gain obtained from each solution against other solutions in the population:

$$
\begin{aligned}
G_{\mathrm{PG}}(\boldsymbol{q})=\max _{\boldsymbol{r} \in F_{i}, \boldsymbol{r} \neq \boldsymbol{q}} & \operatorname{gain}(\boldsymbol{q}, \boldsymbol{r}) \\
& -\max _{\boldsymbol{r} \in F_{i}, \boldsymbol{r} \neq \boldsymbol{q}} \operatorname{gain}(\boldsymbol{r}, \boldsymbol{q})
\end{aligned}
$$

where the definition of gain $(\cdot, \cdot)$ is equal to (7) above.
Applied to the objective values obtained for the MOP candidate solutions, these ranking methods will result in an ordered set, which is then used to select a subset of solutions. Any selection mechanism can be simply applied on the ordered set. MBN-EDA uses truncation selection where the best $\tau \cdot N$ solutions (according to the ranking method) of the population are selected for a given $\tau \in(0,1)$, where $N$ is the number of solutions in the population.

## D. Solution Reproduction based on Probabilistic Modeling

1) Estimating the Probabilistic Model: A search+score strategy [48]-[50] is used in MBN-EDA to learn the MBN from the data. In this strategy, a search algorithm is employed to explore the space of possible MBN structures to find a structure that closely matches the data. The quality of different MBN structures obtained in this search process is measured using a scoring metric, usually computed from data. Although using a search algorithm (structure search) within another search algorithm (solution search) may appear to be circular, note that the aim of the structure search algorithm is to find a structure that adequately represents data characteristics rather than the optimum structure. For further discussion refer to [51].

A greedy local search algorithm is used to learn the structure of MBN. In each iteration, this algorithm weighs up all possible arc addition, removal and reversal operations that will map the current network structure to a new valid structure (according to the MBN structural constrains) in a single step and then applies the operation that will result in the highest increase in the network score [52]. The Bayesian information criterion (BIC) [53] is used to score possible MBN structures, This score is based on a penalized log-likelihood measure

$$
\begin{aligned}
\sum_{k=1}^{N}( & \sum_{i=1}^{n} \log \left(p\left(x_{k i} \mid p a_{k}\left(X_{i}\right)\right)\right) \\
& +\sum_{j=1}^{m} \log \left(p\left(q_{k j} \mid p a_{k}\left(Q_{j}\right)\right)\right) \\
-\frac{1}{2} \log (N)( & \sum_{i=1}^{n}\left|P a\left(X_{i}\right)\right|+\sum_{j=1}^{m}\left|P a\left(Q_{j}\right)\right| \\
& +2(n+m))
\end{aligned}
$$

where $x_{k i}$ and $q_{k j}$ are the values of variable $X_{i}$ and objective $Q_{j}$ in the $k$ th joint solution, respectively. Similarly, $p a_{k}\left(X_{i}\right)$ and $p a_{k}\left(Q_{j}\right)$ are respectively the value combinations of the parents of $X_{i}$ and $Q_{j}$ in the $k$ th joint solution. $\left|P a\left(X_{i}\right)\right| \leq$ $n+m-1$ and $\left|P a\left(Q_{j}\right)\right| \leq m-1$ respectively show the number of parents of $X_{i}$ and $Q_{j}$, according to the MBN structure.

The second term in (9), which is the penalizing term, is computed assuming that MBN is implemented in continuous domains with a GBN. The parameters of this type of MBN are computed from the mean vector and covariance matrix of the multivariate Gaussian distribution (MGD) estimated for the joint vector of variables and objectives: $\mathcal{N}\left(\boldsymbol{m}_{<1 \times(n+m)>}, \boldsymbol{S}_{<(n+m) \times(n+m)>}\right)$. Usually the maximum likelihood (ML) estimation is used to estimate the parameters of MGD (the mean vector and covariance matrix) from the data. However, when the dataset does not provide sufficient statistics, this method cannot obtain a robust estimation of the parameters and especially the covariance matrix which should be symmetric and positive-definite. In our case, since the solutions are extended by appending the objective values, this problem becomes even worse.

Regularization techniques [54], [55] are one of the methods that can be used to overcome this problem. MBN-EDA uses the covariance shrinkage estimation [56] to improve the estimation of MGD for the joint vector of variables and objectives. In this method, the ML estimation of the covariance matrix is linearly combined with a simpler target matrix, which has a smaller number of parameters. More specifically, a diagonal matrix with zeros in all off-diagonal entries is used as the target to enforce shrinkage towards sparser matrices while leaving the diagonal elements (variances) intact, preventing early loss of diversity:

$$
\boldsymbol{S}^{*}=(1-\lambda) \boldsymbol{S}+\lambda \boldsymbol{T}
$$

Here, $\boldsymbol{T}$ represents the target matrix and $\lambda$ is the shrinkage intensity (also called regularization parameter), which can be computed analytically in a data-driven manner by minimizing a mean square error loss function. In practice, the ML estimation of the correlation matrix is used to compute this shrinkage intensity for the specified diagonal target matrix. The regularized estimation in (10) leads to a statistically more efficient covariance matrix that is well-conditioned and positive-definite, as necessary for computing the parameters of MBN. For more details on applying regularization techniques to the model learning of continuous EDAs, see [57].
2) Generating New Solutions: New candidate solutions to the MOP can be sampled from the probability distribution encoded in the MBN. Probabilistic logic sampling [58], also known as forward sampling, is the method frequently used for sampling Bayesian networks. This method first obtains an ancestral or topological ordering of the network nodes. In this ordering, each node appears after its parent nodes according to the Bayesian network structure. Consequently, all objective nodes appear before variable nodes in the topological ordering obtained for an MBN, due to the restrictions imposed by the bridge subgraph in model learning. New solutions are generated by sampling the conditional probability distributions

estimated for each node in the MBN according to the computed order. Since all node $i$ 's parents appear before node $i$ in the ordering, all of its parent nodes will have already been sampled at the time of sampling node $i$ and therefore the parameters of the conditional distribution of this node can be computed.

Thanks to the joint modeling of objectives and variables in the MBN that has encoded the dependencies between the variables and objectives, any information about good objective values can be inserted and propagated in the network in the sampling process, increasing the probability of generating variable values that will result in such objective values. Moreover, the restrictions imposed by the direction of the arcs in the MBN bridge subgraph decrease the number of generated solutions that are inconsistent with the inserted evidence [59].

The approach adopted in this paper treats the objective nodes as normal nodes, and new dummy values (since they are not computed from the objective functions) are generated for these nodes using the probabilities encoded in the MBN. In this way the interdependencies that are captured during model learning between objectives are also taken into account in the sampling process. When a variable node that has some objective nodes as its parents is being sampled, these dummy objective values are used to compute the parameters of the conditional distribution. The values generated for the objectives are an approximation of the characteristics encoded in the model for the objective values of the selected solutions. Therefore, this method can increase the conformity of the sampled solutions with the learnt MBN.

## IV. EXPERIMENTS

To study the performance of MBN-EDA in multi-objective optimization and to see how the proposed scheme for solution reproduction works, this algorithm is applied on a set of MOPs and its behavior is analyzed. The algorithm is implemented using the Matlab toolbox for EDAs (MatEDA) [60], and the implementation of the MBN learning algorithm is adapted from the code provided for GBN learning [61]. Before learning the MBN, training data (extended solutions) are first standardized to have a mean of zero and a standard deviation of one, in order to simplify the learning process by reducing the number of parameters in each node. The learning algorithm restarts the structure search from a new random structure after reaching a local optimum of the score function up to a maximum number of node score evaluations. The algorithm finally returns the highest scoring network in all these sub-searches.

To get a better assessment of the optimization performance of MBN-EDA, the results are compared against two other algorithms: a multi-objective evolutionary algorithm (MOEA) and a multi-objective EDA. The MOEA uses simulated binary crossover [62] and polynomial mutation [63] in continuous domains as its genetic operators to generate new solutions, and is used as a standard reference algorithm in many evolutionary multi-objective optimization studies [5], [64]. The multiobjective EDA, namely the regularity-model based multiobjective EDA (RM-MEDA) [13] has been demonstrated to outperform many MOEAs on several benchmark functions.

RM-MEDA assumes a certain type of smoothness for the Pareto set and iteratively applies local principal component analysis to build a piece-wise continuous manifold of dimension $m-1$ ( $m$ is the number of objectives). This is then used with Gaussian noise to generate new solutions.

The above four ranking methods (Equations (4)-(6) and (8)) are implemented within an individual selector engine which is plugged into each of these algorithms. Since in a black-box optimization scenario, none of the objectives takes precedence over others, equal weights are used for all of the objectives in the weighted sum ranking method $\left(G_{W S}\right)$. To allow the values of different objectives with possibly different ranges to be combined, all objective values are normalized before applying a ranking method. MBN-EDA and MOEA use the same ranking method as for selection in the replacement step. RM-MEDA does not have a replacement step, and the newly generated solutions completely replace the whole population.

## A. MOPs

In [65], Huband et al. reviewed many of the available MOP benchmarks in the literature, based on which they proposed a set of MOPs called the walking fish group (WFG) problems. These problems encompass a diverse set of properties that can be found in real-world MOPs and, therefore, raise substantial obstacles for any multi-objective optimization algorithm. Each of the objective functions $f_{j}$ of an MOP in this benchmark takes the following form

$$
\min _{\boldsymbol{z}} \quad f_{j}(\boldsymbol{z})=D \cdot z_{m}+S_{j} \cdot h_{j}\left(z_{1}, \ldots, z_{m-1}\right)
$$

where $D$ and $S_{j}$ are scaling factors and the functions $h_{j}(\cdot)$ together determine the shape of the Pareto optimal front (e.g., concave, convex, etc.) for that MOP. $\boldsymbol{z}$ is an $m$-dimensional vector obtained by applying a number of transformation functions, like shifting, biasing or reduction, to the $n$-dimensional input solution $\boldsymbol{x} \in \mathcal{D}$ and is composed of two parts: the first $m-1$ parameters, $z_{1}, \ldots, z_{m-1}$, are obtained from the first $k$ variables of the input solution, and the last parameter $\left(z_{m}\right)$ is obtained from the last $l$ variables of the input solution, where $n=k+l$. To simplify the application of transformation functions in the input solution, $k$ is assumed to be a multiple of $m-1$ and $l$ an even number.

The number of both objectives and variables can be scaled in this benchmark, which consists of nine MOPs. All WFG problems, except the first three, have a concave Pareto optimal front. WFG1 has a mixed convex-concave optimal front, WFG2 has a disconnected convex front, and WFG3 has a degenerated one-dimensional linear front. For most of these MOPs, the optimal solution of objectives is shifted away from zero to neutralize any bias of the optimization algorithm towards smaller values for the variables. Moreover, in many of the WFG problems, the objective functions are inseparable, requiring the optimization algorithm to consider the relationships between variables.

In this study, these WFG problems have been used in the experiments to test the algorithms. The number of objectives considered are $3,5,7,10,15$ and 20 , whereas the number of variables is set to 16 (with some exceptions). In this way, we

will be able to investigate the performance of the algorithms against an increasing number of objectives with an unchanged solution space size.

## B. Experimental Design

Each algorithm is applied with each ranking method separately to each WFG problem with different numbers of objectives. Therefore, there will be $3 \times 4 \times 9 \times 6$ possible combinations. The additive epsilon indicator [64], [66] is used to measure the quality of the results obtained by each of the algorithms because of its tractable computational complexity for many-objective problems. This indicator is based on the notion of epsilon efficiency [67], and the corresponding relation of epsilon dominance that is defined as

$$
\begin{aligned}
& \forall \boldsymbol{x}, \boldsymbol{y} \in \mathcal{D} \\
& \quad \boldsymbol{x} \preceq_{\epsilon+} \boldsymbol{y} \quad \Longleftrightarrow \quad \forall f_{i} \in \mathcal{F} \quad f_{i}(\boldsymbol{x}) \leq \epsilon+f_{i}(\boldsymbol{y})
\end{aligned}
$$

The additive epsilon indicator between two approximations $A$ and $B$ of the Pareto set is defined as the smallest epsilon value that allows all the solutions in $B$ to be ' $\epsilon+$ '-dominated by at least one solution in $A$ :

$$
I_{\epsilon+}(A, B)=\min _{\epsilon \in \mathbb{R}^{+}} \quad \forall \boldsymbol{y} \in B \quad \exists \boldsymbol{x} \in A \mid \boldsymbol{x} \preceq_{\epsilon+} \boldsymbol{y}
$$

According to this definition, the additive epsilon indicator for an approximation $A$ of the Pareto set is obtained using a reference set $R$

$$
I_{\epsilon+}(A)=I_{\epsilon+}(A, R)
$$

This definition implies that smaller values of the epsilon indicator are better. A good choice for the reference set $R$ is an approximation of the Pareto optimal set. However, the size of a good approximation of the Pareto optimal set should increase exponentially with the number of objectives in the MOP to offer a good coverage of the Pareto optimal front. Therefore, this choice of reference set is impractical for manyobjective problems. The reference set considered in this paper is composed of the endpoint solutions, obtained by setting one of the objectives to its minimum value and the others to their maximum value, plus the solution representing an approximate compromise between the values of all objectives (e.g., the mean value in the objectives range). The size of this reference set grows only linearly with the number of objectives, and the inclusion of endpoints favors those Pareto set approximations that result in a more scattered Pareto front.

## C. Results

Fig. 4-6 show the epsilon indicator value obtained for the Pareto set approximations of each of the algorithms, averaged over 20 independent runs. All of the algorithms stop after reaching a maximum number of generations, which is set to 300. The population size is equal for all algorithms and is gradually incremented as the number of objectives increases according to Table I. In each generation, $50 \%$ of the solutions in the population are selected for reproduction(i.e., $\tau=0.5$ ).

Table II shows the statistical analysis of the results for the algorithms with different ranking methods on each of

TABLE I
THE POPULATION SIZE USED FOR DIFFERENT NUMBER OF OBJECTIVES AND VARIABLES.


the MOPs with different numbers of objectives. The nonparametric Friedman test [68] is used to check for the statistical differences of the algorithm performance. When the null hypothesis that all the algorithms have an equal average rank is rejected for a specific problem configuration with a p-value less than 0.05 , the entry related to the algorithm with the best Friedman rank is shown in bold. The numbers in parentheses show the results of pairwise comparisons using BergmannHommel's post-hoc test with a significance level of $\alpha=0.05$. The first number shows how many algorithms are significantly worse than the algorithm listed in this column, and the second number shows how many algorithms are significantly better.

The objectives in WFG1 are unimodal and biased for specific regions of their input. For this problem, MBN-EDA is able to obtain significantly better Pareto set approximations than the other two algorithms. The performance of the algorithm is very similar when using the different ranking methods tested in these experiments (Fig. 4, left column). Even though there are more interdependencies between the variables in WFG2, MBN-EDA is able to obtain significantly better results for this problem, evidencing the advantage of its probabilistic model for guiding the solution space search. The difference in the optimal front of the MOP problems does not significantly affect MBN-EDA's optimization ability as observed for WFG3, which is very similar to WFG2 except for the shape of the Pareto optimal front. Moreover, approximating the degenerated front in this problem requires good search process exploitation, which, according to the results for this problem, MBN-EDA is better able to do than the other two algorithms.

For WFG4 (Fig. 5, left column), where all of the objectives are multi-modal, the optimization results obtained by MBNEDA with different ranking methods are significantly better in most of objective space dimensions. For some of the ranking methods, MOEA and MBN-EDA performances are comparable as the number of objectives increase, suggesting the usefulness of genetic operators if there are a large number of optima in a problem. When objective multi-modality is combined with deception, as in WFG5, MBN-EDA performance significantly deteriorates. In fact this algorithm has the worsted optimization performance compared with the other two algorithms for this problem, where it obtains significantly worse Pareto set approximations with all the tested ranking methods, and specially for larger objective space dimensions. A possible explanation for this behavior is that the relationships between deceptive objectives do not provide sufficient information to help the algorithm generate good trade-off solutions in the search space.

The interdependencies between variables in WFG6 are more complex than in the WFG2 and WFG3 problems. Therefore,

![img-2.jpeg](img-2.jpeg)

Fig. 4. The average epsilon indicator values for WFG1 (left column), WFG2 (middle column) and WFG3 (right column) problems.

We find that the choice of the ranking method used in solution selection, which provides the training data for model estimation, will play a major role. In this MOP, the results obtained by MBN-EDA with the $G_{PG}$ and $G_{GD}$ ranking methods are significantly better than for the other algorithms, whereas the results are comparable or significantly worse with the other two ranking methods when the number of objectives is increased. This also shows that the gain function defined in (7) can be a good measure of solutions superiority in this type of MOP.

In WFG7 and WFG8, the optimum value of each variable is biased based on the values of other variables. All of the algorithms find it very difficult to deal with this property of the problem. Again, we see (Fig. 6, left and middle columns) that the choice of ranking method has a significant influence on algorithm performance. With some of the ranking methods (e.g., $G_{PG}$ and $G_{GD}$), MBN-EDA is able to obtain significantly better approximations of the Pareto optimal set for these two problems according to the quality indicator values. The last problem (WFG9) combines many of the properties found in the previous WFG problems. Specifically, apart from variable optimal values being biased, many of the objectives are deceptive as in WFG5. As described previously for WFG5, this prevents MBN-EDA from being able to per-

![img-3.jpeg](img-3.jpeg)

Fig. 5. The average epsilon indicator values for WFG4 (left column), WFG5 (middle column) and WFG6 (right column) problems.

form considerably better than the other two algorithms, despite the additional information it collects from data. Nevertheless, the performance of MBN-EDA for this problem is comparable to the other two algorithms, and, with some ranking methods ($G_{WS}$ and $G_{DB}$), is significantly better.

In general, the results suggest that there are several factors affecting the optimization performance of the tested algorithms on the selected set of MOP problems. According to the selected quality indicator, MBN-EDA is able to obtain better approximations of the Pareto set than the other two algorithms for many of the tested MOPs featuring different properties and on different objective space dimensions. MBN-EDA finds some specific MOP properties, like deception in the variable values, difficult to deal with.

For some of the tested MOPs, the choice of the ranking method plays a crucial role in algorithm performance and some algorithms tend to be more compatible with specific ranking methods. For example, MBN-EDA performed better than the other algorithms for most MOPs using $G_{<PG>}$ as the ranking method. Since the solution selection mechanism is similar in all algorithms (as they use similar ranking methods), a significant difference in the performance between one algorithm and the others can be attributed to its solution reproduction mechanism. Therefore, the better optimization

![img-4.jpeg](img-4.jpeg)

Fig. 6. The average epsilon indicator values for WFG7 (left column), WFG8 (middle column) and WFG9 (right column) problems.

Results for MBN-EDA may be related to model estimation and sampling being better, as they concern both objectives and variables. Moreover, although the choice of probabilistic model in an EDA is important, it should be noted that the difference between MBN-EDA and RM-MEDA performance is not only due to the difference in their probabilistic models. We have previously shown [24] that the incorporation of objectives into the same probabilistic model can result in significantly better performance.

In some of the problem instances (e.g., WFG6 with GPG), with the increase in the objective space dimension, the algorithms seem to obtain better Pareto set approximations that result in lower quality indicator values (meaning better approximations). Note, however, that like the algorithms, the computation of quality indicator values is also affected by the increase in the objective space dimension. In larger objective spaces, the Pareto set approximations obtained by the algorithms will become sparser, as they are using small populations. Also since a small reference set is used to evaluate the algorithms, the differences in the performance of an algorithm in different objective space dimensions will not be clear. However, since an equal reference set is used for each specific objective space dimension, the indicator values can be used to compare the performance of different algorithms in

TABLE II
The results of statistical difference tests for different WFG problems with different number of objectives and four different ranking methods. The bold entries show the algorithm obtaining the best ranking according to the statistical test. The numbers in the parentheses shows the number of algorithms that are significantly worse and better than each algorithm, respectively, considering a 0.05 significance level (refer to the text for more discussion of the statistical test).
![img-5.jpeg](img-5.jpeg)

![img-6.jpeg](img-6.jpeg)

Fig. 7. The average weight of the links from objectives to variables in 5-objective WFG1 problem with irrelevant variables.

![img-7.jpeg](img-7.jpeg)

Fig. 8. The average weight of the links between objectives in 8-objective WFG1 problem with three pairs of similar objectives.

that dimension.

### *D. MOP Structure Estimation*

A major concern of this study is to analyze the MOP structures estimated by MBN-EDA in the course of evolution. These structures are important not only because they can improve optimization by providing information about different types of (in)dependencies existing in the problem (as shown in Section IV-C), but also because they can give decision makers more control over the selection of the desired information from Pareto set approximations [69] and better insight into the way different variables influence the objectives or how objectives interact [70]. MBN-EDA's ability to retrieve the MOP structure is tested in different case studies by investigating the structures learnt for the WFG1 problem with five objectives and 16 variables and an already known MOP structure. To include the factor of different training data for estimating the MOP structure in the analysis, two of the previously introduced ranking methods, i.e., $G_{PG}$ and $G_{DB}$, are used with MBN-EDA in the study.

In the first case study, nine irrelevant variables are added to the problem and uniformly distributed among other variables. These variables do not affect the outcome of objective values in the MOP. Fig. 7 shows the absolute weight of the links encoded in the MBN's bridge substructure between objectives and variables along the evolution path of MBN-EDA. The weights are averaged over 20 independent runs. We found that MBN-EDA is able to clearly distinguish between relevant and irrelevant variables in the studied MOP. The low weight of the links between objectives and irrelevant variables in the estimated MBNs is because either the objectives and these variables have been encoded as conditionally independent of the other variables and objectives or any existing link has been attached a very small weight, allowing the algorithm to bypass the noise introduced by these variables to the problem. Although the models are learnt from different initial populations in the different runs, the structural information encoded between objectives and variables is very similar. It is also shown that the populations selected according to the $G_{PG}$ ranking method help to better distinguish between relevant and irrelevant variables especially in the final generations where the algorithm focuses on specific regions of the search space.

The second case study analyzes the structures learnt for an eight-objective WFG1 problem with three pairs of similar objectives. Fig. 8 compares the absolute weight of the arcs between similar objectives and between dissimilar objective pairs, encoded in the class substructure of MBN in different generations of MBN-EDA. The results are averaged over 20 independent runs. The relatively high weights between similar objectives show that MBN-EDA is correctly encoding a strong dependency between these objectives compared with other de-

![img-8.jpeg](img-8.jpeg)

Fig. 9. Part of the structure learnt for the 5-objective WFG1 problem showing the most significant arcs and their corresponding nodes.

pendencies in the class subgraph. Note that a closer inspection of the models learnt in different runs with different initial populations has revealed that such a dependency between similar objectives is encoded in the model in all the runs, i.e., 100% of the time. We also find that the information about the similarity of objectives in the MBN class subgraph is better captured from the populations selected according to the GDB ranking method.

Based on the observations from the above two case studies, the third case study directly inspects the structures learnt by MBN-EDA for the original WFG1 problem. In the five-objective WFG1 problem considered in the case studies reported in this section, the first k = 4 variables determine the position of a given solution in the objective space using different shape functions h<sup>j</sup>. This is then linearly combined with a distance parameter, obtained from the last l = 12 variables. A simplified definition of the five objective functions in this problem can be given as follows [65]:

$$
\begin{split}
f_1(\mathbf{x}) &= a + 2 \cdot h_1 \left( g_2(x_1), g_2(x_2), g_2(x_3), g_2(x_4)) \right) \\
f_2(\mathbf{x}) &= a + 4 \cdot h_2 \left( g_2(x_1), g_2(x_2), g_2(x_3), g_2(x_4)) \right) \\
f_3(\mathbf{x}) &= a + 6 \cdot h_3 \left( g_2(x_1), g_2(x_2), g_2(x_3)) \right) \\
f_4(\mathbf{x}) &= a + 8 \cdot h_4 \left( g_2(x_1), g_2(x_2)) \right. \\
f_5(\mathbf{x}) &= a + 10 \cdot h_5 \left( g_2(x_1) \right),
\end{split} \tag{15}
$$

where a = g<sub>1</sub>(x<sub>5</sub>, . . . , x<sub>16</sub>), and functions g<sub>1</sub>(·) and g<sub>2</sub>(·) represent a composition of transformations on the input variables.

Fig. 9 shows part of the structure learnt for this problem, consisting of significant arcs and their corresponding nodes that have an average absolute weight value greater than a threshold set to w ≥ 0.1 (constituting about 7% of the most significant arcs). While there are many links capturing the obscure (in)dependencies between variables (not depicted here), it is evident that MBN-EDA attaches more importance to the links between objectives in the class subgraph, and between the objectives and the first four variables in the bridge subgraph. Moreover, these dependencies conform to the function definitions given in (15). For example, the link between objectives Q<sup>2</sup> and Q<sup>4</sup>, which is captured using both tested ranking methods, is supported by the fact that h<sup>2</sup> is a multiplication of h<sup>4</sup> and two other factors obtained from variables X<sup>3</sup> and X<sup>4</sup>. Another example is the relationship between objective Q<sup>1</sup> and the four variables, either directly or through the relationship with other objectives, since all four variables influence the value of this objective.

An important point to note here is the significance of the information provided by the dependencies between objectives and between objectives and variables in multi-objective optimization from MBN-EDA point of view. There are some studies in the literature that analyze how the dependencies between variables are represented in probabilistic models [71]. But, to the best of our knowledge, the importance of the dependencies involving objectives have not been considered so far in other EDAs used for multi-objective optimization. Such dependencies allow the proposed MBN-EDA to approximate how the variables can affect objective values, which is used to generate new solutions with better objective values.

### V. CONCLUSIONS

The similarity between multi-label classification and multi-objective optimization motivates the use of MBNs in the context of EDAs to solve MOPs. This paper proposes a new modeling approach in MO-EDAs that uses MBN estimation to learn a joint model of objectives and variables while at the same time differentiating their role in the network. This model can capture not only the relationships between variables like other EDAs, but also the relationships between variables and objectives, and between objectives. The proposed MBN-EDA is able to deal with many-objective problems by exploiting these new types of relationships encoded in the MBN and implicitly obtaining a decomposition of the MOP, which is used to generate new solutions.

MBN estimation is incorporated into continuous EDAs using Gaussian Bayesian networks where each network node encodes a conditional Gaussian distribution. To obtain a more robust estimation of the model parameters, MBN-EDA employs regularization techniques, previously applied only to single-objective EDAs. This helps the algorithm to obtain a sparser structure, avoiding the effect of possible noise in the data and simplifying many-objective optimization.

The results of exhaustive experiments, applying MBN-EDA with different ranking methods to the WFG problems with a different number of objectives, show that, according to

the epsilon quality indicator and compared with two other algorithms, a standard MOEA and a competitive EDA, this algorithm is able to obtain significantly better approximations of the Pareto set for many of these MOPs, with a significance level of $\alpha=0.05$. We found that the choice of ranking methods has a major influence on the performance of the algorithms for some of the problems, as they determine the population used for model estimation and offspring reproduction. The results also show that the proposed MBN-EDA was unable to satisfactorily deal with some MOP properties, like deception in the values of the variables.

The proposed joint model learning approach suggests a way of obtaining the MOP structure that can be used for decision making. An analysis of the structures learnt by MBN-EDA along the evolution path show that the proposed algorithm is able to distinguish between relevant and irrelevant variables, performing a type of variable selection for the objectives encoded in the model. It can also capture stronger dependencies between similar objectives. The analysis of the specific structures learnt for the five-objective WPQ1 problem shows that MBN-EDA is able to obtain a very good approximation of this MOP structure and that the information provided by the dependencies between variables and objectives and between objectives, which other EDAs completely overlook, can be very important for multi-objective optimization.

There are many ways to extend this work. This new modeling method provides a promising platform for the experts or decision makers to incorporate preference information [72], [73] into the model as conditional (in)dependency relations between objectives and variables, as well as preferable values for some objectives. The dependencies learnt between objectives in the MOP structure can be used to analyze relationships like conflict or redundancy between sets of objectives. The application of MBN-EDA to real-world problems with unknown structures and to check how the captured relationships meet decision-maker expectations are also potential future areas of research.
