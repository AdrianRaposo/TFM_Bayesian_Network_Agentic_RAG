# Interpretable Selection and Visualization of Features and Interactions Using Bayesian Forests 

Viktoriya Krakovna<br>VKRAKOVNA@FAS.HARVARD.EDU<br>Department of Statistics, Harvard University, Cambridge, MA 02138<br>Jiong Du<br>Haitong Securities<br>Jun S. Liu<br>JLIU@STAT.HARVARD.EDU<br>Department of Statistics, Harvard University, Cambridge, MA 02138


#### Abstract

It is becoming increasingly important for machine learning methods to make predictions that are interpretable as well as accurate. In many practical applications, it is of interest which features and feature interactions are relevant to the prediction task. We present a novel method, Selective Bayesian Forest Classifier, that strikes a balance between predictive power and interpretability by simultaneously performing classification, feature selection, feature interaction detection and visualization. It builds parsimonious yet flexible models using tree-structured Bayesian networks, and samples an ensemble of such models using Markov chain Monte Carlo. We build in feature selection by dividing the trees into two groups according to their relevance to the outcome of interest. Our method performs competitively on classification and feature selection benchmarks in low and high dimensions, and includes a visualization tool that provides insight into relevant features and interactions.


## 1. Introduction

Feature selection and classification are key objectives in machine learning that are usually tackled separately. However, performing classification on its own tends to produce black box solutions that are difficult to interpret, while performing feature selection alone can be difficult to justify without being validated by prediction. In addition to screening for relevant features, it is also useful to detect interactions between them. In many decision support systems, e.g. in medical diagnostics, the users care about which features and interactions contributed to a particular decision made by the system. Selective Bayesian Forest Classifier (SBFC) combines predictive power and interpretability by performing classification, feature selection, and feature interaction detection at the same time. Our
![img-0.jpeg](img-0.jpeg)

Figure 1: Example of a SBFC graph
method also provides a visual representation of the relevance of different features and feature interactions to the outcome of interest.

The main idea of SBFC is to construct an ensemble of Bayesian networks [Pearl, 1988], each constrained to a forest of trees divided into signal and noise groups based on their relationship with the class label $Y$ (see Figure 1 for an example). The nodes and edges in Group 1 represent relevant features and interactions. Such models are easy to sample using Markov chain Monte Carlo (MCMC). We combine their predictions using Bayesian model averaging, and aggregate their feature and interaction selection.

We show that SBFC performs competitively with state-of-the-art methods on 25 low-dimensional and 6 highdimensional benchmark data sets. By adding noise features to a synthetic data set, we compare feature selection and interaction detection performance as the signal to noise ratio decreases (Figure 5). We use a high-dimensional data set from the NIPS 2003 feature selection challenge to demonstrate SBFC's superior performance on a difficult feature selection task (Figure 6), and illustrate the visualization tool on a heart disease data set with meaningful features (Figure 4). SBFC is a good choice of algorithm for applications where interpretability matters along with predictive power (an R package is available at github.org/vkrakovna/sbfc).

## 2. Related Work

Tree structures are frequently used in computer science and statistics, because they provide adequate flexibility to model complex structures, yet are constrained enough to facilitate computation. SBFC was inspired by tree-based methods such as Tree-Augmented Naïve Bayes (TAN) [Friedman et al., 1997] and Averaged One-Dependence Estimators (AODE) [Webb et al., 2005]. TAN finds the optimal tree on all the features using the minimum spanning tree algorithm, with the class label $Y$ as a second parent for all the features. While the search for the best unrestricted Bayesian network is usually an intractable task [Heckerman et al., 1995], the computational complexity of TAN is only $O\left(d^{2} n\right)$, where $d$ is the number of features and $n$ is the sample size [Chow \& Liu, 1968]. AODE constrains the model structure to a tree where all the features are children of the root feature, with $Y$ as a second parent, and uses model averaging over model with all possible root features. These methods put all the features into a single tree, which can be difficult to interpret, especially for high-dimensional data sets. We extend on TAN and AODE by building forests instead of single-tree graphs, and introducing selection of relevant features and interactions.

Feature selection is often used as a preprocessing step for classification algorithms. Wrapper methods [Kohavi \& John, 1997] select a subset of features tailored for a specific classifier, treating it as a black box. Variable Selection for Clustering and Classification (VSCC) [Andrews \& McNicholas, 2014] searches for a feature subset that simultaneously minimizes the within-class variance and maximizes the between-class variance, and remains efficient in high dimensions. Categorical Adaptive Tube Covariate Hunting (CATCH) [Tang et al., 2014] selects features based on a nonparametric measure of the relational strength between the feature and the class label.

Our approach, however, is to integrate feature selection into the classification algorithm itself, allowing it to influence the models built for classification. A classical example is Lasso [Tibshirani, 1996], which performs feature selection using $L_{1}$ regularization. Some decision tree classifiers, like Random Forest [Breiman, 2001] and BART [Chipman et al., 2010], provide importance measures for features and the option to drop the least significant features. In many applications, it is also key to identify relevant feature interactions, such as epistatic effects in genetics. Interaction detection methods for gene association models include Graphical Gaussian models [Andrei \& Kendziorski, 2009] and Bayesian Epistasis Association Mapping (BEAM) [Zhang \& Liu, 2007]. BEAM introduces a latent indicator that partitions the features into several groups based on their relationship with the class label. One of the groups in BEAM is designed to capture relevant
feature interactions, but is only able to tractably model a small number of them. SBFC extends this framework, using tree structures to represent an unlimited number of relevant feature interactions.

## 3. Selective Bayesian Forest Classifier (SBFC)

### 3.1. Model

Given $n$ observations with class label $Y$ and $d$ discrete features $X_{j}, j=1, \ldots, d$, we divide the features into two groups based on their relation to $Y$ :

Group 0 (noise): features that are unrelated to $Y$
Group 1 (signal): features that are related to $Y$
We further partition each group into non-overlapping subgroups mutually independent of each other conditional on $Y$. For each subgroup, we infer a tree structure describing the dependence relationships between the features (many subgroups will consist of one node and thus have a trivial dependence structure). Note that we model the structure in the noise group as well as the signal group, since an independence assumption for the noise features could result in correlated noise features being misclassified as signal features.

The overall dependence structure is thus modeled as a forest of trees, representing conditional dependencies between the features (no causal relationships are inferred). The class label $Y$ is a parent of every feature in Group 1 (edges to $Y$ are omitted in subsequent figures). We will refer to the combination of a group partition and a forest structure as a graph.

The prior consists of a penalty on the number of edges between features in each group and a penalty on the number of signal nodes (i.e., edges between features and $Y$ )

$$
P(G) \propto d^{-4\left(E_{0}(G)+E_{1}(G) / v\right)-D_{1}(G) / v}
$$

where $D_{i}(G)$ is the number of nodes and $E_{i}(G)$ is the number of edges in Group $i$ of graph $G$, while $v$ is a constant equal to the number of classes.

The prior scales with $d$, the number of features, to penalize very large, hard-to-interpret trees in high dimensional cases. The terms corresponding to the signal group are divided by $v$, the number of possible classes, to avoid penalizing large trees in the signal group more than in the noise group by default. The coefficients in the prior were found in practice to provide good classification and feature selection performance (there is a relatively wide range of coefficients that produce similar results).

Given the training data $X_{(n \times d)}$ (with columns $\boldsymbol{X}_{j}, j=$ $1, \ldots, d$ ) and $\boldsymbol{y}_{(n \times 1)}$, we break down the graph likelihood

Table 1: Parent sets for each feature type


according to the tree structure:

$$
\begin{aligned}
P(X, \boldsymbol{y} \mid G) & =P(\boldsymbol{y} \mid G) P(X \mid \boldsymbol{y}, G) \\
& =P(\boldsymbol{y}) \prod_{j=1}^{d} P\left(\boldsymbol{X}_{j} \mid \boldsymbol{\Lambda}_{j}\right)
\end{aligned}
$$

Here, $\Lambda_{j}$ is the set of parents of $X_{j}$ in graph $G$. This set includes the parent $X_{p_{j}}$ of $X_{j}$ unless $X_{j}$ is a root, and $Y$ if $X_{j}$ is in Group 1, as shown in Table 1. We assume that the distributions of the class label $Y$ and the graph structure $G$ are independent a priori.

Let $v_{j}$ and $w_{j}$ be the number of possible values for $X_{j}$ and $\Lambda_{j}$ respectively. Then our hierarchical model for $X_{j}$ is

$$
\begin{aligned}
{\left[X_{j} \mid \Lambda_{j}=\Lambda_{j l}, \boldsymbol{\Theta}_{j l}=\boldsymbol{\theta}_{j l}\right] } & \sim \operatorname{Mult}\left(\boldsymbol{\theta}_{j l}\right), l=1, \ldots, w_{j} \\
\boldsymbol{\Theta}_{j l} & \sim \operatorname{Dirichlet}\left(\frac{\alpha}{w_{j} v_{j}} \mathbf{1}_{v_{j}}\right)
\end{aligned}
$$

Each conditional Multinomial model has a different parameter vector $\boldsymbol{\Theta}_{j l}$. We consider the Dirichlet hyperparameters to represent "pseudo-counts" in each conditional model [Friedman et al., 1997]. Let $n_{j k l}$ be the number of observations in the training data with $X_{j}=x_{j k}$ and $\Lambda_{j}=\Lambda_{j l}$, and $n_{j l}=\sum_{k=1}^{v_{j}} n_{j k l}$. Then

$$
P\left(\boldsymbol{X}_{j} \mid \boldsymbol{\Lambda}_{j}, \boldsymbol{\Theta}_{j 1}, \ldots, \boldsymbol{\Theta}_{j w_{j}}\right)=\prod_{l=1}^{w_{j}} \prod_{k=1}^{v_{j}} \theta_{j k l}^{n_{j k l}}
$$

We then integrate out the nuisance parameters $\boldsymbol{\Theta}_{j l}, l=$ $1, \ldots, w_{j}$. The resulting likelihood depends only on the hyperparameter $\alpha$ and the counts of observations for each combination of values of $X_{j}$ and $\Lambda_{j}$.

$$
P\left(\boldsymbol{X}_{j} \mid \boldsymbol{\Lambda}_{j}\right)=\prod_{l=1}^{w_{j}} \frac{\Gamma\left(\frac{\alpha}{w_{j}}\right)}{\Gamma\left(\frac{\alpha}{w_{j}}+n_{j l}\right)} \prod_{k=1}^{v_{j}} \frac{\Gamma\left(\frac{\alpha}{w_{j} v_{j}}+n_{j k l}\right)}{\Gamma\left(\frac{\alpha}{w_{j} v_{j}}\right)}
$$

This is the Bayesian Dirichlet score, which satisfies likelihood equivalence [Heckerman et al., 1995]. Namely, reparametrizations of the model that do not affect the conditional independence relationships between the features, for example by pivoting a tree to a different root, do not change the likelihood.
![img-1.jpeg](img-1.jpeg)
(a) Switch Trees: switch tree $\left\{X_{5}, X_{7}\right\}$ to Group 0 , switch tree $\left\{X_{8}\right\}$ to Group 1
![img-2.jpeg](img-2.jpeg)
(b) Reassign Subtree: reassign node $X_{6}$ to be a child of node $X_{8}$
![img-3.jpeg](img-3.jpeg)
(c) Pivot Trees: nodes $X_{6}$ and $X_{10}$ become tree roots

Figure 2: Example MCMC updates applied to the graph in Figure 1

### 3.2. MCMC Updates

Switch Trees: Randomly choose trees $T_{1}, \ldots, T_{k}$ without replacement (we use $k=10$, and propose switching each tree to the opposite group one by one (see Figure 2a). This is a repeated Metropolis update.

Reassign Subtree: Randomly choose a node $X_{j}$, detach the subtree rooted at this node and choose a different parent node for this subtree (see Figure 2b). This is a Gibbs update, so it is always accepted.

We consider the set of nodes $X_{j^{\prime}}$ that are not descendants of $X_{j}$ as candidate parent nodes (to avoid creating a cycle), with corresponding graphs $G_{j^{\prime}}$. We also consider a "null parent" option for each group, where $X_{j}$ becomes a root in that group, with corresponding graph $\tilde{G}_{i}$ for group $i$. Choose a graph $G^{*}$ from this set according to the conditional posterior distribution $\pi\left(G^{*}\right)$ (conditioning on the parents of all the nodes except $X_{j}$, and on the group membership of all the nodes outside the subtree). The subtree joins the group of its new parent.

As a special case, this results in a tree merge if $X_{j}$ was a root node, or a tree split if $X_{j}$ becomes a root (i.e.

the new parent is null). Note that the new parent can be the original parent, in which case the graph does not change.

Pivot Trees: Pivot all the trees by randomly choosing a new root for each tree (see Figure 2c). By likelihood equivalence, this update is always accepted.
For computational efficiency, in practice we don't pivot all the trees at each iteration. Instead, we just pivot the tree containing the chosen node $X_{j}$ within each Reassign Subtree move, since this is the only time the parametrization of a tree matters. This implementation produces an equivalent sampling mechanism.

Table 2: Data set properties [Friedman et al., 1997]


### 3.3. Classification Using Bayesian Model Averaging

Graphs are sampled from the posterior distribution using the MCMC algorithm. We apply Bayesian model averaging [Hoeting et al., 1998] rather than using the posterior mode for classification. For each possible class, we average the probabilities over a thinned subset of the sampled

Table 3: SBFC runtime on high-dimensional data sets in minutes


graph structures, and then choose the class label with the highest average probability. Given a test data point $\boldsymbol{x}^{\text {test }}$, we find

$$
\begin{aligned}
& P(Y=y \mid \boldsymbol{X}=\boldsymbol{x}^{\text {test }}, X, \boldsymbol{y}) \\
\propto & \sum_{i=1}^{S} P(Y=y \mid \boldsymbol{X}=\boldsymbol{x}^{\text {test }}, G_{i}) P\left(G_{i} \mid X, \boldsymbol{y}\right)
\end{aligned}
$$

where $S$ is the number of graphs sampled by MCMC (after thinning by a factor of 50). We use training data counts to compute the posterior probability of the class label given each sampled graph $G_{i}$.

## 4. Experiments

We compare our classification performance with the following methods.

BART: Bayesian Additive Regression Trees, R package BayesTree [Chipman et al., 2010],

C5.0: R package C50 [Quinlan, 1993],
CART: Classification and Regression Trees, R package tree [Breiman et al., 1984],

Lasso: R package glmnet [Friedman et al., 2010],
LR: logistic regression,
NB: Naïve Bayes, R package e1071 [Duda \& Hart, 1973]
RF: Random Forest, R package ranger [Breiman, 2001],
SVM: Support Vector Machines, R package e1071 [Evgeniou et al., 2000],
TAN: Tree-Augmented Naïve Bayes, R package bnlearn [Friedman et al., 1997].

We use 25 small benchmark data sets used by Friedman et al. [1997] and 6 high-dimensional data sets [Guyon et al.,




Figure 3: Classification accuracy on low- and high-dimensional data sets, showing average accuracy over 5 runs for each method, with the top half of the methods in bold for each data set. Note that some of the classifiers could not handle multiclass data sets, and TAN timed out on the highest-dimensional data sets. SBFC performs competitively with SVM, TAN and some decision tree methods (BART and RF), and generally outperforms the others.
2005], all from the UCI repository [Lichman, 2013], described in Table 2. We split the large data sets into a training set and a test set, and use 5 -fold cross validation for the smaller data sets (we try both approaches for the highdimensional arcene data set). We remove the instances with missing values, and discretize continuous features, using Minimum Description Length Partitioning [Fayyad \& Irani, 1993] for the small data sets and binary binning [Dougherty et al., 1995] for the large ones. For a data set with $d$ features, we run SBFC for $\max (10000,10 d)$ iterations, which has empirically been sufficient for stabilization. Figure 3 compares SBFC's classification performance to the other methods.

We evaluate SBFC's feature selection and interaction detection performance on the data sets heart, corral, and madelon, in Figures 4, 5, and 6 respectively. We compare SBFC's feature selection performance to Lasso, as well as RF's importance metric and BART's varcount metric, which rank features by their influence on classification, in Figures 4c, 5e, 5f, and 6c. We illustrate the structures learned by SBFC on these data sets using sampled graphs, shown in Figures 4a, 5a, 5b, and 6a, and average graphs over all the MCMC samples, shown in Figures 4b, 5c, 5d, and 6 b .

![img-4.jpeg](img-4.jpeg)
(b) Average graph for heart data set


(c) Feature selection comparison for heart data set

Figure 4: The sampled graph in Figure 4a and the average graph in Figure 4b show feature and interaction selection for the heart data set with features of medical significance. The dark-shaded features in the average graph are the most relevant for predicting heart disease. There are several groups of relevant interacting features: (Sex, Thalassemia), (Chest Pain, Angina), and (Max Heart Rate, ST Slope, ST Depression). The features in each group jointly affect the presence of heart disease. Figure 4c compares feature rankings with other methods, showing that all the methods agree on the top 9 features, but SBFC disagrees with the other methods on the top 3 features.

In the average graphs, the nodes are color-coded according to relevance, based on the proportion of sampled graphs where the corresponding feature appeared in Group 1 (dark-shaded nodes appear more often). Edge thickness also corresponds to relevance, based on the proportion of samples where the corresponding feature interaction appeared. To avoid clutter, only edges that appear in at least $10 \%$ of the sampled graphs are shown, and nodes that appear in Group 0 more than $80 \%$ of the time are omitted for high-dimensional data sets. Average graphs are undirected and do not necessarily have a tree structure. They provide an interpretable visual summary of the relevant features and feature interactions.

As shown in Table 3, the runtime of SBFC scales approximately as $d \cdot n \cdot 2 \cdot 10^{-4}$ seconds (on an AMD Opteron 6300-series processor), so it takes somewhat longer to run than many of the other methods on high-dimensional data
sets. SBFC's memory usage scales quadratically with $d$.

## 5. Conclusion

Selective Bayesian Forest Classifier is an integrated tool for supervised classification, feature selection, interaction detection and visualization. It splits the features into signal and noise groups according to their relationship with the class label, and uses tree structures to model interactions among both signal and noise features. The forest dependence structure gives SBFC modeling flexibility and competitive classification performance, and it maintains good feature and interaction selection performance as the signal to noise ratio decreases. Useful directions for future work include extending SBFC to a semi-supervised learning method, and improving runtime and memory performance.

![img-5.jpeg](img-5.jpeg)
(a) A sampled graph for the original corral data set with 6 features
![img-6.jpeg](img-6.jpeg)
(c) Average graph for the original corral data set with 6 features
![img-7.jpeg](img-7.jpeg)
(e) Feature selection comparison for the original corral data set with 6 features
![img-8.jpeg](img-8.jpeg)
(b) A sampled graph for the augmented corral data set with 100 features
![img-9.jpeg](img-9.jpeg)
(d) Average graph for the augmented corral data set with 100 features


Figure 5: In the synthetic data set corral, the true feature structure is known: the relevant features are $\left\{X_{1}, X_{2}, X_{3}, X_{4}, X_{6}\right\}$, and the most relevant edges are $\left\{X_{1}, X_{2}\right\},\left\{X_{3}, X_{4}\right\}$, while the other edges between the first 4 features are less relevant, and any edges with $X_{5}$ or $X_{6}$ are not relevant. The sampled graph in Figure 5a and the average graph in Figure 5c show that SBFC recovers the true correlation structure between the features, with the most relevant edges appearing the most frequently (as indicated by thickness). We generate extra noise features for this data set by choosing an existing feature at random and shuffling the rows, making it uncorrelated with the other features. The sampled graph in Figure 5b and the average graph in Figure 5d show that SBFC recovers the relevant features and some relevant interactions when the amount of noise increases. Figures 5e and 5f show that all the methods consistently rank the 5 relevant features (colored blue) above the rest (colored red).

![img-10.jpeg](img-10.jpeg)
(a) A sampled graph for made 1 on data set
![img-11.jpeg](img-11.jpeg)
(b) Average graph for made 1 on data set
![img-12.jpeg](img-12.jpeg)
(c) Feature selection comparison for made 1 on data set

Figure 6: Feature and edge selection for the synthetic made 1 on data set, used in the 2003 NIPS feature selection challenge. This data set, with 20 relevant features and 480 noise features, was artificially constructed to illustrate the difficulty of selecting a feature set when no feature is informative by itself, and all the features are correlated with each other [Guyon et al., 2005]. SBFC reliably selects the correct set of 20 relevant features [Guyon et al., 2006], as shown in Figure 6c, and appropriately puts them in a single connected component, shown in dark blue in the average graph in Figure 6b. As shown in Figure 6c, none of the other methods correctly identify the set of 20 relevant features (colored blue), though Random Forest comes close with 19 out of 20 correct. Our classification performance on this data set is not as good as that of BART or RF, likely because SBFC constrains these highly correlated features to form a tree structured Bayesian network, while a decision tree structure allows a feature to appear more than once.
