# The impact of measurement errors in the identification of regulatory networks 

André Fujita* ${ }^{1}$, Alexandre G Patriota ${ }^{2}$, João R Sato ${ }^{3}$ and Satoru Miyano ${ }^{1,4}$


#### Abstract

Addresses: ${ }^{1}$ Computational Science Research Program, RIKEN, 2-1 Hirosawa, Wako, Saitama, 351-0198, Japan, ${ }^{2}$ Institute of Mathematics and Statistics, University of São Paulo, Rua do Matão, 1010 - São Paulo, 05508-090, Brazil, ${ }^{3}$ Center of Mathematics, Computation and Cognition, Universidade Federal do ABC, Rua Santa Adélia, 166 - Santo André, 09210-170, Brazil and ${ }^{4}$ Human Genome Center, Institute of Medical Science, University of Tokyo, 4-6-1 Shirokanedai, Minato-ku, Tokyo, 108-8639, Japan


E-mail: André Fujita* - andrefujita@riken.jp; Alexandre G Patriota - patriota@ime.usp.br; João R Sato - joao.sato@ufabc.edu.br; Satoru Miyano - miyano@ims.u-tokyo.ac.jp
*Corresponding author

Published: 13 December 2009
Received: 16 July 2009
BMC Bioinformatics 2009, 10:412 doi: $10.1186 / 1471-2105-10-412$
Accepted: 13 December 2009
This article is available from: http://www.biomedcentral.com/1471-2105/10/412
(c) 2009 Fujita et al; licensee BioMed Central Ltd.

This is an Open Access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/licenses/by/2.0), which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.


#### Abstract

Background: There are several studies in the literature depicting measurement error in gene expression data and also, several others about regulatory network models. However, only a little fraction describes a combination of measurement error in mathematical regulatory networks and shows how to identify these networks under different rates of noise.


Results: This article investigates the effects of measurement error on the estimation of the parameters in regulatory networks. Simulation studies indicate that, in both time series (dependent) and non-time series (independent) data, the measurement error strongly affects the estimated parameters of the regulatory network models, biasing them as predicted by the theory. Moreover, when testing the parameters of the regulatory network models, p-values computed by ignoring the measurement error are not reliable, since the rate of false positives are not controlled under the null hypothesis. In order to overcome these problems, we present an improved version of the Ordinary Least Square estimator in independent (regression models) and dependent (autoregressive models) data when the variables are subject to noises. Moreover, measurement error estimation procedures for microarrays are also described. Simulation results also show that both corrected methods perform better than the standard ones (i.e., ignoring measurement error). The proposed methodologies are illustrated using microarray data from lung cancer patients and mouse liver time series data.

Conclusions: Measurement error dangerously affects the identification of regulatory network models, thus, they must be reduced or taken into account in order to avoid erroneous conclusions. This could be one of the reasons for high biological false positive rates identified in actual regulatory network models.

## Background

There has been an increasing interest among bioinformaticians in the problem of quantifying correctly gene expression in a given sample. It is well accepted that the observed gene expression value is a combination of the
"true" gene expression signal with intrinsic biological variation (natural fluctuation) and a variation caused by the measuring process, also known as measurement error. Studies have documented the presence of sizable measurement error in data collected mainly from

microarrays and also by other approaches such as Real Time RT-PCR, Northern blot, CAGE, SAGE, etc [1,2]. This measurement error can be easily observed when two technical replicates are plotted in a MA (M is the logarithm of the intensity ratio and A is the mean of the logged intensities for a dot in the plot) or scatter plots. Frequently, a considerable dispersion can be observed. This dispersion is due to the measurement error, since, in theory, technical replicates (same samples) must present the same quantifications. In general, these fluctuations are derived from probe sequence, hybridization problems, high background fluorescence, signal quantification procedures (image analysis), etc [3,4]. In the last few years, a considerable number of reports on the problem of quantifying and separating "true" gene expression signal from noise [5-7] has been published with the main aim to find differentially expressed genes [8,9]. Despite these results in gene expression analysis and a large amount of research performed in modeling regulatory networks (Bayesian networks [10,11], Boolean networks [12,13], Relevance networks [14], Graphical Gaussian models [15], Differential equations [16], etc), only a fraction of the statistical studies use procedures designed for modeling networks taking into account measurement error.

Frequently, Ordinary Least Squares (OLS) and methods related to it, such as Pearson and Spearman correlations [17], ridge, lasso and elastic net regressions [18] are widely used as estimators to quantify the strength of association between gene expression signals and model regulatory network structures. In the time series context, estimation process of Autoregressive (AR) [19-22] models also use OLS to identify which gene is or is not Granger causing another gene. Generally, a regression is carried out between the target gene and its potential predictors in order to test which predictor gene has, at a gene expression level, association with the target gene.

It is well known in the statistical literature that, when the measurement errors are ignored in the estimation process, OLS and its variants become inconsistent (i.e., even increasing the sample size the estimates do not converge to the true values). More precisely, the estimation of the slope parameters is attenuated [23] and consequently, regulatory network models become biased. Moreover, there is no control of type I error since standard OLS was not designed to treat measurement error. In this context, an adequate inference treatment must be considered for the model parameters in order to avoid inconsistent estimators. Usually, measurement equations are added to the model to capture the measurement errors effect, therefore, producing consistent estimators, efficient and asymptotically normally distributed. A careful and deep exposition on the
inferential process is presented in [23] and the references therein. Although there are studies referring to problems caused by measurement errors in the statistical literature, there is a gap in the network modeling theory which must be filled in to avoid misinterpretation and distort conclusions from the inferential process. Here, we focus on the development and present some important statistical tools to be applied in OLS-based and VAR network models taking into account the measurement errors effect. We also conduct simulation studies in order to evaluate the impact of the measurement error in the identification of gene regulatory networks using the standard OLS in both conditions, time series and non time series data. Surprisingly, both the simulations and theory described that, in the presence of measurement error, the estimated coefficients are biased even increasing the amount of observations, and the statistical tests are not controlling the rate of false positives properly. These results were also observed in time series context, where the autoregressive coefficients were strongly affected. Thus, a corrected version of the OLS estimator for independent (in the regression context) and dependent (in the autoregressive context) data containing measurement error were developed. Results in both, simulated and actual biological data are illustrated. Moreover, two procedures to estimate measurement error in microarrays are presented.

## Results and discussions

In order to evaluate the performance of conventional OLS and VAR methods in practice, simulations were carried out in artificial data with absence and presence of measurement error. Noise was added at different rates, and sample size was increased in order to evaluate the consistence of conventional and proposed approaches.

In the following we give a brief explanation about the usual and proposed methods. Let $x$ and $y$ be variables (gene expression values) with the following relationship $y=\alpha+\beta x+\varepsilon$, where $\varepsilon$ is the random error (intrinsic biological variation) of the model with zero mean and finite variance. In general, we are interested in estimating the parameters $\alpha$ and $\beta$ to make inferences about them. In practice, we take a sample $x_{i}, y_{i}$ for $i=1, \ldots, n$ and use these quantities to obtain estimates for the parameters of interest. However, it is not always possible to observe directly the values of $x$ and $y$ because sometimes they are latent values, i.e., they are masked by measurement errors derived by the measurement process in microarrays, for example. Then, instead of observing the true variables, we observe surrogate variables $X$ and $Y$ which carry an error, that is $X=x+\epsilon_{1}$ and $Y=y+\epsilon_{2}$, where $\epsilon_{1}$ and $\epsilon_{2}$ are measurement errors. Generally, what is done in practice is a naive solution, since it simply replaces $x$

with $X$ and $y$ with $Y$ in the regression equation and uses the OLS approach to estimate the parameters. That is, based on the equation $Y=\alpha+\beta X+\varepsilon$, estimators are built. On the other hand, the proposed approach is slightly different. The latter considers three equations, namely: $y=\alpha+\beta x+\varepsilon, X=x+\epsilon_{1}$ and $Y=y+\epsilon_{2}$ and uses them to estimate the model parameters. This little difference can result great impact in the estimators properties of each approach. Notice that the former produces inconsistent estimators and the latter produces consistent estimators when the data contains measurement error. The same idea can be applied in the time series context.

The corrected versions of the OLS estimators in both independent and dependent data were compared to their conventional forms in order to evaluate the performance under gene expression data containing measurement error. The standard OLS and VAR models are particular cases of the proposed models in the case when the measurement error is absent. Firstly, simulations were performed in regression models. Table 1 illustrates average coefficients estimated by standard OLS in 10,000 Monte Carlo simulations. Notice that increasing the rate of measurement error, more attenuated become the estimated coefficients, i.e., the estimates are shifted towards zero. Table 2 illustrates the percentage of rejected hypotheses in 10,000 Monte Carlo simulations. Analyzing when $\beta_{1}=0$, i.e., when there is no association between the corresponding covariate and the response variable, Table 2 shows that the OLS approach does not control, at a $5 \%$ nominal level, the rate of false positives. The larger the sample size, the worst the OLS performance, as it was expected to be. On the other hand, the coefficients of the corrected OLS are unbiased (Table 1 values between brackets) and converge to "true" value when sample's size becomes larger. Moreover, the rate of false positives are actually controlled under the null hypothesis (Table 2 - values between brackets).

Analyzing Figure 1A, we conclude that, the standard OLS is not controlling the rate of false positives in the presence of measurement error for any significance level (p-value threshold). On the other hand, Figure 1B describes the consistency of the test performed by the corrected OLS, i.e., the uniform distribution of p-values illustrates that the rate of false positives is actually controlled under any considered threshold, since the

Table I: Ordinary least squares


Average OLS estimated coefficients and corrected OLS (between brackets) in 10,000 simulations. The model is described in (Simulations section, simulation I - independent data)."-" means that it was not possible to calculate due to high measurement error in comparison to sample's size. EM: Standard deviation of the Error of Measure. n: Number of samples. Notice that, in the presence of measurement error, the coefficients $(\beta)$ estimated by the corrected OLS (between brackets) converge to the "true" values, while the estimated by standard OLS do not.

Table 2: Ordinary least squares


Percentage of the number of associations (rejected hypothesis) obtained using standard OLS and corrected OLS (between brackets) in 10,000 simulations. The first line contains the strength of association between predictors and response variables as described in simulation I. The rate of false-positives was controlled in $5 \%$. In bold, are the rate of false-positives, i.e., the number of false-positives divided by the number of simulations. "-" means that it was not possible to calculate due to high measurement error when compared to sample's size. EM: Standard deviation of the Error of Measure, n: Number of samples. Notice that, in fact, the corrected OLS controls the rate of false positives in $5 \%$ while the usual OLS does not (values in bold). uniform distribution emerges for p -values when the distribution of the statistic is correctly specified (otherwise, the p-value distribution may not be uniform).

In the time series case, similar results were observed. The standard VAR estimates produce biased coefficients in the presence of measurement error (Table 3). Moreover, there is no control of the type I error in both, autoregressive and cross-autoregressive coefficients (in all the text, in order to simplify the notation, autoregressive coefficient will denote the auto-loop, i.e., the coefficient related to $z_{i, t, r} \rightarrow z_{i, t}$ and cross-autoregressive coefficient will represent the coefficient for $z_{i, t, r} \rightarrow j$ and $r<t$ ) (Table 4). Analyzing the results produced by the proposed VAR model (Table 3 - values between brackets), it is possible to observe that the estimated coefficients converge to the true value as time series length increases. Notice that, the results produced by the standard VAR model indicate that, increasing the sample size does not imply in convergence of the estimates to the true values (Table 3). By observing Table 4, we see that the corrected VAR approach is actually controlling the rate of false positives in the set significance level ( $\mathrm{p}<0.05$ ). Figure 2 emphasizes this result.

Figure 2A and 2B describe the p-value distributions of autoregressive and cross-autoregressive coefficients of standard VAR under the null hypothesis ( $\beta_{0}=0$ (autoregressive) and $\beta_{1}=0$ (cross-autoregressive)). Notice that when $\beta_{0}=\beta_{1}=0$, the p -value distributions should be uniform in the interval $[0,1]$. However, there is a high concentration around zero, demonstrating that the rates of false positives are inflated (and consequently not controlled) in both autoregressive or cross-autoregressive cases. In Figures 2C and 2D, the p-value distributions are uniform, i.e., the test under the null hypothesis $\left(\beta_{0}=0\right.$ and $\left.\beta_{1}=0\right)$ using the corrected VAR model is actually controlling the type I error in autoregressive and cross-autoregressive coefficients (uniform distribution). Figures 3 and 4 illustrates the corrected power curves for both, OLS and VAR. The corrected power curve $P^{c}(\alpha)$ can be defined as

$$ P^{c}(\alpha)=\frac{P(a(\alpha))}{a(\alpha) / \alpha} $$

where $\alpha$ is the adopted type I error nominal level, $P(a(\alpha))$ is the power using the true probability of the type I error, namely $a(\alpha)$. Notice that the corrected

![img-0.jpeg](img-0.jpeg)

**Figure 1**

**P-value distribution under the null hypothesis (β₁ = 0) in independent data with standard deviation of the measurement error equal to 0.6 and sample size equal to 400 (model described in Simulations section, simulation I).** This simulation was performed 10,000 times. (A) Standard Ordinary Least Squares (non uniform distribution); (B) Corrected Ordinary Least Squares (uniform distribution).

Power is just the power penalized by the distance between *a*(α) and α. This correction in the power is necessary because under the null hypothesis, the power has to be the nominal level, and for comparing powers from different statistics it must be done using the same nominal level.

For a good statistic, notice that under an alternative hypothesis and when *n* → ∞, the corrected power *P*(α) converges to one because *a*(α) → α and *P*(*a*(α)) → 1. On the one hand, for a statistic that does not control the rate of false positives, for example, when α is set to 5% and the true probability of the type I error is *a*(α) = 0.08, since *a*(α)/α is greater than one, *P*(α) will not converge to one. On the other hand, for a good statistic, the rate *a*(α)/α converges to one when *n* → ∞, then *P*(α) will converge to one. Analyzing Figures 3 and 4, it is possible to verify that, for standard OLS and VAR approaches (dashed lines), the ratio *a*(α)/α increases faster than the corresponding powers *P*(*a*(α)), i.e., the dashed lines is decreasing as *n* increases. Notice on Tables 2 and 4 that the rates of false positives (*a*(α)) increase as *n* increases, and consequently, in our specific case, the ratio *a*(α)/α increases and the corrected power *P*(*a*(α)) converges to zero. On the other hand, the proposed methods (full lines) keep the false positive rates controlled while the corrected power increases as *n* increases. It can be observed by the full lines converging to one (Figures 2 and 4) and also on Tables 2 and 4. The variations present in the curves are probably due to variations in Monte Carlo simulations, since these variations decreased (become smoother) when the number of simulations was increased from 5,000 to 10,000 and from 10,000 to 15,000. In order to illustrate the performance of standard and corrected OLS and VAR approaches in actual biological data, firstly, the measurement error was estimated using the method described in the

Table 3: Vector autoregressive model


Standard VAR average estimated coefficients and corrected VAR (between brackets) in 10,000 simulations. The first line contains the strength of association between predictors and response variables as described in simulation II. "-" means that it was not possible to calculate due to high measurement error when compared to sample's size. EM: Standard deviation of the Error of Measure. n: Number of samples. Notice that, in the presence of measurement error, the coefficients $(\beta)$ estimated by the corrected VAR (between brackets) converge to the "true" values, while the estimated by standard VAR do not.

Measurement error estimation section (No technical replicates subsection). Then, the TP53 network was constructed using a dataset composed of 400 microarrays.

Table 5 illustrates the results of a multivariate regression using OLS. Four genes known to be direct targets of TP53 were selected, namely, MDM2, FAS, BAX and MAP4, and a multivariate network was constructed using OLS. In fact, these four genes were actually identified as targets of TP53 (high t-statistics). Notice that comparing the standard and corrected OLS estimators, it is possible to conclude that the t-statistics are different probably due to the biased standard OLS estimator in the presence of measurement error.


Table 6 shows the application of both, standard and proposed VAR models in a set of well known five genes
related to circadian rhythm, namely, CLOCK, CRY2, PER2, PER3 and DBP. The genes CRY2, PER2, PER3 and DBP are known to be regulated by the complex BMAL1CLOCK in mammals [24]. A VAR process of order one was adjusted and applied in a multivariate manner. Notice that also in the time series data, the estimators presented different results due to measurement error.


Comparison of the usual and proposed methods in actual biological data is a difficult task since no one knows the "true" values. However, as observed in the simulation results, it is possible to conclude that the

Table 4: Vector autoregressive model



Percentage of the number of associations (rejected hypothesis) obtained using standard VAR and corrected VAR (between brackets) in 10,000 simulations. The first line contains the strength of association between predictors and response variables as described in simulation II. The rate of false-positives was controlled in $5 \%$. In bold, are the rate of false-positives, i.e., the number of false-positives divided by the number of simulations. "-" means that it was not possible to calculate due to high measurement error when compared to sample's size. EM: Standard deviation of the Error of Measure. n: Number of samples. Notice that, in fact, the corrected VAR controls the rate of false positives in $5 \%$ in both cases, autoregressive ( $\beta_{0}$ ) and cross-autoregressive $\left(\beta_{1}\right)$ coefficients, while the usual VAR does not (values in bold).

![img-1.jpeg](img-1.jpeg)

**Figure 2**

**P-value distribution under the null hypothesis in time series data with standard deviation of the measurement error equal to 0.6 and time series length equal to 400 (model described in Simulations section, simulation II).** This simulation was performed 10,000 times. (A) Standard VAR p-value distribution of autoregressive coefficient β₀ = 0 (non uniform distribution); (B) Standard VAR p-value distribution of cross-autoregressive coefficient β₁ = 0 (non uniform distribution); (C) Corrected VAR p-value distribution of autoregressive coefficient β₀ = 0 (uniform distribution); (D) Corrected VAR p-value distribution of cross-autoregressive coefficient β₁ = 0 (uniform distribution).

Corrected approaches provide more reasonable results than biased standard methods.

In order to uncover more details about the performance of both, OLS and VAR, other experiments were conducted. These experiments consist in adding correlation in the residues and testing other null hypothesis (data not shown). The results obtained ignoring the errors by these methods can be compiled as:

1. In both, independent and time series data, standard OLS does not work correctly in the presence of measurement error and correlated residues;
2. In the presence of measurement error and no correlation among all predictors of independent data, the t-test built, under the standard OLS approach, to test H₀ : βᵢ = m for j = 1, ..., p works perfectly only if m = 0 (for other null hypothesis this t-test does not work correctly). This happens because, under this hypothesis, there is no covariate effect and, consequently, there is no measurement error effect associated with the covariate. The same behavior can be seen in Patriota et al. (2009) [25];
3. In the time series case, the t-test (or Wald's test) does not control the type I error rate in the presence of measurement error, independent whether there is or not correlation between time series;
4. In the presence of measurement error, the estimates obtained by standard OLS are always attenuated.

Therefore, these results demonstrate that improved methods to construct regulatory networks become necessary, since it is known that genes belong to an

![img-2.jpeg](img-2.jpeg)

Figure 3
Corrected power curve. The full line represents the proposed OLS and the dashed line represents the standard OLS. It was performed 15,000 Monte Carlo simulations (model described in simulation I) for each n where $n$ varied from 300 to 1,000 in steps of $100 . n$ : sample size. P-value and standard deviation of measurement error were set to 0.05 and 0.5 , respectively.
![img-3.jpeg](img-3.jpeg)

Figure 4
Corrected power curve. The full line represents the proposed VAR and the dashed line represents the standard VAR. It was performed 15,000 Monte Carlo simulations (model described in simulation II) for each $n$ where $n$ varied from 300 to 1,000 in steps of $100 . n$ : sample size. P-value and standard deviation of measurement error were set to 0.05 and 0.5 , respectively.
intrincate network, i.e., the covariates may be correlated and, moreover, gene expression quantification processes such as microarray technology measure with considerable error. If these conditions are ignored, one may obtain distort results and, consequently, conclude that there is a relationship between gene expressions where there is no association.

Construction of large networks is a challenge in bioinformatics. The methods proposed here do not allow the identification of networks when the number of variables is larger than the number of observations. Increasing the number of variables, the estimates become imprecise and the chances of obtaining multicollinearity problems also increases. In the presence of multicollinearity, one may use a feature selection procedure such as a stepwise (forward or backward, for example) in order to choose the optimum set of predictors.

Analyzing Pearson correlation coefficient, one can observe that it is simply a normalized linear regression coefficient (OLS) between -1 and 1. Therefore, Pearson correlation-based methods such as Relevance networks [14] or Graphical Gaussian models [26] need further studies in order to evaluate if they are also superestimating the rate of false positives and attenuating the coefficients like OLS. Moreover, Pearson correlation is widely used in order to test linear correlation between a certain gene expression signal and another characteristic such as prognostic, phenotype, tumor grade etc. Since these covariates may be measured with error, it is also crucial to develop a corrected Pearson correlation.

In order to develop a corrected Pearson correlation for measurement error, verify that it is possible to use the improved OLS presented in this report. The corrected Pearson correlation $(\rho)$ between two random variables $X$ and $Y$, both measured with error is given by

$$
\rho(X, Y)=\frac{\beta \sqrt{\sigma_{X}^{2}-\sigma_{\epsilon_{1}}^{2}}}{\sqrt{\sigma_{Y}^{2}-\sigma_{\epsilon_{2}}^{2}}}
$$

where $\beta$ should be estimated by using the corrected OLS (i.e., by simultaneously considering the three equations: $y=\alpha+\beta x+\varepsilon, X=x+\epsilon_{1}$ and $Y=y+\epsilon_{2}$ ), $\sigma_{X}$ and $\sigma_{Y}$ are the standard deviations of the observed variables $X$ and $Y$, respectively, and $\sigma_{\epsilon_{1}}$ and $\sigma_{\epsilon_{2}}$ are the standard deviations of the error of measure $\epsilon_{1}$ and $\epsilon_{2}$, respectively. In this way, the estimate of the corrected version of the Pearson correlation is consistent (the larger the sample size, the smaller estimation error tends to be). Notice that, the difference between the corrected and

Table 5: Gene TP53 (lung cancer data)


$$
\begin{aligned}
& t\left(\beta_{\text {standard }}\right)=\frac{\beta_{\text {standard OLS }}}{\sqrt{\operatorname{var}\left(\beta_{\text {standard OLS }}\right)}} \\
& t\left(\beta_{\text {corrected }}\right)=\frac{\beta_{\text {corrected OLS }}}{\sqrt{\operatorname{var}\left(\beta_{\text {corrected OLS }}\right)}}
\end{aligned} \text {. The direction of the arrows }
$$

means the direction of regression, i.e., in the head of the arrow is the predictor and in the tail of the arrow is the response variable. Since it is not a time series data, the $t$ statistics are equal independent of the direction of regression, in other words, the $t$ statistics of $x \varnothing y$ or $y \varnothing x$ are equal.
uncorrected version of the Pearson correlation is that we are removing the excess of variability from the estimated variances of the latent $x$ and $y$, since the sample variances of $X$ and $Y$ always over-estimate them due to the measurement errors $\epsilon_{1}$ and $\epsilon_{2}$ (note that, $\sigma_{X}^{2}=\sigma_{x}^{2}+\sigma_{\epsilon_{1}}^{2}$ and $\sigma_{Y}^{2}=\sigma_{y}^{2}+\sigma_{\epsilon_{2}}^{2}$ ), where $\sigma_{x}^{2}$ and $\sigma_{y}^{2}$ are the variances of $x$ and $y$, respectively.

Although the examples provided here only treat regulatory network models, the proposed approaches can be applied in a straightforward manner also to estimate linear relationships between random variables measured with error.

## Conclusions

Unfortunately, avoiding measurement error in a complete manner is a very difficult task, however, it can be minimized in the measuring (experimental) process and treated during the data analysis step. Here, we have shown evidence that presence of the measurement errors has a high impact in regulatory network models. In order to overcome this problem, approaches in both major data conditions, independent and time series data were proposed in addition to measurement error estimation procedures. Further studies are necessary in order to verify how is the performance of other regulatory networks (Bayesian networks, Structural Equation models, Graphical Gaussian models, Relevance networks, etc) in the presence of measurement error.

Table 6: Gene CLOCK (actual data)


$$
\begin{aligned}
& t\left(\beta_{\text {standard VAR }}\right)=\frac{\beta_{\text {standard VAR }}}{\sqrt{\operatorname{var} \beta_{\text {standard VAR }}}} \\
& t\left(\beta_{\text {corrected VAR }}\right)=\frac{\beta_{\text {corrected VAR }}}{\sqrt{\operatorname{var} \beta_{\text {corrected VAR }}}}
\end{aligned}
$$

## Methods

In this section, standard Ordinary Least Squares and Vector Autoregressive models will be described. Furthermore, corrected methods for measurement error will also be presented. Finally, the model used in the simulations will be detailed.

## Ordinary least squares

In a multivariate regression model, let $x_{1}, x_{2}, \ldots, x_{p}$ be $p$ predictor variables (genes) possibly being related to a response variable $y$ (gene). The conventional linear regression model states that gene $y$ is composed of an intercept or constant $a$ which is the basal expression level of $y$, the predictors or gene expressions $x_{j}$ 's ( $j=$ $1, \ldots, p$ ) which relationship with $y$ is represented by $\beta=$ $\left(\beta_{1}, \ldots, \beta_{p}\right)^{\top}$ (the sign of $\beta_{j}$ represents the relationship between $y$ and $x_{j}$, i.e., positive or negative association), and a random error $\varepsilon$, which accounts for an intrinsic biological variation (this is not the measurement error).

With $n$ independent observations (microarrays) $y$ and the associated gene expression values of $x_{j}$, the complete model becomes

$$
\left\{\begin{array}{l}
y_{i 1}=\alpha_{1}+\beta_{11} x_{i 1}+\beta_{12} x_{i 2}+\ldots+\beta_{1 p} x_{i p}+\varepsilon_{i 1} \\
y_{i 2}=\alpha_{2}+\beta_{21} x_{i 1}+\beta_{22} x_{i 2}+\ldots+\beta_{2 p} x_{i p}+\varepsilon_{i 2} \\
\vdots \\
y_{i q}=\alpha_{q}+\beta_{q 1} x_{i 1}+\beta_{q 2} x_{i 2}+\ldots+\beta_{q p} x_{i p}+\varepsilon_{i q}
\end{array}\right.
$$

for $i=1, \ldots, n$. In matrix notation, it is described as

$$
\mathbf{y}_{i}=\alpha+\beta \mathbf{x}_{i}+\varepsilon_{i}
$$

where

$$
\begin{gathered}
\mathbf{y}_{i}=\left(\begin{array}{c}
y_{i 1} \\
y_{i 2} \\
\vdots \\
y_{i q}
\end{array}\right) \\
\alpha=\left(\begin{array}{c}
\alpha_{1} \\
\alpha_{2} \\
\vdots \\
\alpha_{q}
\end{array}\right) \\
\mathbf{x}_{i}=\left(\begin{array}{c}
x_{i 1} \\
x_{i 2} \\
\vdots \\
x_{i p}
\end{array}\right) \\
\beta=\left(\begin{array}{cccc}
\beta_{11} & \beta_{12} & \cdots & \beta_{1 p} \\
\beta_{21} & \beta_{22} & \cdots & \beta_{2 p} \\
\vdots & \vdots & \ddots & \vdots \\
\beta_{q 1} & \beta_{q 2} & \cdots & \beta_{q p}
\end{array}\right) \\
\varepsilon_{i}=\left(\begin{array}{c}
\varepsilon_{i 1} \\
\varepsilon_{i 2} \\
\vdots \\
\varepsilon_{i q}
\end{array}\right)
\end{gathered}
$$

The entire vector of error terms, $\varepsilon_{i}=\left(\varepsilon_{i 1}, \ldots, \varepsilon_{i q}\right)^{\top}$, are assumed to be independent and identically distributed as a $q$-variate normal distribution with zero vector mean and positive definite covariance matrix $\Sigma_{c}$ for all $i=1, \ldots$, $n$, where $q$ is the number of response variables. Notice that the proposed method is considering the homoscedastic case, i.e., the covariance matrix $\Sigma_{c}$ does not change with $i$. Let $\Sigma_{y x}, \Sigma_{x x}$ and $\Sigma_{y y}$ be the covariances of $(y, x),(x, x)$ and $(y, y)$, respectively. These covariance matrices could be estimated by:

$$
\begin{aligned}
& \hat{\Sigma}_{y x}=n^{-1} \sum_{i=1}^{n}\left(\mathbf{y}_{i}-\overline{\mathbf{y}}\right)\left(\mathbf{x}_{i}-\overline{\mathbf{x}}\right)^{\top} \\
& \hat{\Sigma}_{x x}=n^{-1} \sum_{i=1}^{n}\left(\mathbf{x}_{i}-\overline{\mathbf{x}}\right)\left(\mathbf{x}_{i}-\overline{\mathbf{x}}\right)^{\top}
\end{aligned}
$$

and

$$
\hat{\Sigma}_{y y}=n^{-1} \sum_{i=1}^{n}\left(\mathbf{y}_{i}-\overline{\mathbf{y}}\right)\left(\mathbf{y}_{i}-\overline{\mathbf{y}}\right)^{\top}
$$

where

$$
\overline{\mathbf{x}}=n^{-1} \sum_{i=1}^{n} \mathbf{x}_{i}
$$

and

$$
\overline{\mathbf{y}}=n^{-1} \sum_{i=1}^{n} \mathbf{y}_{i}
$$

Then, the intercept $\alpha$ is estimated as

$$
\hat{\alpha}=\overline{\mathbf{y}}-\hat{\beta} \overline{\mathbf{x}}
$$

and the estimator for the model's coefficient is given by

$$
\hat{\beta}=\hat{\Sigma}_{y x} \hat{\Sigma}_{x x}^{-1}
$$

The asymptotic variance-covariance matrix of $\operatorname{vec}\left(\hat{\beta}^{\top}\right)$ and its estimate are given, respectively, by

$$
\Sigma_{\hat{\beta}}=n^{-1} \Sigma_{\varepsilon} \otimes \Sigma_{x x}^{-1}
$$

and

$$
\hat{\Sigma}_{\hat{\beta}}=n^{-1} \hat{\Sigma}_{\varepsilon} \otimes \hat{\Sigma}_{x x}^{-1}
$$

where $\otimes$ is the Kronecker product and $\hat{\Sigma}_{\varepsilon}=(n-p-1)^{-1} \sum_{i=1}^{n} \hat{\varepsilon}_{i} \hat{\varepsilon}_{i}^{\top}$ (non biased estimator). Notice that, the diagonal elements of $\Sigma_{\hat{\beta}}$ are the variances of the elements of $\hat{\beta}$, say $\Sigma_{\hat{\beta}_{j}}^{2}$ for $j=1, \ldots, p$.

Let $\hat{\mathbf{y}}=\hat{\alpha}+\mathbf{x} \hat{\beta}$ denote the fitted values of $y$, then, the residuals are

$$
\hat{\varepsilon}_{i}=\mathbf{y}_{i}-\hat{\mathbf{y}}_{i}
$$

## Hypothesis testing

The main interest in a simple regression model $\left(\mathbf{y}_{i}=\alpha+\right.$ $\beta \mathbf{x}_{i}+\varepsilon_{i}$ ) lies in testing the strength of the relationship

between the predictor variable (gene) $x$ and the response variable (gene) $y$, in other words, if $\beta$ is equal to a certain value $m$ (in general, $m=0$, i.e., there is or not linear relationship between genes $x$ and $y$ ).

The asymptotic distribution of $\operatorname{vec}\left(\hat{\beta}^{\top}\right)$ is given by

$$
\sqrt{n}\left(\operatorname{vec}\left(\beta^{\top}\right)-\operatorname{vec}\left(\beta^{\top}\right)\right) \xrightarrow{D} N\left(0, \Sigma_{\beta}\right)
$$

and the test is described by:

$$
H_{0}: \operatorname{Cvec}\left(\beta^{\top}\right)=\mathbf{m} \text { versus } H_{1}: \operatorname{Cvec}\left(\beta^{\top}\right) \neq \mathbf{m}
$$

This test may be performed using the Wald-type statistic expressed as

$$
n\left(\operatorname{Cvec}\left(\hat{\beta}^{\top}\right)-\mathbf{m}\right)^{\top}\left[\mathbf{C} \Sigma_{\beta} \mathbf{C}^{\top}\right]^{-1}\left(\operatorname{Cvec}\left(\hat{\beta}^{\top}\right)-\mathbf{m}\right)
$$

where $\mathbf{C}$ is a matrix of contrasts (usually, $\mathbf{C}=\mathbf{I}$ ). For more details about the matrix of contrasts, see [27]. Under the null hypothesis, (20) has a limit $\chi^{2}(d)$ distribution, where $d=\operatorname{rank}(\mathbf{C})$ gives the number of linear restrictions.

## Ordinary least squares with measurement error

Now, we shall study models of the regression type where one is unable to observe expression values of genes $x$ and $y$ (as described before) directly. Instead of observing $x$ and $y$, one observes the sum

$$
\mathbf{X}=\mathbf{x}+\epsilon_{1}
$$

and

$$
\mathbf{Y}=\mathbf{y}+\epsilon_{2}
$$

with

$$
\mathbf{y}=\alpha+\beta \mathbf{x}+\varepsilon
$$

where $\epsilon_{1} \sim N\left(0, \Sigma_{\epsilon_{2}}\right)$ independent of $\epsilon_{2} \sim N\left(0, \Sigma_{\epsilon_{2}}\right)$ with $\Sigma_{\epsilon_{1}}$ and $\Sigma_{\epsilon_{2}}$ known are called as measurement errors, i.e., the variation derived by the measurement process (for example, the measurement error introduced when analyzing microarrays), $\varepsilon \sim N\left(0, \Sigma_{\varepsilon}\right)$ is the random error (intrinsic biological variation) and $\mathbf{x} \sim N\left(\mu_{x}, \Sigma_{x x}\right), \mathbf{y} \sim N$ $\left(\mu_{y}, \Sigma_{y y}\right)$ with $\mu_{y}=\alpha+\beta \mu_{x}$ and $\Sigma_{y y}=\beta \Sigma_{x x} \beta^{\top}+\Sigma_{\varepsilon}$.

The matrices $\Sigma_{\epsilon_{1}}$ and $\Sigma_{\epsilon_{2}}$ are given by

$$
\Sigma_{\epsilon_{2}}=\left(\begin{array}{ccc}
\sigma_{\epsilon_{1} 11}^{2} & \ldots & \sigma_{\epsilon_{2} 1 p}^{2} \\
\vdots & \ddots & \vdots \\
\sigma_{\epsilon_{1} p 1}^{2} & \cdots & \sigma_{\epsilon_{1} p p}^{2}
\end{array}\right)
$$

and

$$
\Sigma_{\epsilon_{2}}=\left(\begin{array}{ccc}
\sigma_{\epsilon_{2} 11}^{2} & \ldots & \sigma_{\epsilon_{2} 1 q}^{2} \\
\vdots & \ddots & \vdots \\
\sigma_{\epsilon_{2} q 1}^{2} & \cdots & \sigma_{\epsilon_{2} q q}^{2}
\end{array}\right)
$$

i.e., the measurement errors may be different for each variable. Notice that the components of the measurement error's vector may be correlated but the entire vectors are independent.

Let $\Sigma_{Y X}, \Sigma_{X X}$ and $\Sigma_{Y Y}$ be the sample covariances of $(Y, X)$, $(X, X)$ and $(Y, Y)$, respectively. These covariance matrices could be estimated by substituting $x$ and $y$ by $X$ and $Y$ in equations (8-12). Then, the intercept $a$ is estimated as

$$
\hat{\alpha}=\overline{\mathbf{Y}}-\hat{\beta} \overline{\mathbf{X}}
$$

and the estimator for the model's coefficient is given by

$$
\hat{\beta}=\hat{\Sigma}_{Y X} \hat{\Sigma}_{x x}^{-1}
$$

where

$$
\hat{\Sigma}_{x x}=\hat{\Sigma}_{X X}-\hat{\Sigma}_{\epsilon_{1}}
$$

Notice that $\hat{\Sigma}_{X X}$ is estimated using equation (10) and $\hat{\Sigma}_{\epsilon_{1}}$ must be known a priori (it can be estimated using the procedures described in the section "Measurement errors estimation").

The asymptotic variance-covariance matrix of $\operatorname{vec}\left(\hat{\beta}^{\top}\right)$ and its estimate are given, respectively, by (the proof is in the Appendix)

$$
\Sigma_{\hat{\beta}}=\Sigma_{\hat{\alpha}} \otimes \Sigma_{\alpha i}^{-1} \cdot\left(\mathbf{I}_{\alpha} \otimes \Sigma_{\alpha i}^{-1}\right)\left(\Sigma_{\hat{\alpha}} \otimes \Sigma_{\epsilon_{1}} \cdot\left(\mathbf{I}_{\alpha} \otimes \Sigma_{\epsilon_{1}}\right)\left(\beta^{\top} \otimes \beta\right)\left(\mathbf{I}_{\alpha} \otimes \Sigma_{\epsilon_{1}}\right)\right)\left(\mathbf{I}_{\alpha} \otimes \Sigma_{\alpha i}^{-1}\right)
$$

and

$$
\hat{\Sigma}_{\hat{\beta}}=\hat{\Sigma}_{\hat{\alpha}} \otimes \hat{\Sigma}_{\alpha i}^{-1} \cdot\left(\mathbf{I}_{\alpha} \otimes \hat{\Sigma}_{\alpha i}^{-1}\right)\left(\hat{\Sigma}_{\hat{\alpha}} \otimes \hat{\Sigma}_{\epsilon_{1}} \cdot\left(\mathbf{I}_{\alpha} \otimes \hat{\Sigma}_{\epsilon_{1}}\right)\left(\hat{\beta}^{\top} \otimes \hat{\beta}\right)\left(\mathbf{I}_{\alpha} \otimes \hat{\Sigma}_{\epsilon_{1}}\right)\right)\left(\mathbf{I}_{\alpha} \otimes \hat{\Sigma}_{\alpha i}^{-1}\right)
$$

where $\mathbf{I}_{q}$ denotes the $q \times q$ identity matrix and

$$
\Sigma_{\beta}=\Sigma_{\varepsilon}+\Sigma_{\epsilon_{2}}+\beta \Sigma_{\epsilon_{1}} \beta^{\top}
$$

Notice that, in the absence of measurement error, i e., $\Sigma_{\epsilon_{1}}=\Sigma_{\epsilon_{2}}=0$ the corrected OLS is exactly equal to standard OLS. Furthermore, it is noteworthy that this asymptotic variance is similar to the one presented by [23] but in a multivariate manner with no correlation in the errors.

## Hypothesis testing

Similar to the OLS with no measurement error, the interest in a simple regression model $\left(\mathbf{y}_{i}=\alpha+\beta \mathbf{x}_{i}+\varepsilon_{i}\right)$ lies in testing the strength of the relationship between the predictor gene $x$ and the response gene $\gamma$. The asymptotic distribution of $\operatorname{vec}\left(\hat{\beta}^{\top}\right)$ is given by

$$
\sqrt{n}\left(\operatorname{vec}\left(\hat{\beta}^{\top}\right)-\operatorname{vec}\left(\beta^{\top}\right)\right) \xrightarrow{D} N\left(0, \Sigma_{\hat{\beta}}\right)
$$

and the test is similar to the previous case (standard OLS) described by:

$$
H_{0}: \operatorname{Cvec}\left(\beta^{\top}\right)=\mathbf{m} \text { versus } H_{1}: \operatorname{Cvec}\left(\beta^{\top}\right) \neq \mathbf{m}
$$

This test may be performed using the Wald-type statistic expressed as

$$
n(\operatorname{Cvec}(\hat{\beta})-\mathbf{m})^{\top}\left[\mathbf{C} \Sigma_{\hat{\beta}} \mathbf{C}^{\top}\right]^{-1}(\operatorname{Cvec}(\hat{\beta})-\mathbf{m})
$$

where $\mathbf{C}$ is a matrix of contrasts. Under the null hypothesis, (33) follows a $\chi^{2}$ distribution with $\operatorname{rank}(\mathbf{C})$ degrees of freedom.

## Vector autoregressive model

Here we define the usual VAR model as defined in Lütkepohl (2006) [28].

Let $\mathbf{z}_{t}=\left(z_{1 t}, \ldots, z_{p t}\right)^{\top}$ be a $(p \times 1)$ vector of time series variables. The usual $\operatorname{VAR}(r)$ model (of order $r$ ) has the form

$$
\mathbf{z}_{t}=\alpha+\beta_{1} \mathbf{z}_{t-1}+\ldots+\beta_{r} \mathbf{z}_{t-r}+\varepsilon_{t}, t=1, \ldots, n
$$

where $n$ is the time series length, $\beta_{j}$ for $j=1, \ldots, p$ are $(p \times p)$ coefficient matrices and $\varepsilon_{t}$ is an $(p \times 1)$ unobservable zero mean white noise vector process with covariance matrix $\Sigma_{c}$. Under stationarity conditions, the mean and autocovariance function are given, respectively, by

$$
\begin{gathered}
E\left(\mathbf{z}_{1}\right)=\mu_{z}=\left(\mathbf{I}_{p}-\sum_{j=1}^{r} \beta_{j}\right)^{-1} \alpha \\
\gamma(h)=E\left(\mathbf{z}_{1}-\mu_{z}\right)\left(\mathbf{z}_{t-h}-\mu_{z}\right)^{\top}=\sum_{j=1}^{r} \beta_{j} \gamma(h-j), \text { for }|h|=1,2,3 \ldots
\end{gathered}
$$

and

$$
\gamma(0)=\sum_{j=1}^{r} \beta_{j} \gamma(h-j)+\Sigma_{\varepsilon}
$$

where $\mathbf{I}_{p}$ denotes the $p \times p$ identity matrix.

The model (34) can be re-written as

$$
\mathbf{z}_{t}=\alpha+\beta \mathbf{z}_{t-r}^{\dagger}+\varepsilon_{t}, t=1, \ldots, n
$$

where $\beta_{j}=\left(\beta_{1} \beta_{2} \ldots \beta_{r}\right)$ is a $p \times p r$ matrix and $\mathbf{z}_{t-r}^{\dagger}=\left(\mathbf{z}_{t-1}^{\top}, \mathbf{z}_{t-2}^{\top}, \ldots, \mathbf{z}_{t-r}^{\top}\right)^{\top}$.

Therefore, if the white noise ( $\varepsilon$ ) has normal distribution, the conditional Maximum Likelihood (ML) estimators of $\alpha, \beta$ and $\Sigma_{\varepsilon}$ are equal to the OLS estimators. They are given, respectively by

$$
\begin{gathered}
\hat{\alpha}=\overline{\mathbf{z}}_{t}-\hat{\beta} \overline{\mathbf{z}}_{t-r}^{\dagger} \\
\hat{\beta}=\left(\mathbf{S}_{\mathbf{z}_{t-r}^{\dagger}}^{-1} \mathbf{S}_{\mathbf{z}_{t-r}^{\dagger} \mathbf{z}_{t}}\right)^{\top}
\end{gathered}
$$

and

$$
\hat{\Sigma}_{\varepsilon}=n^{-1} \sum_{i=1}^{n} \hat{\varepsilon}_{i} \hat{\varepsilon}_{i}^{\top}
$$

where

$$
\begin{gathered}
\overline{\mathbf{z}}_{t-r}^{\dagger}=n^{-1} \sum_{i=1}^{n} \mathbf{z}_{t-r}^{\dagger} \\
\overline{\mathbf{z}}_{t}=n^{-1} \sum_{i=1}^{n} \mathbf{z}_{i} \\
\hat{\varepsilon}_{i}=\mathbf{z}_{i}-\hat{\alpha}-\hat{\beta} \mathbf{z}_{t-r}^{\dagger} \\
\mathbf{S}_{\mathbf{z}_{t-r}^{\dagger}}=n^{-1} \sum_{i=1}^{n}\left(\mathbf{z}_{t-r}^{\dagger}-\overline{\mathbf{z}}_{t-r}^{\dagger}\right) \mathbf{z}_{t-r}^{\dagger \top}
\end{gathered}
$$

and

$$
\mathbf{S}_{\mathbf{z}_{t-r}^{\dagger} \mathbf{z}_{t}}=n^{-1} \sum_{i=1}^{n}\left(\mathbf{z}_{t-r}^{\dagger}-\overline{\mathbf{z}}_{t-r}^{\dagger}\right) \mathbf{z}_{i}^{\top}
$$

The consistence of those conditional ML estimators is assured under the stationary conditions [28]. The covariance function of $\mathbf{z}_{t-r}^{\dagger}$ is given by

$$
\boldsymbol{\Gamma}_{r}(h)=\left(\begin{array}{cccc}
\gamma(h) & \gamma(h+1) & \ldots & \gamma(h+r-1) \\
\gamma(h-1) & \gamma(h) & \ldots & \gamma(h+r-2) \\
\vdots & \vdots & \ddots & \vdots \\
\gamma(h-r+1) & \gamma(h-r+2) & \ldots & \gamma(h)
\end{array}\right)
$$

## Vector autoregressive model with measurement error

Now, the VAR model with measurement error will be presented.

Let $\mathbf{z}_{t}$ be the "true" variables that are not directly observed. Let $\mathbf{Z}_{t}$ be the observed surrogate variables which have an additive structure given by

$$
\mathbf{Z}_{t}=\mathbf{z}_{t}+\epsilon_{t}, t=1, \ldots, n
$$

where $\mathbf{Z}_{t}=\left(Z_{1 t}, Z_{2 t}, \ldots, Z_{p t}\right)^{\top}$ is the surrogate vector and $\epsilon_{t}=\left(\epsilon_{1 t}, \epsilon_{2 t}, \ldots, \epsilon_{p t}\right)^{\top}$ is the measurement error vector. In most cases, if the usual conditional ML estimator is adopted for the observations subject to errors, i.e., replacing $\mathbf{z}_{t}$ with $\mathbf{Z}_{t}$ in the equation (34), the estimator of $\beta$ will be biased as well as its asymptotic variance. Therefore, in order to overcome this limitation the measurement errors should be included in the estimation procedure. Nevertheless, the model (34) plus the equation (48) is not identifiable, since the covariance matrices of $\epsilon_{t}$ and $\epsilon_{t}$ are confounded. This problem can be avoided considering known the variance of $\epsilon_{t}$.

Let $\epsilon_{t} \sim N\left(0, \Sigma_{\epsilon}\right)$ be the measurement error with $\Sigma_{\epsilon}$ known (refer to section Measurement error estimation for details about how to estimate $\Sigma_{\epsilon}$ ). Then, the parameters of the model (34) under measurement errors as in (48) have consistent estimators (Patriota et al.: Vector autoregressive models with measurement errors for testing Granger causality, submitted) given by

$$
\begin{gathered}
\tilde{\alpha}=\overline{\mathbf{Z}}_{t}-\hat{\beta} \overline{\mathbf{Z}}_{t-r}^{\dagger} \\
\hat{\beta}=\left(\left(\mathbf{S}_{\mathbf{z}_{t-r}}^{\dagger}-\mathbf{I}_{r} \otimes \Sigma_{\epsilon}\right)^{-1} \mathbf{S}_{\mathbf{z}_{t-r}^{\dagger} \mathbf{z}_{t}}\right)^{\top}
\end{gathered}
$$

and

$$
\tilde{\Sigma}_{\epsilon}=n^{-1} \sum_{i=1}^{n}\left(\mathbf{Z}_{i}-\tilde{\alpha}-\hat{\beta} \mathbf{Z}_{t-r}^{\dagger}\right)\left(\mathbf{Z}_{i}-\tilde{\alpha}-\hat{\beta} \mathbf{Z}_{t-r}^{\dagger}\right)^{\top}-\Sigma_{\epsilon}-\hat{\beta}\left(\mathbf{I}_{r} \otimes \Sigma_{\epsilon}\right) \hat{\beta}^{\top}
$$

where

$$
\begin{gathered}
\overline{\mathbf{Z}}_{t-r}^{\dagger}=n^{-1} \sum_{i=1}^{n} \mathbf{Z}_{t-r}^{\dagger} \\
\overline{\mathbf{Z}}_{t}=n^{-1} \sum_{i=1}^{n} \mathbf{Z}_{i} \\
\mathbf{S}_{\mathbf{z}_{t-r}^{\dagger}}=n^{-1} \sum_{i=1}^{n}\left(\mathbf{Z}_{t-r}^{\dagger}-\overline{\mathbf{Z}}_{t-r}^{\dagger}\right) \mathbf{Z}_{t-r}^{\dagger \top}
\end{gathered}
$$

Then, the asymptotic distribution of $\operatorname{vec}(\hat{\beta})$ is given by [29].

$$
\sqrt{n}\left(\operatorname{vec}\left(\hat{\beta}^{\top}\right)-\operatorname{vec}\left(\beta^{\top}\right)\right) \xrightarrow{O} N\left(0, \Sigma_{\hat{\beta}}\right)
$$

where the matrix $\Sigma_{\hat{\beta}}$ is given by

$$
\Sigma_{\hat{\beta}}=\Sigma_{v} \otimes \Gamma_{r}(0)^{-1}+\left(\mathbf{I}_{p} \otimes \Gamma_{r}(0)^{-1}\right) \mathbf{A}_{r}\left(\mathbf{I}_{p} \otimes \Gamma_{r}(0)^{-1}\right)
$$

where

$$
\begin{aligned}
\mathbf{A}_{r} & =\Sigma_{v} \otimes\left(\mathbf{I}_{r} \otimes \Sigma_{\epsilon}\right)+\beta^{\top} \otimes\left[\Sigma_{\epsilon} \beta\left(\mathbf{I}_{r} \otimes \Sigma_{\epsilon}\right)\right] \\
& -\sum_{h=1}^{r}\left\{\left(\beta_{h} \Sigma_{\epsilon}\right) \otimes \Gamma_{r}(h)+\left(\Sigma_{\epsilon} \beta_{h}^{\top}\right) \otimes \Gamma_{r}(-h)\right\} \\
& -\sum_{h=1}^{r-1}\left[\beta\left(\mathbf{I}_{-h} \otimes \Sigma_{\epsilon}\right) \beta^{\top}\right] \otimes \Gamma_{r}(h)
\end{aligned}
$$

where $\Sigma_{v}=\Sigma_{\epsilon}+\Sigma_{\epsilon}+\beta\left(\mathbf{I}_{\epsilon} \otimes \Sigma_{\epsilon}\right) \beta^{\top}$ and $\mathbf{J}_{l}$ is a $(r \times r)$ matrix of zeros with one's in the $|l|^{\text {th }}$ diagonal above (below) the main diagonal if $l>0(l<0)$ and $\mathbf{J}_{0}$ is a $(r \times r)$ matrix of zeros.

Notice that, if $r=1$ we have the $\operatorname{VAR}(1)$ model and the asymptotic covariance simplifies to

$$
\Sigma_{\hat{\beta}}=\Sigma_{v} \otimes \gamma(0)^{-1}+\left(\mathbf{I}_{p} \otimes \gamma(0)^{-1}\right) \mathbf{A}_{1}\left(\mathbf{I}_{p} \otimes \gamma(0)^{-1}\right)
$$

where

$$
\mathbf{A}_{1}=\Sigma_{v} \otimes \Sigma_{\epsilon}+\beta^{\top} \otimes\left(\Sigma_{\epsilon} \beta \Sigma_{\epsilon}\right)-\left[\left(\beta \Sigma_{\epsilon}\right) \otimes\left(\gamma(0) \beta^{\top}\right)+\left(\Sigma_{\epsilon} \beta^{\top}\right) \otimes \beta \gamma(0)\right)]
$$

The $i^{\text {th }}$ element of $\operatorname{vec}\left(\hat{\beta}^{\top}\right)$, is asymptotically normally distributed with standard error given by the square root of $i^{\text {th }}$ diagonal element of $\Sigma_{\hat{\beta}}$. Thus, we can construct hypotheses testing on the individual coefficients, or in more general form of contrasts

$$
H_{0}: \operatorname{Cvec}\left(\beta^{\top}\right)=\mathbf{m} \text { versus } H_{1}: \operatorname{Cvec}\left(\beta^{\top}\right) \neq \mathbf{m}
$$

involving coefficients across different equations of the VAR model. It may be tested using the Wald statistic conveniently expressed as

$$
n\left(\operatorname{Cvec}\left(\hat{\beta}^{\top}\right)-\mathbf{m}\right)^{\top}\left(\mathbf{C} \Sigma_{\hat{\beta}} \mathbf{C}^{\top}\right)^{-1}\left(\operatorname{Cvec}\left(\beta^{\top}\right)-\mathbf{m}\right)
$$

where $\mathbf{C}$ is a matrix of contrasts ( $\mathbf{C}=\mathbf{1}$, for instance) and $\mathbf{m}$ is usually a $(p \times 1)$ vector or zeros.

Under the null hypothesis, (59) has a limiting $\chi^{2}(d)$ distribution where $d=\operatorname{rank}(\mathbf{C})$ gives the number of linear restrictions. This test is useful to identify, in a statistical sense (controlling the rate of false positives), which gene (predictor variable) is Granger causing another gene (response variable).

## Measurement error estimation

Here, two methods to estimate measurement error are proposed. One when technical replicates are available and another one in the case when they are not available.

## Technical replicates

When technical replicates are available, measurement error estimation may be performed by applying a strategy extending the methods described by Dahlberg (1940) [30] (more details about Dahlberg's method in the Appendix). For microarray data, it is known that the variance varies along the spots (heteroscedasticity) due to variations in experimental conditions (efficiency of dye incorporation, washing process, etc) [31]. Moreover, it is known that Dahlberg's approach is not suitable in the presence of systematic errors. Therefore, the application of the Dahlberg's formula is not straightforward. In order to overcome this problem, we suggest the following algorithm [32].

Let $W$ and $W^{\prime}$ be two microarrays, where $W^{\prime}$ is the technical replicate of $W$.

1. Perform a non-linear regression such as splines smoothing between $\log (W)$ and $\log \left(W^{\prime}\right)$, i.e., $\log \left(W^{\prime}\right)=$ $f(\log (W))+\varepsilon_{1}$. Notice that the logarithm was calculated as a variance stabilizer (due to the high variance observed in microarray data). This is a common practice in microarray analysis;
2. Apply again the splines smoothing between $\varepsilon_{1}^{2}$ and $\log (W)$, i.e., $\varepsilon_{1}^{2}=g(\log (W))+\varepsilon_{2}$;
3. Calculate $\hat{\delta}=\frac{g(\log (W))}{2}$. This is a possible estimate for the standard deviation of the measurement error. Notice that with this process, we obtain one $\hat{\delta}_{i}$ for each spot $i=1, \ldots, m$, where $m$ is the number of spots in the microarray, also in the presence of heteroscedasticity.

## No technical replicates

However, unfortunately, technical replicates is not always available. To this case, we have developed a strategy based on negative control probes and housekeeping genes frequently provided in commercial microarrays. Technically, housekeeping genes and negative controls should not change their expression levels [33]. Therefore, any variation measured by them can be understood as measurement error. In order to overcome the problem of heteroscedasticity in microarrays, we present a method based on splines smoothing. The main idea of this method consists in estimating how much of the total variance (intrinsic biological variation + measurement error) is due to measurement error. The method is as follows:

1. Let $S$ be the set of all probes in the microarray and $H$ be the set of housekeeping genes and negative controls. Calculate the mean and variance for each probe of $S$ and $H$;
2. Perform a splines smoothing in both sets of probes separately, i.e., a splines smoothing $\operatorname{var}(H)=f(\operatorname{mean}$ $(H))+\varepsilon_{1}$ and $\operatorname{var}(S \backslash\{H\})=g(\operatorname{mean}(S \backslash\{H\}))+\varepsilon_{2}$, where $H$ is a matrix containing the expression values of each housekeeping gene and negative controls in each row and $S \backslash\{H\}$ is a matrix containing the expression values of the remaining set of probes in each row. The functions $f$ and $g$ may be represented by a linear combination of spline functions $\varphi_{j}(\cdot)$, i.e., they may be written as

$$
f(\cdot)=\sum_{j=1}^{d} c_{j} \phi_{j}(\cdot)
$$

where $d$ is the number of knots used in the spline expansion ( $d$ may be obtained by selecting the value that minimizes the Generalized Cross Validation). mean $(H)$ and $\operatorname{var}(H)$ (or mean(S $\backslash\{H\}$ ) and $\operatorname{var}(S \backslash$ $\{H\})$ ) are vectors containing the mean and variance values of each row of $H$ (or $S \backslash\{H\}$ ), respectively. In this step, the smoothed curves $\hat{f}$ and $\hat{g}$ represent the estimated variance for each probe. Notice that the smoothed curve in housekeeping genes and negative controls $\hat{f}$ represents the estimated measurement error for each gene expression level. Moreover, the smoothed curve in the remaining set of probes $\hat{g}$ represents the total variance (intrinsic biological variance + measurement error) for each gene expression level;
3. Divide the smoothed curve $\hat{f}$ (obtained in step 2) by the other smoothed curve $\hat{g}$. Notice that this ratio $\left(\hat{f} / \hat{g}\right)$ is the estimation of measurement error in percentage of the total variance for each probe. With this percentage, it is possible to estimate the variance of the measurement error for each probe.

## Simulations

In order to evaluate the behavior of both, standard and proposed methods, we have conducted two simulations in small, moderate and large samples sizes (50, 100, 200 and 400). Computations were performed on the R software (a free software environment for statistical computing and graphics) [34]. For each group of simulation, 10,000 Monte Carlo samples were generated. Simulation I is for independent data and Simulation II for time series data.

## Simulation I - independent data

In order to evaluate the performance of both, usual and corrected OLS methods, a controlled structure was defined. Let $x$ and $y$ be gene expression values where

one is interested in examining if a certain gene $x_{i}(i=1, \ldots$, $p ; p=9)$ is linearly correlated to gene $y(q=1)$ partialized by other genes. This situation can be represented by the following structure

$$
y=\beta_{1} x_{1}+\beta_{2} x_{2}+\beta_{3} x_{3}+\beta_{4} x_{4}+\beta_{5} x_{5}+\beta_{6} x_{6}+\beta_{7} x_{7}+\beta_{8} x_{8}+\beta_{9} x_{9}+\varepsilon
$$

where

$$
\beta=\left(\begin{array}{c}
0 \\
-0.1 \\
-0.2 \\
-0.3 \\
-0.4 \\
0.5 \\
0.6 \\
0.7 \\
0.8
\end{array}\right)
$$

The observed variables $X_{i}(i=1, \ldots, 9)$ and $Y$ are defined by

$$
\begin{aligned}
& X_{i}=x_{i}+\epsilon_{1} \\
& Y=y+\epsilon_{2}
\end{aligned}
$$

where $x_{i} \sim N(0,1), \varepsilon \sim N\left(0, \Sigma_{c}\right)$ is the intrinsic biological random variation and $\epsilon_{1} \sim N\left(0, \Sigma_{\epsilon_{1}}\right)$ independent of $\epsilon_{2} \sim N\left(0, \Sigma_{\epsilon_{2}}\right)$ are the measurement errors, with $\Sigma_{\epsilon_{1}}=$ $\Sigma_{\epsilon_{2}}$ varying from 0 to 0.8 . The standard deviation $\Sigma_{c}$ is defined by

$$
\Sigma_{\varepsilon}^{(9 \times 9)}=\left(\begin{array}{cccc}
1 & 0.2 & \ldots & 0.2 \\
0.2 & 1 & \ddots & \vdots \\
\vdots & \ddots & \ddots & 0.2 \\
0.2 & \ldots & 0.2 & 1
\end{array}\right)
$$

In order to become the simulation more realistic (since actual biological gene expression signals are generally quite correlated), notice that $\Sigma_{c}$ is not a diagonal matrix, i.e., there are little correlations between the predictors. The sample's size varied from 50 to 400 .

## Simulation II - time series data

In the time series case, the data has some peculiarities which are not present in the independent data. Time series data are known to be autocorrelated (past values associated with future values) and also contemporaneously correlated (contemporaneous correlation between time series). Considering these characteristics, a similar structure described in the previous section was designed. Let $X_{t}$ and $Y_{t}$ being gene expression time series data and one is interested in verifying if certain gene $x_{i, t}$ $(i=1, \ldots, p ; p=9)$ Granger causes gene $y_{t}(q=1)$. This
problem can be modeled by a VAR process of order one as described below:

$$
\begin{aligned}
y_{t}= & \beta_{0} y_{t-1}+\beta_{1} x_{1, t-1}+\beta_{2} x_{2, t-1}+\beta_{3} x_{3, t-1}+\beta_{4} x_{4, t-1}+\beta_{5} x_{5, t-1} \\
& +\beta_{6} x_{8, t-1}+\beta_{7} x_{7, t-1}+\beta_{8} x_{8, t-1}+\beta_{9} x_{9, t-1}+\varepsilon_{t}
\end{aligned}
$$

where

$$
\beta=\left(\begin{array}{c}
0 \\
0 \\
-0.1 \\
-0.2 \\
-0.3 \\
-0.4 \\
0.5 \\
0.6 \\
0.7 \\
0.8
\end{array}\right)
$$

and

$$
x_{i, t}=0.5 x_{i, t-1}+\varepsilon_{t} i=1, \ldots, 9
$$

The observed variables $X_{t}$ and $Y_{t}$ are defined by

$$
\begin{aligned}
& X_{t}=x_{t}+\epsilon_{1} \\
& Y_{t}=y_{t}+\epsilon_{2}
\end{aligned}
$$

where $\varepsilon \sim N\left(0, \Sigma_{c}\right)$ is the intrinsic biological random variation and $\epsilon_{1} \sim N\left(0, \Sigma_{\epsilon_{1}}\right)$ independent of $\epsilon_{2} \sim$ $N\left(0, \Sigma_{\epsilon_{2}}\right)$ are the measurement errors, where $\Sigma_{\epsilon_{1}}=\left(\begin{array}{ccc}\sigma_{x, 11}^{2} & \ldots & \sigma_{x, 1 p}^{2} \\ \vdots & \ddots & \vdots \\ \sigma_{x, p 1}^{2} & \ldots & \sigma_{x, p p}^{2}\end{array}\right)$, varies from 0 to 0.8 . The standard deviation $\Sigma_{c}$ is defined by

$$
\Sigma_{\varepsilon}^{(10 \times 10)}=\left(\begin{array}{cccc}
1 & 0.2 & \ldots & 0.2 \\
0.2 & 1 & \ddots & \vdots \\
\vdots & \ddots & \ddots & 0.2 \\
0.2 & \ldots & 0.2 & 1
\end{array}\right)
$$

The time series length varied from 50 to 400 .
Notice that $\beta_{0}$ is the autoregressive coefficient and all time series $X_{i}$ for $i=1, \ldots, 9$ are autocorrelated and also contemporaneously correlated ( $\Sigma_{c}$ is not a diagonal matrix).

## Actual biological data

The standard and proposed OLS methods were applied to lung cancer gene expression data collected by [35]. This dataset is composed of 400 microarrays, each of

which constructed using a different cDNA obtained from a different patient. Standard and corrected VAR approaches were applied to mouse liver time series data collected by [36]. This data is composed by 48 time points distributed at intervals of 1 hour.

## Authors' contributions

AF has made substantial contributions to the conception, design and implementation of the study, and has also been responsible for drafting the manuscript. AGP has made substantial contributions to the development of the methods. JRS has made contributions to data analysis. SM has discussed the results and critically revised the manuscript. All authors read and approved the final version of the manuscript.

## Appendix

## Proof of the asymptotic variance of $\beta$ - equation (29)

Here, we proof equation (29), i.e., the asymptotic variance of $\beta$ in the multivariate case with no correlated errors.

Consider the following model:

$$
\begin{aligned}
& \mathbf{y}_{i}=\alpha+\beta \mathbf{x}_{i}+\varepsilon_{i} \\
& \mathbf{X}_{i}=\mathbf{x}_{i}+\epsilon_{1 i} \\
& \mathbf{Y}_{i}=\mathbf{y}_{i}+\epsilon_{2 i}
\end{aligned}
$$

where $\mathbf{X}_{i}$ and $\mathbf{Y}_{i}$ are the observed vectors with dimensions $p \times 1$ and $q \times 1$, respectively, $\alpha$ is the model intercept ( $q \times$ 1), $\beta$ is a $(q \times p)$ matrix of slope parameters, $\varepsilon_{i}$ is a white noise vector with mean zero and covariance matrix $\Sigma_{c}$. The joint distribution of $\epsilon_{1 i}, \epsilon_{2 i}, \varepsilon_{i}$ and $\mathbf{x}_{i}$ is given by

$$
\left(\begin{array}{c}
\varepsilon_{i} \\
\epsilon_{1 i} \\
\varepsilon_{2 i} \\
\mathbf{x}_{i}
\end{array}\right) \sim N_{2(q+p)}\left(\left(\begin{array}{c}
\mathbf{0} \\
\mathbf{0} \\
\mathbf{0} \\
\mu_{x}
\end{array}\right),\left[\begin{array}{cccc}
\Sigma_{c} & \mathbf{0} & \mathbf{0} & \mathbf{0} \\
\mathbf{0} & \Sigma_{c_{1}} & \mathbf{0} & \mathbf{0} \\
\mathbf{0} & \mathbf{0} & \Sigma_{c_{2}} & \mathbf{0} \\
\mathbf{0} & \mathbf{0} & \mathbf{0} & \Sigma_{x x}
\end{array}\right]\right)
$$

In this section, we investigate the asymptotic distribution of

$$
\hat{\beta}=\hat{\Sigma}_{Y X} \hat{\Sigma}_{x x}^{-1}
$$

where

$$
\hat{\Sigma}_{Y X}=n^{-1} \sum_{i=1}^{n}\left(\mathbf{Y}_{i}-\overline{\mathbf{Y}}_{i}\right)\left(\mathbf{X}_{i}-\overline{\mathbf{X}}_{i}\right)^{\top}, \quad \hat{\Sigma}_{x x}=\hat{\Sigma}_{X X}-\Sigma_{c_{1}}
$$

and

$$
\hat{\Sigma}_{X X}=n^{-1} \sum_{i=1}^{n}\left(\mathbf{X}_{i}-\overline{\mathbf{X}}_{i}\right)\left(\mathbf{X}_{i}-\overline{\mathbf{X}}_{i}\right)^{\top}
$$

The proof idea, similar to presented in [23], has two main steps. The first step consists in showing that vec $\left(\hat{\beta}^{\top}\right)-\operatorname{vec}\left(\beta^{\top}\right)$ can be written as linear combinations of a vectorial mean. In the second one, we must demonstrate that this vectorial mean has an asymptotic normal distribution. Therefore, we need some auxiliar results for proving the asymptotic result, which are exposed in two propositions below.

Proposition 1 Under the model (61) under (62) the proposed estimator $\hat{\beta}$ has the following relationship

$$
\operatorname{vec}\left(\hat{\beta}^{\top}\right)-\operatorname{vec}\left(\beta^{\top}\right)=\left(\mathbf{I}_{q} \otimes \Sigma_{x x}^{-1}\right) \overline{\mathbf{W}}+\mathcal{O}_{\text {prob }}\left(n^{-1}\right)
$$

where

$$
\overline{\mathbf{W}}=n^{-1} \sum_{i=1}^{n}\left(\begin{array}{c}
\mathbf{w}_{1 i} \\
\vdots \\
\mathbf{w}_{q i}
\end{array}\right)=n^{-1} \sum_{i=1}^{n} \mathbf{w}_{i}
$$

with $\mathbf{W}_{i}=\left(\varepsilon_{i}+\epsilon_{2 i}-\beta \epsilon_{1 i}\right) \otimes\left(\mathbf{x}_{i}-\mu_{x}+\epsilon_{1 i}\right)-\boldsymbol{\Psi}, \boldsymbol{\Psi}=\left(\mathbf{I}_{q} \otimes\right.$ $\left.\Sigma_{c_{1}}\right) \operatorname{vec}\left(\beta^{\top}\right)$ and $b_{n}=\mathcal{O}_{\text {prob }}\left(n^{-1}\right)$ means that $n b_{n}$ is limited in probability when $n$ diverges. It implies that, $\sqrt{n} \mathcal{O}_{\text {prob }}\left(n^{-1}\right)_{\text {prob }}\left(n^{-1}\right)$ goes to zero when $n$ increases.

Proof: Define $\beta_{k}$ as the coefficients associated with the $k^{t h}$ element of the vector $\mathbf{y}_{i}$, that is

$$
y_{k i}=\alpha_{k}+\beta_{k}^{\top} \mathbf{x}_{i}+\varepsilon_{k i}
$$

Thus, we have that $\operatorname{vec}\left(\beta^{\top}\right)=\left(\beta_{1}^{\top}, \beta_{2}^{\top}, \cdots, \beta_{q}^{\top}\right)^{\top}$ and its estimator can be written as $\operatorname{vec}(\hat{\beta})=\left(\hat{\beta}_{1}^{\top}, \hat{\beta}_{2}^{\top}, \ldots, \hat{\beta}_{q}^{\top}\right)^{\top}$, where $\hat{\beta}_{k}=\left(\hat{\Sigma}_{X X}-\Sigma_{c_{1}}\right)^{-1} \hat{\Sigma}_{X X_{k}}$ and $\hat{\Sigma}_{X Y_{k}}=n^{-1} \sum_{i=1}^{n}\left(\mathbf{x}_{i}-\overline{\mathbf{x}}\right) Y_{k i}$ for $k=1, \ldots, q$. Moreover, the model (61) may be rewritten in terms of the observed variables as

$$
\begin{aligned}
& \mathbf{Y}_{i}=\alpha+\beta \mathbf{X}_{i}+\vartheta_{i} \\
& \vartheta_{i}=\varepsilon_{i}+\epsilon_{2 i}-\beta \epsilon_{1 i}
\end{aligned}
$$

and for the $k^{t h}$ element of $\mathbf{Y}_{i}$ we have

$$
\begin{aligned}
& Y_{k i}=\alpha_{k}+\beta_{k}^{\top} \mathbf{X}_{i}+\vartheta_{k i} \\
& \vartheta_{k i}=\varepsilon_{k i}+\epsilon_{2, k i}-\beta_{k}^{\top} \epsilon_{1 i}
\end{aligned}
$$

where $\epsilon_{2 i}=\left(\epsilon_{2,1 i}, \ldots, \epsilon_{2, q i}\right)^{\top}$.
Then, it follows that

$$
\hat{\Sigma}_{X Y_{k}}=n^{-1} \sum_{i=1}^{n}\left(\mathbf{X}_{i}-\overline{\mathbf{X}}\right)\left(\alpha_{k}+\beta_{k}^{\top} \mathbf{X}_{i}+\vartheta_{k i}\right)=\hat{\Sigma}_{X X} \beta_{k}+\hat{\Sigma}_{X \vartheta_{k}}
$$

where $\hat{\mathbf{x}}_{x \partial_{k}}=n^{-1} \sum_{i=1}^{n}\left(\mathbf{x}_{i}-\overline{\mathbf{x}}\right) \partial_{k i}=n^{-1} \sum_{i=1}^{n}\left(\mathbf{x}_{i}-\mu_{x}+\epsilon_{i i}\right) \partial_{k i}+\mathcal{O}_{\text {prob }}\left(n^{-1}\right)$. Thus, denoting $\mathbf{\Sigma}_{x \partial k}=n^{-1} \sum_{i=1}^{n}\left(\mathbf{x}_{i}-\mu_{x}+\epsilon_{1 i}\right) \partial_{k i}$ we have that

$$
\hat{\mathbf{\Sigma}}_{X Y_{k}}=\left(\hat{\mathbf{\Sigma}}_{X X}-\mathbf{\Sigma}_{\epsilon_{1}}\right) \boldsymbol{\beta}_{k}+\mathbf{\Sigma}_{x \partial_{k}}-\boldsymbol{\Psi}_{k}+\mathcal{O}_{\text {prob }}\left(n^{-1}\right)
$$

with $\boldsymbol{\Psi}_{k}=-\boldsymbol{\Sigma}_{\epsilon_{1}} \boldsymbol{\beta}_{k}$. As a result, we have

$$
\hat{\boldsymbol{\beta}}_{k}=\boldsymbol{\beta}_{k}+\left(\mathbf{I}_{q} \otimes \mathbf{\Sigma}_{x x}\right)^{-1} \widehat{\mathbf{W}}_{k}+\mathcal{O}_{\text {prob }}\left(n^{-1}\right)
$$

where $\widehat{\mathbf{W}}_{k}=n^{-1} \sum_{i=1}^{n} \mathbf{W}_{k i}$ and $\mathbf{W}_{k i}=\left(\mathbf{x}_{i}-\mu_{x}+\epsilon_{1 i}\right) \boldsymbol{\vartheta}_{k i}-\boldsymbol{\Psi}_{k}$. Hence, it follows that

$$
\operatorname{vec}\left(\hat{\boldsymbol{\beta}}^{\top}\right)-\operatorname{vec}\left(\boldsymbol{\beta}^{\top}\right)=\left(\mathbf{I}_{q} \otimes \mathbf{\Sigma}_{x x}^{-1}\right) \widehat{\mathbf{W}}+\mathcal{O}_{\text {prob }}\left(n^{-1}\right)
$$

where

$$
\widehat{\mathbf{W}}=n^{-1} \sum_{i=1}^{n}\binom{\mathbf{W}_{1 i}}{\frac{1}{i}}=n^{-1} \sum_{i=1}^{n} \mathbf{W}_{i}
$$

with $\mathbf{W}_{i}=\left(\varepsilon_{i}+\epsilon_{2 i}-\beta \epsilon_{1 i}\right) \otimes\left(\mathbf{x}_{i}-\mu_{x}+\epsilon_{1 i}\right)-\boldsymbol{\Psi}$ and $\boldsymbol{\Psi}=\left(\mathbf{I}_{q} \otimes\right.$ $\left.\sum_{\epsilon_{1}}\right) \operatorname{vec}\left(\beta^{\top}\right)$.

Proposition 2 Under all conditions stated in this paper, the mean $\widehat{\mathbf{W}}$ of Proposition has an asymptotic distribution given by

$$
\sqrt{n} \widehat{\mathbf{W}} \xrightarrow{\mathcal{D}} N(0, \mathbf{T})
$$

where " $\xrightarrow{\mathcal{D}}$ means "converge in distribution to",

$$
\mathbf{T}=\mathbf{\Sigma}_{\partial} \otimes \mathbf{\Sigma}_{x x}+\mathbf{\Sigma}_{\partial} \otimes \mathbf{\Sigma}_{\epsilon_{1}}+\left(\mathbf{I}_{q} \otimes \mathbf{\Sigma}_{\epsilon_{1}}\right)\left(\boldsymbol{\beta}^{\top} \otimes \boldsymbol{\beta}\right)\left(\mathbf{I}_{q} \oplus \mathbf{\Sigma}_{\epsilon_{1}}\right)
$$

and $\mathbf{\Sigma}_{\partial}=\mathbf{\Sigma}_{\varepsilon}+\mathbf{\Sigma}_{\varepsilon_{2}}+\boldsymbol{\beta} \mathbf{\Sigma}_{\varepsilon_{1}} \boldsymbol{\beta}^{\top}$
Proof: Notice that the expectation of $\mathbf{W}_{i}$ is equal to zero for all $i$. Then, defining $\tilde{x}=n^{-1} \sum_{i=1}^{n} x_{i}$, where $x_{i}=$ $\delta^{\top} \mathbf{W}_{i}$ we have that $\mathrm{E}\left(x_{i}\right)=0, \operatorname{Var}\left(x_{i}\right)=\delta^{\top} \mathrm{E}\left(\mathbf{W}_{i} \mathbf{W}_{i}^{\top}\right) \delta$ and

$$
\begin{aligned}
E\left(\mathbf{W}_{i} \mathbf{W}_{i}^{\top}\right) & =E\left[\mathbf{F}_{i} \otimes\left(\mathbf{x}_{i}-\mu_{x}\right)\left(\mathbf{x}_{i}-\mu_{x}\right)^{\top}\right]+E\left[\mathbf{F}_{i} \otimes \epsilon_{1 i} \epsilon_{1 i}^{\top}\right] \\
& +E\left[\mathbf{F}_{i} \otimes \epsilon_{1 i}\left(\mathbf{x}_{i}-\mu_{\mathbf{z}}\right)^{\top}\right]+E\left[\mathbf{F}_{i} \otimes\left(\mathbf{x}_{i}-\mu_{x}\right) \epsilon_{1 i}^{\top}\right] \\
& -\boldsymbol{\Psi} \boldsymbol{\Psi}^{\top}
\end{aligned}
$$

with $\mathbf{F}_{i}=\left(\varepsilon_{i}+\epsilon_{2 i}-\beta \epsilon_{1 i}\right)\left(\varepsilon_{i}+\epsilon_{2 i}-\beta \epsilon_{1 i}\right)^{\top}$. Thus, using the fact that the random quantities have independent normal distributions and we have that

$$
E\left(\mathbf{W}_{i} \mathbf{W}_{i}^{\top}\right)=\mathbf{\Sigma}_{\partial} \otimes \mathbf{\Sigma}_{x x}+\mathbf{\Sigma}_{\partial} \otimes \mathbf{\Sigma}_{\epsilon_{1}}+\left(\mathbf{I}_{q} \otimes \mathbf{\Sigma}_{\epsilon_{1}}\right)\left(\boldsymbol{\beta}^{\top} \otimes \boldsymbol{\beta}\right)\left(\mathbf{I}_{q} \oplus \mathbf{\Sigma}_{\epsilon_{1}}\right)
$$

That is, $x_{1} \ldots, x_{n}$ is an iid sequence and we can use the central limit theory, which says that

$$
\sqrt{n} \tilde{x} \xrightarrow{\mathcal{D}} N(0, V)
$$

where $V=\delta^{\top} \mathrm{T} \delta$ with $\mathbf{T}=\mathbf{\Sigma}_{\partial} \otimes \mathbf{\Sigma}_{x x}+\mathbf{\Sigma}_{\partial} \otimes \mathbf{\Sigma}_{\epsilon_{1}}+\left(\mathbf{I}_{q} \otimes \mathbf{\Sigma}_{\epsilon_{1}}\right)\left(\boldsymbol{\beta}^{\top} \otimes \boldsymbol{\beta}\right)\left(\mathbf{I}_{q} \otimes \mathbf{\Sigma}_{\epsilon_{1}}\right)$. As $\sqrt{n} \delta^{\top} \widehat{\mathbf{W}}$ is asymptotically normally distributed for all $\delta \neq 0$, then, by the Cramer-Wold device [37], we have that

$$
\sqrt{n} \widehat{\mathbf{W}} \xrightarrow{\mathcal{D}} N(\mathbf{0}, \mathbf{T})
$$

Then, by the Propositions (1) and (2), we have that

$$
\sqrt{n}\left(\operatorname{vec}\left(\hat{\beta}^{\top}\right)-\operatorname{vec}\left(\beta^{\top}\right)\right) \xrightarrow{\mathcal{D}} N\left(\mathbf{0}, \mathbf{\Sigma}_{\beta}\right)
$$

where $\mathbf{\Sigma}_{\hat{\beta}}=\left(\mathbf{I}_{q} \otimes \mathbf{\Sigma}_{x x}^{-1}\right) \mathbf{T}\left(\mathbf{I}_{q} \otimes \mathbf{\Sigma}_{x x}^{-1}\right)$.

## Dahlberg's error

Consider the following model:

$$
Z_{i j}=\mu_{i}+\epsilon_{i j}
$$

where $Z_{i j}$ is the measure obtained in one experiment (microarray), $i$ is the sample index $i=1, \ldots, m, m$ is the number of spost in the microarray, $j$ is the replicate number ( $j=1,2$ in the case of duplicates), $\mu_{i}$ is the unknown true value of the measure and $\epsilon_{i j}$ is the error of measure.

Then, assume that $E\left(\epsilon_{i j}\right)=0$ and $\operatorname{Var}\left(\epsilon_{i j}\right)=\delta_{\epsilon}^{2}$. Thus, one quantification of the quality of measure is the standard deviation of $\epsilon_{i j}$, i.e., $\delta_{\epsilon}$. Notice that the lower is the standard deviation of the error of measure $\left(\delta_{\epsilon}\right)$, the lower is the measurement error.

Consider

$$
d_{i}=Z_{i 2}-Z_{i 1}
$$

Therefore

$$
\operatorname{Var}\left(d_{i}\right)=\operatorname{Var}\left(\epsilon_{i 2}-\epsilon_{i 1}\right)=2 \delta_{\epsilon}^{2}
$$

Assuming that there is no bias (systematic error), one intuitive estimator for $2 \delta_{\epsilon}^{2}$ is

$$
2 \hat{\delta}_{\epsilon}^{2}=\sum_{i=1}^{m} \frac{d_{i}^{2}}{m}
$$

The quantity $\hat{\delta}_{\epsilon}=\sqrt{\sum_{i=1}^{m} \frac{d_{i}^{2}}{2 m}}$ is exactly the Dahlberg's formula proposed in [30].

## Acknowledgements

This research was supported by grants from RIKEN and FAPESP.

## Publish with Bio Med Central and every

scientist can read your work free of charge
"BioMed Central will be the most significant development for disseminating the results of biomedical research in our lifetime."

Sir Paul Nurse, Cancer Research UK
Your research papers will be:

- available free of charge to the entire biomedical community
- peer reviewed and published immediately upon acceptance
- cited in PubMed and archived on PubMed Central
- yours - you keep the copyright

Submit your manuscript here:
http://www.biomedcentral.com/info/publishing_adv.asp
BioMedcentral