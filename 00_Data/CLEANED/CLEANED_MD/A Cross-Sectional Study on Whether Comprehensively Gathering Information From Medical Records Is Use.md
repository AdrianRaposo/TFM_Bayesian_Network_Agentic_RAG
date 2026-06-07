# A Cross-Sectional Study on Whether Comprehensively Gathering Information From Medical Records Is Useful for the Collection of Operational Characteristics 

Daiki Yokokawa ${ }^{1}$, Takanori Uehara ${ }^{1}$, Yoshiyuki Ohira ${ }^{2}$, Kazutaka Noda ${ }^{1}$, Naofumi Higuchi ${ }^{3}$, Eigo Kikuchi ${ }^{4}$, Kazuaki Enatsu ${ }^{5}$, Masatomi Ikusaka ${ }^{1}$<br>1. General Medicine, Chiba University Hospital, Chiba, JPN 2. General Medicine, International University of Health and Welfare Narita Hospital, Chiba, JPN 3. General Medicine, Kameda Medical Center, Kamogawa, JPN 4. General Medicine, Kawakita General Hospital, Tokyo, JPN 5. Pathology/Medical Inspection, Tokyo Metropolitan Tama Medical Center, Fuchu, JPN

Corresponding author: Daiki Yokokawa, dyokokawa6@gmail.com


#### Abstract

This study tests whether comprehensively gathering information from medical records is useful for developing clinical decision support systems using Bayes' theorem. Using a single-center cross-sectional study, we retrospectively extracted medical records of 270 patients aged $>16$ years who visited the emergency room at the Tokyo Metropolitan Tama Medical Center with a chief complaint of experiencing headaches. The medical records of cases were analyzed in this study. We manually extracted diagnoses, unique keywords, and annotated keywords, classifying them as either positive or negative. Cross tables were created, and the proportion of combinations for which the likelihood ratios could be calculated was evaluated. Probability functions for the appearance of new unique keywords were modeled, and theoretical values were calculated. We extracted 623 unique keywords, 26 diagnoses, and 6,904 annotated keywords. Likelihood ratios could be calculated only for 276 combinations ( $1.70 \%$ ), of which $24(0.15 \%)$ exhibited significant differences. The power function+constant was the best fit for new unique keywords. The increase in the number of combinations after increasing the number of cases indicated that while it is theoretically possible to comprehensively gather information from medical records in this way, doing so presents difficulties related to human costs. It also does not necessarily solve the fundamental issues with medical informatics or with developing clinical decision support systems. Therefore, we recommend using methods other than comprehensive information gathering with Bayes' theorem as the classifier to develop such systems.


Categories: Internal Medicine, Healthcare Technology
Keywords: bayes' theorem, clinical support systems, headache, operational characteristics, medical records

## Introduction

Clinical decision support systems improve clinical decision-making [1] and reduce diagnostic error rates [2]. Further, using natural language processing (NLP) to extract numerous diagnoses and keywords from electronic medical records (MRs) could facilitate the development of clinical decision support systems [3,4]. Prior studies on the creation of disease classification models for various diseases [5-10] used NLP to extract predetermined feature values as keywords.

Developing clinical support systems requires appropriate data and classifiers. Although many machine learning and deep learning models have been published in the last decade, Bayes' theorem remains a classic and powerful clinical tool [11]. This theorem $[6,8,12]$ is often selected as the classifier owing to its similarity to clinicians' reasoning; it requires data in the form of combinations of diagnoses and keywords to calculate operational characteristics, for example, the likelihood ratio (LR). However, the mechanical processing of MRs has some deficiencies. First, non-medical professionals may have difficulty interpreting the terminology in medical data [13]. Additionally, the creation of an expert-level dictionary would be both costand labor-intensive [3], and narrative data are not encoded in a format suitable for immediate use, thereby requiring preparation [14]. Furthermore, although humans tacitly understand the content of negative words, the accuracy of machine processing is insufficient to add annotations to extracted keywords, particularly for positive and negative words ( $\mathrm{P} / \mathrm{N}$ assessment) [3], which is critical for clinical support systems.

Under limited data conditions, the first and second problems could be solved by having doctors manually analyze such data; however, with big data, manual analysis is not feasible. Therefore, a more robust data processing methodology is required. Nevertheless, under limited data conditions, another problem arises owing to keyword frequency. Bias in the frequency of each keyword may be problematic. The frequency of character strings in English has a power-law distribution [15,16]. If the frequency of keywords in Japanese MRs has a similar power-law distribution, if the data are long-tailed, there may be a bias regarding each

keyword's frequency.

Therefore, even if big data can be collected, this may not increase the number of completed places in the diagnosis and keyword cross table. Therefore, we examined the number and usefulness of operational characteristics obtained from MR data using a cross table created from annotated keywords (AKs) and diagnoses extracted manually from MRs. We also measured the level of equality in keyword frequencies and modeled the probability functions for the appearance of new keywords. Thus, this study aimed to determine whether the comprehensive collection of MRs could contribute to the development of clinical support systems using Bayes' theorem.

# Materials And Methods 

## Setting and participants

This was a single-center study. We retrospectively extracted the MRs of patients aged $\geq 16$ years whose chief complaint was experiencing headaches and who visited the emergency room (ER) at the Tokyo Metropolitan Tama Medical Center between May 1 and June 30, 2014. Approximately 150 patients experiencing headaches visit the hospital every month. The number of patients' records that could be annotated by reviewing all MRs was approximately 300. Patients were included in the study if they visited the hospital on their own or by ambulance. In Japan, pediatricians treat patients under 16 years of age. The hospital under study does not have a pediatric department; therefore, patients under 16 years of age were excluded. Similarly, if patients were in a severe or critical condition, having experienced a stroke or shock based on vital signs and symptoms noted in the ER or ambulance, they were transferred to a critical emergency center, which became responsible for tertiary care, and thus were excluded from the study.

## Keyword extraction, P/N word assessment, and name of diagnosis coding

Two of the researchers extracted and recorded unique keywords (UKs) from MRs written by doctors (Figure 1). Subsequently, they recorded the results of the assessment of these P/N keywords as AKs. UKs were extracted regarding current and previous medical histories (Hx) and findings of physical and laboratory examinations or imaging (Px). MR entries were not converted, but arbitrary interpretations were eliminated. We generated the AKs via P/N assessment. Referencing previous studies [3,17], assessments were based on the context and presence of negative phrases such as "negative for..." and "...not present." Keywords that did not appear in a case were treated as "no data (null)." AKs were expressed as the total number of keywords that appeared in the text of MRs. The number of UKs and AKs were calculated separately for Hx, Px, positive findings, and negative findings, and the number per case was calculated.

![img-0.jpeg](img-0.jpeg)

FIGURE 1: Extraction from natural language
ICHD-II: International Classification of Headache Disorders 2nd edition; P: positive; N: negative

Diagnosis names extracted from the MRs were coded using the International Classification of Headache Disorders 2nd edition (ICHD-II) [18]. Cases in which a diagnosis was not reached, such as 'cause unknown,' 'non-urgent headache,' or 'non-specific headache,' were coded as 'Other headaches, head neuralgia, central or primary facial pain (ICHD-II code: 14.0.0).'

# Creating the cross table and calculating each UK's operational characteristics 

A cross table was created to store the combinations of UKs and ICHD-II diagnoses for all cases. First, true positives (TPs) and true negatives (TNs) were counted using the number of AKs for each ICHD-II diagnosis. Next, TPs and TNs were subtracted from the total AKs, including non-ICHD-II diagnoses, to calculate the number of false positives (FPs) and false negatives (FNs). Operational characteristics (sensitivity, specificity, positive predictive value (PPV), negative predictive value (NPV), positive LRs, and negative LRs) were calculated based on these data. However, because the LRs cannot be calculated unless the TP, TN, FP, and FN values are all $>1$, we determined the number and proportion of combinations for which LRs could be calculated. Furthermore, we examined the operational characteristics that exhibited significant differences in the cross table, using a chi-squared test; subsequently, we calculated their number and proportion.

## Creation of keyword histograms and examination of long-tailed distributions

The UKs were sorted in descending order of frequency as AKs to create a histogram. Because the histogram was expected to be long-tailed, the proportion of UKs with a frequency $>4$ or 1 were calculated for both Hx and Px , and the differences in the ratios were examined. Moreover, because UKs can be categorized as positive or negative, these proportions were also calculated and compared between these two groups.

To investigate long-tailed distributions, the proportion of AKs in the top $1 \%, 10 \%$, and $20 \%$ were shown in a histogram ordered by AK frequency, and the differences in their ratios were examined. Additionally, equality of the AKs' frequency was used to examine whether the keyword's frequencies had a long-tailed distribution. Indicators of equality include the Gini coefficient (GC) [19,20]. Larger GC values suggest that the distribution is lopsided and long-tailed [21], whereas smaller values indicate that the distribution is more uniform: 0-perfect equality and 1-perfect inequality. The formula for calculating the GC is as follows:

GiniCoefficient $=2 \times\left(0.5-\int_{0}^{1} L(x) d x\right)$. Here, the Lorenz curve is $L(F)=\frac{\int_{0}^{F} \times\left(F^{\prime}\right) d F}{\int_{0}^{1} \times\left(F^{\prime}\right) d F}, \mathrm{~F}(\mathrm{x})$ is the cumulative distribution function for the keyword frequency, and $\mathrm{x}(\mathrm{F})$ is the inverse function of $\mathrm{F}(\mathrm{x})$.

In this study, the GC was calculated for the frequency of AKs for each UK. This was calculated separately for Hx and Px and for positive and negative findings.

# Regression models of probability functions for the appearance of new keywords 

Modeling the increase in dependent variables per case was performed with the frequency of AKs, new UKs, and new ICHD-II diagnoses as the dependent variables and the number of cases as the independent variable. Using linear regression, we calculated the estimated values, standard errors, and coefficients of determination $\left(R_{2}\right)$ for primary linear, power, and logarithmic functions. Furthermore, considering the model's shape and characteristics, a power function+constant model was created as a form of nonlinear regression, which was used to perform similar calculations. In the nonlinear regression, R2 was calculated as 1 (the residual sum of squares/corrected sum of squares). We entered $10^{1}-10^{5}$ cases into the regression formulas to determine how this changed the dependent variable and concentration values.

## Analytics

A chi-squared test was conducted for the operational characteristics, and 95\% CIs were calculated. The Clopper-Pearson method was used when there were few samples. Z-scores were calculated by testing differences between the ratios of keyword frequencies and other items. All statistical analyses were conducted using IBM SPSS Statistics for Windows, Version 25.0 (Released 2017; IBM Corp., Armonk, New York, United States). The threshold for significance was set at $\mathrm{p}<0.05$.

## Results

The MRs of 270 patients were analyzed. We extracted 36 diagnoses classified into 26 headache diseases based on the ICHD-II. Table 1 shows the ICHD-II diagnoses and the number of cases. The most frequent diagnosis was 'other headaches, head neuralgia, and central or primary facial pain' (ICHD-II code: 14.0.0; 73 cases, $27.0 \%$ ), followed by 'migraine' (ICHD-II code: 1; 36 cases, 13.3\%), 'tension-type headache' (ICHD-II code: 2; 33 cases, 13.0\%), and 'headache due to systemic viral infection' (ICHD-II code: 9.2.2; 30 cases, $11.1 \%)$.


![img-1.jpeg](img-1.jpeg)

# TABLE 1: Diagnosis names and number of cases

# UKs and frequencies 

There were 623 UKs and 6,904 AKs. Table 1 shows UK and AK frequencies for $\mathrm{Hx}, \mathrm{Px}$, positive findings, and negative findings. There were 5.1 times more UKs for Hx than for Px ( 521 vs. 102) and 2.3 times more for positive findings than for negative ones ( 552 vs. 237). There were 1.2 times more AKs for Hx than for Px $(3,789$ vs. 3,115$)$ and 1.5 times more for negative findings than for positive ones ( $4,164 \mathrm{vs} .2,740$ ). AKs' frequency per case was 1.5 times higher for negative findings than for positive ones ( 15.42 vs. 10.15 ).

## Proportion of calculable operational characteristics and their contents

Table 2 shows UK and AK frequencies and proportions in the cross table for which the operational characteristics could be calculated. A 623+26 cross table was created ( 16,198 entries). LRs were calculated for 276 combinations ( $1.70 \%$ of the total); of these, $24(0.15 \%)$ exhibited significant differences, according to the chi-squared test. Table 3 details the operational characteristics of these 24 combinations. For migraines, the keywords nausea, vomiting, and photosensitivity exhibited significant differences.


TABLE 2: Frequency of unique keywords, annotated keywords, and calculated combinations
N : number of; PPV: positive predictive value; NPV: negative predictive value; LR: likelihood ratio; Hx: history; Px: physical examinations and tests; Pos: positive; Neg: negative; P/N: positive/negative




# TABLE 3: Operational characteristics with significant differences 

The keywords shown in the table represent only those from among the 16,198 entries that exhibited significant differences in likelihood ratios
$\dagger$ : significant difference; $\alpha: 0.05$; CI: confidence interval; Hx: history; Px: physical examinations and tests; PPV: positive predictive value; NPV: negative predictive value; PLR: positive likelihood ratio; NLR: negative likelihood ratio; ICHD-II: International Classification of Headache Disorders 2nd edition

## Long-tailed distribution of keyword frequencies

Figure 2 shows the histograms of each UK's frequency in the MRs (frequency of AKs). The histograms are long-tailed, being more pronounced for Hx and positive findings than for Px and negative findings. Table 4 shows an analysis of the long-tailed distributions of keyword frequencies. The frequencies in the top $20 \%$ comprised $78.2 \%$ of the total $(5,428 / 6,904)$. UKs with a frequency of 1 in the tail made up $36.4 \%$ of the total. UKs with a frequency $>4$ comprised $43.2 \%$ of the total, showing that over half of the UKs' frequency was lower than 4 , which is the minimum needed for calculations in the cross table. Hx and positive findings had larger percentages of UKs with a frequency $>4$, compared with Px and negative findings. Table 5 shows the 623 UKs arranged by frequency. The overall GC was high ( 0.726 ); a high GC indicates a lack of frequency equality, with large disparities in the number of keyword frequencies. This finding is consistent with longtailed histograms. Figure 5 shows the Lorenz curves.
![img-2.jpeg](img-2.jpeg)

FIGURE 2: Histograms of annotated keywords
(A) Histogram of keywords related to histories and physical exams and tests. (B) Histogram of keywords annotated with positive and negative


TABLE 4: Analysis of long-tailed distributions of keyword frequencies
Hx: histories; Px: physical exams and tests; Pos.: positive; Neg.: negative; UK: unique keyword; AK: annotated keyword; Z: Z score; GC: Gini coefficient


TABLE 5: Ranking of numbers of annotated keywords
Pos.: positive; Neg.: negative

![img-3.jpeg](img-3.jpeg)

# FIGURE 3: Lorenz curves 

(A) Lorenz curves related to histories and physical exams and tests. (B) Lorenz curves related to keywords annotated with positive and negative

## Regression models of probability functions for the appearance of new keywords

Table 6 and Table 7 present the modeling and regression results. Linear regression was possible for increases in the AKs. Modeling new UKs and ICHD-II diagnoses per increase in the number of cases showed that, for both linear and nonlinear functions, the best fit was a power function+constant. In both cases, the exponent of the independent variable was $<1$, and the curve was convex at the top.

![img-4.jpeg](img-4.jpeg)

TABLE 6: Assigning theoretical values to regression models and equations
*In nonlinear regression, $R^{2}$ was calculated as 1-(residual sum of squares/corrected sum of squares)
Std. error: standard error; ICHD-II: International Classification of Headache Disorders 2nd edition


TABLE 7: Best-fit models to theoretical values for variables
ICHD-II: International Classification of Headache Disorders 2nd edition

# Discussion 

In this study, 623 UKs, 6,904 AKs, and 26 diagnoses were manually extracted from 270 MRs. A cross table with 16,198 combinations of keywords and diagnoses was created, but only $1.70 \%$ of the cross tables were completed. We surmised that a comprehensive extraction of MR information would not suffice to gather all the necessary information required to calculate LRs. We also analyzed the distribution of keyword frequencies in MRs. While the top $20 \%$ comprised $78 \%$ of the frequencies, the histogram had a long tail, with

36.4% of the keywords appearing only once. Because we could not find any previous reports on GC based on free textual descriptions in electronic MRs, no comparisons were possible. However, the GC of 0.726 indicates extremely high inequality, which is consistent with a long-tailed distribution. Therefore, even with a rise in cases, a uniform collection of keywords crucial for calculating operational characteristics cannot be guaranteed. Thus, the comprehensive collection of big data from electronic MRs may not necessarily contribute to developing clinical decision support systems with high diagnostic accuracy. This limitation is notable when using MRs as a data source for developing clinical decision support systems.

Negative data are considered to have the most important contextual characteristics of all clinical information and contribute greatly to classification accuracy [17,22]. In prior studies, mechanical P/N assessments of medical corpora have been performed in English [10,22,23], displaying precision and recall levels of 84% and 73%, respectively, for positive data and 84% and 82%, respectively, for negative data, which indicates that 20% of findings were misinterpreted [9]. In Japanese, the precision and recall levels of P/N assessments were 85.4% and 79.4%, respectively, for positive data, but only 67.6% and 33.3%, respectively, for negative data [7]. A study that extracted negative English words using an algorithm found that slightly less than half of the medical text contained negative information [24]. In the present study, there were 1.5 times more negative than positive data, which is higher than that in previous studies. It is expected for medical text to contain negative findings; however, the extraction of negative findings is often inaccurate, even when using algorithms [3], which is a limitation of recent NLP methods. The negative findings that previous studies' algorithms failed to extract may have been picked up manually by the present study's analysis.

Many of the unique Hx keywords and AKs indicated positive findings; further, for many combinations, PPV could be calculated only with positive findings (Table 1). The reason Hx had more positive findings could be that Hx is dependent on patients' complaints, which means that symptoms they do not mention are unlikely to be recorded. Additionally, patients tend to express their complaints in unique ways, which could make it difficult to identify them with negative words in the natural language. As Table 2 shows, there were some examples of Hx of negative LRs with significant differences, while, in everyday clinical practice, negative Hx commonly contributes to diagnosis.

Meanwhile, Px had many negative findings, and the NPV could be calculated for many combinations. This is likely because physical examinations generally have low sensitivity and are gathered systematically, which generates numerous negative findings. Systematically gathering results is expected to lead to high levels of equality without a long tail (i.e. a short tail). Visually, Px and negative findings are evident in the shorter tails in Figure 2.

One explanation for the more short-tailed appearance of Px and negative findings in Figure 2 is that these categories exhibited clearer sublanguage characteristics, compared with Hx and positive findings, as they had a stronger limitation on the number of words. Past studies indicate that medical texts constitute a sublanguage [25] (i.e. a language used in certain domains by specialized individuals) [26,27] with a limited number of word frequencies and co-occurrence patterns, namely, closure properties, unlike natural language. This is because sublanguages are used to share information among individuals who have similar training and use the same lexicon [28]. Thus, the individuals who wrote the MRs analyzed in our study also comprise a subgroup.

The theoretical values from the regression equations had a power function for the number of UKs and diagnoses and a linear function for the number of AKs. Collecting more cases, UKs, and diagnoses could increase the number of combinations in the cross table. Collecting more AKs would also increase the number of combinations. However, there are two problems associated with increasing the number of combinations. First, AKs had a long-tailed distribution. The keywords appearing in specialist journals extracted from MEDLINE [29] exhibit a long-tailed distribution. If the distribution of AK frequencies in MRs is long-tailed, that in unexamined MRs are also likely to be long-tailed, which means that regardless of how many MRs are collected, the structure of data accumulating in the head and not in the tail will remain identical. Second, a power-law distribution is the best fit for the probability distributions of newly appearing UKs and diagnoses, while their appearance frequencies decrease as the number of diagnoses increases. This suggests that electronic MRs have sublanguage characteristics: closure properties. Therefore, manual annotation would not increase the subsequent efficiency to increase UKs and diagnosis, even if numerous records are gathered [30].

Thus, we cannot conclude that as the concentration rises and the number of combinations that complete the cross table increases, so will the number of combinations with operational characteristics that have significant differences. In fact, only the extremely low 0.15% combination exhibited significant differences in this study.

Limitations

This was a single-center study, which limits the generalizability of the results. Disease occurrence and the reproducibility of physician examinations are limited, potentially introducing selection bias. Further, the entries in the MRs made by non-neurologists working in the ER may have been inaccurate. Although the

headache diagnoses were standardized using the ICHD-II, neurologists were not consulted. Additionally, the study period only lasted two months, which meant we were unable to determine the impact of seasonal diseases, which may have biased the diagnoses' distribution. Moreover, the physical examinations' findings may have been inaccurate. These results may have been affected by cultural background and expressions in the Japanese language. Japanese electronic MRs do not describe phenotypes sufficiently and are not intended for reuse in terms of the quality and structuring of the data [4].

# Conclusions 

To obtain accurate data, we improved data source selection, extraction, and pre-processing by using narrative MR data and manual annotations. Despite achieving near-perfect accuracy, some combinations could not yield LRs. This study highlights the limitations of using narrative clinical reports for clinical support systems, advocating for a comprehensive approach. Effective design should integrate multiple strategies, including large language models and expert systems, rather than relying solely on algorithms based on Bayes' theorem or LRs.

## Additional Information

## Author Contributions

All authors have reviewed the final version to be published and agreed to be accountable for all aspects of the work.

Concept and design: Daiki Yokokawa, Takanori Uehara, Naofumi Higuchi, Eigo Kikuchi, Kazuaki Enatsu, Masatomi Ikusaka

Acquisition, analysis, or interpretation of data: Daiki Yokokawa, Yoshiyuki Ohira, Kazutaka Noda, Naofumi Higuchi, Eigo Kikuchi, Kazuaki Enatsu

Drafting of the manuscript: Daiki Yokokawa, Takanori Uehara

Critical review of the manuscript for important intellectual content: Daiki Yokokawa, Takanori Uehara, Yoshiyuki Ohira, Kazutaka Noda, Naofumi Higuchi, Eigo Kikuchi, Kazuaki Enatsu, Masatomi Ikusaka

## Disclosures

Human subjects: Consent was obtained or waived by all participants in this study. Animal subjects: All authors have confirmed that this study did not involve animal subjects or tissue. Conflicts of interest: In compliance with the ICMJE uniform disclosure form, all authors declare the following: Payment/services info: All authors have declared that no financial support was received from any organization for the submitted work. Financial relationships: All authors have declared that they have no financial relationships at present or within the previous three years with any organizations that might have an interest in the submitted work. Other relationships: All authors have declared that there are no other relationships or activities that could appear to have influenced the submitted work.
