## OPEN ACCESS

EDITED BY
Ovais Wadoo,
Qatar University, Qatar
REVIEWED BY
Wei Luo,
Chinese Center for Disease Control and
Prevention, China
Sheikh Mohd Saleem,
Ministry of Health and Family Welfare, India
Sami Ouanes,
Hamad Medical Corporation, Qatar
*CORRESPONDENCE
Li Ling
lingli@mail.sysu.edu.cn
SPECIALTY SECTION
This article was submitted to
Public Mental Health,
a section of the journal
Frontiers in Public Health
RECEIVED 30 August 2022
ACCEPTED 23 December 2022
PUBLISHED 17 January 2023
CITATION
Tang X, Fan C, Wang C, Wang W, Chen Z, Xu C and Ling L (2023) The risk assessment of relapse among newly enrolled participants in methadone maintenance treatment: A group-LASSO based Bayesian network study. Front. Public Health 10:1032217.
doi: 10.3389/fpubh.2022.1032217
COPYRIGHT
(c) 2023 Tang, Fan, Wang, Wang, Chen, Xu and Ling. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

## The risk assessment of relapse among newly enrolled participants in methadone maintenance treatment: A group-LASSO based Bayesian network study

Xijia Tang ${ }^{1}$, Chaonan Fan ${ }^{1}$, Chijie Wang ${ }^{1}$, Wenjuan Wang ${ }^{1}$, Zouxiang Chen ${ }^{1}$, Chaofan Xu ${ }^{1}$ and Li Ling ${ }^{1,2 *}$<br>${ }^{1}$ Department of Medical Statistics, School of Public Health, Sun Yat-sen University, Guangzhou, Guangdong, China, ${ }^{2}$ Clinical Research Design Division, Clinical Research Center, Sun-Yat sen Memorial Hospital, Sun Yat-sen University, Guangdong, China

Background: Relapse is a great barrier to improving the effectiveness of methadone maintenance treatment (MMT). Participants with different treatment durations could vary in their compliance with MMT, which may lead to different levels of relapse risk. This study aims to identify the risk factors for relapse and assess the relapse risk of MMT participants of different treatment durations.
Method: This retrospective study used data collected from seven MMT clinics in Guangdong Province, China, from January 2010 to April 2017. Newly enrolled participants who received $6(n=903)$ and $12(n=710)$ months of consecutive treatment with complete data were included. We selected significant risk factors for relapse through the group lasso regression and then incorporated them into Bayesian networks to reveal relationships between factors and predict the relapse risk.
Results: The results showed that participants who received 6-month treatment had a lower relapse rate ( $32.0 \%$ ) than those of 12 -month treatment ( $39.0 \%, P<$ 0.05 ). Factors including personal living status and daily methadone dose were only influential to those who received the 6-month treatment. However, age, age at the initial drug use, HIV infection status, sexual behaviors, and continuous treatment days were common factors of both durations. The highest relapse risk for those after the 6 -month treatment was inferred as $66.7 \%$ while that of the 12 -month treatment was $83.3 \%$. Farmers and those who have high accessibility to MMT services may require additional attention.
Conclusion: It is necessary to implement targeted interventions and education based on the treatment durations of participants to decrease the relapse rate. Meanwhile, those about HIV/sexually transmitted infection prevention and anti-narcotics should be held in the whole process.

## KEYWORDS

methadone maintenance treatment, relapse, treatment duration, risk assessment, Bayesian networks

## Introduction

Methadone maintenance treatment (MMT) is one of the safest and most cost-effective substitution therapies to manage opioid dependence, which has been implemented in 84 countries and territories worldwide (1). It is thought to be effective in reducing high-risk behavior of opioid users, such as unprotected sex, syringe sharing, and contributing greatly to preventing human immunodeficiency virus (HIV) infection/acquired immunodeficiency

syndrome (AIDS). It also assists in crime reduction and enhances social productivity among opioid users (2, 3). China has the largest MMT program in the world, covering 29 of 34 provinces nationwide by 2020 (4, 5), and it has served nearly 10% of MMT participants globally. However, for most countries implementing MMT (6, 7), including China, relapse has always been a common and great barrier to its development. It is a complex consequence led by multiple factors and will put participants at higher risk of HIV infection and overdose, and negatively affects their return to day-to-day life (8). It was reported that 20--57% of MMT participants would relapse in the first 6 months and the rate would increase when they were treated longer (9--11). A study conducted in Iran showed that the relapse rate was approximately 30--50% after 12-month MMT (12) and was as high as 94% when the duration was extended to 18 to 36 months (13). Similarly, 31% of Chinese MMT participants reported relapse in the first 6 months and the rate rose to 56% after 12-month consecutive treatment (5).

Therefore, participants receiving MMT over different durations may be at different risk levels of relapse. Identifying high-risk groups and assessing the risk based on their treatment durations could help healthcare providers to target more aggressive adjunct therapies and increase the effectiveness of MMT. Previous studies have explored much about risk factors of relapse (14--19) and developed several tools for risk assessment (5, 16); however, there are still research gaps to be filled.

On the one hand, there were some commonly recognized risk factors including the age of onset of opioid abuse, frequent injection, insufficient methadone dose, and poor social support (5, 16, 20). Specifically, the younger age at the onset of substance use may increase the relapse risk due to genetic and environmental influences (21). Those who reported frequent injection behavior may require higher levels of opioids and suffer more social marginalization, making them difficult to manage on the MMT (16). In addition, the insufficient dose could not effectively control the euphoric effects of heroin and then cause withdrawal symptoms, which drives the participants to relapse (22). However, whether these factors and their effect size will vary along with treatment durations remains unclear.

On the other hand, the developed tools were usually constructed using the logistic regression model (23) or the Cox proportion hazard model (24). These methods did not perform well in dealing with the dependence on variables, which is the character of relapse. To solve this problem, previous studies chose to remove the variables with dependence (25) and apply stepwise (26) or penalized regression (27). The least absolute shrinkage and selection operator (LASSO) is one of the penalized regressions, and the group lasso regression, as an extension, can select variables at the group level instead of a single dummy variable (28), which suits analyzing the complicated outcome such as relapse. In addition, traditional methods could not reveal the association between variables and quantify the risk at the individual level either. Bayesian networks (BNs) are graphical models that describe the probability relationship between a set of variables (29). BNs have been increasingly used to predict the risk of particular diseases, such as accurate kidney injury (28) and chronic obstructive pulmonary disease (30), while none was found in the field of MMT yet.

In this study, we combined these two methods to triage the high-risk groups and assess the relapse risk of different treatment durations. Hopefully, our findings will be instructive for developing individualized treatment plans for MMT participants to improve their compliance and decrease the relapse rate.

## Materials and methods

### Study design and data source

This is a retrospective study that used secondary data to assess the risk of relapse among newly enrolled MMT participants of different treatment durations. We selected Guangdong province as the study setting, as it had the highest rate of drug crimes (31) and 30% of registered drug users in China by 2018 (32), and it has established 66 MMT clinics, ranking 4th place in the country (4). We employed a two-stage stratified sampling methodology by first choosing eight cities in Guangdong with different levels of economic development, and then randomly selecting one or two MMT clinics from each city. Accordingly, 10 MMT clinics were selected and three of them were excluded for the lack of baseline information. A total of seven MMT clinics were finally included.

The data analyzed in this study were derived from the web-based National Unified MMT management system.

### Data collection

We collected the unidentifiable baseline information of newly enrolled participants from January 2010 to April 2017 from a questionnaire developed by the National Working Group on MMT. All participants gave their written consent for their information to be stored in the national web-based MMT system and allowed to use for research (33). This survey was completed by the clinic staff and included demographic information, sex, drug use-related behavior, and infection status (HIV and HCV). The HIV antibody was initially screened by the colloidal gold method, and positive samples were confirmed using Western blotting. The HCV antibody test was conducted using the enzyme-linked immunosorbent assay method. Both tests were conducted at enrollment. The daily methadone dose and the result of monthly urine morphine were also collected. All the aforementioned tests were conducted by doctors of the MMT clinic or the local center for disease control and prevention (CDC).

Participants were eligible if they were >18 years old, provided written informed consent, and were diagnosed as opioid-dependent using the Chinese Classification of Mental Diseases Criteria (third version). The description definition of these criteria was improved based on ICD-10 and the diagnostic criteria were referred to ICD-10 and the Diagnostic and Statistical Manual of Mental Disorders, 4th edition (DSM-IV) (34), but it had a unique definition of some disorders, such as culturally related diagnoses. Participants who were re-enrolled or referred from another MMT clinic, who were residents outside Guangdong, and who had an incomplete record of the daily dose and urine morphine test were excluded.

### Outcome and definitions of calculated variables

#### Relapse

Our primary outcome is whether the participants relapsed during the MMT. Relapse in this study was defined as showing at least two consecutive positive results of the monthly urine morphine test during treatment, in line with the relevant literature and guidelines (11, 20, 35--37). The first 10 to 30 days after the enrollment was usually

considered the adjustment phase (38) and there was still a relatively high possibility for participants to use heroin during this period. Therefore, the result of the urine morphine test in the first month was excluded from the analysis, and the actual treatment durations were extended to 7 and 13 months accordingly.

## Initial daily methadone dose

The initial daily methadone dose indicated the average daily methadone dose of the first week of MMT, rather than that of the first day, to provide a stable result.

## Continuous treatment days

Drop-out was usually defined as being absent from MMT for more than 14 consecutive days (39). The continuous treatment days were days participants resumed MMT after their last drop-out (18). For those who did not drop out, continuous treatment days equaled their entire treatment duration. This is an indicator of the compliance of participants.

## Statistical analysis

To assess the risk of relapse among MMT participants, we used the group lasso regression to select significant risk factors and then incorporate them into Bayesian networks to make risk predictions.

To be more detailed, the lasso regression applies the L1 norm to the unknown coefficient vector and the coefficients with smaller absolute values would be directly compressed to 0 , those with nonzero coefficients were considered significant variables (40). Factors associated with relapse are usually dependent on each other while the lasso regression will treat them as independent variables (41). We used the group lasso instead to select predefined grouping variables (28). The parameter estimation of the group lasso is presented as follows:

$$
\hat{\beta}^{G r L a s s o}=\arg _{\beta} \min \left\{\sum_{i=1}^{n} \frac{1}{2}\left(y_{i}-\sum_{j=1}^{p} x_{i j} \beta_{j}\right)^{2}\right\}+n \lambda \sum_{j=1}^{p}\left\|\beta_{j}\right\|
$$

Where $j$ presents the number of groups of the variables and each group has $p_{1}, p_{2}, \ldots p_{j}$ levels. $\lambda$ is the adjusted parameter, which was used to control the extent of the penalty, and the optimal parameter was selected by k -folded cross-validation. The minimum cross-validation error refers to the best model (28).

The selected variables were then used to establish Bayesian networks (BNs). BNs consist of a directed acyclic graph (DAG) and conditional probability tables (CPT). DAG is constructed based on the assumption of conditional independence, and the probability dependence among nodes is quantified by CPT, specified as follows:

$$
P(X)=\prod_{i=1}^{N} P\left(X_{i} \mid \prod_{k} \Theta_{X_{i}}\right)
$$

Where $P(X)$ indicates the probability of the outcome, $\Theta_{X_{i}}$ represents the parameter of node $X_{i}$, and $\prod_{X_{i}}$ means the parent node set of $X_{i}$. A complete BN model is established through parameter learning and structure learning. In this study, we chose maximum likelihood estimation as the parameter learning method. Tabu-search was chosen as the structure learning method as it can avoid the locally optimal solution (29).

The Pearson chi-square test or Fisher's exact test (when the expected frequencies were $<1$ in either cell or $<5$ of over $20 \%$ of cells) was used to compare the difference in the distribution of categorical variables between participants who relapsed and those who did not, and $\alpha$ was set as 0.1 . The area under the receiver operating characteristic curve (AUC) was applied to estimate the prediction capacity of the models. Missing values were imputed using multiple imputations, as it suited most types of data (42).

## Sensitivity analysis

This study included the initial daily dose to reflect the baseline status of participants, while the average daily dose of the whole maintenance period was also a determinant for relapse. Therefore, we alternatively included the average daily dose of the whole maintenance period in the group lasso regression models for both treatment durations to examine its significance on relapse.

All the analyses were performed using R 4.1.0 (R Foundation for Statistical Computing, Vienna, Austria). The BN models were visualized by Netica 5.18 (Norsys Software Corp., Vancouver, BC, Canada).

## Results

From January 2010 to April 2017, a total of 903 newly enrolled participants with completed records received MMT for over 6 consecutive months, 710 of whom have received treatment for 12 months. The detailed process of participant inclusion is displayed in Figure 1. We found that $32.0 \%$ (289) of them relapsed during the first 6 months. Among those who persisted in MMT for 12 months, $39.0 \%$ of them (277) relapsed in the process. This was significantly more than those who received 6 -month treatment $(P=0.003$, Table 1) and only $27.8 \%$ of the relapses occurred in the last 6 months. Supplementary Tables 1, 2 showed the baseline characteristics of participants of both treatment durations.

## The variables selection through the group lasso regression

The optimal parameter $\lambda$ was specified in the group lasso regression through the 10 -fold cross-validation error and was used to select significant variables (Figure 2). A total of 18 groups of variables were considered as risk factors for participants who have received the 6 -month treatment, while eight groups of variables were chosen for those who have received the 12 -month treatment. The coefficients of variables are presented in Supplementary Table 3, where 0 indicates the statistical insignificance.

## BN model for the risk assessment of relapse

The initial BN models for 6- and 12-month treatments were constructed using the Tabu-search algorithm (Supplementary Figures 2, 3) and were then adjusted based on

![img-0.jpeg](img-0.jpeg)

FIGURE 1
Flow chart of participants' inclusion. Excluded because of the incomplete data, test results, or record of daily methadone dose.

the published literature and experience of experts in this field (Figure 3). The nodes were clarified into four types, which comprised outcome (relapse), demographic factors, drug use, and sex behavior-related factors.

For participants who have received the 6-month MMT, we found that HIV infection status, age at the initial drug use, continuous treatment days, the time required to reach the clinic, communication with drug friends in the last month, and the relationship with family members were directly related to relapse. Those who were HIV-positive, first used drugs before 20 years of age, had an estranged relationship with family, communicate with friends who used drugs at least once a week, and had received treatment for more than 90 days consecutively had the highest possibility (66.7%) of relapse (Figure 4A).

When the treatment duration was extended to 12 months, only age, age at the initial drug use, HIV infection status, and continuous treatment days were directly associated with relapse. In this case, HIV-negative participants, who were below 30 years of age, first took drugs at the age of 20–30 years, and received MMT for 30–60 days since the last drop-out, would have the highest relapse risk of

83.3% (Figure 4B). When a participant who received the 6-month treatment was under the same situation mentioned earlier, the risk would decrease to 46.3% (Supplementary Figure 4).

We also investigated the conditional probabilities of nodes that only were significant in either the 6- or 12-month model, including jobs, initial daily doses, the time needed to the clinic, and the transportation they took to the clinic. Specifically, among those who were treated for 6 consecutive months, farmers (40.1%), participants who took <30 mg per day at the initial stage (40.2%), and who needed <10 min to reach the clinic (48.3%) were predicted to have the highest risk of relapse (Table 2). The above groups also accounted for the largest proportion among those with the shortest retention (<30 continuous treatment days), compared with other subgroups, which were 17.0, 14.3, and 19.3%, respectively (Supplementary Table 6).

As for participants who received MMT for 12 months, the transportation that they took to the clinic was an additional factor that impacted relapse. Those who drove to the clinic were most possible to relapse (39.6%, Table 3) and to have retention of fewer than 30 days (10.7%, Supplementary Table 6), while those who walked to the clinic had the lowest risk.

TABLE 1 The proportion of relapse among newly enrolled participants who received 6 and 12 months of consecutive MMT in seven clinics in Guangdong Province.


### Evaluation of model performance

The group lasso is always combined with logistic regression when the dependent variable is binary. Thus, we compared the group lasso logistic model and the group lasso BNs model, using the AUC value. Figure 5 illustrated that the BNs model had better performance (6-month model: AUC = 0.835, 95%CI: 0.810–8.863; 12-month model: AUC = 0.659, 95%CI: 0.630–0.712) than the logistic model (6-month model: AUC = 0.700, 95%CI: 0.664–0.737; 12-month model: AUC =

![img-1.jpeg](img-1.jpeg)

FIGURE 2 Variables selection using the group lasso regression. (A, B) present the 10-fold cross-validation error of the parameter λ based on the baseline data of newly enrolled MMT participants who received the 6- and 12-month consecutive treatments, respectively. (C, D) present the parameter solution path based on the baseline data of newly enrolled MMT participants who received the 6- and 12-month consecutive treatments, respectively. The gray dashed line denotes the optimal λ of each model. Every colored line means a single variable and those that the gray passed across were selected.

![img-2.jpeg](img-2.jpeg)

FIGURE 3 Adjusted BN model of factors related to relapse among participants receiving the 6- and 12-month consecutive MMT. Each color indicates a particular type of variable. (A) The adjusted BN model of factors for relapse of MMT participants after the first 6-month treatment. (B) The adjusted BN of that during the first 12-month treatment.

![img-3.jpeg](img-3.jpeg)

FIGURE 4 BNs show the highest risk of relapse for participants who have received 6- and 12-month consecutive MMT. (A) The BNs that lead to the highest risk of relapse in participants during the first 6 months of treatment. (B) The BNs that lead to the highest risk during the first 12 months of treatment.

0.644, 95%CI: 0.602–0.685) in this study. The parameter estimation result of the ROC curve is presented in Supplementary Table 7.

### The variable selection results of sensitivity analysis

For the model of those who received the 6-month MMT, the initial daily dose was considered significant in the main result while the average daily dose was not in the sensitivity analysis. Apart from these, the other selected variables were the same as that of the main text, with little difference in the coefficients of variables between the two analyses. For the 12-month treatment, the average daily dose was not considered significant, being the same as that of the initial dose in the main result. The cross-validation results are presented in Supplementary Figure 1, and the coefficients of variables are presented in Supplementary Table 4.

To sum up, most results of sensitivity analysis were similar to those of the main results, which confirmed the robustness of our findings. The average daily dose was considered insignificant in the group of the 12-month treatment. The initial daily dose was significant in the model of 6-month treatment duration. This supported our finding that the initial dose is important for participants at an early stage.

### Discussion

This study found that the relapse risk of newly enrolled MMT participants might increase with the treatment duration and risk factors differed from those who have received the 6- and 12-month consecutive treatments.

It is believed that the maximum effectiveness of MMT starts to show up at least after 12 months (2); however, participants tend to relapse at the early stage because of withdrawal symptoms, side effects, and a strong craving for drugs (43). Most relapses happened in the first 6 months (12) and this was confirmed by our study. Nonetheless, the relapse risk might rise when the participants were

TABLE 2 Conditional probability distribution of relapse with the job, initial daily dose, and time needed to the clinic.


*The probability was obtained based on the BN model of 6-month treatment duration.

TABLE 3 The conditional probability distribution of relapse with transportation and time needed to the clinic as parent nodes.


*The probability was obtained based on the BN model of 12-month treatment duration. treated for a longer time. According to our findings, participants who received the 12 -month treatment had a higher possibility of relapse (39\%), compared with those who received the 6 -month treatment (32\%), and this was consistent with other research (16).

Relapse is a multifactorial outcome (44), which has been proven to be correlated with factors, such as marital status, living status, relationship with family, and drug use behavior (12, 16, 45, 46). This study implied that these factors were influential for participants who completed the 6 -month consecutive MMT. Specifically, living alone or being estranged from family and friends might indicate that the participants received little social support, which made them more likely to drop out and relapse $(47,48)$. This could be more apparent among Chinese participants because of their family-oriented culture (49). They may be impacted by poor family relationships more greatly, causing mental health or economic issues. Both of these will increase the risk of relapse. Previous drug-use habits are associated with relapse as well (47). For instance, people who used drugs more frequently before MMT and exhibit high-risk behaviors such as syringe sharing might feel difficult to adapt to the substitution of methadone. Severe withdrawal symptoms could also lead them to return to heroin use (50). In addition, the daily methadone dose also counts for relapse, especially at the initial stage of MMT (12, 51). Komasi et al. (12) found that participants who relapsed during the first 6 -month treatment reported more dose non-satisfaction than those who did not. A low methadone dose is a leading risk factor for relapse and could hinder the effectiveness of MMT. In this study, participants who took $<30 \mathrm{mg}$ of methadone per day during the first 6 months had the lowest retention and the highest relapse risk. Therefore, we suggest conducting interventions about family engagement and in-time dose adjustment for those who are at the early stage of MMT.

However, the effects of these factors will be fading with the treatment duration in line with our findings. This could be explained by several reasons: first, pleasant family relationships and reduced communication with drug friends could engage better compliance of participants, reflected by longer treatment duration. Second, the craving for drugs would decrease with treatment. Therefore, previous drug-use behaviors might gradually become less of a determinant for those with longer treatment duration. Finally, those who were treated for 12 months might have been taking a more appropriate dose at the beginning of the treatment than those with short retention, which decreased the possibility of suffering the withdrawal symptoms and helped with a quick adaptation to methadone.

In contrast, age, the age at the initial drug use, the HIV infection status, sexual behavior, and continuous treatment days had long-lasting effects on relapse, regardless of the treatment duration. Among these factors, age and age at the initial drug use could reflect the severity of the drug addiction history. A long addiction history is usually related to a high risk of relapse, and this has been reported among participants at different stages of treatment $(49,52)$. Adjusting to MMT might be harder for those who were addicted to heroin at a younger age (53). In addition, having unprotected sex and multiple sexual partners increases the relapse risk as they are strongly associated with HIV infection, and HIV-positive participants are believed to have poorer compliance with MMT (54). Some antiretroviral medications can reduce the potency of methadone (55), which makes it harder for them to adapt to MMT. Therefore, high-risk sexual behaviors are related to a greater probability of relapse. In addition, short continuous treatment days indicate poor adherence because of which relapse is always a dominant cause $(18,56)$. Our findings are consistent with the aforementioned conclusions, and we, therefore, suggest implementing health education for preventing HIV/STI and antinarcotics in the whole process of treatment to promote adherence and reduce the relapse rate.

We also identified the groups with the highest relapse risk for participants of both durations. Among those who persisted with 6month MMT, if they were HIV-positive, addicted to drugs since their teenage, communicated with friends more than once a day, and had poor family supports, they would have the highest possibility of relapse ( $66.7 \%$ ). In contrast, the riskiest group among those who received the 12 -month MMT was HIV-negative participants who were younger than 30 years and started to use drugs after 20 years of age, with continuous treatment of 30-60 days. They were predicted to have a relapse risk as high as $83.3 \%$. Being inconsistent with other research, we did not find being HIV-positive was a risk for relapse in this group. It might be because the number of relapsed and non-relapsed HIV-positive participants was the same ( 23 vs. 23 , see Supplementary Table 2), and no statistical significance was detected between the groups. Apart from this, other findings that young participants who were addicted to drugs at an early age with poor compliance to MMT were at a risk of relapse, which was confirmed by previous research $(56,57)$.

![img-4.jpeg](img-4.jpeg)

FIGURE 5 Comparison of ROC curves between the group lasso logistic model and the BN model. (A) The ROC curve of two models based on the baseline data of newly enrolled participants receiving MMT for 6 months. (B) The ROC curve of two models based on the baseline data of newly enrolled participants receiving MMT for 12 months. The blue curve indicates the group lasso logistic model and the red curve indicates the BN model.

If participants who have received the 6-month MMT were under the same condition leading to the highest relapse risk for those who received the 12-month MMT, the relapse risk would be 46.3%, nearly half of that of the latter. This might be because the occurrence of relapse during the first 6-month treatment was associated with more factors, compared with those with longer treatment; thus, the effects of common factors might be weakened.

There are also some highlights in this study. For example, we found that those who drove or needed <10 min to reach the clinic were more likely to relapse than other participants. Theoretically, the long distance and traveling difficulties to the clinic would reduce adherence to MMT (58, 59). However, the high accessibility such as living too close to the clinic means having the flexibility in choosing the time to get there, which might decrease adherence as well. In addition, being capable of driving indicates that participants might have a relatively high income or well-being life. They have a greater possibility to buy drugs such as heroin, compared to those who were less paid or unemployed.

Another unexpected finding is that it was farmers, rather than the unemployed, who were most vulnerable to relapse. A rational interpretation could be that, unlike those who live in towns, people who live in rural areas might have poorer accessibility to MMT services. Research conducted in Thailand showed that rural residents faced barriers to utilizing MMT services, including missing the opening hours of clinics and the unaffordable cost of travel (60). Harm Reduction International (1) also highlighted that rural communities were underserved by harm reduction services and this geographical gap has hindered the implementation of MMT among rural residents, including farmers. Hence, more adaptive operations are required to improve the accessibility of MMT for this group.

Based on the findings mentioned earlier, we, herein, provided several recommendations for future policy-making:

1. The influence of treatment durations should be considered when implementing or evaluating the effectiveness of relevant interventions or strategies.
2. The future guideline for methadone dosage adjustment should specifically consider the participants at the early stage of MMT.
3. The continuity of health education on HIV/STI and anti-narcotics should be emphasized when implementing related interventions.

In addition, we also listed several clinical implications based on the findings, which hopefully could be referenced for healthcare providers:

1. Family engagement and in-time dosage adjustment should be emphasized for those who received short-term MMT.
2. Health education on HIV/STI and anti-narcotics should be insisted on in the whole process of MMT.
3. High-risk groups, such as farmers and those who can easily assess MMT require more attention to prevent relapse.

To our knowledge, this study is the first one that revealed the difference in risk factors of relapse between participants who have received the short-term (6-month) and long-term (12-month) MMT. This enriched the previous findings, which only treated all the participants as a whole, regardless of the treatment duration. In addition, this study first applied the group lasso-based Bayesian network to assess the relapse risk of MMT participants. These methods have been popular in health research and excel in dealing with the dependence on variables, which is the issue to be solved in this study. Performing these methods filled the gap in methodology in the field of MMT.

Several limitations exist in this study. First, this was a retrospective study that used secondary data. This type of study design will have issues, such as the absence of confounders, selection bias, and less timeliness (61–63). Particularly, we did not include factors such as mental health status (64) or brain function (65), which were also considered to be influential to relapse. The

latest data can only be dated back to 2017. These may impact the replicability and robustness of our findings. However, the questionnaire from which we obtained the data was designed by the national MMT working group and filled by the professional clinic staff for quality control. It also covered the majority of aspects of the participants' information and most MMT-related research in China was conducted using data from this questionnaire. Therefore, its rigor and authority can be ensured. Second, the sample is not that representative as all the participants were from seven MMT clinics in Guangdong Province. It needs to be cautious when generalizing our findings to other contexts. The sample size is not large enough either and this made the BN model of 12 months less discriminative, evidenced by the lower AUC. All these issues could be improved once we obtained more data from more settings.

## Conclusion

In summary, participants receiving MMT for a long duration may be generally at a higher risk of relapse than those of short duration. Factors including personal living status, previous druguse behaviors, and daily methadone dose would become less significant as the treatment continued. However, the duration of drug-use history, sexual behaviors, HIV infection status, and adherence to MMT would remain influential in the long term. Therefore, we recommend implementing interventions about family engagement and in-time dose adjustment for those who attended MMT for a short term and conducting health education for preventing HIV/STI and anti-narcotics in the whole process. More focus should be paid to farmers and those who have high accessibility to MMT services. In this manner, participants could receive more targeted treatment, contributing to reducing the relapse rate and improving compliance with MMT.

## Data availability statement

The data analyzed in this study is subject to the following licenses/restrictions: The data supporting the findings of this study are not publicly available to protect the confidentiality and privacy of participants. Requests to access these datasets should be directed to lingli@mail.sysu.edu.cn.

## Ethics statement

The study was reviewed and approved by the Institutional Review Board of the School of Public Health, Sun Yat-sen University, Guangzhou, China (No. 2020-39).

## Author contributions

XT and LL conceptualized and designed the study. XT, CF, and CX completed the data cleaning and formal analysis. XT wrote the original draft. XT, CF, WW, CW, and ZC contributed to reviewing and editing the manuscript. LL provided the funding for this study. All the authors have read and approved the final manuscript.

## Funding

This work was supported by the National Natural Science Foundation of China (Grant Number: 82073664).

## Conflict of interest

The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.

## Publisher's note

All claims expressed in this article are solely those of the authors and do not necessarily represent those of their affiliated organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article, or claim that may be made by its manufacturer, is not guaranteed or endorsed by the publisher.

## Supplementary material

The Supplementary Material for this article can be found online at: https://www.frontiersin.org/articles/10.3389/fpubh.2022. 1032217/full\#supplementary-material

[^0]
[^0]:    4. Chen T, Zhao M. Meeting the challenges of opioid dependence in China: experience of opioid agonist treatment. Curr Opin Psychiatry. (2019) 32:2827. doi: 10.1097/TCO.0000000000000509
    5. Liu X. Development of a Relapse Risk Assessment tool for Methadone Maintenance Treatment Patients (in Chinese). Chinese Center for Disease Control and Prevention (2021).
    6. Liu C, Wu Z, Detels R. Opiate users' perceived barriers against attending methadone maintenance therapy: a qualitative study in China. Subst Use Misuse. (2011) 46:11908. doi: 10.3109/10826084.2011.561905
    7. Soyka M, Zingg C, Koller G, Kuefner H. Retention rate and substance use in methadone and buprenorphine maintenance therapy and predictors of outcome:

results from a randomized study. Int J Neuropsychopharmacol. (2008) 11:64153. doi: $10.1017 /$ S146114570700836X
8. Kerr T, Marsh D, Li K, Montaner J, Wood E. Factors associated with methadone maintenance therapy use among a cohort of polysubstance using injection drug users in Vancouver. Drug Alcohol Depend. (2005) 80:329-35. doi: 10.1016/j.drugalcdep.2005.05.002
9. Sadeghi Bimorgh M, Omidi A, Ghoreishi FS, Rezaei Ardani A, Ghaderi A, Banafshe HR. The effect of transcranial direct current stimulation on relapse, anxiety, and depression in patients with opioid dependence under methadone maintenance treatment: a pilot study. Front Pharmacol. (2020) 11:401. doi: 10.3389/fphar.2020.00401
10. Saitz R. Treatment of alcohol and other drug dependence. Liver Transpl. (2007) 13:S59-S64. doi: 10.1002/lt.21339
11. Stone AC, Carroll JJ, Rich JD, Green TC. Methadone maintenance treatment among patients exposed to illicit fentanyl in Rhode Island: safety, dose, retention, and relapse at 6 months. Drug Alcohol Depend. (2018) 192:94-7. doi: 10.1016/j.drugalcdep.2018.07.019
12. Komasi S, Sseidi M, Amiri MM, Nazeie N, Shams Alizadeh N, Soroush A. Triggers of substance abuse slip and relapse during outpatient treatment in methadone/buprenorphine maintenance therapy clinics: a predictive model with emphasis on treatment-related factors. Jundishapur J Health Sci JJHS. (2017) 9:57688. doi: 10.5812/jjhs. 57688
13. Ducray K, Darker C, Smyth BP. Situational and psycho-social factors associated with relapse following residential detoxification in a population of Irish opioid dependent patients. Ir J Psychol Med. (2012) 29:72-9. doi: 10.1017/S07909667000 1733X
14. Preston KL, Umbricht A, Epstein DH. Abstinence reinforcement maintenance contingency and one-year follow-up. Drug Alcohol Depend. (2002) 67:125-37. doi: 10.1016/S0376-8716(02)00023-6
15. Nguyen LH, Nguyen HTT, Nguyen HLT, Tran BX, Latkin CA. Adherence to methadone maintenance treatment and associated factors among patients in Vietnamese mountainous area. Subst Abuse Treat Prev Policy. (2017) 12:31. doi: 10.1186/s13011-017-0115-4
16. Naji L, Dennis BB, Bawor M, Plater C, Pare G, Worster A, et al. A Prospective study to investigate predictors of relapse among patients with opioid use disorder treated with methadone. Subst Abuse Res Treat. (2016) 10:SART.S37030. doi: 10.4137/SART.S37030
17. Sun Y, Bao Y, Kosten T, Strang J, Shi J, Lu L. Editorial: challenges to opioid use disorders during COVID-19. Am J Addict. (2020) 29:174-5. doi: 10.1111/ajad.13031
18. Zhang L, Zou X, Zhang D, Li X, Zhao P, Ling L. Investigation of repeat client dropout and re-enrolment cycles in fourteen methadone maintenance treatment clinics in Guangdong, China. PLoS ONE. (2015) 10:e0139942. doi: 10.1371/journal.pone. 0139942
19. Lin C-K, Hung C-C, Peng C-Y, Chao E, Lee TS-H. Factors associated with methadone treatment duration: a cox regression analysis. PLoS ONE. (2015) 10:e0123687. doi: 10.1371/journal.pone. 0123687
20. Arlotta CJ. Some Opioid Users On Methadone Have High Risk Of Relapse. Forbes. Available online at: https://www.forbes.com/sites/zarletta/2016/04/14/methadone-treatment-for-opioid-users-identifying-high-risk-of-relapse/ (accessed September 8, 2021).
21. Richmond-Rakerd LS, Slutske WS, Lynskey MT, Agrawal A, Madden PAF, Bucholz KK, et al. Age at first use and later substance use disorder: shared genetic and environmental pathways for nicotine, alcohol, and cannabis. J Abnorm Psychol. (2016) 125:946-59. doi: 10.1037/abn0000191
22. Faggiano F, Vigna-Taglianti F, Versino E, Lemma P. Methadone maintenance at different dosages for opioid dependence. Cochrane Database Syst Rev. (2003) 2003:CD002208. doi: 10.1002/14651858.CD002208
23. Zhang S, Qiao S, Li H, Zhang R, Wang M, Han T, et al. Risk factors and nomogram for predicting relapse risk in pediatric neuromyelitis optica spectrum disorders. Front Immunol. (2022) 13:765839. doi: 10.3389/fimmu.2022.7 65839
24. Guglielmi C, Martelli M, Federico M, Zinzani PL, Vitolo U, Bellesi G, et al. Riskassessment in diffuse large cell lymphoma at first relapse. A study by the Italian Intergroup for Lymphomas. Haematologica. (2001) 86:941-50.
25. You J, Ahn SS, Jung SM, Song JJ, Park Y-B, Lee S-W. Delta neutrophil index is associated with vasculitis activity and risk of relapse in ANCA-associated vasculitis. Yonsei Med J. (2018) 59:397-405. doi: 10.3349/ymj.2018.59.3.397
26. Sun J, Sun R, Jiang Y, Chen X, Li Z, Ma Z, et al. The relationship between psychological health and social support: evidence from physicians in China. PLoS ONE. (2020) 15:e0228152. doi: 10.1371/journal.pone. 0228152
27. Paccapelo A, Lolli I, Fabrini MG, Silvano G, Detti B, Perrone F, et al. A retrospective pooled analysis of response patterns and risk factors in recurrent malignant glioma patients receiving a nitrosourea-based chemotherapy. J Transl Med. (2012) 10:90. doi: 10.1186/1479-5876-10-90
28. Li Y, Chen X, Wang Y, Hu J, Shen Z, Ding X. Application of group LASSO regression based Bayesian networks in risk factors exploration and disease prediction for acute kidney injury in hospitalized patients with hematologic malignancies. BMC Nephrol. (2020) 21:162. doi: 10.1186/s12882-020-01786-w
29. Zhang X. The Application of Bayesian Network Based on Tabu Search Algorithm in Diseases Prediction and Diagnosis (in Chinese). Shanxi: Shanxi Medical University (2015).
30. Shangguan C, Yu L, Liu G, Song Y, Chen J. Risk assessment of chronic obstructive pulmonary disease using a Bayesian network based on a provincial survey. Pol Arch Intern Med. (2021) 131:345-55. doi: 10.20452/pamw. 15867
31. China.com.cn. Supreme People's Prevuratenate of P.R.C: All Provinces Have Drug Crimes and Guangdong, Hunan and Sichuan Accounted for 40\%. (2018). Available online at: https://www.sohu.com/a/www.sohu.com/a/237841246_116897 (accessed November 10, 2021).
32. Guangdong Provincial Bureau of Drug Rehabilitation. Analysis on the Number of Minors Taking Drugs and Detoxification in Guangdong. Anal Number Minors Tak Drugs Detoxif Guangdong (in Chinese) (2019). Available online at: http://gdidj.gd.gov.cn/gdjdj/ swgb/ajlb/content/post_2677836.html (accessed November 10, 2021).
33. Xia Y-H, McLaughlin MM, Chen W, Ling L, Tucker JD. HIV and Hepatitis C virus testing delays at methadone clinics in Guangdong Province, China. PLoS ONE. (2013) 8:e66787. doi: 10.1371/journal.pone. 0066787
34. Chen Y-F. Chinese classification of mental disorders (CCMD-3): towards integration in international classification. Psychopathology. (2002) 35:171-5. doi: 10.1159/000065140
35. Zhou X, Zhuang G. Retention in methadone maintenance treatment in mainland China, 2004-2012: a literature review. Addict Behav. (2014) 39:229. doi: 10.1016/j.addbeh.2013.09.001
36. Sharma V, Chamroonowasdi K, Srisorrachatr S. Rate of adherence to and factors associated with methadone maintenance treatment program (MMTP) compliance among injecting drug use patients in Nepal. Southeast Asian J Trop Med Public Health. (2016) 47:287-98.
37. Moradinazar M, Farnia V, Alikhani M, Asadi A, Marzbani B, Najafi F. The effects of anxiety on relapse of patients with opioid use disorders under methadone maintenance treatment: control of the confounding variables. J Subst Dis. (2020) 25:349. doi: 10.1080/14659891.2019.1659868
38. National Health and Family Planning Commission. Notice of the General Office of the National Health and Family Planning Commission on the Issuance of 3 Documents Including the Basic Requirements for Maintenance Treatment Institutions of Drug Detoxification Drugs (in Chinese). (2015). Available online at: http://www.nhc.gov. cn/cms-search/xtgk/getManuscriptXzgk.htm?id=dx4df09437444819b104904a5dc24ee (accessed December 12, 2021).
39. Lu Q, Zou X, Liu Y, Gong C, Ling L. Dose tapering strategy for heroin abstinence among methadone maintenance treatment participants: evidence from A retrospective study in Guangdong, China. Int J Environ Res Public Health. (2019) 16:E2800. doi: 10.3390/ijerph16152800
40. Efron B, Hastie T, Johnstone J, Tibshirani R. Least angle regression. Ann Stat. (2004) 32:407-99. doi: 10.1214/009053604000000067
41. Yuan M, Lin Y. Model selection and estimation in regression with grouped variables. J R Stat Soc Ser B Stat Methodol. (2006) 68:49-67. doi: 10.1111/j.1467-9868.2005.00532.x
42. Jakobsen JC, Gland C, Watterslov J, Winkel P. When and how should multiple imputation be used for handling missing data in randomised clinical trials - a practical guide with flowcharts. BMC Med Res Methodol. (2017) 17:162. doi: 10.1186/s12874-017-0442-1
43. NHS.UK. Methadone-Medicine Used to Treat Heroin Dependence. (2021). Available online at: https://www.nhs.uk/medicines/methadone/ (accessed December 12, 2021).
44. Kabisa E, Biracyaza E, Habagusenga J d'Amour, Umubyeyi A. Determinants and prevalence of relapse among patients with substance use disorders: case of Icyizere- Psychotherapeutic Centre. Subst Abuse Treat Prev Policy. (2021) 16:13. doi: 10.1186/s13011-021-00347-0
45. Hassan NM, Daud N, Aziz AA, Mat KC. Associated factors for relapse in opioid addicts undergoing therapy. Res J Pharm Technol. (2018) 11:27248. doi: 10.5958/0974-360X.2018.00503.6
46. Zhang L, Bao J, Harrington A, Fan X, Ning Z, Zhang J, et al. Mixed methods to explore factors associated with the decline of patients in the methadone maintenance treatment program in Shanghai, China. Harm Reduct J. (2019) 16:34. doi: 10.1186/s12954-019-0304-8
47. Hafez asghar A, Kazemeini T, Shayan S. The relationship of social support and religious orientation with relapse rates in opioid dependent patients under methadone maintenance therapy. Adv Nurs Midwifery. (2015) 24:35-44.
48. Garmendia ML, Alvarado ME, Montenegro M, Pino P. Social support as a protective factor of recurrence after drug addiction treatment. Rev Med Chil. (2008) 136:16978. doi: 10.4067/30034-90072008000200005
49. Cao X, Wu Z, Ren K, Li L, Lin C, Wang C, et al. Retention and its predictors among methadone maintenance treatment clients in China: a six-year cohort study. Drug Alcohol Depend. (2014) 145:87-93. doi: 10.1016/j.drugalcdep.2014.09.776
50. Ingrid Davstad MA, Marlene Stenbacka P, Anders Leifman MSE, Olof Beck P, Seher Korkmaz MD, Anders Romelajo MD. Patterns of illicit drug use and retention in a methadone program: a longitudinal study. J Opioid Manag. (2007) 3:2734. doi: 10.5055/joe.2007.0038
51. Darker CD, Ho J, Kelly G, Whiston L, Barry J. Demographic and clinical factors predicting retention in methadone maintenance: results from an Irish cohort. Ir J Med Sci. (2016) 185:433-41. doi: 10.1007/s11843-015-1314-5
52. Hetzahi K, Ti L, Arutthaya PPN, Suwannawong P, Kaplan K, Small W, et al. Barriers to retention in methadone maintenance therapy among people who

inject drugs in Bangkok, Thailand: a mixed-methods study. Harm Reduct J. (2017) 14:63. doi: 10.1186/s12954-017-0189-3
53. Does Age Matter in Methadone Treatment? MedMark Treat Cent. (2019). Available online at: https://medmark.com/does-age-matter-in-methadone-treatment/ (accessed December 14, 2021).
54. Karki P, Shrestha R, Huedo-Medina TB, Copenhaver M. The impact of methadone maintenance treatment on HIV risk behaviors among high-risk injection drug users: a systematic review. Evid-Based Med Public Health. (2016) 2:e1229.
55. Vlahov D, O'Driscoll P, Mehta SH, Ompad DC, Gern R, Galai N, et al. Risk factors for methadone outside treatment programs: implications for HIV treatment among injection drug users. Addiction. (2007) 102:771-7. doi: 10.1111/j.1360-0443.2007.01767.x
56. Durand L, Boland F, O'Driscoll D, Bennett K, Barry J, Keenan E, et al. Factors associated with early and later dropout from methadone maintenance treatment in specialist addiction clinics: a six-year cohort study using proportional hazards frailty models for recurrent treatment episodes. Drug Alcohol Depend. (2021) 219:108466. doi: 10.1016/j.drugalcdep.2020.108466
57. Mu L-L, Wang Y, Wang L-J, Xia L-L, Zhao W, Song P-P, et al. Associations of executive function and age of first use of methamphetamine with methamphetamine relapse. Front Psychiatry. (2022) 13:971825. doi: 10.3389/fpsyt.2022.971825
58. Eibl JK, Gomes T, Martins D, Camacho X, Juurlink DN, Mamdani MM, et al. Evaluating the effectiveness of first-time methadone maintenance therapy across northern, rural, and urban regions of Ontario, Canada. J Addict Med. (2015) 9:4406. doi: 10.1097/ADM. 0000000000000156
59. Le TA, Le MQT, Dang AD, Dang AK, Nguyen CT, Pham HQ, et al. Multilevel predictors of psychological problems among methadone maintenance treatment patients in difference types of settings in Vietnam. Subst Abuse Treat Prev Policy. (2019) 14:39. doi: 10.1186/s13011-019-0223-4
60. Khampang R, Assanangkornchai S, Teerawattananon Y. Perceived barriers to utilise methadone maintenance therapy among male injection drug users in rural areas of southern Thailand. Drug Alcohol Rev. (2015) 34:645-53. doi: 10.1111/dar. 12268
61. Baldwin JR, Pingault J-B, Schoeler T, Sallis HM, Munalii MR. Protecting against researcher bias in secondary data analysis: challenges and potential solutions. Eur J Epidemiol. (2022) 37:1-10. doi: 10.1007/s10654-021-00839-0
62. Silvia V. Secondary Data: Advantages, Disadvantages, Sources, Types. (2020). Available online at: https://www.intellspot.com/secondary-data/ (accessed December 7, 2022).
63. Sedgwick P. Retrospective cohort studies: advantages and disadvantages. BMJ. (2014) 348:g1072. doi: 10.1136/bmj.g1072
64. Clark RE, Baxter JD, Aweh G, O'Connell E, Fisher WH, Barton BA. Risk factors for relapse and higher costs among Medicaid members with opioid dependence or abuse: opioid agonists, comorbidities, and treatment history. J Subst Abuse Treat. (2015) 57:75-80. doi: 10.1016/j.jsat.2015.05.001
65. Chang H, Li W, Li Q, Chen J, Zhu J, Ye J, et al. Regional homogeneity changes between heroin relapse and non-relapse patients under methadone maintenance treatment: a resting-state fMRI study. BMC Neurol. (2016) 16:145. doi: 10.1186/s12883-016-0659-2