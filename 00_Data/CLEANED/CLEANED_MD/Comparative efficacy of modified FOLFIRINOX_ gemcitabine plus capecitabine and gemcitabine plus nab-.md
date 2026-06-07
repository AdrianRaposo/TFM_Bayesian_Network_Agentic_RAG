# Lecancermedicalscience 

## Comparative efficacy of modified FOLFIRINOX, gemcitabine plus capecitabine and gemcitabine plus nab-paclitaxel as adjuvant treatment for resected pancreatic cancer: a Bayesian network meta-analysis

Victor Hugo Fonseca de Jesus and Rachel P Riechelmann<br>Medical Oncology Department, A.C. Camargo Cancer Center, Rua Prof. Antônio Prudente 211, São Paulo SP 01509-010, Brazil


#### Abstract

Background: There are no head-to-head comparisons evaluating the efficacy of the main polychemotherapy regimens used for patients with pancreatic cancer in the adjuvant setting. We aimed to describe the relative efficacy of modified FOLFIRINOX (mFOLFIRINOX), gemcitabine plus capecitabine (GEM-CAP) and gemcitabine plus nab-paclitaxel (GEM-NAB) in this setting using a Bayesian network approach.

Methods: We collected data from the ESPAC-4, PRODIGE 24 and APACT trials. Diseasefree survival (DFS), according to the investigators, and overall survival (OS) for the three polychemotherapy regimens were compared using gemcitabine as the reference arm. We ran Markov chain Monte Carlo simulations with a fixed-effect model to generate the posterior distribution of the hazard ratios (HRs) using non-informative priors. Relative efficacy was measured by HRs, surface under cumulative ranking and rankograms.

Results: mFOLFIRINOX was the chemotherapy regimen most likely to be the most effective in the adjuvant setting ( $98.9 \%$ and $89.6 \%$ probability for DFS and OS, respectively). GEM-NAB marginally improved DFS (HR $=0.97,95 \%$ credible interval $(95 \% \mathrm{CrI})=0.77-$ 1.21) and OS (HR $=0.98,95 \% \mathrm{CrI}=0.76-1.25$ ) when compared to GEM-CAP. However, GEM-NAB had the highest chances of being the second most active chemotherapy regimen ( $61.4 \%$ and $52.5 \%$ probability for DFS and OS, respectively), whereas GEM-CAP was less likely to represent the second most active regimen ( $37.7 \%$ and $40.1 \%$ probability for DFS and OS, respectively).

Conclusion: For patients eligible and fit enough to undergo adjuvant treatment with mFOLFIRINOX, this constitutes the treatment of choice. For those with contraindications to mFOLFIRINOX, while both GEM-NAB and GEM-CAP can be considered appropriate alternatives, GEM-NAB is likely the most effective regimen.


Keywords: FOLFIRINOX, gemcitabine, capecitabine, nab-paclitaxel, adjuvant, pancreatic, cancer

Correspondence to: Victor Hugo Fonseca de Jesus Email: victor.jesus@accamargo.org.br
ecancer 2021, 15:1276
https://doi.org/10.3332/ecancer.2021.1276
Published: 16/08/2021
Received: 23/10/2020
Publication costs for this article were supported by ecancer (UK Charity number 1176307).

Copyright: © the authors; licensee ecancermedicalscience. This is an Open Access article distributed under the terms of the Creative Commons Attribution License (http:// creativecommons.org/licenses/by/4.0), which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.

## Background

Pancreatic cancer currently stands as the 14th most common type of cancer worldwide, with 458,918 estimated cases in 2018 [1]. In the same year, it represented the seventh most common cause of cancer-related mortality, with 432,242 estimated deaths. Furthermore, data from developed [2, 3] and developing [4] countries suggest that the burden of pancreatic neoplasms in cancer epidemiology is expected to grow significantly in the decade to come. This high lethality rate is partially related to the disease stage at diagnosis. Only 15%--20% of the patients are candidates for curative-intent surgery [5]. Moreover, for those submitted to surgery, survival outcomes are dismal when this treatment modality is used in isolation [6].

In this sense, the ESPAC-1 [7] and the CONKO-001 [8, 9] have established the role of 5-Fluorouracil and gemcitabine in the treatment of localised pancreatic cancer, respectively. Subsequently, these two drugs were compared in the ESPAC-3 trial [10]. The authors demonstrated that while there were no differences in survival, gemcitabine was associated with lower rates of treatment-related serious adverse events (7.5% versus 14.0%). As a result, gemcitabine became the standard chemotherapy regimen in this scenario.

With the rise of polychemotherapy regimens such as FOLFIRINOX and gemcitabine-based combinations in the metastatic setting [11--13], randomised trials were designed to assess whether patients could benefit from treatment intensification in the setting of less advanced disease. While two randomised trials showed no benefit of adding erlotinib to gemcitabine [14, 15], three randomised trials demonstrated improved overall survival (OS) with combination chemotherapy: the ESPAC-4 (gemcitabine plus capecitabine (GEM-CAP)) [16], the PRODIGE 24 (modified FOLFIRINOX) [17] and the APACT (gemcitabine plus nab-paclitaxel (GEM-NAB)) trials [18].

At this moment, there are no randomised trials directly comparing these three chemotherapy regimens and such comparisons are unlikely to be ever pursued in a controlled setting. Thus, we analysed the results of these trials using a Bayesian network meta-analysis framework. This methodology allows us to infer the probable gains (e.g. in OS) of an intervention over another when formal direct comparisons of therapies through randomised trials are not available. An advantage of this approach is that one can generate probabilistic results that can support the decision-making process [19]. Our aim was to establish the relative efficacy and to compare the toxicity profile of each of these chemotherapy regimens using single-agent gemcitabine as the reference treatment.

## Methods

### Data extraction and collection

Data regarding the inclusion and exclusion criteria, the characteristics of the studies' populations and the toxicity profile were extracted from the original publications for the ESPAC-4 [16] and PRODIGE 24 [17] trials and from the 2019 American Society of Medical Oncology Annual Meeting presentation for the APACT trial [18]. Additionally, updated survival data were extracted from recent presentations for the ESPAC-4 [20] and the APACT trials [21].

### Treatment schedules

In the experimental arm of the ESPAC-4 trial, patients received capecitabine 1,660 mg/m^{2} for 21 days followed by a 7 days' rest plus gemcitabine 1,000 mg/m^{2} once a week for three every 4 weeks. In the PRODIGE 24 study, patients assigned to combination chemotherapy received 5-Fluorouracil 2,400 mg/m^{2} (46-hour continuous infusion), irinotecan 150 mg/m^{2}, oxaliplatin 85 mg/m^{2} and folinic acid 400 mg/m^{2} once every 2 weeks. In the experimental arm of the APACT trial, patients received nab-paclitaxel 125 mg/m^{2} and gemcitabine 1,000 mg/m^{2} once a week for three every 4 weeks. In the control arms of the trials, patients received gemcitabine 1,000 mg/m^{2} weekly for three every 4 weeks. For all treatments, the planned adjuvant treatment duration was 24 weeks.

### Outcomes

The primary outcome was OS in the intention-to-treat population. In all three trials, it was defined as the time from randomisation to death. It was the primary outcome of the ESPAC-4 and the PRODIGE 24 trials. As a secondary outcome, we analysed investigator-assessed disease free-survival (DFS) (relapse-free survival in the ESPAC-4) in the intention-to-treat population. In all three trials, it was defined as the time from randomisation to death or disease progression. It was a secondary outcome of the ESPAC-4 and PRODIGE 24 trials, and it was a prespecified sensitivity analysis of the primary outcome of the APACT study (independently assessed DFS). Since comparable depiction of either any severe or any grade 3--4 adverse events across the three studies was not available, we did not perform a Bayesian network meta-analysis on toxicity. Therefore, data on toxicity are summarised using only descriptive statistics.

### Statistical analysis

Before data analysis, we assessed the transitivity assumption by inspecting the characteristics of the populations and the inclusion and exclusion criteria of the studies [22]. Data on time-to-event outcomes (DFS and OS) were extracted using hazard ratios (HRs) and their 95% confidence intervals (CIs) (95% CI). Before data manipulation, we used the approach described by Parmar et al [23] to convert these measures into log(HR) and selog(HR), respectively. In the Supplementary Material, we have provided formulas and model specifications in accordance with Hu et al [24]. Given the limited number of studies and the indirect nature of all the comparisons between polychemotherapy regimens, there would be no information on between-trial heterogeneity for pairwise comparisons. Thus, we employed a pragmatic approach in which we fit a fixed-effect model to the data [25]. We used a Markov chain Monte Carlo (MCMC) method using Gibbs' sampling algorithm to perform network meta-analyses (codes are available in the Supplementary Material). Briefly, using non-informative priors (mean equal to 0 and variance equal to 1,000) and after a burn-in phase of 40,000 iterations using three chains, we drew 120,000 samples from the posterior distribution (40,000 additional iterations for each chain without thinning). We chose non-informative priors so that results of the analyses would be driven solely by the data from the studies. Parameter convergence was checked by inspection of the Brooks--Gelman--Rubin plots [26]. Gemcitabine was used as the reference comparator (common to all trials). Pairwise comparisons were summarised using HRs and 95% credible intervals (95% CrIs). By definition, the true value of the parameter (HR in this case) has a 95% probability of belonging to such an interval [27]. To portray effectiveness, we ranked treatments according to surface under cumulative ranking (SUCRA) and plotted treatment ranks against their probabilities using rankograms [28]. These probabilities were calculated as the ratio between the number of cycles of the MCMC in which a specific treatment had a log HR (effect size) more or less than the ones of other treatments and the total number of cycles of the MCMC. We compared the distribution of categorical variables across studies with Fisher's exact test or chi-square test. Bayesian analyses were conducted using the software WinBUGS version 1.4.3 (MRC Biostatistics Unit, Cambridge, UK). The comparisons of categorical variables across studies and the graphics were carried out using the software R version 3.6.0.

## Results

The network map is shown in Figure 1. Overall, the studies presented similar inclusion and exclusion criteria - Supplementary Table 1. Patients included in these trials should be 18 years old or above, have the pathological diagnosis of ductal adenocarcinoma and have been submitted to microscopically complete (R0) or incomplete (R1) resection. Also, patients should present an Eastern Cooperative Oncology Group (ECOG) performance status (PS) 0 or 1 at randomisation. However, slight differences among the studies' protocols were noted. Patients aged 80 years old or above were not included in the PRODIGE 24 study. Also, the ESPAC-4 study allowed for the enrolment of patients with ECOG PS 2. Importantly, both ESPAC-4 and APACT mandated a CT scan at least 3 months before patient registration. Lastly, the PRODIGE 24 and the APACT studies excluded patients with post-operative Carbohydrate antigen 19-9 (CA 19-9) levels above 180 and 100 UI/mL, respectively.

Table 1 describes the characteristics of the studies' populations. Despite similar inclusion and exclusion criteria, we observed differences in the distribution of patients' characteristics across trials. We noted significant differences in the rate of microscopically involved resection margins (R1 resection), with a high rate seen particularly in the ESPAC-4 trial. Moreover, patients in the ESPAC-4 trial more often presented with stage III disease. Despite these differences, we considered that, based on the similar inclusion and exclusion criteria among the trials, the populations were homogenous enough for the transitivity assumption to be valid. The assessment of the Brooks--Gelman--Rubin plots suggested model convergence for all comparisons of HRs.

![img-0.jpeg](img-0.jpeg)

Figure 1. Network map. Each node represents a chemotherapy regimen. The node size reflects the total number of patients treated with a specific chemotherapy regimen across studies. Solid lines represent direct comparisons. Dashed lines represent indirect comparisons.


# Disease-free survival

The median duration of follow-up in the three studies ranged from 33.6 to 53.3 months. Table 2 describes the survival outcomes of the trials. No significant difference in DFS according to the investigators was observed in ESPAC-4 ( $p=0.069$ ). Conversely, patients treated with combination chemotherapy experienced improved investigator-assessed DFS in both PRODIGE 24 and APACT. The relative efficacy in terms of

DFS of each chemotherapy regimen is shown in Table 3. According to the rankogram, modified FOLFIRINOX had a $98.9 \%$ probability of being the most active chemotherapy among the four regimens in the adjuvant setting (Figure 2). The analysis of SUCRA for DFS also described modified FOLFIRINOX as the single most active chemotherapy agent (Table 4). Additionally, GEM-NAB (61.4\% probability) was more likely than GEM-CAP ( $37.7 \%$ probability) to be the second best chemotherapy regimen.

# Overall survival 

In all three trials, patients treated with combination chemotherapy experienced longer OS. The relative efficacy in terms of OS of each chemotherapy regimen is shown in Table 3. According to the rankogram, modified FOLFIRINOX had $89.6 \%$ probability of being the most active chemotherapy among the four regimens in the adjuvant setting (Figure 2). The analysis of SUCRA for OS also described modified FOLFIRINOX as the single most active chemotherapy agent (Table 4). Additionally, GEM-NAB (52.5\% probability) was more likely than GEM-CAP $(40.1 \%)$ to be the second best chemotherapy regimen.

## Outcomes of patients treated with single-agent gemcitabine across trials

There were significant differences in OS across trials for patients undergoing adjuvant treatment with single-agent gemcitabine (Table 2). Patients who were treated in the gemcitabine arm in the ESPAC-4 trial experienced numerically worse OS (median OS: 26.0 months; 95\% CI $=22.7-28.4$ ) when compared to those treated with the same regimen in the PRODIGE 24 (median OS: 35.0 months; $95 \% \mathrm{Cl}=28.7-43.9$ ) and APACT (median OS: 37.7 months) trials. However, there were no differences in the relapse-free survival for patients treated with singleagent gemcitabine across the three trials.

Table 2. Survival outcomes according to the treatments across studies.


aBased on original publication (not on updated analysis). For the ESPAC-4, administrative censoring occurred at 5 years of follow-up
CI, Confidence interval; NA, not reached

Table 3. HRs and 95\% Crls for DFS and OS.


![img-1.jpeg](img-1.jpeg)

Figure 2. Rankograms for DFS and OS show the probability that each chemotherapy regimen has of being the first, second, third and fourth best chemotherapy regimen in terms of DFS and OS. These rankograms are created by assessing throughout the cycles from the MCMC the relative frequency in which the coefficient of the HR (log HR) for one specific chemotherapy regimen was greater or lesser than those of the other chemotherapy regimens.

Table 5 describes the toxicity patterns observed in the three studies. In all studies, combination chemotherapy was associated with an increased risk of grade 3-4 toxicity. In ESPAC-4, GEM-CAP was associated with numerically increased rates of grade 3-4 neutropenia, diarrhoea and hand-foot syndrome. In PRODIGE 24, modified FOLFIRINOX was associated with increased rates of grade 3-4 fatigue, nausea, vomiting, diarrhoea and peripheral neuropathy. In the APACT trial, GEM-NAB was associated with higher frequency of grade 3-4 anaemia, fatigue, diarrhoea and peripheral neuropathy. By indirect comparison, patients treated with GEM-NAB experienced the highest rates of grade 3-4 anaemia, neutropenia and peripheral neuropathy. Patients who received modified FOLFIRINOX presented the highest frequency of grade 3-4 diarrhoea. GEM-CAP was the regimen which most commonly led to hand-foot syndrome. However, it is worth noting that when we evaluate only the single-agent gemcitabine arms of the trials, rates of grade 3-4 haematological toxicities were higher in the APACT when compared to the other studies. Thus, indirect comparisons of toxicities across trials should be interpreted with caution.

# Discussion 

In our study, modified FOLFIRINOX was the chemotherapy regimen most likely to represent the best currently available option in the adjuvant treatment of pancreatic ductal adenocarcinoma. While the PRODIGE 24 had a lower median follow-up compared to the other two studies and had a rather selected patient population in terms of age and post-operative CA 19-9 levels, modified FOLFIRINOX had 98.9\% and $89.6 \%$ chance of being the most active chemotherapy regimen in terms of investigator-assessed DFS and OS, respectively. These results are in line with the ones found in a previous Bayesian network meta-analysis including patients with more advanced disease [27]. That said, while long-term survival outcomes of this trial are expected, we believe that FOLFIRINOX is currently the standard of care for all the patients with resected pancreatic cancer who are fit enough to undergo adjuvant chemotherapy with this regimen.

However, some patients will not be optimal candidates to adjuvant treatment with modified FOLFIRINOX. Notably, among the highly selected patient population enrolled in the PRODIGE 24 trial, roughly one-third could not complete the planned 12 cycles of modified FOLFIRINOX; this rate is likely to be even higher among real-world patients. Also, $33 \%$ of all patients diagnosed with localised pancreatic cancer in the USA are older than 80 years at diagnosis [29] and it is currently unknown whether this chemotherapy regimen is safe enough for patients in this age group as they were not included in the PRODIGE 24 trial. Moreover, patients with dihydropyrimidine dehydrogenase (DPD) deficiency (present in $8 \%$ of African-American and 3-5\% of Caucasian patients) [30] are at increased risk of toxicity when treated with fluoropyrimidines while those with uridine diphosphate glucoronosyltransferase 1A (UGT1A) polymorphisms (present in at least 20\% of Caucasians and 15\% of African-Americans or Asian patients) [31] are at an increased risk of toxicity when treated with irinotecan. While adjustments in the dose of irinotecan seem to be sufficient to decrease the risk of severe toxicity even in patients with homozygous UGT1A polymorphism [32], treatment with a fluoropyrimidine in patients with severe DPD deficiency is associated with a prohibitively high risk of severe toxicity and is not recommended [33]. Additionally, other limitations associated with the use of FOLFIRINOX include the need for a permanent catheter and the cumulative cold-induced peripheral neuropathy (particularly relevant in regions with long winters).

Table 4. SUCRA for DFS and OS.


Table 5. Toxicity patterns of studies' treatments.


Apart from toxicity concerns, recent data points out that the efficacy of 5-Fluorouracil-based chemotherapy in pancreatic cancer might depend on the patterns of tumour gene expression. GATA6 is a transcription factor associated with cell differentiation in early pancreatic embryogenesis and low levels of GATA6 are associated with basal-like (or quasi-mesenchymal) gene expression profile. While no prospective randomised trial in the adjuvant setting has been specifically designed to assess this hypothesis, a retrospective analysis from the ESPAC-3 trial showed that patients who had tumours with low or medium levels of GATA6 expression who were treated with 5-Fluorouracil had worse survival when compared to those with high-level tumours [34]. The same phenomenon was not seen for those treated with gemcitabine. Also, pre-clinical data have shown that gemcitabine treatment might be more active against tumours with basal-like (or quasi-mesenchymal) gene expression profile (and therefore, low levels of GATA6 expression) [35] and recent data in the metastatic setting support the effects of this treatment interaction [36]. Thus, while GATA6 expression and gene expression profiling are not currently used to tailor adjuvant chemotherapy for pancreatic cancer, compelling emerging data suggest the choice of fluoropyrimidine-based or gemcitabine-based chemotherapy could be guided by the molecular characteristics of the tumour.

The use of gemcitabine-based doublets could match the need for less toxic or non-fluoropyrimidine-based regimens in the adjuvant setting. In this sense, we showed that GEM-NAB is likely associated with the highest probability of being the best gemcitabine-based treatment in terms of both investigator-assessed DFS and OS. GEM-CAP had a slightly worse performance than GEM-NAB in terms of survival outcomes. Also, in the real world, the use of GEM-CAP has been shown to be challenging given its toxicity profile [37]. Likewise, the rate of chemotherapy completion among patients treated with GEM-CAP in the ESPAC-4 study was the lowest among the three studies - Supplementary Table 2. Furthermore, retrospective data from the X-ACT study in colon cancer suggest worse tolerance to fluoropyrimidine among North Americans when compared to Europeans [38]. Because only European patients were included in the ESPAC-4, non-European Western patients might face even more difficulties in trying to complete adjuvant chemotherapy with GEM-CAP. However, despite potential differences in the chances of experiencing chemotherapy-related toxicity between North Americans and Europeans, it is important to state that current data support similar survival rates for patients with stage I-II pancreatic cancer who undergo resection in the United States and in Europe [39], which suggest that potential differences in survival outcomes across these trials are probably not secondary to ethnic or geographical reasons.

Despite these results, one might say that GEM-NAB should not be considered a treatment option in this setting since the APACT trials failed to meet the primary endpoint of DFS as assessed by the independent review. We believe that the conclusion as to whether a trial is considered positive or negative is complex and should not rely solely on the statistical significance of the test for the primary outcome [40]. The APACT investigators chose the independently reviewed DFS as the primary outcome in an attempt to improve reproducibility. Nonetheless, pancreatic cancer relapse is often suspected based on clinical (symptoms) or laboratory (CA 19-9 levels) information, which is not available for the independent reviewers [41, 42]. These data seem particularly important for patients with locoregional recurrences, which might be very difficult to distinguish from post-operative alterations based only on radiological grounds [43, 44]. Accordingly, a recent analysis from the APACT trial showed that there were significant discordances in the number of DFS events between independent and investigator assessment that likely influenced outcomes [21].

Another argument that supports the use of GEM-NAB in the adjuvant setting is the significant OS benefit. This outcome is perceived by many experts in pancreatic cancer as the most important indicator of outcome quality [45]. Accordingly, OS was the primary outcome for both the PRODIGE 24 and the ESPAC-4 trials. Interestingly, in the latter study, the OS benefits were considered significant despite the lack of significant improvement in DFS. Additionally, in the recently presented SWOG S1505 trial [46], which compared perioperative modified FOLFIFIRINOX to perioperative GEM-NAB in the resectable disease setting, no significant differences in DFS and OS times were found. That said, despite the limited sample size and some methodological issues, the results of SWOG S1505 suggest that FOLFIRINOX and GEM-NAB offer similar anti-tumour activity in localised pancreatic cancer, further supporting the use of adjuvant GEM-NAB in case modified FOLFIRINOX is not feasible.

Patients treated with single-agent gemcitabine in the ESPAC-4 trial experienced numerically worse OS when compared to those in the PRODIGE24 and APACT trials. That is in line with the distribution of known prognostic factors, such as ECOG and stage, across these studies. This might have favoured the modified FOLFIRINOX and GEM-NAB arms when compared to GEM-CAP, at least in terms of absolute survival benefit. Furthermore, the lack of seemly significant differences in median relapse-free survival across the single-agent gemcitabine

arms in these trials suggests that factors apart from the adjuvant chemotherapy regimen might have played a part in determining OS, such as characteristics of the post-progression therapy.

Our study has limitations. We did not carry out a systematic search for all the articles comparing different adjuvant chemotherapy regimens for patients with resected pancreatic cancer. Nevertheless, apart from 5-1 which is used almost exclusively in Asia, it is largely known by those with expertise in pancreatic cancer that these are the most clinically relevant chemotherapy regimens tested in randomised trials in the adjuvant setting. Furthermore, inconsistencies in the descriptions of the toxicities prevented us from making indirect comparisons of grade $3-4$ or severe adverse events. However, we displayed the data from the studies in a way that readers can have an idea of the comparative risks of toxicities. Our study also has merits. As far as we know, this is the first Bayesian network meta-analysis evaluating the comparative effectiveness of these chemotherapy regimens. With this methodology, we were able to rank the efficacy of these regimens using a probabilistic approach that can aid the decision-making process. Moreover, we used matched outcomes, considering differences in independent reviewer-assessed and investigator-assessed DFSs. Furthermore, we present updated results for survival analysis from two of the three studies.

# Conclusion 

Modified FOLFIRINOX is the standard of care for the treatment of pancreatic cancer in the adjuvant setting for patients fit enough to receive this chemotherapy regimen. For those with contraindications or who are not fit enough for modified FOLFIRINOX, GEM-NAB might be the preferred adjuvant therapy, particularly to those patients who have contraindications for fluoropyrimidines.

## Conflicts of interest

Victor Hugo Fonseca de Jesus received honoraria from United Medical and had travel expenses paid by United Medical in the past 12 months. United Medical is the company responsible for the distribution and sale of nab-paclitaxel in Brazil. Rachel Pimenta Riechelmann received consultancy fees from Astra Zeneca in the past 12 months.

## Funding source

This study had no funding source.

## Authors' contributions

Victor Hugo Fonseca de Jesus: conceptualisation, methodology, data curation, data analyses, writing and visualisation; Rachel Pimenta Riechelmann: methodology, writing and visualisation.

## Acknowledgment

The authors would like to thank Vinicius Fernando Calsavara (chief statistician) for reviewing the WinGUBS codes for the Bayesian network meta-analysis.

# Supplementary material

## Supplementary tables

## Supplementary Table 1. Inclusion and exclusion criteria.


${ }^{a}$ Defined as no cancer cells within 1 mm of all resection margins ${ }^{\text {b }}$ Clear CT scan of chest, abdomen, and pelvis required within 3 months before randomization ${ }^{c}$ CT without evidence of disease

## Supplementary Table 2. Treatment compliance.


${ }^{a}$ In cycle 6, 59\% of patients on Gemcitabine plus Nab-Paclitaxel received Nab-Paclitaxel

# Codes for the WinBUGS 

## \# MODEL for OS

## \# Defining the model for log-hazard ratios (lhr)
```
model
\{
for(i in 1:ndp)\{
$\operatorname{prec}[i]<-1 /(\operatorname{se}[i] * s e[i])$
lhr[i]-dnorm(md[i],prec[i])
\# Defining the fixed-effect model for the log hazard ratios (lhr)
$\mathrm{md}[\mathrm{i}]<-d[t[i]]-d[b[i]]$
\# Give priors to log hazard ratios (lhr)
$d[1]<-0$
for $(k$ in 2:nt) $\{$
$d[k]-\operatorname{dnorm}(0, .001)$
\}
\# Defining ranks (rk)
for $(k$ in 1:nt) $\{$
$r k[k]<-r a n k(d[], k)$
best $[k]<-e q u a l s(r k[k], 1)$
```
## \# Defining SUCRA
```
for(j in 1:nt)(effectiveness[k,j]<-equals(rk[k],j))]
for(k in 1:nt)(for(j in 1:nt)(cumeffectiveness[k,j]<-sum(effectiveness[k,1:j]))]
for(k in 1:nt)(SUCRA[k]<-sum(cumeffectiveness[k,1:(nt-1)])/(nt-1)
\}
```
# Construct all pairwise log hazard ratios (lhr) and hazard ratios (HR) 
```
for (c in 1:nt-1) $\{$
for $(k$ in $(c+1): n t)\{$
$l h z r[c, k]<-d[k]-d[c]$
$H R[c, k]<-e x p(l h z r[c, k])$
\}
\}
\}
\# Entering the data in the model (observed data)
data
\#\#\#\#\#\#\#\#
list(ndp=3, nt=4, $t=c(2,3,4), b=c(1,1,1), \operatorname{lhr}=c(-0.174353387,-0.198450939,-0.446287103), \mathrm{se}=c(0.088424645,0.088788212,0.14876180$ 7))
\#\#\#\#\#\#\#\#
\# Entering initial values in the model
initials
\# three chains
list(d=c(NA,-0.5,-0.5,-0.5))
list(d=c(NA,0,0,0)
list(d=c(NA,0.5,0.5,0.5))
\# MODEL FOR DFS
\# Defining the model for log-hazard (lhr)
model
\{
for(i in 1:ndp) $\{$
$\operatorname{prec}[i]<-1 /(\operatorname{se}[i] * s e[i])$
lhr[i]-dnorm(md[i],prec[i])
```
# # Defining the fixed-effect model for the log hazard ratios (lhr) 

$\operatorname{md}[i]<-d[t[i]]-d[b[i]]$

## \# Give priors to log hazard ratios (lhr)
```
$d[1]<-0$
for $(k$ in 2:nt) $\{$
$d[k] \sim \operatorname{dnorm}(0, .001)$
\}
```
## \# Defining ranks (rk)
```
for $(k$ in 1:nt) $\{$
$r k[k]<-r a n k[d[], k)$
best $[k]<-e q u a l s(r k[k], 1)$
```
## \# Defining SUCRA
```
for(j in 1:nt)(effectiveness[k,j]<-equals(rk[k],j))]
for(k in 1:nt)(for(j in 1:nt)(cumeffectiveness[k,j]<-sum(effectiveness[k,1:j]))]
for(k in 1:nt)(SUCRA[k]<-sum(cumeffectiveness[k,1:(nt-1)])/(nt-1)
\}
\# Construct all pairwise log hazard ratios (lhr) and hazard ratios (HR)
for (c in 1:nt-1) $\{$
for $(k$ in $(c+1): n t)\{$
lhzr[c,k] <- d[k] - d[c]
$\operatorname{HR}[c, k] \leftarrow \exp (\operatorname{lhzr}[c, k])$
\}
\}
\}
```
# Entering the data in the model (observed data) 
```
data
\#\#\#\#\#\#\#\#\#
list(ndp $=3, n t=4, t=c(2,3,4), b=c(1,1,1), \operatorname{lhr}=c(-0.1625189,-0.1984509,-0.5447272), s e=c(0.08028335,0.08409595,0.11781073)) \#\#\#\#\#\#\#\#\#
```
## \# Entering initial values in the model
```
initials
\# three chains
list $(d=c(N A,-0.5,-0.5,-0.5))$
list $(d=c(N A, 0,0,0)$
list $(d=c(N A, 0.5,0.5,0.5))$
```
## Formulas

The formula below specifies the Bayesian model:

$$
\operatorname{lhr}_{i}=\mathrm{N}\left(\theta_{i} \mathrm{~V}_{i}\right)
$$

where $\operatorname{lhr}_{i}$ represents trial-specific log hazard ratio and $\mathrm{V}_{\mathrm{i}}$ represents the within-trial variance. It is worth noting that in WinBUGS variance needs to be recorded as precision (precision being the inverse of the variance). As stated in the Methods section, we employed a pragmatic approach in which we fit a fixed-effect model to the data. In this setting, any difference between the log hazard ratios is believed to be due to sampling error [1]. In other words:

$$
\operatorname{lhr}_{i}=\theta+\varepsilon_{i}
$$

where the sampling error $\varepsilon_{i}$ is normally distributed with mean 0 and variance equal to the within-trial variance. This fixed-effect model can be described as:

$$
\theta_{i}=\mathrm{d}_{\mathrm{ij}}-\mathrm{d}_{\mathrm{bi}}
$$

where $d_{i j}$ are defined as basic parameters and $d_{i j}$ are defined as functional parameters. For the basic parameters, a non-informative prior with mean 0 and variance 1000 was chosen. Further information can be found on the paper by Hu et al [2]

## References

1. Wang S, Hawkins H. Indrotuction. In: Biondi-Zoccai G, editor. Network Meta-Analysis: Evidence Synthesis with Mixed Treatment Comparison. First ed: Nova Science; 2014. p. 157-70.
2. Hu D, O'Connor AM, Wang C, Sargeant JM, Winder CB. How to Conduct a Bayesian Network Meta-Analysis. Front Vet Sci. 2020;7:271.