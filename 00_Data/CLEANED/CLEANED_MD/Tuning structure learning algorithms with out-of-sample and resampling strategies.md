# Tuning structure learning algorithms with out-of-sample and resampling strategies 

Kiattikun Chobtham ${ }^{1} \cdot$ Anthony C. Constantinou ${ }^{1}$<br>Received: 26 June 2023 / Revised: 2 March 2024 / Accepted: 21 March 2024 /<br>Published online: 24 May 2024<br>(c) The Author(s) 2024


#### Abstract

One of the challenges practitioners face when applying structure learning algorithms to their data involves determining a set of hyperparameters; otherwise, a set of hyperparameter defaults is assumed. The optimal hyperparameter configuration often depends on multiple factors, including the size and density of the usually unknown underlying true graph, the sample size of the input data, and the structure learning algorithm. We propose a novel hyperparameter tuning method, called the Out-of-sample Tuning for Structure Learning (OTSL), that employs out-of-sample and resampling strategies to estimate the optimal hyperparameter configuration for structure learning, given the input dataset and structure learning algorithm. Synthetic experiments show that employing OTSL to tune the hyperparameters of hybrid and score-based structure learning algorithms leads to improvements in graphical accuracy compared to the state-of-the-art. We also illustrate the applicability of this approach to real datasets from different disciplines.


Keywords Bayesian networks $\cdot$ Bootstrapping $\cdot$ Causal discovery $\cdot$ Hyperparameter optimisation $\cdot$ Probabilistic graphical models

## 1 Introduction

A Bayesian Network (BN) is a probabilistic graphical model that enables decision-makers to reason under uncertainty, particularly in complex systems that require answers to interventional and counterfactual questions (Pearl, [27]). It is represented by a Directed Acyclic Graph (DAG) $G$ which consists of a set of nodes $\boldsymbol{V}=\left\{A_{1}, \ldots, A_{\mathrm{V}}\right\}$ corresponding to random variables and a set of arcs corresponding to the dependence relationships between variables in a BN or the causal relationships in a causal BN , where an arc $A_{\mathrm{k}} \rightarrow A_{\mathrm{j}}$ is viewed as $A_{\mathrm{k}}$

[^0]
[^0]:    囚 Kiattikun Chobtham
    k.chobtham@qmul.ac.uk
    Anthony C. Constantinou
    a.constantinou@qmul.ac.uk

    1 Bayesian Artificial Intelligence Research Lab, Machine Intelligence and Decision Systems (MInDS) Research Group, School of Electronic Engineering and Computer Science, Queen Mary University of London, London E1 4NS, UK

being the direct cause of node $A_{\mathrm{j}}$. The causal or dependency relationships are represented by a set of conditional probabilities $P\left(A_{\mathrm{i}} \mid \operatorname{parent}\left(A_{\mathrm{i}}\right)\right)$, where parent $\left(A_{\mathrm{i}}\right)$ refers to the parent-set of $A_{\mathrm{i}}$. The joint distribution over all nodes $\boldsymbol{V}$ is defined as the product of all conditional probabilities as follows:

$$
P\left(A_{1}, \ldots, A_{\mathrm{V}}\right)=\prod_{\mathrm{i}=1}^{\mathrm{V}} P\left(A_{\mathrm{i}} \mid \operatorname{parent}\left(A_{\mathrm{i}}\right)\right)
$$

The graphical structure of a BN model refers to the way in which the nodes and edges are organised. In the context of BN structure learning, the objective involves finding the most appropriate structure that best represents the probabilistic relationships amongst the input variables. Conversely, in causal discovery (i.e. learning causal BNs), the goal is explicitly to uncover structures where the relationships are presumed to be causal. Learning the graph structure of a BN from data, whether causal or not, is generally NP-hard where the number of possible graphs grows super-exponentially in the number of variables, making it computationally intractable.

There are two main classes of unsupervised structure learning algorithms; namely constraint-based and score-based learning. A constraint-based algorithm typically relies on statistical Conditional Independence (CI) tests (see Sect. 2.1) to construct a graph skeleton, and then orientate some of the edges that make up the skeleton. On the other hand, a scorebased algorithm involves a search method that traverses the space of possible graphs, and returns the graph with the highest objective score (see Sect. 2.2). Algorithms that combine both of these learning strategies are common in the literature, and they are referred to as hybrid learning algorithms.

There are hundreds of structure learning algorithms in the literature [23]. One of the most well-established constraint-based algorithms is PC-Stable by Colombo and Maathuis [7], which is based on PC by Spirtes and Glymour [37] but addresses PC's sensitivity to the order of the variables as read from data. PC-Stable returns a Partially DAG (PDAG) that contains directed and undirected edges, and which can sometimes be converted into a Completed PDAG (CPDAG) that represents a set of Markov equivalence DAGs that encode the same CI statements. For instance, a serial connection $(\mathrm{A} \rightarrow \mathrm{B} \rightarrow \mathrm{C})$ and a divergence connection $(\mathrm{A} \leftarrow \mathrm{B} \rightarrow \mathrm{C})$ encode $\mathrm{A} \perp \mathrm{C} \mid \mathrm{B}$, indicating that the direction of these edges cannot be determined purely from observational data. Score-based algorithms will often return a DAG or a CPDAG output. However, if a score-based algorithm employs a score-equivalent objective function, the DAG output will represent a random DAG of the highest scoring Markov equivalence class (or CPDAG).

Traversing the search-space of graphs is computationally expensive, and hence, most score-based algorithms tend to be approximate. For example, the Hill-Climbing (HC) algorithm by Heckerman et al. [19] and the FGES algorithm by Ramsey [30] rely on greedy heuristics. HC performs hill-climbing search in the space of DAGs, whereas FGES greedily searches the space of CPDAGs. Approximate solutions include hybrid algorithms such as the Max-Min Hill-Climbing (MMHC) by Tsamardinos et al. [40] and hybrid MCMC by Kuipers et al. [24]. Hybrid algorithms tend to involve a restrict phase and a maximisation phase, and MMHC is a widely-used example of this; i.e. it starts with constraint-based learning and uses CI tests to determine the restricted space of DAGs, followed by applying hill-climbing search to the reduced space of DAGs. Hybrid MCMC works in a similar manner and starts by creating a restricted search-space using PC, followed by MCMC sampling in the node

ordering space of DAGs. It is also worth noting the NOTEARS algorithm [45] which introduces a novel score-based approach that combines continuous optimisation with an acyclicity constraint, for DAG discovery suitable for high-dimensional continuous data learning.

An issue with these algorithms is that they come with a set of unoptimised hyperparameters. Because there is little guidance on how to choose these hyperparameters, most papers in the literature use these algorithms with either their hyperparameter defaults or test them over a restricted set of different plausible hyperparameter values. This approach, which can be viewed as a grid search over all hyperparameter combinations, is also supported by Yang and Shami [44] who provide a comprehensive review of hyperparameter tuning methods with their available libraries, and discuss suitable tuning methods for common machine learning algorithms. However, evaluating machine learning algorithms over different combinations of plausible hyperparameters is, in general, a computationally expensive and a time-consuming process. On this basis, Filippou et al. [15] propose a pipeline to handle the generation and evaluation of machine learning models, including hyperparameter optimisation, with a focus on improving the efficiency of model creation.

In this paper, we focus on hyperparameter tuning for structure learning algorithms that are typically used to recover causal relationships. These algorithms can generally be divided into in-sample tuning and out-of-sample tuning methods, where the former utilises all available data and the latter uses a subset of the available data as a test data to tune hyperparameter configurations on data points that were not included in the training set. In-sample tuning approaches include the Stability Approach to Regularization Selection (StARS) by Liu et al. [25], which optimises for model stability by selecting the hyperparameter configuration that generates the most stable learnt graphs over perturbations of the input data. Out-of-sample tuning approaches include the Out-of-sample Causal Tuning (OCT) by Biza et al. [2, 3], which performs cross-validation to identify the Markov Blankets (MBs) for each variable. The MB of a variable A represents a set of variables that make A independent of all other variables, and can serve as a feature selection method. Specifically, the MB of A includes the parents of A, its children, and the parents of its children. The OCT algorithm uses MBs to obtain a Random Forest model and optimises hyperparameters for predictive accuracy over test data. Experimental results showed that it performed well against the in-sample StARS approach discussed above.

This paper proposes a novel hyperparameter tuning method that employs out-of-sample and resampling strategies to estimate the optimal hyperparameter configuration for structure learning, given the input dataset and structure learning algorithm. This optimisation approach is tailored for unsupervised structure learning algorithms due to the necessity of adapting to structural objective scores and graphical metrics, as well as accommodating non-standard hyperparameter spaces that are essential for effectively addressing the computational efficiency challenges inherent to structure learning algorithms that are typically used to explore intractable search-spaces of graphical structures. The paper is organised as follows: Sect. 2 provides preliminary information on hyperparameters in the context of structure learning, Sect. 3 describes the proposed hyperparameter tuning approach, Sect. 4 presents the results, and we provide our concluding remarks in Sect. 5.

# 2 Preliminary information 

This section provides an overview of the common CI tests used by constraint-based algorithms, and the common objective functions used by score-based algorithms. Sections 2.1

and 2.2 cover the hyperparameters that could be tuned for functions that test for CI and for objective functions, respectively.

# 2.1 Functions that test for conditional independence (CI) 

### 2.1.1 Pearson's Chi ${ }^{2}$

The Pearson's $\mathrm{Chi}^{2}$ statistical test [28] is a commonly used function for testing CI given discrete data. It assumes the null hypothesis that node A and node B are conditionally independent given the set of nodes $\mathbf{C}$. The test produces a $p$-value of the test statistic which is used to determine whether to reject or not the null hypothesis. The significance threshold ( $\alpha$ ) serves as the hyperparameter of the Pearson's $\mathrm{Chi}^{2}$ test, and is set to 0.05 by convention. If the $p$-value is less than, the null hypothesis is rejected, and node A and node B are assumed to be conditionally dependent given $\mathbf{C}$. If the $p$-value is greater than $\alpha$, the null hypothesis is not rejected, and hence, node A and node B are assumed to be conditionally independent given $\mathbf{C}$. The formula for the Pearson's $\mathrm{Chi}^{2}$ test is:

$$
\chi^{2}=2 \sum \frac{\left(n_{\mathrm{abc}}-m_{\mathrm{abc}}\right)^{2}}{n_{\mathrm{abc}}}
$$

where $n_{\mathrm{abc}}$ is the number of instances in the data D where $A=a, B=b$, and $C=c$, $m_{\mathrm{abc}}=\frac{n_{\mathrm{ac}} \cdot n_{\mathrm{bc}}}{n_{\mathrm{c}}}$, and the process of calculating the number of instances of $n_{\mathrm{ac}}, n_{\mathrm{bc}}$, and $n_{\mathrm{c}}$ is analogous to that of $n_{\mathrm{abc}}$. We will use $\mathrm{Chi}^{2}$ interchangeably with the Pearson's $\mathrm{Chi}^{2}$ test for the rest of this paper.

### 2.1.2 Mutual information (MI)

Shannon's Mutual Information (MI) was introduced as a measure of mutual dependence between two discrete variables [13]. The MI between two nodes A and B is defined as follows:

$$
\operatorname{MI}(A, B)=\sum_{a, b} \widehat{p}(a, b) \ln \left[\frac{\widehat{p}(a, b)}{\widehat{p}(a) \widehat{p}(b)}\right]
$$

where $\widehat{p}(a, b)$ refers to $\widehat{p}(A=a, B=b)$ the maximum likelihood estimate of $p(a, b)$. It is calculated as $\widehat{\mathrm{p}}(a, b)=\frac{n_{\mathrm{ab}}}{n}$, where $n$ is the total number of samples, and the process of calculating $\widehat{p}(a)$ and $\widehat{p}(b)$ is analogous to that of $\widehat{p}(a, b)$. Consequently, conditional MI [35] can be used for CI test, defined as follows:

$$
\operatorname{MI}(A, B \mid \mathbf{C})=\sum_{\mathrm{a}, \mathrm{~b}, \mathrm{c}} \widehat{\mathrm{p}}(a, b, c) \ln \left[\frac{\widehat{\mathrm{p}}(a, b, c) \widehat{\mathrm{p}}(c)}{\widehat{\mathrm{p}}(a, c) \cdot \widehat{\mathrm{p}}(b, c)}\right]
$$

where $\widehat{p}(a, b, c)=\frac{n_{\mathrm{abc}}}{n}$, and the process of calculating $\widehat{p}(a, c), \widehat{p}(b, c)$, and $\widehat{p}(c)$ is analogous to that of $\widehat{p}(a, b, c)$. The significance threshold $\alpha$ serves the same purposed as in the $\mathrm{Chi}^{2}$ test, i.e. if $\operatorname{MI}(A, B \mid \mathbf{C})$ is greater than $\alpha$, node $A$ and node $B$ are conditionally independent given $\mathbf{C}$.

### 2.1.3 Shrinkage mutual information test (MI-sh)

James and Stein [20] proposed a shrinkage estimate of MI for two random variables in the form of a regulariser, which they call the James-Stein-type shrinkage intensity $\lambda$. The conditional

MI-sh test [34] between A and B given $\mathbf{C}$ is defined as the expectation of $\mathrm{MI}-\operatorname{sh}(A, B \mid \mathbf{C})$ with respect to the distribution of $\mathbf{C}$. As with the $\mathrm{Chi}^{2}$ and MI tests, they use the significance threshold $\alpha$ to accept or reject the same null hypothesis. The MI-sh test is described as follows:

$$
\mathrm{MI}-\operatorname{sh}(A, B \mid \mathbf{C})=\sum_{\mathrm{a}, \mathrm{~b}, \mathrm{c}} p^{\text {shrink }}(a, b, c) \log \left[\frac{p^{\text {shrink }}(a, b, c) p^{\text {shrink }}(c)}{p^{\text {shrink }}(a, c) p^{\text {shrink }}(b, c)}\right]
$$

where

$$
\begin{gathered}
p^{\text {shrink }}(a, b, c)=\lambda \frac{1}{|A||B||C|}+(1-\lambda) \widehat{p}(a, b, c) \\
p^{\text {shrink }}(a, c)=\lambda \frac{1}{|A||C|}+(1-\lambda) \widehat{p}(a, c) \\
p^{\text {shrink }}(b, c)=\lambda \frac{1}{|B||C|}+(1-\lambda) \widehat{p}(b, c) \\
p^{\text {shrink }}(c)=\lambda \frac{1}{|C|}+(1-\lambda) \widehat{p}(c)
\end{gathered}
$$

where $|A|,|B|$, and $|C|$ denote the number of states of variables $A, B$, and the set of variables $\boldsymbol{C}$, respectively, and $\lambda$ is the shrinkage intensity. Hausser and Strimmer [18] proposed a closed-form estimator $\lambda^{*}$ that employs James-Stein-type shrinkage making it highly efficient computationally. In the case of estimating a single parameter, $\lambda^{*}$ is defined as follows:

$$
\lambda^{*}=\frac{1-\sum_{k=1}^{V}\left(\widehat{p}_{k}\right)^{2}}{(n-1) \sum_{k=1}^{V}\left(\frac{1}{V}-\widehat{p}_{k}\right)^{2}}
$$

where $\lambda^{*}=[0,1]$ is the shrinkage intensity, $\lambda^{*}=0$ means no shrinkage and $\lambda^{*}=1$ full shrinkage, n is the sample size, and $\widehat{p}_{1} \ldots, \widehat{p}_{V}$ are the probabilities of a given variable where $\sum_{k} \widehat{p}_{k}=1$.

# 2.2 Objective functions 

### 2.2.1 Bayesian Dirichlet with equivalent uniforms (BDeu $_{\text {iss }}$ )

$\mathrm{BDeu}_{\text {iss }}$ is an objective function proposed by Heckerman et al. [19] to determine the maximum a posteriori (MAP) structure by assuming equivalent uniform priors for a graph G . $\mathrm{BDeu}_{\text {iss }}$ is score-equivalent, which means that it generates the same score for DAGs which entail the same joint probability distribution and are part of the same Markov equivalence class. Moreover, $\mathrm{BDeu}_{\text {iss }}$ is a decomposable score where the score of a graph represents the sum of $\mathrm{BDeu}_{\text {iss }}$ scores allocated to each node, given its parents, that is part of that graph. Decomposability is an important property that makes objective functions computationally efficient for structure learning. Traversing the search-space of graphs with a decomposable score implies that the scores of nodes that have not had a change to their parent-set can be carried over from the previous iteration, rather than re-computed.

Because the $\mathrm{BDeu}_{\text {iss }}$ score is typically represented by a small value, its closed-form solution is expressed as a log function:

$$
\mathrm{BDeu}_{\mathrm{iss}}(G, D)=\sum_{i=1}^{V} \sum_{j=1}^{q_{i}}\left[\log \frac{\Gamma\left(\mathrm{iss} / q_{i}\right)}{\Gamma\left(\mathrm{iss} / q_{i}+N_{\mathrm{ij}}\right)}+\sum_{k=1}^{r_{i}} \log \frac{\Gamma\left(\mathrm{iss} / r_{i} q_{i}+N_{\mathrm{ijk}}\right)}{\Gamma\left(\mathrm{iss} / r_{i} q_{i}\right)}\right]
$$

where $G$ is a DAG, $D$ is observational data, $V$ is the number of variables, $\Gamma$ is the gamma function, $\mathrm{q}_{\mathrm{i}}$ denotes the number of possible combinations of values of parents of node $A_{i}$ and is equal to 1 if $A_{i}$ has no parents, $j$ is the index of that combination, $N_{\mathrm{ijk}}$ represents the number of instances in the data D where node $A_{\mathrm{i}}$ takes on its $k$ th value and its parents the $j$ th combination of values, $r_{\mathrm{i}}$ is the number of states of node $A_{\mathrm{i}}$, and $N_{\mathrm{ij}}=\sum_{k=1}^{r_{\mathrm{i}}} N_{\mathrm{ijk}}$ represents the total number of instances in data D where parents of node $A_{\mathrm{i}}$ have the $j$ th combination of values. The imaginary sample size (iss) represents the hyperparameter of $\mathrm{BDeu}_{\mathrm{iss}}$, and it is often referred to the user's prior belief about the impact of the prior distribution on the objective score. Silander et al. [36] observed that increasing iss led to a higher number of arcs and, hence, denser learnt structures. They suggest that a reasonable iss for small sample sizes is between 1 and 20. In this work, we assume that the default iss hyperparameter for $\mathrm{BDeu}_{\mathrm{iss}}$ score is 1 , as it is set in most studies and implementations of $\mathrm{BDeu}_{\mathrm{iss}}$.

# 2.2.2 Bayesian information criterion (BIC) 

Schwarz [32] proposed BIC as a model-selection function to reduce the risk of modeloverfitting by balancing the goodness-of-fit with model dimensionality. It is based on Occam's razor principle in that the simplest solution is usually the best solution. Like $\mathrm{BDeu}_{\mathrm{iss}}$, BIC is decomposable and score-equivalent. The general form of the score for discrete variables is expressed as follows:

$$
\operatorname{BIC}(G, D)=\operatorname{LL}(G, D)-\frac{\log (n)}{2} F
$$

where $n$ is the sample size, $\operatorname{LL}(G, D)$ denotes the Log-Likelihood (LL) of the data $D$ given the graph $G$ :

$$
\operatorname{LL}(G, D)=\log [\widehat{p}(D \mid G)]=\sum_{i=1}^{V} \sum_{j=1}^{q_{\mathrm{i}}} \sum_{k=1}^{r_{\mathrm{i}}} N_{\mathrm{ijk}} \log \frac{N_{\mathrm{ijk}}}{N_{\mathrm{ij}}}
$$

and $F$ is the complexity penalty represented by the number of free parameters of the model. It can be expressed as follows:

$$
F=\sum_{i=1}^{V}\left(r_{i}-1\right) q_{\mathrm{i}}
$$

Chen and Chen [4] presented a modified version of BIC which they call Extended BIC (EBIC) that can be used to control the density of the learnt graph. This is achieved by introducing the hyperparameter $0 \leq \gamma$ that penalises the number of free parameters in the BN, which, in turn, are inversely proportional to the number of arcs in the learnt graph. This is equivalent to saying that large values of $\gamma$ will favour sparser graphs. EBIC is defined as follows:

$$
\operatorname{EBIC}_{\gamma}(G, D)=\operatorname{LL}(G, D)-\frac{\log (n)}{2} F-\gamma \log (V) F, 0 \leq \gamma
$$

Foygel and Drton [16] studied the impact of the hyperparameter $\gamma^{\prime} \in[0,1]$ and found that $\gamma^{\prime}=0.5$ is best in most synthetic experiments. However, it is acknowledged that the optimal value of $\gamma^{\prime}$ is not invariant, and hence, its optimisation remains an open question. In this paper, we define $\mathrm{EBIC}_{\text {normalised } \gamma}$ as:

$$
\operatorname{EBIC}_{\text {normalised } \gamma}(G, D)=\operatorname{LL}(G, D)-\frac{\log (n)}{2} F-\gamma^{\prime} \log (V) F, 0 \leq \gamma^{\prime} \leq 1
$$

where the hyperparameter $0 \leq \gamma$ is normalised to $\gamma^{\prime} \in[0,1]$. Thus, $\gamma$ is the hyperparameter of $\mathrm{EBIC}_{\gamma}$ and $\mathrm{EBIC}_{\text {normalised }_{\gamma}}$ where $\mathrm{EBIC}_{\gamma=0}=\mathrm{EBIC}_{\text {normalised }_{\gamma}=0}=\mathrm{BIC}$.

# 3 Out-of-sample tuning for structure learning (OTSL) 

This section describes the algorithm we propose for hyperparameter tuning, which we call Out-of-sample Tuning for Structure Learning (OTSL). OTSL determines the optimal hyperparameter configuration for a structure learning algorithm by performing out-of-sample resampling and optimisation on test data.

### 3.1 Resampling with replacement with multiple training and test datasets

We consider the out-of-sample tuning approach OCT by Biza et al. [2, 3]. However, instead of utilising cross-validation as in the original studies, we employ an approach that relies on resampling with replacement. Our decision is motivated by the relevant studies of McLatchie et al. [26], Rao et al. [31], and Piironen et al. [29] that empirically show that cross-validation led to the learning of complex models, with a tendency to underperform when the input data contain many variables with a relatively small sample size. On the other hand, resampling with replacement in structure learning was found to improve the accuracy of the learnt graphical structure $[5,17]$.

Resampling with replacement or bootstrapping [14] is commonly used for sampling in statistics and machine learning. Unlike traditional cross-validation where each fold is drawn from a dataset without replacement, bootstrapping involves resampling with replacement to produce new data for validation that may contain multiple instances of the original cases. We adopt this strategy for the OTSL algorithm and use resampling with replacement to generate multiple datasets for training and testing from a single observational dataset, where the training datasets are used for structure learning and the test datasets for hyperparameter tuning.

### 3.2 Tuning hyperparameters on test data

Section 2 describes both the BIC and $\mathrm{BDeu}_{\text {iss }}$ scores, which are commonly used as objective functions in score-based structure learning algorithms. However, an issue with these modelselection scores is that the graph they score the highest tends not to be the ground truth graph. The model averaging MAHC by Constantinou et al. [11] demonstrates that output graphs with slightly lower average BIC score may improve the graphical accuracy of the learnt graph, especially in the presence of data noise which is inevitably present in real data. This model averaging approach motivates the design of the proposed tuning approach, especially in that it focuses on maximising model-selection by taking the average over multiple data splits.

We use the illustrations in Fig. 1 to motivate our optimisation strategy, which is based on the HC algorithm and synthetic ALARM data with sample size 10 k . Figure 1a presents the relationship between the graphical metric F1 (refer to Sect. 4) and the objective score $\mathrm{BDeu}_{\text {iss }}$ when iss varies between 1 and 20. The tuning method involves resampling with replacement, where the input dataset of 10 k is resampled 10 times and, at each iteration, split 9-to-1 for training and testing (refer to Algorithm 1). Specifically,

![img-0.jpeg](img-0.jpeg)

Fig. 1 The F1 scores over different hyperparameter values for $\mathrm{BDeu}_{\text {iss }}$ and $\mathrm{EBIC}_{\gamma}$. The illustration is based on the HC algorithm and synthetic ALARM data with a sample size 10 k
i. $\mathrm{BDeu}_{\text {iss }}$ is the tuning score optimised for different iss hyperparameters. Note that at each iteration of iss, the tuned score represents the average $\mathrm{BDeu}_{\text {iss }}$ score over 10 iterations of resampling (refer to Algorithms 1 and 3).
ii. F1 is the score for each graph recovered at different values of iss in $\mathrm{BDeu}_{\text {iss }}$.

The illustration shows that it may be possible to optimise for iss in $\mathrm{BDeu}_{\text {iss }}$ such that it improves the F1 score. Specifically, Fig. 1a shows that the optimal value for iss in $\mathrm{BDeu}_{\text {iss }}$ is 6 , which, in turn, leads to a $0.57 \%$ improvement in F1 relative to the unoptimised hyperparameter default when iss $=1$.

Figure 1 b repeats the same exercise and assumes that the tuning score is $\mathrm{EBIC}_{\text {normalised }_{\gamma}}$, where $\gamma$ in $\mathrm{EBIC}_{\gamma}$ varies between 0 and 19. In this example, we notice that the optimal $\gamma$ hyperparameter is $\gamma=3$ and happens to lead to the highest F1 score; an improvement of $11.63 \%$ relative to the unoptimised $\mathrm{EBIC}_{\text {normalised }_{\gamma}}$ score when $\gamma=0$.

# 3.3 The out-of-sample tuning for structure learning (OTSL) algorithm 

Algorithm 1 describes the OTSL algorithm. As described in Algorithm 1, OTSL takes as input a dataset D , the number of iterations $K$ for resampling (we assume 10 as default), the tuning score (we explore $\mathrm{BDeu}_{\text {iss }}$ and $\mathrm{EBIC}_{\text {normalised }_{\gamma}}$ in this study), and a list of configurations $C$ that specify the structure learning algorithm along with its hyperparameters and a range of those hyperparameters to be explored.

OTSL starts by resampling $K$ training and test datasets given the input data. It then applies the specified structure learning algorithm with configurations C to each training dataset in $K$, and optimises the hyperparameters of either $\mathrm{BDeu}_{\text {iss }}$ or $\mathrm{EBIC}_{\text {normalised }_{\gamma}}$ on each corresponding test dataset in $K$. The optimal configuration is the one that generates the highest average tuning score over $K$ training and test datasets, and is returned as the optimal configuration. This process is described in Algorithms 1, 2, and 3, where Algorithms 2 and 3 describe the tuning process for $\mathrm{EBIC}_{\text {normalised }_{\gamma}}$ and $\mathrm{BDeu}_{\text {iss }}$, respectively.

Algorithm 1 Out-of-sample Tuning for Structure Learning (OTSL)

Input: dataset D , a list of configurations $\mathbf{C}$, iteration K , score for tuning
Output: $\mathrm{c}^{\prime}$
1: The sample size of train data $\mathrm{X}=$ the number of instances of $\mathrm{D} \times(\mathrm{K}-1) / \mathrm{K}$
2: The sample size of test data $\mathrm{Y}=$ the number of instances of $\mathrm{D} / \mathrm{K}$
3: $\quad$ For $\mathrm{k}=1$ to $\mathbf{K}$
4: $\quad \mathrm{D}_{\mathrm{k}, \text { training }} \leftarrow$ resample with replacement (D) with sample size X
5: $\quad \mathrm{D}_{\mathrm{k}, \text { test }} \leftarrow$ resample with replacement $\left(\mathrm{D} \backslash \mathrm{D}_{\mathrm{k}, \text { training }}\right)$ with sample size Y
6: For $\mathrm{c} \in \mathbf{C} / /$ find the optimal configuration
7: $\quad$ For $\mathrm{k}=1$ to $\mathbf{K}$
8: $\quad \mathrm{G}_{\mathrm{c}, \mathrm{k}} \leftarrow$ structure learning algorithm $\left(\mathrm{D}_{\mathrm{k}, \text { training }}, \mathrm{c}\right)$
9: If $\mathrm{G}_{\mathrm{c}, \mathrm{k}}$ is CPDAG
10 $\mathrm{G}_{\mathrm{c}, \mathrm{k}} \leftarrow$ CPDAGtoDAG $\left(\mathrm{G}_{\mathrm{c}, \mathrm{k}}\right)$
11: If $\mathrm{G}_{\mathrm{c}, \mathrm{k}}$ is PDAG
12: $\quad \mathrm{G}_{\mathrm{c}, \mathrm{k}} \leftarrow$ PDAGtoDAG $\left(\mathrm{G}_{\mathrm{c}, \mathrm{k}}\right)$
13: $\quad \mathrm{S}_{\mathrm{c}, \mathrm{k}} \leftarrow$ score_for_tuning $\left(\mathrm{G}_{\mathrm{c}, \mathrm{k}}, \mathrm{D}_{\mathrm{k}, \text { test }}, \mathrm{c}\right) / /$ scoring functions given test data and hyperparameters
14: $\mathrm{S}_{\mathrm{c}}=$ average $\mathrm{S}_{\mathrm{c}, \mathrm{k}}$ over K
15: $\quad \mathrm{c}^{\prime}=\arg \max \mathrm{S}_{\mathrm{c}}$
16: return $\mathrm{c}^{\prime}$

Algorithm 2 score_for_tuning (EBICnormalised $\gamma$ )
Input: DAG G, dataset $\mathcal{D}$, configuration c from a list of configurations $\mathbf{C}$
Output: EBIC $_{\text {normalised } \gamma}$
1: If c contains $\gamma$
2: $\quad$ score $=\operatorname{EBIC}_{\text {normalised } \gamma}(\mathrm{G}, \mathcal{D})$
3: Else
4: $\quad$ score $=\operatorname{EBIC}_{\text {normalised } \gamma=0}(\mathrm{G}, \mathcal{D})$

Algorithm 3 score_for_tuning $\left(\mathrm{BDeu}_{\text {iss }}\right)$
Input: DAG G, dataset $\mathcal{D}$, configuration c from a list of configurations $\mathbf{C}$
Output: $\mathrm{BDeu}_{\text {iss }}$
1: If c contains iss
2: $\quad$ score $=\mathrm{BDeu}_{\text {iss }}(\mathrm{G}, \mathcal{D})$
3: Else
4: $\quad$ score $=\mathrm{BDeu}_{\text {iss }=1}(\mathrm{G}, \mathcal{D})$

# 4 Case studies and experimental setup 

We consider 10 real-world BNs whose properties are provided in Table 1. Six of them are taken from the bnlearn [33] and Bayesys [9] repositories and are used to generate synthetic data with sample sizes of 1 k and 10 k . In addition to the six synthetically generated datasets, we also consider four real datasets which we discuss in more detail in Sect. 5.2.

Table 1 The properties of the 10 case studies


Table 2 lists the five structure learning algorithms considered for hyperparameter optimisation, spanning all three classes of structure learning. Because OTSL is designed to optimise either $\mathrm{EBIC}_{\text {normalised } \gamma}$ or $\mathrm{BDeu}_{\text {iss }}$, we follow a somewhat different strategy when optimising constraint-based learning algorithms which do not involve score-based hyperparameters such as iss and $\gamma$. As shown in Table 2, the PC-Stable algorithm is tuned by exploring the three different thresholds for significance test $\alpha$ by maximising either EBIC or BDeu given their hyperparameter defaults; i.e. we iterate over hyperparameter values for $\alpha$-not for iss or $\gamma$-when the input algorithm is constraint-based. Specifically, (a) for constraintbased PC-Stable, we optimise hyperparameter $\alpha$ which represents the statistical significance

Table 2 The algorithms tested for hyperparameter optimisation, along with the set of hyperparameters optimised. Brackets indicate the hyperparameter defaults. The size of the separation-set for CI tests is set to -1 to allow for an unlimited size of conditioning sets


Constraint-based
PC-Stable
$\mathrm{Chi}^{2}, \mathrm{MI}, \mathrm{MI}-\mathrm{sh}$
$0.01,[0.05], 0.1$
$[1]$
Score-based
HC, FGES
$\mathrm{BDeu}_{\text {iss }}, \mathrm{EBIC}_{\gamma}$
$-$
$[0], 1,2, \ldots, 19$
$[1], 2,3, \ldots$,
20
Hybrid-based
MCMC
$\mathrm{Chi}^{2} / \mathrm{BDeu}_{\text {iss }}$
$[0.05]$
$-$
$[1], 2,3, \ldots$,
20
MMHC
$\mathrm{Chi}^{2} / \mathrm{BDeu}_{\text {iss }}$,
$0.01,[0.05]$
$[0], 1,2, \ldots, 9$
$[1], 2,3, \ldots$,
10

threshold for either $\mathrm{Chi}^{2}$, MI, or MI-sh (refer to Sect. 2.1), (b) for score-based HC and FGES, we optimise hyperparameter $\gamma$ in $\mathrm{EBIC}_{\gamma}$ and iss in $\mathrm{BDeu}_{\text {iss }}$ (refer to Sect. 2.2), and (c) for hybrid algorithms MCMC and MMHC, we optimise for all three possible hyperparameters. However, as shown in Table 2, we reduce the size of the set of possible hyperparameters to be explored for hybrid algorithms due to the much larger number of possible combinations of hyperparameters they produce. For example, if we were to explore the same range of hyperparameters for MMHC then that would require 1920 structure learning experiments for that algorithm alone; i.e. 3 hyperparameters for $\alpha \times 20$ for $\gamma$ or 3 hyperparameters for $\alpha \times 20$ for iss for each case study and sample size. Because this study involves adjusting the default hyperparameters to values that optimise a given score or objective function, we also explore how the performance of the algorithms could change if this hyperparameter modification was randomised. The randomisation process involves random hyperparameter assignment across the same hyperparameter ranges investigated, and recording the average score obtained across 10 randomisations per experiment.

We use the F1 and Structural Hamming Distance (SHD) by Tsamardinos et al. [40] graphical metrics to assess synthetic experiments where the ground truth DAG is known. The F1 metric represents the harmonic mean of precision $(P)$ and recall $(R)$ where $\mathrm{F} 1=2 \frac{P R}{P+R}$, and the SHD score represents the number of edge additions, deletions, and reversals needed to convert the learnt DAG into the true DAG. The scores reported in this study reflect comparisons between learnt and true DAGs. If a structure learning algorithm produces a CPDAG, then a random DAG is generated from the learnt CPDAG.

The hyperparameter optimisation performance of OTSL is assessed with reference to other hyperparameter tuning methods that are specifically proposed for tuning structure learning algorithms, and specifically, the StARS and OCT approaches discussed in the introduction. In addition, we also consider the BIC and the Akaike Information Criterion (AIC) [1] modelselection functions as baselines for tuning, consistent with how they are used in other relevant studies for evaluation purposes, where tuning is determined by the hyperparameter value that maximises the given model-selection function [2].

We conduct all experiments by performing 10 iterations of resampling for both OTSL and StARS, and assuming a tenfold cross-validation for OCT. We set a runtime limit of 24 h for each experiment and yet, this was not enough to complete all experiments. Because most tuning experiments failed to complete learning on the real-world Diarrhoea and Weather datasets within the runtime limit, we had to modify the experimental setup for these two datasets. The issue with the Diarrhoea dataset is that it contains a large number of samples $(259,627)$, which we address by modifying the resampling technique such that it creates 10 sets of training data restricted to a sample size of 9 k and 10 sets of test data restricted to a sample size of 1 k , derived from the 259,627 instances of the Diarrhoea dataset. On the other hand, the issue with the Weather dataset is that it contains a large number of variables, and we address this by reducing the number of iterations for resampling to 5 for the Weather dataset.

Experiments with real data provide no access to ground truth. As a result, it is difficult to judge the unsupervised learning performance of these algorithms on real data. Therefore, we use real data to primarily investigate the issues we may face, specifically with large datasets as discussed above, and to illustrate how OTSL influences the structure learning performance of the different algorithms considered, in terms of model-selection, goodness-of-fit, and model dimensionality.

We test PC-Stable, HC, and MMHC using the bnlearn R package [33]. FGES using Tetradbased rcausal R package [42], and MCMC (the order-MCMC version) using the BiDAG R package [39]. The model-selection scores of BIC and AIC, as well as the StARS and OCT

tuning algorithms are tested using the MATLAB implementations available at: https://github. com/mensxmachina/OCT. The implementation of OTSL is made available online at https:// github.com/kiattikunc/OTSL. All experiments were conducted on a High-Performance Computing (HPC) cluster with 32 GBs of RAM, whereas the experiments involving the FGES algorithm were ran on a laptop with an M1 CPU at 3.2 GHz and 8 GB of RAM due to compatibility issues with the HPC cluster.

Overall, this study has carried out 7736 structure learning experiments across the 10 case studies specified in Table 1, two sample sizes ( 1 k and 10 k samples), five structure learning algorithms (PC-Stable, HC, MMHC, MCMC, and FGES), five hyperparameter tuning approaches (AIC, BIC, OTSL, StARS, and OCT), with three hyperparameter baseline settings specified in Sect. 5.1.1 (Default $A$, Default $B$, and randomised), and five objective scores or statistical tests for optimisation shown in Table $2\left(\mathrm{Chi}^{2}, \mathrm{MI}, \mathrm{Mi}-\mathrm{sh}, \mathrm{EBIC}_{\gamma}\right.$, and $\left.\mathrm{BDeu}_{\text {iss }}\right)$.

# 5 Empirical results 

### 5.1 Results based on synthetic data

### 5.1.1 Impact of hyperparameter tuning on graphical structure

In addition to randomising hyperparameter values, the baseline comparisons include two different cases for hyperparameter defaults: (a) Default $A$ where $\alpha=0.05$ for $\mathrm{Chi}^{2}$ test and $\gamma=0$ for $\mathrm{EBIC}_{\gamma}$, and (b) Default $B$ where and $\alpha=0.05$ for $\mathrm{Chi}^{2}$ test and iss $=1$ for $\mathrm{BDeu}_{\text {iss }}$. Figure 2 compares the F1 scores obtained by the four specified algorithms across all synthetic
![img-1.jpeg](img-1.jpeg)

Fig. 2 The average F1 scores with and without hyperparameter tuning. Untuned algorithms assume Default A configuration and tuned algorithms assume OTSL with $\mathrm{EBIC}_{\text {normalised }}$ as the tuning score. The average scores are derived over four structure learning algorithms (excluding MCMC that does not support $\mathrm{EBIC}_{\gamma}$ ) and six synthetic case studies. The boxplots represent the highest and lowest F1 scores with outliers, $\times$ is the mean, and - is the median. The lower edge of the boxplot represents the first (lower) quartile, while the higher edge of the boxplot represents the third (upper) quartile. Figure a depicts the scores for datasets with sample size 1 k and $\mathbf{b}$ with sample size 10 k

experiments, with and without (i.e. Default A) hyperparameter optimisation. These default hyperparameters reflect the typical scenarios in the literature where structure learning algorithms are applied as implemented in the relevant libraries, without hyperparameter tuning. It is noted that most previous studies tend to utilise these algorithms with their default settings as provided in existing libraries, partly because these hyperparameter defaults are known to be generally effective, and partly due to the lack of guidance on selecting or optimising these hyperparameters values for structure learning. In this set of experiments, hyperparameter optimisation is restricted to $\mathrm{EBIC}_{\text {normalised } \gamma}$, and hence, the MCMC algorithm is not included in these results since $\mathrm{EBIC}_{\gamma}$ is not available in the BiDAG R package. Figure 2a depicts the results when trained with datasets of sample size 1 k , whereas Fig. 2b depicts the results when trained with datasets of sample size 10 k .

Across the 12 comparisons shown in both Fig. 2a and b, the results show that the hyperparameter tuning applied by OTSL improves the average F1 scores in nine cases, and slightly decreases performance in three cases; i.e. for Property at both 1 k and 10 k sample sizes and for Sports at 10 k sample size. In Fig. 2a, the average F1 score across all DAGs learnt over the six cases and four structure learning algorithms is 0.448 for default configurations, and increases (improves) to 0.458 (or by $\sim 2.3 \%$ ) when tuning the hyperparameters of $\mathrm{EBIC}_{\text {normalised } \gamma}$. Figure 2b repeats these experiments for sample sizes 10 k and shows that the results remain consistent with those obtained when the sample size is set to 1 k . Specifically, the average F1 score across all DAGs is 0.5 for the default configurations and increases to 0.513 (or by $\sim 2.5 \%$ ) when tuned with OTSL.

Figure 3a and b repeat the experiments of Fig. 2a and b, and use $\mathrm{BDeu}_{\text {iss }}$ as the tuning score instead of $\mathrm{EBIC}_{\text {normalised } \gamma}$. In this case, however, the results show that the hyperparameter tuning applied by OTSL did not improve the average F1 scores. Specifically, the average F1
![img-2.jpeg](img-2.jpeg)

Fig. 3 The average F1 scores with and without hyperparameter tuning. Untuned algorithms assume Default B configuration and tuned algorithms assume OTSL with $\mathrm{BDeu}_{\text {iss }}$ as the tuning score. The average scores are derived over five structure learning algorithms and six synthetic case studies. The boxplots represent the highest and lowest F1 scores with outliers, $\times$ is the mean, and - is the median. The lower edge of the boxplot represents the first quartile, while the higher edge of the boxplot represents the third quartile. Figure a depicts the scores for datasets with sample size 1 k and $\mathbf{b}$ with sample size 10 k

Table 3 The change in average F1 and SHD scores for each algorithm, after randomising their hyperparameters and after tuning them with OTSL. The average score is derived from all six synthetic case studies and both 1 k and 10 k sample sizes. The hyperparameter defaults are $\alpha=0.05$ for $\mathrm{Chi}^{2}$ test and $\gamma=0$ for $\mathrm{EBIC}_{\gamma}$ (Default A). The values highlighted in green indicate an increase (improvement) in the F1 score or a decrease (improvement) in the SHD score, and the best performance values are shown in bold


scores for the default configurations (Default B) are 0.51 and 0.56 for sample sizes 1 k and 10 k , respectively, and 0.506 and 0.56 , respectively, when tuned with OTSL.

Table 3 details the average change in F1 and SHD scores for each structure learning algorithm, when we randomise their hyperparameters or tune them with OTSL, relative to the hyperparameter default configurations (Default A). The average change depicted in Table 3 is derived across all six case studies, and over both 1 k and 10 k sample sizes per case study. The positive scores indicate a percentage increase (improvement) in the F1 score or a percentage decrease (improvement) in the SHD score, while the negative scores indicate a percentage decrease (worsening) in the F1 score or a percentage increase (worsening) in the SHD score. The results depicted in Table 3 show that randomising the hyperparameters leads to an average worsening of $1.71 \%$ in F1 score and an average worsening of $4.89 \%$ in SHD score, relative to the results obtained when assuming hyperparameter defaults. On the other hand, the F1 score improves by $3.9 \%$ and the SHD score improves by $6.12 \%$, respectively, when optimising the hyperparameters using OTSL. However, the constraint-based PC-Stable generates poor tuning performance with the F1 score worsens by $1.81 \%$ and the SHD score worsening by $1.08 \%$. This might suggest that the score-based tuning applied by OTSL to tune constraint-based CI tests might not be appropriate.

Table 4 repeats the experiments but assumes Default $B$ configurations, and that the tuning score is $\mathrm{BDeu}_{\text {iss }}$ instead of $\mathrm{EBIC}_{\text {normalised } \gamma}$ assumed in Table 3. In this case, the results show that both randomising and optimising the hyperparameter iss of $\mathrm{BDeu}_{\text {iss }}$ worsen graphical scores relative to those obtained by assuming hyperparameter defaults. In other words, it seems that assuming iss $=1$ for $\mathrm{BDeu}_{\text {iss }}$ produces strong performance with little, if any, room for improvement via hyperparameter tuning, and this is consistent with what is reported by Steck [38] and Uneo [41] who recommend to set iss $=1$, especially when the distributions of the variables are assumed to be skewed or when the true underlying structure is assumed to be sparse. Our results show that randomising the iss hyperparameter of $\mathrm{BDeu}_{\text {iss }}$ worsens the F1 score by $4.86 \%$ and worsens the SHD score by $11.02 \%$, whereas optimising iss with OTSL improves the F1 scores by $0.12 \%$ and worsens the SHD scores by $3.36 \%$. These results suggest that the $\mathrm{BDeu}_{\text {iss }}$ function may not be suitable for tuning, at least compared to $\mathrm{EBIC}_{\text {normalised } \gamma}$, and that setting iss $=1$ might indeed be sufficient, in general.

Table 4 The change in average F1 and SHD scores for each algorithm, after randomising their hyperparameters and after tuning them with OTSL. The average score is derived from all six synthetic case studies and both 1 k and 10 k sample sizes. The hyperparameter defaults are $\alpha=0.05$ for $\mathrm{Chi}^{2}$ test and $\gamma=0$ for $\mathrm{BDeu}_{\text {ISS }}$ (Default B). The values highlighted in green indicate an increase (improvement) in the F1 score or a decrease (improvement) in the SHD score, and the best performance values are shown in bold


# 5.1.2 Assessing OTSL relative to existing tuning algorithms for structure learning 

We compare the results of OTSL with those obtained by the out-of-sample tuning OCT and the in-sample tuning StARS. We also consider the baseline tuning results obtained by the modelselection scores BIC and AIC. This process involves applying the other four approaches to the same experiments presented in Sect. 5.1.1 and comparing the changes to the F1 and SHD scores across all hyperparameter tuning approaches.

Tables 5 and 6 summarise these results for both Default $A$ and Default $B$ hyperparameter configurations, respectively. Table 5 shows that while none of the hyperparameter tuning approaches improves the graphical accuracy for all four structure learning algorithms, most of the approaches do improve the average structure learning performance across all algorithms. Specifically, all five tuning approaches improve the average F1 score across the four structure learning algorithms considered, although only three out of the five tuning approaches also improve the SHD score. The OTSL algorithm with $\mathrm{EBIC}_{\text {normalisedy }}$ tuning improves the F1 (up by $3.9 \%$ ) score and improves the SHD score (up by $6.12 \%$ ) scores the most across all the tuning approaches considered. Interestingly, the F1 and SHD scores provide contradictory conclusions about the impact on graphical structure for OCT and StARS algorithms, and this inconsistency between the F1 and SHD metrics is in agreement with other studies [10].

Table 5 The average change in F1 and SHD scores due to hyperparameter tuning by the specified tuning method. The averages are derived from all six synthetic case studies and over both sample sizes. The structure learning algorithms assume Default $A$ hyperparameter configuration ( $\mathrm{Chi}^{2}$ test with $\alpha=0.05$, and $\mathrm{EBIC}_{\gamma}$ with $\gamma=0$ ). The values highlighted in green indicate an increase (improvement) in the F1 score or a decrease (improvement) in the SHD score, and the highest improvements in graphical accuracy are shown in bold


Table 6 The average change in F1 and SHD scores due to hyperparameter tuning by the specified tuning method. The averages are derived from all six synthetic case studies and over both sample sizes. The structure learning algorithms assume Default $B$ hyperparameter configuration $\left(\mathrm{Chi}^{2}\right.$ test with $\alpha=0.05$, and $\mathrm{BDeu}_{\text {iss }}$ with iss $=1$ ). The values highlighted in green indicate an increase (improvement) in the F1 score or a decrease (improvement) in the SHD score, and the highest improvements in graphical accuracy are shown in bold


For example, the F1 metric suggests that the hyperparameter tuning of OCT improves the structure learning performance of all four structure learning algorithms, whereas the SHD metric suggests that OCT worsens the graphical accuracy of three out of the four structure learning algorithms.

Table 6 presents the same results when the hyperparameter tuning approaches are applied to the iss hyperparameter of $\mathrm{BDeu}_{\text {iss }}$. Overall, the results are consistent with those presented in Tables 3 and 4, in that hyperparameter tuning appears to be successful for $\mathrm{EBIC}_{\text {normalisedy }}$ but not for $\mathrm{BDeu}_{\text {iss }}$. While tuning with $\mathrm{BDeu}_{\text {iss }}$ is found to be rather inadequate for all tuning methods, OTSL is found to perform considerably better compared to the other tuning approaches with an improvement of $0.12 \%$ in the average F1 score (improved the scores of four out of the five algorithms) and a worsening of $3.36 \%$ in the average SHD score (improved the scores of three out of the five algorithms).

We also assess the computational complexity of OTSL by comparing its hyperparameter tuning and overall structure learning runtimes against those produced by the other hyperparameter tuning approaches. Provisional results show that the runtimes are similar for both $\mathrm{EBIC}_{\text {normalisedy }}$ and $\mathrm{BDeu}_{\text {iss }}$, but here we focus on $\mathrm{EBIC}_{\text {normalisedy }}$ which produces the best tuning performance. Figure 4a depicts the total runtimes (hyperparameter tuning and structure learning) across all six case studies, two sample sizes, and five structure learning algorithms, whereas Fig. 4b shows the runtime for the same experiments but restricted to the hyperparameter tuning phase. As expected, optimisation with model-selection functions such as BIC and AIC results in very low runtimes, since they do not involve out-of-sample or resampling strategies, whereas OTSL, OCT, and StARS perform 10 iterations of either in-sample or out-of-sample tuning for each hyperparameter configuration, and hence, they produce considerably higher runtimes. Overall, the results in Fig. 4a show that the computational runtime of OTSL is similar to that of StARS, and considerably faster than that of OCT. Importantly, the tuning runtimes of OTSL and StARS represent just $0.2 \%$ and $0.4 \%$ of the total structure learning runtime, respectively, whereas the tuning runtime of OCT represents $43 \%$ of its total structure learning runtime. Figure 4 b shows that the tuning runtime of OTSL is slower than the tuning runtime of StARS, but much faster than the tuning runtime of OCT.

![img-3.jpeg](img-3.jpeg)

Fig. 4 a Overall runtime (structure learning and tuning) and $\mathbf{b}$ tuning runtime, summed over all six synthetic datasets and two sample sizes, across all five structure learning algorithms

# 5.2 Applying OTSL to real data 

While previous subsections focused on evaluating OSTL in terms of how its tuning improves the recovery of the ground truth graphs that were used to generate synthetic data, this subsection illustrates how OTSL could be used in practice with application to four different real datasets that come from different disciplines. As discussed in Sect. 3, real data do not come with an access to ground truth, and hence, the purpose here is to illustrate how tuning influences the structure learning performance of the different algorithms considered when applied to real data. We consider the following four discrete datasets, where the first three are obtained from the Bayesys repository [9] and the fourth from the National Center for Environmental Prediction (NCEP) and the National Center for Atmospheric Research (NCAR) in the USA, known as the NCEP/NCAR Reanalysis Project [21]:
a) ForMed A case study on assessing and managing the risk of violence in released prisoners with history of violence and mental health $[6,8]$. The data were collected through interviews and assessments comprising risk factors for 953 individual cases. The dataset contains a total of 56 categorical variables.
b) COVID-19 A dataset that captures pandemic data about the COVID-19 outbreak in the UK [12]. The data comprise of 18 variables that capture information related to viral tests, infections, hospitalisations, vaccinations, deaths, COVID-19 variants, population mobility such as usage of transportation, schools, and restaurants, as well as various government policies such as facemasks and lockdowns. The data instances represent daily information, spanning from 30 January 2020, to 13 June 2022, resulting in a total of 866 instances.
c) Diarrhoea Survey data collated and pre-processed from the Demographic and Health Survey (DHS) programme, which was used to investigate the factors associated with childhood diarrhoea in India [22]. The dataset captures relevant cases from 2015 to 2016 and contains 28 variables and 259,627 instances.
d) Weather A dataset that captures the monthly means of air temperature and other climatological data for each location as measured by latitude (y coordinate) and longitude (x

coordinate) over the global grid system [21]. The dataset merges information obtained from multiple sources, i.e. balloons, satellites, and buoys. It provides a comprehensive 75 years record from 1948 to 2022 of global atmospheric field analyses. We used the bnlearn R package (2019) to discretise the dataset. Because the raw data are too big for our experiments, we also resized the spatial dataset from 2.5 degree $\times 2.5$ degree global grids to 10 degree $\times 10$ degree global grids and reduced the total number of variables from $10,512(144 \times 73)$ to $648(36 \times 18)$. Therefore, the dataset used in this study contains a total of 648 variables and 900 instances.
We apply the structure learning algorithms to each of the four datasets and tune their hyperparameters using OTSL. We only consider Default A hyperparameter configuration with $\mathrm{EBIC}_{\text {normalised } \gamma}$ for tuning, which was shown to be more suitable for hyperparameter optimisation. Table 7 presents the results obtained by applying the specified structure learning algorithms to the ForMed dataset and tuning their hyperparameters with OTSL. We report the model-selection score BIC, the goodness-of-fit score LL, the number of free parameters as a measure of model dimensionality, and the tuning scores $\mathrm{EBIC}_{\text {normalised } \gamma}$. Table 7 shows that out of the four structure learning algorithms considered, only one ( HC with $\gamma=2$ ) had its hyperparameter changed following tuning with OTSL. The tuning scores $\mathrm{EBIC}_{\text {normalised } \gamma}$ in Table 7 suggest that the graph produced by MMHC, presented in Fig. 5, might be the 'best' structure to consider amongst those learnt by the different algorithms, although this suggestion contradicts the BIC score which suggests that the best structure may be the one learnt by HC.

Tables 8, 9, and 10, and corresponding Figs. 6, 7, and 8, repeat the above analyses for case studies COVID-19, Diarrhoea, and Weather, respectively. Note that only two algorithms are reported for the Weather case study, and this is because HC did not complete learning within the 24 -h time limit, while FGES returned a memory allocation error. The results show that OTSL modified the hyperparameters of three and four, out of the four, structure learning algorithms in COVID-19 and Diarrhoea cases, respectively, and for one out of the two algorithms for dataset Weather. Table 8 shows that FGES produces the best structure for the COVID-19 case study (see Fig. 6) according to both $\mathrm{EBIC}_{\text {normalised } \gamma}$ and BIC scores. On the other hand, the results in Table 9 suggest that the graph produced by FGES is the best structure according to $\mathrm{EBIC}_{\text {normalised } \gamma}$, which once more contradicts the BIC score that scores the graph produced by HC the highest. Lastly, in Table 10, both $\mathrm{EBIC}_{\text {normalised } \gamma}$ and BIC are in agreement that MMHC produced the best structure shown in Fig. 8. The nodes in Fig. 8 represent random variables of a monthly temperature for each location, whereas the arcs represent the spatial dependencies of surface temperatures for each grid. ${ }^{1}$

# 6 Conclusions and future work 

Learning causal models from observational data remains a major challenge. Traditionally, structure learning algorithms are evaluated and applied to real data with their hyperparameter defaults, or by iterating over a small set of possible hyperparameters. However, no specific set of hyperparameters is optimal for all input datasets which vary in sample size and dimensionality, and structure learning algorithms which vary in learning strategy. Therefore, the

[^0]
[^0]:    ${ }^{1}$ The orange arcs represent short-distance temperature dependencies, while the red arcs show the teleconnected dependencies. We observe that the local short-distance arcs are dense, representing atmospheric thermodynamic processes, while the teleconnected dependencies are represented by only three arcs. One of these teleconnected dependencies indicates the El Niño effects, which are caused by temperatures along the equator in the Pacific Ocean (Yamasaki et al., 2008).

Table 7 The tuning, model-selection, goodness-of-fit, and dimensionality scores of the graphs learnt by the specified structure learning algorithms when applied to the ForMed dataset, with OTSL tuning


The best performance values are shown in bold

![img-4.jpeg](img-4.jpeg)

Fig. 5 The DAG learnt by MMHC for the ForMed dataset with OTSL tuning (Table 7)
question of which hyperparameter values might be best for a given structure learning algorithm and input dataset combination remains an open question.

In this study, we propose and evaluate a hyperparameter tuning algorithm, called OTSL, that employs out-of-sample resampling and score-based tuning to find the optimal hyperparameters for a given structure learning algorithm, given the input data. We describe and implement OTSL with a focus on score-based learning, and determine the hyperparameters of different algorithms by optimising either the iss or $\gamma$ hyperparameters of $\mathrm{BDeu}_{\text {iss }}$ and $\mathrm{EBIC}_{\text {normalised }_{\gamma}}$ objective scores.

Synthetic experiments show that tuning with OTSL leads to reasonable improvements in structure learning in terms of the F1 and SHD scores, and when assuming $\mathrm{EBIC}_{\gamma}$ as the objective score for score-based learning. However, this level of improvement is not repeated

Table 8 The tuning, model-selection, goodness-of-fit, and dimensionality scores of the graphs learnt by the specified structure learning algorithms when applied to the COVID-19 dataset, with OTSL tuning


The best performance values are shown in bold

Table 9 The tuning, model-selection, goodness-of-fit, and dimensionality scores of the graphs learnt by the specified structure learning algorithms when applied to the Diarrhoea dataset, with OTSL tuning


The best performance values are shown in bold

Table 10 The tuning, model-selection, goodness-of-fit, and dimensionality scores of the graphs learnt by the specified structure learning algorithms when applied to the Weather dataset, with OTSL tuning


The best performance values are shown in bold

![img-5.jpeg](img-5.jpeg)

Fig. 6 The DAG (sampled from the learnt CPDAG) learnt by FGES for the COVID-19 dataset with OTSL tuning (Table 8)
for $\mathrm{BDeu}_{\text {iss }}$, and this observation is consistent for OTSL, and all the other tuning approaches investigated in this study. This is because the hyperparameter default of iss $=1$ in $\mathrm{BDeu}_{\text {iss }}$ tends to improve F1 and SHD scores compared to the graphs learnt when iss $>1$ (and hence benefits little, if any, from hyperparameter tuning), and this observation is consistent with the past studies [38], Uneo [41].

The performance of OTSL's tuning is assessed by comparing it to two baseline settings; default hyperparameters and randomised hyperparameters, and by comparing it to the state-of-the-art hyperparameter tuning approaches that are proposed for structure learning. We have considered the OCT and StARS tuning approaches, as well as the BIC and AIC modelselection scores that serve as baselines for tuning hyperparameters. Overall, the results show that OTSL provides better tuning performance from results derived across different structure learning algorithms, case studies, and sample sizes. In terms of computational complexity, OTSL was found to be more efficient than OCT but slightly less efficient than StARS.

We note that hyperparameter tuning does not always lead to improvements in causal discovery as measured by graphical scores, such as the F1 score. This phenomenon can be attributed to the fact that hyperparameter tuning optimises a specific score or objective function that estimates the underlying structure, and not the actual graphical scores which remain unknown in practice due to the absence of ground truth. As a result, a higher objective score does not necessarily imply a higher graphical score, leading to situations where optimal hyperparameters might decrease, instead of increase, graphical scores like F1. This observation is consistent with the previous studies that highlight the effectiveness of default hyperparameters, which are designed to ensure broad applicability and balanced performance, thus making the algorithms robust across a variety of datasets. However, despite the strong baseline provided by default settings, hyperparameter tuning may be necessary to achieve optimal performance in certain specific scenarios or with unique datasets.

A limitation is that while OTSL can be applied to structure learning algorithms that come from different classes of learning, it is designed with score-based learning in mind and assumes that the optimal hyperparameters are those that maximise either the $\mathrm{EBIC}_{\text {normalisedy }}$ or $\mathrm{BDeu}_{\text {iss }}$ objective scores, and this also applies when tuning CI functions in constraint-based learning. This might explain why the results from tuning score-based learning algorithms are better that those derived from tuning constraint-based learning. Another limitation is that, because OTSL optimises hyperparameters on test data, this process involves resampling multiple training and test datasets from a single input dataset, which impacts the computational efficiency of structure learning; a learning process that is already known to be computationally expensive.

![img-6.jpeg](img-6.jpeg)

Fig. 7 The DAG (sampled from the learnt CPDAG) learnt by FGES for the Diarrhoea dataset with OTSL tuning (Table 9)

![img-7.jpeg](img-7.jpeg)

Fig. 8 The DAG learnt by MMHC for the Weather dataset with OTSL tuning (Table 10). The vertices of the world map superimposed over the DAG represent latitude and longitude locations on $10 \times 10$ degree grids

Acknowledgements This research was supported by the Royal Thai Government Scholarship offered by Thailand's Office of Civil Service Commission (OCSC).

Author contributions Kiattikun Chobtham takes on the role of the primary author, contributing to conceptualisation, methodology, experiments, and writing. All authors reviewed the manuscript.

# Declarations 

Conflict of interest The authors declare no competing interests.
Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
