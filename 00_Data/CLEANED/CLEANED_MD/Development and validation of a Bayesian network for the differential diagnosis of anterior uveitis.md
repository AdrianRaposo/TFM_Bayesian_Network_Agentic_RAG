## Development and validation of a Bayesian network for the differential diagnosis of anterior uveitis


#### Abstract

Purpose To develop and validate a Bayesian belief network algorithm for the differential diagnosis of anterior uveitis. Patients and methods The 11 most common etiologies were included (idiopathic, ankylosing spondylitis, psoriasis arthritis, reactive arthritis, inflammatory bowel diseases, sarcoidosis, tuberculosis, Behçet, Posner-Schlossman syndrome, juvenile idiopathic arthritis (JIA), and Fuchs' heterochromic cyclitis). Frequencies of association between factors and etiologies were retrieved from a systematic review of the literature. Prevalences were calculated using a random sample of 200 patients receiving a diagnosis of anterior uveitis in Moorfields Eye Hospital in 2012. The network was validated in a random sample of 200 patients receiving a diagnosis of anterior uveitis in the same hospital in 2013 plus 10 extra cases of the most rare etiologies (JIA, Behçet, and psoriasis arthritis). Results In $63.8 \%$ of patients the most probable etiology by the algorithm matched the senior clinician diagnosis. In $80.5 \%$ of patients the clinician diagnosis matched the first or second most probable results by the algorithm. Taking into account only the most probable diagnosis by the algorithm, sensitivities for each etiology ranged from $100 \%$ ( 7 of 7 patients with reactive arthritis and 5 of 5 with Behçet correctly classified) to $46.7 \%$ ( 7 of 15 patients with tuberculosisrelated uveitis). Specificities ranged from $88.8 \%$ for sarcoidosis to $99.5 \%$ in Posner. Conclusions This algorithm could help clinicians with the differential diagnosis of anterior uveitis. In addition, it could help with the selection of the diagnostic tests performed.


JJ González-López ${ }^{1}$, ÁM García-Aparicio ${ }^{2}$, D Sánchez-Ponce ${ }^{3}$, N Muñoz-Sanz ${ }^{1}$, N Fernandez-Ledo ${ }^{1}$, P Beneyto ${ }^{4}$ and MC Westcott ${ }^{1,5}$

Eye (2016) 30, 865-872; doi:10.1038/eye.2016.64; published online 8 April 2016

## Introduction

The differential diagnosis of anterior uveitis is often complex for junior and general ophthalmologists. Diagnosis of the different conditions causing anterior uveitis is based on the presence of different signs (anterior chamber cells and flare, keratic precipitates, synechiae, iris atrophy, iris nodules, IOP, and posterior involvement), symptoms (visual acuity and pain) and epidemiologic characteristics (age, gender, and ancestry). Patients with part but not all of the characteristics of one of the diagnoses and some signs of other diagnosis are frequently found in clinic. Most times, ancillary tests increase the post-test probability for some diagnosis (ACE for sarcoid, tuberculin skin test for TB, syphilis serology). However, for a few etiologies, we do have confirmatory tests (PCR for viral uveitis, HLA-B27). Thus, the exact diagnosis often remains elusive. ${ }^{1}$

A prompt diagnosis of some of the conditions may lead to a better management of the patient, especially if they have systemic involvement.

Bayes theorem was posthumously presented in 1763 by reverend Thomas Bayes' friend, Richard Price. Bayes' theorem links the degree of belief in a proposition before and after, accounting for evidence. This theorem has been used by computer scientists to create complex networks that have been used for artificial intelligence, named Bayesian Belief Networks. Its use has recently expanded to social sciences, biology, and medicine. Its use in medical diagnosis has been extensive. ${ }^{2}$

Our first objective was to implement a Bayesian belief network algorithm for the
${ }^{1}$ Medical Retina and Uveitis Department, Moorfields Eye Hospital NHS Foundation Trust, London, UK
${ }^{2}$ Department of Rheumatology, Complejo Hospitalario de Toledo, Toledo, Spain
${ }^{3}$ Department of Neuroscience, Universidad Complutense, Madrid, Spain
${ }^{4}$ Department of Ophthalmology, Complejo Hospitalario de Toledo, Toledo, Spain
${ }^{5}$ The Institute of Ophthalmology, University College London, London, UK

Correspondence: JJ González-López, Medical Retina and Uveitis Department, Moorfields Eye Hospital NHS Foundation, 162 City Road, EC1V 2PD London, UK Tel: +44 (0)1412111041; Fax: +44 (0)34914338099. E-mail: juliojose.gonzalez@ live.com

Received: 3 June 2015
Accepted in revised form: 20 February 2016
Published online:
8 April 2016

differential diagnosis of the most common causes of anterior uveitis based on the reported clinical characteristics of each etiology and the incidence of each etiology in our center. The second objective was to measure the diagnostic ability of the algorithm for the etiologic diagnosis of 11 common causes of anterior uveitis.

## Materials and methods

The study was approved by the Research Committee at Moorfields Eye Hospital, study number ROAD 13/009. All research adhered to the tenets of the Declaration of Helsinki Principles.

## Algorithm development

The 11 most common causes of anterior uveitis were selected for diagnostic demonstration (idiopathic, ankylosing spondylitis, psoriasic arthritis, reactive arthritis, inflammatory bowel diseases, sarcoidosis, tuberculosis, Behçet, Posner- Schlossman syndrome, juvenile idiopathic arthritis (JIA), and Fuchs' heterochromic cyclitis).

The Bayesian network was developed using the OpenMarkov software, an open, Java based software for the design of Bayesian Belief Networks. ${ }^{3}$ It can be downloaded from http://www.openmarkov.org/org. openmarkov.full-0.1.4.jar.

The Bayes theorem of conditioned probability is expressed as follows:
$p(A \mid B)=\frac{p(B \mid A) \cdot p(A)}{p(B)}$
However, for medical testing, Bayes theorem is often simplified. We speak of pre-test probability when we refer to the probability of a patient with uveitis having a determined etiology, which matches the relative frequency of this etiology in the population. We speak of post-test probability when we refer to the probability of a patient with uveitis and another special characteristic (for example, the presence of hypopyon) having the determined etiology (for example, Behçet). Thus, $p(A)$ is the pre-test probability, and $p(A \mid B)$ is the post-test probability. $p(B \mid A) / p(B)$ can be defined as the likelihood ratio, and this can be calculated from sensitivity and specificity:

Positive likelihood ratio $=\frac{\text { Sensitivity }}{1-\text { Specificity }}$
Negative likelihood ratio $=\frac{1-\text { Sensitivity }}{\text { Specificity }}$

Thus, the formula can be simplified to:
Post-test probability=(Pre-test probability) $\cdot($ Likelihood ratio)
If we wish to combine two or more characteristics (for example, iris nodules and cataracts), then we calculate the post test probability by multiplying the the pre-test probability with all the normalized likelihoods together.

The center node in our Bayesian belief network was the uveitis etiology. Chance nodes, which stand for various factors that had influential relationship with the etiology, were categorized in the following groups: gender, ocular symptoms at presentation, ocular signs, systemic signs and symptoms and laboratory findings. Frequencies of association between these factors and the included etiologies were retrieved from a systematic review of the literature. The methodology previously reported for Fuchs' heterochromic cyclitis ${ }^{4}$ has been reproduced for the rest of the etiologies included in the Bayesian belief network. In summary, MEDLINE, EMBASE, LILACS, Pascal, Dissertation Abstracts, Proceedings of the Association for Research in Vision and Ophthalmology, international symposia on uveitis, and reference lists of found review articles were searched. Case series were considered if they included more than 20 patients with a single etiology of anterior uveitis, or more than 50 patients with anterior uveitis of any cause. When more than one series was included for a determined frequency, fixed model meta-analysis techniques were used to combine the results. When there was no evidence of a specific sign or symptom for a specific uveitis etiology, the prevalence of that sign or symptom in the population was used. Relevant articles used for quantifying frequencies of association are included in Supplementary Appendix 1.

Missing data is very well tolerated by the algorithm. The algorithm calculates the probabilities for each of the missing variables based on the known variables and pre-test probabilities. Thus, only known variables need to be entered in the network in order to obtain the diagnostic probability for our case.

In order to define the prevalence of each of the different etiologies in our population, we identified all patients receiving a new diagnosis of anterior uveitis in the uveitis clinic at Moorfields Eye Hospital between 1 January 2012 and 31 December 2012. A random sample of 200 patients was selected using a computerized random number generator, and their notes were reviewed by one of the authors (JJG-L). These patients were classified according to the cause of their uveitis, as diagnosed by a senior clinician. Some causes of anterior uveitis are not included in our list of possible diagnoses. If any of these other causes was found in the random sample, it was excluded from it and a new random case was selected. Thus, the

cases in the 'idiopathic' category are genuinely idiopathic after all pertinent investigations.

The finished network was trialed in a small number of selected patients with known diagnoses in order to confirm the feasibility of our approach. In order to check the model robustness, the trial was repeated after equalizing the pre-test probabilities for the 11 etiologies (an equal pre-test probability of $9.09 \%$ for each etiology).

## Algorithm validation

A retrospective validation of a diagnostic test was performed.

The validation sample was selected among all patients receiving a new diagnosis of anterior uveitis in Moorfields Eye Hospital between 1 January 2013 and 31 December 2013. A random sample of 200 patients was selected using a computerized random number generator, and their notes were reviewed by one of the authors (JJG-L). Epidemiologic data, clinical signs and symptoms and results of ancillary tests were obtained from the patients' clinical notes. The data were entered in the algorithm by a different author (DS-P), who was masked to the senior clinician diagnosis. The results obtained by the algorithm were compared to the senior clinician diagnosis, which was considered the gold standard.

In order to improve the estimation of the most uncommon diagnosis, the sample was enriched with three cases of JIA, three cases of uveitis associated with psoriasic arthritis and four cases of Behçet's disease. Robustness analysis was performed using a second algorithm with equalized pre-test probabilities for the 11 etiologies.

## Results

## Algorithm development

2954 individual patients received a diagnosis of anterior uveitis in Moorfields Eye Hospital between 1 January 2012 and 31 December 2012. Among these, 200 patients (6.77\%) were randomly selected, and their notes were reviewed in order to set the prevalence for each condition in our population. Table 1 summarizes these findings.

As an example, Table 2 illustrates the calculation of the pooled prevalence of vitritis in patients with Fuch's heterochromic cyclitis using fixed effects meta-analysis, as previously reported. ${ }^{4}$

This was repeated for all demographic and eye characteristics for the 11 chosen uveitis conditions.

The final Bayesian Belief Network can be downloaded and used in the Supplementary Material (Supplementary Appendix 2). It has been released under a Creative Commons Attribution-NonCommercial-NoDerivatives

Table 1 Etiologic classification of a random sample of 200 patients receiving a diagnosis of anterior uveitis in Moorfields Eye Hospital between 1 January 2012 and 31 December 2012


Table 2 Calculation of pooled prevalence of vitritis in patients with Fuch's heterochromic cyclitis using fixed effects metaanalysis


References for the included studies are provided in Supplementary Appendix 1.
The bold value is the result of the fixed-effect meta analysis of the prevalences reported in the articles found in the systematic review of the literature.
4.0 International License. It can be freely distributed unchanged and for non-commercial purposes, as long as authorship is cited.

Ten typical cases were used to evaluate the accuracy and plausibility of the Beyesian Network design. These results are presented in Table 3. Figure 1 shows the algorithm graphic interface in use for one of these sample patients who had a clinical and Bayesian-network-predicted diagnosis of sarcoidosis. Most of the results, including probabilities for all diseases and their orders, were found to be similar to the actual diagnosis of senior clinicians.

Table 4 shows the results of the robustness test. The most likely etiology continued to agree with the clinical diagnosis even after resetting pre-test probabilities.

## Algorithm validation

3674 individual patients received a diagnosis of anterior uveitis in Moorfields Eye Hospital between 1 January 2013 and 31 December 2013. Among these, 200 patients $(5.44 \%)$ were randomly selected in order to form the

Table 3 Comparison between clinical diagnosis and automated diagnosis by Bayesian belief network in 10 typical cases of anterior uveitis


validation cohort. In addition, 10 cases of the most uncommon diagnosis were added to the cohort in order to improve the estimation for these etiologies ( 3 cases of JIA, 3 psoriasis arthritis and 4 Behçet).
In 136 of 210 patients ( $64.8 \%$ ) the most probable etiology by the algorithm matched the senior clinician diagnosis. In 169 of 210 patients ( $80.5 \%$ ) the clinician diagnosis matched the first or second most probable results by the algorithm. Table 5 (prevalence-adjusted model) shows the sensitivities and specificities of the algorithm for each of the individual diagnosis. Taking into account only the most probable diagnosis by the algorithm, sensitivities for each etiology ranged from $100 \%$ ( 7 of 7 patients with reactive arthritis and 5 of 5 with Behçet correctly classified) to $51.2 \%$ ( 43 of 84 patients with idiopathic anterior uveitis). Specificities ranged from $88.8 \%$ for sarcoidosis to $99.5 \%$ for PosnerSchlossman syndrome.
We looked in detail at the three patients with Fuchs' heterochromic cyclitis that were misclassified by the algorithm, as an example of a type of uveitis with clear clinical presentation but without well-defined diagnostic criteria. One of the patients was misclassified as psoriasis arthritis, as he complained from back pain. Othe was misclassified as Posner-Schlossman syndrome, probably because IOP at presentation was higher than 25 mm Hg . A third patient was classified as idiopathic, but Fuchs' was the second most likely diagnosis.
A second model with equal pre-test probabilities for all 11 etiologies (Table 5, robustness analysis) correctly classified 87 of 210 ( $41.4 \%$ ) for the most probable etiology, and 109 of $210(51.9 \%)$ for first or second most probable etiologies.

## Discussion

The use of Bayesian belief networks has been previously reported for the differential diagnosis of a wide variety of conditions, from prostate ${ }^{5,6}$ and breast lesions, ${ }^{7}$ to dementia. ${ }^{8}$ To the best of our knowledge, this is the first time this technique has been applied to the differential diagnosis of uveitis. We have shown that a Bayesian Belief network is able to correctly classify common cases of anterior uveitis, agreeing to the diagnosis made by a senior clinician in a high percentage of cases. Interestingly, specificities obtained are generally very high, so it can be confidently used for the exclusion of the less likely etiologies. Sensitivities varied significantly among the different etiologies. Conditions with welldefined diagnostic criteria were correctly identified easily ( $100 \%$ for Behçet's disease and reactive arthritis, $80 \%$ for ankylosing spondylitis). However, those with poorly defined diagnostic criteria or which diagnosis is of exclusion and depends more on clinical expertise were

more frequently misdiagnosed by the algorithm ( $46.7 \%$ for ocular tuberculosis, $51.2 \%$ for idiopathic). This needs to be taken in consideration when using the algorithm, as TB-associated disease may need specific treatment and
investigations for other TB-associated conditions. The diagnosis of TB-related uveitis is very challenging for the clinician and currently lacks sensitive or specific tests. ${ }^{9}$ It is possible that our algorithm may simply be reflecting
![img-0.jpeg](img-0.jpeg)

Figure 1 Screenshots of the Bayesian network algorithm running in OpenMarkov version 0.0.1 (UNED, Madrid, Spain). (a) Edition mode. (b) Inference mode before entering information about the case. The probabilities observed in the central node (Uveitis) correspond to the observed prevalences in our population. (c) Inference mode after entering the observed data from patient 1 in Table 3 (highlighted in gray). Probabilities for each etiology in the central node have changed, making Sarcoidosis the most likely diagnosis for this patient.

Table 4 Comparison between clinical diagnosis and automated diagnosis by Bayesian belief network in 10 typical cases of anterior uveitis, after equalizing pre-test probabilities for the 11 etiologies in order to test robustness of the model


this. Nevertheless, we plan to refine this in the future on the light of new knowledge on TB-associated uveitis.

We believe that the use of this algorithm could help less experienced clinicians with the differential diagnosis of uveitis. In addition, it could help making decisions about ancillary test requests. Changes between pre-test and post-test probability can be simulated in the network for a specific patient. Hence, tests that significantly modify the probabilities can be favored against those that do not modify the post-test probability. This could help clinicians making a more efficient use of resources in a struggling economy.

Another useful application for this algorithm could be helping with tele-diagnosis in rural or isolated communities, by allowing the identification of patients that will require a more thorough investigation.

Importantly, this algorithm should not be taken as an exact test, but as a useful tool that can help medical decision making. Its main value is highlighting candidate etiologies, and guiding the way to clinical diagnosis. In uveitis, there is rarely certainty of diagnosis, and in many cases there are often several plausible candidate diagnoses. A benefit of the algorithm is that it provides a framework for expressing the likelihood of a diagnosis in probabilistic terms.

The authors advise any clinicians willing to use this tool for their own patients to modify the prevalence settings according to their own population. This can be easily made through the OpenMarkov software and this is essential for optimizing the algorithm. B27 positivity in our sample was lower than expected, as this allele has been shown to be present in up to $50 \%$ of anterior uveitis. ${ }^{10}$ This may be due to the fact that ours is a tertiary referral center, and most cases of B27-related anterior uveitis can be managed in secondary units. Thus, the prevalences we observed will probably be more similar to those of tertiary uveitis centers than secondary care eye clinics. Robustness analysis showed that, if prevalences are not adjusted to the local population, the model frequently incorrectly assigns patient to the least common etiologies. Interestingly, the robustness analysis showed a very-low sensitivity for diagnosing idiopathic uveitis. Cases of idiopathic anterior uveitis can be very heterogenic, and this is an exclusion diagnosis. This shows that if the pre-test probability for idiopathic is turned down, the algorithm tends to assign the patients to an etiologoic diagnosis even though the patient's finding are not sufficient for assigning that diagnosis to them.

In our study, we used a random sample size of 200 cases in order to calculate the prevalences of the different etiologies in our area. Assuming a binomial distribution and the observed prevalence of $1 \%$, we would have needed a sample size of at least 914 cases in order to

Table 5 Sensitivity and specificity of the Bayesian network-based algorithm for each tested etiology, before and after equalizing the 11 pre-test probabilities


have a $95 \%$ probability of observing a minimum of 5 cases of Behçet's disease, the least frequent etiology in our study. Users should bear in mind the importance of selecting a minimum sample that will provide a robust estimate of the prevalences of rarer causes of uveitis. In our study, as acquiring such a large validation sample would have been impractical, we decided to enrich the random validation sample with several non-random cases of the more rare etiologies, in order to include a minimum of five cases per etiology.

Our model has a series of limitations. First, some important conditions like herpetic uveitis, syphilis or multiple sclerosis have not been included among the etiologic candidates. Uveitis can be secondary to many different conditions, both infective and noninfective. For practicality reasons, we had to limit the number of etiologies to the most frequent in our practice. We plan to include more etiologies in new versions of the algorithm if it is found to be useful in clinical practice.

Second, the age of the patient is a very important feature for the diagnosis of uveitis. This predictive factor was excluded as it is non-binary, and including it would have much complicated the development of the algorithm. Again, if we find the algorithm to be useful in clinical practice, we plan to incorporate a child vs adult feature in future versions of the software.

Finally, another important limitation of this study is its retrospective nature. Some signs and symptoms may have been omitted in the case notes and could not be entered in the model. Traditionally, clinicians do not always record the absence of signs as negative findings, although documenting this may be more prevalent in countries with more litigious healthcare systems. These unavailable data were treated as missing information in the algorithm, which may have artificially weakened the diagnostic ability of the algorithm.

In summary, the Bayesian network developed may help clinicians with the differential diagnosis of anterior uveitis. In addition, it can help with the selection of the diagnostic tests performed, by avoiding those that will not change post-tests probabilities. However a large prospective study will be required to robustly test the diagnostic performance of the Bayesian network against senior clinician gold standard.

## Summary

## What was known before

- Recently, Bayesian belief networks have started to be used in medical diagnosis.


## What this study adds

- This study shows the development and validation of a Bayesian belief network algorithm that can help clinicians with the differential diagnosis of anterior uveitis.


## Conflict of interest

JJG-L has received study grants from Alcon, Novartis, Thèa and Merck, and has provided consultancy to Bayer. The remaining authors declare no conflict of interest.

## Author contributions

JJG-L, ÁMG-A, PB, and MCW carried out conception and design of the article; JJG-L and MCW performed the analysis and interpretation of results; JJG-L helped in writing the article; ÁMG-A, PB, and MCW helped in critical revision of the article; JJG-L, ÁMG-A, DS-P, NM-S, NF-L, PB, and MCW helped in final approval of the article; JJG-L, ÁMG-A, DS-P, NM-S, and NF-L helped in data collection; ÁMG-A, PB, and MCW took part in provision of materials, patients, or resources; JJG-L and

MCW helped in statistical expertize; JJG-L, ÁMG-A, and PB performed the literature search.

## Acknowledgements

The contents of this article were presented at the 2015 ARVO Annual Meeting in Denver, Colorado (abstract number 3123). We thank Dr Maria Pefkianaki for her administrative support.
