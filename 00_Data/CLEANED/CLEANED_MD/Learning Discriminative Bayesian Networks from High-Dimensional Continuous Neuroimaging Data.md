# HHS Public Access 

Author manuscript
IEEE Trans Pattern Anal Mach Intell. Author manuscript; available in PMC 2017 November 30.

Published in final edited form as:
IEEE Trans Pattern Anal Mach Intell. 2016 November ; 38(11): 2269-2283. doi:10.1109/TPAMI. 2015.2511754.

## Learning Discriminative Bayesian Networks from Highdimensional Continuous Neuroimaging Data

Luping Zhou,<br>School of Computing and Information Technology, University of Wollongong, NSW 2500, Australia

## Lei Wang,

School of Computing and Information Technology, University of Wollongong, NSW 2500, Australia

## Lingqiao Liu,

Shool of Computer Science, University of Adelaide, Australia
Philip Ogunbona, and
School of Computing and Information Technology, University of Wollongong, NSW 2500, Australia

## Dinggang Shen

Department of Radiology, University of North Carolina at Chapel Hill, USA


#### Abstract

Due to its causal semantics, Bayesian networks (BN) have been widely employed to discover the underlying data relationship in exploratory studies, such as brain research. Despite its success in modeling the probability distribution of variables, BN is naturally a generative model, which is not necessarily discriminative. This may cause the ignorance of subtle but critical network changes that are of investigation values across populations. In this paper, we propose to improve the discriminative power of BN models for continuous variables from two different perspectives. This brings two general discriminative learning frameworks for Gaussian Bayesian networks (GBN). In the first framework, we employ Fisher kernel to bridge the generative models of GBN and the discriminative classifiers of SVMs, and convert the GBN parameter learning to Fisher kernel learning via minimizing a generalization error bound of SVMs. In the second framework, we employ the max-margin criterion and build it directly upon GBN models to explicitly optimize the classification performance of the GBNs. The advantages and disadvantages of the two frameworks are discussed and experimentally compared. Both of them demonstrate strong power in learning discriminative parameters of GBNs for neuroimaging based brain network analysis, as well as maintaining reasonable representation capacity. The contributions of this paper also include a new Directed Acyclic Graph (DAG) constraint with theoretical guarantee to ensure the graph validity of GBN.


## Index Terms

Bayesian network; discriminative learning; Fisher kernel learning; max-margin; brain network

# 1 Introduction 

As an important probabilistic graphical model, Bayesian network (BN) has been used to model the probability distribution of a set of random variables for a wide spectrum of applications, e.g., diagnosis, troubleshooting, web mining, meteorology and bioinformatics. It combines graph representation with Bayesian analysis, providing an effective way to model and infer the conditional dependency of the variables. A BN has to be a directed acyclic graph (DAG). Two factors characterize a BN, i.e., the structure of the network (the presence/absence of edges in the graph) and the parameters of the probability distribution. Recent research of BN focuses on how to learn the structure and the parameters of BN directly from the data.

The approaches of learning BN structures can be roughly categorized into the constraintbased, the score-based, and the hybrid approaches. The constraint-based approaches use a serie of conditional independence testing to ensure the model structure is consistent with the conditional independency entailed by the observations. Methods in this class include the IC algorithm [1], PC algorithm [2], and more recent methods [3], [4]. Score-based approaches define a scoring function over the space of candidate DAGs and optimize this function through certain search strategies. Methods in this class vary with scoring criteria, e.g., the posterior probability [5], [6], [7] and the minimum description length [8], or vary with search strategies, e.g., the heuristic search [9] and the Monte Carlo methods [5]. Hybrid approaches usually employ constraint-based methods to prune the search space of DAG structures and consequently restrict a subsequent score-based search [10], [11]. Many existing BN learning methods, such as LIMB-DAG [12], MMHC [10], TC and TC-bw [13], comprise of two stages: the identification of candidate parent sets in the first stage and the further pruning of them based on certain criteria in the second stage. Despite the mitigation of computational complexity, a drawback arises that if a parent node is missed in the first stage, it will never be recovered in the second stage [14]. To address this issue, one-stage learning process has been preferred in recent research work [14], [15]. In these studies, based on Gaussian Bayesian network (GBN), the parent sets of all variables are learned together to optimize a LASSO-based score function in a single stage. The related optimization problems are solved either approximately [14] or exactly [15]. They have demonstrated improved reliability of BN edge identification over traditional two stage methods.

Although BN is naturally a generative method, it has also been used in classification tasks for diagnostic or predictive purposes. A straightforward usage is to train each class a BN and classify a new sample into the class with the highest likelihood value [14]. Another kind of approaches trains "Bayesian network classifiers" with discriminative objective functions [16], [17], [18]. In these approaches, usually a single BN is learned to optimize the discrimination performance. Either the structure or the parameters of the BN are adjusted to reflect the class difference for better classification. Therefore, the resulting BN does not model the distribution of any individual class. The "Bayesian network classifiers" in [16], [17], [18] are designed for discrete variables of multinomial distribution. They still inherit the two-stage learning process, i.e., have to predefine candidate parent sets as mentioned above.

Learning BN from the data faces new challenges in exploratory domains, such as brain research, where the mechanism of brain and mental diseases remain unclear and need to be explored. These domains usually cater for both interpretation and discrimination. "Interpretation" requires interpretable models of the data and the findings explained by domain language rather than mathematical terms. This requirement comes from the demand of understanding the domain problems. "Discrimination" requires the models to have sufficient discriminative power to distinguish groups of interest (such as identifying the diseased from the healthy), for the purpose of prediction. To some extent, a high accuracy of the predictive model also provides a measure of the amount of information captured by that model.

Being a generative method, BN represents the distribution of the data and is naturally amenable for interpretation. However, it is known that generative methods are not necessarily discriminative. They are prone to emphasizing major structures that are shared within each group, and neglecting the subtle but critical changes across groups. The latter, unfortunately, often happens, for example, in disease-induced brain changes across clinical groups. Consequently, generative methods are usually inferior in prediction compared with the discriminative methods that target only the boundary of classes (such as Support Vector Machines (SVMs)). On the other hand, discriminative methods often encounter the difficulty of interpretation, which is critical in exploratory research aimed at both the understanding and the prediction. Thus, this paper is motivated by the advantages that can be gained by learning BNs that are both representative and discriminative. Different from the Bayesian network classifiers in [16], [17], [18] that address discrete variables, we learn discriminative BNs for continuous variables, which is often needed in many domains including neuroimaging-based brain research. Moreover, we learn for each class a BN with enhanced discrimination and maintain the BN representation of each individual class for interpretation ${ }^{1}$. To achieve our goal, we propose two discriminative learning frameworks based on sparse Gaussian Bayesian network (SGBN).

In the first framework (termed KL-SGBN), we employ Fisher kernel [19] to link the generative models of SGBN to the discriminative classifiers of SVMs, and convert the SGBN parameter learning to Fisher kernel learning via maximizing a generalization bound of SVMs. The contributions of this framework include the following. i) By inducing Fisher kernel on SGBN models, we provide a way to obtain sample-specific SGBN-induced feature vectors that can be used by the discriminative classifiers such as SVMs. Through this, we bridge the generative models and the discriminative classifiers. ii) We propose a kernel learning approach to discriminatively learn the parameters of SGBNs by optimizing the performance of SVM. iii) As a by-product, the manipulation of Fisher kernel on SGBN provides a new way of variable selection for SGBNs. This framework has a computational advantage: through the mapping of Fisher kernel, the SGBN-induced feature vectors become

[^0]
[^0]:    ${ }^{1}$ In this paper, we deal with the scenario that maintaining the BN representation of individual class is critical for the understanding of domain problems, such as the brain network models for the healthy and the diseased groups. However, it is not difficulty to see our discriminative learning frameworks could be slightly modified to learn only a single BN as the existing "Bayesian network classifiers" for continuous variables. However, this deviates from our motivation and therefore is not unfolded in this paper.

linear functions of the SGBN parameters, which significantly simplifies the optimization problem in the learning process.

Unlike KL-SGBN where the discrimination is obtained by optimizing the classification performance of SVMs, in the second learning framework (termed MM-SGBN), we propose to optimize a criterion directly built upon the classification performance of SGBNs. The motivation is that optimizing the performance of SVMs may not necessarily guarantee an equivalent improvement on SGBNs when SGBNs are the goal of applications. The contribution of this framework is a max-margin based method to jointly learn SGBNs, one for each class, for both representation and discrimination.

In addition to the two discriminative SGBN learning frameworks, our contributions in this paper also include a new DAG constraint of SGBN based on topological ordering to ensure the validity of the graph. This new DAG constraint circumvents the awkward hard binarization of SGBN parameters in the process of optimization in [14], and simplifies the related optimization problems. This consequently makes it possible to optimize all the SGBN parameters together to avoid the influence of feature ordering encountered in the Block Coordinate Descent (BCD) optimization in [14]. Moreover, this new DAG constraint also circumvents the need for presetting candidate parent sets as in [17].

Although the discriminative learning frameworks proposed in this paper are general methods, we focus on their applications in neuroimaging analysis for the early diagnosis of mental diseases. A newly emerging field in the imaging-based neuroscience, called brain network analysis, attempts to model the brain as a complex network and study the interactions of brain regions via imaging-based features [20]. Such research is important because brain network change is often found to be a response of the brain to damages. Due to its causal semantics, BN has been employed to model the "effective connectivity" of the brain [14], [21], [22]. The directionality of the connections may disclose the pathways of how one brain region affects another. The discoveries may lend further credence to the evidence of causal relationship changes found in many mental diseases, such as the Alzheimer's disease (AD) [23], [14], [24], [22], and uncover novel connectivity-based biomarkers for disease diagnosis. The proposed learning frameworks has been tested on multiple neuroimaging data sets. As demonstrated, our methods can significantly improve the discriminative power of the obtained SGBNs, as well as maintaining their representation capacity.

Early conference versions of this work were published in [25], [26]. In this paper, a significant extension has been made on the following aspects. First, we analyze the problems of the DAG constraint used in [25], [26], [14], and propose a new constraint with theoretically guaranteed DAG property to overcome those drawbacks. Second, we experimentally verify the new DAG constraint on benchmark Bayesian network data sets for network structure learning, and compare our method with another eight competing methods in the literature. Third, we update our two discriminative learning frameworks with the new DAG constraint and redo all the experiments in our early work [25], [26]. Fourth, we analyze the connections and differences between the two proposed discriminative learning

frameworks, and conduct more comprehensive experiments to explore the characteristics of our frameworks with varied parameters, which has not been done in [25], [26].

The rest of the paper is organized as follows. Section 2 reviews SGBN and introduces the background of brain network analysis. Sections 3 elaborates two frameworks to learn discriminative and representative SGBNs from continuous data. Section 4 revisits the problem of the existing DAG constraint of SGBN, and proposes a new one based on topological ordering. The proposed two learning frameworks with the new DAG constraint are experimentally tested in Section 5. This paper is concluded in Section 6. The notations of symbols frequently occurring in this paper are summarized in Table 1.

# 2 Background 

To make this paper self-contained, we introduce the background for both the methodology and its application to brain network analysis. Please note that the methodology could be generalized to applications beyond the example given in this paper.

### 2.1 Sparse Gaussian Bayesian Network (SGBN)

Because this paper is based on SGBN model, in the following, we review the fundamentals of SGBN in [14]. All the symbols are defined in Table 1.

A Bayesian network (BN) $\mathscr{G}$ is a directed acyclic graph (DAG), i.e. there is no closed path within the graph. It expresses the factorization property of a joint distribution $p(\mathbf{x})=\prod_{i=1, \cdots, m} p\left(x_{i} \mid \mathbf{P a}_{i}\right)$. The conditional probability $p\left(x_{i} \mid \mathbf{P a}_{i}\right)$ is assumed to follow a Gaussian distribution in Gaussian Bayesian Network (GBN). Each node $x_{i}$ is regressed over its parent nodes $\mathbf{P a}_{i}: x_{i}=\boldsymbol{\theta}_{i}^{\top} \mathbf{P a}_{i}+\varepsilon_{i}$, where the vector $\boldsymbol{\theta}_{i}$ is the regression coefficients, and $\varepsilon_{i} \sim \mathscr{N}\left(0, \sigma_{i}^{2}\right)$. The structure of BN could be characterized by the $m \times m$ matrix $\mathbf{G}$ or $\mathbf{P}$ (defined in Table 1), representing the edges/paths in the graph, respectively.

Identifying parent sets is critical for BN learning. Traditional methods often consist of two stages: the candidate parent sets are initially identified in the first stage and further pruned by some criteria in the second stage. A drawback arises that when a true parent is missing in the first stage, it will never be recovered in the second stage. The work in [14] proposed a different approach based on sparse GBN (SGBN), denoted as H-SGBN in this paper. In H SGBN, each node $x_{i}$ is regressed over all the other nodes, and its parent set is implicitly selected by the regression coefficients $\boldsymbol{\theta}_{i}$ that are estimated through a constrained LASSO regression. The following optimization is solved in [14]:

A challenge for BN learning is how to enforce the DAG property, i.e., avoiding directed cycles in the graph. A sufficient and necessary condition for being a DAG is proposed in

[14], which requires Θ_{ji} × P_{ij} = 0 for all i and j. Note that P_{ij} is an implicit function of Θ_{ji} (i.e. P = expm(Θ), the matrix exponential function of Θ, as in [14]). Eqn. (2.1) is difficult to solve. In [14], a block coordinate descent (BCD) method is employed to solve a LASSO-like problem efficiently. The whole Θ is optimized column-wisely and iteratively. In each iteration t, only one column of Θ, say Θ:_{t}, is optimized with P fixed as P^{(t-1)} in the last iteration. Then Θ^{(t)}, with the updated column Θ:_{t}, is binarized to obtain G^{(t)}, based on which, P^{(t)} is recalculated by a Breadth-first search with x_{i} being the root node. The process is repeated until convergence. H-SGBN simultaneously obtains the structure and the parameters of an SGBN via learning Θ, e.g. there is no edge i → j if Θ_{ij} is zero. It has been demonstrated to outperform the conventional two-stage methods in network edge recovery.

### 2.2 Brain Network Analysis

Neuroimaging modalities and analysis techniques can provide more sensitive and consistent measurements than traditional cognitive assessment for the early diagnosis of disease. Many mental disorders are found associated with subtle abnormalities distributed over the entire brain, rather than an individual brain region. The “distributive” nature of mental disorders suggests the alteration of interactions between brain regions (neuronal systems) and thus the necessity of studying the brain as a complex network. Brain networks are mathematically represented by graphical models, which can be constructed from neuroimaging data as follows. The brain images belonging to different subjects are first spatially aligned to a common stereotaxic space by affine or deformable transformation, and then partitioned into regions of interest (ROI), i.e. clusters of imaging voxels, using either data-driven methods or predefined brain atlas. A brain network is then modeled by a graph with each node corresponding to a brain region and each edge corresponding to the connectivity between regions. Brain network analysis studies three kinds of brain connectivity. In this paper, we focus on the “effective connectivity” that describes the influence one brain region exert upon another. Some early works in this field require a prior model of brain connectivity and most have only considered a small number (≤ 10) of brain regions using techniques such as structural equation modeling [27] and dynamic causal modeling [28]. More recently, models such as BN and Granger Causality have also been introduced into this field. It is suggested that BN may have advantages over those lag-based methods for brain network analysis by an experimental fMRI study [21]. Among BN-related methods, it is worth noting that the work in [14] is completely data-driven, which recovers SGBN from more than 40 brain regions in fluorodeoxyglucose PET (FDG-PET) images. The method employs the strategy of sparsity constraint to handle relatively larger scale BN construction, and circumvents the traditional two-stage procedure for identifying parent sets in many sparse BN learning methods [12], [10].

## 3 Proposed Discriminative Learning of Generative SGBN

BN models are by definition generative models, focusing on how the data could be generated through an underlying process. In the context of neuroimage analysis, these models represent the effective brain connectivity of the given population. When used for classification, e.g. identifying AD patients from the healthy, the SGBN models are trained for each class separately. A new sample x_{i} is then assigned to the class with the higher

likelihood of SGBN. This may ignore some subtle but critical network differences that distinguish the classes. Therefore, we argue that the parameters of the generative model should be learned from the two classes jointly to keep the essential discrimination.

Integrating generative and discriminative models is an important research topic in machine learning. In [29], the related approaches are roughly divided into three categories: blending, staging and iterative methods. In blending methods, both the discriminative and the generative terms are incorporated into the same objective function. In staging methods, the discriminative model is trained on features provided by the generative model. In iterative methods, the generative and the discriminative models are trained iteratively to influence each other. In this paper, we propose two kinds of discriminative learning frameworks to achieve our goal. One is a staging method, called Fisher-kernel-induced discriminative learning (KL-SGBN). It extracts sample-based features from SGBN by Fisher kernel to optimize the classification performance of SVM. The other is a blending method, called max-margin-based discriminative learning (MMSGBN). It directly optimizes the classification performance of SGBNs subject to maintaining SGBN's representation capacity. The two frameworks are elaborated in the following sections, respectively.

# 3.1 Proposed Fisher-kernel-induced Discriminative Learning (KL-SGBN) 

We first introduce the Fisher-kernel-induced discriminative learning of SGBN, i.e., KLSGBN. The algorithm is illustrated in Fig. 1 and overviewed as follows. Given two classes in comparison, two SGBN models (with the parameters of $\Theta_{1}$ and $\Theta_{2}$ ) are learned, one for each individual class. The original samples are then mapped into the gradient space of the SGBN parameters $\Theta_{1}$ and $\Theta_{2}$ by Fisher kernel (Section 3.1.1). Through this mapping, each sample is represented by a new feature vector (called Fisher vector [19]) that is a function of $\Theta=\left[\Theta_{1}, \Theta_{2}\right]$. These sample-specific feature vectors are then fed into an SVM classifier to minimize its generalization errors by adjusting $\Theta$ (Section 3.1.2). The obtained optimal $\Theta_{1}^{*}$ and $\Theta_{2}^{*}$ encode the discriminative information and therefore improve the original SGBNs. In this way, we convert the discriminative learning of SGBN parameters to the discriminative learning of Fisher kernels.
3.1.1 Induction of Fisher vectors from SGBN-Below we introduce how to use Fisher kernel on SGBNs to obtain feature vectors required for kernel learning.

Fisher kernel [19] provides a way to compare samples induced by a generative model. It maps a sample to a feature vector in the gradient space of the model parameters. The intuition is that similar objects induce similar log-likelihood gradients of the model parameters. Fisher kernel is computed as $K\left(\mathbf{x}, \mathbf{x}^{\prime}\right)=\mathbf{g}_{\mathbf{x}}^{\top} \mathbf{U}^{-1} \mathbf{g}_{\mathbf{x}^{\prime}}$, where the Fisher vector $\mathbf{g}_{\mathbf{x}}=$ $\nabla_{\boldsymbol{\theta}} \log (p(\mathbf{x} \mid \boldsymbol{\theta})$ ) describes the changing direction of parameters to better fit the model. The Fisher information metric $\mathbf{U}$ weights the similarity measure, but is often set as an identity matrix in practice [19].

Fisher kernel has recently witnessed successful applications in image categorization [30], [31] for inducing feature vectors from Gaussian Mixture Model (GMM) of a visual vocabulary. Despite its success, in the applications above, Fisher kernel is mainly used as a

feature extractor ${ }^{2}$. It has not been applied to learning the parameters of probability distributions before the early work of this paper in [25]. The advantage of learning discriminative Fisher kernel has also been confirmed by a recent study that maximizes the class separability [33] of samples based on Fisher kernel, which is developed with different context and different criteria from ours.

Following [14], we only consider $\Theta$ as parameters and predefine $\sigma$. Let $\mathscr{L}_{1}(\mathbf{x} \mid \Theta)=\log (p(\mathbf{x} \mid \Theta))$ denote the log-likelihood. Our Fisher vector for each sample $\mathbf{x}$ is

$$
\Phi_{\Theta}(\mathbf{x})=\left[\nabla_{\Theta_{1}} \mathscr{L}\left(\mathbf{x} \mid \Theta_{1}\right)^{\top}, \nabla_{\Theta_{2}} \mathscr{L}\left(\mathbf{x} \mid \Theta_{2}\right)^{\top}\right]^{\top}
$$

where $\boldsymbol{\Theta}_{1}$ and $\boldsymbol{\Theta}_{2}$ are the parameters of the SGBNs for the two classes $(y=1,2)$, respectively. Recall that, using a BN, the probability $p(\mathbf{x} \mid \boldsymbol{\Theta})$ can be factorized as $p(\mathbf{x} \mid \boldsymbol{\Theta})=\prod_{i=1, \cdots, m} p\left(x_{i} \mid \mathbf{P a}_{i}, \boldsymbol{\theta}_{i}\right)$. Therefore, for GBN it can be shown that

$$
\begin{aligned}
& \mathscr{L}(\mathbf{x} \mid \boldsymbol{\Theta})=\sum_{i=1}^{m} \log p\left(x_{i} \mid \mathbf{P a}_{i}, \boldsymbol{\theta}_{i}\right) \\
= & \sum_{i=1}^{m} \frac{-\left(x_{i}-\mathbf{P a}_{i}^{\top} \boldsymbol{\theta}_{i}\right)^{2}}{2 \sigma_{i}^{2}}-\log \left(2 \pi \sqrt{\sigma_{i}}\right)
\end{aligned}
$$

Taking partial derivative over $\boldsymbol{\theta}_{p}$ we have

$$
\begin{gathered}
\frac{\partial \mathscr{L}(\mathbf{x} \mid \Theta)}{\partial \boldsymbol{\theta}_{i}}=-\frac{\mathbf{P a}_{i} \mathbf{P a}_{i}^{\top}}{\sigma_{i}^{2}} \boldsymbol{\theta}_{i}-\frac{x_{i} \mathbf{P a}_{i}}{\sigma_{i}^{2}} \\
\Leftrightarrow \mathbf{S}\left(x_{i}\right) \boldsymbol{\theta}_{i}+\mathbf{s}_{0}\left(x_{i}\right)
\end{gathered}
$$

where $\mathbf{S}\left(x_{i}\right)$ is a squared matrix and $\mathbf{s}_{0}\left(x_{i}\right)$ is a vector. As shown, both $\mathbf{S}\left(x_{i}\right)$ and $\mathbf{s}_{0}\left(x_{i}\right)$ are constant with respect to $\Theta$. Therefore, the Fisher vector $\Phi_{\Theta}(\mathbf{x})$ is a linear function of $\Theta$. This simple form of $\Phi_{\Theta}(\mathbf{x})$ significantly facilitates our further kernel learning.
3.1.2 Discriminative Fisher kernel learning via SVM—As each Fisher vector is a function of the SGBN parameters, discriminatively learning these parameters can thus be converted to learning discriminative Fisher kernels. We require that the learned SGBN models possess the following properties. Firstly, the Fisher vectors induced by the learned SGBN model should be well separated between classes. Secondly, the learned SGBN models should maintain reasonable capacity of representation. Thirdly, the learned SGBN models should not violate DAG.

We use the following strategies to achieve our goal. Firstly, to obtain a discriminative Fisher kernel, we jointly learn the parameters of SGBN and the separating hyper-plane of SVMs

[^0]
[^0]:    ${ }^{2}$ An exception [32] is discussed in "Generalization" in Section 3.3, which is published after our work [25].

with Fisher kernel. Radiusmargin bound, the upper bound of the Leave-One-Out error, is minimized to keep good generalization of the SVMs. Secondly, to maintain reasonable representation, we explicitly control the fitting (regression) errors of the learned model during optimization. Recall that GBN learns the network by minimizing the regression errors of each node over its parent nodes. Thirdly, we enforce the DAG constraint to ensure the validity of the graph. Our method is developed as follows.

In order to use radius-margin bound, $\mathbb{Z}_{2}$-SVM with soft margin is be employed [34] ${ }^{3}$, which optimizes

$$
\begin{gathered}
\min _{\mathbf{w}, \xi} \frac{1}{2}\|\mathbf{w}\|_{2}^{2}+C \boldsymbol{\xi}^{\top} \boldsymbol{\xi} \\
\text { s.t. } y_{i}\left(\mathbf{w}^{\top} \Phi\left(\mathbf{x}_{i}\right)+b\right) \geq 1-\xi_{i}, \xi_{i} \geq 0, \forall i
\end{gathered}
$$

Following the convention in SVMs, $\mathbf{w}$ is the normal of the separating plane, $b$ the bias term, $\boldsymbol{\xi}$ the slack variables and $C$ the regularization parameter. Here $y_{i}$ is the class label of the $i$-th sample. $\mathbb{Z}_{2}$-SVM can be rewritten as SVM with hard margin by slightly modifying the kernel $\mathbf{K}:=\mathbf{K}+\mathbf{I} / C$, where $\mathbf{I}$ is identity matrix. For convenience, in the following, we redefine $\mathbf{w}:=\left[\begin{array}{ll}\mathbf{w}^{\top} & \sqrt{C} \boldsymbol{\xi}^{\top}\end{array}\right]^{\top}$ and $\Phi\left(\mathbf{x}_{i}\right):=\left[\begin{array}{ll}\Phi^{\top}\left(\mathbf{x}_{i}\right) & \mathbf{e}_{i}^{\top} y_{i} / \sqrt{C}\end{array}\right]^{\top}$. The vector $\mathbf{e}_{i}$ has the value of 1 at the $i$-th element, and 0 elsewhere.

Incorporating radius information leads to solving

$$
\min _{\mathbf{w}} \frac{1}{2} R^{2}\|\mathbf{w}\|_{2}^{2}
$$

s.t. $y_{i}\left(\mathbf{w}^{\top} \Phi\left(\mathbf{x}_{i}\right)+b\right) \geq 1, \forall i$,
where $R^{2}$ denotes the radius of Minimal Enclosing Ball (MEB). It has been observed that when the sample size is small, the estimation of $R^{2}$ may become noisy and unstable [35]. Therefore, it has been proposed to use the trace of the total scatter matrix instead for such cases [35], [36]. We finally solve the following optimization problem:

$$
\begin{gathered}
\min _{\boldsymbol{\theta}, \mathbf{w}} \frac{1}{2} \operatorname{tr}\left(\mathbf{S}_{T}\right)\|\mathbf{w}\|_{2}^{2} \\
\text { s.t. } y_{i}\left(\mathbf{w}^{\top} \Phi_{\Theta}\left(\mathbf{x}_{i}\right)+b\right) \geq 1, \forall i \\
h\left(\mathbf{X}_{1}, \Theta_{1}\right) \leq T_{1}, h\left(\mathbf{x}_{2}, \Theta_{2}\right) \leq T_{2} \\
\Theta_{1} \in D A G, \Theta_{2} \in D A G
\end{gathered}
$$

Here $\operatorname{tr}\left(\mathbf{S}_{T}\right)$ is the trace of the total scatter matrix $\mathbf{S}_{T}$, where $\mathbf{S}_{T}=\sum_{i=1}^{n}\left(\Phi\left(\mathbf{x}_{i}\right)-\mathbf{m}\right)\left(\Phi\left(\mathbf{x}_{i}\right)-\mathbf{m}\right)^{\top}$, and $\mathbf{m}$ is the mean of total $n$ samples in the kernelinduced space. It can be shown that $\operatorname{tr}\left(\mathbf{S}_{T}\right)=\operatorname{tr}(\mathbf{K})-\mathbf{1}^{\top} \mathbf{K} \mathbf{1} / n$, where $\mathbf{1}$ denotes a vector

[^0]
[^0]:    ${ }^{3}$ Radius-margin bound is rooted in hard-margin SVM. $\mathbb{Z}_{2}$-SVM with soft-margin can be rewritten as SVM with hard margin.

whose elements are all 1 , and $\mathbf{K}$ the kernel matrix. Fisher vector $\Phi_{\boldsymbol{\Theta}}\left(\mathbf{x}_{i}\right)$ is obtained as in Section 3.1.1. The function $h(\cdot)$ measures the squared fitting errors of the corresponding SGBNs for the data $\mathbf{X}_{1}$ and $\mathbf{X}_{2}$ from the two classes. It is defined as

$$
h(\mathbf{X}, \boldsymbol{\Theta})=\sum_{i=1}^{m}\left\|\mathbf{x}_{:, i}-\mathbf{P A}_{i}^{\top} \boldsymbol{\theta}_{i}\right\|_{2}^{2}
$$

The two user-defined parameters $T_{1}$ and $T_{2}$ explicitly control the degree of fitting during the learning. Adding these constraints also avoids the scaling problem of $\boldsymbol{\Theta}$.

The DAG constraint in H-SGBN could be employed to enforce the validity of the graph. However, here we adopt a new DAG constraint proposed in Section 4 due to its advantages over that of H-SGBN. The new DAG constraint employs a set of topological ordering variables $(\mathbf{o}, \mathbf{T})$ to guarantee DAG. It is a bilinear function of the ordering variables $(\mathbf{o}, \mathbf{T})$ and the SGBN parameters $\boldsymbol{\Theta}$. An elaboration is given in Section 4. At the moment, let us temporarily skip the details of this DAG constraint and concentrate on the discriminative learning.

One possible approach for solving Eqn. (3.5) is to alternately optimize the separating hyperplane $\mathbf{w}$ and the parameter $\boldsymbol{\Theta}$. That is,

$$
\begin{gathered}
\min _{\Theta, \mathbf{o}, \mathbf{T}} J(\Theta) \\
\text { s.t. } h\left(\mathbf{X}_{1}, \Theta_{1}\right) \leq T_{1}, h\left(\mathbf{X}_{2}, \Theta_{2}\right) \leq T_{2} \\
\Theta_{1} \in D A G\left(\mathbf{o}_{1}, \mathbf{T}_{1}\right), \Theta_{2} \in D A G\left(\mathbf{o}_{2}, \mathbf{T}_{2}\right)
\end{gathered}
$$

where

$$
\begin{gathered}
J(\boldsymbol{\Theta})=\min _{\mathbf{w}} \frac{1}{2} \operatorname{tr}\left(\mathbf{S}_{\boldsymbol{\gamma}}\right)\|\mathbf{w}\|_{2}^{2} \\
\text { s.t. } y_{i}\left(\mathbf{w}^{\top} \Phi_{\boldsymbol{\Theta}}\left(\mathbf{x}_{i}\right)+b\right) \geq 1, \quad \forall i
\end{gathered}
$$

Note that for a given $\boldsymbol{\Theta}$, the term $\operatorname{tr}\left(\mathbf{S}_{\boldsymbol{\gamma}}\right)$ is constant in Eqn. (3.8). Due to the strong duality in SVM optimization, we solve the term $\|\mathbf{w}\|_{2}^{2}$ by

$$
\begin{gathered}
J_{0}(\Theta)=\max _{\boldsymbol{\alpha}} \sum_{i=1}^{n} \alpha_{i}-\frac{1}{2} \sum_{i=1}^{n} \sum_{j=1}^{n} y_{i} y_{j} \alpha_{i} \alpha_{j} K_{\Theta}\left(\mathbf{x}_{i}, \mathbf{x}_{j}\right) \\
\text { s.t. } \sum_{i=1}^{n} \alpha_{i} y_{i}=0, \alpha_{i} \geq 0 \forall i
\end{gathered}
$$

where $\boldsymbol{\alpha}_{i}$ is the Lagrangian multiplier and $K_{\boldsymbol{\Theta}}\left(\mathbf{x}_{i}, \mathbf{x}_{j}\right)=\left\langle\Phi_{\boldsymbol{\Theta}}\left(\mathbf{x}_{i}\right), \Phi_{\boldsymbol{\Theta}}\left(\mathbf{x}_{j}\right)\right\rangle$.

# Algorithm 1 

## KL-SGBN: Discriminative Learning

Input: data $\mathbf{X}_{1}, \mathbf{X}_{2} \in \mathbb{R}^{m \times n}$, label $\mathbf{y} \in \mathbb{R}^{m / 1}$
Denote $\Theta=\left[\Theta_{1}, \Theta_{2}\right]$
Initialize $\Theta^{(0)}, \mathbf{o}^{(0)}, \mathrm{T}^{(0)}$ by Algorithm 3 for each class.
Let $\Theta^{(t-1)}=\Theta^{(0)}, \mathbf{o}^{(t-1)}=\mathbf{o}^{(0)}, \mathrm{T}^{(t-1)}=\mathrm{T}^{(0)}$
repeat
1 Compute $\Phi_{\Theta}^{(t-1)}$ and $\mathbf{K}_{\Theta}^{(t-1)}$ by Eqn. (3.2)
2 Compute $\operatorname{tr}\left(\mathbf{S}_{\gamma}\right)^{(t-1)}=\operatorname{tr}\left(\mathbf{K}_{\Theta}^{(t-1)}\right)-\mathbf{1}^{\top} \mathbf{K}_{\Theta}^{(t-1)} \mathbf{1} / n$
3 Solve $\lambda_{\beta}\left(\Theta^{(t-1)}\right)$ and $\boldsymbol{\alpha}^{*}$ by Eqn. (3.9)
$4 \lambda\left(\Theta^{(t-1)}\right)=\lambda_{\beta}\left(\Theta^{(t-1)}\right) \times \operatorname{tr}\left(\mathbf{S}_{\gamma}\right)^{(t-1)}$
6 Minimize Eqn. (3.7) with $\boldsymbol{\alpha}^{*}$ and obtain $\boldsymbol{\Theta}^{(t)}$ :
6.1 Let $\mathbf{o}=\mathbf{o}^{(t-1)}, \mathbf{T}=\mathbf{T}^{(t-1)}$, solve $\boldsymbol{\Theta}^{(t)}$ by Eqn. (3.7);
6.2 Let $\Theta=\Theta^{(t)}$, solve $\mathbf{o}^{(t)}, \mathrm{T}^{(t)}$ by Eqn. (4.2).
7 Let $\Theta^{(t-1)}=\Theta^{(t)}, \mathbf{o}^{(t-1)}=\mathbf{o}^{(t)}, \mathrm{T}^{(t-1)}=\mathrm{T}^{(t)}$
until convergence/max number of iterations
Output: $\Theta^{*}=\Theta^{(t)}$
As mentioned above, the DAG constraint is a bilinear function of $(\mathbf{o}, \mathbf{T})$ and $\Theta$. Many quadratic programming packages could be used to solve Eqn. (3.7). We use fmincon-SQP (sequential quadratic programming) in Matlab. Gradient information is required by many optimization algorithms (including fmincon-SQP) to speed up the line search. It is not difficult to find that the gradient of $K_{\Theta}\left(\mathbf{x}_{i}, \mathbf{x}_{j}\right)$ is just a linear function of $\Theta$, making the evaluation of gradient $\nabla_{\Theta} /$ easy. Our learning process is summarized in Algorithm 1.

### 3.2 Proposed Max-margin-based Discriminative Learning (MM-SGBN)

KL-SGBN introduces group discrimination into SGBNs by optimizing the performance of SVM classifiers with SGBN-induced features. Although this leads to a relatively simple optimization problem, optimizing the performance of SVMs does not necessarily imply optimizing the discrimination of SGBNs. We believe that, the discrimination of SGBNs can be further improved if we directly optimize their (instead of SVMs') classification performance. Therefore we propose a new learning framework based on max-margin formulation directly built on SGBNs. We call this method MM-SGBN.

For binary classification, maximizing the minimum margin between two classes can be obtained by maximizing the minimum conditional likelihood ratio (MCLR) [18]:

$$
\operatorname{MCLR}(\Theta)=\min _{i=1}^{n} \frac{P\left(y_{i} \mid \mathbf{x}_{i}, \Theta_{y_{i}}\right)}{P\left(\bar{y}_{i} \mid \mathbf{x}_{i}, \Theta_{\bar{y}_{i}}\right)}
$$

Without loss of generality, $y_{i}$ and $\mathcal{F}_{i} \in\{-1,1\}$, representing the true and false labels for the $i$-th sample, respectively. The parameter $\Theta_{y_{i}}=\Theta_{1}$ if $y_{i}=1$, or $\Theta_{y_{i}}=\Theta_{2}$ if $y_{i}=-1$. We can see that MCLR identifies the most confusing sample whose probability of the true class assignment is close to or even less than that of the false class assignment. Hence, maximizing MCLR targets the maximal separation of the most confusing samples in the two classes. It is not difficult to see that MCLR can naturally handle multi-class case when replacing the denominator by the maximal probability induced by all false class assignments. Let $\Theta=\left[\Theta_{1}, \Theta_{2}\right]$. Taking log-likelihood of MCLR, we have

$$
\log \operatorname{MCLR}(\Theta)=\min _{i=1}^{n}\left(\log p\left(\mathbf{x}_{i} \mid y_{i}, \Theta_{y_{i}}\right)-\log p\left(\mathbf{x}_{i} \mid \bar{y}_{i}, \Theta_{\bar{y}_{i}}\right)\right)+\text { const }
$$

where the prior probabilities of $P\left(y_{i}\right)$ and $P\left(\mathcal{F}_{i}\right)$ that are irrelevant to $\Theta$ are absorbed into the constant term. Eqn. (3.10) can be shown to be a quadratic function of $\Theta$ in the case of SGBN. In order to maximize MCLR, we require the difference of log-likelihood function in Eqn. (3.10) be larger than a margin for all samples, $r$, and maximize the margin $r$. To deal with hard separations, we employ a soft margin formulation as follows.

$$
\begin{gathered}
\min _{\Theta_{1}, \Theta_{2}, \xi_{i}, r, \mathbf{o}, \Upsilon} \lambda \sum_{i=1}^{n} \xi_{i}-r \\
\text { s.t. } y_{i}\left(\mathscr{L}\left(\Theta_{1}, \mathbf{x}_{i}\right)-\mathscr{L}\left(\Theta_{2}, \mathbf{x}_{i}\right)\right) \geq r-\xi_{i}, \forall i \\
\xi_{i} \geq 0, \quad r \geq 0 \\
h\left(\mathbf{X}_{1}, \Theta_{1}\right) \leq T_{1}, h\left(\mathbf{X}_{2}, \Theta_{2}\right) \leq T_{2} \\
\Theta_{1} \in D A G\left(\mathbf{o}_{1}, \Upsilon_{1}\right), \Theta_{2} \in D A G\left(\mathbf{o}_{2}, \Upsilon_{2}\right)
\end{gathered}
$$

The constraints in (3.11a) enforce the likelihood of $\mathbf{x}_{i}$ to its true class larger than that to its false class by a margin $r$. The variables $\xi_{i}$ are slack variables indicating the intrusion of the margin. The function $\mathscr{L}_{i}(\cdot)$ denotes the log-likelihood, defined in Eqn. (3.1). We require $\mathscr{L}_{i}\left(\Theta_{1}, \mathbf{x}_{i}\right)$ larger than $\mathscr{L}_{i}\left(\Theta_{2}, \mathbf{x}_{i}\right)$ when $y_{i}=1$, and $\mathscr{L}_{i}\left(\Theta_{2}, \mathbf{x}_{i}\right)$ larger than $\mathscr{L}_{i}\left(\Theta_{1}, \mathbf{x}_{i}\right)$ when $y_{i}=$ -1 .

# Algorithm 2 

MM-SGBN: Discriminative Learning

```
Input: data \(\mathbf{X}_{1}, \mathbf{X}_{2} \in \mathbb{R}^{m \times m}\), label \(\mathbf{y} \in \mathbb{R}^{m \times 1}\)
    Denote \(\Theta=\left[\Theta_{1}, \Theta_{2}\right]\)
    Initialize \(\Theta^{(0)}, \boldsymbol{\theta}^{(0)}, \mathrm{T}^{(0)}\) by Algorithm 3 for each class.
    Fix \(\Theta=\Theta^{(0)}\) and estimate \(r^{(0)}\) and \(r_{i}^{(1)}\) by Eqn. (3.11)
    only with the two constraints (3.11a) and (3.11b).
    Initialize \(t=1\).
    repeat
        Step 1: Fixing \(\mathbf{o}=\mathbf{o}^{(t-1)}\) and \(\mathrm{T}=\mathrm{T}^{(t-1)}\), optimize Eqn. (3.11) with the constraints ( \(3.11 \mathrm{a} \sim 3.11 \mathrm{c}\) ) to update \(\Theta^{(t)}\),
        \(r^{(t)}\) and \(r_{i}^{(1)}\).
        Step 2: Fixing \(\Theta^{(t)}\), optimize Eqn. (4.2) to update \(\boldsymbol{\theta}^{(t)}\) and \(\mathrm{T}^{(t)}\) to enforce DAG.
        Let \(t=t+1\)
    until convergence/max number of iterations
    Output: \(\Theta^{*}=\Theta^{(t)}\)
```

The constraints in (3.11c) control the fitting errors, same to that used in KL-SGBN, and the function $h(\cdot)$ is defined in Eqn. (3.6).

The constraints in (3.11d) are the DAG constraint proposed in Section 4, Eqn. (4.1). To enforce the validity of DAG on both graphs, we introduce a set of order variables $\mathbf{o}=\left\{o_{1}\right.$, $\left.o_{2}, \cdots, o_{m}\right\}$ and T for each class separately, and employ the constraints stated in Eqn. (4.1). Please refer to Eqn. (4.1) for details.

The optimization in Eqn. (3.11) can be solved iteratively by optimizing $\left(\Theta, \xi_{i}, r\right)$ and $(\mathbf{o}, \mathrm{T})$ alternately, as summarized in Algorithm 2. In Step 1, we solve a linear objective function with $n$ non-convex and two convex quadratic constraints by fmincon-SQP (sequential quadratic programming) in Matlab. In Step 2, we solve the linear programming by the package of $\mathrm{CVX}^{4}$.

It is worthy noting that, we learn an SGBN model for each individual class in order to meet the requirement of both interpretation and discrimination in exploratory research. For example, each SGBN may model the brain network of the healthy or the diseased class, as well as carrying the essential class discrimination. Both the network modelling and the discrimination are of interest in such cases. Our method is different from the conventional BN classifers [16], [17], [18] that solely focus on classification. In those methods, only a single BN is learned to reflect the "difference" of the two classes. It does not model any individual class as our method does, and hence deviates from our purpose of both representing and discriminating brain networks. Moreover, the works in [16], [17], [18]

cannot handle the continuous variables of brain imaging measures, and inherit the drawbacks of the traditional two-stage methods.

# 3.3 Discussion and Analysis 

In the following, some issues regarding the two proposed discriminative learning frameworks are discussed.

Classifiers: The proposed discriminative learning frameworks produce a set of jointly learned SGBN models, one for each class. Based on these SGBN models, two kinds of classifiers can be constructed, i.e., the SGBN classifier and the SVM classifier. The SGBN classifier categorizes a sample by comparing the sample's likelihood according to each SGBN model. The SVM classifier is trained by the sample-specific Fisher vectors induced from the SGBN models. These two classifiers are tightly coupled by the underlying SGBN models. Specifically, more discriminative SGBN models directly lead to a better SGBN classifier, and can provide discriminative Fisher vectors to SVM for better classification. Rooted in this relationship, both the KL-SGBN and the MMSGBN can improve the classification performance of these two classifiers simultaneously. Put simply, KLSGBN explicitly optimizes the SVM classifier and in turn implicitly improves the SGBN classifier; while MMSGBN explicitly optimizes the SGBN classifier, bringing an implicit improvement of the SVM classifier as well. When evaluating the discriminative power of the learned SGBN models by the SGBN classifier (a direct measurement), it is therefore expected that MM-SGBN can outperform KL-SGBN. However, KL-SGBN has some computational advantages and provides a new perspective to manipulate BN models, analyzed as follows.

Computational Issues: Compared with KL-SGBN, MM-SGBN requires to solve more complicated optimization problems, which may become problematic when the number of training samples increase. Let us compare Eqn. (3.7) for KL-SGBN and Eqn. (3.11) for MMSGBN. For KL-SGBN, Eqn. (3.7) optimizes $\mathcal{M} \Theta$ ) with two convex quadratic constraints of data fitting and two DAG constraints, which are independent of the number of training samples $n$. The evaluation of $\mathcal{M} \Theta$ ) needs to solve an SVM-like problem in Eqn. (3.8), taking just $n$ linear constraints of $\Theta$, which could be efficiently solved by off-the-shelf SVM packages. For MM-SGBN, in addition to the data fitting and DAG constraints as in Eqn. (3.7), the optimization problem in Eqn. (3.11) also has to satisfy $n$ non-convex quadratic constraints. When $n$ increases to a medium or large value, the optimization problem could be quite hard to solve.

Edge Selection: In addition to the discriminative learning of SGBN, the employment of Fisher kernel in KL-SGBN also provides a new perspective of edge selection for GBN. As introduced in Section 3.1.1, applying Fisher kernel on GBN produces sample-specific feature vectors whose component is the gradient of the log likelihood, i.e., $\frac{\partial\left\langle\partial^{2} \mid \alpha\right\rangle \Theta \partial}{\partial \Theta_{i j}}$. In other words, each feature now corresponds to an edge $\Theta_{i j}$ in the SGBN. This makes it possible to convert the SGBN edge selection to a more traditional feature selection problem that has been well studied and has a large body of options in the literature. Edge selection has been

employed in our work to deal with the "small sample size" problem that is often encountered in medical applications. For example, it is common to have only 100 training samples but 3200 parameters (for SGBNs of 40 nodes from two classes) to learn in brain network analysis. To handle this issue, we keep using the whole $\Theta$ for computing $\mathbf{K}_{\boldsymbol{\Theta}}$, but only optimize a selected subset $\boldsymbol{\Theta}_{s}$. There are many options to determine $\boldsymbol{\Theta}_{s}$. We just compute the Fisher vector $\Phi_{\Theta}$ for each sample, calculate the Pearson correlation between each component of $\Phi_{\Theta}$ and the class labels on the training data, and select the top $\theta_{i}$ with the highest correlations. To keep our problem simple, only the parameters associated with edges present in the graph are optimized to avoid the violation of DAG. It is remarkable that even this simple selection process has significantly improved the discrimination for both KLSGBN and MM-SGBN. Note that this edge selection step is essentially different from that of the traditional two-stage methods. It is just an empirical method to handle the small sample size problem and will become unnecessary when sufficient training data are available. In contrast, identifying the candidate-parent sets is an indispensable step in two-stage methods to obtain computationally tractable solutions.

Generalization: We would like to point out that our learning framework of KL-SGBN could be easily generalized. It could be used to discriminatively learn the parameters of distributions other than that represented by GBN by just simply switching GBN to the target distribution, such as Gaussian Mixture Model (GMM). Indeed, this has been seen in [32], after our work [25]. However, as shown in this paper, the Fisher vector of GBN is a linear function of the model parameters, which significantly simplifies the learning problem. This favorable property may not be guaranteed with other distributions, including GMM.

# 4 Proposed DAG Constraint 

In this section, we revisit H-SGBN and propose a new DAG constraint that could simplify the optimization problems in SGBN and its discriminative learning process as introduced in Sections 3.1 and 3.2.

### 4.1 H-SGBN Revisited

Recall that, the DAG constraint in H-SGBN (Section 2.1) utilizes the matrix $\mathbf{P}$, an implicit function of $\boldsymbol{\Theta}$, which significantly complicates the optimization problem in Eqn. (2.1). In [14], for simplicity, in each optimization iteration, $\mathbf{P}$ is first treated as a constant while optimizing $\boldsymbol{\Theta}$, and then recalculated by searching on the binarized new $\boldsymbol{\Theta}$. This hard binarization could introduce high discontinuity of $\boldsymbol{\Theta}$ into the optimization. Solving $\boldsymbol{\Theta}$ column-wisely by BCD may mitigate this problem since only one column of $\boldsymbol{\Theta}$ is changed in each iteration, inducing less discontinuity. However, we observe that the solution of BCD depends on which column of $\boldsymbol{\Theta}$ to be optimized first. In other words, if we randomly permute the ordering of features (the columns in $\mathbf{X}$ ), we will obtain different SGBNs, which impairs the interpretability of the SGBN model. The optimization ordering matters because the matrix $\mathbf{P}$ used in the DAG constraint changes with the ordering. This problem has been demonstrated in our experiment. Moreover, we find experimentally that if $\mathbf{P}$ is solved as a whole instead of BCD, the optimization in Eqn. (2.1) will not converge but oscillate between some non-DAG solutions, possibly due to the high discontinuity mentioned above ${ }^{5}$. Early

stop cannot help because no premature solution satisfies DAG. These optimization difficulties motivate our work of proposing a new DAG constraint that is much simpler for SGBN, as described below.

# 4.2 Proposed DAG constraint 

It is known that, a BN is equivalent to a topological ordering (Page 362 in [37]). Therefore, we propose a new DAG constraint applicable to continuous variables with GBN based on this equivalence. With a few linear inequalities and variables separable from $\Theta$, the new DAG constraint significantly simplifies that used in [14]. Specifically, given a directed graph $\mathscr{G}$ and the parameters $\Theta$, a real-valued order variable $o_{i}$ is assigned to each node $i$, where $0 \leq$ $o_{i} \leq \Delta$, and $\Delta$ is a predefined arbitrary positive number. We propose a sufficient and necessary condition for $\mathscr{G}$ to be DAG as in Proposition 1.

Proposition 1: Given a sparse Gaussian Bayesian Network parameterized by $\boldsymbol{\Theta}$ and its associated directed graph $\mathscr{G}$ with $m$ nodes, the graph $\mathscr{G}$ is DAG if and only if there exist some $o_{i}(i=1, \cdots, m)$ and $\mathbf{T} \in \mathbb{R}^{m \times m}$, such that for arbitrary $\Delta>0$, the following constraints are satisfied:

$$
\begin{gathered}
o_{j}-o_{i} \geq \frac{\Delta}{m}-\Upsilon_{i j}, \forall i, j \in\{1, \cdots, m\}, i \neq j \\
\Upsilon_{i j} \geq 0 \\
\Upsilon_{i j} \times \Theta_{i j}=0 \\
\Delta \geq o_{i} \geq 0
\end{gathered}
$$

Eqn.(4.1) leads to a topological ordering equivalent to DAG. The topological ordering means that if node $j$ comes after node $i$ in the ordering $\left(o_{j}>o_{i}\right)$, there cannot be a link from node $j$ to node $i$, which guarantees the acyclicity. The proof of Proposition 1 is given in Appendix.

By Proposition 1, we remove the awkward hard binarization for computing P in [14]. The inequalities of (4.1a, 4.1b, 4.1d) are linear to the ordering variables $o_{i}$ and $\mathbf{T}$. The equation (4.1c) differs from the equation $\Theta_{j i} \times \mathbf{P}_{i j}=0$ in [14] in that the variable $\mathbf{T}_{i j}$ is now separable from $\boldsymbol{\Theta}_{i j}$ (while $\mathbf{P}_{i j}$ is not) and does not require the binarization of $\boldsymbol{\Theta}$. This makes it tractable to solve $\Theta$ as a whole instead of BCD (to avoid the feature ordering problem).

[^0]
[^0]:    ${ }^{5}$ Please note that, solving $\Theta$ column-wisely without updating $\mathbf{P}$ in each iteration will only lead to non-DAG solutions

It is worth noting that, provided $\Theta$ is sparse, the number of constraints in Eqn. (4.1) could be significantly reduced. As can be seen, for any $\Theta_{i j}=0$, as long as we set the corresponding $\Upsilon_{i j}$ an arbitary value greater than $\left(\frac{1}{m}+1\right) \Delta$, all the conditions in Eqn. (4.1) will be automatically satisfied. Therefore, we only need to consider the constraints related to $\Theta_{i j} \neq 0$.

The idea of topological ordering is also used to design DAG constraint for the discrete variables in [38]. However, the work in [38] addresses the multinominal distribution of discrete variables, while here we target the Gaussian distribution of continuous variables. It is worthy noting that the constraint in [38] has to predefine candidate parent-node sets. Therefore, it inherits the drawbacks of the two-stage methods as pointed out in Section 1. This has been circumvented in our proposed DAG constraint for SGBN.

# 4.3 Estimation of SGBN from A Single Class 

With our DAG constraint proposed in Eqn. (4.1), we could estimate SGBN from a single class as the initial solution to our discriminative learning of KL-SGBN or MM-SGBN. In particular, we optimize

$$
\begin{gathered}
\min _{\Theta, \mathbf{o}, \boldsymbol{\Upsilon}_{i=1}^{\infty}} \sum_{i=1}^{m}\left\|\mathbf{x}_{:, i}-\mathbf{P A}_{i}^{\top} \boldsymbol{\theta}_{i}\right\|_{2}^{2}+\lambda_{1}\left\|\boldsymbol{\theta}_{i}\right\|_{1}+\lambda_{\text {dag }} \varepsilon_{i}{ }^{\top}\left|\boldsymbol{\theta}_{i}\right| \\
\text { s.t. } o_{j}-o_{i} \geq \frac{\Delta}{m}-\boldsymbol{\Upsilon}_{i j}, \forall i, j \in\{1, \cdots, m\}, i \neq j 0 \leq o_{i} \leq \Delta, \quad \boldsymbol{\Upsilon}_{i j} \geq 0
\end{gathered}
$$

where $\boldsymbol{e}_{i}$ is the $i$-th column of the matrix $\Upsilon$, and $|\boldsymbol{\theta}\rangle$ the component-wise absolute value of $\boldsymbol{\theta}_{i}$. This optimization problem is solved in an iterative way with two alternate steps in each iteration: i) optimize $\mathbf{o}$ and $\Upsilon$ (with $\Theta$ fixed) and ii) optimize $\Theta$ (with $\mathbf{o}$ and $\Upsilon$ fixed). This process is repeated until convergence. We call this proposed method OR-SGBN (Algorithm 3).

When the coefficient $\lambda_{\text {dag }}$ is sufficiently large, the alternate optimization strategy of Eqn. (4.2) will converge to a DAG solution, as shown in Proposition 2 in Appendix. In practice, for numerical stability, we adopt a "warm start" strategy as in [14], that is, to gradually increase the values of $\lambda_{\text {dag }}$ until the resulting $\mathscr{G}$ becomes DAG. Specifically, we use a set of values of $\lambda_{\text {dag }}: \lambda_{\text {dag }}^{(1)}<\lambda_{\text {dag }}^{(2)}<\cdots<\lambda_{\text {dag }}^{(M)}$ to solve Eqn. (4.2) (Algorithm 3).

We use a bias variable $x_{0}=1$ in the regression model to improve data fitting, thus $x_{i}=\left[\begin{array}{lll}\boldsymbol{\theta}_{i} & \boldsymbol{\theta}_{0}\end{array}\right]^{\top}\left[\begin{array}{lll}\mathbf{P a}_{i} & 1\end{array}\right]+\varepsilon_{i}(i>1)$. In the following part, we denote $\boldsymbol{\theta}_{i} \triangleq\left[\begin{array}{lll}\boldsymbol{\theta}_{i} & \boldsymbol{\theta}_{0}\end{array}\right]$ and $\mathrm{Pa}_{i} \triangleq\left[\begin{array}{lll}\mathrm{Pa}_{i} & 1\end{array}\right]$. The bias term $\boldsymbol{\theta}_{0}$ is learned together with other $\boldsymbol{\theta}_{i}$. This equals to introducing a bias node into the graph. It has no parent but is the parent of all the other nodes. If the original graph is a DAG, this does not cause the violation of DAG.

It is interesting yet challenging to analyze the network consistency of OR-SGBN. It is noted that Eqn. (4.2) can be reorganized into a weighted LASSO problem, which can be conceptually linked to "adaptive LASSO" in the literature [39], [40], [41]. The analysis framework provided by these works is suggestive of promising strategies to analyze the network consistency for L1-penalized Gaussian networks. However, a complete treatment of

this analysis for OR-SGBN requires a deep investigation. Considering the significant amount of the required workload and its importance, we will explore this problem in a separate paper in our future work.

# Algorithm 3 

OR-SGBN: SGBN from a single class

```
Input: data \(\mathbf{X} \in \mathbb{R}^{m \times n}\)
    Initialize \(\Theta^{(0)}\) by least square fitting.
    Initialize \(\mathbf{o}^{(0)}\) and \(\mathbf{T}^{(0)}\) by solving Eqn. (4.2) with \(\Theta=\Theta^{(0)}\).
    Let \(T=1\).
    repeat
        Fixing \(\mathbf{T}=\mathbf{T}^{(T-1)}\) and \(\mathbf{o}=\mathbf{o}^{(T-1)}\).
        Let \(t=1, \Theta^{(T-1, t+0)}=\Theta^{(T-1)}\).
        for \(\lambda_{\text {deg }}=\lambda_{\text {deg }}^{(1)} \mathbf{0}\) to \(\lambda_{\text {deg }}^{(M)}\)
            Optimize Eqn. (4.2) with the initial solution \(\Theta^{(T-1, t-1)}\) to obtain \(\Theta^{(T-1, t)}\).
            Let \(\mathrm{t}=\mathrm{t}+1\).
    end for
    Let \(\Theta^{(T)}=\Theta^{(T-1, \lambda t)}\).
    Fixing \(\Theta^{(T)}\) , optimize Eqn. (4.2) to update \(\mathbf{o}^{(T)}\) and \(\mathbf{T}^{(T)}\) to enforce DAG.
    Let \(T=T+1\).
    until convergence/max number of iterations
    Output: \(\Theta^{\star}=\Theta^{(T)}\)
```


## 5 Experiment

In this section, we investigate the properties of our proposed methods from three aspects: the DAG constraint, the discriminative learning process, and the resulting connectivity for brain network analysis. Four experiments are conducted, summarized in Table 2. The data sets and the experiments are elaborated as follows.

### 5.1 Neuroimaging Data Sets

We conduct our experiment on the publicly accessible ADNI [42] database to analyze brain effective connectivity for the Alzheimer's disease. Three data sets are used from two imaging modalities of MRI and FDG-PET downloaded from ADNI. They are elaborated as follows.

MRI data set includes 120 T1-weighted MR images belonging to 50 mild cognitive impairment (MCI) patients and 70 normal controls (NC). These images are preprocessed by the typical procedure of intensity correction, skull stripping, and cerebellum removal. We segment the images into gray matter (GM), white matter (WM), and cerebrospinal fluid (CSF) using the standard FSL ${ }^{6}$ package, and parcellate them into 93 Region of Interest

[^0]
[^0]:    ${ }^{6}$ http://fsl.fmrib.ox.ac.uk/fsl/fslwiki/

(ROI) based on an ROI atlas [43] after spatial normalization. The GM volume of each ROI is used as the imaging feature to characterize each network node. Forty ROIs are included in this study, following [14]. They have higher correlation with the disease and are mainly located in the temporal lobe and subcortical region. Studying brain morphology as a network can take the advantage of statistical tools from graph theory. Moreover, it has been reported that the covariation of gray matter morphology might be related to the anatomical connectivity [44].

PET data set includes 103 FDG-PET images (and their corresponding MR images) of 51 AD patients and 52 NC. The MR images belonging to different subjects are co-registered and partitioned into ROIs as before. The ROI partitions are copied onto their corresponding PET images by a rigid transformation. The average tracer uptakes within each ROI is used as the imaging feature to characterize each network node. Forty ROIs discriminative to the disease are used in the study. The retention of tracer in FDG-PET is analogous to the glucose uptake, thus reflecting the tissue metabolic activity.

MRI-II data set is similar to the MRI data set but using 40 different ROIs covering the typical brain regions spread over the frontal, parietal, occipital and temporal lobes.

We randomly partition each data set into 30 groups of training-test pairs. Each group includes 80 training and 40 test samples in MRI and MRI-II, or 60 training and 43 test samples in PET.

# 5.2 DAG Constraint 

With our proposed DAG constraint, the SGBN model for an individual class can be learned with all the parameters $\Theta$ optimized together (OR-SGBN), instead of column-wisely as did in [14], [25], [26]. To explore the properties of our DAG constraint, we test three experimental configurations, namely, OR-SGBN (WHOLE), H-SGBN (BCD) and H-SGBN (WHOLE). The word in the parenthesis is used to explicitly indicate whether the parameters $\Theta$ are optimized together (WHOLE) or column-wisely (BCD). OR-SGBN (WHOLE) is our SGBN learning method for a single class in Algorithm 3, implemented with the package of CVX. H-SGBN (BCD) is the column-wise method in [14] and implemented with the code downloaded from the authors' website. H-SGBN (WHOLE) is our attempt to optimize $\Theta$ together for the objective function of H-SGBN in [14], which is implemented with the package of $\mathrm{CVX}^{7}$. The same $\Theta$ that is computed by a sparse least square fitting of the training set is provided to all the methods to initialize the optimizations. The "warm-start" strategy is applied wherever applicable in all methods.

It is found that when solving all $\Theta$ as a whole, H-SGBN (WHOLE) that uses the DAG constraint in [14] does not converge: the optimization is trapped to oscillate between a few solutions that are not DAG. Therefore, from now on, we only consider H-SGBN (BCD) and OR-SGBN (WHOLE).

[^0]
[^0]:    ${ }^{7}$ The optimization problem is solved by a series of convex subproblems.

Exp-I: In this experiment, we compare the solutions of OR-SGBN (WHOLE) and H-SGBN (BCD) with respect to the change of feature ordering. To do that, for the neuroimaging data sets, we randomly permute the feature ordering for 100 times. The estimated $\Theta$ of the resulting 100 SGBNs are re-arranged according to the initial feature ordering and then averaged as in Fig. 2. As shown, the averaged result from OR-SGBN (WHOLE) (Fig. 2(d)) is almost identical to the result using the original feature ordering (Fig. 2(c)), reflecting its robustness to feature ordering. In contrast, H-SGBN (BCD) generates SGBNs with large variations when the feature ordering changes ((Fig. 2(a) versus (b)). To give a quantitative evaluation, the Euclidean distance and the correlation between the averaged $\Theta$ and the original $\Theta$ are presented in Table 3. Consistently, the solutions from OR-SGBN (WHOLE) are much less affected by the ordering permutation, indicating the advantage of solving $\Theta$ as a whole via the proposed DAG constraint.

Exp-II: In this experiment, we test the ability of OR-SGBN (WHOLE) at identifying network structures from data. Since no ground-truth is available for the three neuroimaging data sets due to the unknown mechanism of the disease, we conduct experiments on nine benchmark network data sets mostly coming from the Bayesian Network Repository [45] as was done in the literature [12], [46]. The nine benchmark data sets are: Factors (27 nodes, 68 arcs), Alarm (37 nodes, 46 arcs), Barley (48 nodes, 84 arcs), Carpo (61 nodes, 74 arcs), Chain (7 nodes, 6 arcs), Hailfinder (56 nodes, 66 arcs), Insurance (27 nodes, 52 arcs), Mildew (35 nodes, 46 arcs) and Water (32 nodes, 66 arcs). We compare the OR-SGBN (WHOLE) with another eight BN learning methods, including L1MB [12], GS [47], TC and its variant TC-bw [13] and three variants of IAMB [48]. The experiment is repeated for 50 simulations. In each simulation, for each network, we randomly sample 1000 samples from $\pm \operatorname{Uniform}(0.5,1)$ for the regression coefficients of each variable on its parents. The parameters of the eight methods to be compared are set according to [14]. A predefined $\lambda$ that controls the sparsity of OR-SGBN is uniformly applied to all the nine data sets, which simply brings the number of the resulting edges to a reasonable range ${ }^{8}$. We use the first stage estimate of L1MB as the initial solution of OR-SGBN. Table 4 shows the total numbers of mis-identified edges (including both the false and the missing edges), while Table 5 shows the numbers of falsely identified edges (false positive). In addition, Table 6 lists the numbers of falsely identified PDAG structures. PDAG structures are statistically indistinguishable structures, i.e., representing the same statistical dependency. The PDAG of BN is obtained by the method in [49]. From Tables $4 \sim 6$, it can be seen that OR-SGBN shows significantly smaller errors on six data sets (Factors, Alarm, Barley, Carpo, Hailfinder and Insurance) in identifying both edges and PDAG structures. For the data sets of Mildew and Water, OR-SGBN performs similarly to the other methods. It only performs relatively inferior on Chain. This experiment demonstrates that the proposed DAG constraint for SGBN can perform effectively for BN structure identification. Its relatively low risk of misedge identification is a favorable property for exploratory research.

[^0]
[^0]:    ${ }^{8}$ The Bayesian Information Criterion is used to select $\lambda$ in [14]. However, it did not behave well in our experiment.

# 5.3 Comparison of Discrimination 

After testing the effectiveness of the proposed DAG constraint, we now investigate the theme of this paper: the discriminative learning frameworks. We consider two kinds of classifiers: i) the SGBN classifier (with two SGBN models, one for each class), and ii) the SVM classifier learned by the Fisher vectors induced from the SGBN models.

Exp-III: In this experiment, we test whether our learning methods (KL-SGBN and MMSGBN) can improve the discriminative power on both kinds of classifiers for the real neuroimaging data sets. The initial SGBN models are obtained by our proposed OR-SGBN (WHOLE), since it has been shown more robust to feature ordering than H-SGBN as above. For the SGBN classifier, assuming equal prior, we assign a test sample to the class with a higher likelihood. For the SVM classifier, we use $\mathcal{L}_{2}$-SVM with Fisher kernels. In order to maintain representation capability, we allow maximal $1 \%$ additional squared fitting errors (that is, $T_{i}=1.01 \times T_{R},(i=1,2)$, where $T_{R}$ is the squared fitting error of the initial solution) to be introduced during the learning process of KL-SGBN or MM-SGBN.

The test accuracies are averaged over the 30 randomly partitioned training-test groups. The classification performances of SGBN and SVM classifiers are evaluated with the varied parameter $\lambda$ that controls the sparsity level and the number of edges optimized in the learning process in Fig. 3. The results of our proposed KL-SGBN and MM-SGBN are plotted by the green and the red lines, respectively. The results of the individually learned OR-SGBN and H-SGBN are plotted by the blue and the black lines, respectively. The top two rows in Fig. 3 correspond to the results from the SGBN classifiers, while the bottom two rows correspond to those from the SVM classifiers. From Fig. 3, we have the following observations.
i. Both KL-SGBN and MM-SGBN can significantly improve the discriminative power of the individually learned SGBNs (Fig. 3, the top two rows), as well as their associated SVM classifiers (Fig. 3, the third row). Such improvements are consistent over the three neuroimaging data sets and different parameter settings, and could reach the significant increases of $10 \% \sim 20 \%$ on most occasions. When the network becomes more sparse, the classification performance of the individually learned SGBNs (H-SGBN and OR-SGBN) drops significantly possibly due to the insufficient modeling of data. However, under such circumstances, KL-SGBN and MM-SGBN can still maintain high classification accuracies, which may indicate the necessity and effectiveness of the discriminative learning in classification scenarios.
ii. When using SGBN classifiers, for all the three data sets, MM-SGBN consistently achieves higher test accuracies at all sparsity levels (Fig. 3, the first row) with different numbers of optimized edges than KL-SGBN (Fig. 3, the second row). The advantage of MM-SGBN over KL-SGBN comes from explicitly optimizing the discriminative power of SGBNs, instead of getting help from optimizing the performance of SVM on SGBN-induced features.

iii. When using SVM classifiers, the SVM built upon KL-SGBN-induced features performs slightly better than that built upon MM-SGBN-induced features at all sparsity levels (Fig. 3, the third row). This is expected since KL-SGBN optimizes the performance of its associated SVM classifier.
iv. When cross-referencing the first and the third rows in Fig. 3, it is noticed that SVM classifiers in general perform worse than the discriminatively learned SGBN classifiers. These may be because our Fisher vectors have very high dimensionality, which causes serious overfitting of data in SVM classifiers. Such situation might be somewhat improved for SGBN-classifiers since the simple Gaussian model may "regularize" the model fitting. Based on this assumption, we further select a number of leading features from Fisher vectors by computing the Pearson correlation of the features and the labels, and use the selected features to construct the Fisher kernel for the SVM classifiers. As shown in the fourth row of Fig. 3, the simple feature selection step can further significantly improve the classification performance of the Fisher-kernel based SVM.
v. The individually learned OR-SGBN and H-SGBN perform similarly for classification. However, as mentioned above, OR-SGBN has an additional advantage of being invariant to the feature ordering.
vi. Recall that these improvement on discrimination are achieved with no more than $1 \%$ increase of squared fitting errors, which is explicitly controlled through the user defined parameters $T_{1}$ and $T_{2}$. Note that the rate of $1 \%$ is application dependent. More tolerance of fitting errors can potentially bring more discrimination.

# 5.4 Comparison of Connectivity 

We also conduct an investigation to gain some insights into the learned brain networks for the diseased and the healthy populations, respectively.

Exp-IV: In this experiment, we visualize the learned brain networks and compare the connectivity patterns obtained by different methods and from different populations. MRI-II data set is used for this study since it covers regions spread over the four lobes of brain.

The structures of the brain networks recovered from NC and MCI groups are displayed in Fig. 4 by using H-SGBN (BCD) and OR-SGBN (WHOLE), respectively. The network structure is obtained by thresholding the edge weights $\Theta$ with a cutoff value of 0.01 [14]. Each row $i$ represents the effective connections (dark dots) starting from the node $i$, and each column $j$ represents the effective connections ending at the node $j$. Note that, due to the different optimization problems involved, the same parameter $\lambda$ leads to different sparsity levels for H-SGBN and OR-SGBN. However, for a given method, different $\lambda$ values do not change the major structures of the resulting networks.

In Fig. 4, it is noticed that H-SGBN (BCD) usually generates more connections in the upper triangle of the graphs even when we randomly permute the nodes. We suspect that this is caused by the column-wise optimization. The parameters $\theta_{i}$ (corresponding to the columns

in the graph) optimized at the early stage tend to be made more sparse than those optimized later in order to satisfy the DAG constraint. This phenomenon is not observed in OR-SGBN (WHOLE) that is used to initialize the discriminative learning.

Let us focus on OR-SGBN. Compared with H-SGBN, OR-SGBN has an additional bias node corresponding to the last row and column in Fig. 4. Visualizing $\Theta$ can provide rich information for medical analysis. Here we just list a few observations as examples. With the same $\lambda$, OR-SGBN produces 183 edges for NC, and 145 edges for MCI. Such loss of connectivity also happens at the temporal lobe ( $24 \%$ loss) for MCI. The temporal lobe (and some subcortical structures) is known to play a very important role in the progression of AD. The loss of connectivity in this region has been well-documented in wide AD-related studies [50], [51], [14]. In Fig. 4, we also observe an increase of connectivity (the left bottom corner in the figure) between the frontal and the temporal lobe in MCI. Some study [52] mentioned that the frontal lobe may have connectivity increase at the early stage of AD as a compensation of cognitive functions for the patients. Moreover, significant directionality changes are also found for the left (node 35) and the right (node 38) hippocampi, an important structure among the earliest ones affected by AD. Both hippocampi have reduced incoming connectivity (communications dominated by other nodes) but increased outgoing connectivity (communications dominated by themselves) in MCI. Please note that the above observations could be influenced by the factors such as the limited number of data, the degree of disease progression and the imaging modality used in this study. More reliable medical analysis should be validated on larger data sets and worth further exploration, which is, however, beyond the scope of this paper.

To illustrate the difference of edge weights learned by KL-SGBN and MM-SGBN, an example of 30 edge weight changes (from the initial OR-SGBN) learned by these two methods is given in Fig. 5, where the SGBN networks from the two classes are vectorized and concatenated as $x$-axis. As shown, the signs of weight changes are quite similar in both methods. The most significant difference is that, MM-SGBN gives negative weight changes to the bias node of the left Amygdala and the right Parahippocampus (red lines in Fig. 5) while KL-SGBN gives them positive weight changes. The adjustment of edge weights leads to $10 \%$ increase of test accuracy for MM-SGBN in this example.

# 6 Conclusion 

In this paper, we focus on the discriminative learning of Bayesian network for continuous variables, especially for neuroimaging data. Two discriminative learning frameworks are proposed to achieve this goal, i.e., KL-SGBN improves the performance of SVM classifiers based on SGBN-induced features, and MM-SGBN explicitly optimizes an SGBN-based criterion for classification. We demonstrate how to utilize Fisher-kernel to bridge the generative methods of SGBN and the discriminative classifiers of SVM, and how to embed the max-margin criterion into SGBN for discriminative learning. The optimization problems are analyzed in details, and the advantages and disadvantages of the proposed methods are discussed. Moreover, a new DAG constraint is proposed to ensure the validity of the graph with theoretical guarantee and validation on the benchmark data. We apply the proposed methods to modeling brain effective connectivity for early AD prediction. Significant

improvements have been observed in the discriminative power of both the SGBN models and the associated SVM classifiers, without sacrificing much representation power.

# Appendix 

## Proposition 1

Given a sparse Gaussian Bayesian Network parameterized by $\Theta$ and its associated directed graph $\mathscr{G}$ with $m$ nodes, the graph $\mathscr{G}$ is DAG if and only if there exist some $o_{i}(i=1, \ldots, m)$ and $\Upsilon \in \mathbb{R}^{m \times m}$, such that for arbitary $\Delta>0$, the following constraints are satisfied:

$$
\begin{gathered}
o_{j}-o_{i} \geq \frac{\Delta}{m}-\Upsilon_{i j}, \forall i, j \in\{1, \cdots, m\}, i \neq j \\
\Upsilon_{i j} \geq 0 \\
\Upsilon_{i j} \times \Theta_{i j}=0 \\
\Delta \geq o_{i} \geq 0
\end{gathered}
$$

Proof
As is known, a Bayesian network is equivalent to a topological ordering (Chapter 8, Section 8.1 on Page 362 in [37]). Therefore, we prove Proposition 1 by showing that i) Eqn. (1a 1d) lead to a topological ordering (the necessary condition), and ii) a topological ordering from a DAG can meet the requirements in Eqn. (1a 1d) (sufficient condition).

First, we prove the necessary condition by contradiction (Fig. 6). We consider three cases for two nodes $j$ and $i$. Case 1) the nodes $j$ and $i$ are directly connected. If there is an edge from node $i$ to node $j$, the parameter $\Theta_{i j}$ is then non-zero, and thus $\Upsilon_{i j}$ must be zero. According to Eqn. (1a), we have $o_{j}>o_{i}$. If at the same time, there is an edge from node $j$ to node $i$, similarly we have $o_{i}>o_{j}$, which contradicts with $o_{j}>o_{i}$, and therefore is impossible. Case 2: the nodes $j$ and $i$ are not directly linked but connected by a path. Suppose there is a directed path $P 1$ from node $i$ to node $j$, where $P 1$ is composed of nodes $k_{1}, k_{2}, \ldots, k_{m_{1}}$ in order. Following the above proof, we can have $o_{j}>o_{k_{m_{1}}}>\ldots>o_{k_{1}}>o_{i}$. If at the same time another directed path $P 2$ links node $j$ to node $i$, where $P 2$ is composed of nodes $l_{1}, l_{2}, \ldots, l_{m_{2}}$ in order, similarly we have $o_{i}>o_{l_{m_{2}}}>\ldots>o_{l_{1}}>o_{i}$, making the contradiction. Case 3) If there is no edge between node $i$ and node $j$, by definition $\Theta_{i j}=0$. It is straightforward to see

Eqn. (1b) and Eqn. (1c) hold for any arbitrary non-negative $\mathrm{T}_{i j}$. Moreover, for any $o_{i}$ and $o_{j}$ satisfying Eqn. (1d), we can show that as long as $\boldsymbol{\Upsilon}_{i j} \geq\left(\frac{1}{m}+1\right) \Delta$ (which is positive), Eqn. (1a) will always hold. This is further explained as follows. By Eqn. (1d), we have $-\Delta \leq o_{j}-$ $o_{i} \leq \Delta$. For Eqn. (1a) to be always held, we need some $\mathrm{T}_{i j}$ such that $o_{j}-o_{i} \geq-\Delta \geq \frac{\Delta}{m}-\Upsilon_{i j}$, which requires $\Upsilon_{i j} \geq\left(\frac{1}{m}+1\right) \Delta$. Therefore, there exist a set of $o_{i}$ and $T$ valid for Eqn. (1a 1d) when no edge links node $i$ and node $j$. In sum, Eqn. (1a 1d) show a topological ordering, that is, if node $j$ comes after node $i$ (that is, $o_{j}>o_{i}$ ) in the ordering, there can not be a link from node $j$ to node $i$, which guarantees the acyclicity.

Now let us consider the sufficient condition. if $\mathscr{G}$ is a DAG, we can obtain some topological ordering $(1,2, \ldots, m)$ from it. Let $\tilde{o}_{i}$ be the index of node $i$ in this ordering. Setting $o_{i}=\left(\tilde{o}_{i}-1\right) \frac{\Delta}{m}\left(\forall i \in\{1, \cdots, m\}\right)$, we have $\min \left(o_{i}\right)=(1-1) \frac{\Delta}{m}=0$ and $\max \left(o_{i}\right)=(m-1) \frac{\Delta}{m} \leq \Delta$. If node $j$ comes after node $i$, we have $o_{j}-o_{i} \geq \frac{\Delta}{m} \geq \frac{\Delta}{m}-\Upsilon_{i j}$. If node $j$ comes before node $i$, we can always set $\mathrm{T}_{i j}$ sufficiently large to satisfy Eqn. (1a 1d). Therefore, from a DAG, we can always construct a set of ordering variables that satisfy Eqn. (1a 1d).

Combining the proofs above, Eqn. (1a 1d) are the sufficient and necessary condition for a directed graph $\mathscr{G}$ to be DAG.

# Proposition 2 

The optimization problem in Eqn. (2) (i.e., Eqn. (4.2) in the paper) is iteratively solved by alternate optimizations of (i) $\mathbf{o}$ and $\mathbf{T}$ with $\Theta$ fixed, and (ii) $\boldsymbol{\Theta}$ with $\mathbf{o}$ and $\mathbf{T}$ fixed. This optimization converges and the output $\Theta^{\star}$ is DAG when $\lambda_{\text {dag }}>\frac{2 m(m-2)(n-1)^{2}+m \lambda_{1}\left(2 n-2-\lambda_{1}\right)}{\lambda_{1}(1+m) \Delta}$, where $m$ is the number of nodes and $n$ is the number of samples.

$$
\begin{gathered}
\min _{\Theta, \mathbf{o}, \boldsymbol{\Upsilon}_{i=1}^{m}}\left\|\mathbf{x}_{:, i}-\mathbf{P A}_{i}^{\top} \boldsymbol{\theta}_{i}\right\|_{2}^{2}+\lambda_{1}\left\|\boldsymbol{\theta}_{i}\right\|_{1}+\lambda_{\text {dag }} \varepsilon_{i}^{\top}\left|\boldsymbol{\theta}_{i}\right| \\
\text { s.t. } o_{j}-o_{i} \geq \frac{\Delta}{m}-\boldsymbol{\Upsilon}_{i j}, \forall i, j \in\{1, \cdots, m\}, i \neq j \\
0 \leq o_{i} \leq \Delta, \boldsymbol{\Upsilon}_{i j} \geq 0
\end{gathered}
$$

Here $\mathbf{o}$ and $\mathbf{T}$ are the variables defined in the DAG constraint in Section 4.2, and $\Theta$ is the model parameters of SGBN. The vector $\boldsymbol{\varepsilon}_{i}$ denotes the $i$-th column of the matrix $\mathbf{T}$, and $|\boldsymbol{\theta}|$ the component-wise absolute value of the $i$-th column of $\Theta$. Other parameters are defined in Table 1 in the paper.

## Proof

In the following, we prove that:

1. The alternate optimization in Eqn. (2) converges.
2. The solution $\Theta^{\star}$ of Eqn. (2) is DAG when $\lambda_{\text {dag }}$ is sufficiently large.

Let us denote $f(\Theta, \mathbf{o}, \Upsilon)=\sum_{i=1}^{m}\left\|\mathbf{x}_{:, i}-\mathbf{P A}_{i}^{\top} \boldsymbol{\theta}_{i}\right\|_{2}^{2}+\lambda_{1}\left\|\boldsymbol{\theta}_{i}\right\|_{1}+\lambda_{\text {dag }} \varepsilon_{i}^{\top}\left|\boldsymbol{\theta}_{i}\right|$.

First, we prove Eqn. (2) converges by showing that (i) $f(\boldsymbol{\Theta}, \mathbf{o}, \mathbf{T})$ is lower bounded; and (ii) $f\left(\boldsymbol{\Theta}^{(t+1)}, \mathbf{o}^{(t+1)}, \mathbf{T}^{(t+1)}\right) \leq f\left(\boldsymbol{\Theta}^{(\ell)}, \mathbf{o}^{(\ell)}, \mathbf{T}^{(\ell)}\right)$, meaning that the function value will monotonically decrease with the iteration number $t$.

It is easy to see that $f(\boldsymbol{\Theta}, \mathbf{o}, \mathbf{T})$ is lower bounded by 0 , since each term in $f(\boldsymbol{\Theta}, \mathbf{o}, \mathbf{T})$ is nonnegative. And the second point can be proven as follows. At the $t$-th iteration, we update $\boldsymbol{\Theta}$ by

$$
\Theta^{(t+1)}=\underset{\Theta}{\arg \min } \sum_{i=1}^{m}\left\|\mathbf{x}_{:, i}-\mathbf{P A}_{i}^{\top} \boldsymbol{\theta}_{i}\right\|_{2}^{2}+\lambda_{1}\left\|\boldsymbol{\theta}_{i}\right\|_{1}+\lambda_{\text {d } \alpha g} \varepsilon_{i}{ }^{(t) \top}\left|\boldsymbol{\theta}_{i}\right|
$$

$$
\begin{aligned}
& =\underset{\Theta}{\arg \min } f\left(\boldsymbol{\Theta}, \mathbf{o}^{(t)}, \boldsymbol{\Upsilon}^{(t)}\right) .
\end{aligned}
$$

It holds that $f\left(\boldsymbol{\Theta}^{(t+1)}, \mathbf{o}^{(\ell)}, \mathbf{T}^{(\ell)}\right) \leq f\left(\boldsymbol{\Theta}^{(\ell)}, \mathbf{o}^{(\ell)}, \mathbf{T}^{(\ell)}\right)$. Also it is noted that $\boldsymbol{\Theta}^{(t+1)}$ is an achievable global minimum of $\boldsymbol{\Theta}$ since $f\left(\boldsymbol{\Theta}, \mathbf{o}^{(\ell)}, \mathbf{T}^{(\ell)}\right)$ is a convex function with respect to $\boldsymbol{\Theta}$. Similarly, we then update $\mathbf{o}$ and $\mathbf{T}$ by

$$
\begin{gathered}
\left\{\mathbf{o}^{(t+1)}, \boldsymbol{\Upsilon}^{(t+1)}\right\}=\arg \min _{\mathbf{o}, \mathbf{T}} f\left(\boldsymbol{\Theta}^{(t+1)}, \mathbf{o}, \boldsymbol{\Upsilon}\right) \\
\text { s.t. } o_{j}-o_{i} \geq \frac{\Delta}{m}-\boldsymbol{\Upsilon}_{i j}, \forall i, j \in\{1, \cdots, m\}, i \neq j \\
0 \leq o_{i} \leq \Delta, \boldsymbol{\Upsilon}_{i j} \geq 0
\end{gathered}
$$

It holds that $f\left(\boldsymbol{\Theta}^{(t+1)}, \mathbf{o}^{(t+1)}, \mathbf{T}^{(t+1)}\right) \leq f\left(\boldsymbol{\Theta}^{(t+1)}, \mathbf{o}^{(\ell)}, \mathbf{T}^{(\ell)}\right)$. Also, $f\left(\boldsymbol{\Theta}^{(t+1)}, \mathbf{o}, \mathbf{T}\right)$ is a linear function with respect to $\mathbf{o}$ and $\mathbf{T}$. Consequently we have

$$
f\left(\boldsymbol{\Theta}^{(t+1)}, \mathbf{o}^{(t+1)}, \boldsymbol{\Upsilon}^{(t+1)}\right) \leq f\left(\boldsymbol{\Theta}^{(t+1)}, \mathbf{o}^{(t)}, \boldsymbol{\Upsilon}^{(t)}\right) \leq f\left(\boldsymbol{\Theta}^{(t)}, \mathbf{o}^{(t)}, \boldsymbol{\Upsilon}^{(t)}\right)
$$

Therefore, the optimization problem in Eqn. (2) is guaranteed to converge with the alternate optimization strategy, because the objective function is lower-bounded and monotonically decreases with the iteration numbers.

Second, we prove that when $\lambda_{\text {d } \alpha g}>\frac{2 m(m-2)(n-1)^{2}+m \lambda_{1}\left(2 n-2-\lambda_{1}\right)}{\lambda_{1}(1+m) \Delta}$, the output $\boldsymbol{\Theta}^{\star}$ is guaranteed to be DAG. This could be proven by contradiction. Suppose that such a $A_{\text {d } a g}$ does not lead to a DAG, say, $\boldsymbol{\Upsilon}_{j i} \times \Theta_{j i}^{*} \neq 0$ for at least one pair of nodes $i$ and $j$, with $\Theta_{j i}^{*} \neq 0$ and $\mathbf{T}_{j i}>0$. Without loss of generality, we assume $\boldsymbol{\Upsilon}_{j i} \geq\left(\frac{1}{m}+1\right) \Delta$ (where $\Delta$ is an arbitary positive number), so the ordering constraints in Eqn. (2) always hold regardless of the variables $o_{j}$ and $o_{j}$. This is because $o_{i}$ and $o_{j}$ are constrained by $0 \leq o_{i} \leq \Delta$ and $0 \leq o_{j} \leq \Delta$, and $o_{j}-o_{i} \geq-\Delta=\frac{1}{m} \Delta-\left(\frac{1}{m}+1\right) \Delta$. Based on the first-order optimality condition, $\Theta_{j i}^{*} \neq 0$ i.f.f. $2\left|\left(\mathbf{x}_{:, i}-\mathbf{P A}_{i \mid \backslash j,:}^{\top} \boldsymbol{\theta}_{i \backslash j}^{*}\right)^{\top} \mathbf{x}_{:, j}\right|-\left(\lambda_{1}+\lambda_{\text {d } \alpha g} \boldsymbol{\Upsilon}_{i j}\right)>0$. Here, $\mathbf{P A}_{i \mid j,:}$ denotes the elements in the matrix $\mathbf{P A}_{i}$ with the $j$-th row removed (i.e., parents of the node $i$ without the node $j$ ), and $\boldsymbol{\theta}_{i \backslash j}^{*}$ denotes the elements in $\boldsymbol{\theta}_{i}^{*}$ without $\Theta_{j i}^{*}$. However, it can be shown that,

$$
\begin{gathered}
\left|\left(\mathbf{x}_{:, i}-\mathbf{P A}_{i\left(\backslash j,:\right)}^{\top} \boldsymbol{\theta}_{i \backslash j}^{*}\right)^{\top} \mathbf{x}_{:, j}\right| \leq\left|\mathbf{x}_{:, i}^{\top} \mathbf{x}_{:, j}\right|+\left|\boldsymbol{\theta}_{i \backslash j}^{*}{ }^{\top} \mathbf{P A}_{i\left(\backslash j,:\right)} \mathbf{x}_{:, j}\right| \\
=\left|\mathbf{x}_{:, i}^{\top} \mathbf{x}_{:, j}\right|+\sum_{k=1, k \neq i, j}^{m}\left|\boldsymbol{\Theta}_{k i}^{*} \mathbf{x}_{:, k}^{\top} \mathbf{x}_{:, j}\right| \\
\leq(n-1)+(m-2)(n-1) \max _{\mathbf{x}}\left|\boldsymbol{\Theta}_{k i}^{*}\right| \\
\leq(n-1)+\frac{(m-2)(n-1)^{2}}{\lambda_{1}}
\end{gathered}
$$

The second last inequality holds due to the normalization of features $\mathbf{x}_{:, i}$ (to zero mean and unit std). The last inequality holds because

$$
\begin{aligned}
& \max \left|\boldsymbol{\Theta}_{k i}^{*}\right| \leq\left\|\boldsymbol{\theta}_{i}^{*}\right\|_{1} \leq \frac{1}{\lambda_{1}}\left(\left\|\mathbf{x}_{:, i}-\mathbf{P A}_{i}^{\top} \boldsymbol{\theta}_{i}^{*}\right\|_{2}^{2}+\lambda_{1}\left\|\boldsymbol{\theta}_{i}^{*}\right\|_{1}+\lambda_{\text {day }} \varepsilon_{i}^{*}{ }^{\top}\left|\boldsymbol{\theta}_{i}^{*}\right|\right) \\
& \quad=\frac{1}{\lambda_{1}} f\left(\boldsymbol{\Theta}^{*}, \mathbf{o}^{*}, \boldsymbol{\Upsilon}^{*}\right) \leq \frac{1}{\lambda_{1}} f\left(\mathbf{0}, \mathbf{o}^{*}, \boldsymbol{\Upsilon}^{*}\right) \\
& \quad=\frac{1}{\lambda_{1}} \mathbf{x}_{:, i}^{\top} \mathbf{x}_{:, i}=\frac{n-1}{\lambda_{1}} \\
& \text { With the given } \boldsymbol{\lambda}_{\text {dag }} \text {, }
\end{aligned}
$$

Eqn. (5) results in

$$
2\left|\left(\mathbf{x}_{:, i}-\mathbf{P A}_{i\left(\backslash j,:\right)}^{\top} \boldsymbol{\theta}_{i \backslash j}^{*}\right)^{\top} \mathbf{x}_{:, j}\right|-\left(\lambda_{1}+\lambda_{\text {day }} \boldsymbol{\Upsilon}_{i j}\right)<0
$$

which contradicts the above first-order optimality condition with $\Theta_{j i}^{*} \neq 0$. Therefore, when $\lambda_{\text {dag }}$ is sufficiently large, the output $\boldsymbol{\Theta}^{\star}$ is guaranteed to be DAG.

Summing up the proofs above, the alternate optimization of Eqn. (2) converges and the output $\boldsymbol{\Theta}^{\star}$ is guaranteed to be DAG when $\lambda_{\text {dag }}$ is sufficiently large.

![img-0.jpeg](img-0.jpeg)

Fig. 1.
Illustration of Fisher-kernel-induced Discriminative Learning.

![img-1.jpeg](img-1.jpeg)

Fig. 2.
One example of the estimated parameter $\Theta$ for the MCI class (reshaped as a long vector) with regard to the random permutation of the feature ordering. Quantitative measurements of the changes are given in Table 3.

![img-2.jpeg](img-2.jpeg)

Fig. 3.
Comparison of classification accuracies on data sets of MRI (the left column), PET (the middle column) and MRI-II (the right column). The top two rows correspond to the test accuracies obtained by the learned SGBNs. The first row shows the test accuracies varied with the sparsity levels (i.e., the parameter $\mathcal{X}$ ). The second row shows the test accuracies varied with the number of edges (denoted as "\#Sel Edges" in the figure) optimized in discriminative learning. The bottom two rows correspond to the test accuracies obtained by SVMs using the SGBN-induced Fisher vectors either in full length (the third row) or with (100) selected components (the fourth row).

![img-3.jpeg](img-3.jpeg)

# OR-SGBN (WHOLE): NC 

OR-SGBN (WHOLE): MCI

Fig. 4.
Visualization of connectivities for MRI-II. The four red boxes correspond to the frontal, parietal, occipital and temporal (including subcortical regions) lobes of the brain. The green row (Row 35) and column (Col 35) correspond to the left hippocampus while the blue ones (Row 38 and Col 38) correspond to the right hippocampus.

![img-4.jpeg](img-4.jpeg)

Fig. 5.
An example: change of edge weights learned by KL-SGBN and MM-SGBN

![img-5.jpeg](img-5.jpeg)

Fig. 6.
Explanation of our ordering based DAG constraint.

# TABLE 1 

## Notation


TABLE 2
Summary of Experiment Purpose


# TABLE 3 

Quantitative Analysis of $\Theta$ for the random permutation of feature ordering (between the original and the averaged $\Theta$ )


TABLE 4 Total errors (number of both false and missing edges, averaged on 50 simulations) on benchmark networks


TABLE 5 Number of falsely identified edges (averaged on 50 simulations) on benchmark networks


TABLE 6 Number of falsely identified P-DAG structures (averaged on 50 simulations) on benchmark networks
