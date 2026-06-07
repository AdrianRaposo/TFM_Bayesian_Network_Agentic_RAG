# Gene regulatory network inference based on a nonhomogeneous dynamic Bayesian network model with an improved Markov Monte Carlo sampling 

Jiayao Zhang ${ }^{1}$, Chunling $\mathrm{Hu}^{1 *}$ and Qianqian Zhang ${ }^{1}$<br>*Correspondence:<br>huchunling@hfuu.edu.cn<br>${ }^{1}$ College of Artificial Intelligence and Big Data, Hefei University, Hefei 230031, China


#### Abstract

A nonhomogeneous dynamic Bayesian network model, which combines the dynamic Bayesian network and the multi-change point process, solves the limitations of the dynamic Bayesian network in modeling non-stationary gene expression data to a certain extent. However, certain problems persist, such as the low network reconstruction accuracy and poor model convergence. Therefore, we propose an MD-birth move based on the Manhattan distance of the data points to increase the rationality of the multi-change point process. The underlying concept of the MD-birth move is that the direction of movement of the change point is assumed to have a larger Manhattan distance between the variance and the mean of its left and right data points. Considering the data instability characteristics, we propose a Markov chain Monte Carlo sampling method based on node-dependent particle filtering in addition to the multi-change point process. The candidate parent nodes to be sampled, which are close to the real state, are pushed to the high probability area through the particle filter, and the candidate parent node set to be sampled that is far from the real state is pushed to the low probability area and then sampled. In terms of reconstructing the gene regulatory network, the model proposed in this paper (FC-DBN) has better network reconstruction accuracy and model convergence speed than other corresponding models on the Saccharomyces cerevisiae data and RAF data.


Keywords: Nonhomogeneous dynamic Bayesian network mode, Multi-change point process, Markov chain Monte Carlo, Gene regulatory network

## Introduction

The construction of gene regulatory networks through the analysis of gene expression data is an important method to study gene regulatory relationships, thus aiding in the analysis of biological phenomena [1], for example, studying the etiology of diseases, particularly in developing the target genes at the molecular level of bioinformatics, to better influence the effect of drugs. Given that the gene regulatory networks are frequently constructed from gene expression data, several mathematical models have

## E BMC

© The Author(s) 2023. Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http:// creativecommons.org/licenses/by/4.0/. The Creative Commons Public Domain Dedication waiver (http://creativecommons.org/publicdo- main/zero/1.0/) applies to the data made available in this article, unless otherwise stated in a credit line to the data.

been introduced and successfully applied in this field, thus providing important computational biology tools for a systematic research on the regulation and patterns of gene transcription in living systems. Representative network models include Boolean network [2, 3], association network [4, 5], differential equation [6-8], and Bayesian network models [9-11]. The Boolean network simplifies the gene state accordingly, and uses Boolean functions instead of differentials and derivatives to describe the relationship between genes. The shortcoming of this model lies in its inaccuracy. Just by using fixed logic rules to describe and reflect the interaction between genes, it cannot accurately describe the real gene regulatory network topology, and it will inevitably cause many problems when discretizing genetic data. The modeling of association network is mainly realized by the degree of association between gene expression data. Mutual information, Pearson correlation coefficient and other measures are usually used to calculate the similarity between genes. If the similarity between gene pairs is higher than a certain threshold, the gene pair is directly connected in the network. The advantage of this method is that the establishment of the model is simple and easy to operate, but there are many false positive edges in the constructed network. Differential equation models can well simulate complex systems, including gene regulatory networks that describe complex regulatory relationships among genes. Although it reflects the internal law, since the establishment of the equation is based on the assumption of the independence of local laws, the deviation is a bit large when making medium and long-term forecasts, and the solution of the differential equation is relatively difficult to obtain.

Recently, the Bayesian network models of gene regulatory networks have been extensively developed owing to their ability to reconstruct directed acyclic graphs, which can describe both the regulatory relationship and the direction of regulation of genes. Friedman et al. have constructed a gene regulatory network containing 800 genes on the basis of the Bayesian network model [12]. However, an unavoidable time delay exists between the regulation of two genes. On the basis of this property, Murphy et al. have proposed a dynamic Bayesian network model to analyze temporal gene expression data [13]. Since real gene networks have cyclic regulatory pathways including feedback loops. When we have time series microarray data, the use of dynamic Bayesian networks (DBNs) is a promising alternative, since DBNs can treat time delay information and can construct cyclic networks. Kim et al. [14] through extensive work, have also improved the dynamic Bayesian network by combining linear or nonlinear models and corresponding biological knowledge.

The structure and parameters of the traditional dynamic Bayesian network model cannot change over time; that is, the time series is required to be a stable distribution generated by a homogeneous Markov chain; thus, the traditional dynamic Bayesian network model is limited by the non-stationary nature of gene expression data. To address this issue, Lèbre et al. [15] have proposed a dynamic Bayesian network model based on a Bayesian regression model (BR-DBN), which incorporates a multi-change point process, thus allowing the network structure and parameters to vary over time. However, the shortcomings of BR-DBN have been exposed in modeling short timeseries data of genes. BR-DBN considers dividing data into different segments, and assumes that the regulatory networks in different segments are inconsistent. However, for short time series, even if the environment changes slightly, it is unrealistic for

the regulatory network to undergo significant changes. In fact, what changes is only the regulatory strength rather than the regulatory relationship. Such schemes thus lead to overfitting and exaggerated uncertainties for short time series. Subsequently, Dongdelinger et al. [16, 17] have proposed several variants of BR-DBN, on the basis of the assumption that the network structure in different segments is fixed, and only the parameters change. These models all include multi-change point process, but data from different segments must be assigned to different components and do not take into account the temporal information of the data points. To address these problems, the HMM-DBN [18], proposed by Grzegorczyk et al. is based on the assumption of a hidden Markov model dependency structure between time data points. HMM-DBN considers the time order of data points and also does not restrict the distribution of data points. Since the HMM-DBN parameters are node specific, the conditional probabilities of parameters vary among segments. The notable advantage of HMM-DBN is the independence and conjugation of parameters, which can be inferred in a closed form on the basis of the likelihood. Therefore, the inference process has been reduced to sampling the network structure and the polymorphic point process from the posterior distribution through the Markov chain Monte Carlo method.

Herein, to fully exploit the hidden prior information of data points on the basis of HMM-DBN, given the unstable nature of microarray gene expression data, birth action based on the Manhattan distance of data points has been first proposed to improve the rationality of the multi-change point process. Second, according to the sampling network structure of the Markov chain Monte Carlo method, a multichange point process has been proposed along with the correlations between gene nodes that are calculated in segments, and thus a particle filter is constructed. Pushing nodes to the high probability area causes the sampled particles to be close to the actual state, thereby improving the sampling efficiency, and ultimately the network reconstruction accuracy and the convergence of the model.

This article is divided into four parts. The first part describes the Bayesian regression model combined with the variable point process and the necessary parameter inference. The second part describes the network structure inference combined with particle filters. The third part describes the variable point process. The last section describes the experimental results.

The contributions of this article can be summarized as follows.
(1) The dynamic Bayesian network is combined with the multi-variable point process for the analysis of the non-stationarity of gene expression data, including the prior information, variance of the gene data, and Manhattan distance of the mean, for the target gene calculation. The change-point birth process increases the rationality of the multi-change point process.
(2) By combining the multi-variable point process, the Pearson correlation coefficient between genes has been calculated segmentally, thus forming a particle filter, which pushes the parent node set close to the true state to the high-probability region and increases the performance of the MCMC sampler.

(3) Finally, through experiments using a yeast dataset and nine RAF pathway datasets, the effectiveness, convergence, and model stability of FC-DBN in reconstructing small-scale gene regulatory networks are verified.

# Methods 

The overall framework of gene regulatory network construction based on a dynamic Bayesian network structure prediction is shown in Fig. 1.
The overall framework of dynamic Bayesian network modeling based on structure prediction is mainly composed of five parts: (a) data preprocessing, (b) Bayesian network parameter learning, (c) multi-change point process, (d) Bayesian network structure learning, and (e) model performance evaluation. Data preprocessing is not described in detail in this paper. "Piecewise Bayesian linear regression" section introduces the parameter inference process of Bayesian network, "Network structure sampling based on node correlation particle filtering" section introduces the structure inference process of Bayesian network, and "Multi-change point process" section introduces the multi-variation point process. "Experiments and results" section presents the performance evaluation.
![img-0.jpeg](img-0.jpeg)

Fig. 1 Overall framework of dynamic Bayesian network modeling based on structure prediction: a Data are processed into the short time series data required by the model. b SNR hyperparameters, regression parameters, and variance parameters are updated through a Markov chain Monte Carlo sampling method. c The multi-change point process is updated by the Markov Chain Monte Carlo Sampling method. d A particle filter is constructed with a multivariate point process, and the network structure is resampled. e Network performance is assessed with standard F-score and AUPR measures, and an experimentally validated biological network

# Piecewise Bayesian linear regression 

The FC-DBN proposed herein is based on piecewise Bayesian linear regression. Its regression equation is:

$$
y_{g, k}=X_{\pi_{g, k}}^{T} w_{g, k}+\varepsilon_{g, k}
$$

In each component $k$ of FC-DBN, where $g=1, \ldots, N, N$ is the number of nodes; $y_{g, k}$ is assigned to the observation vector of component $k$, the regression coefficient matrix of the $w_{g, k}$ regression model, $w_{g, k}$ is the set of parent nodes of node $g$ in component $k, X_{\pi_{g, k}}^{T}$ is the observation matrix of the parent node set of node $g$ in component $k, \varepsilon_{g, k}$ is the noise parameter of the regression model, which obeys a Gaussian distribution with a mean of 0 and a variance of $\sigma_{g}$. Then the regression model likelihood is:

$$
P\left(y_{g, k} \mid X_{\pi_{g, k}}, w_{g, k}, \sigma_{g}\right)=N\left(y_{g, k} \mid X_{\pi_{g, k}}^{T} w_{g, k}, \sigma_{g}^{2} I\right)
$$

For the fixed variable point vector $V_{g}$ and the parent node set $\pi_{g}$ of the node, let the regression parameter $w_{g, k}$, the inverse signal-to-noise ratio hyperparameter $\delta_{g}^{-1}$, and the inverse variance hyperparameter $\sigma_{g}^{-2}$ obey conjugate Gaussian and Gamma distributions. The level-2 hyperparameter $A_{\delta}, B_{\delta}, A_{\sigma}, B_{\sigma}$ is fixed. Figure 2 shows the hierarchical structure of the non-homogeneous dynamic Bayesian network model. The MCMC sampling is according to Eq. (6). Algorithm 1 generates samples from the posterior distribution, and Eq. (3-5) is used to update the hyperparameters.

$$
\begin{aligned}
& \left\{\begin{array}{l}
P\left(w_{g, k} \mid \sigma_{g}^{2}, \delta_{g}\right)=N\left(w_{g, k} \mid 0, \delta_{g} \sigma_{g}^{2} I\right) \\
P\left(w_{g, k} \mid y_{g, k}, X_{\pi_{g, k}}, \sigma_{g}^{2}, \delta_{g}\right)=N\left(\left(\delta_{g}^{-1} I+X_{\pi_{g, k}} X_{\pi_{g, k}}^{T}\right)^{-1} X_{\pi_{g, k}} y_{g, k}, \sigma_{g}^{2}\left(\delta_{g}^{-1} I+X_{\pi_{g, k}} X_{\pi_{g, k}}^{T}\right)^{-1}\right. \\
& \left\{\begin{array}{l}
P\left(\delta_{g}^{-1} \mid A_{\delta}, B_{\delta}\right)=\operatorname{Gam}\left(\delta_{g}^{-1} \mid A_{\delta}, B_{\delta}\right)=\frac{\left|B_{\delta}\right|^{A_{\delta}}}{\Gamma\left(A_{\delta}\right)}\left[\delta_{g}^{-1}\right]^{A_{\delta}-1} e^{-B_{\delta} \delta_{g}^{-1}} \\
P\left(\delta_{g}^{-1} \mid w_{g, k}, \sigma_{g}^{2}\right)=\operatorname{Gam}\left(A_{\delta}+\frac{K_{g}\left(\left\lceil\sigma_{g}\right\rceil+1\right)}{2}, B_{\delta}+\frac{1}{2 \sigma_{g}^{2}} \sum_{k=1}^{K_{g}} w_{g, k}^{T} w_{g, k}\right)
\end{array}\right.
\end{aligned}
$$

![img-1.jpeg](img-1.jpeg)

Fig. 2 Hierarchy of inhomogeneous dynamic Bayesian network models. The inverse signal-to-noise ratio hyperparameter and the inverse variance hyperparameter are assumed to obey the conjugate gamma distribution, and the regression parameter is assumed to obey the conjugate Gaussian distribution

$$
\left\{\begin{array}{l}
P\left(\sigma_{g}^{-2} \mid A_{\sigma}, B_{\sigma}\right)=\operatorname{Gam}\left(\sigma_{g}^{-2} \mid A_{\sigma}, B_{\sigma}\right)=\frac{\left|B_{\sigma}\right|_{\sigma}^{A_{\sigma}}}{\Gamma\left(A_{\sigma}\right)}\left[\sigma_{g}^{-2}\right]^{A_{\sigma}-1} e^{-B_{\sigma} \sigma_{g}^{-2}} \\
P\left(\delta_{g}^{-1} \mid w_{g, k}, \sigma_{g}^{2}\right)=\operatorname{GamP}\left(\sigma_{g}^{-2} \mid y_{g, V_{g}}, X_{\sigma_{g}, k}, \delta_{g}\right)=\operatorname{Gam}\left(A_{\sigma}+\frac{T-1}{2}, B_{\sigma}\right. \\
+\frac{\sum_{k=1}^{K_{g}}\left(y_{g, k}^{T}\left(I+\delta_{g} X_{\sigma_{g, k}}^{T}\right)^{-1} y_{g, k}\right)}{2}\left(A_{\delta}+\frac{K_{g}\left(\left|\sigma_{g}\right|+1\right)}{2}, B_{\delta}+\frac{1}{2 \sigma_{g}^{2}} \sum_{k=1}^{K_{g}} w_{g, k}^{T} w_{g, k}\right)
\end{array}\right.
$$

$$
P\left(w_{g, k}, \delta_{g}, \sigma_{g}^{2} \mid D\right) \propto \prod_{g} P\left(\delta_{g}\right) P\left(\sigma_{g}^{2}\right) \prod_{k} P\left(w_{g, k} \mid \delta_{g}, \sigma_{g}\right) P\left(y_{g, k} \mid X_{\sigma_{g, k}}, \sigma_{g}, w_{g, k}\right)
$$

Algorithm 1. Pseudo-code for updating the SNR hyperparameter $\delta_{g}$

```
For each node \(g=1, \ldots, N\)
Input: \(\sigma_{g}, V_{g}, \delta_{g}^{-1}\)
Output: \(\delta_{g}^{(1)}\)
MCMC iteration: \((i-1) \rightarrow i\)
(1) Sample a concrete variance hyperparameter \(\sigma_{g}^{(i)}\) from \(\sigma_{g}^{-2}\left[\left(y_{g, V_{g}}, X_{\sigma_{g}, k}, \delta_{g}^{(i-1)}\right)\right.\) [Eq. (5)]
(2) Sample regression parameter vectors \(w_{g, k}^{i}\) from \(w_{g, k}\left(\left(y_{g, k}, X_{\sigma_{g, k}}, \sigma_{g}^{(i)}, \delta_{g}^{(i-1)}\right)\right.\) [Eq. (4)] set:
\(w_{g, k}^{i}=\left(w_{g, 1}^{i}, \ldots, w_{g, K_{g}}^{i}\right)\)
(3) Sample a new SNR hyperparameter \(\delta_{g}^{(i)}\) from \(\delta_{g}^{-1}\left[\left(w_{g, k}^{(i)}, \sigma_{g}^{(i)}\right)\right.\) [Eq. (3)], and output: \(\delta_{g}^{(i)}\)
```


# Network structure sampling based on node correlation particle filtering 

The parent node set is ideally sampled close to the actual state. Using MCMC sampling with the parent node set obeying a uniform distribution result in the multiple invalid sampling by the sampler. To overcome this shortcoming, we propose a method to push the parent node set with high similarity to the actual state to the high probability region, and the parent node set dissimilar to the actual state to the low probability region, by using observational information and a variable point process. And the resampling process of the particle filter combined with the multi-variation point process is shown in Fig. 3.
![img-2.jpeg](img-2.jpeg)

Fig. 3 The particle filter is constructed by combining a multi-point process, calculating the Pearson correlation coefficient between nodes in components, and then resampling

The particle is represented by $\left(\pi_{g}, V_{g}, X_{g, k}\right), g$ is the node, $\pi_{g}$ is the parent node set, $V_{g}$ is the variable point vector, and $C$ is the auxiliary matrix. At initialization, $\pi_{g}=0$, $V_{g}=I, X_{g, k}=X_{g}$. After one MCMC sampling, the particle state is transferred to the current particle state. According to Algorithm $3, \pi_{g}^{(i-1)}$ is transformed into $\pi_{g}^{(i)}$, and according to Algorithm $5, V_{g}^{(i-1)}$ is transformed into $V_{g}^{(i)}$.
The candidate parent node set has been obtained by adding or removing parent nodes from the current parent node set. Therefore, we determine whether the parent node set is close to the actual state by constructing a filter matrix based on the correlation between the two nodes. When $g^{\prime} \rightarrow g$ is the real state, the node correlation coefficient $R_{g, g^{\prime}}$ between nodes $g^{\prime}$ and $g$ is close to 1 , and under the action of the filter matrix $R$, the candidate parent node set is expected to be pushed to the high probability region.
The Pearson's correlation coefficient is used in statistics to measure the linear correlation between two variables [19]. However, the non-stationarity of gene expression data makes analyzing the relationship between gene nodes by Pearson correlation coefficient invalid. We calculate the Pearson's correlation coefficient between nodes by combining the multi-point process. Through the auxiliary matrix C, the Pearson correlation coefficient of the longer data segment can have a greater effect on the gene node correlation than the shorter date segment. Finally, the particle filter matrix R is obtained.

$$
R^{i} \mid\left(D, V_{g}^{(i)}, R^{(i-1)}\right) \sim R_{g, g^{\prime}}^{i}=\left(R_{g, g^{\prime}}^{(i-1)} \times C^{(i-1)}+P_{X_{g, k}, X_{g^{\prime}, k^{\prime}}} \times \frac{\left|X_{g, k}\right|}{T}\right) /\left(C^{i}\right)
$$

where $C^{i}=C^{(i-1)}+\frac{\left|X_{g, k}\right|}{T}{ }^{(i-1)},\left|X_{g, k}\right|$ represents the data length of $\left|X_{g, k}\right|, k\left(k=1, \ldots, K_{g}\right)$ is randomly selected with the probability of $\frac{\left|X_{g, k}\right|}{T}, k^{\prime}=V_{g^{\prime}, X_{g, k^{\prime}}} P_{X_{g, k}, X_{g^{\prime}, k^{\prime}}}$ is the Pearson's correlation coefficient, and $P_{X_{g, k}, X_{g^{\prime}, k^{\prime}}}=\frac{\cos \left(X_{g, k}, X_{g^{\prime}, k^{\prime}}\right)}{\sigma_{X_{g, k}} \sigma_{X_{g^{\prime}, k^{\prime}}}}}$. Two important properties in the process of building the filter matrix are as follows.
(1) In-component data with more data points are relatively easier to use to build filter matrices.
(2) In MCMC sampling, the later the sampling, the weaker the update effect of the filter.

On the basis of Algorithm 2, the particles that are close to the real state are pushed to the high probability area.

```
Algorithm 2 Pseudo-code for particle filter
Input: \(V_{g}, \pi_{g}^{(i-1)}, R^{(i-1)}\)
Output: \(\pi_{g}^{i-1}, R^{i}\)
For \(g^{\prime}=1, \ldots, N\)
(1) Randomly select \(g^{\prime}, \mathrm{s}=\operatorname{rand}(1)\)
if \(a<R_{g, g^{\prime}},\) according to [oq (7)]
add node \(g^{\prime}\) to the parent node set \(\pi_{g}^{(i-1)}\);
otherwise, remove node \(g^{\prime}\) from the parent node set \(\pi_{g}^{(i-1)}\)
(2) Output: \(\pi_{g}^{i-1}, R^{i}\)
```

The fixed inverse SNR hyperparameter is $\delta_{g}^{-1}$, the regression parameter id $w_{g, k}$, the inverse variance hyperparameter is $\sigma_{g}^{-2}$, and the variable point component vector is $V_{g}$. Let the network structure $M=\left(\pi_{1}, \ldots, \pi_{N}\right)$; then the probability distribution of the network structure is:

$$
P(M)=\prod_{g=1}^{N} P\left(\pi_{g}\right)
$$

For each node g , the conditional probability of its parent node set $\pi_{g}$ is:

$$
P\left(\pi_{g} \mid D, V_{g}, \delta_{g}\right) \propto P\left(y_{g, V_{g}} \mid X_{\pi_{g}, k}, \delta_{g}\right)
$$

According to the Metropolis-Hastings sampling ( $\mathrm{M}-\mathrm{H}$ sampling) criterion, the probability that the candidate parent node sets $\pi_{g}^{(\mathrm{c})}$ is accepted is:

$$
A\left(\pi_{g}^{(i-1)} \rightarrow \pi_{g}^{(\mathrm{c})}\right)=\min \left(1, \frac{P\left(y_{g, V_{g}} \mid X_{\pi_{g}^{(\mathrm{c})}, k}, \delta_{g}\right)}{P\left(y_{g, V_{g}} \mid X_{\pi_{g}^{(i-1)}, k}, \delta_{g}\right)} \times \frac{P\left(\pi_{g}^{(\mathrm{c})}\right)}{P\left(\pi_{g}^{(i-1)}\right)} \times \frac{\left|S\left(\pi_{g}^{(i-1)}\right)\right|}{\left|S\left(\pi_{g}^{(\mathrm{c})}\right)\right|}\right)
$$

If the action is accepted, then: $\pi_{g}^{(i)}=\pi_{g}^{(\mathrm{c})}$; otherwise, $\pi_{g}^{(i)}=\pi_{g}^{(i-1)}$.

Algorithm 3. Pseudo-code for the MCMC inference of the parent node sets $\pi_{g}$
For each node $g=1, \ldots, N$
Input: $\delta_{g}, Y_{g}, \pi_{g}^{(i-1)}$
Output: $\pi_{g}^{(i)}$
MCMC sampling: $(\boldsymbol{i}-\mathbf{1}) \rightarrow \boldsymbol{i}$
(C) According to Algorithm 2, obtain the candidate parent node set $\pi_{g}^{(\mathrm{c})}$
(D) According to [sq (10)], if the action is accepted, then: $\pi_{g}^{(i)}=\pi_{g}^{(\mathrm{c})}$; otherwise, $\pi_{g}^{(i)}=\pi_{g}^{(i-1)}$, and the output is $\pi_{g}^{(i)}$

# Multi-change point process 

The above reasoning is based on the assumption of that the component vector $V_{g}$ is fixed. This section describes the sampling process of the component vector $V_{g}$. The component vector changes are determined by the moves of birth, death, and
![img-3.jpeg](img-3.jpeg)

Fig. 4 Three move schemes for the multi-change process: birth move, death move, inclusion move, and exclusion move

complementary inclusion of the transition point. Figure 4 is a schematic diagram of three actions.

```
Algorithm 4. Pseudo-code for the MD-birth move
Input: \(V_{g}, k_{\max }\)
Output: \(V_{g}, k_{\max }\)
Randomly select \(k \in V_{g}\)
for \(X_{i} \in X_{g, k}\)
    Change the component after \(X_{i}\) to \(k^{\prime}=k_{\max }+1\), and obtain the Manhattan distance \(d\) according to
    formula 11
    \(u=\operatorname{rand}(0,1)\)
    If \(u<\mathrm{d}\)
        update and output: \(V_{g}, k_{\max }=k^{\prime}\)
        calculate acceptance rate \(b_{k}\)
        break
```

We propose a birth move based on the Manhattan distance of data points, and assume that the mean and variance of observation vectors of different components will differ. According to this assumption, by calculating the Manhattan distance of the mean and variance within different components, the birth move will tend to move in the direction of the larger Manhattan distance

$$
d=\lambda\left(\left|\operatorname{var}\left(X_{g, k}\right)-\operatorname{var}\left(X_{g, k^{\prime}}\right)\right|+\left|u\left(X_{g, k}\right)-u\left(X_{g, k^{\prime}}\right)\right|\right)
$$

where $b_{k}, d_{k}$, and $r_{k}$ represent the acceptance rates of the birth move, death move, and inclusion and exclusion move actions, respectively, which can be obtained according to the method proposed by Grzegorczyk et al. The RJ-MCMC algorithm steps for updating the changepoint are shown in Algorithm 5.

```
Algorithm 5. Pseudo-code for the RJ-MCMC sampling changepoint based on the Euclidean distance of data points
Input: component vector \(V_{g}\) of the current node g and the maximum number of change points \(k_{\max },\) network \(M\)
Output: \(V_{g}, k_{\max }\)
(1) For each sampling process, calculate \(b_{k}, d_{k}\), and \(r_{k}\) according to the current number of conversion points \(k_{\max }\)
(2) Gibbs Sampler move
    \(\mathrm{A}=\operatorname{rand}(0,1)\)
    If \(\mathrm{A}<b_{k}\) birth move according to Algorithm 4
    If \(\mathrm{A}<d_{k}\) death move
    If \(\mathrm{A}<r_{k}\) inclusion and exclusion move
(3) Output: \(V_{g}, k_{\max }\)
```

The algorithm flow of the FC-DBN is shown in Algorithm 6.

Algorithm 6. MCMC sampling pseudo-code for the FC-DBN model

```
Input: MCMC samples the current state: \(M^{(i-1)}, K_{g}^{(i-1)}, V_{g}^{(i-1)}, \delta_{g}^{(i-1)}\)
Output: new MCMC status: \(M^{(i)}, K_{g}^{(i)}, V_{g}^{(i)}, \delta_{g}^{(i)}\)
    (1) Keep the current \(M^{(i-1)}, V_{g}^{(i-1)}\) fixed, and update \(\delta_{g}^{(i-1)}\) to \(\delta_{g}^{(i)}\) according to Algorithm 1
    (2) Keep the current \(V_{g}^{(i-1)}\) and \(\delta_{g}^{(i)}\) fixed, and update \(M^{(i-1)}\) to \(M^{(i)}\) according to Algorithm 2
    (3) Keep the current \(K_{g}^{(i)}, K_{g}^{(i-1)},\) and \(\delta_{g}^{(i)}\) fixed, and update \(V_{g}^{(i-1)}\) to \(V_{g}^{(i)}\) according to Algorithm 5
```


# Experiments and results 

## Experimental settings

The experimental section is divided into three parts using a yeast dataset and nine datasets of the RAF pathway to evaluate the FC-DBN network reconstruction accuracy, model stability, and convergence of MCMC sampling. The yeast dataset containing five gene nodes is a small network structure designed by Cantone et al. The authors measured the expression levels of these genes in vivo through real-time quantitative polymerase chain reaction over 37 time points. Cantone et al. have changed the carbon source from galactose to glucose during the experiment. The dataset contains 16 measurements in galactose and 21 measurements in glucose; the observed value of $g$ at each node was recorded. Owing to the error in washing while changing glycogen, the two first measurement values have been removed to obtain a $5 \times 35$ dataset [4]. The RAF pathway data with 11 nodes has been provided by Grzegorczyk et al. [18]. The RAF pathway shows the regulatory interactions among the following $n=11$ proteins: PIP3, PLCG, PIP2, PKC, PKA, JNK, P38, RAF, MEK, ERK, and AKT. There are 20 regulatory interactions (directed edges) in the RAF pathway. Figure 5 shows the yeast network structure and the topology of the RAF pathway.

According to the posterior probability $e_{n, j} \in(0,1)$ of the existence of each edge, $E(\xi)$ is defined as the set of all edges whose posterior probability exceeds a threshold $\xi$, where $\xi \in[0,1]$. According to $E(\xi)$, the numbers of true positive $T P[\xi]$, false positive $F P[\xi]$, and false negative $F N[\xi]$ are determined. The network reconstruction ability of the model is evaluated with two evaluation metrics.

Equations 12-14 show the evaluation index expression. The precision-recall (PR) curve is obtained by connecting adjacent points through nonlinear interpolation. The area under the PR curve (AUC-PR) is a quantitative measure that can be obtained by
![img-4.jpeg](img-4.jpeg)

Fig. 5 a The gold standard network of the yeast data. b The gold standard network of the RAF pathway data

numerically integrating the PR curve [21]. The larger the AUC-PR and $F_{\text {score }}$ value, the stronger the network reconstruction ability of the model.

$$
\begin{aligned}
& R[\xi]=T P[\xi] /\left(T P[\xi]+F N[\xi]\right) \\
& \mathrm{P}[\xi]=\mathrm{TP}[\xi] /(\mathrm{TP}[\xi]+\mathrm{FP}[\xi]) \\
& \mathrm{F}_{\text {score }}=\left(2 \times \mathrm{R}[\xi] \times \mathrm{P}[\xi]\right) /(\mathrm{R}[\xi]+P[\xi])
\end{aligned}
$$

To assess convergence, we consider scatter plots of the edge scores of ten independent MCMC simulations on the same dataset. We assume that the current number of MCMC simulations is $I$, the burning rate is burn_in, and $\operatorname{net}(n, j)^{i}=1$ indicates that edge $n \rightarrow j$ exists when the number of iterations is $i$; otherwise, $\operatorname{net}(n, j)^{i}=0$. We perform Q independent replicates of MCMC sampling. Plots of a scatterplot with average_edge_scores ${ }_{(n, j)}$ values as the vertical axis and edge_scores ${ }_{(n, j)}$ values as the horizontal axis are constructed.

$$
\begin{aligned}
& \text { edge_scores }_{(n, j)}^{q}=\frac{\sum_{i=\text { burn_in }+1}^{I} \operatorname{net}(n, j)^{i}}{I-\text { burn_in }} \\
& \text { average_edge_scores }_{(n, j)}=\frac{\sum_{q=1}^{Q} \text { edge_scores }_{(n, j)}^{q}}{Q}
\end{aligned}
$$

# Experimental results 

## Network reconstruction accuracy evaluation

A particle filter is constructed to improve the efficiency of the MCMC sampler. Table 1 shows the experimental results of the ratio of acceptance times to sampling times for the MCMC sampling network structure. The MCMC sampler of FC-DBN performs significantly better than HMM-DBN. The efficiency of HMM-DBN's MCMC sampler is less

Table 1 Comparison of acceptance rates of HMM-DBN and FC-DBN samplers


![img-5.jpeg](img-5.jpeg)

Fig. 6 Comparison of network reconstruction capabilities of different models under different evaluation indicators: a evaluation of network reconstruction ability with the AUC-PR evaluation index. b Evaluation of network reconstruction ability with the F-score evaluation index. c Comparison of network reconstruction capability of HMM-DBN and FC-DBN under different MCMC sampling times
![img-6.jpeg](img-6.jpeg)

Fig. 7 AUC-PR and F-score evaluations of three different models on nine sets of RAF data: a evaluation of network reconstruction ability with the AUC-PR evaluation index. b Evaluation of network reconstruction ability with the F-score evaluation index
than $40 \%$ on the yeast dataset and less than $50 \%$ even on the RAF pathway data. Therefore, more than half the sampler's performance is wasted. However, compared with that of HMM-DBN, the performance of FC-DBN's MCMC sampler is greatly improved, since we constructed a particle filter to cause the particles to be sampled closer to the actual state. The improvement in the performance of the MCMC sampler enables higher network reconstruction accuracy to be obtained with fewer MCMC samples.
We have used 50 independent MCMC samples to obtain 50 sets of AUC-PR and F-scores, with the mean as the final criterion. Figure 6a shows the AUC-PR of different models under yeast data, and Fig. 6b shows the F-score of different models under yeast data, where HOM-DBN is a dynamic Bayesian network model that does not include a multivariate point process. The network reconstruction accuracy of the dynamic Bayesian network model (HMM-DBN, FC-DBN) combined with the multi-change point process performs significantly better than that of HOM-DBN. Owing to the improved performance of the MCMC sampler, the AUC-PR and F-score values of the FC-DBN network have improved by $3 \%$ and $5 \%$, respectively, with respect to those of the HMMDBN. Figure 6c shows the yeast network reconstruction accuracy at different MCMC sampling times. Although the FC-DBN model does not converge at 1500 MCMC samples, the same average network reconstruction accuracy as that of HMM-DBN can be obtained with 50,000 MCMC samples. Figure 7a shows the comparison of AUC-PR values under three different models: SSC-DBN [20], HMM-DBN, and FC-DBN. Figure 7b

Table 2 AUC-PR estimates of three models on nine sets of RAF data


Table 3 F-score estimates of three models on nine sets of RAF data


shows the comparison of F-scores of the three models. Tables 2 and 3 give the specific values.

We have used 50 independent MCMC samples to obtain 50 sets of AUC-PR and F-scores, with the mean as the final criterion. Figure 6a shows the AUC-PR of different models under yeast data, and Fig. 6b shows the F-score of different models under yeast data, where HOM-DBN is a dynamic Bayesian network model that does not include a multivariate point process. The network reconstruction accuracy of the dynamic Bayesian network model (HMM-DBN, FC-DBN) combined with the multi-change point process performs significantly better than that of HOM-DBN. Owing to the improved performance of the MCMC sampler, the AUC-PR and F-score values of the FC-DBN network have improved by $3 \%$ and $5 \%$, respectively, with respect to those of the HMMDBN. Figure 6c shows the yeast network reconstruction accuracy at different MCMC sampling times. Although the FC-DBN model does not converge at 1500 MCMC samples, the same average network reconstruction accuracy as that of HMM-DBN can be obtained with 50,000 MCMC samples. Figure 7a shows the comparison of AUC-PR values under three different models: SSC-DBN [20], HMM-DBN, and FC-DBN. Figure 7b shows the comparison of F-scores of the three models. Tables 2 and 3 give the specific values.

From Figs. 6 and 7, we can find that in the RAF pathway data data5, data6 and data8, the network reconstruction accuracy of SSC-DBN compared with HMM-DBN does not have a more obvious improvement than that of YEAST data. After analyzing the main differences in data characteristics and models, there may be two reasons:
(1) RAF data has obvious segmentation characteristics. Compared with SSC-DBN, HMM-DBN, which performs data segmentation based on hidden Markov model To a certain extent, it makes up for the SSC-DBN with sequential coupling parameters.
(2) The coupling relationship between the segments of RAF data is not strong enough. When the data segmentation is not particularly in line with the actual situation, the

coupling parameters cannot fully compensate for the segmentation The impact of the segment.

# Model convergence evaluation 

The simulation platform had the following specifications. (1) Processor: Intel Core i5-9500, CPU 3.0 GHz . (2) Installed memory (RAM): 8 GB. (3) Hard disk: 1 TB. (4) Software: MATLAB R2018b. On the yeast data, we performed MCMC simulations at three different times. The MCMC simulation for each time consisted of ten independent MCMC simulations. The edge score and the average edge score have been calculated, and a scatter plot was drawn. Figures 8 and 9 show the MCMC simulation convergence of FC-DBN and HMM-DBN under different conditions. Under the same conditions, the closer edge score of scatter plot to $\mathrm{y}=\mathrm{x}$, results in better convergence effect.

Supplementary experiments were performed here and modified in the manuscript. The variance of each edge is obtained from 10 independent MCMC samples, and the variance of all edges is summed. We believe that the smaller the sum of the variances, the better the model convergence. Table 4 shows the comparison of the variance of edge scores between HMM-DBN and FC-DBN under different time losses. Obviously, FCDBN has a smaller variance than HMM-DBN edge scores. Concomitantly, with respect to the MCMC simulation time, the scatter plot of FC-DBN is closer to the $y=x$ line than that of HMM-DBN. Therefore, the convergence of FC-DBN is better than that of HMM-DBN for the yeast data.

Table 5 shows the comparison of HMM-DBN and FC-DBN loss lower edge score variance with a time loss of 100 min . Obviously, the variance of FC-DBN is smaller than the edge score of HMM-DBN. Among them, under four sets of data $(3,4,8,9)$ FC-DBN has a significant improvement in convergence performance compared to HMM-DBN. The
![img-7.jpeg](img-7.jpeg)

Fig. 8 Convergence effect of HMM-DBN and FC-DBN under different MCMC simulation time: a convergence effect of HMM-DBN under MCMC simulation for $1 \mathrm{~min}, 6 \mathrm{~min}$, and 50 min . b Convergence effect of FC-DBN under MCMC simulation for $1 \mathrm{~min}, 6 \mathrm{~min}$, and 50 min

![img-8.jpeg](img-8.jpeg)

Fig. 9 Convergence scatter plot of HMM-DBN and FC-DBN at an MCMC simulation time of 100 min on four sets of RAF data: a convergence scatter plot of HMM-DBN for four groups of RAF data. b Convergence scatter plot of FC-DBN for four groups of RAF data

Table 4 Comparison of variance of marginal scores under different models and different time losses in yeast data


Table 5 Comparison of marginal score variance of different models under 9 sets of data in RAF pathway

|  Model/
data | Data1 | Data2 | Data3 | Data4 | Data5 | Data6 | Data7 | Data8 | Data9  |
DBN | $4.3 \times 10^{-2} 6.4 \times 10^{-2} 3.8 \times 10^{-2} 4.6 \times 10^{-2} 4.8 \times 10^{-2} 3.6 \times 10^{-2} 6.3 \times 10^{-2} 3.3 \times 10^{-2} 2.9 \times 10^{-2}$ |  |  |  |  |  |  |  |   |

scattergram in Fig. 9b is closer to the $y=x$ line than the scattergram in Fig. 9a. Although Fig. 10 shows the scatterplots under the other five sets of data, the convergence of FCDBN is not significantly better than that of HMM-DBN. But from the variance comparison of edge scores in Table 5, it can be seen that the convergence performance of FC-DBN is still slightly better than that of HMM-DBN.

# Conclusion

FC-DBN has been proposed owing to the low efficiency of MCMC samplers during the DBN network reconstruction. The purpose of FC-DBN is to provide a sampling space proximate to the real state space for the network structure sampling of DBN through the particle filter step, which must push TP edges and TN edges to high-probability regions and low-probability regions. Therefore, in the network structure sampling stage, the efficiency of the MCMC sampler is greatly improved.

![img-9.jpeg](img-9.jpeg)

Fig. 10 Convergence scatter plot of HMM-DBN and FC-DBN at an MCMC simulation time of 100 min on five sets of RAF data: a convergence scatter plot of HMM-DBN for five groups of RAF data. b Convergence scatter plot of FC-DBN for four groups of RAF data

Furthermore, combining the birth action of Manhattan distance makes the multichange point process more reasonable, thus establishing the basis for building particle filters.

In our experiments, we have first evaluated the FC-DBN and HMM-DBN MCMC samplers and found that FC-DBN resulted in a significantly higher sampler efficiency than HMM-DBN. Then, we have compared the accuracy of network reconstruction, for the yeast data, for the dynamic Bayesian network model (HOM-DBN) without the combination of the multi-point process, the dynamic Bayesian network model (HMMDBN) combined with the multi-point process, and the combination of the multi-point process and the dynamic Bayesian network model of particle filter (FC-DBN). Experimental comparisons have indicated that HMM-DBN has better network reconstruction ability than HOM-DBN. With the improved MCMC sampler, FC-DBN can obtain the same network reconstruction accuracy as HMM-DBN with shorter sampling times, while improving the network reconstruction ability. Since FC-DBN adds a particle filter step, which inevitably increases the time loss, the result comparisons have been considered only for the same times in the convergence analysis with HMM-DBN. Through the experimental comparison of the yeast data and the nine sets of data of the RAF pathway, we have found that FC-DBN has a better convergence than HMM-DBN. This convergence owes to the sampling progress of MCMC that leads to the convergence of the multi-point process, and hence the particle filter can push the MCMC sampling space.

However, the model proposed in this paper also has some problems. First, especially in the face of a large multi-node network structure, the time overhead of the algorithm increases exponentially; second, in the face of some specific data sets, satisfactory results cannot be obtained.

We thank Marco Grzegorczyk for data and guidance.

## Author contributions

software, QZ, writing—original draft preparation, JZ, writing—review and editing, CH. All authors have read and agreed to the published version of the manuscript.

## Funding

This work was supported by the following grants: National Natural Science Foundation of China (General Program) 61772321, Natural Science Foundation of Hefei 2021035, Hefei University Graduate Innovation and Entrepreneurship Program (21YCXL25, 21YCXL18).

# Availability of data and materials 

The datasets analysed during the current study are available in the figshare repository, https://figshare.com/s/96f57 8777aa6b43f3638.

## Declarations

## Ethics approval and consent to participate

Not applicable.

## Consent for publication

Not applicable.

## Competing interests

The authors declare no competing interests.
Received: 8 January 2023 Accepted: 7 June 2023
Published online: 24 June 2023

## Publisher's Note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.