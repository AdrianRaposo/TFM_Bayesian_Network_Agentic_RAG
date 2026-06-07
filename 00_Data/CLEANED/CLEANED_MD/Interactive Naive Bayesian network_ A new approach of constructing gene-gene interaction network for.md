# Interactive Naive Bayesian network: A new approach of constructing gene-gene interaction network for cancer classification 

Xue W. Tian ${ }^{\mathrm{a}}$ and Joon S. Lim ${ }^{\text {b,* }}$<br>${ }^{a}$ Department of Educational Technology, Teachers College, Qingdao University, QingDao, China<br>${ }^{b}$ IT College, Gachon University, Seongnam, South Korea


#### Abstract

Naive Bayesian (NB) network classifier is a simple and well-known type of classifier, which can be easily induced from a DNA microarray data set. However, a strong conditional independence assumption of NB network sometimes can lead to weak classification performance. In this paper, we propose a new approach of interactive naive Bayesian (INB) network to weaken the conditional independence of NB network and classify cancers using DNA microarray data set. We selected the differently expressed genes (DEGs) to reduce the dimension of the microarray data set. Then, an interactive parent which has the biggest influence among all DEGs is searched for each DEG. And then we calculate a weight to represent the interactive relationship between a DEG and its parent. Finally, the gene-gene interaction network is constructed. We experimentally test the INB network in terms of classification accuracy using leukemia and colon DNA microarray data sets, then we compare it with the NB network. The INB network can get higher classification accuracies than NB network. And INB network can show the gene-gene interactions visually.


Keywords: Gene interaction, naive Bayesian, differently expressed genes (DEGs), leukemia, colon, DNA microarray

## 1. Introduction

Genetic interactions have long been studied in model organisms as a means of identifying functional relationships among genes or their corresponding gene products, with the nature of the relationships depending on the types of interactions [1-6]. The availability of complete genome sequences facilitates the development of high-throughput assays that can probe cells at a genome-wide scale [7-9]. Such assays measure molecular networks and their components at multiple levels. These include mRNA transcript quantities; protein-protein and protein-DNA interactions; chromatin structure; and protein quantities, localization, and modifications [10-12]. These rich data illuminate the working of cellular processes from different perspectives and offer much promise for novel insights into these processes [13-16]. However, there is still a tendency to look for the smallest and most accurate set of genes that are able to distinguish between two or more phenotypes [17-20]. We propose an interactive naive Bayesian (INB) network to classify gene phenotypes with the smallest gene set and map the relation-

[^0]
[^0]:    *Address for correspondence: Joon S. Lim, IT College, Gachon University, Seongnam, South Korea. Tel.: 82-031-7505750; Fax: 82-031-750-5662; E-mail: jslim@gachon.ac.kr.

ships of the genes with the set. We experimentally test the INB network in terms of its classification accuracy.

There are many approaches to classification, including decision trees, neural networks, support vector machines, and the Bayesian network. The Bayesian approach is the most commonly used when dealing with uncertainty because it is based on the probability theory [21, 22]. A Bayesian network is a graphical model that encodes probabilistic relationships of variables. Its main distinguishing feature from classical statistical inference approaches is the use of subjective or personal beliefs (prior probabilities) in the analysis [23, 24]. These probabilistic approaches make strong assumptions about how the data is generated and posit a probabilistic model that embodies these assumptions. Naive Bayesian (NB) network classifiers are very robust in terms of irrelevant attributes, and the classification takes into account evidence from many attributes to make the final prediction [24, 25]. NB classifiers have been adapted to handle continuous attributes primarily using Gaussian distributions or discretizing the domain, both of which present certain disadvantages. In the former approach, the probability density of the attributes is not always well fitted by a Gaussian distribution. In the latter approach, there can be loss of information.

We determine a weight for the INB classifier by assigning a weight between each node and its interactive parent on the NB network. This decreases the independence and increases the classification performance. The weights are constructed by a neuro-fuzzy network called a neural network with weighted membership functions (NEWFM) [26, 27]. With NEWFM we can determine the relationships between each attribute. We use the relationships to calculate the weight for each node of the Gaussian NB network. The INB network can also provide a gene interaction network using the weight between the node and its interactive parents.

We apply the INB network to classify leukemia and colon DNA microarray data sets [28, 29]. With the successful completion of the Human Genome Project (HGP), we are entering the post-genomic era. Facing massive amounts of data, traditional biological experiments and data analysis techniques encounter significant challenges. In this situation, cDNA microarrays and high-density oligonucleotide chips, which are novel biotechnologies, are global (genome-wide or system-wide) experimental approaches that are used effectively in the systematic analysis of large-scale genome data [30]. In this paper, we apply INB classifiers for the analysis of DNA microarray data. The experimental results demonstrate that INB classifiers are more reliable than NB classifiers.

# 2. Materials and method 

### 2.1. Preprocessing of the data set

### 2.1.1. Materials

In [28], the authors present methods for analyzing gene expression data obtained from DNA microarrays in order to classify types of cancer. Their leukemia data is available on-line. The data is split into two subsets: A training set and a test set. Their training set consists of 38 samples ( 27 ALL and 11 AML) from bone marrow specimens. Their test set has 34 samples ( 20 ALL and 14 AML), prepared under different experimental conditions and including 24 bone marrow and 10 blood sample specimens. All samples have 7129 features, corresponding to some normalized gene expression value extracted from the micro-array image. We retained the exact same experimental conditions for ease of comparison with their method.

Table 1
The selected sets of DEGs


In [29], the authors describe and study a data set that is available on-line. Gene expression information was extracted from DNA microarray data resulting, after pre-processing, in a table of 62 tissues $\times 2000$ gene expression values. The 62 tissues include 22 normal and 40 colon cancer tissues. The matrix contains the expression of the 2000 genes with highest minimal intensity across the 62 tissues. Some genes are non-human genes. Since there was no defined training and test set, we used all 62 samples for both training and test.

# 2.1.2. General remarks on figures 

We use the Bhattacharyya distance (BD) [31] and a neuro-fuzzy network [27] as our differently expressed gene (DEG) selection method for microarray data analysis. The detail of this method is represented on the previous paper [32, 33]. Finally, we select six DEGs from the leukemia data set and seven DEGs from the colon data set [32, 33]. The selected sets of DEGs are shown in Table 1.

### 2.1.3. Data normalization

After DEGs selection, we normalize the values of DEGs on the scale of $[0,1]$ and transform them with a concentrated distribution [34]. The set of normalized expression values for the $i$ th DEG with $s$ samples, $\mathrm{N}_{i}$, is given by

$$
\mathrm{N}_{i}=\left\{n_{i, j} \mid n_{i, j}=\frac{1}{1+e^{-\left(d_{i, j}-\min \left(\mathrm{D}_{i}\right)\right) /\left(\max \left(\mathrm{D}_{i}\right)-\min \left(\mathrm{D}_{i}\right)\right)}}, \forall j=1,2, \ldots, s\right\}
$$

Table 2
The representations of DEGs and their corresponding original and normalized expression values


![img-0.jpeg](img-0.jpeg)

Fig. 1. Finding interactive parent $D_{p i}$ of $D_{i}$ with the highest classification accuracy $a_{C}\left(D_{i}\right)$.
where $\mathrm{D}_{i}$ is the set of expression values of the $i$ th DEG $D_{i}$ in microarray samples, $\min \left(\mathrm{D}_{i}\right)$ and $\max \left(\mathrm{D}_{i}\right)$ are the minimum and maximum values in $\mathrm{D}_{i}$, and $d_{i, j}$ and $n_{i, j}$ are the $j$ th expression value and normalized value in $\mathrm{D}_{i}$ and $\mathrm{N}_{i}$, respectively. Table 2 shows the representations of DEGs and their corresponding original and normalized expression values. $C$ is the set of class variables, $c_{j}^{*}$ is the class variable of the $j$ th samples set $\left\{d_{1, j}, \ldots, d_{i, j}, \ldots, d_{n, j}\right\}$ and $\left\{n_{1, j}, \ldots, n_{i, j}, \ldots, n_{n, j}\right\}$, it can be represented by class 1 or class 2 .

# 2.2. Interactive Naive Bayesian network 

In order to effectively relax the conditional independence assumptions of the NB network, we suppose every attribute (or gene) has an interactive relationship with other attributes (or genes). This proposed model, called interactive naive Bayesian network (INB), contains attributes each of which has an interactive attribute as a parent and one classification node connected to all attributes as another parent. We use a non-overlap area distribution measurement method (NADM) [27] to measure the interactive relationship between attributes.

After data normalization, one target gene $D_{i}$ in DEGs is classified in turn by the other genes using a neural network with a weighted fuzzy membership function (NEWFM) [27]. A class is given to all gene samples in $\mathrm{N}_{i}$ for classifying a target gene $D_{i}$, denoted by class $\left(n_{i, j}\right)$, is defined such that:

$$
\operatorname{class}\left(n_{i, j}\right)=\left\{\begin{array}{l}
1, n_{i, j}<\operatorname{mean}\left(\mathrm{~N}_{i}\right) \\
2, n_{i, j} \geq \operatorname{mean}\left(\mathrm{~N}_{i}\right)
\end{array}\right.
$$

Then, the every target gene $D_{i}$ in DEGs is classified in turn by the NEWFM obtaining classification accuracy of $D_{i}, a_{C}\left(D_{i}\right)$, with interactive parent gene $D_{p}$ of $D_{i}$, denoted by $D_{p i}=I P\left(D_{i}\right)$, where $i \nRightarrow p$ as in Figure 1. The input nodes of the NEWFM are the normalized values of DEGs except $D_{i}$ for classifying $D_{i}$. To find the $D_{p i}$, the training and test processes are iterated $t$ times. During the iterations, $D_{p}$ is found by the NADM method in the NEWFM as an interactive parent gene $D_{p i}$ of $D_{i}$.

In each iteration, the best gene for the classification of $D_{i}$ is chosen by the NADM. Every input gene node keeps a variable storing the number of choices. The variable is added by one whenever the gene is chosen. After $t$ time iterations, the gene $D_{p}$ that has the highest number of variable will be assigned as $I P\left(D_{i}\right)$. The variable is called $h\left(D_{p i}\right)$ to be used for calculating the weight between the gene $D_{i}$ and its interactive parent $D_{p i}$.

![img-1.jpeg](img-1.jpeg)

Fig. 2. Structure of the INB network.
After finding $D_{p i}$ with $h\left(D_{p i}\right)$, the interaction weight calculations between $D_{i}$ and its interactive parent $D_{p i}$ are continued for enhancing classification power of INB. The weight between $D_{i}$ and $D_{p i}$, denoted by $w_{i \in p}$ is shown in Eq. (3), where $t$ is the number of classification iterations for $D_{i}, a_{C}\left(D_{i}\right)$ is the classification accuracy of $D_{i}$, and $n$ is the number of DEGs.

$$
w_{i \leftarrow p}=\frac{h\left(D_{p i}\right)}{t} * a_{C}(D i) \text { for } \mathrm{C}=1,2, i=1,2, \ldots, n \text {, where } i \neq p
$$

The $w_{i \in p}$ represents the degree of interactive relationship from $D_{p i}$ to $D_{i}$ using gene expression data, which is the goal of the genomic revolution for understanding the genetic interacts in a complex living system.

The proposed INB network is constructed by adding the interactive parents with their weights to naive Bayesian network. The higher weight causes the stronger interactive influence from the interactive parent to the target gene. Figure 2 shows the structure of an INB network, where $C$ is the diagnostic class node that is the parent of all other nodes (DEGs) $D_{i}$, where $i=1,2, \ldots, n$. Each node $D_{i}$ has one more interactive parent $D_{p i}$ represented by arc with the weight on the arc, and also can be an interactive parent of other DEGs or not.

# 2.3. Classification of interactive Naive Bayesian network 

The naive Bayes classifier uses the Bayes theorem in conjunction with the conditional independence hypothesis. The naïve Bayes paradigm is thus based on two conditions over the features of predictive variables and the class variable to predict. Based on the NB network, the joint distribution represented by an INB network is defined as:

$$
P\left(D_{1}, \ldots, D_{n}, C\right)=P(C) \prod_{i=1}^{n} P\left(D_{i} \mid D_{p}, C\right)
$$

where $C$ is the class node.
The classification corresponding to an INB network on samples set $\mathrm{S}_{j}\left\{n_{1, j}, \ldots, n_{n, j}\right\}, c_{j}^{*}$, is defined as

$$
c_{j}^{*}=\arg \max _{c_{j}^{*} \in C} P(C) \prod_{i=1}^{n} P\left(n_{i, j} \mid n_{p, j}, C\right)
$$

Where

$$
P\left(n_{i, j} \mid n_{p, j}, C\right)=P\left(n_{i, j} \mid C\right)+\left(P\left(n_{p, j} \mid C\right)-P\left(n_{i, j} \mid C\right)\right) * w_{i \in p}
$$

The expression values are continuous, in Eq. (6), $P\left(n_{i, j} \mid C\right)$ and $P\left(n_{p, j} \mid C\right)$ are got by Gaussian distribution. In an INB network, attribute dependencies are represented by interactive parents of attributes. The method of defining interactive parents determines the capability of representing attribute dependencies.

# 3. Experiment results 

We experimentally test the INB classifier in terms of classification accuracy, using leukemia and colon DNA microarray data sets, and compare it to the NB classifier. The comparison results shown in Table 3 demonstrate that the INB classifier is more reliable than the NB classifier. In Table 3, Sensitivity (Se) is the ability (probability) to classify. Specificity (Sp) is the probability of identifying class 2 correctly. Positive probability $(\mathrm{Pp})$ is the probability that classified class 1 is truly class 1 . Negative probability $(\mathrm{Np})$ is the probability that classified class 2 is truly class 2 . Accuracy (Acc) is the probability of obtaining a correct classification. The performance results for leukemia show that $95 \%$ accuracy can be achieved with the INB classifier. The NB classifier can only attain $94 \%$. For the colon data set classification, the accuracy of the INB classifier is $3 \%$ higher than the NB classifier.

After the experiment, we construct a gene interaction network to represent the relationship between DEGs shown in Figure 3. Figure 3a is the gene interaction network of leukemia and Figure 3b shows the gene interaction network of a colon. For leukemia, Figure 3a reflects the interaction relationship by the arcs. The number on each arc is the weight between the two connected genes. As arc D88270_at $\rightarrow$ L33930_s_at, weight 407 shows the degree of effect between gene D88270_at and L33930_s_at. The higher the degree, the stronger the effect and the darker the arc is.

Table 3
Experimental Results Comparison


![img-2.jpeg](img-2.jpeg)

Fig. 3. Gene INB network of leukemia and colon.

# 4. Conclusions 

In this research, a new approach to identify gene interactions has been proposed based on the INB. We selected the six DEGs from the leukemia data set and the seven DEGs from the colon data set to construct and test the INB network. The advantage of the INB network is that it is not only a naive Bayesian network, but also give the gene-gen interactive from the selected DEGs. We combined the NB network and gene interactive network to obtain a novel Bayesian model, INB, for gene classification, and represented the gene interaction network. We experimentally tested the INB classifier in terms of classification accuracy using leukemia and colon DNA microarray data sets, and compared it to the NB classifier. The experimental results show that the INB classifier outperforms the NB classifier. We constructed a gene interaction network to represent the relationship between genes. It represents more informative way than a single variable list of genes. This network approach could be useful also to other research field, such as finding interactions of features for classification approach.

## Acknowledgment

This research was supported by Basic Science Research Program through the National Research Foundation of Korea (NRF) funded by the Ministry of Education, Science and Technology. (2012R$\cdot$1A1A2044134).
