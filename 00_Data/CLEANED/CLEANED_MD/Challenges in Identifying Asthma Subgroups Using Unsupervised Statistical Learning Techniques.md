# Challenges in Identifying Asthma Subgroups Using Unsupervised Statistical Learning Techniques 

Mattia C. F. Prosperi ${ }^{1,2}$, Umit M. Sahiner ${ }^{3}$, Danielle Belgrave ${ }^{1,2}$, Cansin Sackesen ${ }^{3}$, Iain E. Buchan ${ }^{1}$, Angela Simpson ${ }^{2}$, Tolga S. Yavuz ${ }^{3}$, Omer Kalayci ${ }^{3 *}$, and Adnan Custovic ${ }^{2 *}$<br>${ }^{1}$ Centre for Health Informatics, Institute of Population Health, and ${ }^{2}$ Centre for Respiratory Medicine and Allergy, Institute of Inflammation and Repair, University of Manchester, United Kingdom; and ${ }^{3}$ Hacettepe University School of Medicine, Pediatric Allergy and Asthma Unit, Ankara, Turkey

Rationale: Unsupervised statistical learning techniques, such as exploratory factor analysis (EFA) and hierarchical clustering (HC), have been used to identify asthma phenotypes, with partly consistent results. Some of the inconsistency is caused by the variable selection and demographic and clinical differences among study populations. Objectives: To investigate the effects of the choice of statistical method and different preparations of data on the clustering results; and to relate these to disease severity.
Methods: Several variants of EFA and HC were applied and compared using various sets of variables and different encodings and transformations within a dataset of 383 children with asthma. Variables included lung function, inflammatory and allergy markers, family history, environmental exposures, and medications. Clusters and original variables were related to asthma severity (logistic regression and Bayesian network analysis).
Measurements and Main Results: EFA identified five components (eigenvalues $\geqslant 1$ ) explaining $35 \%$ of the overall variance. Variations of the HC (as linkage-distance functions) did not affect the cluster inference; however, using different variable encodings and transformations did. The derived clusters predicted asthma severity less than the original variables. Prognostic factors of severity were medication usage, current symptoms, lung function, paternal asthma, body mass index, and age of asthma onset. Bayesian networks indicated conditional dependence among variables.
Conclusions: The use of different unsupervised statistical learning methods and different variable sets and encodings can lead to multiple and inconsistent subgroupings of asthma, not necessarily correlated with severity. The search for asthma phenotypes needs more careful selection of markers, consistent across different study populations, and more cautious interpretation of results from unsupervised learning.

Keywords: asthma; children; clustering; machine learning; endotypes

[^0]
## AT A GLANCE COMMENTARY

## Scientific Knowledge on the Subject

Unsupervised statistical learning techniques have been used to identify latent subgroups of children and adults with asthma who display different patterns of clinical features. The results were only partly consistent across different studies, giving rise to different subgroupings.

## What This Study Adds to the Field

The observed heterogeneity reflects differences in demographic and clinical characteristics of the populations examined. However, we also demonstrate that such inconsistencies may be an artifact of the clustering techniques used, and of the variable encodings and transformations (e.g., discretization and dimension reduction).

Despite efforts made by the pharmaceutical industry and academia, asthma remains poorly understood, with a modest drug armamentarium (1). There is increasing recognition that asthma is a heterogeneous disease with multiple disease variants, which may have a similar clinical presentation, but differ in their etiology and pathogenesis $(2,3)$. It is likely that these different asthma subgroups (sometimes referred to as asthma endotypes [3]) have different causative mechanisms, and may require different treatments. Appropriate identification of such asthma subgroups is a critically important first step toward understanding their specific underlying biologic mechanisms, which is a key building block for therapeutic target identification and the development of novel treatments (4). This is a prerequisite for the move toward personalized or stratified health care to optimize clinical management and prevention of asthma (5).

Computer-assisted reasoning can facilitate the exploration of rich clinical data sets to enable better understanding of disease subgroups and their pathophysiology, and optimization of existing treatments. A data-driven approach with unsupervised statistical learning techniques can be used for discovery of latent asthma phenotypes, which can be derived based on a series of observable disease manifestations, instead of using predetermined classifications proposed by committees of experts. Several previous studies applied principal components analysis, exploratory factor analysis (EFA), partitioning clustering, hierarchical clustering (HC), and other techniques to identify latent groups and associated symptom patterns among adults (6-8) and children (9-12) with asthma. The results have been inconsistent. This inconsistency may be explained in part by natural heterogeneity (differences in the demographic or clinical characteristics of the populations studied), and in part by artifacts of data


[^0]:    (Received in original form April 12, 2013; accepted in final form October 23, 2013)

    * These authors contributed equally.

    Supported in part by University of Manchester's Health Research Centre funded by the MRC grant MR/K006665/1.
    Author Contributions: M.C.F.P., study concept, data analysis, and manuscript writing. U.M.S., patient recruitment and data acquisition. D.B., statistical analysis. C.S., patient recruitment and data acquisition. I.E.B., statistical/informatics review and manuscript review. A.S., study concept and manuscript review. T.S.Y., patient recruitment and data acquisition. O.K., study design, clinical review, and manuscript review. A.C., study design, study concept, and manuscript review.
    Correspondence and requests for reprints should be addressed to Mattia C. F. Prosperi, M.Eng., Ph.D., Centre for Health Informatics, Institute of Population Health, University of Manchester, 1st Floor, Jean McFarlane Building, Room 1.314, Oxford Road, Manchester M13 9PL, UK. E-mail: mattia.prosperi@ manchester.ac.uk
    This article has an online supplement, which is accessible from this issue's table of contents at www.atsjournals.org
    Am J Respir Crit Care Med Vol 188, Iss. 11, pp 1303-1312, Dec 1, 2013
    Copyright (c) 2013 by the American Thoracic Society
    Originally Published in Press as DOI: 10.1164/rccm.201304-0694OC on November 1, 2013 Internet address: www.atsjournals.org

processing and analysis. We hypothesize that the subgrouping of asthma from typical study datasets is influenced by investigators' choice of factors, encoding/categorization and transformation (including dimensionality reduction) of variables, and choice of statistical method. To investigate this hypothesis, we compared variations of HC and EFA, with respect to different encodings and subsets of symptoms, markers, and diagnoses studied in populations of children with asthma. We then related the clustering to physician-reported asthma severity, and also considered which of the original variables (apart from cluster memberships) best predicted severity.

## METHODS

## Study Population

Children aged 6-18 years were recruited from the Pediatric Asthma Clinic at the Hacettepe University, Ankara, Turkey. Parents were interviewed by a pediatrician using a modified ISAAC questionnaire (13) to ascertain information on symptoms and prescribed medications. Children completed skin tests, spirometry (14), and measurement of bronchodilator reversibility. Those with a negative reversibility test underwent either methacholine or exercise challenge test to measure airway hyperresponsiveness (15-17). Blood sample was collected for measurement of eosinophils and total serum IgE.

Asthma was defined as all three of the following: (1) physiciandiagnosed asthma, (2) current use of asthma medication, and (3) either bronchodilator reversibility or airway hyperresponsiveness (positive methacholine or exercise challenge test). Asthma severity was categorized into three ordinal categories (mild, moderate, and severe) using Global Initiative for Asthma guidelines (http://www.ginasthma.org/), based on the clinical features present and the patient's current step of the medication regimen.

## Variables Used

The following variables were used:
Asthma symptoms and exacerbations: Presence of asthma-related symptoms within the past 4 weeks, number of asthma exacerbations within the past year, and hospitalization for acute asthma (ever).
Interview-derived variables: Age, sex, age of asthma onset, physiciandiagnosed allergic rhinitis, conjunctivitis, urticaria and/or eczema, family history of asthma, and presence of smokers and pets or animals in the home.
Objective measurements: Height, weight, body mass index (BMI; standardized for age and growth and sex) (18), serum eosinophil number or percentage, and total serum IgE.
Medication usage: Use of short-acting $\beta_{2}$-agonists (SABA); inhaled corticosteroids (ICS), dose expressed as beclometasone-equivalent; long-acting $\beta_{2}$-agonists (LABA); and leukotriene receptor antagonist.
Lung function: \% predicted $\mathrm{FEV}_{1}, \mathrm{FVC}$, forced expiratory flow $\left(\mathrm{FEF}_{25-75}\right)$, and $\mathrm{FEV}_{1} / \mathrm{FVC}$ ratio.
Bronchodilator reversibility: Greater than or equal to $12 \%$ increase in $\mathrm{FEV}_{1}$ following administration of $200 \mu \mathrm{~g}$ of inhaled albuterol.
Airway hyperresponsiveness: Provocative concentration of methacholine causing a $20 \%$ decline in $\mathrm{FEV}_{1}\left(\mathrm{PC}_{20}\right)$ less than or equal to $8 \mathrm{mg} / \mathrm{mf}(16)$ or greater than or equal to $10 \%$ reduction in $\mathrm{FEV}_{1}$ following exercise challenge (17, 19-21).
Atopic sensitization: Wheal 3 mm greater than negative control to at least one allergen.

## Statistical Methods

Variables were encoded either as raw mixed types or categorized with equal-frequency binning and projected into binary dummy variables. No missing values were present, apart from the alternative measures of airway hyperresponsiveness. Variables with a relative frequency below $1 \%$
were excluded. We performed EFA both by means of multiple factor analysis and principal component analysis (22). To facilitate visualization of weightings on dimensions, variables were grouped together in terms of (1) lung function ( $\%$ predicted $\mathrm{FEV}_{1}, \%$ predicted FVC, $\mathrm{FEV}_{1} / \mathrm{FVC}$ ratio, $\mathrm{FEF}_{25-75}$, bronchodilator reversibility, airway hyperresponsiveness), (2) markers of severity or exacerbation (symptoms within the past 4 wk , number of attacks within the last year, hospitalization), (3) family history, (4) comorbidities and atopy (rhinitis, eczema, sensitization, \% eosinophils, total IgE); (5) environmental factors (exposure to tobacco smoke, pet ownership), (6) asthma medication (ICS, LABA, montelukast, and any combination), and (7) general characteristics (age, sex, BMI, age of onset of wheeze).

We applied different HC methods $(23,24)$ to the dataset, varying distance measures, linkage functions, feature selection $(22,25)$, and then identifying an optimal partition of the inferred trees (26). For control, a set of random trees and clusters was also created. All different variations of HC were mutually compared in a so-called "meta" HC , using the adjusted Rand index (27) and the Penny-Hendy index (28) as measures of trees and clusters similarity. Classical

TABLE 1. CHARACTERISTICS OF THE STUDY POPULATION ( $\mathrm{N}=383$ )


Definition of abbreviations: $\mathrm{BMI}=$ body mass index; $\mathrm{FEF}=$ forced expiratory flow; LABA $=$ long-acting $\beta_{2}$-agonists; SABA $=$ short-acting $\beta_{2}$-agonists.

Categorical variables are given as percentages, and numerical variables are given as median (interquartile range).

multidimensional scaling (29) was then applied to identify relations among different HC methods and deviations from randomization.

The predictive ability of clusters and of original variables with respect to asthma severity (dichotomized into mild vs. moderatesevere) was assessed through information gain ratio (which measures how much information is gained when a variable is known to approximate an outcome) (30), multivariable logistic regression, and Bayesian network analysis (31). Feature selection and network topology optimization were done by stepwise algorithms for both the logistic regression and Bayesian network analyses (32). Specifically, we fitted four logistic models with raw variables: Model 1 included all variables apart from those used to define severity (medication usage, symptoms within the past 4 wk , and $\mathrm{FEV}_{1}$ ); Model 2 included all variables; Model 3 was a stepwise selection of variables, adding or removing covariates heuristically based on the Akaike Information Criterion, from Model 1; and Model 4 was a stepwise selection of variables from Model 2. We then reran the logistic regressions, but using cluster memberships as variables. Model performance was assessed by repeated cross-validation and area under the receiver operating characteristic curve (24), which is a composite indicator of sensitivity and specificity. All analyses were performed
within the R (www.r-project.org/) and Weka (www.cs.waikato.ac.nz/ $\mathrm{ml} /$ weka/) software.

The online supplement provides additional details.

## RESULTS

## Study Population

The characteristics of the study population are shown in Table 1. The cross-sectional set comprised 383 children with asthma, median (interquartile range) age $9(8-12)$ years, age of asthma onset of $3(5-8)$ years, $60.6 \%$ boys, $25.3 \%$ classified as obese or overweight, $43.3 \%$ with physician-diagnosed allergic rhinitis, $36.0 \%$ exposed to tobacco smoke, all receiving SABA, $46.7 \%$ receiving additional asthma medication, $17.0 \%$ experiencing symptoms within the past 4 weeks, with total serum IgE of 144 (54-375) and $\mathrm{FEV}_{1} \%$ predicted of $89 \%$ (79-99). Asthma was classified as mild, moderate, or severe in $72.6 \%, 25.6 \%$, and $1.8 \%$ of cases, respectively.

TABLE 2. EIGENVALUES OF THE FIRST 10 COMPONENTS OF THE MULTIPLE FACTOR ANALYSIS AND CONTRIBUTION OF EACH VARIABLE IN THE DATASET TO EACH OF THESE COMPONENTS


Definition of abbreviations: $\mathrm{BMI}=$ body mass index; $\mathrm{FEF}=$ forced expiratory flow; $\mathrm{ICS}=$ inhaled corticosteroids; $\mathrm{LABA}=$ long-acting $\beta_{2}$-agonists; $\mathrm{SABA}=$ short-acting $\beta_{2}$-agonists.

## Exploratory Factor Analysis

The optimal solution from the multiple factor analysis presented five dominant dimensions (eigenvalues $\geqslant 1$ ) accounting for only $35 \%$ of the total variance of the data. Table 2 shows the eigenvalues of the first 10 dimensions and the correlation of each variable in the dataset to each of these dimensions. The correlation map of variables (Figure 1a) graphically illustrates the correlation of each individual variable with the first principal plane. The significant absolute correlations greater than 0.4 with given dimensions were as follows:

Dimension 1: Medication use (any drug apart from SABA, ICS), lung function (methacholine challenge and $\mathrm{FEV}_{1}$ ), age, and age of asthma onset

Dimension 2: Age, markers of atopy (IgE, \% eosinophils, sensitization), use of LABA, and $\mathrm{FEV}_{1} / \mathrm{FVC}$ ratio
Dimension 3: Rhinitis and environmental exposures (tobacco smoke, pets)
Dimension 4: Paternal atopy and tobacco smoke exposure
Dimension 5: $\mathrm{FEV}_{1}$ and asthma exacerbations within the past year

Figure 1b shows the coordinates of the imposed groups on the first and second dimensions ( $16 \%$ of variance explained). The plot illustrates that measures of lung function showed a correlation with both Dimensions 1 and 2, use of medication in addition to SABA and exacerbations with Dimension 1, and
![img-0.jpeg](img-0.jpeg)

Figure 1. (a) Principal coordinate plot from the multiple factor analysis. (b) Representation of the groups on the first and second dimensions. BMI $=$ body mass index; $\mathrm{FEF}=$ forced expiratory flow; $\mathrm{ICS}=$ inhaled corticosteroids; $\mathrm{LABA}=$ long-acting $\beta_{2}$-agonists; $\mathrm{SABA}=$ short-acting $\beta_{2}$-agonists.

general characteristics with Dimension 2. The principal component analysis gave a similar grouping of variables, but with some notable differences in the number of components and the coefficient sets (see online supplement). In summary, EFA yielded a low percentage of the variance explained and relatively weak components' characteristics.

## Hierarchical Clustering

We performed multiple inferences of HC trees by varying $(I)$ the encoding (e.g., binary vs. raw variables), (2) the distance-linkage function (e.g., Gower vs. Jaccard distance), and (3) the feature selection and dimensionality reduction space. This resulted in a total of 85 trees; we then generated an additional set of 42 random trees (i.e., ratio 2:1).

After identifying clusters, similarity matrices were calculated across all the trees and clusters. There was a clear difference between the trees inferred using the data compared with random trees. On average, real trees produced a lower number of clusters compared with random trees $(P=0.005)$. Real trees were more similar to each other than random trees ( $P<0.0001$ ); HC plots in Figure 2 (left) illustrate segregation between the real trees inferred from the data and the random trees, demonstrating that there is a clear signal in the data.

The variations of the HC method (in the linkage-distance functions) did not affect the cluster inference and yielded similar trees and clusters (Figure 2). However, using different variable encodings and transformations led to more pronounced differences in the clusters, with segregation among real trees.

## Prognostic Factors of Severity

After univariate analysis of the raw variables, we ranked them by the information gain ratio in relation to asthma severity (dichotomized into mild vs. moderate-severe) (Figure 3). The highest gain was that of lung function markers and the use of asthma medications in addition to SABA, followed by family history. We next performed multivariable analysis with raw variables (Table 3). Model 1 (in which we excluded $\mathrm{FEV}_{1}$, current asthma symptoms, and the step of the medication regime, which were used to categorize asthma severity), identified younger age, BMI, paternal asthma, and decreasing FVC and $\mathrm{FEV}_{1}$ / FVC ratio as variables consistently with higher log-odds of moderate-severe asthma. Model 2 (which included all variables) showed that use of asthma medication in addition to SABA (ICS, LABA, or montelukast), asthma symptoms within the last 4 weeks (trend, $P=0.06$ ), and lower $\mathrm{FEV}_{1}$ were significantly associated with moderate-severe asthma, with BMI, and lower FVC and $\mathrm{FEV}_{1} / \mathrm{FVC}$ ratio still yielding significant associations. Stepwise Models 3 and 4 selected younger age of asthma onset, lower FVC, $\mathrm{FEV}_{1} / \mathrm{FVC}$ ratio, and $\mathrm{FEF}_{25-75}$, as associates of moderate-severe asthma (besides medications, symptoms within the past 4 wk , and $\mathrm{FEV}_{1}$, which were used to define asthma severity). Logistic models using cluster memberships (obtained by HC) as covariates showed consistently worse goodness-of-fit than Models 1-4, both in terms of Akaike Information Criterion and cross-validation estimates using areas under receiver operating characteristic curves (see the online supplement).
![img-1.jpeg](img-1.jpeg)

Figure 2. Meta-hierarchical clustering (left) and classical multidimensional scaling (right) of different clustering methods, compared with randomized trees and clusters, using the adjusted Rand Index (upper) and Penny-Hendy tree distance (lower). Colors identify different variable encodings, and label replications represent different linkage and distances on the same encoding. The figure shows how there is a clear signal in the data (random trees are segregated from the data clusters), and that variations of the hierarchical clustering method (same color) yield similar trees and clusters (i.e., branching together in a subtree). However, different variable sets, encodings, and transformations lead to more pronounced differences in the clusters.

On deeper analysis using Bayesian network methods we saw a complex conditional structure of variables, which may indicate nonlinear relationships not captured by the logistic models. Figure 4 shows an optimal Bayesian network with these data, with casual dependencies inferred by stepwise algorithm.

## DISCUSSION

## Summary of Findings and Novelty of Approach

In a cross-sectional study of children with asthma we applied several dimension reduction and data clustering algorithms, associating components, clusters, and raw variables to asthma severity. We systematically explored the effects of varying the variable encodings (e.g., comparing continuous with discretized, or raw variables with those transformed using EFA) and the clustering methods (within HC we tested 85 different models). Changes in linkage and distance resulted in minor changes in the clusters, whereas the changes in the variable encodings and transformations made larger differences to the cluster assignments. Compared with the original raw variables, all of the inferred clusters correlated relatively poorly with asthma severity.

## Comparison with Previous Works and Interpretation

Several groups have previously applied different methods of clustering and dimensionality reduction on well-characterized populations of adults and children with asthma to identify patterns within the data. In adults, Moore and coworkers (6) identified five asthma clusters using HC (Ward linkage) of the data from 726 patients with severe asthma. Starting with greater than 600 variables, the data were reduced manually to 34 indicators covering a broad spectrum of routine assessments of asthma without missing data. A subsequent decision tree analysis showed that prebronchodilator and post-bronchodilator $\mathrm{FEV}_{1}$ and age of
onset of asthma were responsible for more than $80 \%$ of correct cluster assignments. Haldar and coworkers (7) used the same Ward HC plus a k-means partitioning clustering to infer and compare clusters in two distinct populations (mild-moderate and refractory asthma), validating the findings in a third population of refractory subjects with asthma. However, the variable choice and encoding were different: principal components analysis was performed on 16 variables, chosen among those "considered important in defining the disease phenotype rather than being a product of the disease process" (7) (for instance, post-bronchodilator $\mathrm{FEV}_{1}$ was not included). Differences among the cluster sets (three in the mild-moderate vs. four in the refractory asthma populations, two in common) for the two populations were discussed in relation to treatment strategies, driven by the role of inflammatory markers. Siroux and coworkers (8) applied latent class analysis on two adult cohorts ( $\mathrm{n}=641, \mathrm{n}=1,895$; 14 markers preprocessed by EFA, including demographics, lung function, and treatment types), showing a discriminatory value of treatment types, a certain degree of stability of inferred clusters (four in both populations, two of these common between the populations), and some resemblance to previous findings. Fitzpatrick and coworkers (9) applied Ward HC to a population of 161 children ( $>500$ variables reduced to 12 by expert advice), and identified four clusters that were highly discriminated by lung function markers, asthma duration, and the use of medications (these parameters were responsible for $93 \%$ of the correct cluster assignments). There was some, but not complete resemblance with previous clustering in adults (6), and the clusters had poor discriminating value with respect to asthma severity. Just and coworkers (10) recently identified two novel asthma phenotypes in children (using 19 variables selected by principal components analysis from the initial set of 40) in a three-groups clustering inferred by Ward HC plus a k-means partitioning clustering, focusing on the role of inflammatory markers.

# information gain ratio (+/- sd.err.) 

![img-2.jpeg](img-2.jpeg)

Figure 3. Univariate analysis. Information gain ratio (which measures the $\%$ of information gained to approximate the outcome when the variable was known) between single variables and disease severity (mild vs. moderate-severe asthma). $\mathrm{BMI}=$ body mass index; $\mathrm{FEF}=$ forced expiratory flow; ICS = inhaled corticosteroids; LABA $=$ long-acting $\beta_{2}$-agonists; SABA $=$ short-acting $\beta_{2}$-agonists.

TABLE 3. MULTIVARIABLE ANALYSIS OF THE RAW VARIABLE SET IN RELATION TO ASTHMA SEVERITY (MILD VS. MODERATE-SEVERE)




Definition of abbreviations: AIC $=$ Akaike Information Criterion; BMI $=$ body mass index; $\mathrm{CI}=$ confidence interval; $\mathrm{FEF}=$ forced expiratory flow; $\mathrm{ICS}=$ inhaled corticosteroids; LABA $=$ long-acting $\beta_{2}$-agonists; OR $=$ odds ratio; $\mathrm{Q} 1=1$ st quartile; $\mathrm{Q} 2=2 \mathrm{nd}$ quartile; $\mathrm{Q} 3=3 \mathrm{rd}$ quartile; $\mathrm{Q} 4=4 \mathrm{th}$ quartile; SABA $=$ short-acting $\beta_{2}$ agonists.
Logistic regression models: Model 1 excluded $\mathrm{FEV}_{1}$, symptoms within the last 4 weeks, and medication step as they were used to define severity; Model 2 included all variables; Model 3 and 4 were stepwise of 1 and 2 .
*Betamethasone-equivalent dosage.

In these previous studies of patients with asthma and in similar studies of atopy $(33,34), \mathrm{HC}$ seemed robust with respect to different linkage and distances, or by data bootstrapping. To
some extent, it was stable when considering data from different populations with similar variable sets and variable processing. However, our work highlights that the same does not hold when

![img-3.jpeg](img-3.jpeg)

Figure 4. Bayesian network model explaining dependencies between severity as diagnosed by the physician and the original variable space. Both network topology and variables have been selected by a stepwise search. BMI $=$ body mass index; $\mathrm{FEF}=$ forced expiratory flow; ICS = inhaled corticosteroids; LABA $=$ long-acting $\beta_{2}$-agonists.
systematically changing the variable sets and encodings, or when transforming the data (e.g., reducing dimensions by EFA), where topologies of trees and cluster sets differ substantially.

The results of our EFA show that there is a diversification of age, age at asthma onset, parental history of disease, environmental factors, lung function markers, exacerbation markers, and inflammatory markers. This diversification was highlighted in previous studies, both in adults (6-8) and children $(9,10)$. However, the stability of the components was weak, and less robust to changes in the model assumptions (like rotations) or variable discretization policies. The subsequent HC analysis also led to instability in inferred trees and clusters when changing the variable sets, encodings, and transformations.

These findings might be a characteristic exclusive of our study population. An aggregation bias caused by the discretization of skewed variables may play a role, and the use of mixed data types. One previous study (6) highlighted the importance of selecting variables with no missing values, of using normalized variables, and of selecting variable sets explaining the highest variance. Therefore, when asthma subgroups are identified through unsupervised learning, they must be subject to a careful interpretation of the original variable space and its transformations. We did not perform a discrimination analysis of the original variables with respect to each clustering, but this might help to select subsets of variables that lead to more stable clustering, even when varying their encoding.

Consistent with previous findings $(9,10)$, our HC yielded groups that were relatively poor predictors of asthma severity. This does not imply necessarily that clustering has a poor diagnostic value in general. Indeed, this finding suggests an important point that severe asthma as a phenotype of disease may not be directly associated with unique or uniform pathophysiologic mechanisms (i.e., that it is not a distinct asthma endotype), but likely a phenotypic characteristic at a severe end of the spectrum of a number of asthma subgroups.

When looking at the original variables, prognostic factors of moderate-severe asthma, besides the medication usage, current asthma symptoms, and $\mathrm{FEV}_{1}$, were paternal asthma, BMI, younger age of asthma onset, and other lung function parameters (FVC, $\mathrm{FEF}_{25-75}, \mathrm{FEV}_{1} / \mathrm{FVC}$ ratio). There was evidence of conditional dependence among variables from the Bayesian network analysis (Figure 4); however, given the high computational complexity of the model selection, the reliability of the
network (in terms of variables and relations) was limited by the heuristic procedure for variable selection, and could not be properly quantified.

## Methodologic Discussion

In ideal situations, for example with dimension-dense samples of data from normal distributions, different unsupervised learning methods may produce the same results. For instance, it has been demonstrated that the relaxed solution of the k-means clustering algorithm, specified by the cluster indices, is given by the principal components of the data (35). However, even with the same method, different results can be obtained if the analysis is performed with different starting values, or different optimization routines (e.g., using singular value rather than eigenvector decomposition, or using different starting points in k-means). The empirical robustness of a method can be assessed using multiple runs and/or bootstrapping; theoretic robustness, however, may remain debatable. A different case is the conceptual variation of a technique: for instance, in principal component analysis, the premax rotation relaxes the orthogonality assumption, whereas the varimax does not (principal components are guaranteed to be independent only if the dataset is jointly normally distributed).

Medicine often throws up high-dimensional, sparse, noisy data. In such situations, EFA may be applied before HC (36); however, this has been criticized for not being justified in the general case (37). Other approaches include model-based clustering (38). Witten and Tibshirani developed the sparcl technique for selecting features in clustering (25), which we used in this study. However, these enhanced methods are difficult to apply in medical research where the typically heterogeneous data (nonnormality, missing values, and mixture of numeric and categorical types) makes it more difficult to design distance metrics (39) or likelihood functions. In addition, different approaches may have different ways of identifying the optimal number of clusters by their internal measures (40) or external indices (41), in which case ensemble approaches (42) might be needed.

## Conclusions

Unsupervised statistical learning can help investigators to identify complex patterns and structures in data, and to reduce dimensionality to something conceivable. This interaction with

the data may in turn generate or shape novel hypotheses. However, the patterns used for hypothesis generation must be reliable. We have shown that clustering using different variable sets and encodings in asthma datasets can lead to different clusters. A more thoughtful selection of markers, encoded appropriately, and consistent across different populations is required before attempting unsupervised statistical learning. Then, careful interpretation of the variable space and its transformations are essential if true asthma subgroups are to be identified by interacting with data in this way.

Author disclosures are available with the text of this article at www.atsjournals.org.
