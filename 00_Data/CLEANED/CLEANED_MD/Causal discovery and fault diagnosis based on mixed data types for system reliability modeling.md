# Causal discovery and fault diagnosis based on mixed data types for system reliability modeling 

Xiaokang Wang ${ }^{1} \cdot$ Siqi Jiang ${ }^{1} \cdot$ Xinghan $\mathrm{Li}^{2} \cdot$ Mozhu Wang ${ }^{1}$<br>Received: 16 January 2024 / Accepted: 1 December 2024 / Published online: 4 January 2025<br>(c) The Author(s) 2024


#### Abstract

Causal relationships play an irreplaceable role in revealing the mechanisms of phenomena and guiding intervention actions. However, due to limitations in existing frameworks regarding model representations and learning algorithms, only a few studies have explored causal discovery on non-Euclidean data. In this paper, we address the issue by proposing a causal mapping process based on coordinate representations for heterogeneous non-Euclidean data. We propose a data generation mechanism between the parent nodes and the child nodes and create a causal mechanism based on multi-dimensional tensor regression. Furthermore, within the aforementioned theoretical framework, we propose a two-stage causal discovery approach based on regularized generalized canonical correlation analysis. Using the discrete representation in the shared projection direction, causal relationships between heterogeneous non-Euclidean variables can be discovered more accurately. Finally, empirical research is conducted on real-world industrial sensor data, which demonstrates the effectiveness of the proposed method for discovering causal relationships in heterogeneous non-Euclidean data.


Keywords Causal discovery $\cdot$ Non-Euclidean data $\cdot$ Canonical correlation analysis $\cdot$ Industrial fault diagnosis

## Introduction

In recent years, with the rapid advancement of information technology such as sensors and hardware storage, artificial intelligence algorithms based on deep learning have seen widespread application. However, current machine learning methods primarily capture correlations within the data rather than causality, limiting their ability to answer intervention or counterfactual questions [1]. For example, researchers might want to predict a patient's potential response to medication or the impact on their recovery if the medication were not taken. Addressing such questions requires an understanding of the causal relationships underlying the data.

In real-life scenarios, the structure of causal networks is often unknown, particularly when dealing with highdimensional variables. Traditional methods for discovering causal relationships through randomized experiments are

[^0]typically expensive and may pose ethical risks. Therefore, discovering meaningful causal relationships from purely observational data remains an urgent research challenge in the field of data science. This is essential for guiding intervention strategies and analyzing causal effects [2].

Existing causal discovery methods can be broadly categorized into three main approaches: constraint-based methods, score-based methods, and functional causal models [2]. Constraint-based methods begin with a fully connected undirected network and use conditional independence tests to remove edges that are conditionally independent. They then identify v-structures and collider structures in the network based on a set of directional rules while ensuring acyclicity. This process ultimately results in a Markov equivalence class of directed acyclic graphs (DAGs) that encode the same conditional independence relationships. Score-based methods, on the other hand, use a scoring function to measure the goodness-of-fit of the model to the data, incorporating sparsity penalties to prevent overfitting. The aim of these methods is to identify causal relationships within the Markov equivalence class. Functional causal modeling methods utilize structural equation models (SEMs) to fully identify causal relationships within the Markov equivalence class. The causal direction is determined by testing


[^0]:    囚 Mozhu Wang
    mz.wang@bupt.edu.cn
    1 School of Economics and Management, Beijing University of Posts and Telecommunications, Beijing, China
    2 International School, Beijing University of Posts and Telecommunications, Beijing, China

the independence between the independent and noise variables. Examples of methods in this category include Linear Non-Gaussian Acyclic Models (LiNGAM), Post Nonlinear models (PNL), and Additive Noise models (ANM).

The aforementioned causal discovery methods assume that the data consist entirely of homogeneous discrete or numerical variables. However, in many application scenarios such as financial markets, healthcare, and government institutions, data obtained from multiple sources often exhibit diverse characteristics, including pie charts and continuous curves [3]. Such complex data need to be represented by specific geometric structures on a non-Euclidean space, commonly referred to as non-Euclidean data [4, 5]. NonEuclidean data are prevalent in social networks, gene regulatory networks, large-scale sensor networks, and other fields. Common types include compositional data, functional data, and positive semidefinite manifold data.

For example, Bruno et al. (2015) [6] measured the distribution of inhalable particles of different diameters at various heights in Milan, Italy. At a particular height, the relative proportions of each particle size constitute a set of compositional data. The temperature, humidity, and other indicators that continuously change over time at each measurement location can be considered functional data. Moreover, it is often necessary to simultaneously consider two or more types of data. Balancing the inherent geometric structure differences among different data types and developing statistical theories and hybrid modeling methods compatible with different algebraic systems are crucial for applying non-Euclidean data analysis theory to causal discovery based on observational data.

To date, most causal discovery methods for heterogeneous data types have focused on mixing numerical and discrete data [7-9]. Specifically, these methods either discretize continuous variables [10] or transform the conditional distributions of mixed-type variables into a uniform type [11, 12]. For instance, the Copula PC algorithm [13] modifies rank-based correlation measures in continuous spaces to accommodate discrete variables. Similarly, Causal MGM [14] employs a likelihood ratio test for conditional independence tests, applying linear regression for continuous variables and multinomial logistic regression for categorical variables. The above-mentioned methods all rely on linear assumption of the causal mechanism or some parametric form that makes them restrictive.

In this work, the goal is to develop a causal discovery method for a dataset of mixed non-Euclidean data, which possess some unique challenges beyond the previous case involving only numerical and discrete data. First, each type of non-Euclidean data originates from a different distribution, necessitating the construction of a common subspace to define inner products and covariances between heterogeneous variables under a unified algebraic system. Second, existing methods are unable to effectively describe the causal mechanisms between different types of data. For instance, defining the impact of changes in the proportions of components on the overall shape of a curve, where an increase in one component's proportion corresponds to a decrease in the proportions of others, remains problematic. Third, for non-Euclidean data lacking linear structures, appropriate correlation measures are required, especially in high-dimensional scenarios.

The proposed framework involves a mixed heterogeneous non-Euclidean causal model (MH-NECM) and a causal network structure learning method based on this model. Specifically, MH-NECM first projects the non-Euclidean data, along with their complete inner product structures, into a set of unconstrained numerical variables in Euclidean space. This process results in the coordinate representation of non-Euclidean data within their respective coordinate systems. To describe the causal mechanisms between different types of non-Euclidean data, a multivariate mapping process is proposed. Furthermore, a non-Euclidean causal network structure learning (NE-CNSL) method is introduced to handle mixed non-Euclidean data. This method utilizes generalized regularized canonical correlation analysis (CCA) to calculate dependency measures while simultaneously extracting the inherent feature information of non-Euclidean data. Subsequently, a greedy hill-climbing search algorithm is employed to obtain the directed acyclic graph (DAG) structure of the causal network. To summarize, the main contributions of this work are as follows:
(1) This paper extends classical causal network structure learning methods to handle complex heterogeneous nonEuclidean data. It proposes a coordinate representation approach for different types of data within a unified framework.
(2) A causal mechanism is introduced by leveraging the equivalence relationship between the respective algebraic spaces and Euclidean space. This mechanism consists of a generalized causal mapping process constructed within the latent projected subspace.
(3) The paper presents an efficient causal network structure learning method that utilizes dependency measures based on canonical correlation. This method provides a flexible algorithmic framework for handling mixed nonEuclidean data types.

In Sect. "background", we introduce mainstream causal discovery methods and common approaches for dealing with heterogeneous data. Section "Theoretical framework" presents a causal theoretical model based on mixed heterogeneous non-Euclidean data. A detailed description of the proposed algorithm is provided in Sect. "Method". Section "Numerical experiments" aims to compare the accuracy

of the algorithm in discovering causal relationships using multiple simulated datasets and Sect. "Real-world data analysis" presents a real-world dataset collected from an industrial sensor network. Finally, Sect. "Discussion and conclusion" summarizes this work and provides directions for future research.

## Background

In Sect. "Causal discovery methods based on observational data", we will provide an overview of three types of causal discovery methods based on observational data. In Sect. "Methods for discovering causal relationships based on heterogeneous data", we will discuss causal discovery methods based on heterogeneous data that combines numerical and categorical data. We will also explore causal discovery algorithms for non-Euclidean data of a single type.

## Causal discovery methods based on observational data

Causal discovery methods can be classified into three categories [2]: constraint-based methods, score-based methods, and functional causal models.

Constraint-based methods, such as the Peter-Clark (PC) algorithm, the Inductive Causation (IC) algorithm, and the FCI (Fast Causal Inference) and RFCI (Really Fast Causal Inference) algorithms for handling latent variables [15, 16], start with a completely undirected graph. These methods learn the skeleton of the causal network using conditional independence tests. Then, they utilize the v-structures and directional rules implied by independence information to determine the direction of edges as much as possible. Constraint-based methods do not make any assumptions about the form of the causal mechanisms, making them more adaptable to handle complex data types, including nonstationary time series data or mixed heterogeneous data. For example, Sun et al. [17] proposed a conditional independence measure based on kernel-based Hilbert-Schmidt norms (HSN), and Zhang et al. [18] introduced a kernel function-based conditional independence testing method for non-independent and identically distributed data.

Score-based methods utilize a scoring function and tackle a combinatorial optimization problem to select the network structure with the highest score. The Notears algorithm, introduced by Zheng et al. [19], stands out as a renowned score-based method that integrates the smoothness constraint of a directed acyclic graph (DAG) into the scoring function. It addresses a continuous optimization objective to derive the Bayesian network structure. Subsequently, various researchers have enhanced the Notears method. Pamfil et al. [20] extended the Notears algorithm to accommodate time series data. Goudet et al. [21] proposed a causal generative neural network approach that merges neural networks with continuous optimization, thereby eliminating the necessity of manually specifying the causal function form and discovering the optimal network structure in a data-driven manner. Ng et al. [22] reformulated the structure learning problem into a graph autoencoder model, which proves to be more effective in uncovering nonlinear structural relationships between variables.

In contrast to traditional causal network structure learning methods, functional causal models represent the data generation process using structural equation models (SEMs). Shimizu et al. (2014) [23] proposed the linear non-Gaussian acyclic model, which uniquely identifies the causal network structure within the linear SEM framework when the data follow a non-Gaussian distribution. The network structure can be determined using independent component analysis (ICA). Some methods assume the presence of observational errors in a nonlinear functional form and propose additive noise models (ANMs) [24]. Zhang et al. (2015) [25] introduced a more general post-nonlinear model (PNL). Generally, if the data satisfy the assumptions of the functional causal model, it is impossible to find a reverse causal model where the noise is independent of the causal variable. Therefore, the independence between the noise and the causal variable is crucial for determining the direction of causality in such models.

In summary, the constraint-based approach faces the challenge of "indistinguishable Markov equivalence classes", where multiple causal network structures share the same conditional independence relationships, thereby impeding the inference of causal directions for certain edges. Additionally, this approach often fails to produce satisfactory results when the dimension of the conditioning set is high. Conversely, the score-based approach experiences computational performance degradation when dealing with a large number of potential causal structures or high-dimensional variables. Lastly, the functional causal modeling approach heavily relies on assumptions about the model's form, which may yield suboptimal results when the actual data does not meet these assumptions.

## Methods for discovering causal relationships based on heterogeneous data

Most causal discovery methods discussed in the previous section primarily focus on inferring causal relationships among numerical variables. However, when a dataset contains diverse data types, such as a combination of numerical and categorical data, it is necessary to establish an appropriate methodology for determining causal relationships. This can be achieved by devising novel conditional independence tests or formulating likelihood scoring functions that account for mixed data types. Additionally, it is crucial to define the

causal mechanisms between different data types to ensure clear and interpretable interpretations of causal effects.

Marx and Vreeken (2019) [26] introduced a criterion based on Kolmogorov complexity to ascertain causal directions in mixed data. The fundamental idea is that the Kolmogorov complexity, calculated in the 'cause $\rightarrow$ effect | cause' order, is smaller under the correct causal direction compared to the reverse direction. Handhayani and Cussens (2019) [27] computed kernel functions for each variable and used a kernel alignment approach to determine a 'pseudo-correlation' matrix instead of the conditional correlation matrix used in the PC algorithm. They demonstrated the applicability of their approach using a dataset comprising continuous, categorical, and ordinal variables. Liu et al. (2020) [28] extended the ANM model to incorporate causal discovery with mixed numerical and categorical data. They proposed an information-theoretic method for deducing causal directions and employed discrete regression and classification techniques to learn the causal network structure. Wei and Feng (2021) [29] developed a nonlinear causal discovery method specifically designed for mixed numerical and categorical data. Their approach involved searching for the optimal causal ordering through the maximization of a likelihood function, while also using Gaussian process regression based on kernel functions to prune the DAG hyperspace.

Given the intrinsic nonlinear structures of non-Euclidean data, current methods for detecting causal relationships are not directly applicable to complex non-Euclidean data types such as functional data and compositional data [4]. Yang et al. (2022) [4] reviewed existing literature and used functional data and symmetric positive definite manifold data as examples of non-Euclidean data, proposing two types of tensor-based causal function mapping mechanisms. They also introduced a method for discovering the skeleton of a causal network based on spherical covariance and a scorebased DAG search strategy. In the context of compositional data, changes in one component may lead to simultaneous changes in the relative ratio of others due to unit-sum constraints. Arnold et al. (2020) [30] analyzed the identifiability problem of causal effects when intervening in one component of compositional data. They introduced the concept of the Weighted Average Compositional Effect to enhance the interpretability of causal effects. Additionally, Kumakura et al. (2021) [31] integrated the concept of the Reciprocal Logarithmic Ratio with the discovery of nonlinear time series causal relationships, providing a comprehensive framework for causal relationship analysis. Ailer et al. (2021) [32] analyzed the causal effect of compositional variables from the perspective of instrumental variables, emphasizing potential issues surrounding explainability when compositional data are used as intervention variables.

## Theoretical framework

In this section, we present the theoretical framework of the Mixed Heterogeneous Non-Euclidean Causal Model (MHNECM). By leveraging a complete inner product structure in the respective space and employing mutually orthogonal basis systems, we obtain equivalent coordinate representations of different types of variables in Euclidean space. Building on this, we propose a causal mapping process based on the coordinate representations, integrating transformations and inverse transformations between Euclidean space and the original non-Euclidean space. This enables us to fully define the entire causal data generation mechanism.

The observational data are assumed to be obtained from $n$ samples, each containing $J$ variables, represented as $\mathcal{X}=$ $\left[X_{1}, X_{2}, \cdots, X_{J}\right]^{\prime}$. Each variable $X_{j}$, where $j=1, \ldots, J$, is assumed to be generated by a function:
$X_{j}=f\left(\operatorname{Pa}\left(X_{j}\right), n_{j}\right)$,
which includes its parent nodes $\operatorname{Pa}\left(X_{j}\right)$ and independent external noises $n_{j}$. The function $f(\cdot)$ represents the data generation process from the parent nodes to the child nodes.

When dealing with high-dimensional variables or heterogeneous data with different distributions, it is necessary to extend and update the concept of the mapping mechanism in functional causal models. Due to the complex intrinsic structure of non-Euclidean data (such as constraints in compositional data or smoothness in functional data), causal relationships between variables may be embedded within their latent features. Inspired by this feature-based mapping mechanism, Yang et al. (2022) [4] transformed the causal relationships between heterogeneous data types into relationships between their respective features, defining a unified perspective of causal mechanisms. Motivated by this featurebased mapping mechanism, this paper proposes a causal mapping framework based on coordinate representations.

Consider a general scenario in which we have $J$ random non-Euclidean complex data variables $X_{j} \in \mathcal{H}_{j}$, where $\mathcal{H}_{j}$ represents the complete inner product space in which $X_{j}$ is located. Each variable can belong to any type of nonEuclidean data. In the complete inner product space $\mathcal{H}_{j}$, we can linearly represent the random complex data $X_{j}$ as $X_{j}=\Omega_{j}^{\prime} \cdot \mathcal{U}_{j}$, where $\mathcal{U}_{j} \in \mathbb{R}^{p_{j}}$ denotes the representation coefficient of $X_{j}$ in the direction of $\Omega_{j}$. To handle any type of non-Euclidean data, it is feasible to find a subspace within the original space and consider the mutually orthogonal basis functions in this subspace as the coordinate axes. Through algebraic deduction, we can derive the projection coefficients of the original data along each axis. This approach avoids high computational complexity resulting from the excessively large original space. Subsequently, utilizing these numerical coefficients, we can effectively characterize the

original non-Euclidean space and apply classical statistical analysis methods. If the selected transformation is orthogonal and preserves the mathematical properties and geometric characteristics before and after the transformation, the statistical analysis conclusions obtained in the transformed sample space can accurately represent the characteristics of the original variable space.

After expressing the coefficient using appropriate basis functions for the explanatory and response variables separately, the mapping process can be defined as follows:

Definition 1 For two different types of non-Euclidean complex data, define the parent node $X_{\mathrm{Pa}_{j}} \in \mathcal{H}_{1}$ and the child node $X_{j} \in \mathcal{H}_{2}$, assuming there exist sets of orthogonal basis vectors $\Omega^{(1)}=\left(\Omega_{1}^{(1)}, \Omega_{2}^{(1)}, \ldots, \Omega_{M}^{(1)}\right)^{\prime}$ and $\Omega^{(2)}=$ $\left(\Omega_{1}^{(2)}, \Omega_{2}^{(2)}, \ldots, \Omega_{M^{\prime}}^{(2)}\right)^{\prime}$ in $\mathcal{H}_{1}$ and $\mathcal{H}_{2}$, respectively, the original non-Euclidean data can be expressed linearly as

$$
\begin{aligned}
X_{\mathrm{Pa}_{j}} & =\sum_{m=1}^{M} \mathcal{U}_{m}^{(1)} \cdot \Omega_{m}^{(1)} \\
X_{j} & =\sum_{m=1}^{M^{\prime}} \mathcal{U}_{m}^{(2)} \cdot \Omega_{m}^{(2)}
\end{aligned}
$$

Then, a mapping mechanism based on coordinate representation can be defined in the Euclidean space:
$<X_{j}, \Omega^{(2)}>_{\mathcal{H}_{2}}=\mathbf{g}\left(<X_{\mathrm{Pa}_{j}}, \Omega^{(1)}>_{\mathcal{H}_{1}}, n_{j}\right)$,
where $n_{j}$ represents the noise variable, $<\cdot, \cdot>_{\mathcal{H}_{j}}$ represents the inner product in the corresponding space, and $\mathbf{g}(\cdot)$ represents the functional form assumption of the causal function model.

To effectively describe the causal relationships within non-Euclidean data as a whole, Definition 2 introduces a comprehensive causal mapping mechanism for heterogeneous non-Euclidean data. The mechanism begins with identifying a set of orthogonal basis vectors aligned with the parent node data, which yields numerical representation coefficients. These coefficients are then employed alongside an appropriate causal mapping function $\mathbf{g}(\cdot)$ to compute the representation coefficients of the child node's multivariate coefficient vector. Finally, a reverse mapping process utilizing coordinate representation enables the estimation of the specific data values for the child node.

Definition 2 Causal mapping mechanism based on coordinate representation:

Parent node $X_{\mathrm{Pa}_{j}} \in \mathcal{H}_{1} \rightarrow$ Representation coefficients $\mathcal{U}^{(1)}$,
Representation coefficients $\mathcal{U}^{(2)}=\mathbf{g}\left(\mathcal{U}^{(1)}, n_{j}, \theta_{j}\right)$,
Representation coefficients $\mathcal{U}^{(2)} \rightarrow$ Child node $X_{j} \in \mathcal{H}_{2}$.

## Method

In this section, under the framework of the MH-NECM causal model, we propose a causal network structure learning method based on heterogeneous non-Euclidean data for the purpose of fault detection and diagnosis of industrial systems. The proposed method can discover and learn causal relationships between faults and symptoms using a novel two-stage heuristic search approach. It offers superior interpretability and reliability compared to conventional data-driven methods, which typically focus on uncovering statistical correlations between faults and symptoms rather than discerning their causal relationships.

An overview of the framework is illustrated in Fig. 1. The method is composed of two parts, causal discovery and causal infererence. First, a causal discovery approach based on canonical feature extraction and heuristic greedy hill-climbing search is presented for discovering symptoms which a fault affects dramatically. Second, a backward structural causal model-based causal inference approach is further developed to learn a reasoning model related to faults and their significant symptoms. A backward structural causal model is intrinsically based on the interpretable causal graph from the previous step, from which reasoning functions based on causal treatment effect estimation reveal the root causes of symptoms to every fault.

To further illustrate the implementation procedures of our proposed algorithm, we take the industrial fault diagnosis example in Sect. "Real-world data analysis" to show how the method is used in practice. The hydraulic test bench data set contains continuous time series measurements such as the pressure, flow rate and temperature, etc. The measurement curves can be viewed as realizations of an infinite-dimensional functional process. On the other hand, cooler condition, valve condition or internal pump leakage provide the relative proportions of the hydraulic device under different states which can be naturally viewed as compositional data. Assume that non-Euclidean data not only have causal relationships in data elements, but may also have some causal relationships in separable features due to their complex structure (e.g., base information of functional data). As shown in Fig. 1, the parent variables are mapped to their own feature domain through a CCA-guided feature extraction process from $X_{\mathrm{Pa}_{j}}$ to $\mathcal{U}$. Then, the causal discovery method is effectively carried out using $\mathcal{U}$ in the Euclidean space. Finally, from the constructed causal network, the system faults can be effectively traced back to the respective origins.

![img-0.jpeg](img-0.jpeg)

**Fig. 1** A schematic diagram showing the mapping process from the original non-Euclidean data space to its equivalent Euclidean space using CCA, and applying the causal mapping to derive the child nodes

### Causal network skeleton learning

In the skeleton learning stage, first, we need to provide a measure of the correlation between any two non-Euclidean variables. Second, this measure is used to search for the corresponding skeleton structure.

### Regularized generalized canonical correlation analysis

From the analysis in the previous section, it is evident that different types of non-Euclidean data exhibit diverse distributions and inherent geometric structures. The distances between variables do not satisfy the properties of Euclidean space, rendering the classic inner product definition inapplicable. Therefore, it is necessary to propose a generalized dependence measure capable of effectively handling complex and high-dimensional non-Euclidean data. Tenenhaus and Tenenhaus (2017) [33] introduced a theoretical framework known as Regularized General Canonical Correlation Analysis (RGCCA). This framework aims to maximize the sum of correlation measures between pairwise variables by projecting a series of non-Euclidean data with diverse and complex features onto a shared subspace of numerical variables. Through the computation of correlations, this method achieves comprehensive dimensionality reduction and the feature extraction of variables with complex structures.

For *J* random complex variables *X<sub>j</sub>* ∈ *H<sub>j</sub>*(*j* = 1, 2, · · · , *J*), where *X<sub>j</sub>* belongs to a complete inner product space *H<sub>j</sub>*. Let's assume *A<sub>j</sub>* represents the projection weights in the corresponding space. We need to solve the following optimization problem:

$$
\underset{\mathcal{A}_1, \mathcal{A}_2, \ldots, \mathcal{A}_J}{\text{maximize}} \sum_{j=1}^{J} \sum_{k=1}^{J} c_{jk} g(\operatorname{Cov}((\mathcal{A}_j, X_j)_{\mathcal{H}_j}), (\mathcal{A}_k, X_k)_{\mathcal{H}_k}).
$$

s.t. $\tau_j \parallel \mathcal{A}_j \parallel_{\mathcal{H}_j}^2$

$$
+(1 - \tau_j) \operatorname{Var}((\mathcal{A}_j, X_j)_{\mathcal{H}_j}) = 1, (j = 1, 2, \ldots, J). \tag{3}
$$

In the above equation, each variable can be any type of non-Euclidean data. The symbol $(\cdot, \cdot)_{\mathcal{H}_j}$ represents the inner product operation in the complete inner product space *H<sub>j</sub>*. The symbol $\|\cdot\|$ denotes the norm in the corresponding space. The function *g(·)* represents a generalized measure of correlation, and the parameter *c<sub>jk</sub>* (*k* = 1, 2, · · · , *J*) represents prior knowledge of the existence of a relationship between the *k*-th group of vectors and the *j*-th group of vectors. The projection weights *A<sub>j</sub>* can project *X<sub>j</sub>* from *H<sub>j</sub>* to a subspace, enabling the representation of the characteristics of the original non-Euclidean data using a set of finite-dimensional numerical vectors in Euclidean space, making numerical calculations feasible. Once the projection weights are obtained, the dependency between two variables can be calculated using the function *g(·)* in Eq. (3).

Suppose *U<sub>j</sub>*, *a<sub>j</sub>* ∈ ℝ<sup>p<sub>j</sub></sup> represents the representation coefficients of *X<sub>j</sub>* and *A<sub>j</sub>* in Ω<sub>j</sub>, which **W<sub>j</sub>** ∈ ℝ<sup>p<sub>j</sub> × p<sub>j</sub></sup> is the measurement matrix of Ω<sub>j</sub>. Then, the optimization problem in Eq. (3) can be reformulated as:

$$
\underset{a_{1}, a_{2}, \ldots, a_J}{\text{maximize}} \sum_{j=1}^{J} \sum_{k=1}^{J} c_{jk} g[\operatorname{Cov}(\mathbf{a}_j' \mathbf{W}_j \mathbf{U}_j, \mathbf{a}_k' \mathbf{W}_k \mathbf{U}_k)],
$$

s.t. $\mathbf{a}_j' \mathbf{M}_j \mathbf{a}_j = 1(j = 1, 2, \ldots, J),$

where **M<sub>j</sub>** = τ<sub>j</sub> **W<sub>j</sub>** + (1 - τ<sub>j</sub>) **W<sub>j</sub>** Cov(**U<sub>j</sub>**) **W<sub>j</sub>**. Then, the projection coefficients can be solved by the following Lagrange optimization problem:

$$
\begin{aligned}
\mathcal{L}\left(\mathbf{a}_{j}, \lambda_{j} ; j= & 1,2, \ldots, J)=\sum_{j=1}^{J} \sum_{k=1}^{J} c_{j k} g\left(\mathbf{a}_{j}^{\prime} \mathbf{W}_{j} \boldsymbol{\Sigma}_{j k} \mathbf{W}_{k} \mathbf{a}_{k}\right) \\
& -\sum_{j=1}^{J} \frac{\lambda_{j}}{2}\left(\mathbf{a}_{j}^{\prime} \mathbf{M}_{j} \mathbf{a}_{j}-1\right)
\end{aligned}
$$

where $\boldsymbol{\Sigma}_{j k}=\operatorname{Cov}\left(\mathbf{U}_{j}, \mathbf{U}_{k}\right)(j, k=1,2, \ldots, J), \lambda_{j}$ is the Lagrange multiplier. Additionally, for ease of computation, we define an inner component $v_{j}$ :
$v_{j}=\sum_{k=1, k \neq j}^{J} c_{j k} \mathbf{a}_{k}^{j} \mathbf{x}_{k}$.

The equivalent form of the parameter $\mathbf{a}_{j}$ can be expressed as follows:

$$
\begin{aligned}
\mathbf{a}_{j}= & \left(\operatorname{Cov}_{\Omega_{j}}\left(X_{j}, v_{j}\right)^{\prime} \mathbf{M}_{j}^{-1} \operatorname{Cov}_{\Omega_{j}}\left(X_{j}, v_{j}\right)\right)^{-\frac{1}{2}} \\
& \times \mathbf{M}_{j}^{-1} \operatorname{Cov}_{\Omega_{j}}\left(X_{j}, v_{j}\right)
\end{aligned}
$$

where $\operatorname{Cov}_{\Omega_{j}}\left(X_{j}, v_{j}\right)$ represents the covariance between $X_{j}$ and its internal component $v_{j}$. Given an initial value $\mathbf{a}_{j}^{(\omega)}(j=1,2, \ldots, J ; \omega=0,1,2, \ldots)$, it is updated using Eq. (7) to obtain $\mathbf{a}_{j}^{(\omega+1)}$. By further updating the internal component $v_{j}$ according to Eq. (6), the iterative solving process of optimization problem (3) is completed. In Algorithm 1, we summarize the overall optimization algorithm.

```
Algorithm 1 Regularized Generalized Canonical Correlation Analysis optimization for solving the projection weights.
    Input: Complete inner product space orthogonal basis system
    \(\left\{\boldsymbol{\Omega}_{j}\right\}_{j=1}^{J}\) and coefficients of representing random complex data
    \(\left\{\mathbf{U}_{j}\right\}_{j=1}^{J}\), initial coefficients of projection weights \(\left\{\tilde{\mathbf{a}}_{j}\right\}_{j=1}^{J}\), connec-
    tion parameters \(\left\{c_{j k}\right\}_{j, k=1}^{J}\), correlation measure \(g\); shrinkage parameter
    \(\left\{\tau_{j}\right\}_{j=1}^{J}\), convergence threshold \(\varepsilon_{0}\), iteration limit \(\omega_{\max } \).
    Output: The optimal solution for projection weights \(\mathcal{A}_{j}(j=\)
    \(1,2, \ldots, J)\).
    1: Calculate \(\mathbf{M}_{j}\) and standardize the initial values of the coefficients
        \(\mathbf{a}_{j}^{(\theta)}(j=1,2, \ldots, J): \mathbf{M}_{j}=\tau_{j} \mathbf{W}_{j}+\left(1-\tau_{j}\right) \mathbf{W}_{j} \boldsymbol{\Sigma}_{j j} \mathbf{W}_{j} ; \mathbf{a}_{j}^{(\theta)}=\)
        \(\left[\tilde{\mathbf{a}}_{j}^{\prime} \mathbf{M}_{j}^{-1} \tilde{\mathbf{a}}_{j}\right]^{-\frac{1}{2}} \mathbf{M}_{j}^{-1} \tilde{\mathbf{a}}_{j}\).
    Let \(\omega=0\) and repeat the following steps:
    3: for \(j=1,2, \ldots, J\) do
        Calculate the inner components \(v_{j}^{(\omega)}\) using Equation (6).
        Update the expression coefficients \(\mathbf{a}_{j}^{(\omega+1)}\) using Equation (7).
    end for
    7: Let \(\omega=\omega+1\),
    8: Carry out iterations until the change in the values of \(\mathbf{a}_{j}^{(\omega)}\) between
        two iterations is smaller than a certain threshold \(\varepsilon_{0}\) or the iteration
        limit \(\omega_{\max }\) is exceeded.
    9: Return \(\mathcal{A}_{j}=\Omega_{j}^{\prime} \mathbf{a}_{j}^{(\omega)}(j=1,2, \ldots, J)\).
```

After obtaining the projection weights $\mathcal{A}_{j}(j=1,2, \ldots, J)$, assuming this paper adopts the Horst type unit function listed by Tenenhaus and Tenenhaus [33]: $g(t)=t$, the correlation measure between two heterogeneous non-Euclidean data variables can be defined as follows:

Definition 3 Given arbitrary non-Euclidean data $X_{1}$ and $X_{2}$ of two different types, along with their linear representation coefficients $\mathcal{U}_{1}$ and $\mathcal{U}_{2}$ in their respective complete inner product spaces $\mathcal{H}_{1}$ and $\mathcal{H}_{2}$. By using Algorithm 1, the optimal projection weights $\mathcal{A}_{1}$ and $\mathcal{A}_{2}$ can be determined. Therefore, the measure of dependency between the two variables can be expressed by the following equation:
$\operatorname{Cov}\left(\mathbf{a}_{1}^{\prime} \mathbf{W}_{1} \mathbf{U}_{1}, \mathbf{a}_{2}^{\prime} \mathbf{W}_{2} \mathbf{U}_{2}\right)$,
where $\mathbf{W}_{j} \in \mathbb{R}^{p_{j} \times p_{j}}$ is the metric measurement matrix of the corresponding basis function system $\boldsymbol{\Omega}_{j}$.

## Skeleton search

To identify the causal network skeleton, it is essential to determine the existence of edges between two variables based on the strength of their correlation. This paper proposes a method for establishing a correspondence between the level of correlation and the presence of edges, utilizing the correlation measure defined in Definition 3.

Definition 4 In the causal network, there exists an undirected edge between any two types of non-Euclidean data, $X_{1}$ and $X_{2}$, with a threshold $K_{\alpha}$ if and only if the following relationship holds:
$\operatorname{Cov}\left(\mathbf{a}_{1}^{\prime} \mathbf{W}_{1} \mathbf{U}_{1}, \mathbf{a}_{2}^{\prime} \mathbf{W}_{2} \mathbf{U}_{2}\right)>K_{\alpha}$.
According to the edge existence rule defined in Definition 4, Algorithm 2 presents a method for learning the causal network skeleton $\mathcal{G}^{*}$. Given $J$ non-Euclidean data variables $X_{j}$ and a threshold $K_{\alpha}$, the causal network skeleton is determined using canonical correlation analysis techniques based on the coordinate representation rules in the corresponding algebraic space. The correlation measure value is then used to establish the causal network skeleton.

## Scoring function

Firstly, in the newly defined functional causal model given by Eq. (1), we need to obtain the maximum likelihood estimate $\hat{\theta}^{\text {mle }}$ of the parameters under specific model assumptions. This can be achieved by solving the following optimization objective function based on minimizing the least squares:

Algorithm 2 Causal network skeleton search.
Input: $J$ random and complex data variables $X_{j} \in \mathcal{H}_{j}(j=$ $1,2, \ldots, J)$ and threshold $K_{\alpha}$.
Output: The causal network skeleton $\mathcal{G}^{u}$.
1: for $j=1,2, \ldots, J$ do
2: According to Algorithm 1, obtain the projection weights $\mathcal{A}_{j}(j=$ $1,2, \ldots, J)$ in canonical correlation analysis.
3: Calculate the equivalent Euclidean space representation $\mathbf{a}^{\prime} \mathbf{W U}$ in Definition 4.
4: end for;
5: for $j=1,2, \ldots, J-1$ do
6: for $j^{\prime}=j+1, \ldots, J$ do
7: The correlation measure $C o v$ can be computed using equation (8).
8: $\quad$ If $C o v>K_{\alpha}$, then set the $(i, j)$ position of the connectivity matrix $\mathcal{G}^{u}$ in the skeleton network to 1 .
9: end for;
10: end for;
11: Return $\mathcal{G}^{u}$.
$\hat{\theta}_{j}^{\text {mle }}=\arg \min _{0} \operatorname{LSF}\left(U_{j}, \operatorname{Pa}\left(U_{j}\right), \theta_{j}\right) j=1,2, \ldots, J$.

Here, $\operatorname{LSF}(\cdot)$ represents the least squares fitting between the resulting variable $U_{j}$ and the causal variable $\mathrm{Pa}\left(U_{j}\right)$ under the assumption of a linear model. Within the maximum likelihood framework, we can solve for the maximum likelihood estimate (MLE) $\hat{\theta}_{j}^{\text {mle }}$ of the parameter vector. The goodness of fit for the overall data can then be evaluated using the residual sum of squares (RSS), and the evaluation function is defined as follows:
$\operatorname{NLL}\left(U_{j}, \operatorname{Pa}\left(U_{j}\right), \hat{\theta}_{j}^{\text {mle }}\right)=\sum_{i=1}^{n}\left(U_{i j}-\hat{\theta}_{j}^{\text {mle }} \operatorname{Pa}\left(U_{i j}\right)\right)^{2}$,
where $U_{i j}$ represents the coefficients of variable $j$ in sample $i, \operatorname{Pa}\left(U_{i j}\right)$ represents the expression coefficients of variable $j$ 's parent node in sample $i$, and $\hat{\theta}_{j}^{\text {mle }}$ is obtained through Eq. (10). Based on Eq. (11), the score function can be defined using the principle of Minimum Description Length (MDL) as follows:
$M D L(G)=\sum_{j=1}^{J}\left(\operatorname{NLL}\left(U_{j}, \operatorname{Pa}\left(U_{j}\right), \hat{\theta}_{j}^{\text {mle }}\right)+\frac{\left|\operatorname{Pa}\left(U_{j}\right)\right|}{2} \log n\right)$,
where $\frac{\left|\operatorname{Pa}\left(U_{j}\right)\right|}{2} \log n$ represents the penalty term for the complexity of the network, $\left|\operatorname{Pa}\left(U_{j}\right)\right|$ denotes the number of parent nodes, and $n$ is the number of samples in the dataset. The MDL score effectively balances the complexity of the model and the degree of fit to the data, enabling the selection of the most appropriate model that closely matches the observed data.

## Greedy hill-climbing search strategy

Once the scoring function is determined, the structural learning problem of a DAG transforms into a search problem. A greedy hill-climbing search strategy is employed to explore the pruned subspace of the causal network structure by performing a series of operations, such as adding edges, deleting edges, or reversing the direction of edges. Initially, starting from $\mathcal{G}^{u}$, a greedy search is performed while ensuring no cycles exist in the network. Each operation-adding edges, deleting edges, or reversing the direction of edges-is tested sequentially, and the reduction in the $\operatorname{MDL}\left(\mathcal{G}^{u}\right)$ score is recorded. The operation resulting in the largest decrease in the MDL score is selected. After several rounds of local optimization, the search process returns to the initial state and redefines the starting search space. These operations are repeated until the maximum number of search iterations is reached. Ultimately, this process returns a network topology with the globally optimal MDL score.

## Algorithm and implementation

In this proposed algorithm, we first learn a sparse skeleton among variables using the regularized generalized canonical correlation method proposed in Sect. "Regularized generalized canonical correlation analysis" equipped with the covariance thresholding method, and then project this skeleton using a proposed MDL scoring function onto a reduced search space. Next, the final directed network is estimated using a heuristic greedy search algorithm over the feasible space. We develop a novel scoring function optimizer to estimated the MDL score during the search. Assume the number of non-Euclidean variables is $J$, the number of iterations for calculating the canonical correlation projection weights is $\omega^{*}$, in calculating the canonical correlations, the complexity of the algorithm is $O\left(\omega^{*} J^{2}\right)$; Furthermore, in the covariance thresholding stage, the complexity is $O\left(J^{2}\right)$. In the second heuristic search stage, the algorithm typically converges within a reasonable number of iterations. However, most local search algorithms, including the proposed algorithm, check their neighboring solutions around a current solution to improve the score function value. These algorithms can be stuck in suboptimal solutions or saddle points, and the leaving edges often become reselected as an entering edge in the immediately succeeding iterations. Therefore, it is rather difficult to give an exact complexity upper bound for this algorithm. Assume the maximal degree for the undirected network derived from the previous stage is $D$, taking into consideration the possibility of revisiting some edges, the complexity of this component is $O\left(J D^{2}\right)$. Overall, the complexity of the whole algorithm is $O\left(\omega^{*} J^{2}+J D^{2}\right)$.

## Numerical experiments

In this section, we used the MH-NECM model to generate non-Euclidean data and applied a causal network structure learning approach based on generalized canonical correlation analysis to perform DAG structure search. We validated the superiority of the proposed method across multiple scenarios.

## Experimental setup

The method proposed in this paper for learning causal structures of non-Euclidean data demonstrates versatility in handling mixed data types. For the non-Euclidean data, two data types are selected for this numerical experiment: functional data and compositional data.

Functional data analysis (FDA) is a popular statistical tool that assumes measurement vectors are realizations of functions defined on some continuous domains. Examples of functional data include the daily closing prices of a stock, the data that make up a time series are the individual points which are considered to be random draws from an underlying stochastic process. On the other hand, compositional data are nonnegative data carrying relative, rather than absolute information-these are often data with a constant-sum constraint on the sample values, for example, proportions or percentages summing to $1 \%$ or $100 \%$, respectively. Compositional data are observed in many fields, such as geochemistry (e.g., mineral compositions), biochemistry (e.g., fatty acid proportions), finance (e.g., portfolio weights), political science (e.g., voting proportions), and marketing (e.g., brand shares).

Acquiring real datasets that contain mixed-type variables and ground truth causal Directed Acyclic Graph (DAG) structures poses a significant challenge. To overcome this obstacle, we leverage a benchmark simulator within the Tetrad framework to generate six datasets. These datasets are based on DAGs with varying numbers of nodes $(\mathrm{n}=50,100)$ and average node degrees $(3,10,20)$. It is important to note that as the node degree (the number of edges connected to each node) increases, the graph becomes denser. Each dataset comprises $100 \times n$ samples, with an equal distribution of $50 \%$ for each data type.

For functional root nodes, the data generated for the root nodes are assumed to follow a Gaussian process with a covariance function $\Sigma_{1}\left(t, t^{\prime}\right)=e^{-10\left(t-t^{\prime}\right)^{2}}$. In the case of compositional root nodes, we adopt the generation method proposed by Wang et al. [34]. It is assumed that each compositional variable is governed by a non-spherical Dirichlet distribution, obtained through the closure operation of a $D$ dimensional vector $Z_{d}$, where $d=1,2, \ldots, D$, following a gamma distribution. The marginal probability density func-
tion is determined by a gamma distribution with a shape parameter $\alpha_{d}>0$ and a scale parameter $v>0$.

$$
\begin{aligned}
f\left(z_{d} \mid \alpha_{d}, v\right)= & \frac{v^{\alpha_{d}}}{\Gamma\left(\alpha_{d}\right)} z_{d}{ }^{\alpha_{d}-1} \exp \left(-v z_{d}\right) \\
& \cdot I\left(z_{d}>0\right), d=1,2, \ldots, D
\end{aligned}
$$

Then, the compositional vectors can be obtained by $\mathbf{x}=$ $\left(x_{1}, \ldots, x_{D}\right)^{\prime}$, where $x_{d}=Z_{d} / \sum_{k} Z_{k}, d=1,2, \ldots, D$.

For all non-root nodes in the given network structure, if $X_{k}$ has a functional parent node $j \in \mathrm{~Pa}_{k}^{(f)}$. In this case, a Gaussian process with coefficient given by $\beta_{k j}(s, t)=$ $\sum_{l=1}^{3} \gamma_{l k j}(t) \phi_{l k j}(s), l=1,2,3$, is used to model the relationship. On the other hand, if $X_{k}$ is generated by its compositional parent nodes $j \in \mathrm{~Pa}_{k}^{c}$. Then, the original compositional vector $X_{j} \in \mathbb{S}^{D}$ is transformed using isometric log-ratio transformation, resulting in the equivalent representation $X_{j}=\operatorname{ilr}\left(X_{j}\right) \in \mathbb{R}^{D-1}$. The coefficient matrix $B \in \mathbb{R}^{K \times(D-1)}$ will be used to describe this relationship. The data generation processes differ for different types of child nodes, respectively.
(1) If a child node is of the functional type:

$$
\begin{aligned}
x_{k}(t)= & \sum_{j \in \mathrm{pa}_{k}} \int_{0}^{1} x_{j}^{(f)}(s) \theta_{j}^{\top}(s) B_{j k} \theta_{k}(t) \mathrm{d} s \\
& +\sum_{j \in \mathrm{Pa}_{k}} \mathbf{x}_{j}^{*(c)} \boldsymbol{\gamma}_{j}^{* \prime}+\sigma_{k} \varepsilon_{k}(t)
\end{aligned}
$$

where $B_{j k} \in \mathbb{R}^{P_{j} \times P_{k}}, \theta_{k}:=\left[\theta_{k}\left(t_{1}\right), \ldots, \theta_{k}\left(t_{n k}\right)\right] \in$ $\mathbb{R}^{P_{k} \times m_{k}}, \boldsymbol{\gamma}_{j}^{*} \in \mathbb{R}^{m_{k} \times m_{j}}$ and $\varepsilon_{k}(t) \in \mathbb{R}^{N \times m_{k}}$.
(2) If a child node is of compositional data type:

$$
\begin{aligned}
x_{k}^{*}= & \sum_{j \in \mathrm{pa}_{k}} \int_{0}^{1} x_{j}^{(f)}(s) \theta_{j}^{\top}(s) B_{j k}^{*} \mathrm{~d} s \\
& +\sum_{j \in \mathrm{~Pa}_{k}} \mathbf{x}_{j}^{*(c)} \boldsymbol{\gamma}_{j}^{* \prime}+\sigma_{k} \varepsilon_{k}
\end{aligned}
$$

where $B_{j k}^{*} \in \mathbb{R}^{P_{j} \times m_{k}}, \boldsymbol{\gamma}_{j}^{*} \in \mathbb{R}^{m_{k} \times m_{j}}$ and $\varepsilon_{k} \in \mathbb{R}^{N \times m_{k}}$.
The evaluation metrics used in this paper include Precision, Recall, F1 Score and Structural hamming distance (SHD). Precision is the ratio between true positives versus all positives, while recall is the measure of how accurate the model is in identifying true positives. The F1 score is a weighted average of the precision and recall, SHD refers to the number of changes that must be made to an estimated causal graph to recreate the ground truth graph. These metrics are widely used in causal discovery research as performance evaluation indicators for detecting the correct edges [8].

Table 1 Simulated results of multiple methods under 500 repetitions of experiments


- $\quad$ True Positive

True Positive + False Positive,

- $\quad$ True Positive

True Positive + False Negative,

- $F_{1}=2 \cdot \frac{\text { Precision } \cdot \text { Recall }}{\text { Precision }+ \text { Recall }}$


## Experimental results

This section primarily focuses on testing the proposed method from two perspectives. Firstly, under the experimental settings described in Sect. "Experimental setup", we compare the proposed method with classical causal network structure learning methods mentioned in the literature. Secondly, we validate the superiority of the proposed nonEuclidean data representation method in terms of algorithm efficiency and data approximation error.

## Accuracy of structure learning

For the collection involving both functional and compositional data, assuming that all data has been uniformly processed through discretization, we compare the causal network structure learning method proposed in Sect. "Method" with the classical PC-Stable [35], Functional Graphical Model (FGM) [36], and PenPC [37] algorithms. The FGM proposed by Qiao et al. [36] presents an undirected graphical model representing the conditional dependency among $p$ functional variables. In the numerical simulation experiment, we will compare and analyze the FGM with the skeleton corresponding to the true network structure. As for the PCStable and PenPC, which are constraint-based methods, they can only obtain the Markov equivalence class of the DAGs.

Hence, in the experiment, we will analyze the results using the Markov equivalence class corresponding to all networks.

Table 1 shows the results of all methods under the experimental settings provided in Sect. "Experimental setup". The experimental results reveal that the causal relationship identification method proposed in this paper, grounded in generalized canonical correlation analysis, achieves superior numerical simulation results compared to the FGM, PCStable, and PenPC algorithms. Higher F1 score and lower SHD indicate better performance. We can observe that our proposed model outperforms the other methods in most datasets. When the graph is dense, the maximal number of parents of a node can be as large as 10 , making the number of conditional independence tests very large and hard to estimate for all constraint-based methods. Our proposed method by nature is a hybrid method which to some extent alleviates the compounded errors from the statistical tests. Comparing the performance of our proposed method and the PenPC algorithm, the core difference lies in the second stage of the greedy search algorithm, where our proposed scoring function and heuristic search method have shown better accuracies under most simulation settings.

## Ablation study

Concerning the method proposed in this paper, the canonical correlation analysis utilized in Sect. "Regularized generalized canonical correlation analysis" establishes the projection direction of different non-Euclidean data based on the maximization of the summed correlation. Moreover, it defines the causal generative mechanism and mixed structural learning algorithm within this shared subspace. In this subsection, we evaluate the incremental contribution of the main components of this algorithm. Firstly, given two types of non-Euclidean data present in this data set, we leave out the

Table 2 Simulated results of multiple methods under 500 repetitions of experiments


canonical correlation analysis and effectively transform each variable into its equivalent Euclidean space representation without considering the canonical correlations across variables. Secondly, with regards to the greedy heuristic search algorithm, it is replaced with the edge pruning algorithm in PenPC. The results are shown in Table 2. For comparison purposes, the results for the complete proposed algorithm and the PenPC algorithm are also shown.

The experimental results indicate that the dependency measure based on canonical correlation analysis can improve the accuracy of causal network structure learning. However, the greedy search method employed in the second stage has shown a much larger performance contribution, as the performance shown on the third line without the greedy search algorithm effectively reduces the accuracy by a large margin compared to the previous two cases.

## Prediction error

In order to assess the parameter estimation performance of the proposed causal structure learning algorithm, in this section, using the same causal network structures described in the previous section, we generate a dataset consisting of $n=100$ samples and randomly divide it into an 80 -sample training set and a 20 -sample test set. For each non-root node, we calculate the mean squared prediction error (MSPE) at that node on the test set:
$M S P E_{\text {test }}=\frac{1}{n_{\text {test }}} \sum_{i=1}^{n_{\text {test }}}\left(x_{i}-\hat{x}_{i}\right)^{2}$.
Furthermore, we calculate the average of MSPE across all nodes as a measure of overall prediction accuracy:

Table 3 Calculate the average and standard deviation of MSPE across all nodes for different numbers of nodes $(p)$, network densities $(d)$, and signal-to-noise ratios (snr) using the PenPC algorithm and the proposed method


$$
\operatorname{MSPE}=\frac{1}{J} \sum_{j=1}^{J} \operatorname{MSPE}_{j}
$$

We conducted 500 repetitions of the experiment where we varied the experimental parameters $p$ (number of nodes), $d$ (network densities), and snr (signal-to-noise ratios), and calculated the average MSPE (mean squared prediction error) and its corresponding standard deviation for both the PenPC algorithm and the proposed method, as shown in Table 3. The results reveal that the signal-to-noise ratio has a significant impact on the accuracy of the network structure learning models, especially in scenarios where the number of nodes is large and the network density is high. In such cases, both methods experience a decrease in prediction accuracy. Furthermore, when comparing the proposed method to the benchmark PenPC algorithm under the same experimental settings, our method consistently achieves higher prediction accuracy.

Table 4 Statistics of each benchmark network structure


## Application on real-world data

We also generate mixed-type synthetic data based on some benchmark network structures in causal discovery (https://www.bnlearn.com/bnrepository/), which are summarized in Table 4.

The source variables are defined as the ones without parents and the remaining ones are non-source variables. A functional non-source variable $X_{j}$ is generated following Eq. (14) and a compositional non-source variable $X_{j}$ is generated following Eq. (15). Note that the data types are not limited to the two types above, for any data types, provided with a transformation from its original non-Euclidean space to the Euclidean space, we can apply a similar procedure to that specific data type. For each network, we simulate the mixedtype data sets with:

- Percentages of functional and compositional variables are $50 \%$, respectively.
- Various noise distributions: Normal, Uniform and Exponential.
- Various functional causal mechanisms: (1) linear function; (2) "modified-sigmoid" function, i.e., a weighted combination of $\frac{b(x+a)}{1+|b(x+a)|}$, where $a$ and $b$ are randomly chosen coefficients.

In summary, we generate 6 mixed-type data sets for each network. In Fig. 2, we present the averaged F1-score and normalized structural hamming distance to evaluate the performance of each causal discovery method. Higher F1 score and lower N-SHD indicate better performance. We can thus observe that our proposed model outperforms the other methods. Note that, the functional graphical model does not provide the full directed network and hence the SHD is significantly higher than the other methods.

## Real-world data analysis

In the real world, data is collected from various complex sources, often requiring the handling of mixed complex data that includes different types. In addition to the commonly encountered numerical and categorical data, industrial man-
![img-1.jpeg](img-1.jpeg)
(a) F1 score for various benchmark datasets.
![img-2.jpeg](img-2.jpeg)
(b) N-SHD for various benchmark datasets.

Fig. 2 The model performance w.r.t. F1-score and N-SHD on synthetic data sets
ufacturing processes often involve diverse types of complex data. For example, functional data can be used to represent observed values of physical variables measured by industrial sensors, while compositional data variables can represent the relative proportions of a specific industrial component under different operating conditions.

In reliability modeling, causal Bayesian networks can be used to learn the causal relationships between different intermediate variables and performance indicators, taking into account the reliability of the various components and their interactions. These networks are useful for assisting industrial process control, fault tracing, and other tasks. In reality, industrial systems have interdependent nodes, making it difficult to obtain clear modeling results through classical correlation analysis. Therefore, refining correlation analysis into causal relationships can provide detailed feedback on the internal relationships within the system, guiding subsequent in-depth modeling work. In this section, we will combine an understanding of the physical process data of hydraulic devices and employ causal relationship mining techniques to identify

Table 5 Categorical variables and their components


![img-3.jpeg](img-3.jpeg)

Fig. 3 Industrial System Process Diagram
features that have strong causal relationships, greatly enhancing the interpretability of fault detection results (Table 5).

Two assumptions are made in this study. First, we assume that the functional data follows a joint multivariate Gaussian distribution, which is commonly used in the traditional literature on probability graphical models (Qiao et al., 2019) [36]. Additionally, we assume that the compositional data is defined on a simplex space, denoted as $\mathcal{S}^{D}$. Secondly, in order to ensure that the learned graph structure is acyclic, we assume the existence of a variable ordering, known as a topological ordering, where only variables that appear earlier in the ordering can be parents of variables that appear later. This kind of topological ordering between variables is also commonly observed in industrial production. For example, in a production line operation, upstream process variables can influence downstream process variables, but not vice versa. In the operation of an internal combustion engine, for instance, the vehicle speed depends on the position of the accelerator pedal and the gear ratio. Therefore, in this model, the causal ordering of the latter two variables is lower than the vehicle speed. Drawing on domain knowledge, we can establish the topological structure's ordering. Based on this, we define the potential set of parent nodes for each node and ensure that the learned probability graphical model is a Directed Acyclic Graph (DAG).

The data utilized in this chapter is obtained from Helwig et al. [38]. In a hydraulic test bench, reversible experiments are conducted to assess the performance of various components. The hydraulic system comprises a main working system (Fig. 3a) and a secondary cooling-filtration loop (Fig. 3b), interconnected through an oil tank. Within the working circuit, the main pump MP1 (with a motor power of 3.3 kW ) is employed, along with the proportional pressure relief valve V11, to facilitate cycling through different load levels. The testing of the system involves two types of working cycles: a fixed working cycle with predefined load levels, based on typical cyclic operations and repeated load characteristics in industrial applications, and a variable working cycle with

pseudo-random load variations distributed within a defined range, commonly found in mobile machinery applications. Multiple sensors installed in the testing system measure various process values such as pressure (PS1-PS6), flow rate (FS1, FS2), temperature (TS1-TS4), electrical power (EPS1), and vibration (VS1). Furthermore, three derived variables, namely cooling efficiency (CE), cooling power (CP), and system efficiency (SE), which can be calculated from the physical sensor values, are considered as virtual sensors. Hence, a total of 17 numerical variables are available in this testing system. Additionally, the authors have collected variables that describe the degradation processes of components over time, including cooler condition (CC), valve condition (VC), internal pump leakage (IPL), and hydraulic accumulator (HA). The data provides the relative proportions of the hydraulic device under different states for each of these variables. These situations encompass:

In the aforementioned variables, people often pay more attention to the relative proportions of component damage levels in the overall context. Therefore, the four variables mentioned above can be considered as compositional data.

The processed data consists of 2205 samples. Due to the inherent causal ordering of the components in the hydraulic system (as shown in Fig. 3), the proposed hybrid complex data causal Bayesian network learning method can be applied in this order. The results are presented in Fig. 4. Continuous function-based features are represented by squares labeled 1-17, while component-type variables are represented by circles labeled 18-21. From the obtained network structure, interesting patterns can be observed, allowing users to infer the connections between the physical states of different components under varying operating conditions. For example, due to the exponential relationship between temperature and viscosity, there is a causal relationship between the condition of the cooler (node 18) and the potential damage levels of multiple components. The valve condition (VC) is naturally closely related to pressure-related variables (PS1-PS6). These connections are between component-type variables and numerical variables. Additionally, it was found that variables of the same type often have closer connections, such as pressure variables with each other, as well as temperature variables with each other. Moreover, the network also includes some relatively independent variables, including EPS1, VS1, and HA.

## Discussion and conclusion

In our paper, we introduce a hybrid algorithm for learning causal structures in mixed-type non-Euclidean data, such as datasets containing both functional and compositional data types. Our approach involves a novel method based on regularized general canonical correlation for deriving unified
![img-4.jpeg](img-4.jpeg)

Fig. 4 Estimated Network Topology
latent space representations across diverse data types. Additionally, we present a heuristic greedy hill-climbing method for structure learning, utilizing the Minimum Description Length (MDL) scoring function. This method determines edge directions through iterative operations including addition, deletion, or reversal of edges.

Overall, our numerical experiments demonstrate that the proposed method surpasses three benchmark methods in terms of structure learning accuracy. Additionally, our ablation study sequentially removes the canonical correlation component and the greedy heuristic search component to assess their individual contributions. Our numerical findings indicate that the greedy DAG search plays a significantly larger role in the overall performance improvement. This is because the benchmark methods rely on conditional independence tests as an edge pruning mechanism to eliminate non-causal edges from the skeletons initially. However, this process relies on parametric functional assumptions and conditional independence testing thresholds, making it susceptible to significant drops in learning accuracy with even slight parameter variations. Moreover, the feature extraction method based on canonical correlations offers an efficient representation of mixed data types, thereby enhancing the skeleton search stage by facilitating correlation calculations between different variables.

The proposed method does possess several limitations and potential biases with the two-stage approach. In particular, the greedy heuristic search method relies on the discovered skeleton to restrict the search space to a smaller subset, therefore, if the result of the first stage is inaccurate, the error is likely to propagate to the next stage and the greedy heuris-

tic algorithm will likely converge to an incorrect solution. In terms of future research directions, there is more to learn in the non-Euclidean causal discovery, for example, it is possible to extend our model to dynamic settings with regime shifts.

Acknowledgements This work was supported by the Youth Project of MOE (Ministry of Education Foundation on Humanities and Social Sciences (Grant No. 23YJCZH223), the Beijing University of Posts and Telecommunications-China Mobile Research InstituteJoint Innovation Center (OMYJY-202300186), and the open research fund of the Engineering Research Center of Network Management Technology for High-Speed Railway of Ministry of Education, Beijing Jiaotong University.

Author Contributions XW: funding acquisition, investigation, formal analysis, project administration; SJ: conceptualization, data curation; XL: methodology, software, visualization and writing—original draft; MW: resources, supervision and writing-review and editing.

Funding This research was financially supported by the Youth Project of MOE (Ministry of Education) Foundation on Humanities and Social Sciences (23YJCZH223), National Natural Science Foundation of China Grant No. 72374031.

Data Availability The data used to support the findings of this study are available from the corresponding author upon request.

## Declarations

Conflict of interest The authors have no relevant financial or nonfinancial interests to disclose.

Ethical approval Not applicable.
Human participants and/or animals There are no human subjects in this article and informed consent is not applicable.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecomm ons.org/licenses/by/4.0/.
