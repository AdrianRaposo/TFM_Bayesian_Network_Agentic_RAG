# MicroRNA Expression Profiles for Classification and Analysis of Tumor Samples* 

Dang Hung TRAN ${ }^{\dagger \mathrm{a})}$, Nonmember, Tu Bao HO ${ }^{\dagger \dagger \mathrm{b})}$, Member, Tho Hoan PHAM ${ }^{\dagger \mathrm{c})}$, Nonmember, and Kenji SATOU ${ }^{\dagger \dagger \dagger \mathrm{d})}$, Member


#### Abstract

SUMMARY One kind of functional noncoding RNAs, microRNAs (miRNAs), form a class of endogenous RNAs that can have important regulatory roles in animals and plants by targeting transcripts for cleavage or translation repression. Researches on both experimental and computational approaches have shown that miRNAs indeed involve in the human cancer development and progression. However, the miRNAs that contribute more information to the distinction between the normal and tumor samples (tissues) are still undetermined. Recently, the high-throughput microarray technology was used as a powerful technique to measure the expression level of miRNAs in cells. Analyzing this expression data can allow us to determine the functional roles of miRNAs in the living cells. In this paper, we present a computational method to (1) predicting the tumor tissues using high-throughput miRNA expression profiles; (2) finding the informative miRNAs that show strong distinction of expression level in tumor tissues. To this end, we perform a support vector machine (SVM) based method to deeply examine one recent miRNA expression dataset. The experimental results show that SVM-based method outperforms other supervised learning methods such as decision trees, Bayesian networks, and backpropagation neural networks. Furthermore, by using the miRNA-target information and Gene Ontology annotations, we showed that the informative miRNAs have strong evidences related to some types of human cancer including breast, lung, and colon cancer.


key words: microRNA, gene regulation, cancer, support vector machine, feature selection

## 1. Introduction

MicroRNAs (miRNAs) are a class of small functional noncoding RNAs (20-24nt) that can play important regulatory roles in animals and plants. They regulate the expression of target genes by binding to specific sites in the $3^{\prime}$ UTR of the messenger RNAs (mRNAs) [1], [2]. Each miRNA can bind to many different transcripts and down-regulates protein expression of multiple target genes. Through experimental approaches and bioinformatics applications, thousands of miRNAs have been identified in complex eukary-

[^0]otic genomes. Together with this, greater than one third of all human genes have been predicted to be miRNA targets [3]-[5]. Therefore, miRNAs are an abundant and important class of regulatory molecules. However, the cellular function of most mammalian miRNAs is still unknown [6]. Hence, it is necessary to understand biological mechanisms that miRNAs are involved.

Recent studies have been shown that several miRNAs were directly involved in human cancers (including lung, breast, brain, liver, and colon cancer) [7]-[10]. While some miRNAs play functions as oncogenes, other ones as tumor suppressors. This is because more than $50 \%$ of miRNA genes are located in cancer-associated genomic regions or fragile sites [11]. This evidence also suggests that miRNAs may play a more important role in the human cancers than was previously thought. However, it is still not clear which miRNAs contribute the most information to the specific cancer diseases.

Recently, the high-throughput microarray technology is used as a powerful technique to measure the expression level of miRNAs at biological molecules. While traditional methods only allow one or a few miRNAs to be examined at once, the microarray techniques measure the expression level of thousands of miRNAs simultaneously. Analyzing this expression data can allow us to determine the functional roles of miRNAs in the living cells. Furthermore, investigating of miRNA expression data at the level of biological modules, rather than individual genes, is recognized as an important factor for understanding the cancer regulatory mechanisms [12].

In 2005, Zheng et al. [13] used a Discrete Function Learning (DFL) algorithm to find the subset of miRNAs that shows strong distinction of expression levels in normal and tumor tissues. The DFL algorithm is based on a theorem of information theory. The advantage of using the DFL algorithm is to remove the irrelevant and redundant features so that the induction algorithms may produce better prediction accuracies. To do this, the algorithm needs to examine all possible subsets of features, however, it is a NP-hard problem. Hence, in their paper they proposed several heuristics to reduce the searching space for the DFL algorithm. It thus makes their results are unreliable. Other method, proposed by Kim et al. [14], used a random hypernetwork to identify the gene modules associated with cancers from miRNA microarray data. Hypernetwork is a generalization of the hypergraph by assigning weights to its hyperedges. However,


[^0]:    Manuscript received May 7, 2010.
    Manuscript revised September 30, 2010.
    ${ }^{\dagger}$ The authors are with the Hanoi National University of Education, Vietnam.
    ${ }^{\dagger \dagger}$ The author is with the Japan Advanced Institute of Science and Technology, Nomi-shi, 923-1292 Japan.
    ${ }^{\dagger \dagger \dagger}$ The author is with the Kanazawa University, Kanazawa-shi, 920-1192 Japan.
    ${ }^{\dagger}$ The early version of this paper was presented at the 3rd International Conference on Knowledge, Information and Creativity Support Systems
    a) E-mail: hungtd@hnue.edu.vn
    b) E-mail: bao@jaist.ac.jp
    c) E-mail: hoanpt@hnue.edu.vn
    d) E-mail: ken@t.kanazawa-u.ac.jp

    DOI: 10.1587/transinf.E94.D. 416

to construct a hypernework, they faced a combinatorial explosion problem. In order to solve this problem, they generated a hypernetwork by repeating a random hypergraph process. Thus, their hypernetwork was strongly depended on the initial process of generating a first hypergraph, however - it is a random process. Though the experimental results showed that their method provided a competitive performance to BNN and SVM, but they did not proclaim the value of parameters of SVM classifiers that they used to report the results.

In this paper, we present a computational method to (1) predicting the tumor tissues using high-throughput miRNA expression profiles; (2) finding the informative miRNAs that show strong distinction of expression level in tumor tissues. To this end, we perform a supervised learning method to deeply examine one recent miRNA expression dataset [15]. Specifically, we present a support vector machine (SVM) classifier to predicting and analyzing tumor tissues. An SVM is one of the most popular machine learning algorithms and it has good performance in classification problems. In fact, the experimental results show that the SVMbased method outperforms other methods such as decision trees, Bayesian networks, and backpropagation neural networks.

Moreover, to answer the question of which miRNA is important for discriminating between normal and tumor samples, we used a two-step feature selection method to find a subset of informative miRNAs that have strong relevance to the tumor class. The investigation into the biological significance of target genes of informative miRNAs reveals strong evidences related to some types of human cancer, including breast, lung, and colon cancer.

## 2. Method

### 2.1 Support Vector Machines for Binary Classification

The support vector machine (SVM) is a learning technique based on statistical learning theory, which from a set of positively and negatively labeled training vectors learns a classifier that can be used to classify new unlabeled test samples. SVM learns the classifier by mapping the input training samples into a possibly high-dimensional feature space, and seeking a hyperplane in this space which separates the positive examples from the negative ones with the largest possible margin (Fig. 1). If the training set is not linearly separable, SVM finds a hyperplane, which optimizes a tradeoff between good classification and large margin.

The implementation of SVM is as follows. Let $\left(x_{i}, y_{i}\right)$, $i=1, \ldots, \ell$, be a training dataset, where $x_{i}$ is a vector and $y_{i}= \pm 1$ is a class attribute. SVM training solves the following primal problem:
![img-0.jpeg](img-0.jpeg)

Fig. 1 An illustration of the SVM training method. Red and green circles indicate positive and negative samples to be classified.

$$
\left\{\begin{array}{l}
\min _{w, b, \xi} \frac{w^{T} w}{2}+C \sum_{i=1}^{\ell} \xi_{i} \\
y_{i}\left(w^{T} \phi\left(x_{i}\right)+b\right) \geq 1-\xi_{i}, \quad i=1, \ldots, \ell \\
\xi_{i} \geq 0, \quad i=1, \ldots, \ell
\end{array}\right.
$$

Its dual is a quadratic optimization problem:

$$
\left\{\begin{array}{l}
\min _{\alpha} \frac{\alpha^{T} Q \alpha}{2}-e^{T} \alpha \\
0 \leq \alpha_{i} \leq C, \quad i=1, \ldots, \ell \\
y^{T} \alpha=0
\end{array}\right.
$$

where $e$ is the vector of all ones, $C>0$ is an error penalty parameter, $y=\left\{y_{i}\right\}_{i=1, \ldots, \ell}, Q_{i j}=y_{i} y_{j} K\left(x_{i}, x_{j}\right), K\left(x_{i}, x_{j}\right)=$ $\phi\left(x_{i}\right)^{T} \phi\left(x_{j}\right)$ is a kernel function, and $\phi\left(x_{i}\right)$ maps $x_{i}$ into a higher (maybe infinite) dimensional space. So $K\left(x_{i}, x_{j}\right)$ is a symmetric positive definite function that reflects the similarity between examples $x_{i}$ and $x_{j}$. In this research, we employed a linear function $K\left(x_{i}, x_{j}\right)=x_{i} \cdot x_{j}$, a polynomial function $K\left(x_{i}, x_{j}\right)=\left(x_{i} \cdot x_{j}+1\right)^{\delta}$, and a radial basis function (RBF) $K\left(x_{i}, x_{j}\right)=\exp \left(-\gamma\left(x_{i}-x_{j}\right)^{2}\right)$ as kernel functions. The SVMs classification function, once trained, has the following form:

$$
f(x)=\sum_{i} \alpha_{i} y_{i} K\left(x, x_{i}\right)+b
$$

where $\alpha=\left\{\alpha_{i}\right\}_{i=1, \ldots, \ell}$ is the solution of the above dual problem and $b$ is in the solution of the primal problem. Based on Karush-Kuhn-Tucker theory [16], the solutions of the primal and dual problems satisfy the following equation:

$$
\alpha_{i}\left\{y_{i}\left(w^{T} \phi\left(x_{i}\right)+b\right)-1+\xi_{i}\right\}=0
$$

Therefore, if $\alpha_{i} \neq 0$ for some $i$, then $y_{i}\left(w^{T} \phi\left(x_{i}\right)+b\right)-1+\xi_{i}=$ 0 . In this case, $x_{i}$ is called a support vector (see Fig. 1).

SVMs have a solid theoretical background, a good performance in practice, and a guaranteed global optimum. It can also handle large datasets and is easier to implement and train than a neural network. A more detailed description of SVMs can be found in [17], [18].

2.2 Ranking Informative Feature Using Fisher Criterion and Linear SVM

Ranking informative (discriminative) features is of fundamental and practical interest in data mining and knowledge discovery. The aim here is to select a subset of relevant features available from the dataset that most contribute to distinguishing instances from different classes. In this research, we use two feature ranking methods to select the informative miRNAs that contribute more information to tumor class. First, we rank all miRNAs based on their Fisher scores and then use a SVM-based feature selection method for ranking miRNAs.

Fisher method. Fisher criterion is one of statistical criteria that is simple, effective and independent of the choice of classification methods. In this criterion, the discriminative strength of each feature is defined as follows. Given a dataset $X$ with two classes, denote instances in class 1 as $X^{1}$ and those in class 2 as $X^{2}$. Suppose $\tilde{x}_{j}^{k}$ is the average of the $j$ th feature in $X^{k}$, the Fisher score of the $j$ th feature is:

$$
F(j)=\frac{\left(\tilde{x}_{j}^{1}-\tilde{x}_{j}^{2}\right)^{2}}{\left(s_{j}^{1}\right)^{2}+\left(s_{j}^{2}\right)^{2}}
$$

where

$$
\left(s_{j}^{k}\right)^{2}=\sum_{s \in X^{k}}\left(x_{j}-\tilde{x}_{j}^{k}\right)^{2}
$$

The numerator indicates the discrimination between two classes and the denominator indicates the scatter within each class. The larger the Fisher score is, the more likely this feature is more discriminative.

SVM-based method. SVM has been successfully applied to feature selection [19]-[21]. When SVM uses a linear kernel, it finds an optimal hyperplane that separates the positive from the negative class in the original space (not mapping into a higher dimensional space). This optimal hyperplane has then the following form (replacing $K(x, y)=x . y$ in Eq. (3)):

$$
f\left(X=\left(f_{1}, f_{2}, \ldots, f_{m}\right)\right)=\sum_{i=1}^{m} w_{i} f_{i}+b
$$

We can change the sign of the weights $w_{i}, i=1, \ldots, m$, and $b$ in the above function such that if $f(X)>0$ then $X$ would be classified as a positive example and otherwise, as a negative example. It can be clearly seen that if $w_{i}$ is positive, then feature $i$ would support the positive class. Otherwise, this feature would support the negative class (or prevent the positive class), and the larger the absolute value of $w_{i}$, the stronger feature $i$ supports (or prevents) the respective class. From this remark, we define the weight $w_{i}$ as the support of feature $i$.

### 2.3 Validating of Target Genes of Informative miRNAs Using Gene Ontology

With the current knowledge of combinatorial coregulation,
it is hard for us to directly validate the predicted target genes of the informative miRNAs. Fortunately, using Gene Ontology (GO) [22] we can validate the target genes of each miRNA with respect to biological processes, cellular components and molecular functions. This validation can be achieved by searching for statistically significant GO terms associated with genes.

## 3. Results and Discussions

### 3.1 Datasets

In this work, we used a microarray dataset, which contains expression profiles of miRNAs in human. The original experimental dataset was obtained from Lu et al. [15]. This includes the expression profiles of 151 miRNAs on 223 samples. Of these 223 samples, 166 samples are normal samples from six different tissues, including colon, kidney, prostate, uterus, lung, and breast. The remaining 57 samples are tumor samples from the same six different tissues. We used normal samples as positive data and tumor samples as negative data in our classification problem. To validate the biological significance of target genes of miRNAs, we obtained a set of computationally predicted human miRNA target genes from Krek et al. [23]. The current miRNA target prediction methods are mainly based on the principle of miRNA-target interactions, and the accuracy of these methods has been confirmed by experimental validation of randomly selected miRNA targets [24] and by largescale gene expression profiling studies [25]. Up to $90 \%$ of the randomly selected miRNA targets from the predictions by Krek et al. [23] has been validated as true targets [24].

### 3.2 Prediction Results

In general, a 10 -fold cross-validation is good enough for evaluating the predictive accuracy of classification methods. However, in case of small data (as the dataset used in this study), a leave-one-out cross-validation (LOOCV) performs better than the 10 -fold cross-validation. LOOCV simulates the performance of a classification algorithm on unseen samples. In LOOCV, the algorithm is repeatedly retrained, leaving out one sample in each round, and testing each sample on a classifier that was trained without this sample. In our experiments, we used SVMs with three kernel functions (RBF, Linear, and Polynomial kernels) to perform LOOCVs on the miRNA expression dataset (Sect. 3.1). Three popular criteria of Precision, Recall, and F1 are used to evaluate the results. They are defined as follows:

$$
\begin{aligned}
& \text { Precision }=T P /(T P+F P) \\
& \text { Recall }=T P /(T P+F N) \\
& F 1=2 *(\text { Precision } * \text { Recall }) /(\text { Precision }+ \text { Recall })
\end{aligned}
$$

Where $T P, T N, F P$, and $F N$ are the number of true positive, true negative, false positive and false negative examples, respectively. $F 1$ is the harmonic mean of Precision

and Recall, it is maximized when Precision and Recall are maximized at the same time. We also use the area under the curve (AUC) of a receiver operating characteristic (ROC) curve for describing classification performance. The AUC gives a good indication for the overall performance of classifier and whether one classifier performs better than the other classifiers. The bigger value is the better than small ones.

We used LIBSVM (version 2.84) [26] for training and test our SVM classifiers. For preprocessing data, we developed a C++ program to convert the dataset from delimited file format to the format of the LIBSVM. In the other hand, we also conducted a simple scaling on the data by transforming each attribute-value to the range of $[0,1]$. Three kernel functions (RBF, Linear, and Polynomial) were used in our experiments to validate the classification ability of the SVM. For RBF kernel, we tried several values of $C$ and $\gamma$ for finding good parameters. We found that the best accuracy was reached when $C=1.0$ and $\gamma=0.001$. The performance of the method is shown in Table 1. As can be seen that, in our experiment, we can obtain the highest result of Precision $=0.92$, Recall $=0.98, F 1=0.95$, and $A U C=0.98$ when using SVM with RBF kernel. This indicates that the SVM-based method with RBF kernel is suitable for distinguishing the tumor samples from normal samples when using miRNA expression data.

To make a comparison of the SVM-based method to other classification methods, we used the Weka (version 3.5) [27] to evaluate the performance of backpropagation neural network (BNN), decision tree (DT), $k$-nearest neighbor ( kNN ), and bayesian network (BN) methods. Accord-

Table 1 The results of SVM classifiers on the miRNA expression dataset.


ing to making a fair comparison, we carry out all experiments by using LOOCV on the same dataset that mentioned in Sect. 3.1. We also carefully selected appropriate parameters for each method. The prediction results of all compared methods, including ours, are shown in Fig. 2. It can be seen that SVM (RBF kernel) classifier is better than other classification methods on all critical measures. For example, SVM classifier gave the $F 1=0.95$ while BNN, DT (C4.5 algorithm), kNN, and BN had the $F 1$ equal to $0.93,0.85,0.79$, and 0.75 , respectively. The highest results are detected from the SVM method with $F 1=0.95$ and $A U C=0.98$. While the lowest results are detected from BN with 0.2 and 0.09 lower values on $F 1$ and $A U C$, respectively.

### 3.3 Informative miRNAs Supporting for Tumor Tissues

In this paper, we used feature selection methods to investigate which might play a more dominant role in tumor tissues. Such methods are then used to improve the performance of a classifier and to help understand the problem. Our intention is to determine which features (miRNAs) contribute more information to the tumor tissue class. As described in Sect. 2.2, we used a two-step feature selection method to find the important miRNAs. In the first step, we calculated the Fisher score of each feature (miRNA) and ranked in descending order by their scores. Then, only miRNAs, which have a Fisher score equal or greater than 0.1, were selected for the next step. Those features were evaluated using the SVM classifier with a linear kernel in the second step. When applying to the miRNA expression dataset (see Sect. 3.1), the top 20 contributing features (informative miRNAs) are shown in Table 2.

Of these informative miRNAs, hsa-miR-205 has the first rank with a weight of 0.34 . Hsa-miR-125b has the second rank with a weight of 0.27 . Three members of let-7 family (hsa-let-7c, hsa-let-7a, and hsa-let-7i) also appear in that list. Other ones, including hsa-miR-146, hsa-miR-145, hsa-
![img-1.jpeg](img-1.jpeg)

Fig. 2 Comparison results of SVMs and conventional methods on the miRNA expression dataset.

Table 2 The top 20 miRNAs contributing to tumor tissues (negative class) obtained from the trained linear SVM model and their corresponding high-confidence target genes (with PicTar_score $\geq 4.5$ ).


miR-181b, and hsa-miR-7-5p are conserved in some mammalian species. Interestingly, we can see that in the top 20 miRNAs contributing to tumor tissues, some of them have been confirmed to be related to several types of human cancer. For example, hsa-miR-205 is located at the region amplified in lung cancer. It had a low expression level in the lung, breast, colorectal, and prostate cancer samples [28]. Besides, Iorio et al. [29] reported that hsa-miR-125b and hsa-miR-145 were indeed involved in human breast cancer. While hsa-miR-125b was down-regulated, hsa-miR145 was up-regulated in human breast cancer. Their analysis suggested that these miRNAs may potentially act as tumor suppressors. Furthermore, expression of hsa-miR145 was found at a low level in lung cancer samples compared to normal samples [28]. Based on the target prediction and expression level of hsa-miR-145 in human cancers, Akao et al. [30] also suggested that this miRNA may suppress genes involved in signal transduction and oncogenesis. The expression level of hsa-miR-181b was investigated in the study of Xi et al. [31]. Their analysis revealed that hsa-miR-181b was strongly associated with the mutation status of the $p 53$ in tumor.

To determine the biological significance of informative miRNAs, we analyzed target genes that are regulated by these miRNAs. Though there are several available miRNA target prediction methods such as PicTar, miRanda, and TargetScan. A recent study indicated that PicTar had the highest success rate in target gene prediction [32]. We thus utilized PicTar algorithm [23] for obtaining predicted target genes of each informative miRNA. High-confidence target genes (PicTar_score $\geq 4.5$ ) of each informative miRNAs are
listed in the last column of Table 2.
To test if the target genes for each informative miRNA might be enriched functionally based on arbitrary Gene Ontology (GO) terms [22], we performed GO annotation and significance analysis using GOstat [33]. We observed terms associated significantly with the target genes included in the GO gene-association database (goa_human and Affymetrix HG_U95AV2 Human known genes). In order to find significantly overrepresented GO terms, GOstat calculates a $p$ value upon assuming hyper-geometric distribution of annotated GO terms. Table 3 shows the shared GO terms of target genes of two first informative miRNAs (hsa-miR-205 and hsa-let-7c). We examine the significant terms with $p$-value $\leq 0.005$ and $p$-value $\leq 0.001$ for hsa-miR-205 and hsa-let7 c , respectively. It can be seen that target genes of hsa-miR205 and hsa-let-7c belong to biologically functional categories, which are related to post-transcription, protein modification, and regulation of metabolic processes.

Table 4 presents the target genes of hsa-miR-205 and hsa-let-7c in detail. It shows the functional description of each target gene. Interestingly, all these genes function as oncogenes in some types of human cancer. For instance, DYRK1A is a member of a conserved family of serine kinases which a activated by intramolecular tyrosine phosphorylation. Amplification of the DYRK1A has been observed in several different types of cancer. YES1 is an oncogene with kinase activity in a number of solid tumors, including breast and colon [34]. The MAP3K3 gene encodes a transduction protein. More interestingly, the oncogene YES1 and the transduction protein MAP3K3 are potential targets of both hsa-miR-145 and hsa-miR-155, which are known as

Table 3 The GO terms associated to target genes of hsa-miR-205 and hsa-let-7c.


Table 4 Description of target genes of hsa-miR-205 and hsa-let-7c.


tumor suppressors in breast cancer [29]. Thus, it is reasonable for us to conclude that the method presented in this research can find informative miRNAs that contribute much information to tumor tissues.

## 4. Conclusions

We have presented a computational method based on SVMs to analyze microRNA expression profiles from a wet lab experiment. Our prediction results indicated that support vector machines are able to classify tissues base on this data and outperforms other classification methods, such as decision trees, Bayesian networks, and backpropagation neural networks.

Furthermore, relied on a two-step feature selection method using Fisher criterion and SVM with linear kernel, we found a subset of informative miRNAs which contribute more information for discriminating between normal and tumor samples. An analysis of predicted target genes of these miRNAs allowed us to determine the functional roles of these miRNAs in the living cells. This analysis revealed that informative miRNA are involved in several types of cancer and their corresponding target genes indeed share common roles in biological processes.

## Acknowledgment

The authors would like to thank Dr. Chih-Jen Lin from National Taiwan University for providing the LIBSVM tool and Prof. Ian Witten from University of Waikato for providing the Weka software. This work was supported by Vietnam's National Foundation for Science and Technology Development (NAFOSTED Project No. 102.03.21.09).
