# Review 

## Causal Modelling for Supporting Planning and Management of Mental Health Services and Systems: A Systematic Review

Nerea Almeda ${ }^{1, *}$, Carlos R. García-Alonso ${ }^{2}$, José A. Salinas-Pérez ${ }^{2}$ (D), Mencía R. Gutiérrez-Colosía ${ }^{1}$ (D) and Luis Salvador-Carulla ${ }^{3}$ (D)<br>1 Universidad Loyola Andalucía, Department of Psychology, C/Energía Solar 1, 41014 Seville, Spain; menciaruiz@uloyola.es<br>2 Universidad Loyola Andalucía, Department of Quantitative Methods, C/Energía Solar 1, 41014 Seville, Spain; cgarcia@uloyola.es (C.G.-A.); jsalinas@uloyola.es (J.A.S.-P.)<br>3 Centre for Mental Health Research, Research School of Population Health, Australian National University, 63 Eggleston Rd, Acton, ACT 2601, Australia; luis.salvador-carulla@anu.edu.au<br>* Correspondence: nmalmeda@uloyola.es; Tel.: +34-955-64-16-00

Received: 19 November 2018; Accepted: 19 January 2019; Published: 25 January 2019


#### Abstract

Mental health services and systems (MHSS) are characterized by their complexity. Causal modelling is a tool for decision-making based on identifying critical variables and their causal relationships. In the last two decades, great efforts have been made to provide integrated and balanced mental health care, but there is no a clear systematization of causal links among MHSS variables. This study aims to review the empirical background of causal modelling applications (Bayesian networks and structural equation modelling) for MHSS management. The study followed the PRISMA guidelines (PROSPERO: CRD42018102518). The quality of the studies was assessed by using a new checklist based on MHSS structure, target population, resources, outcomes, and methodology. Seven out of 1847 studies fulfilled the inclusion criteria. After the review, the selected papers showed very different objectives and subjects of study. This finding seems to indicate that causal modelling has potential to be relevant for decision-making. The main findings provided information about the complexity of the analyzed systems, distinguishing whether they analyzed a single MHSS or a group of MHSSs. The discriminative power of the checklist for quality assessment was evaluated, with positive results. This review identified relevant strategies for policy-making. Causal modelling can be used for better understanding the MHSS behavior, identifying service performance factors, and improving evidence-informed policy-making.


Keywords: mental health systems; mental health services; mental health care, management; policymaking; planning; causal model; Bayesian networks; structural equation modelling; systematic review

## 1. Introduction

Throughout the history of psychiatric care, the deinstitutionalization process has constituted an inflexion point in mental health care provision. With the decline of asylums in the mid-fifties and their closure in the eighties in Europe and the United States of America, mental health care delivery was shifted from isolated hospitals and asylums to communities [1,2]. Community mental health care is understood as the promotion of mental health for a target population, considering its needs and strengths, favouring social support, and highlighting evidence-based and recovery-oriented services [3]. Nevertheless, the provision of integrated care into the community is still a major challenge [4] due to the added complexity of mental health systems $[5,6]$.

The current mental health environment is characterized by high levels of mental disorders [7], socioeconomic costs [8,9,10], and unmet population needs [11,12,13,14], which require improved planning and management of mental health services and systems (MHSS). Trying to use an approach from an ecological perspective, four levels of analysis can be defined: macro, meso, micro, and nano levels. This framework is useful for classifying models in order to know the levels at which they can have a potential impact. The majority of studies focus on analyzing the nano level, which involves patient or consumer interventions [15,16,17,18] and career and professional characteristics [19,20]. The other levels have been less frequently studied, although they are relevant for planning and management of mental health care. Thus, micro-level analyses include organizations for care provision (for example, mental health centres or acute wards), meso-level analyses include local information (for example, small mental health catchment areas), and macro-level analyses comprise global information (large health districts, regional or national) [21,22]. Findings from environmental sciences show that advanced methodologies, modelling, and real simulations can play an important role in guiding evidence-informed policy design based on the analysis of healthcare ecosystems for providing better mental health care [6]. Recent studies focused on developing decision support systems (DSS) show that expert knowledge formalization is fundamental to guide both operational and statistical techniques [23,24]. A DSS is a computer-based tool that usually integrates databases with analytical procedures [24] (operational like relative efficiency analysis, statistical like factor analysis, artificial intelligence like fuzzy inference, etc.). These tools are designed and developed for processing data and producing useful information for decision makers in complex and uncertain environments. In some cases, resulting formal representations of the explicit knowledge (rule-based models, causal models, etc., obtained from a knowledge discovery process) have been integrated into analytical procedures (operational, statistical, etc.) [5]. A knowledge discovery process includes qualitative (focus and Delphi groups, structured interviews, etc.) and quantitative techniques (knowledge discovery from data, cluster analysis, factor analysis, etc.) in order to make expert knowledge explicit. The final product of this process is a structured model (hierarchical, causal, rule-based, etc.) that can be included in, for example, DSS [5,24]. One of the best ways to do so is to design a causal model wherein all the critical variables and dimensions are identified, as well as their causal relationships [25], if they exist.

A causal model, or its formal expression, a Bayesian network, shows causes and effects [26,27] by using variables (nodes in, usually, a graph) and their relationships (connections-different kinds of arrows or lines-in, again, graphs). Bayesian networks (BNs) can be integrated in DSS for explaining causal links between variables for both operational and statistical analysis because in real systems, variables and/or dimensions (that summarize the behaviour of a set of variables with a specific meaning, for example, deprivation) cannot be considered exogenous (there are causes and effects). Very often, BNs are theoretical models, but if data are available, their structure (variables/dimensions and causal links) can be tested and, sometimes, confirmed by using statistical procedures, such as structural equations modelling (SEM) [25].

The formal structure of a causal model can be defined as a set of equations (usually represented by a graph), such as:

$$
x_{i}=f_{i}\left(p r_{i}, u_{i}\right), i=1,2, \ldots, n
$$

where $x_{i}$ is the value of the $i$ th variable ( $n$ is the number of variables of the model); $p r_{i}$ is the minimum set of predecessor variables of $x_{i}$, which are Markovian parents that make $x_{i}$ independent of all its other predecessors; and, finally, $u_{i}$ is the error that assumes the existence of unobserved variables, factors, or relationships. The Markovian parents are the minimum set of variables that can be considered direct causes of $x_{i}$ and, therefore, they have a direct and unidirectional link to $x_{i}$ in a BN. This model (1) is perfectly causal, nonparametric, and nonlinear and is therefore more general than the structural equations that, in linear form, are defined by a set of equations, such as:

$$
x_{i}=\sum_{j=1}^{m} \beta_{i j} x_{j}+u_{i}, i=1,2, \ldots, n
$$

where $x_{j}$ represents the independent variables (variables than can be considered causes of $x_{i}$ ), and $\beta_{i j}$ represents the structural coefficients of $x_{j}$. The structural equations model (2)—always algebraic - can be more general if it includes nonlinear equations, but it can be difficult to solve. In this situation, the problem is answering the following question: can we consider the structural coefficients calculated using a mathematical procedure as a representation of causal behaviour? This question is fundamental and not easy to answer [25] because causal relationships cannot be derived from any statistical or functional operation. Causal relationships derive from previous causal assumptions that have to be formalized in an appropriate way like, for example, graphs [25,27]. By using graphs as a mathematical language, researchers can overcome one of the main drawbacks in (2), that is: causal relationships between two variables cannot be correctly defined without taking into account that the cause can also have cause variables [25]. Therefore, the effect of the latter cannot be separated when the effect variable is assessed. Taking into account this circumstance, we have added structural equations in the search strategy in order to check the influence of causal reasoning in the resulting studies.

In health care, BNs have been applied for decision-making [28,29,30,31] and case assessment: analyzing new diagnosis strategies [32,33,34] and diagnosing social anxiety [35], depression [36,37], and Alzheimer's disease [38,39]. Despite its reported utility in formalising the explicit knowledge about the structure of a system, in assessing potential responses:

$$
\mathbf{X}_{\mathbf{M}_{\mathbf{x}_{\mathbf{j}}}}^{\mathrm{i}}(\mathbf{u})
$$

where $\mathbf{X}^{\mathbf{i}}$ and $\mathbf{X}_{\mathbf{j}}$ are two subsets in the set of variables -endogenous or exogenous (U)- of the BN and $\mathbf{M}_{\mathbf{x}_{\mathbf{j}}}$ is the action:

$$
\operatorname{do}\left(\mathbf{X}_{\mathbf{j}}=\mathbf{x}_{\mathbf{j}}, \forall \mathbf{j}\right)
$$

on it (system) and in evaluating counterfactual sentences (in situation $u, \mathbf{X}^{i}$ would be $\mathbf{x}_{\mathbf{i}}$, had $\mathbf{X}_{\mathbf{j}}$ been $\mathbf{x}_{\mathbf{j}}$ ) $(3,4)$, the application of BNs for the analysis of health care services and systems is scarce. A number of studies have used BNs for assessing the quality of nursing homes [40], but it is not a frequent method for planning or management. In mental health, the design of a BN is complex because all the organizations involved must be coordinated at the micro, meso, and macro levels [22]. Although there is an abundant background concerning the provision of mental health care in the community [41,42,43,44,45,46,47], there is still no clear identification of its critical variables (inputs and outcomes of the system) and their causal links (causes and effects of any real intervention). For example, the number of persons in staff is a consequence of the number of places, beds, or programs or vice versa.

The aim of this paper is to systematically review the empirical background of causal modelling applications by employing a BN and SEM for planning and management of MHSS. Both the studies and the most relevant strategies for policy-making are identified.

# 2. Materials and Methods 

We followed the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) guidelines [48] for systematically reviewing the literature. This study has been registered in the International Prospective Register of Systematic Reviews database (PROSPERO number CRD42018102518). In order to facilitate the reading of this study, we have specified the acronyms used in Table 1.

### 2.1. Search Strategy

Several search strategies were explored. First, we aimed to identify potential studies that applied BNs for supporting decision-making in mental health. We designed an inclusive Boolean algorithm including specific terms for psychopathology and BNs (Table 2). After carrying out the procedure, 20 studies focused on BNs and mental health care, with the majority focusing on case assessment and diagnosis of psychopathologies (nano level). In addition, it was detected that SEM was frequently used without mentioning its relationship (see the introduction) with causal models. Pearl [25] stated there exists a potential risk of using SEM, like, for example, a regression model that can show spurious causal links. These kind of analyses are not based on a real BN developed previously by using explicit

expert knowledge for explaining the causal nature of the system under study. In BN, causal links represent real cause-effect relationships between variables (domains and/or constructs can also be included) that sometimes, if complete and reliable datasets are available, can be confirmed by using statistical analysis like SEM.

Table 1. Acronyms used in the text.


Table 2. Search strategy piloted in MEDLINE-PubMed version (First version).


Consequently, a second and definitive search strategy was designed to solve all the limitations mentioned above, including new terms related to mental health services (to avoid terminological problems in mental health services classifications), SEM, and planning and management. This search strategy was piloted on April 1, 2018. The final Boolean algorithm was conducted in the MEDLINE database (PubMed version) (Table 3). At a third stage, we conducted the search in the following databases: Scopus, Web of Science, PsycARTICLES, PsycINFO, Psychology Database, Nursing \& Allied Health Database, and Health \& Medical Collections.

The search strategy was developed based on the PICO Model:

1. Population (P): All types of mental health services and/or systems that provide care for the population with a lived experience of mental disorder. Due to the wide terminological variability relating to MHSS, an inclusive set of terms was included [49-53] (Table 3).
2. Intervention (I): Causal modelling, including BNs and SEM (as a simplification of a BN), for guiding and supporting planning and management of MHSS [54].
3. Comparator (C): Refers to a control group or comparison intervention (PICO is a guide for designing research questions based on structured search strategies in a clinical framework). In our study, it is not applicable.
4. Outcome (O): Any resulting expert-based or data-based causal model.

Table 3. Search strategy piloted in MEDLINE-PubMed version.


# 2.2. Eligibility Criteria 

We included studies that employed BNs and SEM for supporting planning and management of mental health services and/or systems. Only peer-reviewed articles and book chapters were selected (no constraints due to country of origin, publication date, or language were taken into consideration), and other publication types were excluded.

### 2.3. Study Selection, Data Collection, and Summary Measures

After piloting the Boolean algorithm, we removed duplicated results of the record pool. CG and NA independently carried out the selection procedure in two phases: screening and eligibility. In the first step, NA and CG checked paper titles and abstracts to decide if they met the inclusion criteria. In the second step, they reviewed their full text. JAS, a third author not involved in the selection process, resolved any disagreement between CG and NA. The concordance degree was assessed by statistical tests (kappa and ICC).

Data extracted were organized into five sections: (1) study selection, (2) study characteristics, (3) main findings, (4) quality of included studies, and (5) implications for policy-making. In the "study selection" section, we describe the process for selecting studies (screening and eligibility). "Study

characteristics" involves information regarding the country and year, objectives, type of MHSS, target population, data, variables, and methods. The "quality of included studies" section offers a new proposal for the assessment of the study quality. Finally, the "implications for policy-making in mental health care" section identifies potential strategies for management and planning.

A meta-analysis of the information available was not developed because of the extreme variability of the studies found (their findings are not comparable).

# 2.4. Quality Assessment 

To assess the quality of the studies included, a new checklist was designed based on MHSS structure [51,53,55], target population for care delivery, and causality [25,54]. In addition, we took into consideration a specific quality assessment tool developed by Thomas, Ciliska, Dobbins and Micucci [56] for evaluating systematic literature reviews assessing the effectiveness of public health nursing interventions. The items finally selected for quality assessment were: the study includes more than one type of mental health service or system (one item related to the MHSS structure under study); the study specifies more than one type of target population for care delivery (one item related to the characteristics of the target population); the study analyzes variables, including resources and outcomes of the mental health care (one item related to the existence of resources and outcomes); and the study includes a causal graph, takes into account external expert knowledge for identifying the nodes and the causal relationships of the causal graph, combines data and external expert-based knowledge, includes sensitivity or parametric analysis, carries out factorial confirmatory/exploratory analysis, develops any kind of causal-related inference and, finally, the causal model is integrated in a decision support system (seven items related to causal methodology). Due to the purpose of the systematic review, the weight of methodological issues is greater than items related to the search strategy (Table 3): types of mental health services and management and planning. To assess the relevance of causal modelling, three domains (groups of items that can be considered essential in this kind of studies) have been taken into consideration: (1) expert-based issues (existence of a causal graph, expert identification of the nodes, and knowledge inclusion), (2) statistical procedures (sensitivity/parametric/factor analysis and causal-related inference), and (3) managerial implications (decision support systems). These domains balance the relevance of the knowledge, permit statistical analysis, and introduce practical implications for management.

## 3. Results

### 3.1. Study Selection

In total, the search strategy retrieved 1847 records (Figure 1); the bibliography of the selected studies was also checked, and no additional references were found. After removing duplicates, 1229 records were analysed (CG and NA) by titles and abstracts: 58 fulfilled inclusion criteria. These 58 studies were thoroughly assessed (CG and NA) for eligibility (full text) and, finally, seven articles fulfilled the inclusion criteria (Figure 1). The main reasons for rejecting a study were (in order, more to less important): the object of study was a group of patients or specific illnesses and their methods were not really used to develop a BN or an SEM or were mainly used in diagnosis. The degree of agreement was assessed by using the intra-class correlation (ICC) analysis and Kappa index. As expected, the results evidenced that there was a strong agreement level (Kappa $=0.972, p=0.000 ; I C C=0.986$, $p=0.000)$.

![img-0.jpeg](img-0.jpeg)

Figure 1. Flow chart of articles included and excluded after the systematic review.
From: Moher D, Liberati A, Tetzlaff J, Altman DG, the PRISMA Group (2009). Preferred Reporting Items for Systematic Reviews and Meta-Analyses: The PRISMA Statement. PLoS Med 6(7): e1000097. doi:10.1371/journal.pmed1000097

# 3.2. Study Characteristics 

### 3.2.1. Country and Year

High variations in publication dates and countries were found (Table 4). The first study was published forty years ago [57], while the last one was recently published [58]. Since the first publication, the production of studies has been irregular. Pioneer studies were from United States of America [57,59] and were published between the 1980s and 1990s; no other study was published until 2012 [60].

Table 4. Results: Study characteristics.


Table 4. Cont.

Group 1: Resources.
Eight ICD-10 adult mental disorder
Group 2: Service user's characteristics.
Hospital admissions, median length of stay, annual numbers of Mental Health Act detentions, and community team activity.
Group 3: Service performance and outcomes. | Linear regression, Pearson's $r$-statistic, SEM, parametric bootstrap, and two-tailed $t$ test.  |
Direction: Strategic planning.
System: Human Resources Orientation; Process
Management; and Patient, customer, \& Market Orientation.
Foundation: Measurement, Analysis, \& Knowledge management.
Group 1: Resources.
Results: Hospital Performance.
Group 3: Service performance and outcomes. | Confirmatory factor analysis and SEM analysis.  |
Group 2: Service user's characteristics.
Service performance: Adjusted adequacy of help (Montreal Assessment of Needs Questionnaire), Continuity of care (Alberta Continuity of Services Scale for Mental Health), and Recovery service orientation (Recovery Self-Assessment Scale, revised person-in-recovery version). Outcomes: Quality of life (Satisfaction with Life Domains Scale) and Personal recovery (Recovery Assessment Scale). Group 3: Service performance and outcomes. | Zero order correlations, Pearson's correlations, bootstrap method with 2000 iterations; SEM and mediation analysis.
Factor loadings, regression analyses, non-parametric model-based bootstrapping with 2000 iterations; chi-squared goodness-of-fit statistic, Bolian-Srine bootstrap method, Tucker-Lewis Index, and root-mean-square error of approximation.  |

Table 4. Cont.

Group 1: Resources.
Risks factors for mental health and psychiatric morbidity.
Group 2: Service user's characteristics.
Treated prevalence in a small health area in a specific year $t$ (patients_t), patients already in contact with mental health community service in the year t-1 (patients_t-1), new patients who contact the specialized community services in this year (new patients_t), activities with patients, and relative technical efficiency.
Group 3: Service performance and outcomes. | "Bayesian network Data Envelopment Analysis model": Data Envelopment Analysis (DEA) with returns variables to scale (BCC), BN integrating fuzzy rules base to interpret causal relationships, interpretation of efficiency variables according to rule-base "if ... then" (Model of Basic Mental Health Community Care). Services are standardized using ESMS/DESDE-LTC classification system.  |
Group 1: Resources.
Socioeconomic Status, Marital Status/Living Arrangement, Age, Ethnicity, Race, and Urbanization.
Group 2: Service user's characteristics.
Mental Hospital Utilization, General Hospital Utilization, and Long-Term Care Utilization.
Group 3: Service performance and outcomes. | Path analysis, path coefficients, test of variable distributions for normality, regression analysis, factor analysis, covariance analysis, path diagram, zero-order correlations, and multiple regression equations.  |

# 3.2.2. Objectives 

The selected studies show very different aims (Table 4). In [61], causal reasoning is used to develop a model for discharged decision-making in medium secure services. In the Delany, Fletcher and Lennox study [59], it is used for testing the impact of the structure of shelter organizations on services-amenities and organizational relations. For Roux, Passerieux and Fleury [58], the purpose was to assess the service performance as a mediating factor between patient needs and outcome production. Finally, two papers aimed to identify determinants of long-term care services use [57] and trends in hospital and community care over 14 years [62]. The remaining two studies wanted to identify evaluation criteria for mental health care quality assessment [60] and to improve relative technical efficiency assessment [22].

### 3.2.3. Types of Mental Health Services and Systems

Studies can be divided into two main groups, depending on whether they analyzed a single MHSS or a group of MHSSs (Table 4). Four studies examined a single MHSS and the services analyzed were medium secure services [61]; sheltered homes [59]; mental hospitals [60]; and residential services, including mental hospitals, general hospitals, and nursing homes care [57]. On the other hand, three studies [22,58,62] combined hospital and community-based care services, following a systems approach and analysis.

### 3.2.4. Target Population

In all studies, the target population was people with a lived experience of mental disorder. Two studies [58,62] used an international diagnostic criteria, such as DSM-5 or ICD-10, for classifying psychiatric cases. Three studies focused on general mental health diagnosis, but they did not specify the diagnostic criteria employed [22,60,61]. Finally, two studies were focused on specific target groups: homeless [59] and/or elderly people with long-term care needs [57] (Table 4).

### 3.2.5. Data

Six out of seven studies collected data by using questionnaires or surveys [57-62] (Table 4). Some used data retrieved at the national level, for example, from the Police National Computer [61], NHS England [62], state-operated hospitals in Korea [60], Mental Health Service Network from Quebec [58], Public Mental Health System of Andalusia [22], and Massachusetts Department of Public Health [57]. In the study of Salvador-Carulla et al. [22], data were used for assessing the relative technical efficiency, not for checking the BN, which showed the causal relationships between variables. Again, many sources had different purposes.

### 3.2.6. Variables

BNs [22,61] included greater numbers of variables than SEM [57-60,62] (Table 4). Due to the variability within the analyzed variable sets, three categories have been designed to classify them: resources, service user's characteristics, and service performance and outcomes (Table 4).

### 3.2.7. Methods

Regarding the causal methodology, both BNs and SEM were identified in the selected studies. Five out of seven applied SEM and data-based causal models [57-60,62] combined with additional statistical methods (Table 4).

On the other hand, two out of seven studies [22,61] developed a BN. Constantinou et al. [61] tested the causal predictability of their BN by carrying out a quantitative analysis. In Salvador-Carulla et al. [22], formalized expert knowledge (standard if $\ldots$ then $\ldots$ rule-base model) from senior managers and policy-makers was used for designing the BN and for interpreting variable values (Table 4).

BNs used more variables than SEM. In addition, BNs were more flexible because they could include almost any causal information, but SEM depends on the availability of data.

The methods carried out in the seven studies and their main outcomes are represented in Figure 2.
![img-1.jpeg](img-1.jpeg)

Figure 2. Formal representation of the selected studies (Note: no study combines Bayesian networks and Structural Equation Modelling).

# 3.3. Main Findings 

The main findings of the selected studies were classified according to the complexity of the systems under analysis, distinguishing if they focused their attention on a single MHSS or a group of MHSSs and including the levels (macro, meso, micro, and nano) at which the designed models can have a potential impact (Table 5). Therefore, complexity is directly related to the potential number of variables and relationships needed to explain the whole environment under study. Regarding the number of MHSSs, the DSVM-MSS model (micro level) is an appropriate DSS for predicting if a service user is ready to be discharged from medium-secure services [61], and this model introduces moderate to significant improvements in comparison with the methodology currently used (clinical or regression-based models). In shelter homes (micro level), the effect of the organizational structure on the service and amenities performance is better through organizational relations. Therefore, organizational relations represent a mediator between organizational structure and services and amenities [59]. The case of mental health hospitals (micro level), which analyzed the structure of the Malcolm Baldrige National Quality Award model, showed that Driver, Direction, System, and Foundation elements of the model had a variable impact among them and/or on the results [60]. In addition, sociocultural variables explained only $9 \%$ of the variance of mental hospital utilization, at the meso level [57].

Following with studies that included a group of MHSSs (Table 5), the results showed that the pattern of inpatient admissions and length of stay varied across different psychopathologies over 14 years, at the micro level (1998-2012) [62]. In addition, there was a significant association between patient needs, service performance, and/or outcomes produced at the micro level [58]. Finally, the EbCA-BNW-DEA model, at the meso level, was an appropriate decision-making tool for supporting planning and management of MHSSs, as it improved efficiency assessment, included expert knowledge, and established causal relationships among their elements [22].

Finally, all the studies that used SEM linked their results to causal structures. As it was stated before, this fact can be arguable. Looking for evidence in that sense, the references cited in the selected studies were studied. Only [22,61] developed a BN (Figure 2) and directly cited Judea Pearl's research (Adnan Darwiche is not cited at all). Checking the references cited by the selected studies, only [61], 17 studies, and [58], one study, include Pearl's research, and Darwiche's research is not cited at all. On the other hand, no selected study has designed any counterfactual sentence related to their causal models.

Table 5. Results: Main Findings.


# 3.4. Quality of Included Studies 

The quality assessment of selected studies involved four components: MHSS structure, target population, resources and outcomes, and methodology (Table 6).

Table 6. Checklist for quality assessment


Three out of seven studies [22,58,62] included more than one type of mental health service under analysis and the correspondent diverse target population (not restricted to a specific target population). All studies integrated variables of resources and outcomes of the MHSSs in the causal model.

Regarding the methodology, six out of the seven studies included a graph defining variables (nodes) and causal relationships (links) [22,57-61]. Four out of the seven studies included external expert knowledge for designing the graph [22,57,60,61]. Four studies combined data and external expert-based knowledge [57,58,60,61]. Following with the methods, four studies used sensitivity or parametric analysis [58,59,61,62], while the development of factorial confirmatory or exploratory analysis was included in three studies [57,59,60]. In addition, two studies included causal-related inference [61,62]. Finally, two studies integrated a BN in a more complex DSS [22,61].

Analyzing the checklist for quality assessment (Table 6), item 3 (variables include resources and outcomes of mental health care) was not discriminative and must be removed because all the studies matched with it.

According to the number of fulfilled items, the best study is [61] because it fulfils six ( $100 \%$ methodological items) out to nine items (after the exclusion of item 3); in second position are [22,58], with five ( $60 \%$ methodological) out nine items; in third are [57,60], with four items ( $100 \%$ methodological); in fourth is the study [62], which fulfils four items, only $20 \%$ of which are methodological ones; and finally, [59] can be considered the last one, fulfilling three items ( $100 \%$ methodological). If a weight is assigned to the methodological items (the last 7: causal modelling ones), for values greater than 0.51, the new ranking is: [61], [57,60], [22,58], [59], and finally [62].

### 3.5. Implications for Policy-Making in Mental Health Care

All studies included in the present systematic review developed a causal model that can be used, directly or indirectly, for guiding MHSS management and planning, but only two were designed to be integrated in a DSS [22,61].

Regarding studies that assessed a single MHSS, recommendations for shelter home services focused on the finding that the interaction between the organizational structure of the services (shelter homes) and the community (real environment) should be improved because it has a relevant impact on the service delivered to homeless people [59]. In addition, integrated care should be provided within the community to avoid the segregation of homeless people, and it is crucial to carry out specialized

training in this population's needs for social workers. In the case of nursing home services, it may be possible to decrease the wrong placement capacity by reorganizing the process of treatment in general hospitals and providing training for families who would like to take care of patients at home, being the admission policy determinant, especially for elderly people to mental hospitals [57].

Following with studies that assessed a group of MHSSs, the results suggested that a reduction of beds, based on the deinstitutionalization policy, had a variable impact, depending on the mental disorders, on hospital admissions (e.g., decreasing depression admissions and increasing eating disorders admissions), and on length of stay (e.g. significant decreasing for specific diagnoses such as abuse of alcohol) [62]. Moreover, evidence shows that the changes in admissions are not associated with the activity of community mental health teams after deinstitutionalization. Additionally, the relationship between patient needs and outcomes was partially mediated by service performance, which means that improving mental health service performance is important for improving recovery outcomes [58]. The effectiveness of MHSS for people with the highest needs is lower, and the main implications showed the importance of developing recovery-oriented services (e.g., assertive community treatment, intensive case management, and supported employment) for helping this kind of user; consequently, increased investment in specialist services is needed.

On the other hand, only one study include service-user information that can be considered an approximation to the analysis of service user perspectives: quality of life and personal recovery [58]. Service user experiences and family opinions are relevant clinical outcomes for assessing service performance and quality, as well as in designing mental health interventions and policies.

# 4. Discussion 

To the best of our knowledge, this is the first study to collect empirical evidence of causal modelling applications (BNs and SEM) for MHSS planning and management. It followed the PRISMA guidelines [48] by designing an integrative and extensive search strategy without restrictive inclusion criteria. This article provides an updated state of the art and highlights some strategies for policy-making.

Although causal modelling has been widely applied in general health and mental health care for supporting decision-making (patient level, e.g., for supporting the diagnosis) [35,37,38], it is not the case for the other levels of analysis (micro, meso, and macro). Despite its utility and increased interest in the last years [22,58,61,62], the development of causal modelling is still scarce due to the complexity (the number of variables -sometimes grouped in imprecise domains or constructs- and their causal relationships -sometimes difficult to explain- are very high) and the uncertainty (the statistical nature of the variables are unknown -unreliable or imprecise- and there are missing variables) of real environments. As it was stated before, it is very difficult to identify the critical variables/domains and their causal relationships without formal expert-based models that can explain the behaviour of mental health systems.

The results show that causal models are accurate for supporting the management of not only specialized MHSS, but also nursing homes, secure medium services, and shelter homes that provide care for mentally ill people. In conclusion, advanced and hybrid methodologies are appropriate tools for supporting decision-making, planning, and management of mental health services [22,61]. Regarding the services and organization, the performance of mental health services plays a role in recovery outcomes and care provision [58], as well as the interaction between the environment and shelter homes impact on care provision to homeless users [59]. In this line, organizational interventions, such as reductions in bed availability, impact on service utilization [62]. In addition, socioeconomic and demographic factors explained the utilization of long-term care services [57]. In addition, it was shown how process management impacted hospital performance, and this information can be used by planners and managers of mental hospitals for decision-making [60]. Finally, although three studies [22,58,62] provided MHSS information from a holistic perspective, integrating hospital and community-based care, there was a lack of systematization of mental health care provision.

The new extensive checklist for quality assessment of the selected studies was sufficiently discriminative, and only one criterion should be considered arguable (all the studies fulfilled it). Taking into account that the checklist included both structural (MHSS) and methodological (causality) questions, it can be considered as a basis for new proposals in this research field. By using the checklist, it is possible to rank the selected studies according to their quality.

This paper also notes the extreme variability in the terminology used for MHSSs (e.g., medium secure service, shelter organizations, mental hospitals, community-based mental health agencies, community mental health housing resources, or nursing homes). Just one out of seven studies [22] used an international standard codification tool called DESDE-LTC [51],for classifying the mental health systems according to the main type of care provided (residential, day, or outpatient care). In addition, this book chapter included a large sample of MHSSs, grouped in small health areas, providing a meso-level analysis. The lack of using standard classification systems, such as DESDE-LTC or ESMS [53], is a handicap to making international comparisons or conducting meta-analysis among studies, catchment areas, and services [63,64,65].

# Limitations 

The high variability of the included studies did not allow us to carry out a meta-analysis. In addition, the lack of mental health services standardization did not make it possible to compare MHSS internationally. There is no standardized quality assessment tool for this area of study, which can be considered another limitation. This limitation was overcome by developing an ad hoc checklist.

## 5. Conclusions

In the present study, it is stated that, in spite of the potential utility, there are few studies that have applied causal modelling for supporting MHSS planning and management. Causal modelling utility is demonstrated by checking the variability of the systems under study. By applying causal modelling, it is possible to identify relevant strategies in policy-making. Finally, it is feasible to assess the quality of the studies by using the checklist developed in this paper.

Therefore, keeping in mind the current context characterized by economic constrains and gaps of unmet population needs [11,12,13,14], MHSS planning and management should be dramatically improved because they have a key role in decreasing the gaps and increasing the MHSS efficiency and effectiveness. MHSS research is crucial for designing evidenced-informed decisions, which will improve care delivery for people suffering from a mental disease. In this sense, it is highly recommended that new studies are developed to identify causal relationships among the different elements of the mental health care system for guiding decision-making. Following with this idea, the inclusion of service user perspectives as clinical outcomes is essential to designing new BNs (they can be causes or effects, depending on the causal model orientation) for mental health management and planning.

Author Contributions: Conceptualization, C.G.-A. and N.A.; methodology, N.A., C.G.-A., and J.A.S.P.; formal analysis, C.G.-A. and N.A.; investigation, N.A., C.G.-A., J.A.S.P., M.R. G.-C., and L.S.-C.; writing-original draft preparation, N.A. and C.G.-A.; writing-review and editing, N.A., C.G.-A., J.A.S.P, M.R.G.-C., and L.S.-C.; funding acquisition, C.G.
Funding: This research was funded by the Institute of Health Carlos III, REFINEMENT Spain project PI15/01986.
Acknowledgments: We are grateful to the senior managers of the Mental Health Network of Gipuzkoa (Basque Country, Spain), highlighting Doctor Álvaro Iruin and Doctor Andrea Gabilondo, and the senior managers of the Mental Health Network of Bizkaia (Basque Country, Spain), particularly Doctor Carlos Pereira, Doctor Enrique Pinilla and Mrs. José Uriarte, for the support in developing the present study.
Conflicts of Interest: The authors declare no conflict of interest.
