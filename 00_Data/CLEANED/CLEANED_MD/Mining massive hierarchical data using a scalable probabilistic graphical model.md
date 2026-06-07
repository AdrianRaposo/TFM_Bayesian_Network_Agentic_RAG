# Mining Massive Hierarchical Data Using a Scalable Probabilistic Graphical Model 

Khalifeh AlJadda ${ }^{1 *}$, Mohammed Korayem ${ }^{2}$, Camilo Ortiz ${ }^{3}$, Trey Grainger ${ }^{3}$, John A. Miller ${ }^{1}$, Khaled Rasheed ${ }^{1}$, Krys J. Kochut ${ }^{1}$, William S. York ${ }^{4}$, Rene Ranzinger ${ }^{4}$ and Melody Porterfield ${ }^{4}$<br>*Correspondence:<br>aljadda@uga.edu<br>${ }^{1}$ Department of Computer Science, University of Georgia, Athens,GA, USA Full list of author information is available at the end of the article ${ }^{1}$ Equal contributor


#### Abstract

Probabilistic Graphical Models (PGM) are very useful in the fields of machine learning and data mining. The crucial limitation of those models, however, is the scalability. The Bayesian Network, which is one of the most common PGMs used in machine learning and data mining, demonstrates this limitation when the training data consists of random variables, each of them has a large set of possible values. In the big data era, one would expect new extensions to the existing PGMs to handle the massive amount of data produced these days by computers, sensors and other electronic devices. With hierarchical data - data that is arranged in a treelike structure with several levels - one would expect to see hundreds of thousands or millions of values distributed over even just a small number of levels. When modeling this kind of hierarchical data across large data sets, Bayesian Networks become infeasible for representing the probability distributions. In this paper we introduce an extension to Bayesian Networks to handle massive sets of hierarchical data in a reasonable amount of time and space. The proposed model achieves perfect precision of 1.0 and high recall of 0.93 when it is used as multi-label classifier for the annotation of mass spectrometry data. On another data set of 1.5 billion search logs provided by CareerBuilder.com the model was able to predict latent semantic relationships between search keywords with accuracy up to 0.80 .


## Introduction

Probabilistic graphical models (PGM) consist of a structural model and a set of conditional probabilities [1, 2]. They are widely used in machine learning and data mining techniques, like classification, speech recognition [3], bioinformatics [4, 5], Natural Language Processing (NLP) [6, 7], etc. Scalability and restricted domain size (e.g., propositional domain) are the major challenges for PGMs. To overcome these challenges one would expect extensions to the existing PGMs. One extension is offered by the hierarchical probabilistic graphical models (HPGM) which aim to extend the PGM to work with more structured domains [8, 9]. However, this extension tackles the restricted domain size problem, but not scalability. For hierarchical data, where data can be divided into several levels arranged in tree-like structures, data items in each level depend on or are influenced only by the data items in the upper levels while a Bayesian Network (BN) is the most appropriate PGM to represent a probability distribution since the dependencies in this kind of data are not bidirectional, a BN is often infeasible, as it may not provide a concise enough representation of a large probability distribution. When dealing with the kind of massive hierarchical data that is becoming increasingly common in the big data

era, this is true because each level represents a random variable, while each node in that level represents an outcome (possible value) of that random variable, so the data can grow horizontally (number of values) faster than vertically (number of random variables). Moreover, since the dependency between the random variables is pre-defined in the hierarchical data, the structure of the network is predefined. Hence, the first phase of building Bayesian Network to find the optimal structure is not applicable

For example, consider the glycan ontology "GlycO" [10] which describes 1300 glycan structures (see section ) whose theoretical tandem mass spectra (MS) can be predicted by GlycoWorkbench [11]. If the maximum of cleavages is set to two and the number of cross-ring cleavages is set to one, then the theoretical $\mathrm{MS}^{2}$ spectrum contains $2,979,334$ ions, which themselves can be fragmented to form tens of millions of ions in $\mathrm{MS}^{3}$. To represent this data set of only two levels of the MS data using a Bayesian Network (BN) the network will be composed of two nodes, $\mathrm{MS}^{1}$ and $\mathrm{MS}^{2}$ with a single path $M S^{1} \rightarrow M S^{2}$ while the conditional probability table (CPT) for the $M S^{2}$ will contain $3,873,134,200(2,979,334 \times 1300)$ entries. For this kind of data, we propose a simple probabilistic graphical model for massive hierarchical data (PGMHD) which we consider as an extension to the Bayesian Network (BN,) that can represent massive hierarchical data in a more efficient way. We successfully apply the PGMHD in two different domains: bioinformatics (for multi-label classification) and search log analytics (for latent semantic discovery of related terms, as well as, semantically ambiguous terms).

The main contributions of this paper are as follows: We propose a simple, efficient and scalable probabilistic model that extends Bayesian Network for massive hierarchical data. We successfully apply this model to the bioinformatics domain in which we automatically classify and annotate high-throughput mass spectrometry data. We also apply this model for large-scale latent semantic discovery and semantically ambiguous terms discovery using 1.6 billion search log entries provided by CareerBuilder.com, using the Hadoop Map/Reduce framework.

# Background 

Graphical models can be classified into two major categories: (1) directed graphical models (the focus of this paper), which are often referred to as Bayesian Networks, or belief networks, and (2) undirected graphical models which are often referred to as Markov Random Fields, Markov networks, Boltzmann machines, or log-linear models [12]. Probabilistic graphical models (PGMs) consist of both graph structure and parameters. The graph structure represents a set of conditionally independent relations for the probability model, while the parameters consist of the joint probability distributions [1]. Probabilistic graphical models are often considered to be more convenient than numerical representations for two main reasons [13]:
1 To encode a joint probability distribution for $\mathrm{P}\left(X_{1}, \ldots, X_{n}\right)$ for $n$ propositional random variables with a numerical representation, we need a table with $2^{n}$ entries.
2 Inadequacy in addressing the notion of independence: to test independence between $X$ and $Y$, one needs to test whether the joint distribution of $x$ and $y$ is equal to the product of their marginal probability.

![img-0.jpeg](img-0.jpeg)

Figure 1 Bayesian Network

PGMs are used in many domains. For example, Hidden Markov Models (HMM) are considered a crucial component for most of the speech recognition systems [3]. In bioinformatics, probabilistic graphical models are used in RNA sequence analysis [4]. In natural language processing (NLP), HMM and Bayesian models are used for part of speech (POS) tagging [6]. The problem with PGMs in general, and Bayesian Networks in particular, is that they are not suitable for representing massive data due to the time complexity of learning the structure of the network and the space complexity of storing a network with thousands of random variables or random variables taking in many values. In general, finding a network that maximizes the Bayesian score which maximizes the posterior probability and Minimum Description Length (MDL) score which gives preference to a simple BN over a complex one, is an NP-hard problem [14].

# Bayesian Network 

A Bayesian Network is a concise representation of a large probability distribution to be handled using traditional techniques such as tables and equations [15]. The graph of a Bayesian Network is a directed acyclic graph (DAG) [2]. A Bayesian Network consists of two components: a DAG representing the structure (as shown in Figure 1), and a set of conditional probability tables (CPTs). Each node in a Bayesian Network must have a CPT which quantifies the relationship between the variable represented by that node and its parents in the network. Completeness and consistency are guaranteed in a Bayesian Network since there is only one probability distribution that satisfies the Bayesian Network constraints [15]. The constraints that guarantee a unique probability distribution are the numerical constraints represented by CPT and the independence constraints represented by the structure itself. The independence constraints is shown in Figure 1. Each variable in the structure is independent of any other variables other than its parents, once its parents are known. For example, once the information about A is known, the probability of L will not be affected by any new information about F or T , so we call L independent of F and T once A is known.

Bayesian Networks are widely used for modeling causality in a formal way, for decision-making under uncertainty, and for many other applications [15].

![img-1.jpeg](img-1.jpeg)

Figure 2 Naive Bayes

# Related Work 

Our research is related closely to Bayesian Network classifiers. In this section we review different forms of Bayesian Network classifiers to understand how the PGMHD extends BN in a way different than the existing models. We will cover the following BN classifiers:
1 Naive Bayes Classifier (NB).
2 Selective Naive Bayes (SNB)
3 Tree Augmented Naive Bayes (TAN).
4 Hidden Naive Bayes (HNB).
we will also cover how we applied PGMHD to other data mining problems, such as, latent semantic discovery of related search terms in users search logs, and of semantically ambiguous keywords by analyzing users' search logs.

## Naive Bayes (NB)

Naive Bayes is the simplist form of the BN classifiers and the most common one. This classifier is based on an assumption that all the features are independent given the class. Figure 2 shows an example of NB. A NB classifier is defined as follows:

$$
P(c \mid \mathbf{x}) \propto P(c) \prod_{j=1}^{n} P\left(x_{j} \mid c\right)
$$

Where $\mathbf{x}=\left(x_{1}, . ., x_{n}\right) . P(c)$ is the prior probability of class $c$ and $P\left(x_{j} \mid c\right)$ is the conditional probability of feature/variable $x_{j}$. The value of $c$ that maximizes the right hand side is chosen. A Naive Bayes classifier's performance depends upon the quality of the predictor features, such that the performance is improved when the predictor features are relevant and non redundant.

## Selective Naive Bayes (SNB)

In order to improve the performance of BN classifier by selecting the predictive features that are relevant and not redundant, Selective Naive Bayes (SNB) [16] is proposed as a feature subset selection problem. Let us define $\mathbf{x}_{F}$ as the projection of $\mathbf{x}$ onto a selected feature subset $\mathbf{F} \subset\{1,2, \ldots, n\}$. The classification equation becomes

![img-2.jpeg](img-2.jpeg)

Figure 3 Tree Augmented Naive Bayes

$$
P(c \mid \mathbf{x}) \propto P\left(c \mid \mathbf{x}_{F}\right)=P(c) \prod_{j \in F} P\left(x_{j} \mid c\right)
$$

# Tree Augmented Naive Bayes (TAN) 

This form of Bayesian Network classifier extends the NB by allowing each attribute to have at most one attribute parent in addition to its class parent. This extension tends to represent the fact that in some cases there is dependency or influence between features in a way that a value of a feature $x_{j}$ depends on a value of feature $y$. TAN classifier is defined as follows:

$$
P(c \mid \mathbf{x})=P(c) \prod_{j=1}^{n} P\left(x_{j} \mid p_{x j}, c\right)
$$

Where $p_{x j}$ is the attribute parent of $x_{j}$. Figure 3 shows an example of TAN.

## Hidden Naive Bayes (HNB)

HNB (Figure 4) is another extension of NB. In this extension each attribute $A_{i}$ gets a hidden parent $A_{h p i}$ to integrate the influences from all other attributes. The definition of the HNB classifier is as follows:

$$
P(c \mid \mathbf{x})=P(c) \prod_{j=1}^{n} P\left(x_{j} \mid h p_{j}, c\right)
$$

where,

$$
P\left(x_{j} \mid x_{h p j}, c\right)=\sum_{i=1, i \neq j}^{n} w_{j i} * P\left(x_{j} \mid x_{i}, c\right)
$$

## Probabilistic Graphical model for Massive Hierarchical Data Problems (PGMHD)

In this section we describe PGMHD. We discuss the structure of the model, its learning algorithm, and how it extends BN.

![img-3.jpeg](img-3.jpeg)

Figure 4 Hidden Naive Bayes

# Model Structure 

Consider a multi-level directed graph $G=(V, A)$ where $V$ and $A \subset V \times V$ denote the sets of nodes and arcs, respectively, such that:
$1 \quad V$ is partitioned into $m$ levels $L_{0}, \ldots, L_{m-1}$ such that $V=\cup_{i=0}^{m-1} L_{i}$, and $L_{i} \cup L_{j}=\emptyset$ for $i \neq j$.
2 The arcs in $A$ only connect one level to the next, i.e., if $a \in A$ then $a \in$ $L_{i-1} \times L_{i}$ for some $i=1, \ldots, m-1$.
3 An arc $a=\left(v_{i-1}, v_{i}\right) \in L_{i-1} \times L_{i}$ represents the dependency of $v_{i}$ with its parent $v_{i-1}, i=1, \ldots, m-1$. Moreover, let pa : $V \rightarrow \mathcal{P}(V)$ be the function that maps every node to its parents, i.e.,

$$
\operatorname{pa}(v)=\{w:(w, v) \in A\} \quad \forall v \in V
$$

4 The nodes in each level $L_{i}$ represent all the possible outcomes of a finite discrete random variable, namely $X_{i}, i=1, \ldots, m-1$.
Note that the nodes in the first level $L_{0}$ can be seen as root nodes and the ones in $L_{m-1}$ as leaves. Also, an observation $x$ in our probabilistic model is an outcome of a random variable, namely $X \in L_{0} \times \cdots \times L_{m-1}$, defined as

$$
X=\left(X_{0}, X_{1}, \ldots, X_{m-1}\right)
$$

which represents a path from $L_{0}$ to $L_{m-1}$ such that $\left(X_{i-1}, X_{i}\right) \in A$.
In addition, we assume that there are $t$ observations of $X$, namely $x^{1}, \ldots, x^{t}$, and let $f: V \times V \rightarrow \mathbb{N}$ be a frequency function defined as $f(w, v)=$ Frequency of Co-Occurrence $w$ and $v$. Moreover, these latter $t$ observations are the ones used to train our model, so that $f(w, v)>0$ for every $(w, v) \in A$.
It should be observed that the proposed model can be seen as a special case of a Bayesian Network by considering a network consisting of directed predefined paths. However, we believe that a leveled directed graph that explicitly defines one node per outcome of the random variables (as described above): i) leads to an easily scalable (and distributable) implementation of the problems we consider; ii) improves the readability and expressiveness of the implemented network; and iii) simplifies and facilitates the training of the model.

# Probabilistic-based Classification 

Given an outcome at level $i \in\{1, \ldots, m-1\}$, namely $v \in L_{i}$, we calculate the classification score $\mathrm{Cl}_{i}(w \mid v)$ of $v$ to the parent outcome $w \in L_{i-1}$ by estimating the conditional probability $P\left(X_{i-1}=w \mid X_{i}=v\right)$ as follows

$$
\begin{aligned}
\mathrm{Cl}_{i}(w \mid v) \quad:=\quad \frac{f(w, v)}{\operatorname{In}(v)}=\frac{\left(\frac{f(w, v)}{\operatorname{Out}(w)}\right) \cdot\left(\frac{\operatorname{Out}(w)}{t}\right)}{\left(\frac{\operatorname{In}(v)}{t}\right)} \\
= \text { for } \quad \frac{P\left(X_{i}=v \mid X_{i-1}=w\right) \cdot P\left(X_{i-1}=w\right)}{P\left(X_{i}=v\right)} \\
\quad=P\left(X_{i-1}=w \mid X_{i}=v\right)
\end{aligned}
$$

where

$$
\operatorname{In}(v):=\sum_{u \in \mathrm{pa}(v)} f(u, v), \quad \forall v \in V
$$

and

$$
\operatorname{Out}(w):=\sum_{u:(w, u) \in A} f(w, u), \quad \forall w \in V
$$

## Probabilistic-based Similarity scoring

Fix a level $i \in\{1, \ldots, m-1\}$, and let $X, Y \in L_{0} \times \cdots \times L_{m-1}$ be identically distributed random variables as in (1). We define the probabilistic-based similarity score CO (Co-Occurrence) between two outcomes $x_{i}, y_{i} \in L_{i}$ by computing the conditional joint probability

$$
\mathrm{CO}\left(x_{i}, y_{i}\right):=P\left(X_{i}=x_{i}, Y_{i}=y_{i} \mid X_{i-1} \in \operatorname{pa}\left(x_{i}\right) \cap \operatorname{pa}\left(y_{i}\right), Y_{i-1} \in \operatorname{pa}\left(x_{i}\right) \cap \operatorname{pa}\left(y_{i}\right)\right)
$$

as

$$
\mathrm{CO}\left(x_{i}, y_{i}\right)=\prod_{w \in \mathrm{pa}\left(x_{i}\right) \cap \mathrm{pa}\left(y_{i}\right)} p_{i}\left(w, x_{i}\right) \cdot \prod_{w \in \mathrm{pa}\left(x_{i}\right) \cap \mathrm{pa}\left(y_{i}\right)} p_{i}\left(w, y_{i}\right)
$$

where $p_{i}(w, v)=P\left(X_{i-1}=w, X_{i}=v\right)$ for every $(w, v) \in L_{i-1} \times L_{i}$. We can naturally estimate the probabilities $p_{i}(v, w)$ with $\hat{p}(v, w)$ defined as

$$
\hat{p}(w, v):=\frac{f(w, v)}{\operatorname{Out}(w)}
$$

Hence, we can obtain the related outcomes of $x_{i} \in L_{i}$ (at level $i$ ) by finding all the $y \in L_{i}$ with a large estimated probabilistic similarity score $\mathrm{CO}\left(x_{i}, y_{i}\right)$.

## Progressive Learning

PGMHD is designed to allow progressive learning which is shown in Algorithm 1. Progressive learning is a learning technique that allows a model to learn gradually

![img-4.jpeg](img-4.jpeg)
over time. Training data does not need to be given at one time to the model. Instead, the model can learn from any available data and integrate the new knowledge incrementally. This learning technique is very attractive in the big data age for the following reasons:
1 Training the model does not require processing all data upfront
2 It can easily learn from new data without the need to re-include the previous training data in the learning.
3 The training session can be distributed instead of doing it in one long-running session.
4 It supports recursive learning which allows the results of the model to be used as new training data, provided they are judged to be accurate by the user.

# PGMHD an extension to NB 

PGMHD extends NB in different directions to improve its scalability and ability to handle massive hierarchical data as follows:
1 It enables multi-label classification.
2 It enables multi-level representation of the predictive features.
3 It enables lazy classification.
The first dimension PGMHD extends is the multi-label classification. Our model allows more than one class to be in the root level of the classifier where any instance can be classified to more than one class. The second dimension of this extension is the multi-level classification which allows the classifier to represent the predictive features in $m$ levels instead of only 2 levels as in the regular NB. This extension allows the hierarchical modeling to preserve the structure of the data, which our experiments show is important for improving the quality of the classification. The last dimension of this extension is lazy classification against the eager NB. PGMHD is considered a lazy classifier since the calculation of the classification score of a new instance is all done during the classification process, unlike NB where all the CPT are pre-calculated and stored. This extension makes the PGMHD suitable for progressive learning, which can be very important for scalability.

## Experiments and Results

Glycans (Figure 6) are the third major class of biological macro-molecules besides nucleic acids and proteins [17]. Glycomics refers to the scientific attempts to char-

```
Data: Input Hierarchical Data
Result: PGMHD Instance
begin
    currentLevel = 0
    while currentLevel < maxInputLevel do
        foreach inputNode \in pgmhd(currentLevel) do
            if inputNode exists in PGMHD then
                get pgmhdNode where pgmhdNode.data = inputNode.data
                pgmhdNode.frequency+ = 1
            else
                pgmhdNode = newnode
                pgmhdNode.frequency = 1
            end
            childrenLevel = currentLevel + 1
            foreach inputChildNode \in inputNode.children do
                foreach pgmhdChildNode \in pgmhdNode.children do
                    if inputChildNode.data = pgmhdChildNode.data then
                    edge = edge(pgmhdNode, pgmhdChildNode) edge.frequency+ = 1
                    else
                    if childNode \in pgmhd(childrenLevel) then
                        pgmhdChildNode = node where node.data = childNode.data
                        edge = createNewEdge(pgmhdNode, pgmhdChildNode)
                        edge.frequency = 1
                    else
                        pgmhdChildNode = newNode pgmhdChildNode.data = child
                        pgmhdChildNode.frequency = 1
                        edge = createNewEdge(pgmhdNode, pgmhdChildNode)
                        edge.frequency = 1
                    end
                    end
                    end
            end
        end
    currentLevel = currentLevel + 1
    end
end
```

Algorithm 1: Learning Algorithm for PGMHD. currentLevel represents the current level in the input hierarchical data, we start with level ${ }_{0}$. maxInputLevel is the highest level in the input hierarchical data. In Figure $5 A_{i n}$ is an inputNode, while $A_{p g}$ is the pgmhdNode. $C_{1}$ is inputChildNode. $C_{3}$ is PgmhdChildNode. $F_{1}$ is edge.Frequency. $C_{1}, C_{2} \in$ inputParentNode.children. $C_{3}, C_{4}, C_{5} \in$ PgmhdParentNode.children

![img-5.jpeg](img-5.jpeg)

Figure 6 Glycan structure in CFG format. The circles and squares represent the monosaccharides which are the building blocks of a glycan while the lines are the linkages between them
acterize and study glycans, as defined in [17] or an integrated systems approach to study structure-function relationships of glycans as defined in [18].
Mass spectrometry (MS) is an analytical technique used to identify the composition of a sample [19]. Although (MS) has become the major analytical technique for glycans, no general method has been developed for the automated identification of glycan structures using MS and tandem MS data. MS ${ }^{\mathrm{n}}$ refers to the sequence of MS selection with some form of fragmentation, it is also called tandem MS. The relative ease of peptide identification using tandem MS is mainly due to the linear structure of peptides and the availability of reliable peptide sequence databases. In proteomic analyses, a mostly complete series of high abundance fragment ions is often observed. In such tandem mass spectra, the mass of each amino acid in the sequence corresponds to the mass difference between two high-abundance peaks, allowing the amino acid sequence to be deduced. In glycomics MS data, ion series are disrupted by the branched nature of the molecule, significantly complicating the extraction of sequence information. In addition, groups of isomeric monosaccharides commonly share the same mass, making it impossible to distinguish them by MS alone. Databases for glycans exist but are limited, minimally curated, and suffer badly from pollution from glycan structures that are not produced in nature or are irrelevant to the organism of study. PGMHD attempts to employ machine learning techniques (mainly probabilistic-based multi-label classification) to find a solution for the automated identification of glycans using MS data.
We recently implemented the Glycan Elucidation and Annotation Tool (GELATO), which is a semi-automated MS annotation tool for glycomics integrated within our MS data processing framework called GRITS (http://www.grits-toolbox.org/). Figures 7, and 8 show screen shots from GELATO for annotated spectra. Figure 7 shows the MS profile level and Figure 8 shows the annotation of $\mathrm{MS}^{2}$ peaks using fragments of a selected candidate glycan for annotation of the $\mathrm{MS}^{1}$ data. The output GELATO represents all the possible annotations to the given spectra. The user may select a subset of those possible annotations as the correct ones, but then he/she needs a smarter tool that can learn the correct selection and eliminate the incorrect ones in the future. PGMHD is successfully applied for that purpose as we show in this section.
To represent the MS data annotation using PGMHD, each annotation of $M S^{1}$ data (which is a glycan) is represented as a node in the top-layer of PGMHD. All

![img-6.jpeg](img-6.jpeg)

Figure 7 MS¹ annotation using GELATO. Scan is the ID number of the scan in the MS file, peak charge is the charge state of that peak in the MS file, peak intensity represents the abundance of an ion at that peak, peak m/z is the mass over charge of the given peak, cartoon is the annotation of that peak (glycan) in CFG format, feature m/z is the mass over charge for the glycan, and glycanID is the ID of the glycan in the Glycan Ontology (GlycO).

The fragments generated by that glycan and used to annotate peaks in MS² are represented by nodes in the lower layer and connected by edges with the parent node in the upper layer, and this pattern can be extended until MSn. Each fragment at level MS¹ is represented by a node in layer L¹-1 and connected by an edge with its parent node at layer L¹-2. The edge's weight represents the co-occurrence frequency between a child and a parent, and storing frequencies rather than probabilities facilitates progressive learning. Figure 9 shows the PGMHD for MS data with three levels (MS¹, MS², and MS³) in these figures. As shown in the model, three layers are created: one for the MS¹ level, a second one for the MS² level, and a third for MS³. Several different nodes at the MS¹ level can be annotated with the same fragment ion at the MS² level, so MS² nodes can have several parents. The frequency values are shown on the edges.

We annotated 3314 MS scans of banceriatic cancer samples using GELATO. Then an expert manually approved 1990 scan annotations which we used to train and test PGMHD. We split this data set into training data and test data sets. The size of the training data is 1779 scans and 121 scans for testing. We trained PGMHD and compared it against leading classifiers including Naive Bayes [20], SVM [21], Decision Tree [22], K-NN [23], Neural Network [24], Radial Basis Function network (RBF Network) [25] and Bayesian Network [26] from Weka [27]. Then we provide the test list to each classifier to predict the best glycan that annotates the scans in the test set. We also used Mulan [28], which is a Java library that extends Weka classifiers to handle multi-label classification problems. Also, we applied the m-estimate as a probability estimation technique To help PGMHD overcome the common problem for any Bayesian model which is the zero-frequency problem [29]. Figure 10 shows the precision and recall for the different classifiers compared to PGMHD after we used Mulan for multi-label classification and m-estimate for PGMHD. Another important aspect in our experiment besides accuracy is the scalability. In order to measure the scalability of PGMHD compared to the other classifiers we measure the space and time complexity. Figure 11 shows how PGMHD was the fastest model in the training phase, however it was not the best in the classification time as shown


Figure 8 Fragments of a selected glycan at the MS ${ }^{2}$ level. Each ion observed in MS ${ }^{1}$ is selected and fragmented in MS ${ }^{2}$ to generate smaller ions, which can be used to identify the glycan structure that most appropriately annotates the MS ${ }^{1}$ ion. Theoretical fragments of the glycan structure that had been used to annotate the MS ${ }^{1}$ spectrum are used to annotate the corresponding MS ${ }^{2}$ spectrum.
in Figure 12, though it did get the third best time. Most important is the space complexity used by each model which is shown in Figure 13. The memory usage which is the most important aspect in the scalability shows that PGMHD is much better than all the other classifiers especially the bayesian ones. Due to the difficulty of getting more manually curated MS annotations dataset for testing the scalability of our model in comparison to other machine learning models, we synthesized a dataset using GELATO. To synthesize a dataset with a massive number of MS annotations we used GELATO to generate all the possible annotations for the MS experiments which were manually curated before. We assume that all the generated annotations by GELATO are valid and correct annotations. Our focus in this part of the experiment is the scalability not the accuracy since the accuracy was already tested using the manually curated dataset. The new dataset includes 6776 instances for training and 392 instances for testing. The number of features is 2952 while the number of classes is 1340 . As a result of this extension in the training data, the Baysian Network classifer, K-NN, and RBF ran out of memory which means they can not handle this dataset in 4 GB of main memory. On the other hand PGMHD used only 160 MB to represent this dataset in memory. Figure 14 shows the memory usage of the models which scale successfully to handle the new dataset.

# Semantically Related Keywords in Search Logs 

Semantic similarity is a metric that is defined over documents or terms in which the distance between them reflects the likeness of their meaning [30], and it is widely used in Natural Language Processing (NLP) and Information Retrieval (IR) [31]. Generally, there are two major techniques used to compute semantic similarity: one is computed using a semantic network (Knowledge-based approach) [32], and

![img-7.jpeg](img-7.jpeg)

Figure 9 PGMHD representing MS annotations. The root nodes are the glycans that annotate the peaks at MS ${ }^{1}$ level, while the level 2 and 3 nodes are the glycan fragments that annotate the peaks at MS ${ }^{2}$ and MS ${ }^{3}$ level respectively and the edges represent dependency associating the glycans with their MS ${ }^{2}$ fragments and MS ${ }^{2}$ with their MS ${ }^{3}$ fragments.
the other is based on computing the relatedness of terms within a large corpus of text (corpus-based approach) [31]. The major techniques classified as corpusbased approaches are Pointwise Mutual Information (PMI) [33] and Latent Semantic Analysis (LSA) [34], though PMI outperforms LSA on mining the web for synonyms [35]. A group of Google researchers proposed two efficient models which can discover semantic word similarities [36]. The two novel models are the following:
1 Continuous Bag-of-Words model
2 Continuous Skip-gram model
These models aim to use large scale Neural Network to learn word vectors. The two models have restrictions that make them not suitable in our usecase. The first restriction is that both models require words and context in which those words are used. In their experiments, the authors built vectors of at least 50 words around the given word (words before and after the given word from the text in which that word was used). One more restriction is that they allow only single token words to be processed (no phrases). In our case, the two models are not applicable since the searches conducted by the users usually contains a single phrase with no context or other words surrounding it. Also, we care about phrases as opposed to single words, since small phrases are most commonly used in our search engine. For example "Java Developer" should be considered as a single phrase when we discover the semantically related phrases. In our experiment, we discovered high quality semantic relationships using a data set of 1.6 billion search logs (search keywords used to search for jobs on CareerBuilder.com). PGMHD completed this task in 45 minutes.

# Motivation 

We would like to create a language-independent algorithm for modeling semantic relationships between search phrases that provides output in a human-understandable format. It is important that the person searching can be assisted by an augmented query without us creating a black-box system in which that person is unable to understand and adjust the query augmentation. CareerBuilder ${ }^{[1]}$ operates job boards

[^0]
[^0]:    ${ }^{[1]}$ http://www.careerbuilder.com/

![img-8.jpeg](img-8.jpeg)

Figure 10 Precision and Recall after the Multi-label classification. PGMHD was applied with the m-estimate where $m=1$ and $p=0.1$
in many countries and receives tens of millions of search queries every day. Given the tremendous volume of search data in our logs, we would like to discover the latent semantic relationships between search terms and phrases for different region-specific websites using a novel technique that avoids the need to use natural language processing (NLP). We wish to avoid NLP in order to make it possible to apply the same technique to different websites supporting many languages without having to change the algorithms or the libraries per-language.
It is tempting to suggest using a synonym dictionary since the problem sounds like finding synonyms, but the problem here is more complicated than finding synonyms since the search terms or phrases on our site are often job titles, skills, and company names which are not, in most cases, regular words from any dictionary. For example if a user searches for "java developer", we would not find any synonyms for this phrase in a dictionary. Another user may search for "hadoop" which is also not a word that would be found in a typical English dictionary.

# Probabilistic Semantic Similarity Scoring using PGMHD 

We applied the proposed PGMHD model to discover the semantically related search terms by measuring probabilistic-based semantic similarity between those search terms. Given the search logs for all the users and the users' classifications as shown in Table 1, PGMHD can represent this kind of data by placing the classes of the users as root nodes and placing the search terms for all the users in the second level as children nodes. Then, an edge will be formed linking each search term back to the class of the user who searched for it. The frequency of each search term (how many users search for it) will be stored in the node of that term, while the frequency of a specific search term searched for by users of a specific class (how many users belonging to that class searched for the given term) will be stored in the edge between the class and the term. The frequency of the root node is the

![img-9.jpeg](img-9.jpeg)

Figure 11 Training time for different classifiers. Lazy classifiers (PGMHD, and K-NN) are much faster in the training phase due to the fact that no complicated calculation is required.

Table 1 Input data to PGMHD over hadoop


summation of the frequencies on the edges that connect that root node with its children (Figure 15).

# Distributed PGMHD 

In order to process 1.6 billion search logs (each search log contains one or more keywords used by a user to search for jobs on careerbuilder.com) provided by Careerbuilder in reasonable time, we designed a distributed PGMHD using Hadoop HDFS [37], Hadoop Map/Reduce [38] and Hive [39]. The design of distributed PGMHD is shown in figure 16. Basically we use Hive to store the intermediate data while we are buidling and training PGMHD. Once it is trained we can then run our inquires to get an ordered list of the semantically related keywords for a specific term(s).

### 0.0.1 Experiment Setup and Results

The experiment performing latent semantic discovery among search terms using PGMHD was run on a Hadoop cluster with 69 data nodes, each having a 2.6 GHz AMD Opteron Processor with 12 to 32 cores and 32 to 128 GB RAM. Table 2 shows sample results of 10 terms with their top 5 related terms discovered by PGMHD. To evaluate the model's accuracy, we sent the results to data analysts at CareerBuilder who reviewed 1000 random pairs of discovered related search terms and returned the list with their feedback about whether each pair of discovered related terms was "related" or "unrelated". We then calculated the accuracy (precision) of the model based upon the ratio of the number of related results to the total number

![img-10.jpeg](img-10.jpeg)

Figure 12 Classification time for different classifiers. The eager classifiers (Decision Tree, SVM, and RBF) are faster than the lazy ones due to the fact that the complicated computations are done during the training phase, which causes the classification time to be faster. Naive Bayes and Bayesian Networks did not do well due to the multi-label classification for which they are not suitable.
of results. The results show the accuracy of the discovered semantic relationships among search terms using the PGMHD model to be 0.80 .

Table 2 PGMHD results for latent semantic discovery


# Discovering Semantic Ambiguity of a Keyword 

The semantic ambiguity of a keyword can be defined as the likelihood of seeing different meanings of the same keyword in different contexts [40, 41]. The techniques mentioned in the literature focuses on utilization of ontologies and dictionaries like Wordnet as described in [40, 41]. Those solutions are not applicable when the keywords are from a domain like job search. In the job search domain the used keywords are typically job titles, skills, company names, etc. which are not regular English keywords. For example, java can mean a programming language, as well as, coffee but an English dictionary would not provide both of those meanings.

PGMHD is applied successfully to discover the semantic ambiguity of a keyword. About 1.6 billion search logs used in this experiment. The search keywords extracted from those 1.6 billion logs were used to train PGMHD, which was then used to calculate the normalized PMI score for each term with all of its parents. The initial

![img-11.jpeg](img-11.jpeg)

Figure 13 Memory usage by each model in MB for a dataset of 1779 instances annotated by 468
glycans (classes).

![img-12.jpeg](img-12.jpeg)

Figure 14 Memory usage by each model in MB for a training dataset of 6776 instances, 1640
features, and annotated by 1340 glycans (classes).

![img-13.jpeg](img-13.jpeg)

Figure 15 PGMHD Representing Job Search Keywords

results of this use case are promising, though work to improve the implementation

![img-14.jpeg](img-14.jpeg)
are is still ongoing. We plan to publish a separate paper about this use case of PGMHD soon.

Table 3 shows sample results of the discovered semantically ambiguous terms using PGMHD.

Table 3 PGMHD results for semantic ambiguity discovery. The first column shows the keyword, while the second column shows the related keywords of each possible meaning separated by horizontal line


# Conclusions and Future Work 

Probabilistic graphical models are very important in many modern applications such as data mining and data analytics. The major issue with existing probabilistic graphical models is their scalability to handle large data sets, making this a very important area for research, especially given the tremendous modern focus on big data due to the number of data points produced by modern computer systems and sensors. PGMHD is a probabilistic graphical model that attempts to solve the scalability problems with existing models in scenarios where massive hierarchical data is present. PGMHD is designed to fit hierarchical data sets of any size, regardless of the domain in which the data belongs. PGMHD can represent the hierarchical data with any number of levels, it can handle multi-label classification, and it is suitable for progressive learning since it is considered to be a lazy classifier. In this paper we present three experiments from different domains: one being the automated tagging of high-throughput mass spectrometry data in bioinformatics, the other being latent semantic discovery using search logs from the largest job board in the U.S, and the last one being identification of semantically ambiguous keywords. The three use

cases in which we tested PGMHD show that this model is robust and can scale from a few thousand entries to billions of entries, and that it can also run on a single computer (for smaller data sets), as well as in a parallelized fashion on a large cluster of servers ( 69 were used in our experiment). PGMHD is used in production at CareerBuilder.com for discovery of semantically related keywords and semantically ambiguous keywords. The work on discovering semantically ambiguous keywords is ongoing, and we plan to publish a separate paper about it. We plan to compare machine learning algorithms implemented in Apache Spark with PGMHD.

# Competing interests 

The authors declare that they have no competing interests.

## Author's contributions

KA carried out the design, implementation, and experiments related to MS annotation, Discovering semantically related keywords, and discovering semantically ambiguous keywords. MK participated in the design, implementation, and experiments related to discovering semantically related keywords, and discovering semantically ambiguous keywords. CO participated in the design, implementation, and experiments related to discovering semantically related keywords, and discovering semantically ambiguous keywords. TG participated in the design, and experiments related to discovering semantically related keywords, and discovering semantically ambiguous keywords. RR, WY, and MP participated in the design and validation of the MS annotation experiments. JM, KR, KK, and WY they all contributed to writing this manuscript and validating the model as well as the results. All authors read and approved the final manuscript.

## Acknowledgements

The authors would like to thank David Crandall from Indiana University for providing very helpful comments and suggestions to improve this paper. We also would like to thank Kiyoko Aoki Kinoshita from Soka University for the valuable discussions and suggestions to improve this model. Deep thanks to the search team, the big data team, and the data science team at CareerBuilder.com for their support while implementing and test this model over their Hadoop cluster.

## Author details

${ }^{1}$ Department of Computer Science, University of Georgia, Athens,GA, USA. ${ }^{2}$ School of Informatics and Computing, Indiana University, Bloomington, IN, USA. ${ }^{3}$ CareerBuilder.com, Norcross, GA, USA. ${ }^{4}$ Complex Carbohydrate Research Center, University of Georgia, Athens,GA, USA.
