# Locally Weighted Learning: How and When Does it Work in Bayesian Networks? 

Jia Wu ${ }^{1}$, Bi Wu ${ }^{3}$, Shirui Pan ${ }^{2}$, Haishuai Wang ${ }^{2}$, Zhihua Cai ${ }^{1 *}$<br>${ }^{1}$ School of Computer Science, China University of Geosciences, Wuhan 430074, China<br>${ }^{2}$ Quantum Computation \& Intelligent Systems Centre, University of Technology Sydney, Australia<br>${ }^{3}$ School of Computer Science and Engineering, Wuhan Institute of Technology, Wuhan 430073, China

Received 12 February 2015
Accepted 27 October 2015


#### Abstract

Bayesian network (BN), a simple graphical notation for conditional independence assertions, is promised to represent the probabilistic relationships between diseases and symptoms. Learning the structure of a Bayesian network classifier (BNC) encodes conditional independence assumption between attributes, which may deteriorate the classification performance. One major approach to mitigate the BNC's primary weakness (the attributes independence assumption) is the locally weighted approach. And this type of approach has been proved to achieve good performance for naive Bayes, a BNC with simple structure. However, we do not know whether or how effective it works for improving the performance of the complex BNC. In this paper, we first do a survey on the complex structure models for BNCs and their improvements, then carry out a systematically experimental analysis to investigate the effectiveness of locally weighted method for complex BNCs, e.g., tree-augmented naive Bayes (TAN), averaged one-dependence estimators AODE and hidden naive Bayes (HNB), measured by classification accuracy (ACC) and the area under the ROC curve ranking (AUC). Experiments and comparisons on 36 benchmark data sets collected from University of California, Irvine (UCI) in Weka system demonstrate that locally weighting technologies just slightly outperforms unweighted complex BNCs on ACC and AUC. In other words, although locally weighting could significantly improve the performance of NB (a BNC with simple structure), it could not work well on BNCs with complex structures. This is because the performance improvements of BNCs are attributed to their structures not the locally weighting.


Keywords: Bayesian Network, Locally Weighted Learning, Ranking, Classification

## 1. Introduction

Bayesian network (BN), which can be regarded as an annotated directed graph that encodes the probabilistic relationships among variables of interest ${ }^{7}$, is a popular data mining technique used to predict the class of a test instance in classification. Each node corresponds to a variable, and the conditional probability table (CPT) associated with it contains

[^0]the probability of each state of the variable given every possible combination of states of its parents. Moreover, each node is conditionally independent of its non-descendants given its parents. And the BN structure can be exploited by the explicit representation of probabilistic relations in BN for a given problem domain. In this way, it makes incorporating domain knowledge in the BN model design easier. In addition, the intuitive graphical represen-


[^0]:    *Corresponding: zhcai@cug.edu.cn.

tation of BN is very beneficial in decomposing a large and complex problem representation into several smaller, self-contained models.

The BN has been applied in many application areas including computational molecular biology ${ }^{20}$, computer vision ${ }^{21}$, relational databases ${ }^{19}$, text processing ${ }^{11}$, image processing ${ }^{46}$ and sensor fusion ${ }^{5}$. In the BN classification problem, a Bayesian network classifier (BNC) from a given set of labeled training instances that are represented by a tuple of attribute variables should be constructed in order to predict the distribution of the class variable. Learning BNC has become an active research in the past decade. The two issues of learning BNC are the structure of the network (structure learning) and the set of CPTs (parameter learning). Structure learning often has high computational complexity due to the extremely huge number of possible structures. Thus, heuristic and approximate learning algorithms are the realistic solution. A variety of learning algorithms have been proposed ${ }^{26}$. Moreover, it has been observed that learning an unrestricted Bayesian network classifier seems to not necessarily lead to a classifier with good performance. For example, Friedman et al. ${ }^{4}$ observed that unrestricted Bayesian network classifiers do not outperform naive Bayes, the simplest Bayesian network classifier, on a large sample of benchmark data sets. One major reason is that the resulting network tends to have a complex structure, and thus has high variance because of the inaccurate probability estimation caused by the limited amount of training examples. So, learning restricted Bayesian network classifiers is a more realistic solution.

In this paper, we assume that the $A_{i}, i=$ $1,2, \cdots, n$, are n attributes. Each instance can be described by the tuple of attribute values $<$ $a_{1}, a_{2}, \cdots, a_{n}>$, where $a_{n}$ denotes the value of the $n$th attribute $A_{n}$. The most probable target value is described as $v_{M A P}$, while $C$ is a finite set building on every target value $c_{j}$. The Bayesian approach for classification is to assign the most probable target value of the test instance. Typically, one set of training instances with class labels are given, a classifier must be learned to predict the class distribution of an instance with its class label unknown. The classifier
represented by Bayesian approach can be defined as:

$$
c_{M A P}=\underset{c_{j} \in C}{\arg \max } P\left(c_{j}\right) P\left(a_{1}, a_{2}, \cdots, a_{n} \mid c_{j}\right)
$$

Assume that all the attributes satisfy the attribute independence assumption, and then the probability of observing the conjunction is just the product of the probabilities for the individual attributes. This is the core concept of naive Bayes, simply NB, as one highly practical Bayesian networks method, as shown in Figure 1. It is easy to estimate $p\left(c_{j}\right)$, opposite to $P\left(a_{1}, a_{2}, \cdots, a_{n} \mid c_{j}\right){ }^{37}$. Unless the number of possible instances in training data is very large, we can not obtain reliable estimates. The corresponding details can be defined as:

$$
c_{N B}=\underset{c_{j} \in C}{\arg \max } P\left(c_{j}\right) \prod_{i=1}^{n} P\left(a_{i} \mid c_{j}\right)
$$

![img-0.jpeg](img-0.jpeg)

Fig. 1. The structure of Naive Bayes (NB).
In NB, each node has a class node as its parent, and it does not have any other parent from other attribute nodes. Constructing naive Bayes network is easy because it only needs to compile a table of class probability estimation $p\left(c_{j}\right)$ and a table of conditional attribute-value probability estimates $P\left(a_{i} \mid c_{j}\right)$ from the training examples.

However, the attribute independence assumption made by naive Bayes harms its classification performance when it is violated in reality. In order to weak the attribute independence assumption of NB while at the same time retaining its simplicity and efficiency, researchers have proposed many effective methods to further improve the performance of NB , which can be broadly divided into the following five main categories ${ }^{13}$ : (1) Structure Extension:

Extending the structure of naive Bayes to represent the dependencies among attributes; (2) Feature Selection: Selecting an attribute subset from the whole space of attributes; (3) Attribute Weighting: Assigning different weights to attributes in building naive Bayes; (4) Local Learning: Employing the principle of local learning to build a local naive Bayes; and (5) Data Expansion: Expanding training data and building a naive Bayes on the expanded training data. It is worth noticing that the attribute weighting ${ }^{40}$ methodizing for naive Bayes has demonstrated good performance ${ }^{36,33,42,31}$.

Specifically, for the structure extension, three methods have been demonstrated to improve the NB to a remarkably accurate level. Selective Naive Bayes (SBC) ${ }^{16}$ demonstrates a remarkable improvement by using the selected subset of variables. Tree Augmented Naive Bayes (TAN) ${ }^{4}$ appears as a natural extension to the naive Bayes classifier. And a Naive Bayes/Decision-Tree Hybrid (NBTree) ${ }^{15}$ has combined a decision tree with naive Bayes. But recently major work on improving NB is called Averaged One-Dependence Estimators, simply AODE ${ }^{29}$, achieving significant success. In AODE, an aggregate of one-dependence classifiers is learned and the prediction is produced by averaging the predictions of all these qualified one-dependence classifiers. Hidden Naive Bayes (HNB) ${ }^{13}$ is another extension of NB, in which a hidden parent is created for each attribute which combines the influences from all other attributes. However, learning an optimal Bayesian network is a NPhard problem ${ }^{2}$.

The locally weighted method has been proved as a effect improvement for naive Bayes due to the studies in the previous works ${ }^{10,27,28}$. However, for the more complex BNC models, such as TAN ${ }^{4}$, AODE ${ }^{29}$ and HNB ${ }^{13}$, locally weighted learning is comparatively less explored. In this case, we could not make sure how much effect the locally weighting make exactly. Moreover, in recent years, the area under the ROC curve ranking (AUC) has attracted considerable attention in data mining community ${ }^{17}$, such as decision tress ${ }^{25}$, naive Bayes ${ }^{18}$ and SVM ${ }^{8}$. Hand and Till ${ }^{6}$ show that, for binary classification, AUC is equivalent to the probability
that a randomly chosen instance of class will have a smaller estimated probability of belonging to positive class than a randomly chosen instance of positive class. In this paper, we systematically analyze the performance of locally weighted complex BNCs (TAN, AODE and HNB) by using locally weighted learning method proposed by Frank et al. ${ }^{3}$. Experiments and comparisons, on 36 UCI benchmark data sets ${ }^{1}$ demonstrate that the locally weighted technologies just slightly outperforms unweighted complex BNCs on ACC and AUC, which means that the locally weighted do not work very well for the complex BNCs.

The rest of the paper is organized as follows. In Section 2, we introduce the Tree Augmented Naive Bayes (TAN), one of the improvement versions of Naive Bayes (NB) on the structure, with the Averaged One-dependence Estimators (AODE) been summarized in Section 3. We also give the details of Hidden Naive Bayes (HNB) in Section 4. In Section 5, we review the related work on locally weighting methods. In Section 6, we describe the experimental conditions, methods, and results in details. Section 7 concludes the paper.

## 2. TAN: Tree Augmented Naive Bayes

Tree Augmented Naive Bayes (TAN) is a seminaive Bayesian learning method. It relaxes the naive Bayes attribute independence assumption by employing a tree structure, in which each attribute only depends on the class and one other attribute. A maximum weighted spanning tree that maximizes the likelihood of the training data is used to perform classification. Moreover, TAN appears as a natural extension to the NB classifier. TAN model is a restricted family of Bayesian networks in which the class variable has no parents and each attribute has as parents the class variable and at most another attribute. TAN outperforms naive Bayes in terms of accuracy ${ }^{4}$ and still maintains a considerably simple structure as shown in Figure 2. The corresponding TAN classifier is defined as follows.

![img-1.jpeg](img-1.jpeg)

Fig. 2. The structure of Tree Augmented Naive Bayes (TAN).

$$
c_{T A N}=\underset{c_{j} \in C}{\arg \max } P\left(c_{j}\right) \prod_{i=1}^{n} P\left(a_{i} \mid p_{a i}, c_{j}\right)
$$

The TAN model has received the widespread attention, due to its excellent performance in data mining in spite of the assumption of one-dependence of attributes. For instance, Zhao et. al, ${ }^{47}$ proposed a new approach of classification under the pessimistic network (PN) framework with TAN, named tree augmented naive possibilistic network classifier (TANPC), which combines the advantages of the PN and TAN. The classifier is built from a training set where instances can be expressed by imperfect attributes and classes. It is able to classify new instances those may have imperfect attributes. Jiang ${ }^{9}$ posed an improving tree augmented naive Bayes for class probability estimation, called Averaged Tree Augmented Naive Bayes (ATAN). The experimental results on a large number of UCI datasets published on the main web site of Weka platform show that ATAN significantly outperforms TAN and all the other algorithms used to compare in terms of conditional log likelihood.

## 3. AODE: Averaged One-dependence Estimators

As discussed above, TAN has high computational complexity at training time. The determinant of its computational profile lead to the development of Averaged One-dependence Estimators, simply AODE ${ }^{29}$. In AODE, an aggregate of one-
dependence classifiers are learned and the prediction is produced by averaging the predictions of all these qualified one-dependence classifiers, as shown in Figure 3. For simplicity, a one-dependence classifier is firstly built for each attribute, in which the attribute is set to be the parent of all other attributes. Then, AODE directly averages the aggregate consisting of many special tree augmented naive Bayes. In addition to having good performance, AODE retains the simplicity and direct theoretical foundation of naive Bayes without incurring the high time. The corresponding AODE classifier is defined as follows:

$$
c_{A O D E}=\underset{c_{j} \in C}{\arg \max }\left(\sum_{i=1}^{n} P\left(a_{i}, c_{i}\right) \prod_{j=1}^{n} P\left(a_{j} \mid a_{i}, c_{j}\right)\right)
$$

In recent years, Jiang had made a lot of related research on AODE. One significant part of research about improving AODE algorithm by Jiang ${ }^{12}$ was Weightily Averaged One-Dependence Estimators, simply WAODE. Wu ${ }^{35}$ proposed an active AODE learning classification model, which is based on the uncertainty sampling and classification accuracy loss sampling strategy. Experimental results on three UCI standard data sets and a real remote sensing data set show that the active AODE can get better classification accuracy with fewer labelled samples than that of the state-of-the-art approaches for active learning. Recently, he also investigated a novel approach to ensemble the single SPODE based on the boosting strategy, boosting for superparent-onedependence estimators, namely BODE ${ }^{32}$.

## 4. HNB: Hidden Naive Bayes

As discussed in previous sections, naive Bayes ignores attribute dependencies. On the other hand, although a Bayesian network can represent arbitrary attribute dependencies, it is intractable to learn it from data ${ }^{43}$. Thus, learning restricted structures, such as TAN, is more practical. However, only one parent is allowed for each attribute in TAN, even though several attributes might have the similar influence on it. The motivation is to develop a new model that can avoid the intractable computational

![img-2.jpeg](img-2.jpeg)

Figure 3: The structure of Averaged One-Dependence Estimators (AODE).
complexity for learning an optimal Bayesian network and still take the influences from all attributes into account. The idea is to create a hidden parent for each attribute, which combines the influences from all other attributes. This model is called hidden naive Bayes (HNB), as shown in Figure 4. It represents an approximation of the joint distribution defined as follows.
![img-3.jpeg](img-3.jpeg)

Fig. 4. The structure of Hidden Naive Bayes (HNB).

$$
c_{H N B}=\underset{c_{j} \in C}{\arg \max } P\left(c_{j}\right) \prod_{j=1}^{n} P\left(a_{i} \mid A_{h i}, c_{j}\right)
$$

where

$$
P\left(a_{i} \mid A_{h i}, c_{j}\right)=\sum_{j=1, j \neq i}^{n} w_{i, j} P\left(a_{i} \mid a_{j}, c_{j}\right)
$$

where $w_{i, j}$ is the conditional weight contributed by attribute $A_{i}$ and $A_{j}$, which can be defined as follows:

$$
w_{i, j}=\frac{I_{p}\left(A_{i} ; A_{j} \mid C\right)}{\sum_{j=1}^{n} I_{p}\left(A_{i} ; A_{j} \mid C\right)}
$$

where $I_{p}\left(A_{i} ; A_{j} \mid C\right)$ is the conditional mutual information between $A_{i}$ and $A_{j}$ given $C$, which could be defined as
$I_{p}\left(A_{i} ; A_{j} \mid C\right)=\sum_{a_{i}, a_{j}, c_{j}} P\left(a_{i}, a_{j}, c_{j}\right) \log \frac{P\left(a_{i}, a_{j} \mid c_{j}\right)}{P\left(a_{i} \mid c_{j}\right) P\left(a_{j} \mid c_{j}\right)}$
In HNB, attribute dependencies are actually represented by hidden parents of attributes. It can be

viewed in such a way that a hidden parent $A_{h i}$ is created for each attribute $A_{i}$. HNB should be an accurate model due to the fact that it can represent the influences on each attribute from all other attributes and assign higher weights to more importance attributes.

## 5. LW: Locally Weighting

The basic idea of the locally weighting approach is building a Bayesian network model on the neighbourhood of the test instance, instead of on the whole training data ${ }^{3}$. Local learning helps to mitigate the effects of attribute dependencies that may exist in the data as a whole and we expect this method to do well if there are no strong dependencies within the neighbourhood of the test instance.

The local learning approach is actually a kind of training data selection approach ${ }^{10}$, namely the selected training instances are dropped into the neighbourhood of the test instance. As naive Bayes requires relatively little data for training, the neighbourhood can be kept small, thereby reducing the chance of encountering strong dependencies. Therefore, although the attribute conditional independence assumption of naive Bayes is always violated on the whole training data, it could be expected that the dependencies within the neighbourhood of the test instance is much weaker than that on the whole training data and thus the conditional independence assumptions required for naive Bayes are likely to be true ${ }^{14}$.

## 6. Experiments

### 6.1. Experimental Settings

In this section, we run our experiments under the framework of Weka ${ }^{30}$ using 36 UCI data sets ${ }^{1}$ to validate the effectiveness of the complex Bayesian networks (TAN, AODE and HNB) with locally weighting. These data sets in format of arff are downloaded from the official website of Weka, which represent a wide range of domains and data characteristics and are described in Table 1. The data among the data sets is preprocessed as the following four steps ${ }^{44,34}$.

1. Replacingmissingattributevalues. We use the unsupervised filter named ReplaceMissingValues to replace all missing values with the modes and means from the training data.
2. Discretizingnumericattributevalues. Numeric attributes are discretized by the filter of Discretize in Weka using unsupervised 10-bin discretization.
3. Removinguselessattributes. Apparently, if the number of values of an attribute is almost equal to the number of examples in a data set, it rarely contributes to classification. Thus, we use the unsupervised filter named Remove in Weka to remove this type of attribute. In these 36 data sets, there are only three such attributes: the attribute "Hospital Number" in the data set "colic.ORIG", the attribute "instance name" in the data set "splice", and the attribute "animal" in the data set "zoo".
4. Samplinglargedatasets. For saving the time of running experiments, we use the unsupervised filter named Resample with the size of 20 percent in Weka to randomly sample each large data set having more than 5,000 examples. In these 36 data sets, there are three such data sets: "letter", "mushroom" and "waveform-5,000".

Moreover, all experiments are conducted on a Linux cluster node with an Interl(R) Xeon(R) @3.33GHZ CPU and 3GB fixed memory size.

### 6.2. Evaluation Criterions

In our experiment, the selected algorithms are evaluated in terms of classification accuracy measured by ACC and ranking performance measured by AUC. The ACC of each method is calculated by the percentage of successful predictions on the text data sets. ACC criterion has been successful used on many specific problems ${ }^{24,22,23,41,39}$. Nevertheless, in some data mining real world application, learning a classifier with accurate ranking or probability estimation is also desirable, not just only classification accuracy ${ }^{45,38}$. For example, in direct marketing, we often need to promote the top $x \%$ of customers during gradual roll-out, or we often deploy different promotion strategies to customers with different likelihood of buying some products. To accomplish these learning tasks, a ranking of customers in

Table 1: Detailed information of experimental data


terms of their likelihood of buying is more useful than merely a classification of buyer or non-buyer. In recent years, the AUC has been noticed by ma-
chine learning and data mining community as measures for ranking of the learned classifiers. And the

Table 2: The detailed experimental results on classification accuracy (ACC) and standard deviation. TAN: Tree Augmented Naive Bayes; LWTAN: Locally Weighted TAN; AODE: Averaged One-dependence Estimators; LWAODE: Locally Weighted AODE; HNB: Hidden Naive Bayes; LWHNB: Locally Weighted HNB.


v, * : statistically significant improvement or degradation with a $95 \%$ confidence level.

Table 3: The detailed experimental results on AUC ranking and standard deviation. TAN: Tree Augmented Naive Bayes; LWTAN: Locally Weighted TAN; AODE: Averaged One-dependence Estimators; LWAODE: Locally Weighted AODE; HNB: Hidden Naive Bayes; LWHNB: Locally Weighted HNB.


v, * : statistically significant improvement or degradation with a $95 \%$ confidence level.

AUC of the classifier is calculated as follow:

$$
E=\frac{P_{0}-t_{0}\left(t_{0}+1\right) / 2}{t_{0} t_{1}}
$$

where $t_{0}$ and $t_{1}$ are the numbers of negative and positive instances, repressively. $P_{0}=\sum r_{i}$, with $r_{i}$ denoting the rank of $i$ th negative instance in the ranked list. It is clear that AUC is essentially a measure of the quality of ranking. Unfortunately, this can only deal with two-level classes problem. For multiple classes, Hand and Till ${ }^{6}$ propose an improved AUC calculating measure:

$$
E^{\prime}=\frac{2}{g(g-1)} \sum_{i<j<L} E\left(c_{i}, c_{j}\right)
$$

where $g$ is the number of classes and $E\left(c_{i}, c_{j}\right)$ is the AUC of each pair of classes $c_{i}$ and $c_{j}$.

### 6.3. Analysis of Locally Weighted BNCs

We empirically investigated three Bayesian network classifiers: TAN, AODE, and HNB, in terms of classification accuracy (ACC) and the area under the ROC curve ranking (AUC). We use the implementation of versions for our BNCs in Weka. In all experiments, the classification accuracy of classifiers on a data set was obtained via 10 runs of 10 -fold cross validation. Runs with the various algorithms were carried out on the same training sets and evaluated on the same test sets. Moreover, the probability estimation for all the BNCs in our experiment use the Laplace estimate.

Tables 2 and 3 report the detailed results (the ACC and AUC with the underlying standard deviation) of BNCs (TAN, AODE and HNB) and locally weighted BNCs, respectively. In these two tables, the symbols $v$ and $*$ represent statistically significant upgradation and degradation over the BNC with the $p$-value less than 0.05 . Based on the statistical theory, the difference is statistically significant only if the probability of significant difference is at least 95 percent, i.e., the $p$-value for a $t$-test between two algorithms is less than 0.05 . Overall, the results can be summarized as:

1. Locally weighted TAN could not have significant superiority compared to TAN in ACC and AUC
ranking. Locally weighted TAN model LWTAN almost ties TAN on ACC around ( 6 wins and 7 losses), and has inferior to TAN on AUC (2 wins and 14 losses).
2. LWAODE ties AODE on ACC ( 8 wins and 8 losses), and show worse performance in term of AUC ( 2 wins and 16 losses).
3. LWHNB sightly fails than HNB on both ACC ( 2 wins and 4 losses) and AUC ( 3 wins and 10 losses).
4. When handling the data set with large number of instances (e.g., "waveform-5000" with 5000 samples), all of the locally weighted Bayesian network (e.g., LWTAN, LWAODE, and LWHNB) show inferior performance on both ACC and AUC.
5. For the data set with large number of attributes (e.g., "audiology" with 70 attributes), although the locally weighted LWTAN and LWAODE could obtain a higher accuracy $78.69 \%$ and $77.14 \%$ than unweighted TAN ( $65.35 \%$ ) and AODE ( $71.66 \%$ ), the AUC performance of all the locally weighted Bayesian networks is worse than the unweighted versions.

According, although the locally weighted method has been proved as a effect improvement for NB with simple structure due to the studies in the previous works ${ }^{10,27,28}$, it could not achieve good performance on BNCs (TAN, AODE and HNB) with complex structure. This is mainly because that for the complex BNCs, the reason why the corresponding BNCs can improve the performance in classification is attributed to the structure not the locally weighting approach.

## 7. Conclusion and Future Work

In this paper, we first investigated the complex structure models for BNCs and their improvements, then carried out systematical experiments to analyze the effectiveness of the locally weighting strategies for complex BNCs focusing on Tree Augmented Naive Bayes (TAN), Averaged One-Dependence Estimators (AODE) and Hidden Naive Bayes (HNB). The systematic experiments and comparisons on 36

benchmark data sets on the classification accuracy, and ranking performance showed that although locally weighting had been demonstrated significantly improving the performance of NB (a BNC with simple structure), it could not work well on BNCs with complex structures. In principle, the core parts for improving the performance of naive Bayes corresponding to those complex BNCs are attributed to their structures.

## Acknowledgments

The work was supported by the Key Project of the Natural Science Foundation of Hubei Province, China (Grant No. 2013CFA004), and the National Scholarship for Building High Level Universities, China Scholarship Council (No. 201206410056), and National Natural Science Foundation of China (Grant No. 61403351 and 61370025). It is also partially supported by the Australian Research Council Discovery Projects under Grant No. DP140100545 and DP140102206. This research was also partially done when the first author visited Sa-Shixuan International Research Centre for Big Data Management and Analytics hosted in Renmin University of China. This Center is partially funded by a Chinese National "111" Project "Attracting International Talents in Data Engineering and Knowledge Engineering Research".
