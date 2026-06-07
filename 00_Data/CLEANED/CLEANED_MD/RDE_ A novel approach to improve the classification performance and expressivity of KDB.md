# RESEARCH ARTICLE 

## RDE: A novel approach to improve the classification performance and expressivity of KDB

Hua Lou ${ }^{1 *}$, LiMin Wang ${ }^{2}$, DingBo Duan ${ }^{1}$, Cheng Yang ${ }^{1}$, Musa Mammadov ${ }^{3}$<br>1 Changzhou College of Information Technology, ChangZhou, China, 2 College of Computer Science and Technology, Jilin University, ChangChun, China, 3 Faculty of Science and Technology, Federation University, Ballarat, Australia<br>* ccit-louhua@139.com

## 6

OPEN ACCESS
Citation: Lou H, Wang L, Duan D, Yang C, Mammadov M (2018) RDE: A novel approach to improve the classification performance and expressivity of KDB. PLoS ONE 13(7): e0199822. https://doi.org/10.1371/journal.pone.0199822

Editor: Lars Kaderali, Universitatsmedizin Greifswald, GERMANY

Received: December 21, 2017
Accepted: June 14, 2018
Published: July 23, 2018
Copyright: © 2018 Lou et al. This is an open access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

Data Availability Statement: The data used in this study are third party and are publicly available from the UCI repository of machine learning databases: http://archive.ics.uci.edu/ml/datasets.html.

Funding: The authors received no specific funding for this work.

Competing interests: The authors have declared that no competing interests exist.

## Abstract

Bayesian network classifiers (BNCs) have demonstrated competitive classification performance in a variety of real-world applications. A highly scalable BNC with high expressivity is extremely desirable. This paper proposes Redundant Dependence Elimination (RDE) for improving the classification performance and expressivity of $k$-dependence Bayesian classifier (KDB). To demonstrate the unique characteristics of each case, RDE identifies redundant conditional dependencies and then substitute/remove them. The learned personalized $k$-dependence Bayesian Classifier (PKDB) can achieve high-confidence conditional probabilities, and graphically interpret the dependency relationships between attributes. Two thyroid cancer datasets and four other cancer datasets from the UCI machine learning repository are selected for our experimental study. The experimental results prove the effectiveness of the proposed algorithm in terms of zero-one loss, bias, variance and AUC.

## Introduction

Data mining is the analysis step of the "knowledge discovery in databases" process and its goal is the extraction of patterns and knowledge from large amounts of data. During the past decades, statistical models, such as Bayesian network, neural network and support vector machine, have been proposed and applied in many real life applications, e.g. precision medicine. Due to the high prediction performance of these statistical models, researchers would like to gain an understanding of the reasons behind such a prediction, especially when the prediction contradicts their intuition. For example, physicians are typically not only interested in the final prediction, but also like to understand the underlying inference procedure that may help explain why the system makes a certain recommendation. An explanatory, causal and graphical model is more desirable to visualize and mine previously undiscovered knowledge from data [1].

Bayesian network classifiers (BNCs) have long been a popular tool for graphically representing the probabilistic dependencies and inferring under conditions of uncertainty [2-5]. Numerous BNCs (e.g., Naive Bayes (NB) [6], tree augmented Naive Bayes (TAN) [7],

Averaged One-Dependence Estimators (AODE) [8] and $k$-dependence Bayesian classifier (KDB) [9-11] have been proposed to mine dependency relationships from data. Among them, KDB can generalize to describe any higher degrees of attribute dependence. KDB provides the "average network" to express significant dependencies and this "one size fits all" solution obviously cannot apply to all cases. Patients with similar symptoms may have different kinds of diseases. For example, because of low incidence rate, AIDS (Acquired Immune Deficiency Syndrome) at early stage is often diagnosed as influenza [12]. How to enable person to have "personalized network", which can describe the dependency relationships among specific characteristics or attributes for each case, is still challenging. Local graph structure $\mathrm{KDB}_{P}$ [2] takes each case or unlabeled testing instance $\mathcal{P}$ as a target and can describe local causal relationships implicated. However, the number of conditional dependencies in $\mathrm{KDB}_{P}$ is determined by user-specified parameter $k$. Some redundant dependencies should be replaced with more meaningful or "personalized" dependencies that only hold in specific instances.

In this paper, a new approach, called Redundant Dependency Elimination (RDE), is proposed to identify redundant conditional dependencies in $\mathrm{KDB}_{P}$ and then substitute/remove them at classification time. The resulting optimized network structure of $\mathrm{KDB}_{P}$, denoted by $\mathrm{KDB}_{\mathrm{O}}$, can increase the confidence level of conditional probabilities. The final personalized classifier, PKDB, is an ensemble of KDBs learned from training data and testing instance respectively. PKDB combines the computational efficiency of classical generative learning with the control of bias/variance trade-off. Two thyroid disease datasets and four other cancer datasets from the UCI machine learning repository are selected for our experimental study. The experimental results show the advantages of PKDB over other classifiers.

# Materials and methods 

## Classifiers

LibSVM [13] and Random forest [14] are introduced in this paper for comparison study. We use Weka's implementations and default settings of Random forest with the exceptions of 20 decision trees. We use Weka's implementations and default settings of LibSVM and performing a "grid-search" on $C$ and $\gamma$ for the RBF kernel using 5-fold cross-validation. Each pair of $(C, \gamma)$ is tried $\left(C=2^{-5}, 2^{-3}, \cdots, 2^{15}, \gamma=2^{-15}, 2^{-13}, \cdots, 2^{3}\right)$ and the one with the lowest cross-validation zero-one loss is selected. For clarity, the abbreviation of algorithms mentioned above is shown in Table 1.

Table 1. Abbreviation of algorithms introduced in this paper.


https://doi.org/10.1371/journal.pone.0199822.t001

Table 2. Description of data sets.


https://doi.org/10.1371/journal.pone.0199822.t002

# Data 

Six datasets from UCI machine learning repository [15] are selected in this paper for case study. The detailed introduction of these datasets are shown in Table 2, which summarizes the characteristics of each dataset, including the numbers of instances, attributes and classes. For each benchmark dataset, we use MDL discretization [16] to discretize quantitative attributes using 3-bin equal frequency discretization.

## Metrics

Zero-one loss is one of the most commonly used metrics to measure the classification performance of a classifier. Zero-one loss can measure how well a classifier correctly identifies or discriminate an unlabeled instance. Let $\mathbf{X}$ and $Y$ be the input and output spaces respectively, and elements $\mathbf{x}$ and $y$ respectively. The zero-one loss function for instance $\mathbf{x}$ is defined as [17]:

$$
\xi(\mathbf{x})=1-\delta(y, \hat{y})
$$

where $\delta(y, \hat{y})=1$ if $\hat{y}=y$ and zero otherwise, $y$ and $\hat{y}$ are respectively the true class label and predicted label of $\mathbf{x}$. Kohavi and Wolpert presented a bias-variance decomposition of the zeroone loss function [17]. The bias term measures the squared difference between the average output of the target and the algorithm, and it is defined as follows [17]:

$$
\operatorname{bias}(\mathbf{x})=\frac{1}{2} \sum_{y^{\prime} \in Y}\left[P\left(y^{\prime} \mid \mathbf{x}\right)-P(y \mid \mathbf{x})\right]^{2}
$$

The variance term measures the sensitivity of the algorithm to the changes in the training set, and it is defined as follows [17]:

$$
\operatorname{variance}(\mathbf{x})=\frac{1}{2}\left[1-\sum_{y^{\prime} \in Y} P\left(y^{\prime} \mid \mathbf{x}\right)^{2}\right]
$$

In machine learning, the bias-variance tradeoff is a central problem for supervised learning. Ideally, one wants to choose a model that both accurately captures the regularities in its training data, but also generalizes well to unseen data. Unfortunately, it is typically impossible to do both simultaneously. High-variance learning methods (e.g., high-dependence BNCs) are usually more complex, enabling them to capture more complex multivariate relationships, but at risk of overfitting to noisy or unrepresentative training data. In contrast, high-bias component of zero-one loss is highly appealing to simpler models that don't tend to overfit, but may underfit their training data, failing to capture important regularities.

The statistical hypothesis test, e.g. Friedman test [18], can test the null hypothesis of no differences between algorithms. Friedman test ranks the algorithms for each data set separately:

the best performing algorithm getting the rank of 1 , the second best ranking 2 , and so on. In case of ties, average ranks are assigned. The Friedman statistic can be computed as follows [18]:

$$
X_{F}^{2}=\frac{12}{N t(t+1)} \sum_{j=1}^{n} R_{j}^{2}-3 N(t+1)
$$

where $R_{i}=\sum_{i} r_{i}^{i}$ and $r_{i}^{i}$ is the rank of the $j$-th of $t$ algorithms on the $i$-th of $N$ datasets.
Sensitivity measures the proportion of actual positives that are correctly identified and specificity measures the proportion of actual negatives that are correctly identified. Receiver operating characteristic curve, i.e. ROC curve, is a powerful tool to illustrate the diagnostic ability of a binary classifier by plotting the true positive rate (Sensitivity) against the false positive rate (100-Specificity) for different cut-off points. Each point on the ROC curve represents a sensitivity/specificity pair corresponding to a particular decision threshold. The ROC curve graphically displays the trade-off between sensitivity and specificity and is useful in assigning the best cut-offs. The area under the ROC curve (AUC) [19] provides a simple numeric measure indicating the performance over the visual comparison of ROC curves.

# Bayesian network classifiers 

Given class variable $Y$ and a set of discrete attributes $\mathbf{X}=\left\{X_{1}, X_{2}, \cdots, X_{n}\right\}$ (In the following formulas, all variables are assumed to be discrete.) the aim of supervised learning is to predict the discrete class label $y$ of a testing instance $\mathbf{x}=\left(x_{1}, \cdots, x_{n}\right)$, where $x_{i}$ is the value of attribute $X_{i}$ and $y$ is the value of class variable $Y$. The restricted BNCs, e.g., KDB, model joint probability distribution $P(\mathbf{x}, y)$ according to chain rule, which can be described in the form of a product of a set of conditional probabilities.

$$
P(\mathbf{x}, y)=P(y) \prod_{i=1}^{n} P\left(x_{i} \mid \Pi_{i}, y\right)
$$

where $\Pi_{i}$ represents the parent attribute set of $X_{i}$.
From the definition of conditional probability, we use the following Formula to classify

$$
P(y \mid \mathbf{x})=\frac{P(\mathbf{x}, y)}{P(\mathbf{x})}=\frac{P(\mathbf{x}, y)}{\sum_{y} P(\mathbf{x}, y)}
$$

When attribute number $n$ is high and/or data size $N$ is relatively small, it would be difficult to obtain a sufficiently accurate estimate of $P\left(x_{i} \mid \Pi_{i}, y\right)$ from the sample frequencies. One popular solution is to restrict the number of parents of each attribute while trying to retain accurate estimate of $P\left(x_{i} \mid \Pi_{i}, y\right)$. That is, given attribute subset $\hat{\Pi}_{i} \subset \Pi_{i}, P\left(x_{i} \mid \hat{\Pi}_{i}, y\right) \approx P\left(x_{i} \mid \Pi_{i}, y\right)$ holds. Sahami [11] proposed the notion of $k$-dependence BNC, which allows each attribute $X_{i}$ to have a maximum of $k$ attribute nodes as parents.

NB is the simplest of the BNCs, assuming that all attributes are independent given the class. There exist no dependency relationships between attributes and thus NB is a 0 -dependence BNC. AODE utilizes a restricted class of one-dependence estimators (ODEs) and aggregates the predictions of all qualified estimators within this class. TAN relaxes NB's independence assumption by allowing every attribute to have at most one other attribute as parent. Its basic structure extends the Chow-Liu tree [20] to a maximum spanning tree. The arc or conditional dependence between attributes $X_{i}$ and $X_{j}$ is measured by conditional mutual information

(CMI) $I\left(X_{i} ; X_{j} \mid Y\right)$ given class variable, which is defined as follows [21],

$$
I\left(X_{i} ; X_{j} \mid Y\right)=\sum_{x_{i}} \sum_{x_{j}} \sum_{y} P\left(x_{i}, x_{j}, y\right) \log \frac{P\left(x_{i}, x_{j} \mid y\right)}{P\left(x_{i} \mid y\right) P\left(x_{j} \mid y\right)}
$$

KDB further relaxes NB's independence assumption by allowing any attribute $X_{i}$ to be conditioned on at most $k$ other attributes, i.e., at most $k$ arcs from other attributes to $X_{i}$. Unlike TAN, KDB requires to determine the attribute order by comparing the mutual information (MI) $I\left(X_{i} ; Y\right)$ between attribute $X_{i}$ and class $Y$, which is defined as follows [21],

$$
I\left(X_{i} ; Y\right)=\sum_{x_{i}} \sum_{y} P\left(x_{i}, y\right) \log \frac{P\left(x_{i}, y\right)}{P\left(x_{i}\right) P(y)}
$$

The learning procedures of KDB is described in Algorithm 1.

# Algorithm 1: Structure learning of KDB 

Input: Training set $\mathcal{T}$, parameter $k=2$, crosstab CMI $=\left\{I\left(X_{i}, X_{j} \mid Y\right) \mid 1 \leq\right.$ $i \neq j \leq n\}$ (see formula (4)) and vector $M I=\left\{I\left(X_{i} ; Y\right) \mid 1 \leq i \leq\right.$ $n\}$ (see formula (5)).
Output: Network structure $\mathrm{KDB}_{T}=\{\mathcal{V}, \mathcal{E}\}$, where $\mathcal{V}$ is the node set and $\mathcal{E}$ is the edge set.
1 Let $\mathcal{L}$ be a list of all $X_{i}$ in descending order of $I\left(X_{i} ; Y\right)$.
$2 \mathcal{V}=\{Y\} ; \mathcal{E}=\varnothing$;
3 for $i=1 \rightarrow n$ do
$4 \quad \mathcal{V}=\mathcal{V} \cup \mathcal{L}[i] ;$
$5 \quad \mathcal{E}=\mathcal{E} \cup(Y \rightarrow \mathcal{L}[i]) ;$
6 end
7 for $i=1 \rightarrow n$ do
$8 \quad S=\varnothing$;
$9 \quad \hat{k}=\hat{k} ;$
10 while $(\hat{k}>0)$ do
$11 \quad m=\operatorname{argmax}_{j}\left\{I(\mathcal{L}[i] ; \mathcal{L}[j] \mid Y): 1 \leq j<i\right\}, j \notin S\}$;
$12 \quad \mathcal{E}=\mathcal{E} \cup(\mathcal{L}[m] \rightarrow \mathcal{L}[i]) ;$
$13 \quad \hat{k}=\hat{k}-1 ;$
$14 \quad S=S \cup\{m\} ;$
15 end
16 end
17 return $\mathrm{KDB}_{T}$
Algorithm 2: Structure learning of $\mathrm{KDB}_{T}$.
Input: testing instance $\mathcal{P}$, parameter $k=2$, vector LMI $=\left\{I\left(x_{i} ; Y\right) \mid 1 \leq\right.$ $i \leq n\}$, crosstab CLMI $=\left\{I\left(x_{i}, x_{j} \mid Y\right) \mid 1 \leq i \neq j \leq n\right\}$ (see formula (6)).
Output: Network structure $\mathrm{KDB}_{P}=\{\mathcal{V}, \mathcal{E}\}$, where $\mathcal{V}$ is the node set and $\mathcal{E}$ is the edge set.
1 Let $\mathcal{L}$ be a list of all $x_{i}$ in descending order of $I\left(x_{i} ; Y\right)$.
$2 \mathcal{V}=\{Y\} ; \mathcal{E}=\varnothing$;
3 for $i=1 \rightarrow n$ do
$4 \quad \mathcal{V}=\mathcal{V} \cup \mathcal{L}[i] ;$
$5 \quad \mathcal{E}=\mathcal{E} \cup(Y \rightarrow \mathcal{L}[i]) ;$
6 end
7 for $i=1 \rightarrow n$ do
$8 \quad S=\varnothing ;$

```
9 \(\hat{k}=k\);
1 0 while ( \(\hat{k}>0\) ) do
\(m=\operatorname{argmax}_{i}\left\{I(\mathcal{L}[i] ; \mathcal{L}[j] \mid Y): 1 \leq j<i\right), j \notin S\} ;\)
\(E=\mathcal{E} \cup(\mathcal{L}[m] \rightarrow \mathcal{L}[i])\);
\(i=\hat{k}-1\);
\(S=S \cup\{m\}\);
end
end
return \(\mathrm{KDB}_{P}\)
```

KDB can represent the "average knowledge" or "expert knowledge" mined from data, that roughly describes the dependency relationships between different inputs, e.g., the dependency relationship between \{Gender, Age\} and TSH. However, KDB cannot finely describe the dependency relationships in different patient records, e.g., the relative independency relationship between $\{$ Gender $=$ "male", Age $=20\}$ and TSH $=$ "yes", or the relative dependency relationship between $\{$ Gender $=$ "female", Age $=45\}$ and TSH $=$ "yes". In contrast, $\mathrm{KDB}_{P}$ represents "personalized knowledge" mined from instance $\mathcal{P}$. The "average knowledge" learned from labeled training data and the "personalized knowledge" learned from unlabeled testing instance are complementary in nature. Thus they should be considered simultaneously for classification. To achieve this goal, $\mathrm{KDB}_{P}$ applies the same learning strategy that KDB uses. Given testing instance $\mathcal{P}=\left(x_{1}, \cdots, x_{n}\right), \mathrm{KDB}_{P}$ sorts attributes by comparing local mutual information (LMI) $I\left(x_{i} ; x_{j} \mid Y\right)$ and choose appropriate conditional dependencies by comparing conditional local mutual information (CLMI). LMI and CLMI are defined as follows [2],

$$
\left\{\begin{array}{l}
I\left(x_{i} ; Y\right)=\sum_{y} P\left(x_{i}, y\right) \log \frac{P\left(x_{i}, y\right)}{P(y) P\left(x_{i}\right)} \\
I\left(x_{i} ; x_{j} \mid Y\right)=\sum_{y} P\left(x_{i}, x_{j}, y\right) \log \frac{P\left(x_{i}, x_{j} \mid y\right)}{P\left(x_{i} \mid y\right) P\left(x_{j} \mid y\right)}
\end{array}\right.
$$

From the viewpoint of information theory, MI or $I\left(X_{i} ; Y\right)$ can measure the uncertainty reduction in $Y$ given the information from $X_{i}$. The attributes corresponding to greater reduction will get higher rank and added to the network structure in priority. By comparing formulas (5) and (6) we can see that, $I\left(X_{i} ; Y\right)=\sum_{x_{i}} I\left(x_{i} ; Y\right)$. MI refers to the average of all possible events, and it is the expected value of LMI over all possible values of $X_{i}$. LMI can be used to measure the uncertainty reduction in $Y$ given the information from $X_{i}=x_{i}$. Because $I\left(X_{i} ; X_{j} \mid Y\right)=\sum_{x_{i}, x_{j}} I\left(x_{i} ; x_{j} \mid Y\right)$, we can get similar results that $I\left(x_{i} ; x_{j} \mid Y\right)$ can measure the conditional dependence between $X_{i}$ and $X_{j}$ when they take specific values.

The ensemble of KDB and $\mathrm{KDB}_{P}$, i.e., AKDB [2], has better overall prediction accuracy, on average, than any individual member. KDB and $\mathrm{KDB}_{P}$ apply the same learning strategy whereas model different data spaces (training data and testing instance). It is difficult to judge which output from these two classifiers should be considered in priority. The linear combiner is used for models that output real-valued numbers, so is applicable for BNC. In practice, it is inappropriate to pre-determine the weight of subclassifier. Thus in practice AKDB uses the uniformly rather than nonuniformly weighted average. The ensemble probability estimate is

$$
\hat{P}(y \mid \mathcal{X}, \mathrm{AKDB})=\frac{P(y \mid \mathcal{X}, \mathrm{KDB})+P(y \mid \mathcal{X}, \mathrm{KDB}_{P})}{2}
$$

Given $m$ class labels, the class label $y^{*}$ of unlabeled instance $\mathbf{x}$ corresponds to the highest value of posterior probability of $\hat{P}(y \mid \mathcal{X}, \mathrm{AKDB})$, where $y \in\left\{y_{1}, \cdots, y_{m}\right\}$, i.e.,

$$
y^{*}=\arg \max \hat{P}(y \mid \mathcal{X}, \mathrm{AKDB})
$$

The classification procedure of AKDB is shown in Algorithm 3.
Algorithm 3: Classification procedure of AKDB

```
Input: testing instance \(\mathcal{P}=\left(x_{1}, \cdots, x_{n}\right)\), KDB learned from Algorithm 1 and
    KDB \(_{P}\) learned from Algorithm 2.
Output: Class label \(y^{\prime}\).
1 Compute the joint probability \(P(y, \mathbf{x} \mid\) KDB \()\) and \(P\left(y, \mathbf{x} \mid \mathrm{KDB}_{P}\right)\) by Formula (2);
2 Compute the conditional probability \(P(y \mid \mathbf{x}\), KDB) and \(P\left(y \mid \mathbf{x}, \mathrm{KDB}_{P}\right)\) by
    Formula (3);
3 Compute the conditional probability \(P(y \mid \mathbf{x}\), AKDB) by Formula (7);
4 Compare and predict the class label \(y^{\prime}\) for \(\mathcal{P}\) by Formula (8);
5 Return \(y^{\prime}\);
```


# Redundant dependency elimination 

Suppose that $\Pi_{i}=\left\{X_{1}, \cdots, X_{i-1}\right\}$, from the chain rule of mutual information we have [21]

$$
\begin{aligned}
I\left(X_{i} ; \Pi_{i}, Y\right)= & I\left(X_{i} ; Y\right)+I\left(X_{i} ; X_{1} \mid Y\right)+I\left(X_{i} ; X_{2} \mid X_{1}, Y\right)+ \\
& \cdots+I\left(X_{i} ; X_{i-1} \mid X_{1}, \cdots, X_{i-2}, Y\right)
\end{aligned}
$$

KDB implicitly reduces $I\left(X_{i} ; X_{j} \mid X_{1}, \cdots, X_{j-1}, Y\right)$ to $I\left(X_{i} ; X_{j} \mid Y\right)$ when $j>1$. The same strategy is also applicable to $\mathrm{KDB}_{P}$. Obviously, the dependency relationships between the parent attributes of $X_{i}$ are neglected, that will inevitably result in estimation bias. For different instances, the dependency relationships may differ. Here, we introduce Pointwise mutual information (PMI) $I\left(x_{i} ; x_{j}\right)$ and Pointwise conditional mutual information (PCMI) $I\left(x_{i} ; x_{k} \mid x_{i}\right)$ to address this issue. The definitions of PMI and PCMI are as follows [22],

$$
\left\{\begin{array}{l}
I\left(x_{i} ; x_{j}\right)=\log \frac{P\left(x_{i}, x_{j}\right)}{P\left(x_{i}\right) P\left(x_{j}\right)} \\
I\left(x_{i} ; x_{k} \mid x_{j}\right)=\log \frac{P\left(x_{i}, x_{k} \mid x_{j}\right)}{P\left(x_{i} \mid x_{j}\right) P\left(x_{k} \mid x_{j}\right)}
\end{array}\right.
$$

The dependency relationships in $\mathrm{KDB}_{P}$ that are relevant or irrelevant to class labels are respectively measured by formulas (6) and (10), the confidence levels of which are determined by the estimation of probability distributions. The probability distributions have to be estimated from training data before structure learning. For small datasets, the sparsely distributed attribute values make the estimation of lower-order probability estimations much more reliable than that of the higher-order ones. If the probability distributions learned from training data are not reliable, the resulting non-robust classifier will make wrong prediction. That may be the main reason why NB offers competitive performance with high efficiency, strong robustness and loose coupling on some small datasets.

PMI and PCMI refer to single events. Like MI, PMI also follows the chain rule, i.e.,

$$
I\left(x_{i} ; x_{1}, \cdots, x_{i-1}\right)=I\left(x_{i} ; x_{1}\right)+I\left(x_{i} ; x_{2} \mid x_{1}\right)+\cdots+I\left(x_{i} ; x_{i-1} \mid x_{1}, \cdots, x_{i-2}\right)
$$

In computational linguistics, PMI has been used for finding co-occurrences of words in a text corpus and to approximate the probabilities $P(x)$ and $P(x, y)$ respectively. MI can roughly

![img-0.jpeg](img-0.jpeg)

Fig 1. Example: Conditional dependencies between $X_{i}$ and its parents. (a) $X_{i}$ has two parent attributes $X_{j}$ and $X_{k}$. (b) Parent attribute $X_{k}$ is substituted with $X_{i}$. https://doi.org/10.1371/journal.pone.0199822.g001 measure the dependency relationship between the associated variables, but cannot measure the inherent relational mapping between specific variable values. Given two attributes $X_{i}, X_{j}$, each having two values and $\left\langle X_{i}, X_{j}\right\rangle=\{(1,1),(1,2),(2,2)\}$ for example, obviously when $X_{i}=$ 1 the uncertainty of $X_{j}$ reaches a maximum, whereas when $X_{i}=2$ the uncertainty of $X_{j}$ is reduced to zero. In practice, it may be the case that certain values are more significant than others, or that certain patterns of association are more semantically important than others. Further, it is desirable to obtain reasonable causal relationships for causality analysis rather than a simple classification result. Considering an example of a substructure shown in Fig 1(a), Corresponding training data is presented in Table 3. In this example, $X_{i}$ has two parents $X_{j}, X_{k}$ and its conditional probability is $P\left(x_{i} \mid x_{j}, x_{k}, y\right)$.

KDB or $\mathrm{KDB}_{7}$ just consider the conditional dependence between $X_{i}$ and its parents, and the relationships among parents are neglected, that may not help to increase the confidence level of $P\left(x_{i} \mid \Pi_{i}, y\right)$ or reduce the uncertainty of $X_{i}$ when it takes specific values. For testing instance $\mathcal{P}$, its class label is unknown thus Redundant Dependency Elimination (RDE) just considers the dependency relationships between attribute values. For example, given $\left\{X_{i}=b\right.$,

Table 3. An example of training data with four attributes, in which the mapping relationships between $\left\{X_{i}, X_{j}, X_{k}\right\}$ are shown.


https://doi.org/10.1371/journal.pone.0199822.t003

$X_{j}=d, X_{k}=e$ ) in Table 3, from the chain rule of PMI we will have

$$
\begin{aligned}
I\left(x_{i} ; x_{j}, x_{k}\right) & =I\left(x_{i} ; x_{j}\right)+I\left(x_{i} ; x_{k} \mid x_{j}\right)=\log \frac{P(b, d)}{P(b) P(d)}+\log \frac{P(b, e \mid d)}{P(b \mid d) P(e \mid d)} \\
& =\log \frac{P(b, d)}{P(b) P(d)}+\log \frac{P(b, d, e) P(d)}{P(b, d) P(d, e)} \\
& =\log \frac{\frac{1}{2}}{\frac{1}{2} \cdot \frac{1}{6}}+\log \frac{\frac{1}{2} \cdot \frac{4}{6}}{\frac{1}{2} \cdot \frac{4}{6}} \\
& =\log \frac{6}{4}+0=\log \frac{6}{4}
\end{aligned}
$$

Thus $I\left(x_{i} ; x_{j}, x_{k}\right)=I\left(x_{i} ; x_{j}\right)$, i.e., $x_{k}$ does not provide any extra valuable information to reduce the uncertainty of $x_{i}$. To further increase the conditional probability of $x_{i}$, we should select another attribute value, e.g., $x_{i}$, to take the place of $x_{k}$. If $I\left(x_{i} ; x_{i} \mid x_{j}\right)>0$, then

$$
I\left(x_{i} ; x_{j}, x_{i}\right)-I\left(x_{i} ; x_{j}, x_{k}\right)=\left[I\left(x_{i} ; x_{j}\right)+I\left(x_{i} ; x_{i} \mid x_{j}\right)\right]-I\left(x_{i} ; x_{j}\right)=I\left(x_{i} ; x_{i} \mid x_{j}\right)>0
$$

Thus the larger the difference is, the more appropriate $X_{i}$ is as the parent of $X_{i}$. If the attributes are sorted by comparing $I\left(x_{i} ; Y\right)$ and the resulting order is $\left\{x_{1}, \cdots, x_{n}\right\}$, then $x_{i}$ can select at most $k$ parents from $i-1$ attributes that ranks higher. Suppose that its parents are sorted by comparing $I\left(x_{i} ; x_{j} \mid Y\right)(j<i)$ and the order is $\left\{\hat{x}_{1}, \cdots, \hat{x}_{i-1}\right\}$, RDE first operates by iteratively identifying redundant parents of each attribute. It uses the criterion

$$
\frac{I\left(x_{i} ; \hat{x}_{j} \mid \hat{x}_{1}\right)}{I\left(x_{i} ; \hat{x}_{1}\right)} \geq \delta
$$

to infer that except the information $\hat{x}_{1}$ provides to $x_{i}, \hat{x}_{j}$ can provide extra information to $x_{i}$, where $\hat{X}_{j} \in \Pi_{i}$ and $1<j \leq i-1, \delta$ is a minimum redundancy ratio. If there exist attribute values that make formula (14) hold, then an appropriate parent of $x_{i}$ should be selected from them. This process is terminated if there is no redundancy or no substituted attribute available. We keep the attribute value with the smallest index and disregard the other attribute values. For instance, if $\hat{x}_{2}, \hat{x}_{3}$ and $\hat{x}_{4}$ hold for formula (14), we only take $\hat{x}_{2}$ as the parent of $x_{i}$.

Starting from the basic network structure learned from testing instance, $\mathrm{KDB}_{\mathrm{O}}$ repairs "harmful" interdependencies by applying RDE to remove highly correlated attribute values in classification time. Note that attribute selection approaches, such as Backwards sequential elimination (BSE, [23, 24]), simply remove attributes to achieve zero-one loss improvement. BSE operates by iteratively removing successive attributes until no zero-one loss improvement. According to Formula 2, attribute $X_{i}$ can have at most $i-1$ parents, i.e., there exists $i-1$ conditional dependencies between $X_{i}$ and its parents. If $X_{i}$ is removed from Bayesian network structure, then $i-1$ conditional dependencies will be implicitly removed correspondingly. That will result in great change in network structure and classification bias. In contrast, RDE retains all attributes and resolve such interdependencies with much more flexible strategy and finer tuning, as for some test instances one conditional dependence may be identified as redundant and then substituted or removed, for other test instances it may hold.

One effective way of resolving the trade-off between bias and variance is to use ensemble learning [9, 25]. For example, boosting combines many "weak" (high bias) models in an ensemble that has lower bias than the individual models, while bagging combines "strong" learners in a way that reduces their variance. KDB and $\mathrm{KDB}_{\mathrm{O}}$ are both "strong" learners. KDB takes training set as a target and build general BNC for it. $\mathrm{KDB}_{\mathrm{O}}$ takes testing instance $\mathcal{P}$ as a target and build a specific BNC for $\mathcal{P}$. In contrast to $\mathrm{KDB}, \mathrm{KDB}_{\mathrm{O}}$ is defined by the conditional

dependencies at the attribute values in $\mathcal{P}$. Obviously, for different testing instances, KDB remains the same while $\mathrm{KDB}_{\mathrm{O}}$ may differ greatly. RDE identifies and then substitutes/removes the redundant dependencies in $\mathrm{KDB}_{P}$, that will make the conditional dependencies in $\mathrm{KDB}_{\mathrm{O}}$ much more reasonable.

The final model, PKDB, is an ensemble of KDB and $\mathrm{KDB}_{O}$. The ensemble probability estimate for PKDB is

$$
\hat{P}(y \mid x, \mathrm{PKDB})=\frac{P(y \mid x, \mathrm{KDB})+P\left(y \mid x, \mathrm{KDB}_{O}\right)}{2}
$$

PKDB can represent arbitrary $k$-dependence relationships. It seems that PKDB with higher degree of attribute dependence will more closely fit the training data and can achieve better generalization performance than those with lower degree of attribute dependence. However, higher degree of attribute dependence needs more training instances to ensure more accurate estimation of conditional probability. From Table 2, the thyroid disease datasets for experimental study contain relatively small number $(<3800)$ of instances but large number $(\geq 25)$ of attributes. To make resulting algorithm combine the computational efficiency of classical generative learning with the control of bias/variance trade-off, in the following discussion we restrict PKDB to be 2-dependence, i.e., $k=2$, as used in [2]. Since attribute $X_{i}$ can have $k$ parent attributes with higher ranks, the problem of redundant dependency arises when $i \geq k+2$. The detailed learning procedure of PKDB is presented in Algorithm 4.

```
Algorithm 4: Redundant Dependency Elimination for \(\mathrm{KDB}_{\mathrm{O}}\) when \(k=2\)
Input: Network structure \(\mathrm{KDB}_{P}\), parameter \(k\), testing instance \(\mathcal{P}\).
Output: \(\mathrm{KDB}_{\mathrm{O}}, \quad\) network structure after applying RDE.
1 Transform \(\mathrm{KDB}_{P}\) to a set of children-parent pairs \(\left\{x_{1}, \Pi_{1}\right\} \cdots\),
    \(\left\{x_{n}, \Pi_{n}\right\}\).
2 Let \(\mathcal{L}\) be a list of all \(x_{i}\) in descending order of \(I\left(x_{i} ; Y\right)\).
3 for \(i=k+2 \rightarrow n\) do
4 Let \(\mathcal{L}^{\prime}\) be a list of all \(x_{j}\left(x_{j} \in \Pi_{i}\right)\) in descending order of
    \(I\left(x_{i} ; x_{j} \mid Y\right) ;\)
\(5 \quad \Pi_{i}=\left\{\mathcal{L}^{\prime}[1]\right\} ;\)
6 for \(j=2 \rightarrow i-1\) do
7 if \(\left(I\left(\mathcal{L}[i] ; \mathcal{L}^{\prime}[j] \mid \mathcal{L}^{\prime}[1]\right) \geq \delta \cdot I\left(\mathcal{L}[i] ; \mathcal{L}^{\prime}[1]\right)\right)\) (see formula (14)) then
\(8 \quad \Pi_{i}=\left\{\mathcal{L}^{\prime}[1], \mathcal{L}^{\prime}[j]\right\} ;\)
9 end
10 end
11 end
12 Transform revised children-parent pairs \(\left\{x_{1}, \Pi_{1}\right\} \cdots,\left\{x_{n}, \Pi_{n}\right\}\)
    to \(\mathrm{KDB}_{\mathrm{O}}\).
13 return \(\mathrm{KDB}_{\mathrm{O}}\)
```

During training PKDB generates a three-dimensional table of co-occurrence counts for each pair of attribute values and each class value to estimate the probabilities $P(y), P\left(x_{i}, y\right), P$ $\left(x_{i}, x_{j}, y\right), P\left(x_{i}, x_{j}\right)$ and $P\left(x_{i}, x_{j}, x_{k}\right)$. KDB requires $O\left(N m(m v)^{2}\right)$ time (dominated by calculating CMI) [11] to build the network structure, where $v$ is the average number of discrete values that an attribute may take. The basic structure of $\mathrm{KDB}_{\mathrm{O}}$ only considers the attribute values in testing instance and thus requires $O\left(N m n^{2}\right)$ time. RDE requires $O\left(N n^{2}\right)$ time to calculate PCMI, then an extra pass is needed to perform identification and then substitute/remove redundant conditional dependencies. The final time complexity for building $\mathrm{KDB}_{\mathrm{O}}$ is $O\left(N m n^{2}\right)+O\left(N n^{3}\right)$. The time complexities of classifying a single instance for KDB and $\mathrm{KDB}_{O}$ are the same, $O$ (mnk).

# Results 

The experimental system is implemented in C++. The experiments are conducted on a desktop computer with an Intel(R) Core(TM) i5-7200 CPU @3.20GHz, 64 bits and 12,288 MB of memory. For the BNCs to be compared, 10 -fold cross validation is applied to obtain an accurate estimation of the average performance. For each fold, leave-one-out cross validation zero-one loss [26] [27] is used as selection criterion to determine $\delta$ in Formula (14). Table 4 summarizes the experimental results in terms of zero-one loss, bias, variance and AUC. The Friedman statistic is distributed according to $X_{F}^{2}$ with $t-1$ degrees of freedom. Thus, for any pre-determined level of significance $\alpha$, the null hypothesis will be rejected if $X_{F}^{2}>X_{F}^{\alpha}$. The critical value of $X_{F}^{\alpha}$ for $\alpha=0.05$ with seven degrees of freedom is 14.07 . The Friedman statistic of zero-one loss in Table 4 is 15.32 , which is larger than 14.07 . Hence, the null-hypotheses is rejected and these classifiers are different.

Quinlan believed that the two relatively large datasets, i.e. Dis and Hypothyroid, have been corrupted [28] and many missing values exist ( 6064 missing values in dataset Dis and 5329 missing values in dataset Hypothyroid). When we substitute these missing values with a specific value, i.e., "?" or unknown, noise is artificially introduced and the performance of learned classifier may be degraded. For the other four small datasets with less than 800 instances, the training data provided only accounts for a small portion of the full dataset. Thus the estimation of conditional probability will be of low-confidence. Relatively simple structure resulted from underfitting rather than overfitting may help to improve the classification performance of learning algorithm. From the experimental results of zero-one loss in Table 4 we can see that, classifiers with complex structure don't necessarily enjoy significant advantage over classifiers with simple structure. For example, KDB, LibSVM and RF perform poorer than NB on datasets Breast-cancer-w and Heart-disease-c. However, $\mathrm{KDB}_{P}$ provides an effective way to learn high-confidence dependency relationships implicated in testing instance. RDE can remove the redundant dependency relationships that are irrelevant to class label and add high-confidence conditional dependencies. The negative effect caused by noise and insufficient data will be mitigated to some extent. AKDB performs better than KDB. PKDB even performs the best among all classifiers in terms of zero-one loss.

We then clarify from the viewpoint of bias-variance decomposition. The experimental results of variance are reasonable that AODE achieves higher variance than NB because of its complex structure. However, AODE achieves higher bias on dataset Dis, which means underfitting to some extent. Since AODE indiscriminately represents all $29 * 28=812$ conditional dependencies, some weak dependencies may represent a large noise component in the training set and counteract the effect the strong dependencies, making it underfit dataset Dis and its prediction less accurate than NB. For dataset Hypothyroid AODE only needs to represent $25^{*} 24=600$ conditional dependencies and negative effect of weak dependencies can be mitigated. When $k=2$, KDB can represent $0+1+2 \cdots+2=49$ conditional dependencies (as shown in Fig 2 whereas TAN only needs to represent 28 conditional dependencies. Thus KDB achieves higher variance since it fits training set well even there exists noise. As a result, the KDB does not fit the testing instance much better than TAN. Noisy training data will reduce the confidence level of the classification model. For classifiers learned from the other four small datasests, overfitting is almost inevitable. KDB, LibSVM and RF perform poorer than NB on datasets Breast-cancer-w and Heart-disease-c in terms of variance. How to reduce variance is a crucial point for improving classification accuracy. RDE helps to mitigate the negative effect of overfitting, thus the variance for PKDB is always lower than that for AKDB and KDB.

Table 4. The comparison of classification performance between classifiers in terms of zero-one loss, bias, variance and AUC.


https://doi.org/10.1371/journal.pone.0199822.t004

$$
\begin{aligned}
& X_{0}=\text { Sex } \\
& X_{1}=\text { On thyroxine } \\
& X_{2}=\text { Query on thyroxine } \\
& X_{3}=\text { Medication } \\
& X_{4}=\text { Thyroid surgery } \\
& X_{5}=\text { Query hypothyroid } \\
& X_{6}=\text { Query hyperthyroid } \\
& X_{7}=\text { Pregnant } \\
& X_{8}=\text { Sick } \\
& X_{9}=\text { Tumor } \\
& X_{10}=\text { Lithium } \\
& X_{11}=\text { Goitre } \\
& X_{12}=\text { TSH measured }
\end{aligned}
$$

![img-1.jpeg](img-1.jpeg)

Fig 2. The network structure of $\operatorname{KDB}(k=2)$ on dataset Hypothyroid. Class variable $Y$ is not included for simplicity. Only conditional dependencies between attributes are shown.
https://doi.org/10.1371/journal.pone.0199822.g002

AUC is often used to evaluate the classification performance while dealing with imbalanced data. From Table 4 we can see that, TAN and KDB perform better than NB more often than not on small datasets. That indicates although the negative effect caused by overfitting may reduce the classification accuracy, the dependency relationships implicated will help to improve the the discriminatory power of BNCs. The definitions of LMI and CLMI considers all possible values of class variable, thus $\mathrm{KDB}_{T}$, cannot overfit the given testing instance $\mathcal{P}$, but provides a possible dependence tree structure to describe the relationships among attribute values in $\mathcal{P}$. The advantage of PKDB over other classifiers in AUC is especially obvious on datasets Dis and Hypothyroid. In contrast, AKDB also uses the personalized $\mathrm{KDB}_{T}$, it performs much worse. This can be attributed to the low-confidence dependency relationships mined from these small datasets. LibSVM performs poorer on datasets Dis and Hypothyroid but better on the other four small datasets. RF demonstrates significant robustness while dealing with relatively large or small datasets.

# Discussion 

Doctors may need to determine if blood tests are necessary for patients due to their respective risk factors, e.g., family history of goitres, Gender or Age. By computing LMI, CLMI from the local perspective, $\mathrm{KDB}_{\mathrm{O}}$, which learns from individual testing instance, is obviously an example of learners for precision medicine. PKDB can utilize the information provided by the training set and testing instances with the help of the aggregating mechanism. To prove this, we take two cases for example from Hypothyroid dataset, which take different class labels. The

![img-2.jpeg](img-2.jpeg)

Fig 3. The substructures of $\mathrm{KDB}_{7}$ (a) and $\mathrm{KDB}_{O}$ (b) for $\left\{X_{8}, X_{6}, X_{9}\right\}$ learned from Case $1=\left(x_{19}=43, x_{23}=47, x_{22}=1.26, x_{20}=2, x_{21}=59, x_{12}=y, x_{13}=y, x_{6}=\right.$ $\left.t, x_{14}=y, x_{15}=y, x_{16}=y, x_{5}=f, x_{24}=?, x_{17}=n, x_{1}=f, x_{0}=F, x_{18}=28, x_{4}=f, x_{2}=f, x_{8}=f, x_{11}=f, x_{7}=f, x_{9}=t, x_{3}=f, x_{10}=f\right)$. The arcs $X_{6}$ (Query hyperthyroid) $\rightarrow X_{8}$ (Sick), $X_{12}$ (TSH measured) $\rightarrow X_{8}$ (Tumor) in (a) are identified as redundant and removed. As shown in (b), no more attributes with higher ranks are considered as possible parents of $X_{8}$ and $X_{9}$.
https://doi.org/10.1371/journal.pone.0199822.g003
first case that is diagnozed as "hypothyroid" is shown as follows

$$
\begin{aligned}
\text { Case1 }= & \left(x_{19}=43, x_{23}=47, x_{22}=1.26, x_{20}=2, x_{21}=59, x_{12}=y, x_{13}=y, x_{6}=t\right. \\
& \left.x_{14}=y, x_{15}=y, x_{16}=y, x_{5}=f, x_{24}=?, x_{17}=n, x_{1}=f, x_{0}=F, x_{18}=28\right. \\
& \left.x_{4}=f, x_{2}=f, x_{8}=f, x_{11}=f, x_{7}=f, x_{9}=t, x_{3}=f, x_{10}=f\right)
\end{aligned}
$$

where '?' is used to denote a value that is missing or unknown. The attribute values in case 1 have been sorted by comparing $I\left(x_{i} ; Y\right)$. Among them, $x_{19}$ or TSH ranks the highest, thus the level of TSH is closely related to some definite results and further tests will be needed. The full network structure with 25 attributes are too complex ( 47 arcs or conditional dependencies) to explain, so we just select one substructure to clarify. The conditional dependencies in $\mathrm{KDB}_{7}$ and KDB , which focus on attributes $\left\{X_{8}, X_{6}, X_{9}\right\}$, are respectively shown in Figs 3(a) and 4. In Fig 3(a), the testing result of $X_{22}(\mathrm{~T} 4 \mathrm{U})$ can explain why the patient does not feel $\operatorname{sick}\left(X_{8}=f\right)$, thus $X_{6}$ (query on hyperthyroid) does not provide valuable information. The $\operatorname{arc} X_{6} \rightarrow X_{8}$ is removed. By comparing KDB shown in Fig 4 and $\mathrm{KDB}_{O}$ shown in Fig 3(b), the limitation of KDB in precise representation is obvious. Hyperthyroidism is a condition in which thyroid gland produces too much of the hormone thyroxine. One symptom for hyperthyroid is an enlarged thyroid gland, which may appear as a swelling at the base of one's neck. It is reasonable in Fig 3(b) that $X_{9}$ (tumor) is related to $X_{6}$ (query on hyperthyroid) whereas in Fig 4 $X_{9}$ (tumor) is related to $X_{5}$ (query on hypothyroid). To judge the possibility of hypothyroidism, blood tests (including $\operatorname{TSH}\left(X_{12}\right), \mathrm{T} 3\left(X_{20}\right)$ and $\mathrm{T} 4 \mathrm{U}\left(X_{22}\right)$ ) are needed. The close relationships can be clearly seen in Fig 3.

![img-3.jpeg](img-3.jpeg)

Fig 4. The substructure of KDB for $\left\{X_{0}, X_{6}, X_{9}\right\}$ learned from training set. The arc $X_{5}$ (TSH measured) $\rightarrow X_{9}$ (Tumor) is not reasonable when $X_{9}=t$ (i.e., 'true').
https://doi.org/10.1371/journal.pone.0199822.g004

The detail of the second instance that is diagnozed as "negative" is shown as follows,

$$
\begin{aligned}
\text { Case2 }= & \left(x_{23}=51, x_{21}=37, x_{20}=0.5, x_{19}=9.7, x_{22}=0.72, x_{13}=y, x_{12}=y, x_{1}=t\right. \\
& x_{14}=y, x_{15}=y, x_{16}=y, x_{5}=f, x_{0}=F, x_{24}=?, x_{17}=n, x_{4}=f, x_{18}=46 \\
& \left.x_{6}=f, x_{8}=f, x_{2}=f, x_{11}=f, x_{9}=f, x_{7}=f, x_{3}=f, x_{10}=f\right)
\end{aligned}
$$

The conditional dependencies in $\mathrm{KDB}_{T}$ and KDB , which focus on attributes $\left\{X_{1}, X_{15}, X_{16}\right\}$, are respectively shown in Figs 5(a) and 6. The information implicated in some attribute values may overlap or even cover that in other attribute values. For example, "TSH measured $=y$ " is a premise of "TSH = 4.6". "Sex $=F$ " is a premise of "Pregnant $=t$ ". Although there exist strong dependencies between these attribute values and they may appear simultaneously as the coparents of some attributes, this kind of dependencies are redundant and should be substituted. The $\operatorname{arc} X_{12} \rightarrow X_{1}$ is removed from Fig 5(a) and we should find another parent for $X_{1}$ as shown in Fig 5(b). To provide accurate diagnosis for hypothyroid, the blood tests of TT4 and FTI are always used simultaneously. Thus the $\operatorname{arc} X_{15} \rightarrow X_{16}$ is also redundant and should be removed. The limitation of KDB in scalability is obvious. As shown in Fig 6, the value of $X_{13}$ (T3 measured) is a premise of the value of $X_{20}(\mathrm{~T} 3)$. When they appear as the co-parents of some other attribute, e.g., $X_{1}$, the conditional probability $P\left(x_{1} \mid x_{13}, x_{20}, y\right)$ will approximate the estimate of $P\left(x_{1} \mid x_{20}, y\right) . X_{13}$ (T3 measured) cannot provide any valuable information to $X_{1}$.

# Conclusion and future work 

$\mathrm{KDB}_{T}$ takes instance $\mathcal{P}$ as the target and its network structure describes the dependency relationships in $\mathcal{P}$. Because of the computational overhead, only a limited number of dependencies, which are determined by parameter $k$, can be described by $\mathrm{KDB}_{T}$. The proposed approach, RDE, is a filter that transforms the testing instance to substitute these redundant

![img-4.jpeg](img-4.jpeg)

**Fig 5. The substructures of KDB<sub>c</sub> (a) and KDB<sub>H</sub> (b) for {X<sub>1</sub>, X<sub>13</sub>, X<sub>16</sub>} learned from Case2 = (x<sub>23</sub> = 51, x<sub>21</sub> = 37, x<sub>20</sub> = 0.5, x<sub>19</sub> = 9.7, x<sub>22</sub> = 0.72, x<sub>13</sub> = y, x<sub>12</sub> = y, x<sub>1</sub> = t, x<sub>14</sub> = y, x<sub>15</sub> = y, x<sub>16</sub> = y, x<sub>5</sub> = f, x<sub>0</sub> = F, x<sub>24</sub> = ?, x<sub>17</sub> = n, x<sub>4</sub> = f, x<sub>18</sub> = 46, x<sub>6</sub> = f, x<sub>8</sub> = f, x<sub>2</sub> = f, x<sub>11</sub> = f, x<sub>9</sub> = f, x<sub>7</sub> = f, x<sub>3</sub> = f, x<sub>10</sub> = f)**. The arcs X<sub>12</sub>(TSH measured) → X<sub>15</sub>(Query hypothyroid) and X<sub>15</sub>(T4U measured) → X<sub>16</sub>(FTI measured) in (a) are identified as redundant and removed. No more attributes with higher ranks are considered as possible parents of X<sub>15</sub> and X<sub>16</sub>. Arc X<sub>12</sub>(TSH measured) → X<sub>1</sub>(On thyroxine) is substituted with arc X<sub>20</sub>(T3) → X<sub>1</sub>(On thyroxine).

<https://doi.org/10.1371/journal.pone.0199822.g005>

![img-5.jpeg](img-5.jpeg)

**Fig 6. The substructure of KDB for {X<sub>1</sub>, X<sub>13</sub>, X<sub>16</sub}.** The arc X<sub>13</sub> (T3 measured) → X<sub>1</sub> (On thyroxine) is redundant since the information provided by X<sub>20</sub> (T3) includes the information provided by X<sub>13</sub> (T3 measured).

<https://doi.org/10.1371/journal.pone.0199822.g006>

dependencies with other dependencies at classification time. The experimental results show that the classification accuracy (or zero-one loss) and robustness (bias and variance) are significantly enhanced by the addition of RDE. Besides, the dependency relationships that RDE identified in testing instance are irrelevant to class label, thus it is especially applicable to imbalanced data, e.g. Dis and Hypothyroid. That may be the main reason why RDE obtains the highest AUC values among all the BNCs on the datasets Dis and Hypothyroid.

RDE searches for the mapping relationships between specific attribute values and then identifies redundant ones. Thus it is suited to probabilistic techniques which deal with discrete attributes, such as KDB. RDE can also be extended to deal with continuous attributes. One possible solution is that, if the conditional probability density function $p\left(x_{j} \mid x_{i}\right)$ is relatively high (or greater than a specified value $\delta$ ) then the mapping relationship $x_{i} \rightarrow x_{j}$ is supposed to exist and $x_{j}$ is redundant. The estimation of $p\left(x_{j} \mid x_{i}\right)$ should be learned reliably from training data and the data size should be very large. Although the estimation of $p\left(x_{j} \mid x_{i}\right)$ will be time-consuming and more experimental study is needed to determine the value of $\delta$ for different attributes, the research work on extending RDE is still very promising.

# Author Contributions 

Formal analysis: DingBo Duan.
Investigation: Hua Lou.
Methodology: Hua Lou.
Resources: LiMin Wang, Musa Mammadov.
Software: LiMin Wang, DingBo Duan, Cheng Yang.
Validation: Cheng Yang, Musa Mammadov.
Writing - original draft: Hua Lou, LiMin Wang, Musa Mammadov.
