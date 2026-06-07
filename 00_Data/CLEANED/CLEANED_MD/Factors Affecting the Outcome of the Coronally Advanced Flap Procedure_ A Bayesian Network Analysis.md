# Factors Affecting the Outcome of the Coronally Advanced Flap Procedure: A Bayesian Network Analysis 

Michele Nieri,* Roberto Rotundo,* Debora Franceschi,* Francesco Cairo,* Pierpaolo Cortellini, ${ }^{\dagger}$ and Giovanpaolo Pini Prato*


#### Abstract

Background: The aim of this study was to explore possible causal relationships among several variables in the coronally advanced flap for root coverage procedure using structural learning of Bayesian networks.

Methods: Sixty consecutive patients with maxillary buccal recessions ( $\geq 2 \mathrm{~mm}$ ) were enrolled. All defects were treated with the coronally advanced flap procedure. Age, gender, smoking habits, recession depth, width of keratinized tissue, probing depth, distance between the incisal margin and the cemento-enamel junction, root sensitivity, and distance between the gingival margin and the cemento-enamel junction were recorded and calculated for all patients at baseline, immediately after surgery, and at 6 months after surgery. A structural learning algorithm of Bayesian networks was used.

Results: The distance between the gingival margin and the cemento-enamel junction immediately after surgery was affected by the baseline recession depth; deeper recessions were associated with a more apical location of the gingival margin after surgery. Moreover, complete root coverage also seemed to be affected by the location of the gingival margin after surgery; a more coronal location of the gingival margin after surgery was associated with a greater probability of complete root coverage.

Conclusions: The use of structural learning of Bayesian networks seemed to facilitate the understanding of the possible relationships among the variables considered. The main result revealed that complete root coverage seemed to be influenced by the post-surgical position of the gingival margin and indirectly by the baseline recession depth. J Periodontol 2009; 80:405-410.


## KEY WORDS

Bayesian analysis; gingival recession; prognosis; surgery/therapy.

[^0]The surgical treatment of gingival recession is indicated for reducing root sensitivity and for improving esthetics. ${ }^{1,2}$ Complete success is achieved when the following criteria are satisfied: gingival margin located at the cementoenamel junction (CEJ), sulcus depth $\leq 2 \mathrm{~mm}$, presence of clinically attached gingiva, and no bleeding on probing at the treated sites. ${ }^{3}$ The coronally advanced flap procedure is frequently able to achieve complete root coverage (CRC) and clinical attachment gain. ${ }^{4,5}$ Nevertheless, the roles of the etiologic factors of gingival recession and the prognostic factors affecting treatment outcome are unclear. Few data are available in the periodontal literature concerning factors affecting the outcomes of root-coverage procedures, ${ }^{6}$ and there are no data about the possible relationships among these factors.

In a previous study, Pini Prato et al. ${ }^{7}$ found a relationship between the postsurgical position of the gingival margin $\left(\mathrm{GM}_{1}\right)$ and CRC. In the same study, the investigators reported the individual patient data for all 60 patients enrolled in the study.

The availability of a large amount of data regarding several factors related to the coronally advanced flap procedure may favor the application of explorative analyses aimed at investigating the relationships among these factors.


[^0]:    * Department of Periodontology, University of Florence, Florence, Italy.
    $\dagger$ Tuscan Academy of Dental Research and European Research Group on Periodontology, Berne, Switzerland.

The structural learning of Bayesian networks (BNs) is a new explorative statistical tool for analyzing possible causal relationships among variables. ${ }^{8-10}$ A BN is composed of a directed acyclic graph in which stochastic variables are represented by vertices or nodes of the graph, whereas oriented lines (arrows) represent the relationships among the variables. The arrows relate the variables in such a way that cycles are not formed; by following the arrows, it is impossible to return to a vertex or starting point. The variables from which the arrows start influence those to which they arrive, possibly through a causal relationship. ${ }^{9}$ Dedicated algorithms called structural learning algorithms automatically generate graphs after data are entered. The likely advantages of this methodology have yet to be recognized in medical studies. An example of BN analysis was reported in an oral oncology genomic study, ${ }^{11}$ and some aspects of a directed acyclic graph have been elucidated in dental research. ${ }^{12}$ To the best of our knowledge, there are no publications concerning applications of structural learning algorithms of BNs in periodontology.

The aim of this study was to investigate the possible causal relationships among the variables, using the BNs analysis, in patients treated with a root-coverage procedure.

## MATERIALS AND METHODS

The study population, the inclusion criteria, the surgical technique and post-surgical care, and the data collection were described in a previous article. ${ }^{7}$

In brief, the study population consisted of 60 consecutively enrolled patients ( 15 males and 45 females), aged 22 to 57 years (mean: $29.70 \pm 6.04$ ). They were all white, of middle income, and each contributed one single recession. Eleven subjects were smokers ( $>10$ cigarettes per day). All patients were selected from individuals referred from private practices and treated by a single clinician (GPP). All patients were informed about the study design and signed an appropriate consent form. The study was conducted in accordance with the Helsinki Declaration of 1975, as revised in 2000.

## Inclusion Criteria

The following entry criteria were used to select the population and the sites: non-compromised systemic health and no contraindications for periodontal surgery; the presence of maxillary buccal recessions ( $\geq 2 \mathrm{~mm}$ ) classified as Miller Class I and II; the presence of an identifiable CEJ; tooth vitality and the absence of grooves, irregularities, caries, or restorations in the area to be treated; no periodontal surgical treatment of the involved sites during the previous 24 months; full-mouth plaque score $<20 \%$ and full-mouth bleed-
ing score $<20 \%$; and the absence of plaque and bleeding on probing at the selected sites.

## Surgical and Post-Surgical Procedures

The coronally advanced flap procedure for single gingival recessions was performed in all enrolled patients. The surgical technique and post-surgical care procedures were reported in a previous study by Pini Prato et al. ${ }^{7}$

## Data Collection

Age, gender, smoking habits, and type of tooth were recorded for all patients. The clinical measurements were taken using a periodontal probe and magnification lens ( $\times 4$ ). The measurements were rounded to the nearest 0.5 mm .

At baseline ( $\mathrm{T}_{0}$ ), before surgery, the following variables were measured at the mid-buccal point of the involved tooth: recession depth $\left(\mathrm{Rec}_{\mathrm{T} 0}\right)$, width of keratinized tissue $\left(\mathrm{KT}_{\mathrm{T} 0}\right)$, probing depth $\left(\mathrm{PD}_{\mathrm{T} 0}\right)$, and the distance between the incisal margin and the CEJ (IMCEJ). Root sensitivity (Sens $_{\mathrm{T} 0}$ ) was also recorded.

Immediately after surgery ( $\mathrm{T}_{1}$ ), the distance between the incisal and gingival margins $\left(\mathrm{IMGM}_{\mathrm{T} 1}\right)$ was measured, and the distance between the gingival margin and the CEJ $\left(\mathrm{GM}_{1}=\mathrm{IMCEJ}-\mathrm{IMGM}_{\mathrm{T} 1}\right)$ was calculated (Fig. 1).

Six months after surgery ( $\mathrm{T}_{2}$ ), recession depth $\left(\operatorname{Rec}_{\mathrm{T} 2}\right)$, width of the keratinized tissue $\left(\mathrm{KT}_{\mathrm{T} 2}\right)$, and probing depth $\left(\mathrm{PD}_{\mathrm{T} 2}\right)$ were measured. The following variables were calculated: recession reduction $\left(\operatorname{Rec}_{\mathrm{T} 0}-\operatorname{Rec}_{\mathrm{T} 2}\right), \mathrm{CRC}, \mathrm{PD}$ difference $\left(\mathrm{PD}_{\text {diff }}=\mathrm{PD}_{\mathrm{T} 0}-\right.$

![img-0.jpeg](img-0.jpeg)

Figure 1.
The location of the gingival margin after suturing $\left(\mathrm{GM}_{1}\right)$ with respect to the CEJ is calculated as follows: $\mathrm{GM}_{1}=a-b=I M C E J-I M G M_{T 1}$. $I M=$ incisal margin; $G M_{T 1}=$ gingival margin after suturing; $a=$ distance between $I M$ and $C E J ; b=$ distance between $I M$ and $G M_{T 1}$; and $G M_{1}=$ the entity of the coronal displacement of the flap immediately after surgery calculated as $a-b$.

$\left.\mathrm{PD}_{\mathrm{T} 2}\right)$, and KT difference $\left(\mathrm{KT}_{\text {diff }}=\mathrm{KT}_{\mathrm{T} 0}-\mathrm{KT}_{\mathrm{T} 2}\right)$. Root sensitivity (Sens $_{\mathrm{T} 2}$ ) was also evaluated.

## Statistical Analysis

An explorative analysis was performed using the structural learning of BNs with the PC algorithm ${ }^{8}$ as implemented in specific software, ${ }^{\dagger}$ at the threshold of 0.05 . The variables used for this analysis were located in the following levels: first level: gender and age; second level: smoking, $\mathrm{Rec}_{\mathrm{T} 0}, \mathrm{Sens}_{\mathrm{T} 0}, \mathrm{PD}_{\mathrm{T} 0}$, and $\mathrm{KT}_{\mathrm{T} 0}$; third level: $\mathrm{GM}_{1}$; and fourth level: CRC, Sens $_{\mathrm{T} 2}, \mathrm{KT}_{\text {diff }}$, and $\mathrm{PD}_{\text {diff }}$.

These levels imply a hierarchic order, so that subsequent levels are not able to influence the previous ones (e.g., $\mathrm{GM}_{1}$ is unable to influence age or gender).

All of these variables were considered continuous. ${ }^{8,9} \mathrm{An} R^{2}$ analysis was performed for each dependent variable in the graph.

A cross-validation was performed by dividing the data randomly into five parts and using four parts together to learn the network. The links resulting from the five networks were compared to the links of the network learned from all subjects.

A goodness-of-fit test was performed in the five cross-validation samples using four parts together to learn the network and the fifth for prediction of $\mathrm{GM}_{1}$, CRC, and Sens $_{\mathrm{T} 2}$ using root mean square error (RMSE).

## RESULTS

Descriptive statistical analysis and linear and logistic regression were reported by Pini Prato et al. ${ }^{7}$
![img-1.jpeg](img-1.jpeg)

Figure 2.
BN: PC algorithm 0.05. Numbers represent $R^{2}$ values. $+=$ the variable at the base of the arrow positively influences the variable at the arrowhead. $--=$ the variable at the base of the arrow negatively influences the variable at the arrowhead.

BNs resulting from the PC algorithm are shown in Figure 2. Patient gender seemed to affect the baseline recession depth. Male patients exhibited deeper average recessions than females in this study. $\mathrm{GM}_{1}$ was affected by the baseline recession depth; deeper recessions were associated with lower $\mathrm{GM}_{1}$ (more apical gingival margin). CRC seemed to be influenced by $\mathrm{GM}_{1}$; greater $\mathrm{GM}_{1}$ levels (more coronal gingival margin) were related to a greater probability for obtaining CRC. In addition, CRC was correlated with reduced Sens $_{T 2}$. Older patients showed less Sens $_{T 0}$ and deeper probing levels $\left(\mathrm{PD}_{\mathrm{T} 0}\right)$. Moreover, the greater the $\mathrm{PD}_{\mathrm{T} 0}$, the greater the reduction in probing depth $\left(\mathrm{PD}_{\text {diff }}\right)$. The $\mathrm{KT}_{\mathrm{T} 0}$ seemed to be affected by the $\mathrm{Rec}_{\mathrm{T} 0}$; the wider the baseline recession, the narrower the $\mathrm{KT}_{\mathrm{T} 0}$. The $\mathrm{KT}_{\mathrm{T} 0}$ was affected by root sensitivity; the higher the Sens $_{\mathrm{T} 0}$, the higher the $\mathrm{KT}_{\mathrm{T} 0}$. A greater reduction in keratinized tissue width ( $\mathrm{KT}_{\text {diff }}$ ) was associated with greater values of $\mathrm{KT}_{\mathrm{T} 0}$ and $\mathrm{PD}_{\mathrm{T} 0}$. Smoking was not associated with any of the considered variables.

The five networks resulting from the cross-validation analysis are shown in Figures 3 through 7. The RMSE of prediction of the five-fold cross validation for $\mathrm{GM}_{1}$, CRC, and Sens $_{\mathrm{T} 2}$ are reported in Table 1.

## DISCUSSION

Some patient-, site-, and technique-related factors may influence the degree of root coverage. ${ }^{6}$ The aim of this study was to explore the possible causal relationships among patient-, tooth-, and site-related variables, using the BNs, in the coronally advanced flap procedure for root coverage.

In this study, the observed influence of gender on the baseline recession (deeper recessions in male patients) may be explained in several ways. One reason could be a lack of interest; male patients only seem concerned about severe lesions, and ignoring minor lesions leads to delays in seeking advice and treatment. Other explanations may include more vigorous toothbrushing among females.

The relationship $\mathrm{Rec}_{\mathrm{T} 0}-\mathrm{GM}_{1}$ shown in the graph (Fig. 2) highlights the difficulty in moving the gingival margin of the flap coronally to the CEJ $\left(\mathrm{GM}_{1}\right)$ in the presence of greater baseline recession. The need for passive adaptation of the flap, virtually without any tension, was confirmed in an earlier study. ${ }^{13}$

The BN suggests a causal relationship between $\mathrm{GM}_{1}$ and CRC. This relationship was noted in an article $^{7}$ based on the same data, in which the logistic regression resulted in a positive association between these two variables. However, further randomized clinical trials are needed to confirm this cause-effect hypothesis.

[^0]
[^0]:    ‡ TETRAD, version 3.1, Peter Spirtes, Richard Scheines, Clark Glymour, Christopher Meek, Thomas Richardson, Herbert Hoijtink, and Anne Boomsma, Department of Philosophy, Carnegie Mellon University, Pittsburgh, PA.

![img-2.jpeg](img-2.jpeg)

Figure 3.
Cross-validation analysis 1: PC Algorithm 0.05. $+=$ the variable at the base of the arrow positively influences the variable at the arrowhead; - = the variable at the base of the arrow negatively influences the variable at the arrowhead.
![img-3.jpeg](img-3.jpeg)

Figure 4.
Cross-validation analysis 2: PC Algorithm 0.05. $+=$ the variable at the base of the arrow positively influences the variable at the arrowhead; - = the variable at the base of the arrow negatively influences the variable at the arrowhead.
![img-4.jpeg](img-4.jpeg)

Figure 5.
Cross-validation analysis 3: PC Algorithm 0.05. $+=$ the variable at the base of the arrow positively influences the variable at the arrowhead; - = the variable at the base of the arrow negatively influences the variable at the arrowhead.
![img-5.jpeg](img-5.jpeg)

Figure 6.
Cross-validation analysis 4: PC Algorithm 0.05. $+=$ the variable at the base of the arrow positively influences the variable at the arrowhead; - = the variable at the base of the arrow negatively influences the variable at the arrowhead.

![img-6.jpeg](img-6.jpeg)

Figure 7.
Cross-validation analysis 5: PC Algorithm 0.05. $+=$ the variable at the base of the arrow positively influences the variable at the arrowhead, $-=$ the variable at the base of the arrow negatively influences the variable at the arrowhead.

Table I.
RMSE of Prediction of $\mathrm{GM}_{1}$, CRC, and Sens $_{\text {T2 }}$ in the Cross-Validation Analyses


Based on these initial data, the causal sequence $\operatorname{Rec}_{\mathrm{T} 0} \rightarrow \mathrm{GM}_{1} \rightarrow$ CRC suggests that baseline recession is able to influence CRC in an indirect way by means of $\mathrm{GM}_{1}$. This hypothesis finds support in two systematic reviews ${ }^{5,14}$ in which the investigators showed that preoperative recession depth correlated with CRC: the greater the initial recession, the lower the frequency of CRC.

The ability of CRC to decrease dental hypersensitivity is confirmed by the same graph (Fig. 2). The chain $\operatorname{Rec}_{\mathrm{T} 0} \rightarrow \mathrm{GM}_{1} \rightarrow \mathrm{CRC} \rightarrow$ Sens $_{\mathrm{T} 2}$ is present in each cross-validation graph, and it seems robust in this sample. In fact, the goodness-of-fit test generally showed a low level of RMSE. This indicated that the
model is well suited for predicting the variables $\mathrm{GM}_{1}$, CRC, and Sens $_{\mathrm{T} 2}$.

Age seems to affect baseline sensitivity because older patients show less sensitivity associated with recessions; this may be due to sclerosis of the dentinal tubules. ${ }^{15}$

The BN also indicates greater probing values $\left(\mathrm{PD}_{\mathrm{T} 0}\right)$ associated with advancing age, but this relationship was unduly influenced by the high leverage point of one patient in the study population. This relationship is not shown in three of five graphs of the cross-validation analysis (Figs. 3 through 7).

The relationship between $\mathrm{Rec}_{\mathrm{T} 0}$ and $\mathrm{KT}_{\mathrm{T} 0}$ is rather obvious, although four cross-validation analyses do not report this relationship. The association revealed between Sens $_{\mathrm{T} 0}$ and $\mathrm{KT}_{\mathrm{T} 0}$ is more difficult to interpret. The BN does not show a direct relationship between hypersensitivity and recession depth; this lack of association is consistent with clinical observations that show that shallow recessions are sometimes associated with marked hypersensitivity, whereas deep recessions may not be associated with any hypersensitivity. In addition, no relationship between $\mathrm{KT}_{\mathrm{T} 0}$ and CRC was found in the BN analysis. However, a surprising relationship was found between $\mathrm{PD}_{\mathrm{T} 0}$ and $\mathrm{KT}_{\text {diff }}$ : a greater reduction in keratinized tissue width was associated with higher $\mathrm{PD}_{\mathrm{T} 0}$ values. However, the cross-validation analysis did not fully confirm this relationship; further investigation is required.

The relationships between $\mathrm{KT}_{\mathrm{T} 0}$ and $\mathrm{KT}_{\text {diff }}$ and between $\mathrm{PD}_{\mathrm{T} 0}$ and $\mathrm{PD}_{\text {diff }}$ were expected based on the phenomenon of the regression toward the mean. ${ }^{16,17}$

Smoking did not seem to be associated with any other variable, perhaps because of the low percentage of smokers in the sample population. The literature on this subject is inconsistent.

## CONCLUSIONS

The use of structural learning of BNs seems to facilitate the understanding of the possible relationships among the considered variables. The main result revealed that CRC seemed to be influenced by the post-surgical position of the gingival margin and, indirectly, by the baseline recession depth.

## ACKNOWLEDGMENT

The authors report no conflicts of interest related to this study.
