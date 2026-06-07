# A framework for personalized medicine: prediction of drug sensitivity in cancer by proteomic profiling 

Dong-Chul Kim ${ }^{1}$, Xiaoyu Wang ${ }^{2}$, Chin-Rang Yang ${ }^{2}$, Jean X Gao ${ }^{1 *}$<br>From IEEE International Conference on Bioinformatics and Biomedicine 2011<br>Atlanta, GA, USA. 12-15 November 2011


#### Abstract

Background: The goal of personalized medicine is to provide patients optimal drug screening and treatment based on individual genomic or proteomic profiles. Reverse-Phase Protein Array (RPPA) technology offers proteomic information of cancer patients which may be directly related to drug sensitivity. For cancer patients with different drug sensitivity, the proteomic profiling reveals important pathophysiologic information which can be used to predict chemotherapy responses.


Results: The goal of this paper is to present a framework for personalized medicine using both RPPA and drug sensitivity (drug resistance or intolerance). In the proposed personalized medicine system, the prediction of drug sensitivity is obtained by a proposed augmented naive Bayesian classifier (ANBC) whose edges between attributes are augmented in the network structure of naive Bayesian classifier. For discriminative structure learning of ANBC, local classification rate (LCR) is used to score augmented edges, and greedy search algorithm is used to find the discriminative structure that maximizes classification rate (CR). Once a classifier is trained by RPPA and drug sensitivity using cancer patient samples, the classifier is able to predict the drug sensitivity given RPPA information from a patient.
Conclusion: In this paper we proposed a framework for personalized medicine where a patient is profiled by RPPA and drug sensitivity is predicted by ANBC and LCR. Experimental results with lung cancer data demonstrate that RPPA can be used to profile patients for drug sensitivity prediction by Bayesian network classifier, and the proposed ANBC for personalized cancer medicine achieves better prediction accuracy than naïve Bayes classifier in small sample size data on average and outperforms other the state-of-the-art classifier methods in terms of classification accuracy.

## Background

In this paper, we present a framework for personalized cancer medicine with RPPA and drug sensitivity. The goal of personalized medicine is to provide optimal drug treatment based on individual's drug sensitivity level, which will save unnecessary cost and treatment. To achieve this, it is assumed that drug sensitivity can be predicted by using quantitative patterns of protein

[^0]expression which represents molecular characteristics of individual patients [1,2]. More precisely, as medicinal effect is closely relevant to cancer signaling transduction pathways, proteomic profiling can provide important pathophysiologic cues regarding responses to chemotherapies $[3,4]$.
Figure 1 shows the process flow of the proposed framework for personalized cancer medicine. In step (1), a classifier is trained using RPPA and drug sensitivity data. A single classifier is generated per each drug which means the number of classifiers is same as the number of drugs. In step (2), RPPA of a patient's sample


[^0]:    * Correspondence: gao@uta.edu
    ${ }^{1}$ Department of Computer Science and Engineering, The University of Texas at Arlington, Arlington, TX 76019, USA
    Full list of author information is available at the end of the article

![img-0.jpeg](img-0.jpeg)

**Figure 1 Overview of the personalized medicine**. In step 1, each classifier is trained by RPPA and sensitivity of corresponding drug. In step 2 and 3, patient's RPPA is tested in each classifier, and the sensitivity of each drug is predicted. As a final step, only the drugs predicted to have low sensitivity are recommended to the patient.

is provided as a test data, then in step (3), the classifier predicts *High* or *Low* as a drug sensitivity of the given test sample (Different discrete levels of sensitivity are available such as *High/Neutral/Low*). Based on the result of the prediction, the classifier can recommend a set of drugs that is more likely to have *Low* sensitivity.

The prerequisite work of the proposed personalized medicine is the proteomic profiling of patients who have Different drug sensitivity level. The proteomic profiling is implemented by measuring the expression level of selected proteins which could be related to signaling pathways of the target cancer. To quantitatively measure the systemic responses of proteins in pathways, RPPA is used in conjunction with the quantum dots (Qdot) nano-technology. RPPA originally introduced in [5] is designed for quantitatively profiling protein expression levels in a large number of biological samples [6]. In RPPA, sample lysates are immobilized in series of dilutions to generate dilution curves for quantitative measurements being able to use only small amount (nanoliter) of sample while other protein arrays immobilize antibodies. After primary and secondary antibodies are probed, signal is detected by Qdot assays. Qdot is a nano-metal fluorophore with more bright and linear signal, and also Qdot prevents photo-bleaching effect that often occurs in organic fluorophores [7,8]. In addition, RPPA offers more accurate pathophysiologic information in a signaling pathway with posttranslational modifications (e.g. phosphorylation) not obtainable by gene microarray and protein-protein interactions.

For the classification in personalized medicine system, we employ a probabilistic approach, Bayesian Network Classifier where the class label (drug sensitivity) is predicted with its probability so that we can select only drugs that are predicted to have high probability of low sensitivity rather than any drugs that are predicted to have low sensitivity without considering the probability. Naive Bayes Classifiers (NBC) [9] (Figure 2(A)) competitively works with state-of-the-art classifiers in many complex real-world applications. Basically NBC assumes that all random variables (attributes) are conditionally independent to each other given a class variable. This assumption, however, is not realistic especially in biological domain because the interactive dependencies between cancer-related proteins in signaling pathways may exist. To overcome this limitation of NBC, how to involve the relationship between attributes for improving the classification performance has been the issue of Bayesian network classifier study during the past years. In [10], Friedman et al. proposed a *Tree-Augmented Naive Bayesian classifier* (TAN) by adding edges into the structure of NBC. Augmented edges in TAN are restricted to tree structure and learning structure algorithm is based on the conditional mutual information between two variables given a class variable. In this paper, we focus on *augmented naive Bayes classifier* (ANBC) where each attribute can have at least class variable as a parent and at most two parents and the structure of augmented edges is not necessary to be tree. To find discriminative structure, we propose a new method based on *local classification rate* (LCR) to score augmented edges and greedy search algorithm to find the ANBC structure that has the highest classification rate. In the experiments, the proposed ANBC for personalized medicine is compared to state-of-the-art classifiers including NBC and TAN in lung cancer data.

The paper is organized as follows. In the methods section, the basic concept of Bayesian network and Bayesian network classifier are reviewed, and we give a detailed account of the proposed ANBC. In the results section, we present the experimental result comparing to other classification algorithms. Finally, we conclude with summary and future work in the conclusion section.

# **Method**

## **Bayesian networks**

A Bayesian network is a directed acyclic graph that encodes a joint probability distribution over a set of random variables *X* = {*X*<sub>1</sub>,...,*X*<sub>*n*</sub>} (Variable, attribute, and

![img-1.jpeg](img-1.jpeg)

Figure 2 An example of the Bayesian network structure for NBC and augmented NBC (ANBC). (A) In NBC, all the attributes are conditionally independent given the class variable. (B) In ANBC, each attribute have at most one other attribute as an additional parent but augmented edges of ANBC are not necessary to constitute the tree structure which means that any attribute can have only class variable as a single parent.

feature are interchangeably used). In this paper, we assume that all variables are discrete. A Bayesian network is defined by a pair B = (G, Θ). The first component G is a network structure where each node represents a variable in X. If there is a directed edge from variable X<sup>j</sup> to X<sup>i</sup> (X<sup>j</sup> → X<sup>i</sup>), X<sup>j</sup> is a parent of X<sup>i</sup>. For each variable X<sup>i</sup>, a set of parent variables is denoted by ∏<sub>X<sup>i</sup></sub>, and X<sup>i</sup> takes the state x<sub>ik</sub> that is the kth state of x<sub>i1</sub>, ..., x<sub>ir</sub>, where r<sub>i</sub> is the number of possible states of X<sup>i</sup>. The second component Θ is a set of parameters for local conditional probability distributions representing the probability of a state of the variable given states of its parents. A parameter is defined as

$$P_B(X_i = x_{ik} \mid \Pi_{X_i} = \pi_{ij}) = \theta_{ijk} \tag{1}$$

where π<sub>ij</sub> ∈ {π<sub>i1</sub>, ..., π<sub>iq</sub>} is the jth parent configuration (the states of parents) of ∏<sub>X<sup>i</sup></sub> and q<sub>i</sub> is the number of possible parent configuration given ∏<sub>X<sup>i</sup></sub>. The parameter θ<sub>ijk</sub> denotes the probability that the state of X<sup>i</sup> is x<sub>ik</sub> given π<sub>ij</sub> as the state of ∏<sub>X<sup>i</sup></sub>. A structure of Bayesian network defines a unique joint probability distribution over X given by the product of local distributions as

$$P_B(X_1, \dots, X_n) = \prod_{i=1}^n P_B(X_i \mid \Pi_{X_i}) \tag{2}$$

### Bayesian networks classifier

**Bayesian Network Classifier (BNC)** is a probabilistic classifier based on Bayes' theorem. A set of random variables is defined as X = {X<sub>1</sub>,..., X<sub>n-1</sub>, C} where nth variable is a class variable. Bayesian network classifier predicts the label c that maximizes the posterior probability P<sub>B</sub>(C = c|X<sub>1</sub> = x<sub>1</sub>,..., X<sub>n-1</sub> = x<sub>n-1</sub>) given a Bayesian network structure (Figure 2) and an instance {x<sub>1</sub>,..., x<sub>n-1</sub>} of attributes.

### Naive Bayes classifier

In **Naive Bayes Classifier (NBC)**, the posterior probability is defined as

$$p(C | X_1, \dots, X_{n-1}) = \frac{1}{Z} p(C) \prod_{i=1}^{n-1} p(X_i | C) \tag{3}$$

where p(C)∏<sub>i=1</sub><sup>n-1</sup> p(X<sub>i</sub>|C) (prior×likelihood) is same as joint probability in (2) since it is assumed that each variable X<sup>i</sup> is conditionally independent of every other variable X<sup>j</sup> for i ≠ j given class variable C as a parent of X<sup>i</sup> (Figure 2(A)); we can cancel the constant Z since the evidence Z<sub>c</sub> p(X<sub>1</sub>,..., X<sub>n-1</sub>), is independent of C in maximizing the posterior. Hence, the classifier is defined as argmax<sub>c∈C</sub> p(C = c)∏<sub>i=1</sub><sup>n-1</sup> p(X<sub>i</sub> = x<sub>i</sub> | C = c) given a test instance {x<sub>1</sub>,..., x<sub>n-1</sub>}. In our application, discrete class variable C = {High, Low} indicates a drug sensitivity level, and an attribute X<sup>i</sup> refers to a discretized protein expression level in RPPA. So, in NBC, it is assumed that each protein is conditionally independent of other protein and dependent of only the drug sensitivity. However, this assumption is unrealistic since the selected proteins of RPPA could have the biological interactions in the signaling pathway affecting the efficacy of the drug.

To calculate the likelihood in the classifier, firstly the **maximum likelihood (ML)** parameters that maximize log likelihood (LL) can be obtained by frequency estimation with training data in the form

$$\hat{\theta}_{ijk} = \frac{N_{ijk}}{N_{ij}} \tag{4}$$

where N<sub>ijk</sub> denotes the number of instances in training data where X<sup>i</sup> = x<sub>ik</sub> and ∏<sub>X<sup>i</sup></sub> = π<sub>ij</sub>, and N<sub>ij</sub> = ∑<sub>i=1</sub><sup>n</sup> N<sub>ijk</sub>. After the parameters are estimated, then these parameters Θ = {θ<sub>ijk</sub>}<sub>i∈{1,...,n|,j∈{1,...,q|,k∈{1,...,r|}}</sub> are used to

compute the likelihood $p\left(X_{i} \mid C\right)$ of the classifier given a test instance and a class label. In addition, the logarithm of likelihood $\left(\sum \log p\left(X_{i} \mid C\right)\right)$ is practically taken to avoid numerical underflow in the implementation instead of products of all likelihoods, $\Pi p\left(X_{i} \mid C\right)$.

## Augmented naive Bayes classifier

To solve the limitation of NBC, Friedman et al. [10] introduced TAN classifier where edges are added in the structure of NBC. These additional edges are called augmented edge. The idea is that if a strong dependency between $X_{1}$ and $X_{2}$ exists, the directed edge is added between $X_{1}$ and $X_{2}$ (Figure 2(B)). The maximum number of edges added to relax the independent assumption between variables is $n-1$, but the augmented edges of TAN are limited to construct tree-like Bayesian network. Instead, We are focusing on augmented naive Bayes classifier (ANBC) where an attribute $X_{i}$ have at least the class variable as a parent and at most two parents, the class variable and another attribute $X_{j}$, and the class variable has no parent. More precisely, the augmented edges of TAN are restricted to tree structure but the augmented edges of ANBC are not necessary to be tree structure (i.e. Some node may not have an augmented edge in ANBC). Once the structure is constructed and the parameters are estimated with training data, we can classify an instance into a class label that maximizes the posterior given by

$$
p(C) \prod_{i=1}^{m} p\left(X_{i} \mid \Pi_{X_{i}}^{C}, C\right)
$$

where $\Pi_{X_{i}}^{C}$ denotes the parent set of variable $X_{i}$ except the class variable $C$.

## Discriminative structure learning

We focus on discriminative structure learning for ANBC since it is shown that a good discriminative structure is sufficient to generate good discriminative classifier in the comparative research [11]. Indeed, BNC with discriminative structures and generative parameters outperforms BNC with not only discriminative structures and discriminative parameters but also generative structures and either discriminative or generative parameters in their experimental results. In [11,12], the classification rate (CR) is used to score how a given structure is discriminative. The CR is defined as

$$
C R=\frac{1}{|S|} \sum_{m=1}^{|S|} I\left(B N C\left(x_{1}^{m}, \ldots, x_{n-1}^{m}\right), c^{m}\right)
$$

where $|S|$ is the number of instances in training data $S . B N C\left(x_{1}, \ldots, x_{n-1}\right)$ is an Bayesian network classifier, $\arg$ $\max _{c \in C} p\left(C \mid X_{1}, \ldots, X_{n-1}\right)$, given a Bayesian network structure. $I\left(\hat{c}^{m}, c^{m}\right)$ is an indicator function for $\hat{c}^{m}=c^{m}$ where $\hat{c}^{m}$ is the class label predicted by $B N C\left(x_{1}^{m}, \ldots, x_{n-1}^{m}\right)$ and $c^{m}$ is the correct class label (the
state of the class variable $C$ of the $m_{t h}$ instance). To estimate CR of a given structure, BNC is trained and tested on the training data $S$ by using leave-one-out. In [11], they use the greedy method, hill climbing search, to find the structure that has local optimum CR in updating (adding or deleting augmented edge) the structure iteratively. However, CR based scoring and searching approach is computationally expensive than other method due to the exponential searching space $\left((n-1)^{n^{-}}\right.$ ${ }^{2}$ ) as training and testing of updated structure is repeated in every iterations. In order to improve CR based approach, we propose a new algorithm in which the basic idea is to reduce the search space by excluding unnecessary edges. Each edge between attributes is evaluated by a modified CR. We call the proposed score function Local Classification Rate (LCR) as the score measures how each augmented edge is likely to contribute the increase of classification rate when only the edge is added in NBC. LCR is defined as

$$
L C R_{i j}=\frac{1}{|S|} \sum_{m=1}^{|S|} I\left(A N B C_{i j}\left(x_{1}^{m}, \ldots, x_{n-1}^{m}\right), c^{m}\right)-I\left(N B C\left(x_{1}^{m}, \ldots, x_{n-1}^{m}\right), c^{m}\right)
$$

where $A N B C_{i j}$ is a ANBC where the single directed edge from $j$ to $i\left(E_{i j}\right)$ is augmented in the structure of NBC. More precisely, $A N B C_{i j}\left(x_{1}^{m}, \ldots, x_{n-1}^{m}\right)$ is defined as $\arg \max _{i \mid C} p\left(X_{i}=x_{i} \mid X_{j}=x_{j}, C=c\right) \Pi_{h, h \neq i} p\left(X_{h}=x_{h} \mid\right.$ $C=c$ ). As the second term is CR of NBC, it is constant with respect to $i$ and $j . L C R_{i j}>0$ indicates that the edge $E_{i j}$ could increase the classification rate of ANBC when $E_{i j}$ is augmented in the structure of NBC. For ANBC, the number of all possible augmented edges are $(n-1)$ ( $n-2$ ). After we calculate LCR for all possible augmented edges, the edges that have negative LCR are excluded from structure searching space. To decrease more the number of available augmented edges, we select the edge $E_{i j}$ only if $L C R_{i j}$ is equal to the max $L C R_{i h}$ for $h \in X^{i t}$. Because variable $X_{i}$ can have only a single $X_{j}$ as a parent except class variable, only the variable that maximizes $\hat{L C R}_{X_{i} \Pi_{X_{i}}^{C}}$ is selected as the parent of $X_{i}$. In searching step, the structure is iteratively updated by randomly adding or deleting an augmented edge maintaining the acyclic property and the limited number of parents per attribute (Each attribute can have at most two parents including class variable).

## Experiments

## Lung cancer data

In this section, lung cancer data is used to gauge the performance of proposed personalized medicine system with a new score function LCR for learning discriminate structure of ANBC. RPPA for lung cancer consists of 55 antibodies (Table 1), 75 cell lines. There are 24 drugs to measure the drug sensitivity of each cell lines but a drug is not tested in all cell lines which mean each drug has

Table 155 antibodies of used in RPPA


Prefix $p$ indicates phosphorylation. tested in Different set of cell lines. The sensitivity of each drug is measured with 43 cell lines on average. As a preprocessing, the drug sensitivity is discretized into 2 states (High or Low) by K-means clustering algorithm in which the maximum and minimum values of drug sensitivity are used for initial centroid. The protein expression level of RPPA is discretized by minimum entropy based discretization method [13].

## Experimental setup

We conducted the comparative evaluations with the following classification algorithms: Support Vector

Machine with three Different kernels, Linear kernel (SVML), Polynomial kernel (SVMP), and Radial basis function kernel (SVMR), Logistic Regression (LR), Random Forest (RF), Tree-Augmented Naive Bayes (TAN) [10], NBC, and ANBC we proposed. To evaluate the performance of Different methods, we measure the prediction accuracy on average using leave-one-out estimation Since the structure is randomly updated in searching, 5 times leave-one-out are performed in ANBC. The original continuous values of RPPA are used in SVM, LR, and RF. For the parameter estimation, only maximum likelihood parameters are used for NBC, TAN, and ANBC since we only compare the structure leaning methods rather than discriminative parameter learning methods. To avoid zero conditional probability in logarithm of likelihood when we calculate the joint probability, we set $\hat{\theta}*{i j k}=\frac{\sum*{i=1}^{N_{i j k}} C_{i j k}^{N_{i j k}}}{N_{i j k}}=0.5, N_{i j}=1$ if $N_{i j k}=0$ or $N_{i j}=0$. Accuracy is calculated by a ratio of the number of correct predictions to the total number of samples in leave-one-out estimation. In addition, for reasonable comparison, feature selection is applied for all classification methods because some of methods may not produce a good result in high dimension data and also all 55 proteins may be not related to drug sensitivity directly. For SVM, LR, and RF, attributes are selected by using Information Gain [14] and Ranker

Table 2 Accuracy of sensitivity prediction for 24 drugs with 20 selected features


implemented in Weka [15]. To select proteins (features) in NBC, TAN, and ANBC, we used Mutual Information between attribute and class variable. The number of features to be selected is predefined as 10,20 , and 30 .

## Experimental results

Table 2 shows the classification accuracy of each classification method for 24 drugs in 20 selected features (The results in 10 and 30 features are in the additional file 1). Over all, ANBC outperformed support vector machine classification with three Different kernels, logistic regression, and random forest algorithm in all feature sets (10, 20, and 30 features). ANBC outperforms NBC in 10 and

20 selected features but not 30 features. Surprisingly NBC performed better than TAN which has developed to solve the limitation of independence assumption in NBC. The reason for this might be the small sample size of our data ( 43 per drug on average) as it is shown that NBC can outperform the discriminatively trained model for small sample data sets in the empirical results of [16] and it is true that the number of samples should be sufficient for conditional probability (likelihood in the classifier form) to represent the data. In Table 2, ANBC achieved $100 \%$ accuracy in four drugs, Docetaxel, Gemcitabine, Orexin, and Paclitaxel. Logistic regression shows the lowest accuracy, $64.61 \%$ on average, and SVM with Radial basis function
![img-2.jpeg](img-2.jpeg)

Figure 3 Scatter plots of the accuracy of the proposed method vs. state-of-the-art classifiers.

![img-3.jpeg](img-3.jpeg)
kernel has the lowest accuracy, $17.78 \%$ in Cyclopamine. The scatter plot (Figure 3) is for comparison of two algorithms. Each point represents a data set ( 24 drugs) where the $y$ and $x$ coordinate of a point is the accuracy rate according to ANBC and counterpart respectively. The red points above the diagonal line represent the drug whose sensitivity is predicted better in ANBC (vertical axis) than counterpart (horizontal axis). In Figure 3(f), 6 red points are relatively far from the diagonal line while NBC has better accuracy in 3 drugs (blue points). ANBC also has better accuracy than TAN in most of the drugs except four drugs (Figure 3(g)). Figure 4 shows the accuracy of each classifier using Different feature sets. The performance of each method is similar to Table 2. ANBC, NBC, and TAN outperform other methods in all three feature sets. In ANBC and NBC, the prediction accuracy slightly increases when they have larger number of features while the performance of TAN and SVM is independent of the number of features. In LR and RF, the accuracy is decreased with more features. The results imply that Bayesian network based classifiers (ANBC, NBC, and TAN) can work more effectively than other methods in RPPA and drug sensitivities, and it is confirmed that the classification for the drug sensitivity prediction with RPPA can be potentially improved by effectively using the dependency of proteins. However, the result of TAN implies that too many augmented edges may decrease the accuracy in small sample size data.

## Conclusion

In this paper, we introduce the personalized medicine with RPPA and drug sensitivity. The goal of personalized medicine is to provide the optimal therapy to patients who have Different biological profile regarding the target cancer. For this goal, Bayesian network classifier is applied for the drug sensitivity prediction given patient's RPPA. We propose a new score function LCR for learning discriminative structure of Bayesian network classifier. All augmented edges are scored by LCR that is based on the difference between CR before and after a single edge is augmented. In other words, the score represents how the edge augmented in NBC is likely to increase the classification rate in ANBC. Based on the scored edges, the discriminative structure is discovered through Hill-Climbing search. Since it is known that NBC normally outperforms discriminative learning algorithm for small sized sample data (In our data the number of samples on average is 43), we focus on the idea that is to augment only a least number of edges to improve the performance mostly maintaining the advantage of NBC structure while TAN augments too many edges in NBC. In the experiments, ANBC with proposed score function is compared to well-known classification algorithms such as Support vector machine, Logistic regression, and Random forest. We also compare to Bayesian network classifiers, TAN and NBC with generative parameters. The results show that the ANBC outperforms other classification algorithms and achieves slightly better accuracy than NBC in small sized sample data sup-porting the claim that the dependency of proteins can be used to improve the sensitivity prediction for the personalized medicine. To overcome the limitation of sample size, we plan to investigate more about discriminative parameter learning and effective feature selection for Bayesian network classifier as future works.

## Additional material

Additional file 1: Accuracy of sensitivity prediction for 24 drugs with 10 and 30 selected features. The file includes two tables for classification accuracy in 10 and 30 selected features.

## Acknowledgements

This article has been published as part of Proteome Science Volume 10 Supplement 1, 2012: Selected articles from the IEEE International Conference on Bioinformatics and Biomedicine 2011: Proteome Science. The full contents of the supplement are available online at http://www.proteomesci. com/supplements/10/S1.

## Author details

${ }^{1}$ Department of Computer Science and Engineering, The University of Texas at Arlington, Arlington, TX 76019, USA. ${ }^{2}$ Simmons Comprehensive Cancer Center, The University of Texas Southwestern Medical Center, Dallas, TX 75390, USA.

## Authors' contributions

Dong-Chul Kim and Jean Gao contribute the computational algorithm design and the manuscript writing. Xiaoyu Wang carried out the biological experiment for the RPPM data generation. Chin-Rang Yang was responsible for the overall project layout and direction.

## Competing interests

The author(s) declare that they have no competing interests.

Published: 21 June 2012

## Submit your next manuscript to BioMed Central and take full advantage of:

- Convenient online submission
- Thorough peer review
- No space constraints or color figure charges
- Immediate publication on acceptance
- Inclusion in PubMed, CAS, Scopus and Google Scholar
- Research which is freely available for redistribution

Submit your manuscript at www.biomedcentral.com/submit
(3) BioMed Central