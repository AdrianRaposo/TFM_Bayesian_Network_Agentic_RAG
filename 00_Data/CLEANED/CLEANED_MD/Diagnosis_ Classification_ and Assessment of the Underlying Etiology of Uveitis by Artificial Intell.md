# Diagnosis, Classification, and Assessment of the Underlying Etiology of Uveitis by Artificial Intelligence: A Systematic Review 

Robin Jacquot ${ }^{1,2, *}$, Pascal Sève ${ }^{1,2}$ (D), Timothy L. Jackson ${ }^{3,4}$ (D), Tao Wang ${ }^{5}$ (D), Antoine Duclos ${ }^{2}$ and Dinu Stanescu-Segall ${ }^{6}$

check for updates

Citation: Jacquot, R.; Sève, P.; Jackson, T.L.; Wang, T.; Duclos, A.; Stanescu-Segall, D. Diagnosis, Classification, and Assessment of the Underlying Etiology of Uveitis by Artificial Intelligence: A Systematic Review. J. Clin. Med. 2023, 12, 3746. https://doi.org/10.3390/jcm12113746

Academic Editor: Gerard Espinosa
Received: 20 April 2023
Revised: 26 May 2023
Accepted: 27 May 2023
Published: 29 May 2023

## (0)

Copyright: (c) 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Department of Internal Medicine, Croix-Rousse Hospital, Hospices Civils de Lyon, Claude Bernard-Lyon 1 University, F-69004 Lyon, France; pascal.seve@chu-lyon.fr
2 Research on Healthcare Performance (RESHAPE), INSERM U1290, Claude Bernard Lyon 1 University, F-69000 Lyon, France; antoine.duclos@chu-lyon.fr
3 Department of Ophthalmology, King's College Hospital, London SE5 9RS, UK; t.jackson1@nhs.net
4 Faculty of Life Science and Medicine, King's College London, London SE5 9RS, UK
5 DISP UR4570, Jean Monnet Saint-Etienne University, F-42300 Roanne, France; tao.wang@univ-st-etienne.fr
6 Department of Ophthalmology, La Pitié-Salpêtrière Hospital, APHP, F-75013 Paris, France; dinustanescusegall@gmail.com

* Correspondence: robin.jacquot@chu-lyon.fr


#### Abstract

Recent years have seen the emergence and application of artificial intelligence (AI) in diagnostic decision support systems. There are approximately 80 etiologies that can underly uveitis, some very rare, and AI may lend itself to their detection. This synthesis of the literature selected articles that focused on the use of AI in determining the diagnosis, classification, and underlying etiology of uveitis. The AI-based systems demonstrated relatively good performance, with a classification accuracy of $93-99 \%$ and a sensitivity of at least $80 \%$ for identifying the two most probable etiologies underlying uveitis. However, there were limitations to the evidence. Firstly, most data were collected retrospectively with missing data. Secondly, ophthalmic, demographic, clinical, and ancillary tests were not reliably integrated into the algorithms' dataset. Thirdly, patient numbers were small, which is problematic when aiming to discriminate rare and complex diagnoses. In conclusion, the data indicate that AI has potential as a diagnostic decision support system, but clinical applicability is not yet established. Future studies and technologies need to incorporate more comprehensive clinical data and larger patient populations. In time, these should improve AI-based diagnostic tools and help clinicians diagnose, classify, and manage patients with uveitis.


Keywords: uveitis; diagnosis; etiology; decision support system; artificial intelligence; Bayes' theorem; algorithms

## 1. Introduction

Uveitis is an intraocular inflammation with a reported incidence of 17 to 52 per 100,000 people and a prevalence of $38-284$ per 100,000 [1]. It is the fifth leading cause of blindness worldwide, with vision loss most often mediated by macular edema, glaucoma, and retinal ischemia [2]. In 2021, the Standardization of Uveitis Nomenclature (SUN) system set out classification criteria for uveitis [3] based on anatomic location, onset, duration, course, and severity.

Uveitis is associated with approximately 80 different etiologies, the most common of which are infectious, autoimmune, or autoinflammatory [4]. The causal epidemiology can vary from country to country. For example, in some countries, genetic factors such as HLA-B27 are key, while in others, diseases such as sarcoidosis or infections such as tuberculosis may be over-represented. Hence, the epidemiological background of patients with uveitis is important in determining the underlying cause. In addition, ocular (anatomic

location, laterality, chronicity, and associated signs) and extraocular (clinical examination and systemic workup) features may help orient the diagnosis. The plethora of potentially relevant variables makes the etiological diagnosis complex [4,5]. In Western countries, onequarter of uveitis diagnoses are related to an isolated ophthalmic disease, one-quarter to a confirmed systemic disease, one-quarter to a suspected systemic disease, and in between $23 \%$ and $44 \%$ of cases, the cause remains undetermined, varying by center [6].

A small number of studies have focused on the best diagnostic approach for a given type of uveitis. Only one was a controlled study, comparing a "standardized 3-step approach" to an "open" strategy for investigation, with allocation based on simple ocular characteristics, namely the location and type of uveitis [7].

Because of these diagnostic complexities and a lack of strong evidence or consensus to guide diagnostic approaches, inexperienced or non-specialist clinicians may find uveitis a challenging condition to diagnose and classify. In recent years, machine learning and deep learning have shown increasing utility in the analysis, interpretation, and exploitation of mass data. In medicine, Bayesian belief networks have been proposed as a tool to assist in the differential diagnosis of medical conditions [8,9]. More recently, researchers applied this technique to the diagnosis of uveitis, with promising results [10,11]. Ophthalmological AI algorithms have been applied mainly in diabetic retinopathy screening, age-related macular degeneration, and corneal disease [12]. Most of these algorithms could be applied for uveitis ophthalmological exams. It would help to have a synthesis of the available literature and identify what further evidence is required.

This article aims to synthesize the literature on the use of AI in the diagnosis of uveitis, its classification, and its assistance in determining the underlying cause.

# 2. Materials and Methods 

### 2.1. Search Strategy and Selection Criteria

A systematic literature review was completed on 6 March 2023. The review followed the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) guidelines, and the protocol was registered in the International Prospective Register of Ongoing Systematic Reviews (PROSPERO) (ID: 409568) [13]. The search strategy was conducted across four electronic databases (PubMed, Cochrane, MEDLINE, and EMBASE). To capture all relevant articles, the following combination of terms and/or MESH headings were used: "uveitis", "algorithms", "artificial intelligence", "decision support system, clinical", and "Bayes Theorem". An example search in PubMed was (("uveitis" [MeSH Terms]) AND ("algorithms" [MeSH Terms] OR "artificial intelligence" [MeSH Terms] OR "decision support system, clinical" [MeSH Terms] OR "Bayes Theorem" [MeSH Terms])) (Table 1).

We included studies that reported the use of AI systems to determine any underlying etiology in patients with uveitis and/or as a tool to enhance the diagnosis or classification of uveitis. Meta-analyses, randomized controlled trials (RCTs), comparative and noncomparative clinical studies, systematic reviews, reviews, and consensus guidelines were potentially eligible. Single-case reports, animal studies, editorials, abstracts, and articles not written in English were excluded. The bibliographies of retrieved articles were searched for eligible studies. They were no limitations regarding the publication date.

Table 1. MESH terms used for PUBMED research.


# 2.2. Data Collection and Assessment 

The retrieved abstracts were reviewed by two independent readers (one senior uveitis specialist and one senior internal medicine specialist), and, from these, articles were selected for full review. Uncertainties were resolved via discussion with another reviewer. Then, the full text of all the selected articles was read to determine the eligibility and collect data.

### 2.3. Risk of Bias Assessment and Outcome Measures

The risk of bias and applicability were assessed for primary diagnostic accuracy studies using the QUADAS-2 tool but not for secondary research (systematic reviews, reviews, and consensus guidelines) [13]. In the anticipated absence of many or any RCTs, we did not plan to undertake a meta-analysis or to pre-define any quantitative outcome measures, but rather, we aimed to synthesize and describe the available literature and identify areas for further research.

## 3. Results

### 3.1. Study Selection, Characteristics, and Risk of Bias

We reviewed 106 abstracts, of which 56 articles were selected for full review (Figure 1). Of these, 24 were eligible for inclusion. These comprised 2 RCTs, 12 comparative clinical studies, 2 non-comparative clinical studies, 1 review, and 7 diagnostic accuracy studies. The articles detailing primary research included a total of 15,917 patients in 23 articles. The risk of bias was determined to be high in eight articles, low in nine articles, and unknown in seven articles. The risk of bias and applicability were determined for each study (Figure 2).

### 3.2. Diagnosis

### 3.2.1. Anterior Segment

AI has been applied to medical imaging to assist with the diagnosis of uveitis. Researchers have demonstrated that AI-based analysis of anterior segment (AS) optical coherence tomography (OCT) images compared to a clinical examination with a slit lamp shows a significant and independent correlation with SUN classification for quantifying AS inflammation [15-21]. AS inflammation was detected by the identification of hyperreflective spots, which are then used as a representative for the AS. Agarwal et al. have shown a good correlation for hyperreflective spot count between automated and manual

methods (Pearson coefficient for grade 1: 0.995, grade 2: 0.948, grade 3: 0.985, and grade 4: 0.893). There were no significant differences in mean values between the two methods except for grade 4. In this case, the automated method was more sensitive and detected a higher number of cells [15]. Similarly, Sorkhabi et al. have developed an automated AI-based method to quantify inflammation in the AS. They showed a significant correlation between clinical SUN grading and AI software-detected particle count (Spearman $p=0.7077$ ) and particle density (Spearman $p=0.7035$ ). AI-based image analysis of AS-OCT slides shows a significant and independent correlation with clinical SUN assessment [16]. Sharma et al. applied an automated algorithm to count the number of hyperreflective spots by AS spectral-domain OCT. The Spearman correlation coefficient was 0.967 between OCTs and clinical slit lamp evaluation. Interestingly, Ozer et al. suggested that the iris pigment optical density measured at the pupillary margin of spectral-domain OCT could be a marker of Fuch's heterochromic uveitis [22].
![img-0.jpeg](img-0.jpeg)

Figure 1. PRISMA flow diagram.

![img-1.jpeg](img-1.jpeg)

Figure 2. Risk of bias and applicability concerns table (QUADAS-2) [14]. Legend: Red (-) = high risk of bias; Yellow (?) = unknown risk of bias; Green ( + ) = low risk of bias [3,10,11,15,16,17,18,19,20,21,22,23,24,25].

### 3.2.2. Vitreous Segment

The current gold standard for the quantification of vitreous inflammation, as recommended by the SUN working group, is clinical examination with an indirect ophthalmoscope, compared to a set of standard photographs. Several authors have suggested that macular OCT scans can offer greater reliability and accuracy by measuring the vitreous intensity [23,24,25]. Keane et al. provided a measurement of the vitreous signal intensity, which was then compared with that of the retinal pigment epithelium, generating an optical density ratio. These OCT-derived measurements showed a significant and positive correlation with clinical vitreous haze scores (r = 0.566) and a good degree of intergrader reproducibility (95% limit of agreement) [23]. Furthermore, Terheyden et al. suggested that 3 OCT b-scans might be sufficient to obtain a reliable automatic measurement of vitreous

intensity [25]. Passaglia et al. designed an image-processing algorithm and compared computer scores against clinicians' vitreous haze grading. Exact agreement between the algorithm and expert clinicians' grades had a kappa value of 0.61 [26].

# 3.2.3. Posterior Segment 

Choroidal vascularity was used by Agrawal et al. to quantify choroidal inflammation [27]. They defined the choroidal vascularity index (CVI) as the proportion of the intraluminal subfoveal choroidal area to the total circumscribed subfoveal choroidal area in enhanced-depth imaging OCT. This was achieved by manually segmenting the choroid with custom software after processing it with ImageJ. They showed a $6.2 \%$ decrease in CVI between the time of uveitis diagnosis and 3-month follow-up, which was significantly higher than the $0.7 \%$ CVI decrease in control eyes. As such, CVI has potential as a novel tool for monitoring the clinical course of posterior uveitis, panuveitis, and choroidal disease.

McKay et al. proposed to identify and quantify inflammatory choriocapillaris lesions from automated swept-source OCT [28]. The algorithm demonstrated a high degree of agreement with human graders in the determination of lesion area, spatial overlap, and reproducibility. Chu et al. used similar methods to detect choriocapillaris flow attenuation, with significantly larger areas of flow attenuation in patients with posterior uveitis than uveitis with no posterior involvement [29].

Automated detection and quantification of macular edema already exist in neovascular age-related macular degeneration, diabetic retinopathy, and retinal vein occlusion [30,31,32]. Therefore, it could be applied to macular edema caused by uveitis, although intraocular inflammation could potentially obscure retinal structures [36]. Schmidt et al. and Moraes et al. applied a deep learning method for the localization and quantification of fluid in the retina using OCT scans, with promising results in neovascular age-related macular degeneration $[32,36]$.

The potential utility of these advances is that AI may be able to minimize inter-observer variability and thereby facilitate more appropriate patient follow-up scheduling. It may also be able to assist, or conceivably even replace, clinicians' classification of uveitis, and thereby triage severity. By identifying less severe cases, AI could provide ophthalmologists with more time to focus on sight-threatening diseases [37]. However, to date, none of these tools have been applied in clinical practice, and their impact on real-world diagnosis, treatment, and optimization of the clinical workflow needs to be evaluated by prospective, and ideally comparative, clinical studies.

### 3.3. Classification

AI has also been used in uveitis to process non-imaging clinical data. The SUN working group used AI to classify uveitis into 25 of the most common categories. First, they collected 4046 cases of uveitis from multiple uveitis centers on 5 continents with about 100-200 cases per entity, with the ground truth based on supermajority clinical agreement. Cases were split into a training set ( $\sim 85 \%$ of the cases) and a validation set ( $\sim 15 \%$ of the cases). Machine learning techniques through multinominal logistic regressions were then used within each uveitis subclass to classify patients with uveitis. The results with required and exclusion criteria showed a high degree of accuracy, ranging from $93.3 \%$ to $99.3 \%$ agreement, and appeared to perform well enough for use in clinical and translational research [3]. The final criteria of the 25 uveitic entities were later published.

Limitations include the lack of an external validation set, and in terms of clinical applicability, about half of the patients had a disease for which no SUN classification criteria existed [38]. Demographic data and bias assessment were not available in those papers, along with applied models and data that were not publicly available. There are, as of yet, no prospective or comparative studies detailing how the system performs in clinical practice.

# 3.4. Etiology 

How one approaches the workup of patients with uveitis may determine how technology can assist in the process. An algorithmic approach to uncovering any underlying etiology may be the most efficient [39]. Such a systematic approach typically starts with history taking and demographics (age, gender, race, and socio-economic history). Secondly, the characteristics of ocular examination are considered (chronology, laterality, anatomical location, corneal changes, intraocular pressure, granulomatous changes, and the presence of synechiae, retinal vasculitis, papillary edema, macular edema, and focal or multifocal choroiditis and retinitis). Thirdly, the physical signs of extraocular disease can point to an underlying etiology. Given the potential benefits of a systematic approach, several AI algorithms have been designed to work with the resulting clinical data flow (Table 2).

Table 2. Review of algorithm approach for etiological diagnosis of uveitis and their diagnostic performance.


In 2016, Gonzalez-Lopez et al. reported the results of a Bayesian belief network algorithm designed to help diagnose the cause of anterior uveitis [10]. The center node of the Bayesian network was the uveitis etiology ( 11 etiologies: idiopathic; ankylosing spondylitis; psoriatic arthritis; reactive arthritis; inflammatory bowel diseases; sarcoidosis; tuberculosis; Behçet disease [BD]; Posner-Schlossman syndrome; juvenile idiopathic arthritis; and Fuchs heterochromic cyclitis). Chance nodes included demographic data (gender), ophthalmic data (ocular symptoms and signs), extraocular data (systemic signs and symptoms), and laboratory findings, with a retrospective collection. In a dataset of 200 patients, the etiology (determined by the senior expert clinician) matched the first or second most likely diagnosis

given by the algorithm in about $80.5 \%$ of cases. Interestingly, the algorithm was more useful for the exclusion of certain etiologies thanks to its high specificity ( $88.8 \%$ for sarcoidosis and $99.5 \%$ for Posner-Schlossman syndrome). The limitations of this algorithm were the absence of important conditions (syphilis, multiple sclerosis, and herpetic uveitis) and retrospective data collection.

In 2019, Mutawa et al. introduced a multilayered rule-based expert system to serve as a decision-making support system [33]. This medical expert system consisted of long-term memory, short-term memory, an inference engine, and a possible extra module for providing explanations. The system was tested on 61 cases, and the authors reported perfect agreement with human experts on each occasion. Indeed, the algorithm reported a match of $60.8 \%$ for all tested cases, overmatch (correct diagnosis among a list of probable diagnoses) in $39.2 \%$, and no mismatch. However, in such cases, further investigations such as laboratory tests, would be necessary to exclude mimicking diseases. Furthermore, the sample size was limited, which may have affected the algorithm's performance and generalizability.

Tugal-Tuktun et al. developed an algorithm for the diagnosis of uveitis associated with BD [34]. Firstly, they defined 10 ocular signs with a high diagnostic ratio for BD among 418 patients with uveitis ( 211 with BD and 207 with other uveitides). Secondly, they developed an algorithm using classification and regression tree analyses based on recursive partitioning analysis, applied to prospective data with a high-scoring tree re-evaluated for clinical relevance. The expert-guided diagnostic tree provided an area under the curve (AUC) of $0.92(95 \% \mathrm{CI}, 0.89-0.96)$, but this study was focused only on a single etiology.

Most recently, Jamilloux et al. used a Bayesian belief network on a dataset composed of 877 incident uveitis cases to identify the etiology (center node) [11]. Variables included age, gender, ethnicity, and the anatomic and clinical characteristics of the uveitis. To assess the algorithm performance, internal (by Monte Carlo cross-validation) and external validations were carried out. Network performance was quantified in terms of the proportion of patients correctly classified. Performance indicators were estimated for the most and the two most probable diagnoses. When the algorithm's two most probable diagnoses were considered, they reported $80 \%$ agreement with the clinical diagnosis in the training dataset, confirmed at $85 \%$ in the independent validation set. Limitations of this study were collection from just one tertiary care center, which may affect generalizability to other centers and settings, and the risk of bias from retrospective data collection.

Two web-based diagnostic decision support systems (DDSSs) have been reported [35,40]. The first, Uveitis Doctor (Lara-Medina, Alcazar de San Juan, Spain), comprises more than 59 uveitis syndromes and an inference engine based on decision trees. The second, Uvemaster, contains a knowledge base of 88 uveitis syndromes acquired from the medical literature data, each comprising 76 clinical items. Each clinical sign was assigned a value of 0 to 100 , depending on its prevalence for each specific uveitis syndrome. Then, the interference engine combines the filtering rules with the patient dataset in order to offer possible diagnoses with diagnostic performance indicators (sensitivity, specificity, or positive predictive value). Performance was assessed as the percentage of cases for which a specific diagnosis was obtained using the app. In a series of 228 patients, the diagnostic accuracy of the algorithm was $96.6 \%$, and when the first diagnoses proposed by the app were considered, the sensitivity was $73.9 \%$ and the positive predictive value was $29.5 \%$. Helpfully, it incorporates ophthalmic, demographic, and clinical data in the dataset, but there are relatively few cases reported relative to the number of potential causes.

These apps may improve the clinical management of uveitis by offering potential diagnoses and reducing the number of cases labeled as idiopathic uveitis. However, the knowledge base includes diagnoses with very high specificity tests and ophthalmic diagnoses that can usually be easily recognized. This could lead to an overestimation of the algorithm's diagnostic performance, where results are extrapolated to other situations.

All these systems had acceptable or good performance, especially when the two most likely diagnoses were sought. However, the most common etiologies were considered in

three of the systems, and it is not yet known how they will perform with rarer or more complex etiologies.

# 4. Discussion 

In this systematic review, we summarize the contribution of AI in the diagnosis, classification, and assessment of the underlying etiology of uveitis. However, there are significant limitations in many studies, and the interpretation of results should be within these limitations. First, the design of the studies concerning uveitis diagnosis does not lead to high-level evidence recommendations, with only two randomized controlled trials. Before use in daily practice, we suggest that future studies test these AI-based image analyses for the diagnosis of uveitis in studies with higher methodological quality. Second, the validation of algorithms developed to assist clinicians in the assessment of the underlying etiology of uveitis was carried out on the test cohort in the majority of diagnostic accuracy studies. Only one used an external validation cohort, but both cohorts (test and validation) contained uveitis patients from the same country (France). This limits the international implementation of these algorithms, especially because of the heterogeneity of the uveitis causes between countries related to environmental influence.

Uveitis is an important ophthalmic disease worldwide, with multiple etiologies, a wide variation in its presentation, and a potentially complex differential diagnosis. This can lead to excessive testing and costs, delays in initiating the correct treatment, and a lack of clear information for patients. Any tools that enhance diagnostic accuracy and efficiency may therefore help optimize the management of patients with uveitis. Computer-aided systems may enhance diagnostic performance because of their greater capacity to process, compare, and summarize clinical data. They have shown potential in the diagnosis of uveitis, its classification, and in determining the underlying cause. McKay et al. have shown, using a Bayesian approach, that failure to consider all of the patient's relevant characteristics reduces the ability to determine the underlying etiology and leads to overdiagnosis, greater cost to the healthcare system, and overtreatment [41]. Accordingly, existing algorithms may be improved by incorporating new demographic elements (e.g., ethnicity), additional ophthalmic variables (e.g., the existence of papilledema or focal or diffuse choroiditis), detailed clinical examination findings (e.g., oral aphthosis and arthralgias), and paraclinical data (e.g., laboratory tests and organ biopsy). Increasing the number of patients is also important. An AI system that incorporates these extra data and that is developed and tested in large patient numbers may facilitate individualized patient management by improving diagnostic accuracy (especially for non-expert clinicians). This will provide rapid and more targeted therapy as well as extend the reach of AI to more complex and rare diagnoses.

For this purpose, the evidence base needs to be improved, as, currently, there are few comparative studies and no relevant RCTs. To this aim, patient populations should be well characterized and described and the methodology should be accurately described, and the use of shared outcome measures (Table 3) will facilitate meta-analyses and a comparison between technologies.

Table 3. Suggested outcome metrics for reporting outcomes of diagnostic decision support systems in uveitis.


Table 3. Cont.


# 5. Conclusions 

AI algorithms show promising results to help clinicians in the diagnosis of uveitis, in its classification, and in determining the underlying cause. Future studies should aim to establish not only the diagnostic accuracy of new technologies but also that they enhance clinical and health economic outcomes in comparison with the standard of care. The inclusion of other etiologies of uveitis and more comprehensive data through collaborative research and data sharing seems essential to carry out well-designed, adequately powered RCTs.

Author Contributions: Conceptualization, R.J., D.S.-S., P.S. and T.W.; methodology, R.J., T.L.J., A.D. and D.S.-S.; writing-original draft preparation, R.J.; writing-review and editing, R.J., P.S., D.S.-S., A.D., T.L.J. and T.W.; supervision, P.S. and D.S.-S.; project administration, A.D. and P.S. All authors have read and agreed to the published version of the manuscript.
Funding: This research received no external funding.
Conflicts of Interest: The authors declare no conflict of interest.
