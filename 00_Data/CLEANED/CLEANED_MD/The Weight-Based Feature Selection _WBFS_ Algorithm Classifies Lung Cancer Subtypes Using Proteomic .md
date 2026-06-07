# Article 

## The Weight-Based Feature Selection (WBFS) Algorithm Classifies Lung Cancer Subtypes Using Proteomic Data

Yangyang Wang ${ }^{1}$, Xiaoguang Gao ${ }^{1, *}$, Xinxin Ru ${ }^{1}$, Pengzhan Sun ${ }^{1}$ and Jihan Wang ${ }^{2, *}$


#### Abstract

check for updates Citation: Wang, Y.; Gao, X.; Ru, X.; Sun, P.; Wang, J. The Weight-Based Feature Selection (WBFS) Algorithm Classifies Lung Cancer Subtypes Using Proteomic Data. Entropy 2023, 25, 1003. https://doi.org/10.3390/ e25071003

Academic Editors: Kathleen M. Jagodnik and Alon Bartal

Received: 3 April 2023
Revised: 27 June 2023
Accepted: 28 June 2023
Published: 29 June 2023


## (0)

Copyright: (c) 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 School of Electronics and Information, Northwestern Polytechnical University, Xi'an 710129, China; wangyang2154@mail.nwpu.edu.cn (Y.W.)
2 Xi'an Key Laboratory of Stem Cell and Regenerative Medicine, Institute of Medical Research, Northwestern Polytechnical University, Xi'an 710072, China

* Correspondence: xggao@nwpu.edu.cn (X.G.); jihanwang@nwpu.edu.cn (J.W.)

Abstract: Feature selection plays an important role in improving the performance of classification or reducing the dimensionality of high-dimensional datasets, such as high-throughput genomics/proteomics data in bioinformatics. As a popular approach with computational efficiency and scalability, information theory has been widely incorporated into feature selection. In this study, we propose a unique weight-based feature selection (WBFS) algorithm that assesses selected features and candidate features to identify the key protein biomarkers for classifying lung cancer subtypes from The Cancer Proteome Atlas (TCPA) database and we further explored the survival analysis between selected biomarkers and subtypes of lung cancer. Results show good performance of the combination of our WBFS method and Bayesian network for mining potential biomarkers. These candidate signatures have valuable biological significance in tumor classification and patient survival analysis. Taken together, this study proposes the WBFS method that helps to explore candidate biomarkers from biomedical datasets and provides useful information for tumor diagnosis or therapy strategies.

Keywords: feature selection; information theory; The Cancer Proteome Atlas (TCPA); The Cancer Genome Atlas (TCGA); lung cancer; Bayesian network; biomarkers

## 1. Introduction

Lung cancer is one of the deadliest cancers in the world, and lung adenocarcinoma (LUAD) and lung squamous cell carcinoma (LUSC) are the most common subtypes, which have drastically different biological signatures [1]. The precise biomarkers to be implemented in clinical settings remain ambiguous, and accurate classification of lung cancers into clinically significant subtypes is of utmost importance in making therapeutic decisions; this gap demands immediate attention.

The Cancer Proteome Atlas (TCPA) database [2] is a large-scale proteomic database that contains molecular and clinical data from over 11,000 patient samples across 32 different cancer types. The Cancer Genome Atlas (TCGA) database [3,4] is a comprehensive genomic database that also contains the clinical information of patients. Both TCPA and TCGA databases are publicly available and have been widely used by researchers around the world. They provide valuable resources for cancer research, enabling researchers to investigate the molecular mechanisms underlying cancer and identify new targets for therapeutic intervention. However, discovering key biomarkers for lung cancer from the extensive datasets in these databases is a difficult task in biomedical research [5].

Feature selection is an important task in machine learning and data analysis, where the goal is to identify a subset of relevant features from a large set of potential predictors [6]. One approach to feature selection is based on information theory; such an approach involves quantifying the amount of information that a feature provides about the outcome variable of interest. This approach is especially useful in situations where the number of potential predictors is large and the relationship between the predictors and the outcome variable

is complex. Information-theoretic feature selection methods are based on measures such as entropy, mutual information, and conditional mutual information. These measures are used to assess the relevance of a feature to the outcome variable, as well as the redundancy between features. The goal is to select a subset of features that maximizes the amount of relevant information while minimizing the amount of redundant information.

One application of information-theoretic feature selection is in the field of biomarker discovery, where the goal is to identify a set of molecular features (such as genes or proteins) that are associated with a particular disease or condition [7]. By using information-theoretic methods to select key biomarkers, researchers can gain insights into the underlying biological mechanisms of the disease, as well as develop diagnostic and therapeutic tools. In the past two decades, many studies on filter feature selection algorithms based on information theory have been reported due to their robustness and computational efficiency [8]. The pioneering work of Battiti employed the mutual information (MI) criterion to evaluate a set of candidate features, and his research proved that mutual information is suitable for assessing arbitrary dependencies between random variables [8,9]. To date, most feature selection methods based on information theory obtain the optimal feature subset by maximizing correlation and minimizing redundancy, such as Mutual Information Maximisation (MIM) [10], Mutual Information Based Feature Selection (MIFS) [9], Mutual Information Feature Selector under Uniform Information Distribution (MIFS-U) [11], Max-Relevance and Min-Redundancy (mRMR) [12], Conditional Informative Feature Extraction (CIFE) [13], and Conditional Redundancy (CONDRED) [14]. Most existing feature selection strategies aim to maximize the classification performance only by considering the relevance between features and classes and redundancy between pairs of features without assessing interactions and complementarity; consequently, some features with discriminative ability may be mistakenly removed. The concept of interaction has been widely explored in different scenarios [15]. For example, exploring the interaction information of microarray gene expression data is beneficial for discovering cancer biomarkers and identifying cancer subtype classifications [16].

This study involved an extensive examination of a lung cancer protein expression dataset sourced from the TCPA database, in conjunction with phenotype and survival information from the TCGA database. Firstly, it aimed to provide an overview of the functional proteomic heterogeneity of LUAD and LUSC tumor samples. Secondly, a unique filter weight-based feature selection (WBFS) method that assesses selected features and candidate features was used to identify candidate protein biomarkers that exhibited superior performance in classifying the two major lung cancer subtypes. Additionally, Bayesian etworks (BNs) were utilized to identify the direct impact factors that had causal relationships with the classification of the two subtypes. Finally, the potential clinical implications of the candidate protein biomarkers for prognosis were evaluated.

## 2. Materials and Methods

### 2.1. Data Acquisition and Preprocessing

We extracted the lung cancer subset from the original dataset (TCGA-PANCAN32-L4.zip belongs to the level 4 data set, and the batch effect has been processed in the past) in TCPA (https://tcpaportal.org/tcpa, accessed on 11 January 2023), resulting in 687 tumor cases comprising 362 LUAD samples and 325 LUSC samples, with 258 proteins. The proteins that contained missing values ("NA") in over 50% of the samples were removed, and the "NA" values for six proteins were replaced by their average values. This led to the creation of a proteome profiling dataset consisting of 687 tumor samples and 217 proteins. We also downloaded relevant clinical information, including survival information and phenotype information, for these 687 tumor samples from the TCGA data (11 January 2023).

### 2.2. Proteome Profiling Analysis

T-Distributed Stochastic Neighbor Embedding (t-SNE) is a non-linear technique that is particularly useful for visualizing high-dimensional data in low-dimensional space [17].

Principal Component Analysis (PCA) is a linear method that aims to reduce the number of features in a dataset while retaining the maximum amount of information. It can be used to capture the most important patterns in the data and visualization of the classification performance. Unlike PCA, t-SNE is not a linear method and instead tries to preserve the local structure of the data in the low-dimensional space.

We utilized t-SNE and PCA techniques based on the "Rtsne" [18] and "FactoMineR" [19] packages to visualize the differences between the original proteins and the selected proteomic biomarkers.

# 2.3. Using WBFS to Obtain Candidate Protein Biomarkers 

High-dimensional datasets have stimulated the development of feature selection techniques. In this section, some basics of information theory are outlined, and then a new feature selection algorithm based on information theory is proposed.

Mutual information is the overlapping information of two entropies and is commonly utilized to analyze the correlation and statistical dependency between two random variables. It has been employed in various feature selection algorithms for obtaining the redundancy between the input features $X$ and the classifications $Y$ as well as the correlation between any pair of features.

$$
I(X ; Y)=\sum_{x \in X} \sum_{y \in Y} p(x, y) \log \frac{p(x, y)}{p(x) p(y)}
$$

where $p(x)$ is the probability when $X=x$, and $p(x, y)$ is the joint probability when $X=x, Y=y$.

Conditional mutual information is the mutual information of $X$ and $Y$ given the third variable $Z$ and can be computed by:

$$
I(X ; Y \mid Z)=\sum_{z \in Z} p\left(z_{k}\right) \sum_{x \in X} \sum_{y \in Y} p(x, y \mid z) \log \frac{p(x, y \mid z)}{p(x \mid z) p(y \mid z)}
$$

where $p(x \mid z)$ is the conditional probability of $X=x$ when $Z=z$ is known, and $p(x, y \mid z)$ is the conditional probability of $X=x, Y=y$ when $Z=z$ is known.

As an extension of mutual information, 3-way interaction information denotes the information shared by three random variables $X, Y, Z$ and can be determined using conditional information and mutual information:

$$
I(X ; Y ; Z)=I(X, Y ; Z)-I(X ; Z)-I(Y ; Z)
$$

Interaction information can be positive, zero, or negative; it is positive when the two variables of $X, Y$ together provide information that cannot be provided by any one of them individually. Therefore, $I(X ; Z)<I(X ; Z \mid Y)$ is always true when $X, Y$ have an interaction relationship.

Table 1 summarizes all symbols used for the WBFS formula derivation.

Table 1. The symbols used in feature selection method.


For a dataset $D$ that has $m$ features $F=\left\{f_{1}, f_{2}, \ldots, f_{m}\right\}$ and $n$ samples, the aim of a feature selection method is to find an optimal feature subset $F^{\prime}=\left\{f_{1}, f_{2}, \ldots, f_{k}\right\}$ that can maximize the objective function $J\left(f_{k}\right)$ and yield the same or a better classification accuracy than the original feature set as much as possible, where $k \leq m$ and $F^{\prime} \subseteq F$. The concepts of relevance, redundancy, complementarity, and interaction are critical for a feature selection approach. The relevance between feature and class can be expressed using the mutual information of $I\left(f_{i} ; C\right) ; f_{i}$ is called a stronger correlated feature than $f_{j}$ when $I\left(f_{i} ; C\right)>I\left(f_{j} ; C\right)$. In addition, the mutual information $I\left(f_{i} ; f_{j}\right)$ between pairs of features is called redundancy. Considering correlation alone is definitely not sufficient because redundant features may reduce the classification performance and increase computational complexity; therefore, the redundancy should be eliminated while a new candidate feature $f_{k}$ is selected into $S$ from the candidate feature set $F / S$. However, there is still a flaw in the objective function $J\left(f_{k}\right)$ based only on relevance and redundancy due to the absence of supplementary information when a new candidate feature $f_{k}$ is introduced into $S$.

We used the following equation as the objective function to screen the candidate features individually:

$$
J\left(f_{k}\right)=\operatorname{argmax} \sum_{f_{k} \in F-S, f_{j} \in S} \omega * I\left(f_{k} ; C \mid f_{j}\right)
$$

Specifically, instead of using equal weight to define the influence of selected features on candidate features, a dynamic parameter $\omega$ is considered to evaluate the differences of the selected features and updated when a new feature $f_{k}$ is introduced into $S$.

For two interaction features, $f_{k}$ and $f_{j}, I\left(f_{j} ; C\right)<I\left(f_{j} ; C \mid f_{k}\right)$ will be true if their interaction information is positive. In other words, the addition of feature $f_{k}$ will produce a positive influence in predicting $C$ for $f_{j}$. Hence, we can use $I\left(f_{k} ; C \mid f_{j}\right)-I\left(f_{k} ; C\right)$ to measure the weight $\omega$, which can be expressed as follows:

$$
\omega=1+\frac{2\left(I\left(f_{j} ; C \mid f_{k}\right)-I\left(f_{j} ; C\right)\right)}{H\left(f_{j}\right)+H(C)}
$$

Theorem 1. $0 \leq \omega<2$.
Proof of Theorem 1. For feature $f_{k}, f_{j}$ and class $C$, we have:

$$
\left\{\begin{array}{l}
0 \leq I\left(f_{j} ; C\right) \leq H\left(f_{j}\right) \\
0 \leq I\left(f_{j} ; C\right) \leq H(C) \\
0 \leq I\left(f_{j} ; C \mid f_{k}\right) \leq H\left(f_{j}\right) \\
0 \leq I\left(f_{j} ; C \mid f_{k}\right) \leq H(C)
\end{array} \Rightarrow 0 \leq 2 I\left(f_{j} ; C \mid f_{k}\right) \leq H\left(f_{j}\right)+H(C)\right.
$$

Then,

$$
\left\{\begin{array}{l}
0 \leq \frac{2 I\left(f_{j} ; C\right)}{H\left(f_{j}\right)+H(C)} \leq 1 \\
0 \leq \frac{2 I\left(f_{j} ; C \mid f_{k}\right)}{H\left(f_{j}\right)+H(C)} \leq 1
\end{array} \Rightarrow-1 \leq \frac{2\left(I\left(f_{j} ; C \mid f_{k}\right)-I\left(f_{j} ; C\right)\right)}{H\left(f_{j}\right)+H(C)} \leq 1\right.
$$

Hence,

$$
0 \leq \omega=1+\frac{2\left(I\left(f_{j} ; C \mid f_{k}\right)-I\left(f_{j} ; C\right)\right)}{H\left(f_{j}\right)+H(C)} \leq 2
$$

Based on Equations (4) and (5), the final objective function of WBFS is shown as:

$$
J_{W B F S}\left(f_{k}\right)=\operatorname{argmax} \sum_{f_{k} \in F-S, f_{j} \in S}\left(1+\frac{2\left(I\left(f_{j} ; C \mid f_{k}\right)-I\left(f_{j} ; C\right)\right)}{H\left(f_{j}\right)+H(C)}\right) * I\left(f_{k} ; C \mid f_{j}\right)
$$

Our proposed method of WBFS consists of two components: $\omega$ and $I\left(f_{k} ; C \mid f_{j}\right)$. The first component considers not only the importance of features in $S$ but also the influence of candidate feature $f_{k} \in F / S$ on the relevance between $S$ and $C$. The strong positive interaction of features $f_{k} \in F / S$ and $f_{j} \in S$, the larger this value. The second component, $I\left(f_{k} ; C \mid f_{j}\right)$, is conditional mutual information, which fully covers the relevance between candidate feature $f_{k}$ and class $C$ based on the selected feature $f_{j} \in S$. Algorithm 1 presents the pseudocode of the WBFS algorithm:

```
Algorithm 1 Weight-based feature selection (WBFS)
    Input : F, S, C, K (K \ 1\)
    Output : F'
    Initialization : S \leftarrow \varnothing, F' \leftarrow \varnothing;
    for \(i=0 ; i<|F| ; i++\) do
        \(M I_{i} \leftarrow I\left(f_{i} ; C\right)\);
    end for
    \(S \leftarrow f^{\prime}\) which \(I\left(f^{\prime} ; C\right)=\max (M I)\);
    \(|S| \leftarrow 1 ;\)
    while \(|S|<K\) do
        for \(k=0 ; k<|F \backslash S| ; k++\) do
            \(J_{W B F S}\left(f_{k}\right)=\operatorname{argmax} \sum_{f_{k} \in F-S, f_{j} \in S}\left(1+\frac{2 *\left(I\left(f_{j} ; C \mid f_{k}\right)-I\left(f_{j} ; C\right)\right)}{H\left(f_{j}\right)+H(C)}\right) * I\left(f_{k} ; C \mid f_{j}\right) ;\)
            \(S \leftarrow f_{k} ;\)
        end for
    end while
    \(F^{\prime} \leftarrow S ;\)
    Return \(F^{\prime}\);
```

In Algorithm $1, H\left(f_{j}\right)$ and $H(C)$ represent the entropy of the feature $f_{j}$ and the categorical variable $C$, respectively.

When we need to select the top $K$ features from the original feature set $F$, the steps of the WBFS algorithm are as follows:

First, we obtain the mutual information between each feature in $F$ and class $C$. Second, the feature $f^{\prime}$, which has the largest relevance among the features, is added into $S$. Third, for the candidate feature set $F / S$, Equation (6) is utilized to obtain the feature $f_{k}$ and add it to the selected feature set $S$. When the number of features in $S$ is equal to $K, S$ is the optimal feature set $F^{\prime}$.

The time consumption largely depends on the computation times of mutual information or conditional mutual information for information theory-based feature selection methods. For a dataset $D$ with $m$ samples and $n$ features, the time complexity is $O(m)$ when mutual information or conditional mutual information is calculated. When a new feature is introduced into the selected feature set, mutual information or conditional mutual information among all features must be calculated; the time complexity is $O(m n)$ for one iteration. Therefore, for WBFS, the final time complexity is $O(k m n)$ if the top $k$ features are chosen from the original features. The MIFS [9], mRMR [12], CIFE [13] and CONDRED [14] methods have the same time complexity as WBFS; and the time complexity of MIM [10] is $O(m n)$ because only the relevance between features and classes is considered.

# 2.4. Using Bayesian Networks to Discover Causalities 

Causal discovery aims to find causal relations by analyzing observational data [20]. As a widely used graphical model in bioinformatics and employed for related aspects of classification and prediction, the Bayesian network (BN) provides a convenient and coherent way to represent uncertainty from a perspective of probability [21]. BN models can estimate the joint probability distribution $P$ over a vector of random variables $X=\left(X_{1}, \ldots, X_{n}\right)$, and

the joint probability distribution factorized as a product of several conditional distributions denotes the dependency or independency structure by a directed acyclic graph (DAG):

$$
P\left(X_{1}, \ldots, X_{n}\right)=\prod_{i=1}^{n} P\left(X_{i} \mid P a\left(X_{i}^{G}\right)\right)
$$

where $P\left(X_{1}, \ldots, X_{n}\right)$ is the joint probability, $P a\left(X_{i}^{G}\right)$ are the parent nodes of $X_{i}$ and $P\left(X_{i} \mid P a\left(X_{i}^{G}\right)\right)$ is the conditional probability of $X_{i}$ when the parent nodes of $X_{i}$ are known. Tsamardinos et al. were the first to establish the connection between local causal discovery and feature selection [22]. Yu et al. developed a unified view of causal and non-causal feature selection methods based on the BN perspective, and their experimental results show that noncausal feature selection is more suitable for high-dimensional data, especially for gene sequencing data [23]. Therefore, the combination of non-causal feature selection and BN local causal discovery is a promising strategy for identifying key signatures of a target in a high-dimensional dataset. The regulatory network composed of the selected biomarkers defines the regulatory interactions among regulators and their potential targets and can be used for inference and prediction. We constructed a regulatory network using BN to explore the causality interaction between any two of the selected proteins using WBFS based on the Causal Learner toolbox, which is available on GitHub (https://github.com/zdragonl/Causal-Learner, accessed on 11 January 2023) [24].

# 2.5. Receiver Operating Characteristic (ROC) and Survival Analysis 

The candidate protein biomarkers obtained with WBFS were analyzed for ROC and survival curves in order to evaluate the potential applications of these candidate signatures as possible markers for lung cancer diagnosis and prognosis. Medcalc statistical software [25] was used to analyze the candidate proteins for distinguishing LUAD and LUSC samples, and the sensitivity, specificity, and area under the curve (AUC) values were obtained. A multiple regression model to evaluate the combination classification performance of specific set biomarkers was also assessed, and it can be expressed as follows:

$$
\text { multiple regression }=\frac{1}{1+e^{-\left(\text { constant }+\sum_{i=1}^{n} \text { coefficient }_{i} * \text { expression }_{i}\right)}}
$$

In the above Equation (8), the constant represents the value that would be predicted for the dependent variable if all the independent variables were simultaneously equal to zero, the coefficient $_{i}$ is the slope of the linear relationship of the $i$-th protein, and the expression $_{i}$ is the expression value of the $i$-th protein.

For survival analysis, Kaplan-Meier survival curves were explored and visualized (using $\alpha=0.05$ as the test level) using the Survminer toolkit [26] in R based on age, gender, and the tumor, node, metastasis (TNM) stage (clinical information was collected in the TCGA dataset), as well as the expression pattern of candidate proteins in LUAD and LUSC subjects.

## 3. Results

### 3.1. The Distributions Overview of the LUAD and LUSC Tumor Samples

The t-stochastic neighbor embedding (t-SNE) algorithm and principal component analysis (PCA), using the "Rtsne" and "FactoMineR" packages, respectively, were employed to display the difference between the original proteins and the 10 proteomic biomarkers. Overviews of the original lung cancer dataset based on t-SNE and PCA are shown in Figure 1A,C, respectively. t-SNE and PCA were also performed based on the subset containing 10 signatures. As shown in Figure 1B, the samples using 10 protein signatures clustered significantly better than the 258 original proteins. From Figure 1C,D, we also observed that the PCA scores for Dim1 significantly increased from $14.4 \%$ to $36.4 \%$.

![img-0.jpeg](img-0.jpeg)

**Figure 1.** Overview of the proteome profiling across lung adenocarcinoma (LUAD) and lung squamous cell carcinoma (LUSC) samples. The subgraphs (**A,B**) are the results performing t-SNE; the subgraphs (**C,D**) are the results performing PCA; (**A**) t-SNE and (**C**) PCA showed the clusters of samples based on whole proteome profiling; (**B**) t-SNE and (**D**) PCA showed the clusters of samples based on the top 10 selected protein profiling.

### 3.2. Using WBFS Method Identifying Protein Signatures for Classifying the Two Cancer Subtypes

#### 3.2.1. Evaluate WBFS Classification Performance Based on UCI Datasets

To evaluate the classification performance of the WBFS algorithm and the advantage in terms of prediction accuracy compared with other feature selection algorithms, 12 high-dimensional datasets with different numbers of features, samples, and classification labels from the UCI repository (https://archive.ics.uci.edu/mL/datasets.php, accessed on 11 January 2023) and additional studies were employed (https://github.com/jundongl/scikit-feature, accessed on 11 January 2023). We discretize continuous datasets using an equal-width strategy into five bins. Additionally, we introduced the ratio concept to evaluate the classification difficulty for each dataset, with a smaller value indicating a more challenging feature selection. For dataset *D*, *N* is the number of samples, *m* is the median arity of the features, and *c* is the number of classes. The ratio can be calculated by *N*/(*mc*). All 12 datasets are described in Table 2.

Table 2. Description of 12 datasets for experiment.


The experiment was performed using MATLAB 2020 based on Windows 10 with a 1.6 GHz Intel Core CPU and 8 GB memory. Three types of classifiers, k-nearest neighbors (KNN) [27], naïve Bayes classifier (NBC) [28], and the Library for Support Vector Machines (LibSVM) [29], were used to test the prediction performance using selected features in the experiment. Ten-fold cross-validation was employed, in which each of these datasets was randomly partitioned into a training dataset ( $90 \%$ ) and a testing dataset ( $10 \%$ ) and fed to every feature selection algorithm 10 times. Five well-known feature selection algorithms were selected to be compared with the proposed WBFS method, including CONDRED [14], MIM [10], mRMR [12], DISR [30], and CIFE [13]. A $t$-test was used to determine the significant differences between two groups of classification accuracies, and a Win/Tie/Loss (W/T/L) paradigm was adopted for describing performance: Win means WBFS shows better than other baseline methods, Tie means that there is no statistically significant difference with other methods and other cases are classified as Loss. Specifically, the "*' symbols and ' $v$ ' identify statistically significant (at the 0.1 level) wins or losses over the proposed WBFS method. The average accuracies, standard deviation, and W/T/L information of 12 datasets based on three classifiers are shown in Tables 3-5. The number of selected features for all methods was fixed at 15 and $k=5$ for the KNN classifier.

In Tables 3-5 bold values indicate the largest value among the six feature selection methods. WBFS obtains the best average classification accuracies of $84.48 \%, 73.15 \%$, and $83.01 \%$ and occupies first place on five datasets (Lung, Krvskp, Madelon, Musk, and Waveform), six datasets (Breast, Colon, Ionosphere, Krvskp, Sonar, Waveform), and six datasets (Breast, Krvskp, Madelon, Musk, Sonar, Waveform) based on the three classifiers KNN, NB and LibSVM, respectively. For the other methods of CONDRED [14], MIM [10], mRMR [12], DISR [30], and CIFE [13], the numbers of cases for which they achieve the highest classification accuracy are $1,2,2,1,1$ with KNN; $1,1,0,1,3$ with NBC; and $1,1,2,1$, 1 with LibSVM, respectively.

Table 3. Accuracy (\%) of selected features using the k-nearest neighbors (KNN) algorithm.


The '*' symbols and ' $v$ ' identify statistically significant (at the 0.1 level) wins or losses over the proposed WBFS method.

Table 4. Accuracy (\%) of selected features using the naïve Bayes classifier (NBC) algorithm.


The '*' symbols and ' $v$ ' identify statistically significant (at the 0.1 level) wins or losses over the proposed WBFS method.

Table 5. Accuracy (\%) of selected features using the Library for Support Vector Machines (LibSVM) algorithm.


The '*' symbols and ' $v$ ' identify statistically significant (at the 0.1 level) wins or losses over the proposed WBFS method.

From the perspective of W/T/L, WBFS obtains the best result in most cases. According to Table 5, WBFS achieves significantly higher classification accuracy than the CONDRED, MIM, mRMR, DISR, and CIFE methods with case numbers of $7,6,3,6$, and 8 . For Tables 3 and 4, the numbers are $6,5,3,5,7$ and $7,4,3,4,4$.

Considering that the above six feature selection algorithms are all based on a feature ranking strategy, an effective method for further comparing their classification accuracies is to individually add features for learning. We employed this strategy using a range of 1-30 selected features. Figure 2 shows the comparative results based on six representative datasets (Lung, Madelon, Sonar, Musk, Krvskp and Waveform). For each subgraph, the xaxis refers to the first $k$ selected features, and the $y$-axis represents the average classification accuracy of three classifiers for the top $k$ selected features. In Figure 2, it is obvious that the proposed WBFS method shows better average accuracies than the others in most cases based on the Lung, Madelon, Sonar, and Musk datasets. For instance, WBFS obtains the highest average classification accuracy of $76.39 \%$ with only seven features, while accuracies of $68.50 \%, 67.44 \%, 70.40 \%, 74.31 \%$, and $64.84 \%$ are achieved by MIM, mRMR, DISR, CIFE and CONDRED, respectively, with the same number of selected features. For Krvskp and Waveform, the accuracies of each method are comparable because their ratio value is sufficiently large; WBFS still obtains the best accuracy in most cases.
![img-1.jpeg](img-1.jpeg)

Figure 2. Average classification accuracy based on three classifiers vs. different number of selected features for six datasets: (A) Lung, (B) Madelon, (C) Sonar, (D) Musk, (E) Krvskp, (F) Waveform.

In addition, we also compared the classification accuracy of feature selection subsets obtained by the WBFS algorithm and ensemble learning algorithm Random Forest (RF) based on the Isolet, Sonar, Waveform, Madelon, and Splice datasets, as shown in Figure S1. The results suggest that both methods have similar classification accuracy on

low-dimensional datasets such as Waveform, Sonar, and Splice. However, WBFS demonstrates a clear advantage in classification accuracy on high-dimensional datasets such as Madelon and Isolet.

All of the above experiments demonstrate that the WBFS technique performs better than the other methods in terms of classification accuracy, which lays the foundation for its application in bioinformatics data.

# 3.2.2. Using WBFS to Obtain the Top 10 Candidate Biomarkers 

We discretized the expression data into three bins by utilizing an equal-width strategy for WBFS according to the three expression states of protein (high expression, normal expression, and low expression). The top 10 proteins (MIG6, GAPDH, NDRG1_pT346, BRD4, CD26, TFRC, INPP4B, GSK3ALPHABETA, IGFBP2, and DUSP4) were screened by applying the WBFS algorithm, and they can be regarded as the candidate biomarkers that are most closely associated with the classification of lung cancer subtypes.

### 3.3. Using Bayesian Networks to Discover Causalities

In Figure 3, we can observe that the direct determinants for differentiating the subtypes of lung cancer include the protein markers MIG6, NDRG1_pT346, BRD4, CD26, INPP4B, and DUSP4, while the others can be considered as having an indirect impact on the classification outcome. Therefore, the Bayesian network (BN) provides significant factors for mechanistic studies at the molecular level.
![img-2.jpeg](img-2.jpeg)

Figure 3. The Bayesian network (BN) for the top 10 selected signatures and class label based on lung tumor dataset. These directed arrows represent the causal relationship between every two nodes. The cyan nodes are the key factors that are critical for subtype classification, and the yellow node represents the lung subtype classification.

3.4. ROC and Survival Analysis of the Candidate Protein Signatures

From Figure 4 and Table 6, it is possible to accurately distinguish LUAD and LUSC by each of the 10 protein biomarkers, as indicated by the AUC, which had a value up to 0.72 (*p* < 0.001). Multiple regression results of the 10 biomarkers indicated that eight protein markers, MIG6, GAPDH, NDRG1_pT346, BRD4, CD26, TFRC, INPP4B, and DUSP4, had significant differentiation abilities in disease classification between the LUSC and LUAD groups, as shown in Table S1. The detailed results of multiple regression analysis are shown in Table 6. The combination of the eight features achieved the best classification performance (AUC = 0.960, *p* < 0.001).

![img-3.jpeg](img-3.jpeg)

**Figure 4.** ROC curves of the 10 selected protein features and the combination test of 8 biomarkers. (**A**) shows the ROC curves of the 6 protein features of BRD4, CD26, DUSP4, GAPDH, GSK3ALPHABETA and IGFBP2; (**B**) shows the ROC curves of the 4 protein features of INPP4B, MIG6, NDRG1_pT346, TFRC and the combination test curve of 8 biomarkers.

**Table 6.** The Receiver Operating Characteristic (ROC) analysis of 10 selected protein biomarkers and a combination test of 8 biomarkers.


The detailed information of the eight biomarkers in combination test are shown in Table S1.

Figure 5 shows the Kaplan–Meier survival curves of the above factors, which demonstrates that MIG6, TFRC, INPP4B and IGFBP2 factors have a significant impact on the overall survival rate of LUAD patients (*p* < 0.05), and the MIG6, TFRC, and INPP4B factors have a significant negative prognosis correlation (*p* < 0.05). For LUSC patients, the factors of MIG6, GAPDH, CD26, and TFRC are all significantly correlated with the overall survival.

rate of patients (*p* < 0.05), and TFRC was the only factor that has a significant positive prognosis correlation (*p* < 0.05).

![img-4.jpeg](img-4.jpeg)

**Figure 5.** The Kaplan–Meier curves for lung adenocarcinoma (LUAD) (**A**–**D**) and lung squamous cell carcinoma (LUSC) (**E**–**H**). The values of all protein expressions were divided into high and low groups by cut-off values. The horizontal axis represents the survival time (day), and the vertical axis represents the overall survival rate.

### 4. Discussion

Lung cancer is one of the most common malignant tumors worldwide. Accurate classification of lung cancers into clinically significant subtypes is of utmost importance, making it critical for clinical and scientific researchers to discover new molecular markers and potential diagnostic and therapeutic targets [6,31]. Additionally, it is worth noting that the TCPA platform has already standardized protein expression information, while the TCGA database catalogs and explores cancer-causing genomic alterations, establishing a comprehensive "atlas" of cancer genomic signatures. By integrating the information from TCPA and TCGA, we could identify potential diagnostic and prognostic biomarkers for lung tumor subtypes to help understand the underlying mechanisms of tumorigenesis and improve approaches or standards for cancer diagnosis and therapy.

Feature selection is a fundamental technique for achieving efficient data reduction in high-dimensional datasets, such as those used in biological and text data mining [8,32,33]. This strategy is crucial for identifying accurate models and key factors in classification or clustering tasks [34,35]. Many studies have focused on developing feature selection strategies that return an optimal feature subset. Information theory-based approaches, such as mutual information and its extensions, can efficiently evaluate the relevance, redundancy, or interaction information [36,37,38]. However, most proposed approaches concentrate primarily on relevance or redundancy without considering interaction information. In this paper, we present a new weight-based feature selection (WBFS) method that considers the weight between selected features and candidate features based on information theory. Our proposed algorithm outperforms other methods in terms of classification performance, as demonstrated through experiments on 12 datasets and three classifiers.

Feature selection methods have an interesting application in biomarker discovery from high-throughput genomics data, which can guide clinical diagnosis by identifying the most discriminative biomarkers for a particular problem. In this study, the WBFS method was applied to real-world lung cancer datasets to obtain key protein biomarkers for the

classification of lung tumor subtypes. The causalities among the selected biomarkers were also explored using the Bayesian network (BN) strategy. The study found six promising protein biomarkers that were directly correlated with the classification of lung cancer subtypes, including MIG6, NDRG1_pT346, BRD4, CD26, INPP4B, and DUSP4. ROC analysis and survival curves based on selected proteins were also implemented. The ROC analysis has shown that 10 protein biomarkers were able to accurately distinguish between LUAD and LUSC with an AUC value of up to 0.72 and that eight of the protein markers had significant utility in disease classification. When combined, the eight features produced an AUC of 0.960 , indicating strong classification performance. Survival curves showed that MIG6, TFRC, INPP4B, and IGFBP2 had a significant impact on the overall survival rate of LUAD patients, while MIG6, GAPDH, CD26, and TFRC were all significantly correlated with the overall survival rate of LUSC patients. A study [39] demonstrated that MIG6 is essential for controlling the regulation of cell signaling in lung cancer cells.

This work involves some limitations that are worth noting. Firstly, our WBFS method is based on the feature ranking strategy, where the selection of the number of features $k$ is critical for achieving optimal classification performance and accuracy. Unfortunately, there is currently no effective strategy for determining the optimal value of $k$. Moreover, in the era of big data, it is more important than ever to identify the causal relationships among large datasets. However, most of the proposed feature selection methods are non-causal, and thus, it is necessary to establish a connection between non-causal feature selection and causality inference. In our future work, we plan to focus on two main aspects:
(1) Developing a more efficient feature selection algorithm that can automatically determine the optimal number of selected features based on the intrinsic dimension of a high-dimensional dataset.
(2) Investigating the relationship between causal and non-causal feature selection methods and applying non-causal feature selection methods to the Bayesian network. This will facilitate Bayesian network structure learning based on high-dimensional data.

# 5. Conclusions 

In this paper, we developed a new weight-based feature selection (WBFS) method to identify protein biomarkers to distinguish between two different subtypes (LUAD and LUSC) of lung cancer. Additionally, we further explored the direct influencing factors for lung cancer subtype classification using Bayesian networks. Six promising protein biomarkers (MIG6, NDRG1_pT346, BRD4, CD26, INPP4B, and DUSP4) specifically contributed to the subtype classification. These biomarkers, along with others, were able to accurately distinguish between LUAD and LUSC with a high AUC value. The identification and characterization of these biomarkers hold enormous potential for improving the diagnosis, treatment, and outcomes of lung cancer patients.

Supplementary Materials: The following supporting information can be downloaded at: https: //www.mdpi.com/article/10.3390/e25071003/s1, Table S1: Multiple regression results of the selected features in disease classification, Figure S1: BWFS vs. RF classification accuracy comparison based on five datasets: (A) Waveform, (B) Splice, (C) Sonar, (D) Madelon, (E) Isolet. The X axis shows the number of selected features, and the Y axis shows the average classification accuracy of three classifiers (KNN, NBC and LibSVM).

Author Contributions: Conceptualization, Y.W. and J.W.; methodology, Y.W. and X.R.; validation, X.R. and P.S.; writing, original draft preparation, Y.W.; writing, review and editing, X.G. and J.W.; supervision, J.W. and X.G.; funding acquisition, X.G. All authors have read and agreed to the published version of the manuscript.
Funding: This research was funded by the National Natural Science Foundation of China, grant number 81900134.

Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.

Data Availability Statement: The data presented in this study are available at https://github.com/ jihanwang/WBFS (accessed on 11 January 2023).

Conflicts of Interest: The authors declare no conflict of interest.
