# NIH Public Access 

## Author Manuscript

Circ Cardiovasc Genet. Author manuscript; available in PMC 2015 April 01.
Published in final edited form as:
Circ Cardiovasc Genet. 2014 April 1; 7(2): 206-217. doi:10.1161/CIRCGENETICS.113.000087.

## Identification of Functional Modules by Integration of Multiple Data Sources Using a Bayesian Network Classifier

Jinlian Wang, PhD ${ }^{1}$, Yiming Zuo, BS ${ }^{1,2}$, Lun Liu, MS ${ }^{3}$, Yangao Man, MD, PhD ${ }^{4}$, Mahlet G. Tadesse, ScD ${ }^{5}$, and Habtom W Ressom, PhD ${ }^{1}$<br>${ }^{1}$ Lombardi Comprehensive Cancer Center, Georgetown University Medical Center, Washington, DC<br>${ }^{2}$ Department of Electrical and Computer Engineering, Virginia Polytechnic Institute and State University, Arlington, VA<br>${ }^{3}$ Beijing Research Center for Information Technology, Beijing Academy of Agriculture and Forestry Sciences, Beijing, P. R. China<br>${ }^{4}$ Diagnostic and Translational Research Center, Henry Jackson Foundation, Gaithersburg, MD<br>${ }^{5}$ Department of Mathematics and Statistics, Georgetown University, Washington DC


#### Abstract

Background-Prediction of functional modules is indispensable for detecting protein deregulation in human complex diseases such as cancer. Bayesian network (BN) is one of the most commonly used models to integrate heterogeneous data from multiple sources such as protein domain, interactome, functional annotation, genome-wide gene expression, and the literature.


Methods and Results-In this paper, we present a BN classifier that is customized to: 1) increase the ability to integrate diverse information from different sources, 2) effectively predict protein-protein interactions, 3) infer aberrant networks with scale-free and small world properties, and 4) group molecules into functional modules or pathways based on the primary function and biological features. Application of this model on discovering protein biomarkers of hepatocelluar carcinoma (HCC) leads to the identification of functional modules that provide insights into the mechanism of the development and progression of HCC. These functional modules include cell cycle deregulation, increased angiogenesis (e.g., vascular endothelial growth factor, blood vessel morphogenesis), oxidative metabolic alterations, and aberrant activation of signaling pathways involved in cellular proliferation, survival, and differentiation.

Conclusion-The discoveries and conclusions derived from our customized BN classifier are consistent with previously published results. The proposed approach for determining BN structure facilitates the integration of heterogeneous data from multiple sources to elucidate the mechanisms of complex diseases.

[^0]
[^0]:    Correspondence: Habtom W. Ressom, PhD, Lombardi Comprehensive Cancer Center, Georgetown University Medical Center, Room 175 Building D, 4000 Reservoir Road, NW, Washington, DC 20057, Tel: 202-687-2283, Fax: 202-687-0227, bwr@georgetown.edu.
    Conflict of Interest Disclosures: None.

## Keywords

systems biology, statistical model, genomics, genetics, bioinformatics, bioinformatics, functional genomics, gene expression, statistical model, computational biology, protein-protein interaction

## Introduction

Complex biological networks underlying cell and organ functions cannot be explained by considering merely individual genes, proteins or pathways. ${ }^{1}$ The increased collection and accumulation of high-throughput omic data from a large number of studies in genomics, transcriptomics, proteomics, metabolomics, and interactomics provide an opportunity to model useful biological networks for biomarker discovery. ${ }^{2}$ The integration of omic data from multiple sources can help understand normal cellular responses and potential dysfunctions in cancers. ${ }^{3}$ This may subsequently lead to a better understanding of the mechanisms of the genesis, development, and metastasis of various cancers. However, modeling biological networks and extracting useful information from a wealth of data sources are challenging. The main difficulties include: 1) selecting a reliable and efficient framework to build a computational model, 2) reducing the intrinsic high noise and bias in the data, 3) integrating heterogeneous and incomplete data, and 4) dealing with the inconsistency of results from various omic studies reported by different groups.

A variety of approaches have been applied to model biological networks by integrating data from multiple sources. These methods include graph theory, ${ }^{4}$ fuzzy logic model, ${ }^{5}$ text mining, ${ }^{6}$ decision tree, ${ }^{7}$ support vector machine (SVM), ${ }^{8}$ relevance vector machine (RVM), ${ }^{9}$ and Bayesian network (BN) classifier. ${ }^{10}$ SVM is a theoretically well motivated algorithm that searches for a decision boundary maximizing the margin of separation between prespecified classes. It enjoys important properties such as convexity and nonlinearity using kernels and has been applied successfully in classification problems. Compared with SVM, the BN classifier offers an attractive alternative for inferring biological networks by integrating multiple data sets. BN is a probabilistic model based on directed acyclic graphs (DAGs) that allow efficient and effective representation of the joint probability distribution over a set of random variables. ${ }^{11}$ It learns from the training data the conditional independent relationships among features $\left(f_{1}, f_{2}, \ldots, f_{n}\right)$ given the class label $y$. Then classification is done by computing the probability of each state of $y$ given a particular instance of $f_{1}, f_{2}, \ldots, f_{n}$ by Bayes rule and selecting the class with the highest posterior probability. The core task is to determine the network structure. ${ }^{12}$ If all the features are conditionally dependent given the class, the BN classifier reduces to a full Bayesian network (FBN) classifier, which substantially increases the computational complexity and potentially leads to an overfitting problem. On the other hand, if all features are conditionally independent given $y$, the BN classifier reduces to a Naïve Bayes (NB) classifier, which may bias the likelihood function estimation because that it fails to account for the conditional dependence among the features given $y$. This paper proposes a method that integrates data from multiple sources to construct a BN classifier that reflects the conditional dependence among features given the class and applies the model to predict aberrant functional modules in hepatocellular carcinoma (HCC). ${ }^{13}$

## Methods

### Framework

The proposed framework is shown in Figure 1. It starts with the collection of biological features from different databases. We selected five features relevant for predicting protein-protein interactions based on domain-domain interactions, biological process, gene expression, homology, and from the literature as shown in Table 1. We then built a BN classifier integrating different features to predict the class (i.e. whether a protein pair is interacting or not). There are two essential steps in constructing a BN classifier: 1) infer the structure of the BN which encodes the conditional independence relationship among the features given the class, and 2) predict the class by calculating and comparing the posterior probability of each class given all the features. Once the BN classifier is learned from the training data, we collected potential HCC protein biomarkers using text mining strategy and constructed an HCC PPI network. Finally, the Girvan and Newman (GN) algorithm^{14} was applied to detect functional modules. Below is a detailed description of each step.

### Data sources

The data sources for the features considered in this study are summarized in Table 1. They are:

- **Domain-Domain interactions (DDIs, f1)**. Proteins consist of one or multiple domains, which are structural or functional units of protein. In many cases, DDIs are crucial clues of protein interactions. Therefore, DDIs can be key supporting evidence for protein interaction mechanisms.^{15,16} Protein domain and protein family assignments were downloaded from the UniDomInt database. It contains 15,625 DDIs of 4,470 distinct protein family (Pfam) domains and combines nine different domain interaction prediction methods to provide a score that captures the reliability of the DDI.^{17} This reliability score was used as the DDI feature, f1.
- **Gene Ontology (GO, f2)**. GO characterizes biological annotation of gene products using terms from hierarchical ontologies.^{18} It aims to provide consistent descriptions of gene products in different databases. Various methods have sought to infer PPIs using their associated GO terms.^{19} There are about 2,000 biological processes and about 2 million protein pairs in the database. We denoted f2 the number of co-occurrence of protein pairs in the same biological process or functional class, which was used as a measure of their interactions.
- **Gene co-expression (CO, f3)**. Gene expression level is a good complement to investigate protein-protein interactions. It has been shown that interacting proteins have similar expression patterns (i.e. are co-expressed).^{20} Therefore, gene co-expression is one of the key supporting evidence for protein-protein interactions. For example, Qi et al.^{21} used 16 gene expression data from GEO to predict protein-protein interactions. We downloaded from Coxpressdb^{14} (http://coxpressdb.jp/) the expression patterns of 19,777 human genes in 123 experiments deposited in ArrayExpress. The Pearson correlation coefficients calculated for each of the

195,554,976 gene pairs by Coxpressdb were used as the gene co-expression feature, $f_{3}$.

- Homology (HOM, $f_{4}$ ). Various protein-protein interactions are conserved across species. ${ }^{22}$ It is well established that many of the protein-protein interactions are confirmed via homology. ${ }^{23}$ Homology information was obtained from Hitdb (Homologous Interactions Database), which provides high confidence homologous interactions that are experimentally determined from IntAct, BioGRID, and HPRD by PSI-Blast ${ }^{18}$ (http://hintdb.hgc.jp/hint/). We considered 92,734 human homologous protein pairs. The Hintdb homology pair scores were used as the homology feature, $f_{4}$.
- Literature (LIT, $f_{5}$ ). Protein-protein interaction database resources capture only a portion of the experimental interactions. Information on other experimentally detected interactions can be extracted from the literature by searching PubMed and other online resources using text mining tools. The higher the co-citation frequency of two proteins, the more likely they are functionally related. Using a Java package developed in-house, 60,888 protein pairs that had been cited together at least once were selected and the co-citation for each pair was used as a measure of the strength of their interaction. As a result, 60,888 protein pairs were selected and the co-citation frequencies were used as $f_{5}$.


# Training data 

To train the BN classifier, we need gold standard positive (GSP) and gold standard negative (GSN) sets. Two proteins can be considered to constitute a positive pair if they are known to interact in the same pathway. The selection of an appropriate GSP set is essential to build an accurate BN classifier and to obtain reliable PPI prediction. We queried the Reactome database, ${ }^{24}$ which consists of structured information on 1,371 biological pathways involving 6,571proteins and 5,763 complexes. We used the resulting 68,285 distinct PPIs to construct a GSP set. The selection of a GSN set is based on identifying protein pairs that are not involved in the same pathway. There are three different ways to generate a GSN set: ${ }^{10}$ (i) two non-interacting genes can be obtained by considering pairs that have no interaction in any biological pathway; (ii) pairs from different cellular localizations are considered unlikely to interact; and (iii) a random set of protein pairs can be selected after filtering the positive pairs. We used the last method to select 98,589 protein pairs from the Reactome database to construct the GSN set.

## Bayesian network classifier

Bayesian network is a type of graphical model that consists of a directed acyclic graph $\mathbf{G}$ and a set of probability distributions $\mathbf{P}$, where nodes represent random variables, edges represent direct dependence between two nodes, and $\mathbf{P}$ is the set of local probability distributions for each node. More precisely, the network encodes the following conditional independence statements: each variable is independent of its non-descendants in the graph given the state of its parents. Given a set of features $f_{1}, f_{2}, \ldots, f_{n}$, BN classifiers can return the state of the outcome $y$ that maximizes the posterior probability $p\left(y \mid f_{1}, f_{2}, \ldots, f_{n}\right)$ based on

the BN structure. They have been widely used in the integration of data from multiple sources and the prediction of biological networks and pathways. ${ }^{10,25}$

Following Bayes rule, the posterior odds $\left(O_{\text {post }}\right)$ for a protein pair is defined as the ratio of the probability that the class is one, $y=1$ (i.e., this pair of proteins is interacting) given all features $f_{1}, f_{2}, \ldots, f_{n}$ to the probability that the class is zero, $y=0$ (i.e., this pair of proteins is not interacting) given all features. It equals to the product of the likelihood ratio $(L R)$ and the prior odds $\left(O_{\text {prior }}\right)$ as shown in Eq. (1).

$$
O_{\text {post }}=\frac{p\left(y=1 \mid f_{1}, f_{2}, \ldots, f_{n}\right)}{p\left(y=0 \mid f_{1}, f_{2}, \ldots, f_{n}\right)}=\frac{p\left(f_{1}, f_{2}, \ldots, f_{n} \mid y=1\right)}{p\left(f_{1}, f_{2}, \ldots, f_{n} \mid y=0\right)} \times \frac{p(y=1)}{p(y=0)}=L R \times O_{\text {prior }}
$$

where $p(y=1)$ and $p(y=0)$ are the prior probabilities specified as the proportion of interacting and non-interacting protein pairs in the gold standard sets, which are calculated empirically. In the special case of some features $\left(f_{\mathrm{M}+1}, \ldots f_{\mathrm{n}}\right)$ being conditionally independent given $y$, the $L R$ for the combined features $\left(f_{1}, f_{2}, \ldots, f_{\mathrm{n}}\right)$ is:

$$
L R\left(f_{1}, f_{2}, \ldots f_{n}\right)=\frac{p\left(f_{1}, f_{2}, \ldots f_{M} \mid y=1\right)}{p\left(f_{1}, f_{2}, \ldots f_{M} \mid y=0\right)} \prod_{i=M+1}^{n} \frac{p\left(f_{i} \mid y=1\right)}{p\left(f_{i} \mid y=0\right)}
$$

According to Eq. (1), we compute $O_{\text {post }}$ for a pair of proteins and classify the two proteins as interacting pair if $O_{\text {post }}>1$, i.e.,

$$
O_{\text {post }}=L R\left(f_{1}, f_{2}, \ldots f_{n}\right) \times O_{\text {prior }}>1
$$

The larger the $O_{\text {post }}$, the more likely that this interaction is true.

# BN structure determination 

The BN structure should capture the predominant dependencies and be as parsimonious as possible. Among the five features we used, Rhodes et al. showed the dependence between DDI and GO and suggested proteins should be assigned to biological process based on their domains. ${ }^{3}$ Browne et al. used correlation to measure the dependence between DDI and GO. ${ }^{26}$ To measure quantitatively the conditional dependence among features $f_{1}, f_{2}, \ldots, f_{n}$ given the state of $y$, we computed the Pearson correlation coefficient between each pair of $f_{1}$, $f_{2}, \ldots, f_{n}$ under different states of $y$. We tested whether the correlation between each pair is significantly different from zero and corrected for multiple testing using the BenjaminiHochberg (BH) false discovery rate (FDR) procedure. We found statistically significant correlation between $f_{1}$ and $f_{2}\left(\operatorname{cor}\left(f_{1}, f_{2} \mid y=1\right)=0.26 ; \operatorname{cor}\left(f_{1}, f_{2} \mid y=0\right)=0.21\right.$; both with adjusted p values $<0.001$ ). This suggests conditional dependence between $f_{1}$ and $f_{2}$ while $f_{3}, f_{4}$ and $f_{5}$ were deemed to be conditional independent features given the state of $y$. In addition, we discretized the feature value into four bins based on their respective quartiles and adjusted the size to make sure that sufficient protein pairs are contained in each bin. Spearman's correlation coefficients were calculated for each pair of $f_{1}, f_{2}, \ldots, f_{n}$ given the state of $y$. All the correlations had BH-FDR adjusted p-values greater than 0.001 , except for the correlation between $f_{1}$ and $f_{2}\left(\operatorname{cor}\left(f_{1}, f_{2} \mid y=1\right)=0.418, \operatorname{cor}\left(f_{1}, f_{2} \mid y=0\right)=0.3978\right.$ both with adjusted p -

values $<0.001$ ). This indicates that the conditional dependence between $f_{1}$ and $f_{2}$ given $y$ is maintained after discretizing the features into bins. In view of this, we proposed the BN structure shown in Figure 2; the arrow from DDI to GO depicts the conditional dependence between $f_{1}$ and $f_{2}$ given $y$ and agrees with the suggestions of previously published paper. ${ }^{3}$ In this case, for the likelihood ratio in Eq. (2), it can be rewritten as follows:

$$
L R\left(f_{1}, f_{2}, f_{3}, f_{4}, f_{5}\right)=\frac{p\left(f_{1} \mid y=1\right) p\left(f_{2} \mid f_{1}, y=1\right) p\left(f_{3} \mid y=1\right) p\left(f_{4} \mid y=1\right) p\left(f_{5} \mid y=1\right)}{p\left(f_{1} \mid y=0\right) p\left(f_{2} \mid f_{1}, y=0\right) p\left(f_{3} \mid y=0\right) p\left(f_{4} \mid y=0\right) p\left(f_{5} \mid y=0\right)}
$$

# Predicting PPIs 

Prediction of protein-protein interactions starts from training the classifier with the GSP and GSN sets. We put all protein pairs which are known to interact or not into associated bins. The range of each bin for each feature is presented in Figure 3. For example, a protein pair in the GSP set with $f_{1}=2, f_{2}=5, f_{3}=0.5, f_{4}=2$ and $f_{5}=8$ is assigned into the following bins: $f_{1}=2, f_{2} \in(4,9), f_{3} \in(0.437,0.962), f_{4}=2$, and $f_{5} \in(7,764)$ with each bin indicating a value or a range for the corresponding feature. Then we calculated in each bin the conditional probability of observing $f_{i}$ given $y$ :

$$
\begin{gathered}
p\left(f_{2} \in x_{2} \mid y=k, f_{1} \in x_{1}\right)=\frac{\#\left\{y=k, f_{1} \in x_{1}, f_{2} \in x_{2}\right\}}{\#\left\{y=k, f_{1} \in x_{1}\right\}} \\
p\left(f_{i} \in x_{i} \mid y=k\right)=\frac{\#\left\{y=k, f_{i} \in x_{i}\right\}}{\#\{y=k\}}
\end{gathered}
$$

where \# represents the number of protein pairs satisfying the specified condition; $x_{i}$ denotes the bin in which $f_{i}$ falls, $i=\{1,3,4,5\}, k=\{1,0\}$.

Consider for example the bin $f_{5} \in(7,764)$. The likelihood ratio is calculated as follows:

$$
\begin{gathered}
L R\left(f_{5} \in x_{5}\right)=\frac{O_{\text {post }}\left(f_{5} \in x_{5}\right)}{O_{\text {prior }}\left(f_{5} \in x_{5}\right)}=\frac{p\left(f_{5} \in x_{5} \mid y=1\right)}{p\left(f_{5} \in x_{5} \mid y=0\right)} \\
p\left(f_{5} \in x_{5} \mid y=1\right)=\frac{\#\left\{f_{5} \in x_{5}, y=1\right\}}{\#\{y=1\}} \\
p\left(f_{5} \in x_{5} \mid y=0\right)=\frac{\#\left\{f_{5} \in x_{5}, y=0\right\}}{\#\{y=0\}}
\end{gathered}
$$

where $x_{5}$ represents the interval $(7,764) ; p\left(f_{5} \in x_{5} \mid y=1\right)$ denotes the ratio of the number of GSP protein pairs falling into this bin over the number of total GSP protein pairs; $p\left(f_{5} \in x_{5} \mid y\right.$ $=0$ ) is the ratio of the number of GSN protein pairs falling into this bin over the number of the total GSN protein pairs.

For $f_{3}, f_{4}$ and $f_{5}$, we can calculate the likelihood ratio according to Eq. (6). However, since $f_{1}$ and $f_{2}$ are correlated given the state of $y$, we need to make a slight modification to Eq. (6) to calculateas outlined below:

$$
\begin{aligned}
& L R\left(f_{1} \in x_{1}, f_{2} \in x_{2}\right) \\
& =\frac{O_{\text {post }}\left(f_{1} \in x_{1}, f_{2} \in x_{2}\right)}{O_{\text {prior }}\left(f_{1} \in x_{1}, f_{2} \in x_{2}\right)} \\
& =\frac{p\left(f_{1} \in x_{1}, f_{2} \in x_{2} \mid y=1\right)}{p\left(f_{1} \in x_{1}, f_{2} \in x_{2} \mid y=0\right)} \\
& =\frac{p\left(f_{1} \in x_{1} \mid y=1\right) \times p\left(f_{2} \in x_{2} \mid f_{1} \in x_{1}, y=1\right)}{p\left(f_{1} \in x_{1} \mid y=0\right) \times p\left(f_{2} \in x_{2} \mid f_{1} \in x_{1}, y=0\right)} \\
& p\left(f_{1} \in x_{1} \mid y=1\right)=\frac{\#\left\{f_{1} \in x_{1}, y=1\right\}}{\#\{y=1\}} \\
& p\left(f_{1} \in x_{1} \mid y=0\right)=\frac{\#\left\{f_{1} \in x_{1}, y=0\right\}}{\#\{y=0\}} \\
& p\left(f_{2} \in x_{2} \mid f_{1} \in x_{1}, y=1\right)=\frac{\#\left\{f_{1} \in x_{1}, f_{2} \in x_{2}, y=1\right\}}{\#\left\{f_{1} \in x_{1}, y=1\right\}} \\
& p\left(f_{2} \in x_{2} \mid f_{1} \in x_{1}, y=0\right)=\frac{\#\left\{f_{1} \in x_{1}, f_{2} \in x_{2}, y=0\right\}}{\#\left\{f_{1} \in x_{1}, y=0\right\}}
\end{aligned}
$$

where $p\left(f_{2} \in x_{2} \mid f_{1} \in x_{1}, y=1\right)$ represents the ratio of the number of GSP protein pairs falling into both $x_{1}$ bin and $x_{2}$ bin to that of GSP protein pairs falling into $x_{1}$ bin; $p\left(f_{2} \in x_{2} \mid f_{1} \in x_{1}, y\right.$ $=0$ ) denotes the ratio of the number of GSN protein pairs falling into both $x_{1}$ bin and $x_{2}$ bin to that of GSN protein pairs falling into $x_{1}$ bin.

The trained BN model was applied to predict interacting protein pairs by computing individual likelihood for each feature, and the $L R$ for the five combined features is as follows:

$$
L R\left(f_{1}, f_{2}, f_{3}, f_{4}, f_{5}\right)=L R\left(f_{1}, f_{2}\right) \times L R\left(f_{3}\right) \times L R\left(f_{4}\right) \times L R\left(f_{5}\right)
$$

We then computed $O_{\text {post }}$ according to Eq. (1). If $O_{\text {post }}>1$, we considered the protein pair to be interacting.

# Results 

## Calculating predictive strength of each feature

To evaluate the predictive strength of each individual feature in identifying protein pairs, we computed $O_{\text {post }}$ of $y=1$ using the five features $\left(f_{1}, f_{2}, \ldots, f_{5}\right)$ listed in Table 1. This was done for each protein pair in the GSP and GSN sets. Figure 4 shows $O_{\text {post }}$ for the four levels of

each feature. Except for homology, nearly all four other features have a weak positive association between the posterior odds and the feature values. For gene co-expression and co-citation, we observe their posterior odds monotonically increasing as the corresponding feature values increase, indicating the potential power of these two features in predicting reliable PPIs.

# Performance evaluation 

We trained BN, NB, FBN and SVM classifiers using the above five features and the GSP and GSN sets described in Section II. For BN classifier, all features $\left(f_{1}, f_{2}, \ldots, f_{5}\right)$ are assumed conditionally independent given the class label $(y)$. Eq. (4) can be rewritten as follows:

$$
L R\left(f_{1}, f_{2}, f_{3}, f_{4}, f_{5}\right)=\frac{p\left(f_{1} \mid y=1\right) p\left(f_{2} \mid y=1\right) p\left(f_{3} \mid y=1\right) p\left(f_{4} \mid y=1\right) p\left(f_{5} \mid y=1\right)}{p\left(f_{1} \mid y=0\right) p\left(f_{2} \mid y=0\right) p\left(f_{3} \mid y=0\right) p\left(f_{4} \mid y=0\right) p\left(f_{5} \mid y=0\right)}
$$

All the other configurations are the same as our proposed BN classifier. In contrast, FBN classifier assumes all features are conditionally dependent given class label. As a result, the likelihood ratio can be rewritten as:

$$
L R\left(f_{1}, f_{2}, f_{3}, f_{4}, f_{5}\right)=\frac{p\left(f_{1} \mid y=1\right) p\left(f_{2} \mid f_{1}, y=1\right) p\left(f_{3} \mid f_{1}, f_{2}, y=1\right) p\left(f_{4} \mid f_{1}, f_{2}, f_{3}, y=1\right) p\left(f_{5} \mid f_{1}, f_{2}, f_{3}, f_{4}, y=1\right)}{p\left(f_{1} \mid y=0\right) p\left(f_{2} \mid f_{1}, y=0\right) p\left(f_{3} \mid f_{1}, f_{2}, y=0\right) p\left(f_{4} \mid f_{1}, f_{2}, f_{3}, y=0\right) p\left(f_{5} \mid f_{1}, f_{2}, f_{3}, f_{4}, y=0\right)}
$$

We applied the strategy introduced by Su and Zhang to build the FBN classifier. ${ }^{41}$ For the SVM classifier, we used Weka, an open source machine learning software (http:// www.cs.waikato.ac.nz/ml/weka/), with a Gaussian kernel while other configurations were set as default. We then compared the predictive performance of the proposed BN classifier to that of NB, FBN and SVM classifiers based on a 10 -fold cross-validation. Briefly speaking, we split the positive and negative training sets into ten approximately equal sets. Nine of these were used for training and the remaining one was used for testing. True positives (TP) and false positives (FP) were calculated. This process was repeated 10 times (choosing a different test set each time). We then calculated the area under the receiver operating characteristic (AUC) for each model with the proposed BN classifier showing the largest AUC as displayed in Figure 5.

In addition to cross-validation, we also used an independent test set to evaluate the predictive performance of our proposed BN classifier. The independent set was derived from the MINT database, a public PPI database built from results published in peer-reviewed journals. We downloaded 187,456 binary interactions for 8,707 human proteins from (http:// mint.bio.uniroma2.it/mint/ ${ }^{27}$ to evaluate the BN, NB, FBN and SVM classifiers previously built using the training set. After removing the known 187,456 binary interactions from the 8,707 proteins, a random set of 187,456 protein pairs was selected. Figure 6 depicts the receiver operating characteristic (ROC) curves for each classifier. As shown in Figures 5 and 6 , the proposed BN classifier provides the best performance. For naïve Bayes classifier, our proposed BN classifier outperforms it since ours can capture the conditional dependence structure among features given the class. For SVM, our proposed classifier can handle

missing values without imputation, whereas SVM requires missing values be estimated before using it as an input. For FBN classifier, our proposed classifier significantly reduces the computational complexity and avoids the risk of overfitting caused by the assumption of FBN classifier that all features are conditionally dependent given the class.

# HCC PPI network 

We applied the trained BN classifier to construct an HCC PPI network using 256 candidate protein biomarkers for HCC that have been reported as differentially expressed between HCC cases and healthy controls or patients with liver cirrhosis (adjusted $p$-value $<0.0001$ ) using high-throughput technologies including microarray and mass spectrometry.

Before we applied the BN classifier to construct the HCC PPI network, we used a Javabased tool developed in-house to collect the interaction information of the 256 biomarkers from protein-protein interaction databases such as BioGrid, HPRD, STRING and KEGG. We obtained 11,513 distinct protein pairs and their corresponding five feature values. Using the trained BN classifier 1,291 protein-protein interactions were predicted as true positives $\left(O_{\text {post }}>1\right)$. They were used to construct the HCC PPI network shown in Figure 7A. The nodes represent proteins and the edges correspond to the interactions between two proteins.

To identify previously unknown interactions, we mapped to IntAct (http://www.ebi.ac.uk/ intact/) 18 predicted interacting pairs between 23 unique proteins with high confidence $\left(O_{\text {post }}>200\right)$. In addition to known pathways involved in HCC or liver disease, such as Wnt and Hepatitis C pathways, we found some novel predicted interactions that are not included in the IntAct database (see edges marked in red in Figure 7B). For example, the SOS1 interactors are involved in T-cell receptor signaling pathway and regulate protein complex assembly (GO0043254). PLAK1 and its interactors are related to mitotic spindle checkpoint and cell cycle (GO00278) pathways which are important for HCC progression. Also, we observed interactions between TP53, AR1H2 and PPP2R1A correlated with cell growth (GO0016049). The largest posterior odds $\left(O_{\text {post }}=7329.19\right)$ was for CDC20 and PLK1 (red nodes in Figure 7B).

To understand better the inferred HCC PPI network, we analyzed its topological properties such as degree of distribution and the length of the shortest paths. The degree of distribution is the number of connections per node. In the HCC PPI network, the degree of distribution exhibits approximately a power law property (Figure 8A). The length of the shortest paths between pairs of nodes in the HCC network is around 4 (Figure 8B). Both of these indicate that the HCC PPI network satisfies the property of scale-free and small world networks. The topological analysis reveals that the predicted HCC network is in concordance with previously reported cancer biological network characteristics. ${ }^{28}$

## Functional modules

We performed a network module analysis using the $\mathrm{GN}^{14}$ algorithm on the HCC PPI network shown in Figure 7A. To explore the biological function that these modules may imply, we annotated these modules with GO terms using BiNGO. ${ }^{29}$ The significance of these modules was evaluated using the hypergeometric test and Bonferroni family-wise error

rate correction (adjusted p-value<0.005) provided by BiNGO. The GO biological process and cellular component enrichment analysis found 24 functional modules; seven of the top rankings are listed in Tables 2 and 3 along with their enrichment p-values and the number of nodes and edges for each module. Modules 1 and 2 are mainly related to the chemical reactions and pathways resulting in the breakdown of a protein or peptide by hydrolysis, and mediated by APC (anaphase-promoting complex)-dependent proteasomal ubiquitin-dependent protein degradation, and cell cycle (adjusted p-value=1.26E-24). The gene products present in Module 3 are in the mitochondrial inner membrane (adjusted p-value=3.18E-23). Pathways in this module are significantly related to energy metabolism pathways (adjusted p-value=2.3E-06). We queried the OMIM database and found that genes in this module are associated with: 1) abnormality of carbohydrate metabolism/homeostasis (OMIM: 107741, 117550), 2) reduced ability of liver functions and 3) hepatic failure and abnormality of body fluids regulation. Pathways assigned to Modules 4 and 5 are mainly related to angiogenesis and Wnt signaling. HCC is a hypervascular tumor; angiogenic factors such as VEGF can stimulate proliferation and migration of endothelial cells leading to elevated vascular density. Aberrant activation of Wnt signaling plays an important role in hepatocarcinogenesis. ${ }^{30}$ Cumulating evidence suggests that Wnt signaling is required for angiogenesis. ${ }^{3132,33}$ Module 6 shows that proteins are mainly involved in cholesterol metabolism and sterol homeostasis. Enriched pathways of chylomicron-mediated lipid transport (adjusted p-value=5.29 E -30) and fat digestion and absorption (adjusted pvalue $=4.89 E-05)$ in this module could be correlated with the mechanism of cellular control of lipid and lipoprotein metabolism. Thus, associated proteins suggest the role of lipid metabolism in the pathogenesis of HCC. Bile acids are the end products of cholesterol catabolism, they are produced in the liver ${ }^{34}$ to facilitate hepatobiliary secretion of endogenous metabolites and xenobiotics and intestine absorption of lipophilic nutrients, and to control the metabolism of glucose and lipids in the enterohepatic system. ${ }^{35}$ Proteins in Module 7 are significantly related to glucagon stimulus, energy derivation by oxidation of organic compounds and bile acid transport, suggesting bile acid signaling regulation of glucose and lipid metabolism. Also, Module 7 indicates that bile acid signaling pathway could be the master of metabolic disorders in liver disease and HCC. Table 3 lists the subcellular locations of the functional modules. For example, the top ranked proteins in Module 1 are primarily located at the cytoplasmic and intracellular parts, suggesting changes in proteins expressed in cytoplasmic tumor progression. ${ }^{36}$ In Model 7, all proteins appear to be associated with protein synthesis-related organelles or complexes. Aberrant protein synthesis has been consistently linked to liver cancer development and progression. ${ }^{37,38}$ In summary, functional module analysis yields biologically relevant contexts for identifying the 'driver' and 'passenger' proteins in cancer development, generating hypothesis for subsequent experimental validation, indicating systematic integration of multiple level -omic data provides insights into the mechanism of cancer.

# Discussion 

Integration of protein-protein interaction information from multiple data sets contributes to a better understanding of aberrant pathways and network activities within the cell. However, it is difficult to manually and comprehensively integrate all available information for the

following reasons: 1) too many data sources, 2) too many levels of interactions, 3) too many different fields, 4) too many contradictory reports, and 5) too rapidly increasing scientific terms, definitions, experimental methods and methodologies. In this paper, we propose a customized BN classifier to infer protein-protein interactions by integrating heterogeneous data from multiple sources. The proposed BN classifer can capture the relationships between diverse biological features. A simulation result shows that our BN classifier outperforms other classifiers including NB, FBN and SVM. We applied the BN classifier to construct HCC networks by integrating information from biological databases and literature. We then discovered functional modules, 'hub' proteins, and relevant interactions between candidate protein biomarkers for HCC. Enrichment analysis was applied to infer the mechanism of HCC based on these functional modules.

Our future work will focus on 1) seeking better approaches to determine the structure of the BN classifier, and 2) extending the proposed BN classifier to predict metabolic pathways and networks by incorporating data from metabolite profiling studies into current framework.

Funding Sources: This work was supported by NIH grants R01CA143420 and R01GM086746 awarded to HWR.

# DDI reliability score

![img-4.jpeg](img-4.jpeg)

# Protein pairs sharing biological process

![img-5.jpeg](img-5.jpeg)

# NH-PA Author Manuscript

## NIH-PA Author Manuscript

### Note

-1~0.137

0.137~0.278

0.278~0.437

0.437~0.962

### General

- **Posterior Odds**
- **Nitri-PA Author Manuscript**
- **Nitri-PA Author Manuscript**

Gene pairwise correlation

![img-6.jpeg](img-6.jpeg)

# Homologous protein pairs

![img-7.jpeg](img-7.jpeg)

Figure 4.
Multiple data sources contribute to the BN classifier. Bar plots of posterior odds for domaindomain interactions (A), Gene Ontology (B), gene co-expression (C), homology (D), and literature (E).

![img-8.jpeg](img-8.jpeg)

Figure 5.
Comparisons of prediction performance of the BN, NB, FBN and SVM classifiers by 10fold cross-validation on the training set. The Y-axis represents the area under ROC curve score. AUC for $\mathrm{BN}=0.9001, \mathrm{NB}=0.8723, \mathrm{FBN}=0.8010, \mathrm{SVM}=0.67$

![img-9.jpeg](img-9.jpeg)

Figure 6.
ROC curves of the proposed BN, NB, FB and SVM classifiers based on independent testing set. AUC for the $\mathrm{BN}=0.9072, \mathrm{NB}=0.82025, \mathrm{FBN}=0.77001$, and $\mathrm{SVM}=0.687$

![img-10.jpeg](img-10.jpeg)

Cirr Cardiovasc Genet. Author manuscript; available in PMC 2015 April 01.

![img-11.jpeg](img-11.jpeg)

Figure 7.
Global and focused views of the predicted HCC PPI network. A: Global view of the HCC PPI network. B: Zoomed view of the predicted interactions generated by the 18 true positive interactions among 23 unique proteins ( $O_{\text {post }}>200$ ). Known interactions in IntAct are shown in green edge and predicted ones are shown in red. Known interactors in IntAct are shown in light purple and predicted ones are shown in yellow. The network is drawn by Cytoscape.

![img-12.jpeg](img-12.jpeg)

*Circ Cardiovasc Genet.* Author manuscript; available in PMC 2015 April 01.

![img-13.jpeg](img-13.jpeg)

**Figure 8.** The topology properties of the identified HCC PPI network. (A), node degree distribution (B), path length

# Table 1 

The data sources integrated for the prediction of human protein-protein interactions


# Table 2 

Top seven highly significant modules with corresponding top five GO biological processes


Table 3
Top seven highly significant modules with corresponding top five GO cellular compartments
