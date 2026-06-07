# Comparative efficacy of inhaled corticosteroid and long-acting beta agonist combinations in preventing COPD exacerbations: a Bayesian network meta-analysis 

Yuji Oba<br>Nazir A Lone

University of Missouri, School of Medicine, Division of Pulmonary, Critical Care and Environmental Medicine, Columbia, MO, USA

[^0]This article was published in the following Dove Press journal: International Journal of COPD
12 May 2014
Number of times this article has been viewed

## Background: A combination therapy with inhaled corticosteroid (ICS) and a long-acting beta agonist (LABA) is recommended in severe chronic obstructive pulmonary disease (COPD) patients experiencing frequent exacerbations. Currently, there are five ICS/LABA combination products available on the market. The purpose of this study was to systematically review the efficacy of various ICS/LABA combinations with a network meta-analysis.
Methods: Several databases and manufacturer's websites were searched for relevant clinical trials. Randomized control trials, at least 12 weeks duration, comparing an ICS/LABA combination with active control or placebo were included. Moderate and severe exacerbations were chosen as the outcome assessment criteria. The primary analyses were conducted with a Bayesian Markov chain Monte Carlo method.
Results: Most of the ICS/LABA combinations reduced moderate-to-severe exacerbations as compared with placebo and LABA, but none of them reduced severe exacerbations. However, many studies excluded patients receiving long-term oxygen therapy. Moderate-dose ICS was as effective as high-dose ICS in reducing exacerbations when combined with LABA.
Conclusion: ICS/LABA combinations had a class effect with regard to the prevention of COPD exacerbations. Moderate-dose ICS/LABA combination therapy would be sufficient for COPD patients when indicated. The efficacy of ICS/LABA combination therapy appeared modest and had no impact in reducing severe exacerbations. Further studies are needed to evaluate the efficacy of ICS/LABA combination therapy in severely affected COPD patients requiring long-term oxygen therapy.
Keywords: combination therapy

## Introduction

Chronic obstructive pulmonary disease (COPD) continues to be a major cause of disability, mortality, and rising health care costs. In 2005, 210 million people were diagnosed with COPD worldwide, and 3 million died of the disease. ${ }^{1}$ In the United States, it is estimated that more than 12 million people are affected by the disease, and COPD has become the third leading cause of death after cardiovascular disease and malignancy. ${ }^{2}$ It is predicted that COPD will also become the third leading cause of death worldwide by $2030 .{ }^{3}$

Current guidelines developed by Global Initiative for COPD recommend a combination of an inhaled corticosteroid (ICS) and a long-acting beta agonist (LABA) in patients with severe disease (stage III and IV) who are experiencing frequent exacerbations. ${ }^{4}$ Results from a large randomized trial, Toward a Revolution in COPD Health (TORCH), including over 6,000 patients with severe COPD, suggest that


[^0]:    Correspondence: Yuji Oba
    University of Missouri, School of Medicine, Division of Pulmonary, Critical Care and Environmental Medicine, One Hospital Drive, CE 412, Columbia, MO 65212, USA Tel +15738828583
    Fax +15738846050
    Email obay@health.missouri.edu

treatment with ICS/LABA combination therapy resulted in a reduced rate of exacerbations, improved health status, and greater lung function values relative to placebo and the other agents. ${ }^{5} \mathrm{~A}$ trend toward improved survival with the ICS/ LABA combination therapy was not statistically significant and of questionable clinical relevance.

Currently, there are five ICS/LABA combination products available on the market: budesonide/formoterol (BUD/FM), "Symbicort" (AstraZeneca, Wilmington, DE, USA); fluticasone propionate/salmeterol (FP/SAL), "Advair", "Seretide", "Viani", "Adoair", or "Foxair" (GlaxoSmithKline, Brentford, UK); mometasone/formoterol (MF/FM), "Dulera" or "Zenhale" (Merck, White House Station, NJ, USA); beclomethasone dipropionate/formoterol (BDP/FM), "Fostair" (Chiesi Ltd, Cheadle, UK); and fluticasone furoate/vilanterol (FF/VI), "Breo" or "Relvar Ellipta" (GlaxoSmithKline). ${ }^{6}$

When no clinical trials exist that directly compare all relevant treatment options, indirect comparisons can be made by comparing the relative effects of treatments against a common comparator or combining a variety of comparisons that taken together form one or more chains linking the treatments of interest (variously referred to as a mixed or multiple treatment comparison or network meta-analysis). ${ }^{7}$ The purpose of this study was to systematically review the efficacy of various ICS/LABA combinations in COPD from randomized controlled trials with a Bayesian network meta-analysis.

## Materials and methods

## Identification of trials

We identified all relevant clinical trials that studied clinical efficacies of an ICS/LABA combination in COPD. Two authors independently searched the Ovid Medline database for studies published from 1946 to January 21, 2014 using Medical Subject Headings (MeSH) and keywords: randomized controlled trial AND pulmonary disease, chronic obstructive AND FM, SAL, or VI AND FF, FP, BUD, MF, or BDP. In addition, we searched Scopus, Cumulative Index to Nursing and Allied Health Literature (CINAHL), and the internet, including the online trial registries of above mentioned ICS/LABA manufacturers. Bibliographies of all selected articles and review articles that included information on ICS/LABA combination therapy in COPD were also reviewed for other relevant articles. We included any randomized clinical trial, published or unpublished, evaluating COPD patients with an ICS/LABA combination. Randomized control trials had to be of at least 12 weeks duration. Control interventions included active interventions
and/or placebo. Searches were limited to English language. We excluded pharmacokinetic studies, proof of concept studies, and trials with a cross-over design. Two reviewers independently screened studies by title and abstract to evaluate whether a trial met the inclusion criteria. Disagreement between reviewers was resolved by consensus. We chose moderate-to-severe and severe exacerbations as the outcome assessment criteria for the purpose of our meta-analysis. We extracted data on COPD exacerbations as moderate and severe. Moderate was defined as "worsening respiratory status which required additional medication such as oral steroids and/or antibiotics" and severe as "rapid deterioration of respiratory status which was life-threatening or required hospitalization". A subgroup analysis was planned a priori for exacerbations selecting clinical trials which did not exclude patients receiving long-term oxygen therapy (LTOT).

## Statistical analysis

The primary analyses were conducted with a Bayesian Markov chain Monte Carlo method and fitted with the Bayesian software in WinBUGS version 1.4.3 (Medical Research Council Biostatistics Unit, Cambridge, UK). ${ }^{8}$ Bayesian metaanalyses involve data, a likelihood distribution, a model with parameters, and prior distributions. The technique estimates the relative efficacy between treatments that have not been directly compared and provides the most flexible approach to indirect comparison modeling. It has become a very popular tool when multiple treatments exist for a given condition. For the analyses in WinBUGS, every sample consisted of 100,000 iterations with an initial burn-in period of 10,000 iterations. ${ }^{9}$ We used a Poisson likelihood and a log link. Each pair of treatments was compared by estimating a hazard ratio (HR) of the outcome. The Poisson model is useful for repeated event data such as number of exacerbations, where each individual may have more than one event. ${ }^{10}$

To assess the impact of ICS/LABA combinations on moderate-to-severe and severe exacerbations, data was extracted in the form of rates and given as the number of events per person-years observed. When the number of events was not available in a given study, we substituted the number of subjects who experienced an exacerbation. We assumed that each of the log HRs had been sampled from a normal distribution and that the hazard was constant in each arm over the follow-up period. We gave vague priors for all trial baselines, treatment effects, and between-trial variances.

The autocorrelation plots showed that throughout the iterative process, the autocorrelation was satisfactorily reduced to a nominal amount and the Brooks-Gelman-Rubin

plots showed that the model had converged satisfactorily. ${ }^{9}$ We assessed the fit of our model using the deviance information criterion (DIC), a measure of model fit that penalizes model complexity. This criterion advocates selecting the model with the lowest DIC value among a series of competing models for the same data, as this model is believed to provide the best fit to the data. ${ }^{11}$ All results for the network meta-analysis were reported as posterior means with corresponding $95 \%$ credibility intervals (CrIs). CrIs are the Bayesian equivalent of classical confidence intervals.

## Results

## Study selection

The electronic database searches identified 219 citations. One hundred seventy four studies were excluded on abstract review. The remaining 45 studies were reviewed for further details. An additional 27 studies were excluded for various reasons, as shown in Figure 1. One online first study and two unpublished studies (SFCT01 and SUMIRE) were found on the internet and the manufacture's websites. ${ }^{12-14}$ We included 21 studies comparing five different ICS/LABA combinations for moderate-to-severe exacerbations and 13 studies for severe exacerbations including a total of 26,868 and 19,368 patients, respectively. ${ }^{5,12-31}$ The study and patient characteristics are presented in Table 1. The mean ages (range: 60-66 years), proportion of male patients (range: $54 \%-95 \%$ ), and the mean baseline percentage predicted forced expiratory volume in 1 second $\left(\mathrm{FEV}_{1}\right.$; range: $33 \%-47 \%$ ) were comparable across the studies. The definitions of COPD exacerbations were similar across the included studies (Table S1). The network of treatments is displayed in Figure 2. The treatments formed a closed network, which was amenable to multiple treatment comparison analyses.

## Methodological quality of included studies

Generally, the risk of bias in the included studies appeared moderate to low. Allocation concealment was appropriate in ten studies and unclear in eleven studies. Eleven out of 21 studies presented intention-to-treat analyses. All studies were double blinded (Table 1). In the opinion of the authors, there were no studies that clearly should have been excluded from the analysis because of differences in baseline characteristics or poor quality.

## Comparison of ICS/LABA combinations on moderate-to-severe exacerbations

When the efficacy of various strengths of each ICS/LABA combination was assessed individually, all but BUD/FM
![img-0.jpeg](img-0.jpeg)

Figure 1 Flow of study selection.

400/12 ( $400 \mu \mathrm{~g} / 12 \mu \mathrm{~g})$ and BDP/FM 200/12 ( $200 \mu \mathrm{~g} / 12 \mu \mathrm{~g})$ reduced moderate-to-severe exacerbations as compared with placebo. When the overall efficacy of each ICS/LABA combination was assessed (all strengths of each combination combined), all but BDP/FM reduced moderate-to-severe exacerbations (Figure 3). The BDP/FM combination had the lowest sample size of 718 as compared with other combinations (FP/SAL, $\mathrm{n}=12,354$; BUD/FM, $\mathrm{n}=7,667$; $\mathrm{FF} / \mathrm{VI}, \mathrm{n}=3,878 ; \mathrm{MF} / \mathrm{FM}, \mathrm{n}=2,251$ ). All combination therapy except FF/VI 50/25, FP/SAL 250/50, BUD/FM 400/12, and BDP/FM 200/12 reduced moderate-to-severe exacerbations as compared with LABA alone. BDP/FM was the only combination which did not reduce moderate-to-severe exacerbations when the overall efficacy of each ICS/LABA combination was compared with that of LABA alone (Figure 4). Medium-dose ICS/LABA combinations were as effective as high-dose ICS/LABA combinations in reducing moderate-to-severe exacerbations when directly compared. Random models gave lower DIC scores than fixed models. Therefore, random models were used for the above analyses.


Oba and Lone

Dovepress

Table 1 Study characteristics of included trials that provide data on the total number of exacerbations and/or the mean annual rate of exacerbations



Notes: ${ }^{1}$ Postbronchodilator: ${ }^{2}$ less than 12 hours LTOT was allowed.
Abbreviations: BDP, beclomethasone dipropionate; bid, twice a day; BUD, budesonide; FEV ${ }_{1}$, forced expiratory volume in 1 second; FF, fluticasone furoate; FM, formoterol; FP, fluticasone propionate; ITT, intention to treat; LTOT, longterm oxygen therapy; MF, mometasone furoate; NR, not reported; PLB, placebo; qd, once a day; SAL, salmeterol; VI, vilanterol.

![img-1.jpeg](img-1.jpeg)

Figure 2 Diagram displaying the network of eight arms involved in the Bayesian analyses.
Notes: The links between nodes are used to indicate a direct comparison between pairs of treatments. The numbers shown along the link lines indicate the number of trials comparing pairs of treatments head-to-head.
Abbreviations: BDP, beclomethasone dipropionate; BUD, budesonide; FF, fluticasone furoate; FM, formoterol; FP, fluticasone propionate; ICS, inhaled corticosteroids; LABA, long-acting beta agonists; MF, mometasone furoate; PLB, placebo; SAL, salmeterol; VI, vilanterol.

## Comparison of ICS/LABA combinations on severe exacerbations

None of the ICS/LABA combination therapy reduced severe exacerbations as compared with placebo or LABA. (Figures 5 and 6). The results were unchanged when the overall efficacy of each combination therapy was assessed with all strengths of each combination combined. Although most of the combination therapy showed a trend toward decreased incidence of severe exacerbations, the difference did not reach statistical significance. The BUD/FM 320/9 combination, as compared with placebo, was the closest to being statistically significant with an HR of 0.68 ( $95 \%$ CrI 0.49 to 1.00). Random models were used for the analyses above because of their lower DIC scores as compared with those of fixed models. The sample size for FP/SAL, BUD/FM, FF/ VI, MF/FM, and BDP/FM was 7,938, 4,583, 3,878, 2,251, and 718 respectively.

A subgroup analysis was performed for severe exacerbations, selecting clinical trials which did not exclude patients receiving LTOT. BUD/FM did not reduce severe exacerbations as compared with LABA alone, even in such a population. The results were unchanged when BUD/FM 160/9 and 320/9 formulations were assessed individually. A subgroup analysis for BUD/FM versus placebo or other ICS/LABA combinations could not be done due to a lack of data.

## Discussion

Our analysis demonstrated that most of the ICS/LABA combinations reduced moderate-to-severe exacerbations as compared with placebo and LABA, but none of them reduced severe exacerbations. This is the first study which examined the class effects of ICS/LABA combinations in patients with COPD. Medium-dose ICS/LABA combinations were as effective as high-dose ICS/LABA combinations in reducing moderate-to-severe exacerbations. A few ICS/ LABA combinations, namely BUD/FM 400/12 and BDP/FM 200/12, failed to reduce moderate-to-severe exacerbations. However, the samples size of those formulations was not as large as other formulations.

In the TORCH study, FP/SAL 500/25 significantly reduced severe exacerbations when compared with placebo but not with LABA. ${ }^{5}$ Four studies, three for FP/SAL 500/25 (including TORCH) and one for 250/50, were included in our analysis for FP/SAL (Table 1). One study was unpublished. In our analysis, FP/SAL did not reduce severe exacerbations as compared with placebo or LABA. The results were unchanged when two strengths of FP/SAL were analyzed individually or combined, and excluding the unpublished study also did not affect the results. It is possible that the TORCH study may have overestimated the impact of FP/SAL on severe exacerbations. The number of patients included in our analysis for FP/SAL was 7,938 as compared with 6,112 for the TORCH study. Bayesian analyses generally give wider $95 \%$ CrIs than the frequentist method because the Bayesian approach incorporates all sources of uncertainty into the model. On the other hand, it is possible that the pooled analysis with heterogeneous data may have diluted the robust TORCH data.

Nannini et al pooled two studies ${ }^{17,19}$ using the rate ratio and mean difference and concluded that BUD/FM reduced severe exacerbations compared with placebo. ${ }^{32}$ We included four studies for BUD/FM, including one unpublished, to evaluate its impact on severe exacerbations. We used the number of events per person-years observed and analyzed data using the Poisson model, which is useful for repeated event data where each individual may have more than one event. ${ }^{10}$ The difference in methodology and number of included studies could explain the difference in results between Nannini's study and ours. Excluding the unpublished studies ${ }^{12,13}$ did not affect the results of our analysis.

Our study has the following limitations. First, it was assumed that there were no significant differences in efficacies among various formulations of LABAs and

![img-2.jpeg](img-2.jpeg)

Figure 3 Pooled effect estimate on moderate-to-severe exacerbations for all combined inhalers versus placebo.
Abbreviations: BDP, beclomethasone dipropionate; BUD, budesonide; FF, fluticasone furoate; FM, formoterol; FP, fluticasone propionate; MF, mometasone furoate; SAL, salmeterol; VI, vilanterol.

Hazard ratio
![img-3.jpeg](img-3.jpeg)

Figure 4 Pooled effect estimate on moderate-to-severe exacerbations for all combined inhalers versus long acting beta-agonist.
Abbreviations: BDP, beclomethasone dipropionate; BUD, budesonide; FF, fluticasone furoate; FM, formoterol; FP, fluticasone propionate; MF, mometasone furoate; SAL, salmeterol; VI, vilanterol.

![img-4.jpeg](img-4.jpeg)

Figure 5 Pooled effect estimate on severe exacerbations for all combined inhalers versus placebo.

Abbreviations: BDP, beclomethasone dipropionate; BUD, budesonide; FF, fluticasone furoate; FM, formoterol; FP, fluticasone propionate; MF, mometasone furoate; SAL, salmeterol; VI, vilanterol.

ICSs when they were used alone. In our pooled analysis, eight studies did not have a placebo arm. We tried to include as many studies as possible to be most comprehensive, utilizing direct and indirect comparisons with a large network. To assure the robustness of our analysis, we compared the efficacy of ICS/LABA combinations anchored on placebo only, and the results were unchanged. There were no studies directly comparing BDP/FM with placebo (Figure 2). Therefore, BDP/FM could not be included in such analysis.

Second, we used the number of exacerbations per person-years observed to assess the exacerbation rates. The efficacy of MF/FM combination was derived from one study which reported the number of subjects instead of exacerbation events for moderate-to-severe exacerbations.28 We used the number of subjects in place of exacerbation events for this

![img-5.jpeg](img-5.jpeg)

Figure 6 Pooled effect estimate on severe exacerbations for all combined inhalers versus long acting beta-agonist.

Abbreviations: BDP, beclomethasone dipropionate; BUD, budesonide; FF, fluticasone furoate; FM, formoterol; FP, fluticasone propionate; MF, mometasone furoate; SAL, salmeterol; VI, vilanterol.

arm because excluding this study would have precluded the inclusion of the MF/FM arm. We assumed the point estimate of efficacy would be quite similar when using the number of subjects instead of events because we picked the HR instead of mean difference as the outcome assessment parameter. In addition, excluding the MF/FM arm did not affect the results of other combination therapies.

Third, we did not include other outcomes such as mortality or quality of life. No randomized controlled trials of ICS/LABA combination have shown a significant mortality benefit. We felt it would be just hypothesis-generating, even if we found a significant mortality benefit with the current analysis. A previous meta-analysis failed to show mortality benefit with ICS/LABA combinations. ${ }^{32}$ We also believed preventing exacerbations would improve quality of life, which was already demonstrated in the previous meta-analysis with ICS/LABA combinations as compared with placebo. ${ }^{32}$

Fourth, the clinical heterogeneity of the trials included in our analysis might have affected the estimates of treatment effects. For example, only seven out of 23 studies included patients receiving LTOT for 12 hours or longer (Table 1). The subgroup analysis limited to studies which included patients receiving LTOT failed to show that ICS/ LABA combination therapy was superior to LABA alone in reducing severe exacerbations. The subgroup analysis was possible only for BUD/FM versus LABA alone because of a lack of data. Further studies are needed to examine the impact of an ICS/LABA combination on severe exacerbations in the most severely affected patients with COPD receiving LTOT.

In conclusion, our analysis demonstrated that ICS/LABA combinations had a class effect with regard to the prevention of COPD exacerbations. No particular formulation is better than the other. Moderate-dose ICS/LABA combinations were as effective as high-dose ICS/LABA combinations. None of the ICS/LABA combinations reduced severe exacerbations contrary to the results of the TORCH study. ICS/LABA combination therapy may not be as efficacious as the TORCH study suggested in reducing severe exacerbations.

## Disclosure

The authors report no conflicts of interest in this work.

# Supplementary material 

Table SI Definitions of COPD exacerbations in the included trials


Abbreviation: COPD, chronic obstructive pulmonary disease.

## International Journal of COPD

## Publish your work in this journal

The International Journal of COPD is an international, peer-reviewed journal of therapeutics and pharmacology focusing on concise rapid reporting of clinical studies and reviews in COPD. Special focus is given to the pathophysiological processes underlying the disease, intervention programs, patient focused education, and self management protocols.

Submit your manuscript here: http://www.dovepress.com/international-journal-of-copd-journal

## Dovepress

This journal is indexed on PubMed Central, MedLine and CAS. The manuscript management system is completely online and includes a very quick and fair peer-review system, which is all easy to use. Visit http://www.dovepress.com/testimonials.php to read real quotes from published authors.