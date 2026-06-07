# Uncertainty and energy-sector equity returns in Iran: a Bayesian and quasi-Monte Carlo time-varying analysis 

Babak Fazelabdolabadi

Correspondence: fazelb@ripi.ir Center for Exploration and Production Studies and Research, Research Institute of Petroleum Industry (RIPI), P.O. Box 14665-1998, Tehran, Iran


#### Abstract

This study investigates whether the implied crude oil volatility and the historical OPEC price volatility can impact the return to and volatility of the energy-sector equity indices in Iran. The analysis specifically considers the refining, drilling, and petrochemical equity sectors of the Tehran Stock Exchange. The parameter estimation uses the quasi-Monte Carlo and Bayesian optimization methods in the framework of a generalized autoregressive conditional heteroskedasticity model, and a complementary Bayesian network analysis is also conducted. The analysis takes into account geopolitical risk and economic policy uncertainty data as other proxies for uncertainty. This study also aims to detect different price regimes for each equity index in a novel way using homogeneous/non-homogeneous Markov switching autoregressive models. Although these methods provide improvements by restricting the analysis to a specific price-regime period, they produce conflicting results, rendering it impossible to draw general conclusions regarding the contagion effect on returns or the volatility transmission between markets. Nevertheless, the results indicate that the OPEC (historical) price volatility has a stronger effect on the energy sectors than the implied volatility has. These types of oil price shocks are found to have no effect on the drilling sector price pattern, whereas the refining and petrochemical equity sectors do seem to undergo changes in their price patterns nearly concurrently with future demand shocks and oil supply shocks, respectively, gaining dominance in the oil market.


Keywords: Quasi-Monte Carlo, Bayesian optimization, Bayesian network, Oil volatility index

## Introduction

As global financial markets become more integrated, knowledge of their mutual interplay becomes more important for market participants to choose appropriate investment strategies. Furthermore, the financialization of the commodity markets has provided valuable tools for managing portfolio risks (Erb and Harvey 2006; Silvennoinen and Thorp 2013). As a commodity, crude oil has a well-recognized impact on equity markets worldwide. Early studies of the impact of oil prices on aggregate stock returns are limited to specific countries, with mixed findings. Some studies find a positive relationship (Narayan and Narayan 2010; Zhu et al. 2011; Zhu et al. 2014; Silvapulle et al. 2017), others find a negative relationship (Gjerde and Saettem 1999; Sadorsky 1999; Papapetrou 2001; Basher and

[^0]
[^0]:    (c) The Author(s). 2019 Open Access This article is distributed under the terms of the Creative Commons Attribution 4.0 International License (http://creativecommons.org/licenses/by/4.0/), which permits unrestricted use, distribution, and reproduction in any medium, provided you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made.

Sadorsky 2006; Driesprong et al. 2008; Park and Ratti 2008; Chen 2009; Filis 2010; Basher et al. 2012), and still others find no relationship (Huang et al. 1996; Cong et al. 2008; Apergis and Miller 2009; Miller and Ratti 2009; Reboredo and Rivero-Castro 2014; Hatemi et al. 2017). These conflicting results may arise owing to several underlying pitfalls in the studies, such as not considering the level of oil dependence among stock markets, not explicitly considering heterogeneity in the context in which the aggregate index is exposed to gains or losses from changes in the oil price, the nature of the oil price shock considered, and the time-varying element used (Smyth and Narayan 2018).

Whereas earlier studies assume linear and symmetrical adjustment processes for the underlying variables (Zhu et al. 2011), the current view favors assuming an asymmetrical effect of oil prices on stock returns (Basher and Sadorsky 2006; Kilian 2008; Kilian and Park 2009; Arouri 2011; Aggarwal et al. 2012; Asteriou and Bashmakova 2013; Narayan and Gupta 2015; Phan et al. 2015; Kang et al. 2016; Li et al. 2017). This view is further supported by the nonlinear characteristics of the oil price-stock return relationship. However, some empirical studies do not support this view, as they either find no asymmetric effects (Bachmeier 2008; Cong et al. 2008; Nandha and Faff 2008; Mollick and Assefa 2013; Reboredo and Rivero-Castro 2014; Asalman and Herrera 2015; Reboredo and Ugolini 2016) or only find evidence for such effects in oil-importing countries in the period after the global financial crisis (Ramos and Veiga 2013). Failure to account for the mixed heterogeneous effects of positive and negative oil price shocks on individual stock returns and merely considering aggregate stock returns may result in these conflicting findings (Tsai 2015).

Furthermore, Kilian (2008) seminal work demonstrates that the nature of the oil price structural shock, be it an oil supply shock, aggregate demand shock, or oil-specific demand shock, could be an important factor in the oil-stock interplay, and failure to consider it may result in erroneous findings (Kilian and Park 2009). The period during which each type of stock gains dominance can be obtained by decomposing oil price data (Fueki et al. 2016). Performing this analysis shows that oil supply shocks were mainly influential from the second half of 2013 through the first half of 2015. Currently, oil supply shocks are no longer as important to macroeconomic developments, and aggregate demand shocks are seen as more influential (Kang et al. 2016). Further, empirical evidence shows that the effect of the oil price on equity returns varies considerably across sectors depending on the nature of the structural shock (Broadstock and Filis 2014). The effect of an oil supply shock is found to be positive (Basher et al. 2012; Abhyankar et al. 2013) or negative (Gupta and Modise 2013; Cunado and de Gracia 2014). For oil-specific demand shocks, however, the empirical evidence almost unanimously suggests a negative effect on equity returns in oil-importing countries (Filis et al. 2011; Basher et al. 2012; Abhyankar et al. 2013; Gupta and Modise 2013; Güntner 2014; Koh 2017) and a positive effect for Norway, an oil-exporting nation.

Another puzzling feature of the oil-stock relationship is that it exhibits different behaviors in periods of low and high economic volatility; in other words, it varies over time. Quite a few studies focus on this feature, primarily using Markov-switching vector autoregression (VAR) models, regime switching models, wavelet decomposition, or frequency domain methods (Aloui and Jimmazi 2009; Chen 2009; Mohanty et al. 2010; Reboredo 2010; Jammazi and Aloui 2010; Daskalaki and Skiadopolous 2011; Filis et al. 2011; Chang and Yu 2013; Ciner 2013; Broadstock and Filis 2014; Reboredo and

Rivero-Castro, 2014; Zhang and Li 2014; Kang et al. 2015; Martin-Barragan et al. 2015; Xu 2015; Zhang 2017; Zhu et al. 2017). Concurrently, studies have examined the role of oil price volatility on stock returns using both generalized autoregressive conditional heteroskedasticity (GARCH)-type models and structural VAR models (Äijö 2008; Arouri and Nguyen 2010; Choi and Hammoudeh 2010; Elyasiani et al. 2011; Chen 2014; Lin et al. 2014; Narayan and Sharma 2014; Kang et al. 2015; Salisu and Oloko 2015; Awartani et al. 2016; Maghyereh et al. 2016; Bouri et al. 2017a, 2017b). The findings show that the volatility spillovers across markets can be strong and are significantly influenced by structural breaks, indicating a heterogeneous volatility transmission phenomenon with potential economic significance for hedging purposes. Thus, the recommended approach involves using the implied rather than the historical volatility in analyzing the cross-market association, as the former is a more accurate predictor of investor sentiment.

Many studies have focused on the effect of the oil price-stock returns relationship at the sector level (Cong et al. 2008; Arouri 2011; Elyasiani et al. 2011; Narayan and Sharma 2011; Lee et al. 2012; Li et al. 2012; Moya-Martinez et al. 2014; Caporale et al. 2015; Xu 2015; Zhu et al. 2016; Li et al. 2017; Peng et al. 2017), and many specifically focus on the oil and gas sector (Sadorsky 2001; Boyer and Filion 2007; Cong et al. 2008; Nandha and Faff 2008; Gupta 2016; Li et al. 2017). A key conclusion of these studies is that oil price increases positively affect the stock returns of firms in the oil and gas sector (Smyth and Narayan 2018), with a prolonged nonlinear relationship that strengthens over time (Managi and Okimoto 2013). However, the bulk of these studies focus on developed economies and rarely extend their analyses to emerging or transition markets.

At the country level, studies have been conducted for oil-importing (Masih et al. 2011; Cunado and de Gracia 2014; Bouri 2015; Silvapulle et al. 2017) and oil-exporting countries (Bjornland 2009; Arouri and Rault 2012; Mohanty et al. 2011; Ramos and Veiga 2013; Gil-Alana and Yaya 2014; Demirer et al. 2015), as is intuitive. Although their findings vary, these studies generally find that oil prices positively affect equity returns in oil-exporting countries (Smyth and Narayan 2018). Only a limited number of previous studies examine the oil price-stock relationship in Iran, and few focus on the effect on the price index of the Tehran Stock Exchange (TSE) (Najafabadi et al. 2012) or its volatility (Davoudi et al. 2018).

Based on the above literature review, this study makes a two-fold contribution to the existing literature. It provides the first analysis of the oil price impact on equity returns in Iran's oil sector, and it uses a firsthand application of the quasi-Monte Carlo (QMC) method and Bayesian network (BN) theory in this setting. The remainder of the paper proceeds as follows. The next section provides a description and preliminary analysis of the data. Section 3 outlines the research methodology used in the empirical investigation. A discussion of the results is presented in Section 4, followed by the concluding remarks.

# Data 

## Implied oil volatility index

The implied oil volatility index is reported by the Chicago Board of Options Exchange and is constructed on an option basis, disregarding the pricing models. In this process, the market prices of out-of-the-money calls and puts are incorporated into the computation, and the implied crude oil volatility (OVX) is obtained using Eq. 1:

$$
O V X=\left[\frac{2}{T} \sum_{i} \frac{\Delta K_{i}}{K_{i}^{2}} \exp (R T) Q\left(K_{i}\right)-\frac{1}{T}\left(\frac{F}{K_{0}}-1\right)^{2}\right]^{1 / 2} \times 100
$$

Here, $T$ is the time to maturity of the set of options, $F$ is the forward price level derived from the smallest call-put option premium difference, $R$ is the risk-free interest rate, $\Delta K_{i}=\frac{k_{i+1}-K_{i-1}}{2}$ measures the average interval of the two strike prices adjacent to the strike price of option $i, K 0$ denotes the first strike price below the forward price level $F$, and ( $K i$ ) represents the option premium computed as the midpoint of the bid-ask $Q$ spread of each option with strike price $K i$ (Maghyereh et al. 2016). This measure provides an accurate reflection of future market volatility. Other useful texts (Maghyereh et al. 2016) on this topic, however, provide more detailed information on the OVX computation.

# Preliminary statistics 

Daily data on stock prices were obtained from the TSE archive (Tehran Stock Exchange archive 2018). The archive contains data on several equity sectors, among which the oil drilling (ODR), oil refining (ORE), and chemical/petrochemical (PET) categories are presumably the most-relevant to the energy sector. Thus, this study uses data from these sectors. In addition, data on geopolitical risk (GPR), global economic policy uncertainty (EPU) (Economic Policy Uncertainty 2018) and the TSE price index (TPI) are incorporated to account for other proxies for uncertainty in the analysis. The implied oil volatility is inferred from OVX, whereas the historical oil volatility is taken from OPEC oil price data (OPEC), both of which were obtained using the Quandl package (McTaggart et al. 2016).

The sample spans September 27, 2009 to November 12, 2018, which is an interesting period that witnessed several major market events, including the emergence of shale oil as a key market player, the collapse of cooperation among OPEC members, the start of the global economic recovery, and so on (Maghyereh et al. 2016). The first date of the sample is the first available date in the TSE archive. To provide better insight into the sector data used, Fig. 1 plots these data, and Table 1 provides descriptive statistics of their log returns. Plots of OVX and OPEC are given in Fig. 2. For all the model parameters reported herein, the precision estimates are available from the author.

An augmented Dickey-Fuller Test confirms that log return series is stationary. All the equity returns show leptokurtic characteristics (i.e., kurtosis $>3$ ), suggesting that a GARCH model is an appropriate choice in this setting. The Jarque-Bera test rejects the null hypothesis of a normal distribution for all series at the $1 \%$ significance level. The results of ARCH tests also confirm the presence of heteroscedasticity in the data.

## Methodology

## GARCH

We initially considered a simple GARCH model class for studying the return $(r i, t)$ and variance $\left(\sigma^{2} i, t\right)$ dynamics of asset $i$ at time $t$. In doing so, the OVX and OPEC data were used as external regressors, as in Eqs. 2 and 3.

![img-0.jpeg](img-0.jpeg)

$$
\begin{aligned}
& r_{i,t}=\mu+\eta_{i, 1} r_{i,t-1}+\eta_{i, 2} r_{i,t-2}+\eta_{i, 3} \varepsilon_{i,t-1}+\eta_{i, 4} \varepsilon_{i,t-2}+\eta_{i, 5} \varepsilon_{i,t-3}+\eta_{i, 6} r_{o v s_{t-1}}+\eta_{i, 7} r_{O P E C_{t-1}} \\
& i \in\{O R I, P E T, O D R\} \\
& \varepsilon_{i, t}=\sigma_{i, t} z_{i, t} \\
& \sigma_{i, t}^{2}=\omega+\eta_{i, 8} \sigma_{i, t-1}^{2}+\eta_{i, 9} \sigma_{i, t-2}^{2}+\eta_{i, 10} \varepsilon_{i, t-1}^{2}+\eta_{i, 11} \sigma_{o v s_{t-1}}^{2}+\eta_{i, 12} \sigma_{o p v s_{t-1}}^{2}
\end{aligned}
$$

We also applied dynamic conditional correlation GARCH (DCC-GARCH) and asymmetric DCC-GARCH (ADCC-GARCH) models; Appendix 1 provides an explanation of these methods.

# Quasi-Monte Carlo method 

Let $\Omega$ be a separable topological space in an $N$ dim -dimensional space. Clearly, any point in $\Omega$ can be described by a set of $\operatorname{dim} N$ values, with $\varpi=(\times 1, \times 2, \ldots, x N \operatorname{dim})$ for $x i \in \Re 1 \leq i \leq N \operatorname{dim}$. Let $f$ be a real-valued function on $\Omega$ for which a global maximum is sought. Because $f$ is assumed to hold a global maximum in the region of interest, it is bounded from above, and we define its global maximum as:

$$
m(f)=\max _{\pi \in \Omega} f(\pi)
$$

Let $\lambda$ prob be a probability measure on $\Omega$. Furthermore, let $S$ be a sequence of $N$ independent $\lambda$ prob-distributed random samples, $\varpi 1, \varpi 2, \ldots, \varpi N \in \Omega$. We define

$$
m_{N}(f ; S)=\max _{1 \leq i \leq N} f\left(\pi_{i}\right)
$$

The QMC method of quasi-random search uses a deterministic sequence of points $\varpi 1$ , $\varpi 2, \ldots, \varpi N$ in $\Omega$ to find the global optimum. It is proven that $m N(f ; S)$ converges to the global maximum of $f$ with unit probability if $f$ is continuous and if a positive probability measure $(\lambda \operatorname{prob}>0)$ is taken for every nonempty subset of $\Omega$ (Niederreiter 1994).

Table 1 Descriptive statistics of the equity log returns


[^0]
[^0]:    ${ }^{a}$ Jarque-Bera test rejects the null of normality at $1 \%$ level of significance

![img-1.jpeg](img-1.jpeg)

**Fig. 2** The historical price data for OVX (**a**), and OPEC (**b**)

$$
\lim_{N \to \infty} m_N(f; S) = m(f) \tag{6}
$$

Consider a point set $P = (\pi 1, \pi 2,...,\pi N)$. The *dispersion* of point $P$ in $\Omega$ is defined by:

$$
\begin{aligned}
& \text{disp}_N(P; \Omega) = \max\min_{1 \leq i \leq N} \text{disp}(\pi, \pi_i) \\
& \text{disp}(\theta, o) = \max_{1 \leq i \leq N_{\text{disp}}} |\theta_i - o_i| \quad \text{for} \\
& \theta_i = (y_1, y_2, \dots, y_s); o_i = (z_1, z_2, \dots, z_s)
\end{aligned} \tag{8}
$$

In summary, point sets with *small* dispersion are proven to be *suitable* for quasi-random search purposes (Niederreiter 1994). In addition, the point set used for QMC should possess nice properties on its *discrepancy*, which is interpreted as the difference between the empirical and uniform distributions of the QMC point set (Drew and Homem-de-Mello 2006). QMC deals with infinite *low discrepancy sequences* (LDS), which have the additional property that, for arbitrary $N$, the initial segments have relatively small discrepancies (Lei 2002). The merits of LDS are twofold; first, they provide uniform sample points avoiding large gaps or clusters, and, second, they *know* about their predecessors and fill the gaps left from previous iterations (Kucherenko 2006), eliminating empty areas in which *no* information on the behavior of the underlying problem can be deducted. The choice of LDS is therefore central to the QMC methodology.

Different principles have been used to generate LDS sets (Sobol 1976; Bratley et al. 1992; Niederreiter 1994). Whereas other theories, such as Niederreiter's (1994), result in better asymptotic properties (Kucherenko 2006), Sobol's LDS sets provide enhanced reliability in terms of rapid convergence in high dimensionality situations (Jäckel 2002). As a result, Sobol's (1976) method was adopted for LDS generation in this study. A description of this method can be found in Appendix 2 to keep this text within a reasonable length.

Once an LDS set is available, the *multistart* QMC algorithm implements an inexpensive local search (such as the steepest descent) on the quasi-random points to concentrate the sample, which is subsequently reduced by replacing the worst points (with lower function values) with the new quasi-random points. A completely new local search is then applied to any point retained for a certain number of iterations. Two types of stopping criteria may be used for this algorithm. The first is to stop if no new value for the local maximum is found after several iterations (Glover and Kochenberger 2003).

The second is to stop if the number of worse stationary points exceeds the number of stationary points, usually by a fraction of three (Hickernell and Yuan 1997). Appendix 3 provides a more detailed description of the QMC algorithm.

# Bayesian optimization 

Consider the original problem of maximizing the function $f$ on a bounded set $\Omega$. If $\varpi$ is a point in this region, a dataset of the point parameters and their corresponding function evaluations can be iteratively collected, $\wp=\left\{\pi^{i}, f\left(\pi^{j}\right)\right\}_{1 \leq i \leq t i t e r}$ up to the iter $^{\text {th }}$ iteration. The dataset can be subsequently used to build a response surface. At this point, the optimization of the original function can be replaced by an alternative optimization of the response surface; the difference is that the latter optimization merely requires the evaluation of the learned model rather than that of the original function $f$.

Thus, the first requirement of Bayesian optimization (BO) is adopting a probabilistic model to create the response surface. Such a probabilistic framework allows the use of priors that encode the collected information in a principled way. Moreover, probabilistic models tend to be more robust to the effect of model errors, as they take into account uncertainty about the model (Calandra et al. 2016). In other words, the first step involves selecting a prior distribution over functions that expresses assumptions about the function being evaluated (Snoek et al. 2012). The prior over functions is then updated in light of new observations (Brochu et al. 2010). This analysis uses a Gaussian process (GP) (Rasmussen and Williams 2006) for the prior, meaning that any finite set of function values induces a multivariate Gaussian distribution. Other plausible choices for the prior include the random forest (Criminsi et al. 2011) and the Student-t processes (Shah et al. 2014).

In the second step, the previously collected data, $\varphi$, are combined with the prior to obtain a posterior distribution using Bayes' rule. The posterior captures our updated beliefs about the unknown objective function (Brochu et al. 2010). We attempt to maximize the posterior at each step to decrease the distance between the true global maximum and the expected maximum given by the model (Brochu et al. 2010). The next point to evaluate, $\pi^{i t e r+1}$, is determined based on an acquisition function, $f$ acquisition, which is a posterior over the functions induced by prior knowledge and data (Snoek et al. 2012). In practice, the next sample is drawn at the maximal acquisition function, $\pi^{i t e r+1}=\operatorname{argmax} \pi f(\pi)$. This study uses the acquisition function of Srinivas et al. (2010), which exploits the upper confidence bound, for maximization.

$$
f_{\text {acquisition }}\left(\pi ; \varphi, \theta_{G P}\right)=\mu\left(\pi ; \varphi, \theta_{G P}\right)-K_{\text {balance }} \sigma\left(\pi ; \varphi, \theta_{G P}\right)
$$

Here, $\theta G P$ stands for the GP hyper-parameters; $\mu(\pi ; \varphi, \theta G P)$ and $\sigma^{2}(\pi ; \varphi, \theta G P)$ are the mean and variance functions of the multivariate Gaussian distribution, respectively; and kbalance is a tradeoff parameter ( $k$ balance $>0$ ) tuned to balance the search in terms of exploitation (where $f$ is uncertain) against exploration (where $f$ is expected to be high). Exploration prevails if the value of $\kappa$ balance is increased. In this analysis, this parameter was set such that $\kappa$ balance $=2.576$. The BO algorithm conducts these steps sequentially (Appendix 4) in search for the global optimum. The mathematical foundations behind the method are thoroughly described in several useful texts (Brochu et al. 2010; Snoek et al. 2012), which also provide illustrations of its implementation.

# Bayesian network 

A BN is an implementation of a graphical model in which nodes represent random variables and arrows represent probabilistic dependencies between the nodes (Korb and Nicholson 2004). The BN's graphical structure is a directed acyclic graph (DAG) that enables estimation of the joint probability distribution. For each variable, the DAG defines a factorization of the joint probability distribution into a set of local probability distributions, and the factorization form is given by the BN's Markov property, which assumes that a variable is solely dependent on its parents (Scutari 2010). In this way, the methodology seeks to find a structure along with its parameters.

The two classifications of the BN-structure-learning process either handle this issue by analyzing the probabilistic relationships supervised by the Markov property of BNs with conditional independence tests and subsequently constructing a graph that satisfies the corresponding d-separation statements (constraint-based algorithms) or by assigning a score to each BN candidate and maximizing it with a heuristic algorithm (score-based algorithms) (Scutari 2010). This study tested both algorithm types. For the constrained-based type, we used a Monte Carlo permutation test for the conditional independence test, whereas, in the score-based case, we applied a score-equivalent Gaussian posterior density criterion. The implementation of the graphical structure-learning of the BNs was attempted using the bnlearn package (Scutari 2017).

## Results

The choice of lag in the GARCH models was rendered, following a series of computations, over a grid of lag values to identify the model with the least Bayesian information criterion (BIC) value. As our primary deduction on the cross-market association is based on the GARCH model parameters, we meticulously performed their estimation using a variety of techniques, as shown in Tables 2, 3 and 4. As evident from the results, the choice of solution technique clearly affects the estimated parameter values and is therefore extremely critical.

In the ORI sector, for example, the limited Broyden-Fletcher-Goldfarb-Shanno (LBFGS)/Bayesian methods estimate a positive effect of OVX/OPEC, whereas the QMC method finds that the effect is insignificant. Furthermore, the LBFGS/Bayesian results estimate that the volatility transmission from OVX/OPEC to ORI is positive, but this result is not supported by the QMC. Similar contradictions arise in other sectors. For example, OVX returns are found to affect PET returns positively and negatively by the LBFGS and Bayesian methods, respectively. The LBFGS/Bayesian method finds that the effect of OPEC returns on PET returns is significant, whereas the QMC method finds minimal effects. The Bayesian method finds that the volatility transmission from OVX/OPEC to PET is significant, whereas the other methods find an insignificant effect.

Table 2 The GARCH parameters for the ORI sector


Table 3 The GARCH parameters for the PET sector


In the ODR sector, the LBFGS and Bayesian methods find a negative effect of OVX returns on ODR returns, but the methods largely disagree on the direction of the effect of OPEC returns on ODR returns. The QMC method, however, considers ODR returns to be insensitive to external factors. We find similar results for volatility transmission in the ODR sector; the LBFGS/Bayesian methods estimate opposite directions of the volatility transmission between OPEC and ODR returns, but both find a positive volatility transmission scheme between OVX and ODR returns. Likewise, the QMC method finds that the ODR volatility is independent of any external factors. The results for the mean dynamic correlation from the DCC/ADCC-GARCH models, shown in Table 5, also find a strong positive correlation between TPI and the sectors studied.

To help understand the underlying connectedness, the data were also analyzed in the framework of BN theory, which is essentially a GARCH-free scheme. Interestingly, the results, shown in Figs. 3 and 4, indicate a mostly different set of significant relationships relative to those found in the GARCH results. Specifically, the BN results indicate that OPEC returns do affect returns in the ORI and PET sectors and that the volatility transmission between OPEC returns and the ORI and ODR sectors is positive.

To further investigate whether the dependency structure changes over time, we conducted a copula analysis by estimating the copula dependence parameters for Gaussian, Student-t, Gumbel, Clayton, and Frank copula models, as shown in Table 6. The results on a monthly basis indicate a positive correlation between GPR and EPU and all the energy sectors studied, as shown in Table 7. The correlation is stronger for GPR than for EPU.

To avoid the potential pitfall of bias in the parameters due to periods of high or low volatility, price regimes were also detected for each sector, as shown in Table 8. We initially determined the number of plausible price regimes for each sector by identifying the case with the lowest BIC value out of the results obtained by applying the homogeneous/nonhomogeneous Markov switching autoregressive models (Monbet 2018), as shown in Additional file 1: Tables S1-S2 of the supplementary information. The exact timing of the period was later determined by fitting a regression tree model (Therneau et al. 2015).

Interestingly, some of the time spans identified coincide with times when the oil price was undergoing breaks owing to changes in the type of shocks (i.e., oil supply or future

Table 4 The GARCH parameters for the ODR sector


Table 5 The mean dynamic correlations, obtained from DCC/ADCC GARCH


demand shocks). For example, the ORI sector clearly enters a new price regime in early 2015, when future demand shocks became more dominant than supply shocks in influencing the oil market (Fueki et al. 2016). Likewise, the PET sector begins a new price regime in late 2013, which fits chronologically with the timeline of the positive contribution of future supply shocks to the oil price hike (Fueki et al. 2016). The only exception to this rule is the ODR sector, which has been rather insensitive to shocks. For the sake of brevity, however, the results for the selected price periods are given in the supplementary information to the article.

When the analysis is restricted to a specific price-regime timeline, the results for the GARCH and BN methods tend to agree more. For instance, both methods now confirm the volatility transmission between OPEC returns and the ORI and ODR sectors. Similarly, both methods confirm that the OPEC returns have a contagion effect on the ORI and PET returns.

# Conclusions 

The choice of solution technique has a clear effect on the parameter values estimated by GARCH, making it an unreliable platform for analyzing cross-market associations. The Bayesian scheme provides an alternative robust route for understanding the underlying connectivity in the market. We find a positive correlation between GPR, EPU, and all the energy sectors studied. Neither the contagion effect on returns nor the volatility transmission between the markets, however, can be deducted upfront, as the methods yield different results. Nevertheless, the results point to the OPEC (historical) price volatility as having a stronger effect on the energy sectors relative to the implied volatility. The ODR sector is found to be insensitive to the type of oil price shock, whereas the price patterns in the ORI and PET sectors seemingly changed when future demand shocks and oil supply shocks, respectively, gained dominance in the oil market. This latter information may have potential significance for TSE market participants in re-shaping their investment portfolios.

## Appendix 1

## Dynamic Conditional Correlation (DCC-GARCH)

The model specifies the conditional mean and the conditional variance dynamics of an asset at time $t$, as follows (Engle and Sheppard, 2001):

![img-2.jpeg](img-2.jpeg)

**Fig. 3** The extracted Bayesian network for returns in each sector, obtained by the score-based algorithm. The solid/dashed lines refer to statistically significant/insignificant arcs, respectively. The letters represent **A** *r*<sub>i</sub>, **B** *r*<sub>i−1</sub>, **C** *r*<sub>i−2</sub>, **D** *r*<sub>OVX</sub>, *t*−1</sub>, **E** *r*<sub>OVX</sub>, *t*−2</sub>, **F** *r*<sub>OPEC</sub>, *t*−1</sub>, **G** *r*<sub>OPEC</sub>, *t*−2</sub>

$$
\begin{aligned}
r_{i,t} &= \mu_i + \eta_{i,13} r_{i,t-1} + \eta_{i,14} r_{i,t-2} + \varepsilon_{i,t} \\
\sigma_{i,t}^2 &= \omega_i + \eta_{i,15} \sigma_{i,t-1}^2 + \eta_{i,16} \varepsilon_{i,t-1}^2 \\
i \in \{OVX, OPEC, ORI, PET, ODR\} \\
\varepsilon_t &= H_t^{1/2} \varepsilon_t \\
H_t &= D_t R_t D_t \\
R_t &= Q_t^{r-1} Q_t Q_t^{r-1} \\
Q_t &= (1 - \eta_{17} - \eta_{18}) \overline{Q} + \eta_{17} \varepsilon_t \varepsilon_t^t + \eta_{18} Q_{t-1}
\end{aligned}
\tag{12}
$$

Here, *z<sub>t</sub>* is a vector of independent and identically distributed (IID) errors, *H<sub>t</sub>* is the conditional covariance matrix, *R<sub>t</sub>* is the conditional correlation matrix, *D<sub>t</sub>* is a diagonal matrix with conditional volatilities on its main diagonal, *Q<sub>t</sub>* = [*q*<sub>ij, t</sub>]; *i*, *j* ∈ {*OVX*, *OPEC*, *ORI*, *PET*, *ODR*} is a time-varying covariance matrix, *Q<sub>t</sub><sup>t</sup>* is a diagonal matrix with the square root of the diagonal elements of *Q<sub>t</sub>* at the diagonal, *Q̄* is an unconditional covariance matrix of standardized residuals. For the Asymmetric-DCC (ADCC-GARCH), the conditional variance is modeled by:

![img-3.jpeg](img-3.jpeg)

Table 6 The estimated copula dependence parameters for Gaussian, Student-t, Gumbel, Clayton, and Frank copula models


$$ \sigma_{i, t}^{2}=\omega_{i}+\eta_{i, 15} \sigma_{i, t-1}^{2}+\eta_{i, 16} \varepsilon_{i, t-1}^{2}+\eta_{i, 19} \varepsilon_{i, t-1}^{2} l\left(\varepsilon_{i, t-1}^{2}\right) $$

The (dynamic) correlation estimator at timet, $\hat{\rho}*{i j, t}$, is given by:

$$ \hat{\rho}*{i j, t}=\frac{\eta_{i j, t}}{\sqrt{\eta_{i i, t} \eta_{i j, t}}} $$

# Appendix 2

## The construction of Sobol's low-discrepancy sequences

The initial stage in generating a Sobol LDS set deals with operation on a set of integers in the interval $\left[1,2^{b}-1\right]$, where $b$ represents the number of bits in an unsigned integer on the operating computer (typically $b=32$ ). Let $x_{n k}$ be the $n^{\text {th }}$ draw of one of Sobol' integers in dimensionk.

Generation of numbers in the Sobol's method, is based on a set of direction integers. A distinct direction integer is considered for each of the $b$ bits in the binary integer representation. Let $v_{k l}$ denote the $l^{\text {th }}$ direction integer for dimension $k$. In order to construct Sobol' numbers, one needs to evaluate the direction integers, first. This process involves the binary coefficients of a selected primitive modulo two for each dimension (Jäckel 2002). Take $p_{k}$ as the primitive polynomial modulo two for dimension $k$ with the degreeg $_{k}$ (defined by Eq. 18). We assume $a_{k 0} \ldots a_{k p}$ representing the coefficients of $p_{k}$, with $a_{k 0}$ being the coefficient of the highest monomial term.

$$ p_{k}(z)=\sum_{j=0}^{g_{k}} a_{k j} z^{g_{k}-j} $$

In each dimension, the first $g_{k}$ direction integers $v_{k l}$ for $l=1 \ldots g_{k}$ are allowed to be freely chosen for the associated $p_{k}$ of the dimension, provided that two conditions are

Table 7 The correlation between GPR/EPU and the equity sectors, on a monthly basis


met. First, the $l^{\text {th }}$ leftmost bit of the direction integer $v_{k l}$ must be set. Second, only the $l$ leftmost bits can be non-zero, where the leftmost bit refers to the most significant one in a bit field representation. All subsequent direction integers are calculated from a recurrence relation (Eq. 19) (Jäckel 2002):

$$
v_{k l}=\frac{v_{k}\left(l-g_{k}\right)}{2^{g_{k}}} \oplus_{2} \sum_{j=1}^{g_{k}} \oplus_{2} a_{k j} v_{k(l-j)} \text { for } l>g_{k}
$$

Hereby, $\oplus_{2}$ represents the binary addition of integers modulo two (often referred to in the computer science literature as the XOR gate), and $\sum_{-}^{-} \oplus_{2}$ stands for a set of XOR operations. The procedure is to right-shift the direction integer $v_{k}\left(l-g_{k}\right)$ by $g_{k}$ bits, and then performing the XOR operation with a selection of the un-shifted direction integers $v_{k}(l-j)$ for $j=1 \ldots g_{k}$. The summation is performed analogous to the conventional $\sum$ summation operator.

The only remaining requirement for the algorithm is the generating integer of the $n^{\text {th }}$ draw. For this sake, the natural choice appears to be the draw number itself, $n$. Nevertheless, any other sequence with a unique integer for each new draw is equally useful (Jäckel 2002). Once all the preliminaries are set, the Sobol` integers, for the $s$ dimensions of interest, are generated by (Jäckel 2002);

$$
x_{n k}=\sum_{j=1}^{s} \oplus_{2} v_{k j} 1
$$

In which the $j^{\text {th }}$ bit of the generating integer is set (counting from the right).
Jäckel (2002) has provided tabulated initialization numbers for generating Sobol` integers, up to a dimension of 32 (Table 9). The generated sequence, using these initialization numbers, posesses the property; such that for any binary segment of the $s$-dimensional sequence of length $2^{s}$ there is exactly one draw in each of the $2^{s}$ hypercubes which result from subdividing the unit hypercube along each of its unit length extensions into half (Jäckel 2002).

Table 8 The time span of the detected price regimes, for the equity sectors


Table 9 An instance of the initialisation numbers for generating Sobol's LDS, up to a dimension of 32 (Jäckel 2002)


Once generated, conversion of Sobol' integers to other scales is fairly straightforward. For example, they can be converted to the $[0,1]$ scale by dividing the integers by $2^{k}$.

# Appendix 3 

## The algorithm to perform Quasi-Monte Carlo maximization

Assume $\varpi_{i}^{\text {iter }}$ to represent the best solution for $i^{\text {th }}$ point at the iter $^{\text {th }}$ iteration, also consider FBESTas the best (maximum) value off, recorded up to the iter $^{\text {th }}$ iteration. A detailed description of the QMC procedure is then ensued as follows (Hickernell and Yuan 1997):

# Step-0 Initialize. 

Input the number of initial points, $N$, the number of points with best (highestt) objective function values to retain in each iteration, $N_{\text {best }}$, and the desired number of iterations to be done for local search on each of the points, Niter $_{\text {local. search }}$.

Set the number of iterations, iter $=0$.
Set $N S P=0 ; N S W P=0 ; N T I X(j)=0$ for $(1 \leq j \leq N)$.

## Step-1 Concentrate

Obtain a new point set, by applying Niter $_{\text {local. search }}$ iteration(s) of an inexpensive local search to each of $\varpi_{j}^{\text {iter }}$ points $(1 \leq i \leq N)$.

## Step-2 Reduce

Find $\Xi($ iter $) \subset\{1, \ldots, N\}$ such that $\Xi($ iter $)$ has $N_{\text {best }}$ elements and that $f\left(\varpi_{j}^{\text {iter }}\right) \geq f\left(\varpi_{j}^{\text {iter }}\right) \forall i$ $\in \Xi($ iter $)$ and $\forall j \notin \Xi($ iter $)$.

If $j \in \Xi($ iter $)$, set $N T I X(j)=N T I X(j)+1$.
If $j \notin \Xi($ iter $)$, set $N T I X(j)=0$.

## Step-3 Find local maximum

For $j=1, \ldots, N$ such that $N T I X(j) \geq 2$.
Set $N T I X(j)=0$.
If $N S P=0$ or $f\left(\varpi_{j}^{\text {iter }}\right) \geq F B E S T+10^{-4}$ then.
Starting from $\varpi_{j}^{\text {iter }}$, perform a local optimization search, to obtain the local maximum of the point, $\varpi_{j, \text { local. }}^{\text {iter }}$.

If $f\left(\varpi_{j, \text { local. }}^{\text {iter }}\right)>F B E S T$ then.
Set $N S P=N S P+1 ; N S W P=0 ; F B E S T=f\left(\varpi_{j, \text { local. }}^{\text {iter }}\right)$.
Else.
Set $N S W P=N S W P+1$.
End
Else.
If $\frac{N S W P}{}$ NSP $\geq 3$ then stop (success).

## Step-4 Sample additional points

For $j=1,2, \ldots, N$.
If $N T I X(j)=0$ then.
Generate $\varpi_{j}^{\text {iter }+1}$ by the Sobol's LDS technique.
Else.
Set $\varpi_{j}^{\text {iter }+1}=\varpi_{j}^{\text {iter }}$.
End
Set iter $=$ iter +1 .
If the total number of function calls reached then stop (failure).
Go to Step-1.

# Appendix 4 

## The algorithm to perform Bayesian Optimization

Assume that the upper confidence bound scheme is chosen, as for the acquisition function. The algorithm to perform Bayesian optimization follows the below procedures (Brochu et al. 2010):

## Step-0 Initialize

Input the desired number of iterations to be done for BO search, $N_{\text {iter }}$. Input the tunable parameter $\kappa_{\text {balance }}$ (Eq. 14).
Set the number of iterations, iter $=0$.
Sample the (objective) function at point $\pi^{\text {iter }}$.
Form the data set, $\wp=\left\{\pi^{\text {iter }}, f\left(\pi^{\text {iter }}\right)\right\}$.

## Step-1 Repeat

Find the next point to sample, $\pi^{\text {iter }+1}$, by optimizing the acquisition function over GP.

$$
\pi^{\text {iter }+1}=\arg \max _{\pi \mathrm{i}} f_{\text {acquisition }}\left(\left.\pi\right|_{\wp_{1: t i e r}}\right)
$$

Sample the (objective) function at point $\pi^{\text {iter }+1}$.
Augment the data set $\wp$.
Update the GP prior.
Set iter $=$ iter +1 .
If the total number of desired iterations reached then stop.
Go to Step-1.

## Additional file

Additional file 1: Figure S1. The ADCC-GARCH dynamic conditional correlation between OVX and ORI (a), PET (b), and ODR (c). Figure S2. The extracted Bayesian network for returns in each sector in selected price regime periods - [2015-03-17-'2018-06-12'] (ORI); [2013-11-18'-2018-06-12'] (PET); [2009-07-27'-2018-07-23'] (ODR) - obtained by the score-based algorithm. The solid/dashed lines refer to statistically significant/insignificant arcs, respectively. The letters represent (A) $r_{i r}\left(B\right) r_{i-1},(\mathrm{C}) r_{i-2},(\mathrm{D}) r_{O V X, t-1},(\mathrm{D}) r_{O V X, t-2}$, (F) $r_{O P E C, t-1}$, (G) $r_{O P E C, t-2}$. Figure S3. The extracted Bayesian network for volatility in each sector in selected price regime periods - [2015-03-17'-2018-06-12'] (ORI); [2013-11-18'-2018-06-12'] (PET); [2009-07-27'-2018-07-23'] (ODR) - obtained by the score-based algorithm. The solid/dashed lines refer to statistically significant/insignificant arcs, respectively. The letters represent (A) $r_{i j}^{2},(\mathrm{B}) r_{i-1}^{2},(\mathrm{C}) r_{i-2}^{2},(\mathrm{D}) r_{O V X, t-1}^{2}$, (F) $r_{O V X, t-2}$, (F) $r_{O P E C, t-1}$, (G) $r_{O P E C, t-2}$. Table S1. The BIC for different price regimes, under homogeneous Markov switching autoregressive models. Table S2. The BIC for different price regimes, under non-homogeneous Markov switching autoregressive models. Table S3. Descriptive statistics of the equity log returns in the selected periods. Table S4. The GARCH parameters for the ORI sector in the period [2015-03-17'-2018-06-12]. Table S5. The GARCH parameters for the PET sector in the period [2013-11-18'-2018-06-12]. Table S6. The GARCH parameters for the ODR sector in the period [2009-07-27'-2018-07-23]. Table S7. The mean dynamic correlations, obtained from DCC/ADCC GARCH, over the corresponding selected periods. Table S8. The estimated copula dependence parameters for Gaussian, Student-t, Gumbel, Clayton, and Frank copula models, over the corresponding selected periods. (DOCX 470 kb )

## Abbreviations

ARCH: Autoregressive conditional heteroscedasticity; BIC: Bayesian information criterion; BN: Bayesian network; CBOE: Chicago board of options exchange; DCC-GARCH: Dynamic conditional correlation; GARCH: Generalized autoregressive conditional heteroskedasticity; GP: Gaussian process; LBFGS: Low Memory Broyden-Fletcher-GoldfarbShanno; LDS: Low discrepancy sequences; NSP: Number of stationary points; NWSP: Number of worse stationary points; ODR: Oil drilling; OPEC: OPEC basket oil price; ORI: Oil refining; OVX: Oil volatility index; PET: Petrochemical; QMC: Quasi-Monte Carlo; TPI: Price index of tehran stock exchange; TSE: Tehran stock exchange

## Acknowledgements

Not applicable.

## Funding

Not applicable.

# Availability of data and materials 

Not applicable.

## Authors' contributions

The work was solely done by the corresponding author, BF. The author read and approved the final manuscript.

## Competing interests

The author declares that he has no competing interests.

## Publisher's Note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.
Received: 22 September 2018 Accepted: 25 February 2019
Published online: 12 March 2019

# Submit your manuscript to a SpringerOpen ${ }^{\circledR}$ journal and benefit from: 

- Convenient online submission
- Rigorous peer review
- Open access: articles freely available online
- High visibility within the field
- Retaining the copyright to your article

Submit your next manuscript at $\rightarrow$ springeropen.com