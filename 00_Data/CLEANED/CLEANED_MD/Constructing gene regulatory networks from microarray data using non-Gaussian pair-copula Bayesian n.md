# Constructing gene regulatory networks from microarray data using non-Gaussian pair-copula graphical models 

O. Chatrabgoun<br>Department of Statistics, Malayer University, Malayer, Iran.<br>o.chatrabgoun@malayeru.ac.ir

A. Hosseinian-far<br>Department of Business Systems $\mathcal{E}$ Operations, University of Northampton, NN2 7AL, UK.<br>amin.hosseinian-far@northampton.ac.uk

A. Daneshkhah*<br>Faculty of Engineering, Environment $\mathcal{E}$ Computing, Coventry University, CV1 2JH, UK. ac5916@coventry.ac.uk

Received (Day Month Year)
Revised (Day Month Year)
Accepted (Day Month Year)

Many biological and biomedical research areas such as drug design require analysing the Gene Regulatory Networks (GRNs) to provide clear insight and understanding of the cellular processes in live cells. Under normality assumption for the genes, GRNs can be constructed by assessing the nonzero elements of the inverse covariance matrix. Nevertheless, such techniques are unable to deal with non-normality, multi-modality and heavy tailedness that are commonly seen in current massive genetic data. To relax this limitative constraint, one can apply copula function which is a multivariate cumulative distribution function with uniform marginal distribution. However, since the dependency structures of different pairs of genes in a multivariate problem are very different, the regular multivariate copula will not allow for the construction of an appropriate model. The solution to this problem is using Pair-Copula Constructions (PCCs) which is decomposition of a multivariate density into a cascade of bivariate copula, and therefore, assign different bivariate copula function for each local term. In fact, in this paper, we have constructed inverse covariance matrix based on the use of Pair-Copula Constructions when the normality assumption can be moderately or severely violated for capturing a wide range of distributional features and complex dependency structure. To learn the non-Gaussian model for the considered GRN with non-Gaussian genomic data, we apply modified version of copula-based PC algorithm in which normality assumption of marginal densities is dropped. This paper also considers the Dynamic Time Warping (DTW) algorithm to determine the existence of a time delay relation between two genes. Breast cancer is one of the most common diseases in the world where GRN analysis of

its subtypes is considerably important; Since by revealing the differences in the GRNs of these subtypes, new therapeutic and drugs can be found. The findings of our research are used to construct GRNs with high performance, for various subtypes of breast cancer rather than simply using previous models.

Keywords: Gene regulatory networks; Gaussian graphical models; Dynamic time warping algorithm; Modified PC algorithm; Pair-copula constructions.

# 1. Introduction 

The past few decades have witnessed numerous developments of GRNs using time series gene expression data which is measured by microarray technology ${ }^{1,2}$. The mechanism of genetic regulation and the interactions of genes are crucial in a wide range of biological and biomedical research. If there is a problem in this mechanism, it can lead to a disease as discussed in ${ }^{5}$. One of the benefits of genetic network modelling is to obtain hypotheses for possible relationships between different genes and the role of each gene followed by the practical confirmation of these assumptions ${ }^{3}$. In addition, these networks provide the possibility of comparing the expression patterns of different genes, and so the unknown genes can be guessed ${ }^{3}$.

Since GRNs play an important role in cell processes, numerous methods have been proposed for simulating/modelling GRNs. Among the available techniques linear models, neural networks, (stochastic) differential equations, and the Bayesian networks are more well-known ${ }^{6,7}$. Generally, the existing methods can be classified into three categories. The first category is focused on using association rules to find the regulatory relations between genes ${ }^{8} \cdot{ }^{10}$. Methods belonging to the second category use soft computing approaches to predict GRNs ${ }^{11,12}$. The last category focused on using the probabilistic models, particularly Bayesian network (BN) to predict GRNs. Friedman et al. ${ }^{13}$ were the first to use BNs to study GRNs by analysing using bread gene expression data. Moreover, dynamic Bayesian networks (DBNs) are used to construct GRNs (See ${ }^{10,14,15}$ ).

Under normality assumption for the genes, GRNs can be constructed by assessing the nonzero elements of the inverse covariance matrix (precision matrix) by considering the conditional independencies between genes. In such a model gene $i$ and gene $j$ are conditionally independent if and only if the $(i, j)$ entry in the inverse covariance matrix equals zero. Therefore, much effort has been made to achieve inverse covariance matrix through the use of $L_{1}$ (Lasso) regularization such that it makes sense to impose an $L_{1}$ penalty to increase its sparsity. However, constructing inverse covariance matrix using Lasso are often confined to Gaussian models. This Lasso technique may not reflect the true connectivity between genes when the normality assumption is not accurate. Nevertheless, such techniques are unable to deal with non-normality, multi-modality and heavy tailedness that are commonly seen in current massive genetic data. In fact, the resulting estimates can be inaccurate when the normality assumption is moderately or severely violated, making the techniques unsuitable for dealing with genetic data ${ }^{16}$. To relax this limitative constraint, one can apply copula function which is a multivariate cumulative distribution function

and marginal probability distribution of each variable is uniform. However, since the dependency structures of different pairs of genes in a multivariate problem are very different, the regular multivariate copula will not allow for the construction of an appropriate model. The solution to this problem is using Pair-Copula Constructions (PCCs) which is decomposition of a multivariate density into a cascade of bivariate copula, and therefore, assign different bivariate copula function for each local term which here we have applied the technique of Bauer and Czado (2016). In fact, in this paper, we have constructed precision matrix based on the use of Pair-Copula Constructions (Lasso technique based on the copula function) when the normality assumption can be moderately or severely violated.

In this regard, Elidan ${ }^{18}$ was the first that introduced an innovative by copula function, a marriage between copula functions and graphical models. The combination of copula with graphical model constructs multivariate distribution with univariate marginals and a copula function $C$ that links the marginals. However, the regular copula functions such as Gaussian copula may not be able to accurately depict multi-modal joint distributions in the genomic data ${ }^{16}$. In addition, the nonGaussian probabilistic graphical model is subject to selection of a copula function for each local term.

In this paper, we propose a novel methodology to construct GRNs based on the so-called Pair-Copula Constructions (PCCs) which are merged with graphical models. In fact, PCC is a more flexible multivariate copula which has recently developed for modelling multivariate dependency ${ }^{19,20,21}$. This modelling structure is based on decomposition of a multivariate density into a cascade of bivariate copula. The only restriction of PCC model is the challenge of selecting the best model structure ${ }^{22,23,24}$. This can be fixed by capturing conditional independence in the graphical model. PCCs create a novel class of multivariate statistical models, that combine the distributional flexibility of PCCs with the parsimony of conditional independence models associated with graphical models, which could be used to construct GRNs. The flexibility of these PCCs allows for capturing a wide range of distributional features such as heavy-tailedness, tail dependence, and non-linear asymmetric dependence in genomic data to construct GRNs. Further details about the combination of PCC with graphical models are provided in ${ }^{22,23,24}$. In fact, in this paper, we have constructed precision matrix based on the use of Pair-Copula Constructions (Lasso technique based on the copula function) when the normality assumption can be moderately or severely violated.

The majority of the existing methods for GRNs construction ignore the time delay regulatory relation ${ }^{25}$ between two genes. Hence, in addition to the PCCBNs as a novel method for GRNs construction, we apply Dynamic Time Warping (DTW) that takes the time delay regulatory relation into consideration for GRNs prediction. Therefore, we use DTW, to construct GRNs from microarray datasets. In the other words, the proposed method uses the DTW algorithm to determine the existence of a time delay relation between two genes.

Breast cancer is one of the most common diseases for which many researchers

have been tirelessly working to discover new drugs and treatments. This cancer has several subtypes and each subtype has different therapeutic approaches based on the GRNs. Therefore, analysis of a GRN subtype can be beneficial. Given the mentioned properties of genetic data, we use the method outlined in this paper to analyse different subtypes of breast cancer's GRN.

The paper is organised as follows. In Section 2, we present the PCCs associated with the non-Gaussian BNs of multivariate genomic data. In Section 3, we study some concepts about the breast cancer GRNs and its different subtypes. Moreover, we study the dynamic DTW algorithm to determine the existence of a time delay relation between two genes. The rest of Section 3 include learning Bayesian networks for the breast cancer GRNs using modified version of PC algorithm for non-Gaussian data. In the sequel, we demonstrate breast cancer GRNs construction using described PCCBNs based on the model selection techniques and parameter estimation. A simulation study from constructed GRNs is illustrated in Section 4, and finally we conclude the paper in Section 5.

# 2. Pair-copula construction for non-Gaussian Bayesian networks 

The genes within GRN can be shown as nodes. An interaction between two considered genes can be shown as a directional edge (activation, inhibition). This directional edge actually represents the causal relationship between the two genes. When a specific gene is expressed within the GRNs, due to the causal relationship to the other gene, it can lead to a range activities within the organisms ${ }^{28}$. Therefore, one can use a BN, which is a probabilistic Directed Acyclic Graph (DAG) with Markov property, to model and predict a GRN.

A BN is certainly the most common and applicable probabilistic graphical model to construct and predict GRNs. It represents a set of genes as our random variables and their conditional dependencies via a DAG with Markov property. The preliminary notations of the BNs and their detailed theory with some applications are presented in ${ }^{29}$.

The decomposition of a multivariate distribution can be efficiently implemented benefiting from the conditional independencies offered by a DAG. In a GRN, suppose that gene $i$ is expressed by time series $\left\{X_{i}: i=1,2, \ldots d, d \in \mathbb{N}\right\}$. Then, the density function $f($.$) of d$ genes expression, $\left(X_{1}, \ldots, X_{d}\right)$, can be decomposed as a product of $d$ conditional density functions as:

$$
f\left(x_{1}, \ldots, x_{d}\right)=\prod_{i=1}^{d} f\left(x_{i} \mid p a\left(x_{i}\right)\right)
$$

where $p a\left(x_{i}\right)$ represents the parent set of gene $i$ that is expressed by gene expression $x_{i}$. The density decomposition given in (1) illustrates that once the value of $p a\left(x_{i}\right)$ is learned, knowing the value of the other preceding variables is redundant.

Using copula function, a marriage between copula functions and BNs, conventional BNs models can be extended to a more flexible non-Gaussian BNs. In order

to define copula function, we suppose that gene $i$ is expressed by time series $X_{i}$, $i=1,2, \ldots, d, d \in \mathbb{N}$ with cumulative distribution function (cdf) $F_{i}$. A $d$-variate copula for $d$ considered genes is an cdf on $[0,1]^{d}$ such that all univariate marginals are uniform on the interval $[0,1]$. In fact, every cdf $F$ for $d$ considered genes on $\mathbb{R}^{d}$ with marginals $F_{i}$ can be written as:

$$
F(\mathbf{x})=C\left(F_{1}\left(x_{1}\right), F_{2}\left(x_{2}\right), \ldots, F_{d}\left(x_{d}\right)\right)
$$

for $\mathbf{x}=\left(x_{1}, x_{2}, \ldots, x_{d}\right) \in \mathbb{R}^{d}$, and some suitable copula $C$. If $F$ is absolutely continuous and $F_{1}, \ldots, F_{d}$ are strictly increasing, a similar relationship exists for the probability density function (pdf) $f$ of $F$, namely

$$
f(\mathbf{x})=c\left(F_{1}\left(x_{1}\right), F_{2}\left(x_{2}\right), \ldots, F_{d}\left(x_{d}\right)\right) \prod_{i=1}^{d} f\left(x_{i}\right)
$$

for $\mathbf{x}=\left(x_{1}, x_{2}, \ldots, x_{d}\right) \in \mathbb{R}^{d}$ where the copula pdf $\mathbf{c}$ is uniquely determined (See ${ }^{30}$ for more details about the copula function).

While in recent years numerous bivariate copula families (also known as paircopula families) have been developed, many of these bivariate families have no straightforward multivariate extension. A rich and flexible class of multivariate copulas that uses bivariate (conditional) copulas as building blocks only has recently investigated and applied on the numerous applications in ${ }^{19,21}$. The corresponding decomposition of a multivariate copula into bivariate copulas is called a pair-copula construction (PCC) ${ }^{19}$. The most widely researched copulas arising from PCCs are the vine copulas. These vine copulas admit a graphical representation called a regular vine (R-vine), which consists of a sequence of trees, each edge of which is associated with a certain pair copula in the PCC ${ }^{30,19}$.

There have been several attempts to develop a method through using the nice properties of both graphical model and vine model, simultaneously. The main purpose is to benefit from the conditional independence in the graphs and the vine structure. This gap was filled in ${ }^{22}$ and ${ }^{23}$ by introducing non-Gaussian graphical model by combining useful properties of both pair-copula and DAG which was then called non-Gaussian PCCBNs.

Bauer et al. ${ }^{22}$ and Bauer and Czado ${ }^{23}$ by merging PCCs with (1), illustrate how the multivariate density given in (1) can be represented in terms of the PCC model. They suppose $D=(V, E)$ to be a DAG for a considered GRN with vertex set $V$ and edge set $E$, and let $f$ be a multivariate density function on $d$ genes with marginal density $f_{i}$ and the corresponding cumulative distribution function (CDF) $F_{i}, i=1,2, \ldots, d$. Then $f$ is uniquely determined by its univariate margins $f_{i}, \quad i=1,2, \ldots, d$; its conditional pair-copula $c_{v w \mid p a(v, w)}, v \epsilon V, w \epsilon p a(v)$ and $f$ can be decomposed as:

$$
\begin{aligned}
& f\left(x_{1}, \ldots, x_{d}\right) \quad=\prod_{v=1}^{d} f\left(x_{v}\right) \\
& \times \prod_{w \in p a(v)} c_{v w \mid p a(x, w)}\left(F_{v \mid p a(v, w)}, F_{w \mid p a(v, w)}\right) .
\end{aligned}
$$

Such that $p a(x, w) \in E$ stands for an arrow $x \longrightarrow w$. By making suitable choices of marginal densities and pair-copula functions, the above presentation given in (2) provides us with an approach for the multivariate density. However, in practice, we have to use copula from a convenient class, and this class can be selected by criteria such as AIC and maximum likelihood (ML) and model selection techniques (For more explanations see ${ }^{22,23}$ ). In the following sections, we address this issue in more details to construct breast cancer GRNs.

# 3. Data Analysis: Breast Cancer Gene Regulatory Network 

Breast cancer first develops from breast tissue and usually there are signs such as a mass in a breast, deformity in a breast, nasal discharge in a breast, secretion of fluid from a nipple, and so on, while many breast cancers have no obvious symptoms at all. Therefore, analysis of the GRNs for the breast cancer tumors is critical. On the other hand, breast cancer as a heterogeneous disease has multiple distinct molecular subtypes which depend on different therapies. There are 4 subtypes of breast cancer based on gene expression profiles: Basal-like (Basal), HER2-enriched (Her2), Luminal A (LumA), and Luminal B (LumB) ${ }^{31}$. LumA cancers are hormone-receptor positive (estrogen-receptor and/or progesterone-receptor positive) and Her2 negative. Her2-enriched cancers are hormone-receptor negative (estrogen-receptor and progesterone-receptor negative) and Her2 positive. LumA cancers tend to grow slowly and have the good prognosis, while basal-like cancers tend to grow fast and have poor prognosis. Therefore, in this section we intend to construct and compare the GRN of these breast cancer subtypes using the method outlined in this paper. It is hoped that this research could be a guide for various researchers to treat various subtypes of breast cancer.

Consider a real data set containing gene expression measurements from breast tumors, obtained from the Cancer Genome Atlas (TCGA) project ${ }^{32}$. The primary goal is to understand the underlying patterns of GRN variation among tumors in different subtypes of breast cancer: Basal, Her2, LumA, and LumB. Therefore, we will have the gene expression information of disease subtype for each tumor. We may regard cancer subtypes as a partial driver of the underlying structure of the gene expression data ${ }^{2}$. Samples from the same subtype will share common genetic variations. The raw data set contains 17814 genes and 343 samples. Out of the 343 samples, there are 4 subtypes of breast cancer with different number of 450 samples in each subtype: Her2 (42), Basal (66), LumA (154) and LumB (81). We preprocessed the data in the same way as in ${ }^{33}$. We first imputed missing values with the $k$-nearest neighbours algorithm $(k=10)$, then removed genes with low variations across samples (standard deviation smaller than 1.8), and finally mean centred each gene. The result is a 455 column-centred data matrix $X$ with 343 samples and 645 genes.

Another widely cited characteristic of GRN is their abundance of certain repetitive sub-networks known as network motifs. In fact in many cases, due to the large

size of a GRN, the researchers examine an important sub-network that has been frequently repeated within the main network. Network motifs can be regarded as repetitive topological patterns when dividing a large network into smaller blocks ${ }^{34}$. Therefore, given that the GRN associated with breast cancer tumors is typically very large, we shall examine the considered motif for different subtypes of the breast cancer tumor using the method proposed within this paper, i.e. the non-Gaussian PCCBNs. The raw data set contains 17814 genes and 348 samples. We preprocessed the data in the same way as in Lock and Dunson (2013). We first imputed missing values with the k-nearest neighbors algorithm $(\mathrm{k}=10)$, then removed genes with low variations across samples (standard deviation smaller than 1.8), and finally mean centered each gene. The result is a column-centered data matrix X with 348 samples and 10 genes. Note that by reducing the standard deviation of the studied genes, the less effective genes are incorporated into the model and the model components become significantly larger such that eventually leading to an inefficient model. The motif has been selected through an approach explained in ${ }^{34}$, and it consists of 10 genes (EYA2, PRC1, TACC3, GSTP1, AQP5, CSDA, EFS2, TPM2, $B C L 2$ and $H E C$ ). Hereafter, we denote these genes by $G 1$ to $G 10$, for readers' convenience. Figure 1 shows gene expression for different subtypes of breast cancer tumor Her2, Basal, LumA and LumB, individually. We first examine whether or not the gene expression data for the Her2 subtype follow a Gaussian distribution. The result of descriptive statistics and Kolmogorov-Smirnov normality test are reported in Table 1. As it is evident, the null hypothesis of normality for some genes are rejected ( $p$-value is less than $5 \%$ significance level). Thus, a flexible and effective modelling is needed to model both non-Gaussian distributions and complex dependency structure between genes. Similarly, patterns can be used for other subtypes.

Table 1. Descriptive statistics and Kolmogorov Smirnov test for genes of Her2 breast cancer subtype


![img-0.jpeg](img-0.jpeg)

Fig. 1. gene expression for different subtypes of breast cancer tumor: Basal, Her2, LumA and LumB

# 3.1. Dynamic Time Warping 

To construct GRNs, when the gene $A$ is expressed, it takes a certain amount of time to express the gene $B$; therefore there will be a time delay. In many previous studies ${ }^{26,17,27}$ during GRN construction, the time delay regulatory relation ${ }^{25}$ between two genes has been ignored. We therefore consider the time delay regulatory relation for constructing GRNs using PCCBNs. This can be done using Dynamic Time Warping (DTW) which is a popular technique for comparing time series, providing both a distance measure that is insensitive to local compression and stretches, and the warping which optimally deforms one of the two input series onto the other.

DTW was first introduced in ${ }^{35}$. It has been employed for clustering gene expressions ${ }^{36,37}$. After stretching, the distance between the two genes is computed, by summing the distances of individual aligned elements. Suppose that $X=\left(x_{1}, x_{2}, \ldots, x_{n}\right)$ and $Y=\left(y_{1}, y_{2}, \ldots, y_{m}\right)$ are two gene expression with lengths equal to $n$ and $m$, respectively. Also suppose that a non-negative, local dissimilarity function $\gamma$ is defined between any pair of elements $x_{i}$ and $y_{j}$ by $D(i, j)=\gamma\left(x_{i}, y_{j}\right) \geq 0$. The most common choice for $\gamma(\cdot, \cdot)$ is to assume the Euclidean distance. DTW finds a vector of ordered pair denoted $\phi_{k}$, warping curve, for $k=1,2, \ldots, T$ such that $\phi(k)=\left(\phi_{x}(k), \phi_{y}(k)\right)$, with $\phi_{x}(k) \in\{1,2, \ldots, n\}$ and $\phi_{x}(k) \in\{1,2, \ldots, m\}$. The warping functions $\phi_{x}$ and $\phi_{y}$ remap the time indices of $X$ and $Y$, respectively. Given $\phi$, we compute the sum accumulated distortion

between the warped gene expression $X$ and $Y$ by

$$
d_{\phi}(X, Y)=\sum_{k=1}^{T} d\left(\phi_{x}(k), \phi_{y}(k)\right)
$$

To ensure reasonable warps, constraints are usually imposed on $\phi$. For instance, monotonicity is imposed to preserve their time ordering and avoid meaningless loops such that $\phi_{x}(k+1) \geq \phi_{x}(k), \& \phi_{y}(k+1) \geq \phi_{y}(k)$. The idea underlying DTW is to find the optimal alignment $\phi$ such that

$$
D(X, Y)=\min _{\phi} d_{\phi}(X, Y)
$$

This minimization rule is fully described in literature ${ }^{38}$. Package "dtw" in $R$ software provides a unification to compute and visualize DTW alignments ${ }^{39}$. Usually, two- and three-way plots are used to inspect the gene expression data along with their alignment. One intuitive alignment visualization style places both time series in the same plane, and connects the matching point pairs with segments. Another effective layout to display alignments places a gene expression data (G1) horizontally in a small lower panel, the other gene expression data vertically on the left; a larger inner panel holds the warping curve. Hence, the matching points can be recovered by tracing indices on gene G1, moving upwards until the warping curve is met, and then moving leftwards to discover the index of matched gene G2. One of the advantages of this method is the clear visualization.

The above pattern can now be used to determine time delay in breast cancer gene expression data. For instance, two and three way plots can be used to show the alignment for gene G1 and G2 in breast cancer Her2 subtype as presented in Figure 2 (a) and (b), respectively.
![img-1.jpeg](img-1.jpeg)

Fig. 2. Two (a) and three (b) way plot for gene expression alignment using DTW for Her2.

# 3.2. Learning Bayesian networks for the breast cancer GRNs 

Understanding causal relationships between genes is the primary goal in GRNs. A convenient approach for learning BNs in genetics is the use of expert knowledge. This method is ineffective since the elicitation process for such complex problems is very lengthy and almost impractical. Therefore, alternatively, the computational algorithms which can be implemented based on the existing gene expression data are used. The high dimensionality of the data sets-common in GRNs have led to the development of several learning algorithms focused on reducing computational complexity yet discovering the correct network. These algorithms provide us with invaluable information/statistics about the genes that could or could not be a cause of other genes of interest.

In our method, we initially apply a modified version of PC-algorithm ${ }^{41}$ which Gaussian assumption of the marginal distribution is dropped. In other words, we provide an algorithm to approximate the network structure. In particular, this algorithm is well suited to determine a DAG structure of the non-Gaussian continuous variables constituting different subtypes of breast cancer GRNs. In the conventional version of the PC algorithm, a series of tests for conditional independence is performed given the normality assumption of marginals. Alternatively, we shall introduce a novel class of conditional independence tests that are particularly tailored for the algorithm and are applicable to non-Gaussian continuous data. In a Gaussian framework, the test of choice was usually a test for zero partial correlation (see ${ }^{42}$ ). We therefore need to introduce an equivalent of this test for the non-Gaussian case.

Suppose $P$ is an absolutely continuous probability measure with Markov property for a DAG $(V, E)$ on $[0,1]^{d}$ with uniform univariate marginal distributions. Moreover, let $\mathbf{u}=\left\{\mathbf{u}^{1}, \ldots, \mathbf{u}^{n}, n \in \mathbb{N}\right\}$ be a random sample realisation of $\left\{\mathbf{U}^{1}, \ldots, \mathbf{U}^{n}\right\}$ from a random variable $\mathbf{U}$ distributed as $P$. Considering the PC algorithm, for all distinct vertices $i, j \in V$ and chosen vertex sets $K \in V \backslash i, j$, the null hypothesis $H_{0}: U_{i} \perp U_{j} \mid \mathbf{U}_{\mathbf{K}}$ is tested against the general alternative $H_{1}: U_{i} \perp U_{j} \mid \mathbf{U}_{\mathbf{K}}$ of conditional dependence. Given a suitable independence test of choice, we should therefore determine $H_{0}$ and $H_{1}$ at significance level $\alpha$. By confirming $H_{0}$, we remove the edge $i-j$ from considered DAG. In a Gaussian framework, the null hypothesis is then translated into $H_{0}: \rho_{i j-K}\left(X_{i}, X_{j} ; X_{K}\right)=0$, where $X_{k}:=\Phi^{1}\left(U_{k}\right)$ for all $k \in V$, and $\Phi$ denotes the univariate standard normal cdf. In fact, conditional independence test is translated to the test for zero partial correlation under the assumption of joint normality. We will now introduce a copula-based alternative test for conditional independence that is also applicable to non-Gaussian continuous data. Let $F_{i, j \mid K}\left(., . \mid \mathbf{v}_{\mathbf{K}}\right)$ denote the conditional cdf of $U_{i}$ and $U_{j}$ given $\mathbf{U}_{\mathbf{K}}=\mathbf{v}_{\mathbf{K}}$, and let $C_{i, j \mid K}\left(., . \mid \mathbf{v}_{\mathbf{K}}\right)$ be the corresponding conditional copula. Moreover, let $C_{\perp}$ denote the independence copula on $[0,1]^{2}$. The conditional independence $U_{i} \perp U_{j} \mid \mathbf{U}_{\mathbf{K}}$ holds if and only if

$$
F_{i, j \mid K}\left(v_{i}, v_{j} \mid \mathbf{v}_{\mathbf{K}}\right)=C_{i, j \mid K}\left(F_{i \mid K}\left(v_{i} \mid \mathbf{v}_{\mathbf{K}}\right), F_{j \mid K}\left(v_{j} \mid \mathbf{v}_{\mathbf{K}}\right) \mid \mathbf{v}_{\mathbf{K}}\right)
$$

$$
=F_{i \mid K}\left(v_{i} \mid \mathbf{v}_{\mathbf{K}}\right) F_{j \mid K}\left(v_{j} \mid \mathbf{v}_{\mathbf{K}}\right)
$$

for all $v_{i}, v_{j} \in[0,1]$ and $\mathbf{v}_{\mathbf{K}} \in[0,1]^{|K|}$. Therefore, the null hypothesis of the conditional independence test can be stated as $H_{0}^{*}: C_{i, j \mid K}\left(\ldots \mid \mathbf{v}_{\mathbf{K}}\right)=C_{\perp}(\ldots)$. The new null hypothesis $H_{0}^{*}$ can be tested ${ }^{43}$ for the transformed observations $W_{i \mid K}^{1}, \ldots, W_{i \mid K}^{1}$ and $W_{j \mid K}^{1}, \ldots, W_{j \mid K}^{1}$, where

$$
W_{i \mid K}^{k}:=F_{i \mid K}\left(U_{i}^{k} \mid \mathbf{U}_{K}^{k}\right), \quad \text { and } \quad W_{j \mid K}^{k}:=F_{j \mid K}\left(U_{j}^{k} \mid \mathbf{U}_{K}^{k}\right)
$$

for all $k \in 1, \ldots, n$. In practice, with regards to DAG selection for non-Gaussian data, we can substitute the function gaussCItest in the function $p e$ from pealg with the independence test of Genest and Favre ${ }^{44}$. This is the modified version of $P C$ algorithm for the non-Gaussian data by the use of copula function property; such that we have used the functions CDVineCopSelect and BiCopHfunc, implemented in the CDVine package, to compute the Rosenblatt transforms ${ }^{43}$, and a significance level of $\alpha$ in the independence tests.

We are now in a position to create a GRN as a non-Gaussian BN for different subtypes of the breast cancer in order to reveal their differences. Therefore, by following the discussed approach for gene expression data of each breast cancer subtype, we can create the GRN. The related GRN for the Her2 breast cancer subtype is illustrated in Figure 3 (a). In addition, this GRN for the other subtypes Basal, LumA, and LumB is presented in Figure 3 (b), (c) and (d), respectively. As it is evident, the number of edges in the Basal and Her2 subtypes is 12, while the LumA and LumB subtypes have 11 edges. In Basal subtype, in comparison to Her2, there exists edge G7 $\longrightarrow$ G3, while in Her2 this edge is removed, and instead, unlike Basal, G7 $\longrightarrow$ G8 is active. LumA and LumB are quite similar to each other. However, as shown in Figure 3, there are obvious differences with other subtypes. For example, G3 $\longrightarrow$ G8 is active in Basal while there is no such edge in LumA and LumB. Furthermore, instead of G7 $\longrightarrow$ G3, in Basal there are two edges G3 $\longrightarrow$ G8 and G7 $\longrightarrow$ G8. As discussed earlier, one of the most important principles in constructing GRNs is to distinguish active and inhibit genes; this can be done by adding and merging PCCs to the constructed DAGs for different breast cancer subtype. We explain this within the next subsection.

# 3.3. Model selection 

Given the derived non-Gaussian DAG for different subtypes of breast cancer, we can decompose the multivariate density of our data by merging BNs with PCCs in order to derive PCCBNs model. We fully explain this matter for subtype Her2 and only present the final model for the rest of breast cancer subtypes.

Note that gene G8 has 4 parents (G3, G5, G6, G7) as the order of the parents is based on the heuristic rule of modelling strong bivariate dependences prior to weak dependences. Our decision was based on $\hat{\tau}$ of Kendall's estimates between the variables: $\hat{\tau}_{G 8, G 3}=0.248, \hat{\tau}_{G 8, G 5}=0.269, \hat{\tau}_{G 8, G 6}=0.155$, and $\hat{\tau}_{G 8, G 7}=-0.145$. A similar rule can be applied for gene G4 and its parents G2 and G3. The estimated

![img-2.jpeg](img-2.jpeg)
(a) Her2
![img-3.jpeg](img-3.jpeg)
(c) LumA
![img-4.jpeg](img-4.jpeg)
(b) Basal
![img-5.jpeg](img-5.jpeg)
(d) LumB

Fig. 3. The GRN for different breast cancer subtypes.
$\tau$ 's Kendall between G4 and its parents G2 and G3 are: $\hat{\tau}_{G 4, G 2}=0.399$ and $\hat{\tau}_{G 4, G 3}=$ -0.129 . The estimated $\tau$ 's Kendall between gene G9 and its parents G2 and G7 are reported as $\hat{\tau}_{G 9, G 2}=0.252$, and $\hat{\tau}_{G 9, G 7}=0.142$. Based on these ordering, the resulting multivariate density decomposition using (2) is given by:

$$
\begin{gathered}
f_{1, \ldots, 10}\left(x_{1}, \ldots, x_{10}\right)=\prod_{i=1}^{10} f_{i}\left(x_{i}\right) \times c_{21}\left(F_{1}\left(x_{1}\right), F_{2}\left(x_{2}\right)\right) \times \\
c_{6,10}\left(F_{6}\left(x_{6}\right), F_{10}\left(x_{10}\right)\right) \times c_{42}\left(F_{2}\left(x_{2}\right), F_{4}\left(x_{4}\right)\right) \times \\
c_{92}\left(F_{2}\left(x_{2}\right), F_{9}\left(x_{9}\right)\right) \times c_{10,2}\left(F_{2}\left(x_{2}\right), F_{10}\left(x_{10}\right)\right) \times \\
c_{53}\left(F_{5}\left(x_{5}\right), F_{3}\left(x_{3}\right)\right) \times c_{85}\left(F_{5}\left(x_{5}\right), F_{8}\left(x_{8}\right)\right) \times \\
c_{97 \mid 2}\left(F_{7 \mid 2}\left(x_{7} \mid x_{2}\right), F_{9 \mid 2}\left(x_{9} \mid x_{2}\right)\right) \times \\
c_{83 \mid 5}\left(F_{3 \mid 5}\left(x_{3} \mid x_{5}\right), F_{8 \mid 5}\left(x_{8} \mid x_{5}\right)\right) \times \\
c_{43 \mid 2}\left(F_{3 \mid 2}\left(x_{3} \mid x_{2}\right), F_{4 \mid 2}\left(x_{4} \mid x_{2}\right)\right) \times
\end{gathered}
$$

$$
\begin{gathered}
c_{86 \mid 35}\left(F_{6 \mid 35}\left(x_{6} \mid x_{3}, x_{5}\right), F_{8 \mid 35}\left(x_{8} \mid x_{3}, x_{5}\right)\right) \times \\
c_{87 \mid 356}\left(F_{7 \mid 356}\left(x_{7} \mid x_{3}, x_{5}, x_{6}\right), F_{8 \mid 356}\left(x_{8} \mid x_{3}, x_{5}, x_{6}\right)\right)
\end{gathered}
$$

Considering the model selection techniques for the non-Gaussian PCCBNs $\left({ }^{22,23,20}\right)$, we can determine the best fitted copulas to any bivariate distribution in (3). For this purpose, we use the package CDVine and apply the function Bi copSelect to the selected best fitted bivariate copulas. This also provides us with the estimates of the parameters and Kendall's $\tau$ for each copula. The results of the fitted

Table 2. Maximised log-likelihoods and parameters value for the Gaussian and non-Gaussian PCCBNs corresponding to the Her2 Brest cancer subtypes


non-Gaussian PCCBN model and Gaussian BN are presented in Table 2. Some of the selected copula functions have two parameters, hence the second parameter is added in brackets. Note that each conditional distribution (or copula) in the Gaussian BN model must be normally distributed. Results, based on Log-Likelihood (LL) and AIC criteria, suggest that the non-Gaussian PCCBN model is much better fit to Her2 breast cancer subtype. As discussed, the flexibility of PCCBNs allow for capturing a wide range of distributional features and complex dependency structure such as heavy-tailedness, tail dependence, and non-linear, asymmetric dependence in the constructed GRN for Her2 subtype. One approach to present these features is contour plot. The contour plots for the estimated copula are presented in Figure 4. As it can be seen from these contour plots, the occurrence of extreme events in some pair of genomic data is evident. Also, in order to study the occurrence of extreme events in genomic data, the pair-wise analysis of upper (U) and lower (L) tail dependence (TD) of the gene expression variables can be implemented using the fitted copula models ${ }^{30,45}$. The computed coefficients of upper and lower tail dependence of any two gene expression variables are presented in Table 2. In genetic data, it is crucial to consider the tail-dependence coefficient in modelling of

![img-6.jpeg](img-6.jpeg)

Fig. 4. Contur plot for the estimated copula function of Her2 subtype.
joint GRN construction ${ }^{45}$. Otherwise, it can lead to a serious misspecification of GRNs' structures. Therefore, computing the tail dependence coefficients as precise as possible can provide an accurate interpretation of the constructed GRN accurately. The resulted contour plots for the estimated copula confirms the obtained calculations in Table 2. As an example, the contour plot, demonstrated in Figure 4, between $G 3$ and $G 8$ given $G 5$ confirms the calculated TD in this table. The final

Table 3. Maximised log-likelihoods, numbers of parameters, and AIC values for the Gaussian and non-Gaussian PCCBNs corresponding to the different Breast cancer subtypes


![img-7.jpeg](img-7.jpeg)

Fig. 5. The final GRN for different breast cancer subtypes.
results for the other subtypes of breast cancer based on the LL and AIC criteria in Table 3 confirms our claims about the superiority of non-Gaussian PCCBN versus Gaussian BN.

Using Kendall's $\tau$ correlation criterion obtained from fitted copula function between two interested genes, it can be shown which genes deactivate others. A simple rule in this is that if Kendall's $\tau$ correlation coefficient of the fitted copula between two interested genes is negative, then the two genes inhibit each other. Final GRN's for each subtype of breast cancer, following coefficient calculations using a copula function, are shown in Figure 5. For instance, in Figure 5 (a) for Her2 subtype, G1 deactivate G2 (dashed line), and G6 deactivate G8. Similar pattern is repeated for Basal. The difference between the two structures is that in Her2, G3 deactivate G8, while in Basal G5 deactivate G8. Moreover, LumA and LumB cn be easily compared visually. In fact, such network construction for various breast cancer subtypes-with activated and inhibited genes-can help to discover new drugs, new treatments, and even new preventive approaches.

# 4. Simulation 

First, we follow the simulation method proposed in ${ }^{30}$ which is based on the sampling of the cumulative distributions and is widely known as the probability integral transform (PIT). This simulation method has later been followed by ${ }^{22,23}$. The same simulation method is used in ${ }^{20}$ to draw samples from the approximated PCCBNs where data availability is very limited. The sampling strategy, based on the PIT is as follows: 1) sample from two independent variables, denoted by $U_{1}, U_{2}$ and distributed uniformly on $[0,1] ; 2)$; then calculate values of the original variables using the following equations:

$$
x_{1}=u_{1}, \quad x_{2}=F_{2 \mid 1}^{-1}\left(u_{2} \mid x_{1}\right)
$$

where $x_{i}$ 's and and $u_{i}$ 's are realization values of $X_{i}$ 's and $U_{i}$ 's respectively. Finally, this can be easily continued to all variables within the PCCBN considering a similar argument ${ }^{20,19,24}$.

One of the effective measures to evaluate the performance of non-Gaussian PCCBN against Gaussian BN in the construction of GRN of interest, is the $F$-score which is defined as:

$$
F=\frac{2 p r}{p+r}
$$

where $p$ and $r$ denote precision and recall, respectively. They can be computed using the following equation:

$$
p=\frac{T P}{T P+F P} \quad \text { and } \quad r=\frac{T P}{T P+F N}
$$

where $T P$ is true positive, $F P$ is false positive and $F N$ is false negative. $T P s$ denote the number of the edges that are inferred by the GRN algorithm that actually exist within the true network. $F P s$ are the edges inferred by the GRN algorithm however do not actually exist in the true network. $F N$ edges actually exist in the true network but cannot be inferred by the GRN algorithm. The use of truly and falsely inferred edges (TPs and FPs) only is not sufficient to measure the performance of the underlying model fairly. Missing edges (FNs) in the final network should also be considered in the performance evaluation process. Since the $F$-score given in Eq. (4) takes into account all types of edges, it is a more reliable measure for completely known networks (mostly the synthetic ones). Table 4 presents F-scores for non-Gaussian PCCBN versus Gaussian BN associated with reconstruction of the different breast cancer subtypes. It can be observed that the F-score of the GRNs for different subtype reconstructed based on the non-Gaussian PCCBN is significantly greater that the ones reconstructed using the Gaussian BN.

## 5. Conclusions

The Gaussian graphical models with Markov property, in particular BNs, have been widely used in modelling gene regulatory networks in many research studies such as

Table 4. The $F$-score evaluation of the reconstructed GRN for different breast cancer subtypes.


detecting the activator genes of the genetic diseases, determining the functions of the regulating and regulated genes, obtaining the drug targets of the medical cures, etc. The main drawback of the Gaussian BN models is that the normal assumption of data in most of these applications is not realistic, and the inferred networks will be misleading if the data distributions are non-Gaussian. In the present paper, we propose a novel method of constructing GRNs based on the PCCBN models which benefit from the computational power and flexibility of the PCC models and the parsimony of conditional independence concepts of the BNs. We demonstrated that the effectiveness of using the PCCBNs in constructing GRN where the marginal and conditional distributions are not normal. In addition, we adopted the PC algorithm to select the best network structure for the GRNs of interest by considering the conditional independence/dependence extracted from the considered BN and PCC models. Furthermore, we demonstrated that the flexibility of PCCBNs allow for capturing a wide range of distributional features with the complex dependency including the tail dependence, non-linear, and asymmetric dependence which are common in the underlying GRNs. We also compared the proposed non-Gaussian PCCBNs with Gaussian BN based on various goodness-of-fit measures and the $F$-score which is a combination measure of TP, FP, and FN. The results clearly suggest that the non-Gaussian PCCBN outperformed Gaussian BN based on the aforementioned criteria illustrated in Tables 3 and 4.
