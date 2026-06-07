# Classification of High Dimensionality Data through Feature Selection Using Markov Blanket 

Junghye Lee, Chi-Hyuck Jun*<br>Department of Industrial and Management Engineering, Pohang University of Science and Technology, Pohang, Korea

(Received: May 4, 2015 / Revised: May 28, 2015 / Accepted: June 6, 2015)


#### Abstract

A classification task requires an exponentially growing amount of computation time and number of observations as the variable dimensionality increases. Thus, reducing the dimensionality of the data is essential when the number of observations is limited. Often, dimensionality reduction or feature selection leads to better classification performance than using the whole number of features. In this paper, we study the possibility of utilizing the Markov blanket discovery algorithm as a new feature selection method. The Markov blanket of a target variable is the minimal variable set for explaining the target variable on the basis of conditional independence of all the variables to be connected in a Bayesian network. We apply several Markov blanket discovery algorithms to some high-dimensional categorical and continuous data sets, and compare their classification performance with other feature selection methods using wellknown classifiers.


Keywords: Feature Selection, Classification, High Dimensionality Data, Markov Blanket

* Corresponding Author, E-mail: chjun@postech.ac.kr


## 1. INTRODUCTION

A classification problem is to predict a target variable of an observation on the basis of the features involved. When dealing with this problem, one of the most important things to consider is dimensionality reduction. If the number of features increases, the accuracy of classification generally increases also. However, this applies only when the number of observations is infinitely many. Exponential growth in the number of observations is required to accurately estimate a function for the target variable as the dimension increases. It is called the curse of dimensionality. In the actual data, however, since there are a finite number of observations, the accuracy of classification may decrease from the moment that the number of features exceeds a certain threshold because features, which are less relevant to the target variable, play a role in disturbing the classification in a finite number of observations. Successful re-
duction of dimensionality can achieve higher classification accuracy than using the entire features. Moreover, dimensionality reduction brings additional benefits such as reducing the time and memory complexity. Research on dimensionality reduction has been recognized as significant and it has been carried out very actively.

Two basic types of dimensionality reduction include feature extraction and feature selection. Feature extraction is transforming the existing features into a lower dimensional space. On the other hand, feature selection is selecting a subset of the existing features without a transformation. The representative techniques of feature extraction are Principal Component Analysis (PCA) and Linear Discriminant Analysis (LDA) which assume the linearity of the function. Also, nonlinear methods using kernels and other varieties are available such as ISO maps. Feature selection is divided into three categories filter methods, wrapper methods, and embedded methods (Guyon and Elisseeff, 2003; Saeys et al., 2005).

Each method has its own advantages and disadvantages. In this paper, we focus on the filter methods which are relatively simple and fast in computation. Furthermore, these methods can be tested by any classifier since feature selection task is executed independently of the classifier.

The Markov blanket feature selection method belongs to a filter method. Koller and Sahami (1996) defined that the Markov blanket of a target variable is the minimal set of features conditioned on which all other features are independent of the target variable in a probabilistic graphical model. In other words, the Markov blanket of a target variable is the minimum information to explain the target variable fully. Based on this, the Markov blanket can be utilized as a feature selection method when the target variable is a class variable.

The usefulness of Markov blanket feature selection has been demonstrated in a few papers (Zeng et al., 2009), but the classification performance has not been reported extensively. In this paper, we compare three algorithms of Markov blanket discovery to test how they perform in classifying high-dimensional categorical and continuous data. These algorithms include Incremental Association Markov Blanket (IAMB) (Tsamardinos et al., 2003a), Max-Min Markov Blanket (MMMB) (Tsamardinos et al., 2003b), and HITON Markov Blanket (HITON-MB) (Aliferis et al., 2003a). Common classifiers are considered such as Naïve Bayes (NB), support vector machine (SVM), and $k$-nearest neighborhood (KNN). When comparing the classification performance, we also include two other feature selection methods: Correlation-based Feature Selection (CFS) (Hall, 1999) and two versions of Minimum Redundancy Maximum Relevance (MRMR) method (Ding and Peng, 2005).

In Section 2, Markov blanket is defined in the context of a probabilistic graphical model called a Bayesian network. Then in Section 3, we introduce three Markov blanket discovery algorithms for feature selection. Section 4 provides a description of two other feature selection methods which are compared with Markov blanket algorithms, and describes several classifiers which are used in this paper. In Section 5, we report the classification performance of each feature selection method combined with each classifier, which is applied to four categorical data sets and four continuous data sets. In Section 6 we conclude the paper with a summary of observations from the experiments.

## 2. BAYESIAN NETWORK AND MARKOV BLANKET

A Bayesian network is a probabilistic graphical model that compactly represents a joint probability distribution $P$ over a set of random variables $U$ via a directed acyclic graph (DAG) $G$. Its nodes represent random variables and the edges involve conditional dependencies between nodes. If the Markov condition property
holds in a Bayesian network, then a node is independent from all nodes other than its descendants when conditioned on its parents (Pearl, 1988). Therefore, a Bayesian network consists of a qualitative part in the form of a DAG and a quantitative part in the form of conditional probabilities (Van Harmelen et al., 2008).

All Markov blanket discovery algorithms begin with two basic assumptions. The first is correctness of a conditional independence test, which means that we always obtain the correct result by the conditional independence test. The second assumption is faithfulness between a Bayesian network $G$ and a joint distribution $P$, which indicates that every conditional independence entailed by the graph $G$ and the Markov condition have to be presented in $P$ (Fu and Desmarais, 2008; Fu and Desmarais, 2010; Pearl, 1988).

Now, the Markov blanket is defined formally as follows (Fu and Desmarais, 2010):

## - Definition 1 (Markov Blanket)

Given the faithfulness assumption, from the perspective of the probability, the Markov Blanket of a target variable $T$, denoted by $M B(T)$, is the minimal set of variables conditioned on which all other variables $F$ are independent of $T$. In the graphical perspective, the Markov blanket of $T$ is the union of parent, child $(P C)$, and parent of children, spouse $(S P)$, nodes of $T$. For example, in Figure 1, the parent and child nodes of $T$ are $P C(T)=\{\mathrm{A}$, $B, C\}$, and the spouse node is $S P(T)=\{D\}$. So, the Markov blanket for $T$ is $M B(T)=\{A, B, C, D\}$. It means that nodes $E, F$, and $G$ are independent of $T$ conditioned on $M B(T)$ (Fu and Desmarais, 2010).

## 3. MARKOV BLANKET DISCOVERY ALGORITHMS AS FEATURE SELECTION METHODS

In this section, three algorithms for Markov blanket discovery are introduced. In the algorithm, $(X \perp Y \mid \boldsymbol{Z})$ represents that $X$ and $Y$ are independent given a node set of $\boldsymbol{Z}$ and $\operatorname{dep}(X, Y \mid \boldsymbol{Z})$ is the degree (or score) of the dependence between $X$ and $Y$ given $\boldsymbol{Z}$ which is $p$-value of a conditional independence test. In the case of cate-
![img-0.jpeg](img-0.jpeg)

Figure 1. An example Bayesian network.

gorical variables, all of the Markov blanket discovery algorithms implement a $G^{2}$ conditional independence test (McDonald, 2009). On the other hand, in the case of continuous variables, they conduct a conditional independence test based on Fisher's $z$-transformation of the partial correlation coefficient.

### 3.1 Incremental Association Markov Blanket

The IAMB algorithm (Tsamardinos et al., 2003a) is the basic algorithm to discover the Markov blanket. Figure 2 is the pseudo code of IAMB. It is a grow-andshrink approach that consists of two phases. In the first grow phase, nodes determined to be dependent on the target node are added to $M B$ through the independence test (lines 2-6). In the next shrink phase, any node among $M B$ determined to be independent of the target node is removed from $M B$ (line 7-9).

Tsamardinos et al. (2003a) proved that IAMB satisfies soundness (correctness) under the faithfulness assumption. In order to achieve a reliable result from the algorithm, independence tests have to be correct, which means that they conclude (in)dependence if and only if the (in)dependence holds in $P$. However, IAMB has a drawback in terms of the data efficiency (Peña et al., 2007). IAMB is known to give a reliable result in discovering MB when the amount of instances is at least five times the degree of freedom in the test. In other words, IAMB requires that the number of instances increases exponentially according to the size of MB because the degree of freedom in the test is exponentially increasing in the size of the conditioning set, and the size of the conditioning set is the same as MB in IAMB.

### 3.2 Max-Min Markov Blanket

The MMMB algorithm (Tsamardinos et al., 2003b) tries to overcome the data inefficiency of IAMB while

```
\(\operatorname{IAMB}(T)\)
/* add true positives to MB */
\(1 \quad M B=\varnothing\)
2 repeat
\(3 \quad Y=\arg : \max _{X \in\left(U \backslash M B \backslash\{Y\}\right)} \operatorname{dep}\left(T, X \mid M B\right)\)
4 if \(T \not \subset Y \mid M B\) then
\(5 \quad M B=M B \cup\{Y\}\)
6 until \(M B\) does not change
/* remove false positives from MB */
7 for each \(X \in M B\) do
8 if \(T \perp X \mid(M B \backslash\{X\})\) then
\(9 \quad M B=M B \backslash\{X\}\)
10 return \(M B\)
```

Figure 2. IAMB algorithm.
still being scalable given the faithfulness assumption. MMMB is also divided into two phases, but it takes the divide-and-conquer approach which is different from IAMB in terms of using topological information. At the first phase (called MMPC), parent and child nodes of $T$ are identified, and then the spouse nodes of $T$ are to be found in MMMB phase. Not all nodes, although determined to be dependent on the target node in the test, may be included into the MB. Figure 3 is the pseudo code of MMMB. However, as stated in Pena et al. (2007), the MMMB algorithm does not guarantee the correct output under the faithfulness, but it works well in practical applications. Compared to IAMB, MMMB is slow because MMPC considers every subset of the output as the conditioning set for the tests (line 4 in MMPC (T)).

### 3.3 HITON Markov Blanket

The HITON-MB algorithm (Aliferis et al., 2003a) is similar to MMMB in terms of data efficiency, sound-

```
\(\operatorname{MMPC}(T)\)
/* add true positives to \(\mathrm{PC}^{* /}\)
\(1 \quad P C=\varnothing\)
2 repeat
3 for each \(X \in(U \backslash M B \backslash\{T\})\) do
\(4 \quad \operatorname{Sep}[X]=\arg : \max _{X \subseteq P C} \operatorname{dep}(T, X \mid \mathbb{Z})\)
\(5 \quad Y=\arg : \max _{X \in\left(U \backslash P C \backslash\{T\}\right)} \operatorname{dep}(T, X \mid \operatorname{Sep}[X])\)
\(6 \quad\) if \(T \not \subset Y \mid \operatorname{Sep}[Y]\) then
\(7 \quad P C=P C \cup\{Y\}\)
8 until \(P C\) does not change
/* remove false positives from \(\mathrm{PC}^{* /}\)
9 for each \(X \in P C\) do
10 if \(T \perp X \mid \mathbb{Z}\) for some \(\mathbb{Z} \subseteq P C \backslash\{X\}\) then
\(11 \quad P C=P C \cup\{X\}\)
12 return \(P C\)
\(\operatorname{MMMB}(T)\)
/* add true positives to \(M B^{*} /\)
\(1 \quad P C=M M P C(T)\)
\(2 \quad M B=P C\)
\(3 \quad \operatorname{Can} M B=\left(P C \cup_{X \in P C} M M P C(X)\right) \backslash\{T\}\)
\(/^{*}\) add more true positives to \(M B^{*} /\)
4 for each \(X \in \operatorname{Can} M B \backslash P C\) do
5 find any \(\mathbb{Z}\) such that \(T \perp X \mid \mathbb{Z}\) and \(T, X \notin \mathbb{Z}\)
\(6 \quad\) for each \(Y \in P C\) do
\(7 \quad\) if \(T \not \subset X \mid \mathbb{Z} \cup\{Y\}\) then
\(8 \quad M B=M B \cup\{X\}\)
\(9 \quad\) return \(M B\)
```

Figure 3. MMMB algorithm.


Figure 4. HITON-MB algorithm.
ness, and time complexity. Like MMMB, HITON-MB takes a divide-and-conquer approach to identifying MB: first finding PC and then, finding SP. Figure 4 is the pseudo code of HITON-MB. The algorithm proceeds in the same manner as MMMB except that it combines addition and removal steps in a same loop for the purpose of removing false positives as early as possible to make the conditioning set small. However, Pena et al. (2007) proved that HITON-MB does not guarantee the correct output under the faithfulness. Since HITON-MB uses the topology of G in the same manner as MMMB, it returns similar results with MMMB.

## 4. OTHER FEATURE SELECTION METHODS AND CLASSIFIERS UNDER CONSIDERATION

In this section, first, we briefly describe the other feature selection methods which will be compared with Markov blanket feature selection methods described in Section 3, and then explain the commonly used classifiers which are adopted in this paper for the experiment.

### 4.1 Other Feature Selection Methods

The feature selection methods to be described in this section are selected because these are multivariate filter methods which are popular in the area of bioinformatics. Just like the Markov blanket feature selection methods, these feature selection methods can be applied to both categorical and continuous data.

### 4.1.1 Correlation-based Feature Selection

CFS considers every subset of all features, which is based on the following philosophy: a good feature subset contains features which are highly correlated with the target (class) variable and not redundant between them (Hall, 1999). Consider a subset S of all features, which consists of k features $f_{1}, \cdots, f_{k}$. Let $r_{f_{i} f_{j}}$ be the correlation coefficient of $f_{i}$ and $f_{j}$ and let $r_{i f_{i}}$ be the correlation coefficient between the target (class) variable and $f_{i}$. Then, the CFS is to find the subset having the following maximum score.

$$
C F S=\max _{s}\left[\frac{r_{i f_{1}}+r_{i f_{2}}+\cdots+r_{i f_{k}}}{\sqrt{k+2\left(r_{f_{1} f_{2}}+\cdots+r_{f_{i} f_{j}}+\cdots+r_{f_{k-1} f_{k}}\right)}}\right]
$$

CFS can be run on Weka (Hall et al., 2009) with a best first search strategy. Like the greedy hill climbing, the best first search strategy moves through the search space by making local changes to the current feature subset. However, unlike the hill climbing, if the path being explored begins to look less promising, the best first search can back-track to a more promising previous subset and continue the search from there.

### 4.1.2 Minimum Redundancy Maximum Relevance

Ding and Peng (2005) developed the MRMR method which ranks features considering their relevance to the class variable and redundancy within features simultaneously. Top ranked features have larger relevance to the class variable and smaller redundancy within features, and they are regarded as more significant than others. Due to the ranking process, MRMR provides the right of choice for the number of features. MRMR method has two kinds of schemes to search for the next feature depending on the data type.

For categorical data features, the relevance of a feature to the class variable $c$ is evaluated by the mutual information value between a feature and the class variable, which is denoted by $R f_{i}, c$ ). Mutual Information Difference (MID) and Mutual Information Quotient (MIQ) are defined, respectively, by

$$
M I D=\max _{f_{i} \in \mathrm{O}_{c}}\left[I\left(f_{i}, c\right)-\frac{1}{|S|} \sum_{f_{j} \in S} I\left(f_{i}, f_{j}\right)\right]
$$

$$
M I Q=\max _{f_{i} \in \Omega_{s}}\left[I\left(f_{i}, c\right) / \frac{1}{|S|} \sum_{f_{j} \in S} I\left(f_{i}, f_{j}\right)\right]
$$

where the second term in the bracket is the average of all mutual information values between feature $f_{i}$ and other features in S which represents the redundancy of $f_{i}$.

For continuous data features, the F-statistic is used as a measure of relevance between a feature and the class variable, which has the following form (Ding and Peng, 2005; Ding, 2002).

$$
F\left(f_{i}, c\right)=\left[\Sigma_{k} n_{k}\left(\bar{v}_{i k}-\bar{v}_{i}\right)^{2} /(K-1)\right] / \sigma^{2}
$$

where $\bar{v}_{i}$ is the average across all observations in $f_{i}, \bar{v}_{i k}$ is the average of $f_{i}$ within the $k$-th class $(k=1, \cdots, K)$, and $\sigma^{2}=\left|\Sigma_{k}\left(n_{k}-1\right)\right| \sigma_{k}^{2} \mid /(n-K)$ is the pooled variance $\left(n_{k}\right.$ and $\left.\bar{\sigma}_{k}^{2}\right)$ are the size and the variance of the $k$-th class, respectively). For $K=2$, the $F$ statistic will reduce to the $t$ statistic, with the relation $F=t^{2}$. On the other hand, as a measure of redundancy, the absolute value of Pearson correlation coefficient of $f_{i}$ and $f_{j}$, which is denoted by $c\left(f_{i}, f_{j}\right)$, is chosen. Hence the F-test correlation difference (FCD) and the F-test correlation quotient (FCQ) can be defined as follows.

$$
\begin{gathered}
F C D=\max _{f_{i} \in \Omega_{s}}\left[F\left(f_{i}, c\right)-\frac{1}{|S|} \sum_{f_{j} \in S} c\left(f_{i}, f_{j}\right)\right] \\
F C Q=\max _{f_{i} \in \Omega_{s}}\left[F\left(f_{i}, c\right) / \frac{1}{|S|} \sum_{f_{j} \in S} c\left(f_{i}, f_{j}\right)\right]
\end{gathered}
$$

### 4.2 Classifiers under Consideration

Classifiers described in this section are selected since they are commonly used and easy to implement. The first two classifiers are parametric methods, and the last classifier is nonparametric. Because the model complexity of nonparametric methods is relatively high, the KNN may cause an over-fitting problem.

### 4.2.1 Naïve Bayes

The NB classifier is a simplified version of evaluating the posterior probability of each class for the classification purpose (Zhang, 2004). Suppose an observed instance consists of $p$-dimensional feature $f=\left(f_{1}, f_{2}\right.$, $\left.\cdots, f_{p}\right)$. Then, using the Bayes' rule, the posterior probability of $j$-th class, denoted by $p\left(c_{1} \mid f_{1}, f_{2}, \cdots, f_{p}\right)$, can be calculated:

$$
p\left(c_{j} \mid f_{1}, f_{2}, \cdots, f_{p}\right) \propto p\left(f_{1}, f_{2}, \cdots, f_{p} \mid c_{j}\right) p\left(c_{j}\right)
$$

where $p\left(f_{1}, f_{2}, \cdots, f_{p} \mid c_{j}\right)$ is the likelihood and $p\left(c_{j}\right)$ is the prior probability of each class. The goal of the Bayes' rule is to find the decision boundary that every instance is assigned to the class with the highest posterior prob-
ability. The key assumption of the naïve Bayes is that conditioned on the class, the distribution of input features $f_{1}, f_{2}, \cdots, f_{p}$ is independent. Due to the assumption, the likelihood can be expressed in a product form:

$$
p\left(f_{1}, f_{2}, \cdots, f_{p} \mid c_{j}\right) \propto \prod_{k=1}^{p} p\left(f_{k} \mid c_{j}\right)
$$

Although it is simple and straightforward to implement, the NB is often well-performed, more so than the sophisticated classification methods.

### 4.2.2 Support Vector Machine

Vapnik and Cortes (1995) first invented the SVM. Its performance has been increasingly recognized and it has become one of the most powerful classification methods. Under $p$-dimensional input feature space, for the two-class problem, SVM seeks the two parallel hyperplanes which maximize the distance (or margin) between them and the ( $p-1$ )-dimensional hyperplane placed in the middle of the two parallel hyperplanes plays the role of a discriminant function. SVM is based on the hypothesis that the larger the margin between these parallel hyperplanes, the better the performance of the classifier will be. These hyperplanes can be derived by solving optimally a quadratic programming. One advantage of SVM is to consider a nonlinearity of data by introducing a variety of kernel functions. In this study, however, we do not use any kernel function.

### 4.2.3 $k$-nearest Neighborhood

The $k$-nearest neighborhood ( KNN ) method was first introduced by Fix and Hodges (1989). Since it is a non-parametric method for classifying an instance based on $k$ closest instances, a similarity measure (Euclidean distance or others) is calculated between all pairs of instances in a dataset. Whenever a new data point has to be classified, its $k$-closest neighbors are found from the training data ( $k$ being the number of neighbors) by sorting the distance matrix. The most dominant class label in the set of neighbors is finally assigned to the new data. The best choice of $k$ depends upon the data. Larger values of $k$ reduce the effect of noise on the classification but make boundaries between classes less distinct. Generally, $k$ is often chosen close to the square root of the data size (Fukunaga, 1990). In this paper, we change $k$ from 1 to 10 , and then the best result of $k$ is recorded.

## 5. EXPERIMENTS

This section describes our experiments on four categorical data sets and four continuous data sets, and reports their classification performance results, at first, using three Markov Blanket discovery methods introduced in Section 3 and three other feature selection methods in Section 4. Then, three classifiers, including naïve Bayes, support vector machine, and $k$-nearest

neighborhood, are applied to each selected feature set. Therefore, 18 classification models are executed for each data set basically. To avoid the bias between the training and test data, we compare each model by averaging 5 runs of 5 -fold cross validation. All other algorithms except CFS are run in Matlab. CFS is run in Weka with a best first search strategy. For MB discovery algorithms, we used the Matlab version of Causal Explorer toolkit (Aliferis et al., 2003b). However, MMMB is not available for continuous data. We experimented on the MB feature selection methods with different significant levels. The significant level is used for implementing the conditional independence test, and it may result in a different output of the selected features. Since the MRMR method is based on ranking process, the number of features needs to be fixed beforehand. Two or three levels are considered here depending on the number of all features. For example, in the Audiology data set having a total of 69 features; 20,10 , and 5 features are selected in MRMR to keep the balance with the number of selected features in MB.

### 5.1 Categorical Data

For categorical data, three data sets, Audiology, Promoter, and Splice, were selected from the UCI repository of machine learning; and the other data set, Lung Cancer, is from Causality Workbench repository (Guyon et al., 2011). The information about the data sets is summarized in Table 1. The Audiology data set
contains 69 features and one class variable divided into 24 classes, which is to predict the auditory state. The Promoter data set is to determine whether it is a promoter or not, using the information of gene sequences. The Splice data set is a type similar to the Promoter data set. The Lung Cancer data set is to predict lung cancer, using generic health status variables such as smoking and fatigue.

Tables 2-5 show the classification result of each data set, which includes the number of features selected, classification accuracies of test data and those of training data (numbers in parenthesis) in percentage. The best performing feature selection method for each classifier is marked in bold numbers. In Table 2, IAMB with $5 \%$ significance level outperforms other feature selection methods for all classifiers with a significantly large gap. This result is remarkable when considering that this data set contains a large number of classes as many as 24. Using only 8 features, IAMB records the best accuracy among the feature selection methods, and it even has better performance than the entire features. For this data set, MMMB and HITON-MB do not provide any MB, so the results are not reported here. This tells us about some drawbacks of MMMB and HITON-MB although they use topology information differently from IAMB.

Tables 3, 4 and 5 show the similar results for Promoter, Splice and Lung Cancer data sets, respectively. In Tables 3-5, the results based on the MB feature selection methods are generally well-performed. Sometimes

Table 1. Categorical data sets for experiments


Table 2. Performance comparison for Audiology data set


Table 3. Performance comparison for promoter data set


Table 4. Performance comparison for splice data set


MB does not return the best accuracy but there is not a big difference. We note that MMMB and HITON-MB discover almost the same MB. Even though the MB feature selection methods do not guarantee to provide the best solution in all data sets, their usefulness is still evident since the selection method reduces the number of features significantly while maintaining the good performance. Among these MB discovery algorithms, IAMB generally performs well for all these categorical data sets.

### 5.2 Continuous data

For continuous data, all data sets are from Kent Ridge Bio-medical repository ( Li and Liu, 2002). The
information about the data sets is in Table 6. All continuous data sets are microarray gene expression data, which are high-dimensional in features having relatively small number of observations. The AML/ALL data set is to predict the presence of acute myeloid leukemia or acute lymphoblastic leukemia. Colon Cancer, Prostate Cancer and Ovarian Cancer data sets are to predict colon cancer, prostate cancer and ovarian cancer of patients, respectively.

Tables 7-10 show the performance result for each data set of each classification model, which includes the number of features selected, classification accuracy of the test data and accuracy of the training data (in parenthesis). The best performing feature selection method for each classifier is marked in bold numbers.

Table 5. Performance comparison for Lung cancer data set


Table 6. Continuous data sets for experiments


Table 7. Performance comparison for AML/ALL data set


It is observed in Tables 7-10 that the MB feature selection methods perform quite well for these continuous data sets when combined with suitable classifiers. It seems that IAMB extracts more features than HITONMB for these continuous data sets. For the AML/ALL data set, the CFS method shows the best performance when combined with the classifier SVM or KNN, but the MB feature selection methods show relatively good results. For this data set, HITON-MB having $1 \%$ significance level produce better performance than any other feature selection methods when combined with the classifier NB. It should be noted that IAMB achieves the best performance for the Colon Cancer data set using only
three features out of two thousands. For the Prostate and Ovarian Cancer data sets, the MB feature selection methods generally produce better performance. When comparing the CFS method with the MRMR method, the former generally performs better than the latter in these data sets.

## 6. CONCLUSION

We have shown that Markov blanket discovery algorithms can be utilized as feature selection methods by constructing a minimal set of features from a Bayesian network formed by the whole variables. Moreover, Mar-

Table 8. Performance comparison for Colon Cancer data set


Table 9. Performance comparison for Prostate Cancer data set


Table 10. Performance comparison for Ovarian Cancer data set


kov blanket discovery algorithms are shown to be competitive in the classification performance as compared to other popular feature selection methods in the experiments with categorical and continuous data sets. Among these MB discovery algorithms, the IAMB algorithm, which is simplest, generally performs quite well for all categorical and continuous data sets considered.

## ACKNOWLEDGEMENTS

This research was supported by a grant of the Korea Health technology R\&D Project through the Korea Health Industry Development Institute (KHIDI), funded by the Ministry of Health and Welfare, Republic of Korea (Grant Number: HI13C-0790-010013).
