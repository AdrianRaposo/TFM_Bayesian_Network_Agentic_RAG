# RESEARCH METHODS 

## Prior Choices of Between-Study Heterogeneity in Contemporary Bayesian Network Meta-analyses: an Empirical Study

Kristine J. Rosenberger, MS ${ }^{1}$, Aiwen Xing, MS ${ }^{1}$, Mohammad Hassan Murad, MD ${ }^{2}$, Haitao Chu, MD, PhD ${ }^{3}$, and Lifeng Lin, PhD ${ }^{1}$ (D)<br>${ }^{1}$ Department of Statistics, Florida State University, Tallahassee, FL, USA; ${ }^{2}$ Evidence-Based Practice Center, Mayo Clinic, Rochester, MN, USA; ${ }^{3}$ Division of Biostatistics, University of Minnesota, Minneapolis, MN, USA.

BACKGROUND: Network meta-analysis (NMA) is a popular tool to compare multiple treatments in medical research. It is frequently implemented via Bayesian methods. The prior choice of between-study heterogeneity is critical in Bayesian NMAs. This study evaluates the impact of different priors for heterogeneity on NMA results.
METHODS: We identified all NMAs with binary outcomes published in The BMJ, JAMA, and The Lancet during 2010-2018, and extracted information about their prior choices for heterogeneity. Our primary analyses focused on those with publicly available full data. We re-analyzed the NMAs using 3 commonly-used non-informative priors and empirical informative log-normal priors. We obtained the posterior median odds ratios and $95 \%$ credible intervals of all comparisons, assessed the correlation among different priors, and used Bland-Altman plots to evaluate their agreement. The kappa statistic was also used to evaluate the agreement among these priors regarding statistical significance.
RESULTS: Among the selected Bayesian NMAs, 52.3\% did not specify the prior choice for heterogeneity, and $84.1 \%$ did not provide rationales. We re-analyzed 19 NMAs with full data available, involving 894 studies, 173 treatments, and 395,429 patients. The correlation among posterior median (log) odds ratios using different priors were generally very strong for NMAs with over 20 studies. The informative priors produced substantially narrower credible intervals than non-informative priors, especially for NMAs with few studies. Bland-Altman plots and kappa statistics indicated strong overall agreement, but this was not always the case for a specific NMA.
CONCLUSIONS: Priors should be routinely reported in Bayesian NMAs. Sensitivity analyses are recommended to examine the impact of priors, especially for NMAs with relatively small sample sizes. Informative priors may produce substantially narrower credible intervals for such NMAs.

KEY WORDS: Bayesian analysis; heterogeneity; network meta-analysis; prior distribution; sensitivity analysis.

[^0]J Gen Intern Med 36(4):1049-57
DOI: 10.1007/s11606-020-06357-1
(c) Society of General Internal Medicine 2021

## INTRODUCTION

Network meta-analysis (NMA) is a statistical method often used to draw conclusions about multiple-treatment comparisons. ${ }^{1-3}$ It simultaneously synthesizes both direct and indirect evidence, where the direct evidence comes from head-to-head trials while the indirect evidence comes from indirect comparisons with common comparators. ${ }^{4,5}$ For example, the comparison between two active drugs A and B can be informed from indirect comparisons of A vs. C and B vs. C, where C may be placebo or standard care, or from direct comparison in clinical trials comparing A vs. B.

In addition to the advantage of combining direct and indirect evidence, NMAs improve the precision of estimates (i.e., make the confidence/credible intervals narrower). ${ }^{6,7}$ This precision however is affected by the amount of heterogeneity between studies, because heterogeneity is modeled into the uncertainty and impacts the width of confidence/credible intervals. ${ }^{8,9}$ Currently, many NMAs are performed via a Bayesian framework that uses a prior distribution for the betweenstudy heterogeneity. ${ }^{10}$ Some NMAs use the traditionally nonor weakly informative priors for heterogeneity. ${ }^{11-13}$ Recently, Turner et al. ${ }^{14}$ have suggested informative log-normal priors based on a large database of conventional pairwise metaanalyses in the Cochrane Library. These empirical priors have the potential to improve the precision of the treatment effect estimates, especially when the number of studies is small.

The choice of prior distribution is important and should be explicitly reported according to the PRISMA-NMA statement (Preferred Reporting Items for Systematic Reviews and MetaAnalyses extension for Network Meta-Analysis). ${ }^{15}$ It is critical that authors of NMAs describe the details of choices and assumptions made to select the prior distribution for transparency purposes and to allow reproducibility of the work. Nevertheless, it has been found that the rapid growth of NMAs published in recent years was not accompanied with better methodological and reporting quality. ${ }^{16,17}$ Therefore, we


[^0]:    Supplementary Information The online version contains supplementary material available at https://doi.org/10.1007/s11606-020-06357-1.
    Received March 30, 2020
    Accepted November 22, 2020
    Published online January 5, 2021

conducted this empirical study to assess recent NMAs published in high-impact medical journals for the quality of reporting heterogeneity priors (in terms of distribution and rationale) and to evaluate how NMAs' conclusions would differ based on applying various commonly used prior distributions.

## METHODS

## Data Collection

We designed and executed a literature search in July, 2019, for research articles published in The BMJ, JAMA, and The Lancet between January 1, 2010, and December 31, 2018, using the terms "network meta-analysis," "network meta-analyses," "multiple-treatment comparison," "multiple-treatment metaanalysis," and "multiple-treatment meta-analyses." If Bayesian models were used, we examined if the original articles gave information about prior choices for heterogeneity and their rationales.

In our primary analyses, we excluded methodological reviews that did not present original data. The outcome type was restricted to be binary, because the heterogeneity may depend on the measure scale for other outcome types (e.g., for continuous outcomes) and needed to be modeled on a case-bycase basis. In addition, we focused on articles whose full NMA datasets were publicly available. Originally reported effect measures, outcomes, studies, treatments, event counts, sample sizes, statistical methods (frequentist or Bayesian) used for NMAs, and prior distributions (for Bayesian NMAs) were obtained from the published articles (and the corresponding supplemental files). If the authors used the Bayesian method but did not report their prior distributions, we contacted them for information about the priors. An article may report multiple NMAs with various outcomes; our analyses focused on the primary outcome. If no primary outcome was specified, we used the NMA with the largest number of studies. In addition, regardless the original effect measures, we re-analyzed the collected data based on the odds ratio (OR) (on a logarithmic scale) for a consistent comparison across NMAs.

## Prior Distribution Choices for Heterogeneity

The Bayesian framework treats unknown parameters, such as overall treatment effects and heterogeneity variances, as random variables and attempts to estimate them via the assignment of prior distributions. This is commonly implemented via the Markov chain Monte Carlo (MCMC) algorithm. ${ }^{18,19}$ The Supplementary Material presents the Bayesian contrast-based random-effects model to perform an NMA (Appendix A). Among the various parameters to be estimated, the heterogeneity variance, denoted by $\tau^{2}$, plays a critical role, because researchers often have diverse opinions toward its prior choice and it sometimes has influential impact on credible intervals (CrIs) of

Table 1 Summary of Prior Distributions for the Heterogeneity Component (Variance $\tau^{2}$ or Standard Deviation $\tau$ ) for Odds Ratios


treatment comparisons. On the other hand, researchers generally have consensus about the prior for treatment effects ( $\log$ ORs in this study), which is usually noninformative and follows a normal distribution with mean 0 and a very large variance (e.g., $100^{2}$ ).

To re-analyze the collected datasets, we considered three different non-informative (or arguably, weakly informative) prior distributions for the heterogeneity variance or standard deviation: the inverse-gamma, uniform, and half-normal distributions. Table 1 summarizes the multiple choices.

The inverse-gamma prior $I G(\alpha, \beta)$ is conjugate (that is, it produces a posterior also in the inverse-gamma family) and therefore may facilitate the computation in the MCMC algorithm. It also has the potential to improve both stability and convergence, and may be useful for sparse data. ${ }^{20}$ The hyperparameters for both $\alpha$ and $\beta$ (determining distribution shape and scale, respectively) are conventionally assigned to some value close to 0 . As both hyper-parameters approach 0 , it leads to a flat distribution for the heterogeneity variance on a logarithmic scale. We consider three choices of the hyper-parameters, i.e., $0.1,0.01$, and 0.001 .

The uniform prior $U(0, c)$ is another commonly used prior for the heterogeneity standard deviation $\tau$. Here, $c$ denotes the upper bound of the uniform distribution, and is assigned to values 2,5 , and 10 in our analyses; these are common choices for $\log$ ORs in practice. We also considered the half-normal prior $H N\left(0, \sigma^{2}\right)$ for $\tau .{ }^{21}$ This distribution is generated by taking

the absolute value of a random variable that follows the normal distribution $N\left(0, \sigma^{2}\right)$. The hyper-parameter $\sigma^{2}$ determines the range of heterogeneity, ${ }^{22}$ and is assigned values $0.5,1$, and 2 in our analyses.

In addition to the non-informative priors above for heterogeneity, we considered the empirical informative priors derived by Turner et al. ${ }^{14}$ for $\log$ ORs, which were grouped based on outcome type and treatment comparison type. Specifically, the treatment comparisons were classified into three groups, i.e., pharmacological treatment vs. placebo/control, pharmacological treatment vs. pharmacological treatment, and comparisons involved with non-pharmacological treatments (e.g., medical devices, surgical procedures). The outcome types were classified as all-cause mortality, semiobjective outcomes (e.g., cause-specific mortality, major morbidity events, obstetric outcomes), and subjective outcomes (e.g., pain, mental health outcomes, general physical health). For NMAs containing multiple comparison types, the type of pharmacological vs. pharmacological treatment comparison was used for the primary analyses.

## Statistical Analyses

For each dataset, we re-performed the random-effects NMAs with the non-informative priors and the informative priors in Table 1 for the heterogeneity parameter $\tau$ or $\tau^{2}$. The non-informative prior $N\left(0,100^{2}\right)$ was used for all treatment effects ( $\log$ ORs), and we assumed consistency between direct and indirect evidence in each NMA. In addition, all treatment comparisons in each NMA were assumed to share a common heterogeneity variance. ${ }^{5}$ Of note, the NMA model used in this article was contrastbased, because it is currently the most widely used model and the informative priors were derived under the contrastbased framework. Many alternatives, such as the armbased model (which focuses on estimating each treatment arm's absolute effect), may be also used for NMAs. ${ }^{23}$

The Bayesian analyses were conducted with R (version 3.6.2) package "rjags" (version 4-9). The models were implemented via the MCMC algorithm with three chains ${ }^{24-27}$; each chain contained a 50,000 -run burn-in period for achieving stabilization and convergence. The samples generated during the burn-in period were discarded prior to the final analyses; the final posterior distributions for each NMA were based on a run of 200,000 updates after the burn-in period. We checked trace plots for assessing MCMC convergence. Trace plots with certain long-term trends or drifts, instead of stable up-and-down variation, may indicate non-convergence; see Figs. S1-S4 in the Supplementary Material for illustrations. The MCMC may not converge well in cases such as extreme posterior samples of ORs (produced seemingly due to many zero even counts) or improper priors. When Markov chains converged well, the posterior medians and $95 \%$ equal-tailed CrIs can be reliably used as estimates of the parameters of interest. CrIs of $\log$ ORs not covering 0 indicated significant
treatment comparisons. We obtained the posterior estimates for all treatment comparisons and the heterogeneity variance in each NMA. We also calculated the width of $95 \% \mathrm{CrI}$ of $\log$ OR for each comparison, which implied the estimate's precision.

Correlation coefficients between the non-informative priors and informative priors were calculated for both point estimates (posterior median $\log$ ORs) and CrI widths for each NMA and for all NMAs combined. Bland-Altman plots were used to evaluate the agreement between these results. The kappa statistic, $\kappa$, was also calculated to quantify the agreement of statistical significance between the treatment effects produced by the different priors. This statistic is upper bounded by 1 ; roughly, $\kappa<0$ indicates no agreement, and $\kappa$ within $0-0.4$, $0.4-0.6$, and $0.6-1$ indicates weak, moderate, and strong agreement, respectively. ${ }^{28,29}$

Secondary analyses were performed for NMAs which contained a placebo or control treatment. Among these NMAs, we additionally considered the informative prior of the comparison type of pharmacological treatments vs. placebo/control (Table 1).

## RESULTS

## Basic Characteristics

The literature search identified 67 research articles containing NMAs. Of the 44 NMAs that used the Bayesian framework, $52.3 \%$ of the NMAs did not explicitly provide the prior distributions of heterogeneity, and $84.1 \%$ did not provide rationales for the prior choices (Table S1 in the Supplementary Material). A total of 19 NMAs met inclusion criteria for our primary analyses (Fig. 1). Total sample sizes in the selected NMAs ranged from 792 to 111,282; numbers of treatments ranged from 3 to 23 ; and numbers of studies ranged from 7 to 473 . We denoted each NMA by the first author's surname with the publication year of the corresponding article. Table 2 presents summaries of these NMAs; the complete references of these NMAs are in the Supplementary Material (Appendix B). Of note, the NMA of Wu 2013 contained zero events in many treatment arms, causing poor MCMC convergence in our re-analyses; thus, we only present the results of the remaining 18 NMAs in the following.

## Overall Impact of Priors

Figure 2 compares the posterior median ORs and $95 \% \mathrm{CrI}$ widths produced by non-informative priors with those by informative priors among all 18 NMAs. There was a nearly perfect correlation between posterior median (log) ORs by each type of non-informative priors and those by the informative priors; the correlation coefficients for each set of hyperparameters were larger than $r=0.99$. The correlations decreased in terms of $95 \%$ CrI widths. Specifically, $95 \% \mathrm{CrI}$ widths produced by the informative prior were strongly

![img-0.jpeg](img-0.jpeg)

Fig. 1 Flow diagram of network meta-analysis selection.
correlated with those by inverse-gamma priors $I G(0.1,0.1)$, $I G(0.01,0.01)$, and $I G(0.001,0.001)$, all having $r=0.90$. The half-normal priors, with $r=0.89$ for $H N(0,0.5), r=0.91$ for $H N(0,1)$, and $r=0.94$ for $H N(0,2)$, also displayed strong correlations. The correlation with those by the uniform priors experienced greater variability, with $r=0.87$ for $U(0,2), r=$ 0.82 for $U(0,5)$, and $r=0.80$ for $U(0,10)$. All $P$ values of the above correlations were $<0.001$.

Figure S5 in the Supplementary Material (Appendix C) presents the Bland-Altman plots among all 18 NMAs. It indicates strong agreement for both posterior median log ORs and $95 \%$ CrI widths by the various priors. Large differences in posterior median log ORs were likely observed when
the $\log$ ORs were close to 0 , and large differences in $95 \% \mathrm{CrI}$ widths were likely observed when CrIs were very wide.

Table 3 shows the kappa statistics between significant treatment comparisons identified via informative priors and noninformative priors. A total of 942 treatment comparisons were assessed among all NMAs. The kappa statistic for each pair of informative and non-informative priors was positive, mostly close to 1 . A total of 236 treatment comparisons were found to be statistically significant via informative priors, which were more than those via non-informative priors.

Compared with the results based on the informative priors, the greatest variability in kappa statistics due to differences in hyper-parameters was observed when using the inverse-

Table 2 Summaries of the 19 Network Meta-analyses


${ }^{a}$ Prior distribution for heterogeneity is only available for Bayesian analyses; it is not available (NA) for frequentist analyses
${ }^{b}$ Priors assigned based on the criteria by Turner et al. ${ }^{14}$ In cells with two priors listed, the second was used for the secondary analyses because a placebo or control treatment is included in the network
${ }^{c}$ Prior was not specified in the published article, but was obtained by contacting the corresponding author
${ }^{d}$ The corresponding author was contacted for heterogeneity prior but did not respond at the time of submission
gamma prior. Specifically, based on $I G(0.1,0.1)$, there were 194 significant treatment comparisons identified with $\kappa=$ 0.87. This number increased to $218(\kappa=0.95)$ using $I G(0.01,0.01)$ and further increased to $232(\kappa=0.97)$ using $I G(0.001,0.001)$. While $I G(0.001,0.001)$ produced the strongest agreement with the informative priors, it also produced 5 treatment comparisons that were identified as significant by the non-informative priors but non-significant by the informative prior. All uniform priors had $\kappa=0.93$ as did the halfnormal priors $H N(0,1)$ and $H N(0,2)$; both uniform priors $U(0,2)$ and $U(0,5)$ produced 211 significant treatment comparisons, while this number slightly increased to 212 when using $U(0,10)$. The half-normal priors $H N(0,1)$ and $H N(0,2)$
both produced 213 significant treatment comparisons; $H N(0$, 0.5 ) yielded $\kappa=0.94$ with 216 significant ones.

## Impact of Priors Within Network Meta-analyses

Table 4 presents the correlation coefficients between the results and the kappa statistics within NMAs. The largest NMA (in terms of sample size) was Cipriani 2018, which included 111,282 samples, while the smallest NMA was Anothaisintawee 2011 with 792 samples. In the NMA of Cipriani 2018, the correlations of posterior median log ORs between the informative prior and each of the non-informative priors were nearly perfect with no discernable difference; they were all $>0.99$ with $P$ values $<0.001$. An almost identical

![img-1.jpeg](img-1.jpeg)

Fig. 2 Distributions of posterior median odds ratios on a logarithmic scale (a-c) and $95 \%$ credible interval widths (d-f) by various prior distributions among 18 network meta-analyses.
result was observed for the correlation between the $95 \% \mathrm{CrI}$ widths.

The correlations between posterior median $\log$ ORs for each set of non-informative priors were consistently strong in the NMA of Anothaisintawee 2011; all non-informative priors for the median $\log$ ORs had correlation coefficients of at least 0.99 . However, as this NMA had the smallest sample size, the correlations between the $95 \%$ CrI widths

Table 3 Kappa Statistics for Assessing the Agreement Between Informative and Non-Informative Priors with Respect to Significant Treatment Comparisons


exhibited more variability across different prior types and hyper-parameters; the half-normal priors had the highest correlation coefficients with values of $1.00,0.99$, and 0.97 for $H N(0,0.5), H N(0,1)$, and $H N(0,2)$, respectively. The least variability was observed for the inverse-gamma distribution; the correlation coefficients were 0.92 for $I G(0.1$, 0.1 ) and 0.91 for both $I G(0.01,0.01)$ and $I G(0.001,0.001)$. The greatest variability across hyper-parameters was observed for the uniform prior; the priors $U(0,2), U(0,5)$, and $U(0,10)$ had correlation coefficients of $0.98,0.91$, and 0.89 , respectively. All correlations had $P$ values $<0.001$.

A total of 231 treatment comparisons were produced to assess the agreement among priors in the NMA of Cipriani 2018. All hyper-parameters led to $100 \%$ agreement likely due to the large number of samples. On the other hand, the small NMA of Anothaisintawee 2011 contained a total of 28 treatment comparisons. The informative prior led to 2 significant comparisons, while all non-informative priors produced no significant comparison. This resulted in a kappa statistic that was incalculable.

Regardless of the size of NMAs, the informative and noninformative priors produced fairly similar point estimates of ORs, because all correlation coefficients were $>0.90$. However,

Table 4 Correlation Coefficients Between the Results (Posterior Median Log Odds Ratios and 95\% Credible Interval Widths) and Kappa Statistics for Assessing the Agreement Produced By Informative Priors and Non-Informative Priors Within Each Network Meta-analysis


${ }^{a}$ Inverse-gamma priors for $\tau^{2}$ with three sets of hyper-parameters: IG1, IG(0.1, 0.1); IG2, IG(0.01, 0.01); IG3, IG(0.001, 0.001)
${ }^{b}$ Uniform priors for $\tau$ with three sets of hyper-parameters: $U 1, U(0,2) ; U 2, U(0,5) ; U 3, U(0,10)$
${ }^{c}$ Half-normal priors for $\tau$ with three sets of hyper-parameters: HN1, HN(0, 0.5); HN2, HN(0, 1); HN3, HN(0, 2)
the correlation between the $95 \% \mathrm{CrI}$ widths for the different priors was possibly smaller and exhibited greater variability than that between point estimates of ORs in some NMAs. The informative priors typically produced narrower $95 \%$ CrIs than the non-informative priors (Fig. 2d-f). The greatest variability in correlations between $95 \%$ CrI widths was observed in Palmerini 2015 and in the smallest NMA of Anothaisintawee 2011. While all non-informative priors in Castellucci 2013 ( $0.95 \leq r \leq 0.98$ ), Giacoppo 2015 ( $0.88 \leq r \leq 0.97$ ), and Palmerini 2015 ( $0.89 \leq$
$r \leq 0.99$ ) had strong correlations, the correlations were not as strong as those in most other NMAs, which had $r>0.99$ for all non-informative priors. Chatterjee 2013, Daniels 2012, Dulai 2016, Hazlewood 2016, and Phung 2010 had $r>0.99$ for all priors except $I G(0.1,0.1)$.

The Supplementary Material includes the scatterplots of posterior median ORs and $95 \%$ CrI widths by all priors (Figs. S6-S23 in Appendix C) and Bland-Altman plots (Figs. S24S41 in Appendix C) in all NMAs separately.

There was generally small variability in kappa statistics across informative priors within NMAs. The four NMAs of Castellucci 2014, Cipriani 2018, Giacoppo 2015, and Phung 2010 had $\kappa=1$ for all priors. For the NMAs of Castellucci 2013, Palmerini 2015, and Zheng 2018, each treatment comparison was non-significant by both the informative and noninformative priors. Xu 2018 had the same kappa statistic for all uniform and half-normal priors $(\kappa=0.91)$ and for $I G(0.1,0.1)$ and $I G(0.001,0.001)(\kappa=0.90)$, while $I G(0.01,0.01)$ had $\kappa=$ 1. For Isayama 2016, $I G(0.1,0.1)$ had $\kappa=0, I G(0.001,0.001)$ had $\kappa=1$, and all other priors had identical agreement $(\kappa=$ 0.63). Chatterjee 2013 ( $\kappa=0.53$ ), Dulai 2016 ( $\kappa=0.94$ ), and Price 2014 ( $\kappa=0.67$ ) all had identical agreements for the uniform and half-normal priors with different hyper-parameters. The greatest variability in agreements between hyperparameters occurred when using the inverse-gamma prior; it was consistent with the observations in the overall assessment among all NMAs.

## Secondary Analyses

A total of 11 NMAs contained a placebo or control treatment; the secondary analyses were performed for them by additionally considering alternative informative priors (i.e., for the type of comparisons with placebo/control as in Tables 1 and 2). Tables S2 and S3 and Figs. S42-S65 in the Supplementary Material (Appendix D) present the results. As in the primary analyses, the correlation coefficients of posterior median log ORs for each set of hyper-parameters were larger than $r=$ 0.99 . The correlations of $95 \% \mathrm{CrI}$ widths for the secondary analyses were higher than their primary counterparts for $U(0$, 10) $(r=0.80)$ and $H N(0,2)(r=0.94)$; all other correlations were lower in the secondary analyses than in the primary analyses. As in the primary analyses, the half-normal priors led to the highest correlation, and the greatest variability was observed for the uniform priors. The greatest variability in kappa statistics due to differences in hyper-parameters was observed when using the inverse-gamma prior, and the largest number of significant comparisons was observed using $I G(0.001,0.001)$. All uniform and half-normal priors led to $\kappa=0.95$. Four NMAs had $r>0.99$ for all hyper-parameters for both the $95 \%$ CrI widths and median $\log$ ORs. All NMAs had strong correlations for all hyper-parameters; the weakest correlation was present in Anothaisintawee 2011, as in the primary analyses.

## DISCUSSION

## Main Findings

In this empirical study of 19 NMAs, we found that posterior median ORs produced by different priors had a very strong association. Noticeable variability appeared in estimates by different priors for NMAs with relatively small sample sizes per treatment comparison; thus, these NMAs tended to be
sensitive to the prior specification. For large NMAs, noninformative priors generally produced nearly identical point estimates and $95 \% \mathrm{CrI}$ widths, thus leading to an almost perfect agreement with the results based on informative priors. For small NMAs, the point estimates by informative priors were approximately the same as those produced by noninformative priors, but the CrIs produced by non-informative priors were often substantially wider than those produced by the informative priors. As a result, overall, informative priors yielded more statistically significant treatment effects. The greatest variability in agreement was observed when using the inverse-gamma priors, while the uniform and half-normal priors yielded approximately similar results.

## Strengths and Limitations

This study considered most commonly used prior choices for modeling heterogeneity in the current practice of Bayesian NMAs. The results were based on recent NMAs published in high-impact medical journals, which were thus expected to be of high quality. All R code is provided in the Supplementary Material (Appendix E).

Nevertheless, this study had several limitations. First, we focused on assessing the impact of priors on the posterior medians and $95 \%$ CrIs of ORs, while the conclusions may not be directly generalized to other effect measures. Second, because the datasets involved in this study were relatively large, we did not examine the validity of several important assumptions (e.g., transitivity, consistency, reporting bias) in each NMA. ${ }^{30}$ These factors may also influence NMA estimates along with the choice of priors, and researchers should investigate them on a case-by-case basis. Third, the NMAs published in high-impact journals may contain more studies, treatments, and samples than those published in other journals. The results of much smaller NMAs were likely more sensitive to prior choices.

## Implications

Contemporary Bayesian NMAs published in high-impact journals do not adequately report details on the choice of heterogeneity prior distributions and their rationales. If an NMA does not have a large sample size, sensitivity analyses are recommended to examine the impact of using different hyper-parameters or other types of prior distributions, especially for the inverse-gamma prior. When the number of studies included in NMA is large, various non-informative priors produce similar conclusions. When the number of studies is small, conclusions become more sensitive to the prior type and hyperparameters. In such cases, empirical informative priors may be used to produce more precise estimates.

[^0]
[^0]:    Corresponding Author: Lifeng Lin, PhD; Department of Statistics, Florida State University, Tallahassee, FL 32306, USA [e-mail: linl@stat.fsu.edu].

Funding This research was supported in part by the U.S. National Institutes of Health/National Library of Medicine grant R01 LM012982 (HC and LL) and National Institutes of Health/National Center for Advancing Translational Sciences grant UL1 TR001427 (LL). The content is solely the responsibility of the authors and does not necessarily represent the official views of the National Institutes of Health.

## Compliance with Ethical Standards:

This article focused on statistical methods for network meta-analyses, and all analyses were performed based on published data. Therefore, this study did not require ethical approval and patient consent.

Conflict of Interest: The authors declare that they do not have a conflict of interest.
