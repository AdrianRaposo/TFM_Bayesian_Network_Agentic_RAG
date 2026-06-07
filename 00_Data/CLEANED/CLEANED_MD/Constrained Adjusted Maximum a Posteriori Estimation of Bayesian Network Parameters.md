# Article 

## Constrained Adjusted Maximum a Posteriori Estimation of Bayesian Network Parameters

Ruohai $\mathrm{Di}^{1}$, Peng Wang ${ }^{1}$, Chuchao $\mathrm{He}^{1}$ and Zhigao Guo ${ }^{2, *}$


#### Abstract

check for updates Citation: Di, R.; Wang, P.; He, C.; Guo, Z. Constrained Adjusted Maximum a Posteriori Estimation of Bayesian Network Parameters. Entropy 2021, 23, 1283. https:// doi.org/10.3390/e23101283


Received: 11 August 2021
Accepted: 27 September 2021
Published: 30 September 2021

Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## (0)

Copyright: (c) 2021 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 School of Electronics and Information Engineering, Xi'an Technological University, Xi'an 710021, China; diruohai@xatu.edu.cn (R.D.); wang_peng@xatu.edu.cn (P.W.); hechuchao@xatu.edu.cn (C.H.)
2 School of Electronic Engineering and Computer Science, Queen Mary University of London, London E1 4NS, UK

* Correspondence: zhigao.guo@qmul.ac.uk; Tel.: +44-075-0247-6882


#### Abstract

Maximum a posteriori estimation (MAP) with Dirichlet prior has been shown to be effective in improving the parameter learning of Bayesian networks when the available data are insufficient. Given no extra domain knowledge, uniform prior is often considered for regularization. However, when the underlying parameter distribution is non-uniform or skewed, uniform prior does not work well, and a more informative prior is required. In reality, unless the domain experts are extremely unfamiliar with the network, they would be able to provide some reliable knowledge on the studied network. With that knowledge, we can automatically refine informative priors and select reasonable equivalent sample size (ESS). In this paper, considering the parameter constraints that are transformed from the domain knowledge, we propose a Constrained adjusted Maximum a Posteriori (CaMAP) estimation method, which is featured by two novel techniques. First, to draw an informative prior distribution (or prior shape), we present a novel sampling method that can construct the prior distribution from the constraints. Then, to find the optimal ESS (or prior strength), we derive constraints on the ESS from the parameter constraints and select the optimal ESS by crossvalidation. Numerical experiments show that the proposed method is superior to other learning algorithms.


Keywords: graphical models; domain knowledge; prior distribution; equivalent sample size; parameter constraints

## 1. Introduction

A Bayesian network (BN) is a type of graphical model that combines probability and causality theory. A BN becomes a causal model that enables reasoning about intervention under a desired causal assumption [1-3]. BNs have been shown to be powerful tools for addressing statistical prediction and classification problems, and they have been widely applied in many fields, such as geological hazard prediction [4], reliability analysis [5,6], medical diagnosis [7,8], gene analysis [9], fault diagnosis [10], and language recognition [11]. A $\mathrm{BN} B=(G, \Theta)$ includes two components: a graph structure $G$ and a set of parameters $\Theta$. The structure $G$ is a Directed Acyclic Graph (DAG) that consists of nodes (also called vertices) representing random variables, $\left(X_{1}, \ldots, X_{n}\right)$, where $n$ is the number of variables, and directed edges (also called arcs) correspond to the conditional dependence relationships among the variables. Notice that there should be no directed cycles in the graph. When sufficient data are available, the parameters of BN can be precisely and efficiently learnt by statistical approaches such as Maximum Likelihood (ML) estimation. When the sample data set is small, ML estimation often overfits the data and fails to approximate the underlying parameter distribution. To address this problem, Maximum a Posteriori (MAP) estimation has been introduced and shown to be effective in improving parameter learning. Because of the useful properties, i.e., (I) hyper-parameters of the BN model can be taken as equivalent sample observations and (II) experts find it convenient to define the uniformity

of the distribution, the Dirichlet distribution is often preferred for the discrete BN model and therefore added into the estimating process. For the sake of clarity, we define the MAP parameter estimation of node $i$ as $\left(N_{i j k}+\alpha_{i j k}\right) /\left(N_{i j}+\alpha_{i j}\right)$. $N_{i j k}$ is the number of observations in the data set where node $i$ has the $k$ th state and its set of parents has the $j$ th state of its configurations. $N_{i j}$ is the sum of $N_{i j k}$ over all $k$. $\alpha_{i j k}$ and $\alpha_{i j}$ are the equivalent numbers of $N_{i j k}$ and $N_{i j}$ in prior beliefs. For all $k, \alpha_{i j k}$ is also the hyper-parameter values of the Dirichlet prior distribution of the BN parameter $\theta_{i j k}$, and $\alpha_{i j}$ is also the prior strength or equivalent sample size (ESS).

Given no extra domain knowledge, a uniform prior or flat prior is often chosen among all the candidate Dirichlet priors. Based on the uniform prior, MAP scores, such as Bayesian Dirichlet uniform (BDu) [12], Bayesian Dirichlet equivalent uniform (BDeu) [13] and Bayesian Dirichlet sparse (BDs) [14] have been developed and investigated [15,16,17,18,19]. When the underlying parameter distribution is uniform, (I) if the distribution obtained by purely data-driven estimation $N_{i j k} / N_{i j}$ for the parameter $\theta_{i j k}$ is also uniform, the selection of ESS has minor effects on MAP estimation and (II) if the distribution obtained by purely data-driven estimation $N_{i j k} / N_{i j}$ for the parameter $\theta_{i j k}$ is non-uniform, the ESS becomes crucial and the MAP estimation only approximates the underlying distribution by a large ESS value. However, when the underlying parameter distribution is non-uniform, the uniform prior becomes non-informative and, no matter what size the ESS value is, the MAP estimation based on the uniform prior fails to approximate the underlying distribution. Therefore, a well-defined or informative prior is significant.

In practice, unless the domain experts are totally unfamiliar with the studied problem, they would be able to provide some prior information about the underlying parameters [20,21], e.g., parameter A is very likely to be larger than 0.6 , or parameter A is larger than B . In this paper, we assume that the expert opinion or domain knowledge is trustworthy, i.e., the domain knowledge would not be incorporated into the parameter estimation unless the domain experts are confident about their opinions. In fact, this is the assumption that many existing parameter estimation algorithms rely on [22,23,24,25,26]. From the reliable domain knowledge, we can refine informative priors. Then, with an informative prior, we can further select a reasonable ESS. In view of the above considerations, we conclude that, to obtain accurate MAP estimation, informative prior distribution is required to represent the given domain knowledge and thereby select the reasonable ESS to balance the impact of data and prior. Based on such an idea, in this paper, we present a Constrained adjusted Maximum a Posteriori (CaMAP) estimation approach to learn the parameter of a discrete BN model.

This paper is organized as follows. Section 2 briefly introduces related concepts and the studied problem. Section 3 focuses on the illustration of a novel prior elicitation algorithm and a novel optimal ESS selection algorithm. Section 4 presents the experimental results of the proposed method. Finally, we summarize the main findings of the paper and briefly explore the directions for future research in Section 5.

# 2. The Background 

### 2.1. Bayesian Network

A BN is a probabilistic graphical model representing a set of variables and their conditional dependencies via a DAG. Learning a BN includes two parts: structure learning and parameter learning. Structure learning consists of finding the optimal DAG $G$ that identifies the dependencies between variables from the observational data. Parameter learning entails estimating the optimal parameters $\theta$ that quantitatively specify the conditional dependencies between variables. Given the structure, the parameter estimation of a network can be factorized into the independent parameter estimations of individual variables, which means:

$$
\ell(D \mid \theta)=\sum_{i=1}^{n} \sum_{j=1}^{q_{i}} \sum_{k=1}^{r_{i}} N_{i j k} \log \theta_{i j k}
$$

where $\ell(D \mid \theta)$ is the likelihood function of parameters $\theta$ given observational data $D$, and the ML estimation of parameter $\theta_{i j k}$ is

$$
\theta_{i j k}=\frac{N_{i j k}}{N_{i j}}
$$

where $N_{i j}=\sum_{k=1}^{r_{i}} N_{i j k}$.
When the observed data are sufficient, the ML estimation often fits the underlying distributions well. However, when the data are insufficient, additional information such as domain knowledge is required to prevent over-fitting.

# 2.2. Parameter Constraints 

Domain knowledge can be transformed into qualitative parameter constraints. In practice, there are three common parameter constraints [22,27], which are all convex (i.e., the constraints form a convex constrained parameter feasible set that is easy to compute its geometric center, see Section 3.1). The constraints are:
(1) Range constraint: This constraint defines the upper and lower bounds of a parameter, and it is commonly considered in practice.

$$
\theta_{i j k}^{\text {lower }} \leq \theta_{i j k} \leq \theta_{i j k}^{\text {upper }}
$$

(2) Intra-distribution constraint: This constraint describes the comparative relationship between two parameters that refer to the same parent configuration state but different child node states.

$$
\theta_{i j k} \leq \theta_{i j k^{\prime}}, \forall k \neq k^{\prime}
$$

(3) Cross-distribution constraint: This constraint has also been called "order constraint" [23] or "monotonic influence constraint" [24]. It defines the comparative relationship between two parameters that share the same child node state but different parent configuration node states.

$$
\theta_{i j k} \leq \theta_{i j^{\prime} k}, \forall j \neq j^{\prime}
$$

The third type of constraints might be hard to understand. As an example, smoking $(S=1)$ and polluted air $(P A=1)$ are two causes of lung cancer $(L C=1)$ and medical experts agree that smoking is more likely to cause lung cancer. Then, the medical knowledge could be expressed as a cross-distribution constraint, $\mathrm{P}\left(C=1 \mid S=1, P A=0\right)>\mathrm{P}(C=1 \mid S=0, P A=1)$.

### 2.3. Problem Formulation

With observational data and domain knowledge, the parameter learning problem of a discrete BN can be formally defined as:

Input:
$n$ : Number of nodes in the network.
$G$ : Structure with unknown parameters.
$D$ : Set of complete observations for variables.
$\Omega$ : Set of parameter constraints transformed from reliable domain knowledge, $\Omega=$ $\left\{\Omega_{1}, \Omega_{2}, \ldots, \Omega_{n}\right\}$, where $\Omega_{i}$ denotes all the constraints on node $i$.

Task: Find the optimal parameters that approximate the underlying parameter distribution, $\hat{\theta}=\left\{\hat{\theta}_{1}, \ldots, \hat{\theta}_{n}\right\}, \hat{\theta}_{i}=\left\{\hat{\theta}_{i 1}, \ldots, \hat{\theta}_{i q_{i}}\right\}, \hat{\theta}_{i i}=\left\{\hat{\theta}_{i j 1}, \ldots, \hat{\theta}_{i j r_{i}}\right\}$. Here, $q_{i}$ is the number of configuration state values of the parents of the variable $X_{i}$ and $r_{i}$ is the number of state values of the variable $X_{i}$.

### 2.4. Sample Complexity of BN Parameter Learning

Basically, the ML estimation method learns accurate parameters when the acquired data are sufficient. However, when the data are insufficient, ML estimation is often inaccurate. Thus, definition of sample complexity for BN parameter learning helps to

determine whether ML meets the accuracy requirement. With regard to this problem, Dasgupta [28] defined the lower bound of the sample size for BN parameters learning with known structures. Given that a network has $n$ binary variables, and no node has more than $k$ parents, then the sample complexity with confidence $1-\delta$ is lower bounded by

$$
\frac{288 \times n^{2} \times 2^{k}}{\varepsilon^{2}} \times \ln ^{2}\left(1+\frac{3 n}{\varepsilon}\right) \times \ln \left(\frac{1+3 n / \varepsilon}{\varepsilon \delta}\right)
$$

where $\varepsilon$ is the error rate and is often computed as $\varepsilon=n \sigma$, for a small constant $\sigma$.

# 3. The Method 

Among all the parameter learning algorithms, MAP estimation is a learning algorithm that conveniently combines the prior knowledge and observed data. For node $i$, the posteriori estimation of parameters $\theta_{i j}$ can be written as

$$
P\left(\theta_{i j} \mid D\right)=\frac{P\left(D \mid \theta_{i j}\right) P\left(\theta_{i j}\right)}{P(D)} \propto P\left(D \mid \theta_{i j}\right) P\left(\theta_{i j}\right)
$$

where $P\left(\theta_{i j}\right)$ denotes the prior distribution and $P\left(D \mid \theta_{i j}\right)$ equals to $I\left(D \mid \theta_{i j}\right)$. Thus, the MAP estimation of $\hat{\theta}_{i j}$ can be further defined as:

$$
\hat{\theta}_{i j}=\underset{\theta_{i j}}{\operatorname{argmax}} P\left(\theta_{i j} \mid D\right)=\underset{\theta_{i j}}{\operatorname{argmax}} P\left(D \mid \theta_{i j}\right) P\left(\theta_{i j}\right)
$$

Since the parameters $\theta_{i j}$ studied in this paper follows the multinomial distribution and the conjugate prior for the multinomial distribution is Dirichlet distribution, the prior distribution of $\theta_{i j}=\left(\theta_{i j 1}, \ldots, \theta_{i j r_{i}}\right)$ is set to be the Dirichlet distribution, i.e., $\theta_{i j} \sim \operatorname{Dir}\left(\alpha_{i j 1}, \ldots, \alpha_{i j r_{i}}\right)$, where $\left(\alpha_{i j 1}, \ldots, \alpha_{i j r_{i}}\right)$ are the priors equivalent to the observations $\left(N_{i j 1}, \ldots, N_{i j r_{i}}\right)$. As a result, the approximate MAP estimation (see Appendix A) for $\theta_{i j k}$ has the form

$$
\hat{\theta}_{i j k}=\frac{N_{i j k}+\alpha_{i j k}}{N_{i j}+\alpha_{i j}}
$$

where $\alpha_{i j}=\sum_{k=1}^{r_{i}} \alpha_{i j k}$ is the equivalent (or hypothetical) sample size.
Generally, domain experts would find it difficult to provide a specific prior Dirichlet distribution but feel more comfortable to make qualitative statements on unknown parameters. From such qualitative parameter statements or parameter constraints, the prior distribution $\operatorname{Dir}\left(\alpha_{i j 1}, \ldots, \alpha_{i j r_{i}}\right)$ can be further defined as

$$
\operatorname{Dir}\left(\alpha_{i j 1}, \ldots, \alpha_{i j r_{i}}\right)=\operatorname{Dir}\left(\alpha_{i j} * \theta_{i j}^{\text {prior }}\right)
$$

where $\theta_{i j}^{\text {prior }}=\left(\theta_{i j 1}^{\text {prior }}, \theta_{i j 2}^{\text {prior }}, \ldots, \theta_{i j r_{i}}^{\text {prior }}\right)$ is the prior hyper-parameter vector of the prior distribution that represents the domain knowledge and can be sampled from the parameter constraints. Finally, the MAP estimation for $\theta_{i j k}$ can be expressed as

$$
\hat{\theta}_{i j k}=\frac{N_{i j k}+\alpha_{i j} \theta_{i j k}^{\text {prior }}}{N_{i j}+\alpha_{i j}}
$$

As the parameter constraints are incorporated into the MAP estimation, we define the above estimation as Constrained adjusted Maximum a Posteriori (CaMAP) estimation. In the following sections, we will introduce the elicitation of the prior parameter $\theta_{i j}^{\text {prior }}$ and the selection of the optimal $\operatorname{ESS} \alpha_{i j}$.

# 3.1. Prior Elicitation 

Before defining the optimal ESS $\alpha_{i j}$, the prior parameter $\theta_{i j}^{\text {prior }}$ is required, which could be elicited from the parameter constraints in a sampling manner. In this paper, we design a sampling method that applies to all types of convex constraints. Specifically, in the sampling method,
(1) First, we search for the optimal parameters of the following model:

$$
\begin{gathered}
\text { minimize } C \\
\text { subject to } \left.\Omega\left(\theta_{i}\right)\right.
\end{gathered}
$$

where $C$ is a random constant and $\Omega\left(\theta_{i}\right)$ represents all the parameter constraints on node $i$. The constrained model is simple and could be efficiently solved. Note that even though the objective function is a constant, the solutions of the constrained model could vary each time. In fact, any parameters satisfying the given parameter constraints are solutions of the constrained model. Therefore, through iteratively solving the constrained model, we collect the parameters that cover the feasible parameter region constrained by the parameter constraints.
(2) Then, the first step is repeated (In this paper, we set the repetition times at 100 and the sampling code is available at: https://uk.mathworks.com/matlabcentral/fileexchange/ 34208-uniform-distribution-over-a-convex-polytope (accessed on 26 September 2021)) to collect sufficient sampled parameters that cover the constrained parameter space. To make sure that the sampled parameters are uniformly distributed over the constrained parameter space, for each sampling step, we add an extra constraint

$$
\left\|\theta_{i}^{t+1}-\theta_{i}^{t}\right\|_{2} \geq \tau
$$

where $\tau$ is a small value (e.g., 0.1 ), $\theta_{i}^{t}$ represents the sampled parameters at step $t$, and $\theta_{i}^{t+1}$ represents the sampled parameters at step $t+1$.
(3) Finally, we average over all the sampled parameters and set the mean values as the prior $\theta_{i}^{\text {prior }}=\left\{\theta_{i j}^{\text {prior }}\right\}, j=\left\{1, \ldots q_{i}\right\}$, where $\theta_{i j}^{\text {prior }}=\left(\theta_{i j 1}^{\text {prior }}, \ldots, \theta_{i j r_{i}}^{\text {prior }}\right)$.

### 3.2. ESS Value Selection

Although the sampled prior $\theta_{i}^{\text {prior }}$ guarantees satisfying all the parameter constraints, the overall estimation (Equation (10)) may violate the constraints if ESS $\alpha_{i j}$ is not reasonably defined. For example, for binary variables, $\{L C=$ Lung Cancer, $S=$ Smoking, $P A=$ Pollution Air $\}$, smoking and pollution air are shown to cause lung cancer. Parameter $\theta_{142}$ represents the probability that the value of variable $L C$ is true given that the values of variables $S$ and $P A$ are both true. In this example, $\theta_{142}$ is the probability of having lung cancer $(L C=1)$ given that the patients consistently smoke $(S=1)$ and work in polluted air $(P A=1)$. The medical experts assert that $\theta_{142}$ lies in the interval, $[0.6,1.0]$, which is also the parameter constraint. Now, the elicited prior $\theta_{142}^{\text {prior }}$ is 0.80 , which satisfies the parameter constraint, and the purely data-driven estimation (also ML estimation) is $N_{142} / N_{14}=1 / 7$. Then, with a small ESS, such as 5, the estimation (Equation (11)) is computed as follows:

$$
\hat{\theta}_{142}=\frac{1+5 * 0.80}{7+5}=0.42
$$

Obviously, the above estimation does not satisfy the constraint, $\theta_{142} \in[0.6,1.0]$. In fact, to make sure that the estimation does not violate the constraint, the optimal ESS should not be less than 16, which could be inferred from the parameter constraints. Therefore, given the elicited prior and observation counting, to guarantee that the overall CaMAP estimation satisfies all the parameter constraints, the optimal ESS should satisfy certain constraints.

From each type of constraint imposed on the parameters, ESS constraints could be derived as follows:

(1) To satisfy the range constraint, the CaMAP estimation in Equation (11) should satisfy

$$
\theta_{i j k}^{\text {lower }} \leq \frac{N_{i j k}+\alpha_{i j} \theta_{i j k}^{\text {prior }}}{N_{i j}+\alpha_{i j}} \leq \theta_{i j k}^{\text {upper }}
$$

which implies

$$
\begin{aligned}
& \alpha_{i j} \geq \frac{N_{i j} \theta_{i j k}^{\text {lower }}-N_{i j k}}{\theta_{i j k}^{\text {prior }}-\theta_{i j k}^{\text {lower }}} \\
& \alpha_{i j} \geq \frac{N_{i j} \theta_{i j k}^{\text {upper }}-N_{i j k}}{\theta_{i j k}^{\text {prior }}-\theta_{i j k}^{\text {upper }}}
\end{aligned}
$$

(2) To satisfy the intra-distribution constraint, the CaMAP estimation should satisfy

$$
\frac{N_{i j k_{1}}+\alpha_{i j} \theta_{i j k_{1}}^{\text {prior }}}{N_{i j}+\alpha_{i j}} \leq \frac{N_{i j k_{2}}+\alpha_{i j} \theta_{i j k_{2}}^{\text {prior }}}{N_{i j}+\alpha_{i j}}
$$

which implies

$$
\alpha_{i j} \geq \frac{N_{i j k_{2}}-N_{i j k_{1}}}{\theta_{i j k_{1}}^{\text {prior }}-\theta_{i j k_{2}}^{\text {prior }}}
$$

(3) To satisfy the cross-distribution constraint, the CaMAP estimation should satisfy

$$
\frac{N_{i j_{1} k}+\alpha_{i j_{1}} \theta_{i j_{1} k}^{\text {prior }}}{N_{i j_{1}}+\alpha_{i j_{1}}} \leq \frac{N_{i j_{2} k}+\alpha_{i j_{1}} \theta_{i j_{2} k}^{\text {prior }}}{N_{i j_{2}}+\alpha_{i j_{2}}}
$$

where $\alpha_{i j_{1}}$ and $\alpha_{i j_{2}}$ represent the ESS values of the distributions under the cross-distribution constraint. Thus, we have

$$
\alpha_{i j_{1}} \alpha_{i j_{2}}\left(\theta_{i j_{1} k}^{\text {prior }}-\theta_{i j_{2} k}^{\text {prior }}\right)+\alpha_{i j_{1}}\left(N_{i j_{2}} \theta_{i j_{1} k}^{\text {prior }}-N_{i j_{2} k}\right)+\alpha_{i j_{2}}\left(N_{i j_{1} k}-N_{i j_{1}} \theta_{i j_{2} k}^{\text {prior }}\right)
$$

In this paper, we set $\alpha_{i j_{1}}=\alpha_{i j_{2}}$ and thus we have

$$
\alpha_{i j_{1}}^{2}\left(\theta_{i j_{1} k}^{\text {prior }}-\theta_{i j_{2} k}^{\text {prior }}\right)+\alpha_{i j_{1}}\left(N_{i j_{1} k}-N_{i j_{2} k}+N_{i j_{2}} \theta_{i j_{1} k}^{\text {prior }}-N_{i j_{1}} \theta_{i j_{2} k}^{\text {prior }}\right)+N_{i j_{2}} N_{i j_{1} k}-N_{i j_{1}} N_{i j_{2} k} \leq 0
$$

From the above inequality, constraints on the ESS values $\alpha_{i j_{1}}$ and $\alpha_{i j_{2}}$ could be derived.
Furthermore, in this paper, for each node, we define two classes of ESSs: "global" and "local" ESS. "Global" ESS refers to the equivalent sample size imposed on all parameter distributions of the given node, such as node $i$, while "local" ESS refers to the equivalent sample size working on parameter distribution that refers to a specific parent configuration state. For example, in Figure 1, for node $i, \alpha_{i}$ is the "global" ESS, while $\left(\alpha_{i 1}, \ldots, \alpha_{i q_{i}}\right)$ are the "local" ESSs.

In general, with the elicited prior, observational data and parameter constraints, for node $i$, the optimal ESSs could be determined by the following procedure:
(1) First, from the elicited prior and observational data, the optimal "global" ESS $\alpha_{i}$ could be determined by cross-validation [29]. In the cross-validation, each candidate ESS (In this paper, the candidate ESS varies from 1 to 50) is evaluated based on the likelihood of posteriori estimation in Equation (11).
(2) Then, based on the parameter constraints, we can derive the constraints on each "local" ESS $\alpha_{i j}$.
(3) Finally, for "local" ESS $\alpha_{i j}$, (I) If there is no constraint imposed on $\alpha_{i j}$, then we set $\alpha_{i j}=\alpha_{i}$. (II) If there are constraints imposed on $\alpha_{i j}$ and meanwhile the "global" ESS $\alpha_{i}$ satisfies the constraints, then, we set $\alpha_{i j}=\alpha_{i} ;$ if not, $\alpha_{i j}$ is determined by further crossvalidation using data, prior and ESS constraints. Note that in the process of validation, the

initial candidate ESS value of $\alpha_{i j}$ is set to be the lower bound value of the range defined by its constraints.
![img-0.jpeg](img-0.jpeg)

Figure 1. Illustration of "global" and "local" ESS.
The pseudo-code of the proposed CaMAP algorithm could be summarized as following Algorithm 1:

```
Algorithm 1 Constrained adjusted Maximum a Posteriori (CaMAP) algorithm
    Input: \(n, G, D, \Omega\)
    Output: \(\hat{\theta}=\left\{\hat{\theta}_{i j k}\right\}, i=\{1, \ldots, n\}, j=\left\{1, \ldots, q_{i}\right\}, k=\left\{1, \ldots r_{i}\right\}\).
    1 for (i<=n) do // Learn the parameters of each individual node
    \(2 \quad \alpha_{i} \leftarrow\) Determine the "global" ESS by the cross-validation
    \(3 \quad \theta_{i j}^{\text {prior }} \leftarrow\) Elicit the prior parameter from the parameter constraints
    \(4 \quad C\left(\alpha_{i j}\right) \leftarrow\) Derive the constraints on the "local" ESS
    \(5 \quad \alpha_{i j} \leftarrow\) Determine the "local" ESS by the judgment rules or cross-validation
    \(6 \quad \hat{\theta}_{i j k} \leftarrow\) Complete the parameter estimation by Eq. (11)
    7 end
```


# 3.3. Numerical Illustration of CaMAP Method 

To illustrate the principle of the proposed method, we demonstrate the parameter learning of the BN shown in Figure 2, which is extracted from the brain tumor BN [23]. Nodes in the network have meanings as below. Specifically, the network indicates that the presence of brain tumor and the increased level of serum calcium may cause coma.

- $C \rightarrow$ Coma
- $B T \rightarrow$ Brain Tumour
- IS $\rightarrow$ Increased level of Serum calcium

![img-1.jpeg](img-1.jpeg)

Figure 2. Brain tumor BN.
(1) First, we assume that a small data set of 20 patients is available. From the data, the following counting are observed:

$$
\begin{aligned}
& N(C=0, B T=0, I S=0)=0, N(C=0, B T=0, I S=1)=1 \\
& N(C=0, B T=1, I S=0)=3, N(C=0, B T=1, I S=1)=9 \\
& N(C=1, B T=0, I S=0)=3, N(C=1, B T=0, I S=1)=0 \\
& N(C=1, B T=1, I S=0)=4, N(C=1, B T=1, I S=1)=0
\end{aligned}
$$

Furthermore, we acquire the following medical knowledge from the medical experts: a brain tumor as well as an increased level of serum calcium are likely to cause the patient to fall into a coma in due course. From this medical knowledge, we generate the following parameter constraints:

$$
\begin{aligned}
& P(C=1 \mid B T=0, I S=1) \geq P(C=1 \mid B T=0, I S=0) \\
& P(C=1 \mid B T=1, I S=0) \geq P(C=1 \mid B T=0, I S=0) \\
& P(C=1 \mid B T=1, I S=1) \geq P(C=1 \mid B T=0, I S=0) \\
& P(C=1 \mid B T=1, I S=1) \geq P(C=1 \mid B T=0, I S=1) \\
& P(C=1 \mid B T=1, I S=1) \geq P(C=1 \mid B T=1, I S=0)
\end{aligned}
$$

(2) Then, based on the parameter constraints, we elicit the following priors using the proposed prior elicitation algorithm (Section 3.1):

$$
\begin{aligned}
& P^{\prime}(C=0 \mid B T=0, I S=0)=0.99, P^{\prime}(C=0 \mid B T=0, I S=1)=0.56 \\
& P^{\prime}(C=0 \mid B T=1, I S=0)=0.60, P^{\prime}(C=0 \mid B T=1, I S=1)=0.05 \\
& P^{\prime}(C=1 \mid B T=0, I S=0)=0.01, P^{\prime}(C=1 \mid B T=0, I S=1)=0.44 \\
& P^{\prime}(C=1 \mid B T=1, I S=0)=0.40, P^{\prime}(C=1 \mid B T=1, I S=1)=0.95
\end{aligned}
$$

(3) Furthermore, from the parameter constraints, we derive the constraints on the "local" ESSs:

$$
\begin{aligned}
& \alpha(B T=0, I S=0) \geq 5.49, \alpha(B T=0, I S=1) \geq 5.92 \\
& \alpha(B T=1, I S=0) \geq 9.01, \alpha(B T=1, I S=1) \geq 9.01
\end{aligned}
$$

(4) Next, for node $C$, the optimal "global" ESS is cross-validated to be 3. As the "global" ESS does not satisfy any of the ESS constraints, the "local" ESSs would not be equal to the "global" ESS and should be further validated. Based on the prior, data and ESS constraints, the optimal "local" ESSs are cross-validated to be as follows:

$$
\begin{gathered}
\alpha(B T=0, I S=0)=50, \alpha(B T=0, I S=1)=6 \\
\alpha(B T=1, I S=0)=50, \alpha(B T=1, I S=1)=50
\end{gathered}
$$

(5) Finally, with the elicited priors and optimal ESSs, the CaMAP estimation are computed as follows:

$$
\begin{aligned}
& P(C=0 \mid B T=0, I S=0)=\frac{0+50+0.99}{3+50}=0.93 \\
& P(C=0 \mid B T=0, I S=1)=\frac{1+6 \times 0.56}{3+6}=0.62 \\
& P(C=0 \mid B T=1, I S=0)=\frac{3+50+0.60}{7+50}=0.58 \\
& P(C=0 \mid B T=1, I S=1)=\frac{9+50+0.05}{9+50}=0.19 \\
& P(C=1 \mid B T=0, I S=0)=\frac{3+50+0.01}{3+50}=0.07 \\
& P(C=1 \mid B T=0, I S=1)=\frac{0+6 \times 0.44}{1+6}=0.38 \\
& P(C=1 \mid B T=1, I S=0)=\frac{4+50+0.40}{7+50}=0.42 \\
& P(C=1 \mid B T=1, I S=1)=\frac{0+50+0.95}{9+50}=0.81
\end{aligned}
$$

# 4. The Experiments 

We conducted experiments to investigate the performance of the proposed CaMAP method in terms of learning accuracy, under different sample sizes and constraint sizes. In the experiments, we used the networks from [16,17], shown in Figures 3-7. The true parameter distributions in these networks show different uniformities, varying from strongly skewed to strongly uniform distributions. As the true parameters were set or known in advance, the learnt parameters were evaluated by the Kullback-Leibler (KL) divergence [30], which indicates the divergence between the learnt parameters or estimated distribution and the true parameters or underlying distribution. The proposed method was evaluated against the following learning algorithms: ME [31], ML [32], MAP [13], CME [26,33], and CML [24,34] (The code of all the six tested algorithms can be found at https://github.com/ZHIGAO-GUO/CaMAP (accessed on 26 September 2021)). The full names of the tested algorithms are listed as follows:

- ME : maximum entropy
- ML : maximum likelihood
- MAP : maximum a posteriori
- CME : constrained maximum entropy
- CML : constrained maximum likelihood
- CaMAP : constrained adjusted maximum a posteriori
![img-2.jpeg](img-2.jpeg)

Figure 3. Strongly skewed distribution.

![img-3.jpeg](img-3.jpeg)

Figure 4. Skewed distribution.
![img-4.jpeg](img-4.jpeg)

Figure 5. Uniform distribution.
![img-5.jpeg](img-5.jpeg)

Figure 6. Strongly uniform distribution.

![img-6.jpeg](img-6.jpeg)

Figure 7. Combined skewed and uniform distribution.
Notice that, (I) in the MAP method, we used a uniform (or flat) prior, which means, $\theta_{i j k}^{\text {prior }}$ in Equation (11) was set to be $1 / r_{i}$ and ESS value is 1 , and (II) in the CaMAP method, we set the maximum candidate ESS to be 50, which is a sufficient number for all networks.

# 4.1. Learning with Different Sample Sizes 

First, we examined the learning performance of all algorithms under different sample sizes. Our experiments were carried out under the following settings: (1) The sample sizes were set to be $10,20,30,40$, and 50 , respectively. (2) The parameter constraints were randomly generated from the true parameters of the tested networks, with the maximum number of constraints for each node at 3 . Specifically, the parameter constraints are generated using the following rules: (1) Range constraints are generated as $\left[\theta_{i j k}^{\text {lower }}, \theta_{i j k}^{\text {upper }}\right]$, where $\theta_{i j k}^{\text {lower }}$ is equal to be $\max \left(0, \theta_{i j k}^{*}-\tau_{1}\right)$ and $\theta_{i j k}^{\text {upper }}$ is equal to be $\min \left(1, \theta_{i j k}^{*}+\tau_{2}\right)$, where $\theta_{i j k}^{*}$ represents the true parameter, and $\tau_{1}$ and $\tau_{2}$ are two random values around 0.2. (2) Inequality constraints are generated as $\theta_{i j_{1} k_{1}} \geq \theta_{i j_{2} k_{2}}$ if $\left(\theta_{i j_{1} k_{1}}-\theta_{i j_{2} k_{2}}\right) \geq 0.2$. Therefore, when $j_{1}=j_{2}$ and $k_{1} \neq k_{2}$, the constraint becomes the intra-distribution constraint, while the constraint becomes the cross-distribution constraint when $j_{1} \neq j_{2}$ and $k_{1}=k_{2}$.

We performed 100 repeated experiments. The average KL divergence values of different algorithms on different networks under different sample sizes are summarized in Table 1 with the best results highlighted in bold.

From the experimental results, we draw the following conclusions: (1) With increasing data, the performance of all algorithms improved by different levels. (2) In almost all cases, CaMAP outperformed the other learning algorithms. However, when the available data are extremely insufficient, e.g., 10, the CaMAP was inferior to the MAP method. The explanation might be that the insufficiency of data impacts the cross-validation of ESS values. Therefore, the optimal ESS turns out to be extreme, either small or large, and fails to balance data and prior (see the 2nd future study in Discussion and Conclusions section).

### 4.2. Learning with Different Constraint Sizes

Next, we further explored the learning performance of different learning algorithms under different constraint sizes. The experiments were conducted under the following settings: (1) The data set size for all the tested networks was set to be 20, which is a small number for all networks. (2) Parameter constraints were generated from the true parameters of the networks and the maximum number of constraints for each node was set to be 3. The parameters were learnt from a fixed data set but an increasing number of parameter constraints that were randomly chosen from all generated constraints. The constraint sparsity varied from $0 \%$ to $100 \%$. For each setting, we performed 100 repeated experiments.

The average KL divergence values of different algorithms on different networks under different constraint sizes are summarized in Table 2.

Table 1. Parameter learning under different sample sizes.


From the experimental results, we draw the following conclusions: (1) For the algorithms that did not use constraints, such as ML, ME, and MAP, changing the constraint size did not impact their performance. However, for the algorithms that have been incorporated constraints, such as CML, CME, and CaMAP, an increase in constraints affected their performances to a certain degree depending on the number of incorporated constraints. (2) In most cases, CaMAP outperformed the other parameter learning algorithms, except for MAP, when no parameter constraints were incorporated into the learning. In fact, when no parameter constraints were available, CaMAP method was slightly inferior to the MAP estimation with uniform prior. The explanation might be as follows: when the parameter constraints are not available, constraints on ESS values could not be deduced. Therefore, ESS values in CaMAP estimation are the same at those in MAP estimation. Then, the difference between the CaMAP and MAP estimation lies in the prior, $\theta_{i}^{\text {prior }}$. However, unlike uniform prior in MAP estimation, prior in the CaMAP method is elicited using a sampling method. For the sampling methods, it is hard to achieve completely uniform sampling unless the sampling size is very large (see the $1^{\text {st }}$ future study in the Discussion and Conclusions section).

Table 2. Parameter learning under different constraint sizes.


# 5. Discussion and Conclusions 

For MAP estimation in BN parameter learning, informative prior distribution and reasonable ESS values are two crucial factors that impact the learning performance. Empirically, a uniform prior is preferred and ESS is further cross-validated according to the uniform prior. However, when the underlying parameter distribution is non-uniform or skewed, MAP estimation with a uniform prior does not fit the underling parameter distribution well, and, in that case, an informative prior is required. In fact, reliable qualitative domain knowledge has been proved to be useful and can be used for eliciting informative priors and selecting the reasonable ESS. In this paper, we proposed a CaMAP estimation method. The proposed method automatically elicits the prior distribution from the parameter constraints that are transformed from the domain knowledge. Besides, constraints on ESS values are derived from the parameter constraints. Then, the optimal ESS, including "global" and "local" ESS, are further chosen from the ranges derived from the ESS constraints by cross-validation. Our experiments demonstrated that the proposed method outperformed most of the mainstream parameter learning algorithms. In future study:
(1) A more effective prior elicitation approach is desired. Compared to the samplingbased methods, geometric constraint-solving methods would be more robust and could elicit more informative priors.
(2) A more reasonable ESS selection method is preferred. For the cross-validation method, when the available data are extremely insufficient or less informative, the optimal ESS tends to maximize the likelihood of data and makes the CaMAP estimation fail to approach the underling parameter distribution. In fact, data bootstrapping guided by the parameter constraints may extend the data and make the data more informative and thus improve the ESS selection.

Author Contributions: Conceptualization, R.D. and C.H.; methodology, R.D.; formal investigation, C.H.; writing—original draft preparation, R.D.; writing—review and editing, R.D., P.W.; supervision, Z.G.; funding acquisition, R.D. All authors have read and agreed to the published version of the manuscript.

Funding: This research was funded by the National Key Laboratory fund and Nature Science Foundation of Shanxi, the grant numbers are CEMEE2020Z0202B, 2020JQ-816,20JK0608.

Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Data used in the experiments are synthetically generated from the networks (refer to Figures 3-7) and could be generated by the open-source code provided in the paper.

Conflicts of Interest: The authors declare no conflict of interest.

# Appendix A 

The approximate MAP estimation for $\theta_{i j k}$ has the form

$$
\hat{\theta}_{i j k}=\frac{N_{i j k}+\alpha_{i j k}}{N_{i j}+\alpha_{i j}}
$$

Proof. The posterior estimation of parameter $\theta_{i j}$, where $\theta_{i j}=\left(\theta_{i j 1}, \ldots, \theta_{i j r_{i}}\right)$ and $r_{i}$ is the number of states of node $i$, is

$$
P\left(\theta_{i j} \mid D\right)=\frac{P\left(D \mid \theta_{i j}\right) P\left(\theta_{i j}\right)}{P(D)} \propto P\left(D \mid \theta_{i j}\right) P\left(\theta_{i j}\right)
$$

where $P\left(\theta_{i j}\right)$ is the prior and $P\left(D \mid \theta_{i j}\right)$ is the likelihood. Thus, the maximum a posteriori estimation of $\theta_{i j}$ is

$$
\hat{\theta}_{i j}=\underset{\theta_{i j}}{\operatorname{argmax}} P\left(\theta_{i j} \mid D\right)=\underset{\theta_{i j}}{\operatorname{argmax}} P\left(D \mid \theta_{i j}\right) P\left(\theta_{i j}\right)
$$

As it is more convenient to deal $\log$, the MAP estimation of $\theta_{i j}$ can be expressed as

$$
\hat{\theta}_{i j}=\underset{\theta_{i j}}{\operatorname{argmax}} \log P\left(\theta_{i j} \mid D\right)=\underset{\theta_{i j}}{\operatorname{argmax}}\left(\log \left(P\left(D \mid \theta_{i j}\right)\right)+\log \left(P\left(\theta_{i j}\right)\right)\right.
$$

Since the parameters $\theta_{i j}$ studied in this paper follows the multinomial distribution and the conjugate prior for the multinomial distribution is Dirichlet distribution. The above equation could be further written as

$$
\hat{\theta}_{i j}=\underset{\theta_{i j}}{\operatorname{argmax}} \log P\left(\theta_{i j} \mid D\right)=\underset{\theta_{i j}}{\operatorname{argmax}}\left(\sum_{k=1}^{r_{i}} N_{i j k} \log \theta_{i j k}+\sum_{k=1}^{r_{i}}\left(\alpha_{i j k}-1\right) \log \theta_{i j k}\right)
$$

where $\operatorname{Dir}\left(\alpha_{i j 1}, \alpha_{i j 2}, \ldots, \alpha_{i j r_{i}}\right)$ is the prior distribution. Then, the maximum a posteriori estimation of $\theta_{i j k}$ is

$$
\hat{\theta}_{i j k}=\frac{N_{i j k}+\alpha_{i j k}-1}{N_{i j}+\alpha_{i j}-r_{i}}
$$

However, the above estimation only holds for $\alpha_{i j}>1$ and it is only one choice of point estimation since the true $\theta_{i j k}$ is unknown. Instead of exact MAP estimation, the approximate estimation

$$
\hat{\theta}_{i j k}=\frac{N_{i j k}+\alpha_{i j k}}{N_{i j}+\alpha_{i j}}
$$

holds for any choice of prior. Therefore, in this paper, we adopt the above approximate estimation.
