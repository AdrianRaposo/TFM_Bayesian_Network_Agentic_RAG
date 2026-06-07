# A Bayesian Network Classification Methodology for Gene Expression Data 

Paul Helman, ${ }^{1}$ Robert Veroff, ${ }^{1}$ Susan R. Atlas, ${ }^{2}$ and Cheryl Willman ${ }^{3}$


#### Abstract

We present new techniques for the application of a Bayesian network learning framework to the problem of classifying gene expression data. The focus on classification permits us to develop techniques that address in several ways the complexities of learning Bayesian nets. Our classification model reduces the Bayesian network learning problem to the problem of learning multiple subnetworks, each consisting of a class label node and its set of parent genes. We argue that this classification model is more appropriate for the gene expression domain than are other structurally similar Bayesian network classification models, such as Naive Bayes and Tree Augmented Naive Bayes (TAN), because our model is consistent with prior domain experience suggesting that a relatively small number of genes, taken in different combinations, is required to predict most clinical classes of interest. Within this framework, we consider two different approaches to identifying parent sets which are supported by the gene expression observations and any other currently available evidence. One approach employs a simple greedy algorithm to search the universe of all genes; the second approach develops and applies a gene selection algorithm whose results are incorporated as a prior to enable an exhaustive search for parent sets over a restricted universe of genes. Two other significant contributions are the construction of classifiers from multiple, competing Bayesian network hypotheses and algorithmic methods for normalizing and binning gene expression data in the absence of prior expert knowledge. Our classifiers are developed under a cross validation regimen and then validated on corresponding out-of-sample test sets. The classifiers attain a classification rate in excess of $90 \%$ on out-of-sample test sets for two publicly available data sets. We present an extensive compilation of results reported in the literature for other classification methods run against these same two data sets. Our results are comparable to, or better than, any we have found reported for these two sets, when a train-test protocol as stringent as ours is followed.


## 1. Introduction

The advent of high-density microarray technology for gene expression profiling on the genomic scale (Schena et al., 1995; Lockhart et al., 1996; DeResi et al., 1997; Brown and Botstein, 1999) has opened new avenues of research in data analysis and knowledge discovery. With the huge quantities of data now being generated, the opportunities, as well as the challenges, appear almost limitless.

Recent literature explores several types of analyses of gene expression data:

- gene clustering, in which subsets of genes exhibiting similar expression patterns across cases (e.g., patients, experimental conditions, points of a time-series) are identified (Eisen et al., 1998; Tavazoie et al., 1999; Getz et al., 2000; Rigoutsos et al., 2000; Ben-Dor et al., 2001);
- case clustering, in which sets of cases that exhibit similar gene expression patterns are identified (Alizadeh et al., 2000; Getz et al., 2000; Rigoutsos et al., 2000; Bhattacharjee et al., 2001);

[^0]
[^0]:    ${ }^{1}$ Computer Science Department, University of New Mexico, Albuquerque, NM 87131.
    ${ }^{2}$ Department of Physics and Astronomy and Center for Advanced Studies, University of New Mexico, Albuquerque, NM 87131.
    ${ }^{3}$ Department of Pathology and UNM Cancer Research and Treatment Center, UNM School of Medicine, University of New Mexico, Albuquerque, NM 87131.

- case classification, in which the value of one or more attributes external to expression data (e.g., disease subtype, treatment response, prognosis) is predicted from gene expression levels (Alon et al., 1999; Golub et al., 1999; Ben-Dor et al., 2000; Ben-Dor et al., 2001; Khan et al., 2001; Ibrahim et al., 2002; Pomeroy et al., 2002; van't Veer et al., 2002); and
- gene network reconstruction, in which models of the gene regulatory system are built (Friedman et al., 1999; Murphy and Mian, 1999; Tobin et al., 1999; Friedman et al., 2000; D'haeseleer, 2000; Woolf and Wang, 2000; Pe'er et al., 2001). This objective can be viewed as subsuming the others, provided that the external classification variables are included as nodes in the network.

Two factors influence a researcher's focus: the questions of interest in a given setting and the nature of the data sets available. Each of the goals sketched above is of great import, and, in fact, advances in one area often contribute to advances in the others. For example, the identification of strong gene clusters, in addition to indicating potentially significant biological relationships (e.g., co-regulation), in some instances may allow a set of genes to be collapsed into a single abstract unit, thereby reducing problem dimensionality and allowing other objectives to be more successfully addressed.

The data sets available may or may not include information to support classification. Training data that is labeled-associating with each training case the class to which it belongs-supports statistical methods for constructing a classifier. After training on a collection of labeled data, a classifier is constructed which, when presented with new query cases, predicts a class label from gene expression levels and other possibly relevant information which may be associated with a case. Without class-labeled data, genes and cases can be clustered but not classified. Often, however, an effort is made after the fact to construe biological significance for the clusters formed; the success of such clustering methods depends critically on there being a relationship between the measure of similarity used to perform clustering and actual biological similarity. Techniques that attempt to classify after training on labeled data are referred to as supervised, while those that do not utilize labels in training (e.g., many techniques for gene and case clustering) are known as unsupervised.

Additionally, various amounts of prior information (e.g., expert knowledge, such as previously known or suspected functional relationships) can be associated with gene expression data in an attempt to guide the analysis methods toward better results. Again, the amount of information available-and the degree of belief in this information-determines what information can be utilized and how it can be utilized. Little is understood regarding how such information can best be represented and applied within a rigorous and consistent framework. Such a framework will become of ever increasing importance as our biological knowledge base grows and as our objectives increase in their scope and complexity.

Our group at the University of New Mexico (UNM) is fortunate to have unusually large microarray data sets, with a substantial amount of associated clinical information. This clinical information can be utilized both as additional input and to establish classification criteria. For example, clinical history might be available that allows us to search for correlations between environmental factors and gene expression levels and, ultimately, biological manifestation (e.g., disease). In the realm of classification, we expect to have several interesting class labels to associate with our gene expression data, thus allowing us to explore a variety of supervised classification problems. Information that will be available to us includes disease absence or presence, disease type (e.g., leukemia subtypes), response to treatment, relapse / nonrelapse information, and karyotype.

Consequently, we are motivated to concentrate on the development of methodologies that can exploit the unusually rich amount of information to be associated with our gene expression data and to develop techniques particularly well suited to classification in this context. At the same time, we anticipate soon extending our objectives to include the construction of gene regulatory networks and wish also to be able to integrate in a rigorous way external information, such as prior identification of key controlling genes, causal relationships between genes, and known or hypothesized gene clusters. As is argued in the sections to follow, we believe that the mathematically grounded framework of Bayesian networks (Bayesian nets)—for example, Pearl (1988) and Heckerman et al. (1995)—is uniquely suited to meet these objectives. Furthermore, the ability of Bayesian nets to integrate

prior knowledge with observational evidence potentially provides researchers with the ability to build incrementally solutions to problems of increasing scope and complexity. The primary contribution of the current work is the development of a Bayesian network classification model that is customized for the characteristics of gene expression data. In particular, we propose a Bayesian network structure whose relative simplicity allows the computational effort to be focused on the very high dimensionality inherent in gene expression data. This strategy is designed specifically to exploit certain domain-specific beliefs regarding gene and class label interactions. The initial experimental results reported here bear out the validity of this approach. Further, by operating within the Bayesian framework, the aforementioned capabilities-such as the ability to capture the inter-gene relationships of regulatory networks-remain available to the model in the form of future enhancements.

The remainder of this paper is organized as follows. Section 2 briefly reviews some of the most successful Bayesian network classification methods reported in the literature, details the key elements of our approach, and offers a motivation for our approach in the context of clinical classification from gene expression data. Section 3 presents alternative search methodologies which we have utilized in Bayesian net classifier construction. Section 4 describes our experimental design and Section 5 presents a suite of results. Since we began developing and implementing our techniques prior to the production of microarray data at UNM, the experimental results reported here are against two publicly available Affymetrix data sets: ${ }^{4}$

- MIT leukemia data (Golub et al., 1999), for samples of two types, ALL and AML, of leukemia. This data set is available at http://www-genome.wi.mit.edu/cgi-bin/cancer/publications/pub_paper.cgi? mode=view\&paper_id=43.
- Princeton colon cancer data (Alon et al., 1999), for normal and tumor tissue samples (available at http://microarray.princeton.edu/oncology/affydata/index.html).

For purposes of comparison, an appendix presents an extensive compilation of results reported in the literature for these two datasets, generated using a broad range of classification methodologies.

At the time of this writing, some of the UNM data has begun to become available. As is reported in a series of papers (Mosquera-Caro et al., 2003a; Mosquera-Caro et al., 2003b) our classification methodology continues to perform well on these data sets as compared with other classification methods such as support vector machines (Vapnik, 1998) and discriminant analysis (Bishop, 1996; Duda et al., 2000), though we have discovered that some clinical classification tasks (e.g., prognosis prediction) are inherently more difficult than are such tasks as classification by disease subtype.

# 2. Bayesian Nets for the Classification of Gene Expression Data 

A Bayesian net (Pearl, 1988; Heckerman et al., 1995) is a graph-based model for representing probabilistic relationships between random variables. The random variables, which may, for example, represent gene expression levels, are modeled as graph nodes; probabilistic relationships are captured by directed edges between the nodes and conditional probability distributions associated with the nodes. A Bayesian net asserts that each node is statistically independent of all its nondescendants, once the values of its parents (immediate ancestors) in the graph are known, i.e., a node $n$ 's parents render $n$ and its nondescendants conditionally independent. It follows from these conditional independence assertions and the laws of probability that once a conditional distribution is associated with each node, specifying the probability that the node assumes a given value conditioned on the values assumed by the node's parents, a joint distribution for the entire set of random variables is uniquely determined. Algorithms and software packages (Lauritzen and Spiegelhalter, 1988; Jensen et al., 1990; Shafer and Shenoy, 1990; Dawid, 1992; Dechter, 1996; Madsen and Jensen, 1999; Cozman, 2001; Jensen, 2001) have been

[^0]
[^0]:    ${ }^{4}$ These sets were produced using the analysis algorithms of the Affymetrix Microarray Suite (MAS) Version 4.0. Future data sets will be based on the newer statistical algorithms provided by MAS Version 5.0. See http://www.netaffx.com/index.affx.

developed to help the analyst visualize and query Bayesian nets, making this a very convenient representational tool.

While Bayesian nets have found much use as a representational tool for modeling known probabilistic relationships, from the perspective of the gene expression analysis tasks of current interest, their primary utility lies in the fact that they also are a powerful learning paradigm. A body of work has evolved-see, for example, Buntine (1991, 1996), Dawid and Lauritzen (1993), Friedman and Goldszmidt (1996a, 1996b), Heckerman et al. (1995), Lam and Bacchus (1994), Pearl and Verma (1991), and Spiegelhalter et al. (1993)—in which statistical machine learning techniques utilize a combination of data (observations) and prior domain knowledge to direct a search for Bayesian nets which best explain the current state of knowledge embodied by these inputs. This makes Bayesian nets an attractive framework for gene expression analysis, since they can methodically hypothesize and test gene regulatory models, and other such relationships, using the rigorous methods of classical probability theory and statistics.

Not surprisingly then, others-for example, Friedman et al. (1999), Friedman et al. (2000), and Pe'er et al. (2001)—have successfully applied Bayesian nets to the domain of gene expression analysis. Approaches reported in those works differ from those reported here both with respect to goals (e.g., the identification of gene relationships versus our classification objectives) and with respect to the heuristics employed in an attempt to tame the complexities of the problem. The three cited papers, for example, focus on reconstructing regulatory networks by identifying network relationships most strongly supported by the data and develop heuristics for construction of Bayesian nets that reveal such structure.

The construction of regulatory networks is an eventual goal of our work as well. Hence, the natural applicability of Bayesian networks to regulatory network construction provides one of our motivations for tackling with Bayesian networks the specific problem of immediate interest, clinical classification from gene expression data. The literature contains several different Bayesian network classification models. Friedman et al. (1997) describe an approach, Tree Augmented Naive Bayes (TAN), to using Bayesian nets in classification as a way of improving upon the classification approach known as Naive Bayes (Duda and Hart, 1973; Langley et al., 1992). Madden (2002) describes a heuristic for building a Markov blanket classifier (see, for example, Cheng and Greiner (1999)) that focuses search on only those network nodes which are relevant to determining the class label's probability distribution, thus making the search over the space of full, unconstrained Bayesian net classifiers more computationally effective. Buntine (1992) develops classification trees in a Bayesian framework. Friedman and Goldszmidt (1996b) and Chickering et al. (1997) develop extensions to the Bayesian network model in which local structure between variables can be captured and exploited by importing the structure of decision trees and graphs. To our knowledge, however, these approaches have not been applied in the context of classification problems of such high dimensionality as the problem of clinical classification from gene expression data.

The approach we have chosen to take, rather than starting with these most general and potentially complex Bayesian models that have been developed as general-purpose classification methods, is to attempt to utilize a modest amount of domain knowledge and develop a model that allows the computational effort to be focused where that domain knowledge suggests the most benefit will result. Consequently, a primary contribution of the current work is the development of a Bayesian network classification model that is customized for the characteristics of gene expression data.

The most significant aspects of the customizations presented here involve approaches to cope with the very high dimensionality (i.e, large number of genes, each of which assumes a wide range of values) inherent in gene expression data by exploiting the belief that a relatively small number of genes, taken in different combinations, is actually required to predict most clinical classes of interest. This prior belief regarding the nature of these gene expression classification tasks has led us to a rather simple Bayesian network classification structure that, in its initial tests, has performed quite well in comparison with other state-of-the-art learning schemes when applied to several gene expression classification tasks. See the Appendix and (Mosquera-Caro et al., 2003; Kang and Atlas, 2003) for detailed comparisons.

In the following, we introduce our method as an alternative to the existing Bayesian net classifier models, and

then briefly contrast the method with the structurally similar methods of Naive Bayes and TAN. We believe this comparison will motivate our approach as a particularly effective, yet equally compact, alternative for problem domains of extremely high dimensionality, such as gene expression data. The experimental results reported in Section 5 bear out the merit of our approach in the gene expression domain. While it appears that the success of our model structure stems from its focusing of the search on those dimensions of the model space from which the greatest gain often is found, our classification model is nevertheless amenable to future extensions with techniques that can utilize and/or discover additional local structure between the genes (Friedman and Goldzmidt, 1996b; Chickering et al., 1997) and to model averaging techniques (for example, Han and Carlin (2000) and Madigan and York (1995)) for augmenting the distribution blending methods presented in Section 3.5.

The work presented here provides an alternative formulation and solution to the classification problem, a formulation which appears to be particularly well suited to classification based on gene expression data. While the focus of our current research is to extend our methods to other biologically important problems, such as the construction of regulatory networks, in this article we do not consider problems beyond classification. In this context, our work is most appropriately compared with other Bayesian network-based classification schemes, such as Naive Bayes, TAN, and Markov blanket classifiers; with other related classification methods, such as Bayesian classification trees; and, in general, with other classification methods, such as support vector machines and boosting.

# A Bayesian Net Classification Model for Gene Expression Data 

We view each gene as a random variable, with the class label as an additional random variable. The genes assume expression levels (which we shall bin into a small number of distinct values), and the label assumes values such as "cancer" or "no-cancer," type of cancer, or response to treatment. $<e>$ denotes a vector of expression levels assumed by the set genes of all genes in a single case, and $c_{k}$ denotes a value assumed by the class label. The classification problem can be stated as learning the posterior conditional distribution of the class label $C$, conditioned on the gene expression levels, that is, the collection of conditional probabilities

$$
\operatorname{Pr}\left\{C=c_{k} \mid \text { genes }=<e>, \text { current knowledge }\right\}
$$

one for each $c_{k}$ and $<e>$ combination.
The current knowledge appearing in the conditioning event of the above probability generally includes both a training set of cases and prior distributions over the random variables. These prior distributions may capture, for example, prior beliefs regarding biological mechanisms. From this perspective, classification can be solved as a problem of statistical density estimation. After viewing the training set-a sample of vectors of expression values with an associated class label, drawn from the same distribution as the query cases we later will be asked to classify-we apply laws of probability to update our priors and "learn" this common distribution. We then are able to estimate the probability that query $q$ 's class label $q[C]$ is $c_{k}$, given that $q$ 's expression vector $q[$ genes $]$ is $<e>$.

The main difficulty in this learning problem is that the huge dimensionality of $<e>$ implies that any realistically-sized sample will provide only extremely sparse coverage of the sample space. For example, even if continuous expression levels are partitioned into 2 or 3 discrete bins, each of the number_of_bins ${ }^{\text {number_of _genes }}$ combinations of (binned) expression levels of the several thousand genes which appear in the training data typically appears only once, and combinations in the query cases typically have not appeared at all in the training data. Consequently, estimation of the conditional distributions from simple joint frequencies observed in the sample is impossible.

We consider Bayesian nets in which each gene is a node, and the class label is an additional node having no children. Associated with each node $n$ is a conditional distribution, a set of $\theta_{n=v, p a r=<p>} \equiv \operatorname{Pr}\{n=v \mid \operatorname{Par}(n)=<$ $p>\}$, specifying a conditional probability for each value $v$ of $n$, conditioned on each combination of values $<p>$ of the parents of $n$. Note that a Bayesian net is a pair $(G, \Theta)$, where $G$ is a directed acyclic graph (DAG), and $\Theta$ supplies a conditional probability $\theta_{n=v, p a r=<p>}$ for every node value, parent set-combination implied by

G. Such a pair $\langle G, \Theta\rangle$ compactly encodes a unique joint distribution over the nodes of $G$; this joint distribution $\operatorname{Pr}\{$ genes $=<e>, C=c_{k}\}$, and any conditional distribution over the random variables represented by the nodes, can be recovered via various known graph traversal algorithms (Lauritzen and Spiegelhalter, 1988; Jensen et al., 1990; Shafer and Shenoy, 1990; Dawid, 1992; Dechter, 1996; Madsen and Jensen, 1999; Cozman, 2001; Jensen, 2001).

If we had a fixed Bayesian net that encoded the true distribution from which each case is drawn, we could extract a classifier, namely the subgraph defined by the class label node $C$ and its parent set $\operatorname{Par}(C)$, along with the associated conditional distributions $\theta_{C=c_{k}, \text { par=<p> }}=\operatorname{Pr}\left\{C=c_{k} \mid \operatorname{Par}(C)=<p>\right\}$. Note that the conditional independence assertion associated with (leaf) node $C$ implies that the classification of case $q$ depends only on the expression levels of the genes in $\operatorname{Par}(C)$, i.e., the distribution $\operatorname{Pr}\{q[C \mid q[\text { genes }]\}$ is identical to the distribution $\operatorname{Pr}\{q[C] \mid q[\operatorname{Par}(C)]\}$. Note, in particular, that the classification does not depend on other aspects (other than the parent set of $C$ ) of the graph structure of the Bayesian net. Hence, once given a parent set, density estimation becomes far more tractable. Rather than being concerned with combinations of all the genes, we are concerned only with combinations of the parent set, and hence a training sample will generally provide much better coverage of this reduced space.

Given a fixed Bayesian net of the form described, the classification rule it induces is simply a table associating values $<p>$ of the parent variables and $C=c_{k}$ of the class label with the network's induced conditional probability $\theta_{C=c_{k}, \text { par=<p> }}$. However, we are not given the "true" Bayesian net, but, rather, a collection of training cases, plus, possibly, some accumulation of prior knowledge, and our task is to build a classifier to fit these data. How the classifier is constructed to fit the data is what primarily distinguishes methods, ultimately determining success or failure. Two central aspects of the construction enabled by operating within the Bayesian framework are:

The use of a Bayesian metric in controlling the complexity of the classification rule. While it often is observed that tables representing complex classification rules (complex conditions over many attributes) overfit to the training data, our use of the $B D$ metric (Heckerman et al. 1995) as described in Section 3.1 balances in a principled way the gain in adding new conditions with the complexity of the rule. MacKay (1995) has formalized how a Bayesian metric inherently embodies Occam's razor, favoring simple rules unless sufficient gain in information is realized by the addition of conditions. Hence, a stopping condition for rule refinement is not ad hoc, but part of the Bayesian metric evaluation. ${ }^{5}$ Further, when prior information is available, it is incorporated naturally into the evaluation. It also is possible to incorporate into the model local structure, as described in Friedman and Goldzmidt (1996b) and Chickering et al. (1997). While this has not been necessary for the classification tasks undertaken to date, future work will explore the utility of this model extension in the gene expression domain.

The blending of distributions in a principled way. As is detailed in Section 4, we search a space of networks for a collection of networks that score well under the $B D$ metric. If we chose the single best scoring network (the maximal posterior method) we would utilize as our posterior the single conditional distribution this network induces. Our approximation of the posterior is more sophisticated in that it is capable of blending the distributions of a possibly large number of networks. The blending is based directly on the mathematics of the Bayesian analysis. In one of our two search methods, the blending is over the highest a posterior probability networks of an exhaustively searched model space. In the second search method, a larger model space is sampled by means of a greedy search. Future extensions to the sampling methods utilizing MCMC averaging techniques (Han and Carlin, 2000; Madigan and York, 1995) would be quite natural.

# Comparison With Existing Bayesian Net Classification Models 

[^0]
[^0]:    ${ }^{5}$ Similarly, Buntine (1992) applies a Bayesian metric in connection with classification tree construction; alternatively, the MDL evaluation criterion-which includes an explicit penalty term for model complexity-has been used quite successfully in Bayesian network learning (Friedman et al., 1997). In a separate work (Ding, 2003), we are comparing the MDL and $B D$ metric in the gene expression domain.

As was reviewed earlier in this section, several Bayesian network classification models have been proposed. In terms of its simplicity of structure, our model most resembles Naive Bayes and its generalization known as TAN. However, unlike these existing models, our model was conceived specifically to address key characteristics of the gene expression application domain. In particular, our model is customized to application domains having very high dimensionality (e.g., many genes), while at the same time exhibiting a dependency structure which implies that a relatively small number of features, taken in different combinations of several features at a time, is required to predict the class label of interest. These are characteristics consistent with prior experience with gene expression data and which translate to dependency structures which Naive Bayes or TAN are incapable of capturing. After contrasting our model with Naive Bayes and TAN, we briefly consider the potential for extending our model with techniques that have proven successful in other application domains.

A Naive Bayesian classifier (Duda and Hart, 1973; Langley et al., 1992) assumes independence of the features (genes), given the value of the class label. Under this assumption, the conditional probability $\operatorname{Pr}\{q[C] \mid q[\text { genes }]\}$ can be computed from the product $\prod_{g_{i} \in \text { genes }} \operatorname{Pr}\left\{q\left[g_{i}\right] \mid q[C]\right\}$ of the marginal conditional probabilities. The Naive Bayesian model is equivalent to a Bayesian net in which no edges exist between the genes, and in which an edge exists from the class label into each gene. Friedman et al. (1997) introduces Tree Augmented Naive Bayes (TAN), which relaxes somewhat the independence assumption of a Naive Bayesian classifier by allowing each gene to have an incoming edge from at most one other gene, while maintaining an edge from the class label into each gene. This approach yields good improvements over Naive Bayesian classifiers in the experiments-which are over application domains other than gene expression data-reported in Friedman et al. (1997).

By contrast, our modeling assumes neither an edge between each gene and the class label, nor concerns itself with gene interaction. Rather, we are able to ignore the issue of what edges may exist between the genes, and compute $\operatorname{Pr}\{q[C] \mid q[\text { genes }]\}$ as $\operatorname{Pr}\{q[C] \mid q[\operatorname{Par}(C)]\}$, an equivalence that is valid regardless of what edges exist between the genes, provided only that $\operatorname{Par}(C)$ is a set of genes sufficient to render the class label conditionally independent of the remaining genes. This modeling is in response to a prior belief (supported by experimental results reported here and in other gene expression analyses) that for the gene expression application domain, only a small number of genes, taken in combination, is necessary to render the class label (practically) conditionally independent of the remaining genes. This both makes learning parent sets $\operatorname{Par}(C)$ tractable, and generally allows the quantity $\operatorname{Pr}\{q[C] \mid q[\operatorname{Par}(C)]\}$ to be well estimated from a training sample.

Each of these two simple models for Bayesian network classifiers-TAN and the model presented here-has advantages over the other in certain situations. Specifically, because our parent sets, in principle, allow an arbitrary number of genes to interact in combination, any conditional distribution for the class label can be modeled exactly. This is in contrast to TAN, where no term of the joint probability distribution may involve combinations of more than two genes. (Terms of the joint distribution, expanded according the conditional independence assertions implied by any TAN network, are of one of the following three forms: $P\{C\}, P\{g \mid C\}$, or $P\left\{g \mid C, g^{\prime}\right\}$.) Consequently, it is a simple matter to identify families of underlying distributions over $n$ random variables (for any $n \geq 3$ ) where every TAN network is necessarily asymptotically incorrect, while instances of our model are asymptotically correct. That is, for these families of distributions, as the sample grows to reflect the actual distribution, any TAN network misclassifies some (possibly large) fraction of the query cases, whereas our model approaches perfect classification when all the relevant variables are included in the parent set. In practice with gene expression data, it has been our experience that, typically, combinations of between 2 and 5 binary-binned genes determine the class label-that is, render the class label conditionally independent of the other genes-while combinations of up to 5-7 binary-valued genes can reasonably be evaluated (for example, by the $B D$ metric) and distributions learned from data sets of the sizes with which we have been working.

TAN's advantage may be seen when the sample is sparse relative to the number of genes necessary to render the class label approximately conditionally independent of the other genes. In such a case, if the true distribution obeys or approximates the conditional independence assertions of TAN, the TAN model is capable of learning the correct distribution, and will converge to this distribution faster as a function of sample size than will our model.

Our network blending (see Section 3.5) can somewhat mitigate the problem for some distributions, and, further, in some instances it may be desirable to augment our model with local structure, allowing our density estimates to converge to the true distribution even for sparse samples. (Note that the incorporation of local structure would not address the inaccuracies of TAN when its conditional independence assertions are violated.)

One can envision a hybrid search, where the $B D$ metric evaluates the fit of networks from both classification models, choosing the best fitting model, or possibly even blending their distributions. In the limiting case, of course, one could consider unconstrained and full Bayesian nets, using the Markov blankets they define as the classifier (Cheng and Greiner, 1999; Madden, 2002). While this is the most general of the modeling approaches, it is very much an open question (especially for applications with the characteristics described here) whether or not the gain in modeling generality is actually an advantage, given the fact that the search over the more constrained network space implied by our model structure (possibly combined with TAN structures) may focus on that task-construction of good parent sets, expected to be of small cardinality-most likely to determine classifier quality. Similarly, it is not clear whether, in the gene expression domain, the diversion of search time to include consideration of local structure would generally be beneficial or not. As indicated, current gene expression data sets do yield sufficient coverage of the small number (e.g., often less than 5) of binary-binned genes that our experience indicates are required for the class label's parent sets, and focusing search on the selection of such subsets of genes often may be the most fruitful utilization of search time. Future experiments will explore these issues further.

# 3. Additional Model Details 

Our approach requires that we address the following issues, which are considered in this and the sections to follow.

- What does it mean for a Bayesian net to be plausible?
- What do we do with multiple plausible Bayesian nets?
- How do we find (the parent sets $\operatorname{Par}(C)$ in) plausible Bayesian nets?
- How do we specify prior distributions?
- How do bin the continuous gene expression data?
- How do we preprocess (e.g., normalize) the gene expression data?


### 3.1. Scoring the Nets

The derivations in this and the following sections summarize and adapt to our context the work appearing in Heckerman et. al. (1995), and we implicitly accept the set of assumptions made there.

Bayesian net structures are hypotheses. Each network structure $G$ hypothesizes a collection of conditional independence assertions. Were hypothesis $G$ true with probability 1 , the assertions it encodes, plus the priors and observations $D$, would induce via the laws of probability a posterior distribution $f(\Theta \mid G, D$, prior $)$ over the space of conditional distributions for $G$, where each $\Theta$ in the space contains conditional distributions $\theta_{n=v, p a r=<p>}$ for each node $n$ in $G$. Of particular interest are expectations under this distribution of the form

$$
E\left(\theta_{n=v, p a r=<p>} \mid G, D, \text { prior }\right)=\int f(\Theta \mid G, D, \text { prior }) \times \theta_{n=v, p a r=<p>} d \Theta
$$

as this is $\operatorname{Pr}\{n=v \mid \operatorname{Par}(n)=<p>, G, D$, prior $\}$. For classification, of course, the desired quantity is

$$
\begin{aligned}
& E\left(\theta_{C=c_{k}, \text { par=<p> }} \mid G, D, \text { prior }\right) \\
& \quad=\operatorname{Pr}\left\{C=c_{k} \mid \operatorname{Par}(C)=<p>, G, D, \text { prior }\right\} \\
& \quad=\operatorname{Pr}\left\{C=c_{k} \mid<e>, G, D, \text { prior }\right\}
\end{aligned}
$$

for any full expression vector $\langle e\rangle$ whose projection onto the parent set $\operatorname{Par}(C)$ is $\langle p\rangle$. (Recall that class label $C$ is constrained to have no children in the network.)

In a learning context, we generally never obtain a single net structure $G$ with certainty, but rather obtain a collection of plausible $G_{i}$. Therefore, it is desirable to employ a probabilistically-based scoring function, both to guide our exploration of nets, and to specify how to blend the distributions they induce. In a Bayesian framework, one scores how well a hypothesis $G_{i}$ fits $\{D$, prior $\}$ by computing

$$
\operatorname{Pr}\left\{D \mid G_{i}, \text { prior }\right\}=\int \operatorname{Pr}\{D \mid \Theta\} \times f\left(\Theta \mid G_{i}, \text { prior }\right) d \Theta
$$

Then, from priors $P\left(G_{i}\right)$ over network structures, we can obtain $\operatorname{Pr}\left\{G_{i} \mid D\right.$, prior $\}$. Such a scoring function is known as a Bayesian metric.

If we evaluated all possible structures $G_{i}$ in this manner, the posterior distribution over joint distributions $\Theta_{j}$ of the nodes in the networks is computed by

$$
f\left(\Theta_{J} \mid D, \text { prior }\right)=\sum_{G_{i}} f\left(\Theta_{J} \mid G_{i}, D, \text { prior }\right) \times \operatorname{Pr}\left\{G_{i} \mid D, \text { prior }\right\}
$$

The classification probabilities

$$
\operatorname{Pr}\left\{q[C]=c_{k} \mid q[\text { genes }]=<e>, D, \text { prior }\right\}
$$

of interest then are the expectations

$$
E\left(\theta_{q[C]=c_{k}, q[\text { genes }]=<e>} \mid D, \text { prior }\right)
$$

under this distribution and are obtained as a weighted sum of expectations, namely

$$
\sum_{G_{i}} E\left(\theta_{q[C]=c_{k}, \text { par=<p> }} \mid G_{i}, D, \text { prior }\right) \times \operatorname{Pr}\left\{G_{i} \mid D, \text { prior }\right\}
$$

where each parent vector $\langle p\rangle$ is the projection of $\langle e\rangle$ onto the parent set par of $C$ in each $G_{i}$. That is, the probability each $G_{i}$ assigns to $q[C]$ given $q[$ genes $]$ is weighted by the posterior $\operatorname{Pr}\left\{G_{i} \mid D\right.$, prior $\}$. In principle, if we could evaluate this sum over all $G_{i}$, we would have an exact posterior-and hence classifier-given the current state of knowledge represented by our priors and the observed cases. The more peaked is the distribution $\operatorname{Pr}\{q[C]=c_{k} \mid q[$ genes $]=\langle e>, D$, prior $\}$ about its mode class $c^{*}$, the higher is the probability that the classification provided for query $q$ is correct.

# 3.2. Computational Considerations 

Our task can be viewed as approximating expression (2) by finding a set of nets whose respective contributions dominate (e.g., because they have relatively high posterior weights $\operatorname{Pr}\left\{G_{i} \mid D\right.$, prior $\}$ ) the evaluation of this sum. Some empirical studies (Cooper and Herskovita, 1992; Heckerman et al., 1995) indicate that, in a variety of contexts, only a relatively small number of the nets considered (e.g., often 1) have weights large enough to materially influence the evaluation, since the weights drop off quickly as edges which represent necessary

dependencies are omitted or edges which represent unnecessary dependencies are added. The experimental results reported in Section 5 explore the effect of varying the number of nets used in this approximation. One important conclusion we draw is that, in the context of high-dimensional gene expression data, the inclusion of more nets than is typical appears to yield better results. Our experiments indicate this to be the case both because the "polling" provided by a large number of nets is more accurate than that provided by a small number, and because a large number of nets often provides better coverage of the expression value combinations observed in the query cases (that is, the inclusion of more nets increases the chances that query $q$ 's binned expression levels projected onto some included parent sets have been observed in the training sample).

On the surface, the evaluation of even a single $G$ seems a formidable task; both the expectations (1) and the Bayesian metric require an integration over potentially arbitrary distributions for $\Theta$. However, following the work of Heckerman et al. (1995), we assume that a prior distribution is specified in terms of a complete net and is Dirichlet. Intuitively, such a prior can be equated with an imaginary sample of joint observations of the random variables that represents the analyst's beliefs-both in terms of relative frequency counts (corresponding to prior probabilities) and absolute size (corresponding to degree of belief)—prior to observing the sample cases. This prior distribution on the nodes of a complete net induces on the nodes of any net a unique prior distribution consistent with a modest set of assumptions. Then, for any $G$ and this induced prior distribution, plus a set of observed cases, the calculations reduce to a closed form.

In particular, the closed form for the expectation is

$$
\begin{aligned}
& E\left(\theta_{n=v, p a r=<p>} \mid G, D, \text { prior }\right) \\
& \quad=\int f(\Theta \mid G, D, \text { prior }) \times \theta_{n=v, p a r=<p>} d \Theta \\
& \quad=\left(\alpha_{p v}+N_{p v}\right) /\left(\alpha_{p}+N_{p}\right)
\end{aligned}
$$

where $N_{p}$ is the number of cases observed in $D$ in which $\operatorname{Par}(n)=<p>; N_{p v}$ is the number of cases observed in $D$ in which $\operatorname{Par}(n)=<p>$ and $n=v$; and $\alpha_{p}$ and $\alpha_{p v}$ are derived from prior probabilities for these combinations of values and, under our prior assignments, are extremely small (see Section 3.3 and Heckerman et al. (1995)). The closed form for the Bayesian metric is

$$
\begin{aligned}
& \operatorname{Pr}\{D \mid G, \text { prior }\} \\
& \quad=\int \operatorname{Pr}\{D \mid \Theta\} \times f(\Theta \mid G, \text { prior }) d \Theta \\
& \quad=\prod_{n} \prod_{p} \frac{\Gamma\left(\alpha_{p}\right)}{\Gamma\left(\alpha_{p}+N_{p}\right)} \prod_{v} \frac{\Gamma\left(\alpha_{p v}+N_{p v}\right)}{\Gamma\left(\alpha_{p v}\right)}
\end{aligned}
$$

where
$\Gamma$ is the Gamma function;
$n$ ranges over the nodes in $G$;
$p$ ranges over values $<p>$ of $\operatorname{Par}(n)$ for the node $n$ fixed by the outermost $\Pi$;
$v$ ranges over the values of the node $n$ fixed by the outermost $\Pi$; and
$\alpha_{p}, \alpha_{p v}, N_{p}, N_{p v}$ are as defined above, with respect to the node $n$ fixed by the outermost $\Pi$.

The above expression for $\operatorname{Pr}\{D \mid G$, prior $\}$, which assumes a Dirichlet prior, is known as the $B D$ (BayesianDirichlet) metric. (Technically, the $B D$ metric is more commonly defined in terms of the joint posterior probability $\operatorname{Pr}\{D, G \mid$ prior $\}$, which is simply the above expression multiplied by the network prior $P(G)$.)

Further simplifying the computational task is the observation that the scoring function is decomposable; it can be expressed as the product of scores over the nodes, where a node's score depends only on its parent set. In our restricted context of classification, this means we can ignore the score of every node except the label, effectively using the $B D$ metric as an evaluator of potential parent sets. More precisely, the $B D$ evaluation of a parent set $\operatorname{Par}(C)$ is node $C$ 's contribution to the $B D$ score of any Bayesian net containing this subgraph. In particular (in contrast to a Naive Bayesian classifier, in which there must be no edges between genes), the decomposability of the $B D$ score allows the hypothesis represented by parent set $\operatorname{Par}(C)$ to be evaluated in isolation of the question of what other edges may exist in the network. Similarly, since the expectation of interest depends only on frequencies of node $C$ and of its parent set, the remainder of the network can be ignored in our context.

# 3.3. Specification of Priors 

In each of the experiments reported, we choose an uninformed prior over the distributions that can be associated with any given network structure. In particular, we employ an extremely small equivalent sample size (Heckerman et al., 1995) of 0.001 , and assign each joint combination of variable values equal probability. There then is a simple translation of this prior to priors over the possible conditional distributions in any given network structure, yielding the $\alpha_{p v}$ and $\alpha_{p}$ values appearing in expression (3). Our choice of prior minimizes its impact on posterior calculations, allowing the data to dominate.

The network structures $G$ are assigned a uniform prior also, but after various prunings (see Section 4) have been imposed. In the context of our minimal-knowledge greedy algorithm, a prior which assigns equal probability to each DAG in which the class label has $\mathcal{M}$ or fewer parents (and zero probability to all other DAGs) is used, for some specified maximum cardinality choice $\mathcal{M}$. In the context of the external gene selection algorithms, a prior which assigns equal probability to each DAG in which the class label has $\mathcal{M}$ or fewer parents, each of which is a member of the selected set of genes (and zero probability to all other DAGs), is used.

Current research is considering how various types of expert biological information can be incorporated into priors and utilized by our methods. This is an area we believe to be critically important to future advances.

### 3.4. Binning Issues

Though Bayesian nets can be utilized to represent continuous distributions, most Bayesian net procedures assume that the random variables take on only a small number (e.g., 2 or 3 ) of discrete values. This requires procedures to discretize (i.e., collapse) typically continuous gene expression values. We describe in Section 4 the two relatively simple approaches we have used with our current search procedures. The first method bins expression values into "low," "medium," and "high" based on the distance of a particular expression value from the gene's mean expression value. The second method is more closely coupled with our external gene selection method and produces a binary binning based on a maximal "point of separation" in the training data between the classes.

While these simple methods have produced good classification results, we point out here that there are many interesting avenues of research in which the binning procedure is more integrated with the search for good Bayesian nets, and candidate binnings are evaluated in the same framework as are other aspects of the nets (see, for example, Fayyad (1993) and Friedman and Goldszmidt (1996a)). We consider this to be an important avenue

for future research.

# 3.5. A Multi-Parent-Set Classifier 

We have indicated how a parent set of the class label corresponds to the relevant (for classification) subgraph of a Bayesian net and, with expression (2), how the class distributions associated with each parent set in a collection of parent sets are combined by means of the $B D$ scoring metric. Our method then is to build a classifier from some number $\mathcal{P}, S$ of parent sets that score high under the $B D$ metric. That is, we perform some form of search (see the next section), selecting the $\mathcal{P}, S$ top scoring parent sets, and these are the sets whose distributions contribute the terms for our approximation of the expression (2). We see from expression (3) that the individual probabilities contributed are simply of the form $\left(\alpha_{p v}+N_{p v}\right) /\left(\alpha_{p}+N_{p}\right)$.

An important phenomenon results from the sparseness of the data, especially in the high dimensional space of microarray data. It is possible that the combinations of values appearing in $q\left[\right.$ par $\left._{i}\right]$ for some of the parent sets $\mathrm{par}_{i}$ are not seen in training or seen only minimally (for example, one or two occurrences). The distributions yielded by such nets will then reflect only the prior, which (as we shall generally assume) is uninformed, yielding equal class probabilities, or will be determined by the handful of training cases with this par ${ }_{i}$ combination. It is important to note that this is the correct posterior distribution under the hypothesis of this parent set and given current knowledge and should not be interpreted as a "weak" or "missing" distribution simply because it is based on a small or empty sample. The strength of this distribution as it contributes to (2) is determined solely by the $B D$ fit. A dispersed distribution (e.g., uniform) learned from a small sample and a peaked distribution learned from a large sample contribute their expectation in the same way, their relative contributions to the posterior affected only by their $B D$ fit. ${ }^{6}$

Is it appropriate to treat the sparse-sample based distributions on equal footing with large-sample based distributions? We consider the variance of the distribution. Variance reflects, among other characteristics, how much the distribution may be expected to change if more data is observed. In the case of high variance, it is not unlikely that new data will shift the distribution dramatically.

The variance of the posterior $\operatorname{Pr}\left\{C=c_{k} \mid \operatorname{Par}(C)=<p>, G, D\right.$, prior $\}$ of a binary-valued class label, being a Dirichlet distribution, is

$$
\left(\operatorname{Pr}\left\{C=c_{k} \mid \operatorname{Par}(C)=<p>\right\} \times\left(1-\operatorname{Pr}\left\{C=c_{k} \mid \operatorname{Par}(C)=<p>\right\}\right)\right) /\left(\alpha_{p}+N_{p}+1\right)
$$

So, an interpretation is, when the "sample size" $N_{p}$ is small, or when the probability is spread evenly across the classes, variance is relatively high, and the distribution is possibly "unstable" in the presence of additional observations. While the posterior distribution it yields is undeniable given the current state of knowledge, it is not unlikely to change dramatically given new data. In this sense, it is less "reliable".

We have experimented with two heuristics for adjusting a parent set's contribution to the evaluation of a query case in order to address the issue of the variance of the distribution. Note that unlike a set's $B D$ score, which is used in parent set selection as well as for a weight in the posterior computation (2), this adjustment is query specific, reflecting the amount of variance $\operatorname{var}(q)$ in the distribution of a particular query $q$ 's (unknown) label. The two adjustments considered are:

- When evaluating a query $q$, set to zero the weight in (2) of any parent set $\mathrm{par}_{i}$ such that $q\left[\mathrm{par}_{i}\right]$ has no occurrences in the training sample. Then renormalize the remaining $B D$ weights to sum to 1 .
- Generalize the above so that $1 / \operatorname{var}(q)$ is the adjustment factor of each set $\mathrm{par}_{i}$, and then renormalize $B D / \operatorname{var}(q)$.

[^0]
[^0]:    ${ }^{6}$ Though peaked distributions which fit a large sample well tend to have better scores than dispersed distributions that fit small samples well.

A variant of the second adjustment strategy, in which an adjustment factor of zero is used when $N_{p}$ is zero, improved performance in cross validation experiments on the gene data training sets by preventing a large number of parent sets, each yielding few observations on a query case, from unduly influencing the classification. This method is what is used in the experiments reported in this paper. More sophisticated adjustments tied to Bayes risk are the subject of current research.

# 4. Search 

The research presented in the following sections explores two alternative methods of building the type of Bayesian classifier described in the previous sections.

The first method utilizes minimal prior knowledge regarding good parent sets for the class label and, within the Bayesian net framework, performs a simple greedy search over the entire set of genes to construct $\mathcal{P S}$ good parent sets. The second method utilizes gene selection external to the Bayesian net framework to produce a small set $S$ of "good genes" (like the informative genes of Ben-Dor et al. (2000) and Ben-Dor et al. (2001)), and then, within the Bayesian net framework, performs an exhaustive search of this set to find the best $\mathcal{P S}$ subsets of $S$ (each subset up to a specified maximum cardinality $\mathcal{M}$ ).

### 4.1. Minimal-Knowledge Greedy Building Methods

This family of methods ignores essentially all prior knowledge, including, in the experiments reported here, prior knowledge of which genes are "control" or "housekeeping" genes, which expression values are deemed reliable (in particular, as indicated by the $P, M$, and $A$ values in Affymetrix data), and biologically known relationships between genes. We do utilize a biological "prior" that deems it likely that only a small number of genes is necessary to classify the cases, that is, that only a small number of genes is required to render the class label conditionally independent of the remaining genes. This biological prior is necessary for any frequency-based classification method to go forward, due to sample size issues, and makes both the greedy and exhaustive searches computationally feasible. This prior is in fact supported by experiments with the current data sets in which performance-both $B D$ and our actual classification rates-begins to diminish after a cardinality of roughly $>6$. This is not quite conclusive proof, as improvement might follow disimprovement (e.g., as is exploited by simulated annealing), but this seems unlikely, especially in light of sample size issues (e.g., statistically meaningful numbers of observations of any combination of more than six gene's expression levels is unlikely).

The version of greedy employed here proceeds in the following manner. On a designated training set (see details of the methodology in Section 5.1):

1. Use some algorithm to bin the gene expression data.
2. Determine a number $\mathcal{K}$ of seeds, a number $\mathcal{P S}$ of parent sets, and a maximum cardinality $\mathcal{M}$ for the parent sets.
3. Select $\mathcal{K}$ seed genes, based on some "goodness" criterion.
4. For each seed gene $g_{\text {seed }}$,
a. Initialize the parent set to the singleton set $\left\{g_{\text {seed }}\right\}$. Consider the parent set $\left\{g_{\text {seed }}\right\}$ for inclusion in the list of the best $\mathcal{P S}$ parent sets evaluated so far.
b. Iteratively build the set to cardinality $\mathcal{M}$ by adding one gene $g$ at a time, chosen from the universe of all genes to maximize the $B D$ score of $\{$ current set $\} \cup\{g\}$. Consider each such parent set $\{$ current set $\} \cup\{g\}$ for inclusion in the list of the best $\mathcal{P S}$ parent sets evaluated so far, resulting in the inclusion of zero or more of these parent sets $\{$ current set $\} \cup\{g\}$. The single best of these extensions to the previous \{current set\} then becomes the new current parent set and is similarly extended at the next

iteration. Continue iterating until parent sets of cardinality $\mathcal{M}$ genes are evaluated and considered for inclusion in the list of the best $\mathcal{P S}$ parent sets evaluated so far.
5. Construct a $\mathcal{P S}$-parent-set Bayesian net classifier from the list of selected parent sets (each of cardinality between 1 and $\mathcal{M}$ ) as described in Section 3.5.

In Section 5.1, we specify the binning and seed selection methods used in the experiments reported in this paper.
Note that every set the greedy method evaluates, starting from each of its seeds, is a candidate for ultimate selection as one of the $\mathcal{P S}$ parent sets-even those sets of smaller than the maximum cardinality $\mathcal{M}$. In particular, at every iteration, in going from cardinality $c$ to $c+1$, every extension of the best parent set of cardinality $c$ gets a chance to be on the list of top parent sets. Consequently, some seeds may contribute more than one parent set; others may not contribute any parent sets at all.

This simple greedy method was implemented initially as a proof of concept; we suspected it would have many flaws and that we would soon replace it with more sophisticated search methods. However, it performed surprisingly well, as is attested to by both the $B D$ scores of the best sets it finds and by the performance on our cross validation tests of the classifiers it produced (see the results in Section 5). This is not to say that avenues of potential improvements are not apparent. For example, there often is a great deal of overlap in the membership of the parent sets produced. Two or three genes tend to be present in a large fraction of the $\mathcal{P S}$ parent sets selected. This is not necessarily a problem, but it might indicate that a nonrepresentative subspace of the set of all possible parent sets is being searched. As is discussed in Sections 5.2 and 5.4, this effect could explain why a relatively small number of high quality parent sets are found by the algorithm.

An alternative heuristic search would mimic classical integral approximation techniques (Gander and Gautschi, 2000). In a similar learning context (Helman and Bhangoo, 1997; Helman and Gore, 1998), we employ with some success a Monte Carlo sampling method to approximate an integral representing Bayes risk. Such methods are designed to approximate an integral by sampling from regions in proportion to the amount of density contained in the region and may be adaptable to the current approximation problem. Additionally, we will consider utilizing the more sophisticated MCMC averaging techniques (Han and Carlin, 2000; Madigan and York, 1995) in this context.

# 4.2. External Gene Selection Methods 

A second family of methods utilizes gene selection algorithms that have been developed in other contexts. This is both a promising approach to the classification problem and is indicative of how the Bayesian framework can be used to incorporate expert prior knowledge of a variety of types. As is the case with the minimal-knowledge greedy methods, we currently do not utilize prior domain knowledge about the genes; such information may, however, be discovered by our external gene selection and normalization methods and then incorporated into the framework in the form of gene selections, normalization, and binning.

The objective of external gene selection is to identify a small set of genes from which good parent sets can be constructed within a Bayesian net search procedure. By severely limiting a priori the size of the universe of genes to be searched for good parent sets and the maximum cardinality of the resulting parent sets, an exhaustive search for the $\mathcal{P S}$ best parent sets (under the $B D$ metric) can feasibly be performed. Thus, whereas the greedy method described in the previous section heuristically builds $\mathcal{P S}$ good subsets of the universe of all genes, the external method finds the $\mathcal{P S}$ best subsets of an intelligently restricted universe of genes.

We are studying a number of different methods for selecting genes whose expression values are strong indicators of a case's classification. The results reported in this paper are based on a strategy that computes a separation quality value for each gene and orders the genes accordingly. We then, for example, can select the genes that are the best separators.

Our separation measure is similar to Ben-Dor's TNoM score, described in Ben-Dor et al. (2000) and Ben-Dor et al. (2001). Both methods consider partitionings of the cases into two sets; the difference between the two

methods is in how the partitions are evaluated. Where TNoM compares the number of cases from each class in each of the two partitions, we account for the sizes of the two classes by comparing the fraction of cases from each class. The two methods can result in different gene selections, and we claim that the relative score is well justified when, for example, the underlying classes differ significantly in size. We have experimented with both measures and don't find either to be uniformly better than the other. Consequently, for a given application, we currently allow experimental cross validation results against a training set to guide our choice of measure.

Let $E_{1}, E_{2}, \ldots, E_{n}$ be the expression values for a given gene across the $n$ cases of a training set, and let $L_{1}, L_{2} \ldots L_{n}$ be the corresponding class labels. Without loss of generality, we assume that the expression values are ordered $E_{1} \leq E_{2} \leq \ldots \leq E_{n}$ so that $L_{i}$ is the class label of the $i^{\text {th }}$ smallest expression value. The separation quality value of a gene is intended to indicate to what extent identical class labels are grouped together in $L_{1}, L_{2}, \ldots, L_{n}$ as a consequence of the ordering of the $E_{i}$ values. Separation is considered to be perfect, for example, if the $L_{i}$ labels are completely "sorted".

Under the assumption that there are exactly two class labels, $A$ and $B$, we compute separation quality as follows. Let $\operatorname{Acount}(i)$ be the number of $A$ labels in $L_{1}, L_{2} \ldots, L_{i}$, and let $\operatorname{Bcount}(i)$ be the number of $B$ labels in $L_{1}, L_{2} \ldots, L_{i}$. For each position $0 \leq i \leq n$, we can quantify the relative separation of the class labels if we were to split into the two sets $L_{1}, L_{2}, \ldots, L_{i}$ and $L_{i+1}, L_{i+2}, \ldots, L_{n}$ :

$$
\operatorname{Separation}(i)=\left|\frac{\operatorname{Acount}(i)}{\operatorname{Acount}(n)}-\frac{\operatorname{Bcount}(i)}{\operatorname{Bcount}(n)}\right|
$$

We then define separation quality to be the best of these values:

$$
\text { SeparationQuality }=\max _{1 \leq i \leq n} \operatorname{Separation}(i)
$$

Genes can be ordered by their SeparationQuality values, so we can talk about the $k$ best or the $k$ worst separators. The computed values have the following properties.

- $\operatorname{Acount}(0)=\operatorname{Bcount}(0)=0$
- Bcount $(i)=i-\operatorname{Acount}(i)$, for $0 \leq i \leq n$
- Separation $(0)=\operatorname{Separation}(n)=0$
- SeparationQuality $=1$ indicates perfect separation.
- SeparationQuality necessarily is $>0$, since Separation(1) is $1 / \operatorname{Acount}(n)$ or $1 / \operatorname{Bcount}(n)$, depending on whether $L_{1}$ is $A$ or $B$, and we take the maximum of the Separation values.
- We get the same SeparationQuality value if we define Acount and Bcount in terms of $L_{i+1}, L_{i+2}, \ldots, L_{n}$ instead of $L_{1}, L_{2} \ldots, L_{i}$.

We note that if the gene expression values are not distinct, then the ordering of $E_{i}$ values is not unique, and the computed separation quality value will depend on the procedure used to break ties. We are considering a number of ways to pin down the ordering in the case of ties-specifically, to determine an appropriate separation quality value. We currently break these ties arbitrarily.

In addition to computing a separation quality value, we can use the same computation to propose a binning of each gene's expression values into two bins. Let max be the $i$ value that maximizes Separation(i), and compute

$$
\text { BinValue }=\frac{E_{\max }+E_{\max +1}}{2}
$$

which is a gene expression value that lies between the separated $E_{i}$ values in the best separation. The computed BinValue can be used as a boundary between bins.

We note that the maximizing $i$ value is not necessarily unique, even if the $E_{i}$ values are distinct; we currently break these ties arbitrarily. We also note that $L_{\max }$ and $L_{\max +1}$ necessarily are different labels; otherwise, SeparationQuality could be increased by increasing or decreasing max by 1.

This binning strategy is motivated by a prior belief, shared by many domain experts, that a gene is wellmodeled as a binary switch. This belief appears to be supported by preliminary analyses against the data sets considered here, as well as against additional data sets (Mosquera-Caro et al., 2003a; Mosquera-Caro et al., 2003b) reported elsewhere. The method whose analyses are for setting bin boundaries described above is quite natural, as it selects a point yielding bins that maximally distinguish the classes (with respect to SeparationQuality), and thus is highly analogous to the boundaries suggested by Ben-Dor's TNOM-based method. The binning procedure also is similar to the initial binning policy of the procedures described in Fayyad (1993) and Friedman and Goldszmidt (1996a)—though they consider a variety of policy evaluation metrics-in which an initial binary binning is heuristically refined into a finer-grained discretization. We have conducted extensive experiments (Ding, 2003) using each of the $M D L$ and $B D$ evaluation criteria to determine stopping conditions for refinement, and, for a large fraction of genes (i.e., $>90 \%$ of the genes on the Princeton data set), refinement of the initial binary binning is not supported by these measures. Section 5.1 describes an alternative tertiary binning strategy we considered in the context of the uninformed greedy method.

# 4.3 Preprocessing the Data (Normalization) 

One of the advantages of the Bayesian approach is that it provides a natural mechanism to account for special domain knowledge in the construction of a classifier. Nevertheless, in our first round of experiments, we are focusing on the gene expression data, making use of minimal prior knowledge. One of the issues we are addressing in this simplified context is the preprocessing (normalization) of gene expression data before the application of our classification procedures. Because of variabilities in gene expression measurements and uncertainties about the processing done by the tools used to generate the data, ${ }^{7}$ we decided to include the effect of normalization as part of our studies. Specifically, for each data set we study, we attempt to learn via cross validation the most effective of a family of normalization parameters.

Our approach to normalization is to consider, for each case, the average expression value over some designated set of genes, and to scale each case so that this average value is the same for all cases. This approach allows our analysis to concentrate on relative gene expression values within a case by standardizing a reference point between cases. For example, if the expression value within a case of certain genes $g_{i}$ relative to the expression value of some reference point gene $g$ is an effective class discriminator, then it suffices simply to consider these $g_{i}$ values, provided cases have first been normalized to a common $g$ value. The key difference between the normalization strategies we considered is the choice of the reference point gene $g$, or, more generally, the choice of a set $R$ of reference point genes. While selecting an appropriate set $R$ could provide a good opportunity to take advantage of special knowledge of the underlying domain, consistent with our desire to focus first on raw data in the absence of prior knowledge, we use here a simple selection method based on the SeparationQuality value already discussed. In particular, we set $R$ to be the $k$ worst separators-that is, genes with the lowest SeparationQuality values-for some number $k$. The motivation for this choice of $R$ is that, as our experiments indicate, a suitable reference point can be found as the average of the expression values of genes that are independent of the class label for which we are trying to develop a classifier. Further, normalizing with respect to such genes will not discard information that might be valuable in class discrimination. Choosing the $k$ worst separators for normalization is a heuristic for identifying genes likely to be independent of the class label. While many factors (e.g., noise) could mislead this measure into selecting inappropriate reference point genes, it seems reasonable that, in the absence of additional information, genes that appear in the data to be bad separators are good candidates to serve as reference point

[^0]
[^0]:    ${ }^{7}$ Affymetrix Microarray Suite (MAS) Version 4.0.

genes. Indeed, our experimental results support this as a reasonable normalization strategy.
In summary, the normalization algorithm we used is as follows.

1. Let $R$ consist of the $k$ worst separator genes, as described above.
2. Let $A$ represent the target average value for the genes in $R ; A$ may be chosen arbitrarily, since its value does not affect any aspects of the computation.
3. For each case $C$,
a. Compute the average value, $A v e_{R, C}$, of the expression values in case $C$ for the genes in $R$.
b. Multiply every expression value of case $C$ by the scaling factor $A / A v e_{R, C}$.

We took $k$ to be a parameter to be learned in the course of training and experimented with several different values accordingly. The results of these experiments against training data are reported in Section 5.3; Section 5.4 reports how well a choice of $k$ made against training data generalizes to an out-of-sample test set.

# 5. Results 

The MIT leukemia data (Golub et al., 1999) and the Princeton colon cancer data (Alon et al., 1999) are considered. The MIT data consists of 7,129 gene expression values per case. The Princeton data is provided in a heavily pruned form, consisting of only 2,000 genes per case.

### 5.1. Experimental Methodology

In order to avoid any possibility of overfitting our results to specific data sets, we set aside from each data set a fraction of cases, forming a test set. For the MIT data set, a partition into 38 training cases and 34 test cases (our set aside, out-of-sample cases) is provided on the MIT Web site. The Princeton Web site provides a single data set of 62 cases. We randomly partitioned this data set into 38 training cases and 24 set aside test cases. The test sets were not examined at all in the course of algorithm development, nor to establish parameter settings, and were considered only after our best methods, along with their parameter settings, were identified through a cross validation methodology (detailed below) on the training sets. Results of our best method-as identified against the training sets only—run against the set aside test sets are reported in Section 5.4.

We now describe the cross validation methodology that was applied to the 38 -case training sets in order to develop our methods and to indicate which techniques would be the most promising to pursue. In particular, our initial evaluation of a classifier building method under development employed "leave one out" ( $L O O$ ) cross validation. On each experiment, a method would train on 37 cases, building a classifier to be used to classify the single left out query case; the build/evaluate cycle is repeated 38 times, once for each "fold" created by leaving out of the training a different query case.

Care must be taken during development that the methods used in the classifier construction process not exploit any knowledge of the left out query case it is to be evaluated on. That is, any method applied to build the classifier must be applicable when we turn attention to the set aside test set (or to an actual set of query cases for which a classification is desired), at which time knowledge of the query's class label, of course, is unavailable.

This requirement implies, for example:

- Gene selection by external means must be repeated on each of the 38 folds, without being exposed to the left out case to be used as a query in the evaluation.
- Similarly, if normalization or binning is to use label knowledge, it must not be exposed to the left out case, and hence must be repeated for each fold. If, however, a binning algorithm does not use knowledge of labels

(as is the case of the algorithm used in connection with the greedy construction), it may inspect the entire training set, since in an actual classification application, the binning algorithm could inspect the non-label fields (genes) of the cases to be classified at the time these cases are presented for analysis.

# Greedy Parent Set Construction 

The LOO cross validation setup for the greedy method takes the following form:

1. Let $T$ represent the full training set (e.g., of 38 cases).
2. Bin $T$, without using label knowledge.
3. For each $q_{i} \in T$, define fold $F_{i}=\left(T-\left\{q_{i}\right\}\right)$,
a. Select $\mathcal{K}$ seeds against $F_{i}$.
b. Use the greedy method to construct $\mathcal{P S}$ good sets (under $B D$ ) up to cardinality $\mathcal{M}$ against $F_{i}$, starting from each seed.
c. Compute the variance in each set's induced distribution of $q_{i}$ 's unknown label, and adjust the $B D$ score of each set to form a $\mathcal{P S}$-set classifier.
d. Classify $q_{i}[C]$ as the most likely value, given $q_{i}[$ genes $]$ under the classifier's distribution.
e. Compute the error and uncertainty in the classification for fold $F_{i}$.
4. Report the average error and uncertainty rates across the folds.

The information reported in Step 4 is derived from the constructed classifiers' induced distributions. In particular, the classifier constructed for each fold $F_{i}$ specifies a conditional posterior distribution $\operatorname{Pr}\{q[C]=c_{k} \mid q[$ genes $]=<$ $e>\}$ for a query case's class label. In the current experiments, the class label is binary, and $q$ is classified as belonging to the class with higher posterior; if value $=0.5$, no classification is possible. An error occurs if $q[C]$ is the lower probability class. The TER (total error rate) values reported in Tables 3-6 are based on the combined number of misclassifications and no classifications.

Uncertainty is a measure of the strength of a classification. If $\operatorname{Pr}\left\{q[C]=c_{k} \mid q[\right.$ genes $\left.]=<e>\right\}$ is near 1.0, the classification is strong, whereas if it is near 0.5 , it is weak. On each fold, we compute the "probability of error" as well as the $0 / 1$ misclassification indicator. In particular, probability of error is given by (1.0 - (the probability the classifier assigns to the true class $q[C]$ ) ). The APE (average probability of error) values reported in Tables $3-6$ are averages over this quantity.

For the experiments reported in Section 5.2 and 5.4, we utilized the following relatively simple binning (Step 2) and seed selection (Step 3.a) techniques.

Binning: As is indicated in Section 3.1, practical Bayesian net methods require a discretization of the expression values. Following many gene expression researchers, we partition values into three ranges: "under-", "average-", and "over-" expressed. Our partitioning method for greedy creates a tertiary binning for each gene $g$ as

$$
\begin{gathered}
\left(-\infty,(\text { mean }(g)-n_{\text {low }} \times \sigma(g)\right) \\
{\left[\text { mean }(g)-n_{\text {low }} \times \sigma(g), \text { mean }(g)+n_{\text {high }} \times \sigma(g)\right]} \\
\left(\text { mean }(g)+n_{\text {high }} \times \sigma(g), \infty\right)
\end{gathered}
$$

where the mean mean $(g)$ and standard deviation $\sigma(g)$ of each gene's $g$ expression values are computed over all cases. The choices of $n_{\text {low }}$ and $n_{\text {high }}$ are made through experimentation on the training data. Once selected, these

are fixed and used without modification on the set aside test data; otherwise, we would run the risk of overfitting to the data. For the MIT data, setting $n_{\text {low }}=n_{\text {high }}=1.0$ worked well, and there was little sensitivity in the cross validation results. In the Princeton data, there was far more sensitivity in the cross validation, and a limited search arrived at the settings $n_{\text {low }}=1.25$ and $n_{\text {high }}=0.4$. Subsequent analysis indicates that a more extensive search for these parameter settings often results in overfitting to the data. In fact, it appears that the tertiary binning considered here is generally inferior to the binary binning described in Section 4.2 in conjunction with the external gene selection methods.

Seed selection: Singleton parent sets $\{\mathrm{g}\}$ are formed for each gene $g$ and the $B D$ score obtained. The genes corresponding to the $\mathcal{X}$ highest scoring parent sets are used as seeds.

# External Gene Selection Plus Exhaustive Parent Set Construction 

The LOO cross validation setup for external gene selection takes the following form:

1. Let $T$ represent the full training set (e.g., of 38 cases).
2. For each fold defined by $F_{i} \equiv\left(T-\left\{q_{i}\right\}\right)$,
a. Use an external method against $F_{i}$ to normalize expression values and select a set $S$ of $\mathcal{N}$ genes.
b. Bin $F_{i}$, possibly using information returned by gene selection.
c. Exhaustively search the set $S$ for the best $\mathcal{P S}$ subsets (of cardinality up to $\mathcal{M}$ ) under the $B D$ scoring metric.
d. Compute the variance in each set's induced distribution of $q_{i}$ 's unknown label, and adjust the $B D$ score of each set to form a $\mathcal{P S}$-set classifier.
e. Classify $q_{i}[C]$ as the most likely value, given $q_{i}[$ genes $]$ under the classifier's distribution.
f. Compute the error and uncertainty in the classification for fold $F_{i}$.
3. Report the average error and uncertainty rates across the folds.

In our experiments, we employed the external gene selection, normalization, and binning methods described in Section 4.2. In particular, the external gene selection algorithm is invoked on each fold with the following effect:

- The algorithm normalizes the cases in $F_{i}$ using the $k$ genes with the lowest SeparationQuality as controls.
- The algorithm returns the $\mathcal{N}$ genes with the highest SeparationQuality.
- The algorithm returns a binary bin boundary for each selected gene, corresponding to where the maximum separation value is obtained.

Once results of the external gene selection algorithm are returned for a fold, an exhaustive search is performed (on a normalized and binned $F_{i}$ ) for the best $\mathcal{P S}$ parent sets, from which the Bayesian net classifier is formed.

Note that the instantiation of the steps of either methodology with specific algorithms defines a classifier building method. When run on a specific training set (or fold of a training set), it yields a $\mathcal{P S}$-set classifier, which in turn yields a posterior class distribution. This distribution can then be used to classify query cases with unknown labels, assuming that the query cases are drawn from the same distribution which underlies the training

set. We emphasize that it is the building method, not the particular classifiers built on a run against a training set (or fold of a training set), that is being assessed.

# 5.2. Cross Validation Results with Greedy 

In tests of the greedy method, we studied the effects of varying the number $\mathcal{P S}$ of sets used in the classifier. We held fixed at $\mathcal{M}=5$ the maximum cardinality and, due to computational considerations, the number of seeds at $\mathcal{R}=60$.

The following two tables summarize, respectively, results with the Princeton and MIT training sets. Each row of the tables summarizes, for a fixed $\mathcal{P S}$, the LOO cross validation test results for the 38 cases of the respective training set. The table entries MIS, ERR, and TER tally the number of misclassifications and nonclassifications as described in the legand below. APE-average probability of error per fold-captures the uncertainty in the classifications. Since the classification is based on the posterior probability of a class, a posterior near 1.0 or 0.0 is a confident prediction (which may be either correct or incorrect), while a posterior near 0.5 is a prediction with low confidence (when the posterior is approximately 0.5 , no classification is made). The error in a prediction is 1.0 minus the posterior probability assigned by the classifier to the true class, and APE is the average over these errors. The $q$ Max result appearing at the end of each table is discussed below.

Legend:
$\mathcal{P S} \quad$ Number of parent sets used.
APE : Average probability error per fold.
MIS : Number of misclassifications.
$E R R$ : Total error count (misclassifications + nonclassifications).
$T E R$ : Total error rate (including both misclassifications and nonclassifications).


Table 1. Princeton training data ( $n_{\text {low }}=1.25, n_{\text {high }}=0.4$ ).


Table 2. MIT training data $\left(n_{\text {low }}=1.0, n_{\text {high }}=1.0\right)$.

The tables indicate an initial increase in quality as $\mathcal{P S}$ increases, then a leveling off and ultimate decrease in quality. The most interesting result is the significant increase in quality over just a single set ( $\mathcal{P S}=1$, the maximum a posteriori solution), which is a prevalent Bayesian net methodology for learning distributions. As predicted from the discussion in Section 3.3, a single parent set does not provide adequate coverage of gene expression combinations in the query case, leading to a large number of non classifications.

To establish that the polling effect noted in Section 3.3 is real and significant, we also conducted experiments labeled " $q$ Max". Here, 500 sets are built as with $\mathcal{P S}=500$, but for each query case $q$, the single parent set with the highest variance adjusted score is used to classify $q$. Note that this query-specific set selection from the 500 always selects (if available, which is the case in all our cross validation runs) a set in which $q$ 's combination of expression values appears in the training set, eliminating the no-classification errors. That this method underperforms the best $\mathcal{P S}>1$ methods indicates that the blending of distributions contributes to the quality of the classification. Examination of the details of the computations performed by the classifier also indicates that, in many cases, the distributions induced by the parent sets exert competing effects on the classification, and that the weighting resolution generally leads to a correct classification.

We speculate that the degradation in classification quality for $\mathcal{P S}$ above a threshold is caused by the potentially unrepresentative search performed by our simple greedy algorithm, as alluded to in Section 4.1-greedy, being unable to construct enough high scoring sets, must "fill" the classifier with many low scoring (and, hence, worse fitting to the observational data) sets which contribute inaccurate distributions. This explanation is supported by the near monotonic increase in quality reported in Section 5.3 for the exhaustive search following external gene selection. This suggests that refinements to greedy as proposed in Section 4.1 could well obtain overall improvements, especially as is noted in Section 5.4 when we discuss the results of the greedy-built classifiers against the out-of-sample test set.

# 5.3. Cross Validation Results with External Gene Selection 

In tests of the external gene selection methods, we studied the effects of varying both $\mathcal{P S}$ and the fraction $\mathcal{W}$ of genes used as controls in normalization. As with greedy, we held fixed the maximum cardinality $\mathcal{M}$ at 5 . For computational reasons, the number of genes selected was fixed at 30 .

The following two tables summarize, respectively, results with the Princeton and MIT training sets. Each row of the tables summarizes, for a fixed $\mathcal{W}$ and $\mathcal{P S}$, the LOO cross validation test results for the 38 cases of the respective training set. As is the case for Tables 1 and 2, the $q$ Max result at the end of each of Tables 3 and 4 is for 500 available parent sets and with $\mathcal{W}$ set at a value which produced generally good results across the $\mathcal{P S}$ values for the multi-set classifiers.

Legend:
$\mathscr{P S} \quad:$ Number of parent sets used.
$\mathscr{W} \quad:$ Fraction of genes used as controls for normalization.
APE : Average probability error per fold.
MIS : Number of misclassifications.
$E R R$ : Total error count (misclassifications + nonclassifications).
$T E R$ : Total error rate (including both misclassifications and nonclassifications).


Table 3. Princeton training data.


Table 3. Princeton training data (continued).


Table 4. MIT training data.


Table 4. MIT training data (continued).

Unlike the case for greedy selection, the results of Tables 3 and 4 demonstrate that there is a steady improvement for the Princeton data as $\mathcal{P} S$ increases, and near flat behavior for the MIT data for $\mathcal{P} S \geq 60$. Again, the $q$ Max experiments (for the Princeton data) and inspection of the detailed results provide further evidence that the blending provided by a large number of parent sets has a positive impact on classifier quality.

The tables indicate different best values across the two training sets for the fraction $\mathcal{W}$ of control genes used in expression-level normalization, and a greater sensitivity to this value in the Princeton training data. This may be indicative of differences in experimental conditions, analysis preprocessing, and so forth. That we can, without the benefit of descriptive procedural information as input, discover through methodical application of cross validation good normalization parameters for each data set is a significant finding. The results against the test set presented in the following section indicate that these findings are not simply an overfitting to the training data, but truly a learning of the underlying processes that generalizes well.

# 5.4. Out-of-Sample Test Set Results 

Only after running the above experiments on the training sets did we turn attention to the test sets. Our primary interest is to select the single method which performed best (lowest total error rate, $T E R$ ) in the cross validation experiments and assess its classification rate on the out-of-sample test sets. In this way, we avoid a "selection effect" in which one of several methods run against the test set performs well.

Inspection of the tables of Sections 5.2 and 5.3 identifies the external gene selection method as being preferable to the minimal knowledge greedy method in building parent sets for the Bayesian net classifier. Since we have data from two different experimental contexts, it is proper to select the parameters for the selected method (i.e., $\mathcal{P} S$ and $\mathcal{W}$ ) based on performance in the cross validation trials on each training set; such parameter setting would of course be performed in an actual classification application in which we had access to training, but not query, cases in advance.

## External Gene-Selection Method Against Test Data

Inspection of the tables in Section 5.3 indicates that, against the Princeton training set, the best setting is $\mathcal{P} S=500$ (number of parent sets to be used in the Bayesian net classifier) and $\mathcal{W}=0.55$ (control list fraction for normalization). Against the MIT training set, several parameter settings resulted in the minimal $T E R$ of 0.052632 . Somewhat arbitrarily, we selected $\mathcal{P} S=300$ and $\mathcal{W}=0.85 .{ }^{8}$ Using only these settings, we built the classifiers by training against the 38 cases of each of the two training sets and used the resulting classifiers to classify the cases of the respective test sets.

The results are exhibited in Table 5 and are extremely good. The classifier had nearly identical error rates against the MIT training and test sets ( 0.05 for training versus 0.06 for test) and a significantly lower error rate against the Princeton test set ( 0.16 for training versus 0.08 for test). The results strongly suggest that our multi-parent-set Bayesian net classifiers employing external gene selection and normalization algorithms are able to learn from training data underlying distributions which generalize extremely well to out-of-sample query cases whose classifications are of biological and clinical significance.

## Comparison with Other Published Results

The Appendix contains an extensive compilation of results reported in the literature for the MIT and Princeton datasets, generated using a broad range of classification methodologies. The high accuracies achieved in our results are particularly noteworthy given the stringent nature of our 'one-shot' testing approach: we have used

[^0]
[^0]:    ${ }^{8}$ While we chose our single run to be made against the test set with $\mathcal{P} S=300$ and $\mathcal{W}=0.85$, in order to assess the sensitivity of the results to this somewhat arbitrary choice of settings from among settings achieving equally good TER, we later ran against the test set with several other settings which achieved the same $T E R$ against the training data. The majority of those settings tried also incurred the same number 2 of misclassification errors as those reported here, while a few others incurred 3 misclassifications errors.

parameter settings determined from cross-validation results for the training dataset only, followed by a single pass at classifying the held-out test set. Our results compare favorably even with those obtained using rather less stringent training/testing protocols.


Table 5. Out-of-sample results with external gene selection.

# Minimal-Knowledge Greedy Methods Against Test Data 

After obtaining the results reported in the previous subsection for the external methods, we decided also to run our greedy methods against the test sets. Since the greedy method's results in the cross validation experiments were almost as good as the external gene selection methods, we consider this to be an interesting avenue of research as well. We report the results here in order to indicate potential directions for future work.

Table 6 reports the results against the two test sets of Bayesian net classification using the greedy construction method. The only parameter considered in the cross validation against the training set was $\mathcal{P S}$, with the best settings found to be $\mathcal{P S}=20$ for the MIT training set and $\mathcal{P S}=5$ for the Princeton training set.


Table 6. Out-of-sample results with greedy selection.
Against the Princeton test set, the error rate was similar to the rate against the training set ( 0.18 for training versus 0.25 for test), but it was significantly higher against the MIT test set ( 0.08 for training versus 0.35 for test). We speculate that two sources of this lack of generalization, especially in the MIT data, are our failure to normalize the data for the greedy experiments and the use of an overly rigid binning method. This conjecture is consistent with the high number of "nonclassifications" against the test sets. Note also that the MIT data was provided as two distinct data sets. Procedural differences in experimental preparation and processing of the output between the sets as is described in (Golub et al., 1999) may have hampered the greedy method because it fails to normalize across the sets. In the case of the Princeton data, where a single data set is randomly split, performance against the test set was much more comparable to that of the training set.

Consequently, one avenue of future research is to include in the greedy method a normalization procedure similar to that employed by the external gene selection method. Also, as noted in Section 4.1, there is a concern that the greedy search may not provide a good representation of the space of possible parent sets. We speculated that this might be the cause of the degradation observed in the cross validation experiments for large values of $\mathcal{P S}$. Note that the exhaustive (and, hence, completely representative) search of the universe of externally selected genes resulted in large $\mathcal{P S}$ s performing best. The greedy method's use of small values of $\mathcal{P S}$, in combination with the failure to normalize, certainly contributes to the large number of non-classifications in the test set. Hence, modifying the search to be more representative, as discussed in Section 4.1, potentially could give minimalknowledge searches such as greedy access to more good parent sets, thereby addressing the large number of failure-to-classify errors that were observed.

## 6. Summary and Future Work

We have presented a methodology for applying Bayesian nets to the problem of classifying clinical cases from their gene expression profiles. While Bayesian nets have been applied previously to identify relationships

among genes and have been proposed as classifiers for other problem domains, we have outlined new methods for classification particularly well suited to gene expression data. Through a systematic experimental design, we demonstrated that these classifiers, trained by means of a cross-validation methodology, generalize extremely well to out-of-sample test data. In particular, we achieved error rates of $92 \%$ and $94 \%$ on out-of-sample partitions of the MIT leukemia and Princeton colon cancer data sets, respectively. These results are comparable to or better than those reported previously using other classification approaches, even in those instances when less stringent train/test procedures were utilized.

Our Bayesian net classifiers are built by constructing alternative parent sets for the class label node and use a posterior probability and variance-weighted blending of the resulting distributions. This blending of the distributions induced by the competing hypotheses embodied by the alternative parent sets was seen in our experimental results to yield improvements over the so called maximum a posteriori solution, in which only the single most likely hypothesis is used. We experimented with two methods for searching for good parent sets: a simple greedy search of the universe of all genes and an exhaustive search of a universe of genes selected by a separation heuristic. The latter method produced better performing parent sets in the experiments reported here. This method also employs a novel expression-level normalization scheme based on algorithmically discovered control genes. Current work is considering improvements to both methods for parent set construction and to normalization. We are exploring also how other aspects of the problem-value binning and gene clustering, for example-can be studied within the framework.

It also is possible to incorporate into the model local structure, as described in Friedman and Goldzmidt (1996b) and Chickering et al. (1997). While this has not been necessary for the classification tasks undertaken to date, future work will explore the utility of this model extension in the gene expression domain.

We believe that Bayesian approaches to gene expression analysis, such as those described here and in Friedman et al. (1999), Friedman et al. (2000) and Pe'er et al. (2001), have enormous potential, not simply because of the quality of the results achieved so far, but also because the mathematically-grounded formalism provides the opportunity to expand systematically the range of problems treated, integrating newly developed algorithmic techniques with an ever-increasing base of domain knowledge. Thus, results such as those reported here, while significant in their own right, are only the first steps toward the ultimate construction of rigorous and comprehensive models that promise to be of great scientific and clinical import.

# Acknowledgments 

This work has been supported by grants from the D.H.H.S. National Institutes of Health/National Cancer Institute (CA88361), the W.M. Keck Foundation, and National Tobacco Settlement funds to the State of New Mexico Provided to UNM for Genomics and Bioinformatics. We are grateful for the computational support that has been provided by the UNM High Performance Computing Education and Research Center (HPCERC). We are grateful for the comments of the anonymous referee, which greatly improved this work.

# A. COMPILATION OF PUBLISHED CLASSIFICATION RESULTS 

In this Appendix, we list the feature selection and classification methodologies, testing procedures, and accuracies that have been reported in the literature to date for the two datasets considered in this work. Results for the MIT dataset are given in Table 7, and for the Princeton dataset, in Table 8. Within each table, results are listed in order of decreasing testing protocol stringency (most stringent appear first), and within stringency sub-category, in order of decreasing classification success rate. The stringency hierarchy used to order the results is Separate Train/Test followed by One-Shot Test? followed by \# Features. Due to the varied nature of the classification testing protocols utilized in the literature, the detailed ordering of results in cases where multiple attempts were made is necessarily somewhat arbitrary.

Table 7. MIT dataset.


[^0]
[^0]:    ${ }^{1} 10$-fold cross-validated search; search repeated 50 times with 10,000 iterations each.
    ${ }^{2}$ See [1] for definition, also referred to as Mean Aggregate Relevance (MAR) [10].
    ${ }^{3} 100$ trials of random $36 / 36$ splits; \# of features and testing errors reported for each feature selection algorithm are averages computed over 100 trials.
    ${ }^{4}$ Discriminant analysis methods: (a) FLDA; (b) DLDA; (c) method of [GST99]; (d) DQDA.
    ${ }^{5} 200$ trials of different 48/24 (2:1) train/test splits; testing errors for methods (a)-(d) are for median quartile over 200 trials.
    ${ }^{6}$ Classification tree methods: (a) single CART tree with pruning by 10 -fold cross-validation; (b) 50 bagged exploratory trees; (c) 50 boosted (using $A r c-f s$ ) exploratory trees; (d) 50 bagged exploratory trees with convex pseudodata.
    ${ }^{7}$ Three distinct sets of "top 50 " genes were generated using the NBGR, MVR, and MAR feature selection methods. Testing errors are correspondingly labeled (a), (b), (c).

Table 7. MIT dataset, continued.


[^0]
[^0]:    ${ }^{8}$ The three classes are: B-ALL (38), T-ALL (9), AML (25).

Table 7. MIT dataset, continued.


[^0]
[^0]:    ${ }^{9}$ Leave-one-out classification results are total \# errors for training set only (MIT) and full train+test set (Princeton).
    ${ }^{10}$ Result is average over 5 runs, each with a new classifier constructed for a new sample-shuffled dataset, since the perceptron method is sensitive to sample order.
    ${ }^{11}$ Leave-one-out classification results are total errors for train+test set ( $N=72$, MIT; $N=62$, Princeton).
    ${ }^{12}$ Feature lists are labeled according to the algorithm variant with which they were used (A0, A1, A2). Note that for A2, the values $\mathrm{x}-\mathrm{y}-\mathrm{z}$ correspond to the min-mean-max of the $N$-fold gene re-selections.

Table 7. MIT dataset, continued.


[^0]
[^0]:    ${ }^{13}$ Prior to feature selection and classification, the initial genelists were filtered from $7129 \rightarrow 7070$ (MIT) and $2000 \rightarrow 1998$ (Princeton). For \#genes $=7070$ (MIT) and 1998 (Princeton), no feature selection was performed; however, for convenience, the results are reported together with the feature-selected results for each classification methodology.
    ${ }^{14}$ Testing errors are labeled (a), (b), (c) corresponding to the number of boosting iterations (100, 1000, 10,000 respectively).

Table 8. Princeton dataset.


[^0]
[^0]:    ${ }^{15}$ Random partitioning, 38/24 (see Section 5.1, present work).
    ${ }^{16}$ Random split, 31/31.
    ${ }^{17} 42 / 20$ split, first $42+$ remaining 20 samples.
    ${ }^{18} 50$ trials of different 50/12 splits; testing errors for feature selection algorithm (a)-(d) are averages computed over 50 trials.
    ${ }^{19}$ Five samples (N34, N36, T30, T33, and T36), deemed "likely to have been contaminated" were removed, leaving 57 samples. Three different train/test sets ( $40 / 17$ split) were de fined: (a) original: the first 40 samples were placed in the training set, the remainder in the test set; (b) random: 40 samples were randomly assigned to the training set, the remainder to the test set; (c) discrepant: the last 40 samples were placed in the training set, the rest in the test set. Testing errors are correspondingly labeled (a), (b), (c).
    ${ }^{20}$ Five-fold cross-validation on full $(N=62)$ dataset.
    ${ }^{21}$ [19] also tried a variant gene selection approach, "competitive node splits," but since this method is not explained or referenced in the paper, and gave inferior results, we note only that it was tried (" $a$ " notation under "One-Shot Test") but do not report crossvalidation results.

Table 8. Princeton dataset, continued.


# Key/Notes 

1. Separate train/test $=\mathrm{N} \Rightarrow$ classification is via LOO training on full train+test dataset, followed by classification of the left-out sample.
2. One-shot test $=\mathrm{Y} \Rightarrow$ a single 'best shot' classifier is evaluated against the test set, after having been selected from various possible combinations of classifiers/feature sets developed using the training set only. If at any point in the algorithm (feature selection, $f$, classifier parameter tuning, $p$; classifier algorithm details, $a$ ) the test set is included in the procedure, this is considered to be "One-shot test $=\mathrm{N}$." Test set results for multiple feature sets without an a priori (test-set-blind) method to select among feature sets are reported as $\mathrm{N}(f)$.
3. "Testing errors" should be interpreted as applying to the dataset implied by the "Separate train/test?" column. The errors include actual errors + samples characterized as 'unclassifiable.'
4. Train/test set is Golub et al. 38/34 (MIT) and 62 train+test (Princeton), unless otherwise indicated.
5. Boldface \#genes/error \#s correspond to best results in cases where one-shot test $=\mathrm{N}$, and multiple results are reported.

## Abbreviations


# References 

Alizadeh, A., Eisen, M., Davis, R., Ma, C., Lossos, I., Rosenwald, A., Boldrick, J., Sabet, H., Tran, T., Yu, X., Powell, J., Yang, L., Marti, G., Moore, T., Hudson, J. (Jr), Lu, L., Lewis, D., Tibshirani, R., Sherlock, G., Chan, W., Greiner, T., Weisenburger, D., Armitage, J., Warnke, R., Levy, R., Wilson, W., Grever, M., Byrd, J., Botstein, D., Brown, P., and Staudt, L. 2000. Distinct types of diffuse large B-cell lymphoma identified by gene expression profiling. Nature 403, 503-511.
Alon, U., Barkai, N., Notterman, D., Gish, K., Ybarra, S., Mack, D., and Levine, A. 1999. Broad patterns of gene expression revealed by clustering analysis of tumor and normal colon tissues probed by oligonucleotide arrays. In Proc. National Academy of Sciences USA 96(12), 6745-6750.
Bhattacharjee, A., Richards, W., Staunton, J., Li, C., Monti, S., Vasa, P., Ladd, C., Beheshti, J., Bueno, R., Gillette, M., Loda, M., Weber, G., Mark, E., Lander, E., Wong, W., Johnson, B., Golub, T., Sugarbaker, D., and Meyerson, M. 2001. Classification of human lung carcinomas by mRNA expression profiling reveals distinct adenocarcinoma subclasses. In Proc. National Academy of Sciences 98(24), 13790-13795.
Ben-Dor, A., Bruhn, B., Friedman, N., Nachman, I., Schummer, M., and Yakhini, Z. 2000. Tissue classification with gene expression profiles. J. Computational Biology 7(3,4), 559-584.
Ben-Dor, A., Friedman, N., and Yakhini, Z. 2001. Class discovery in gene expression data. In Proc. 5th Annual International Conference on Computational Biology, 31-38, ACM Press.
Bishop, C. 1996. Neural Networks for Pattern Recognition. Oxford University Press, New York.
Brown, P., and Botstein, D. 1999. Exploring the new world of the genome with DNA microarrays. Nature Genetics 21, 33-37.
Buntine, W. 1991. Theory refinement for Bayesian networks. In Proc. 7th Conference on Uncertainty in Artificial Intelligence (UAI), 52-60, Morgan Kaufmann.
Buntine, W. 1992. Learning classification trees. Statistics and Computing 2, 63-73.
Buntine, W. 1996. A guide to the literature on learning probabilistic networks from data. IEEE Trans. on Knowledge and Data Engineering 8, 195-210.
Cheng, J. and Greiner, R. 1999. Comparing Bayesian network classifiers. In Proc. 15th Conference on Uncertainty in Artificial Intelligence (UAI), 101-108, Morgan Kaufmann.
Chickering, D., Heckerman, D., and Meek, C. 1997. A Bayesian approach to learning Bayesian Networks with local structure. In Proc. 13th Conference on Uncertainty in Artificial Intelligence (UAI), 80-89, Morgan Kaufmann.
Chow, M., Moler, E., and Mian, I. 2001. Identifying marker genes in transcription profiling data using a mixture of feature relevance experts. Physiol. Genomics 5, 99-111.
Cooper, G., and Herskovita, E. 1992. A Bayesian method for the induction of probabilistic networks from data. Machine Learning 9, 309-347.
Cozman, F. 2001. http://www-2.cs.cmu.edu/ javabayes/Home/.
D'haeseleer, P. 2000. Reconstructing gene networks from large scale gene expression data. Ph.D. dissertation. Computer Science Department, University of New Mexico. http://www.cs.unm.edu/ patrik.
Dawid, A., 1992. Applications of a general propagation algorithm for a probabilistic expert system. Statistics and Computing 2, 25-36.
Dawid, A., and Lauritzen, S. 1993. Hyper Markov laws in the statistical analysis of decomposable graphical models. Annals of Statistics 21, 1272-1317.

Dechter, R. 1996. Bucket elimination: a unifying framework for probabilistic inference. In Proc. 12th Conference on Uncertainty in Artificial Intelligence (UAI), 211-219, Morgan Kaufmann.
DeRisi, J., Iyer, V., and Brown, P. 1997. Exploring the metabolic and genetic control of gene expression on a genomic scale. Science 278, 680-686.
Ding, J. 2003. An analysis of binning heuristics using MDL and the BD metric. MS thesis in progress.
Duda, R., and Hart, P. 1973. Pattern classification and scene analysis. John Wiley and Sons, New York.
Duda, R., Hart, P., and Stork, D. 2000. Pattern Classification (2nd Edition). Wiley-Interscience, New York.
Dudoit, S., Fridlyand, J., and Speed, T. 2000. Comparison of discrimination methods for the classification of tumors using gene expression data. Technical Report 576, Department of Statistics, University of California, Berkeley.
Dudoit, S., Fridlyand, J., and Speed, T. 2002. Comparison of discrimination methods for the classification of tumors using gene expression data. J. Am. Stat. Assoc. 97, 77-87.
Eisen, M., Spellman, P., Botstein, D., and Brown, P. 1998. Cluster analysis and display of genome-wide expression patterns. In Proc. National Academy of Sciences USA 95, 14863-14867.
Fayyad, U., and Irani, K. 1993. Multi-interval discretization of continuous-valued attributes for classification learning. In Proc. International Joint Conference on Artificial Intelligence (IJCAI), 1022-1027.
Friedman, N., and Goldszmidt, M. 1996a. Discretizing continuous attributes while learning Bayesian networks. In Proc. 13th International Conference on Machine Learning (ICMS), 157-165.
Friedman, N., and Goldszmidt, M. 1996b. Learning Bayesian networks with local structure. In Proc. 12th Conference on Uncertainty in Artificial Intelligence (UAI), 211-219, Morgan Kaufmann.
Friedman, N., Geiger, D., and Goldszmidt, M. 1997. Bayesian network classifiers. Machine Learning 29, $131-163$.
Friedman, N., Nachman, I., and Pe'er, D. 1999. Learning Bayesian network structure from massive datasets: the sparse candidate algorithm. In Proc. 15th Conference on Uncertainty in Artificial Intelligence (UAI), 196-205, Morgan Kaufmann.
Friedman, N., Linial, M., Nachman, I., and Pe'er, D. 2000. Using Bayesian networks to analyze expression data. J. Computational Biology 7(3,4), 601-620.
Furey, T.S., Cristianini, N., Duffy, N., Bednarski, D.W., Schummer, M., and Haussler, D. 2000. Support vector machine classification and validation of cancer tissue samples using microarray expression data. Bioinformatics 16(10), 906-914.
Gander, W., and Gautschi, W. 2000. Adaptive Quadrature Revisited. BIT 40(1), 84-101.
Getz, G., Levine, E., and Domany. E. 2000. Coupled two-way clustering analysis of gene microarray data. In Proc. National Academy of Sciences 97(22), 12079-12084.
Golub, T., Slonim, D., Tamayo, P., Huard, C., Gaasenbeek, M., Mesirov, J., Coller, H., Loh, M., Downing, J., Caliguiri, M., Bloomfield, C., and Lander, E. 1999. Molecular classification of cancer: Class discovery and class prediction by gene expression monitoring. Science 286, 531-537.
Guyon, I., Weston, J., Barnhill, S., Vapnik, V., 2002. Gene selection for cancer classification using support vector machines. Machine Learning 46, 389-422.
Han, C., and Carlin, B. 2000. MCMC methods for computing Bayes factors: a comparative review. Technical Report, Division of Biostatistics, University of Minnesota.
Heckerman, D., Geiger, D., and Chickering, D. 1995. Learning Bayesian networks: The combination of knowledge and statistical data. Machine Learning 20, 197-243.

Helman, P., and Bhangoo, J. 1997. A statistically based system for prioritizing information exploration under uncertainty. IEEE Trans. on Systems, Man, and Cybernetics 27(4), 449-466, 1997.

Helman, P., and Gore, R. 1998. Prioritizing information for the discovery of phenomena. J. of Intelligent Information Systems 11(2), 99-138.
Ibrahim, J., Chen, M., and Gray, R. 2002. Bayesian models for gene expression with DNA microarray data. J. American Statistical Association 97(457), 88-99.
Jensen, F., Lauritzen, S., and Olesen, K. 1990. Bayesian updating in causal probabilistic networks by local computations, Computational Statistics Quarterly 4, 269-282.
Jensen, F., 2001. Bayesian networks and decision graphs. Springer-Verlag, New York.
Kang, H., and Atlas, S. 2003. Methods for evaluating performance of a class predictor. Technical Report, High Performance Computing Education and Research Center, University of New Mexico.
Khan, J., Wei, J., Ringner, M., Saal, L., Ladanyi, M., Westermann, F., Berthold, F., Schwab, M., Antonescu, C., Peterson, C., and Meltzer, P. 2001. Classification and diagnostic prediction of cancers using gene expression profiling and artificial neural networks. Nature Medicine 7, 673-679.
Korenberg, M. 2002. Prediction of treatment response using gene expression profiles. J. of Proteome Research $1,55-61$.

Lam, W., and Bacchus, F. 1994. Learning Bayesian belief networks: an approach based on the MDL principle, Computational Intelligence 10, 269-293.
Langley, P., Iba, W., and Thompson, K. 1992. An analysis of Bayesian classifiers. In Proc. 10th National Conference on Artificial Intelligence, 223-228, AAAI Press.
Lauritzen, S., and Spiegelhalter, D. 1988. Local computations with probabilities on graphical structures and their applications to expert systems, J. Royal Statistical Society Series B 50, 157-224.
Lee, Y., and Lee, C. 2002. Classification of multiple cancer types by multicategory support vector machines using gene expression data. Technical Report No. 1051r, Department of Statistics, University of Wisconsin, Madison.
Li, J., and Wong, L. 2002. Identifying good diagnostic gene groups from gene expression profiles using the concept of emerging patterns. Bioinformatics 18(5), 725-734.
Li, L., Darden, T., Weinberg, C., and Pedersen, L. 2001a. Gene assessment and sample classification for gene expression data using a genetic algorithm/k-nearest neighbor method. Combinatorial Chemistry and High-Throughput Screening 4(8), 727-739.
Li, L., Weinberg, C., Darden, T., and Pedersen, L. 2001b. Gene selection for sample classification based on gene expression data: study of sensitivity to choice of parameters of the GA/KNN method. Bioinformatics 17(12), 1131-1142.
Li, Y., Campbell, C., and Tipping, M. 2002. Bayesian automatic relevance determination algorithms for classifying gene expression data. Bioinformatics 18(10), 1332-1339.
Lockhart, D., Dong, H., Byrne, M., Follettie, M., Gallo, M., Chee, M., Mittmann, M., Wang, C., Kobayashi, M., Horton, H., and Brown, E. 1996. Expression monitoring by hybridization to high-density oligonucleotide arrays. Nature Biotechnology 14(12), 1675.
MacKay, D. 1995. Probable networks and plausible predictions-a review of practical Bayesian methods for supervised neural networks. Network: Computation in Neural Systems 6, 469-505.
Madden, M. 2002. Evaluation of the performance of the Markov Blanket Bayesian Classifier Algorithm. Technical Report NUIG-IT-0110002, Dept. of Information Technology, National University of Ireland, Galway.

Madigan, D., and York, J. 1995. Bayesian graphical models for discrete data. International Statistics Review $63,215-232$.
Madsen, A., and Jensen, F. 1999. Lazy propagation: a junction tree inference algorithm based on lazy evaluation, Artificial Intelligence 113, 203-245.
Moler, E., Chow, M., and Mian, I. 2000. Analysis of molecular profile data using generative and discriminative methods. Physiol. Genomics 4, 109-126.
Mosquera-Caro, M., et al. 2003a. Gene expression profiling for molecular classification and outcome prediction in infant leukemia reveals novel biologic clusters, etiologies, and pathways for treatment failure, in preparation.
Mosquera-Caro, M., et al. 2003b. Heterogeneity of gene expression profiles in MLL-associated infant leukemia: identification of distinct expression profiles and novel therapeutic targets for each MLL translocation variant, in preparation.
Mukherjee, S., Tamayo, P., Slonim, D., Verri, A., Golub, T., Mesirov, J. P., and Poggio, T. 1999. Support vector machine classification of microarray data. Technical Report AI Memo 1677, Massachusetts Institute of Technology, Cambridge.
Murphy, K., and Mian, S. 1999. Modelling gene expression data using dynamic Bayesian networks. Technical Report, Computer Science Division, University of California, Berkeley. http://www.cs.berkeley.edu/ `murphyk/Papers/1smb99.ps.gz.
Nguyen, D., and Rocke, D. 2002. Tumor classification by partial least squares using microarray gene expression data. Bioinformatics 18(1), 39-50.
Nguyen, D., and Rocke, D. 2002. Multi-class cancer classification via partial least squares with gene expression profiles. Bioinformatics 18(9), 1216-1226.
Pearl, J. 1988. Probabilistic reasoning for intelligent systems. Morgan Kaufmann, San Francisco.
Pearl, J., and Verma, T. 1991. A theory of inferred causation. In Knowledge Representation and Reasoning: Proc. 2nd International Conference, 411-452, Morgan Kaufmann.
Pe'er, D., Regev, A., Elidan, G., and Friedman, N. 2001. Inferring subnetworks from perturbed expression profiles. Bioinformatics 17, S215-S224.
Pomeroy, S., Tamayo, P., Gassenbeek, M., Sturla, L., Angelo, M., McLaughlin, M., Kim, J., Goumnerova, L., Black, P., Lau, C., Allen, J., Zagzag, D., Olson, J., Curran, T., Wetmore, C., Blegel, J., Pogglo, T., Mukherjee, S., Rifkin, R., Califano, A., Stolovitzky, G., Louis, D., Mesirov, J., Lander, E., and Golub, T. 2002. Prediction of central nervous system embryonal tumour outcome based on gene expression. Nature $415,436-442$.
Rigoutsos, I., Floratos, A., Parida, L., Gao, Y., and Platt, D. 2000. The emergence of pattern discovery techniques in computational biology. Metabolic Engineering 2(3), 159-177.
Schena, M., Shalon, D., Davis, R., and Brown, P. 1995. Quantitative monitoring of gene expression patterns with a complementary DNA microarray. Science, New Series 270(5235), 467-470.
Shafer, G., and Shenoy, P. 1990. Probability propagation. Annals of Mathematics and Artificial Intelligence 2, $327-352$.
Spiegelhalter, D., Dawid, D., Lauritzen, S., and Cowell, R. 1993. Bayesian analysis in expert systems. Statistical Science 8, 219-292.
Szabo, A., Boucher, K, Carroll, W., Klebanov, L., Tsodikov, A., and Yakovlev, A. 2002. Variable selection and pattern recognition with gene expression data generated by the microarray technology. Mathematical Biosciences 176, 71-98.

Tavazoie, S., Hughes, J., Campbell, M., Cho, R., and Church, G. 1999. Systematic determination of genetic network architecture. Nature Genetics 22, 281-285.

Tobin, F., Damian-Iordache, V., and Greller, L. 1999. Towards the reconstruction of gene regulatory networks. In Technical Proc. 1999 International Conference on Modeling and Simulation of Microsystems, San Juan, Puerto Rico.
van't Veer, L., Dal, H., van de Vijver, M., He, Y., Hart, A., Mao, M., Peterse, H. van der Kooy, K., Marton, M., Witteveen, A., Schreiber, G., Kerkhoven, R., Roberts, C., Linsley, P., Bernards, R., and Friend, S. 2002. Gene expression profiling predicts clinical outcome of breast cancer. Nature 415, 530-536.
Vapnik, V. 1998. Statistical Learning Theory. Wiley-Interscience, New York.
Weston, J., Mikherjee, S., Chapelle, O., Pontil, M., Poggio, T., and Vapnik, V. 2001. Feature selection for SVMs. In Advances in Neural Information Processing Systems (NIPS) 13, 668-674.
Woolf, P., and Wang, Y. 2000. A fuzzy logic approach to analyzing gene expression data. Physiol. Genomics $3,9-15$.

Zhang, H., Yu, C., Singer, B., and Xiong, M. 2001. Recursive partitioning for tumor classification with gene expression microarray data. Proc. National Academy of Science USA 98, 6730-6735.