# A hybrid Bayesian-network proposition for forecasting the crude oil price 

Babak Fazelabdolabadi

Correspondence: fazelb@ripi.ir Center for Exploration and Production Studies and Research, Research Institute of Petroleum Industry (RIPI), 14665-1998, Tehran, Iran

## Abstract

This paper proposes a hybrid Bayesian Network (BN) method for short-term forecasting of crude oil prices. The method performed is a hybrid, based on both the aspects of classification of influencing factors as well as the regression of the out-ofsample values. For the sake of performance comparison, several other hybrid methods have also been devised using the methods of Markov Chain Monte Carlo (MCMC), Random Forest (RF), Support Vector Machine (SVM), neural networks (NNET) and generalized autoregressive conditional heteroskedasticity (GARCH). The hybrid methodology is primarily reliant upon constructing the crude oil price forecast from the summation of its Intrinsic Mode Functions (IMF) and its residue, extracted by an Empirical Mode Decomposition (EMD) of the original crude price signal. The Volatility Index (VIX) as well as the Implied Oil Volatility Index (OVX) has been considered among the influencing parameters of the crude price forecast. The final set of influencing parameters were selected as the whole set of significant contributors detected by the methods of Bayesian Network, Quantile Regression with Lasso penalty (QRL), Bayesian Lasso (BLasso) and the Bayesian Ridge Regression (BRR). The performance of the proposed hybrid-BN method is reported for the three crude price benchmarks: West Texas Intermediate, Brent Crude and the OPEC Reference Basket.


Keywords: Bayesian networks, Random Forest, Markov chain Monte Carlo, Support vector machine

## Introduction

The price of crude oil has a pivotal role in the global economy and remains at the core of energy markets. As such, its fluctuations have the potential to impact economic developments worldwide. The ability to forecast the price of crude oil is therefore a useful tool in the management of most industrial sectors (Shin et al. 2013). Nevertheless, crude oil price forecasting has been a challenging task, owing to its complex behavior resulting from the confluent influence of several factors on the crude oil market. In specific, the nonlinear features exhibited in the dynamics of oil price volatilities present a quandary for predictive techniques, making the issue of (long-term) crude price forecasting open to finance research.

A wealth of literature exists on the topic of forecasting crude oil prices. These articles are myriad, both in terms of the types of models and the number of methods being used concurrently. Some studies use an approach with a single method (non-hybrid) and some are defined by several methods (hybrid). In this regard, the generalized autoregressive

[^0]
[^0]:    (c) The Author(s). 2019 Open Access This article is distributed under the terms of the Creative Commons Attribution 4.0 International License (http://creativecommons.org/licenses/by/4.0/), which permits unrestricted use, distribution, and reproduction in any medium, provided you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made.

conditional heteroskedasticity (GARCH) was amongst the first methods used because of its ability to capture time-varying variance or volatility (Agnolucci 2009; Arouri et al. 2012; Cheong 2009; Fan et al. 2008a; Hou and Suardi 2012; Kang et al. 2009; Mohammadi and Su 2010; Narayan and Narayan 2007; Sadorsky 2006; Wei et al. 2010). We attempted to perform the GARCH model as a hybrid method by combining with other models, such as the stochastic volatility (SV) model, the implied volatility (IV) model and the support vector machine (SVM) model.

The neural network (NNET) method has been another approach for crude price forecasting (Azadeh et al. 2012; Ghaffari and Zare 2009; Movagharnejad et al. 2011; Shin et al. 2013; Wang et al. 2012; Yu et al. 2008; Zhang et al. 2008). However, it reportedly bears the disadvantage of over-fitting, local minima and weak generalization capability (Zhang et al. 2015). For this sake, its hybrid usage has been recommended for the purposes of crude price forecasting.

Some authors opted to use the SVM model for price prediction, taking advantage of its suitability for modeling small-sized data samples with nonlinear behavior (Guo et al. 2012). Others have reported on the merits of the wavelet technique for crude price forecasting (Yousefi et al. 2005) with one major shortcoming being its sensitivity to the sample size. However, the recent literature advocates for the use of hybrid methods to improve on the accuracy of price forecasting. The use of the best of each technique in a hybrid framework has been enhanced by combining the soft-computing or econometric method or both (Fan et al. 2008b; Xiong et al. 2013). The reader is referred to the excellent review by Zhang et al. (2015) for a more complete assessment of past research on oil price forecasting.

The motivation behind the present work was to exploit the potential of Bayesian network (BN) theory, in the context of crude price prediction, by constructing a network over decomposed price components. As such, the present article contributes to the existing literature in this field by proposing a novel hybrid method within a Bayesian network framework. In addition, this article reports results on other devised hybrid methods, using Random Forest (RF), Markov Chain Monte Carlo (MCMC), NNET and SVM. The rest of the article is organized as follows. The next section will detail the methods being used. A description of the results is provided in the third section, which will be followed by some concluding remarks.

# Methodology 

The hybrid methodology followed in this article takes advantage of several concepts, which are introduced in this section.

## Bayesian network

A Bayesian network is an implementation of a graphical model, in which nodes represent (random) variables and arrows represent probabilistic dependencies between the nodes (Korb and Nicholson 2004). The BN's graphical structure is a directed acyclic graph (DAG) that enables estimation of the joint probability distribution. For each variable, DAG defines a factorization of the joint probability distribution into a set of local probability distributions, where the form of factorization is given by the BN's Markov property, assuming a variable to be solely dependent on its parents (Scutari 2010). In this

sake, the BN methodology initially seeks to find a DAG structure amongst the variables being considered. The two classifications of the BN-structure-learning process either treat the issue by analyzing the probabilistic relationships supervised by the Markov property of Bayesian networks with conditional independence tests and subsequently constructing a graph that satisfies the corresponding d-separation statements (constraint-based algorithms), or by assigning a score to each BN candidate and maximizing it with a heuristic algorithm (score-based algorithms) (Scutari 2010).

By taking advantage of the fundamental properties of the Bayesian networks, approximate inference (on an unknown value) is attainable. This approach should be able to avoid the curse of dimensionality due to its usage of local distributions (Nagarajan et al. 2013). Given the established BN network structure, the stochastic simulation can be applied to generate a large number of cases from the distribution network, from which the posterior probability of a target node is estimated. In this regard, the two prominent algorithms are logic sampling (LS) and likelihood weighting (LW). The LS algorithm generates a case by selecting values for each node, weighted by the probability of the values occurring at random. The nodes are traversed from the parent (root) nodes down to children (leaf) nodes. As a consequence, at each step, the weighting probability is either the prior or the Conditional Probability Table entry for the sampled parent values. A representation of all the nodes in the BN is created later on, once the full structure is visited. The collection of instantiation data enables estimation of the posterior probability for node X given evidence E (Appendix 1). The LW algorithm is similar to the former with a slight modification: adding the fractional likelihood of the evidence combination to the run count, instead of one (Appendix 2).

# Empirical mode decomposition (EMD) 

As a signal develops over time, a time-series may possess several temporal features. As such, exploring its characteristic behavior at different time scales should be informative. The Empirical Mode Decomposition (EMD) (Huang et al. 1998) separates the original signal into two parts: a fast-varying symmetric oscillation and a slow-varying local mean. The former constitutes the Intrinsic Mode Functions (IMF) of the original signal while the latter captures its residue. A repetitive sifting process is then implemented in order to extract the residue and the IMFs (Appendix 3). The process terminates once no more oscillations can be separated from the last residue. The EMD method has a stronger local representative capability compared to the wavelet transform and is more effective in processing non-linear or non-stationary signals (Hong 2011). In this work, the EMD implementation was made using the EMD package (Kim and Oh 2009; Kim and Oh 2014).

## Quantile regression with lasso penalty (QRL)

Consider a problem of regression on a data set $\left\{\left(x_{i}, y_{i}\right) ; 1 \leq i \leq n ; x_{i}, y_{i} \in \Re^{n}\right\}$ of size N , with predictors x and response values y . The conditional $\xi$ th quantile function, $\mathrm{f}(\mathrm{x}) \xi$, is defined such that $\mathrm{P}(\mathrm{Y} \leq \mathrm{f} \xi(\mathrm{X}) \mathrm{X}=\mathrm{x})=\xi$, for $0<\xi<1$. Additionally, the absolute loss function, (r) $\rho \xi$, can be defined as (Koenker and Bassett 1978; Wu and Liu 2009):

$$
\rho_{\xi}(r)=\left\{\begin{array}{ll}
\xi r & r>0 \\
-(1-\xi) & r_{\text {otherwise }}
\end{array}\right.
$$

The $\xi$ th conditional quantile function can be obtained by minimizing the following (Koenker 2004):

$$
\min _{f_{\xi}} \sum_{i=1}^{n} \rho_{\xi}\left(y_{i}-f_{\xi}\left(x_{i}\right)\right)+\lambda \Xi\left(f_{\xi}\right)
$$

, where $\lambda \geq 0$ is a regularization parameter and () $\xi \Xi \mathrm{f}$, is a roughness penalty of the $\xi$ f function. Assuming the conditional quantile function to be a linear function of the regressor $x-$ as it is in the case of linear quantile regression - the function can be written as $f_{\xi}(x)=x^{T} \beta_{\xi}$ with $\beta_{\xi}=\left(\beta_{\xi, 1}, \beta_{\xi, 2}, \ldots, \beta_{\xi, p}\right)^{T}$. There are several recommendations for the penalty function in eq. 2. The Least Absolute Shrinkage and Selection Operator (Lasso) (Tibshirani 1996; Tibshirani 2011) treats this minimization case by constraining the L1-norm of the coefficients. In other words, the (classical) Lasso formulation considers a form of $\sum_{i=1}^{p}\left|\beta_{\xi, i}\right|$ as the penalty function. Alternatively, the functional form considered for the penalty function may account for an L2 norm constraint, the Ridge Regression method. The solution should yield a set of ( $\beta$ ) regression parameters for the problem of interest. The rqPen package (Sherwood and Maidman 2016) was used for the QRL implementation in this work.

# Bayesian lasso (BLasso) and Bayesian ridge regression (BRR) 

Recall the original problem of finding the regression parameters $\beta$ for the model in eq. 3:

$$
y=\mu 1_{n}+X \beta+\varepsilon
$$

where $y$ is the $n \times 1$ vector of responses, $\mu$ is the overall mean, $X$ is the $n \times p$ matrix of standardized regressors and $\varepsilon$ is the $n \times 1$ vector of independent and identically distributes normal errors with mean 0 and unknown variance $2 \sigma$. Lasso achieves a solution for $\beta$ by minimizing eq. 4 through L1-penalized least squares. As such, the method should have a Bayesian interpretation, viewing the lasso estimate as the mode of the posterior distribution of $\beta$ (Hans 2009).

$$
\min _{\beta}(\hat{y}-X \beta)^{T}(\hat{y}-X \beta)+\lambda \sum_{i=1}^{p}\left|\beta_{i}\right| \hat{y}=y-\bar{y} 1_{n}
$$

Assuming a conditional Laplace prior on $\beta, \pi\left(\beta \mid \sigma^{2}\right)=\prod_{i=1}^{p} \frac{1}{2 \sqrt{\sigma^{2}}} e^{-\lambda\left|\beta_{i}\right| / \sqrt{\sigma^{2}}}$ and a scale invariant prior on $\sigma^{2}, \pi\left(\sigma^{2}\right)=\frac{1}{\sigma^{2}}$ a hierarchical representation of the full model is suggested as (Park and Casella 2008):

$$
\begin{aligned}
y|\mu, X, \beta, \sigma^{2} & \left.\sim N_{n}\left(\mu 1_{n}+X \beta, \sigma^{2} I_{n}\right) \beta \mid \sigma^{2}, \tau_{1}^{2}, \tau_{2}^{2}, \ldots, \tau_{p}^{2} \sim N_{p}\left(0_{p}, \sigma^{2} D_{\tau}\right) D_{\tau} \\
& =\operatorname{diag}\left(\tau_{1}^{2}, \ldots, \tau_{p}^{2}\right) \sigma^{2}, \tau_{1}^{2}, \ldots \tau_{p}^{2} \sim \pi\left(\sigma^{2}\right) d \sigma^{2} \prod_{i=1}^{p} \frac{\lambda^{2}}{2} e^{-\lambda^{2} \tau_{i}^{2} / 2} d \tau_{i}^{2}
\end{aligned}
$$

Consequently, a basis is formed for an efficient Gibbs sampler from the Bayesian posterior distribution, updating each parameter one at a time conditioned on all other parameters, with the block updating of the regression

parameters. The Bayesian concept can be also extended to the ridge regression-the Bayesian Ridge Regression (BRR) method—with an altered formulation for the priors. The reader is, however, referred to the seminal work of Park and Casella (2008) for comprehensive details of the techniques. The monomvn package (Gramacy 2016) was used to implement the BLasso/BRR methods in this work.

# Markov chain Monte Carlo (MCMC) 

Based on an assumption of a multivariate Gaussian () NK prior on $\beta$, and an inverse Gamma (IG) prior on the conditional error variance $\varepsilon$ (eq. 6), the MCMC method uses Gibbs sampling to evaluate the posterior distribution of a linear regression model, enabling Bayesian inference on the regression parameters:

$$
\begin{aligned}
y & =X \beta+\varepsilon \\
\varepsilon & \sim N\left(0, \sigma^{2}\right) \\
\beta & \sim N_{K}\left(b_{0}, B_{0}^{-1}\right) \\
\sigma^{2} & \sim I G\left(\frac{c_{0}}{2}, \frac{d_{0}}{2}\right)
\end{aligned}
$$

In this work, the parameters used during MCMC implementation were ( $0.001,0.001$ ) $\mathrm{c} 0=\mathrm{d} 0=$ for shape factor/scale parameter of the inverse gamma prior on $\sigma 2$, and $(0,0)$ $\mathrm{b} 0=\mathrm{B} 0=$ for the mean/precision of the prior on $\beta$, respectively. The latter choice corresponds to a case of putting an improper uniform prior on $\beta$. A comprehensive treatment of the MCMC method can be found in Robert and Casella (2004). The MCMC implementation was made using the R Language package, MCMCpack (Martin et al. 2011).

## Random Forest (RF)

Developed upon the seminal work of Breiman (2001), the Random Forest (RF) method is an extension of classification and regression trees with a modified leaning algorithm, that is, selecting a random subset of the features at each candidate split during the learning process. The algorithm exploits trees that use a subset of the observations through bootstrapping techniques. For each tree grown on a bootstrap sample, the error rate for observations left out of the bootstrap sample is monitored as the out-ofbag (OOB) error rate, the accuracy of which indicates the RF predictor accuracy. The Random Forest algorithm seeks to improve on bagging by de-correlating the trees, implementing random feature selection at each node for the set of splitting variables (Meyer et al. 2003). As such, the RF algorithm works with two main input parameters: the number of trees and the number of variables. However, an in-depth description of the method can be found in other useful literature (Breiman 2001). For the development of results presented herein, the number of trees to grow was set to 500, in accordance with the large-value recommendation in the literature (Breiman 2001; Micheletti et al. 2014). The choice for the number of trees, however, was rendered after conducting a series of runs over a grid in the range of [100-1100] (for the number of trees) and [10-32] (for the number of variables randomly sampled) to select the optimum values with minimum mean squared residuals. This resulted in the number of variables randomly sampled as candidate at each split to be set to a 32, corresponding to the maximum number of variables available. The RF implementation was accomplished using the randomForest package (Liaw and Wiener 2002).

The proposed hybrid forecasting methodology

The hybrid methodology proposed herein exploits the characteristics of the IMFs as its mainstream. In other words, the predicted crude oil price at any future point in time is assessed based on the summation of the corresponding IMFs and the residue. Hence, forecasts of the IMFs/residue are required in the time step(s) ahead. The regression forecast is attempted based on the two types of regressors, namely internal and external, for each IMF/residue. The internal regressors were considered to be those previous values of an IMF/residue, to which the current value depends, which is determined through the Partial Autocorrelation of the decomposed signal, whereas the external regressors were considered to be the technical indicators, the volatility index (VIX), and the implied oil volatility index (OVX). In this regard, the technical indicators taken into account have been the Aroon indicator (aroon), the Commodity Channel Index (CCI), the Double Exponential Moving Average (DEMA), the Exponential Moving Average (EMA), the Moving Average Convergence/Divergence (MACD), the Relative Strength Index (RSI), the Simple Moving Average (SMA), the Traders Dynamic Index (TDI) and the Triple Exponentially Smoothed Moving Average (TRIX).

The proposed methodology is hybrid in two different ways: classification and regression. The initial classification step involves the determination of the set of significant regressors, from the pool of regressors described using BN (constrained/scored), QRL, BLasso and as its methods, where the criterion of significance differs for each method. In the BLasso/BRR classification, for instance, a regressor is considered significant when the estimated posterior probability of the individual component's regression coefficient is returned as nonzero. In the BN scenario, on the other hand, significance is recognized in the strength of the corresponding arch-an arch strength coefficient of equal to or less than 0.05 when a conditional independence test is applied (constrained BN), or a strength coefficient of less than zero threshold, when network scores are applied (scored BN) (Scutari 2010). The final set of significant regressors is selected as the whole set of significant parameters, determined by the BN-QRL-BLasso-BRR methods, for each IMF/residue.

Table 1 Different predictive strategies tested


![img-0.jpeg](img-0.jpeg)

**Fig. 1** The Intrinsic Mode Functions- IMF.1 (**a**), IMF.2 (**b**), IMF.3 (**c**), IMF.4 (**d**), IMF.5 (**e**), IMF.6 (**f**), IMF.7 (**g**) - and the residue (**h**), decomposed from WTI price data by the EMD method

The second regression step, being hybrid in essence, involves predicting the IMFs/residue from their corresponding regressors, in the time steps ahead. For this reason, several strategies were devised and later tested for efficiency (Table 1). The first five methods take advantage of the presence of time-varying feature in the decomposed IMF signals. Under such circumstances, the GARCH model is used to forecast the time-varying IMF components, while the rest of the IMFs as well as the residue are predicted by the conjugate model listed. In the second five strategies, the IMFs as well as the residue are computed by a candidate model, in the time steps ahead, regardless of the time-varying aspect of some of the IMFs. The procedures of the proposed hybrid method can be summarized as follows: (1) Apply the EMD method to the original crude price series. Decompose the series into its IMFs and the residue. (2) Extract the significant regressors for each IMF and residue by taking the whole set of significant regressors determined by the BN-QRL-BLassoBRR methods. (3) Under Schemes 1-5 in Table 1, if the corresponding IMF presents the feature of time variation, use the GARCH model to predict its future value. Use the conjugate model in the scheme to predict the future values of other IMFs and the residue based on the regressors determined in stage 2 . (4) Under Schemes $6-10$ in Table 1, use the candidate model prescribed to forecast the future values of the IMFs and residue, based on the regressors determined in stage 2 . (5) Construct the final forecasted crude oil price by summing the future values IMFs and the residue.

The general specification of the mean/variance in the GARCH model considered in Schemes 1-5 of Table 1 is as follows, respectively:

Table 2 Descriptive statistics of the IMFs/residue of WTI, in the period between 06-July-2007 and 25-February-2019

Deviation  |
$(0.01)$ | $0.062(0.1)$ | $81.49(0.184)$ | 3.622 | -0.1983 | 2.266  |
$(0.02)$ | $0.180(0.1)$ | $564.44(0.000)$ | 5.139 | -0.1187 | 6.445  |
$(0.01)$ | $0.276(0.1)$ | $878.23(0.000)$ | 5.682 | 0.2289 | 7.557  |

[^0] [^0]: ${ }^{a}$ Alternative hypothesis: Data is stationary ${ }^{\text {b }}$ Null hypothesis: Data is level stationary

Table 3 Descriptive statistics of the IMFs/residue of BRENT, in the period between 06-July-2007 and 25-February-2019

Deviation  |

${ }^{a}$ Alternative hypothesis: Data is stationary ${ }^{\mathrm{b}}$ Null hypothesis: Data is level stationary

$$ \begin{aligned} x_{o i l, t}=\eta_{1} & +\eta_{2} x_{o i l, t-1}+\eta_{3} x_{o i l, t-2}+\ldots+\eta_{n+1} x_{o i l, t-n}+\eta_{n+2} x_{O V X, t-1}+\eta_{n+3} x_{V I X, t-1} \ & +\eta_{n+4} x_{\text {eroon }, t-1}+\eta_{n+5} x_{C C T, t-1}+\eta_{n+6} x_{D E M A, t-1}+\eta_{n+7} x_{E M A, t-1} \ & +\eta_{n+8} x_{M A C D, t-1}+\eta_{n+9} x_{R S I, t-1}+\eta_{n+10} x_{S M A, t-1}+\eta_{n+11} x_{T D I, t-1} \ & +\eta_{n+12} x_{T R I X, t-1}+\varepsilon_{t} \sigma_{o i l, t}^{2}=\eta_{n+13}+\eta_{n+14} \sigma_{o i l, t-1}^{2}+\eta_{n+15} \varepsilon_{t-1}^{2} \end{aligned} $$

,where $\mathrm{x}*{\mathrm{i} \mathrm{t}}$, refer to the price/value of i at time t , and n refers to the number of previous time steps to which the current oil price data is correlated. The final form of the GARCH specification for the time-varying IMFs may adopt a truncated version in mean, though, as they differ in their type/number of significant regressors, to be incorporated into the equation for mean. The GARCH predictions were made by the rugarch package (Ghalanos 2015). The accuracy of hybrid forecasting methods was evaluated by several statistical criteria, namely, the mean absolute error (MAE), the root mean square error (RMSE) and the mean absolute percentage error (MAPE).

Table 4 Descriptive statistics of the IMFs/residue of ORB, in the period between 06-July-2007 and 25-February-2019

Deviation  |

[^0] [^0]: ${ }^{a}$ Alternative hypothesis: Data is stationary ${ }^{\mathrm{b}}$ Null hypothesis: Data is level stationary

Table 5 The set of significant regressors detected for each IMF/residue of WTI, with the BN-QRL-BLasso-BRR techniques


![img-1.jpeg](img-1.jpeg)

**Fig. 2** The Bayesian Network of significant (solid lines), insignificant (dashed lines) or external regressors for the Intrinsic Mode Functions- IMF.1 (**a**), IMF.2 (**b**), IMF.3 (**c**), IMF.4 (**d**), IMF.5 (**e**), IMF.6 (**f**), IMF.7 (**g**) - and the residue (**h**) of WTI, extracted through the constrained-based BN method

Data and results

The price data of oil/OVX/VIX were acquired through the Quandl package (McTaggart et al. 2016). As for the crude price, the data related to three benchmarks were collected: West Texas Intermediate (WTI), Brent crude (BRENT), and the OPEC Reference Basket (ORB).

A number of seven distinct IMFs (IMF.1, IMF.2, ..., IMF.7) and one residue (RES) were detected for WTI (Fig. 1), while for BRENT/ORB, eight IMFs were detected. In this process, the S stoppage rule (Huang and Wu 2008) was considered, as for the stopping rule of the sifting process. Tables 2, 3 and 4 report the statistics measured on each IMF/residue in the time span between July 6, 2007 and February 25, 2019. The subscripts in parenthesis indicate the corresponding p-values. The IMFs with leptokurtic characteristic (Kurtosis > 3) were later used in Methods 1--5 (Table 1) as input into the GARCH model. The statistics were measured using the tseries package (Trapletti and Hornik 2015).

The technical indicators were computed using the TTR package (Ulrich 2016). However, it should be noted that because the oil price data used contained the closing price values, the CCI numbers obtained herein essentially receive an altered meaning to their original definition. Table 5 lists the set of significant external regressors, separately detected by the BN-QRL-BLasso-BRR methods, for each IMF/residue of WTI. Figure 2 provides a graphical representation of the extracted Bayesian network of significant/insignificant previous-time external regressors of the IMFs/residue of WTI, obtained through the constraint-based BN concept. The Rgraphviz package (Hansen et al. 2008) was used to plot the graph. The final set of previous-time external regressors considered for each IMF/residue was, however, taken as the whole of the significant detected parameters (Tables 6, 7 and 8). Detection of the significant internal regressors was made by following the standard procedure of considering the partial autocorrelation of the decomposed signal (Fig. 3). The DAG graphs (Fig. 3) are important in the sense that they reveal the influencing parameters on each intrinsic mode function. The CCI, SMA and OVX parameters are not directly connected; the DAG assumes that there is no possibility to revisit a given vertex after starting from that same vertex, following a consistently directed sequence of edges. A connection between these nodes (vertices) would violate this rule for the data involved, which is the reason why they appear unconnected in the reported DAGs. Moreover, the CCI, SMA and OVX can be considered to be the parents for most of intrinsic mode functions as well as the residue.

Table 6 The final set of external regressors for each IMF/residue of WTI


Table 7 The final set of external regressors for each IMF/residue of BRENT


The hybrid strategy optimization (Ghalanos 2015) was used within the GARCH implementation in Methods 1-5. This ensures that a number of non-linear solvers are called in a sequence in the case that the initial optimization fails. For the SVM implementation (Methods 2 and 7 in Table 1), a grid-search was initially conducted over the parameter ranges so as to calibration the SVM model (Meyer et al. 2015). This was followed by a kernel-based SVM regression, where the hyperparameters of the kernel were taken as those obtained from the calibration stage. The Laplacian kernel was used within the SVM regression with bound constraint (Karatzoglou et al. 2004). For the NNET predictions (Methods 4 and 9), the k-nearest neighbor method was used without any preprocessing of the predictor data (Kuhn et al. 2016). As for the MCMC (Methods 3 and 8), a number of 1,000 burn-in iterations was elapsed, followed by 10,000 Metropolis iterations for the sampler. Also, a number of 1,000 MCMC samples were collected for the BLasso/BRR outputs. The initial lasso penalty parameter was taken as one and the RaoBlackwellized samples were used for $\sigma 2$ (Gramacy 2016). The selection of the model for the columns of the design matrix for regression parameters in BLasso/BRR was made using the Reverse-Jump MCMC (Gramacy 2016).
Implementation of the graphical structure-learning of the Bayesian networks was attempted using the bnlearn package (Scutari 2017). Both types of constraint/score-based algorithms were tested in this work. For the constraintbased type, the Monte Carlo permutation test was used for the conditional

Table 8 The final set of external regressors for each IMF/residue of ORB


![img-2.jpeg](img-2.jpeg)

**Fig. 3** The partial autocorrelation of the Intrinsic Mode Functions- IMF.1 (**a**), IMF.2 (**b**), IMF.3 (**c**), IMF.4 (**d**), IMF.5 (**e**), IMF.6 (**f**), IMF.7 (**g**) - and the residue (**h**) of WTI

Table 9 The average errors of the 10-days-ahead forecasts of WTI


independence test. While in the score-based case, a score equivalent Gaussian posterior density criterion was applied. For a BN inference, predictions were obtained by applying the LW algorithm and extracting the expected value of the conditional distribution of 500 simulation results. All the available nodes in the structure were taken as evidence in that situation except the node related to the variable being predicted.

The crude price forecasting was attempted from periods of time ten days ahead. To test the performance of the methods, three random training sets were used with a common beginning date of July 6, 2007 and ending dates of January 3, 2017, March 27, 2017 and February 8, 2019, respectively. In each case, the hybrid methods were used to predict the crude prices for the ten out-of-sample days immediately ahead. The average of the errors incurred is reported in Tables 9, 10 and 11. According to the results, Method-10 shows conspicuously better performance when compared with the other methods, in all three statistics measured (MAE, RMSE and MAPE). The superior performance of Method-10 is not merely bounded to a single market, rather it is demonstrated over the three price types (WTI, BRENT and ORB). Furthermore, the predictive accuracy of Method-10 is compared by using a Diebold-Mariano test against other techniques. Table 12 lists the Diebold-Mariano statistics for the 10-day forecast of WTI/BRENT/ORB, assessing the alternative hypothesis that Method-10 is more accurate than the method

Table 10 The average errors of the 10-days-ahead forecasts of BRENT


Table 11 The average errors of the 10-days-ahead forecasts of ORB


of choice, clearly demonstrating the superior accuracy of the proposed hybrid technique. A close inspection of the results also indicates that, overall, Methods 6-10 achieve a better predictive success than Methods $1-5$, which incorporate the GARCH model. However, this should not rule out the application of GARCH in hybrid price forecasting models.

The extracted Bayesian networks indicate that both OVX and VIX are influential on different layers of IMF or the residue, which accounts for their impact on the value of future crude prices. In addition, the established BN structure shows the previous-time technical indicators to affect different layers of IMF and the residue of the decomposed price signal.

The proposed hybrid methodology was chosen for short-term prediction of crude prices, owing to the short-term viability of the regressors employed. The method, however, deserves further investigation and merits being tested for its long-term forecasting capability, for example incorporating regressors with longer life spans.

# Conclusions

The performance of the hybrid Bayesian network proposition was outstanding compared to the other devised hybrid models, in all of the three crude price types (WTI, BRENT and ORB) and against all of the three statistical benchmarks (MAE,

Table 12 The Diebold-Mariano statistics for 10-day forecast of WTI/BRENT/ORB, for the alternative hypothesis that Method-10 is better in terms of accuracy versus the method of choice


RMSE and MAPE). The BN demonstrated that the volatility indices (OVX, VIX) are influential on different decomposed signals of the crude price, affecting the level-ahead price values. The predictive power of the hybrid methods adopting GARCH was shown to be inferior to the other methods, which apply regressions to all of the layers of the decomposed signal for crude price forecasting. Since the proposed hybrid method makes use of regressors with short-term life spans (i.e., technical indicators, OVX, VIX and past price values), the method remains a valid option for short-term forecasting. The question of its capability in handling longterm price forecasts is yet to be answered by the future research using parameters with longer-term viability.

# Appendix 1 

## The Logic sampling algorithm

Consider an established Bayesian Network. Assume $X$ to be node in this BN structure, and $E$ as a given evidence. The Logic sampling algorithm for estimation of the posterior probability of node $X$ given evidence $E=e$, is computed by the following procedure (Korb and Nicholson 2004):

Step-1 Initialize
For each value $x_{i}$ for node $X$
Create a count variable Count $\left(x_{i}, e\right)$
Create a count variable Count (e)
Initialize all count variables to zero
Step-2 Repeat
For all the root (parent) nodes
Choose a value, weighed the choice by the priors, at random
Loop
Choose values for children at random, using the conditional
probability given the known values of the parents
Until all the BN structure is visited
Step-3 Update
If the case (instantiation) includes $E=e$

$$
\operatorname{Count}(e)=\operatorname{Count}(e)+1
$$

If the case includes both $X=x_{i}$ and $E=e$

$$
\operatorname{Count}\left(x_{i}, e\right)=\operatorname{Count}\left(x_{i}, e\right)+1
$$

Step-4 Estimate
Obtain an estimate for the posterior probability

$$
P\left(X=x_{i} \mid E=e\right)=\frac{\operatorname{Count}\left(x_{i}, E=e\right)}{\operatorname{Count}(E=e)}
$$

# Appendix 2 

## The Likelihood weighing algorithm

Consider an established Bayesian Network. Assume $X$ to be node in this BN structure, and $E$ as a given evidence. The Likelihood weighing algorithm for estimation of the posterior probability of node $X$ given evidence $E=e$, is computed by the following procedure (Korb and Nicholson 2004):

Step-1 Initialize
For each value $x_{i}$ for node $X$
Create a count variable Count $\left(x_{i}, e\right)$
Create a count variable Count (e)
Initialize all count variables to zero
Step-2 Repeat
For all root nodes
If a root is an evidence node, $E_{j}$
Choose the evidence value, $e_{j}$

$$
\operatorname{likelihood}\left(E_{j}=e_{j}\right)=P\left(E_{j}=e_{j}\right)
$$

Else
Choose a value for children at random, using the conditional probabilities given the known values of the parents

Until the entire BN structure is visited
Step-3 Update
If the case includes $E=e$

$$
\operatorname{Count}(e)=\operatorname{Count}(e)+\Pi_{j} \text { likelihood }\left(\mathrm{E}_{\mathrm{j}}=e_{j}\right)
$$

If this case includes both $X=x_{i}$ and $E=e$

$$
\operatorname{Count}\left(x_{i}, e\right)=\operatorname{Count}\left(x_{i}, e\right)+\Pi_{j} \text { likelihood }\left(\mathrm{E}_{\mathrm{j}}=e_{j}\right)
$$

Step-4 Estimate
Obtain an estimate for the posterior probability

$$
P\left(X=x_{i} \mid E=e\right)=\frac{\operatorname{Count}\left(x_{i}, E=e\right)}{\operatorname{Count}(E=e)}
$$

# Appendix 3 

## The Empirical Mode Decomposition algorithm

Consider a time series, $f(t)$, with $t$ referring to time. The EMD fractionation of the original data is made following the below steps (Huang et al. 1998):

Step-1

$$
\begin{aligned}
& \text { Find the extrema (maxima and minima) of the input data } m_{0}(t)=f(t) \\
& \text { Form the upper-envelope } U_{0}(t) \text {, and the lower-envelope } L_{0}(t) \text {, by } \\
& \text { connecting the maxima and minima with spline function, respectively. } \\
& \text { Calculate the first envelope mean, } m_{1}(t)=\frac{U_{0}(t)+L_{0}(t)}{2} \\
& \text { Calculate the first difference between the mean and the data, } \\
& h_{1}(t)=m_{0}(t)-m_{1}(t)
\end{aligned}
$$

Step-2

$$
\begin{aligned}
& \text { Take the previous difference, } h_{i-1}(t) \text { as input. } \\
& \text { Find the envelopes, using the procedure in step-1. } \\
& \text { Calculate the mean and difference. }
\end{aligned}
$$

$$
\begin{gathered}
m_{i}(t)=\frac{U_{i-1}(t)+L_{i-1}(t)}{2} \\
h_{i}(t)=m_{i-1}(t)-m_{i-1}(t)
\end{gathered}
$$

Step-3

Repeat step-2 until the stopping condition is satisfied - a condition of small difference between successive iterations, or small value of envelope mean.

Calculate the first IMF and the residue

$$
\begin{gathered}
I M F_{1}(t)=h_{n}(t) \\
r_{1}(t)=f(t)-I M F_{1}(t)
\end{gathered}
$$

Step-4

Take $r_{1}(t)$ as the input and repeat steps 1-3, until the number of extrema is less than 2 .

# Abbreviations 

aroon: Aroon indicator; Blasso: Bayesian Lasso; BN: Bayesian Network; BRENT: Brent crude; BRR: Bayesian Ridge Regression; CCI: Commodity Channel Index; DAG: Directed acyclic graph; DEMA: Double Exponential Moving Average; EMA: Exponential Moving Average; EMD: Empirical Mode Decomposition; GARCH: Generalized autoregressive conditional heteroskedasticity; IMF: Intrinsic Mode Functions; IV: Implied volatility; KSVM: Kernel Support Vector Machine; LS: Logic sampling; LW: Likelihood weighting; MACD: Moving Average Convergence/Divergence; MAE: Mean absolute error; MAPE: Mean absolute percentage error; MCMC: Markov Chain Monte Carlo; NNET: Neural Networks; OOB: out-of-bag; ORB: OPEC Reference Basket; OVX: Implied Oil Volatility Index; QRL: Lasso penalty; RF: Random Forest; RMSE: Root Mean Square Error; RSI: Relative Strength Index; SMA: Simple Moving Average; SV: Stochastic volatility; SVM: Support Vector Machine; TDI: Traders Dynamic Index; TRIX: Triple Exponentially Smoothed Moving Average; VIX: Volatility Index; WTI: West Texas Intermediate

## Acknowledgements

Not applicable.

## Author's contributions

The work was solely done by the corresponding author, Babak Fazelabdolabadi. The author read and approved the final manuscript.

## Funding

Not applicable.

## Availability of data and materials

Not applicable.

## Competing interests

The author declares that he has no competing interests.

## Received: 18 November 2018 Accepted: 10 June 2019 Published online: 11 July 2019

# Publisher's Note 

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.