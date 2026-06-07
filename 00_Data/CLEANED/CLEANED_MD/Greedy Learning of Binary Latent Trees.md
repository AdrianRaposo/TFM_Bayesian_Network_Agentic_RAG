![img-0.jpeg](img-0.jpeg)

# THE UNIVERSITY of EDINBURGH

## Edinburgh Research Explorer

## **Greedy Learning of Binary Latent Trees**

### **Citation for published version:**

Harmeling, S & Williams, CKI 2011, 'Greedy Learning of Binary Latent Trees', *IEEE Transactions on Pattern Analysis and Machine Intelligence*, vol. 33, no. 6, pp. 1087-1097. https://doi.org/10.1109/TPAMI.2010.145

### **Digital Object Identifier (DOI):**

10.1109/TPAMI.2010.145

### **Link:**

Link to publication record in Edinburgh Research Explorer

### **Document Version:**

Peer reviewed version

### **Published In:**

IEEE Transactions on Pattern Analysis and Machine Intelligence

### **Publisher Rights Statement:**

(c) 2011 IEEE. Personal use of this material is permitted. Permission from IEEE must be obtained for all other users, including reprinting/ republishing this material for advertising or promotional purposes, creating new collective works for resale or redistribution to servers or lists, or reuse of any copyrighted components of this work in other works.

### **General rights**

Copyright for the publications made accessible via the Edinburgh Research Explorer is retained by the author(s) and/or other copyright owners and it is a condition of accessing these publications that users recognise and abide by the legal requirements associated with these rights.

### **Take down policy**

The University of Edinburgh has made every reasonable effort to ensure that Edinburgh Research Explorer content complies with UK legislation. If you believe that the public display of this file breaches copyright, please contact openaccess@ed.ac.uk providing details, and we will remove access to the work immediately and investigate your claim.

![img-1.jpeg](img-1.jpeg)

# Greedy Learning of Binary Latent Trees 

Stefan Harmeling and Christopher K. I. Williams


#### Abstract

Inferring latent structures from observations helps to model and possibly also understand underlying data generating processes. A rich class of latent structures are the latent trees, i.e. tree-structured distributions involving latent variables where the visible variables are leaves. These are also called hierarchical latent class (HLC) models. Zhang (2004) proposed a search algorithm for learning such models in the spirit of Bayesian network structure learning. While such an approach can find good solutions it can be computationally expensive. As an alternative we investigate two greedy procedures: the BIN-G algorithm determines both the structure of the tree and the cardinality of the latent variables in a bottom-up fashion. The BIN-A algorithm first determines the tree structure using agglomerative hierarchical clustering, and then determines the cardinality of the latent variables as for BIN-G. We show that even with restricting ourselves to binary trees we obtain HLC models of comparable quality to Zhang's solutions (in terms of cross-validated log-likelihood), while being generally faster to compute. This claim is validated by a comprehensive comparison on several datasets. Furthermore, we demonstrate that our methods are able to estimate interpretable latent structures on real-world data with a large number of variables. By applying our method to a restricted version of the 20 newsgroups data these models turn out to be related to topic models, and on data from the PASCAL Visual Object Classes (VOC) 2007 challenge we show how such tree-structured models help us understand how objects co-occur in images. For reproducibility of all experiments in this paper, all code and datasets (or links to data) is available ${ }^{1}$.


Index Terms-Unsupervised Learning, Latent Variable Model, Hierarchical Latent Class Model, Greedy Methods.

## 1 INTRODUCTION

It is widely recognized that a distribution $p(\mathbf{x})$ over a vector of variables $\mathbf{x}=\left(x_{1}, \ldots, x_{D}\right)$ can often usefully be modelled with the aid of some latent (or hidden) variables. Our goal is to learn tree- or forest-structured distributions involving latent variables where the visible variables $\mathbf{x}$ are leaves, as shown in Figures 1-4. Our focus is primarily on discrete visible variables.

A simple latent-variable model for discrete data is the latent class model (LCM; see e.g. Lazarsfeld \& Henry, 1968). In this model there is one discrete latent variable that can take on $K$ different states, and the visible

[^0]variables are conditionally independent given the latent variable ${ }^{2}$. This model can readily be fitted to data using the EM algorithm. However, it has strong assumptions of conditional independence that in general will not be justified.

These strong assumptions can be relaxed by proposing a richer, tree-structured latent variable model as proposed for example in Zhang (2004). Following Zhang we call this a hierarchical latent class (HLC) model. The network structure is a rooted tree and the leaves of the tree are the visible variables. An attraction of a latent tree structure (compared to more complex DAGs) is that it allows linear time inference (Pearl, 1988). Furthermore, such a latent structure reflects a hierarchical grouping of the visible variables, making HLC models often interpretable and giving insights into the data generating processes. We emphasize the difference between the HLC model and the work of Chow and Liu (1968); the latter algorithm produces a tree-structured model defined solely on the visible variables, and does not induce latent variables.

To specify an HLC model there are two issues to be addressed: (i) the structure of the latent tree and (ii) the cardinality of the latent variables in the tree. Zhang (2004) defines the set of regular HLC models; essentially these are HLC models that are not overparameterized. (For example, for two binary visible variables we only need $K=2$ latent states to model their joint distribution exactly; a model with $K>2$ is overparameterized, as can be observed by parameter counting.) Zhang's algorithm conducts a search in the space of regular HLC models, starting the search from an LCM. The search involves moves which perform node introduction, node elimination, neighbour relocation, and changing the cardinality of a latent variable. Its runtime is dominated by the number of times the EM estimation procedure is called. In Zhang (2004) the EM algorithm is called $O\left(D^{4}\right)$ times (where $D$ is the number of variables), and each run of EM takes $O\left(K^{2} D N\right)$ time (see end of next section for an explanation of the symbols) leading to an overall runtime in $D$ of $O\left(D^{5}\right)$. Zhang and Kočka (2004) reduced this to $O\left(D^{3}\right)$. However, the EM algorithm is still called quadratically often in the number of variables.

We focus on HLC models that are binary trees or
2. This model has the same graphical structure as the naïve-Bayes classifier, but as it is trained in an unsupervised manner we refer to it as the LCM.


[^0]:    - S. Harmeling is with the Max Planck Institute for Biological Cybernetics, Tübingen, Germany.
    E-mail: stefan.harmeling@tuebingen.mpg.de
    - C. K. I. Williams is with the Institute for Adaptive and Neural Computation, University of Edinburgh, Scotland.
    E-mail: ckiw@inf.ed.ac.uk

forests. In Section 2 we investigate two bottom-up procedures: the first, BIN-G, determines both the structure of the tree and the cardinality of the latent variables in a bottom-up fashion. The second algorithm BIN-A uses agglomerative hierarchical clustering to determine the structure of the tree, and then estimates the cardinality of the latent variables as for BIN-G. We show that both call the EM algorithm only $D-1$ times, i.e. they are linear in the number of variables, resulting in overall runtimes of $O\left(D^{2}\right)$.

In Section 3 we apply our methods to several realworld datasets and show experimentally that their performance (in terms of log-likelihood) is comparable to Zhang's method, while being computationally more efficient. Related work is discussed in section 4, and we give our conclusions in section 5.

## 2 Learning Binary Latent Tree Models

Our goal is to induce from $N$ data samples an HLC model which is a good model for the underlying distribution from which the data was drawn. The quality of the induced model could be estimated e.g. using cross-validated predictive log-likelihood, or by a penalized maximum likelihood criterion such as the Bayesian Information Criterion (BIC) $J(\hat{\theta})=l(\hat{\theta})-P / 2 \log N$, where $l(\hat{\theta})$ is the log-likelihood corresponding to optimal parameters $\hat{\theta}$ and structure, $P$ is the number of free parameters of the model and $N$ is the number of data points. The ability to generalize is an important feature as otherwise a sufficiently large model can simply "remember" the input data distribution. For example, consider an LCM which has as many latent states as there are unique data vectors: by making the conditional distribution for a given latent state be a delta function on the corresponding data vector the dataset can be memorized. Thus to encourage generalization the size of the model must be controlled.

We first describe how to learn the basic building block, the LCM, and then discuss two greedy algorithms for building a binary latent tree.

### 2.1 Learning Latent Class Models

We describe the simple case where the parent node has two children. Let $x_{1}$ and $x_{2}$ be two variables which not necessarily refer to visible variables, and a latent variable (denoted $z$ ). We focus on discrete random variables. The LCM for two variables $x_{1}$ and $x_{2}$ introduces a latent variable $z$, so that

$$
p\left(x_{1}, x_{2}\right)=\sum_{k} p(z=k) p\left(x_{1} \mid z=k\right) p\left(x_{2} \mid z=k\right)
$$

Its parameters $\pi_{k}=p(z=k), \theta_{i k}=p\left(x_{1}=i \mid z=k\right)$ and $\eta_{j k}=$ $p\left(x_{2}=j \mid z=k\right)$ are learned from data by the Expectation Maximization (EM) algorithm.

Deriving the EM updates for this model is a simple exercise if $x_{1}$ and $x_{2}$ are both observed, but it becomes
more interesting when they are not observed. The relevant variables $z, x_{1}, x_{2}$ and the children of $x_{1}$ and $x_{2}$ form a tree-structured belief network (TSBN) with $z$ at the root. The EM updates for this case are derived in Appendix A making use of Pearl's belief propagation algorithm for trees (Pearl, 1988). Similar updates have been used in Feng et al., (2002, Eq. (6)),
In practice we try different cardinalities for the latent variable $z$ between 1 and $K_{\max }$, and select automatically using the BIC. We also use a number of random restarts to reduce the problem of local optima (in the reported experiments we did 10 restarts). We denote by LCM the method that automatically learns a latent class model.

### 2.2 Incremental Learning of Binary Tree Models

Our first approach to finding a binary-tree HLC model is by a greedy growing a tree-structured probabilistic model. We start with a simple model in which all visible variables are assumed independent. These variables form the "working set". We then choose from that set the pair with the highest mutual information (MI) and model them with an LCM with a new latent variable $z$. We then remove the selected pair from the working set of variables, add $z$ to this set, and repeat either (i) until either the working set contains only a single variable (which would be the root the overall learned tree), or (ii) if we try to introduce a latent variable with a single state. In the latter case we stop early, and we fix the tree structure and the number of hidden states. Finally, we refine the conditional probability tables (CPTs, see line 19 of Alg. 1 and Appendix B), before we output the current forest of trees. The resulting algorithm, called BIN-G, is stated formally as Alg. 1.
The rationale for selecting the pair of variables with the highest MI is based on the following observation. Consider a distribution $p(\mathbf{x})$ over a vector of random variables $\mathbf{x}$ which is approximated by a distribution $q(\mathbf{x})$, where

$$
q(\mathbf{x})=p\left(x_{i}, x_{j}\right) \prod_{k \neq i, j} p\left(x_{k}\right)=\frac{p\left(x_{i}, x_{j}\right)}{p\left(x_{i}\right) p\left(x_{j}\right)} \prod_{k} p\left(x_{k}\right)
$$

i.e. $q(\mathbf{x})$ models the joint distribution of $x_{i}$ and $x_{j}$, but only the marginal distributions of the other variables. Then

$$
\begin{aligned}
\mathrm{KL}(p \| q) & =\sum_{\mathbf{x}} p(\mathbf{x}) \log p(\mathbf{x})-\sum_{\mathbf{x}} p(\mathbf{x}) \log q(\mathbf{x}) \\
& =-\mathrm{I}\left(x_{i}, x_{j}\right)+\sum_{\mathbf{x}} p(\mathbf{x}) \log \frac{p(\mathbf{x})}{\prod_{k} p\left(x_{k}\right)}
\end{aligned}
$$

where $\mathrm{I}\left(x_{i}, x_{j}\right)$ is the MI of $x_{i}$ and $x_{j}$ under the distribution $p\left(x_{i}, x_{j}\right)$. Thus in order to minimize the KullbackLeibler divergence between $p(\mathbf{x})$ and $q(\mathbf{x})$ we should select the pair that has the highest MI.
Note that each induced tree will have a root. However, as is well-known in phylogenetics (see e.g. Felsenstein, 2004) the root can be "walked" around the tree without changing the joint distribution; there is an equivalence

```
Algorithm 1 BIN-G(x)
    : input: a working set \(V\) of variables \(x_{1}, \ldots, x_{D}\)
    \(G \leftarrow\) the graph with vertices \(V\) and no edges
    calculate pair-wise MI for all observed variables
    loop
        \(W \leftarrow\) pair from \(V\) with highest mutual information
        \(V \leftarrow V \backslash W /^{*}\) remove that pair from \(V^{*} /\)
        \(z \leftarrow \operatorname{LCM}(W) /^{*}\) find latent class model by EM */
        if \(z\) has single state then
            break \(/^{*}\) outer loop */
        end if
        add vertex \(z\) to graph \(G\)
        add edges from \(z\) to children in \(W\) to graph \(G\)
        if \(V\) is empty then
            break \(/^{*}\) outer loop */
        end if
        add latent variable \(z\) to working set \(V\)
        calculate pair-wise MI for the new vertex \(z\) and all
        variables of the working set
    end loop
    recursively refine the conditional probability tables
    using EM on structure \(G\) (see Appendix B for details)
    output: the graph \(G\) (being a forest)
```

class of directed trees which corresponds to one undirected tree (see also discussion in Zhang, 2004, §3.2). This is not a problem for us as we only care about the distribution over the visibles induced by the equivalent undirected tree.

### 2.3 Learning Trees via Agglomerative Hierarchical Clustering

The BIN-G algorithm determines the tree structure and cardinality of the latent variables greedily as it proceeds by estimating a LCM for each introduced latent variable. Thus we are able to compute the MI between inferred latent nodes and other existing nodes (either latent or observed), as discussed above and in the appendix. An interesting question raised by one of the reviewers asked how such an inferred tree-structured model compares with a model based on a tree-structure determined via an agglomerative hierarchical clustering procedure (AHC, see e.g. Duda \& Hart, 1973) running on the variables (not the datapoints). Of course such a tree structure also requires inference of LCMs locally at each node to constitute a full probabilistic model. However, instead of inferring the LCMs simultaneously with the tree structure (as BIN-G does), the LCMs can also be estimated after determining the tree structure.

We state such an algorithm based on AHC formally as Alg. 2 and called it BIN-A. The linkage options of AHC (mentioned in line 13 of Alg. 2) are explained at the beginning of Section 3. First of all we note that both proposed algorithms are similar. The clustering procedure of AHC for BIN-A is analogous to estimating the tree-structure in BIN-G. The differences are:

```
Algorithm 2 BIN-A(x)
    : input: a working set \(V\) of variables \(x_{1}, \ldots, x_{D}\)
    \(G \leftarrow\) the graph with vertices \(V\) and no edges
    calculate pair-wise MI for all observed variables
    loop
        \(W \leftarrow\) pair from \(V\) with highest mutual information
        \(V \leftarrow V \backslash W /^{*}\) remove that pair from \(V^{*} /\)
        add vertex \(z\) to graph \(G\)
        add edges from \(z\) to children in \(W\) to graph \(G\)
        if \(V\) is empty then
            break /* outer loop */
        end if
        add latent variable \(z\) to working set \(V\)
        approximate pair-wise MI for the new vertex \(z\) and
        all variables of the working set by single, complete,
        or average linkage
    end loop
    recursively estimate the cardinality and a latent class
    model at each latent node by EM (i.e. calling LCM)
    beginning at the leaves
    recursively refine the conditional probability tables
    using EM on structure \(G\) (see Appendix B for details)
    output: the graph \(G\) (being a forest)
```

- Instead of estimating an LCM for each introduced latent node and calculating the MI in BIN-G (lines $7-10$ and 17 in Alg. 1), BIN-A omits the immediate LCM estimation and approximates the MI by single, complete, or average linkage (line 13 in Alg. 2).
- In line 15 Alg. 2 estimates the LCMs bottom-up once the tree-structure is fixed, before applying EM on the whole model for refinement (line 16).
The BIN-A algorithm is related to some previous proposals for learning a tree structure by AHC, as discussed in Section 4.


### 2.4 Runtime Complexity of BIN-G and BIN-A

We will use the following constants for the runtime analysis:


The runtime complexity of BIN-G is $O\left(D^{2} N K^{2}+\right.$ $\left.D S I N K^{2} K_{\max }\right)$. Its loop (see Alg. 1) is executed at most $D-1$ times, as the cardinality of the working set of variables $V$ reduces by one on each iteration. The $O\left(D^{2} N K^{2}\right)$ term arises from the calculation of pairwise MIs at line 3, and the fact that the mutual information calculation at line 18 is $O\left(D N K^{2}\right)$ and that it is executed $O(D)$ times. The $O\left(D S I N K^{2} K_{\max }\right)$ term arises from the call to LCM in line 8, and the fact that this will be called at most $D-1$ times. Each iteration of EM in LCM takes

$O\left(N K^{2}\right)$, and there are up to $I$ iterations and $S$ restarts. Thus we conclude that the runtime complexity of BIN-G is quadratic in the number of variables $D$.

How does the second approach BIN-A compare to BIN-G? As already the structural similarity of the algorithms suggests, we will see that both have the same runtime complexity: similar reasoning as above explains that the loop of BIN-A (see Alg. 2) that determines the tree structure via AHC is executed at most $D-1$ times. However, each iteration is much faster than for BIN-G since no latent class model is learned in that step. Thus the AHC step of BIN-A is linear in the number of variables. However, the subsequent recursive estimation procedure (line 15 in Alg. 2) estimates an LCM for each latent variable and thus calls LCM also linearly often in the number of variables $D$. Thus both procedures have similar times, as confirmed in the experimental section below.

### 2.5 Learning Latent Trees for Gaussian Variables

Above we have described a model for discrete visible variables. The analogue of the LCM for Gaussiandistributed continuous variables is the factor analysis (FA) model. Here the number of latent factors plays an analogous role to the cardinality of the latent variable in the discrete case; model selection for FA could be carried out using BIC. Going beyond factor analysis we come to a tree-structured latent-variable model, which is in fact a description of a (recursive) structural equation model (SEM, see e.g. Bollen, 1989). The greedy method above could equally be applied to learn SEMs.

## 3 EXPERIMENTS

Restricting ourselves to binary trees results into large speed-ups in runtime which allow our methods to infer latent structures of large real-world datasets. In Section 3.1 we analyse text data from newsgroups, and search in Section 3.2 for latent structure in co-occurrence data derived from the PASCAL VOC 2007 challenge. We thoroughly evaluate our approach in Sections 3.3 and 3.4 on further datasets. The algorithms we consider are abbreviated in this section as follows: algorithm IND generates baseline results using the model in which all variables are independent of each other. Algorithm ZHANG is the compiled Java code provided by N. L. Zhang implementing the method described in Zhang and Kočka (2004). Algorithm LCM estimates a non-hierarchical Latent Class Model inferring a single latent variable. We also compare against algorithm CL from Chow and Liu (1968), however we note that it does not infer a latent structure. Finally, algorithms BIN-G and BIN-A denote our proposed methods detailed above. Note that BIN-A employs average linkage to approximate the MI between latent and other variables, which means that the MI between two variables $z_{1}$ and $z_{2}$ (either latent or observed) is approximated by the average MI between any leaf below or equal to $z_{1}$ and any leaf below or equal
to $z_{2}$. Results using complete linkage (maximum distance, i.e. minimum MI) or single linkage (minimum distance, i.e. maximum MI) were omitted. These AHC variants produced similar results (in terms of the applied performance measures) and generated qualitively slightly inferior forest structures on the newsgroup (Section 3.1) and visual co-occurrence datasets (Section 3.2).

Note that for reproducibility the code for all experiments is provided as supplementary material (see footnote on the first page of this paper). This includes code and data that generates the toy examples and interfaces to the datasets freely available on the internet as indicated.

### 3.1 Topics of 20 Newsgroups

To demonstrate the ability of BIN-G and BIN-A to deal with a large number of variables we applied it to a binarized word-document matrix derived by Sam Roweis ${ }^{3}$ from the UCI 20 newsgroups dataset. The dataset has been restricted to 100 words, such there are 100 binary variables and 16,242 data points. Our methods terminated after about an hour (BIN-G) and a quarter hour (BIN-A), while Zhang's method did not finish after several days, even though ZHANG's JAVA implementation is based on the Colt framework ${ }^{4}$ for high performance scientific computing, while our code is Matlab. For completeness we also run LCM on this data and obtained the best log-likelihood. However, LCM is slower by factor of ten and it estimates only a single latent variable so it provides no interpretable graph structure.

Figure 1 shows a subtree of the whole latent forest model (shown in Figure 2) which BIN-G has estimated. The trees obtained by BIN-A are shown in Figure 3. Note that BIN-G and BIN-A reached similar log-likelihoods with BIN-G being slightly better (see Table 1). Each leaf corresponds to the word with which it is labelled, and each internal node displays an order number. The lowest order number for this dataset is 101 which corresponds to one plus the number of observed variables. The smaller the order number the earlier its children were merged during the tree building process.

Examining the labels of the tree inferred by algorithm BIN-G reveals that the inferred model can be interpreted in a meaningful way (similar to the work of Blei et al. (2003)): For instance the leaves of the subtree in Figure 1 capture the words from the topic "medicine", such as:
medicine (subtree at node 192): doctor, medicine, disease, patients, cancer, studies, aids, health, insurance.
Similarly, other subtrees (see Figure 2) of the whole latent tree model collect words from other topics:
sports (subtree at node 175): puck, hit, won, win, fans, league, nhl, games, baseball, hockey, players, season, team
3. http://www.cs.toronto.edu/ roweis/data.html
4. http://acs.lbl.gov/ hoschek/colt/

![img-2.jpeg](img-2.jpeg)

Fig. 1. Topics of 20 newsgroups: subtree collecting words of topic "medicine".
politics/religion (subtree at node 170): children, human, president, gun, state, law, government, rights, israel, jews, war, world, religion, christian, bible, god, jesus, evidence, fact
computer (subtree at node 187): email, phone, help, problem, technology, computer, science, data, system, mac, scsi, disk, drive, memory, graphics, card, video, pc, software, driver, ftp, version, program, files, dos, windows, format, image, display, server
spaceflight (subtree at node 162): mars, satellite, lunar, moon, launch, shuttle, nasa, space, earth, orbit, mission, solar
others (subtree at nodes 140): research, university; (subtree at node 188): water, vitamin, food, msg, (subtree at node 178): power, question
car (subtree at node 183): oil, bmw, honda, dealer, car, engine
We note, that the forest of BIN-G is not perfect. For comparison Figure 3 shows the forest inferred by BIN-A which has almost the same subtrees, but did split them, which might be preferable. However, the overall inferred latent structures of both methods do reflect the mixture of topics in the selected newsgroups. Furthermore, there is also interesting structure inside a single tree itself: e.g. in subtree "politics" the word "law" is closer to "government" than to "world" (see both Figures. 2 and 3).

### 3.2 PASCAL VOC 2007 data

A vision-related dataset to which we applied BIN-G and BIN-A was derived from the PASCAL VOC 2007 challenge on object recognition and localization in images ${ }^{5}$ For each image in the dataset, each instance of the 20 considered object classes was labelled with a bounding
5. See http://www.pascal-network.org/challenges/VOC/voc2007 for example images, dataset statistics, etc.
box. The dataset consists of $D=20$ variables that encode the location of each object's bounding box by a number from 0 to 9 . Horizontally, there are three possibilities for the bounding box: either (i) the left edge of a small bounding box is on the far left or (ii) the right edge of a small bounding box is far right or (iii) the bounding is large horizontally and extends from left to right over the image. Similarly we get three possibilities vertically, which amounts to 9 options for an existing bounding box. Option 0 denotes that the corresponding object class is absent. If there is more than one object of a particular class in an image, multiple data points are generated. The challenge of this dataset is that each of the 20 variables has 10 states. Our methods BIN-G and BIN-A terminated after 0.5 and 1.5 hours respectively (see Table 1). We also tried to apply ZHANG. However, it did not finish after several days. Our methods, which estimate reasonable latent structures on this dataset (see Figure 4), are not able to infer a model that beats the slower LCM algorithm and the faster procedure of Chow and Liu (1968) in terms of log-likelihood (see Table 1). However, we note that a latent tree model is much more readily interpretable than the Chow-Liu tree or the flat LCM model.

Figure 4 shows the latent forest inferred by BIN-G. Visual results for BIN-A are omitted since they are similar. Each node either contains the name of a variable, such as "aeroplane", or the node number with the number of states in round brackets. Nodes with smaller numbers have been introduced earlier than nodes with larger numbers.

The learned trees arranges the objects (which correspond to variables) in a meaningful way: the biggest tree groups road scenes (subtree at node 26: person, car, bus, motorbike) and indoor scenes (subtree at node 28: sofa, tvmonitor, pottedplant, bottle, chair, diningtable). The singleton trees (e.g. the pets: cat, dog) make sense since people often take pictures of their pets without other objects. Similarly we wouldn't expect pictures of "aeroplane" to co-occur with other objects. On the other hand "cow" and "horse" can co-occur in images, which is reflected by the fact that they are grouped in a tree (subtree at node 30).

### 3.3 Comparative Study on 10 Datasets

To survey how well our fast greedy methods learn latent trees, we apply our algorithms to several toy and realworld datasets. As a performance measure we choose 10fold cross-validated predictive log-likelihood (CVPLL). That is, we divide each dataset into 10 equal-sized folds, train a model on 9 of the folds and compute the predictive log-likelihood on the remaining fold. Averaging these results over the 10 folds gives the results in Tables 2 and 3 which uses the algorithm abbreviations introduced at the beginning of this section.

All not publicly available datasets are included in the supplementary in form of generating code or files. For

TABLE 1
Log-likelihoods and running times on 20 newsgroups, and PASCAL VOC data.


TABLE 2
Ten-fold cross-validated log-likelihood for various datasets (rows) and algorithms (columns). The winner in each row is shown in boldface, the runner-up in italics. Column $D$ shows the number of variables, $N$ the number of data points.


TABLE 3
Ten-fold cross-validated running times in seconds for various datasets (rows) and algorithms (columns). Note that these numbers show only tendencies since different dataset/algorithm combinations run on different cluster nodes.


completeness we briefly describe in the following the various datasets.

The BINARY-FOREST data is generated from a model with two separated binary trees. One tree has three nodes (two leaves), the other one five nodes (three leaves). At each node a coin is flipped and incorporated into the state. THREE-LEVEL-BINARY is a full binary tree with 4 leaves, each having 8 states (again with a fair coin flip at each node). THREE-COINS consists of three variables $x_{1}=\left(a_{1}, a_{2}\right), x_{2}=\left(a_{2}, a_{3}\right), x_{3}=\left(a_{3}, a_{1}\right)$ with $a_{1}, a_{2}, a_{3}$ being three coin flips. Thus $x_{1}$ shares a single bit with $x_{2}$ and also with $x_{3}$, similarly $x_{2}$ and $x_{3}$. This dataset can not be modelled properly with a binary tree. The SIX-COINS example has four observed variables based on 6 latent variables. Six coins $a_{1}, \ldots, a_{6}$ (with values zero and one) are tossed, and $x_{1}, \ldots, x_{4}$ are set as $x_{1}=a_{1}+2 a_{3}+4 a_{5}, x_{2}=a_{2}+2 a_{3}+4 a_{5}, x_{3}=$ $a_{1}+2 a_{4}+4 a_{6}, x_{4}=a_{2}+2 a_{4}+4 a_{6} . x_{1}$ and $x_{2}$ share two bits, $x_{3}$ and $x_{4}$ share two bits as well. All other pairs share a single bit or none.

For a direct comparison to the work of Zhang (2004) we also use four datasets provided in his paper, namely the Hannover rheumatoid arthritis data on five bi-
nary visible variables (HANNOVER-5), and three datasets COLEMAN, HIV-TEST and HOUSE-BUILDING that are all on 4 binary visible variables. The HANNOVER-5 is reduced from a larger dataset given by Kohlmann and Formann (1997) which has 8 binary visible variables; we include this dataset as HANNOVER-8 in the comparison. To have real data with visible cardinalities greater than two we also selected the UCI dataset ${ }^{6}$ CAR-EVALUATION which has 7 variables all with cardinality 3 or more.

Summarizing Tables 2 and 3 we conclude that BIN-G and BIN-A provide competitive HLC models in comparison with ZHANG, while at the same time often being faster. In Table 2 BIN-G and BIN-A are the winning algorithms for $4 / 10$ datasets, and are close to ZHANG in all cases except for THREE-COINS (which was designed to make BIN-G and BIN-A fail). Note that LCM is comparatively slow because estimating a single latent node with many states is more expensive than estimating several latent nodes each with few states.
6. available from http://archive.ics.uci.edu $/ \mathrm{ml} /$

### 3.4 Results on COIL-42 and COIL-86

The COIL-86 data ${ }^{7}$ is the training set of the COIL Challenge 2000, containing 5822 records and 86 attributes. As in Zhang and Kočka (2004) this dataset was reduced to 42 attributes to produce COIL-42; in this process the cardinalities of the variables was also reduced for many variables. Table 4 compares the BIC scores of BIN-G and BIN-A with the BIC score of ZHANG reported in Zhang and Kočka (2004). All of BIN-G, BIN-A, and ZHANG are better than LCM, with ZHANG being slightly better. However, looking at the run times BIN-G and especially BIN-A excels: our implementation of BIN-G takes 505 seconds, BIN-A takes only 87 seconds, while the reported runtime in Zhang and Kočka (2004) is 121 hours (= 435,600 seconds). Even though computers have got faster since 2004, BIN-G and BIN-A provide a large speedup while delivering good performance.

Additionally, we applied BIN-G and BIN-A to COIL86. Comparing their BIC scores with LCM and IND we see that our methods have extracted some additional structure in the data. To our knowledge no HLC learning method has previously been successfully applied to COIL-86. The steep increase in runtime from COIL-42 to COIL-86 even though the number of variables only doubled is due to the fact that the original COIL-86 data has many more states per variable than the reduced version COIL-42 (as discussed above).

## 4 Related Work

Our work is partly inspired by recent ideas by Hinton et al. (2006) on deep belief networks (DBNs), where a greedy layerwise learning procedure is used, with the same learning algorithm applied at each level to the transformed data. Our work uses the same idea, except that rather than transforming all variables in layer $\ell$, we select a pair of variables which are replaced by a new latent variable, with all other variables from layer $\ell$ being copied to the higher layer $\ell+1$.

In very interesting work, Pearl (1988, Section 8.3) discusses the recovery of latent trees of binary and Gaussian variables in the case that the joint distribution can be exactly decomposed into a latent tree. His algorithm relies on the fact that the correct configuration out of four possibilities for a tree with four visible variables and two internal nodes can be decided based on relationships of pairwise correlations between the visible variables. This fact can be used recursively to connect visible variables one by one into the correct tree structure. However, we note that (i) Pearl does not address the approximation of a distribution $p(\mathbf{x})$ by a latent tree, but only the reconstruction of the underlying true latent tree, (ii) that he assumes that exact pairwise statistics are available (not samples), and (iii) that he only considers binary discrete variables.

There has also been much recent work on branching tree models relating to clustering (see e.g. Williams, 2000;

[^0]Neal, 2003; Teh et al., 2008). However, there is a important difference between such models and our latent trees: in the clustering models each leaf corresponds to a datapoint, not a variable. In these models all nodes (both latent and leaf) have the same type and dimension, and the branching tree represents an evolutionary process, inspired by phylogenetic trees (see e.g. Felsenstein, 2004). In contrast we note that for our latent trees the visible variables can have different number of states, and that a latent variable will in general have a different number of states to either of the variables it replaces.

Kemp and Tenenbaum (2008) proposed a method for comparing different model structures for data. Their method builds models (including latent trees) where the leaves correspond to datapoints (or entities in their terms) rather than variables. However, by transposing the data matrix such a method could be used to build a latent tree model. With respect to the details, they use graphical Gaussian models for the tree and this is less suitable for discrete data (Kemp, pers comm, 2008). Also they use a divisive (as opposed to agglomerative) algorithm for tree construction, using a randomized splitting of a node which is repeated several times, and the best split chosen. In our context the divisive approach would have been expensive since the number of possible splits to be evaluated can be large and each evaluation requires the estimation of a local LCM. Thus we opted for an agglomerative algorithm where each step only requires the selection of a pair of variables to be merged.

There is also some recent work on probabilistic hierarchical clustering, e.g. Heller and Ghahramani (2005); Friedman (2003). It might be thought that by transposing the role of the variables and datapoints in the data matrix these methods could be used to obtain a latent tree model for the data. However, neither of the two constructs a generative model as our approach does. In fact Heller and Ghahramani (2005, Section 6) themselves say "[our model] is not in fact a hierarchical generative model of the data, but rather a hierarchical way of organizing nested clusters."

Especially related to the proposed BIN-A algorithm is the work of Connolly (1993) who also constructs the tree topology by running AHC on the variables, measuring the similarity between two variables by their MI. To define the similarity between groups of variables, he computes the criterion (mean pairwise inter-cluster MI) / (mean pairwise intra-cluster MI) and seeks the join that minimizes this criterion. This is an "average link" type criterion in hierarchical clustering parlance. To construct latent variables Connolly uses Fisher's conceptual clustering algorithm COBWEB (Fisher, 1987), rather than LC modelling and EM. In our view Connolly's paper provides some interesting ideas for HLC model learning, but is lacking a firm statistical framework.

Kojadinovic (2004) also discusses a method for the hierarchical clustering of variables based on their mutual information. He considers the single link, average link and complete link criteria. His method does not actually


[^0]:    7. available from http://kdd.ics.uci.edu/databases/tic/tic.html

TABLE 4
BIC scores and running times on COIL-42 and COIL-86 datasets. The BIC score and running times in columns ZHANG are taken from (Zhang \& Kočka, 2004). All running times are in seconds.


produce a probability model for the data, but only a hierarchical clustering of the variables.

Wang et al. (2008) proposed an algorithm to construct HLC models to approximate inference in Bayesian networks. In their work the tree structure is determined via a lower bound between the latent variables and the visible variables; this turns out to select the two variables (one from each group under consideration) that maximize the MI. Note that as maximizing similarity (MI) is equivalent to minimizing dissimilarity, this is analogous to single link clustering. In their work the same cardinality is used for all latent nodes, based on trading off inferential complexity against fidelity of approximation of the original Bayesian network. Note that the goal of Wang et al. (2008) is rather different from ours: their HLC model is used to approximate inference in Bayesian networks, while we infer interpretable latent structure, as demonstrated e.g. with the 20 newsgroups example.

## 5 CONCLUSION

Estimating HLC models without any restrictions requires searching over a large number of possible latent structures, as implemented in Zhang's framework (Zhang, 2004; Zhang \& Kočka, 2004). However, in its full generality it remains a difficult problem and is (like structure learning for Bayes nets) prone to lots of suboptimal solutions and large runtime complexity.

In this paper we have considered the alternative of greedy algorithms to learn binary latent tree structures. This leads to a sensible trade-off between model complexity and runtime while preserving expressiveness, as demonstrated in our comprehensive experiments. Due to its favorable runtime scaling, inferring a binary latent tree was even possible on datasets with a large number of variables. Binary latent trees can also be sensible starting points for heuristic procedures that learn more sophisticated models. We did explore various extensions of our algorithm to infer non-binary trees using ideas from information theory. However, preliminary experiments suggest that such approaches are not worth the extra computational costs they require.

Restricting the branching factor of latent trees does limit the model class, but still allows rich enough models to take advantage of the hierarchical modelling power of HLC models. Furthermore, the binary tree structure implicitly limits the cardinality of the latent nodes, which facilitates EM estimation; this may be part of the reason
why the simple binary latent trees performed comparably to much richer models.

## APPENDIX A EM-UPDATES

## A. 1 Notation

A single observation consists of $D$ variables $x_{1}, \ldots, x_{D}$. These observed variables are the leaves of a binary latent tree, which is learned in a greedy manner. The latent nodes are denoted by $x_{D+1}, \ldots, x_{R}$ with $R=2 D-1$ being the index of the root. The index of the parent of $x_{t}$ is denoted by $\mathrm{pa}(t)$. Define the parameters at node $t$ as

$$
\begin{aligned}
\theta_{i j}(t) & =p\left(x_{t}=i \mid x_{\mathrm{pa}(t)}=j\right) \\
\pi_{i}(t) & =\bar{p}\left(x_{t}=i\right)
\end{aligned}
$$

Note that $\pi_{i}(t)$ is defined in terms of $\bar{p}$ which is the distribution of the latent subtree with $t$ as the root ignoring all other nodes.

Let $R=2 D-1$ be the index of the root of the completed binary tree for which $\pi_{i}(R)=\bar{p}\left(x_{R}=i\right)=$ $p\left(x_{R}=i\right)$. Then we can write the cumulative distribution as

$$
p\left(x_{1}, \ldots, x_{R}\right)=\pi_{x_{R}}(R) \prod_{t=1}^{R-1} \theta_{x_{t}, x_{\mathrm{pa}(t)}}(t)
$$

Note that the cumulative distribution uses only $\pi(R)$. All other $\pi(t)$ for $t \neq R$ are only used during the greedy building of the tree.

We denote by $\operatorname{in}(t)$ the indices of the observed variables which are descendents of $x_{t}$, i.e. the leaves below $x_{t}$, briefly denoted by $x_{\text {in }(t)}$. Similar to the inside-outside algorithm for probabilistic context free grammars (or forward-backward algorithm for hidden Markov chains) we define

$$
\beta_{i}(t)=p\left(x_{\text {in }(t)} \mid x_{t}=i\right)
$$

which can be calculated recursively as follows: For the leaves, i.e. $t \leq D$, we set

$$
\beta_{i}(t)= \begin{cases}1 & \text { if } x_{t}=i \\ 0 & \text { otherwise }\end{cases}
$$

Latent nodes are calculated recursively from the values of the children, i.e. for $t>D$ and assuming that $t$ has

only two children $u$ and $v$ we have

$$
\begin{aligned}
\beta_{k}(t)= & p\left(x_{\ln (t)} \mid x_{t}=k\right) \\
= & \sum_{i j} p\left(x_{\ln (u)}, x_{\ln (v)}, x_{u}=i, x_{v}=j \mid x_{t}=k\right) \\
= & \sum_{i j} p\left(x_{\ln (u)} \mid x_{u}=i\right) p\left(x_{u}=i \mid x_{t}=k\right) \\
& p\left(x_{\ln (v)} \mid x_{v}=j\right) p\left(x_{v}=j \mid x_{t}=k\right) \\
= & \left(\sum_{i} \beta_{i}(u) \theta_{i k}(u)\right)\left(\sum_{j} \beta_{j}(v) \theta_{j k}(v)\right)
\end{aligned}
$$

For more children there is a factor for each child. Note that for the leaves $\beta(t)$ are distributions, but the $\beta(t)$ s for the other nodes are not necessarily normalized.

## A. 2 Greedy learning

To simplify notation assume we have only observed a single data point. The current state of the learning process is defined by the frontier which are the variables which have no parents yet. Their distributions are defined by $\pi$. For the leaves we have (for $t \leq D$ )

$$
\pi_{i}(t)=\beta_{i}(t)
$$

For these distributions we can calculate all pairwise mutual informations and choose the maximizing pair of variables. Let's denote those two variables by $u$ and $v$, for which we wish to learn a common parent $x_{t}$. For this we maximise the likelihood of the leaves below $u$ and $v$ which will be denoted by $x_{\ln (t)}=x_{\ln (u)} \cup x_{\ln (v)}$,

$$
\begin{aligned}
& p\left(x_{\ln (t)}\right)=\sum_{k} \beta_{k}(t) \pi_{k}(t) \\
& =\sum_{k}\left(\sum_{i} \beta_{i}(u) \theta_{i k}(u)\right)\left(\sum_{j} \beta_{j}(v) \theta_{j k}(v)\right) \pi_{k}(t)
\end{aligned}
$$

From the previous iterations we have $\beta(u)$ and $\beta(v)$. The parameters we need to learn are $\pi(t)$ and $\theta(u)$ and $\theta(v)$. For several observations $x^{(1)}, \ldots, x^{(N)}$ we maximize

$$
\begin{aligned}
& L=\prod_{n=1}^{N} p\left(x_{\ln (t)}^{(n)}\right)=\prod_{n=1}^{N} \sum_{k} \beta_{k}^{(n)}(t) \pi_{k}(t) \\
& =\prod_{n=1}^{N} \sum_{k}\left(\sum_{i} \beta_{i}^{(n)}(u) \theta_{i k}(u)\right)\left(\sum_{j} \beta_{j}^{(n)}(v) \theta_{j k}(v)\right) \pi_{k}(t) \\
& =\prod_{n=1}^{N} \sum_{i j k} \beta_{i}^{(n)}(u) \theta_{i k}(u) \beta_{j}^{(n)}(v) \theta_{j k}(v) \pi_{k}(t) \\
& =\prod_{n=1}^{N} \sum_{i j k} p\left(" \text { latent" }=(i, j, k), " \text { observed } "^{(n)}\right) .
\end{aligned}
$$

## A. 3 Updates

For the EM-updates we need to consider the loglikelihood from Equation (20)

$$
\log L=\sum_{n=1}^{N} \log \sum_{i j k} \beta_{i}^{(n)}(u) \theta_{i k}(u) \beta_{j}^{(n)}(v) \theta_{j k}(v) \pi_{k}(t)
$$

As usual the difficulty is that the logarithm cannot be moved past the inner sum. Thus we assume a distribution $q^{(n)}(i, j, k)=q\left(x_{u}^{(n)}=i, x_{v}^{(n)}=j, x_{t}^{(n)}=k \mid x_{\ln (t)}^{(n)}\right)$ and consider the expected complete data log-likelihood

$$
Q=\sum_{n=1}^{N} \sum_{i j k} q^{(n)}(i, j, k) \log \beta_{i}^{(n)}(u) \theta_{i k}(u) \beta_{j}^{(n)}(v) \theta_{j k}(v) \pi_{k}(t)
$$

$Q$ is then maximized with respect to the parameters $\theta_{i k}(u), \theta_{j k}(v)$ and $\pi_{k}(t)$. For instance for $\pi_{k}(t)$ we take the derivatives of the Lagrangian

$$
Q-C\left(\sum_{k} \pi_{k}(t)-1\right)
$$

where we added a term to enforce $\sum_{k} \pi_{k}(t)=1$. For the other parameters we add similar terms. Equating the derivatives to zero, we obtain the updates for the M-step

$$
\begin{aligned}
\theta_{i k}(u) & \propto \sum_{n=1}^{N} \sum_{j} q^{(n)}(i, j, k)=\sum_{n=1}^{N} q^{(n)}(i, k) \\
\theta_{j k}(v) & \propto \sum_{n=1}^{N} \sum_{i} q^{(n)}(i, j, k)=\sum_{n=1}^{N} q^{(n)}(j, k) \\
\pi_{k}(t) & \propto \sum_{n=1}^{N} \sum_{i j} q^{(n)}(i, j, k)=\sum_{n=1}^{N} q^{(n)}(k)
\end{aligned}
$$

For brevity we write $q^{(n)}(i, k)=\sum_{j} q^{(n)}(i, j, k)$, similarly for $q^{(n)}(j, k)$ and $q^{(n)}(k)$.
The E-step employs the current parameters $\theta$ and $\pi$

$$
\begin{aligned}
q^{(n)}(i, j, k) & =p\left(x_{u}^{(n)}=i, x_{v}^{(n)}=j, x_{t}^{(n)}=k \mid x_{\ln (t)}^{(n)}\right) \\
& =\frac{p\left(x_{u}^{(n)}=i, x_{v}^{(n)}=j, x_{t}^{(n)}=k, x_{\ln (t)}^{(n)}\right)}{p\left(x_{\ln (t)}^{(n)}\right)} \\
& =\frac{\beta_{i}^{(n)}(u) \theta_{i k}(u) \beta_{j}^{(n)}(v) \theta_{j k}(v) \pi_{k}(t)}{\sum_{k} \beta_{k}^{(n)}(t) \pi_{k}(t)}
\end{aligned}
$$

This leads to expressions for the subterms

$$
\begin{aligned}
q^{(n)}(i, k) & =\frac{\beta_{i}^{(n)}(u) \theta_{i k}(u) \pi_{k}(t) \sum_{j} \beta_{j}^{(n)}(v) \theta_{j k}(v)}{\sum_{k} \beta_{k}^{(n)}(t) \pi_{k}(t)} \\
q^{(n)}(j, k) & =\frac{\beta_{j}^{(n)}(v) \theta_{j k}(v) \pi_{k}(t) \sum_{i} \beta_{i}^{(n)}(u) \theta_{i k}(u)}{\sum_{k} \beta_{k}^{(n)}(t) \pi_{k}(t)} \\
q^{(n)}(k) & =\frac{\beta_{k}^{(n)}(t) \pi_{k}(t)}{\sum_{k} \beta_{k}^{(n)}(t) \pi_{k}(t)}
\end{aligned}
$$

Combining these formulas of the E-step with the M-step we get the following multiplicative updates

$$
\begin{aligned}
& \theta_{i k}(u) \propto \theta_{i k}(u) \pi_{k}(t) \sum_{j} \theta_{j k}(v) \sum_{n} \frac{\beta_{i}^{(n)}(u) \beta_{j}^{(n)}(v)}{\sum_{k} \beta_{k}^{(n)}(t) \pi_{k}(t)} \\
& \theta_{j k}(v) \propto \theta_{j k}(v) \pi_{k}(t) \sum_{i} \theta_{i k}(u) \sum_{n} \frac{\beta_{i}^{(n)}(u) \beta_{j}^{(n)}(v)}{\sum_{k} \beta_{k}^{(n)}(t) \pi_{k}(t)} \\
& \pi_{k}(t) \propto \pi_{k}(t) \sum_{i j} \theta_{i k}(u) \theta_{j k}(v) \sum_{n} \frac{\beta_{i}^{(n)}(u) \beta_{j}^{(n)}(v)}{\sum_{k} \beta_{k}^{(n)}(t) \pi_{k}(t)}
\end{aligned}
$$

## APPENDIX B

## Tree REFINEMENT

Tree refinement requires three steps:

1) bottom-up pass to generate $\beta$ messages
2) top-down pass to generate $\alpha$ and $\bar{\alpha}$ messages
3) updating the conditional probability tables (CPTs)

In this section we define the messages as follows

$$
\begin{aligned}
& \beta_{i}(t):=p\left(x_{\text {in }(t)} \mid x_{t}=i\right) \\
& \alpha_{i}(t):=p\left(x_{t}=i \mid x_{\text {out }(t)}\right)
\end{aligned}
$$

Note that in Pearl's notation (1988, see Eqs. (4.15) and (4.16)) our messages $\beta_{i}(t)$ correspond to $\lambda\left(x_{t}\right)=$ $p\left(e_{x_{t}}^{-} \mid x_{t}\right)$ ], and $\alpha_{i}(t)$ correspond to $\pi\left(x_{t}\right)=p\left(x_{t} \mid e_{x_{t}}^{+}\right)$.

## B. 1 Bottom-up propagation

For a leaf $x_{t}$ we have

$$
\beta_{i}(t)= \begin{cases}1 & \text { if } x_{t}=i \text { is observed } \\ 0 & \text { otherwise }\end{cases}
$$

For all other nodes $x_{t}$ we have

$$
\beta_{i}(t)=\prod_{s \in \operatorname{children}(t)} \sum_{j} \theta_{j i}(s) \beta_{j}(s)
$$

## B. 2 Top-down propagation

For the root node we simply copy the current distribution (denoted by $\alpha$ without round brackets)

$$
\alpha_{i}(t)=\alpha_{i}
$$

For children we have

$$
\begin{aligned}
\bar{\alpha}_{k}(t) & \propto \alpha_{k}(\mathrm{pa}(t)) \prod_{s \in \text { siblings }(t)} \sum_{j} \theta_{j k}(s) \beta_{j}(s) \\
\alpha_{i}(t) & =\sum_{k} \bar{\alpha}_{k}(t) \theta_{i k}(t)
\end{aligned}
$$

Note that $\bar{\alpha}_{k}(t)$ needs to be normalized.

## B. 3 Update CPTs

To estimate the parameters $\theta_{i k}$ we need

$$
\begin{aligned}
q(i, k) & =p\left(x_{t}=i, x_{\mathrm{pa}(t)}=k \mid x_{\mathrm{all}}\right) \\
& \propto \beta_{i}(t) \theta_{i k}(t) \bar{\alpha}_{k}(t)
\end{aligned}
$$

Such $q(i, k)$ is calculated for each data vector, thus we write $q^{(n)}(i, k)$. All of these are summed up and normalized, to yield updates for $\theta_{i k}$

$$
\theta_{i k} \propto \sum_{n} q^{(n)}(i, k)
$$

Similarly, for parameter $\pi_{k}$ we have

$$
\begin{aligned}
q(k) & =p\left(x_{\text {root }}=k \mid x_{\text {all }}\right) \\
& \propto \beta_{k}(\text { root }) \alpha_{k} \\
\pi_{k} & \propto \sum_{n} q^{(n)}(k)
\end{aligned}
$$

## ACKNOWLEDGMENTS

We thank Nevin L. Zhang for making compiled code of the algorithm in Zhang and Kočka (2004) available, and Christoph Lampert for generating the vision datasets. We thank the anonymous reviewers for their comments that helped improve the paper; in particular we thank the reviewer who pushed us to formalize the BIN-A algorithm and compare it with BIN-G. Furthermore, SH thanks Dominik Janzing and Hannes Nickisch for general discussion. This work is supported in part by the IST Programme of the European Community, under the PASCAL Network of Excellence, IST-2002-506778. This publication only reflects the authors' views.
