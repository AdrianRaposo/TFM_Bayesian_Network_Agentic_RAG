# HHS Public Access 

Author manuscript<br>Commun Stat Simul Comput. Author manuscript; available in PMC 2019 March 25.

Published in final edited form as:
Commun Stat Simul Comput. 2017 ; 46(7): 5070-5084. doi:10.1080/03610918.2016.1143103.

## An efficient Bayesian approach for Gaussian Bayesian network structure learning

Shengtong Han, Hongmei Zhang, Ramin Homayouni, and Wilfried Karmaus<br>School of Public Health, Bioinformatics Program and Center for Translational Informatics, University of Memphis Memphis, TN hzhang6@memphis.edu


#### Abstract

This article proposes a Bayesian computing algorithm to infer Gaussian directed acyclic graphs (DAG's). It has the ability of escaping local modes and maintaining adequate computing speed compared to existing methods. Simulations demonstrated that the proposed algorithm has low false positives and false negatives in comparison to an algorithm applied to DAG's. We applied the algorithm to an epigenetic data set to infer DAG's for smokers and non-smokers.


## Keywords

DNA methylation; Gaussian DAG; MCMC

## 1 Introduction

There is an increasing attention on learning Directed Acyclic Graphs (DAG's), or Bayesian networks, which have an appealing property of encoding conditional independence relations by graphs explicitly. By definition, a graph is a DAG if all the links (edges) are directed, but there are no directed loops (circles). Conditional independence means each variable in the graph is conditionally independent of its non-descendants given its parent set. Two DAG's are Markov equivalent if they represent the same set of conditional independence. To characterize the class of DAG's with the same set of conditional independence, a partially directed acyclic graph (CPDAG) is introduced, which may be with both directed links and undirected links. One can refer to Andersson et al. (1997); Chickering (2002) for details. It still remains a challenge for inferring Bayesian networks due to network complexity and the existence of multiple local maximums. A number of algorithms are devoted to estimate Bayesian networks, including greedy local search (Heckerman and Chickering, 1995), Optimal Reinsertion search (Moore and keen Wong, 2003), Max-Min Hill-Climbing (Tsamardinos et al., 2006), genetic algorithm (Larranaga et al., 1996; Lee et al., 2010), dynamic programming (Eaton, 2007), branch-and-bound algorithm (de Campos et al., 2011), Markov Chain Monte Carlo (MCMC) approaches (Madigan et al., 1995, 1996; Giudici and Green, 1999; Friedman and Koller, 2003; Ellis and Wong, 2008; Zhou, 2011; Han et al., 2014). The PC algorithm, proposed by Spirtes et al. (2000) becomes very popular to infer DAG's by detecting the conditional independence, then orienting the links as long as there are no directed circles in the resulting network. It is worthy noting that the PC algorithm finds completed partially directed acyclic graphs, not single DAGs. Subsequently related work include Kalisch et al. (2007); Kalisch and Bhlmann (2008); Harris and Drton (2013).

Among these, Friedman and Koller (2003) made an important improvement in inferring Bayesian networks by introducing graph order MCMC and previous work include Bouckaert (1994). Assuming the order is known, Shojaie and Michailidis (2010) proposed an efficient penalized likelihood method for estimation of adjacent matrix of directed graphs; Altomare et al. (2013) proposed an objective method for DAG inference. Even with order MCMC, it is sill difficult to capture the underlying distributions because of the common problem of multiple local maximums, as experimentally demonstrated by Ellis and Wong (2008). To improve sampling efficiency, Ellis and Wong (2008) suggests the use of advanced sampling technique-single queue Equi-Energy sampler, a variant of the Equi-Energy sampler proposed by Kou et al. (2006) to obtain more reliable posterior samples.

However, most efforts, although stated applicable to continuous variables, focus on discrete networks in which each node is a categorical variable such as in the work by Ellis and Wong (2008); Liang and Zhang (2009); Zhou (2011); Balov (2013), and among others. In biomedical studies, to utilize these methods, continuous variables have to be transformed into discrete variables. This discretization manipulation may induce the risk of losing some meaningful information, for instance the dependence relationships among variables. Furthermore, some data sets are continuous in nature and discretizing them may practically be meaningless. In this work, these limitations motivate us to investigate the structure of Bayesian networks from continuous data.

Section 2 presents the model, including an introduction to Bayesian network, priors and posteriors for parameters. The posterior computing, e.g., the proposed algorithm, is given in section 3. Simulation studies and a real data application are included in section 4. It ends with summary and discussion in section 5.

# 2 The Model 

Bayesian network is a directed acyclic graph which can be characterized by two components, a set of nodes $\boldsymbol{X}$ (random variables), and a collection of directed links, $\boldsymbol{E}$. Throughout we assume there are $n$ nodes, $\boldsymbol{X}=\left\{X_{1}, X_{2}, \cdots, X_{n}\right\}$, in the network, and the data are fully observed without any missing values. The joint distribution of $\boldsymbol{X}$ satisfies, by Markov property

$$
P(\boldsymbol{X})=\prod_{i=1}^{n} P\left(X_{i} \mid P a\left(X_{i}\right)\right)
$$

where $P a\left(X_{i}\right) \subset \boldsymbol{X} \backslash\left\{X_{i}\right\}$ is the parent set of $X_{i}$. We assume each $X_{i}$ is a Gaussian random variable with its mean as a function of its parents, i.e., $X_{i}=\beta_{i 0}+\sum_{j: X_{j} \in P a\left(X_{i}\right)} \beta_{i j} X_{j}+\epsilon_{i}, i=$ $1,2, \cdots, n$. Parameters $\beta_{i j}$ are coefficients and ${ }_{i}$ is assumed to be Gaussian random noise with mean 0 and variance $\sigma_{i}^{2}$. We have

$$
X_{i} \mid P a\left(X_{i}\right)-N\left(\mu_{X_{i}} \sigma_{i}^{2}\right)
$$

where $\mu_{X_{i}}=\beta_{i 0}+\sum_{j: X_{j} \in P a\left(X_{i}\right)} \beta_{i j} X_{j}$. Let $\theta_{i}$ be the set of parameters associated with node $X_{i}$, i.e., $\theta_{i}=\left\{\beta_{i 0}, \beta_{i 1}, \beta_{i 2}, \cdots, \beta_{i T_{i}}, \sigma_{i}^{2}\right\}$ and all parameters for the network are denoted by $\theta=\bigcup_{i=1}^{n} \theta_{i}$, where $T_{i}=|P a\left(X_{i}\right)|$, the number of parents for node $X_{i}$. In the following, we assume $T_{i} \leq 4$, i.e., the maximum number of parents is no more than 4 . The assumption of boundness on the number of parents is quite common and unavoidable in Bayesian network structure learning since graphs with overwhelmingly large number of links are usually preferred, resulting in over-fitting problem (Ellis and Wong, 2008; Zhou, 2011; Fu and Zhou, 2013).

Suppose there are M independent observations for each variable in the network, $x_{i h}, i=$ $1,2, \cdots, n ; h=1,2, \cdots, M$. Let $\mathcal{X}=\left\{x_{i h}, i=1,2, \cdots, n ; h=1,2, \cdots, M\right\}$. Given the graph $\mathscr{G}$ and the parameter associated with this graph, $\theta^{\mathscr{G}}\left(\theta^{\mathscr{G}}\right.$ has the same definition as $\theta$ but is specific to graph $\mathscr{G})$, we have

$$
P\left(\mathcal{X} \mid \mathscr{G}, \theta^{\mathscr{G}}\right)=\prod_{h=1}^{M} \prod_{i=1}^{n} P\left(x_{i h} \mid P a\left(x_{i h}\right), \theta_{i}^{\mathscr{G}}\right)
$$

# Prior distributions 

To infer the parameter $\theta^{\mathscr{G}}$, we use the fully Bayesian approach. We choose inverse gamma for the prior distribution of $\sigma_{i}^{2}$, i.e., $\sigma_{i}^{2} \mid \delta_{i}, \Psi_{i} \sim \operatorname{Inv}-\operatorname{Gamma}\left(\delta_{i}, \Psi_{i}\right)$, with $\delta_{i}, \Psi_{i}$ known and set the conditional priors for $\beta_{i}=\left(\beta_{i 0}, \beta_{i 1}, \beta_{i 2}, \cdots, \beta_{i T i}\right)^{T}$ to be of the form $\beta_{i i} \sim$ $M V N\left(0, \sigma_{i}^{2}\left(X_{i}^{P a^{T}} X_{i}^{P a}\right)^{-1}\right)$, where " $M V N$ " denotes multivariate normal distribution, $X_{i}^{P a}$ is an $M \times\left(T_{i}+1\right)$ matrix and represents the observational data for the parents of node $X_{i}$. This prior allows us to obtain the posterior in closed form in (1).

The prior distribution over structures is commonly chosen to be uniform distribution (Heckerman, 1999; Friedman and Koller, 2003), and the sparse network is usually preferred. In our approach, similar to Ellis and Wong (2008), we consider structure priors as a function of the number of links as $P(\mathscr{G}) \propto \gamma^{\sum_{i=1}^{n} \mid P a^{\mathscr{G}}\left(X_{i}\right)}$, for some $0<\gamma<1$.

## Posterior distributions

The joint posterior distribution of $\left(\theta^{\mathscr{G}}, \mathscr{G}\right)$ is

$$
P\left(\theta^{G}, \mathscr{G} \mid \mathcal{X}\right) \propto P\left(\theta^{\mathscr{G}}, \mathscr{G}\right) \times P\left(\mathcal{X} \mid \theta^{\mathscr{G}}, \mathscr{G}\right)
$$

By integrating out the parameters, the marginal posterior distribution of $\mathscr{G}$ is

where $X_{i}^{P a}$ is an $M \times\left(T_{i}+1\right)$ matrix with the $h$ th row $\left(1, s_{h 1}^{(i)}, \cdots, s_{h T_{i}}^{(i)}\right), \mathrm{h}=1,2, \cdots, M, X_{i}=$ $\left(x_{i 1}, x_{i 2}, \cdots, x_{i M} \delta^{T}, i=1,2, \cdots, n\right.$, an $M \times 1$ observation vector for node $X_{i}$, and $\eta_{i}=\left(X_{i}^{P a^{T}} X_{i}^{P a}\right)^{-1} X_{i}^{P a^{T}} X_{i}$. The derivation is given in Appendix. When $X_{i}$ has no parent, i.e. $\left|T_{i}\right|=0, X_{i}^{P a}=(1,1, \cdots, 1)^{T}, \boldsymbol{X}_{\boldsymbol{i}}=\left(x_{i 1}, x_{i 2}, \cdots, x_{i M} \delta^{T}\right.$. Thus

$$
P\left(x_{i} \mid P a\left(x_{i}\right)=\varnothing\right)=\sqrt{\frac{\pi}{M}} \frac{\Gamma\left(\frac{M}{2}+\delta_{i}\right)}{\left\{\psi_{i}-\frac{\left(\sum_{h=1}^{M} x_{i h}\right)^{2}}{4 M}+\frac{1}{2} \sum_{h=1}^{M} x_{i h}^{2}\right\}^{\frac{M}{2}+\delta_{i}}}
$$

# 3 Posterior Computing 

### 3.1 Adjusted Single Queue Equi-Energy sampler (ASQEE)

Many algorithms for network structure inference are available, as described in Section 1. Learning Bayesian networks is known to be NP hard (Chickering et al., 2004) and it poses great challenge on many traditional learning algorithms using MCMC on individual network structures (Madigan et al., 1995, 1996; Giudici and Green, 1999; Grzegorczyk and Husmeier, 2008). Another difficulty in network inference stems from the non-regular posterior distribution of the networks of interest. Friedman and Koller (2003) made a substantial improvement by focusing on graph orders (i.e., treating graph ordering as a random variable), rather than on individual network structures, to build a Markov chain since the space of orders is experimentally verified to be much smaller and more regular than the space of structures. In stead of inferring graphs using (1), we follow the idea of Friedman and Koller (2003) to estimate the orders and construct the graphs based on inferred linked edges.

Given a directed acyclic graph, there exist at least one total ordering, $\mathcal{O}$ (an ordering of $n$ variables, $X_{1}, X_{2}, \cdots, X_{n}$ ), in which $X_{i}$ proceeds $X_{j}$ if $X_{i} \in P a\left(X_{i}\right)$. On the other hand, if $X_{i}$ proceeds $X_{j}$ in order $\mathcal{O}$, directed links from $X_{j}$ to $X_{i}$ are prohibited in all of its consistent graphs, imposing an restriction on network structures. One advantage of graph orders is that it is not necessary to perform acyclicity checking, which is commonly required when updating individual network by edge addition, deletion or reversal. In Friedman and Koller (2003), a Markov chain on graph orders $\mathcal{O}$ and its posterior probability is obtained using all consistent graphs,

$$
P(\mathcal{O} \mid \mathbb{X}) \propto P(\mathcal{O}) \times \sum_{\mathscr{G}: \mathscr{G}^{O}} P(\mathbb{X} \mid \mathscr{G}, \mathcal{O}) P(\mathscr{G} \mid \mathcal{O})
$$

where $\mathscr{G}^{\mathcal{O}}$ are all consistent graphs with order $\mathcal{O}$. However, the enumeration of all consistent graphs becomes practically intractable for large networks. Instead of sampling all consistent graphs, Ellis and Wong (2008) suggested sampling a number of distinct consistent graphs such that

$$
\sum_{i=1}^{k} P\left(\mathscr{G}_{i} \mid \mathcal{O}\right)>1-\epsilon
$$

where $\epsilon$ is a pre-specified small positive number, $\mathscr{G}_{i}, i=1,2, \cdots, k$ are distinct consistent graphs. However, $P\left(\mathscr{G}_{i} \mid \mathcal{O}\right)$ is usually known up to a normalization constant, and calculation of the exact probability is practically impossible. To bypass this difficulty, given an order, we propose to sample a number of consistent graphs and only use the one with highest probability.

Even with smaller space of orders, the problem of local maximum is still severe. To avoid being trapped at local maximums when drawing posterior samples of $\mathcal{O}$, we propose to use the Single-Queue Equi-Energy sampling (SQEE) proposed by Ellis and Wong (2008), a variant of the Equi-Energy (EE) sampler (Kou et al., 2006). The EE sampling proceeds as follows. The first step is to define a sequence of temperatures $1=T_{1}<T_{2}<\cdots<T_{W}$, where $W$ is the number of chains. Then a sequence of energy levels are introduced, i.e., $H_{1}<H_{2}<$ $\cdots<H_{W}$ where $H_{1} \leq \min _{x} H(x), H_{W} \leq \infty$. Based on these energy levels, the tempered distributions are defined as $\pi_{l}(x)=\exp \left(\frac{-\max \left\{H(x), H_{l}\right\}}{T_{l}}\right) \quad l=1,2, \cdots, W$, which is the target distribution of $l$ h chain and the energy rings are constructed as $D_{l}=\{x|H(x) \in\left[H_{l}, H_{l+1}\right), l=$ $1,2, \cdots, W\}$. By definition, the larger the value of $l$, the more flatten distribution the $l$ h chain gets, enhancing the ability of the chain jumping across different modes. Specifically, when $l$ $=1, \pi_{1}(x)$ is the target distribution and $\pi_{1}(x)=\exp (-H(x))$. This illustrates the relation between energy function and the distribution. That is $H(x)=-\log \left(\pi_{1}(x)\right)=-\log (P(O))$. One can refer to Kou et al. (2006) for detailed discussions. The SQEE sampler is the same as the EE sampler, except for the sampling of orders at each chain. The construction of the $l$-th chain in the EE sampler is only based on the $(l+1)$-th chain. The SQEE sampler, on the other hand, uses information from any of previous higher order chains, $l+1, l+2, \cdots, W$, which makes a better communications between different chains.

Due to the use of a single graph in the SQEE sampler for a given order, we name the sampler as the adjusted single queue equi-energy sampler (ASQEE). Admittedly, the use of only one representative graph with highest posterior probability may result in bias in calculating the posterior probability of an order. However, it significantly reduces the computing difficulty

in Ellis and Wong (2008). Our simulations discussed later indicate that this approximation is applicable and produces reasonably good result.

# 3.2 Ordering proposal 

As discussed in earlier sections, graph ordering is a random variable. Order proposal plays a crucial role in building the Markov chain. We still follow the "cylindrical shift" operation (Ellis and Wong, 2008). To improve the convergence of Markov chain, the number of nodes to be flipped in proposing orders is adjusted in a dynamic way for each single chain. Specifically, the number of flipping nodes decreases as the number of iterations grows. That is, at the beginning of MCMC, we expect the chain to move fast from the current stage, while when the MCMC reaches a relatively stable state, then we expect it to move forward slowly. This will help the MCMC chain reach a more reliable stationary distribution quickly. Metropolis-Hastings (Hastings, 1970) algorithms is applied to determine whether the newly proposed ordering will be accepted or not, which is the standard local Metropolis-Hastings move. Thus the graph order is random and to be updated in the MCMC. The detailed algorithm is presented in Algorithm 1.

### 3.3 Performance Evaluation

Our interest is on directed links of the network, e.g., the link $X_{i} \rightarrow X_{j}$, and the associated posterior probabilities. Given a collection of a number of order samplers, $\mathcal{O}_{1}, \mathcal{O}_{2}, \cdots, \mathcal{O}_{K}$ the posterior probability of a directed link $f$ can be calculated

$$
\begin{aligned}
& P(f \mid \mathbb{X})=\sum_{k} P\left(f, \mathcal{O}_{k} \mid \mathbb{X}\right) \\
& =\sum_{k} P\left(\mathcal{O}_{k} \mid \mathbb{X}\right) \times P\left(f \mid \mathcal{O}_{k}, \mathbb{X}\right) \\
& =\sum_{k}\left[P\left(\mathcal{O}_{k} \mid \mathbb{X}\right) \times \sum_{i} P\left(f \mid \mathscr{G}_{i}^{\mathcal{O}_{k}} \mathcal{O}_{k}, \mathbb{X}\right) P\left(\mathscr{G}_{i}^{\mathcal{O}_{k}} \mid \mathcal{O}_{k}, \mathbb{X}\right)\right]
\end{aligned}
$$

where $\mathscr{G}_{i}^{\mathcal{O}_{k}}$ are consistent graphs sampled for order $\mathcal{O}_{k}$. By using (2), for a set of links of interest, the posterior probabilities can be calculated. Given a threshold, a positive number between 0 and 1 , a set of directed edges could be collected with posterior probability greater than the threshold. Further more, false positives and false negatives can be obtained as well for different threshold for the purpose of comparing between different methods in Bayesian network inferences.

## Algorithm 1

Adjusted Single Queue Equi-Energy algorithm (ASQEE)

Assign $X_{1}^{(W)}$ an initial ordering, set $\hat{D}_{l}=\varnothing, l=1,2, \cdots, W$.
For $a=1,2, \cdots$
For $l=W, W-1, \cdots, 1$

1: if $n>(W-\hbar(B+N)$ ( $B$ is the burn in period) then
2: do
3: if $I=W$ or if $\vec{D}_{I}\left(X_{n-1}^{(i)}\right) \neq \varnothing$ then
4: $\quad$ Perform local M-H move to update $X_{n-1}^{(l)}$ by $X_{n}^{(l)}$ with target distribution $\pi_{i}$
5: else if $I<W$ AND if $\vec{D}_{I}\left(X_{n-1}^{(l)}\right) \neq \varnothing$ then
6: $\quad$ Generate $\mu \sim U(0,1)$
7: $\quad$ if $\mu>p_{c e}$ then
8: $\quad$ Perform local M-H move to update $X_{n-1}^{(l)}$ by $X_{n}^{(l)}$ with target distribution $\pi_{i}$
9: else if $\mu \leqslant p_{c e}$ then
10: $\quad$ Uniformly pick a state $y$ from $\vec{D}_{I}\left(X_{n-1}^{(l)}\right)^{\left(\vec{D}_{I}\left(X_{n-1}^{(l)}\right)\right.}$ is the union of all previ-ous energy rings with similar energy level) and $X_{n}^{(l)} \leftarrow y$ with probability $\min \left(1, \frac{\pi_{i}(y) Q\left(y ; X_{n-1}^{(l)}\right)}{\pi_{i}\left(X_{n-1}^{(l)}\right) Q\left(X_{n-1}^{(l)} ; y\right)}\right)(Q(\ldots)$ is the transition kernel function; $X_{n}^{(l)} \leftarrow X_{n-1}^{(l)}$ with the remaining probability
11: end if
12: end if
13: if $n>(W-\hbar(B+N)+B$ then
14: $\quad \vec{D}_{I\left(X_{n}^{(l)}\right)} \leftarrow \vec{D}_{I\left(X_{n}^{(l)}\right)}+\left\{X_{n}^{(l)}\right\}$
15: end if
16: end if
In simulations, $P\left(\mathscr{O}_{k} \mid \mathbb{X}\right)$ is estimated using its relative frequency over all sampled orders after burn in. Similarly, we estimated $P\left(f, \mathscr{E}_{i}^{k} \mid \mathscr{O}_{k}, \mathbb{X}\right)$ by using the relative frequency of related consistent graphs over all sampled consistent graphs of the order.

# 4 Numerical Studies 

### 4.1 Simulated Experiments

Simulation scenarios-In this section, networks with 10 nodes are considered. An order of these 10 nodes is generated via random rearrangement of $r_{1}, r_{2}, \cdots, r_{10}$ with $r_{i} \in\{1,2, \cdots$, 10\}, i.e., $\mathcal{O}^{*}: r_{1}, r_{2}, \cdots, r_{10}, r_{i} \in\{1,2, \cdots, 10\}$. Generation of a consistent graph proceeds in the following way, similar to Ellis and Wong (2008). For each node $r_{i}$, select the number of its parents, $n_{i}$, between 0 and $\min \{(i-1), R\}, R$ is the maximum parents allowed, then assign $n_{i}$ parents to node $r_{i}$ chosen from $i-1$ proceeding nodes. The nodes and the parents of each node consist of the whole network structure. The network structure used to simulated data sets is presented in Fig 1. Given this order and network structure, multiple data sets are

generated with the following parameters: $\epsilon_{i} \sim N\left(0, \sigma_{i}^{2}\right) ; \beta_{i} \sim M V N\left(\mu_{\beta_{i}}, \Sigma_{\beta_{i}}\right) ; \mu_{\beta_{i}} \sim M V N(\mu, \Sigma)$, where $\boldsymbol{\mu}$ is a $\left(T_{i}+1\right) \times 1$ vector with all entries being $2, \Sigma$, and $\Sigma_{\beta_{i}}$ are both diagonal matrix with all elements being 0.1. To evaluate the effect of sample size, we set $M=100,500,1000$. The impact of variance of the inference of network is also considered; $\sigma_{i}$ is considered at two levels, $\sigma_{i}=0.5,1.0$.

To the best of our knowledge, FK algorithm (Friedman and Koller, 2003) is the only order based sampling approach which can make a fair comparison with the proposed ASQEE. Another Bayesian approach by Altomare et al. (2013) focuses on the situation with the order known, which is different from our case. Both FK and ASQEE are tested on generated data sets. To implement FK, an initial order is randomly generated and the total number of iterations is set at 20,000 with the first 10,000 as the burn-in period. To reduce the autocorrelations within the chain, order samples are collected every 200 iterations after burnin. Thus 50 order samples are collected in the final analysis. To make the result from ASQEE comparable to that from FK, the top 50 order samples from ASQEE in terms of posterior probability are used to make the final inference.

Result—We applied both the ASQEE and FK algorithm on 10 simulated data sets generated following each of the simulation scenarios. The averaged number of false positive and false negatives with different parameter settings is reported in Figures 2, 3, respectively. For the ASQEE approach, at a given level of noise, increasing sample size will result in better inference as indicated by smaller number of false positives and false negatives (Figures 2(d) and 3(d)). Higher level in noise seemed to weaken the quality of the inferences, but they are improved as the sample size gets larger. However, for the FK method, in general, it has higher false positives and false negatives. This may be due to its weak ability of escaping local modes. Overall, regardless of the sample size and the level of noise, ASQEE performs better than FK in terms of the averaged number of false positives and false negatives in both scenarios (Figures 2(a)-(c) and Figures 3(a)-(c)).

The findings are as expected. ASQEE has a better ability of escaping local maximum traps but the FK does not. Our simulations also indicate that using all consistent graphs result in a smaller bias compared to using one single consistent graph in calculating the posterior probability of an order. For small networks $(n<10)$ where enumerating all consistent graphs is possible, it is still recommended to use as many consistent graphs as possible. However, for large networks $(n \geq 10)$, selecting one consistent graph with highest posterior probability using M-H is likely to be a good choice.

To further test the better ability of the proposed method in identifying true links, we simulated data sets based the graph in Figure 1, but added two additional noisy nodes generated from normal distribution with mean 0 and variance 0.25 . These two nodes are isolated, i.e., without any links to the true graph or between each other. For the purpose of demonstration, we focus on the case where $M=100, \sigma_{i}=0.5$. Small sample size $(M=100)$ is considered since when sample size is large, the impact of noisy nodes is expected to be reduced. Given a threshold within interval $(0,1)$, a set of directed links are collected with the

posterior probability higher than the cutoff. Based on the collection of directed links, a node is said to be present if it is in the collection. Then we calculated the relative frequency of each node in the collection across 10 randomly generated data sets. The averages of relative frequency are displayed in Figure 4 for the true nodes and noisy nodes respectively. Consistent low frequencies indicate the the method is robust with respect to noisy nodes.

Large Network Inference—The above simulations are based on networks with 10 nodes. We further applied the ASQEE to networks with 50 nodes to assess its ability in dealing with larger networks. The simulation procedure follows the same way as previously stated except that we included four times more nodes in the networks. The averaged numbers of false positives and false negatives of ASQEE and FK are graphically presented in Figure 5 and Figure 6. The FK approach never reached high false positives and never reached low false positives either. On the other hand, the proposed approach (ASQEE) gives a much longer span on possible false positives and false negatives compared to the FK approach, emphasizing the weak ability of FK escaping local modes as noted earlier. Among comparable false positives and false negatives (the lower right corner of each plot in Figures 5 and 6), apparently, our approach overall outperforms FK by observing lower false positives and false negatives.

Moreover, the computing time of FK is much longer than that of ASQEE. This is as expected, since the number of networks is growing exponentially as the number of nodes becomes larger and the FK approach estimates exact posterior probabilities instead of highest posterior probability as in the proposed method. Compared to the performance when dealing with smaller networks with 10 nodes, both ASQEE and FK do not perform equally well when working with larger networks, indicating a great need of developing inference algorithms for large networks.

### 4.2 An Application to A DNA Methylation Data Set

To illustrate the proposed method, we apply it to a set of 26 CpG sites in 10 genes which are related to maternal smoking (Joubert et al. 2012) and aim to explore the connections among them using networks. The relevant information for all 26 CpG sites are given in Table 1. DNA methylation data of 245 girls measured at age 18 is used in the analysis. These 245 subjects are a random sample from the Isle of Wight birth cohort (Arshad and Hide, 1992). Among these 245 girls, 48 were exposed to maternal smoking during pregnancy.

To apply the proposed algorithm to the methylation data set, logit transformation is applied to transform the methylation data in the interval (0,1) to the whole real line domain. The multivariate assumption of the logit-transformed DNA methylation data was satisfied based on Shapiro-Wilk normality tests. We applied the ASQEE algorithm to the data of 197 subjects not exposed and to the 48 exposed subjects. Five chains are run sequentially from high order to low, each with the total number of 3000 iterations and the first 2700 iterations are treated as burn in. Order samples are collected for final analysis. Given an order, Metropolis Hastings algorithm is applied to sample a number of consistent graphs and the one with highest posterior probability is used to construct the pool of directed links, each

with its posterior probability estimated by the frequency of the graph sampled in MCMC after convergence.

With different cutoffs on posterior probability, a varying number of directed links are obtained. So the choice of cutoffs becomes crucial in building the finally inferred network. We follow the rule that a cutoff should be chosen such that the resulting network is of moderate size (“moderate size” means most of the nodes appearing and the number of links is approximately two or three times of the number of nodes) and captures the important information on the connections between genes. The finally inferred graph is then built upon the selected directed links. The result networks for nonsmokers and smokers are presented in Figures 7 and 8, respectively, inferred based on similar thresholds.

The network inferred for the non-smokers (Figure 7) indicates a strong regulatory path from cg 05575921 (CpG index number 6; Table 1) in AHRR gene to CpG sites in genes GFI1, MYO1G, CNTNAP2, ENSG00000225718, CYP1A1, and HLA-DPB2. This is consistent with a recent finding on the AHRR gene related to its potential as a biomarker for smoking (Philibert et al. 2013). The dominance of cg 05575921 does not change in the network for smokers for cg 06338710 (index number 7) in gene GFI1 and cg 04180046 (index number 3) in gene MYO1G. Although the direct control of cg05575921 to some CpG sites in the network for non-smokers disappeared in the network for smokers (Figure 8), indirect connection is still observed for most CpG sites shown in Figure 7. For instance, the regulatory function of cg05575921 to CpG sites cg10399789 (index number 10) and cg 12876356 (index number 15) in gene GFI1 and cg 04598670 (index number 4) in gene ENSG00000225718. We postulate that maternal smoking is likely to impose stronger dependence between CpG sites compared to subjects not exposed to maternal smoking. The size of the network for subjects exposed to maternal smoking is larger than that for nonexposed subjects. We do not expect this difference in network size is caused by sample size difference (197 v.s. 48). Random samples of size 48 chosen from the 197 non-smoking exposed girls resulted in networks with even smaller sizes, supporting the postulation of weaker dependence between CpG sites among non-smokers compared to smokers.

## Summary and Discussion

In this paper, we propose a Bayesian computational algorithm to infer directed links or networks among variables of interest, together with posterior probability. This algorithm is based on a more advanced sampler, Equi-Energy sampler. Moreover, graph orders, of which the space is much smaller than space of networks are employed to build the Markov chain. The proposed algorithm has a better ability of escaping local traps and is expected to obtain more regular posterior distributions compared to existing FK algorithm.

It performs consistently well in terms of smaller number of false positives and false negatives, as seen in simulations. Furthermore, the proposed method has the potential to exclude noisy nodes which should not be in the network. This finding provides informative assistance in the interpretation of the estimated graphs using real data, in that some nodes are shown in the network for non-smokers, but absent in the network for smokers. One potential limitation of the EE or SQEE is the computing efficiency. Although the proposed

ASQEE improved the computing efficiency by use of one graph with a high probability, there is still a need to further reduce the computing time, and this is our ongoing work.

# Acknowledgements 

The project was supported by National Institutes of Health, NIH R01AI091905 (PI: W Karmaus) and NIH R21AI099367 (PI: H Zhang) for the work by H Zhang and W Karmaus, and the University of Memphis Center for Translational Informatics, FedEx Institute of Technology, and the Assisi Foundation of Memphis for the contribution of R Homayouni.

## 6: Appendix-Derivation of the marginal posterior of G

The joint posterior of $\theta^{\mathscr{E}}, \mathscr{G}$ is, up to a normalizing constant,

$$
\begin{aligned}
& P\left(\theta^{\mathscr{G}}, \mathscr{G} \mid \mathbb{X}\right) \propto P\left(\theta^{\mathscr{G}}, \mathscr{G}\right) \times P\left(\mathbb{X} \mid \theta^{\mathscr{G}}, \mathscr{G}\right) \\
& =\prod_{i=1}^{n} \gamma^{T_{i}}\left[\frac{\psi_{i}^{\delta_{i}}}{\Gamma\left(\delta_{i}\right)}\left(\sigma_{i}^{2}\right)^{-\delta_{i}-1} e^{-\frac{\psi_{i}}{\sigma_{i}^{2}}}\left(2 \pi \sigma_{i}^{2}\right)^{-\frac{n_{i}+1}{2}} \cdot\left(\boldsymbol{X}_{i}^{P a^{T}} \boldsymbol{X}_{i}^{P a}\right)^{-1}\right]^{-\frac{1}{2}} \exp \left\{-\frac{\beta_{i}^{T} \boldsymbol{X}_{i}^{P a^{T}} \boldsymbol{X}_{i}^{P a} \beta_{i}}{2 \sigma_{i}^{2}}\right\} \\
& \times \prod_{h=1}^{M} \prod_{i=1}^{n}\left[\frac{1}{\sqrt{2 \pi \sigma_{i}^{2}}} \exp \left\{-\frac{\left(x_{i h}-\beta_{i}^{T} x_{i}^{P a}\right)^{2}}{2 \sigma_{i}^{2}}\right\}\right] \\
& \propto \prod_{i=1}^{n} \gamma^{T_{i}}\left[\left(\sigma_{i}^{2}\right)^{-\frac{M}{2}} \exp \left\{-\frac{1}{2 \sigma_{i}^{2}}\left(\boldsymbol{X}_{i}-\boldsymbol{X}_{i}^{P a} \beta_{i}\right)^{T}\left(\boldsymbol{X}_{i}-\boldsymbol{X}_{i}^{P a} \beta_{i}\right)\right\}\right. \\
& \times\left(\sigma_{i}^{2}\right)^{-\frac{T_{i}+1}{2}} \exp \left\{-\frac{\beta_{i}^{T}\left(\boldsymbol{X}_{i}^{P a^{T}} \boldsymbol{X}_{i}^{P a}\right) \beta_{i}}{2 \sigma_{i}^{2}}\right] \times\left(\sigma_{i}^{2}\right)^{-\delta_{i}-1} \exp \left\{-\frac{\psi_{i}}{\sigma_{i}^{2}}\right\}\right] \\
& =\prod_{i=1}^{n} \gamma^{T_{i}}\left[\left(\sigma_{i}^{2}\right)^{-\frac{T_{i}+1}{2}} \exp \left\{-\frac{2 \beta_{i}^{T}\left(\boldsymbol{X}_{i}^{P a^{T}} \boldsymbol{X}_{i}^{P a}\right) \beta_{i}+\boldsymbol{X}_{i}^{T} \boldsymbol{X}_{i}^{-} \boldsymbol{X}_{i}^{T} \boldsymbol{X}_{i}^{P a} \beta_{i}-\beta_{i}^{T} \boldsymbol{X}_{i}^{P a^{T}} \boldsymbol{X}_{i}}{2 \sigma_{i}^{2}}\right]\right. \\
& \times\left(\sigma_{i}^{2}\right)^{-\left(\frac{M}{2}+\delta_{i}\right)-1} \exp \left\{-\frac{\psi_{i}}{\sigma_{i}^{2}}\right\}\right] \\
& =\prod_{i=1}^{n} \gamma^{T_{i}}\left[\left(\sigma_{i}^{2}\right)^{-\frac{T_{i}+1}{2}} \exp \left\{-\frac{\left(\beta_{i}-\frac{1}{2} \boldsymbol{\eta}_{i}\right)^{T}\left[2 \boldsymbol{X}_{i}^{P a^{T}} \boldsymbol{X}_{i}^{P a}\right]\left(\beta_{i}-\frac{1}{2} \boldsymbol{\eta}_{i}\right)}{2 \sigma_{i}^{2}}\right]\right. \\
& \left.\times\left(\sigma_{i}^{2}\right)^{-\left(\frac{M}{2}+\delta_{i}\right)-1} \exp \left\{-\frac{2 \psi_{i}-\frac{1}{2}\left(\boldsymbol{X}_{i}^{P a^{T}} \boldsymbol{X}_{i}\right)^{T} \boldsymbol{\eta}_{i}+\boldsymbol{X}_{i}^{T} \boldsymbol{X}_{i}}{2 \sigma_{i}^{2}}\right]\right]
\end{aligned}
$$

where $\boldsymbol{\eta}_{i}=\left(\boldsymbol{X}_{i}^{P a^{T}} \boldsymbol{X}_{i}^{P a}\right)^{-1} \boldsymbol{X}_{i}^{P a^{T}} \boldsymbol{X}_{i}$. The last equality is because

$$
\begin{aligned}
& 2 \beta_{i}^{T}\left(X_{i}^{P a^{T}} X_{i}^{P a}\right) \beta_{i}+X_{i}^{T} X_{i}-X_{i}^{T} X_{i}^{P a} \beta_{i}-\beta_{i}^{T} X_{i}^{P a^{T}} X_{i} \\
& =\left\{\beta_{i}-\frac{1}{2}\left(X_{i}^{P a^{T}} X_{i}^{P a}\right)^{-1} X_{i}^{P a^{T}} X_{i}\right\}^{T}\left[2 X_{i}^{P a^{T}} X_{i}^{P a}\right]\left\{\beta_{i}-\frac{1}{2}\left(X_{i}^{P a^{T}} X_{i}^{P a}\right)^{-1} X_{i}^{P a^{T}} X_{i}\right\} \\
& -\frac{1}{2}\left(X_{i}^{P a^{T}} X_{i}\right)^{T}\left(X_{i}^{P a^{T}} X_{i}^{P a}\right)^{-1} X_{i}^{P a^{T}} X_{i}+X_{i}^{T} X_{i} \\
& =\left(\beta_{i}-\frac{1}{2} \eta_{i}\right)^{T}\left[2 X_{i}^{P a^{T}} X_{i}^{P a}\right]\left(\beta_{i}-\frac{1}{2} \eta_{i}\right)-\frac{1}{2}\left(X_{i}^{P a^{T}} X_{i}\right)^{T} \eta_{i}+X_{i}^{T} X_{i}
\end{aligned}
$$

By integrating out $\sigma_{i}^{2}, \beta_{i}$, we get the marginal posterior distribution of $\mathscr{G}$,

$$
\begin{aligned}
& P(\mathscr{G} \mid \mathbb{X}) \propto \prod_{i=1}^{n} \gamma^{T_{i}} \int_{\sigma_{i}^{2}} \int_{\beta_{i}}\left(\sigma_{i}^{2}\right)^{-\frac{T_{i}+1}{2}} \exp \left\{-\frac{\left(\beta_{i}-\frac{1}{2} \eta_{i}\right)^{T}\left[2 X_{i}^{P a^{T}} X_{i}^{P a}\right]\left(\beta_{i}-\frac{1}{2} \eta_{i}\right)}{2 \sigma_{i}^{2}}\right\} \\
& \times\left(\sigma_{i}^{2}\right)^{-\left(\frac{M}{2}+\delta_{i}\right)-1} \exp \left\{-\frac{2 \psi_{i}-\frac{1}{2}\left(X_{i}^{P a^{T}} X_{i}\right)^{T} \eta_{i}+X_{i}^{T} X_{i}}{2 \sigma_{i}^{2}}\right\} \\
& =\prod_{i=1}^{n} \gamma^{T_{i}}\left[\pi^{-\frac{T_{i}+1}{2}} \mid X_{i}^{P a^{T}} X_{i}^{P a}\right]^{-\frac{1}{2}} \int_{\sigma_{i}^{2}}\left(\sigma_{i}^{2}\right)^{-\left(\frac{M}{2}+\delta_{i}\right)-1} \exp \left\{-\frac{2 \psi_{i}-\frac{1}{2}\left(X_{i}^{P a^{T}} X_{i}\right)^{T} \eta_{i}+X_{i}^{T} X_{i}}{2 \sigma_{i}^{2}}\right\} \\
& =\prod_{i=1}^{n} \gamma^{T_{i}}\left[\pi^{-\frac{T_{i}+1}{2}} \mid X_{i}^{P a^{T}} X_{i}^{P a}\right]^{-\frac{1}{2}} \times \frac{\Gamma\left(\frac{M}{2}+\delta_{i}\right)}{\left\{\psi_{i}-\frac{1}{4}\left(X_{i}^{P a^{T}} X_{i}\right)^{T} \eta_{i}+\frac{1}{2} X_{i}^{T} X_{i}\right\}^{\frac{M}{2}+\delta_{i}}}
\end{aligned}
$$
