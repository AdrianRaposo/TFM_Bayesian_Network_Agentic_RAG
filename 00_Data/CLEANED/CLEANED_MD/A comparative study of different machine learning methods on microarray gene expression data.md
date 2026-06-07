# A comparative study of different machine learning methods on microarray gene expression data 

Mehdi Pirooznia ${ }^{1}$, Jack Y Yang², Mary Qu Yang ${ }^{3}$ and Youping Deng ${ }^{* 1}$


#### Abstract

Address: ${ }^{1}$ Department of Biological Sciences, University of Southern Mississippi, Hattiesburg, 39406, USA, ${ }^{2}$ Harvard Medical School, Harvard University, Cambridge, Massachusetts 02140, USA and ${ }^{3}$ National Human Genome Research Institute, National Institutes of Health (NIH), U.S. Department of Health and Human Services Bethesda, MD 20852, USA Email: Mehdi Pirooznia - mehdi.pirooznia@usm.edu; Jack Y Yang - jyang@bwh.harvard.edu; Mary Qu Yang - yangma@mail.nih.gov; Youping Deng* - youping.deng@usm.edu * Corresponding author


from The 2007 International Conference on Bioinformatics \& Computational Biology (BIOCOMP'07)
Las Vegas, NV, USA. 25-28 June 2007
Published: 20 March 2008
BMC Genomics 2008, 9(Suppl I):S13 doi:I0.II86/147I-2164-9-SI-SI3

This article is available from: http://www.biomedcentral.com/147I-2164/9/SI/SI3
(c) 2008 Pirooznia et al.; licensee BioMed Central Ltd.

This is an open access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/licenses/by/2.0), which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.


#### Abstract

Background: Several classification and feature selection methods have been studied for the identification of differentially expressed genes in microarray data. Classification methods such as SVM, RBF Neural Nets, MLP Neural Nets, Bayesian, Decision Tree and Random Forrest methods have been used in recent studies. The accuracy of these methods has been calculated with validation methods such as v-fold validation. However there is lack of comparison between these methods to find a better framework for classification, clustering and analysis of microarray gene expression results.


Results: In this study, we compared the efficiency of the classification methods including; SVM, RBF Neural Nets, MLP Neural Nets, Bayesian, Decision Tree and Random Forrest methods. The v-fold cross validation was used to calculate the accuracy of the classifiers. Some of the common clustering methods including K-means, DBC, and EM clustering were applied to the datasets and the efficiency of these methods have been analysed. Further the efficiency of the feature selection methods including support vector machine recursive feature elimination (SVM-RFE), Chi Squared, and CSF were compared. In each case these methods were applied to eight different binary (two class) microarray datasets. We evaluated the class prediction efficiency of each gene list in training and test cross-validation using supervised classifiers.

Conclusions: We presented a study in which we compared some of the common used classification, clustering, and feature selection methods. We applied these methods to eight publicly available datasets, and compared how these methods performed in class prediction of test datasets. We reported that the choice of feature selection methods, the number of genes in the gene list, the number of cases (samples) substantially influence classification success. Based on features chosen by these methods, error rates and accuracy of several classification algorithms were obtained. Results revealed the importance of feature selection in accurately classifying new samples and how an integrated feature selection and classification algorithm is performing and is capable of identifying significant genes.

## Background

Microarray technology allows scientists to monitor the expression of genes on a genomic scale. It increases the possibility of cancer classification and diagnosis at the gene expression level. Several classification methods such as RBF Neural Nets, MLP Neural Nets, Bayesian, Decision Tree and Random Forrest methods have been used in recent studies for the identification of differentially expressed genes in microarray data. However there is lack of comparison between these methods to find a better framework for classification, clustering and analysis of microarray gene expression.

Another issue that might affect the outcome of the analysis is the huge number of genes included in the original data that some of them are irrelevant to analysis. Thus, reducing the number of genes by selecting those that are important is critical to improve the accuracy and speed of prediction systems. In this study, we compared the efficiency of the classification methods; SVM, RBF Neural Nets, MLP Neural Nets, Bayesian, Decision Tree and Random Forrest methods. We used v-fold cross validation methods to calculate the accuracy of the classifiers. We also applied some common clustering methods such as Kmeans, DBC, and EM clustering to our data and analysed the efficiency of these methods. Further we compared the efficiency of the feature selection methods; support vector machine recursive feature elimination (SVM-RFE) [1][2], Chi Squared [3], and CSF [4][5]. In each case these methods were applied to eight different binary (two class) microarray datasets. We evaluated the class prediction efficiency of each gene list in training and test cross-validation using our supervised classifiers. After features selection, their efficiencies are investigated by comparing error rate of classification algorithms applied to only these selected features versus all features.

## Supervised classification

Supervised classification, also called prediction or discrimination, involves developing algorithms to prioridefined categories. Algorithms are typically developed on a training dataset and then tested on an independent test data set to evaluate the accuracy of algorithms. Support vector machines are a group of related supervised learning methods used for classification and regression. The simplest type of support vector machines is linear classification which tries to draw a straight line that separates data with two dimensions. Many linear classifiers (also called hyperplanes) are able to separate the data. However, only one achieves maximum separation. Vapnik in 1963 proposed a linear classifier as a original optimal hyperplane algorithm [6]. The replacement of dot product by a nonlinear kernel function allows the algorithm to fit the max-
imum-margin hyperplane in the transformed feature space [1-6]. SVM finds a linear separating hyperplane with the maximal margin in this higher dimensional space. $K\left(x_{i}, x_{j}\right)=\Phi\left(x_{i}\right)^{T} \Phi\left(x_{j}\right.$ is called the kernel function [6]. There are four basic kernels: linear, polynomial, radial basic function (RBF), and sigmoid [7].

In decision tree structures, leaves represent classifications and branches represent conjunctions of features that lead to those classifications. There are advantages with decision tree algorithms: they are easily converted to a set of production rules, they can classify both categorical and numerical data, and there is no need to have a priori assumptions about the nature of the data. However multiple output attributes are not allowed in decision tree and algorithms are unstable. Slight variations in the training data can result it different attribute selections at each choice point within the tree. The effect can be significant since attribute choices affect all descendent subtrees [5]. ID3 (Iterative Dichotomiser 3) is an algorithm used to generate a decision tree. Developed by J. Ross Quinlan [8], ID3 is based on the Concept Learning System (CLS) algorithm [9]. J48 is an improved version of ID3 algorithm. It contains several improvements, including: choosing an appropriate attribute selection measure, handling training data with missing attribute values, handling attributes with differing costs, and handling continuous attributes [8].

Artificial Neural Networks (ANN) is an interconnected group of nodes that uses a computational model for information processing. It changes its structure based on external or internal information that flows through the network. ANN can be used to model a complex relationship between inputs and outputs and find patterns in data [10-12]. Two common ANN algorithms are Multi-layer perceptron (MLP) and Radial basis function (RBF) Networks (see methods) [13][14].

A bayesian network represents independencies over a set of variables in a given joint probability distribution (JPD). Nodes correspond to variables of interest, and arcs between two nodes represent statistical dependence between variables. Bayesian refers to Bayes' theorem on conditional probability. Bayes' theorem is a result in probability theory, which relates the conditional and marginal probability distributions of random variables. The probability of an event A conditional on another event B is in general different from the probability of B conditional on A. However, there is an explicit relationship between the two, and Bayes' theorem is the statement of that relationship [15]. Naive Bayes is a rule generator based on Bayes's rule of conditional probability. It uses all attributes and allows them to make contributions to the

decision as if they were all equally important and independent of one another, with the probability denoted by the equation:

$$
P(H \mid E)=\frac{P\left(E_{1} \mid H\right) \cdot P\left(E_{2} \mid H\right) \ldots \ldots P\left(E_{\mathrm{n}} \mid H\right)}{P(E)}
$$

Where $\mathrm{P}(\mathrm{H})$ denotes the probability of event $\mathrm{H}, \mathrm{P}(\mathrm{H} \mid \mathrm{E})$ denotes the probability of event H conditional on event E , En is the n th attribute of the instance, H is the outcome in question, and E is the combination of all the attribute values [16].

Random forest is another classifier that consists of many decision trees. It outputs the class that is the mode of the classes output by individual trees [17][18]. Bagging (Bootstrap Aggregating) can also be used as an ensemble method [19] (see methods).

## Unsupervised clustering

Cluster-analysis algorithms group objects on the basis of some sort of similarity metric that is computed for features. Genes can be grouped into classes on the basis of the similarity in their expression profiles across tissues, cases or conditions. Clustering methods divide the objects into a predetermined number of groups in a manner that maximizes a specific function. Cluster analysis always produces clustering, but whether a pattern observed in the sample data remains an open question and should be answered by methods such as resampling-based methods. The k-means algorithm, Farthest First Traversal Algorithm, Density-based clustering, Expectation Maximization (EM) Clustering are four common methods used in this study [21-26].

## Feature selection

Feature selection methods can be divided into the wrapper model and the filter model [27]. The wrapper model uses the predictive accuracy of a mining algorithm to determine the goodness of a selected subset. Wrapper methods generally result in better performance than filter methods because the latter suffers from the potential drawback that the feature selection principle and the classification step do not necessarily optimize the same objective function [28]. In gene selection, the filter model is often adopted due to its computational efficiency [29]. Filter methods select predictive subset of the features using heuristics based on characteristics of the data. Moreover, in wrapper method, the repeated application of cross validation on the same data set might result in finding a feature subset that performs well on the validation data alone. Filter methods are much faster than wrapper methods and therefore are better suited to high dimensional data sets [30].

SVM-RFE: SVM-RFE is a feature selection method to filter out the optimum feature set by using SVM in a wrapperstyle. It selects or omits dimensions of the data, depending on a performance measurement of the SVM classifier. One of the advantages of SVM-RFE is that it is much more robust to data overfitting than other methods [1]. This is an algorithm for selecting a subset of features for a particular learning task. The basic algorithm is the following: 1) Initialize the data set to contain all features, 2) Train an SVM on the data set, 3) Rank features according to $\mathrm{c}_{\mathrm{i}}=$ $\left(w_{i}\right)^{2}, 4$ ) Eliminate the lower-ranked $50 \%$ of the features, 5) return to step 2. At each RFE step 4, a number of genes are discarded from the active variables of an SVM classification model. The features are eliminated according to a criterion related to their support for the discrimination function, and the SVM is re-trained at each step.

Correlation based (CFS): In CFS features can be classified into three disjoint categories, namely, strongly relevant, weakly relevant and irrelevant features [4][30]. Strong relevance of a feature indicates that the feature is always necessary for an optimal subset; it cannot be removed without affecting the original conditional class distribution. Weak relevance suggests that the feature is not always necessary but may become necessary for an optimal subset at certain conditions. Irrelevance indicates that the feature is not necessary at all. There are two types of measures for correlation between genes: linear and non-linear [4][29]. Linear correlation may not be able to capture correlations that are not linear. Therefore non-linear correlation measures often adopted for measurement. It is based on the information-theoretical concept of entropy, a measure of the uncertainty of a random variable [30,31].

Chi Squared: Another commonly used feature selection method is Chi-square statistic ( $\chi^{2}$ ) method [3]. This method evaluates each gene individually by measuring the Chi-square statistics with respect to the classes. The gene expression numbers are first discretized into several intervals using an entropy-based discretization method. Then the Chi-square value of each gene is computed by

$$
\chi^{2}=\sum_{i=1}^{m} \sum_{j=1}^{k}\left(\frac{A_{i j}-\frac{R_{i} \cdot C_{j}}{N}}{\frac{R_{i} \cdot C_{j}}{N}}\right)^{2}
$$

Where $m$ denotes the number of intervals, $k$ the counts of classes, $N$ the total number of patterns, $R i$ the number of patterns in the $i$ th interval, $C j$ the number of patterns in the $j$ th class, and $A i j$ the number of patterns in the $i$ th interval, $j$ th class. The genes with larger Chi-square statistic values are then selected as marker genes for classification.

## Results and discussion

## Datasets

We applied classification, clustering, and feature selection methods to eight datasets in this work (Table 1). Each dataset is publicly available and data were downloaded from microarray repositories from caGEDA website from University of Pittsburgh [32]:

- Lymphoma [33], contains 25 samples of which came from normal vs. malignant plasma cells including 7129 genes
- Breast Cancer [34], 84 samples of normal vs. tumor subtypes including 1753 genes
- Colon Cancer [35], 45 samples of Epithelial normal cells vs. tumor cells including 7464 genes
- Lung Cancer [36], contains 72 samples of which came from normal vs. malignant cells including 917 genes
- Adenocarcinoma [37], contains 86 samples of which came from survival in early-stage lung adenocarcinomas including 5377 genes
- Lymphoma [38], 96 samples of DLBCL1 vs. DLBCL2 cells including 4027 genes
- Melanoma [39], 38 samples of normal vs. malignant cells including 8067 genes
- Ovarian Cancer [40], 39 samples of normal vs. malignant cells including 7129 genes


## Pre-processing

We applied three steps pre-processing to the datasets. First we applied baseline shift for the datasets by shifting all measurements upwards by a number of means (or averages).

This process then followed by performing global mean adjustment. First, the global mean of all intensities of all datasets is calculated. Then, the difference between each
individual mean and the global mean is calculated. This difference value is then added to (or subtracted from) each individual expression intensity value on each dataset. The result is that all datasets now have the same overall mean.

Finally a log transformation applied to the datasets. Log transformation has the advantage of producing a continuous spectrum of values.

## Classification

We used Weka [25] and SVM Classifier [7] for applying classification, clustering and feature selection methods to our datasets. In house java program was used to convert dataset from delimited file format, which is the default import format for SVM Classifier, to ARFF (Attribute-Relation File Format) file, the import format for Weka [25]. For the SVM we applied the following procedures.

First we transformed data to the format of the SVM software, ARFF for WEKA and Labeled them for SVM Classifier. Then we conducted simple scaling on the data. We applied linearly scaling each attribute to the range $[-1,+1]$ or $[0,1]$.

We considered the RBF kernel and used cross-validation to find the best parameter C and $\gamma$. We used a "gridsearch" [31] on C and $\gamma$ using cross-validation. Basically pairs of ( $\mathrm{C}, \gamma$ ) are tried and the one with the best crossvalidation accuracy is picked. Trying exponentially growing sequences of $C$ and $\gamma$ is a practical method to identify good parameters [31], for example $\mathrm{C}=2^{-5}, 2^{-3}, \ldots, 2^{15}$ and $\gamma=2^{-15}, 2^{-13}, \ldots, 2^{3}$.

The classification methods were first applied to all datasets without performing any feature selection. Results of 10 -fold cross validation have been shown in Figure 1 and Table 2. In most datasets SVM and RBF neural nets performed better than other classification methods. In breast cancer data, SVM classification and RBF Neural Nets had the best accuracy $97.6 \%$, and overall they performed very well on all datasets. The minimum accuracy for RBF we calculated was $81.6 \%$ over melanoma dataset. In lung

Table I: Eight Datasets used in Experiment


cancer dataset MLP Neural Nets did also perform well and it was equal to SVM and RBF.

The lowest accuracies are detected from Decision Tree algorithms (both J48 and ID3). As it is shown in Figure 1, in most cases they performed poorly comparing to other methods. Bayesian methods had also high accuracy in most datasets. Although it didn't performed as good as SVM and RBF, but the lowest accuracy was 85.4% on Lymphoma datasets. However overall we have to mention that it seems that in some cases performance of the classification methods depends on the dataset and a specific method cannot be concluded as a best method. For example Bayesian and J48 Decision Tree performed very well on colon and lung cancer, with 93% and 95% for Bayesian respectively and 91% and 94% for J48, while RBF and MLP out performed on breast and lung cancer (97% and 96% respectively for MLP and 97% for both datasets for RBF).

We applied two class clustering methods to the datasets that are illustrated in Figure 1 and Table 3. As it is shown in Figures 2 we have a consistence performance of Farthest First in almost all datasets. EM performed poorly in Adenocarcinoma and Lymphoma datasets (54.7 and 54.2 respectively) while it was performing well in breast melanoma (81%).

### The effect of feature selection

Pairwise combinations of the feature selection and classification methods were examined for different samples as it is shown in Table 4 and 5 and Figure 1. The procedure is illustrated as a pipeline in Figure 1.

![img-0.jpeg](img-0.jpeg)

**Figure 1**

Percentage accuracy of 10-fold cross validation of classification methods for all genes. Results of 10-fold cross validation of the classification methods applied to all datasets without performing any feature selection.

Table 2: Percentage accuracy of 10-fold cross validation of classification methods for all genes


First we tested SVM-RFE, Correlation based, and Chi Squared methods on several gene numbers (500, 200, 100, and 50). Methods were mostly consistent when gene lists of the top genes 50,100 , or 200 were compared. We selected 50 genes because it performed well, consumed less processing time, and required less memory configurations comparing to others.

Almost in all cases, the accuracy performance classifiers were improved after applying feature selections methods to the datasets. In all cases SVM-RFE performed very well when it applied with SVM classification methods.

In lymphoma dataset SVM-RFE performed 100\% in combination of SVM classification method. Bayesian classifi-

![img-1.jpeg](img-1.jpeg)

Figure 2 Percentage accuracy of 10 -fold cross validation of clustering methods for all genes. Results of 10 -fold cross validation of the two class clustering methods applied to all datasets,

![img-2.jpeg](img-2.jpeg)

Figure 3
Accuracy of 10 -fold cross validation of feature selection and classification methods. Accuracy of 10 -fold cross validation of the pairwise combinations of the feature selection and classification methods

![img-3.jpeg](img-3.jpeg)

Figure 4
Overview of the analysis pipeline. The pipeline illustrates the procedure of the pairwise combinations of the feature selection and classification methods
cation method performed well for SVM-RFE and Chi Squared feature selection methods with $92 \%$ accuracy in both
cases.

CFS and Chi Squared also improved the accuracy of the classification. In breast cancer dataset the least improvement is observed from applying Chi Squared feature selection methods with no improvement over SVM, RBF and J48 classification methods with $97 \%, 84 \%$, and $95 \%$ respectively.

In ovarian cancer dataset all feature selection methods performed very close to each other. However the SVM-RFE had a slightly better performance comparing to other methods. We detected $100 \%$ accuracy with SVM-RFE feature selection with both SVM and RBF classification methods. We also observed high accuracies among MLP classification and all feature selection methods with $94 \%$,
$92 \%$, and $92 \%$ for SVM-RFE, CFS, and Chi Squared respectively.

In lung cancer datasets we can observe high accuracy in Decision Tree classification methods (both J48 and ID3) with all feature selection methods.

Overall we have to repeat again that although it is obvious that applying feature selection method improves the accuracy and also particularly it reduces the processing time and memory usage, but finding the best combination of feature selection and classification method might vary in each case.

## Conclusions

The bioinformatics techniques studied in this paper are representative of general-purpose data-mining techniques. We presented an empirical study in which we compare some of the most commonly used classification, clustering, and feature selection methods. We apply these methods to eight publicly available datasets, and compare, how these methods perform in class prediction of test datasets. We report that the choice of feature selection method, the number of genes in the gene list, the number of cases (samples) and the noise in the dataset substantially influence classification success. Based on features chosen by these methods, error rates and accuracy of several classification algorithms were obtained. Results reveal the importance of feature selection in accurately classifying new samples. The integrated feature selection and classification algorithm is capable of identifying significant genes.

## Methods

Multi-layer perceptron (MLP): Error backpropagation neural network is a feedforward multilayer perceptron (MLP) that is applied in many fields due to its powerful and stable learning algorithm [13]. The neural network learns the training examples by adjusting the synaptic weight according to the error occurred on the output layer. The back-propagation algorithm has two main advantages: local for updating the synaptic weights and biases, and efficient for computing all the partial derivatives of the cost function with respect to these free parameters. A perceptron is a simple pattern classifier.

The weight-update rule in backpropagation algorithm is defined as follows:
$\Delta w_{i t}(n)=\alpha \Delta w_{i t}(n-1)+\eta \delta_{i}(n) y_{i}(n) \quad$ where $w$ is the weight update performed during the $n$th iteration through the main loop of the algorithm, $\eta$ is a positive constant called the learning rate, $\delta$ is the error term associated with

Table 3: Percentage accuracy of 10-fold cross validation of clustering methods for all genes


j, and $0 \leq \alpha<1$ is a constant called the momentum [9][11,12].

Radial basis function (RBF) networks: RBF networks have 2 steps of processing. First, input is mapped in the hidden layer. The output layer is then a linear combination of hidden layer values representing mean predicted output. This output layer value is the same as a regression model in statistics [9]. The output layer, in classification problems, is usually a sigmoid function of a linear combination of hidden layer values. Performance in both cases is often improved by shrinkage techniques, also known as ridge regression in classical statistics and therefore smooth output functions in a Bayesian network.

Moody and Darken [14] have proposed a multi-phase approach to RBFNs. This multi-phase approach is straightforward and is often reported to be much faster than, e.g., the backpropagation training of MLP. A possible problem of the approach is that the RBF uses clustering method (e.g., k-means) to define a number of centers in input space and the clustering method is completely unsupervised and does not take the given output information into account. Clustering methods usually try to minimize the mean distance between the centers they distribute and the given data which is only the input part of the training data. Therefore, the resulting distribution of RBF centers may be poor for the classification or regression problem.

Support Vector Machines (SVM): Given a training set of instance-label pairs $\left(x_{i}, y_{i}\right), \mathrm{i}=1, \ldots, \mathrm{l}$ where $x_{i} \in R^{n}$ and $y \in{1,-1}^{l}$, the support vector machines require the solution of the following optimization problem:

$$ \begin{aligned} & \min *{\omega, b, \xi} \frac{1}{2} \omega^{T} \omega+C \sum*{i=1}^{l} \xi_{i} \ & y_{i}\left(\omega^{T} \phi\left(x_{i}\right)+b \geq 1-\xi_{i}\right. \ & \left.\xi_{i} \geq 0\right] \end{aligned} $$

SVM finds a linear separating hyperplane with the maximal margin in this higher dimensional space. $\mathrm{C}>0$ is the penalty parameter of the error term. $K\left(x_{i}, x_{j}\right)=\Phi\left(x_{i}\right)^{T} \Phi\left(x_{j}\right)$ is called the kernel function [6]. Here there are four basic kernels: linear, polynomial, radial basic function (RBF), and sigmoid:

Linear: $K\left(x_{i}, x_{j}\right)=x_{i}{ }^{T} x_{j}$ Polynomial: $K\left(x_{i}, x_{j}\right)=\left(x_{i}, x_{j}\right)^{d}$ RBF: $K\left(x_{i}, x_{j}\right)=\exp \left(-\frac{\left|\left|x_{i}-x_{j}\right|\right|^{2}}{2 \sigma^{2}}\right)$ Sigmoid: $K\left(x_{i}, x_{j}\right)=\tanh \left(k\left(x_{i} x_{j}\right)+\vartheta\right)$ The k-means: The k-means algorithm takes a dataset and partitions it into $k$ clusters, a user-defined value. Computationally, one may think of this method as a reverse method of analysis of variance (ANOVA). The algorithm starts with $k$ random clusters, and then move objects between those clusters with the goal to 1) minimize variability within clusters and 2) maximize variability between clusters [21]. In other words, the similarity rules will apply maximally to the members of one cluster and minimally to members belonging to the rest of the clusters. The significance test in ANOVA evaluates the between group variability against the within-group variability when computing the significance test for the hypothesis that the means in the groups are different from each other. Usually, as the result of a $k$-means clustering analysis, the means for each cluster on each dimension would be examined to assess how distinct $k$ clusters are. Obtaining very different means for most is perfect [22].

Farthest First: Farthest First Traversal Algorithm works as a fast simple approximate clustering model after Simple

Table 4: 10-fold cross validation evaluation result of feature selection methods applied to the classification methods. X:Y pattern indicates $X$ as the error rate in cancer samples and $Y$ as the error rate in normal samples


K-Means. To find $k$ cluster centers, it randomly chooses one point as a first center, and then selects point with maximal min-distance to current centers as a next center [23].

Density Based Clustering (DBC): Density-based clustering has turned out to be one of the most successful traditional approaches to clustering. It can be extended to detect subspace clusters in high dimensional spaces. A cluster is defined as a maximal set of density-connected points. Correlation clusters are sets of points that fit to a common hyperplane of arbitrary dimensionality. Den-sity-based clustering starts by estimating the density of each point to identify core, border and noise points. A core point is referred to as a point whose density is greater than a user-defined threshold. A noise point is referred to as a point whose density is less than a user-defined threshold. Noise points are usually discarded in the clustering process. A non-core, non-noise point is considered as a border point [24].

Expectation Maximization (EM) clustering: An expecta-tion-maximization (EM) algorithm finds maximum likelihood estimates of parameters in probabilistic models. EM performs repeatedly between an expectation (E) step, an expectation of the likelihood of the observed variables, and maximization (M) step, which computes the maximum expected likelihood found on the E step. EM assigns a probability distribution to each instance which indicates the probability of it belonging to each of the clusters [25]. By cross validation, EM can decide how many clusters to create.

Table 5: Percentage accuracy of 10-fold cross validation of feature selection methods applied to the classification methods.


The goal of EM clustering is to estimate the means and standard deviations for each cluster so as to maximize the likelihood of the observed data. The results of EM clustering are different from those computed by k-means clustering [26]. K-means assigns observations to clusters to maximize the distances between clusters. The EM algorithm computes classification probabilities, not actual assignments of observations to clusters.

Cross validation: In order to perform to measure classification error, it is necessary to have test data samples independent of the learning dataset that was used to build a classifier. However, obtaining independent test data is difficult or expensive, and it is undesirable to hold back data from the learning dataset to use for a separate test because that weakens the learning dataset. V-fold cross validation technique performs independent tests without requiring separate test datasets and without reducing the data used to build the tree. The learning dataset is partitioned into some number of groups called "folds" [31]. The number of groups that the rows are partitioned into is the ' $V$ ' in Vfold cross classification. 10 is the recommended and default number for "V". It is also possible to apply the $v$-fold crossvalidation method to a range of numbers of clusters in $k$ means or EM clustering, and observe the resulting average distance of the observations from their cluster centers.

Leave-one-out cross-validation involves using a single observation from the original sample as the validation data, and the remaining observations as the training data. This is repeated such that each observation in the sample is used once as the validation data [31].

## Competing interests

Financial support from Mississippi Computational Biology Consortium (MCBC) and Mississippi Functional Genomics Networks (MFGN) is gratefully acknowledged. The authors declare that they have no competing interests.

## Authors' contributions

MP and YD initiated the project. MP procured the necessary data and software, carried out the analyses, analyzed the results and drafted the manuscript. YD directed the design of the project and data analysis. JYY and MQY gave suggestions and helped to revise the manuscript. All authors read and approved the final manuscript.

## Acknowledgements

This work was supported by the Mississippi Functional Genomics Networks (MFGN) (DHHS/NIH/NCRR Grant\# 2P20RR016476-04) and Mississippi Computational Biology Consortium (MCBC) (NSF Grant \# EPS0556308).

This article has been published as part of BMC Genomics Volume 9 Supplement 1, 2008: The 2007 International Conference on Bioinformatics \& Computational Biology (BIOCOMP'07). The full contents of the supplement are available online at http://www.biomedcentral.com/1471-2164/ 9?issue=S1.

## Publish with Bio Med Central and every

scientist can read your work free of charge
"BioMed Central will be the most significant development for disseminating the results of biomedical research in our lifetime."

Sir Paul Nurse, Cancer Research UK
Your research papers will be:

- available free of charge to the entire biomedical community
- peer reviewed and published immediately upon acceptance
- cited in PubMed and archived on PubMed Central
- yours - you keep the copyright

Submit your manuscript here:
http://www.biomedcentral.com/info/publishing_adv.asp
BioMedcentral