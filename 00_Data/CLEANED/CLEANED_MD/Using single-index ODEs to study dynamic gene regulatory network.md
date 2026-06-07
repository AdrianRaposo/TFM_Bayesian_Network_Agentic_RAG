# RESEARCH ARTICLE 

## Using single-index ODEs to study dynamic gene regulatory network

Qi Zhang ${ }^{1}$, Yao Yu ${ }^{2}$, Jun Zhang ${ }^{3}$, Hua Liang ${ }^{4 *}$


#### Abstract

1 Department of Statistics, Qingdao University, Qingdao, China, 2 Department of Biostatistics and Computational Biology, University of Rochester School of Medicine and Dentistry, Rochester, New York, United States of America, 3 Institute of Statistical Sciences at Shenzhen University, Shenzhen University, Shenzhen, China, 4 Department of Statistics, George Washington University, Washington, D.C., United States of America


* hliang@gwu.edu

## Abstract

With the development of biotechnology, high-throughput studies on protein-protein, pro-tein-gene, and gene-gene interactions become possible and attract remarkable attention. To explore the interactions in dynamic gene regulatory networks, we propose a singleindex ordinary differential equation (ODE) model and develop a variable selection procedure. We employ the smoothly clipped absolute deviation penalty (SCAD) penalized function for variable selection. We analyze a yeast cell cycle gene expression data set to illustrate the usefulness of the single-index ODE model. In real data analysis, we group genes into functional modules using the smoothing spline clustering approach. We estimate state functions and their first derivatives for functional modules using penalized spline-based nonparametric mixed-effects models and the spline method. We substitute the estimates into the single-index ODE models, and then use the penalized profile leastsquares procedure to identify network structures among the models. The results indicate that our model fits the data better than linear ODE models and our variable selection procedure identifies the interactions that may be missed by linear ODE models but confirmed in biological studies. In addition, Monte Carlo simulation studies are used to evaluate and compare the methods.


## 1 Department of Statistics, Qingdao University, Qingdao, China, 2 Department of Biostatistics and Computational Biology, University of Rochester School of Medicine and Dentistry, Rochester, New York, United States of America, 3 Institute of Statistical Sciences at Shenzhen University, Shenzhen University, Shenzhen, China, 4 Department of Statistics, George Washington University, Washington, D.C., United States of America

* hliang@gwu.edu


## Abstract

With the development of biotechnology, high-throughput studies on protein-protein, pro-tein-gene, and gene-gene interactions become possible and attract remarkable attention. To explore the interactions in dynamic gene regulatory networks, we propose a singleindex ordinary differential equation (ODE) model and develop a variable selection procedure. We employ the smoothly clipped absolute deviation penalty (SCAD) penalized function for variable selection. We analyze a yeast cell cycle gene expression data set to illustrate the usefulness of the single-index ODE model. In real data analysis, we group genes into functional modules using the smoothing spline clustering approach. We estimate state functions and their first derivatives for functional modules using penalized spline-based nonparametric mixed-effects models and the spline method. We substitute the estimates into the single-index ODE models, and then use the penalized profile leastsquares procedure to identify network structures among the models. The results indicate that our model fits the data better than linear ODE models and our variable selection procedure identifies the interactions that may be missed by linear ODE models but confirmed in biological studies. In addition, Monte Carlo simulation studies are used to evaluate and compare the methods.

## Introduction

Gene regulatory networks (GRN) are complex and dynamic systems in nature. They are composed of genes that interact with each other and with other substances inside cells, such as RNAs and proteins. Over the past few decades, a variety of methods have been proposed to model GRN. Commonly used models include information theory models, Boolean networks, ordinary differential equation (ODE) models, and Bayesian networks [1]. Information theory models [2-4] construct network architecture on correlation coefficients. Such models are simple and have a low computation cost, but cannot take into account the dynamic processes and situations when multiple genes participate in regulations. Boolean networks [5-7] are discrete dynamic networks and easy to understand, but have limitations because their networks' nodes

are binary states: "off" or "on". Due to these simplifying assumptions, the study of kinetic gene regulation is still challenging because of the complexity of the biological process [8].

The Bayesian networks [9-12] integrate biological knowledge and measurements to infer network structures. But the estimated results obtained from Bayesian networks depend on the quality and completeness of prior knowledge. As pointed out by [13], the existing ODE models and associated methods used to study GRN are flexible but are limited to small scale gene expression levels. ODE models describe the dynamic behaviors of GRN in a quantitative manner and represent gene expression level changes by functions of gene expression levels:

$$
\frac{d X_{k}(t)}{d t}=F(t, \mathbf{X}(t), \boldsymbol{\theta}), k=1, \ldots, p
$$

where $\mathbf{X}(t)=\left(X_{1}(t), \cdots, X_{p}(t)\right)^{\mathrm{T}}$ represents gene expression levels at the time $t$ of the $p$ genes; $F(\cdot, \cdot, \cdot)$ is a function which can be linear or nonlinear; and $\boldsymbol{\theta}$ is an unknown parameter vector which quantifies the regulations or interactions among the genes in GRN.

Once we can determine $\mathbf{X}(t)$, the gene expression levels which should be included in the ODE model (1), we can infer the interactions within a dynamic GRN. This motivates us to use appropriate models and to develop associated techniques in order to construct dynamic GRN for time course gene expression data. Within a dynamic GRN, the majority of the genes are not significantly relevant to each other. The precision of parameter estimation, model interpretability, and the accuracy of forecasting will be reduced when irrelevant genes are included in models [14]. Thus, those irrelevant genes should be excluded from the final model. However, variable selection for ODE models using traditional statistical methods is important but challenging, especially when it comes to dynamic GRN. The difficulties arise from two aspects: one is the collinearity among genes, i.e., genes sharing same "pathway" are highly correlated in expressions; the other is the high-dimensional feature of GRN, i.e., a large-scale GRN involves hundreds or even thousands of genes. When the number ( $n$ ) of measurements for individual genes is much smaller than the number $(p)$ of genes, traditional statistical methods face significant challenges in developing statistical procedures and deriving theory [15].

Pioneering research has investigated gene regulatory networks using variable selection techniques. For example, [13] proposed linear ODE models: $d X_{k}(t) / d t=\gamma^{\mathrm{T}} \mathbf{X}(t)$ and developed a variable selection procedure based on SCAD penalty. [13] further employed their method to construct a module-based dynamic network. However a linear ODE model has many limitations and is unable to capture certain patterns. In reality, the first derivatives of the gene expression profiles (the time-related changes of a gene expression) can be quantified as a function of gene expression levels of all related genes. The link functions that quantify the regulatory effects of genes on the first derivatives may be nonlinear. In other words, systems of cellular regulations may be nonlinear [1, 16]. Due to the limitations of linear ODE models, developing a flexible modeling approach to explore the interactions among genes has become necessary. When the linear assumption cannot be satisfied, it is natural to consider a singleindex model, $E(Y \mid X)=\eta\left(X^{T} \beta\right)$ with $\eta$ being an unknown differentiable function and $\beta$ an unknown parameter to be estimated. Single-index models have many advantages, such as being able to model the curvature of a smooth curve and circumventing the so-called "curse of dimensionality". More discussions about the usefulness of single-index models are provided in [17]. A nonlinear ODE model (given the function $\eta$ ) may suffer from misspecification and "the curse of dimensionality", whereas single-index ODE models can avoid these two problems and are more flexible, and the index parameter $(\beta)$ can be estimated with the root $-n$ convergence rate though the link function is unknown. More importantly, single index ODE models allow the predictors to have interactions, which is common in characterizing gene-gene regulation.

Various methods have been proposed to estimate regression coefficients for single-index models. See [18-23] for parameter estimators. In addition, much research has been done on variable selection for single-index models. For example, [24] developed a variable selection method based on sliced inverse regression. [25] proposed a leave-m-out cross-validation method to select variables in a single-index model. [26] proposed semiparametrically efficient profile least-squares estimators for parameter estimation, and employed the SCAD approach to simultaneously select variables and estimate regression coefficients. [27] studied estimation and variable selection coupling with dimension reduction procedures.

Although parameter estimation and variable selection for single-index models have gained fruitful results, to the best of our knowledge, no method that couples single-index models with ODE to study dynamic GRN is available. In this paper, we propose a single-index ODE model to study dynamic GRN with the aim of overcoming the inadequacy of linear ODE models. This model can be written as

$$
\frac{d X_{k}(t)}{d t}=\eta_{k}\left(\mathbf{X}(t)^{\mathrm{T}} \boldsymbol{\beta}_{0}^{(k)}\right)+\varepsilon, k=1, \ldots, p
$$

where $\eta_{k}(\cdot)$ is an unknown differentiable function; $\boldsymbol{\beta}_{0}^{(k)}$ is a parameter vector with $\left\|\boldsymbol{\beta}_{0}^{(k)}\right\|=1$, and the first element of $\boldsymbol{\beta}_{0}^{(k)}$ is positive (for identifiability), where $\|\cdot\|$ denotes the Euclidean norm. $\mathbf{X}(t)=\left(x_{1}(t), \cdots, x_{\mathrm{p}}(t)\right)^{\mathrm{T}}$ are state functions. Here $\mathbf{X}(t)$ can be gene-expressing levels of genes or population mean curves for functional modules. To study the interactions within dynamic GRN, one needs to identify the relevant $\mathbf{X}(t)$ for ODE models, that is $\boldsymbol{\beta}_{0}^{(k)} \neq 0$. We therefore apply the penalized least-squares approach for this aspect and for estimating dynamic parameters $\boldsymbol{\beta}_{0}^{(k)}$.

We will apply the mixed-effects nonparametric model with a mixture distribution framework to cluster the genes into functional modules in the first step. This clustering approach allows us to build the module-based dynamic network and identify the interesting functional modules. These interesting modules may play important roles in 'dynamic' regulations. Although these interesting modules may contain many genes with heterogeneous functions, it can allow scientists to focus on the genes in each module for further investigations. As shown in Fig 1 (below), most gene expression levels can be grouped in several clusters. In each cluster, these expression levels share a similar pattern. The genes in a cluster (represented by a node) may play a common function in biological procession. Such a network can single out regula-tor-regulator interactions which are helpful to avoid tedious experiments and to speed biological studies.

In Section of Methods, we briefly describe the procedure for GRN construction with details for penalized profile least-squares (PPrLS) estimation and variable selection. In Section of Numerical Results, we construct a module-based GRN structure by using PPrLS estimator for the yeast cell cycle gene expression data with additional results (S1 and S2 Tables), and conduct Monte Carlo simulation studies to evaluate the performance of the proposed procedure. The simulation settings were designed to mimic the gene expression patterns from the real data example. In Section of Discussions, we conclude the article with a brief discussion. All theory and associated technical details are given in the supporting materials (S1-S7 Files).

# Methods 

Time-course gene expressions are synchronized to many ongoing biological processes such as tissue repair, cell differentiation, or cell cycles [28, 29]. Through understanding the genes underlying the cell cycles, we can study the mechanisms of many diseases at a molecular level and in turn provide potential drug targets for treating those diseases. From the end of the last

![img-0.jpeg](img-0.jpeg)

Fig 1. The scatterplot of gene expressions against time (the same color for each individual gene in a module) and the population mean curve (solid line) of 12 modules for the time course yeast cell data set.
https://doi.org/10.1371/journal.pone.0192833.g001
century, the identification of cell cycles associated genes has attracted considerable attention in biological study. For example, $[28,30]$ performed genome-wide transcriptional analysis of the cell cycle process of yeast using microarrays and identified about 800 cell-cycle-regulated genes. GRN include genes, the products of genes, and the interactions among them, which together affect many cellular processes. To understand the dynamic mechanism of cellular processes, modeling and analysis of dynamic gene regulatory networks using time-course gene expression data has attracted much attention. We model dynamic network for functional modules based on observed time course gene expression levels in three steps.

Step 1. Group genes into functional modules using the smoothing spline clustering (SSC) approach [31-33]. Final number of clusters was selected by the Bayesian information criterion (BIC), and penalty parameters were determined by the leave-one-out cross-validation procedure (GCV);

Step 2. Estimate state function $X(t)$ and first derivative $X^{\prime}(t)$ for each functional module using nonparametric mixed-effect models (NPME) and the spline method respectively;

Step 3. Select modules and estimate dynamic parameters using the PPrLS procedure given below, for which tuning parameter was selected by the BIC, and bandwidths were determined by the GCV.

We now describe the details for these three steps.

# Step 1-Clustering process 

We assume the time-course gene expression levels for gene $i$ can be represented by a smooth function of time and follow a mixture Gaussian distribution:

$$
g_{i}(t) \sim p_{1} N\left(\mu_{1}, \Sigma_{1}\right)+p_{2} N\left(\mu_{2}, \Sigma_{2}\right)+\cdots+p_{p} N\left(\mu_{p}, \Sigma_{p}\right)
$$

where $p_{k}, k=1, \cdots, p$ are the probability that gene $i$ belongs to cluster $k ; \mu_{k}, k=1, \cdots, p$ and $\Sigma_{k}, k=1, \cdots, p$ are the vector representations of the mean curve and variances components for each cluster respectively. The gene expression levels for individual genes are assumed to follow an overall mean curve (fixed-effect) while having a gene-specific shift (random-effect). Therefore nonparametric mixed-effect model can be constructed by fitting the time-course gene expressions for each gene to a function over time by using the smoothing spline method. Through maximizing the penalized log-likelihood, the SSC procedure estimates the probabilities $p_{k}$. The means $\mu_{k}$ and variances component $\Sigma_{k}$ can be estimated as by-products also. More details about the SSC procedure are available in [32] and [33].

## Step 2-Applications of nonparametric mixed-effect models

After grouping genes into functional modules, we apply NPME models to estimate the state function $X(t)$ and its first derivative $X^{\prime}(t)$ for each functional module. For notation simplicity, we consider the estimation of the state function and its first derivative for module $1(k=1)$ and denote them by $X(t)$ and $X^{\prime}(t)$ respectively. Suppose the number of genes in module 1 is $m$, and the number of measurements collected from each gene is $m_{i}$. The NPME model can be described as

$$
g_{i}(t=X(t)+v_{i}(t)+\varepsilon_{i}(t), i=1, \cdots, m
$$

where $g_{i}(t)$ is the observed gene expression level for the $i^{\text {th }}$ gene; $X(t)$ presents the fixed-effect or population curve which reflects an overall time-related trend of the gene expression level for module $1 ; v_{i}(t)$ describe individual curve variations; $\varepsilon_{i}(t)$ are measurement errors; and $v_{i}(t)$ and $\varepsilon_{i}(t)$ are assumed to be independent.

We can combine the penalized spline [34-36] with the linear mixed-effects (LME) modeling framework [37] to approximate $X(t)$. For presentation completeness, we briefly summarize the estimation procedure. We first approximate $\mathrm{X}(\mathrm{t})$ and $v_{i}(t)$ by $\widetilde{X}(t)$ and $\widetilde{v}_{i}(t)$, respectively, which are expressed as:

$$
\widetilde{X}(t)=\sum_{r=0}^{l} \alpha_{r} t^{r}+\sum_{r=1}^{R} u_{r}\left(t-\zeta_{r}\right)_{+}^{l}, \text { and } \widetilde{v}_{i}(t)=\sum_{r=0}^{l} b_{i r} t^{r}+\sum_{r=1}^{R} w_{i r}\left(t-\zeta_{r}\right)_{+}^{l}
$$

where $l \geq 1$ is an integer, $\zeta_{1}<\cdots<\zeta_{R}$ are fixed knots, $u_{r}\left(t-\zeta_{r}\right)_{+}=\max (0, t-\zeta_{r})$, $\boldsymbol{\alpha}=\left(\alpha_{1}, \cdots, \alpha_{l}\right), \mathbf{u}=\left(u_{1}, \cdots, u_{R}\right), \mathbf{b}_{i}=\left(b_{i 0}, \cdots, b_{i l}\right)$, and $\mathbf{w}_{i}=\left(w_{i 0}, \cdots, w_{i R}\right)$. Let

$$
S_{i}=\left(\begin{array}{cccc}
1 & t_{i 1} & \cdots & t_{i 1}^{i} \\
1 & t_{i 2} & \cdots & t_{i 2}^{i} \\
\vdots & \vdots & \ddots & \vdots \\
1 & t_{i m_{1}} & \cdots & t_{i m_{1}}^{i}
\end{array}\right), \text { and } Z_{i}=\left(\begin{array}{ccc}
\left(t_{i 1}-\zeta_{1}\right)_{+}^{i} & \cdots & \left(t_{i 1}-\zeta_{R}\right)_{+}^{i} \\
\left(t_{i 2}-\zeta_{1}\right)_{+}^{i} & \cdots & \left(t_{i 1}-\zeta_{R}\right)_{+}^{i} \\
\vdots & \ddots & \vdots \\
\left(t_{i m_{1}}-\zeta_{1}\right)_{+}^{i} & \cdots & \left(t_{i m_{1}}-\zeta_{R}\right)_{+}^{i}
\end{array}\right)
$$

The approximation of model (4) can be expressed as

$$
\mathbf{g}=\mathbf{S} \boldsymbol{\alpha}+\boldsymbol{\Lambda} \mathbf{b}+\mathbf{Z u}+\boldsymbol{\Gamma} \mathbf{w}+\boldsymbol{\varepsilon}
$$

where $\mathbf{S}=\left(S_{1}^{\mathrm{T}}, \cdots, S_{m}^{\mathrm{T}}\right)^{\mathrm{T}}, \mathbf{g}=\left(g_{1}^{\mathrm{T}}, \cdots, g_{m}^{\mathrm{T}}\right)^{\mathrm{T}}, \Lambda=\operatorname{diag}\left(S_{1}^{\mathrm{T}}, \cdots, S_{m}^{\mathrm{T}}\right), \mathbf{Z}=\left(Z_{1}^{\mathrm{T}}, \cdots, Z_{m}^{\mathrm{T}}\right)^{\mathrm{T}}$, $\boldsymbol{\Gamma}=\operatorname{diag}\left(Z_{1}^{\mathrm{T}}, \cdots, Z_{m}^{\mathrm{T}}\right), \mathbf{b}=\left(b_{1}^{\mathrm{T}}, \cdots, b_{m}^{\mathrm{T}}\right)^{\mathrm{T}}$, and $\mathbf{w}=\left(w_{1}^{\mathrm{T}}, \cdots, w_{m}^{\mathrm{T}}\right)^{\mathrm{T}}$. Model (6) is a standard LME model. As a result, $\boldsymbol{\alpha}, \mathbf{b}, \mathbf{u}$ and $\mathbf{w}$ can be estimated by using the function lme (available in the R package nlme). Substituting the estimated $\widehat{\boldsymbol{\alpha}}$ and $\widehat{\mathbf{u}}$ in Eq (5), we estimate the $X(t)$ for module 1. After estimating $\mathbf{X}(t)$, we apply the spline method (available in the R package splines) to estimate the first derivative of $\widehat{X}(t)$. The detailed estimation procedure is referred to [38] and [39].

# Step 3-Estimation procedure based on the penalized profile least-squares approach 

Suppose a genome-wide time course gene expression levels were clustered into $p$ modules; $X_{j}(t), j=1, \cdots, p$ are the population mean curves estimated by NPME models; and $\widehat{X}_{k}^{\prime}(t)$ are the estimates of the first derivative $d X_{k}(t) / d t$ for the $k$-th module. Substituting $X_{j}(t), j=1, \cdots, p$ and the first derivative $\widehat{X}_{k}^{\prime}(t)$ for the $k$-th module in model (2), we obtain a single-index ODE model for the $k$-th functional module which can be written as

$$
Y_{k}(t)=\eta_{k}\left(\mathbf{X}(t)^{\mathrm{T}} \boldsymbol{\beta}_{i i}^{[k]}\right)+\varepsilon, k=1, \cdots, p
$$

where $\eta_{k}$ is an unknown differentiable function, $Y_{k}(t)=\widehat{X}_{k}^{\prime}(t), \mathbf{X}(t)=\left(X_{1}(t), \ldots, X_{\mathrm{p}}(t)\right)^{\mathrm{T}}$, $\boldsymbol{\beta}_{i i}^{[k]}=\left(\beta_{01}^{[k]}, \cdots, \beta_{0 p}^{[k]}\right)^{\mathrm{T}}$, and $\varepsilon$ is the sum of numerical errors due to integration and estimation. This complexity $\varepsilon$ makes it challenging to study the properties of the proposed estimator for $\boldsymbol{\beta}^{\prime} s$, For simplicity, we adopt an additive error model used in the literature [13, 40, 41]. Once the $\mathbf{X}(t)$ can be identified, we construct a module-based network. Here we develop the variable (population mean of functional modules) selection and estimation procedure for model (7) based on the penalized profile least-squares approach as follows.

Selecting variables by penalized least squares has been widely studied in literature. See, for example, the least absolute shrinkage and selection operator (LASSO) [42], the smoothly clipped absolute deviation (SCAD) approach [43], the adaptive lasso estimator [44], the elas-tic-net estimator [45] and the adaptive elastic-net estimator [46]. However, the variable selection problem for single-index ODE models has not been addressed in the literature. In this paper, we extend the approach proposed by [26] to the single-index ODE model (7).

Let $p$ be the number of all modules; $X_{i}=\left(X_{1}\left(t_{i}\right), \ldots, X_{p}\left(t_{i}\right)\right)^{\mathrm{T}}, i=1, \ldots, N, Y_{i}=\widehat{X}_{k}^{\prime}\left(t_{i}\right)$ be the vector representations of the mean curves of $p$ function modules and the estimates of the first derivative $d X_{k}(t) / d t$ for the $k$-th module. Assume the functional data of the $k$ th module follows

the single-index ODE model

$$
Y_{i}=\eta_{k}\left(X_{i}^{\mathrm{T}} \boldsymbol{\beta}^{[k]}\right)+\boldsymbol{\varepsilon}_{i}, k=1, \cdots, p
$$

Let $\Lambda_{i}=X_{i}^{\mathrm{T}} \boldsymbol{\beta}^{[k]} \cdot \eta_{k}(u)$ can be estimated utilizing the local linear regression method [47], i.e., minimizing

$$
\sum_{i=1}^{N}\left\{a_{k}+b_{k}\left(\Lambda_{i}-u\right)-Y_{i}\right\}^{2} K_{h}\left(\Lambda_{i}-u\right)
$$

with respect to $a_{k}$ and $b_{k}$, where $K_{h}(\cdot)=K(\cdot / h) / h, K(\cdot)$ is a kernel function and $h$ is a bandwidth. We can then obtain

$$
\hat{\eta}_{k}(u, \boldsymbol{\beta})=\widehat{a}_{k}=\frac{K_{20}(u, \boldsymbol{\beta}) K_{01}(u, \boldsymbol{\beta})-K_{10}(u, \boldsymbol{\beta}) K_{11}(u, \boldsymbol{\beta})}{K_{00}(u, \boldsymbol{\beta}) K_{20}(u, \boldsymbol{\beta})-K_{10}^{2}(u, \boldsymbol{\beta})}
$$

where $K_{j l}(u, \boldsymbol{\beta})=\sum_{i=1}^{N} K_{h}\left(X_{i}^{\mathrm{T}} \boldsymbol{\beta}^{[k]}-u\right)\left(X_{i}^{\mathrm{T}} \boldsymbol{\beta}^{[k]}-u\right)^{l} Y_{i}^{l}$, for $j=0,1,2$ and $l=0,1,2$. Consequently, the profile least squares function can be proposed as a function of $\beta^{[k]}$

$$
\mathrm{Q}\left(\boldsymbol{\beta}^{[k]}\right)=\sum_{i=1}^{N}\left\{Y_{i}-\hat{\eta}_{k}\left(X_{i}^{\mathrm{T}} \boldsymbol{\beta}^{[k]}\right)\right\}^{2}
$$

The above estimation procedure can be used when the true model is known a priori. Because we wish to identify GRN structure and enhance the predictive power of a proposed model, we apply the penalized least-squares approach to simultaneously select modules and estimate parameters. Define a penalized profile least-squares (PPrLS) function

$$
\mathcal{L}_{p}\left(\boldsymbol{\beta}^{[k]}\right)=\frac{1}{2} Q\left(\boldsymbol{\beta}^{[k]}\right)+N \sum_{j=1}^{p} p_{\lambda^{[k]}}\left(\left|\beta_{j}^{[k]}\right|\right)
$$

where $p_{\lambda^{[k]}}(\cdot)$ is a penalty function with a regularization parameter $\lambda^{[k]}$. The PPrLS estimator of $\boldsymbol{\beta}^{[k]}$ is the minimizer of Eq (12); i.e.,

$$
\widehat{\boldsymbol{\beta}}^{[k]}=\operatorname{argmin} \mathcal{L}_{p}\left(\boldsymbol{\beta}^{[k]}\right)
$$

For a given tuning parameter $\lambda^{[k]}$, we can estimate $\boldsymbol{\beta}^{[k]}$ by minimizing $\mathcal{L}_{p}\left(\boldsymbol{\beta}^{[k]}\right)$ with respect to $\boldsymbol{\beta}^{[k]}$. By determining non-zero $\boldsymbol{\beta}^{[k]}$, we identify the modules having impacts on the $k$ th module and therefore construct GRN.

There are various penalty functions in the literature of variable selection for semiparametric models. Considering the SCAD method has many good theoretical properties, we adopt the SCAD penalty function [43], and adopt BIC selector proposed by [48] to choose the regularization parameters $\lambda^{[k]}$ by minimizing the following objective function:

$$
\operatorname{BIC}\left(\lambda^{[k]}\right)=\log \left\{\operatorname{MSE}\left(\lambda^{[k]}\right)\right\}+\left\{\log (N) / N\right\} \mathrm{DF}_{\lambda^{[k]}}
$$

where $\operatorname{MSE}\left(\lambda^{[k]}\right)=N^{-1} \sum_{i=1}^{N}\left\{Y_{i}-\hat{\eta}_{k}\left(X_{i}^{\mathrm{T}} \widehat{\boldsymbol{\beta}}_{i^{[k]}}^{[k]}\right)\right\}^{2}$ and $\mathrm{DF}_{\lambda^{[k]}}$ is the number of nonzero coefficients of $\widehat{\boldsymbol{\beta}}_{i^{[k]}}^{[k]}$, the PPrLS obtained from (12) for each $\lambda^{[k]}$.

Remark. Although the proposed method needs three steps to implement and its computational cost is high, compared to the existing methods, its gain in computational efficiency is significant. Most of dynamic network models such as dynamic Bayesian networks and random

graph models require extensive computations for posterior inference. As a result, Bayesian based methods allow one to deal with only small networks. The proposed method can avoid numerically solving the differential equations directly, and does not need the initial or boundary conditions of the state variables. The method also incorporate the high-dimensional ODEs to allow us to perform variable selection and parameter estimation for one equation. These good features gain computational efficiency.

# Numerical results 

## Real data analysis

We used the procedure introduced in Section of Methods to analyze a time-course yeast cell cycle gene expression data set. These 297 genes were identified as expressions across 18 time points during approximate two cell cycles; i.e., each gene has 18 time-related observations [49].

We implemented Step 1 using the MFDA function (available in the R package MFDA), and identified 12 functional modules. The population mean curves for the functional modules are given in Fig 1. We can see that for each functional module, the genes included share a similar pattern. These time-related patterns show two cell cycles (Fig 1). The number of genes included in each functional module ranges from 9 to 53 .

In order to construct a functional landscape of the genome-wide regulatory network through identifying interactions among modules, we used the Database for Annotation, Visualization and Integrated Discovery [50, 51] to identify enriched functional annotations in Gene ontology and Kyoto Encyclopedia of Genes and Genomes pathways for each functional module. A modified Fisher exact test was used to test the null hypothesis that a certain function is not over-represented in the module compared to the background population. Due to space limitation, we displayed part of the selected functional annotations in Table 1. All enriched functional annotations were provided in S1 Table.

As shown in Table 1, the function annotation analysis suggested that genes in the identified functional modules participate in broad biological process such as cell cycle, DNA replication or packaging, meiosis, regulation of transcription etc. For example, module 3 was highly enriched in DNA packaging; module 7 was enriched in cell-division cycle and mitosis; and DNA metabolic process was related to module 12. Although each functional module has multiple enriched annotations, but most annotations can be grouped into one or two clusters.

After grouping genes into functional modules, we applied step 2 to all functional modules, and obtained X $_{i}(t)$ and $\widetilde{X}_{i}^{\prime}(t), i=1, \cdots, 12$. Following the data augmentation strategy used in $[13,52,53]$ and [54], we selected 300 time points from $X_{i}(t)$ and the first derivative $\widetilde{X}_{i}^{\prime}(t)$ for the module. Therefore, the sample size is $N=300$. After substituting the estimates into singleindex models, we built the full model for module 1 , for instance, as follows.

$$
y_{1}=\eta_{1}\left(\mathbf{X}(t)^{\top} \boldsymbol{\beta}_{0}^{[1]}\right)+\varepsilon
$$

where the response variable $y_{1}=\widetilde{X}_{1}^{\prime}(t)$, the estimated first derivatives; $\mathbf{X}(t)=\left(X_{1}(t), \ldots, X_{12}(t)\right)^{T}$ are the population mean estimates of 12 functional modules; and $\boldsymbol{\beta}_{0}^{[1]}=\left(\beta_{01}^{[1]}, \ldots, \beta_{012}^{[1]}\right)^{\top}$. Applying the PPrLS procedure given in step 3 to model (15), we detected significant variables $\mathbf{X}(t)$ and obtained nonzero $\widetilde{\boldsymbol{\beta}}^{[1]}$. As a result, we identified the modules related to the gene-expression changes of the module 1. For a comparison, we also fitted $y$ to $\mathbf{X}(t)$ by using a linear ODE model [13]

$$
y_{1}=\mathbf{X}(t)^{\top} \boldsymbol{\beta}_{10}^{[1]}+\varepsilon
$$

Table 1. The inward and outward regulations in the module-based regulatory network and RSS based on the linear ODE (L-ODE) and the single-index ODE (SiODE).


https://doi.org/10.1371/journal.pone.0192833.t001

We also selected $\mathbf{X}(t)$ and estimated $\boldsymbol{\beta}_{10}^{(1)}=\left(\beta_{101}^{(1)}, \ldots, \beta_{1012}^{(1)}\right)^{\mathrm{T}}$ by applying the SCAD method to the linear ODE model (16).

Applying the procedure to all functional modules, we constructed a regulatory network among modules (Figs 2 and 3) and estimated their corresponding dynamic coefficients by both single-index and linear ODE models.

To compare the results provided by the single-index ODE and linear ODE models, we summarized the inward (significantly impact on) and outward (impacted by) regulatory relationships between modules in Table 1. The number of genes in each module was displayed in the parentheses. One can see that the residuals of sum squares (RSS) of single-index ODE models were smaller than those of the linear ODE models. We can also observe that the single-index ODE models selected more modules than the linear ODE models did. For example, the singleindex ODE model indicated that module 2 was impacted by modules $1,2,7,8,9$ and 12 of which only modules 1,7 and 9 were selected by the linear ODE model. Both linear ODE and single-index ODE indicated that modules 3,7 and 8 were important because they regulated more than $50 \%$ modules. We also noted that module 8 only included 9 genes. Further experiments are needed to explore these new discoveries in biological progression.

# A simulation study 

In this part we conducted Monte Carlo simulation studies to validate the proposed procedure for the single-index ODE models. Due to the intensive computational cost, we designed a system with 7 ODEs, which include following linear and nonlinear forms. The simulation settings

![img-1.jpeg](img-1.jpeg)

Fig 2. The GRN identified by the linear ODE models for the time course yeast cell data set. Each node represents a module and the arrows presents the direction of influence.
https://doi.org/10.1371/journal.pone.0192833.g002
are data-driven because the gene expression pattern show sine and cosines patterns (Fig 1)

$$
\begin{aligned}
& \frac{d X_{1}(t)}{d t}=0.05 *\left(\beta_{01} * X_{1}+\beta_{02} * X_{2}\right), \frac{d X_{2}(t)}{d t}=\cos \left(\beta_{03} * X_{2}+\beta_{04} * X_{3}\right) \\
& \frac{d X_{3}(t)}{d t}=\sin \left(\beta_{05} * X_{2}+\beta_{06} * X_{3}\right), \frac{d X_{3}(t)}{d t}=0.1 *\left(\beta_{07} * X_{2}+\beta_{08} * X_{4}\right) \\
& \frac{d X_{5}(t)}{d t}=\sin \left(\beta_{09} * X_{2}+\beta_{010} * X_{3}\right), \frac{d X_{6}(t)}{d t}=0.05 * \exp \left(\beta_{011} * X_{3}+\beta_{012} * X_{6}\right) \\
& \frac{d X_{7}(t)}{d t}=0.2 *\left(\beta_{013} * X_{2}+\beta_{014} * X_{3}\right), X_{p}\left(t_{0}\right)=X_{p 0}, p=1, \cdots, 7
\end{aligned}
$$

![img-2.jpeg](img-2.jpeg)

**Fig 3. The GRN identified by the single-index ODE models for the time course yeast cell data set.** Each node represents a module and the arrows present the direction of influence.

<https://doi.org/10.1371/journal.pone.0192833.g003>

where $$\beta_{0}^{[1]} = (\beta_{01}, \beta_{02}, 0, 0, 0, 0, 0)^{T} = (0.707, 0.707, 0, 0, 0, 0, 0)^{T},$$

$$\beta_{0}^{[2]} = (0, \beta_{03}, \beta_{04}, 0, 0, 0, 0)^{T} = (0, 0.555, -0.832, 0, 0, 0, 0)^{T},$$

$$\beta_{0}^{[3]} = (0, \beta_{05}, \beta_{06}, 0, 0, 0, 0)^{T} = (0, 0.832, -0.555, 0, 0, 0, 0)^{T},$$

$$\beta_{0}^{[4]} = (0, \beta_{07}, 0, \beta_{08}, 0, 0, 0)^{T} = (0, 0.600, 0, -0.800, 0, 0, 0)^{T},$$

$$\beta_{0}^{[5]} = (0, \beta_{09}, 0, \beta_{010}, 0, 0, 0)^{T} = (0, 0.894, 0, 0.447, 0, 0, 0)^{T},$$

$$\beta_{0}^{[6]} = (0, 0, \beta_{011}, 0, 0, \beta_{012}, 0)^{T} = (0, 0, 0.894, 0, 0, -0.447, 0)^{T}, \text{ and}$$

$$\beta_{0}^{[7]} = (0, \beta_{013}, \beta_{014}, 0, 0, 0, 0)^{T} = (0, 0.894, -0.447, 0, 0, 0, 0)^{T}.$$

Given initial values $X_{p0}, p = 1, \ldots, 7$, we can numerically solve the above ODE system and obtain the numerical solution $X_p(t), p = 1, \ldots, 7$. In this simulation study, we first generated

initial values $X_{p}(0), p=1, \ldots, 7$ by using

$$
X_{p 0}=X_{0}+0.5 * e_{p}, p=1, \ldots, 7
$$

where $e_{p}$ follows $N(0,1)$ and $X_{0}=(0.7628,0.6789,1.2351,0.6170,2.7800,0.2906,0.4441)$. We then numerically solved the ODE system (17) and output $X_{p}(t), p=1, \ldots, 7$, using three different schedules: equally spaced time points on the ranges of $[0,18]$, but three different intervals between time points. As a result, we simulated seven population means $X_{p}\left(t_{i}\right), p=1, \ldots, 7$, $i=1, \ldots, N$ with sample sizes $N=180,288,360$. After generating the population mean curves, we used the spline method to estimate the first derivatives, which are denoted by $\widehat{X}_{p}^{\prime}(t)$, $p=1, \ldots, 7$. For notation simplicity, we gave the model structure and estimation procedure for the first ODE $(k=1)$. The same procedure can be applied to the rest of the ODEs. Substituting the generated $X_{p}(t), p=1, \ldots, 7$ and estimated $\widehat{X}_{1}^{\prime}(t)$ into the single-index ODE models, we obtained the largest model for the first ODE as follows:

$$
\widehat{X}_{1}^{\prime}\left(t_{i}\right)=\eta_{1}\left(\mathbf{X}\left(t_{i}\right)^{\mathrm{T}} \boldsymbol{\beta}_{1}^{(1)}\right)+\varepsilon_{i}, i=1, \ldots, N
$$

where $\boldsymbol{\beta}_{0}^{(1)}=\left(\beta_{01}^{(1)}, \ldots, \beta_{07}^{(1)}\right)^{\mathrm{T}}$ and $\mathbf{X}\left(t_{i}\right)=\left(X_{1}\left(t_{i}\right), \cdots, X_{7}\left(t_{i}\right)\right)^{\mathrm{T}}, i=1, \cdots, N$. Applying the procedure given in Step 3, we selected $\mathbf{X}(t)$ and estimated $\boldsymbol{\beta}_{0}^{(1)}$ for the first ODE. Applying the same procedure to the other six ODEs, we estimated $\boldsymbol{\beta}_{0}^{(k)}, k=2, \ldots, 7$. As a result, we constructed GRN for the simulated functional modules. We repeated the same procedure 100 time and summarized the $\operatorname{MSE}_{q}=\sum_{j=1}^{100}\left(\widehat{\beta}_{q j}-\beta_{0 q}\right)^{2} / 100$ and $\operatorname{ARE}_{q}=\sum_{j=1}^{100} \frac{\left|\widehat{\beta}_{q j}-\beta_{0 q}\right|}{\left|\beta_{0 q}\right|}, q=1, \ldots, 14$, where $\widehat{\beta}_{q j}$ is the estimated $\beta_{q}$ for $j_{10}$ iteration. In Table 2, "overfitted (O)" represents extra variables; "underfitted (U)" represents incorrectly deleting necessary variables. We can see that the PPrLS method can correctly select the variables for most cases in terms of the number of correctly fitted model. Larger sample sizes lead to better performance. For ODEs with a linear form, namely ODE1, ODE4, and ODE7, both variable selection and parameter estimation procedures have good performance when the sample size is 180 . For the nonlinear case, with the increase of the sample size, both variable selection and parameter estimation tend to work better. In addition, we reported the $10 \%$ trimmed MSE and ARE (discarding 5\% of the lowest and the highest values). Meanwhile, we constructed networks among simulated functional modules for each iteration (see Figs 4, 5 and 6). The thick lines represents true connection, and the numbers present the times which were found by our method in 100 iterations. From Figs 4, 5 and 6, we can see that the constructed GRN match the true network in most cases.

# Conclusions and discussions 

In this paper, we have proposed single-index ODE models and developed a procedure to select variables and estimate parameters. The procedure has further been used to analyze a timecourse data set with the aim of exploring the module based and regulator-regulator interactions. We found the interactions identified by using single-index ODE were more accurate, i.e., the linear ODE models overlooked some confirmed regulator-regulator interactions [55]. We took module 12 as an example. MBP1 is a DNA-binding protein that forms MBF complex; a protein complex that binds to the Mlu1 cell cycle box promoter element. [56, 57] showed that MBP1 is topologically related to transcription factors, including SWI4 in Saccharomyces cerevisiae. In addition, there is physical and genetic evidence that MBP1 interacts with SKN7, a transcription factor [58]. These two interactions are identified as potential interactions in module 12 by single-index ODE models, but are overlooked by the linear ODE models.

Table 2. The simulation results for the SCAD method for scenarios with different sample sizes based on 100 replications. The simulation results for the SCAD method for scenarios with different sample sizes based on 100 replications. Correctly fitted (C); underfitted (U); overfitted(O).


(Continued)

Table 2. (Continued)


https://doi.org/10.1371/journal.pone.0192833.t002

![img-3.jpeg](img-3.jpeg)

Fig 4. The constructed gene regulatory networks for simulation studies with $N=180$ and 100 iterations. Solid lines: the true connections, numbers present: the times correctly identified using our procedure in 100 iteration, dots line: incorrectly identified connections. https://doi.org/10.1371/journal.pone.0192833.g004

![img-4.jpeg](img-4.jpeg)

Fig 5. The constructed gene regulatory networks for simulation studies with $N=288$ and 100 iterations. The legend is the same as in Fig 4.
https://doi.org/10.1371/journal.pone.0192833.g005

The advantages of our method include (i) single-index ODE models can fit the data better than linear ODE models; (ii) the interactions found by single-index ODE models can cover most of the interactions identified by linear ODE models for some of the modules; and (iii) our method is computationally efficient because we can select significant modules and estimate index coefficients simultaneously.

Similar to the linear ODE model, our method needs estimated population means and their corresponding first derivatives, which may be treated as the limitation of the proposed procedure. The PPrLS estimator has good performance in identifying significant modules. But new stable techniques are still needed to group genes to reduce the gene cluster uncertainty because cluster assignment still plays an important role in enhancing the usefulness of this research. It is worth noting that the PPrLS estimates may not be most efficient in terms of estimation accuracy because PPrLS estimation is a nonparametric method and inherits error if the data

![img-5.jpeg](img-5.jpeg)

Fig 6. The constructed gene regulatory networks for simulation studies with $N=360$ and 100 iterations. The legend is the same as in Fig 4.
https://doi.org/10.1371/journal.pone.0192833.g006
contain a large noise. Regulator-regulator interaction exploration depends on the knowledge of gene-regulator relationship, which we study. So the proposed method may provide valuable insights into complicated biological processes with understanding gene-gene and gene-regulator relationships. Overall, our procedure is useful to single out high level (module based) and potential regulator-regulator interactions which are helpful to provide guidance for tedious and costly experiments.

# Supporting information 

## S1 Table. All enriched functional annotations.

(PDF)

S2 Table. The estimated regression coefficients for every functional modules using singleindex and linear ODE models.
(PDF)
S1 File. Large-sample properties of the PPrLS procedure and discussion of computation cost.
(PDF)
S2 File. Clustered data.
(TXT)
S3 File. Estimated coefficients using the proposed model and methods.
(TXT)
S4 File. Estimated coefficients using the linear ODE model.
(TXT)
S5 File. Functional annotations.
(XLS)
S6 File. R code for clustering.
$(\mathrm{R})$
S7 File. R code for drawing Fig 3.
$(\mathrm{R})$

# Acknowledgments 

The authors thank the editors and two referees for their constructive comments that have remarkably improved an earlier version of this paper.

## Author Contributions

Formal analysis: Qi Zhang, Yao Yu.
Methodology: Qi Zhang, Yao Yu, Jun Zhang, Hua Liang.
Software: Yao Yu.
Supervision: Hua Liang.
Validation: Yao Yu, Hua Liang.
Writing - original draft: Yao Yu, Jun Zhang, Hua Liang.
Writing - review \& editing: Qi Zhang, Hua Liang.
