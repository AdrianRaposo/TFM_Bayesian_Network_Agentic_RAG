# Intravascular imaging-guided versus angiography-guided percutaneous coronary intervention: a systematic review and bayesian network meta-analysis of randomized controlled trials 

Ahmed Mazen Amin ${ }^{1}$, Yehya Khlidj², Mohamed Abuelazm³, Ahmed Sayed ${ }^{4,11}$, Ubaid Khan ${ }^{5}$, Mariam Mahmoud Elewidi ${ }^{3}$, Mohammad Tanashat ${ }^{6}$, Hesham Elharti ${ }^{3 *}$, Mohamed Hatem Ellabban ${ }^{7}$, Abdullah K. Alassiri ${ }^{8}$, Mohamad Alsaed ${ }^{9}$, Basel Abdelazeem ${ }^{10}$ and Akram Kawsara ${ }^{10}$


#### Abstract

Background Percutaneous coronary intervention (PCI) has become one of the most commonly performed interventional life-saving procedures worldwide. Intravascular Imaging (intravascular ultrasound (IVUS) and optical coherence tomography (OCT)) have initially evolved to guide PCI compared with angiography. However, this technology is not universally employed in all PCI procedures, and there is ongoing controversy regarding its additional benefits to patient outcomes. We aim to estimate the efficacy and safety of imaging modalities during PCI, allowing pre-, per, and post-intervention assessment of coronary vascularization.


Methods A systematic review and Bayesian network meta-analysis of randomized controlled trials (RCTs), which were retrieved from PubMed, WOS, SCOPUS, EMBASE, and CENTRAL through September 2023. We used R, version 4.2.0. Effect sizes will be presented as odds ratios with accompanying $95 \%$ credible intervals. PROSPERO ID: CRD42024507821.
Results Our study, encompassing 36 RCTs with a total of 17,572 patients, revelead that compared to conventional angiography, IVUS significantly reduced the risk of major adverse cardiovascular events (MACE) (OR: 0.71 [95\% Crl: 0.56 to 0.87]) but not OCT (OR: 0.91 [95\% Crl: 0.62 to 1.39]), IVUS and OCT significantly reduced the risk of cardiac death (OR: 0.50 [95\% Crl: 0.33 to 0.76]) and (OR: 0.55 [95\% Crl: 0.31 to 0.98]), respectively, IVUS significantly reduced the risk of target vessel-related revascularization (OR: 0.60 [95\% Crl: 0.48 to 0.75]) but not OCT (OR: 0.86 [95\% Crl: 0.60 to 1.19]), IVUS and OCT significantly reduced the risk of stent thrombosis (OR: 0.50 [95\% Crl: 0.28 to 0.92]) and (OR: 0.48 [95\% Crl: 0.22 to 0.98]), respectively, IVUS significantly reduced the risk of re-stenosis (OR: 0.65 [95\% Crl: 0.46 to 0.88]) but not OCT (OR: 0.55 [95\% Crl: 0.15 to 1.99]), neither IVUS (OR: 0.97 [95\% Crl: 0.71 to 1.38]) nor OCT (OR: 0.75 [95\% Crl: 0.49

[^0]
[^0]:    *Correspondence:

    Hesham Elharti
    hisham_M30898424@med.tanta.edu.eg
    Full list of author information is available at the end of the article

to 1.22]) were associated with statistically significant reductions in all-cause mortality, neither IVUS (OR: 0.70 [95\% Crl: 0.45 to 1.32]) nor OCT (OR: 0.81 [95\% Crl: 0.47 to 1.59]) were associated with statistically significant reductions in target vessel failure, neither IVUS (OR: 0.88 [95\% Crl: 0.43 to 2.44]) nor OCT (OR: 0.81 [95\% Crl: 0.37 to 2.04]) were associated with statistically significant reductions in target lesion failure, and neither IVUS (OR: 0.82 [95\% Crl: 0.60 to 1.06]) nor OCT (OR: 0.84 [95\% Crl: 0.59 to 1.19]) were associated with statistically significant reductions in myocardial infarction.

Conclusion Intravascular imaging-guided, including IVUS and OCT, improved the postinterventional outcomes of PCI, notably suggesting their advantage over traditional angiography with no significant difference between IVUS and OCT.

Keywords Intravascular ultrasound, Optical coherence tomography, Angiography, Coronary artery disease, Percutaneous coronary intervention

## Introduction

Percutaneous coronary intervention (PCI) has become one of the most commonly performed interventional life-saving procedures worldwide. It is now the dominant method for coronary revascularization, allowing pre-, per, and post-interventional assessment of coronary vascularization [1]. Yet, it has a few disadvantages in efficacy, such as the 2D aspect of the angiographic views and the inability to precisely measure the stenosis due to the X-ray source, the image intensifier, and the chemical properties of the cinefilm [2, 3]. Moreover, it is exposed to several safety risks related to its radiologically invasive nature and the chemotoxic or anaphylactoid effects of the iodinated contrast product [4].

Two primary modalities are currently being evaluated as adjunctive tools for PCI, including intravascular ultrasound (IVUS) and optical coherence tomography (OCT). IVUS has the advantage of providing detailed guidance on PCI at the pre-interventional time by characterizing the nature of the atherosclerotic plaque and the mechanism of stenosis along with thrombotic plaque morphology, lesion length, and reference vessel diameter. Moreover, it has a post-interventional advantage by assessing coronary stent implantation results, including minimal stent area and expansion [5]. These benefits had clinical implications as the use of IVUS guidance during PCI was correlated with a significant reduction in the risk of 3-year target lesion failure, medium-term mortality, and target vessel revascularization [6, 7]. Additionally, registry-based data revealed reduced flow-impairing coronary dissection rates among patients undergoing PCI with IVUS on an elective basis [8]. On the other hand, OCT produces a more sophisticated visualization of the coronary artery wall and microstructures via nearinfrared light to produce high-definition, cross-sectional 3D volumetric images [9]. It has a shorter wavelength compared to IVUS ( $1.3 \mu \mathrm{~m}$ vs. $-40 \mu \mathrm{~m}$ at 40 MHz ), which allows greater axial resolution ( $10-20 \mu \mathrm{~m}$ versus $50-150 \mu \mathrm{~m}$ ) [9]. Indeed, real-world data showed that OCT optimized PCI outcomes, particularly during the complex left main and bifurcation lesions [10]. It further
revealed reduced risks of major adverse cardiovascular events (MACE), myocardial infarction, or repeat revascularization when PCI is assisted by OCT [11].

However, the superiority of OCT-guided PCI or IVUS to angiography-guided PCI remains uncertain, especially with continuously updated evidence. In this systematic review and meta-analysis, we examined the available data from randomized controlled trials (RCTs), comparing the efficacy and safety of PCI directed by OCT, IVUS, or angiography.

## Methodology

## Protocol registration

We prospectively registered this network meta-analysis in the International Prospective Register of Systematic Reviews (PROSPERO) under ID: CRD42024507821. We conducted this network meta-analysis in accordance with the PRISMA and PRISMA NMA statement guidelines for systematic reviews and meta-analysis [12, 13] and the Cochrane Handbook for Systematic Reviews and MetaAnalysis guidelines [14].

## Data sources \& search strategy

We systematically searched the following databases: Web of Science, SCOPUS, EMBASE, PubMed, and Cochrane Central Register of Controlled Trials (CENTRAL) up to September 2023. The detailed search strategy and results are shown in (Table S1).

## Eligibility criteria

We included RCTs with the following PICO criteria: population (P): Patients undergoing PCI; intervention (I): IVUS or OCT; control (C): coronary angiography; and outcomes (O): primary outcomes: major adverse cardiovascular events (MACE), while our secondary outcomes included: all-cause mortality, cardiac death, target vessel failure, target lesion failure, myocardial infarction, any revascularization, target vessel revascularization, stent thrombosis, CABG, and restenosis. Single-arm, observational studies, abstracts, and non-randomized trials were excluded.

## Study selection

After duplicates removal using Covidence software, six investigators (U.K. M.T. H.E. M.M.E. M.E. and A.K.E.) independently assessed the titles and abstracts of the retrieved records. Then, they screened the full texts in accordance with the previously mentioned eligibility criteria. Any disagreements were resolved via discussion.

## Data extraction

Using an Excel sheet, six reviewers (U.K. M.T. H.E. M.M.E. M.E. and A.K.E.) independently extracted summary characteristics of the included studies (study design, countries, total participants, intervention details (IVUS, OCT, and coronary angiography), MACE definition, follow-up period, and primary outcome), patients baseline characteristics (number of patients in each group, mean of age, male percentage, body mass index (BMI), left ventricular ejection fraction (LVEF), and comorbidities), and efficacy sheet (MACE, all-cause mortality, cardiac death, target vessel failure, target lesion failure, myocardial infarction, any revascularization, target vessel revascularization, stent thrombosis, CABG, and restenosis). Any disagreements were resolved through discussion.

## Risk of bias and certainty of evidence

Using the revised Cochrane collaboration's tool for assessing the risk of bias in randomized trials (ROB 2) [15], six reviewers (U.K. M.T. H.E. M.M.E. M.E. and A.K.E.) independently assessed the included RCTs for risk of bias in domains that include the randomization process, deviations from intended interventions, missing outcome data, measurement of the outcome, selection of the reported result, and overall bias. Any disagreements were resolved via discussion.

## Statistical analysis

We conducted a Bayesian network meta-analysis using the “bnma” package on R, version 4.2.0. We will use a random-effects model to account for between-study variation in treatment effects for outcomes reported by a sufficient number of studies. We primarily described heterogeneity using tau, an absolute measure that represents the standard deviation of treatment effects across studies. Effect sizes were presented as odds ratios with accompanying 95% credible intervals. A league table was constructed to compare all treatments, and the Surface Under the Cumulative Ranking Area (SUCRA) provides a single-number summary. Additionally, we performed a frequentist sensitivity analysis to ensure that the robustness of our findings was not sensitive to the statistical framework adopted. This analysis was performed using both random-effects and fixed-effect models to ensure that our findings were robust to the approach to heterogeneity. Funnel plots were used to assess publication bias. When the number of studies permitted (minimum of 10), we formally assessed funnel plot asymmetry using Egger's test (a linear regression test of asymmetry).

## Results

### Search results and study selection

Our search strategy resulted in 6,411 records from the previously mentioned databases. After removing duplicates, 4,405 records were included in the title and abstract screening, followed by 137 records in full-text screening. Finally, 41 publications (36 main records of the RCTs and five follow-up papers of some of the included RCTs) were included in our network meta-analysis (Fig. 1).

### Characteristics of included studies

Forty-one records (36 RCTs) were included [16--56], with 17,572 patients included, of whom 6,523 patients were in the IVUS group, 4,157 patients in the OCT group, and 6,892 patients in the coronary angiography group. A total of 21 RCTs compared IVUS with angiography [16, 18, 19, 22--24, 28--30, 33, 35--37, 40, 42--44, 46, 47, 49--52, 54--56], 12 RCTs compared OCT with angiography [16, 17, 21, 25, 26, 28, 31, 34, 38, 39, 48, 50, 53], and six RCTs compared IVUS with OCT [16, 20, 27, 28, 32, 41, 50]. Summary RCTs characteristics and baseline characteristics of the participants are shown in (Tables 1 and 2).

### Risk of bias and certainty of evidence

ROB 2.0 assessment showed that 15 RCTs had an overall low risk of bias; however, 21 RCTs had some concerns due to concerns about the randomization process, deviations from the interventions, and selection of the reported results (Fig. 2).

### Primary outcome: MACE

Pooling 22 RCTs [16, 18, 19, 21--26, 28--32, 35, 39, 40, 43, 46, 47, 49, 50, 52, 54, 56], compared to conventional angiography, IVUS significantly reduced the risk of MACE (OR: 0.71 [95% CrI: 0.56 to 0.87]). Although rates of MACE were numerically lower with OCT compared to conventional angiography, this did not reach statistical significance (OR: 0.91 [95% CrI: 0.62 to 1.39]) (Fig. 3; Table 3). Based on the SUCRA analysis, IVUS had the highest probability of reducing revascularization (94.1%), followed by OCT (40.2%) and angiography (15.7%) (Fig. 4).

### Secondary outcomes

### All-cause mortality

Pooling 26 RCTs [16--21, 24, 26--30, 32, 33, 36--43, 47, 48, 50, 51, 53--56], neither IVUS (OR: 0.97 [95% CrI: 0.71 to 1.38]) nor OCT (OR: 0.75 [95% CrI: 0.49 to 1.22]) were associated with statistically significant reductions in all-cause mortality compared to conventional angiography

![img-0.jpeg](img-0.jpeg)

Fig. 1 PRISMA flow chart of the screening process
(Fig. 3; Table 3). Based on the SUCRA analysis, OCT had the highest probability of reducing all-cause mortality ( $87.9 \%$ ), followed by IVUS ( $36.5 \%$ ) and angiography $(25.6 \%)$ (Fig. 4).

## Cardiac death

Pooling 22 RCTs [16-19, 21-23, 25, 27-30, 32, 33, 35, $39,41,46,47,49-53,55,56]$, compared to conventional angiography, IVUS significantly reduced the risk of cardiac death (OR: 0.50 [ $95 \%$ CrI: 0.33 to 0.76 ]), as did OCT (OR: 0.55 [95\% CrI: 0.31 to 0.98]) (Fig. 3; Table 3). Based on the SUCRA analysis, IVUS had the highest probability of reducing cardiac death ( $80.4 \%$ ), followed by OCT ( $68.4 \%$ ) and angiography ( $1.1 \%$ ) (Fig. 4).

## Target vessel failure

Target-vessel failure was defined as death from cardiac causes, target-vessel myocardial infarction, or ischemiadriven target-vessel revascularization. Upon pooling six RCTs [16, 17, 27, 28, 32, 33, 51, 55], neither IVUS (OR: $0.70[95 \% \mathrm{CrI}: 0.45$ to 1.32]) nor OCT (OR: 0.81 [ $95 \% \mathrm{CrI}$ : 0.47 to 1.59]) was associated with statistically significant reductions in target vessel failure compared to conventional angiography (Fig. 3; Table 3). Based on the SUCRA analysis, IVUS had the highest probability of reducing target vessel failure ( $80.7 \%$ ), followed by OCT ( $55.0 \%$ ) and angiography ( $14.3 \%$ ) (Fig. 4).

Table 1 Summary characteristics of the included RCTs

Table 2 Baseline characteristics of the participants

Target lesion failure was defined as death from cardiac causes, target-vessel myocardial infarction, or ischemiadriven target-lesion revascularization. Upon pooling four RCTs [16, 17, 27, 28, 51, 55], neither IVUS (OR: 0.88 [95% CrI: 0.43 to 2.44]) nor OCT (OR: 0.81 [95% CrI: 0.37 to 2.04]) was associated with statistically significant reductions in target lesion failure compared to conventional angiography (Fig. 3; Table 3). Based on the SUCRA analysis, OCT had the highest probability of reducing target lesion failure (66.4%), followed by IVUS (51.5%) and angiography (32.1%) (Fig. 4).

### Myocardial infarction

Pooling 27 RCTs [16--21, 24--30, 32, 33, 35--38, 40--43, 46--50, 52, 56], compared to conventional angiography, neither IVUS (OR: 0.82 [95% CrI: 0.60 to 1.06]) nor OCT (OR: 0.84 [95% CrI: 0.59 to 1.19]) was associated with statistically significant reductions in myocardial infarction (Fig. 3; Table 3). Based on the SUCRA analysis, IVUS had the highest probability of reducing myocardial infarction (75.0%), followed by OCT (64.1%) and angiography (10.9%) (Fig. 4).

### Any revascularization

Any revascularization is defined as any repeat revascularization (PCI or coronary artery bypass grafting). Upon Pooling 12 RCTs [16, 17, 19--21, 27, 28, 33, 35--37, 41, 48, 54], neither IVUS (OR: 0.87 [95% CrI: 0.63 to 1.22]) nor OCT (OR: 0.92 [95% CrI: 0.67 to 1.28]) were associated with statistically significant reductions in any revascularization compared to conventional angiography (Fig. 3; Table 3). Based on the SUCRA analysis, IVUS had the highest probability of reducing any revascularization (70.6%), followed by OCT (54.4%) and angiography (25.0%) (Fig. 4).

### Target-vessel-related revascularization

Target-vessel-revascularization was defined as a target vessel requiring any repeat revascularization (PCI or coronary artery bypass grafting). Upon pooling 18 RCTs [16--19, 21, 27--30, 32, 33, 35--38, 41, 47, 48, 51, 52, 55, 56], compared to conventional angiography, IVUS significantly reduced the risk of target-vessel-related revascularization (OR: 0.60 [95% CrI: 0.48 to 0.75]). However, this was not seen with OCT (OR: 0.86 [95% CrI: 0.60 to 1.19]) (Fig. 3; Table 3). Based on the SUCRA analysis, IVUS had the highest probability of reducing target-vessel-related revascularization (98.1%), followed by OCT (42.6%) and angiography (9.3%) (Fig. 4).

### CABG

CABG was defined as any repeat revascularization by coronary artery bypass grafting. Upon pooling nine RCTs

![img-1.jpeg](img-1.jpeg)

Fig. 2 Quality assessment of risk of bias in the included trials. The upper panel presents a schematic representation of risks (low = green, unclear = yellow, and high = red) for specific types of biases of each study in the review. The lower panel presents risks (low = green, unclear = yellow, and high = red) for the subtypes of biases of the combination of studies included in this review

![img-2.jpeg](img-2.jpeg)

**Fig. 3** Forest plot of the clinical outcomes, OR: odds ratio, CI: confidence interval

[18, 19, 21, 27, 35, 40, 43, 47, 51, 55, 56], neither IVUS (OR: 1.12 [95% CrI: 0.59 to 1.99]) nor OCT (OR: 0.60 [95% CrI: 0.16 to 2.12]) were associated with statistically significant reductions in CABG operations compared to conventional angiography (Fig. 3; Table 3). Based on the SUCRA analysis, OCT had the highest probability of reducing CABG operations (80.3%), followed by angiography (43.3%) and IVUS (26.5%) (Fig. 4).

### *Stent thrombosis*

Pooling 24 RCTs [16, 17, 19, 21–24, 26–33, 35–39, 41, 43, 46, 47, 50, 51, 53, 55], compared to conventional angiography, IVUS significantly reduced the risk of stent thrombosis (OR: 0.50 [95% CrI: 0.28 to 0.92]), as did OCT (OR: 0.48 [95% CrI: 0.22 to 0.98]) (Fig. 3and Table 3). Based on the SUCRA analysis, OCT had the highest probability of reducing stent thrombosis (75.8%), followed by IVUS (72.3%) and Angiography (1.9%) (Fig. 4).

### *Restenosis*

Restenosis was defined as the percent diameter of stenosis at follow-up at ≥50%, confirmed by angiography. Upon pooling 12 RCTs [18, 19, 26, 32, 41–44, 47, 52–54, 56], compared to conventional angiography, IVUS significantly reduced the risk of restenosis (OR: 0.65 [95% CrI: 0.46 to 0.88]). Although rates of restenosis were numerically lower with OCT compared to conventional angiography, this did not reach statistical significance (OR: 0.55 [95% CrI: 0.15 to 1.99]) (Fig. 3and Table 3). Based on the SUCRA analysis, OCT had the highest probability of reducing restenosis (71.3%), followed by IVUS (69.6%) and Angiography (9.0%) (Fig. 4).

### **Assessment of inconsistency and heterogeneity**

Assessments of pairwise heterogeneity and inconsistency (assessed by comparing the direct and indirect estimates via a node-splitting approach) are shown in **(Table S3)**. There was no inconsistency or heterogeneity across any of the assessed outcomes.

### **Sensitivity analysis and assessment of publication bias**

Figures S1-S22 show the sensitivity frequentist analysis (under both random effects and a fixed effect). Figures S23-S33 show funnel plots used to assess publication bias.

### **Discussion**

The available body of evidence supports the superiority of IVUS and, to a lesser degree, OCT over angiography as imaging modalities to assist percutaneous recanalization among patients with coronary artery disease. A decrease in MACE, target-vessel-related revascularization, stent thrombosis, and restenosis risks were noted with IVUS but not OCT-guided PCI. Moreover, IVUS and OCT

Table 3: League table showing all possible comparisons in the network meta-analysis

IVUS: Intravascular ultrasound, OCT: Optical coherence tomography

significantly reduced the risks of cardiac death and instent thrombosis compared to angiography. In contrast, non-conventional modalities did not alter the susceptibility to all-cause mortality, target vessel/lesion failure, myocardial infarction, revascularization, and CABG compared to conventional angiography. The evaluated data was consistent and homogenous. Our findings agree with previous meta-analyses that indicated a worse safety profile of stent implantation when performed with angiography than with IVUS or OCT [57--60].

IVUS and OCT appear to provide a safer procedure of percutaneous coronary angioplasty, likely due to

![img-3.jpeg](img-3.jpeg)

**Fig. 4** SUCRA analysis

The overall greater radiological performance of these modalities compared to angiography, thereby allowing more successful, more refined, and less complicated primary intervention. In particular, the examined evidence showed that IVUS is superior to angiography in terms of lower risk of MACE. IVUS permits visualizing both the coronary lumen and vessel wall at the cross-sectional level, allows characterization of the type (nature, composition, and morphology) of the plaque, and clarifies the stent failure mechanism [61, 62]. At the same time, angiography displays only the opacified luminal silhouette with minimum structural details. This limits the accurate peri-interventional assessment of the target lesion/vessel, notably exposing it to less effective and more risky stent implantation, ultimately exposing it to higher MACE incidence [61, 62].

We found that the risk of target-related revascularization was lower in patients undergoing IVUS-guided PCI than in those managed with angiography-guided PCI. Target-related revascularization is one of the standardized clinically-driven endpoints used to assess the interventional modalities' effectiveness in coronary intervention trials [63]. It is a repeat percutaneous intervention or bypass surgery of the target lesion/vessel due to clinically significant narrowing or other complications [63]. Among the predictors of target-related revascularization are procedure- and lesion-related factors such as ostial location and use of rotablator [64]. Mainly, IVUS was found to be the advantageous modality during PCI of ostial coronary atherosclerotic plaques (i.e., aortic ostia and left anterior descending artery/left circumflex artery ostia) as such lesions prevent optimal coronary guide catheter intubation, which is required for contrast intake in both OCT and angiography [65]. Moreover, the ostium of the left main stem cannot be optimally visualized when this artery is subject to diffuse atherosclerosis. This challenge can be overcome by withdrawing the guide catheter from the left main stem, which allows for visualization of the artery's full length. IVUS is the best modality to achieve such a maneuver [65]. Furthermore, IVUS enhanced the safety of rotational atherectomy (rotablation) [66]. Hence, due to improvements in the deliverability and crossability of IVUS catheters, they can now be used to obtain images of the calcified lesions before and after rotational atherectomy, which would help in the selection of the appropriate guidewire and burr size, ultimately, resulting in better outcomes [66]. The unique advantages of IVUS during ostial coronary lesions and rotablation would favor lesser susceptibility to target-related revascularization.

We also observed a lower tendency to develop restenosis among patients undergoing IVUS-guided PCI. Knowing that lesion-related risk factors of coronary restenosis include lesions at the ostial location, small target vessel, lesions with complex morphology, longer stented lesions, and length of the stenosis > 20 mm [67], the observed finding can be explained by the following reasons: (i) As previously explained, IVUS can help

overcome the challenges of ostial lesions, which decrease the development of restenosis. (ii) The employment of IVUS-guided PCI improved postoperative outcomes of small-vessel coronary lesions; notably prolonging eventfree survival compared to angiography. That was remarkably related to coronary angiography's higher tendency to mistakenly underestimate the real reference vessel diameters in reference to IVUS [68]. (iii) Treatment with IVUS-guided PCI was lined with a lower long-term risk of cardiac death and adverse cardiac events among patients with complex coronary artery lesions compared with angiography-guided PCI [69]. The IVUS-associated optimization of stent deployment may explain that. Thus, the IVUS-guided PCI can result in adequate stent expansion and apposition and full lesion coverage, which is due to its potential to induce larger stent size, longer stent length, higher proportion of post-dilatation, and higher inflation pressures compared to angiographyguided PCI [69]. (iv) IVUS can ameliorate the angiographic and clinical results of stent implantation for long coronary artery stenosis, as shown in the TULIP study. This study's authors argued that IVUS motivated the operators to stent atherosclerotic segments more extensively than angiography in patients with similar stenosis lengths because of the information they received from the former modality [42]. Thus, angiography can fail to accurately identify the extent of atherosclerotic disease (underestimate it), resulting in less optimal lesion coverage. Meanwhile, IVUS defines the stenosis borders not as where significant disease begins or ends but as where compensatory vessel enlargement fails to preserve luminal dimensions [70], which would favor better stenting of large lesions and, thereby, lower restenosis likelihood.

Both IVUS and OCT reduced cardiac death in respect to angiography. Besides the interventional and imaging advantages of IVUS discussed above, OCT can produce high-resolution imaging (up to 10 µm), allowing realtime observation of the coronary structures and lesions. Thus, it can accurately measure coronary luminal parameters, identify different tissue characteristics of arterial intima and atherosclerotic plaques, and detect preoperatively vulnerable plaques and inflammation presence [71]. These would refine the immediate effect of stent implantation, which would optimize the results of the stent implantation in terms of both effectiveness and safety [71], perhaps contributing to more reduced cardiac death than conventional angiography.

Another finding is that IVUS and OCT implementation was linked with lesser risks of stent thrombosis. The latter is another event favored by lesions at small target vessels, complex lesions, those with higher lengths, or those at ostial sites or bifurcations [72]. Since IVUS can reduce the operative difficulties imposed by these lesions and allow their safer management compared to angiography (as previously discussed), it would reduce the likelihood of stent thrombosis. Likewise, it was demonstrated that PCI under OCT guidance improves clinical outcomes of patients with complex lesions and/or bifurcation lesions [21, 73, 74], which may translate to fewer stent thrombosis events.

## Study limitations

We acknowledge several limitations to the present study. First, most studies' sample size was small, representing considerable methodological weakness. Second, patients' selection and generalizability issues were reported in some of the included trials due to the exclusion of essential populations of patients that could benefit from PCI in real-world (e.g. those with cardiogenic shock in Wang et al. 2015 study and those with myocardial infarction in Tan et al. 2015 study). Third, the definition of our primary outcome (MACE) was heterogeneous across the RCTs and was not reported in some of them. Additionally, the limited data available for each outcome within the MACE term made them inapplicable for analysis. Finally, a large proportion of the studies used a singlecenter trial design, which is known to provide suboptimal data quality.

## Implications for clinical practice

In the American Heart Association 2021 guidelines, the use of IVUS and OCT during PCI has received a Class IIa recommendation, which refers to the weight of evidence/opinion in favor of usefulness/efficacy [75]. The guidelines suggest that IVUS provides useful guidance during stent implantation, particularly in cases of left main or complex lesions, allowing the prevention of ischemic events. At the same time, OCT is recommended as an alternative to IVUS except in the ostial left main disease. Our findings support these guidelines by demonstrating the clear superiority of IVUS and the relative superiority of OCT to conventional angiography. Notably, IVUS and OCT represent promising modalities for enhancing PCI efficacy and safety. Hence, the diagnostic and therapeutic advantages of IVUS/OCT should drive a shift in cardiology interventionists' enthusiasm toward these modalities, leaving conventional angiography as the alternative instead of the standard.

Nonetheless, the non-conventional imaging techniques have many obstacles that would prevent the angiographyguided PCI era from continuing for longer than expected. One major obstacle is the accessibility issues, which would delay or even preclude the extensive generalizability of IVUS/OCT devices due to high costs and reduced availability in the market. Moreover, like any innovative procedure, interventionists' lack of familiarity with IVUS/OCT may favor the more conventional option. However, this can be overcome through the active

training of interventionists and experience sharing in scientific events and networks. Operative disadvantages also represent a key challenge that may antagonize the benefit of IVUS/OCT-guided coronary angioplasty. For instance, the currently commercialized IVUS imaging catheter has poor cross-ability for more severe stenosis or twisted angular lesions, low resolution, and suboptimal ability to assess small vascular structures [71]. Similarly, OCT increases the difficulty of PCI and limits its application in severe coronary ischemic diseases due to the necessity of blocking or removing the blood in the corresponding detection vessel [71]. These issues may be resolved with technology improvement and the acquisition of progressive expertise.

## Conclusion

In patients undergoing PCI, the current evidence shows that IVUS reduces the risks of MACE, target-vesselrelated revascularization, and restenosis compared to standard angiography. However, this is not the case for OCT. Also, IVUS and OCT appear to lower the susceptibility to cardiac death and in-stent thrombosis in reference to angiography. This indicates that IVUS, followed by OCT, may be the privileged radiological technique for stent implantation whenever available. However, there is still a need for high-quality data to confirm the benefit and cost-effectiveness of these modalities in the context of coronary angioplasty.

## Supplementary Information

The online version contains supplementary material available at https://doi. org/10.1186/s12872-024-04105-5.

## Supplementary Material 1

## Acknowledgements

None.

## Author contributions

M.A. conceived the idea. A.M.A. and M.A. designed the research workflow. A.M.A. and M.A. searched the databases. U.K., M.T., H.E., M.M.E., M.E., and A.K.E. screened the retrieved records, extracted relevant data, assessed the quality of evidence, and B.A. resolved the conflicts. A.S. performed the analysis. A.M.A., Y.K., and M.A. wrote the final manuscript. B.A. supervised the project. All authors have read and agreed to the final version of the manuscript.

## Funding

We received no funding for this study.

## Data availability

No datasets were generated or analysed during the current study.

## Declarations

Ethics approval and consent to participate
Not applicable.

## Consent for publication

Not applicable.

## Competing interests

The authors declare no competing interests.

## Author details

${ }^{1}$ Faculty of Medicine, Mansoura University, Mansoura, Egypt
${ }^{2}$ Faculty of Medicine, Algiers University, Algiers, Algeria
${ }^{3}$ Faculty of Medicine, Tanta University, Tanta, Egypt
${ }^{4}$ Faculty of Medicine, Ain Shams University, Cairo, Egypt
${ }^{5}$ Division of Cardiology, University of Maryland School of Medicine, Baltimore, Maryland, USA
${ }^{6}$ Faculty of Medicine, Yarmouk University, Irbid, Jordan
${ }^{7}$ Faculty of Medicine, Al-Azhar University, Cairo, Egypt
${ }^{8}$ Faculty of Medicine, King Abdulaziz University, Jeddah, Saudi Arabia
${ }^{9}$ Department of Medicine, West Virginia University, Morgantown, WV, USA
${ }^{10}$ Department of Cardiology, West Virginia University, Morgantown, WV, USA
${ }^{11}$ Houston Methodist DeBakey Heart \& Vascular Center, Houston, Texas, USA

Received: 4 April 2024 / Accepted: 7 August 2024
Published online: 11 September 2024

## Publisher's Note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.