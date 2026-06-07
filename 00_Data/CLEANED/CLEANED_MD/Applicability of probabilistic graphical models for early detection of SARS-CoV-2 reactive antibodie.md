# Applicability of probabilistic graphical models for early detection of SARS-CoV-2 reactive antibodies after SARS-CoV-2 vaccination in hematological patients 

José Luis Piñana ${ }^{1,2}$ (D) $\cdot$ Pablo Rodríguez-Belenguer ${ }^{3} \cdot$ Dolores Caballero ${ }^{4} \cdot$ Rodrigo Martino ${ }^{5} \cdot$<br>Lucia Lopez-Corral ${ }^{4} \cdot$ María-José Terol ${ }^{1,2} \cdot$ Lourdes Vazquez ${ }^{4} \cdot$ Marisa Calabuig ${ }^{1,2} \cdot$ Gabriela Sanz-Linares ${ }^{6} \cdot$<br>Francisca Marin-Jimenez ${ }^{7} \cdot$ Carmen Alonso ${ }^{8} \cdot$ Juan Montoro ${ }^{9} \cdot$ Elena Ferrer ${ }^{1,2} \cdot$ Ana Facal ${ }^{9} \cdot$ María-Jesús Pascual ${ }^{10} \cdot$<br>Alicia Rodriguez-Fernandez ${ }^{11} \cdot$ María T. Olave ${ }^{12} \cdot$ Almudena Cascales-Hernandez ${ }^{13} \cdot$ Beatriz Gago ${ }^{10}$.<br>José-Ángel Hernández-Rivas ${ }^{14} \cdot$ Lucia Villalon ${ }^{15} \cdot$ Magdalena Corona ${ }^{16} \cdot$ Alicia Roldán-Pérez ${ }^{17} \cdot$ Julia Ribes-Amoros ${ }^{6}$.<br>Clara González-Santillana ${ }^{18} \cdot$ Ramon Garcia-Sanz ${ }^{4} \cdot$ David Navarro ${ }^{19,20} \cdot$ Antonio J. Serrano-López ${ }^{21}$.<br>Ángel Cedillo ${ }^{22} \cdot$ Emilio Soria-Olivas ${ }^{21} \cdot$ Anna Sureda ${ }^{6} \cdot$ Carlos Solano ${ }^{1,2,19} \cdot$ On behalf of Infectious Complications Subcommittee of the Spanish Hematopoietic Stem Cell Transplantation and Cell Therapy Group (GETH-TC)

Received: 19 February 2022 / Accepted: 25 June 2022 / Published online: 2 July 2022
(c) The Author(s), under exclusive licence to Springer-Verlag GmbH Germany, part of Springer Nature 2022


#### Abstract

Prior studies of antibody response after full SARS-CoV-2 vaccination in hematological patients have confirmed lower antibody levels compared to the general population. Serological response in hematological patients varies widely according to the disease type and its status, and the treatment given and its timing with respect to vaccination. Through probabilistic machine learning graphical models, we estimated the conditional probabilities of having detectable anti-SARS-CoV-2 antibodies at 3-6 weeks after SARS-CoV-2 vaccination in a large cohort of patients with several hematological diseases ( $n=1166$ ). Most patients received mRNA-based vaccines ( $97 \%$ ), mainly Moderna ${ }^{\circledR}$ mRNA-1273 (74\%) followed by Pfizer-BioNTech® BNT162b2 (23\%). The overall antibody detection rate at 3 to 6 weeks after full vaccination for the entire cohort was $79 \%$. Variables such as type of disease, timing of anti-CD20 monoclonal antibody therapy, age, corticosteroids therapy, vaccine type, disease status, or prior infection with SARS-CoV-2 are among the most relevant conditions influencing SARS-CoV-2-IgG-reactive antibody detection. A lower probability of having detectable antibodies was observed in patients with B-cell non-Hodgkin's lymphoma treated with anti-CD20 monoclonal antibodies within 6 months before vaccination (29.32\%), whereas the highest probability was observed in younger patients with chronic myeloproliferative neoplasms ( $99.53 \%$ ). The Moderna ${ }^{\circledR}$ mRNA-1273 compound provided higher probabilities of antibody detection in all scenarios. This study depicts conditional probabilities of having detectable antibodies in the whole cohort and in specific scenarios such as B cell NHL, CLL, MM, and cMPN that may impact humoral responses. These results could be useful to focus on additional preventive and/or monitoring interventions in these highly immunosuppressed hematological patients.


Keywords Probabilistic graphical models $\cdot$ Bayesian Networks $\cdot$ mRNA vaccine $\cdot$ SARS-CoV-2 vaccines $\cdot$ Hematological malignancies $\cdot$ Non-Hodgkin lymphoma $\cdot$ Chronic lymphocytic leukemia $\cdot$ CAR-T therapy $\cdot$ Allogeneic stem cell transplantation $\cdot$ Autologous stem cell transplantation $\cdot$ COVID-19 $\cdot$ Respiratory virus $\cdot$ Immunocompromised patients $\cdot$ Moderna mRNA-1273 $\cdot$ Pfizer-BioNTech BNT162b2

[^0]
## Introduction

Hematological patients have proven to be the most vulnerable population to coronavirus infectious disease 2019 (COVID-19) pandemic caused by the new zoonotic coronavirus (SARS-CoV-2) in terms of delayed treatments, deferral of cell therapy procedures and more importantly


[^0]:    $\boxtimes$ José Luis Piñana
    jlpinana@gmail.com
    Extended author information available on the last page of the article

suffering a relevant mortality that exceeds 25% [1--6]. Although hematological patients have been inexplicably excluded from randomized SARS-CoV-2 vaccine trials, national and scientific societies have actively recommended on SARS-CoV-2 vaccination in order to lessen the severity of COVID-19 in these immunocompromised patients [7--11]. Initial reports on antibody response after full SARS-CoV-2 vaccination in hematological patients have confirmed the lower antibody response rates compared to the general population [12--18]. Serological response in hematological patients varies significantly according to several factors such as the type of hematological disease, disease status at the time of vaccination, the timing and type of past or current treatments/procedures with regard to the time of vaccination, the type of SARS-CoV-2 vaccine and according to the prior development of COVID-19 [12--18]. Some hematological patients' subsets can achieve seroconversion rates comparable to general population (i.e. those who had prior COVID-19) [19, 20], whereas others showed a reduced serological response [12--18]. Given this high variability, it is of great interest to understand conditions predisposing to a lower antibody response rate in hematological patients. It is also of utmost importance to know the pre-vaccine likelihood of serological responses according to specific conditions in general hematological population and in each of the diseases/treatments/procedures for patients counseling and to prioritize those with lower probability of response for additional vaccine doses, for serological monitoring after vaccination, for pre-exposure neutralizing SARS-CoV-2 monoclonal antibodies therapy, or for considering early therapy with efficient antivi-ral drugs. To this aim, we use supervised machine learning (ML) methodologies, such as probabilistic graphical models which have shown excellent performance given their simplicity and explainability [21].

The current study analyzes the conditions that influence the detection of SARS-CoV-2-reactive IgG antibodies at 3 to 6 weeks after a full course of SARS-CoV-2 vaccination and explored conditional probabilities of humoral response in a Spanish cohort of 1166 patients with hematological disorders. This prospective study was conducted by the Spanish Hematopoietic Stem Cell Transplantation and Cell Therapy Group (GETH-TC).

## Patients and methods

### Study population

This is a prospective observational multicenter registry study that includes more than 1600 patients with several hematological disorders conducted by the GETH-TC in collaboration with the Spanish Society of Hematology and Hemotherapy (SEHH). The cohort included patients who received cell therapy procedures (allogeneic or autologous HSCT and/or CAR-T cell therapy) and patients with hematological diseases who did not receive cell-based procedures. The local ethical committee of the Hospital Clínico Universitario of Valencia approved the registry and study protocol (reference code 35.21).

### Inclusion criteria and cohort selection

Details of this multicenter registry have been already reported elsewhere [20]. Briefly, this registry included consecutive adult patients with a prior history of hematological disorders who were vaccinated against SARS-CoV-2 from December 30, 2020, to June 30, 2021, in 21 participating Spanish centers. All patients included in this registry gave their sign informed consent according to the Declaration of Helsinki.

The status of all included patients was updated on July 30, 2021. At this time, the predominant SARS-CoV-2 variant of concern in Spain was gamma (P.1). Variables included in the REDCap on-line platform in the GETH database were patient and disease characteristics, date of vaccination, type of vaccination, self-reported adverse events (AEs) after vaccination, prior history of SARS-CoV-2 infection, serological status before vaccination, serological response at 3 to 6 weeks, and data regarding characteristics of breakthrough COVID-19 when applicable. Details on the past or current treatment(s) of the underlying malignancy, immunosuppression status, and status disease at the time of vaccination were also captured. As well, baseline laboratory variables before SARS-CoV-2 vaccination (absolute lymphocyte and neutrophil counts) were also collected.

As of July 30, 2021, 1683 patients with different hematological disorders who had been fully vaccinated against COVID-19 were registered in the GETH-TC database. With the aim of assessing the probabilities of having SARS-CoV-2 antibodies after full vaccination in the whole series and in specific scenarios, we excluded those who did not have serological assessment at 3 to 6 weeks after complete vaccination (n= 354) and those without data on their underlying disease and treatments received (n= 161). Thus, only patients with complete available disease characteristics data and serological testing at 3 to 6 weeks after full vaccination were included (n= 1166). To exclude reporting bias, we explored the 6-week survival and the rates of breakthrough COVID-19 during the study period in the 1166 included patients and the 515 excluded patients and found no differences (data not shown). To differentiate the serological effect of the baseline diseases and their treatments from that of the cell therapy procedures, analyses in the whole cohort were segregated by patients' disease and cell therapy status. Analysis of specific factors associated with the detection of SARS-CoV-2 reactive antibodies after full vaccination

in recipients of allogeneic stem cell transplantation (allo-HSCT) and autologous stem cell transplantation (ASCT) and in those with prior COVID-19 have been previously published [19, 20].

## Definitions and technical considerations

Having received full vaccination was defined as receiving two doses of vaccines with an interval of 2 to 14 weeks between doses. Antibody detection or seropositivity was defined as the detection of SARS-CoV-2-reactive IgG antibodies at any level above the lower limit level of detection for each of the serological tests used. We assessed seropositivity using serological ELISA or chemiluminescence immunoassay assays (see supplementary Table S1) as previously described [20]. Overall results were reported as positive or negative detection.

Pre-vaccination SARS-CoV-2 infection was defined as patients with prior history of PCR-proven COVID-19 and/ or positive SARS-CoV-2 serostatus (IgG and/or IgM) before the first vaccine dose.

## Endpoints

The primary objective of the study was to estimate the likelihood of having detectable SARS-CoV-2 antibodies in the whole series according to different conditions. We also estimated the probabilities of SARS-CoV-2-reactive IgG antibodies detection in well represented (> 100 patients) subgroup of patients.

The main characteristics of patients were reported by descriptive statistics. The median and range were used for continuous variables, whilst absolute and percentage frequency were used for categorical variables. Comparison between percentages was performed through X^{2}-test when appropriate.

## Machine learning analysis

A detailed description of ML analyses is available in the online Supplementary file. In brief, we used Bayesian Networks (BN) (also known as a probabilistic graphical models or belief networks) to represent a mixture of probability and graph theory in which the dependencies between variables are expressed graphically. Each node corresponds to a random variable and a directed acyclic graph (DAG) representing the conditional dependencies of the variables. The graph is a DAG. Nodes that are not connected represent variables that are conditionally independent. Each node is associated with a probability function that takes (as input) a particular set of values for the node's parent variables and gives (as output) the probability, or probability distribution, if any, of the variable represented by the node. The probability distribution depends on the graphical structure of the network. There are several possibilities to obtain these basic structures [22]. In the current study, we used the Tree augmented Naïve Bayes (TAN), an extension of a Naïve Bayes classifier, in which each variable is allowed to have dependence on another variable in addition to the target variable or class. The tree structure is learned from the data and provides probabilistic information about the relationships between the predictor variables (e.g. anti-CD 20 monoclonal antibody therapy and B cell non-Hodgkin's lymphoma) and the target class (antibody response after complete SARS-CoV-2). A 5-repeated 2-fold cross-validation was used in order to get the best hyperparameters of the TAN model [22]. We will also use the receiver operating curve (ROC) to show the relationship between the sensitivity (true positive rate) and specificity (false positive rate) obtained by the model and evaluate its predictive power with the area under the operating curve (AUC).

All the descriptive analyses were performed using the software SPSS v. 25, whereas we used the R and Python programming languages for developing the scripts to create and analyze the models. In Python, we extensively used the standard libraries Sklearn [23], Pandas [24], and Numpy [25]. For R, we mainly used the following libraries: ggplot2 [26] and bnlearn [27].

## Results

## Patient characteristics, antibody detection, and adverse events after SARS-CoV-2 vaccines

This study includes 1166 hematological patients meeting the inclusion criteria. Detailed clinical and laboratory characteristics are summarized in Table 1. The median age was 63 years (range 18--97). Overall, the most common hematological diseases were B cell non-Hodgkin's lymphoma (B cell NHL) (n= 187, 16%), plasma cell disorders (PCD) (n= 131, 11.2%), chronic lymphocytic leukemia (CLL) (n= 125, 10.7%), and chronic myeloproliferative neoplasias (cMPN) (n= 111, 9.5%). Among the cell therapy procedures, the most common was allo-HSCT (n= 318, 27.3%) followed by ASCT (n= 87, 7.5%) and CAR-T therapy (n= 21, 1.8%). Of note, this series included 99 patients (8.4%) with prior PCR and/or serological proof of SARS-CoV-2 infection before being vaccinated.

Most patients received mRNA vaccines (97%), mainly Moderna® mRNA-1273 (74%) followed by Pfizer-BioNTech® BNT162b2 (23%). Distribution of SARS-CoV-2 vaccine types according to the disease or procedure is detailed in Table 2.

Overall, SARS-CoV-2-reactive IgG antibody tests were positive in 925 of the 1166 patients (79%) at a median

Table 1 Patients' characteristics


Table 1 (continued)


$P C R$, polimerase chain reaction; $A M L$, acute myeloid leukemia; $A L L$, acute lymphoblastic leukemia; $M D S$, myelodysplastic syndrome; $B$ cell $N H L, \mathrm{~B}$ cell non-Hodgkin lymphoma; $T$ cell $N H L, \mathrm{~T}$ cell non-hodgkin lymphoma; $C L L$, chronic lymphocytic leukemia; $H D$, Hodgkin disease; $c M P N$, chronic myeloproliferative neoplasm; Allo-HSCT, allogeneic stem cell transplantation; $A S C T$, autologous stem cell transplantation; $C A R-T, \mathrm{~T}$ cell chimeric antigen receptor; $m o A b$, monoclonal antibody; BTK inhibitor, Bruton's tyrosine kinase inhibitor; TKIs, tyrosine kinase inhibitors; SCoV2-R-A, SARS-CoV-2-reactive IgG antibodies
*Differences in SARS-CoV-2 seropositivity after complete vaccination with these compounds are statistically significant $(p<0.0001)$
${ }^{\text {a }}$ Non-malignant diseases not allografted $(n=17)$ include aplastic anemia $(n=5)$, paroxysmal nocturnal hemoglobinuria $(n=3)$, autoimmune hemolytic anemia $(n=3)$, combined immunodeficiency disorder $(n=$ 2), immune thrombocytopenia $(n=1)$ and cyclic neutropenia $(n=3)$. Among allo-HSCT recipients with non-malignant diseases, there were 8 with aplastic anemia and 2 with major talassemia

Table 2 Distribution of SARS-CoV-2 vaccines according to the disease or procedures-


AML, acute myeloid leukemia; $A L L$, acute lymphoblastic leukemia; $M D S$, myelodysplastic syndrome; $B$ cell NHL, B cell non-Hodgkin lymphoma; $T$ cell NHL, T cell non-Hodgkin lymphoma; $C L L$, chronic lymphocytic leukemia; $H D$, Hodgkin disease; $c M P N$, chronic myeloproliferative neoplasm; Allo-HSCT, allogeneic stem cell transplantation; $A S C T$, autologous stem cell transplantation; $C A R-T, \mathrm{~T}$ cell chimeric antigen receptor; $P C D$, plasma cell disorders
of 21 days (range, 14-61 days) after the full vaccination schedule. Median follow-up after vaccination was 28 days (range 17-139 days) with 6 patients ( $0.5 \%$ ) developing breakthrough COVID-19 diagnosed by PCR; three of these patients had a negative SARS-CoV-2 serostatus after full vaccination.

Overall, vaccination was well-tolerated. Self-reported adverse events (AEs) are detailed in Table 3. The occurrence of any AE was reported in $10.5 \%$ and $13 \%$ of patients after the first and second dose, respectively ( $p>0.4$ ). Acute myeloid leukemia (AML) patients reported the lowest rate of any AE after the first vaccine dose followed by allo-HSCT recipients, whereas patients with other hematological disorders and ASCT recipients reported the highest rates of any AE. Regarding the overall rates of any AEs after the second vaccine dose, allo-HSCT recipients followed by CAR-T cell therapy recipients showed the lowest rates of any AE in contrast with other hematological disorders, multiple myeloma, and cMPN patients who reported the highest rates of AEs.

## Probabilities of SARS-CoV-2-reactive antibody detection

We first described the overall rate of detectable SARS-CoV-2 antibodies at 3 to 6 weeks after complete vaccination according to the baseline disease or type of cell therapy procedures which are detailed in Fig. 1. We observed 3 groups with differential rates of antibody detection. In
increasing order of antibody detection rates, the first group (detection rates between 50 and $70 \%$ ) included T and B cell NHL along with CAR-T cell recipients and CLL, the second group (detection rates in the $80 \%$ ) comprised allo-HSCT recipients, PCD, ASCT recipients, and AML patients. The third group, with detection rates $>90 \%$, included Hodgkin's disease (HD), other hematological diseases, cMPN, and myelodysplastic syndromes (MDS).

We further developed the TAN model and evaluated by Bayesian network (probabilistic graph) the strength of the variables' dependency, which are represented in Fig. 2. We observed several dependencies among variables based on the TAN model. Variables with a statistically significant direct relationship with the SARS-CoV-2 serological status (bold arrows in Fig. 2) were age, baseline disease, disease status, ECOG performance status, lymphocyte count $<0.5 \times 10^{9} /$ mL and lymphocyte count $<1.0 \times 10^{9} / \mathrm{mL}$. The accuracy of the TAN model was checked by area under the curve test which was 0.87 ( $95 \%$ confidence interval: $0.85-0.90$ ) (Supplementary Figure S1).

## Probabilities of having SARS-CoV-2-reactive antibody according to the interrelation with the most relevant conditions

To estimate the individual conditional probabilities of having detectable antibodies against SARS-CoV-2 after full vaccination schedule according to variables

Table 3 Characteristics of self-reported adverse events according to the disease or procedure


of interest, we built a TAN graph. Figure 3 summarizes the conditional probabilities in the overall cohort. The lowest probability of detecting SARS-CoV-2 reactive antibodies were observed in patients who received anti-CD20 monoclonal antibody therapy at the time of vaccination or within the 6 months before the first dose ( $32.47 \%$ ). Although the probabilities increased in those who received anti-CD20 monoclonal antibody therapy between 6 and 12 months before vaccination, we still observed a low probability of antibody detection ( $49.88 \%$ ). However, the likelihood of antibody detection in patients treated with anti-CD20 monoclonal antibodies more than 1 year before vaccination was similar to other patients ( $76.3 \%$ ). In contrast, a high rate of SARS-CoV-2 antibody detection was observed in patients with SARS-CoV-2 infection prior to vaccination ( $92.09 \%$ ). Regarding the type of vaccine, recipients of the Moderna ${ }^{\circledR}$ mRNA1273 vaccine showed the highest seropositivity rates, especially in patients above the age of 60 .

## Probabilities of detecting SARS-CoV-2-reactive antibodies according to the interrelation with several conditions in specific diseases

To depict conditions that impact the detection of SARS-CoV-2 antibodies in specific scenarios, we conduct a TAN model analyses in disease subsets (Fig. 4A-D).

In patients with B cell NHL (Fig. 4A), we observed again that only $29.32 \%$ of patients who received anti-CD20 monoclonal antibodies within 6 months of the first vaccine dose had detectable SARS-CoV-2 antibodies. Antibody detection decreased with increasing age irrespective of the timing of the last treatment given before vaccination. In contrast, disease status at the time of vaccination showed similar probabilities of antibody detection in those with active disease, partial remission, and complete remission, while it was higher in untreated patients. Of note, allo-HSCT in B cell NHL patients was able to overcome the effect of other conditions (prior anti-CD20 monoclonal antibody therapy, age, or vaccine type) showing the highest rate of antibody detection $(89.5 \%)$.

In patients with plasma cell disorders (Fig. 4B), those who remained untreated before vaccination showed the highest probabilities of antibody detection ( $99.40 \%$ ). Again, increasing age inversely correlates with the probability of mounting SARS-CoV-2 antibodies, whereas lenalidomide therapy at the time of vaccination had no impact on antibody detection.

Regarding CLL patients (Fig. 4C), younger age ( $\leq 60$ years old) showed the highest rate of SARS-CoV-2 antibody detection ( $95.14 \%$ ). Bruton's tyrosine kinase inhibitor therapy and disease status did not show a relevant effect. In contrast, the type of mRNA vaccine showed an

![img-0.jpeg](img-0.jpeg)

Fig. 1 Antibody detection rates according to the baseline disease or procedure. Abbreviations: AML, acute myeloid leukemia; ALL, acute lymphoblastic leukemia; MDS, myelodysplastic syndrome; $B$ cell NHL, B cell non-Hodgkin lymphoma; $T$ cell NHL, T cell nonHodgkin lymphoma; $C L L$, chronic lymphocytic leukemia; $H D$,

Hodgkin disease; cMPN, chronic myeloproliferative neoplasm; AlloHSCT, allogeneic stem cell transplantation; ASCT, autologous stem cell transplantation; CAR-T, T cell chimeric antigen receptor; $P C D$, plasma cell disorders

Fig. 2 Bayesian network and its arcs according to the strength of the dependencies they represent [bold arrows represent the statistically significant relationship between nodes ( $p<0.05$ according to the chi-square test)]. A, gender; B lymphoproliferative disorders; $\mathbf{C}$, age; $\mathbf{D}$, baseline disease; $\mathbf{E}$, daratumomab; $\mathbf{F}$, venetolax; $\mathbf{G}$, lena; H, ruxo; I, iBTK; J, anti-CD20; K, iTK; L, time last treatment; M, status disease; N, ECOG; O, corticosteroids; P, inmunossupresant drugs; $\mathbf{Q}$, neutrophile; R, lymphocyte $<0.5 \times 10^{9} / \mathrm{mL}$; S, lymphocyte $<1 \times 10^{9} / \mathrm{mL} ; \mathbf{T}$, prior COVID; U, HSCT type; V, allo type; W, vaccine; $\mathbf{X}$, serological response
![img-1.jpeg](img-1.jpeg)
important impact in the probabilities of having detectable SARS-CoV-2 antibodies in CLL patients irrespective of the patients' age. Pfizer-BioNTech® BNT162b2 showed a lower detection rate ( $52.47 \%$ ) as compared to Moderna® mRNA1273 (73.16\%), ( $p=0.004$ ).

Finally, cMPN patients (Fig. 4D) are among those who had the highest rates of SARS-CoV-2 antibody detection. Again, older age and Pfizer-BioNTech® BNT162b2 showed a lower probability of having detectable SARS-CoV-2 antibodies.

## Discussion

The current study provides several insights that could help hematologists in clinical practice to focus SARS-CoV-2 vigilance in hematological patients with lower probabilities of mounting SARS-CoV-2 antibodies after full vaccination. First, the statistical model we used was based on conditional probabilities which allows to establish the relationship between the variables in a visual way, representing the results in a very understandable way. Second, we

![img-2.jpeg](img-2.jpeg)

Fig. 3 Conditional probabilities (explained with Probabilities in all tables, where the first variable is the independient variable, serological response, and after the separator the depending variables) using TAN model over the most relevant variables
have visually depicted the likelihood of having detectable SARS-CoV-2 antibodies in the whole cohort according to the most relevant conditions and in specific scenarios such as in patients with B-cell NHL, PCD, CLL, and cMPN.

The first observation of the current study was an encouraging SARS-CoV-2 seropositivity rate in the overall population of hematological patients ( $79 \%$ ) which is in line with prior experiences in this setting [12-20]. We also confirmed the robust immunogenicity and safety of mRNA vaccines in this highly immunosuppressed population. In line with prior reports [17, 28], we also observed that the mRNA1273 vaccine induced higher seropositive rates than the

BNT162b2 and adenoviral vector-based vaccines ( $p<$ 0.0001 , see Table 1). Although BNT162b2 showed lower seropositivity in all diseases/procedures, the main difference was observed in those older than 60 years and particularly in the CLL group ( 52 vs $73 \%, p=0.004$ ). This fact suggests that the amount of spike mRNA in mRNA-1273 (100 $\mu \mathrm{g}$ ) and BNT162b2 ( $30 \mu \mathrm{~g}$ ) per dose could matter in these subsets of patients, supporting the prioritization of using the mRNA-1273 vaccine.

From a practical point of view, we sought to identify the most relevant conditions which had an impact on the serological response in the whole cohort through ML

![img-3.jpeg](img-3.jpeg)

Fig. 4 Conditional probabilities (explained with $P$ in all tables, where the first variable is the independent variable, serological response, and after of separator you have the dependent variables) in numeri-
cally important diseases $\mathbf{A}$ patients with B cell non-hodgkin lymphoma, B plasma cell disorders, C chronic lymphocytic leukemia, and $\mathbf{D}$ chronic myeloproliferative neoplasia

![img-4.jpeg](img-4.jpeg)

Fig. 4 (continued)
methodology. In line with prior reports, we observe a lower antibody detection after vaccination in patients who recently received anti-CD20 monoclonal antibody therapy [12, 17, 29-31], B cell NHL diseases [17, 28, 30], corticosteroids [20], and treated less than 6 months before vaccination [12, $18,28,31]$, as well as in CLL patients [32, 33]. On the other hand, we found conditions associated with higher probabilities of having detectable antibodies, such as patients whose last treatment was given within 1 year before vaccination (but more than 6 months), younger age ( $<60$ years old), and SARS-CoV-2 infection prior to vaccination. Additionally, we were able to identify 3 groups of diseases with different serological positivity rate patterns. Altogether, these findings could be of great value to stratify the need and the urgency of additional interventions and/or monitorization of SARS-CoV-2 immunity and risk of infection in real-life clinical practice (Tables 2 and 3).

Regarding specific scenarios, we focused the TAN model inferences in B cell NHL, CLL, PCD, and cMPN patients representing the three groups with different serological positivity rate patterns (B cell NHL and CLL $<70 \%$, MM in the $80 \%$, and cMPN $<90 \%$ ). Regarding B cell NHL patients and like other series [30], timing of anti-CD20 monoclonal antibody therapy was of utmost relevance, with seropositivity rates increasing as timing from last anti-CD20 therapy increased beyond 6 months, between 6 and 12 months and more than 1 year before vaccination ( $29.32 \%, 45.3 \%$, and $72.6 \%$, respectively). In

contrast with other series [30], age was relevant in our cohort. Younger patients were more likely to be seropositive after vaccination irrespective of the timing of last anti-lymphoma therapy (Fig. 4A). This fact suggests that immunosenescence could also occur in B cell NHL patients and should also be considered for vaccine prioritization programs. Of note, patients with B cell NHL who underwent allo-HSCT showed a higher seropositivity rate (89.5%) than those who underwent an ASCT (59.99%), being in fact similar to untreated patients (85.22%). This fact indicates that allo-HSCT may be able to overcome the impact of prior anti-CD20 monoclonal antibody exposure on vaccine humoral response likely because donor-derived T and B cell lymphocytes has not been exposed to anti B cell lymphocyte monoclonal antibody treatments.

Regarding CLL patients, we observed subtle differences with prior studies regarding conditions affecting serological positivity [32, 33]. While the study of Herishanu and cols showed the highest serological response in complete remission CLL patients, in our series, naïve-treatment patients showed one of highest seropositivity rates (86%) which is in line with another CLL study [33]. This fact infers that CLL patients on Bruton's tyrosine kinase inhibitors and/or venetoclax therapy had lower probabilities of mounting anti-SARS-CoV-2 antibodies not only because of the drugs' effects but likely because the immunodeficiency experienced by patients with CLL. In contrast to both studies, younger age had a positive effect on seropositivity in our cohort. An important finding in CLL patients was the lower probability of seroconversion with the BNT162b2 compound as compared to the mRNA-1273.

MM patients had quite an encouraging seropositivity rate (82%) in line with several other studies [18, 34, 35]. Although some studies found a negative effect on seropositivity of specific treatments such as anti-CD38 monoclonal antibody therapy [36], we did not find relevant differences among those who received lenalidomide or daratumumab. However, the use of corticosteroids showed a negative effect on the seropositivity rate (73.49%) as compared to those not treated with steroids (94.78%). However, the use of corticosteroids was linked with patients receiving anti-myeloma treatment, and thus, this latter finding may simply reflect the fact that patients on active anti-myeloma treatment have a lower likelihood of developing detectable SARS-CoV-2 antibodies. Finally, cMPN patients showed a higher seropositivity rate than MM patients, in line with a prior report [37]. We did not find a relevant impact regarding the treatment status but again older age was the most relevant condition for lower probability of seropositivity.

Our study has several limitations. We focused on qualitative antibody testing to define seropositivity using different serological tests which could be regarded as an incomplete way to measure vaccine-induced immunity. A relevant number of patients who do not develop an adequate humoral response may elicit a specific T cell immunity, as has been observed in patients under anti-CD20 monoclonal antibody therapy [38]. Quantitative humoral assessment may be more accurate than qualitative since the former better predict the risk of breakthrough SARS-CoV-2 infection, and, more importantly, its severity [39]. We also did not analyze neutralizing antibody titers nor T cell responses after vaccination. However, the large number of patients and hematological diseases included, the multicenter approach, and the concordance of our results with other reports should be considered as strengths.

## Conclusions

Our data highlight specific hematological conditions that should be considered when stratification is required for subsequent measures to limit the severity and/or to prevent post-vaccination COVID-19 in these highly immunosuppressed patients. We report conditional probabilities in different scenarios which could be used to further establish a potential timeline for revaccination and/or to better identify patients most probable to benefit from booster doses, which have been shown to be effective in around a half of non-responders to the two-dose initial vaccination [40]. In addition, other preventive approaches such as the use of anti-SARS-CoV-2 monoclonal antibody therapy as pre-exposure and post exposure prophylaxis could be an appealing option for poor responders [41].

Supplementary Information The online version contains supplementary material available at https://doi.org/10.1007/s00277-022-04906-8.

REDCap is developed and supported by Vanderbilt Institute for Clinical and Translational Research. We thank the Spanish Society of Hematology (SEHH) for its support on the study. We sincerely want to thanks the invaluable aid of microbiology services for their commitment in SARS-CoV-2-reactive IgG antibody monitoring in these highly immunosuppressed patients from all participating centers. Finally, we also want to thank the patients, nurses, and study coordinators for their foremost contributions in this study.

The authors who were responsible for patient recruitment are Dolores Caballero, Lucia Lopez-Corral, María-José Terol, Lourdes Vazquez, Marisa Calabuig, Gabriela Sanz-Linares, Francisca Marin, Carmen Alonso, Juan Montoro, Elena Ferrer, Ana Facal, María-Jesús Pascual, Alicia Rodriguez-Fernandez, María T. Olave, Beatriz Gago,

Almudena Cascales-Hernandez, José Ángel Hernández-Rivas, Lucia Villalon, Magdalena Corona, Alicia Roldán-Pérez, Julia Ribes-Amoros, Clara González-Santillana, Ramon Garcia-Sanz, David Navarro, Anna Sureda, and Carlos Solano

The authors who were responsible for writing the manuscript are Jose Luis Piñana, Pablo Rodríguez-Belenguer, Rodrigo Martino, Antonio J. Serrano-López, Emilio Soria-Olivas, and David Navarro were responsible for writing and supervising the writing of the manuscript.

All co-authors were responsible for reviewing the analysis interpretation, suggesting modifications to the text, critically reviewing the manuscript, and for final approval of the manuscript.

Data availability Data available upon request by email to the Spanish hematopoietic transplant and cell therapy group (GETH-TC).

## Declarations

Ethics approval The local ethical committee of the Hospital Clínico Universitario of Valencia approved the registry and study protocol (reference code 35.21)

Patient consent All patients included in this registry gave their sign informed consent according to the Declaration of Helsinki.

Conflict of interests The author(s) declare that they have no conflict of interests.

# Authors and Affiliations 

José Luis Piñana ${ }^{1,2}$ (D) $\cdot$ Pablo Rodríguez-Belenguer ${ }^{3} \cdot$ Dolores Caballero ${ }^{4} \cdot$ Rodrigo Martino ${ }^{5} \cdot$ Lucía Lopez-Corral ${ }^{4} \cdot$ María-José Terol ${ }^{1,2} \cdot$ Lourdes Vazquez ${ }^{4} \cdot$ Marisa Calabuig ${ }^{1,2} \cdot$ Gabriela Sanz-Linares ${ }^{6} \cdot$ Francisca Marín-Jimenez ${ }^{7} \cdot$ Carmen Alonso ${ }^{8} \cdot$ Juan Montoro ${ }^{9} \cdot$ Elena Ferrer ${ }^{1,2} \cdot$ Ana Facal ${ }^{9} \cdot$ María-Jesús Pascual ${ }^{10} \cdot$ Alicia Rodríguez-Fernandez ${ }^{11} \cdot$ María T. Olave ${ }^{12} \cdot$ Almudena Cascales-Hernandez ${ }^{13} \cdot$ Beatriz Gago ${ }^{10}$. José-Ángel Hernández-Rivas ${ }^{14} \cdot$ Lucía Villalon ${ }^{15} \cdot$ Magdalena Corona ${ }^{16} \cdot$ Alicia Roldán-Pérez ${ }^{17} \cdot$ Julia Ribes-Amoros ${ }^{6}$. Clara González-Santillana ${ }^{18} \cdot$ Ramon Garcia-Sanz ${ }^{4} \cdot$ David Navarro ${ }^{19,20} \cdot$ Antonio J. Serrano-López ${ }^{21}$. Ángel Cedillo ${ }^{22} \cdot$ Emilio Soria-Olivas ${ }^{21} \cdot$ Anna Sureda ${ }^{6} \cdot$ Carlos Solano ${ }^{1,2,19} \cdot$ On behalf of Infectious Complications Subcommittee of the Spanish Hematopoietic Stem Cell Transplantation and Cell Therapy Group (GETH-TC)
1 Hematology Department, Hospital Clínico Universitario de Valencia, Avda Blasco Ibañez, 17, 46010 Valencia, Spain
2 Fundación INCLIVA, Instituto de Investigación Sanitaria Hospital Clínico Universitario de Valencia, Valencia, Spain
3 Research Program on Biomedical Informatics (GRIB), Department of Experimental and Health Sciences, Hospital del Mar Medical Research Institute (IMIM), Universitat Pompeu Fabra, Barcelona, Spain
4 Hematology department, University Hospital of Salamanca, IBSAL, CIBERONC, Centro de Investigación del Cáncer-IBMCC (USAL-CSIC), Salamanca, Spain
5 Hematology Division, Hospital de la Santa Creu i Sant Pau, Barcelona, Spain
6 Clinical Hematology Division, Institut Català Oncologia-Hospitalet, IDIBELL, Universitat de Barcelona, Barcelona, Spain
7 Hematology Division, Hospital General universitari d'Elx, Elche, Spain
8 Hematology Division, Hospital Arnau de Vilanova, Valencia, Spain
9 Hematology Division, Hospital universitario y politécnico La Fe, Valencia, Spain
10 Hematology Division, Hospital Regional Universitario Carlos Haya, Malaga, Spain
${ }^{11}$ Hematology Division, Hospital Universitario Virgen Macarena, Sevilla, Spain
12 Hematology Division, Hospital Clínico Universitario Lozano Blesa, IIS Aragon, Zaragoza, Spain
13 Hematology Division, Hospital Clínico Universitario Virgen de la Arrixaca, Murcia, Spain
14 Hematology Division, Hospital Universitario Infanta Leonor, Madrid, Spain
15 Hematology Division, Hospital Universitario Fundación Alcorcón, Madrid, Spain
16 Hematology Division, Hospital Ramon y Cajal, Madrid, Spain
17 Hematology Division, Hospital Universitario Infanta Sofia, Madrid, Spain
18 Hematology Division, Hospital Universitario de Fuenlabrada, Madrid, Spain
19 Department of Medicine, School of Medicine, University of Valencia, Valencia, Spain
20 Microbiology department, Hospital Clinico Universitario de Valencia, Valencia, Spain
21 IDAL, Intelligent Data Analysis Laboratory, ETSE, Universitat de Valencia, Valencia, Spain
22 Hematopoietic Stem Cell Transplantation and Cell Therapy Group (GETH), Valencia, Spain