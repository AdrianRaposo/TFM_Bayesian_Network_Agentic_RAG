# HHS Public Access 

Author manuscript
Proc Data Compress Conf. Author manuscript; available in PMC 2017 October 16.
Published in final edited form as:
Proc Data Compress Conf. 2017 April ; 2017: 455-. doi:10.1109/DCC.2017.82.

## Compressing Tabular Data via Pairwise Dependencies

Dmitri S. Pavlichin ${ }^{1}$, Amir Ingber ${ }^{2}$, and Tsachy Weissman ${ }^{1}$<br>${ }^{1}$ Stanford University<br>${ }^{2}$ Yahoo! Research


#### Abstract

Tabular datasets, such as server logs, business transactions, social media interactions and more, are very commonly generated and maintained across industries and organizations. Generic lossless compression algorithms, such as Lempel-Ziv and variants, are fast and robust, but do not exploit the unique structure of the data that can be learned from the source file. Previous work in this setting includes [1, 2] and references therein.


We propose a method and algorithm for lossless compression of tabular data, based on a method known as a Chow-Liu tree [3] with a minimum description length-like criterion for graph selection. The "vanilla" Chow-Liu tree approach captures pairwise dependencies between different columns (or more generally fits a Bayesian network to the dataset) by entropy coding with respect to a maximum spanning tree Bayesian network model on the features, with edge weights given by the empirical mutual informations $\hat{\boldsymbol{\ell}}\left(\boldsymbol{X}_{p} \boldsymbol{X}_{j}\right)$ between the features $\boldsymbol{X}_{p} \boldsymbol{X}_{j}$. We improve on the Chow-Liu choice of tree by modifying the edge weights to account for the space to store the model description "metadata" - the pairwise joint empirical distributions - since in practice this cost can be large. Our choice of Bayesian network graph is $T^{*}$, optimized over all forest graphs $T=(V, E)$ on the features:

$$
T^{*}=\arg \max _{T=(V, E)} \sum_{(i \rightarrow j) \in E}\left(n \tilde{I}\left(X_{i} ; X_{j}\right)-\sum_{(i \rightarrow j) \in E}\left|c_{n}\left(\hat{p}_{i, j}\right)\right|\right)
$$

where $n$ is the number of rows in the file and $\left|c_{n}\left(\hat{p}_{i, j}\right)\right|$ denotes the length of an encoding $c_{n}$ of an empirical pairwise joint histogram $\hat{p}_{i, j}$.

Our algorithm benefits from several features combined in a novel way: 1) efficient encoding of the (often sparse) empirical distributions by a combination of Golomb and arithmetic coding; 2) memory-efficient empirical mutual information approximation using hashing; 3) special handling of the (often many) values that occur only once in a file.

We test the algorithm on several datasets, and demonstrate an improvement in the compression rates of between 2 X and 5 X compared to gzip, columnar gzip, and bzip2. The larger improvements are observed for very large datasets, such as the Criteo click prediction dataset which was published as part of a recent Kaggle competition: 736MB vs 3.76GB for gzip.
