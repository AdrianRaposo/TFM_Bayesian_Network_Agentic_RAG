# Article 

## Constructing a Gene Regulatory Network Based on a Nonhomogeneous Dynamic Bayesian Network

Jiayao Zhang ${ }^{1,2}$ (D), Chunling $\mathrm{Hu}^{1,2, *}$ (D) and Qianqian Zhang ${ }^{1,2}$<br>check for updates<br>Citation: Zhang, J.; Hu, C.; Zhang, Q. Constructing a Gene Regulatory Network Based on a Nonhomogeneous Dynamic Bayesian Network. Electronics 2022, 11, 2936. https://doi.org/10.3390/ electronics11182936

Academic Editor: Christos J. Bouras
Received: 5 August 2022
Accepted: 13 September 2022
Published: 16 September 2022
Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## 0

Copyright: (c) 2022 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 College of Artificial Intelligence and Big Data, Hefei University, Hefei 230031, China
2 Anhui Province Urban Infrastructure Big Data Technology Application Engineering Laboratory, Hefei University, Hefei 230031, China

* Correspondence: huchunling@hfuu.edu.cn; Tel.: +86-138-5513-6422

Abstract: Since the regulatory relationship between genes is usually non-stationary, the homogeneity assumption cannot be satisfied when modeling with dynamic Bayesian networks (DBNs). For this reason, the homogeneity assumption in dynamic Bayesian networks should be relaxed. Various methods of combining multiple changepoint processes and DBNs have been proposed to relax the homogeneity assumption. When using a non-homogeneous dynamic Bayesian network to model a gene regulatory network, it is inevitable to infer the changepoints of the gene data. Based on this analysis, this paper first proposes a data-based birth move (ED-birth move). The ED-birth move makes full use of the potential information of data to infer the changepoints. The greater the Euclidean distance of the mean of the data in the two components, the more likely this data point will be selected as a new changepoint by the ED-birth move. In brief, the selection of the changepoint is proportional to the Euclidean distance of the mean on both sides of the data. Furthermore, an improved Markov chain Monte Carlo (MCMC) method is proposed, and the improved MCMC introduces the Pearson correlation coefficient (PCCs) to sample the parent node-set. The larger the absolute value of the Pearson correlation coefficient between two data points, the easier it is to be sampled. Compared with other classical models on Saccharomyces cerevisiae data, synthetic data, RAF pathway data, and Arabidopsis data, the PCCs-ED-DBN proposed in this paper improves the accuracy of gene network reconstruction and further improves the convergence and stability of the modeling process.

Keywords: gene regulatory networks; multiple changepoint processes; non-homogeneous dynamic Bayesian; Markov chain Monte Carlo; Pearson correlation coefficient

## 1. Introduction

With the rapidly decreasing cost of genome sequencing technology and the accelerated acquisition of biological experimental data, one of the key challenges in systems biology is to deduce gene regulatory networks from gene expression data. Gene regulatory networks are of great significance in biological development, maintenance of homeostasis, and the occurrence and development of diseases [1-4]. Although a large number of known regulatory relationships in organisms have been documented in various databases, they are still far from the number of interactions and complex relationships that actually exist in biological systems. Experiments are generally able to measure the abundance of elements, but it is difficult to directly discover the complex relationships among them [5]. Structural learning of dynamic Bayesian networks (DBNs) plays an important role in the construction of gene regulatory networks [6]. The traditional (homogeneous) dynamic Bayesian network models assume the network parameters to stay constant across time. This can lead to biased results and wrong conclusions, as cellular regulatory processes can change over time. Although there have been various methods to relax the homogeneity assumption of the undirected graphical model $[7,8]$, relaxing this restriction in DBN is still a popular research topic [9-12]. Various authors have proposed a combination of multiple changepoint

processes and DBNs to relax the homogeneity assumption of DBNs [13,14]. Each time series segment is delimited by two changepoints. The parameters of DBNs are node specific, so the conditional probability of the parameters varies from segment to segment. In certain regularity conditions, the outstanding advantage of the above methods is the parameter independence and conjugacy of the prior; the parameters can be integrated out in the closed form in the likelihood. Therefore, the inference task is simplified to sample the network structure and the number and location of changepoints from the posterior distribution, which can be influenced by reversible jump Markov chain Monte Carlo (RJMCMC) [15,16,17,18].

Early, the Bayesian regression model (BR-DBN), proposed by Lèbre et al., became the basic probabilistic model for non-homogeneous DBNs [19]. However, the disadvantage of the BR-DBN model is that the network structure varies from segment to segment, which leads to overfitting and exaggerated inference uncertainty for short time series. Grzegorczyk et al. proposed various variants of BR-DBN. The network structure between different segments is fixed, and the parameters are changed [20,21,22]. However, these abovementioned variable point processes combined with DBN have limitations: data points from different segments must be divided into different components. If the allocation scheme for eight time data points is [11223311], the earlier allocation scheme can only approximate it as [11223344]. Unlike CPS-DBN with changepoints, MIX-DBN can assign data points to different components without the above restrictions [23,24]. However, it does not consider the time series of data points for time series data. Adjacent data points are more likely to be assigned to the same component than distant data points.

Subsequently, Grzegorczyk et al. proposed a non-homogeneous DBN with a hidden Markov model between changepoints (HMM-DBN). The HMM-DBN not only considers the time sequence of data points but also does not impose restrictions on the distribution of data points [25]. First, HMM-DBN introduces two pairs of new complementary MCMC movesGibbs sampler move and complementary inclusion move-to improve the assignment sampler, and second, assumes a first-order hidden Markov dependency structure for transition point inference. Based on the research of HMM-DBN, this paper makes full use of the latent prior knowledge hidden in the data to improve the accuracy of the changepoint and network inference and then improves the accuracy and the stability of the network structure and the convergence of the model.

Based on the above points of view, this paper first explores the relationship between each time data point as a changepoint and time-series data points of the component. Moreover, suppose that the larger the Euclidean distance of the data means on both sides of the time data point, the more likely it is to be a changepoint. Moreover, this idea is applied to the birth move of the changepoint to improve the rationality of the conversion point birth, and then the RJMCMC sampling time data point allocation is used. Second, the causal relationship between the Pearson correlation coefficient and the edge between the node data is discussed. Suppose that the higher the Pearson correlation coefficient of the node data, the more likely there is an edge. Finally, the accuracy and stability of the network structure and the convergence of the model are improved.

# 2. Bayesian Regression Model 

A non-homogeneous DBN is an extension of a DBN in processing nonstationary time series data. A traditional dynamic Bayesian network generally contains two critical assumptions [26].
(1) First-order Markov hypothesis: Assuming that the edges between nodes cannot span a time component, the value of a node at time $t$ is only related to the value of other nodes at that time and the node at time $t-1$.
(2) Homogeneity hypothesis: The stable distribution of time data points generated by a homogeneous Markov chain requires that the model's structure and parameters cannot change over time.

However, in the actual process, most of the time-series data are nonstationary, and the homogeneity assumption described above cannot be satisfied. Therefore, traditional

dynamic Bayesian networks lose the modeling function of nonstationary data. To deal with nonstationary time series data, the changepoint process is added to the traditional dynamic Bayesian network. That is, the $m$ changepoint is added to the time sequence of time length $T$, and it is divided into $k$ components.

The hierarchical structure of the non-homogeneous DBN proposed in this paper is shown in Figure 1, and the regression equation is:

$$
y_{g, k}=X_{\pi_{g, k}}^{T} w_{g, k}+\varepsilon_{g, k}
$$

![img-0.jpeg](img-0.jpeg)

Figure 1. Hierarchy of PCCs-ED-DBN.
In each component $k$ of non-homogeneous dynamic Bayes, where $g=1, \ldots, N, N$ is the number of nodes; $y_{g, k}$ is assigned to the observation vector of component $k$, the regression coefficient matrix of the $w_{g, k}$ regression model, $\pi_{g, k}$ is the set of parent nodes of node $g$ in component $k, X_{\pi_{g, k}}^{T}$ is the observation matrix of the parent node set of node $g$ in component $k, \varepsilon_{g, k}$ is the noise parameter of the regression model, the mean is 0 , and the variance is $\sigma_{g}$ (Table 1 shows the actual meaning of each symbol). Then, the regression model likelihood is:

$$
P\left(y_{g, k} \mid X_{\pi_{g, k}}, w_{g, k}, \sigma_{g}\right)=N\left(y_{g, k} \mid X_{\pi_{g, k}}^{T} w_{g, k}, \sigma_{g}^{2} I\right)
$$

Table 1. Hyperparameters and symbols.


For, $w_{g, k}, \sigma_{g}^{-2}$ and $\delta_{g}^{-1}$ impose a Gaussian prior and conjugated gamma prior, respectively:

$$
\begin{gathered}
P\left(w_{g, k} \mid \sigma_{g}^{2}, \delta_{g}\right)=N\left(w_{g, k} \mid 0, \delta_{g} \sigma_{g}^{2} I\right) \\
P\left(\delta_{g}^{-1} \mid A_{\delta}, B_{\delta}\right)=\operatorname{Gam}\left(\delta_{g}^{-1} \mid A_{\delta}, B_{\delta}\right)=\frac{\left|B_{\delta}\right|^{A_{\delta}}}{\Gamma\left(A_{\delta}\right)}\left[\delta_{g}^{-1}\right]^{A_{\delta}-1} e^{-B_{\delta} \delta_{g}^{-1}} \\
P\left(\sigma_{g}^{-2} \mid A_{\sigma}, B_{\sigma}\right)=\operatorname{Gam}\left(\sigma_{g}^{-2} \mid A_{\sigma}, B_{\sigma}\right)=\frac{\left|B_{\sigma}\right|^{A_{\sigma}}}{\Gamma\left(A_{\sigma}\right)}\left[\sigma_{g}^{-2}\right]^{A_{\sigma}-1} e^{-B_{\sigma} \sigma_{g}^{-2}}
\end{gathered}
$$

The level-2 hyperparameter $A_{\delta}, B_{\delta}, A_{\sigma}, B_{\sigma}$ is fixed. Then, samples can be generated from the posterior distribution $P\left(w_{g, 1}, \ldots, w_{g, K_{g}}, \delta_{g}, \sigma_{g}^{2} \mid D\right)$ through Gibbs sampling [22].

Assuming that the time data points have been allocated, $V_{g}$ is known. Then, the conditional distribution of $\delta_{g}^{-1}$ and $w_{g, k}$ can be obtained as:

$$
\begin{gathered}
\delta_{g}^{-1} \mid\left(w_{g, k}, \sigma_{g}^{2}\right) \sim \operatorname{Gam}\left(A_{\delta}+\frac{K_{g}\left(\left|\pi_{g}\right|+1\right)}{2}, B_{\delta}+\frac{1}{2 \sigma_{g}^{2}} \sum_{k=1}^{K_{g}} w_{g, k}^{T} w_{g, k}\right) \\
w_{g, k} \mid\left(y_{g, k}, X_{\pi_{g, k}}, \sigma_{g}^{2}, \delta_{g}\right)=\underset{\left.\left.X_{\pi_{g, k}} X_{\pi_{g, k}}^{T}\right)_{-1}}{N\left(\left(\delta_{g}^{-1} I+X_{\pi_{g, k}} X_{\pi_{g, k}}^{T}\right)^{-1} X_{\pi_{g, k}} y_{g, k}, \sigma_{g}^{2}\left(\delta_{g}^{-1} I+\right.\right.}
\end{gathered}
$$

where $K_{g}$ is the maximum number of states allocated by node $g,\left|\pi_{g}\right|$ is the number of parent nodes of node $g$, and the inverse variance hyperparameter $\sigma_{g}^{-2}$ can also be sampled from the conditional distribution:

$$
\sigma_{g}^{-2} \mid\left(y_{g, V_{g}}, X_{\pi_{g, k}}, \delta_{g}\right) \sim \operatorname{Gam}\left(A_{\sigma}+\frac{T-1}{2}, B_{\sigma}+\frac{\sum_{k=1}^{K_{g}}\left(y_{g, k}^{T}\left(I+\delta_{g} X_{\pi_{g, k}}^{T} X_{\pi_{g, k}}\right)^{-1} y_{g, k}\right)}{2}\right.
$$

Keeping the parent node set $\pi_{g}$ and the component $V_{g}$ fixed, the MCMC sampling according to Equation (9) and Algorithm 1 can generate samples from the posterior distribution and use Equations (6)-(8) to update the hyperparameters.

$$
P\left(w_{g, k}, \delta_{g}, \sigma_{g}^{2} \mid D\right) \propto \prod_{g} P\left(\delta_{g}\right) P\left(\sigma_{g}^{2}\right) \prod_{k} P\left(w_{g, k} \mid \delta_{g}, \sigma_{g}\right) P\left(y_{g, k} \mid X_{\pi_{g, k}}, \sigma_{g}, w_{g, k}\right)
$$

Algorithm 1: Pseudocode for updating the signal-to-noise ratio hyperparameter $\delta_{g}$
For each node $g=1, \ldots, N$
Input: $\pi_{g}, V_{g}, \delta_{g}^{-1}$
Output: $\delta_{g}^{(i)}$
MCMC iteration: $(i-1) \rightarrow i$
(1) Sampling a concrete variance hyperparameter $\sigma_{g}^{(i)}$ from $\sigma_{g}^{-2} \mid\left(y_{g, V_{g}}, X_{\pi_{g, k}}, \delta_{g}^{(i-1)}\right)$

Equation (8)
(2) Sampling regression parameter vectors $w_{g, k}^{i}$, from $w_{g, k} \mid\left(y_{g, k}, X_{\pi_{g, k}}, \sigma_{g}^{(i)}, \delta_{g}^{(i-1)}\right)$

Equation (7) set: $w_{g, k}^{i}=\left(w_{g, 1}^{i}, \ldots, w_{g, K_{g}}^{i}\right)$
(3) Sampling a new SNR hyperparameter $\delta_{g}^{(i)}$ from $\delta_{g}^{-1} \mid\left(w_{g, k}^{(i)} \sigma_{g}^{(i)}\right)$ Equation (6), and output: $\delta_{g}^{(i)}$

# 3. PCCs-ED-DBN Model 

The above inference of SNR hyperparameters $\delta_{g}$ assumes that the network structure $M$ and component vectors $V_{g}$ are fixed; in fact, these need to be inferred. In this section, the inference of the network structure and component vectors is divided into two parts for

description. First, PCCs-ED-DBN infers network structure $M$ based on PCCs of data points and assumes fixed component vectors. Second, PCCs-ED-DBN infers component vectors $V_{g}$ based on Euclidean distances of data points.

# 3.1. Network Structure M Inference Based on PCCs of Data Points 

When inferring the network structure, it is still assumed that the component vector $V_{g}$ is fixed, and the probability distribution of the network structure $M=\left(\pi_{1}, \ldots, \pi_{N}\right)$ is set as:

$$
P(M)=\prod_{g=1}^{N} P\left(\pi_{g}\right)
$$

Infer the parent node set of each node $g$, that is, obtain the entire network structure. For each node, the conditional probability of its parent node set is:

$$
P\left(\pi_{g} \mid D, V_{g}, \delta_{g}\right) \propto P\left(y_{g, V_{g}} \mid \mathrm{X}_{\pi_{g}, k}, \delta_{g}\right)
$$

According to Equation (12), Metropolis-Hastings (M-H) keeps $\delta_{g}$ and $V_{g}$ fixed and moves from the current parent node set $\pi_{g}^{(i-1)}$ to a new set $\pi_{g}^{(*)}$. The move is accepted with probability:

$$
\left(\pi_{g}^{(i-1)} \rightarrow \pi_{g}^{(*)}\right)=\min \left(1, \frac{P\left(y_{g, V_{g}} \mid \mathrm{X}_{\pi_{g}^{(*)}, k^{\prime}} \delta_{g}\right)}{P\left(y_{g, V_{g}} \mid \mathrm{X}_{\pi_{g}^{(i-1)}, k^{\prime}} \delta_{g}\right)} \times \frac{P\left(\pi_{g}^{(*)}\right)}{P\left(\pi_{g}^{(i-1)}\right)} \times \frac{\left|S\left(\pi_{g}^{(i-1)}\right)\right|}{\left|S\left(\pi_{g}^{(*)}\right)\right|}
$$

If accepted, set $\pi_{g}^{(i)}=\pi_{g}^{(*)}$; otherwise, $\pi_{g}^{(i)}=\pi_{g}^{(i-1)}$.
This paper introduces the Pearson correlation coefficient [27] to explore the causal relationship between nodes. $X_{i}, X_{j}$ represent nodes, and $\lambda$ represents the slack variable; in this paper, $\lambda=1$. When the parent node is sampled by the Markov chain Monte Carlo sampling method, the node with a high Pearson correlation coefficient is more likely to be sampled. Obtain the $S\left(\pi_{g}\right)$ according to Equation (13). Algorithm 2 describes the pseudocode of M-H sampling:

$$
R_{X_{i}, X_{j}}=\lambda\left|\frac{\sum_{t=1}^{T}\left(X_{i, t}-\bar{X}_{i}\right)\left(X_{j t}-\bar{X}_{j}\right)}{\sqrt{\sum_{t=1}^{T}\left(X_{i, t}-\bar{X}_{i}\right)^{2}} \sqrt{\sum_{t=1}^{T}\left(X_{j t}-\bar{X}_{j}\right)^{2}}}\right|
$$

Algorithm 2: Pseudocode for updating the parent node sets $\pi_{g}$
For each node $g=1, \ldots, N$
Input: $\delta_{g}, V_{g}, \pi_{g}^{(i-1)}$
Output: $\pi_{g}^{(i)}$
MCMC iteration: $(i-1) \rightarrow i$
(1) Get the system of parent sets $S\left(\pi_{g}^{(i)}\right)$ :

Randomly select node $X_{j}, R_{X_{g}, X_{j}}=\lambda\left|\frac{\sum_{t=1}^{T}\left(X_{g, t}-\bar{X}_{g}\right)\left(X_{j t}-\bar{X}_{j}\right)}{\sqrt{\sum_{t=1}^{T}\left(X_{g, t}-\bar{X}_{g}\right)^{2}} \sqrt{\sum_{t=1}^{T}\left(X_{g, t}-\bar{X}_{j}\right)^{2}}}\right|_{w} a=\operatorname{rand}(1)$, if $a<R_{X_{g}, X_{j}}$ (i) adding the node $X_{j}$ to $\pi_{g}^{(i-1)}$
else (ii) deleting the node $X_{j}$ from $\pi_{g}^{(i-1)}$
(iii) exchanging a node $u \in \pi_{g}^{(i-1)}$ for a node $v \notin \pi_{g}^{(i-1)}$.

Randomly select a new candidate parent set $\pi_{g}^{(*)}$ from $S\left(\pi_{g}^{(i)}\right)$
(2) According to the probability Equation (13). If accepted, set: $\pi_{g}^{(*)}$ from $S\left(\pi_{g}^{(i)}\right)$. Otherwise, set $\pi_{g}^{(i)}=\pi_{g}^{(i-1)}$. Output: $\pi_{g}^{(i)}$

# 3.2. Component Vector $V_{g}$ Infer Based on Euclidean Distance of Data Points 

In the above sampling process, it is assumed that the component vector $V_{g}$ is fixed but in the actual process, $V_{g}$ needs to be sampled. Figure 2 lists the non-homogeneous dynamic Bayesian network with two changepoints divided into three components, namely, $V_{g}=[1,1,2,2,3,3]$. Suppose that the network structure in different components is the same, but the parameters are different.
![img-1.jpeg](img-1.jpeg)

Figure 2. Example of a non-homogeneous dynamic Bayesian network with two changepoints.

### 3.2.1. Component Transition

The component transition of the time data point is determined by the birth move, death move, and inclusion and exclusion move of the changepoint. The following describes the component transition in detail, and Figure 3 gives a specific example.
![img-2.jpeg](img-2.jpeg)

Figure 3. Component transition example.
Birth move: Randomly select a component $k$, randomly select one of the data points allocated to component $k$, and reallocate the data points allocated to component $k$ to a known new component.

Death move: Randomly select two components, $k=1$ and $k=3$, and assign the data points of component $k=3$ to component $\mathrm{k}=1$.

Inclusion and exclusion move: It is recommended to redistribute the component vector $\left[V_{g}(3), V_{g}(4)\right]=[2,2]$ to $k=1$. This is because the surrounding time points $\left[V_{g}(1), V_{g}(2)\right]$ and $\left[V_{g}(5), V_{g}(6), V_{g}(7)\right]$ are all assigned to the state $k=1$.

Therefore, if the potential prior knowledge in the data can be fully mined, it is more likely to accurately find the position of the conversion point, that is, to infer a correct component vector $V_{g}$ with node $g$, and ultimately improve the inferred accuracy of the network structure and model stability.

### 3.2.2. Birth Move Based on the Euclidean Distance

The experimental results found that the Euclidean distance of the mean on both sides of the changepoint is generally larger than that of the nonchanged point. Based on this finding,

it is not difficult to conclude that when the Euclidean distance of the mean on both sides of a data point is large, it may be the real changepoint. Based on this conclusion, this paper proposes an ED-birth move whose changepoint possibility is proportional to the Euclidean distance on both sides of the data point. Algorithm 3 shows the ED-birth move algorithm flow.
Algorithm 3: Pseudocode for changepoint birth move detection based on the Euclidean distance of data points
Input: The component vector $V_{g}$ of the current node $g$ and the maximum number of changepoint $k_{\text {max }}$
Output: $V_{g}, k_{\max}$
(1) for $k_{g} \in V_{g}$

$$
\text { for } k_{0} \in k_{g}
$$

$$
u=\operatorname{rand}(0,1), d=\left|\frac{\sum_{i=1}^{k_{0}} y g_{i} i}{k_{0}}-\frac{\sum_{i}^{3} y g_{i} i}{L-k_{0}+1}\right|
$$

$$
\begin{aligned}
& \text { if } u<d \\
& \quad g_{-k_{0}}=k_{0} ; \\
& \text { break; } \\
& \text { end } \\
& \text { end }
\end{aligned}
$$

(2) Change the component of all data points with state $k_{g}$ after $g_{-} k_{0}$ to a new component $k_{g \text { new }}=k_{\text {max }}+1$, and update $V_{g}$ and $k_{\text {max }}$ to calculate the acceptance rate $b_{k}$.
$b_{k}, d_{k}, r_{k}$, respectively, represent the acceptance rates of the birth move, death move, inclusion, and exclusion move actions. The RJ-MCMC algorithm steps for updating the changepoint are shown in Algorithm 4.
Algorithm 4: Pseudocode of RJ-MCMC sampling changepoint based on Euclidean distance of data points
Input: The component vector $V_{g}$ of the current node $g$ and the maximum number of changepoint $k_{\text {max }}$, network M
Output: $V_{g}, k_{\text {max }}$
(1) For each sampling process, calculate $b_{k}, d_{k}, r_{k}$ based on the current number of conversion points $k_{\text {max }}$
(2) Gibbs Sampler move
$\mathrm{A}=\operatorname{rand}(0,1)$
If $\mathrm{A}<b_{k}$ birth move according to Algorithm 3
If $\mathrm{A}<d_{k}$ death move
If $\mathrm{A}<d_{k}$ Inclusion and Exclusion move
(3) Output: $V_{g}, k_{\text {max }}$

The whole algorithm flow of the non-homogeneous DBN with multiple changepoints based on PPCs and Euclidean distance of data points is shown in Algorithm 5.
Algorithm 5: MCMC sampling pseudocode for the PCCs-ED-DBN model
Input: MCMC samples the current state: $M^{(i-1)}, K_{g}^{(i-1)}, V_{g}^{(i-1)}, \delta_{g}^{(i-1)}$
Output: New MCMC status: $M^{(i)}, K_{g}^{(i)}, V_{g}^{(i)}, \delta_{g}^{(i)}$
(1) Keep the current $M^{(i-1)}, V_{g}^{(i-1)}$ fixed, and update $\delta_{g}^{(i-1)}$ to $\delta_{g}^{(i)}$ according to Algorithm 1.
(2) Keep the current $V_{g}^{(i-1)}$ and $\delta_{g}^{(i)}$ fixed, and update $M^{(i-1)}$ to $M^{(i)}$ according to Algorithm 2.
(3) Keep the current $\pi_{g}^{(i)}, K_{g}^{(i-1)}, \delta_{g}^{(i)}$ fixed, and update $V_{g}^{(i-1)}$ to $V_{g}^{(i)}$ according to Algorithm 4.

# 4. Empirical Results 

### 4.1. Evaluation Standard

### 4.1.1. Convergence Evaluation Criteria

Assuming that the current number of MCMC simulations is 1 , the burning rate is burn_in, and $\operatorname{net}(n, j)^{i}=1$ indicates that there is edge $n \rightarrow j$ when the number of iterations is $i$; otherwise, $\operatorname{net}(n, j)^{i}=0$. Perform $Q$ independent replicates of MCMC sam-

pling. Plots of a scatterplot with average_edge_scores (n,j) values as the vertical axis and average_edge_scores (n,j) values as the horizontal axis.

$$
\begin{gathered}
\text { edge_scores }_{(n, j)}^{q}=\frac{\sum_{i=burn, i n+1}^{J} \operatorname{net}\left(n_{i} j\right)^{i}}{I-\text { burn_in }} \\
\text { average_edge_scores }_{(n, j)}=\frac{\sum_{q=1}^{Q} \text { edge_scores }_{(n, j)}^{q}}{Q}
\end{gathered}
$$

# 4.1.2. Network Structure Accuracy Evaluation Criteria 

$\mathrm{M}(\mathrm{n}, \mathrm{j})=1$ indicates that there is an edge $\mathrm{n} \rightarrow \mathrm{j}$, while $\mathrm{M}(\mathrm{n}, \mathrm{j})=0$ indicates that there is no edge $\mathrm{n} \rightarrow \mathrm{j}$. Define $\mathrm{E}(\mathcal{L})$ as the set of all edges whose posterior probability $\mathrm{e}_{\mathrm{n}, \mathrm{j}} \in(0,1)$ exceeds the threshold $\mathcal{L}$ for each edge. Calculate true positive $\operatorname{TP}[\mathcal{L}]$, false-positive $\operatorname{FP}[\mathcal{L}]$, and false negative $\mathrm{FN}[\mathcal{L}]$ for each $\mathrm{E}(\mathcal{L})$. Plot a precision-recall (PR) curve with $\mathrm{P}[\mathcal{L}]$ as the ordinate and $\mathrm{R}[\mathcal{L}]$ as the abscissa. A larger area under the PR curve (PR-AUC) [28] value indicates better network reconstruction accuracy.

$$
\begin{aligned}
& \mathrm{P}[\mathcal{L}]=\mathrm{TP}[\mathcal{L}] /(\mathrm{TP}[\mathcal{L}]+\mathrm{FP}[\mathcal{L}]) \\
& \mathrm{R}[\mathcal{L}]=\mathrm{TP}[\mathcal{L}] /(\mathrm{TP}[\mathcal{L}]+\mathrm{FN}[\mathcal{L}])
\end{aligned}
$$

### 4.1.3. Criteria for Model Stability

Assume the accuracy of the network structure obtained from different MCMC iteration times $i$, denoted as $A U C_{i, p}$, can be calculated. Perform $P$ independent experiments to obtain different $A U C_{i, p}$, and then calculate the variance of all $A U C_{i, p}$, denoted as $V_{i}$. A smaller variance means that the network structure inferred from each independent experiment is similar, i.e., the model is more stable. Draw a variance iteration curve with $V_{i}$ as the ordinate and $I$ as the abscissa. The stability of the network structure can be measured by comparing the curves.

$$
V_{i}=\frac{\sum_{p=1}^{P} A U C_{i, p}}{P}
$$

### 4.2. Experimental Results

### 4.2.1. Saccharomyces Cerevisiae

The Saccharomyces cerevisiae data containing five gene nodes is a small network structure designed by Cantone et al. [29]. The authors measured the expression levels of these genes in vivo by real-time quantitative polymerase chain reaction over 37-time points. Cantone et al. changed the carbon source from galactose to glucose during the experiment. There are 16 measurements in galactose and 21 measurements in glucose, and the observed value of $g$ at each node is recorded. Since there is an error in washing when changing glycogen, the two first measurement values are removed to obtain a $5 \times 35$ data set. Figure 4 shows the network structure of Saccharomyces cerevisiae.
![img-3.jpeg](img-3.jpeg)

Figure 4. The network structure of Saccharomyces cerevisiae.

It can be seen from Figure 5 that when the number of MCMC iterations is 10,000, the edge scores simulated by 20 independent MCMC simulations are almost the same, and the convergence is almost reached. With the same number of iterations, the convergence of the PCCs-ED-DBN model is better than that of the HMM-DBN.
![img-4.jpeg](img-4.jpeg)

Figure 5. Saccharomyces cerevisiae edge convergence scatter plot under HMM-DBN and PCCs-ED-DBN.
In the experiment, this paper follows the setting of Grzegorczyk et al. for hyperparameters. Set MCMC iteration: 10,000, the MCMC sampling results are saved once for each iteration, and 10,000 network structures are obtained. One hundred independent MCMC sampling results in 100 network structure accuracies, and the average value is used to obtain the final network structure accuracy (PR-AUC), as shown in Figure 6.
![img-5.jpeg](img-5.jpeg)

Figure 6. Accuracy comparison among different models on Saccharomyces cerevisiae dataset.
Figure 6 shows that the non-homogeneous DBN (PCCs-ED-DBN, HMM-DBN, CPSDNM, MIX-DBN) [23-25] can achieve higher network reconstruction accuracy than a homogeneous DBN (HOM-DBN). The PR-AUC value of PCC-ED-DBN is about $15 \%$ higher than that of the homogeneous dynamic Bayesian network (HOM-DBN), and compared with other non-homogeneous dynamic Bayesian networks (MIX-DBN, CPS -DBN, HMM-DBN) increases were $12 \%, 6 \%$, and $4 \%$.

The homogeneous dynamic Bayesian network (HOM-DBN) follows the Markov assumption, the regulation network does not change with time and the regulation intensity obeys the same distribution during the modeling process. However, when the living environment of the organism changes, it is obviously unrealistic to assume that the distribution of gene regulation strength remains unchanged. The non-homogeneous dynamic Bayesian network (PCCs-ED-DBN, HMM-DBN, CPS-DBN, MIX-DBN) constructs a regulating network with the same network structure and different parameter distributions by combining the multiple changepoint processes. In this way, the model can better reflect the actual situation of natural biological development, and the network reconstruction ability is better.

Figure 7a shows the network structure accuracy of PCCs-ED-DBN and HMM-DBN under different times of MCMC sampling. Figure 7b shows the variance comparisons of the network structure, and Table 2 gives some specific numerical comparisons. Comparing Figure 7 and Table 2, it can be found that PCCs-ED-DBN has better network structure accuracy compared with HMM-DBN. Moreover, the network structure inferred under the same MCMC sampling times, compared with HMM-DBN, PCCs-ED-DBN inferred network structure accuracy variance is smaller, so the model is more stable than HMM-DBN.
![img-6.jpeg](img-6.jpeg)

Figure 7. PR-AUC and variance under HMM-DBN and PCCs-ED-DBN. The line graph in panel (a) shows the relationship between the network reconstruction accuracy in terms of PR-AUC and the number of MCMC iterations. Line graph in panel (b) showing model stability in terms of PR-AUC variance versus number of MCMC iterations.

Table 2. The specific value of network structure variance under different models.


In addition, ED-birth is also applied to the globally coupled NH-DBN [21] and partially coupled EWC NH-DBN [30] models for comparative experiments. In the experiment, this paper follows the setting of Grzegorczyk et al. for hyperparameters. Set MCMC iterations: 20,000, the MCMC sampling results are saved once for each iteration, and 20,000 network structures are obtained. Five hundred independent MCMC sampling results in 500 network structure accuracies, and the average value is used to obtain the final network structure accuracy (PR-AUC), as shown in Figure 8a.
![img-7.jpeg](img-7.jpeg)

Figure 8. Cont.

![img-8.jpeg](img-8.jpeg)

Figure 8. PR-AUC and variance under different models. Panel (a) shows the network reconstruction accuracy in terms of PR-AUC scores incorporating the proposed ED-birth into the Globally Coupled NH-DBN and EWC NH-DBN. Panel (b) shows the relationship between the network reconstruction accuracy in terms of PR-AUC and the number of MCMC iterations under Globally Coupled NH-DBN. Panel (c) shows model stability in terms of PR-AUC variance under globally coupled NH-DBN.

From Figure 8a, it can be concluded that the non-homogeneous dynamic Bayesian networks of ED-birth move are applied, and the network structure sampled by MCMC can obtain higher accuracy. In the EWC NH-DBN models, the effect is more obvious, but the global coupled NH-DBN network structure accuracy (PR-AUC) improvement is not significant.

Figure 8b show the network structure accuracy of the ED-birth move under different numbers of MCMC samplings (Globally Coupled NH-DBN). Figure 8c show the variance comparisons of the network structure, and Table 3 gives some specific numerical comparisons.

Table 3. The specific value of network structure variance (Globally Coupled NH-DBN).


Comparing Figure 8 and Table 3, it can be found that the ED-birth move has better network structure accuracy in the globally coupled NH-DBN compared with the birth move. The network structure is inferred under the same MCMC sampling times. Compared with the birth move, the ED-birth move inferred network structure accuracy variance is smaller, so the model is more stable.

# 4.2.2. Synthetic Yeast Data

This paper generated synthetic yeast data for the $\mathrm{K}=4$ segment. Comparative experiments between HMM-DBN [25] and PCCs-ED-DBN are performed using this dataset.

We analyzed the experimental results of the synthetic yeast dataset under the HMM model. Figure 9a shows the average AUC score, and Figure 9b shows the change in the

AUC difference as the data point increases. With the increase in data points, PCCs-ED-DBN has better results for the detection of changepoints.
![img-9.jpeg](img-9.jpeg)
(a)
![img-10.jpeg](img-10.jpeg)
(b)

Figure 9. PR-AUC of synthetic dataset. Panel (a) shows the network reconstruction accuracy in terms of PR-AUC scores at different data point lengths. Panel (b) shows the difference in network reconstruction accuracy in terms of PR-AUC scores at different data point lengths.

# 4.2.3. Gene Regulatory Network in Arabidopsis 

Plants are well-suited experimental systems to study the mechanistic basis of developmental dynamics, given that they are more amenable to in vivo manipulation than, for example, animals. Constructing the Arabidopsis gene regulatory network is currently topical research [31,32,33]. Figure 10 shows that the convergence effect of the MCMC iteration number of 50,000 under the PCCs-ED-DBN model is approximately the same as the convergence effect of the MCMC iteration number of 200,000 under the HMM-DBN model. This means that to achieve the same convergence effect, PCCs-ED-DBN saves more than half the time overhead compared to HMM-DBN. Figure 11. Arabidopsis gene regulatory network with marginal probability greater than 0.5 inferred using the PCCs-ED-DBN model. Since the gene regulatory network of Arabidopsis has not been fully documented in the biological literature, the network construction accuracy cannot be calculated. However, known edges given in some biological literature are marked with bold lines in Figure 11 (GI $\rightarrow$ CCA1 [34], GI $\rightarrow$ TOC1 [34], ELF3 $\rightarrow$ TOC1 [35], ELF3 $\rightarrow$ CCA1 [35], ELF3 $\rightarrow$ PRR9 [36], TOC1 $\rightarrow$ LHY [37], LHY $\rightarrow$ TOC1 [37], ELF4 $\rightarrow$ PRR9 [38]).
![img-11.jpeg](img-11.jpeg)

Figure 10. Scatter plot of Arabidopsis edge convergence under HMM-DBN and PCCs-ED-DBN.

![img-12.jpeg](img-12.jpeg)

Figure 11. Arabidopsis gene regulatory network inferred by the PCCs-ED-DBN model.

# 4.2.4. Simulated Data from the RAF Pathway 

Figure 12 shows the RAF protein signaling pathway as described by Sachs et al. [39] consists of 11 proteins (pip3, plcg, pip2, pkc, p38, raf, pka, jnk, mek, erk, and akt), and the edges represent protein interactions. Figure 13 shows the experimental comparison of network reconstruction accuracy on the dataset provided by Marco Grzegorczyk [25]. Compared with CPS-DBN and MIX-DBN, the PR-AUC value of PCCs-ED-DBN is improved significantly. However, in data 1, data 2, and data 3, the PR-AUC values of PCCs-ED-DBN were only $2 \%, 3 \%$, and $4 \%$ higher than that of HMM-DBN, respectively. However, in data 4 , the increase was more obvious, about $8 \%$.
![img-13.jpeg](img-13.jpeg)

Figure 12. RAF pathway.

![img-14.jpeg](img-14.jpeg)

Figure 13. Accuracy comparison of different models on four RAF pathway datasets.

# 4.2.5. Time Overhead 

Compared with HMM-DBN, PCCs-ED-DBN has improved network reconstruction accuracy, convergence, and stability, but this inevitably adds additional time overhead. Table 4 gives a comparison of the additional time overhead during the fourth part of the experiment. The simulation platform is (1) Processor Intel Core i5-9500, CPU 3.0 GHz . (2) Installed memory (RAM) 8 GB. (3) Hard disk: 1 TB. (4) Tool MATLAB R2018b.

Table 4. time overhead comparison between HMM-DBN and PCCs-ED-DBN.


## 5. Conclusions

This paper makes two improvements compared to the HMM-DBN model. First, the changepoint sampling method based on the Euclidean distance of data points proposed in this paper fully mines the prior knowledge between data points. Second, we explore the causal relationship between gene expression data and the Pearson correlation coefficient between genes and apply this relationship to the selection of candidate parent nodes. In addition, the advantages of the PCCs-ED-DBN can be described in detail from the following three aspects.

Network reconstruction accuracy:
On the Saccharomyces cerevisiae dataset, the PR-AUC value of PCC-ED-DBN is about $15 \%$ higher than that of the homogeneous dynamic Bayesian network (HOM-DBN), and compared with other non-homogeneous dynamic Bayesian networks (MIX-DBN,

CPS -DBN, HMM-DBN) increases were $12 \%, 6 \%, 4 \%$. On the four datasets of the RAF pathway, the PR-AUC value of PCC-ED-DBN is more than $10 \%$ higher than that of MIX-DBN and CPS-DBN, but compared with HMM-DBN, in data_1, data_2, data_3, with only $2 \%, 3 \%$, and $4 \%$ improvement, and $8 \%$ improvement in data_4.

Convergence:
On Saccharomyces cerevisiae data and Arabidopsis data, PCCs-ED-DBN has a better convergence effect than HMM-DBN, especially on Arabidopsis data, the improvement of convergence is more obvious. The convergence effect of HMM-DBN with 200,000 MCMC iterations is basically the same as that of PCCs-ED-DBN with 50,000 MCMC iterations. Although PCCs-ED-DBN has more time consumption in a single iteration than HMM-DBN, it can still reduce the time consumption by more than half.

Model stability:
The network reconstruction accuracy (PR-AUC) inferred in multiple independent MCMC simulations is experimentally verified, and the variance of PCCs-ED-DBN is smaller than that of HMM-DBN, which means that the model proposed in this paper is more stable. Finally, the ED-birth move proposed in this paper is applied to the coupled model (Globally Coupled NH-DBNs, EWC NH-DBNs) in the experiment, and the network reconstruction accuracy is also improved, but the improvement effect is not as good as that of the uncoupled model. This is because coupling parameters are added to the coupled model. Through the action of the coupling parameters, the regression parameters in the coupled components can influence each other, thereby adjusting the regression parameters in the components. This means that even if the component assignment deviates from the actual situation, it is still possible to infer regression parameters that are close to the actual situation.

This paper only proposes a method to find the changepoint using Euclidean distance. In future work, I hope to fully exploit the underlying prior knowledge of the data to infer component vectors. The convergence of MCMC sampling is also a topic worthy of study. I hope that the methods I explore in the future can improve the convergence of the model and express the problem of proving convergence mathematically.

Author Contributions: software, Q.Z. writing—original draft preparation, J.Z.; writing—review and editing, C.H. All authors have read and agreed to the published version of the manuscript.
Funding: This work was supported by the following grants: National Natural Science Foundation of China (General Program) 61772321, Natural Science Foundation of Hefei 2021035, Hefei University Graduate Innovation and Entrepreneurship Program (21YCXL25,21YCXL18).
Conflicts of Interest: The authors declare no conflict of interest.
