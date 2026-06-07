# NIH Public Access 

## Author Manuscript

Conf Comput Vis Pattern Recognit Workshops. Author manuscript; available in PMC 2014 October 15 .

Published in final edited form as:
Conf Comput Vis Pattern Recognit Workshops. 2013 ; 2013: 2243-2250. doi:10.1109/CVPR.2013.291.

## Discriminative Brain Effective Connectivity Analysis for Alzheimer's Disease: A Kernel Learning Approach upon Sparse Gaussian Bayesian Network


#### Abstract

Analyzing brain network from neuroimages is becoming a promising approach in identifying novel connectivity-based biomarkers for the Alzheimer's disease (AD). In this regard, brain "effective connectivity" analysis, which studies the causal relationship among brain regions, is highly challenging and of many research opportunities. Most of the existing works in this field use generative methods. Despite their success in data representation and other important merits, generative methods are not necessarily discriminative, which may cause the ignorance of subtle but critical disease-induced changes. In this paper, we propose a learning-based approach that integrates the benefits of generative and discriminative methods to recover effective connectivity. In particular, we employ Fisher kernel to bridge the generative models of sparse Bayesian network (SBN) and the discriminative classifiers of SVMs, and convert the SBN parameter learning to Fisher kernel learning via minimizing a generalization error bound of SVMs. Our method is able to simultaneously boost the discrimination power of both the generative SBN models and the SBN-induced SVM classifiers via Fisher kernel. The proposed method is tested on analyzing brain effective connectivity for AD from ADNI data. It demonstrates significant improvements over the state-of-the-art: classification accuracy increased above $10 \%$ by our SBN models, and above $16 \%$ by our SBN-induced SVM classifiers with a simple feature selection.


## 1. Introduction

As the most common form of dementia, Alzheimer's disease (AD) is a fatal and progressive neurodegenerative disease that has caused serious socioeconomic problems in developed countries. Early diagnosis of AD may benefit the patients with disease-interrupted therapies when the dementia is still mild. Neuroimaging techniques are important in AD study because they may provide more sensitive and consistent measures than traditional cognitive assessment.

Currently, neuroimage analysis has evolved from studying local morphometry to complex relationships and interactions across brain regions. This is because the brain is, by nature, a complex network of many interconnected regions. A brain network is usually modeled by a graph with each node corresponding to a brain region and each edge corresponding to the connectivity between regions. The connectivity could be statistical dependencies (functional connectivity) or causal relationships (effective connectivity) [15], represented by undirected or directed graph, respectively. This paper focuses on brain effective connectivity analysis, which has gradually accumulated attentions due to its ability to analyze the directional effect

of one brain region over another. Effective connectivity analysis has been applied to fMRI [6], PET [2], and gray matter morphology in structural MRI [7], and has exhibited its promising potential in identifying novel connectivity-based biomarkers for AD.

With sparse learning techniques, effective connectivity analysis has been able to handle medium to large scale brain network. A remarkable recent work is from Huang, et al. [2, 1], where a sparse Gaussian Bayesian network (SGBN) is recovered from more than 40 brain regions in fluorodeoxyglucose PET (FDG-PET) images for AD analysis. That approach learns the Bayesian network (BN) structure and parameters simultaneously in one step, which demonstrates a more accurate network recovery than the conventional two-stage approaches in sparse BN learning (such as LIMB-DAG [14], MMHC [17], TC and TC-bw [10], etc.). Despite the effectiveness in network representation, the above methods (including $[2,1]$ ) are all generative methods. As known, generative methods focus on representing an individual group, thus may not be discriminative. When analyzing brain network, they are prone to over-emphasizing major structures within an individual group, and neglecting the subtle disease-induced structural changes across different groups. Therefore, generative methods are usually inferior in prediction compared with the discriminaitve methods that focus on the class boundary (such as Support Vector Machines (SVMs)). However, discriminative methods are not amenable for interpretation, which is critical in exploratory research aiming at both the understanding and the diagnosis of the disease. Therefore, we aim to integrate the merits of generative and discriminative methods to learn BNs that are not only representative but also discriminative. Recent progress in [11, 12] for learning discriminative BNs follows the conventional two-stage approach and works for discrete variables. They may not suit for brain network analysis where the brain regional measurements are usually continuous variables.

To achieve our goal, we improve the model of the SGBN in [2], and further boost its discrimination power via a kernel learning approach that links the generative SGBN with the SVM classifiers. The contribution of this paper includes: 1) We propose an augmented SGBN model (A-SGBN) by revisiting the method in [2]. A-SGBN fits the underlying distribution more precisely, therefore bringing better prediction. 2) By inducing Fisher kernel on our A-SGBN models, we provide a way to obtain subject-specific SGBN-induced feature vectors that can be used by discriminative classifiers such as SVMs. Through this, we integrate the generative and discriminative models. 3) More significantly, we convert the learning of SGBN parameters to the learning of discriminative Fisher kernels, which simplifies the optimization. Specifically, we jointly learn the SGBN parameters and the separating hyperplane of SVMs over Fisher kernel by minimizing a generalization error bound of SVMs. 4) We apply our method on ADNI ${ }^{1}$ data to analyze brain effective connectivity for AD from both T1-weighted MRI and FDG-PET images. Our method significantly improves the discrimination power of the generative SGBN and the discriminative SVM classifier simultaneously. 5) By Fisher kernel, we obtain a new kind of features that reflect the changing rate of connection strength, which have not been investigated in conventional approaches.

[^0]
[^0]:    ${ }^{1}$ http://www.adni-info.org/

# 2. Related Work 

### 2.1. Gaussian Bayesian Network

Gaussian Bayesian network (GBN) is the fundamental tool that we use to learn effective brain connectivity in this paper. It is therefore briefed here, together with the definition of symbols used throughout the paper.

Let $\mathrm{x}=\left[x_{1}, x_{2}, \ldots, x_{m}\right]$ be a sample of $m$ features (variables). Let $\mathbf{D} \in \mathbb{R}^{n \times m}$ be a data matrix of $n$ samples. The $i$-th row of $\mathbf{D}$ represents a sample $\mathbf{x}_{i}$. The $j$-th column of $\mathbf{D}$, denoted as $\mathbf{f}_{j}$, represents a realization of the $j$-th variable $x_{j}$ on the $n$ samples.

A Bayesian network (BN) $\mathscr{G}$ is a directed graph that expresses the factorization property of a joint distribution $p(\mathrm{x})$. With each variable correponding to a node in $\mathscr{G}$, the joint distribution is factorized as $p(\mathrm{x})=\prod_{i=1, \cdots, m} p\left(x_{i} \mid \mathbf{P a}\left(x_{i}\right)\right)$, where $\mathbf{P a}\left(x_{i}\right)$ denotes the parent nodes of $x_{i}$. A GBN assumes that $p\left(x_{i} \mid \mathbf{P a}\left(x_{i}\right)\right)$ follows a Gaussian distribution. Each node $x_{i}$ is regressed over its parent nodes $\mathbf{P a}\left(x_{i}\right): x_{i}=\boldsymbol{\theta}_{i}^{\top} \mathbf{P a}\left(x_{i}\right)+\varepsilon_{i}$, where the vector $\theta_{i}$ is the regression coefficients, and $\varepsilon_{i} \sim \mathscr{N}\left(0, \sigma_{i}^{2}\right)$. The matrix $\Theta=\left[\theta_{1}, \ldots, \theta_{m}\right]$ are called the parameters of a GBN. A BN has to be a directed acyclic graph (DAG), in which there must be no directed cycles. In this paper, following [2], a $p \times p$ matrix $\mathbf{G}$ is used to represent network structure, in which, if there is a direct edge from $x_{i}$ to $x_{j}, \mathbf{G}_{i j}=1$; otherwise, $\mathbf{G}_{i j}=0$. In addition, another $p \times p$ matrix $\mathbf{P}$ is also kept to record all the directed pathes in the structure. If there is a directed path from $x_{i}$ to $x_{j}, \mathbf{P}_{i j}=1$; otherwise $\mathbf{P}_{i j}=0$.

### 2.2. Sparse Gaussian Bayesian Network

The state-of-the-art work for brain causal relationship analysis in [2, 1] underpins our study in this paper. In [2, 1], it is proposed to learn a sparse GBN (SGBN) for brain effective connectivity analysis utilizing FDG-PET images. Compared with the conventional BN methods that learn the network structure and parameters in two steps, SGBN simultaneously learns the structure and parameters by enforcing sparseness constraint on a GBN. This onestep learning approach outperforms the conventional two-step methods with higher accuracies for the network edge recovery. In particular, it is proposed in [2, 1] to solve a constrained least-square fitting problem:

$$
\begin{aligned}
& \min _{\boldsymbol{\theta}} \sum_{i=1}^{m}\left\|\mathbf{f}_{i}-\boldsymbol{\theta}_{i}^{\top} \mathbf{P a}\left(\mathrm{x}_{i}\right)\right)\left\|_{2}+\lambda_{1}\right\| \boldsymbol{\theta}_{i} \|_{1} \\
& \text { s.t. } \left\|\boldsymbol{\Theta}_{j i}\right\| \times \mathbf{P}_{i j}=0, \forall i, j=1, \cdots, m, i \neq j
\end{aligned}
$$

Here $\mathbf{f}_{i}$ and $\theta_{i}$ are defined as above. The $i$-th row of the matrix $\mathbf{P a}\left(\mathbf{x}_{i}\right)$ correpond to the parent nodes of $x_{i}$, which are initially set as all the nodes other than $x_{i}$, and further filtered implicitly by the sparseness constraint over their regression coefficients $\theta_{i}$. In BN learning, a difficult problem is how to enforce the DAG property to ensure the validity of the resulting BN. In [2] it is proved that a sufficient and necessary condition for a DAG is $\left|\Theta_{j i}\right| \mathbf{P}_{i j}=0$ for all $i$ and $j$. The $\mathbf{P}_{i j}$ is computed by a Breadth-first search on $\mathbf{G}$ with $\mathbf{x}_{i}$ being the root node. For more details, please read $[2,1]$.

# 3. Our Method 

In this paper, we study brain networks from two sources. The first source is gray matter morphology from T1-weighted MRI. It has been reported that the covariation of gray matter morphology might be related to the anatomical connectivity [16]. Studying brain morphology as a network can take the advantage of statistical tools from graph theory. The second source is FDG-PET images. The retention of tracer in FDG-PET is analogue to the glucose uptake, thus reflecting the tissue metabolic activity.

Building brain network includes identifying network nodes and reconstructing the connectivity. This paper focus on the latter. Therefore, after briefing how network nodes are defined in our method in Section 3.1, we concentrate on how to infer the effective connectivity that is both representative (Section 3.2) and discriminative (Section 3.3).

### 3.1. Determine Network Nodes

MRI—This study involves 120 subjects including 50 MCI (mild cognitive impairment, a prodromal of AD) patients and 70 NC (normal controls) from the publicly accessible data of ADNI. The T1-weighted MR images are segmented into gray matter (GM), white matter (WM), and cerebrospinal fluid (CSF) using FAST in the FSL ${ }^{2}$ package after intensity correction, skull stripping, and cerebellum removal. These tissue-segmented images are spatially normalized into a template space by HAMMER ${ }^{3}$, and partitioned into 100 Region of Interest (ROI) via an ROI atlas [4]. We use the GM volumes of each ROI as network nodes, and select 40 ROIs that have the highest correlation with class labels into our study. The ROI names are provided in the supplementary material.

PET—This study involves 103 subjects including 51 AD patients and 52 NC whose FDGPET and MR images are downloaded from ADNI. We first co-register the MR images into a template space and partition them into ROIs as mentioned above. Then the PET images are aligned with their MR images from the same subject by a rigid transformation. The average tracer uptakes within each ROI are used as network nodes. Similarly, we select 40 ROIs that are most discriminative with regards to AD (see the supplementary material).

### 3.2. Augment SGBN in $[2,1]$

A simple way to use generative BNs for prediction is to train each class a BN and classify a new sample $\mathbf{x}_{i}$ by assigning it to the class with a higher likelihood ratio. The more precisely the BN model reflects the underlying distribution, the more accurate the prediction. The comparison of the likelihood must be conducted in the same space, which means the data should not be normalized separately for each class as in [2] where a single population is focused.

Regression of a node $x_{i}$ over all other nodes leads to an estimated expectation $\hat{\mathbb{E}}\left[x_{i}\right]=\boldsymbol{\theta}_{i}^{\top} \mathbb{E}\left(\operatorname{Pe}\left(x_{i}\right)\right)$. This agrees with the true $\mathbb{E}\left[x_{i}\right]$ in [2] if the sparseness constraint is not considered, because every feature (node) has been normalized to have a zero mean, and

[^0]
[^0]:    2 http://fsl.fmrib.ox.ac.uk/fsl/fslwiki/
    ${ }^{3}$ http://www.med.unc.edu/bric/ideagroup/tools/projects-1/brain/pages-1/hammer

a unit standard deviation. However, $\hat{\mathbb{E}}\left[x_{i}\right]$ may largely deviate from $\mathbb{E}\left[x_{i}\right]$ when the normalization cannot be performed or the underlying data relationship is not linear.

To handle this, we introduce a bias term $x_{0}$ in the regression, i.e., $x_{i}=\boldsymbol{\theta}_{i}^{\top}\left[\operatorname{Pa}\left(x_{i}\right), x_{0}\right]+\varepsilon_{i}$. Accordingly, in the graph $\mathscr{G}$, a bias node is added, which has no parent but being the parent of all the other nodes. If originally $\mathscr{G}$ is a DAG, adding $x_{0}$ in this way will not cause the violation of DAG. To be distinguished from SGBN in [2], we call ours A-SGBN. Intuitively, there may be two reasons to include a bias node into a brain network: i) there possibly exist some latent variables related to the disease, which are not included into the current study, and their influences may be absorbed by the bias node; or ii) the state of a node may depend not only on the interactions with other nodes, but also on the prior of itself. Our experiment in Section 4 indicates that A-SGBN may be a more precise model than SGBN (smaller fitting errors for both the training and the test data), thus improve the classification. Despite the advantage of A-SGBN over SGBN, in the following we show that actively learning the discrimination can further boost the classification performance.

# 3.3. Discriminatively Learn SBN via Fisher Kernel 

Both SGBN and A-SGBN learn the brain network for AD or NC separately. This may ignore some subtle but important network differences that distinguish the two classes. We argue that the parameters of the generative model should be learned from the two classes jointly to keep the essential discrimination. This can be achieved by maximizing the posterior probability $p(y \mid \mathbf{x})$, where $y$ is the class label of $\mathbf{x}$. Although conceptually direct, this approach often leads to complicated optimization problems. This paper takes another approach. Specifically, we employ Fisher kernel to extract feature vectors from the SGBN models of two classes, and then convert the model parameter learning to Fisher kernel learning with SVMs. We find that the SGBN-induced Fisher vector (see below) is a linear function of parameters $\theta$, which well simplifies the optimization.
3.3.1 Induce Fisher Vectors from SGBN-Below we introduce how to use Fisher kernel on SGBNs to obtain feature vectors used for kernel learning.

Fisher kernel provides a way to compare samples induced by a generative model. It maps a sample to a feature vector in the gradient space of the model parameters. The intuition behind is that similar objects induce similar log-likelihood gradients of the model parameters. Fisher kernel is computed as $K\left(\mathrm{x}, \mathrm{x}^{\prime}\right)=\mathrm{g}_{\mathrm{x}}^{\top} \mathbf{U}^{-1} \mathrm{~g}_{\mathrm{x}^{\prime}}$, where the Fisher vector $\mathrm{g}_{\mathrm{x}}$ $=\cdot \theta \log (p(\mathbf{x} \mid \theta))$ describes the changing direction of parameters to better fit the model. The Fisher information metric $\mathbf{U}$ weights the similarity measure, but is often set as an identity matrix in practice [3].

Fisher kernel has recently witnessed successful applications in image categorization [13, 5] for inducing feature vectors from Gaussian Mixture Model (GMM) of a visual vocabulary. Despite its success, to the best of our knowledge, Fisher kernel has not been applied to BN for brain connectivity analysis. More importantly, in the applications above, there is no discriminative learning for Fisher kernel as in this paper. The advantage of discriminative

Fisher kernel has also been confirmed by a very recent study that uses a different learning criterion within a different context [9].

Following [2, 1], we only consider $\Theta$ as parameters and predefine $\sigma$. Let $\mathscr{L}(\mathrm{x} \mid \boldsymbol{\Theta})=\log (p(\mathrm{x} \mid \boldsymbol{\Theta})$ denote the log likelihood. Our Fisher vector for each sample $\mathbf{x}$ is $\Phi_{\Theta}(\mathrm{x})=\left[\nabla_{\Theta_{1}} \mathscr{L}\left(\mathrm{x} \mid \Theta_{1}\right)^{\top}, \nabla_{\Theta_{2}} \mathscr{L}\left(\mathrm{x} \mid \Theta_{2}\right)^{\top}\right]^{\top}$, where $\Theta_{1}$ and $\Theta_{2}$ are the parameters of the SGBNs for the two class $(y=1,2)$, respectively. Recall that, using a BN, the probability $p(\mathbf{x} \mid \Theta)$ can be factorized as $p(\mathrm{x} \mid \Theta)=\prod_{i=1, \cdots, m} p\left(x_{i} \mid \operatorname{Pa}\left(x_{i}\right), \boldsymbol{\theta}_{i}\right)$. Therefore, it holds that

$$
\begin{aligned}
\mathscr{L}(\mathrm{x} \mid \Theta)) & =\sum_{i=1}^{m} \log p\left(x_{i} \mid \operatorname{Pa}\left(x_{i}\right), \boldsymbol{\theta}_{i}\right) \\
& =\sum_{i=1}^{m} \frac{-\left(x_{i}-\boldsymbol{\theta}_{i}^{\top} \operatorname{Pa}\left(x_{i}\right)\right)^{2}}{2 \sigma_{i}^{2}}-m \log \left(2 \pi \sqrt{\sigma_{i}}\right)
\end{aligned}
$$

Taking partial derivative over $\theta_{0}$, we have

$$
\begin{aligned}
\frac{\partial \mathscr{L}(\mathrm{x} \mid \boldsymbol{\Theta})}{\partial \boldsymbol{\theta}_{i}} & =-\frac{\operatorname{Pa}\left(x_{i}\right) \operatorname{Pa}\left(x_{i}\right)^{\top}}{\sigma_{i}^{2}} \boldsymbol{\theta}_{i}-\frac{x_{i} \operatorname{Pa}\left(x_{i}\right)}{\sigma_{i}^{2}} \\
& \triangleq \mathbf{S}\left(x_{i}\right) \boldsymbol{\theta}_{i}+\mathrm{s}_{0}\left(x_{i}\right)
\end{aligned}
$$

where $\mathbf{S}\left(x_{i}\right)$ is a matrix and $\mathbf{s}_{0}\left(x_{i}\right)$ is a vector. As shown, $\Phi_{\Theta}(\mathbf{x})$ is a linear function of $\Theta$. This simple form of $\Phi_{\Theta}(\mathbf{x})$ significantly facilitates our further kernel learning.
3.3.2 Learn Discriminative Fisher Kernel via SVM—As each Fisher vector is a function of the SGBN parameters, discriminatively learning these parameters can thus be converted to learning discriminative Fisher kernels. We require that the learned SGBN models possess the following properties. Firstly, the Fisher vectors induced by the learned SGBN model should be well separated between classes. Secondly, the learned SGBN models should maintain reasonable capacity of group representation. Thirdly, the learned SGBN models should not violate DAG.

We use the following strategies to achieve our goal. Firstly, to obtain a discriminative Fisher kernel, we jointly learn the parameters of SGBN and the separating hyperplane of SVMs with Fisher kernel. Radius-margin bound, the upper bound of the Leave-One-Out error, is minimized to keep good generalization of the SVMs. Secondly, to maintain reasonable representation, we explicitly control the fitting errors of the learned model during optimization. Thirdly, we enforce the DAG constraint in [2] to ensure the validity of the graph. For convenience, we call our method DL-A-SGBN. More details are given below.

In order to use radius-margin bound, $\mathscr{L}_{2}$-SVM with soft margin has to be employed, which optimizes

$$
\begin{aligned}
& \min _{\mathbf{w}, \boldsymbol{\xi}} \frac{1}{2}\|\mathbf{w}\|_{2}^{2}+C \boldsymbol{\xi}^{\top} \boldsymbol{\xi} \\
& \text { s.t. } \quad y_{i}\left(\mathbf{w}^{\top} \Phi\left(\mathrm{x}_{i}\right)+b\right) \geq 1-\xi_{i}, \xi_{i} \geq 0, \forall i
\end{aligned}
$$

Following the convention in SVMs, $\mathbf{x}_{i}$ is the $i$-th sample with class label $y_{i}, \mathbf{w}$ the normal of separating plane, $b$ the bias term, $\boldsymbol{\xi}$ the slack variables and $C$ the regularization parameter.

$\mathscr{L} 2$-SVM can be rewritten as SVM with hard margin by slightly modifying the kernel $\mathbf{K}:=$ $\mathbf{K}+\mathbf{I} / C$, where $\mathbf{I}$ is identity matrix. For convenience, in the following, we redefine $\Phi\left(\mathrm{x}_{i}\right):=\left[\Phi\left(\mathrm{x}_{i}\right) \mathrm{e}_{i} / \sqrt{C}\right]$. The vector $\mathbf{e}_{i}$ has the value of 1 at the $i$-th element, and 0 elsewhere.

Incorporating radius information leads to solving

$$
\min _{\mathbf{w}} \frac{1}{2} R^{2}\|\mathrm{w}\|_{2}^{2}
$$

s.t. $\quad y_{i}\left(\mathrm{w}^{\top} \Phi\left(\mathrm{x}_{i}\right)+b\right) \geq 1, \forall i$,
where $R^{2}$ denotes the radius of Minimal Enclosing Ball (MEB). It has been observed that when the sample size is small, the estimation of $R^{2}$ may become noisy and unstable. Therefore, it has been proposed to use trace-based scatter matrix instead for such cases [8]. We optimize

$$
\begin{array}{ll} 
& \min _{\boldsymbol{\theta}, \mathrm{w}} \frac{1}{2} \operatorname{tr}\left(\mathbf{S}_{T}\right)\|\mathrm{w}\|_{2}^{2} \\
\text { s.t. } & y_{i}\left(\mathrm{w}^{\top} \Phi_{\Theta}\left(\mathrm{x}_{i}\right)+b\right) \geq 1, \forall i \\
& h\left(\mathbf{D}_{1}, \boldsymbol{\Theta}_{1}\right) \leq T_{1}, h\left(\mathbf{D}_{2}, \boldsymbol{\Theta}_{2}\right) \leq T_{2} \\
& \boldsymbol{\Theta}_{1} \in D A G, \boldsymbol{\Theta}_{2} \in D A G
\end{array}
$$

Here $\operatorname{tr}\left(\mathbf{S}_{T}\right)$ is the trace of the total scatter matrix $\mathbf{S}_{T}$, where $\mathbf{S}_{T}=\sum_{i=1}^{n}\left(\mathrm{x}_{i}-m\right)^{\top}\left(\mathrm{x}_{i}-\mathrm{m}\right)$, and $\mathbf{m}$ is the mean of total $n$ samples. It can be shown that $\operatorname{tr}\left(\mathbf{S}_{T}\right)=\operatorname{tr}(\mathbf{K})-\mathbf{1}^{\top} \mathbf{K} \mathbf{1} / n$, where $\mathbf{1}$ denotes a vector whose elements are all 1, and $\mathbf{K}$ the kernel matrix. Fisher vector $\Phi_{\Theta}\left(\mathbf{x}_{i}\right)$ is obtained as mentioned in Section 3.3.1. The function $h(\cdot)$ measures the squared fitting errors of the corresponding SGBNs for the data $\mathbf{D}_{1}$ and $\mathbf{D}_{2}$ from the two classes. It is defined as

$$
h(\mathbf{D}, \boldsymbol{\Theta})=\left.\sum_{i=1}^{m}\left\|\mathbf{f}_{i}-\boldsymbol{\theta}_{i}^{\top} \mathbf{P a}\left(\mathrm{x}_{i}\right)\right)\right\|_{2}
$$

where all the symbols are defined as in 1 . The two user-defined parameters $T_{1}$ and $T_{2}$ explicitly control the degree of fitting during the learning process (Section 4.2). The DAG constraints here are the same to that used in 1. Please recall that the DAG constraint is $\left|\Theta_{j i}\right|$ $\times \mathbf{P}_{i j}=0$, where $\mathbf{P}_{i j}=\{0,1\}$, reflecting the structure of $\Theta$. Enforcing DAG in this way has somewhat enforced the graph sparcity (by constraining the $\mathscr{L} 1$-norm of $\Theta_{i j}$ ). Therefore, we do not impose additional sparseness constraints on $\Theta$ to keep our optimization simple.

One possible approach for solving Eqn. (6) is to alternately optimize the separating hyperplane $\mathbf{w}$ and the parameter $\Theta$. That is,

$$
\begin{array}{ll} 
& \min _{\boldsymbol{\theta}} J(\boldsymbol{\Theta}) \\
\text { s.t. } & h\left(\mathbf{D}_{1}, \boldsymbol{\Theta}_{1}\right) \leq T_{1}, h\left(\mathbf{D}_{2}, \boldsymbol{\Theta}_{2}\right) \leq T_{2} \\
& \boldsymbol{\Theta}_{1} \in D A G, \boldsymbol{\Theta}_{2} \in D A G
\end{array}
$$

where

$$
\begin{aligned}
& J(\boldsymbol{\Theta})=\min _{w} \frac{1}{2} \operatorname{tr}\left(\mathbf{S}_{T}\right)\|\mathrm{w}\|_{2}^{2} \\
\text { s.t. } & y_{i}\left(\mathrm{w}^{\top} \Phi_{\Theta}\left(\mathrm{x}_{i}\right)+b\right) \geq 1, \forall i .
\end{aligned}
$$

Note that for a given $\Theta$, the term $\operatorname{tr}\left(\mathbf{S}_{T}\right)$ is constant to (8). For the term $\|\mathrm{w}\|_{2}^{2}$, due to the strong duality in SVM optimization, we solve it by

$$
\begin{aligned}
J_{0}(\boldsymbol{\Theta}) & =\max _{\boldsymbol{\alpha}} \sum_{i=1}^{n} \alpha_{i}-\frac{1}{2} \sum_{i=1}^{n} \sum_{j=1}^{n} y_{i} y_{j} \alpha_{i} \alpha_{j} K_{\boldsymbol{\Theta}}\left(\mathrm{x}_{i}, \mathrm{x}_{j}\right) \\
\text { s.t. } & \sum_{i=1}^{n} \alpha_{i} y_{i}=0, \alpha_{i} \geq 0 \forall i
\end{aligned}
$$

where $\alpha_{i}$ is the lagrangian multiplier. Many quadratic programming package could be used to solve (7). We use fmincon-SQP (sequential quadratic programming) in matlab. Our learning process is summarized in Table 1.

# 3.3.3 Discussion 

Gradient of (7): A simple form of gradient is favored by many optimization algorithms (including fmincon-SQP) to speed up the line search, which is true in our case. The gradient of the objective function in (7) can be computed as

$$
\begin{aligned}
\nabla_{\Theta} J= & -\frac{1}{2} \operatorname{tr}\left(\mathbf{S}_{T}\right) \sum_{i j} \alpha_{i}^{*} \alpha_{j}^{*} y_{i} y_{j} \nabla_{\Theta} K_{\Theta}\left(\mathrm{x}_{i}, \mathrm{x}_{j}\right) \\
& +J_{0}(\boldsymbol{\Theta})\left(\mathbf{I}+\frac{1}{n} 11^{\top}\right) \nabla_{\Theta} K_{\Theta}\left(\mathrm{x}_{i}, \mathrm{x}_{j}\right)
\end{aligned}
$$

where $\alpha^{*}$ maximizes (9). The symbols $\mathbf{I}$ and $\mathbf{1}$ are defined as before. The terms $\operatorname{tr}\left(\mathbf{S}_{T}\right)$ and $J_{0}(\Theta)$ have been computed when evaluating the objective function $J(\Theta)$ in 7 , thus introduce no additional computational cost. ${ }^{*} \Theta K_{\Theta}\left(\mathbf{x}_{i}, \mathbf{x}_{j}\right)$ is simply a linear function of $\Theta$ :

$$
\begin{aligned}
\frac{\partial K_{\Theta}\left(x_{i}, x_{j}\right)}{\partial \boldsymbol{\theta}_{i}}= & {\left[\mathbf{S}\left(x_{i l}\right)^{\top} \mathbf{S}\left(x_{j l}\right)+\mathbf{S}\left(x_{j l}\right)^{\top} \mathbf{S}\left(x_{i l}\right)\right] \boldsymbol{\theta}_{l} } \\
& +\left(\mathbf{S}\left(x_{j l}\right)^{\top} \mathrm{s}_{0}\left(x_{i l}\right)+\mathbf{S}\left(x_{i l}\right)^{\top} \mathrm{s}_{0}\left(x_{j l}\right)\right)
\end{aligned}
$$

where $x_{i l}$ denotes the $l$-th feature of the $i$-th sample, and $\mathbf{S}$ and $\mathbf{s}_{0}$ are defined in (3).
Variable selection: Learning the whole set of SGBN parameters may encounter the "curse of dimensionality" when the training samples are insufficient. For example, we have less than 100 training samples, but 3600 parameters (from two classes) to learn. This may cause overfitting and make the estimation unstable. To handle this issue, we hypothesis that, learning only a selected subset of parameters may mitigate the overfitting and improve the discrimination. For this purpose, $\theta$ is partitioned into two parts: $\Theta=\left\{\Theta_{\text {sel }} . \Theta_{\text {nosel }}\right\}$. We keep using the whole $\Theta$ for computing $\mathbf{K}_{\Theta}$, but optimize (7) only over $\Theta_{\text {sel }}$. There are many options to determine $\Theta_{\text {sel }}$. We initially compute the Pearson correlation between each component of $\Phi_{\Theta}$ and the class labels on the training data, and select the top $\theta_{i}$ with the highest correlations. To keep our problem simple, only the parameters associated with edges present in the graph are optimized. In this way, the optimization may only eliminate but never add edges in the graph, which avoids the violation of DAG, as well as maintaining the

sparcity of the initial A-SGBN. It is remarkable that even this simple selection process has been able to greatly improve the discrimination experimentally.

Extension: Although focusing on each node corresponding to a scalar ROI feature, our method is readily to be extended to handle multiple features (feature vector) of an ROI. In this case, the conditional distribution for node $i$ becomes
$p\left(\mathrm{x}_{i} \mid \mathbf{P a}\left(\mathrm{x}_{i}\right)\right)=\mathcal{N}\left(\mathrm{x}_{i} \mid \sum_{\mathrm{x}_{j} \in \mathbf{P A}\left(\mathrm{x}_{i}\right)} \mathbf{M}_{i j} \mathrm{x}_{j}, \Sigma_{i}\right)$, where $\mathbf{P A}$ and $\mathbf{M}$ are all matrix. Our learning remains the same. In our future work, we will apply this extension to analyze fMRI where each ROI is associated with a vector of temporal signal.

# 4. Experiment 

We test our proposed A-SGBN and DL-A-SGBN with the baseline SGBN (B-SGBN) from [2] (without normalizing the data) in three aspects: i) model fitting, ii) discrimination, and iii) connectivity. Three data sets are used in our experiment: the MRI and FDG-PET data mentioned in Section 3.1, and another MRI-II data that uses the MR images from the same subjects as MRI, but involves 40 different ROIs (see supplementary material). Although not as discriminative as that in MRI, the ROIs in MRI-II are more spread across the frontal, parietal, occipital and frontal lobes, thus specially used for a detailed lobe-to-lobe comparison on connectivity. We randomly partition each data set into 30 groups of trainingtest pairs. Each group includes 80 training and 40 test samples in MRI and MRI-II, or 60 training and 43 test samples in PET.

### 4.1. Comparison of Fitting

Our DL-A-SGBN targets to become discriminative without sacrificing too much power of data representation compared with B-SGBN. Since the change of data fitting from A-SGBN to DL-A-SGBN has been explicitly controlled by the user-defined parameters $T_{1}$ and $T_{2}$, we simply compare the model fitting between A-SGBN and B-SGBN. The fitting errors are tested on both training and test data for each class in all three data sets. The root of mean squared fitting errors (RMS) are summarized in Table 2. In order to test if the fittings of ASGBN is statistically different from that of B-SGBN, a paired t-test (two-tailed) is conducted on the fitting errors over the 30 groups for each data set, respectively. The resulting $p$-value is also given in the last column in Table 2.

As shown, on all three data sets, our A-SGBN fits the data consistently better than B-SGBN. Such improvement is significant as indicated by the small $p$-values (except for MCI group in MRI-II). This finding indicates that our A-SGBN might better reflect the underlying distribution of the data, which makes it perform well on both the training and the test data. Another interesting finding is that the generative models explain the NC better than the MCI (in MRI data set) or the AD (in PET data set) patients. This may reflect the common impression that compared with the healthy population, the AD population might be more heterogeneous and therefore have more difficulty to find a unified model for representation.

# 4.2. Comparison of Discrimination 

Our proposed learning process results in two kinds of models: two DL-A-SGBN models with one for each class, and one SBN-induced SVM classifier that considers only the boundary of the two classes. We test whether our learning can improve the discrimination power on both kinds. The A-SGBN models estimated separately for each class are used as the initial solution. In order to keep reasonable interpretation, we allow maximal $1 \%$ additional squared fitting errors (that is, $T_{i}=1.01 \times T_{i 0},(i=1,2)$, where $T_{i 0}$ is the squared fitting error of the initial solution) to be introduced during the learning of DL-A-SGBN. We test both the SVM classifier and the DL-A-SGBNs. For the SVM classifier, to agree with (6), we use $\mathscr{L} 2$-SVM with Fisher kernels. For DL-A-SGBNs, as mentioned before, we simply compare the values of the estimated likelihood, and assign the sample to the class with a larger likelihood. We also conduct a paired t-test (two-tailed) to examine the statistical significance of the improvement over the 30 groups for all three data sets. The results are summarized in Table 3.

It can be seen that, as expected, optimizing (6) significantly improves the discrimination power of SVM classifiers by $3.08 \%$ for MRI, $7.68 \%$ for PET, and $4.58 \%$ for MRI-II. More importantly, by learning a discriminative SVM classifier, we also simultaneously improve the discrimination power of the generative models DL-A-SGBN by $3.75 \%$ for MRI, $4.11 \%$ for PET, and $5.67 \%$ for MRI-II. Such improvements are statistically significant as indicated by the small p-values. Moreover, when cross-referencing the third columns in Table 3, it is noticed that our SVM classifiers perform just comparably (for MRI) or even worse (for PET and MRI-II) than our generative DL-A-SGBNs. This may be because our Fisher vectors have very high dimensionality, which causes the serious overfitting of data in SVM classifiers. Such situation might be somewhat leveraged for DL-A-SGBN since the Gaussian model may regularize the fitting. Based on this assumption, we further select a number of leading features from Fisher vectors by computing the Pearson corrlation of the features and the labels, and use the selected features to construct the Fisher kernel for the SVM classifiers. As shown in the last column in Table 4, the simple feature selection step can further significantly improve the classification performance of the fisher-kernel based SVM: from $74.5 \%$ to $80.08 \%$ for MRI, from $65.43 \%$ to $77.83 \%$ for PET, and from $61.83 \%$ to $73.5 \%$ for MRI-II.

In Table 4, the improvement from our proposed learning method is scrutinized at each processing step. Compared with the B-SGBN induced from [2], introducing a biased node (A-SGBN) better fits the population, therefore improves the prediction on test data by $9 \%$ for MRI, $6.04 \%$ for PET, and $6.67 \%$ for MRI-II. The discrimination power of A-SGBN is further improved by $3 \sim 6 \%$ via our discriminative parameter learning. This leads to generative models DL-A-SGBN achieving a classification accuracy above $70 \%$, with no more than $1 \%$ increase of the squared fitting error. Morever, by selecting leading features in the SGBN-induced Fisher vectors, we can construct more discriminative SVM classifiers with additional $6 \%$ or more improvement from our DL-A-SGBN to differentiate both MCI vs NC groups in MRI or MRI-II and AD vs NC groups in PET.

In summary, compared with the baseline B-SGBN, our proposed method can increase the prediction accuracies as high as $\mathbf{1 8 \%}$ for MRI, $\mathbf{1 6 \%}$ for PET, and $\mathbf{2 0 \%}$ for MRI-II by using Fisher kernel induced SVM classifiers with feature selection. Meanwhile, these SVM classifiers are linked to the learned generative model DL-A-SGBN whose discrimination powers have also been increased by about $10 \%$ from B-SGBN on all three data sets. Our DL-A-SGBN models are not only discriminative, but also descriptive with only a slight increase in the squared fitting errors (at most $1 \%$ increase, controlled by the optimization parameter).

# 4.3. Comparison of Connectivity 

In order to gain more insight into the results, we also conduct a lobe-to-lobe comparison on the connectivity derived by our methods and B-SGBN. It is found that, although the 40 ROIs used in MRI and PET are individually discriminative, they do not necessarily cover the representative regions across the whole brain. For example, the 40 nodes used in the MRI data set are mostly located in the temporal lobe and the subcortical region. Therefore, we specially design the MRI-II data set by selecting 40 regions that cover the frontal, parietal, occipital and temporal (including the subcortical region) lobes from MR images of the same subjects involved in MRI data. Although MRI-II (with the best test accuracy of $73.5 \%$ ) is less discriminative than MRI (with the best test accuracy of $80.08 \%$ ) as shown in Table 4, we consistently observe significant improvements of our method over B-SGBN.

The structures of the brain networks recovered from NC and MCI groups are displayed in Fig. 2 by using B-SGBN and DL-A-SGBN, respectively. The network structure is obtained by binarizing the edges $\theta$ with a threshold of 0.01 . Each row $i$ represents the effective connections (dark dots) starting from the node $i$, and each column $j$ representes the effective connections ending at the node $j$.

With similar parameter settings, the B-SGBN produces 273 edges for NC, and 224 edges for MCI, while our DLA-SGBN produces 285 edges for NC, and 236 edges for MCI. Please note that DL-A-SGBN has an additional bias node corresponding to the last row and column. Because the bias node has no parent node, the last column is all zero. We check the edge difference between the two methods lobe by lobe, and give the result in Table 5. As shown, the two methods produce similar network structures both visually and quantitatively in most brain regions. There are in total 36 different edges (less than 15\%) for NC network, and 11 different edges (around 5\%) for MCI network. About half different connections are identified within the temporal lobe ( 15 for NC, 5 for MCI), for which we also include subcortical structures such as hippocampus and amygdala. It is known that temporal lobe (and some subcortical structures) plays a very important role in the progression of AD. Such a structural difference in this lobe may potentially reflect the different capacity of prediction between our DL-A-SGBN and the B-SGBN.

Traditional brain connectivity analysis focuses on the analysis of brain structure which is a binarized connectivity. For example, the network structures from both the BSGBN and our DL-A-SGBN indicate the loss of effective connections (around 17\%) in MCI group in almost all lobes (slightly in the frontal lobe), which agrees well with documented studies. However, binarizing connectivity depends on the selection of threshold. If some connection

strength has been weakened by the disease but not reduced below the threshold, this change will be unnecessarily ignored when merely studying the brain structure. This observation is affirmed by our learning process that promotes the discrimination of A-SGBN. Simply optimizing the connection strength across a subset of selected nodes has already significantly improved the prediction with only a minimum (or mostly no) change of brain structure.

Moreover, using SGBN-induced fisher kernels, we are able to produce a new kind of features to analyze brain connectivity: the subject specific change of connection strength between nodes. We investigate the selected features of MRI-II used in our SBN-induced SVM classifier and visualize three most discriminative connection changes (Fig. 1 right) happening at "middle temporal gyrus left" (in brown) $\rightarrow$ "superior parietal lobe left" (in purple), "hippocampus right" (in blue) $\rightarrow$ "superior parietal lobe left", and "inferior temporal gyrus left" (in green) $\rightarrow$ "middle occipital gyrus right" (in cyan). Also discriminative are the connections from the bias node to "middle occipital gyrus right" and to "precuneus left".

# 5. Conclusion 

In this paper, we present a framework to model brain effective connectivity encoded with essential discrimination information. With the link of Fisher kernel, our proposed framework is able to simultaneously produces generative SGBN models and its associated SVM classifier that are sufficiently discriminative for brain network analysis for AD. In addition, by considering the changes rate of connection strength, our method also provides a new perspective for brain connectivity analysis.
