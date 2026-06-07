# Bayesian Network Structure Learning with Permutation Tests 

Marco Scutari* and Adriana Brogini<br>Department of Statistical Sciences, University of Padova, Italy<br>*Corresponding Author: m.scutari@ucl.ac.uk

October 30, 2018


#### Abstract

In literature there are several studies on the performance of Bayesian network structure learning algorithms. The focus of these studies is almost always the heuristics the learning algorithms are based on, i.e. the maximisation algorithms (in score-based algorithms) or the techniques for learning the dependencies of each variable (in constraint-based algorithms). In this paper we investigate how the use of permutation tests instead of parametric ones affects the performance of Bayesian network structure learning from discrete data. Shrinkage tests are also covered to provide a broad overview of the techniques developed in current literature.


Keywords: Bayesian networks, conditional independence tests, permutation tests, shrinkage tests.

## 1 Introduction and Background

Bayesian networks are a class of graphical models, which allow an intuitive representation of the probabilistic structure of multivariate data using graphs (Pearl, 1988; Koller and Friedman, 2009). They are composed by two parts:

- a set of random variables $\mathbf{X}=\left\{X_{1}, X_{2}, \ldots, X_{p}\right\}$ describing the features of the data. The probability distribution of $\mathbf{X}$ is called the global distribution of the data, while the ones associated with each $X_{i} \in \mathbf{X}$ are called local distributions.
- a directed acyclic graph (DAG), denoted $G=(\mathbf{V}, A)$. Each node $v \in \mathbf{V}$ is associated with one variable $X_{i}$, and they are often referred to interchangeably. The directed arcs $a \in A$ that connect them represent direct

[^0]
[^0]:    This is a preprint of an article whose final and definitive form has been published in the Communications in Statistics - Theory and Methods ( 2012 Taylor \& Francis Group, LLC); Communications in Statistics - Theory and Methods is available online at: www.tandfonline.com/10.1080/03610926.2011.593284.

stochastic dependencies; so if there is no arc connecting two nodes, the corresponding variables are either marginally independent or conditionally independent given a subset of the remaining variables.

In other words, each local distribution is associated with a single node $X_{i}$ and depends only on its parents (i.e. the nodes $X_{j}$ in $\mathbf{X}$ such that $X_{j} \rightarrow X_{i}$, usually denoted by $\boldsymbol{\Pi}_{X_{i}}$ ). This property, which is known as the Markov property of Bayesian networks (Pearl, 1988), specifies the form of the decomposition of the global distribution into the local ones:

$$
\mathrm{P}(\mathbf{X})=\prod_{i=1}^{p} \mathrm{P}\left(X_{i} \mid \boldsymbol{\Pi}_{X_{i}}\right)
$$

In principle there are many possible choices for both the global and the local distribution functions, depending on the nature of the data and the aims of the analysis. However, literature have focused mostly on two cases: the discrete case (Heckerman et al., 1995), in which both the global and the local distributions are multinomial random variables, and the continuous case (Geiger and Heckerman, 1994), in which the global distribution is multivariate normal and the local distributions are univariate normal random variables. In the first case, the parameters of interest are the conditional probabilities associated with each variable, usually represented as conditional probability tables (CPTs); in the latter, the parameters of interest are the partial correlation coefficients between each variable and its parents.

The task of fitting a Bayesian network is called learning, a term borrowed from expert systems theory and artificial intelligence, and in general is implemented in two steps.

The first step consists in finding the graph structure that encodes the conditional independencies present in the data. Ideally it should coincide with the dependence structure of the global distribution, or it should at least identify a distribution as close as possible to the correct one in the probability space. This step is called network structure or simply structure learning (Korb and Nicholson, 2004; Koller and Friedman, 2009), and is similar in approaches and terminology to model selection procedures for classical statistical models. Several algorithms have been presented in literature for this problem, thanks to the application of many results from probability, information and optimisation theory. Despite the (sometimes confusing) variety of theoretical backgrounds and terminology they can all be traced to only three approaches: constraintbased (which are based on conditional independence tests), score-based (which are based on goodness-of-fit scores) and hybrid (which combine the previous two approaches).

The second step is called parameter learning and, as the name suggests, deals with the estimation of the parameters of the global distribution. Assuming the graph structure is known from the previous step, this can be done efficiently by estimating the parameters of the local distributions.

In literature there are several studies on the performance of Bayesian network structure learning algorithms; one of the most extensive performed in

recent years is presented in Tsamardinos et al. (2006). The focus of these studies is almost always the heuristics the learning algorithms are based on, i.e. the maximisation algorithms used in score-based algorithms or the techniques for learning the dependence structure associated with each node in constraintbased algorithms. The influence of the other components of the overall learning strategy, such as the conditional independence tests (and the associated type I error threshold) or the network scores (and the associated parameters, such as the equivalent sample size), is usually not investigated. However, limiting such studies to the performance of heuristics poses serious doubts on their conclusions, because the decisions made by the heuristics are based on the values of the statistical criteria they use to extract information from the data. Therefore, it is important to choose a conditional independence test or a network score presenting a good behaviour for the data at hand and to tune it appropriately.

For this reason, in this paper we will investigate the behaviour of permutation conditional independence tests and tests based on shrinkage estimators for discrete data. These two classes of tests are usually not considered in literature, where the asymptotic $\chi^{2}$ tests based on Pearson's $\mathrm{X}^{2}$ (Bishop et al., 2007) and mutual information (Kullback, 1968) are the de facto standard. In particular, we will study the permutation Pearson's $\mathrm{X}^{2}$ test and the permutation mutual information test described in Edwards (2000), and the shrinkage test based on the estimator for the mutual information presented in Hausser and Strimmer (2009).

# 2 Conditional Independence Tests 

We will now introduce the conditional independence tests whose performance will be considered in Section 3 Since we are limiting ourselves to discrete data, both the global and the local distributions are assumed to be multinomial, and the latter are represented as conditional probability tables. Conditional independence tests and network scores for discrete data are functions of these conditional probability tables through the observed frequencies $\left\{n_{i j k}, i=\right.$ $1, \ldots, R, j=1, \ldots, C, k=1, \ldots, L\}$ for the random variables $X$ and $Y$ and all the configurations of the levels of the conditioning variables $\mathbf{Z}$.

### 2.1 Parametric Tests

Two classic conditional independence tests used in the analysis of contingency and probability tables are:

- mutual information: an information-theoretic distance measure defined as

$$
\operatorname{MI}(X, Y \mid \mathbf{Z})=\sum_{i=1}^{R} \sum_{j=1}^{C} \sum_{k=1}^{L} \frac{n_{i j k}}{n} \log \frac{n_{i j k} n_{++k}}{n_{i+k} n_{+j k}}
$$

It is proportional to the log-likelihood ratio test $\mathrm{G}^{2}$ (they differ by a $2 n$

factor, where $n$ is the sample size) and is related to the deviance of the tested models.

- Pearson's $X^{2}$ : Pearson's $\mathrm{X}^{2}$ test for contingency tables,

$$
\mathrm{X}^{2}(X, Y \mid \mathbf{Z})=\sum_{i=1}^{R} \sum_{j=1}^{C} \sum_{k=1}^{L} \frac{\left(n_{i j k}-m_{i j k}\right)^{2}}{m_{i j k}}, \quad \text { where } \quad m_{i j k}=\frac{n_{i+k} n_{+j k}}{n_{++k}}
$$

The asymptotic null distribution is $\chi^{2}$ with $(R-1)(C-1) L$ degrees of freedom in both cases. For a detailed analysis of their properties we refer the reader to Agresti (2002) and Bishop et al. (2007). The main limitation of these tests is the rate of convergence to their limiting distribution, which is particularly problematic when dealing with small samples and sparse contingency tables. This situation, which is often referred to as "small $n$, large $p$ ", is very common in many settings in which Bayesian networks are used (such as gene expression and omics data).

# 2.2 Permutation Tests 

The mutual information and Pearson's $\mathrm{X}^{2}$ tests can also be performed by conditioning on a sufficient statistic and using the permutation distribution as the null distribution (Pesarin and Salmaso, 2010). The observed significance values are then computed with a conditional Monte Carlo (CMC) simulation, as detailed in Edwards (2000):

1. compute the value of the test statistic for the original data set, and denote it with $T$;
2. perform the following steps for a suitable number $R$ of times, usually between 500 and 5000 :
(a) randomly permute the observations presenting the same configuration of the conditioning variables $\mathbf{Z}$; this is typically done by applying the permutation algorithm from Mehta and Patel (1983) to the contingency tables associated with the configurations of $\mathbf{Z}$;
(b) compute the test statistic on the resulting data, and denote it with $T_{r}^{*}, r=1, \ldots, R$
3. compute the significance value of $T$ as

$$
\hat{\alpha}_{R}=\frac{1}{R} \sum_{r=1}^{R} \mathbb{1}_{\{x \geqslant T\}}\left(T_{r}^{*}\right)
$$

Both the permutation algorithm by Mehta and Patel (1983) and the conditional independence tests considered in this paper have the marginal totals $\left\{n_{i+k}\right\}$ and $\left\{n_{+j k}\right\}$ as sufficient statistics, so they can be computed efficiently.

The main advantage of permutations tests is that they do not require a large sample size or particular distributional assumptions to perform well, because they operate conditioning on the available data (Pesarin and Salmaso, 2010). Therefore, they perform better than the parametric tests usually found in literature, because they are not limited by the rate of convergence to the respective asymptotic distributions. However, the computer time required by the generation of the permutations of the data and by the repeated evaluation of the test statistic have prevented their widespread use in many settings in which high-dimensional problems are the norm.

# 2.3 Shrinkage Tests 

In high-dimensional, multivariate problems, the maximum likelihood estimator is known to be inefficient and displays a considerable instability for most reasonable, finite sample sizes. This phenomenon, which is known as the "curse of dimensionality", is caused by the exponential increase in the number of parameters as the number of variables increase.

These issues can be explained as a consequence of the inadmissibility of the maximum likelihood estimator for the mean of multivariate distributions discovered by Stein (1956) and investigated by James and Stein (1961). A solution is provided in the form of a regularised estimator, which includes some bias in order to increase the overall performance of the estimator. Since the natural parameters of the test statistics we are considering are the probabilities $\left\{p_{i j k}\right\}$ associated with the observed frequencies $\left\{n_{i j k}\right\}$, we will denote such an estimator as $\tilde{\mathbf{p}}=\left\{\tilde{p}_{i j k}\right\}$ and the maximum likelihood estimator as $\hat{\mathbf{p}}=\left\{\hat{p}_{i j k}=\right.$ $\left.n_{i j k} / n\right\}$. The regularised estimator is then defined as a linear combination of the maximum likelihood estimator and a target distribution with probabilities $\mathbf{t}=\left\{t_{i j k}\right\}$, which is usually chosen to be uniform (i.e. $t_{i j k}=1 /|\mathbf{t}|$ ):

$$
\tilde{p}_{i j k}=\lambda t_{i j k}+(1-\lambda) \hat{p}_{i j k}, \quad \lambda \in[0,1]
$$

Such an estimator is called a shrinkage estimator, because $\hat{\mathbf{p}}$ is shrunk towards $\mathbf{t}$ in the parameter space; $\lambda$ is likewise called the shrinkage coefficient.

A closed-form estimator for $\lambda$ has been derived by Ledoit and Wolf (2003) as the value that minimises the mean squared error of $\tilde{\mathbf{p}}$. Hausser and Strimmer (2009) derived its expression for multinomial probabilities, with the aim of defining an improved entropy estimator (Kullback, 1968); it has the form

$$
\lambda^{*}=\frac{1-\sum \hat{p}_{i j k}^{2}}{(n-1) \sum\left(t_{i j k}-\hat{p}_{i j k}\right)^{2}}
$$

The application of this result to the mutual information test leads to the definition of the corresponding shrinkage mutual information test, which is based on the shrinkage estimator $\tilde{\mathbf{p}}$ instead of the usual maximum likelihood estimator $\hat{\mathbf{p}}$. It has the form

$$
\mathrm{MI}_{s h}(X, Y \mid \mathbf{Z})=\sum_{i=1}^{R} \sum_{j=1}^{C} \sum_{k=1}^{L} \tilde{p}_{i j k} \log \frac{\tilde{p}_{i j k} \tilde{p}_{++k}}{\tilde{p}_{i+k} \tilde{p}_{+j k}}
$$

The observed significance value can still be computed using the asymptotic $\chi^{2}$ distribution used for the classic mutual information test, for two reasons. First, Ledoit and Wolf (2003) proved that $\lambda^{*}$ converges to zero as the sample size diverges, which means that the shrinkage test $\mathrm{MI}_{s h}$ and the classic parametric test MI have the same asymptotic behaviour. Furthermore, the shrinkage mutual information test is still a log-likelihood ratio test. The only difference is in the number of the parameters, as both the null and the observed distributions gain an additional parameter, $\lambda$. Therefore, according to Lehmann and Romano (2005) the asymptotic distribution of the shrinkage test is again $\chi^{2}$ with $(R-1)(C-1) L$ degrees of freedom.

# 3 Effects on Structure Learning 

We will now investigate the behaviour of the permutation conditional independence tests and shrinkage tests introduced in the previous section, using the parametric tests as a reference. Five performance indicators will be taken into consideration:

- the posterior density of the network for the data it was learned from, as a measure of goodness of fit. It is known as the Bayesian Dirichlet equivalent score (BDe) from Heckerman et al. (1995) and has a single parameter, the equivalent sample size, which can be thought of as the size of an imaginary sample supporting the prior distribution. The equivalent sample size will be set to 10 as suggested in Koller and Friedman (2009);
- the BIC score (Schwarz, 1978) of the network for the data it was learned from, again as a measure of goodness of fit;
- the posterior density of the network for a new data set, as a measure of how well the network generalises to new data;
- the BIC score of the network for a new data set, again as a measure of how well the network generalises to new data;
- the Structural Hamming Distance (SHD) between the learned and the true structure of the network, as a measure of the quality of the learned dependence structure (Tsamardinos et al., 2006).

These indicators will be estimated for each test, using the bnlearn R package (R Development Core Team, 2010; Scutari, 2010) as follows:

1. generate a sample from the true probability distribution of the ALARM network from Beinlich et al. (1989). ALARM contains 37 nodes and 46 arcs, for a total of 509 parameters, and is frequently used as a benchmark in the literature of Bayesian networks (Larrañaga et al., 1997; Moore and Wong, 2003; de Campos and Ji, 2008);

2. learn a network structure with the Max-Min Hill-Climbing (MMHC) hybrid algorithm (Tsamardinos et al., 2006) using one of the conditional independence tests under investigation and the BDe score. This learning strategy has been shown to be one of the most effective up to date; it combines the Max-Min Parents and Children (MMPC) constraint-based algorithm with a score-based hill climbing search. Two thresholds are considered for the type I error of the tests: 0.05 and 0.01 . Since results are very similar, they are reported only for 0.05 for brevity;
3. learn a second network structure from the same data with the asymptotic, parametric test based either on Pearson's $\mathrm{X}^{2}$ or on the maximum likelihood estimator for the mutual information, depending on which test was used in the previous step;
4. repeat the previous two steps using the BIC score instead of BDe;
5. compute the relevant performance indicators for each pair of network structures, and the differences are standardised to express the relative difference over the values obtained with the asymptotic tests. In particular, BDe will be only considered for networks learned in step 2 and BIC for networks learned in step 4.

These steps will be repeated 50 times for each sample size. The data set needed to assess how well the network generalises to new data is generated again from the true probability structure of the ALARM network and contains 20000 observations. The parameters of the network, which are the elements of the conditional probability tables associated with the nodes of the networks, are estimated using the corresponding empirical frequencies.

# 3.1 Permutation Tests 

Nonparametric conditional independence tests, and permutation tests in particular, provide a feasible alternative to the corresponding parametric tests in a wide range of situations.

The effects of the properties of the permutation Pearson's $\mathrm{X}^{2}$ and the permutation mutual information tests on Bayesian network structure learning are shown in Figure 1 and Figure 2. First, we can clearly see from the box-plots in Figure 1 that the use of permutation tests results in network structures with higher scores for all the considered sample sizes (200, 500, 1000 and 5000). This is also true when considering the new data set, meaning that the network structures learned with these tests are better for predicting the behaviour of new samples. As expected, improvements in the BIC and BDe scores are particularly significant for low sample sizes; the probability structure of the ALARM network has 509 parameters, which means that the ratios between the number of observations and the number of parameters are $0.3929,0.9823,1.9646$ and 9.8231 respectively.

It is also interesting to note that, even though the performance of parametric tests improves with the sample size, both permutation tests appear to improve

![img-0.jpeg](img-0.jpeg)

Figure 1: Improvements in Bayesian network structure learning when using the permutation mutual information (on the left) and the permutation Pearson's $\mathrm{X}^{2}$ (on the right) tests. The black dot in each box-plot represents the median.

![img-1.jpeg](img-1.jpeg)

Figure 2: Differences in the Structural Hamming Distance when using the permutation mutual information (on the left) and the permutation Pearson's $\mathrm{X}^{2}$ (on the right) tests. The black dot in each box-plot represents the median.
at a faster rate. In fact, in all plots in Figure 1 the relative improvement for samples of size 5000 is greater than the corresponding improvement for samples of size 2000, regardless of the score we are considering or the data set it is computed from.

On the other hand, the network structures learned with permutation tests considered in this section are often not as close to the true network structure as the ones learned with the corresponding parametric tests. This is can be clearly seen from the box-plots in Figure 2, which show that in the majority of simulations the relative difference between the SHD values is negative (i.e. the SHD associated with the parametric test is smaller than the SHD associated with the permutation test). Permutation tests outperform parametric tests only for samples of size 5000 .

The comparatively poor performance of permutation tests in terms of SHD can be attributed to the conditioning on the observed sample that characterises them. Most of the samples considered in this analysis are too small to provide an adequate representation of the true probability structure of the ALARM network, as evidenced by the ratios between their sample sizes and the number of parameters. Therefore, the network structures learned with permutation tests from these samples are able to capture only part of the true dependence structure. The arcs that are most likely to be missed, however, are those that represent the weakest dependence relationships; otherwise the networks would not be able to fit new data so well.

In conclusion, permutation tests result in better network structures than the corresponding parametric tests, both in terms of goodness of fit and in how well the networks are able to generalise to new data. However, if the focus of the analysis is the structure of the network itself (such as when the Bayesian network is considered as a causal model) parametric tests may be preferable for small samples.

![img-2.jpeg](img-2.jpeg)

Figure 3: Improvements in Bayesian network structure learning when using the shrinkage estimator for the mutual information. The black dot in each box-plot represents the median.

SHD improvement (shrinkage)
![img-3.jpeg](img-3.jpeg)

Figure 4: Differences in the Structural Hamming Distance when using the shrinkage estimator for the mutual information. The black dot in each boxplot represents the median.

# 3.2 Shrinkage Tests 

The shrinkage mutual information test has a completely different behaviour than the permutation tests covered above.

As expected from a test based on a regularised estimator, the networks learned using shrinkage tests do not fit the data as well as the networks learned with the corresponding maximum likelihood tests. This can be clearly seen from the box-plots in Figure 3. The relative differences in the BIC and BDe scores are almost never positive for either the data the networks have been learned from or the new data, in particular for samples of size 10 and 20. Such small samples are most likely to result in sparse contingency tables, and therefore in high values of the shrinkage coefficient, as soon as a few conditioning variables are included in the tests. Larger samples are less affected by the regularisation of the shrinkage estimator, because the shrinkage coefficient converges to zero as the number of observations diverges (Ledoit and Wolf, 2003). This means that for larger samples (i.e. 100, 150 and 200) the behaviour of the shrinkage mutual information test approaches the one of the classic mutual information test, as can be seen from the increasingly small difference between the two in terms of BIC and BDe scores.

An important side effect of the regularisation performed by the shrinkage estimator is the reduction of the structural distance from the true network structure for small samples. We can see from Figure 4 that the shrinkage test outperforms the test based on the maximum likelihood estimator; there is a systematic improvement for sample sizes 10, 20 and 50 (i.e. SHD is smaller for the shrinkage test). As the sample size increases, the behaviour of the shrinkage test approaches again the one of the corresponding maximum likelihood test. These simulations confirm the results produced with shrinkage tests for many "small $n$, large $p$ " problems, such as those studied in Schäfer and Strimmer (2005) and Krämer et al. (2009), which have led to a widespread use of shrinkage tests in biology and genetics.

## 4 Conclusions

In this paper we investigated how the use of permutation tests instead of parametric ones affects the performance of Bayesian network structure learning from discrete data, while also covering shrinkage tests. Permutation tests result in better network structures than the corresponding parametric tests, both in terms of goodness of fit and in how well the networks are able to generalise to new data. Shrinkage tests, on the other hand, outperform both parametric and permutation tests in the quality of the network structure itself, which is closer to the true dependence structure of the data.
